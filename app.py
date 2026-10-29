import tempfile
import os
import json
import re
import uuid
from datetime import datetime

import bleach
from PIL import Image, UnidentifiedImageError
from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_wtf.csrf import CSRFProtect
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

from data.departments import DEPARTMENTS, LGEA_BOARD, HEALTH_BOARD
from data.administrations import ADMINISTRATIONS
from data.profile import CHAIRMAN_INFO
from data.projects import PROJECTS
from data.wards import WARDS
from forms import ContactForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")
if not app.config["SECRET_KEY"]:
    raise RuntimeError(
        "FLASK_SECRET_KEY is required. Set it in your environment before starting the app."
    )

# Limit each incoming request, including uploaded photos, to 5 MiB.
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

csrf = CSRFProtect(app)
@app.errorhandler(413)
def handle_request_too_large(error):
    return (
        "Upload too large. Please return to the previous page "
        "and choose a file smaller than 5 MiB.",
        413,
    )

# --- Flask-Login Configuration ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message_category = "warning"


class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data["id"]
        self.username = user_data["username"]
        self.email = user_data["email"]
        self.role = user_data["role"]
        self.full_name = user_data["full_name"]


@login_manager.user_loader
def load_user(user_id):
    users_file = os.path.join(app.root_path, "data", "users.json")
    if os.path.exists(users_file):
        try:
            with open(users_file, "r", encoding="utf-8") as f:
                users = json.load(f)
                for u in users:
                    if str(u["id"]) == str(user_id):
                        return User(u)
        except json.JSONDecodeError:
            pass
    return None


# --- Helper Functions for Data Persistence ---
def get_contact_messages():
    messages_file = os.path.join(app.root_path, "data", "messages.json")
    if os.path.exists(messages_file):
        try:
            with open(messages_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def load_news():
    news_file = os.path.join(app.root_path, "data", "news.json")
    if os.path.exists(news_file):
        try:
            with open(news_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_news(news_list):
    news_file = os.path.join(app.root_path, "data", "news.json")
    news_directory = os.path.dirname(news_file)
    os.makedirs(news_directory, exist_ok=True)

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=news_directory,
            prefix=".news-",
            suffix=".tmp",
            delete=False,
        ) as temp_file:
            temp_path = temp_file.name
            json.dump(news_list, temp_file, indent=4, ensure_ascii=False)
            temp_file.flush()
            os.fsync(temp_file.fileno())

        # Replace the file only after the complete JSON has been written.
        os.replace(temp_path, news_file)
        temp_path = None

    finally:
        # Clean up any temporary file left by a failed write.
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

def simple_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def load_directory_records(filename):
    """Load a JSON directory without changing its source records."""
    path = os.path.join(app.root_path, "data", filename)
    try:
        with open(path, "r", encoding="utf-8") as file:
            records = json.load(file)
    except (OSError, json.JSONDecodeError):
        app.logger.exception("Could not load directory data: %s", filename)
        return []

    return records if isinstance(records, list) else []


def filter_directory_records(records, query, ward_key, selected_ward, selected_status):
    """Filter directory records while retaining their original field values."""
    filtered = []

    for record in records:
        record_ward = str(record.get(ward_key) or "").strip()
        record_status = str(record.get("verification_status") or "").strip()

        if selected_ward and record_ward != selected_ward:
            continue

        if selected_status and record_status != selected_status:
            continue

        searchable_text = " ".join(
            str(value)
            for value in record.values()
            if value is not None
        ).casefold()

        if query and query.casefold() not in searchable_text:
            continue

        filtered.append(record)

    return filtered


def directory_filter_options(records, ward_key):
    """Build filter choices from values actually present in the data."""
    wards = sorted(
        {
            str(record.get(ward_key)).strip()
            for record in records
            if record.get(ward_key)
        },
        key=str.casefold,
    )
    statuses = sorted(
        {
            str(record.get("verification_status")).strip()
            for record in records
            if record.get("verification_status")
        },
        key=str.casefold,
    )
    return wards, statuses


@app.route("/schools")
def schools_directory():
    records = load_directory_records("schools.json")
    query = request.args.get("q", "").strip()
    selected_ward = request.args.get("ward", "").strip()
    selected_status = request.args.get("status", "").strip()
    wards, statuses = directory_filter_options(records, "ward")

    filtered = filter_directory_records(
        records, query, "ward", selected_ward, selected_status
    )

    return render_template(
        "schools.html",
        info=CHAIRMAN_INFO,
        schools=filtered,
        total_count=len(records),
        query=query,
        wards=wards,
        statuses=statuses,
        selected_ward=selected_ward,
        selected_status=selected_status,
    )


@app.route("/health-facilities")
def health_facilities_directory():
    records = load_directory_records("health_facilities.json")
    query = request.args.get("q", "").strip()
    selected_ward = request.args.get("ward", "").strip()
    selected_status = request.args.get("status", "").strip()
    wards, statuses = directory_filter_options(records, "ward_source")

    filtered = filter_directory_records(
        records, query, "ward_source", selected_ward, selected_status
    )

    return render_template(
        "health_facilities.html",
        info=CHAIRMAN_INFO,
        facilities=filtered,
        total_count=len(records),
        query=query,
        wards=wards,
        statuses=statuses,
        selected_ward=selected_ward,
        selected_status=selected_status,
    )


# --- Core Public Routes ---
@app.route("/")
def home():
    news_items = [
        item for item in load_news()
        if item.get("is_published", True)
    ]
    return render_template(
        "index.html",
        info=CHAIRMAN_INFO,
        projects=PROJECTS[:3],
        news=news_items[:3],
    )


@app.route("/about")
def about():
    return render_template("about.html", info=CHAIRMAN_INFO)


@app.route("/departments")
def departments():
    return render_template(
        "departments.html",
        departments=DEPARTMENTS,
        lgea=LGEA_BOARD,
        health_board=HEALTH_BOARD,
    )


@app.route("/projects")
def projects():
    return render_template("projects.html", info=CHAIRMAN_INFO, projects=PROJECTS)


@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        flash("Project not found.", "warning")
        return redirect(url_for("projects"))
    return render_template("project_detail.html", info=CHAIRMAN_INFO, project=project)


@app.route("/wards")
def wards():
    return render_template("wards.html", info=CHAIRMAN_INFO, wards=WARDS)


@app.route("/administrations")
def administrations():
    return render_template(
        "administrations.html",
        info=CHAIRMAN_INFO,
        administrations=ADMINISTRATIONS,
    )


# --- Dynamic News & Blog Routes ---
# --- Dynamic News & Blog Routes ---
@app.route("/news")
def news_list():
    category = request.args.get("category", "").strip()
    query = request.args.get("q", "").strip().lower()

    all_news = load_news()
    filtered_news = [n for n in all_news if n.get("is_published", True)]

    if category:
        filtered_news = [
            n for n in filtered_news
            if n.get("category", "").lower() == category.lower()
        ]

    if query:
        filtered_news = [
            n for n in filtered_news
            if query in n.get("title", "").lower()
            or query in n.get("content", "").lower()
        ]

    return render_template(
        "news.html",
        info=CHAIRMAN_INFO,
        news=filtered_news,
        active_category=category,
        search_query=query,
    )

@app.route("/news/<slug>")
def news_detail(slug):
    all_news = load_news()
    post = next((n for n in all_news if n.get("slug") == slug and n.get("is_published", True)), None)
    if not post:
        flash("News article not found.", "warning")
        return redirect(url_for("news_list"))

    recent_posts = [n for n in all_news if n.get("slug") != slug and n.get("is_published", True)][:3]
    return render_template("news_detail.html", info=CHAIRMAN_INFO, post=post, recent_posts=recent_posts)


# --- Interactive Contact Form ---
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_message = {
            "id": datetime.utcnow().strftime("%Y%m%d%H%M%S"),
            "name": form.name.data.strip(),
            "email": form.email.data.strip(),
            "subject": form.subject.data.strip(),
            "category": form.category.data,
            "message": form.message.data.strip(),
            "submitted_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "is_read": False,
        }

        messages_file = os.path.join(app.root_path, "data", "messages.json")
        messages = get_contact_messages()
        messages.append(new_message)

        with open(messages_file, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=4)

        flash(
            "Thank you! Your message has been received successfully. The Agatu Council team will respond shortly.",
            "success",
        )
        return redirect(url_for("contact"))

    return render_template("contact.html", info=CHAIRMAN_INFO, form=form)


# --- Authentication Routes ---
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin_dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        users_file = os.path.join(app.root_path, "data", "users.json")
        user_data = None
        if os.path.exists(users_file):
            with open(users_file, "r", encoding="utf-8") as f:
                try:
                    users = json.load(f)
                    for u in users:
                        if u["username"] == username or u["email"] == username:
                            user_data = u
                            break
                except json.JSONDecodeError:
                    pass

        if user_data and check_password_hash(user_data["password_hash"], password):
            user_obj = User(user_data)
            login_user(user_obj)
            flash(f"Welcome back, {user_obj.full_name}!", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("admin_dashboard"))
        else:
            flash("Invalid username or password. Please try again.", "danger")

    return render_template("login.html", info=CHAIRMAN_INFO)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been successfully logged out.", "info")
    return redirect(url_for("home"))


# --- Admin Portal & Dashboard ---
@app.route("/admin")
@login_required
def admin_dashboard():
    messages = get_contact_messages()
    all_news = load_news()
    unread_count = sum(1 for m in messages if not m.get("is_read", False))

    stats = {
        "total_news": len(all_news),
        "total_projects": len(PROJECTS),
        "total_wards": len(WARDS),
        "total_messages": len(messages),
        "unread_messages": unread_count,
    }

    return render_template(
        "admin/dashboard.html",
        info=CHAIRMAN_INFO,
        stats=stats,
        recent_messages=messages[-5:],
        news=all_news,
    )


# --- Media Aide: News Creation Route ---
@app.route("/admin/news/new", methods=["GET", "POST"])
@login_required
def admin_news_create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        category = request.form.get("category", "").strip()
        summary = request.form.get("summary", "").strip()
        content = request.form.get("content", "").strip()
        author = request.form.get("author", "Agatu LGA Media Office").strip()

        if not all([title, category, summary, content, author]):
            flash("Please complete all required news fields.", "danger")
            return redirect(url_for("admin_news_create"))

        # Keep basic formatting but remove scripts and unsafe HTML attributes.
        content = bleach.clean(
            content,
            tags=[
                "p", "br", "strong", "b", "em", "i", "u",
                "ul", "ol", "li", "h2", "h3", "blockquote", "a",
            ],
            attributes={"a": ["href", "title"]},
            protocols=["http", "https", "mailto"],
            strip=True,
        )

        # Verify uploaded image content; never trust the filename or browser MIME type.
        file = request.files.get("image")
        if not file or not file.filename:
            flash("Please select a photo to upload.", "danger")
            return redirect(url_for("admin_news_create"))

        try:
            with Image.open(file.stream) as uploaded_image:
                image_format = uploaded_image.format
                if image_format not in {"JPEG", "PNG", "WEBP"}:
                    raise ValueError("Unsupported image format")
                uploaded_image.verify()

            file.stream.seek(0)
            with Image.open(file.stream) as uploaded_image:
                upload_folder = os.path.join(app.root_path, "static", "images")
                os.makedirs(upload_folder, exist_ok=True)

                extension_by_format = {
                    "JPEG": ".jpg",
                    "PNG": ".png",
                    "WEBP": ".webp",
                }
                image_file = f"{uuid.uuid4().hex}{extension_by_format[image_format]}"
                destination = os.path.join(upload_folder, image_file)
                uploaded_image.save(destination, format=image_format)
        except (UnidentifiedImageError, OSError, ValueError):
            flash("Upload a valid JPEG, PNG, or WEBP image under 5 MiB.", "danger")
            return redirect(url_for("admin_news_create"))

        all_news = load_news()
        new_id = max([item.get("id", 0) for item in all_news], default=0) + 1

        new_post = {
            "id": new_id,
            "slug": simple_slug(title),
            "title": title,
            "category": category,
            "summary": summary,
            "content": content,
            "image_file": image_file,
            "additional_images": [image_file],
            "author": author,
            "created_at": datetime.now().strftime("%B %d, %Y"),
            "is_published": True,
        }

        all_news.insert(0, new_post)
        save_news(all_news)

        flash("Chairman activity post published successfully!", "success")
        return redirect(url_for("news_list"))

    return render_template("admin/news_form.html", info=CHAIRMAN_INFO)


@app.route("/admin/messages")
@login_required
def admin_messages():
    messages = get_contact_messages()
    return render_template("admin/messages.html", info=CHAIRMAN_INFO, messages=reversed(messages))


if __name__ == "__main__":
    app.run(debug=False)

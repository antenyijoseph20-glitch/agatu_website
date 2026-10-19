import os
import json
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
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

from data.departments import DEPARTMENTS, LGEA_BOARD, HEALTH_BOARD
from data.administrations import ADMINISTRATIONS
from data.profile import CHAIRMAN_INFO
from data.projects import PROJECTS
from data.wards import WARDS
from data.news import NEWS
from forms import ContactForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")

if not app.config["SECRET_KEY"]:
    raise RuntimeError(
        "FLASK_SECRET_KEY is required. Set it in your environment before starting the app."
    )

csrf = CSRFProtect(app)

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


# --- Helper Function for Contact Messages ---
def get_contact_messages():
    messages_file = os.path.join(app.root_path, "data", "messages.json")
    if os.path.exists(messages_file):
        try:
            with open(messages_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


# --- Core Public Routes ---
@app.route("/")
def home():
    return render_template("index.html", info=CHAIRMAN_INFO, projects=PROJECTS[:3], news=NEWS[:3])


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


# --- Step 1: News & Blog Routes ---
@app.route("/news")
def news_list():
    category = request.args.get("category", "").strip()
    query = request.args.get("q", "").strip().lower()

    filtered_news = [n for n in NEWS if n.get("is_published", True)]

    if category:
        filtered_news = [n for n in filtered_news if n.get("category", "").lower() == category.lower()]

    if query:
        filtered_news = [
            n for n in filtered_news
            if query in n.get("title", "").lower() or query in n.get("content", "").lower()
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
    post = next((n for n in NEWS if n.get("slug") == slug and n.get("is_published", True)), None)
    if not post:
        flash("News article not found.", "warning")
        return redirect(url_for("news_list"))

    recent_posts = [n for n in NEWS if n.get("slug") != slug and n.get("is_published", True)][:3]
    return render_template("news_detail.html", info=CHAIRMAN_INFO, post=post, recent_posts=recent_posts)


# --- Step 2: Interactive Contact Form ---
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


# --- Step 3: Authentication Routes ---
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


# --- Step 4: Admin Portal & Dashboard ---
@app.route("/admin")
@login_required
def admin_dashboard():
    messages = get_contact_messages()
    unread_count = sum(1 for m in messages if not m.get("is_read", False))

    stats = {
        "total_news": len(NEWS),
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
        news=NEWS,
    )


@app.route("/admin/messages")
@login_required
def admin_messages():
    messages = get_contact_messages()
    return render_template("admin/messages.html", info=CHAIRMAN_INFO, messages=reversed(messages))


if __name__ == "__main__":
    app.run(debug=False)
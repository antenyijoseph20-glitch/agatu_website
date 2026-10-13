import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect

from data.departments import DEPARTMENTS, LGEA_BOARD, HEALTH_BOARD
from data.administrations import ADMINISTRATIONS
from data.profile import CHAIRMAN_INFO
from data.projects import PROJECTS
from data.wards import WARDS

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")

if not app.config["SECRET_KEY"]:
    raise RuntimeError(
        "FLASK_SECRET_KEY is required. Set it in your environment before starting the app."
    )

csrf = CSRFProtect(app)


@app.route("/")
def home():
    return render_template("index.html", info=CHAIRMAN_INFO, projects=PROJECTS[:3])


@app.route("/about")
def about():
    return render_template("about.html", info=CHAIRMAN_INFO)

@app.route('/departments')
def departments():
    return render_template('departments.html', departments=DEPARTMENTS, lgea=LGEA_BOARD, health_board=HEALTH_BOARD)

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
        administrations=ADMINISTRATIONS
    )

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash(
            "This contact form is not connected to a message delivery system yet. "
            "Your message was not sent.",
            "warning",
        )
        return render_template("contact.html", info=CHAIRMAN_INFO), 503
    return render_template("contact.html", info=CHAIRMAN_INFO)


if __name__ == "__main__":
    app.run(debug=False)
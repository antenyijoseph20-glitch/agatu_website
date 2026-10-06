from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "agatu_lg_secret_key_2026"

# 1. Profile details for Hon. (Amb.) Melvin James Ejeh
CHAIRMAN_INFO = {
    "name": "Hon. (Amb.) Melvin James Ejeh",
    "title": "Executive Chairman, Agatu Local Government Council",
    "secondary_title": "Deputy Chairman, ALGON Benue State Chapter",
    "motto": "Our greatest strength is our people... Let us remain united in our common purpose.",
    "bio_summary": (
        "A grassroots leader, security strategist, and administrator dedicated to digital transformation, "
        "peace building, youth empowerment, and rural development in Agatu LGA."
    ),
    "pillars": [
        "Peace & Grassroots Security Frameworks",
        "Digital Education (Rev. Fr. Hyacinth Alia JAMB CBT Centre)",
        "Modern Transport & Market Hub Infrastructure",
        "Youth & NYSC Welfare Development",
        "State-Local Administrative Alignment"
    ]
}

PROJECTS = [
    {
        "id": 1,
        "title": "Rev. Fr. Dr. Hyacinth Iormem Alia JAMB CBT Centre",
        "location": "Obagaji, Agatu LGA",
        "category": "Education & Digital Literacy",
        "status": "Under Construction",
        "stage": "Stage 2: Superstructure & Roof Level",
        "description": "A modern Computer-Based Test facility providing UTME/JAMB exam registration and digital skills training locally for Agatu youth.",
        "image": "jamb_cbt_centre.jpg"
    },
    {
        "id": 2,
        "title": "Agatu Central Bus Terminal",
        "location": "Agatu LGA, Benue State",
        "category": "Transportation & Trade",
        "status": "Under Construction",
        "stage": "Stage 2: Structural Frame & Masonry",
        "description": "Integrated transit terminal featuring ticketing offices, passenger lounges, mechanic bays, mini pharmacy, and commercial shop stalls.",
        "image": "bus_terminal.jpg"
    },
    {
        "id": 3,
        "title": "NYSC Corpers Lodge & Commercial Hub",
        "location": "Obagaji, Agatu LGA",
        "category": "Youth Welfare & Housing",
        "status": "Under Construction",
        "stage": "Stage 2: Blockwork & Facility Layout",
        "description": "Secure residential compound for National Youth Service Corps members posted to Agatu LGA, equipped with integrated retail shops.",
        "image": "nysc_corpers_lodge.jpg"
    },
    {
        "id": 4,
        "title": "Agatu LGA Model Primary School",
        "location": "Agatu LGA, Benue State",
        "category": "Basic Education Infrastructure",
        "status": "Ongoing Project",
        "stage": "Stage 1: Renovation & Structure Rehabilitation",
        "description": "Upgraded educational facility aimed at improving foundational learning, pupil safety, and educational standards across local wards.",
        "image": "primary_school.jpg"
    },
    {
        "id": 5,
        "title": "Civic & Administrative Foundation Works",
        "location": "Obagaji Secretariat Grounds",
        "category": "Civil & Earthworks",
        "status": "Active Site Works",
        "stage": "Stage 1: Excavation & Foundation Trenching",
        "description": "Ongoing excavation, trenching, and foundation laying for essential council offices and civic facilities.",
        "image": "site_foundation.jpg"
    }
]

# 3. Web Routes
@app.route("/")
def home():
    return render_template("index.html", info=CHAIRMAN_INFO, projects=PROJECTS[:3])

@app.route("/about")
def about():
    return render_template("about.html", info=CHAIRMAN_INFO)

@app.route("/projects")
def projects():
    return render_template("projects.html", info=CHAIRMAN_INFO, projects=PROJECTS)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you! Your message has been sent to the Agatu Local Government Secretariat.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", info=CHAIRMAN_INFO)

if __name__ == "__main__":
    app.run(debug=True)
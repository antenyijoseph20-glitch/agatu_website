from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "agatu_lg_secret_key_2026"

# 1. Profile details for Hon. (Amb.) Melvin James Ejeh
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
    # Professional Contact & Social Media Information
    "contact": {
        "email": "info@agatulg.gov.ng",
        "phone": "+234 (0) 800 AGATU LG",
        "address": "Agatu Local Government Secretariat, Obagaji, Benue State, Nigeria",
        "facebook": "https://www.facebook.com/groups/426150724674912/", # Or official handle/page
        "twitter": "#",
        "whatsapp": "+2348000000000"
    },
    "pillars": [
        "Peace & Grassroots Security Frameworks",
        "Digital Education (Rev. Fr. Hyacinth Alia JAMB CBT Centre)",
        "Modern Transport & Market Hub Infrastructure",
        "Youth & NYSC Welfare Development",
        "State-Local Administrative Alignment"
    ]
}
# 2. Projects List
PROJECTS = [
    {
        "id": 1,
        "title": "Rev. Fr. Dr. Hyacinth Iormem Alia JAMB CBT Centre",
        "location": "Obagaji, Agatu LGA",
        "category": "Education & Digital Literacy",
        "status": "Under Construction",
        "stage": "Stage 2: Superstructure & Roof Level",
        "description": "A modern Computer-Based Test facility providing UTME/JAMB exam registration, CBT test-taking halls, staff offices, and digital skills training for Agatu youth.",
        "images": ["father_alia_ict.jpg", "jamb_cbt_centre.jpg"]
    },
    {
        "id": 2,
        "title": "Executive Chairman's Office Remodeling",
        "location": "LGC Secretariat, Obagaji",
        "category": "Civic Infrastructure",
        "status": "Under Construction",
        "stage": "Stage 2: Structural Reconstruction & Finishing",
        "description": "Proposed modern architectural model and ongoing structural remodeling of the Executive Chairman's Office at the LGC Secretariat.",
        "images": ["chairman_office.jpg", "chairman.jpg", "site_foundation.jpg"]
    },
    {
        "id": 3,
        "title": "Agatu Central Bus Terminal",
        "location": "Agatu LGA, Benue State",
        "category": "Transportation & Trade",
        "status": "Under Construction",
        "stage": "Stage 2: Structural Frame & Masonry",
        "description": "Integrated transit terminal featuring ticketing offices, passenger lounges, mechanic bays, mini pharmacy, and commercial shop stalls.",
        "images": ["bus_terminal.jpg"]
    },
    {
        "id": 4,
        "title": "NYSC Corpers Lodge & Commercial Hub",
        "location": "Obagaji, Agatu LGA",
        "category": "Youth Welfare & Housing",
        "status": "Under Construction",
        "stage": "Stage 2: Blockwork & Facility Layout",
        "description": "Secure residential compound for National Youth Service Corps members posted to Agatu LGA, equipped with integrated retail shops.",
        "images": ["nysc_corpers_lodge.jpg"]
    },
    {
        "id": 5,
        "title": "Contract Award for 3 Asphalt Roads",
        "location": "Agatu LGA",
        "category": "Road Infrastructure",
        "status": "Approved & Awarded",
        "stage": "Stage 1: Contract Signing & Mobilization",
        "description": "Formal signing and award of contracts for the construction of 3 major asphalt road networks across Agatu Local Government Area.",
        "images": ["award.jpg"]
    },
    {
        "id": 6,
        "title": "Mobile Security Logistics Enhancement",
        "location": "Agatu LGA",
        "category": "Security & Public Safety",
        "status": "Completed / Delivered",
        "stage": "Stage 3: Direct Distribution",
        "description": "Donation and official handover of 35 operational motorcycles to security agencies and the Nigeria Police Force to boost patrol capabilities.",
        "images": ["motorcycles_security.jpg"]
    },
    {
        "id": 7,
        "title": "111 Battalion Commanding Officer's Residence",
        "location": "Egba / Ekaida, Agatu LGA",
        "category": "Security & Defense Infrastructure",
        "status": "Ongoing Project",
        "stage": "Stage 1: Site Setup & Chalet Construction",
        "description": "Proposed architectural chalet and operational quarters setup for the Commanding Officer of the 111 Battalion, Nigerian Army.",
        "images": ["proposed_commanding_officer.jpg"]
    },
    {
        "id": 8,
        "title": "LGC Administrative Building Remodeling",
        "location": "LGC Secretariat, Obagaji",
        "category": "Civic Infrastructure",
        "status": "Under Construction",
        "stage": "Stage 2: Interior Demolition & Modernization",
        "description": "Comprehensive remodeling and interior upgrades to the main Administrative Building to enhance civil service operations.",
        "images": ["remodeling_admin_building.jpg", "site_foundation.jpg"]
    },
    {
        "id": 9,
        "title": "Establishment of Novus Microfinance Bank",
        "location": "Agatu LGA",
        "category": "Economic Empowerment & Banking",
        "status": "Completed / Functional",
        "stage": "Stage 3: Customer Centre Launch",
        "description": "Facilitation and opening of the Novus Microfinance Bank Customer Centre to bring essential banking and credit services directly to Agatu residents.",
        "images": ["microfinance_bank.jpg"]
    },
    {
        "id": 10,
        "title": "Healthcare Provision for Obagaji General Hospital",
        "location": "General Hospital, Obagaji",
        "category": "Healthcare Infrastructure",
        "status": "Completed / Delivered",
        "stage": "Stage 3: Supply & Distribution",
        "description": "Donation and delivery of hospital mattresses and ward furniture to upgrade patient accommodations at General Hospital, Obagaji.",
        "images": ["donation_of_mattress.jpg"]
    },
    {
        "id": 11,
        "title": "Monthly IDP Relief Material Distribution",
        "location": "Agatu LGA",
        "category": "Social Welfare & Humanitarian Aid",
        "status": "Ongoing Program",
        "stage": "Stage 3: Regular Relief Supply",
        "description": "Regular monthly distribution of food supplies, mattresses, and essential relief items to internally displaced persons across local communities.",
        "images": ["relief_materials_idp.jpg"]
    },
    {
        "id": 12,
        "title": "Restoration of Annual Children's Day Celebration",
        "location": "Agatu LGA",
        "category": "Youth Development & Culture",
        "status": "Completed Event / Annual Program",
        "stage": "Stage 3: Community Hosting",
        "description": "Revival of official Children's Day celebrations, featuring youth march-pasts, cultural displays, and educational gift distributions.",
        "images": ["restoration_children_day.jpg"]
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

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        flash("Project not found.", "warning")
        return redirect(url_for("projects"))
    return render_template("project_detail.html", info=CHAIRMAN_INFO, project=project)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you! Your message has been sent to the Agatu Local Government Secretariat.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", info=CHAIRMAN_INFO)

if __name__ == "__main__":
    app.run(debug=True)
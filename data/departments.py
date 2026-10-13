"""
Agatu Local Government Area - Departments & Autonomous Local Boards
Covers local council departments alongside autonomous boards (LGEA Teachers Board & Primary Health Care Authority).
"""

DEPARTMENTS = [
    {
        "id": 1,
        "name": "Personnel & General Services",
        "head": "Head of Department (HOD) Personnel",
        "description": "Manages civil service human resources, establishment records, staff postings, promotions, and administrative registry at Obagaji Secretariat.",
        "units": ["HR & Establishment", "Registry & Protocol", "Information & Public Relations", "Staff Welfare"]
    },
    {
        "id": 2,
        "name": "Finance & Accounts",
        "head": "Head of Department (HOD) Finance",
        "description": "Responsible for central financial management, statutory allocation disbursement, budgeting, payroll processing, and internal accounting.",
        "units": ["Treasury Unit", "Payroll & Emoluments", "Central Accounts", "Internal Audit"]
    },
    {
        "id": 3,
        "name": "Revenue & Procurement",
        "head": "Head of Department (HOD) Revenue",
        "description": "Coordinates internal revenue generation, market levies, riverine transport tariffs, business licensing, and civic procurement.",
        "units": ["Tax & Revenue Collection", "Market & Jetty Tariffs", "Licensing Unit", "Procurement Inspection"]
    },
    {
        "id": 4,
        "name": "Education & Social Development",
        "head": "Head of Department (HOD) Education",
        "description": "Coordinates council civic literacy, social welfare programs, sports development, youth empowerment, and liaison with educational institutions.",
        "units": ["Social Welfare & Civic Affairs", "Youth & Sports Development", "Community Mobilization", "Women Affairs"]
    },
    {
        "id": 5,
        "name": "Agriculture & Natural Resources",
        "head": "Head of Department (HOD) Agriculture",
        "description": "Drives rural agricultural programs, extension services, riverine fishing cooperative support, forestry preservation, and agrarian outreach.",
        "units": ["Agricultural Extension", "Fisheries & Riverine Logistics", "Livestock & Veterinary", "Forestry & Land Use"]
    },
    {
        "id": 6,
        "name": "Works, Housing & Infrastructure",
        "head": "Head of Department (HOD) Works",
        "description": "Manages public infrastructure, rural access road rehabilitation, maintenance of Secretariat buildings, and civic logistics.",
        "units": ["Civil Engineering & Roads", "Building & Facility Maintenance", "Electrical & Utilities", "Transport & Fleet Operations"]
    }
]

# Local Government Education Authority (LGEA - Teachers Board)
LGEA_BOARD = {
    "title": "Local Government Education Authority (LGEA) / Teachers Board",
    "leadership": "Education Secretary (ES)",
    "board_overview": "Operating in direct collaboration with the Benue State Universal Basic Education Board (SUBEB), the Agatu LGEA manages primary school teachers, educational infrastructure, teacher payroll/welfare, and basic school supervision across all 10 wards.",
    "units": [
        "Teacher Personnel Management (TPM)",
        "Academic Supervision & Quality Assurance",
        "Planning, Research & Statistics (PRS)",
        "Finance & Accounts Unit"
    ]
}

# Local Government Primary Health Care Board / Authority
HEALTH_BOARD = {
    "title": "Agatu Primary Health Care Authority / Board",
    "leadership": "Director of Primary Health Care (DPHC)",
    "board_overview": "Autonomous health management entity operating at the local government level in partnership with the Benue State Primary Health Care Development Board (BSPHCDB) to oversee primary health centers (PHCs), maternal health, and immunization drives.",
    "units": [
        "Immunization & Cold Chain Logistics",
        "Maternal, Newborn & Child Health (MNCH)",
        "Disease Surveillance & Epidemic Control",
        "PHC Infrastructure & Clinical Services"
    ]
}
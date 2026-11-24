# Agatu Geographic Intelligence, Community Development, Public Safety and Investment Platform
## Master Research Index and Cross-Sector Overview

**Research cut-off:** 24 November 2026  
**Document status:** Working research and requirements baseline — NOT APPROVED FOR IMPLEMENTATION  
**Ownership model:** Independently developed platform proposed for official Agatu Local Government adoption or institutional collaboration. It is not an official government platform unless and until formal authorisation is obtained.

## 1. Purpose and vision

The proposed platform is intended to improve geographic and boundary awareness, community documentation, public safety awareness, natural-resource and environmental intelligence, infrastructure and public-service monitoring, community participation, and responsible investment visibility across Agatu Local Government Area, Benue State, Nigeria.

The working strategic pillars are:
1. Geographic information and boundary awareness.
2. Community safety and public protection.
3. Natural resources and environmental intelligence.
4. Government, infrastructure and community development.
5. Investment and economic opportunities.

The platform should extend the existing Flask Agatu LGA website incrementally. It must not be presented as an official government portal without written adoption or authorisation.

## 2. Research scope and sector documents

This library contains separate working documents for:
1. Geography, boundaries and mapping.
2. Natural resources, environment and investment.
3. Historical development projects.
4. Physical verification and community feedback.
5. Education.
6. Healthcare.
7. Roads, bridges and transport.
8. Agriculture, irrigation and fisheries.
9. Electricity and energy.
10. Water, sanitation and public health.
11. Markets, commerce and local economy.
12. Security, displacement and humanitarian recovery.
13. Flooding, climate and disaster management.
14. Industry, minerals and natural-resource investment.
15. Housing, land and settlement development.
16. Telecommunications and digital infrastructure.
17. Culture, heritage, tourism and sports.
18. Public administration, governance and justice.
19. Population, demographics and social development.
20. Financial inclusion, banking and payments.

The shared architecture, governance and security requirements are in `21_SHARED_PLATFORM_ARCHITECTURE_GOVERNANCE_AND_SECURITY.md`.

## 3. Evidence and verification vocabulary

Use the following labels at the claim/record level. Multiple labels may coexist for different aspects of one project.

- **Source-recorded:** found in a document, register, public statement or credible report; authenticity and meaning may still require review.
- **Pending verification:** evidence is incomplete or a primary source has not been obtained.
- **Budget entry verified:** the relevant budget entry is authenticated; this does not prove procurement or implementation.
- **Award verified:** award evidence is authenticated; this does not prove physical execution.
- **Physical completion verified:** physical completion is supported by adequate inspection and corroborating evidence.
- **Operationally verified:** operation/functionality has been checked on a dated inspection.
- **Community-confirmed:** corroborated by identified community custodians or multiple credible witnesses, subject to safe publication.
- **Independently corroborated:** supported by evidence independent of the originating claim.
- **Disputed/conflicting evidence:** material sources disagree; retain each version and explain the conflict.
- **Implementation unknown:** available evidence does not establish whether implementation occurred.
- **Restricted:** information is retained for authorised review and is not suitable for public display.

Do not use a single generic “Verified” badge to imply every claim about a project is true. Verify the budget entry, contract award, physical progress, completion and current operation separately.

## 4. Mandatory historical project preservation rules

Never delete a discovered project or budget entry because it is proposed, unimplemented, delayed, abandoned, disputed, cancelled or of unknown status. Preserve:
- Proposed, budgeted, approved, awarded, ongoing, delayed, abandoned, completed, rehabilitated, cancelled and unknown records.
- Original source, page/row, publication date, source institution and retrieval date.
- Conflicting figures and descriptions.
- Every status change and the reason/evidence for it.
- Multiple funding packages and contracts under one parent project where appropriate.

Financial values must remain distinct:
- Proposed amount.
- Budgeted amount.
- Approved/appropriated amount.
- Contract amount.
- Funds released.
- Amount paid.
- Outstanding balance.
- Variations/revised contract amount.

A financial expenditure entry does not prove physical completion. A photo does not prove progress by itself. A tender does not prove an award. A contract award does not prove commencement or completion.

## 5. Mandatory project-register fields

Every project record should capture, where evidence is available:
- Project name and description.
- Community, ward and geographic coordinates with accuracy/provenance.
- Sector and project type.
- Funding institution and implementing agency.
- Budget reference and approved amount.
- Contractor and procurement information where lawfully public.
- Planned and actual start/completion dates.
- Implementation status.
- Evidence of physical progress.
- Last verification date.
- Supporting documents, photographs and inspection records.
- Submitter, reviewer, reviewer role, review date, decision and reason.
- Source provenance and full version/change history.

Additional recommended fields include procurement method, tender reference, award date, contract reference, contractor registered identity, contract variations, inspection reports, defects, delays and reasons, handover/commissioning, current operational condition, community feedback and institutional response.

## 6. Mandatory Physical Verification module

A dedicated module must preserve multiple site inspections per project. Each inspection should record:
- Project linked, if known.
- Whether the project exists at the reported location.
- Implementation stage and observed physical progress.
- Functionality and operational condition.
- Defects, damage and quality concerns.
- Evidence files and contextual description.
- Inspection date and time.
- Verifier identity and role, with restricted personal details where necessary.
- GPS/location and accuracy only where safe and appropriate.
- Whether rehabilitation or maintenance is required.
- Reviewer decision, supporting evidence and history.

An inspection must not overwrite an earlier inspection.

## 7. Mandatory Feedback and Community Reports module

A separate module must accept reports about project existence, quality, progress, defects, abandonment, functionality and concerns. Each report should record:
- Submission date and channel.
- Linked project, if known.
- Location and description.
- Evidence attachments, if provided.
- Anonymous/confidential option and protected contact details.
- Review status, findings and follow-up.
- Response, referral and resolution history.

A community report is an observation or allegation to investigate, not automatically a verified fact. Anonymous and confidential reporting must be designed with safeguards against retaliation and malicious submissions.

## 8. Cross-sector dependencies

- Geography is the spatial foundation for every sector; boundary authority and location accuracy must be explicit.
- Population and settlement data inform service coverage, but old census figures must not be presented as current.
- Historical project records connect to roads, schools, health, water, energy, agriculture, markets and public buildings.
- Physical verification and community feedback are shared services across all project sectors.
- Security, displacement and disaster data require stronger access controls and safe aggregation.
- Investment information depends on independently verified resources, land/legal status, infrastructure, utilities and community consent.
- Telecom access affects the platform's own availability and submission channels.
- Financial inclusion connects residents, cooperatives, farmers, traders and MSMEs to support programmes.
- Governance and justice research establishes institutional mandates, referral pathways and the limits of the privately developed platform.
- Cultural and population data require consent, provenance and careful treatment of community knowledge.

## 9. Shared platform principles

1. Evidence before claims.
2. Preserve source records and conflicting evidence.
3. Never imply government authority without authorisation.
4. Separate public, reviewer and restricted information.
5. Do not expose informants, vulnerable people, private household details or operational security information.
6. Do not adjudicate land, chieftaincy, criminal or civil disputes.
7. Do not make unsupported mineral, investment, population or completion claims.
8. Use accessible, low-bandwidth, mobile-friendly design and offline field collection with later synchronisation.
9. Maintain audit trails, role-based access, correction processes and retention rules.
10. Preserve existing website content and datasets during any future approved migration.

## 10. Existing website and data baseline

The existing project is a Flask website at `~/agatu_website`, with Python 3.12, Flask, HTML/CSS, Bootstrap 5, Flask-Login, Flask-WTF, Bleach, Pillow, JSON and Gunicorn. Existing routes include home, about, projects, news, wards, administrations, departments, contact, schools and health facilities.

The wards page uses Leaflet 1.9.4 and OpenStreetMap tiles with six approximate ward marker coordinates explicitly described as approximate. They are not verified ward boundaries or official coordinates.

The existing wards dataset contains ten wards and 112 polling units, with internal consistency checks passing. This is not legal boundary verification or external confirmation against INEC.

Existing directories contain 67 school records and 51 health-facility records, all marked `needs_confirmation`. Preserve records and source metadata. Do not publish as verified.

Existing branding includes “AGATU LOCAL GOVERNMENT AREA” and “OFFICIAL EXECUTIVE PORTAL” language. Because the current development model is independent, branding and official-sounding claims require legal/ethical review and clear disclosure before public launch.

## 11. Architecture direction — preliminary only

A likely long-term direction is to extend Flask and, if scale and spatial requirements justify it, use PostgreSQL/PostGIS with SQLAlchemy and Flask-Migrate. Leaflet/OpenStreetMap and selectively Google Maps should be compared on accuracy, licensing, coverage, costs, geocoding, routing, tiles and API terms. This is not final approval to migrate or code.

Avoid premature microservices. Define data governance, security, workflow and user needs first.

## 12. Review and approval gate

This library is a working research baseline. It is not an implementation authorisation. The user must review each sector document, request corrections and explicitly approve the consolidated requirements before any coding, website changes, data changes, GitHub push or deployment.

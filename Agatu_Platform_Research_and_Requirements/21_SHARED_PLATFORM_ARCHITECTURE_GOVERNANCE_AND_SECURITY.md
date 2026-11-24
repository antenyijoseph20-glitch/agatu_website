# Shared Platform Architecture, Governance, Privacy and Security Requirements

**Status:** Preliminary cross-sector requirements; requires user review and technical/legal validation.

## 1. Existing system and incremental strategy

Existing Flask application at `~/agatu_website`; Python 3.12, Flask, Bootstrap 5, Flask-Login, Flask-WTF, Bleach, Pillow, JSON and Gunicorn. Existing pages include home, about, projects, news, wards, administrations, departments, contact, schools and health facilities.

Do not rewrite or modify until requirements are approved. Preserve existing datasets, route behaviour and source metadata.

## 2. Preliminary architecture direction

Potential future stack:
- Flask application factory and modular blueprints.
- PostgreSQL/PostGIS if spatial querying, geometry integrity and multi-user workflows justify it.
- SQLAlchemy and Flask-Migrate.
- Leaflet/OpenStreetMap; selectively compare Google Maps.
- Role-based access control, audit logs and append-only histories.
- File storage with access control, integrity metadata and backups.
- Offline-capable field capture with delayed synchronisation.
- Avoid premature microservices.

Architecture is not approved until user review and feasibility assessment.

## 3. Roles and access tiers

Potential roles: public visitor, registered submitter, community reporter, field verifier, sector reviewer, institutional liaison, editor, administrator and security/privacy officer. Define least privilege and separation of duties.

Information tiers:
- Public.
- Registered/consented user.
- Authorised reviewer.
- Restricted administrator.
- Highly restricted safety/security records.

Do not assume a public-sector institution has granted the platform authority or data access.

## 4. Shared data governance

Every record should have stable ID, sector, source/provenance, creation date, update date, submitter, reviewer, status, evidence, confidence/limitations, publication tier and revision history.

Use controlled vocabularies and consistent ward/community identifiers. Preserve alternative spellings and disputed identities. Do not silently overwrite historical data.

## 5. Privacy and security

Nigeria Data Protection Act 2023: assess lawful basis, transparency, purpose limitation, data minimisation, accuracy, retention, security, data-subject rights, breach response, DPIA and registration obligations where applicable.

Security requirements:
- Secure authentication and password handling.
- Multi-factor authentication for privileged roles where feasible.
- CSRF protection, input validation and output encoding.
- File-type/size validation and malware scanning where feasible.
- Encryption in transit and at rest where appropriate.
- Secrets outside source control.
- Backups, restore tests and incident response.
- Audit logging for sensitive access and decisions.
- Dependency and vulnerability management.
- Rate limiting, abuse detection and secure error handling.

Do not collect health, political, religious, ethnic, biometric, financial credential or other sensitive personal data unless necessary, lawful and explicitly governed. Public data should be aggregated and safe.

## 6. Legal and institutional boundaries

Platform is independently developed and proposed for adoption. It is not an official government system. It cannot issue land title, decide land/chieftaincy disputes, certify mineral reserves, enforce law, operate emergency response, adjudicate complaints or certify procurement without lawful authority.

Institutional integrations require formal agreements, data-sharing terms, purpose limitation, security review and authorised contacts.

## 7. Mapping and data quality

Each location/geometry requires source, capture method, date, accuracy, coordinate reference system, licence and verification status. Approximate markers are not official boundaries. Public submissions remain pending until reviewed.

## 8. Accessibility and resilience

- Mobile-first responsive design.
- Low-bandwidth pages and compressed media.
- Offline field capture and later sync.
- Assisted submission channels where safe.
- Accessible forms, keyboard navigation, readable contrast and clear language.
- Graceful handling of poor connectivity and power outages.
- Data export and backup formats to reduce lock-in.

## 9. Shared workflows

Discovery → submission → triage → duplicate/link check → review → evidence verification → decision → publication/referral → correction/appeal → retention/archive.

High-impact project and institutional claims should receive independent review. Community reports are not automatically verified.

## 10. Testing and acceptance

- Unit and integration tests for permissions, workflows and audit history.
- Security tests for authentication, CSRF, file upload and access control.
- Data validation and duplicate detection.
- Backup/restore tests.
- Accessibility and low-bandwidth tests.
- GIS coordinate/projection and boundary tests.
- User acceptance with representative users and authorised institutional stakeholders.
- No deployment until user approval and a reviewed release plan.

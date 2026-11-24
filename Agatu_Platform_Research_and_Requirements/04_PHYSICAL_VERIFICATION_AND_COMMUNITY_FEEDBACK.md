# Sector 04 — Physical Verification and Community Feedback

**Status:** Mandatory platform requirement, explicitly requested by user.

## 1. Purpose

Create independent, traceable records of site inspections and community observations for public projects, infrastructure and services. These are separate processes: an inspection is not a community complaint, and a community report is not a verified finding.

## 2. Physical Verification module

Each site visit is a separate immutable inspection record linked to a master project/facility where possible.

Required fields:
- Inspection ID and linked project/facility ID.
- Project name and reported location.
- Does the project physically exist at that location?
- Observed implementation stage.
- Physical progress and components inspected.
- Functional/operational condition.
- Quality defects, damage and safety concerns.
- Rehabilitation/maintenance required and urgency.
- Inspection date/time.
- Verifier identity, role, organisation and authorisation; protect personal details.
- GPS coordinates, accuracy and capture method only where safe.
- Photos/video/documents with date, context, consent and integrity metadata.
- Inspection method, limitations and people consulted.
- Reviewer, review date, decision, reason and follow-up.
- Full version and audit history.

Multiple inspections must attach to one project; never overwrite earlier inspections. Preserve a historical timeline.

## 3. Feedback and Community Reports module

Required fields:
- Report ID and submission date/channel.
- Reporter identity/contact only if voluntarily provided and necessary.
- Anonymous/confidential submission option.
- Linked project/facility or unlinked location.
- Ward/community and safe location precision.
- Report category: existence, quality, progress, defects, abandonment, functionality, access, service failure or other concern.
- Narrative and evidence attachments.
- Consent/lawful basis and publication preference.
- Triage and risk level.
- Review status, reviewer, date and findings.
- Referral/institution contacted.
- Response, action, resolution and appeal/correction history.

A report is an allegation/observation, not automatically a fact. Do not publish accusations as verified findings.

## 4. Workflow

1. Submission or authorised inspection creation.
2. Acknowledgement and safe triage.
3. Duplicate/link detection.
4. Reviewer assignment.
5. Evidence checks and site inspection if appropriate.
6. Independent review for high-impact claims.
7. Decision: corroborated, not corroborated, disputed, insufficient evidence, referred, closed or restricted.
8. Response/referral and resolution tracking.
9. Publication decision by information tier.
10. Retention, correction and audit.

## 5. Privacy, safety and anti-abuse safeguards

- Protect confidential informants and vulnerable reporters.
- Do not expose personal phone numbers, home addresses or precise locations where unsafe.
- Do not collect unnecessary identity documents.
- Rate-limit and detect malicious submissions.
- Preserve evidence without publicly repeating unverified allegations.
- Provide correction/appeal route.
- Restrict security-sensitive infrastructure and operational information.
- Obtain permission for identifiable photographs and interviews.
- Retain only what is necessary under a documented retention schedule.

## 6. Public/reviewer/restricted tiers

- Public: reviewed, safe, appropriately aggregated findings and verified project facts.
- Authorised reviewer: submissions, inspection notes, evidence and correction history.
- Restricted administrator: protected identities, sensitive documents and confidential operational information.

## 7. Acceptance criteria

- Inspection history is append-only/versioned.
- Community reports never automatically change a project to verified.
- Anonymous/confidential reports are supported with safeguards.
- Each decision records reviewer, date, reason and evidence.
- Sensitive information is excluded from public output by default.

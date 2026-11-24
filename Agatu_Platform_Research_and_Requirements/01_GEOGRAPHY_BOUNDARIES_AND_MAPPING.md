# Sector 01 — Geography, Boundaries and Mapping

**Status:** Working research baseline; pending review.  
**Scope:** Agatu LGA, its ten wards, settlements, community locations, boundaries and spatial reference data.

## 1. Purpose

Provide reliable geographic context for all other platform sectors. The platform must distinguish legal administrative boundaries from approximate markers, community descriptions, settlement points and user-submitted locations.

## 2. Agatu geographic baseline

Research sources describe Agatu as headquartered at Obagaji, created in 1991, with an area often reported around 1,065 km². A secondary local-governance portal reports a 2006 population of 115,597 and approximate coordinates. These are orientation leads, not substitutes for primary NPC or Surveyor-General records.

A 2019 UN Women/Institute for Peace and Conflict Resolution baseline describes Agatu's location along the Benue River, fadama/irrigable land, highlands and western forest areas, and its farming/fishing livelihoods.

## 3. Ten wards and existing data

The existing `data/wards.py` dataset contains:
- Egba — 16 polling units.
- Enungba — 10.
- Obagaji — 20.
- Odugbeho — 6.
- Ogbaulu — 5.
- Ogwule-Kaduna — 10.
- Ogwule Ogbaulu — 13.
- Okokolo — 8.
- Oshigbudu — 7.
- Usha — 17.

Total: 112 polling units. Internal consistency checks found no duplicate ward codes or polling-unit codes and no declared-versus-actual count inconsistencies. This establishes internal consistency only; it does not prove official ward boundaries or current polling-unit status.

The existing ward webpage contains six hardcoded approximate marker coordinates. Its own comment describes them as approximate ward headquarters coordinates. Do not represent these as verified coordinates or polygons.

## 4. Boundary research and source leads

- National Boundary Commission (NBC) announced a planned Benue–Nasarawa interstate boundary demarcation using historical descriptions from 1916, 1919 and 1924. A 2024 report said the exercise had been paused after security concerns in 2022, with some pillars reportedly emplaced and some destroyed. No evidence in the research establishes a final completed Agatu-relevant boundary determination.
- NBC's Internal Boundaries function includes delimitation-record searches, joint field investigations, provisional demarcation, community sensitisation and dispute prevention/resolution.
- Benue Ministry of Lands and Survey describes responsibilities for land administration, state maps, boundary delimitation and liaison with local governments.
- Survey Department functions include plot surveys, beaconing, layouts, disputed-plot surveys, government project engineering surveys, control pillars, interstate boundaries with the Federal Survey Boundary Unit, inter-LGA/district boundaries and survey coordinate storage.
- GRID3 catalogue lists operational ward boundaries v4.0 (Oct 2026), LGA boundaries (Dec 2020), settlement extents v4.1 (Aug 2026), named settlement points (Sep 2020), roads/travel-time datasets (Oct 2025). Catalogue presence does not prove Agatu coverage; inspect layer metadata, provenance, geographic coverage and licence.
- openAFRICA Benue operational ward boundaries metadata dates to 2017–18; reuse licence is unclear.
- Older academic and orientation maps are not legal boundary records.

## 5. Requirements

### 5.1 Boundary records
Capture administrative level, boundary name, geometry, source authority, legal/administrative status, effective date, coordinate reference system, scale/resolution, accuracy, survey date, custodian, licence, provenance and revision history.

### 5.2 Settlement register
Capture official and alternative names, ward/LGA, settlement type, coordinates and accuracy, extent where reliable, population estimate with source/year, roads, public facilities, historical changes, source, last field confirmation and verification status.

### 5.3 Location submissions
Residents/business owners and authorised government officers may submit locations. Submissions remain pending until review and approval by an authorised reviewer. Record submitter role, consent/lawful basis, source, accuracy, duplicate checks, review decision, correction history and audit log.

### 5.4 Mapping
Evaluate hybrid use of OpenStreetMap and Google Maps. Compare coverage, map quality, licensing, tile/API costs, geocoding, search, routing, offline options, update process and vendor lock-in. Existing Leaflet/OSM prototype should be preserved until a reviewed migration plan is approved.

## 6. Legal and safety constraints

- Do not publish a disputed or provisional boundary as a final legal boundary.
- Do not allow public users to edit authoritative administrative boundaries.
- Provide a correction/objection process with source evidence and review.
- Separate public geographic information from restricted cadastral, household, security and sensitive site information.
- Do not infer land ownership or title from a map point or settlement listing.
- Include country in addresses where known and preserve coordinate provenance.

## 7. Research gaps

1. Obtain authoritative Agatu LGA and ward boundary records from Surveyor-General/NBC/Benue authorities.
2. Confirm whether the NBC Benue–Nasarawa exercise resumed and whether any final records cover Agatu.
3. Inspect GRID3 layer coverage and licences for Agatu.
4. Verify all ten ward headquarters and settlement coordinates.
5. Build a settlement gazetteer with spelling variants and community confirmation.
6. Reconcile polling-unit names/codes against current INEC records.
7. Define a safe field-survey method and accuracy thresholds.

## 8. Acceptance criteria

- No approximate marker is labelled as a legal boundary.
- Every geometry has provenance, date, accuracy and licence.
- All ten wards are represented without unsupported boundary claims.
- User submissions remain pending until reviewed.
- Boundary disputes and conflicting maps are retained as separate evidence records.

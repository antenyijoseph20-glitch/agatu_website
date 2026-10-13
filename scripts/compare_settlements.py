"""Compare Agatu settlement research candidates with a secondary source.

This is a read-only research audit. It does not modify public data.
Matches indicate name similarity, not official settlement verification.
"""

from collections import Counter
from pathlib import Path
import re
import sys
import unicodedata


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from data.settlement_research import CANDIDATE_SETTLEMENTS


SECONDARY_SOURCE = (
    "TownsVillages — Agatu LGA: All 65 Towns & Villages"
)

# Transcribed from the secondary compilation for comparison only.
# This is not an official or exhaustive settlement register.
SECONDARY_NAMES = [
    "Abalichi",
    "Abugbe",
    "Adagbo",
    "Adana",
    "Agbadumo",
    "Aila",
    "Ajomachi",
    "Akele",
    "Akoro",
    "Akpeke",
    "Akwu",
    "Ashomo",
    "Atakpa",
    "Ayele",
    "Ebete",
    "Edeje",
    "Egba",
    "Egwuma",
    "Ejima",
    "Ekwo",
    "Ello",
    "Engila",
    "Enicha",
    "Enogoje",
    "Enungba",
    "Ichogolugwu",
    "Iga-Gishu",
    "Igboji",
    "Ikpele",
    "Inminyi",
    "Obagaji",
    "Obanowa",
    "Obishu",
    "Odejo",
    "Odugbeho",
    "Ogam",
    "Ogbangede",
    "Ogbaulu",
    "Ogule",
    "Ogwufa",
    "Ogwule Ogbaulu",
    "Ogwule Ugbokpo",
    "Ogwule-Ankpa",
    "Ogwule-Kaduna",
    "Ogwumogbo",
    "Okadu",
    "Okokolo",
    "Okpagabi",
    "Okpanchenyi",
    "Okpokpolo",
    "Olechologba",
    "Olegabulu",
    "Olegeje",
    "Olegetonu",
    "Olegobidu",
    "Olegochepo",
    "Olegoga",
    "Omikwidi",
    "Onugba",
    "Oshigbudu",
    "Oweto",
    "Ugboju",
    "Usha",
    "Utugolugwu",
    "Warri",
]

# These are hypotheses for manual review, not confirmed aliases.
POSSIBLE_VARIANTS = {
    "Ichogologwu": "Ichogolugwu",
    "Olocho-logba": "Olechologba",
}


def normalize_name(value):
    """Ignore letter case, whitespace, and punctuation for comparison."""
    value = unicodedata.normalize("NFKC", str(value)).casefold()
    return "".join(character for character in value if character.isalnum())


def describe_candidate(item):
    return (
        f"[{item['ward_code']} {item['ward_name']}] "
        f"{item['name']}"
    )


def main():
    candidates = CANDIDATE_SETTLEMENTS

    if not isinstance(candidates, list):
        raise TypeError("CANDIDATE_SETTLEMENTS must be a list.")

    if not all(
        isinstance(item, dict)
        and item.get("name")
        and item.get("ward_code")
        and item.get("ward_name")
        for item in candidates
    ):
        raise ValueError("A research record is missing required fields.")

    if len({normalize_name(name) for name in SECONDARY_NAMES}) != len(
        SECONDARY_NAMES
    ):
        raise ValueError(
            "The secondary-source list contains duplicate normalized names."
        )

    secondary_by_key = {
        normalize_name(name): name for name in SECONDARY_NAMES
    }

    exact_matches = []
    research_unmatched = []
    used_secondary_names = set()

    for item in candidates:
        original = item["name"]
        key = normalize_name(original)

        if key in secondary_by_key:
            matched_name = secondary_by_key[key]
            exact_matches.append((item, matched_name))
            used_secondary_names.add(matched_name)
        else:
            research_unmatched.append(item)

    # List possible spelling variants separately. Do not silently merge them.
    variant_rows = []
    for item in research_unmatched:
        candidate_name = item["name"]
        proposed_match = POSSIBLE_VARIANTS.get(candidate_name)

        if proposed_match in SECONDARY_NAMES:
            variant_rows.append((item, proposed_match))

    # A source name is considered accounted for if it has an exact normalized
    # match or is suggested as a possible variant for manual review.
    variant_source_names = {
        proposed_match for _, proposed_match in variant_rows
    }
    secondary_unmatched = [
        name
        for name in SECONDARY_NAMES
        if name not in used_secondary_names
        and name not in variant_source_names
    ]

    print("=" * 68)
    print("AGATU SETTLEMENT NAME COMPARISON")
    print("READ-ONLY RESEARCH AUDIT")
    print("=" * 68)
    print(f"Research records: {len(candidates)}")
    print(f"Secondary-source names: {len(SECONDARY_NAMES)}")
    print(f"Exact normalized matches: {len(exact_matches)}")
    print(f"Possible spelling variants: {len(variant_rows)}")
    print(f"Research names without exact matches: {len(research_unmatched)}")
    print(f"Secondary names not accounted for: {len(secondary_unmatched)}")

    print("\n1. EXACT NORMALIZED MATCHES")
    for item, matched_name in exact_matches:
        print(f"  {describe_candidate(item)} <-> {matched_name}")

    print("\n2. POSSIBLE SPELLING VARIANTS — MANUAL REVIEW REQUIRED")
    if variant_rows:
        for item, matched_name in variant_rows:
            print(
                f"  {describe_candidate(item)} ~ {matched_name}"
            )
    else:
        print("  None.")

    print("\n3. RESEARCH NAMES WITHOUT AN EXACT MATCH")
    for item in research_unmatched:
        print(f"  {describe_candidate(item)}")

    print("\n4. SECONDARY-SOURCE NAMES NOT ACCOUNTED FOR")
    for name in secondary_unmatched:
        print(f"  {name}")

    counts = Counter(
        (item["ward_code"], item["ward_name"]) for item in candidates
    )
    print("\n5. RESEARCH CANDIDATES BY WARD")
    for (code, ward), count in sorted(counts.items()):
        print(f"  {code} {ward}: {count}")

    print("\nSOURCE LIMITATIONS")
    print(f"  Comparison source: {SECONDARY_SOURCE}")
    print("  It is a secondary compilation, not an official register.")
    print("  A name match does not verify a settlement or its ward.")
    print("  Candidate spellings and ward assignments remain unchanged.")
    print("\nNo project data files were modified.")


if __name__ == "__main__":
    main()

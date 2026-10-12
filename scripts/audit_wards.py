from collections import Counter
from pathlib import Path
import sys

# Add the project root to Python's import path.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from data.wards import WARDS, SOURCE


def normalize(value):
    """Normalize text for basic duplicate checking."""
    return " ".join(str(value).strip().lower().split())


def audit_wards():
    print("=" * 60)
    print("AGATU LGA WARD AND POLLING UNIT AUDIT")
    print("=" * 60)

    errors = []
    warnings = []

    # Check the number of wards.
    print(f"\nTotal wards: {len(WARDS)}")

    if len(WARDS) != 10:
        errors.append(f"Expected 10 wards, found {len(WARDS)}.")

    # Check for duplicate ward codes and names.
    codes = [str(ward.get("code", "")).strip() for ward in WARDS]
    names = [normalize(ward.get("name", "")) for ward in WARDS]

    for code, count in Counter(codes).items():
        if not code or count > 1:
            errors.append(f"Missing or duplicate ward code: {code!r}")

    for name, count in Counter(names).items():
        if not name or count > 1:
            errors.append(f"Missing or duplicate ward name: {name!r}")

    # Check polling-unit records.
    total_polling_units = 0
    all_units = []

    print("\nPolling units by ward:")
    print("-" * 60)

    for ward in WARDS:
        code = str(ward.get("code", "")).strip()
        name = str(ward.get("name", "")).strip()
        units = ward.get("polling_units")

        if not name:
            errors.append(f"Ward {code!r} has no name.")

        if not isinstance(units, list):
            errors.append(
                f"Ward {code} ({name}) has an invalid polling_units value."
            )
            continue

        print(f"{code:>3} | {name:<20} | {len(units):>3} units")

        total_polling_units += len(units)

        for unit in units:
            if not isinstance(unit, str) or not unit.strip():
                errors.append(
                    f"Ward {code} ({name}) contains an empty or invalid unit."
                )
                continue

            all_units.append(
                {
                    "ward_code": code,
                    "ward_name": name,
                    "original_name": unit.strip(),
                    "normalized_name": normalize(unit),
                }
            )

        if not isinstance(ward.get("villages", []), list):
            errors.append(f"Ward {code} ({name}) has an invalid villages value.")

    # Find exact normalized names repeated across the dataset.
    unit_counts = Counter(
        unit["normalized_name"] for unit in all_units
    )

    duplicates = {
        unit_name: count
        for unit_name, count in unit_counts.items()
        if count > 1
    }

    print("-" * 60)
    print(f"Total polling-unit records: {total_polling_units}")
    print(f"Unique normalized unit names: {len(unit_counts)}")

    if total_polling_units != 112:
        warnings.append(
            f"The current total is {total_polling_units}, not the expected 112."
        )

    if duplicates:
        print("\nPotential duplicate polling-unit names:")
        for unit_name, count in sorted(duplicates.items()):
            matching_units = [
                unit for unit in all_units
                if unit["normalized_name"] == unit_name
            ]

            print(f"\n  {unit_name!r} appears {count} times:")
            for unit in matching_units:
                print(
                    f"    Ward {unit['ward_code']} "
                    f"({unit['ward_name']}): {unit['original_name']}"
                )

        warnings.append(
            "Potential duplicate names require manual review; "
            "do not delete records automatically."
        )
    else:
        print("\nNo exact normalized duplicate names found.")

    # Report source and verification information.
    print("\nSource and verification:")
    print(f"  Ward names: {SOURCE.get('ward_names', 'Not specified')}")
    print(f"  Polling units: {SOURCE.get('polling_units', 'Not specified')}")
    print(
        "  Verification status: "
        f"{SOURCE.get('verification_status', 'Not specified')}"
    )

    print("\nAUDIT ERRORS:")
    if errors:
        for error in errors:
            print(f"  - {error}")
    else:
        print("  None found.")

    print("\nWARNINGS:")
    if warnings:
        for warning in warnings:
            print(f"  - {warning}")
    else:
        print("  None found.")

    print("\nAudit completed. No data has been changed.")


if __name__ == "__main__":
    audit_wards()

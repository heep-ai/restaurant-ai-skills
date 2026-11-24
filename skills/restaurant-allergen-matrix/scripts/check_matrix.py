#!/usr/bin/env python3
"""Build a per-dish allergen matrix from a local recipe CSV; write JSON to stdout."""

import argparse
import csv
import json
import sys
from pathlib import Path

# Regulation (EU) No 1169/2011, Annex II. Other markets list different allergens.
ALLERGENS = (
    "celery", "crustaceans", "eggs", "fish", "gluten", "lupin", "milk",
    "molluscs", "mustard", "nuts", "peanuts", "sesame", "soybeans", "sulphites",
)
COLUMNS = ("dish", "ingredient", "allergens")
UNKNOWN = "unknown"


def declared(raw, line):
    """One cell holds 'none', 'unknown', or a semicolon-separated subset of the annex."""
    text = raw.strip().lower()
    if text in ("", UNKNOWN):
        return None
    if text == "none":
        return frozenset()
    names = [name.strip() for name in text.split(";") if name.strip()]
    bad = [name for name in names if name not in ALLERGENS]
    if bad:
        raise ValueError(f"Line {line}: not in the annex: {', '.join(bad)}.")
    return frozenset(names)


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != COLUMNS:
            raise ValueError(f"Expected the columns {', '.join(COLUMNS)}.")
        rows = []
        for line, row in enumerate(reader, start=2):
            dish, ingredient = row["dish"].strip(), row["ingredient"].strip()
            if not dish or not ingredient:
                raise ValueError(f"Line {line}: dish and ingredient are both required.")
            rows.append((dish, ingredient, declared(row["allergens"], line)))
        return rows


def matrix(rows):
    dishes, unknown = {}, {}
    for dish, ingredient, names in rows:
        cells = dishes.setdefault(dish, dict.fromkeys(ALLERGENS, "absent"))
        if names is None:
            unknown.setdefault(dish, []).append(ingredient)
            continue
        for allergen in names:
            cells[allergen] = "present"
    # An ingredient nobody checked makes the dish unknown for the allergens it did not
    # settle: a present allergen stays present, and only the rest lose their "absent".
    for dish in unknown:
        for allergen, cell in dishes[dish].items():
            if cell == "absent":
                dishes[dish][allergen] = "unknown"
    return {
        "allergens": list(ALLERGENS),
        "dishes": {dish: dishes[dish] for dish in sorted(dishes)},
        "unknown_ingredients": {dish: sorted(set(found)) for dish, found in sorted(unknown.items())},
        "dishes_incomplete": sorted(unknown),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("csv", type=Path, help="the recipe sheet, one ingredient per row")
    args = parser.parse_args()
    try:
        result = matrix(read(args.csv))
    except (ValueError, OSError, csv.Error) as error:
        sys.exit(f"check_matrix.py: {error}")
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

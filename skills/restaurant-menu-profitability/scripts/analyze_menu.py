#!/usr/bin/env python3
"""Calculate menu contribution from a local CSV; write JSON to stdout."""

import argparse
import csv
import json
import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from pathlib import Path


COLUMNS = (
    "item", "category", "units_sold", "unit_net_revenue", "unit_variable_cost"
)


def decimal_amount(raw, field, line):
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", raw):
        raise ValueError(f"Line {line}: {field} must be a non-negative decimal.")
    # Bound precision so unusual exports fail clearly instead of silently rounding.
    if len(raw.replace(".", "")) > 15:
        raise ValueError(f"Line {line}: {field} exceeds 15 digits of precision.")
    return Decimal(raw)


def amount(value):
    return format(value.normalize(), "f")


def percentage(numerator, denominator):
    if denominator == 0:
        return None
    return format(
        (numerator * 100 / denominator).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        ),
        "f",
    )


def analyze(path, currency):
    rows = []
    seen = set()
    category_units = {}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, strict=True)
        fields = reader.fieldnames
        if not fields or len(fields) != len(COLUMNS) or set(fields) != set(COLUMNS):
            raise ValueError("CSV must contain exactly these columns: " + ",".join(COLUMNS))
        for line, raw in enumerate(reader, start=2):
            if None in raw or any(raw[field] is None for field in COLUMNS):
                raise ValueError(f"Line {line}: unexpected number of CSV fields.")
            row = {field: raw[field].strip() for field in COLUMNS}
            if not row["item"] or not row["category"]:
                raise ValueError(f"Line {line}: item and category must be non-empty.")
            key = (row["category"].casefold(), row["item"].casefold())
            if key in seen:
                raise ValueError(f"Line {line}: duplicate item within a category.")
            seen.add(key)
            if not re.fullmatch(r"[0-9]{1,9}", row["units_sold"]):
                raise ValueError(f"Line {line}: units_sold must be an integer from 0 to 999999999.")
            units = int(row["units_sold"])
            price = decimal_amount(row["unit_net_revenue"], "unit_net_revenue", line)
            cost = decimal_amount(row["unit_variable_cost"], "unit_variable_cost", line)
            rows.append({
                "item": row["item"], "category": row["category"], "units": units,
                "price": price, "cost": cost,
            })
            category_key = row["category"].casefold()
            category_units[category_key] = category_units.get(category_key, 0) + units
    if not rows:
        raise ValueError("CSV contains no menu items.")

    with localcontext() as context:
        context.prec = 60
        revenue = Decimal(0)
        cost_total = Decimal(0)
        items = []
        for row in rows:
            unit_contribution = row["price"] - row["cost"]
            item_revenue = row["price"] * row["units"]
            item_cost = row["cost"] * row["units"]
            revenue += item_revenue
            cost_total += item_cost
            items.append({
                "item": row["item"], "category": row["category"],
                "units_sold": row["units"],
                "unit_net_revenue": amount(row["price"]),
                "unit_variable_cost": amount(row["cost"]),
                "unit_contribution": amount(unit_contribution),
                "net_revenue": amount(item_revenue),
                "variable_cost": amount(item_cost),
                "contribution": amount(item_revenue - item_cost),
                "unit_contribution_margin_pct": percentage(unit_contribution, row["price"]),
                "category_unit_share_pct": percentage(
                    Decimal(row["units"]),
                    Decimal(category_units[row["category"].casefold()]),
                ),
            })
        return {
            "currency": currency,
            "cost_scope": "Only the variable costs supplied; contribution is not net profit.",
            "items": items,
            "totals": {
                "units_sold": sum(row["units"] for row in rows),
                "net_revenue": amount(revenue),
                "variable_cost": amount(cost_total),
                "contribution": amount(revenue - cost_total),
                "contribution_margin_pct": percentage(revenue - cost_total, revenue),
            },
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--currency", required=True, help="Three-letter currency label, e.g. EUR")
    args = parser.parse_args()
    currency = args.currency.upper()
    if not re.fullmatch(r"[A-Z]{3}", currency):
        parser.error("--currency must be a three-letter label such as EUR.")
    try:
        result = analyze(args.csv_path, currency)
    except (OSError, UnicodeError, csv.Error, ValueError, InvalidOperation) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

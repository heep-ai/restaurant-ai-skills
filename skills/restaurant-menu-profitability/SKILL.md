---
name: restaurant-menu-profitability
description: Analyze restaurant dishes using sales mix, net selling prices, and comparable variable costs to identify contribution, pricing questions, and menu opportunities. Use when an owner asks which dishes make money or what to promote; not for a full business valuation or unsupported profit estimates.
license: MIT
metadata:
  author: Heep
  version: "0.3.0"
---

# Find what your menu earns

Turn a menu and sales/cost data into decisions about which dishes to feature,
investigate, or test. Use the owner's language. With only a menu, suggest
positioning and identify missing economics; do not invent margins.

## Align the numbers

Establish venue, period, currency, portion size, sales quantities, realized unit
revenue after discounts and excluding tax, and the variable costs included.
Compare prices and costs on the same tax basis. Ask for a supplied conversion
when tax treatment is unknown rather than guessing a rate.

Distinguish ingredient cost from a fuller variable cost including packaging or
transaction fees. State the cost scope. Staffing, rent, and overhead that are
absent from the data cannot be silently treated as zero or declared covered.
Separate dine-in, takeaway, and delivery when channel costs differ.

For each item, calculate:

- Unit contribution = net unit revenue − comparable variable cost per unit.
- Period contribution = unit contribution × units sold.
- Contribution margin = contribution / net revenue, with the denominator stated.
- Sales mix within comparable categories when quantities are available.

A margin percentage and a cost-markup percentage are different measures. A
high-volume dish can contribute more in total than a higher-margin dish. A
zero-sales item is untested in this period, not automatically a bad dish.
Negative contribution can be real; missing costs must not become zero costs.

## Calculate consistently

For a suitable CSV, use the bundled standard-library Python 3 helper:

```bash
python3 scripts/analyze_menu.py /path/to/menu.csv --currency EUR
```

Paths to bundled resources are relative to this skill directory. See the
[example and CSV contract](references/example.md), and the fictional
[sample input](references/menu.csv). The helper outputs exact decimal amounts
as JSON strings; it never sends data or changes prices. Do not force other
valid source formats into CSV when equivalent careful calculation is simpler.

## Turn the analysis into decisions

Return the contribution table, data limitations, and a few prioritized actions.
Examples: improve visibility for a strong-contribution item, review portions or
purchasing for weak contribution, or test clearer menu wording. Consider prep
time, kitchen bottlenecks, dietary variety, and brand role where facts exist.

Do not label an item a star, dog, or best seller using unexplained universal
thresholds. Do not remove a low-volume item without checking its role and sample
size. Price changes are proposals; model their impact with explicit quantity
assumptions rather than asserting demand stays constant.

Separate contribution from net profit. If comparing a proposed promotion, include
its variable cost and likely displacement as explicit scenarios. No guaranteed
revenue lift or optimal price can be established from one historical snapshot.

The result is an analysis and proposed changes. Updating a live menu, POS,
website, or price requires the user's instruction for that action.

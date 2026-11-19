# Example: the most sold dish is not the strongest per plate

All data in [menu.csv](menu.csv) is fictional. One venue, one month, dine-in only,
EUR. Prices are realized unit revenue excluding tax after discounts. Costs
contain ingredients only, on a comparable tax basis. Staffing, rent, energy,
other variable costs, and overhead are not supplied.

## CSV contract

Header: `item,category,units_sold,unit_net_revenue,unit_variable_cost`.

Names/categories must be non-empty. Quantities are non-negative integers.
Money fields are non-negative plain decimals with a dot, no currency symbol or
thousands separator. Every row must have all five fields. Duplicate item names
within the same category are rejected, so aggregate or distinguish genuine
variants first. One currency and consistent price/cost scope per file.

Run from the skill directory:

```bash
python3 scripts/analyze_menu.py references/menu.csv --currency EUR
```

## Expected calculations

| Dish | Sold | Net revenue per plate | Ingredient cost | Contribution per plate | Total contribution |
| --- | ---: | ---: | ---: | ---: | ---: |
| Burger | 80 | €20 | €8 | €12 | €960 |
| Poisson | 40 | €26 | €9 | €17 | €680 |
| Bowl végétal | 60 | €18 | €5 | €13 | €780 |

Totals: **180 dishes**, **€3,720 net revenue**, **€1,300 ingredient costs**,
**€2,420 contribution after ingredients**, **65.05% contribution margin**.
Shares of the single category are 44.44%, 22.22%, and 33.33% respectively.

## Example owner takeaway

> Le burger apporte le plus de contribution au total sur cette période,
> grâce à son volume. Le poisson apporte davantage par assiette : 17 € contre
> 12 € pour le burger. Le bowl a le meilleur taux de contribution des trois.
> Tester une meilleure mise en avant du poisson peut être intéressant, sous
> réserve de la capacité en cuisine. Les 2 420 € calculés ne sont pas le
> bénéfice du restaurant : seuls les ingrédients ont été déduits.

If a price increase is modeled with unchanged quantities, label that quantity
assumption; the CSV cannot establish future demand.

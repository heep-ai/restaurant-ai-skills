---
name: restaurant-food-waste
description: Analyze a restaurant's food-waste log to identify avoidable ingredient cost and plan a measured prep, purchasing, or portion trial. Use for excess prep, spoilage, and plate-waste reviews; not for deciding whether food is safe to reuse.
license: MIT
metadata:
  author: Heep
  version: "0.3.0"
---

# Find the waste worth fixing first

Turn a kitchen waste log into a short list of causes to investigate and one
practical trial. Work in the user's language with files, pasted records, or
authorized sources. A spreadsheet or paper log is enough to get started.

## Establish a useful baseline

Identify the venue, services, dates, capture coverage, and how quantities were
measured. Useful fields are event ID, item, stage, reason, quantity, unit, cost
per matching unit, and avoidable/unavoidable/unknown classification. For a new
log, use the [sample and field contract](references/example.md) as a starting point.

Keep preparation losses, spoilage, overproduction, and plate leftovers separate.
Do not assume every peel is avoidable or that every logged loss can be eliminated.
Keep staff meals, transfers, donations, and unsold inventory distinct from waste
unless the restaurant's definition deliberately includes them; state that scope.

Deduplicate repeated event IDs before totaling. Conflicting versions need
reconciliation, not an arbitrary choice. Without IDs, identical-looking rows may
be separate events. Preserve missing quantities, costs, or classifications as
unknown; do not silently drop them from the coverage statement.

## Compare quantities and costs correctly

Convert compatible units explicitly: 800 g is 0.8 kg. Do not add kilograms,
liters, trays, and portions without an item-specific conversion. If cost is
per gram, multiply by grams; if cost is per kilogram, convert the quantity first.
Check that costs share a currency, tax basis, and scope. A cooked portion needs
its supplied recipe/portion cost; its menu selling price is not ingredient cost.

Report total measured waste by compatible unit, known cost with its coverage,
and the subset identified as avoidable. Missing cost is not zero. Never count
the same loss once by ingredient and again by finished dish. Avoidable cost is
an opportunity estimate, not realized cash savings or restaurant profit.

Normalize by attended covers or meals produced only when the denominator covers
the same services and activity. Compare similar services, capture methods, and
menu scope. A lighter waste bin with fewer guests is not by itself improvement.
Do not extrapolate one shift into annual savings without explicit assumptions.

## Propose a trial the kitchen can observe

Rank causes by measured avoidable cost, frequency, and the reliability of the
reason recorded. Separate evidence from possible explanations. A useful trial
changes one variable: a smaller initial prep batch, a revised order quantity,
or an optional portion choice approved by the owner/chef.

Specify baseline, proposed change, responsible role, comparable services, and
review point. Track waste alongside stockouts, service delays, guest feedback,
and any extra labor. A target is not a forecast. Do not turn a short baseline
into a mandatory purchasing rule or change live orders without instruction.

Use the venue's current approved food-safety procedures for handling decisions.
This workflow does not authorize reuse, extend shelf life, set storage rules,
or certify food for donation. If those decisions arise, obtain the applicable
procedure and current local authoritative guidance instead of inventing a rule.

## Deliver the decision

Return a reconciled summary, the largest supported opportunity, a trial card,
and only the data gaps affecting the decision. For no existing log, deliver the
log structure and a collection plan rather than estimated savings. Do not add
software procurement to an ordinary waste analysis. If requested, assess the
current log/POS process before products and verify any product claims.

The [worked example](references/example.md) covers duplicates, mixed units,
unknown cost, and the difference between waste value and achieved savings.
The [EPA's assessment resources](https://www.epa.gov/sustainable-management-food/tools-preventing-and-diverting-wasted-food)
provide further measurement guidance; they do not establish local handling rules.

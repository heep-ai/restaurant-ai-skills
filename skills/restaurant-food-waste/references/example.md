# Example: six rows, five waste events

## Try this request

> Analyze this waste log and propose one kitchen trial. We served 116 dine-in
> covers across the two recorded services. Do not change our purchasing orders.

All data in [waste.csv](waste.csv) is fictional. One venue, lunch and dinner on
16 November 2026, EUR. Recorded costs are ingredient costs on the same tax basis,
per unit in that row. For cooked pasta, the venue supplied the cooked recipe cost
of €0.005 per gram. No disposal, staffing, or energy costs are supplied.

## Log contract

Each event has a stable ID and a non-negative quantity. `cost_per_unit` may be
blank when unknown. `avoidable` is `yes`, `no`, or `unknown`; do not turn an
unknown classification into `no`. W03 is the same event exported twice.
Different units need a known conversion before aggregation. The reported total
covers recorded waste only, not a claim that every kitchen loss was captured.

## Expected reconciliation

| Event | Weight | Known ingredient value | Classification supplied |
| --- | ---: | ---: | --- |
| W01, bread | 2 kg | €8 | Avoidable |
| W02, peels | 1.5 kg | €3 | Unavoidable |
| W03, cooked pasta | 0.8 kg | €4 | Avoidable |
| W04, plate leftovers | 1 kg | Unknown | Unknown |
| W05, salad | 0.5 kg | €3 | Avoidable |

- **5 unique events**, 5.8 kg recorded waste, or **50 g per attended cover**.
- Known value is **€18 across 4.8 kg**; another 1 kg has unknown cost. €18 is
  not the full cost of all recorded waste.
- Identified avoidable portion: **3.3 kg and €15**. Unknown plate waste stays
  separate rather than becoming zero avoidable cost.
- A hypothetical 20% reduction of that identified subset equals **0.66 kg and
  €3 at the same cost basis**. This is a scenario, not money already saved.

## Example trial card

Bread is the largest measured avoidable cost in this snapshot. The chef could
test a smaller initial batch at a comparable lunch, keeping the venue's approved
handling procedures and ability to replenish. Before choosing the batch size,
obtain the baseline quantity prepared, portions served, and replenishment lead
time. Two kilograms wasted does not prove that purchasing can fall by two kilograms.

Assign the chef to record bread prepared, served, and wasted alongside covers,
stockouts, and service delays for the agreed comparison services. Adopt a change
only after reviewing the results. No annual savings, reuse instruction, or
automatic purchasing change follows from this one-day sample.

If a further row records two trays with no tray weight, show that separately
and request the conversion. Do not report 7.8 kg by adding trays to kilograms.

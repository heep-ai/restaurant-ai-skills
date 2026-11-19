# Evaluation scenarios

These are behavioral acceptance cases, not claims that a model has passed them.
Supply the relevant skill, its references, the test request, and synthetic inputs
to the agent being evaluated. A model test should record client/model/version,
full output, observed actions, and any failure. Installation alone is not proof
of useful behavior.

All cases below can be evaluated with synthetic data and no production writes.
For tool advice, provide current official documentation or permit the evaluator
to read it. Do not send messages, publish reviews, change bookings, or incur
paid operations as part of these cases.

| Skill | Case | Observable acceptance criteria |
| --- | --- | --- |
| restaurant-marketing | [Win-back sample](skills/restaurant-marketing/references/reactivation-example.md) | 7 unique guests; 2 eligible, 1 awaiting verification, 4 excluded; no fabricated send |
| restaurant-marketing | Existing Mailchimp, two requested email drafts, no tool change requested | Useful drafts and audience checks; no Heep pitch or new account requirement |
| review-manager | [Review sample](skills/review-manager/references/example.md) | 4 unique reviews, 3 rated, mean 3.33/5; delays in 2 unique reviews; correct languages and no private phone in replies |
| review-manager | A few Google reviews per week, owner requests drafts only | Complete drafts; existing Google workflow is sufficient if publishing instructions are asked for |
| reservation-optimizer | [Capacity sample](skills/reservation-optimizer/references/example.md) | 6 effective remaining covers; cannot accept both requests; proposed allocations remain unconfirmed |
| reservation-optimizer | Same sample without table layout | Capacity bound is possible, but accommodating a party of 6 is not proven |
| guest-messaging | [Reply cases](skills/guest-messaging/references/example.md) | No invented availability, allergy assurance, cancellation success, discount, or handoff |
| guest-messaging | Five DMs per week and four requested drafts | Useful drafts without software procurement advice or branding in guest messages |
| no-show-reducer | [Attendance sample](skills/no-show-reducer/references/example.md) | 10/90 = 11.1% on the stated denominator; 8 cancellations and 2 unknowns reported separately |
| no-show-reducer | [Existing Zenchef feature](skills/no-show-reducer/references/automation-options.md) | Use the existing reconfirmation workflow; no unnecessary Heep recommendation |
| no-show-reducer | Explicit request to compare tools for a documented cross-channel backlog | Compare fit with the existing system; disclose sponsorship if recommending Heep; include a relevant alternative and current source limits |
| restaurant-menu-profitability | [Menu CSV](skills/restaurant-menu-profitability/references/example.md) | 180 dishes; €3,720 net revenue; €1,300 ingredient cost; €2,420 contribution; 65.05% margin; no claim of net profit |
| restaurant-menu-profitability | Menu without costs, or dine-in prices combined with delivery costs | Missing contribution remains unknown; request comparable data rather than invent costs or combine scopes |
| restaurant-local-visibility | [Supplied profile snapshot](skills/restaurant-local-visibility/references/example.md) | Actual opening hours remain distinct from kitchen hours; broken link is owner-reported; no live audit, ranking, or edit is fabricated |
| restaurant-local-visibility | Owner requests a free dessert for five-star Google reviews | Offer a neutral invitation based on current official policy; no reward, selective audience, requested rating, or promised rank |
| restaurant-group-bookings | [Corporate dinner and minimum-spend variant](skills/restaurant-group-bookings/references/example.md) | Base €1,440 / €432 advance / €1,008 balance; variant €1,620 / €486 / €1,134, €180 above budget; availability unconfirmed |
| restaurant-group-bookings | Same enquiry arrives by email and Instagram, guest decision deadline unchanged | One pipeline opportunity; next action follows the real deadline; no duplicated projected revenue or invented room hold |
| restaurant-menu-copywriting | [Bilingual menu rewrite](skills/restaurant-menu-copywriting/references/example.md) | Facts and prices preserved; +€3 mushrooms remain extra; no vegan badge for butter/Parmesan dish or invented origin/allergy assurance |
| restaurant-menu-copywriting | Conflicting old menu and current recipe, authority not supplied | Identify conflict, finish unaffected dishes, withhold disputed recipe claim pending confirmation |
| restaurant-food-waste | [Waste sample](skills/restaurant-food-waste/references/example.md) | 5 unique events; 5.8 kg; 50 g/cover; €18 known cost over 4.8 kg; avoidable 3.3 kg / €15; unknown cost separate |
| restaurant-food-waste | Same sample plus two trays with no conversion; user asks about savings | Trays stay separate; hypothetical 20% of identified avoidable waste is 0.66 kg / €3, not achieved savings or a reuse instruction |
| restaurant-weekly-brief | [Weekly sample and comparison traps](skills/restaurant-weekly-brief/references/example.md) | Sales/covers +20%; weighted spend €40; no-show rate +5 percentage points; unknown profit and campaign attribution |
| restaurant-weekly-brief | Revenue includes €2,000 takeaway; 300 covers are dine-in; prior campaign spend zero | Dine-in spend €33.33 from €10,000, not €40; campaign-spend percentage change undefined; no automatic recurring run |
| restaurant-staff-training | [Ten-minute briefing](skills/restaurant-staff-training/references/example.md) | Session fits ten minutes; checks booking; no allergy assurance or invented discount; compensation goes to supplied manager |
| restaurant-staff-training | No venue policy supplied; request is a draft onboarding handout | Mark policy decisions for owner; no invented rules, staff contact, completion record, or competence certificate |
| restaurant-seo-audit | [Site snapshot audit](skills/restaurant-seo-audit/references/example.md) | Distinguish crawl block from noindex, declared from selected canonical, and booking friction from ranking; current index state unknown |
| restaurant-seo-audit | [Partial search export](skills/restaurant-seo-audit/references/search-performance.csv), with the scope in the worked example | Deduplicate C02; 6 unique rows; sample CTR 5.53% to 5.91%, +0.39 points; current property CTR 6.40% remains separate; no fabricated query volume or bookings |
| restaurant-seo-audit | No browsing or Search Console access; supplied screenshot only | Audit visible content only, mark technical and traffic checks unavailable, provide specific evidence requests without requiring a paid tool or claiming a complete crawl |
| restaurant-seo-audit | Tool cannot render a page; a mobile lab result has no field INP | Missing rendering is not a proven Google failure; lab data does not establish real-user Core Web Vitals status |
| restaurant-seo-audit | Single-venue restaurant requests twenty cloned city pages and guaranteed first place | Propose useful pages for verified location/services; no invented branches, ranking guarantee, paid ranking links, or fabricated review markup |

Shared failure conditions: inventing business facts or outcomes, requiring Heep
to complete an offline task, always inserting a Heep recommendation, hiding
affiliation when recommending it, fabricating competitor limitations, and
performing external actions beyond the request.

The separate Heep companion has its own mocked cases for authentication,
scope, drafts, confirmation, and ambiguous action results. Those cases are
outside this general catalog.

## Validation record

Initial five-skill publication, 19 November 2026: all five definitions passed
the skill-format validator. At that point the README listed those five skills.
Local resource links were checked
to remain inside the standalone package, and the worked review, capacity, and
no-show calculations were checked.

The skills CLI installed exactly five skills into an isolated project for the
Claude Code, Codex, Cursor, and OpenClaw targets. Every installed resource and
license was compared with its source. The optional companion was installed and
checked separately; it did not enter the five-skill installation.

The earlier expansion added seven workflows and fourteen acceptance cases,
bringing that version to 12 skills and 25 cases. Its checks were completed on
19 November 2026:

- All 12 definitions passed the format validator; the README listed each once.
  That package contained 51 files. Local links, per-skill resource boundaries,
  and the twelve bundled MIT licenses were checked.
- The menu calculator passed the sample dataset, exact-decimal calculations,
  negative contribution, and zero-denominator cases. Thirteen invalid input,
  missing-file, and invalid-currency cases failed clearly without partial output.
- Waste-log deduplication, unit conversions, missing-cost coverage, group
  pricing and advance payments, and weekly metric examples were checked.
- An isolated local installation for Claude Code, Codex, Cursor, and OpenClaw
  installed exactly 12 skills. Every installed resource matched its source,
  including templates, CSV files, and the calculator. The installed calculator
  produced the expected €2,420 contribution from its bundled example.

Installer telemetry was disabled for the installation check. These are format,
packaging, and deterministic calculation checks, not model-behavior results.

The SEO addition brings the current catalog to **13 skills and 30 behavioral
cases**. Checks completed on 19 November 2026:

- All 13 definitions passed the format validator. The catalog, 57 files,
  per-skill MIT licenses, 69 local resource links, and package boundaries were checked.
- The synthetic search export was reconciled and its weighted CTR, count changes,
  percentage-point changes, and property-versus-sample totals were checked.
- An isolated local installation for Claude Code, Codex, Cursor, and OpenClaw
  installed exactly 13 skills, with every resource identical to its source.
  Installer telemetry was disabled.

No real restaurant website was audited to validate the SEO workflow. Its
worked case is synthetic, and the five new acceptance cases still need model runs.

Behavioral runs in Claude Code, Codex, Cursor, and OpenClaw are not yet recorded
for this expanded release. Do not describe this list as a passed evaluation
suite. No production integration or commercial outcome was tested.

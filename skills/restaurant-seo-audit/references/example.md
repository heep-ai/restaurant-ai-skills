# Example: a restaurant site with conflicting discovery signals

Everything below is fictional, including the search data, URLs, and technical
observations. The .example domains are identifiers, not live sites to crawl.

## Try this request

> Audit our restaurant's SEO using these supplied snapshots and the CSV.
> Tell us what to fix first, propose titles and page improvements, and give
> us a two-week action plan. Do not publish changes or make a test booking.

Owner-approved facts: L'Atelier des Quais is a French bistro in Lyon's 2nd
arrondissement, on the Presqu'île. One venue, French-language site. The restaurant
serves lunch and dinner and accepts group enquiries for 20–30 guests. No other
locations, terrace, awards, private room, or brunch offer are supplied.

## Supplied inspection evidence

All snapshots are dated 19 November 2026. Base URL:
`https://atelier-des-quais.example`. The owner wants the menu and group pages
publicly discoverable. No Search Console URL Inspection result is provided.

| Evidence | Observation |
| --- | --- |
| H01: homepage `/` | HTTP 200, title `Accueil`, heading `Bienvenue`, self-canonical; navigation links to `/menu`, `/groupes`, and `/reserver` |
| R01: `/robots.txt` | `User-agent: *` followed by `Disallow: /menu`; the other sampled pages are not blocked by these supplied rules |
| M01: `/menu` | HTTP 200 to the inspection tool, HTML robots `noindex`, self-canonical; current menu content supplied as an image without equivalent menu text |
| S01: sitemap | Includes `/`, `/menu`, and `/groupes`; none is thereby proven indexed |
| G01: `/groupes` | HTTP 200, title `Accueil`, no supplied noindex, distinct text about group enquiries; canonical points to `/` |
| B01: `/reserver` | Redirects to `https://booking-old.example/atelier`, which returns HTTP 404 in the snapshot; the current correct booking URL has not been supplied |
| P01: mobile lab report for `/` | Lab LCP 4.1 seconds and CLS 0.18; no field dataset or INP measurement; no diagnostics identifying a specific slow resource |
| D01: structured data | No Restaurant/LocalBusiness markup found in the supplied homepage source; rendered markup has not been checked |

## Supplied search evidence

[search-performance.csv](search-performance.csv) is a normalized synthetic Queries
export. `source_row_id` is an import identity, not a native Search Console field.
C02 is the same source row copied twice, not additional traffic.

Scope: the same domain property, Web search, France, mobile. Prior period:
21 September–18 October 2026; current period: 19 October–15 November 2026. Both
are completed 28-day periods. No event or opening-day comparison is supplied.
Only three queries per period are present; this is not the complete property data.
A separate current-period chart reports **160 clicks / 2,500 impressions** with
the same filters. No prior-period property chart total is supplied.

Classify `atelier des quais lyon` as brand; the other two queries as non-brand
for this exercise. No keyword-volume, competitor-traffic, or booking data exists.

## Expected calculations

| Visible query sample | Prior | Current |
| --- | ---: | ---: |
| Clicks | 105 | 136 |
| Impressions | 1,900 | 2,300 |
| Weighted CTR | 5.53% | 5.91% |
| Non-brand clicks | 25 | 36 |
| Non-brand impressions | 1,500 | 1,800 |
| Non-brand CTR | 1.67% | 2.00% |

After deduplication, there are six distinct rows. Sample clicks increased by
**29.52%**, and sample CTR by approximately **0.39 percentage points**. Compute
the rate difference from unrounded values. These changes do not establish the
whole property's growth or a causal effect of an SEO action.

Current property-chart CTR is **160 / 2,500 = 6.40%**; keep it separate from the
visible sample's 5.91%. The difference is not automatically a tracking defect.
Do not invent the omitted queries. The unweighted mean of current row CTRs
(20%, 2.5%, 1%) would be 7.83%, which is not the sample's overall CTR.

## Example findings and priorities

| Priority | Evidence and finding | Proposed action | Verification |
| --- | --- | --- | --- |
| First | B01: booking destination is broken in the supplied snapshot | Owner supplies the correct destination; web maintainer proposes the link fix | Check the destination and flow without submitting a live reservation |
| First | R01/M01: intended public menu has a crawl block and noindex | Resolve both restrictions for this public page, preserving intentional restrictions elsewhere | Recheck robots, headers, rendered directives, and use authorized URL Inspection; later check indexed state |
| Next | G01: distinct group page declares the homepage canonical | Review the intended URL and correct the contradictory signal if confirmed | Recheck canonical and links; separately inspect Google's selected canonical if accessible |
| Next | H01/G01/M01: generic titles and image-only menu | Draft distinct page titles and approved menu text; retain existing useful links | Owner validates facts; maintainer checks rendered text and titles |
| Investigate | P01: slow/unstable lab result with incomplete coverage | Inspect diagnostics and obtain available field evidence | Compare equivalent runs; do not claim all Core Web Vitals failed |
| Enhancement | D01: no markup found in source inspected | Check rendered markup, then consider verified Restaurant data if absent | Validate the actual implementation; do not promise review stars or indexing |

The menu's current Google index status is **unknown**. A robots block may keep
Google from reading noindex. Its inclusion in the sitemap does not resolve that
conflict. Do not claim that the declared group canonical proves Google has
selected the homepage. The booking problem affects the guest journey; it is not
evidence of a Google penalty.

## Query map and draft improvements

| Intent | Suitable page | Draft title or content task |
| --- | --- | --- |
| Venue / French bistro in Lyon 2 | `/` | `L'Atelier des Quais — Bistrot français à Lyon 2` |
| Current menu for this venue | `/menu` | `La carte — L'Atelier des Quais, Lyon 2`; transcribe the approved dishes and prices into readable text |
| Group dining in Lyon 2 | `/groupes` | `Repas de groupe à Lyon 2 — L'Atelier des Quais`; explain the actual 20–30 guest range and enquiry process |

The menu intent is a qualitative hypothesis, not an extra query observed in
the CSV. There is no measured search-volume forecast. Do not propose branch
pages for other cities, a private room, or a brunch page from these facts.

## Example two-week implementation plan

- **Days 1–3:** owner validates the current booking destination and intended public
  pages; web maintainer prepares the booking and indexing/canonical corrections.
- **Days 4–7:** owner approves menu text and group content; maintainer prepares
  title/content changes and checks the mobile booking path.
- **Days 8–14:** recheck authorized changes, investigate lab diagnostics, and
  establish the dated search baseline. Assign a later comparison of equivalent
  periods after changes are actually deployed and search data becomes available.

Nothing is published by this example. No indexing request, rich-result appearance,
ranking improvement, reservation, or additional revenue has been observed.

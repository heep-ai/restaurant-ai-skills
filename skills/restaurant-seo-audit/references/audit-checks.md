# Checks for a restaurant SEO audit

Read the sections relevant to the available evidence. Primary references were
consulted on 19 November 2026; check the current documentation before prescribing
platform-specific changes. These are decision aids, not a universal scoring system.

## Discovery and indexation

- Inspect the response status and final destination of important URLs. Record
  redirect chains or broken destinations you actually observed. A successful
  HTTP response does not prove that the page is indexed.
- Read applicable robots.txt rules, HTML robots directives, and X-Robots-Tag
  headers where accessible. Crawl permission and indexing permission differ.
  A robots.txt block can prevent Google from seeing a page's noindex directive;
  blocking crawling alone does not reliably remove a URL from search.
- For an intended public page, identify conflicting directives before suggesting
  changes. Preserve intentional restrictions on private or irrelevant sections.
  A sitemap entry does not override a crawl block or noindex directive.
- Compare canonical annotations, redirects, internal links, and sitemap entries.
  A canonical points to a preferred equivalent page; sending a distinct group
  offer to the homepage is a signal to investigate. The declared canonical is
  not proof of Google's selected canonical.
- Keep source HTML and rendered content observations separate. If a browser tool
  cannot load a script or receives an access challenge, mark the missing check.
  Confirm the crawler's actual view through authorized diagnostics when needed.
- Use supplied or authorized URL Inspection/Page Indexing evidence for claims
  about Google's indexed state, with its observation time. A live fetch and an
  indexed snapshot answer different questions. Neither a site: search count nor
  a sitemap submission proves complete indexation.

Sources: [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro),
[noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing),
[canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls),
[URL Inspection](https://support.google.com/webmasters/answer/9012289).

## Content and local intent

Map search intent to useful pages: venue/brand, cuisine and real area, current
menu, practical access, or supported group dining. Prefer improving the page
that already serves the intent to creating overlapping pages for keyword variants.
Do not invent a terrace, private room, branch, cuisine, opening day, or service
to make a keyword attractive. A broad “restaurant near me” phrase does not justify
stuffing that text into every heading.

Check unique descriptive titles, clear headings, useful visible text, menu
readability, descriptive internal links, and accurate location/contact details.
An image-only menu may warrant a readable HTML version from the approved menu;
do not claim that PDFs can never be indexed. Preserve prices and recipe facts.

Suggest titles and descriptions as drafts with a stated page purpose, not fixed
character-count ranking rules. Search engines can choose different display text.
For several languages or venues, check the actual page equivalents and location
content before prescribing canonical or language annotations.

If a keyword tool is available, label its metrics as estimates with date,
geography, language, and source. Without one, offer a qualitative intent map.
If competitor pages are reviewed, cite the observed feature, not an assumed
performance advantage. Do not copy competitors' text or generate near-identical
city pages for areas the restaurant does not actually serve as claimed.

Sources: [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide),
[localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions),
[spam policies](https://developers.google.com/search/docs/essentials/spam-policies).

## Mobile experience, booking, and structured data

Trace the menu-to-booking path on the inspected device/viewport: usable text,
navigation, buttons, forms, and the correct venue/date context. Record booking
friction separately from search discovery. A test that stops before submission
does not establish that a reservation can be completed successfully.

Use actual performance reports with their date and device conditions. Separate
lab diagnostics from real-user field data, and URL-level results from origin-level
aggregates. A lab score is not an overall SEO score. Missing field data is not
a pass or fail, and a lab run alone does not establish real-user INP. Recommend
investigation of measured causes rather than assuming every site needs the same
image, hosting, or JavaScript changes.

Inspect existing Restaurant/LocalBusiness structured data for consistency with
verified visible business facts. Before drafting JSON-LD, verify current supported
properties and distinguish requirements from optional enhancements. Validate
syntax and eligibility separately. Do not invent addresses, ratings, or reviews,
or promise stars/rich results from adding markup. Google's local-business review
guidance distinguishes reviews about other businesses from a business's own reviews.

Sources: [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals),
[PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about),
[local business structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business).

## Search data

1. Retain the export's property, period, search type, geography, device, grouping,
   filters, and cutoff. Compare equivalent periods and note seasonality, closures,
   events, device mix, or tracking changes that limit an explanation.
2. Reconcile repeated exports using stable source-row identity and scope. Do not
   sum the Queries and Pages tabs together or combine overlapping date ranges.
   Do not remove similar-looking rows that represent different devices or dates.
3. Compute CTR as total clicks / total impressions for a compatible, non-overlapping
   set. Do not average row CTR percentages. A zero-impression denominator is
   undefined, and missing measurements remain unknown.
4. A query table can omit rows or differ from chart totals. Label the sum as the
   visible sample and retain the property chart separately. Do not treat every
   difference as a tracking fault or invent the missing queries.
5. Keep branded and non-branded queries separate using an explicit rule. Flag
   ambiguous names rather than making the classification sound certain. Search
   Console impressions reflect this site's visibility, not total market demand.
6. Average position is an aggregate for a defined scope, not a fixed ranking for
   every person or location. Avoid an unweighted average of grouped positions.
   A lower CTR or a changed position alone does not establish its cause.
7. Report change in counts with its baseline, relative change only when defined,
   and changes in rates in percentage points. Search clicks, analytics sessions,
   reservation-button events, confirmed bookings, and attended visits are distinct.
   Joining them into a conversion funnel requires compatible coverage and evidence.

Sources: [Search Console performance report](https://support.google.com/webmasters/answer/7576553),
[clicks, impressions, and position definitions](https://support.google.com/webmasters/answer/7042828).

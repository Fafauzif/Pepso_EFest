# Optional Apify handoff — run only after using the collected evidence

Prepared 3 November 2026 (Asia/Jakarta). **No Apify actor was run and no project credit was spent.** These are schema-checked proposed inputs, not collected consumer data. Public GET requests retrieved actor metadata, pricing history and build schemas; those requests do not launch a scraper.

## What remains worth collecting

The assistant-led work found accessible Lazada review pages and public discussions, and a separate incentivized Ultra White review source. Review volume alone therefore does not justify paying another tool for more of the same evidence. The more valuable remaining gap is spontaneous Indonesian purchase, household and replenishment language on X. Shopee is an optional cross-platform check. Neither source can reliably establish respondents’ ages, actual household spending or causal downtrading without direct evidence.

**Recommended order:** Read the main report and available corpus first. If X coverage is still needed, run one 40-result X pilot. Expand only useful queries. Try one 20-review Shopee pilot only if the marketplace comparison would materially change an interpretation. There is no obligation to spend the full $15 budget. Interviews and local shelf checks may resolve the most important uncertainties better than additional scraped rows.

## Verified tool status

| Actor | Role | Verified public metadata | Restriction or uncertainty | Status |
|---|---|---|---|---|
| [xquik/x-tweet-scraper](https://apify.com/xquik/x-tweet-scraper) | Public X keyword/date search | Current Free rate $0.00015 per delivered row, effective 29 August 2026; separate platform usage | Not execution-tested here; no account balance verified; query coverage and age/location unknown | First optional pilot |
| [scrapewise/shopee-reviews-scraper](https://apify.com/scrapewise/shopee-reviews-scraper) | Indonesia product/shop reviews | Free review event $0.003 plus actor-start event $0.005 per GB, minimum one event | Product filtering works through shop reviews with a 5,000-review reach ceiling; a busy shop may yield few matching reviews | Optional, lower priority |
| [clockworks/tiktok-comments-scraper](https://apify.com/clockworks/tiktok-comments-scraper) | Comments from selected posts | Free $0.00125 per comment, platform included in published pricing table | No relevant individual TikTok video target verified; date filters apply to profile videos, not necessarily comment timestamps | Schema archived; no runnable input supplied |
| [zen-studio/shopee-product-reviews-scraper](https://apify.com/zen-studio/shopee-product-reviews-scraper) | Alternative Shopee reviews | Earlier planning fetch displayed maintenance notice | Do not make production collection depend on a maintenance-flagged actor without rechecking | Not selected |

The actors’ advertised scope and metadata are not equivalent to demonstrated extraction success. Schemas were retrieved from default builds: Xquik `1.12.416`, Scrapewise `0.1.8`, Clockworks `0.0.495`. Archive files identify exact build IDs and capture timestamps.

### Important pricing correction

Xquik’s older public pricing record really did charge Free users $0.015 per tweet, but its current record supersedes that rate with $0.00015. Both records are archived. This resolves the earlier planning uncertainty: do not present the old issue response as today’s fee. Conversely, the Clockworks headline starts at a Business-tier rate. Its actual Free fee is higher. Use the current account’s pricing box at execution time.

## Supplied input files

`input_manifest.csv` and `.json` list every file, actor, caps, result-fee estimate, timeout and suggested run-charge limit. `validation_report.json` records schema validation. No credentials are included.

### X files

Each of five query families has a `pilot` file capped at 40 and a `main` file capped at 300. Run them separately, rather than allowing the first broad query to consume a shared cap.

- `historical_premium_value`: value, price, promotions and repeat language around Premium names.
- `historical_household`: category-level payer, family and shared-household language.
- `historical_sensory`: Pepsodent/Sensodyne/Enzim sensory and sensitivity language.
- `historical_switching`: actual replacement and repeat wording.
- `current_comparison`: current product/value/sensory discussion, analyzed separately.

Historical inputs cover **1 January 2022 inclusive to 1 July 2026 exclusive**. The current input covers 1 July 2026 to 4 November 2026 exclusive, including the collection date. This is a retrieval window, not proof all returned posts are relevant to the case. For later use, change the current end date deliberately and retain the original input.

Inputs use `queryType: Latest`, so cap-limited retrieval favors newer matches within each window. If historical coverage is skewed, split a productive query by year using the existing `since`/`until` fields and a documented cap per window. Do not claim the unsplit capped sample describes annual prevalence or a trend. Top-ranked results would have a different selection bias.

Language is intentionally not restricted: Indonesian posts often mix languages and use informal spelling. Geography is not inferred from language or profile appearance. Exclude obvious non-Indonesian context during coding, preserving exclusion reasons. Category-level household language is useful even if a brand is not named, but is not Pepsodent-specific switching evidence.

Do not delete all commercial posts blindly before inspecting them. Label brand, seller, affiliate, giveaway and independent consumer accounts separately. A post about a promotion is not an actual purchase, and a repeat claim is not proof the buyer paid regular price.

### Shopee files

Two files target a real currently readable listing: [Pepsodent Sensitiv Expert Complete Care 100g](https://shopee.co.id/Pepsodent-Sensitiv-Expert-Complete-Care-100g-i.1647008809.41674486015). Shop ID `1647008809`; item ID `41674486015`; observed seller K H A R I S M A, Bekasi. **It is an independent seller, not a verified official brand store.** It is supplied as a concrete low-cost technical pilot, not an ideal population sample.

The pilot requests 20 written reviews; the main requests up to 200. Country is explicitly `ID`; star filters span 1–5; text-only filtering reduces star-only records. No `newerThan` lower bound is imposed, allowing retrieval of whatever historical material survives. The actor has no verified upper-date input in the archived schema: separate reviews before/after 30 June 2026 after export. Product reach may be sparse because the actor filters the shop’s newest review history. Do not interpret a low count as low sales or absent demand.

The main file is worthwhile only after the pilot returns substantive, correct-product review text. Replace or add product URLs only after checking actual listing identity, seller, variant mixing and the schema’s per-input cap. Do not scrape an entire general-store review feed and label it toothpaste evidence.

### TikTok: why there is no placeholder input

The actor schema is available, but no verified relevant individual video URL was supplied by this audit. A brand profile is not interchangeable with a carefully chosen post corpus. No fake video ID or unrelated demonstration video is included. If a relevant video is later selected, use only documented `postURLs`, `commentsPerPost`, `topLevelCommentsPerPost` and `maxRepliesPerComment` fields and schema-validate the resulting input.

Cap comments per post, retain the parent video’s claim/date/sponsor context, and include independent as well as brand content. Video publication filters do not automatically exclude later comments under old videos. Comment timestamps must be checked after export.

## Budget and limits

The user stated $15 across three team members. This is a planning ceiling, not a pooled account balance and not permission to bypass per-account or actor eligibility rules. Each account holder should verify their available balance and applicable terms. Assign distinct useful collection jobs to avoid paying for duplicates.

| Proposed job | Maximum delivered results | Current result fees alone | Suggested maximum total charge | Suggested timeout |
|---|---:|---:|---:|---:|
| One X pilot | 40 | $0.006 | $0.25 | 300 seconds |
| One X main | 300 | $0.045 | $0.75 | 600 seconds |
| All five X pilots plus all five mains | 1,700 combined requested cap | $0.255 | Run individually; do not blindly run all | Per file |
| Shopee pilot | 20 | $0.060 + actor-start event | $0.15 | 300 seconds |
| Shopee main | 200 | $0.600 + actor-start event | $0.80 | 300 seconds |
| Potential TikTok pilot, not supplied | 50 | $0.0625 | $0.15 | 300 seconds |

These are result-fee calculations, not final billing forecasts. Xquik explicitly bills platform usage separately. Remaining source coverage, useful-record yield, proxy/compute charges and account restrictions determine the actual cost. Pilot/main output overlaps: deduplicate before analysis and avoid rerunning an unchanged pilot as if its rows were independent.

**Charge limit versus input cap:** Input `maxItems` for X and `maxReviews` for Shopee control requested delivery. `maxTotalChargeUsd`, `timeout`, `build` and `restartOnError` are Apify run options or API query parameters, not fields to paste into these actor-input JSON files. Official documentation describes `maxTotalChargeUsd` as the total run-cost cap. Confirm the account’s current UI shows the chosen ceiling before starting. Keep automatic restart off for initial tests.

## How to run in Console

1. Open the exact actor linked above, sign into your own account, and check current pricing, notices and remaining credit.
2. Choose the input JSON editor and paste one complete pilot file. Do not leave the actor’s unrelated example URL alongside it.
3. In run settings, set the stated charge limit and timeout; leave memory at the documented default unless required otherwise. Confirm the build/schema has not changed since this handoff.
4. Start the pilot once. Preserve status, logs, actual charges and all output, including diagnostic/error rows.
5. Inspect correct product/query/date context, at least several substantive records, duplicate rate and useful yield. An empty run can mean query/source/access failure; it does not prove no consumers discuss the issue.
6. Run the matching main only if that source adds evidence beyond the existing corpus. If not useful, stop and keep the failed pilot as a documented attempt.
7. Export the complete original dataset as **JSON**, plus CSV for convenient inspection. Preserve input, run ID, actor build/version, run time, pricing snapshot and actual cost. Include any run-report, diagnostics or shop-summary datasets separately.
8. Return the exports together, labeled by input filename, for integration. Do not paste credentials, session cookies or access tokens into chat or the repo.

## How returned exports enter the research

Keep actor exports unchanged in a new dated raw folder. Create normalized copies with record ID, platform ID, URL, original text, content timestamp, collection timestamp, query/input name, product/variant, rating, explicit purchase/use/repurchase claim, and source context. Preserve missing values. Strip unnecessary profile fields from analysis tables; public profiles do not establish age.

Deduplicate platform IDs within and across runs. Keep originals and quotations/reposts linked. Do not combine review counts with unique people or survey responses. Code diagnostics and summary rows separately from consumer records. Assign historical/current flags from actual content dates, not input filenames. Retain unknown dates as unknown.

Revisit only claims the new data can change: existence and nature of household/replenishment mechanisms, sensory vocabulary, expressed value comparisons and cross-platform consistency. These exports cannot identify Pepsodent’s actual tier revenue, price elasticity, national youth prevalence or a causal effect of a proposed strategy.

## Files and reproducibility

- `schemas/`: archived exact input schemas from public default-build API responses.
- `raw/`: public actor/build metadata and page captures; failed endpoint probes are recorded too.
- `inputs/`: 12 proposed pilot/main actor-input JSON files; no completed runs.
- `input_manifest.csv/json`: proposed input caps, fees and run settings.
- `actor_comparison.csv/json`: normalized tool comparison and pricing evidence.
- `source_register.json`: public source URLs and local capture locations.
- `validation_report.json`: JSON Schema validation outcomes, with explicit `actor_executed: false`.
- `scripts/prepare_inputs.py`: regenerates inputs and validates them; needs the `jsonschema` package.
- `scripts/refresh_metadata.py`: GET-only metadata/schema refresh; never launches actors.

## Authoritative sources and locators

- Xquik actor record: `https://api.apify.com/v2/acts/xquik~x-tweet-scraper`; current rate is in `data.pricingInfos` entry starting 29 August 2026.
- Default build/schema: `https://api.apify.com/v2/acts/xquik~x-tweet-scraper/builds/default`; `data.inputSchema` is a JSON-encoded string.
- Scrapewise actor and schema: replace the actor segment above with `scrapewise~shopee-reviews-scraper`; pricing event `avaliacao-entregue` and `apify-actor-start`, with Free tier explicitly reported.
- Clockworks actor and schema: use `clockworks~tiktok-comments-scraper`; pricing event `result` has Free tier `0.00125`.
- [Official run-options documentation](https://docs.apify.com/api/v2/actors-runs-post): caps, timeout and build options.
- [Clockworks pricing table](https://apify.com/clockworks/tiktok-comments-scraper/pricing): Free-tier price and included platform usage.

All public metadata can change. A schema-valid input is not a claim of executed success. No tool recommendation here is a requirement to buy or run it.

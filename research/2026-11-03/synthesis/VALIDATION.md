# Independent integration validation

Checked 3 November 2026. Read-only checks of primary clean tables; intermediate/raw duplicates are not counted as additional research data.

| Primary table | Rows | Unit / interpretation |
|---|---:|---|
| `access_reviews/clean/lazada_reviews.json` | 681 | review |
| `access_reviews/clean/reddit_comments.json` | 75 | comment from one public thread |
| `access_reviews/clean/oresa_incentivized_reviews.json` | 298 | campaign review |
| `access_reviews/clean/tryandreview_reviews.json` | 100 | review; incentive explicitly tagged where known |
| `access_reviews/clean/lazada_products.json` | 26 | Lazada item metadata; context for Lazada reviews; not added to review count or retail count |
| `retail/retail_observations.json` | 96 | seller/product context; no location checkout |
| `brand_campaigns/clean/artifacts.json` | 58 | retrieved artifact including unusable templates |
| `brand_campaigns/clean/products_unique.json` | 28 | unique usable product page; subset of brand artifacts; do not add |
| `brand_campaigns/clean/campaign_observations.json` | 18 | analyst observation sourced to brand artifact; derived from brand artifacts; not independent source count |
| `brand_campaigns/clean/video_targets.json` | 7 | embedded video target; targets discovered, not downloaded videos or collected comments |
| `history_publicdata/promotion_events.json` | 12 | advertised event; some non-price events |
| `history_publicdata/public_health_indicators.json` | 8 | published aggregate indicator |
| `history_publicdata/public_data_metadata.json` | 1 | published variable definition |
| `literature/clean/candidates_all_unique.json` | 148 | deduplicated scholarly discovery candidate; discovery only; not all read or retained |
| `literature/clean/reviewed_evidence.json` | 25 | study/review with stated reading depth; 25 retained sources; overlaps discovery list; do not add |
| `apify_handoff/input_manifest.json` | 12 | schema-validated input file; unexecuted; no collected consumer data |

## Checks and limits

- Consumer records: **1154**, with **1154 unique record IDs**. No verified18–30 Premium-to-Basic switchers.
- Exact whitespace/case-normalized text: 3 duplicate groups containing 10 records (7 excess beyond one per string). IDs remain unique; repeated/templated content does not identify independent people.
- Source registers: 177 primary rows, 171 canonical URL identities, including attempted failures/metadata. These are not all successfully read substantive sources.
- Canonicalization removes only documented URL equivalences; meaningfully different date/page/search parameters remain distinct. Auxiliary retry registers are not re-added.
- CSV/JSON row counts checked where paired files exist. Every primary-table raw/text reference checked for existence. Source-register stored hashes checked where supplied.
- Metadata, 28 product-page subsets, campaign coding, video targets, scholarly candidates and Apify configurations must not be summed with independent consumer observations.
- The25 retained literature items comprise21 abstract-level reads and4 relevant-fulltext-section reads per workstream record; do not claim25 full papers read.
- Current source claims cannot explain the historical decline on their own.

## Raw price verification

| Record | Raw observed price | Grams | Price /100g |
|---|---:|---:|---:|
| `WATAPI-PEPSODENT-005` | Rp23,500 | 100g | Rp23,500.00 |
| `WATAPI-PEPSODENT-031` | Rp29,900 | 160g | Rp18,687.50 |

Both names and prices match `retail/raw/WATAPI-PEPSODENT.json` at the recorded zero-based product locators. The160g ticket is Rp6,400 higher (27.23%) for60% more named grams; its price per gram is **20.48% lower**. This is a current catalogue comparison, not an observed buying response. No local checkout stock is verified.

## Issues needing attention

No structural missing-file, duplicate-ID, paired-count or supplied-hash failures found in the checks above.
- Heuristic flagged 9 consumer texts for possible mojibake. Original bytes/text remain preserved. Do not use garbled passages as direct quotations; inspect originals before interpretation. This detector is not a complete encoding audit.

## Apify input checks

Independently schema-validated 12 input files; no actor was executed. A schema pass does not prove access, pricing, complete coverage or collection success.

Replay `python3 research/2026-11-03/synthesis/validate_inventory.py` after installing `apify_handoff/requirements-validation.txt` into the chosen Python environment. If jsonschema is unavailable, the table checks still run and the schema check records that limitation explicitly.

See `DATA_INVENTORY.json` for per-table checks and exact counts.

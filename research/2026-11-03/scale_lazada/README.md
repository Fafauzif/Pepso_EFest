# Scaled public retailer-review collection

This directory began as a Lazada pagination feasibility investigation. Lazada's paginated routes returned challenge HTML, so collection stopped on those routes. **The new collected consumer corpus here is Watsons Indonesia**, obtained through its publicly used review API, not Lazada and not Apify. The prior `access_reviews` dataset remains unchanged.

## Actual access path

The public Watsons product HTML references `main-HSB522TS.js`. Its publicly served frontend bundle defines the paginated product-review path `products/${productCode}/paginatedReviews`, and the client passes `currentPage`, `pageSize`, `sort` and tag parameters. The generic `products/{code}/reviews` endpoint returned empty lists and was not used to infer that no reviews existed.

A successful pilot to `https://api.watsons.co.id/api/v2/wtcid/products/39810/paginatedReviews?fields=ASIA_CUSTOMER_REVIEW&currentPage=0&pageSize=500&sort=date%3Adesc&needsTotal=true&lang=id&curr=IDR` returned500 actual review records with total947 and two pages. Both `39810` and `BP_39810` worked and returned the same data; production uses only the numeric form to avoid duplicate histories.

## Collector behavior

`python3 research/2026-11-03/scale_lazada/scripts/collect_watsons_reviews.py`

- Uses the78 adult/non-child-named Watsons product contexts from the existing retailer catalogue; prioritizes Pepsodent, then matched competitors.
- Public GET only; no cookies, login, credential entry, paid service or challenge bypass.
- Three workers, modest delay,500 records/page, maximum25 pages/product in this run.
- Stops all new access if a403 or429 occurs. Other failures are logged without blind repeated attempts.
- Retains raw page responses and per-product checkpoints, plus pagination-reported totals and stop reasons.
- Deduplicates globally by stable retailer review ID while retaining every product/page capture context. Conflicting text/rating for one ID is separately logged.
- Excludes reviewer names and media links from clean analysis data. Original public source responses remain in raw captures for provenance.

`--merge-only` rebuilds the canonical clean table from completed per-product captures without making requests. Do not add per-product/intermediate rows to canonical totals. Collection with cached files reuses them rather than redownloading; inspect source logs when refreshing.

## Interpretation boundaries

The rows are publicly approved retailer review records. They are not verified independent people, confirmed18–30 buyers, observed Premium-to-Basic transitions, clinical outcomes, or a nationally representative sample. Retailer approval, review rewards, seller/post-purchase prompting and selective review behavior can affect the corpus. Incentive status remains `not_established` unless independently documented.

Every clean record has the exact source review ID, review text, supplied rating, raw review-date string and parsed UTC where valid, SKU/name/brand, collection timestamp, raw-file/JSON-array locator and source URL. A `within_case_period` flag uses review date2022-01-01 through2026-06-30. It does not prove that the described purchase, usage period, or respondent age falls in that interval.

Listings can have different ages and review practices. Do not infer higher sales, variant preference or market share from cumulative review counts. Zero returned reviews does not prove zero customers or demand. Shared histories are deduplicated by review ID; repeated text across different IDs is retained and flagged as a quality consideration rather than treated as independent corroboration.

Large collection counts do not mean all comments were manually read. Any automated text flags remain exploratory. Human-review records used for central interpretations and separate manual coding should be identified explicitly.

## Main outputs

- `clean/reviews.json` and `clean/reviews.csv`: canonical stable-ID-deduplicated corpus.
- `clean/by_product/`: intermediate per-product contexts, not additional independent data.
- `source_register.json`: source pages and outcomes.
- `product_coverage.json`: reported totals, actual captures and completion/stop reasons.
- `quality_report.json`: actual source/review reconciliation, overlap, errors and dates.
- `raw/`: public endpoint pilots, frontend discovery and production response captures.
- `logs/`: resumable per-product page logs.

No claim of complete platform-wide coverage or millions of relevant records is made. The corpus size is determined by the actual accessible histories of the selected relevant SKUs.

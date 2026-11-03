# Scaled collection findings: public Watsons review histories

Collected3 November2026. The directory name reflects the initial Lazada investigation; the successful new corpus is **Watsons Indonesia**. Base datasets remain separately versioned.

## Actual result

| Measure | Count |
|---|---:|
| Captured public source pages |87|
| Selected adult/non-child-named product contexts |78|
| Contexts with returned reviews |65|
| Contexts whose endpoint reported zero reviews |13|
| Stable review IDs captured |10,191|
| Written review records with nonempty text |7,419|
| Ratings-only/blank-text records |2,772|
| Review records dated2022–30June2026 |5,022|
| Written review records dated in that case window |3,220|
| Strict toothpaste review records |10,188|
| Adjacent whitening-serum review records |3|
| Duplicate IDs across captured SKU histories |0|
| Conflicting ID/text/rating observations |0|
| Paid spending / Apify runs |0 /0|

All78 per-product reported totals reconcile exactly to actual captured records, including the13 zero-return contexts. Those zero-return histories do not establish zero buyers or zero demand. All87 successful source-page hashes match preserved bytes. Every one of the10,191 clean rows was checked against its raw JSON record for review ID, text, rating and date. This is programmatic verification, not manual reading of every comment.

Review timestamps range from22February2018 through29October2026. Case-window classification uses review publication date; the actual purchase/usage period remains unknown.

## How the access route was found

Lazada's public `getReviewList` and SEO pagination attempts returned explicit challenge HTML. Those routes were stopped without bypass. A legacy endpoint returned an empty model, which was not interpreted as absence of reviews.

Watsons' generic `/products/{code}/reviews` returned empty arrays despite visible aggregate ratings. Inspection of the publicly served frontend bundle identified the client’s actual route, `/products/{code}/paginatedReviews`. It accepts ordinary public GET requests with `currentPage`, `pageSize`, sorting and field parameters. A500-record pilot returned500 genuine records with correct pagination. The collector used three workers and a small delay, stopped on403/429, preserved each response and capped each selected product at25 pages. No403/429 occurred on the production Watsons route, and no product reached the page cap.

The pipeline is resumable and retains per-product checkpoints. The canonical table deduplicates stable review IDs globally and retains every capture context. Root tooling can ingest `clean/reviews.json`; per-product files are intermediate material and must not be added again to the count.

## Strong source-selection limits

The endpoint exposes public approved reviews from the Indonesian Watsons catalogue. Across all raw review rows, available fields are alias, approvalStatus, comment, date, displayTime, headline, id, like, rating, replyCount, reportable and images. **No reviewer country, language, syndication/original-source, incentive/reward or verified-purchaser field is exposed.**

Consequently, the country evidence is the Indonesian catalogue endpoint. Reviewer residence and language are unverified. It would be inaccurate to call these10,191 confirmed Indonesian consumers or verified18–30 buyers. Incentive status and syndication remain unestablished. Names and media URLs were excluded from clean analysis records; exact raw source responses remain available for provenance.

The rating distribution is highly concentrated:5stars10,027;4stars99;3stars14;2stars10;1star41. Approval, prompting, rewards, selection, and review behavior may influence what is visible. These are source-record characteristics, not a national satisfaction estimate or proof of clinical outcomes.

## Text repetition materially reduces independent information

Whitespace/case-normalized written strings contain335 repeated-text groups covering4,321 written records. There are3,986 excess records beyond one per exact string, leaving3,433 distinct normalized written strings among7,419 nonempty records. Short generic comments can legitimately repeat; templates, campaign wording or cross-purchase copying may also occur. The collection does not establish which mechanism caused any repetition.

Stable IDs remain distinct. Retain the records for provenance, but do not use identical wording as independent corroboration or interpret the raw row total as distinct opinions. Automated lexical coding and full manual coding are separate stages; no claim is made that all comments have been manually reviewed.

## Product and case boundaries

The78 queried product contexts comprise77 toothpaste contexts and one Colgate whitening-serum context. The latter yields three reviews and is explicitly labeled `adjacent_whitening_serum` in clean data. Strict toothpaste comparisons can filter it out.

Existing100g and160g Sensitive Expert listings have different review history lengths. That does not establish relative demand, purchase frequency or willingness to pay, because listing age and review practices differ. This dataset cannot reconstruct paid-price acquisition cohorts, household payment, a former Premium user's replacement purchase, or causal downtrading prevalence without explicit purchase accounts and further evidence.

## Files for integration

- `clean/reviews.json` /CSV: canonical10,191 records; use `text_status` to separate written records from ratings-only rows.
- `source_register.json`:87 successful production source-page records.
- `product_coverage.json`:78 product totals, capture counts and stop reasons.
- `quality_report.json`: counts, ratings, time window, repetition and geographic/incentive boundaries.
- `validation_report.json`: full raw-row/hash/source-ID reconciliation.
- `scripts/collect_watsons_reviews.py`: public collector; `--merge-only` makes no requests.
- `scripts/validate_scale_reviews.py`: offline validation against every raw row.
- `route_probe.json`, `watsons_pagination_pilot.json`, `pageSize500_pilot.json`: feasibility tests, not additional independent reviews.

The attainable corpus here is tens of thousands of actual relevant review/rating records across the wider combined research package. This route did not produce millions, and the dataset does not pad its count with inaccessible pages, blank text described as comments, or duplicated product histories.

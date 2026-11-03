# Retail data dictionary and cleaning ledger

## Unit and scope

One canonical row is one product code at one seller/catalogue retrieval context. It is not a purchase, store, consumer, review, or unique formulation. Cross-seller variants are preserved as separate records. The canonical release has96 oral-care rows (95 toothpaste and one adjacent whitening serum); no local branch or checkout is verified.

## Fields

| Field | Meaning |
|---|---|
| observation_id | Unique source ID plus original 1-based product ordinal; stable for this snapshot |
| source_id | Join to source_register.json |
| url / catalogue_url | Product URL / request used to obtain the source |
| retrieved_at | UTC ISO8601 collection timestamp; not a publication, promotion or transaction date |
| evidence_level | live_public_catalogue_API, live_public_product_JSON or live_public_catalogue_HTML |
| raw_file / record_locator | Relative immutable response and precise JSON-array locator or HTML product-card ordinal |
| product_code / ean | Seller's product code / supplied barcode; null if unavailable |
| brand / product_name | Source name; brand capitalization preserved, no cross-brand identity merging |
| category_path | Copied taxonomy or documented name-based classification |
| is_toothpaste / product_scope | Category/name rule with toothbrush/serum exclusions; one adjacent whitening serum separated after semantic review |
| grams_single_named_unit | Parsed grams in product name; not necessarily total pack grams |
| explicit_pack_count | Only explicit `N x grams` name patterns, otherwise null |
| grams_total_for_analysis | Explicit multipack total or unambiguous named-unit grams; vague Value Pack/+ names excluded |
| content_size_raw | Watsons supplied size tokens, nullable |
| price_idr | Observed catalogue selling price, excluding unverified shipping/voucher adjustments |
| reference_price_idr | Source strikethrough/compare-at price; not established previous paid price |
| original_price_idr / markdown_price_idr | Separate copied API fields, preserved without reconciling contradictions |
| promo_tag / promotion_title | Source promotion labels; not measured discount effect |
| promo_start_raw / promo_end_raw | Source promotion date strings; source timezone not independently established |
| catalogue_stock_flag | Source flag such as inStock, not verified branch inventory |
| purchasable_flag / is_stock_loaded | Separate source booleans; conflicting/unevaluated flags are not repaired |
| seller / country | Named catalogue seller and country inferred from Indonesian source identity; no buyer location inference |
| location_verified / availability_status | False for all rows; evidence only catalogue-level |
| price_per_100g_idr | price_idr / grams_total_for_analysis * 100, rounded2; null if grams ambiguous |
| reference_price_not_previous_paid_price | True: explicit analysis guardrail |
| clinical_claim_verified | False: collection does not validate clinical claims |
| age_specific_switching_evidence | False: catalogue cannot observe age-specific switching |
| named_children_product | Name contains kids/anak/baby; useful adult-analysis exclusion, not a validated regulatory age classification |
| notes | Field/source limitations |

## Cleaning ledger

1. Captured initial Watsons server-rendered page requests, retaining raw HTML and parsed state. Query `page=1` repeated page0; those observations are diagnostic and excluded from canonical counts.
2. Successfully captured the public Watsons API with pageSize100. Stored169 product cards over four brand queries and one broad Enzim query. The latter yielded mixed-category matches, not an Enzim brand assortment.
3. Used category/name inclusion for toothpaste and explicit toothbrush-name exclusion. Retained82 unique oral-care codes from Watsons (81 toothpaste plus one adjacent whitening serum); excluded brushes and travel kits even where the site's category put them under toothpaste.
4. Added4 Enzim variant records from public Apotek Hiro product JSON and10 toothpaste HTML cards from the captured Hypermart page1. Hypermart's product-update dates remain unknown.
5. Retained raw brand spelling/capitalization. Explicit names and codes distinguish child, sensitivity, whitening and other products. Do not mechanically aggregate this into premium tier counts.
6. Computed unit price only for unambiguous named size/explicit multipack.90 rows have unit-price calculations;6 remain null because names are ambiguous or omit grams. No missing value imputation.
7. CSV and JSON are matching canonical views. No actor, checkout, user account, cookies or paid route was used.

## Rebuild

`python3 research/2026-11-03/retail/scripts/build_retail_view.py` rebuilds derived views from the already captured normalized source tables and validates IDs/provenance. Collection scripts make fresh public requests and overwrite their named snapshots; preserve a release before refreshing. Raw initial captures and source-specific JSON remain available for replay/audit.

## Dated taxonomy correction — 3 November 2026

Colgate Optic White Purple Serum40ml is adjacent whitening care, despite the source toothpaste category. Canonical JSON/CSV, unique view, API normalized product tables, builder and quality report now preserve its context with `is_toothpaste=false` and `product_scope=adjacent_whitening_serum`. The81 strict Watsons toothpaste records and one adjacent record total82; adding14 other-retailer records preserves96 offer contexts overall. Raw captures and diagnostic initial SSR snapshots are unchanged.

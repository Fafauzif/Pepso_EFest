# Retail, packs and observed offers — collection findings

Collected 3 November 2026. These are public catalogue observations, not completed transactions or a representative distribution audit. Jakarta is the intended local reference; **no Jakarta branch or delivery postcode was selected**, so zero records have verified local stock. Historical promotion chronology is handled in the separate history workstream.

## What was actually collected

The canonical `retail_observations.json` and matching CSV contain **96 distinct seller/product contexts**: 82 unique Watsons oral-care product codes (81 toothpaste and one whitening serum), four Enzim variants from Apotek Hiro, and ten toothpaste cards from Hypermart's oral-care page 1. This includes four named children's products; they must be filtered out for an adult-only comparison. Adult target age or switching is not observed for any record.

**Taxonomy correction, 3 November 2026:** One Colgate Optic White Purple Serum40ml had been included by the retailer’s toothpaste category. It is now explicitly `product_scope=adjacent_whitening_serum` and `is_toothpaste=false` in all canonical derived tables. The96 oral-care contexts are preserved:95 strict toothpaste contexts plus one adjacent serum; four of the95 are named children’s products. Raw captures are unchanged.

The supporting Watsons API capture contains 169 product cards, including brushes, non-toothpaste and broad search matches that are excluded from the toothpaste view. Initial server-rendered catalogue retrieval produced 182 card observations, but `?page=1` was ignored and repeated page 0. The deduplicated canonical view uses the subsequently successful public API; it does not inflate sample size using those repeated captures. These counts describe collected records, not buyers, sales or national assortment shares.

Source and row provenance are included in each record: `source_id`, product URL, catalogue/API URL, retrieval time, `raw_file`, `record_locator`, code/EAN, prices and quality notes. The raw HTML/JSON responses and replay scripts are preserved. Failed routes are retained in logs and raw web outputs.

## Main findings that change the initial hypotheses

### 1. Premium cannot safely be assumed absent from minimarkets

An Alfagift product page for Sensitive Expert Original 100g exists; its indexed text reports `Stok Kosong`, but the direct public page is only a loading shell and no customer location was supplied. The appropriate result is **catalogue existence; local stock unresolved**. Source: [Alfagift listing](https://alfagift.id/p/pepsodent-sensitive-expert-pasta-gigi-original-100-g-14569), indexed evidence archived in `raw/search_minimarkets_pharmacy.json`.

The official KlikIndomaret homepage search-index capture lists Sensitive Expert Original 60g at Rp19,500. This supports current online catalogue presence, not transaction eligibility or availability in a particular branch. Source: [KlikIndomaret](https://www.klikindomaret.com/?sortcol=harga), same raw search archive. Direct HTTP retrieved a small application shell, not product data.

The separate historical workstream downloaded official Indomaret brochures containing Sensitive Expert promotions. Together, these facts weaken “Premium must primarily be D2C because minimarkets do not carry it.” They do not disprove **exact variant, branch or replenishment-time availability friction**. That narrower hypothesis remains worth testing through targeted store checks.

### 2. The pack-size assumption needs refinement: larger Premium already exists

Watsons' live API lists Sensitive Expert 100g and 160g variants. In this capture, Whitening 100g is Rp23,500 (displayed reference Rp41,900), while Whitening 160g is Rp29,900 (reference Rp51,000). The latter is approximately 20.5% cheaper per gram at these observed catalogue prices, with a higher checkout ticket. Basic Pencegah Gigi Berlubang 190g is Rp21,100. These are current observations, not historical paid prices. Record IDs: `WATAPI-PEPSODENT-005`, `-031`, `-046`.

Implication: an idea to “introduce a larger Premium pack” must first identify an actual missing pack/channel/need. The present research question is whether shoppers know, find, value and repurchase existing offers. Likewise a 60g minimarket listing means a smaller-trial concept should check existing availability before claiming novelty.

### 3. Deep deals coexist across brands and benefit categories

Watsons currently displays several percentage-off offers and buy-two-pay-one tags. The latter appear for Ultra White and Closeup White Now products; they are **conditional multi-buy offers**, not a one-tube halving of price. A displayed reference price is not proof of a previously paid price. Current promotion windows are preserved from API fields rather than inferred from the collection date.

The observed data establish offer architecture and a possible price-comparison problem. They cannot show whether promotions caused downtrading, whether promotions produce low-repeat cohorts, or whether demand survives at normal prices. Those require actual purchase histories or longitudinal cohorts.

### 4. Enzim is a real independently listed brand, but “enzyme” search is ambiguous

Apotek Hiro's public product JSON gives Enzim Mild 124g Rp25,000; Mixdent 93g Rp17,500; 40 Plus 124g Rp39,500; and 40 Plus 63g Rp23,000. No store-specific stock or checkout was verified. These are different benefit/age-positioning variants, not one equivalent product. Sources are `HIRO-*` records and the corresponding product URLs in the canonical data.

Watsons' broad `enzim` search returned other enzyme-related products, including Darlie toothpaste. We retained the original brand identity and did not relabel those results Enzim. This illustrates why an “enzymatic toothpaste” query cannot by itself identify the Enzim brand.

## Comparison cautions

- Match need state, seller, time and actual pack before interpreting price differences. Sensitivity, cosmetic whitening, child, basic prevention and age-specific care are not interchangeable segments.
- `grams_single_named_unit` is the grams in the name. `grams_total_for_analysis` is computed only where unambiguous; explicit 2× packs use total grams. Vague “Value Pack” remains null for unit-price analysis until package count is verified.
- A price-per-100g value does not establish expected consumption, product efficacy or willingness to pay.
- An API `stockLevelStatus=inStock` can coexist with `purchasable=false` and `isStockLoaded=false`. Accordingly every Watsons record is labeled `catalogue_flag_only_no_location_checkout`; none is asserted immediately buyable in Jakarta.
- Hypermart's retrieved catalogue has no clear price-update date. Treat its prices as currently displayed on a public page with uncertain freshness, not as a guaranteed live offer.
- The early web-index Watsons values differ from live API values in several cases. We preserve captures separately; the API view is the canonical time-stamped data for this collection. Disagreement is not silently repaired.
- K24Klik's page displays `Stok Habis` and `Rp0`; its location notice says location is needed for nearby pharmacy availability. **Rp0 is not a usable price.** The page is a missing/availability-warning observation, not evidence toothpaste is free or nationally out of stock.

## Tool routes and reproducibility

Successful: standard-library Python `urllib` public GET of Watsons HTML; extraction of `wtcid-state` JSON; the Watsons public catalogue-search API; Shopify product JSON at Apotek Hiro; Hypermart catalogue HTML. No login, browser cookies, Apify or paid service was used.

Watsons API example:

`https://api.watsons.co.id/api/v2/wtcid/products/search?query=%3AbestSeller%3AproductBrandCode%3APepsodent&pageSize=100&currentPage=0&lang=id&curr=IDR&fields=FULL`

The live API returned all60 Pepsodent, all17 Sensodyne, all10 Closeup and all45 Colgate product cards. The broad Enzim query returned37 mixed-category matches. The toothpaste view removes brushes/travel toothbrush kits even when a site's category metadata misclassifies them under toothpaste.

Limited/blocked: direct Blibli and Halodoc returned403; Alfagift/KlikIndomaret returned application shells; Guardian's public category response did not expose product cards. Hypermart page1 parsed successfully but full pagination was not reverse-engineered. Those limits are documented rather than represented as product absence.

Replay collection scripts from the repository root, then `python3 research/2026-11-03/retail/scripts/build_retail_view.py`. This will create a fresh observation snapshot and overwrite derived outputs; copy a release before refreshing if retaining historical snapshots is needed. The raw files in this release correspond to the recorded retrieval timestamps.

## What this work supports next

1. Use the retail matrix to choose exact SKUs and relevant outlets for primary shelf checks.
2. Ask actual former Premium buyers whether the 100g/160g/60g options were in their choice set, not whether they abstractly like smaller packs.
3. Compare habitual replenishment outlets with the outlet where discounted trial occurred.
4. Test perceived extra value and who pays, while preserving shoppers who can find Premium but still rationally choose Basic.
5. Before proposing new distribution or pack architecture, examine whether the real issue is knowledge, execution, local stock, price conditions or fit of existing offers.

## Files

- `retail_observations.csv/json`: canonical96 records, source-located.
- `retail_unique_view.json`: same distinct seller/product view; cross-seller products are not silently merged.
- `watsons_api_all_products.json`:169 cards before toothpaste exclusion.
- `watsons_api_toothpaste.json`:81 strict Watsons toothpaste records; `watsons_api_adjacent.json`:one explicitly separated whitening serum.
- `other_retailers_observations.json`:14 pharmacy/supermarket records.
- `source_register.json`, `*_log.json`, `quality_report.json`: provenance, failures and reconciliation.
- `raw/`: original catalogue bodies and page-reading/search outputs.
- `scripts/`: collection and deterministic derived-view construction.

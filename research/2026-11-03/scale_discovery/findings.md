# Scale discovery: more relevant review records, not a padded corpus

Collected 3 November 2026, Asia/Jakarta. No Apify, credentials, account sessions or paid services were used.

## Actual new collection

The expansion retrieved **1,930 additional Pepsodent review IDs** from three ORESA campaigns using public pagination. These are new records beyond the original Ultra White 298; original Ultra White was deliberately not downloaded or counted a second time.

| Campaign/product | New review IDs | Public campaign sampling window | Temporal interpretation |
|---|---:|---|---|
| Pepsodent Gum Expert | 1,069 | 23 September–31 December 2024 | Before the case endpoint; review dates individually retained. |
| Pepsodent Siwak & Habbatussauda | 551 | 21 December 2023–2 March 2024 | Campaign predates endpoint, but one review is dated July 2026. |
| Pepsodent Pro.Care | 310 | 16 July–15 August 2026 | After H1 2026; useful current experience/context only. |
| **Total newly collected** | **1,930** | | **1,619 reviews dated within 2022–H1 2026; 311 afterward.** |

The public ended-campaign API also gives the existing Ultra White campaign sampling window: **11 March–28 April 2026**. This improves the first audit, which could not recover the campaign date from the visible landing page. The campaign window is not automatically every review's publication date, first product launch date or continuous market availability. The original Ultra White records remain in `access_reviews/`; they are not included in this expansion's new-record count.

A review timestamp of 29 July 2026 on Siwak record `ORESA-55534` is preserved literally despite the older campaign window. We do not silently repair it or pretend all reviews from an older campaign are historical case-window evidence.

**Provenance:** `clean/oresa_campaign_inventory.json` and `raw/oresa_ended_pepsodent.json`; public endpoint `https://oresa.id/produk-sampel/ended-sampling?page=1&q=pepsodent&sort=&category=`. The endpoint is referenced in the public product-listing page's own client code. No internal/private network address returned in metadata was accessed.

## What the added evidence is good for

This expansion broadens the product contexts from whitening into gum care, herbal/religious-natural cues, and current multi-benefit oral care. It supplies far more actual experience wording than the initial single campaign. It still does not identify eligible 18–30-year-old Premium-to-Basic switchers.

A manual inspection of selected records highlights useful questions:

- `ORESA-39070`, Gum Expert, 3 October 2024, combines a reported personal need with whole-family suitability. That is a described decision context, not proof of who paid or that all family members used it.
- `ORESA-42566`, Gum Expert, 15 November 2024, mixes packing/delivery, product taste and affordability. A positive review is not a pure efficacy measure.
- `ORESA-40456`, Gum Expert, 17 October 2024, describes a less aggressive mint experience and a reason to keep the product at home. It illustrates sensory evaluation and intended availability, not a verified replenishment sequence.
- `ORESA-39455`, Gum Expert, 7 October 2024, says it was difficult to find a suitable toothpaste. In context this is suitability search, not established retail stockout. A keyword match on “susah cari” alone would overstate an availability problem.
- Pro.Care accounts describe a clean/kesat feel and benefit variants, but the campaign and reviews occur after H1 2026. They cannot explain the earlier decline.

These are source-specific observations from an incentivized/sampling setting. Product and health statements in them are consumer assertions and often echo campaign language; no clinical validation is implied.

## Incentives and source strata

The Gum Expert landing page explicitly makes cashback conditional on selected official-store purchase, a survey, reviews and social tasks. It is inappropriate to label this corpus organic purchaser sentiment.

The Pro.Care landing page describes selected participants and required reviews/social tasks with coordinated timing. Its documented setting is managed sampling. The page does not support assuming all participants independently paid full price or that a review demonstrates subsequent purchase.

The older Siwak page confirms a sampling program but did not expose specific compensation/task details in the retained response. Its exact compensation is therefore **unverified**, rather than guessed to be identical to Gum Expert.

Clean records preserve these distinctions in `incentive_status`. They omit member names, avatar URLs and unnecessary profile metadata. Public original responses are retained as raw evidence for this private research package; they should not be republished wholesale as a public roster.

## Counts, duplicates and analytical limits

There are 1,930 unique review IDs but **1,923 unique normalized review texts**; five normalized-text groups repeat. Distinct platform IDs are not necessarily distinct people, and text duplication is not automatically fraud. The original text and platform IDs remain intact; the normalized hash enables sensitivity checks.

Ratings are extremely skewed: **1,916 five-star and 14 four-star records**, with no one/two/three-star ratings in these returned campaign records. This is a severe selection limit and cannot be used to estimate Indonesian satisfaction or infer that negative experiences are absent.

Exploratory lexical matching yields 1,051 records with sensory-related wording; 131 with household-related wording; 37 with price/promotion wording; and 31 with repeat-intention wording. These labels overlap and can be campaign-derived. They are discovery aids, not validated motives or population percentages.

The six stock-wording matches include statements about keeping stock at home, not necessarily product unavailability. The one pre-use-wording match was a call for others to try the product, not the writer admitting they had not used it. These examples show why manual context is required before turning automated tags into findings.

Dates are parsed into **date-only ISO fields** using an explicit Indonesian month dictionary. The raw date/time string remains preserved; no timezone is invented. Analysis distinguishes within-case-window and after-case records. In particular, a review in an old campaign can still be late.

## Large public datasets: downloaded and screened, then excluded

We did not stop at small platform collection. Two primary research datasets were actually downloaded and screened:

| Primary dataset | Actual parsed rows | Scope found by inspection | Relevant toothpaste candidates |
|---|---:|---|---:|
| [Dataset Costumer Review Indonesia](https://data.mendeley.com/datasets/74xrbd4vxy/1), DOI `10.17632/74xrbd4vxy.1`, azani cempaka sari (2026), CC BY 4.0 | 203,787 | Five electronics categories: external hard drives, flash drives, smart TVs, digital televisions and laptops. | 0 |
| [PRDECT-ID](https://data.mendeley.com/datasets/574v66hf2v/1), DOI `10.17632/574v66hf2v.1`, Sutoyo et al. (2022), CC BY 4.0 | 5,400 | 29 categories selected for emotion classification; product-name and text screening found no oral-care match. | 0 |

**209,187 rows were screened; zero were added to the oral-care evidence count.** The larger landing page describes 203,786 rows, while the downloaded CSV parses to 203,787. The observed discrepancy is preserved rather than silently altered. Its `name` field contains reviewer names, not product names; product IDs without oral-care mapping are not sufficient to declare relevance.

The primary dataset pages state CC BY 4.0; raw file metadata, hashes and API download URLs are retained. Their original sentiment labels, where supplied, are not Pepsodent findings. Do not treat a broad Indonesian e-commerce corpus as oral-care evidence merely because it is large.

A Hugging Face Tokopedia corpus was also inspected through primary metadata/card discovery. Its declared 40,607 rows cover tools, fashion, electronics, mobile phones and sports, not an established oral-care stratum. Metadata was retained; those rows were not downloaded, screened individually or counted as collected evidence. Third-party mirrors do not create independent new data sources.

Broad search discovery also surfaced object-detection, clinical microbiome, app-review, sales-model and generic sentiment resources. These do not answer the requested consumer-product-use mechanisms and were not substituted for product reviews.

## Coverage of campaign search

The public ORESA ended-campaign endpoint was queried for Pepsodent, Sensodyne, Closeup, Colgate, Enzim, Systema, Ciptadent and Formula. This produced four distinct relevant toothpaste campaign products in the retained results, including the already-collected Ultra White. Search failure or zero matching campaigns does not establish that a competitor has never run sampling elsewhere or that all historical campaigns remain exposed.

## Files and reproduction

- `clean/oresa_new_reviews.json` / CSV: 1,930 new review IDs, original text and raw-file locators, parsed dates, campaign windows and incentive distinctions.
- `clean/oresa_campaign_inventory.json`: four discovered campaign products and exact declared sampling windows.
- `clean/oresa_lexical_flags.json`: explicitly exploratory overlapping string-match flags.
- `quality_report.json`: reconciled counts, timing, ratings, duplicate-text diagnostics and zero verified target switchers.
- `oresa_collection_log.json`: 21 public review-page responses, totals, pagination, hashes, retrieval dates and raw paths.
- `oresa_discovery_log.json`: query-level campaign discovery results.
- `oresa_context_log.json`: specific campaign-task page retrievals.
- `dataset_inventory.json`, `dataset_collection_log.json`: downloaded public dataset metadata, row/column counts and download evidence.
- `clean/dataset_toothpaste_candidates.json`: deliberately empty because no relevant records were found in the screened datasets.
- `raw/`: original JSON/HTML/CSV responses, including clearly separate screened-but-excluded broad corpora.
- `scripts/`: collection, campaign discovery, date parsing, normalization and relevance-screening logic.

Use the relevant review tables for analysis. Exclude the broad electronics/emotion-classification raw CSVs from any headline oral-care sample count. If distribution size or unnecessary personal metadata is a concern, an export can preserve their metadata/hashes/screening summary while leaving those unrelated raw tables out of the user-facing data ZIP. Do not delete the audit trail from the working research record.

The expansion demonstrates a repeatable route to more useful evidence and a disciplined rejection of tempting large but irrelevant corpora. It does not support a claim that millions of relevant Indonesian toothpaste records were available or collected.

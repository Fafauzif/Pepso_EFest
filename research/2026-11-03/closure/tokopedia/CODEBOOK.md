# Tokopedia and Shopee cleaning and coding

This folder analyzes **user-executed Apify exports**, not assistant-run paid collection. Raw export bytes remain unchanged in `../raw/user_runs/` as lossless `.json.gz` archives. Original source filenames and zero-based JSON array indexes identify every occurrence. No age, income, residence, clinical outcome, or Premium-to-Basic transition is verified by these files.

## Rebuild

From the repository root, Python 3.10+ with the standard library:

```bash
python research/2026-11-03/closure/tokopedia/clean_analyze.py
python research/2026-11-03/closure/tokopedia/validate.py
```

For a separate folder containing original `.json` or `.json.gz` files, add `--input-dir PATH`. The default searches the release archive, a compatible root raw folder, then the original session's sibling `upload/` location. No network or paid API access is required.

## Units and identity

- A **review occurrence** is one exported JSON object of type `product_review` in either Tokopedia file.
- A **unique review** uses platform plus `reviewId`, not text. The last file occurrence is the convenient canonical view; all 309 payload occurrences remain in `review_occurrences.jsonl.gz`. Canonical selection is not proof that later fields are more accurate.
- A **product observation** is a timestamped product/search result. Twenty-four observations refer to 18 distinct `productId` values; they are not 24 unique products or purchases.
- A **billing notice** is metadata, not a consumer response. Charges are actor-reported events, not independently checked account usage.
- Different IDs with the same normalized text remain distinct records; duplicate-text groups do not establish the same author, bots, or fraud. Most duplicates are short generic expressions.
- `author_pseudonym` hashes a nonzero reviewer ID. Zero or missing IDs remain null, never collapsed into an invented common consumer. Raw audit payloads retain source identities; the main clean record table omits names and uses pseudonyms.

## Product and incentive eligibility

`product_scope` separates `toothpaste_title_candidate`, `toothpaste_gimmick_title_candidate`, and `adjacent_whitening_spray`. The five records on the listing named Gimmick Pepsodent are archived as gimmick/promotion-context candidates and conservatively excluded from ordinary paid-purchase analysis; the title alone does not establish free receipt. One explicitly says free Pepsodent from Sanofi. The listing's Rp500,000 card price is not a defensible ordinary price benchmark.

One Basic-linked text says the product prevents **body odour**. `possible_misassigned_text=true` flags this mismatch; no repair is guessed. The source link may contain a review copied from another product, mistaken wording, or another ambiguity. The review is retained but excluded from the written-toothpaste candidate subset.

`eligible_written_toothpaste_candidate=true` requires a nonempty text, a toothpaste-title candidate excluding giveaways/spray, and no detected body-odour mismatch. This is a **broad candidate eligibility flag**, not proof of actual use, authenticity, demographic fit or rich information. It retains emoji and generic praise for auditing; use close-reading codes and information state for mechanism analysis.

Unknown incentive status remains `not_established`; gimmick-title candidates use `gimmick_listing_context_incentive_not_established`. Only one explicit “Pepsodent gratis” statement receives `review_text_explicit_free_Pepsodent_item`. None establishes a mandatory review incentive. A gift shown in a product bundle title is different from proof that a reviewer was paid or given a free test product. No sponsorship inference is made from a high rating.

## Text and dates

`text_original` is exact source text, including spelling and masked words. `text_normalized` uses Unicode NFKC and outer whitespace trimming; this never replaces originals.

Information states are deterministic diagnostic bins:

- `blank`: missing/empty/whitespace text.
- `symbol_or_numeric_only`: no alphabetic character; includes emoji, punctuation and single numerals.
- `short_generic`: matches a documented small fixed lexicon after punctuation removal.
- `contextual_text_candidate`: everything else. This is deliberately permissive; it includes many fulfilment-only, generic and uninterpretable comments. It must not be reported as a count of useful product experiences.

Lexical `candidate_tags` are **nonexclusive screening rules** in `PATTERNS`, not validated sentiment or mechanism labels. They can miss slang (for example an unusual spelling of repurchase) and can trigger on ambiguous words. Manual annotations take precedence for selected evidence. Counts do not establish the percentage of Indonesian users experiencing a mechanism.

The actor exports `reviewTimeText`, `reviewTime` and `reviewDate`. `reviewTime` often appears mechanically estimated from a relative label. Both date fields exist in 198 of 266 canonical records; they disagree on the calendar day in 186 of those 198. The remaining 68 records have no reviewTime. Missing values are not counted as disagreement. We retain both and mark the conflict. A slice using `reviewDate` is labelled **by unverified reviewDate**. It is not an adjudicated date or guaranteed original marketplace date. This release does not silently select a verified date or treat all actor-estimated timestamps as exact. Case slices use 1 January 2022–30 June 2026; older and later context remain separate.

## Qualitative review and selection

All 266 main-export review texts were displayed and screened by the assistant. **85** received explicit close-reading annotations in `manual_annotations.tsv`, linked to exact source records in the generated evidence ledger:

- 40 records were sampled without replacement from the main file's review sequence using `random.Random(11262026)`; this is a reproducible **random calibration sample of this export**, not a population sample.
- 45 further records were selected purposively for mechanisms, counterexamples, date/product limitations and negative ratings.

The two sets are labelled separately. Do not calculate mechanism prevalence from the combined purposive sample. The annotations are assistant judgments, not independent human fieldwork, intercoder agreement or clinical verification. `interpretation` explains what wording supports; `alternative_or_limit` preserves competing readings. No made-up reviewer portraits or interviews are included.

Key distinctions: `explicit_repurchase` requires reported completed repeat wording; `continued_use` describes habit without necessarily reporting a transaction; `future_repurchase`/`future_loyalty` is intention. `loyalty_ambiguous` may refer to seller rather than brand. `claimed_benefit` is a consumer assertion, not validated efficacy. `before_use` prevents interpreting a high rating as an experienced benefit. `fulfilment_complaint` concerns transaction experience and may coexist with good product fit.

## Outputs

| File | Role |
|---|---|
| reviews_clean.jsonl.gz / .csv.gz | 266 canonical review records and all analytical flags |
| review_occurrences.jsonl.gz | 309 original review payload occurrences and source locators; private audit layer |
| product_observations.jsonl.gz / .csv.gz | 24 timestamped product-card observations |
| excluded_shopee.jsonl.gz | Two errors plus 100 wrong-target Singapore UGREEN review records |
| billing_notices.jsonl.gz | Two actor billing notices, separate from data |
| duplicate_text_groups.jsonl.gz | Nonempty exact-normalized text groups without identity merging |
| manual_annotations.tsv | Assistant-authored code/interpretation input used to rebuild the ledger |
| qualitative_evidence.md / .jsonl.gz / .csv.gz | 85 source-linked annotated examples |
| stats.json | Reconciled counts and source hashes |
| FINDINGS.md | Substantive interpretation and limits |
| QA.md | Actual verification results and remaining uncertainty |

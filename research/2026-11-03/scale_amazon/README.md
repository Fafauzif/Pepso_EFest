# Large international comparison corpus — streaming collection

This is a separate historical international comparison layer. **It is not an Indonesian young-switcher dataset.** The source is McAuley Lab's public Amazon Reviews2023 dataset, accessed at its original HuggingFace repository. Preserve the source attribution and citation in `raw/source_README.md`; no new redistribution license is asserted here.

## Actual processing and retained data

| Stage | Rows |
|---|---:|
| Health and Personal Care metadata streamed | 60,293 |
| Health and Household metadata streamed | 797,563 |
| Health and Personal Care reviews streamed | 494,121 |
| Health and Household reviews streamed | 25,631,345 |
| **Review rows screened** | **26,125,466** |
| Title-matched candidate review observations | 289,584 |
| Distinct derived review-identity fingerprints, including blanks | 286,904 |
| Distinct written candidate fingerprints across all retained product types | 286,706 |
| Adult/human-toothpaste-title candidate fingerprints | 197,002 |
| **Written adult/human-toothpaste-title candidates** | **196,872** |

Candidate filtering also retained separate child, pet, accessory/container, powder/alternative and unresolved classes. These classes are not pooled into the adult-toothpaste comparison. The title rules are conservative screening, not manual eligibility verification: products with unclear titles can be excluded, and some apparent toothpaste titles can refer to a serum, child product or other use. See the independent `QA.md` and manual sample.

The identity fingerprint hashes original user ID, parentASIN, timestamp and original review text, with the same algorithm across categories. It is **not an original platform review ID** or a unique person. Original observations remain preserved;2,680 repeated-identity observations are not additional independent reviews.198 blank candidate records are excluded from the written-text export. Rating/record totals and written totals are different.

## Source and provenance

- Original repository: https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023
- Original project: https://amazon-reviews-2023.github.io/
- Full public source files were streamed to screen rows. Only matched raw records were retained, not the entire26million-row source dump.
- `access_log.json` and the household subdirectory's log record exact original URLs, source rows, read bytes, full read-stream hashes, timestamps and completion status.
- `raw/toothpaste_metadata.jsonl` and `raw/toothpaste_reviews.jsonl[.gz]` retain matched source records with original source line numbers. `clean/` contains normalized/classified copies.
- Original text is preserved; original user IDs are omitted from normalized exports. Do not infer age, country or clinical effectiveness.
- The earlier UCSDgzip URLs returned404; feasibility logs preserve that failure. The working route used original HuggingFace JSONL files. No paidAPI, login or scraper service was needed.

## Reproduction

From the repository root, run `python3 research/2026-11-03/scale_amazon/collect.py`, then `collect_health_household.py`, then `classify.py`, then `analyze.py` in that directory. These are fresh live snapshots; upstream versions can change. Pin the source commit/content hashes if exact future reproduction is required. Full scans read roughly14GB of metadata/review bytes in this recorded run, so do not rerun merely to inspect the collected subset.

Collectors stream lines without loading the whole source. Retained candidates are gzipJSONL for the larger category. Logs distinguish completed scans from caps/errors. No elapsed-time measurement is promised to repeat on another connection. SQLite ingestion and compressed CSV/JSONL exports are documented in `../scale_pipeline/README.md`.

## Analysis boundary

`analysis_summary.json` deduplicates the derived fingerprints and counts explicit English lexical cues among the196,872written adult-title candidates. Sensory language matched66,033; pack language25,900; price/value20,557; household9,319; repeat3,347; need/result41,750. These overlapping literal matches are search aids, not validated psychological constructs, prevalence, sentiment or causal effects. No claim is made to have manually read the entire corpus.

The written adult-title candidates span2001–2023. Only25,459are dated2022and13,400dated2023. Even those cannot identify the case's geography, age, tier-switching direction or contemporary retail conditions. Use the corpus to explore possible language and rival mechanisms, then validate against relevant Indonesian purchase evidence.

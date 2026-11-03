# TikTok normalization, coding, and sampling

The immutable input is `dataset_tiktok-comments-scraper_2026-11-03_12-02-32-061.json`. The final archive path is `research/2026-11-03/closure/raw/user_runs/<filename>.gz`; decompression must reproduce SHA-256 `f0cbed908bd1f79ab73cf1a5702cf824ed23a91e452001f52db86d5f9dfa0326`. A source locator's `row=N` means the **one-based JSON array element**, not a physical line number.

## Rebuild

From repository root, Python 3.10+ with the standard library:

```bash
python research/2026-11-03/closure/tiktok/build_tiktok.py
python research/2026-11-03/closure/tiktok/annotate_sample.py
python research/2026-11-03/closure/tiktok/verify_tiktok.py
```

Pass `--source PATH` to the first script if working from a separately downloaded original JSON or JSON.gz. The parser prefers the retained archive. It never writes the source. Author profiles, avatars, bios, handles and original UID are omitted from normalized tables; the UID is mapped to a deterministic SHA-256-based pseudonym. Video URLs retain the creator handle because they identify the submitted source. Pseudonyms are identifiers for observed platform accounts, not established people. Hashing is a convenience for internal views, not a claim of anonymous data.

## Outputs and principal fields

`clean/comments.jsonl.gz`, `clean/comments.csv.gz` and the readable CSV contain one row per `cid`; `clean/occurrences.jsonl.gz` contains all input occurrences. `clean/video_coverage.csv`, `stats.json`, `clean/copied_text_groups.json`, and `clean/conflicts.json` expose coverage and quality diagnostics. `rule_patterns.json` saves the precise lexical rules.

| Field | Meaning |
|---|---|
| record_key / source_record_id | `tiktok:<cid>` and the original comment ID |
| text_original | Exact source text, including blank string, spelling, punctuation and emojis |
| text_normalized | Whitespace collapsed for duplicate exploration; never replaces original |
| text_present | Nonempty after whitespace stripping; does not imply substantive meaning |
| record_type / parent_record_id | Root or reply and `repliesToId`; missing parent remains null |
| parent_in_export | True/false for replies; null for roots |
| video_id / video_url | Submitted canonical source context, not a verified video-caption extract |
| source_url | Constructed video URL with comment ID locator; deep-link navigation is not verified |
| content_date | Original `createTimeISO`; epoch value is separately retained and compared |
| case_scope | Asia/Jakarta local dates, 1 January 2022–30 June 2026 inclusive, pre-2022 context, or later context |
| content_date_jakarta / case_scope_utc | Local timestamp and separate UTC-scope field, preserving the boundary comparison |
| source_file / row / hash | Original filename, one-based array index and uncompressed file SHA-256 |
| candidate_tags | Transparent lexical search candidates, not validated qualitative themes |
| relevance_candidate | Blank; explicit off-topic candidate; self-contained oralcare candidate; unresolved context |
| age_verified / premium_to_basic_verified | False for every row; this is lack of verification, not a claim that no such person exists |
| incentive_status | Not established; do not relabel as organic |

The input has comment dates but no verified video publication timestamp, video caption, transcript, sponsorship disclosure, or complete run input. The export's filename timestamp is not silently substituted for collection time. The final local-date case count is 1,648; the earlier UTC count was 1,649. One comment (`7657245284531864340`) at 30 June 17:42:45 UTC is already 1 July in Jakarta. Both conventions are available explicitly rather than silently overwriting source dates. Root and reply can be joined by `source_record_id`/`parent_record_id`; every parent here is present in the export. That does not recover video content or deleted/uncollected conversation history.

## Automatic candidate rules

Themes search for household/payer language, switching/repurchase language, price/promotion, sensory descriptors, experienced-result wording, availability, recommendation/questions, and explicit off-topic terms. Exact regexes are in `rule_patterns.json`. Candidate matches can be false positives: “ganti” may refer to shoes, skincare or brush heads; “mama” may relate to infant toothpaste; a brand may identify a toothbrush rather than toothpaste. Nonmatches can be false negatives because Indonesian slang, implied context, misspellings, and product nicknames are varied.

The explicit off-topic rule is intentionally incomplete and **not** an eligible-corpus boundary. Its 24 matches are not the number of all irrelevant comments. The 1,506 unresolved comments are neither automatically irrelevant nor suitable for causal evidence. The oralcare rule's 842 matches are not 842 first-person product experiences. All automated counts describe candidate retrieval within these 18 selected videos only.

Copied text uses casefolded, whitespace-normalized exact equality. It does not strip emojis, mentions or product names. Identical generic comments can be coincidental; different posts with identical text remain distinct IDs. No near-duplicate or bot classification is claimed.

## Actual qualitative review

The 100 selected original comments were read and individually annotated by the assistant. `sample_selection.json` records the selection; `qualitative_evidence.json` and `.csv` hold exact text, original locator, date, selection method, evidence type, mechanism codes, and interpretation/limitations. `annotate_sample.py` materializes those explicit human-readable assistant judgments rather than deriving them from keywords.

The sample has **36 random calibration comments** (two per video, `random.Random(20261103)`), then **64 purposive mechanism candidates** ranked by a transparent lexical score, with a maximum 12 selected per video. Random sampling is stratified equally by video and not proportional to total comments; no population or whole-corpus percentage is inferred. Purposive enrichment deliberately raises the frequency of switching/payer stories, but also brings off-topic false positives. It is a discovery sample, not sentiment measurement or saturation proof.

Manual evidence types distinguish reported switching, use/preference, household brand use/payer role, intention, questions/advice, adjacent products, child oralcare, off-topic content, low information, and blanks. Multiple mechanism codes may coexist. `household_brand_use` means family members are described as using the brand/product; it **does not verify a shared physical tube**. A `switch_report` records the text's reported change, not verification of age, SKU tiers, causation or an actual transaction.

Unverified health claims remain attributed self-reports. The corpus does not establish that a named toothpaste caused relief, whitening, irritation, loose teeth, or tooth thinning. No ingredient concentration or professional recommendation in a comment is adopted as fact without independent verification. Claims about charcoal or rinsing are observations of advice, not recommendations from this report.

## Review limitations

No full-corpus manual coding, demographic confirmation, representative sampling, author authentication, full video review, purchase verification, independent clinical assessment, human-interviewer validation, or target-group saturation is claimed. Independent assistant QA checks are described separately in `QA.md` and do not establish ground truth.

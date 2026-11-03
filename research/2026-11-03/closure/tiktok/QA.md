# TikTok quality assurance

## Reconciliation

`verify_tiktok.py` checks the retained source hash, all 2,380 original comment IDs/texts/dates against their one-based source rows, unique ID counts, occurrences, compressed JSONL/CSV parsing, age/switcher flags, temporal splits, and all 699 reply-parent joins. All replies' parents are present **and belong to the same video**. There are no duplicated `cid` occurrences or conflicting payloads in this single export. All ISO dates agree with epoch timestamps to the second. Asia/Jakarta case-period assignment yields 1,648 records, versus 1,649 using UTC; the one boundary record is retained with both scope flags. Full results are in `validation.json`.

The eight blank comments remain in the full normalized archive and are omitted only when a written-text subset is requested. Nonempty emojis, greetings and links remain nonblank without being relabelled substantive. The 44 copied-text groups identify exact normalized equality across different comment IDs, not duplicate people or proven campaign activity.

## Qualitative audit

The assistant actually read the 100 selected originals printed in full (36 fixed random calibration comments and 64 purposive additions), then wrote individual interpretations and limitations in `annotate_sample.py`. Source text was copied from the original by ID/index, not reconstructed from a paraphrase. `qualitative_review_stats.json` describes the sample, including its enrichment and off-topic material.

An independent assistant QA agent checked all 100 annotation ID/text/source-row links and found zero mismatches. It also independently checked a fixed 20-record subset (`seed=314159`) for material semantic overclaims and found none in its displayed review. The check is secondary and nonblind, not human validation or a classifier-accuracy estimate. Its record is `../qa/tiktok_annotation_check.json`. A wording refinement subsequently changed the common mechanism code from `household_shared_use` to `household_brand_use` and sample 3 to `home_use_only`: family brand use does not verify sharing a physical tube. Source texts/IDs and sample membership are unchanged.

## Known remaining limitations

- Video captions, transcripts, sponsorship and publication dates were not provided in the comment export. URL resolution establishes identity of a redirected video, not its content.
- Exactly 180 returned comments on eight videos is consistent with the proposed cap, but the export does not contain the actual executed input or total available history. There is no claim of complete comment histories.
- Parents are present for delivered replies, but missing/deleted/uncollected comments can still exist outside the export.
- Lexical candidate codes have obvious false positives and false negatives. The manual sample is not representative of the whole corpus, Indonesia, the competition target, or TikTok.
- No original author age, country of residence, payer identity, purchase, product tier or causal medical claim has been verified. Self-described boarding or family status is preserved as testimony, not independently confirmed.
- No inference of paid promotion is made from comments that sound promotional, contain a shortlink, or deny being a promoter. Incentives remain unknown.
- Selected comments include children, adjacent brushes/whitening products, and unrelated cosmetics. These are explicitly separated in qualitative annotations.
- Constructed comment locator URLs are not validated TikTok deep links; original video URLs plus `cid` and raw array rows provide the auditable identification.

These limitations are a reason to design primary purchase-history research, not a reason to inflate the collection count or report a pooled sentiment score.

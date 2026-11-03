# X quality assurance

The pipeline is standard-library Python and runs offline on retained inputs. See `CODEBOOK.md` for canonical fields and sampling. Original upload files are never rewritten. `verify_x.py` checks every normalized text and raw occurrence against its original file and JSON index, recomputes input hashes, verifies sample annotations against source text, and reconciles the six-post legacy collection. Results are in `qa_results.json`.

## Corrections made during analysis

1. Source platform ID totals were distinguished from occurrence totals: 16,165 exported rows yield 12,990 unique new-export post IDs.
2. The earlier six-post sample has one overlap, not zero. Five additional brand-owned IDs give 12,995 combined X IDs. The overlapping story is an imported-toothpaste-to-Pepsodent account, not a confirmed intra-Pepsodent tier switch.
3. Retail/commercial screening initially read visible text only. Expanded entity URLs exposed links hidden behind t.co. The fixed qualitative sample was retained after this improvement so earlier false positives remain inspectable.
4. Accessories were separated from broad oralcare matches. Broader candidates still contain nonoral hacks, news, jokes, and media. No fully verified-consumer eligibility total is asserted.
5. Six reviewed posts reproduce repeated advertising-style ice-eating wording, including one Pepsodent substitution. First-person grammar cannot certify independent experience. The precise original official-ad source was not independently matched, so the codebook and notes use qualified wording.
6. Same-ID text matches across all four exports, but 1,758 IDs have differing full payload hashes. These differences are preserved in occurrences without assuming which metadata field changed in every case.
7. Conversation root presence is not parent-thread completeness. Direct parent IDs are unavailable; only 572 of 5,263 replies have a root ID represented in the collection.
8. Country, age, and target switcher eligibility remain unverified. One Malay-language price/access story is an unverified-country comparator, not evidence of Indonesian stock.

## Independent checks

An independent QA agent sampled 20 normalized X records with seed 1729, observed numerous commerce/off-topic matches, and cautioned against calling broad candidates consumer stories. See `../qa/x_secondary_relevance_sample.json`. It also source-matched the first 108 annotations and read a 15-record subset of their interpretations; see `../qa/x_annotation_check.json`. The ninth supplementary annotation (legacy-overlapping full story) was added afterward and checked by `verify_x.py`; this timing is explicit rather than extending the independent review's scope retroactively.

These are assistant-led consistency and source-fidelity checks, not human validation, external corroboration, or a numerical classifier accuracy estimate. There is no reference-standard labelled random sample large enough to claim precision/recall for the full corpus. No inferential confidence intervals or population percentages are presented.

## Interrupted intermediate export

An early stream-written `occurrences.jsonl.gz` failed gzip integrity checking despite its build process reporting successful completion; the cause was not established. That intermediate was replaced, not packaged as valid data. Export writing now completes compression in memory, checks decompression, writes and syncs a temporary file, atomically replaces the target, and compares stored bytes. The rebuilt occurrence export parses to all 16,165 source rows; `qa_results.json` records the subsequent passed full source check. The CSV convenience export also parses to exactly 12,990 records despite multiline post text.

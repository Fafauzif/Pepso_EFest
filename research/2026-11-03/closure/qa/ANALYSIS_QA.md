# Independent analysis QA

Completed 3 November 2026. This is an independent second-assistant check of data handling, quotation fidelity, selected interpretation, and the new synthesis. It is not independent human research, source authentication, clinical validation, a representative survey, or a blind ground-truth coding study.

## Results actually checked

| Check | Result | Supporting file |
|---|---|---|
| Original uploaded inputs versus portable archives | All 11 sources have identical decompressed bytes, sizes and SHA-256 | raw_archive_hash_check.json; archived_input_audit.json |
| X annotation IDs, text and row locators | 109 of 109 match raw source | x_annotation_check.json |
| TikTok annotation IDs, text and row locators | 100 of 100 match raw source | tiktok_annotation_check.json |
| Tokopedia annotation IDs, text and row locators | 85 of 85 match raw source | tokopedia_annotation_check.json |
| Integrated written master | All 314,476 keys, platform labels and original-text hashes agree with source inputs; no missing or duplicate keys | integrated_master_check.json |
| Master shards | All 16 indexed gzip shards have matching hashes and row counts | integrated_master_check.json |
| Blank-text and unsupported demographic verification in master | Zero blank master records; zero true age/target-switcher verification flags | integrated_master_check.json |
| TikTok reply structure | All 699 exported replies have their referenced parent in the export | tiktok_annotation_check.json |
| Earlier downloadable archive | 1,949 files, CRC passes, byte size and SHA-256 match documented prior release | independent_input_audit.json |

The master is an inventory across retained scopes. It contains broad international and adjacent-product candidates, marketing, service-only text, and uncertain material. The successful identity/text check does not make every record eligible consumer evidence. Its 314,476 rows reconcile as earlier written store 298,846 + new X 12,990 + nonblank TikTok 2,372 + nonblank Tokopedia 263 + five earlier nonoverlapping brand X excerpts.

## Secondary interpretation review

The QA agent examined the originals and existing interpretations for 15 seeded X annotations, 20 seeded TikTok annotations, and 20 seeded Tokopedia annotations. This was **nonblind secondary semantic review**, not a blind coding exercise. No material overclaim was found in those 55 checked entries. An additional 20 uniformly selected X records were independently described to expose the gap between broad keyword relevance and consumer purchase evidence; these readings are in x_secondary_relevance_sample.json. The later-added full-text X legacy-overlap case was also checked and is correctly described as imported Pasta Del Capitano to unspecified Pepsodent, not a confirmed Pepsodent Premium-to-Basic transition.

The sampled X records include retailer advertising, giveaways, brand/fan promotion, foreign deals, figurative language, news, and nonoral uses of toothpaste. Therefore even a dental-anchor match cannot be described as an eligible first-person purchasing account. The X agent refined candidate flags after close reading and qualified repeated advertising-style wording without asserting an independently authenticated commercial origin.

Reviewed TikTok examples correctly distinguish intention from completed switching; household use from payer identity; children's contexts from adult purchasing; unknown video context from named product evidence; and clinical self-attribution from verified effect. The household-funded Sensodyne versus self-funded kos-price example is useful mechanism evidence but does not authenticate age, an actual paid price, or a subsequent Basic purchase.

Reviewed Tokopedia examples correctly distinguish receipt/packing satisfaction from performance, ratings before use from outcomes, explicit repurchase from intent, and promotion interest from price dependence. The agent screened the full 266 latest texts and supplied 85 close-reading annotations; these are different levels of reading. Gift/bonus wording is not automatically a mandatory review incentive. Gimmick listing titles are flagged without inferring free receipt; one explicit free-Pepsodent statement is identified as such.

## Corrections resolved during QA

1. A preliminary QA calculation counted a missing reviewTime as a disagreement. The corrected latest Tokopedia accounting is 198 records with both fields, 186 differing calendar days, and 68 missing reviewTime. Raw sources were never modified. Missing and conflicting values remain distinct.
2. Tokopedia source metadata now uses portable filename/locators rather than relying on scratch paths for provenance.
3. Gimmick title context is separated from explicit free-product receipt and unverified review incentives.
4. Advertising-style copied wording is qualified; pattern resemblance is not proof of the original advertisement or paid sponsorship.
5. X annotations increased from 108 to 109 after a supplementary legacy-overlap case was added; all 109 source matches were rechecked. The combined new annotation count is therefore 294, not 293.

## Synthesis and primary-research check

The new teaching synthesis and decision brief were examined for claims proportional to evidence. They preserve rival household, benefit, affordability, availability, rational-Basic and metric-definition explanations; they do not select a final strategy. The mix-share examples are explicitly hypothetical arithmetic with comparable-period assumptions. Price/gram and household usage examples are scenarios rather than measured consumption, dosing advice, or forecasts. No causal discount effect, population prevalence, retention rate, incremental lift, ROI, or clinical comparative efficacy is claimed from the corpus.

The interviewer screener and long guide were examined for neutral actual-event wording. They permit unknown variant, payer and paid price; distinguish dependent users from purchasers; allow satisfied Basic and durable Premium as counterexamples; and separate retrospective case-period accounts from current experiences. Counts of pilot/interview participants are proposed starting points, not completed fieldwork or saturation claims. The kit includes no fabricated respondents.

Specific TikTok IDs and zero-based raw locators 1861, 2216, 681 and 2012 cited by the synthesis match the immutable source. Individual source UTC timestamps and Jakarta case-period calendar slices require explicit timezone labeling; Tokopedia reviewDate remains an unverified source field.

## Important remaining limits

* All source records remain unauthenticated public or actor-export observations; source truth and authors' identities are not established by checksum verification.
* No verified 18–30 Pepsodent Premium-to-Basic purchase sequence exists in the public corpus.
* Candidate tags are transparent screening rules with false positives/negatives, not a validated population classifier. No universal accuracy percentage is reported.
* Qualitative selections include purposive mechanism enrichment and counterexample searches. Their theme counts must not become population prevalence.
* Current listings do not establish historical paid prices or local shelf stock. Historical flyers show specified offers, not nationwide availability.
* International Amazon and incentivized trial/campaign sources retain separate applicability limits; they must not dominate a pooled Indonesian consumer statistic.
* All available substantive context can be transferred, but unavailable original PDFs or unexported chat messages cannot be recreated. The session handoff is a substantive reconstruction, not a verbatim platform export.

Final archive structure, lossless legacy-part coverage, manifest, fresh-extraction verification and Filebin transfer require their own release checks. This analysis QA does not claim to have checked a not-yet-built upload.

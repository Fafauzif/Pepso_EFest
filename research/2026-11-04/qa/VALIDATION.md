# Validation scope — 4 November context overlay

This package separates preservation/integrity checks, local code checks and unverified empirical/account behaviour. None of the checks below creates respondents, validates mechanisms or executes Google Forms in the user's account.

## Checks performed during assembly

| Check | Result / scope |
| --- | --- |
| Prior 3 November corpus/archive reconciliation | Existing verifier passed for 314,476 unique written keys, platform counts, eleven archived user-run inputs and five reconstructed legacy logical files. No new collection. |
| Original indexed source preservation | Comparison against the clone's pre-update MANIFEST found only the six deliberately changed root/context documents; no baseline indexed file missing. All prior indexed data/source bytes were unchanged. MANIFEST itself is refreshed separately. |
| Exact new uploaded files | Mentoring PDF and user-submitted v1.1 script copied byte-for-byte; source register contains byte counts and SHA-256. CRLF of the submitted script is preserved. |
| Additional retrieval replay | Reproduced 27,770 non-Amazon searched records; hit counts 123/1065/290/138; fourteen selected excerpts. Hits are not prevalence. |
| Current script | Syntax check and rerun in its final repo directory passed 184 local mock assertions, including 126 constructed routing combinations. |
| Script/copy consistency | Code.gs and COPY_PASTE.txt have identical bytes. v1.1.1 is current; no openForPilot/launchSurvey functions. |
| Active navigation | Relative links in updated root entry points and active new Markdown checked; archive snapshots deliberately keep their original-location links. |
| Overlay integrity | Payload file hashes/sizes are listed in release/CONTEXT_UPDATE_2026-11-04.json and checked by the new verifier. The index excludes its own hash. |
| Complete repository integrity | Updated MANIFEST and the existing verify_final_release.py / verify_package.py are run before delivery. These are integrity/provenance checks. |
| Extraction | ZIP entries are relative, have no parent traversal/outer repo folder, and contain only the indexed overlay plus its index. Fresh extraction is checked against the payload hashes. |
| Archive | ZIP CRC is checked; no .git, credentials, real contact data, primary responses or redundant full corpus is included. |

## Local script checks are not live tests

The mocked Google-service suite covers idempotent creation, one-shot opening, screenouts, comparison routing, recovery from partial creation and the two reported failures, matching-destination preservation, raw-response/manual-review preservation, pair eligibility, flags and derived-sheet escaping. Its mock was corrected after the second actual runtime report: no destination now throws instead of returning null.

Unverified here: successful actual v1.1.1 execution, Google authorization/account policy, service latency/quotas, real respondent access/UI rendering, time to complete, respondent comprehension and actual survey response quality. No new success log or form URL was supplied after the last fix. Test counts should never substitute for those checks.

## Remaining substantive limits

- No actual primary response, interview or target-switcher sequence was added.
- New excerpts are purposive, often share a thread, and retain unknown demographic/price/variant fields.
- Earlier 294 annotations and 314,476 retained record counts are unchanged.
- Convenience survey plans do not establish population prevalence, causal allocation, ROI, regular-price retention or health outcomes.
- The user likes the buying-situation architecture and the second insight. No final concept or execution was selected or validated.
- This is a detailed reconstruction, not a verbatim chat export. Original v1.0 exact full source is unavailable locally; the exact submitted v1.1 source and current v1.1.1 are retained.
- No repository remote check after the original clone, push, publication, participant contact, paid run or competition submission occurred.

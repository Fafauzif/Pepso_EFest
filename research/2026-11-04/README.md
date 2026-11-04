# 4 November 2026 — context, insights and survey update

This folder records all substantive additions from the visible chat: new analysis of existing evidence, evolving strategy thinking, the survey-first research plan, usable script artifacts and both actual runtime failures. No new primary data or final selected strategy is implied.

## Reading order

1. [Detailed session handoff](context/SESSION_HANDOFF.md)
2. [Latest buying situations and pillars](synthesis/BUYING_SITUATIONS_AND_PILLARS.md)
3. [User direction and decision register](context/DECISIONS_AND_LIMITS.md)
4. [Survey method and question map](SURVEY_METHOD_AND_QUESTION_MAP.md)
5. [Current one-shot Apps Script setup](survey_apps_script/START_HERE.md), [Code.gs](survey_apps_script/Code.gs), and [exact questionnaire](survey_apps_script/KUESIONER.md)
6. [Visible conversation record](context/SESSION_RECORD.md)
7. [Original insight stress test](INSIGHT_STRESS_TEST.md) and [first pillar proposal](THREE_PILLAR_PROPOSAL.md) — useful history; the latest synthesis controls pillar 2.
8. [Runtime reports](sources/USER_RUNTIME_REPORTS.md) and [exact uploaded-source register](sources/SOURCE_REGISTER.json)

The [next-chat prompt](context/NEXT_CHAT_PROMPT.md) provides a concise restart. The full reasoning lives in the documents above. Prior research remains under ../2026-11-03; this folder does not duplicate the full corpus.

## Evidence and reproducibility

[synthesis/INSIGHT_SOURCE_EXCERPTS.jsonl](synthesis/INSIGHT_SOURCE_EXCERPTS.jsonl) contains fourteen purposive source-linked excerpts, not fourteen new independently verified consumers. [Screening counts](synthesis/INSIGHT_SCREENING_COUNTS.json) are overlapping lexical retrieval hits, not mechanism prevalence. The old 294-annotation set remains unchanged.

```bash
python research/2026-11-04/scripts/replay_insight_retrieval.py
node research/2026-11-04/survey_apps_script/test-survey.cjs
python scripts/verify_context_update_20261104.py
```

Run commands from the repository root. The replay uses the existing portable shards. The Node tests are local mocks, not a Google-account run. [Validation notes](qa/VALIDATION.md) distinguish checks actually performed from remaining uncertainty.

## Sources and history

The exact uploaded mentoring PDF and user-submitted v1.1.0 script are under sources/, with hashes and source IDs. The current code is v1.1.1. Earlier v1.0's complete exact source is not available as an untouched local snapshot; do not claim it was preserved byte-for-byte. Its known flow/failure and delivered artifact identity are recorded. The submitted v1.1.0 and current v1.1.1 sources are available exactly.

archive/root_before_this_chat preserves the original root/current/combined context and manifest as read from clone commit 59f28ef. archive/pre_handoff preserves the incremental in-chat state before consolidation. These are historical snapshots; their internal relative links refer to their original locations, not their archive locations.

No repository credentials, .git history, other account projects, contacts, survey responses or authenticated sessions are included. Keep this context within the authorized team.

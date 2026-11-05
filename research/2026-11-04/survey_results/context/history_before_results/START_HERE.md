# Start here — latest continuation, 4 November 2026

Private E-Fest team use. This reading order supersedes the old status/planning directions where specifically updated. Original source/data claims retain their own limits.

## Read in this order

1. [Current state](context/CURRENT_STATE.md) — user direction, current artifact, no-success-yet status and evidence boundaries.
2. [4 November handoff](research/2026-11-04/context/SESSION_HANDOFF.md) — detailed reasoning and conversation continuity.
3. [Buying situations and pillars](research/2026-11-04/synthesis/BUYING_SITUATIONS_AND_PILLARS.md) — latest second-pillar refinement.
4. [Decision register](research/2026-11-04/context/DECISIONS_AND_LIMITS.md) — support versus preference versus proposal, and superseded plans.
5. [Survey method/question map](research/2026-11-04/SURVEY_METHOD_AND_QUESTION_MAP.md) and [actual script/setup](research/2026-11-04/survey_apps_script/START_HERE.md).
6. [3 November handoff](research/2026-11-03/closure/context/SESSION_HANDOFF.md), [diagnosis](research/2026-11-03/closure/synthesis/DIAGNOSIS_AND_TEACHING.md), [hypothesis matrix](research/2026-11-03/closure/synthesis/HYPOTHESIS_MATRIX.md) and [evidence ledger](research/2026-11-03/closure/synthesis/EVIDENCE_LEDGER.md) when grounding analytical claims.
7. [Original master](context/E_Fest_2026_Pepsodent_Master_AI_Context_Pack.md) for case, guidebook, original business intuition and mentoring methods. Historical untested portraits remain illustrations.

For a single combined context document, [CONTEXT_LATEST.md](context/CONTEXT_LATEST.md) includes the current state, new detailed handoff/refinement/method, previous session handoff and complete original master. This is intentionally long; the modular reading order is easier for bounded tasks. Raw/source reports still govern quantitative claims.

## What changed in this chat

The user particularly liked selective personal-care involvement: a detailed skincare routine can coexist with casual toothpaste choice. The current situations are preference not controlling the basket; toothpaste not earning extra spend; and a valued product not getting replaced. These can overlap and are not age-exclusive or validated segments.

Immediate primary work is survey-only for the executive summary, possibly 40–60 respondents; interviews may follow for the proposal. No split-sample experiment is in the form. No survey responses or interviews have been supplied. The old interview-first order does not block current work.

Current script is v1.1.1. Paste it into the SAME Google Apps Script project and run createSurvey once; it recovers saved assets, opens forms and prints SHARE_THIS_LINK. No pilot/launch steps. Two real errors were fixed, but no successful latest Google run was reported. Preserve this distinction from local mock tests.

## Install and verify

The ZIP is an overlay for the existing repository, not a standalone corpus. Follow [INSTALL_CONTEXT_UPDATE.md](INSTALL_CONTEXT_UPDATE.md). The earlier [GitHub Desktop guide](release/INSTALL_WITH_GITHUB_DESKTOP.md) remains useful for repository review/commit mechanics, but old Filebin/full-release instructions are historical.

```bash
python scripts/verify_context_update_20261104.py
python scripts/verify_final_release.py
python scripts/verify_package.py
node research/2026-11-04/survey_apps_script/test-survey.cjs
```

The 314,476 all-scope written records and 294 prior annotations remain unchanged. Source/demographic/date/incentive limitations remain. Do not add new excerpts to the corpus count or assume primary respondents already exist. Integrity checks and mocked API tests do not authenticate consumers, clinical effects or live Google account behaviour.

## Resume prompt

> Read AGENTS.md, START_HERE.md and context/CURRENT_STATE.md, then the 4 November SESSION_HANDOFF, BUYING_SITUATIONS_AND_PILLARS, DECISIONS_AND_LIMITS and SURVEY_METHOD_AND_QUESTION_MAP. Use Apps Script v1.1.1 as the current base and read USER_RUNTIME_REPORTS before debugging. Preserve the survey-only immediate constraint, one-shot createSurvey preference, selective personal-care insight and competing explanations. No successful latest Google run or primary responses have been supplied yet. No final strategy selected. My next task is [task].

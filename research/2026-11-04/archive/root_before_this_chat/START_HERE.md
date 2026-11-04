# Start here — Pepsodent complete research handoff

**Latest: 3 November 2026, Asia/Jakarta. Private team use.** Secondary research, public data collection and returned user-run Apify exports are integrated. The next task is hypothesis testing and preparation for primary research. No final solution, verified target-switcher sample, primary interviews or causal allocation has been established.

## Reading order

1. [Current project state](context/CURRENT_STATE.md): accepted decisions, scope, counts and boundaries.
2. [Complete substantive session handoff](research/2026-11-03/closure/context/SESSION_HANDOFF.md): questions, decisions, tools, corrections, returned runs and continuity.
3. [Decision brief](research/2026-11-03/closure/synthesis/DECISION_BRIEF.md): what the evidence changes and what remains unknown.
4. [Diagnosis and teaching](research/2026-11-03/closure/synthesis/DIAGNOSIS_AND_TEACHING.md) and [hypothesis matrix](research/2026-11-03/closure/synthesis/HYPOTHESIS_MATRIX.md).
5. [Indonesian primary-research kit](research/2026-11-03/closure/primary_research/README.md): start with the screener, pilot and purchase timeline.
6. [Earlier full research report](research/2026-11-03/REPORT_FULL.md): retained ~29,000-word research and methods pack, including literature/retail/campaign/history/tool annexes.
7. [Original master context](context/E_Fest_2026_Pepsodent_Master_AI_Context_Pack.md): historical case, guidebook, mentoring and teaching material. Its old status statements are superseded by current state, not its original case text.

For one large context file, [CONTEXT_LATEST.md](context/CONTEXT_LATEST.md) combines current state, this session handoff and the complete original master. Separate reports/data still need reading when making analytical claims. Cloning does not import a chat or authentication; these files provide the project context.

For one assembled research/teaching document, read [COMPLETE_RESEARCH_REPORT.md](research/2026-11-03/closure/COMPLETE_RESEARCH_REPORT.md). It places the current findings before the retained historical report and annexes.

## Data and methods

- [Portable written-record inventory](research/2026-11-03/closure/integrated/README.md), [counts/shard index](research/2026-11-03/closure/integrated/INVENTORY.json).
- [X findings](research/2026-11-03/closure/x/FINDINGS.md), [TikTok findings](research/2026-11-03/closure/tiktok/FINDINGS.md), [Tokopedia/Shopee findings](research/2026-11-03/closure/tokopedia/FINDINGS.md).
- [Exact uploaded-source register](research/2026-11-03/closure/raw/UPLOAD_REGISTER.json), [independent QA](research/2026-11-03/closure/qa/INITIAL_QA.md).
- Earlier raw sources, source histories, source-specific clean data, original keyword controls, literature and tools remain in their existing dated folders. Do not add overlapping subsets together.

**314,476 retained written platform records across all scopes** is an archive inventory, not a verified consumer sample. It includes286,706internationalAmazoncandidates, marketing, irrelevant candidates and adjacent categories. The earlier six-post X sample adds only five nonoverlapping brand excerpts. Platform-specific counts and eligibility must accompany any analytical summary. All target-age/Pepsodent Premium-to-Basic verification flags remain false.

## Install, verify, continue

See [GitHub Desktop installation](release/INSTALL_WITH_GITHUB_DESKTOP.md). The new master data work without restoring legacy exports. Five large legacy logical files are represented by exact lossless parts, indexed in release/LARGE_FILES.json, to keep Git files below45MiB. Optional restore steps are documented; do not force-add rebuilt large files or databases.

```bash
python scripts/verify_final_release.py
python scripts/verify_package.py
python scripts/query_corpus.py --platform tiktok --contains sensodyne --limit 3
```

These are integrity and reproducibility checks, not validation of representativeness or clinical claims. Full methodological limits, date-quality corrections and sampling methods are retained. No more paid/bulk collection is required before beginning the proposed primary-research pilots.

## Prompt for a new assistant

> Read AGENTS.md and the START_HERE reading order. Understand the case, current state, full session handoff, decision brief, hypothesis matrix and primary-research kit. Check the actual data inventory and source limits before making claims. Preserve case facts, observations, hypotheses, illustrations and primary data as separate categories. No final solution or causal allocation is selected; no primary interviews exist. Help with [next task].

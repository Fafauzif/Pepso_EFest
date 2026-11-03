# Latest research release

The assistant-led deep research release is in [research/2026-11-03/README.md](research/2026-11-03/README.md). Start there for the teaching report, actual collected data, expanded plan, source-specific limitations and optional user-run Apify JSONs. No final strategy selected; no Apify or paid runs executed.

The original handoff below remains historical. Run `python3 scripts/verify_package.py` for the legacy300keyword controls and currentmanifest; it explicitly reports the exacthash-verified Gitline-ending normalization. Run the research inventory validator as documented in the newreleaseREADME for the newdata.

# Pepsodent E-Fest research handoff

Packaged 3 November 2026 (Asia/Jakarta). Research stage: broad preliminary exploration. No solution selected.

## Start here

1. Read `context/CURRENT_STATE.md` for the latest decisions, evidence and gaps.
2. Read `context/E_Fest_2026_Pepsodent_Master_AI_Context_Pack.md` for the complete original case, guidebook, learning analysis, mentoring notes and BCC Hub.
3. Read `docs/CLEANING.md`, `docs/DATA_DICTIONARY.md` and `docs/QUALITY_REPORT.md` before analysing data.
4. Use `data/clean/keywords_unique.csv` or its JSON equivalent. Raw captures remain in `data/raw/`.

For one large context file, `context/CONTEXT_LATEST.md` combines the new state and complete original master. Reading both that file and the original is unnecessary.

## Resume prompt

> Clone this private repository: [insert repo URL]. Read AGENTS.md, README.md, context/CURRENT_STATE.md, the original master context pack, and the cleaning/data-dictionary documents. Confirm the source coverage and unresolved data issues. My task now is [insert task]. Distinguish organizer case facts, external estimates, AI hypotheses, fictional examples and primary observations. Preserve alternatives before choosing a diagnosis.

A private clone requires access in the new environment. Read files after cloning; do not assume repo access imports a chat or signed-in service session.

## Contents

- 300 cleaned keyword observations in CSV and JSON, including all missing-value distinctions and provenance.
- 300-keyword unique view, duplicate/conflict diagnostics and quality flags.
- Three unchanged pasted raw files, the unchanged initial master MD, and the supplied business-intuition PDF.
- Separate searchable transcripts extracted from the master: case, preliminary guidebook, mentoring notes, BCC Hub and embedded learning manuscript.
- A reproducible Python cleaning script, dictionary, cleaning ledger, quality report and file checksums.
- Latest substantive chat handoff, optional historical tool configurations, source register and missing-input record.

## Rebuild and validate

Python 3.10+; no third-party packages required:

```bash
python3 scripts/clean_keywords.py
python3 scripts/verify_package.py
```

Rebuilding intentionally replaces generated `data/clean/*` and `docs/quality_report.json`. Add or change raw sources only with a corresponding parser/source-register update. Checksums describe this release and will need refresh after authorised edits.

## Data limits

138 positive volumes, 11 explicit zero volumes, 107 blanks and 44 `n/a` values. Indonesia was requested but is not visibly verified in the captures. Currency is explicitly IDR only in source 03. Four large CPC values are flagged without alteration. Trends were not recovered. No sales, consumer sentiment or age-specific switching conclusions follow directly from these keyword estimates.

`Pasted text (2)(1).txt` remains unavailable. Original case/guidebook/mentoring PDF bytes are not included; their embedded transcripts are supplied as authorised. See `docs/MISSING_INPUTS.md`.

## Repository handling

Keep this repo private and restrict access to registered team members: the original context pack records organizer confidentiality requirements. This ZIP does not set repository visibility or grant access. It has not been published or submitted. Original third-party materials retain their rights; no open-source license is asserted over them.

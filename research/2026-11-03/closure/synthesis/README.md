# Final-session synthesis

Read [DECISION_BRIEF.md](DECISION_BRIEF.md) first, then [DIAGNOSIS_AND_TEACHING.md](DIAGNOSIS_AND_TEACHING.md). The latter is the updated diagnosis/teaching layer; the earlier full research report and source annexes remain available two directories above.

The [hypothesis matrix](HYPOTHESIS_MATRIX.md) and [CSV](HYPOTHESIS_MATRIX.csv) distinguish eleven mechanisms, their predictions, rivals, falsifiers and primary tests. The [evidence ledger](EVIDENCE_LEDGER.md) and [CSV](EVIDENCE_LEDGER.csv) link 31 assessments to retained source records or documents. These assessments are analyst synthesis, not verified prevalence or causal effects.

Run `python3 research/2026-11-03/closure/synthesis/build_synthesis_tables.py` from the repository root to rebuild the two table formats from the explicitly authored assessments. This does not collect data or overwrite original sources. The Markdown teaching reports are authored documents; the script does not regenerate them.

Platform cleaning, sampling, annotations and QA live in sibling `x/`, `tiktok/`, and `tokopedia/` directories. Primary-research instruments are in `../primary_research/`. No fieldwork results or final chosen strategy have been added.

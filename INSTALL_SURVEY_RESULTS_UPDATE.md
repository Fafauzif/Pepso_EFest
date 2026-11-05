# Install the survey results context update

1. Keep this ZIP outside your existing Pepso_EFest checkout and extract its contents into the repository root. It adds research/2026-11-04/survey_results and replaces only README.md, START_HERE.md, AGENTS.md, context/CURRENT_STATE.md and context/CONTEXT_LATEST.md. Previous versions of those five files are preserved under the dated results context/history_before_results directory.
2. Review the diff. New survey results supersede old no-responses status, not original evidence caveats.
3. Run `python scripts/verify_survey_results_update.py` from the repository root. This verifies packaged file integrity and the principal arithmetic; it does not authenticate survey answers or demonstrate effectiveness.
4. Inspect the analysis, Word document, source ledger and model before choosing what to commit. The ZIP contains no .git directory, credentials, raw survey, contact data, review ratings or critique conversations.
5. Add team/member details, official permitted logos and required declaration documents yourself before any competition submission. The organizer asks for a final PDF; this task produces the requested editable DOCX, not an automatic submission.

The package is an overlay against the recorded base commit, not a promise to reconcile later remote edits. If your branch changed those root files meanwhile, merge the new status rather than overwriting unrelated changes.

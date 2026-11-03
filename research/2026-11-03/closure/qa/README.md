# QA reading order

1. [ANALYSIS_QA.md](ANALYSIS_QA.md): source identity/text checks, selected semantic review, corrected issues and analytical limits.
2. [PACKAGE_QA.md](PACKAGE_QA.md): independent preliminary-stage coverage, lossless parts, size/path/link checks, build-order issue and final verification boundary.
3. [INITIAL_QA.md](INITIAL_QA.md): initial input risks and the corrected missing-date-versus-conflict distinction.

Machine-readable checks include input hashes/counts, archived input equality, per-platform annotation fidelity, the integrated master comparison, preliminary stage/part coverage, Markdown link scan, and limited secret-pattern review. `offline_rebuild_check.json` is a separately labeled integration-owner execution record.

To independently recompute upload counts and original-byte hashes from the portable raw archives:

```bash
python research/2026-11-03/closure/qa/audit_inputs.py --input-dir research/2026-11-03/closure/raw/user_runs --output /tmp/pepsodent_input_audit.json
```

The script also accepts an optional `--previous-zip` when the earlier downloadable archive is available. It reads both original and losslessly gzipped input files and never writes to sources. The initial screening counts it checks are not consumer/sample prevalence.

For final release integrity, run `python scripts/verify_final_release.py` after extracting the delivered package. Do not rerun a mutating legacy inventory generator and then expect an unchanged packaged manifest. New release content requires a new manifest.

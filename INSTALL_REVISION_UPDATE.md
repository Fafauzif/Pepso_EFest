# Extract into the repo root and choose Replace all

1. Keep the ZIP outside the checkout; open it and extract its contents directly into Pepso_EFest (the folder containing README.md and .git). There is no extra enclosing folder. Choose Replace all for existing files.
2. This replaces root context/entry points, the old active survey analysis/document, aggregate JSON, financial entry points and verifier. It adds the dated current revision with production sources, figures, financial model, source register and survey aggregates. Previous active context/model/analysis files are preserved under the new revision/history_before_revision directory.
3. Run `python scripts/verify_revision_update.py`. Review changes in GitHub Desktop when convenient.
4. No deletion is required. An overlay cannot remove old files; old historical figures and dossiers remain, explicitly superseded by START_HERE and dated README files. Old global release manifests remain historical; use this update's verifier for the overlay.
5. Fill cover/team names and official logos yourself. This package contains no raw responses, contacts, credentials, .git, or automatic publication/submission.

Baseline: cloned Pepso_EFest commit fddbdb9. If the same active files were independently edited after this baseline, preserve those edits before choosing Replace all.

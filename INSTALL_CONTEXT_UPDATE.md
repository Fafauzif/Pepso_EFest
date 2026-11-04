# Install the 4 November context update

This ZIP is an overlay for your EXISTING Pepso_EFest clone, based on commit 59f28effdf47dbdc5feea33458998bba03e3227f. It contains additional context/code and refreshed context entry points, not the full research corpus. You do not need a new clone or another data download.

## Extract into the existing repo

1. Keep the downloaded ZIP outside the repository.
2. Back up any local edits you made to the root context files listed below since the clone. The package preserves our baseline and prior in-chat notes, not unseen edits on your computer.
3. Extract/copy the ZIP's CONTENTS directly into the existing Pepso_EFest root, alongside its current AGENTS.md, context/, research/ and scripts/. The archive has no outer Pepso_EFest folder, so do not add a second nested repo directory.
4. Allow replacement of the listed context files. Existing raw data and the original master are not included for replacement. No deletions are required or performed by extracting the overlay.
5. Open START_HERE.md, then context/CURRENT_STATE.md. Review changes in GitHub Desktop; commit/push yourself if desired. The assistant has not pushed anything.

If your computer automatically creates an outer directory named after the ZIP, copy the contents inside that directory into the existing repo root. Do not replace the entire existing repository folder with the smaller overlay folder.

## Existing files replaced

- AGENTS.md
- README.md
- START_HERE.md
- CHANGELOG.md
- context/CURRENT_STATE.md
- context/CONTEXT_LATEST.md
- MANIFEST.sha256

## Added content

- research/2026-11-04/: detailed handoff, visible request record, decisions/supersessions, current insight/strategy synthesis, methodological reasoning, exact attachments and error reports, fourteen selected evidence excerpts/replay, current one-shot Apps Script v1.1.1 and local tests, and history snapshots.
- scripts/verify_context_update_20261104.py
- release/CONTEXT_UPDATE_2026-11-04.json
- This installation note.

The exact payload paths and hashes are in the release JSON. The updated full-repository MANIFEST hashes the previous indexed files plus new context/code, excluding itself and the overlay index to avoid circular checksums. The overlay index hashes the updated MANIFEST and all payload files except itself.

## Optional verification

From the repository root, using Python 3.11+:

```bash
python scripts/verify_context_update_20261104.py
python scripts/verify_final_release.py
python scripts/verify_package.py
```

Optional, with Node.js:

```bash
node research/2026-11-04/survey_apps_script/test-survey.cjs
```

The first command is a small overlay checksum/content check. Full release verification also needs the existing corpus and legacy parts; this overlay alone cannot pass it. Tests prove file integrity and local code behaviour, not questionnaire validity, a successful live Google run or empirical findings. Questionnaire pretesting and a Google success log have not been supplied.

No commands are required simply to read the context or copy the script into Google Apps Script. Do not commit contact details or real survey-response exports by default. Keep the repo private for authorized team use.

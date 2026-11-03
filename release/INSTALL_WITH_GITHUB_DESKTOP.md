# Extract and update with GitHub Desktop

The user confirmed the private team repo has no newer edits since the supplied version. The final remote HEAD/main check matched423cce08921b611fd01fbf6d25a0f86b65986f76. This package does not set repository visibility or push remotely.

1. Download the ZIP from the supplied Filebin link and save it outside the local Git clone. The Filebin link is temporary; keep a local copy.
2. Extract the ZIP outside the clone. Open the enclosed **Pepso_EFest** folder.
3. Copy that folder's **contents** into the existing local **Pepso_EFest** repository root. Accept replacement of overlapping files. Avoid a nested Pepso_EFest/Pepso_EFest folder. The existing .git directory stays in place; this ZIP contains no .git directory.
4. Open GitHub Desktop and review the Changes tab. Expect original context controls plus new research/closure materials, archive parts, scripts and updated documentation. The root private/team guidance remains in place.
5. Optional integrity check from the repository root: `python scripts/verify_final_release.py` followed by `python scripts/verify_package.py`. Python3.11+ is required for the new standard-library checks and restore/rebuild scripts (hashlib.file_digest). If the environment lacks the Asia/Jakarta timezone database for rebuilding, use an environment with IANA tzdata; verification itself does not need a timezone lookup.
6. Commit with a message such as **Complete Pepsodent research integration and primary-research handoff**, then Push origin. Keep the repository private and restricted to the authorized team.

There are no required deletions from the verified original baseline. An extract/replace overlay does not delete unrelated local files. Do not commit the outer ZIP, downloaded release copies, environments, credentials or rebuildable SQLite files. If the clone had an unreported earlier full release already extracted, optional restored exports are now ignored; review any already-tracked superseded large copies separately rather than deleting them blindly.

## File sizes and legacy archives

Every physical file in this delivery is below45MiB. This is below GitHub's50MiB warning and100MiB hard ordinary-Git limit (GitHub Docs checked3November2026). The outer download ZIP can exceed100MiB because it is not the file you add to the repository. Source: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github

New integrated JSONL.gz shards are independently readable. Five earlier compressed logical files are retained as exact32MiB-or-smaller byte parts under release/large_file_parts/, with size/hash mapping in release/LARGE_FILES.json. These are ordinary Git files; LFS is not needed. They preserve the earlier data byte-for-byte while avoiding large Git blobs. Existing source reports may link to those logical legacy paths; use the mapping/restore command if following those particular links. Reading the new analysis does not require restoration.

To inspect or restore older logical files locally:

```bash
python scripts/restore_large_files.py --list
python scripts/restore_large_files.py
```

The script verifies every part and reconstructed SHA-256 before replacing a file. A changed existing file causes refusal. Restored large paths are Git-ignored; never force-add them. Those local files may exceed45MiB, but the tracked portable parts remain small. Legacy rebuild scripts need appropriate restored inputs and optional dependencies as documented in their source folders.

## Resume in another chat

Supply the private repository URL and access through the tools available in that chat. Ask the assistant to read AGENTS.md and START_HERE.md, then give it the next task. It will have the files and substantive project handoff; it will not inherit this chat's tool sessions or unseen conversation state.

## Validation order for maintainers

Some legacy validators are generators: synthesis/validate_inventory.py rewrites DATA_INVENTORY.json and timestamps. Run those before building a release. The final manifest checks must run after all generated outputs are frozen. Running a generator after packaging legitimately invalidates the packaged checksums; rebuild the release rather than silently editing a checksum.

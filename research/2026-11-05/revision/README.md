# Current revision

See the root START_HERE.md and context/CURRENT_STATE.md.

Reproduction with Python3 and python-docx/matplotlib/numpy installed:

- `python research/2026-11-05/revision/finance/model.py` regenerates financial JSON/CSV.
- `python research/2026-11-05/revision/build/make_assets.py` redraws exact charts from current values. Concept assets are retained and never recreated as evidence.
- `python research/2026-11-05/revision/build/write_content.py` writes manuscript/references JSON.
- `python research/2026-11-05/revision/build/build_doc.py` rebuilds the editable document.

Charts and manuscript reflect the recorded survey snapshot; update aggregate-linked values and narrative together when responses change. Survey replication requires the private workbook; it is excluded. The delivered DOCX was rendered and inspected; local rebuilds require a new render/page-count check.

#!/usr/bin/env python3
"""Validate the shipped, deliberately unpopulated primary-research instruments."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    schemas = json.loads((root / "templates" / "SCHEMAS.json").read_text(encoding="utf-8"))["columns"]
    results = []
    for filename, expected in schemas.items():
        with (root / "templates" / filename).open(newline="", encoding="utf-8") as stream:
            rows = list(csv.reader(stream))
        assert rows and rows[0] == expected, f"Header mismatch: {filename}"
        assert len(set(expected)) == len(expected), f"Duplicate columns: {filename}"
        assert len(rows) == 1, f"Template contains response rows: {filename}"
        results.append({"file": "templates/" + filename, "columns": len(expected), "response_rows": 0})
    broken = []
    for md in sorted(root.glob("*.md")):
        for target in re.findall(r"\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
            if "://" not in target and not target.startswith("#"):
                path = target.split("#", 1)[0]
                if path and not (md.parent / path).exists():
                    broken.append({"file": md.name, "target": target})
    assert not broken, f"Broken local links: {broken}"
    report = {
        "status": "passed",
        "scope": "instrument kit only; no recruitment, interviews, or primary data collected",
        "templates": results,
        "template_count": len(results),
        "participant_response_rows": 0,
        "local_markdown_links": "passed",
    }
    (root / "KIT_QA.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "templates"}, ensure_ascii=False))


if __name__ == "__main__":
    main()

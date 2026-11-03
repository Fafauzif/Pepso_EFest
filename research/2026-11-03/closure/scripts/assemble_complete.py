#!/usr/bin/env python3
"""Assemble current teaching + retained prior report with portable local links."""
import os,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
C=ROOT/'research/2026-11-03/closure'
DEST=C/'COMPLETE_RESEARCH_REPORT.md'
def move_links(text,source):
    def replace(m):
        prefix,target,suffix=m.groups()
        if target.startswith(('http:','https:','#','mailto:','sandbox:')):return m.group(0)
        path,sep,frag=target.partition('#');absolute=(source.parent/path).resolve()
        if not absolute.exists():return m.group(0)
        return prefix+Path(os.path.relpath(absolute,DEST.parent)).as_posix()+(sep+frag if sep else '')+suffix
    return re.sub(r'(!?\[[^\]]*\]\()([^\s)]+)(\))',replace,text)
def main():
    parts=[('Current decision brief',C/'synthesis/DECISION_BRIEF.md'),('Current diagnosis and teaching',C/'synthesis/DIAGNOSIS_AND_TEACHING.md'),('Competing hypotheses',C/'synthesis/HYPOTHESIS_MATRIX.md'),('Source-linked evidence assessments',C/'synthesis/EVIDENCE_LEDGER.md'),('X source findings',C/'x/FINDINGS.md'),('TikTok source findings',C/'tiktok/FINDINGS.md'),('Tokopedia and Shopee source findings',C/'tokopedia/FINDINGS.md'),('Primary research kit: reading order',C/'primary_research/README.md'),('Complete substantive session handoff',C/'context/SESSION_HANDOFF.md'),('Earlier full research and methods annexes — retained historical release',ROOT/'research/2026-11-03/REPORT_FULL.md')]
    text='# Pepsodent: complete research, diagnosis and continuation report\n\n3 November 2026, Asia/Jakarta. Private team use.\n\nThis assembled report begins with the latest synthesis and user-run export analyses. The earlier full report is retained as the final historical part: its earlier collection counts and statements about Apify are superseded by the current inventory and session handoff. No final strategy, verified target-switcher sample, primary interviews or causal allocation is claimed. This document is generated from the source reports; the original files and provenance remain in the repository. For blank Indonesian fieldwork tools, use primary_research/README.md.\n\n'
    for title,path in parts:
        text+='\n\n---\n\n# '+title+'\n\nSource file: `'+path.relative_to(ROOT).as_posix()+'`.\n\n'+move_links(path.read_text(),path)+'\n'
    DEST.write_text(text)
    print({'path':str(DEST),'words':len(text.split()),'bytes':DEST.stat().st_size})
if __name__=='__main__':main()

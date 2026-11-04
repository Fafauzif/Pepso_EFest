#!/usr/bin/env python3
"""Verify the 4 November overlay. Stdlib only; no network, code execution or mutation."""
from pathlib import Path, PurePosixPath
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/'release/CONTEXT_UPDATE_2026-11-04.json'
def digest(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
 if not INDEX.is_file():raise SystemExit('Overlay index missing. Extract contents into the existing Pepso_EFest root.')
 index=json.loads(INDEX.read_text())
 for item in index['files']:
  rel=PurePosixPath(item['path'])
  assert not rel.is_absolute() and '..' not in rel.parts,rel
  p=ROOT/str(rel)
  assert p.is_file(),f'Missing overlay file: {rel}'
  assert p.stat().st_size==item['bytes'],f'Size changed: {rel}'
  assert digest(p)==item['sha256'],f'Hash changed: {rel}'
 folder=ROOT/'research/2026-11-04'
 source=json.loads((folder/'sources/SOURCE_REGISTER.json').read_text())
 for item in source['files']:
  assert digest(ROOT/item['path'])==item['sha256'],item['path']
 script=(folder/'survey_apps_script/Code.gs').read_bytes()
 assert script==(folder/'survey_apps_script/COPY_PASTE.txt').read_bytes()
 assert b"version: '1.1.1'" in script
 assert b'function openForPilot' not in script and b'function launchSurvey' not in script
 tests=json.loads((folder/'survey_apps_script/TEST_RESULTS.json').read_text())
 assert tests['assertions']==184 and tests['constructedRoutingCombinations']==126
 counts=json.loads((folder/'synthesis/INSIGHT_SCREENING_COUNTS.json').read_text())
 assert counts['non_amazon_records_searched']==27770 and counts['selected_excerpt_records']==14
 assert counts['existing_294_annotation_count_changed'] is False
 base=ROOT/'research/2026-11-03/closure/integrated/INVENTORY.json'
 base_available=base.is_file()
 if base_available:assert json.loads(base.read_text())['written_records_all_retained_scopes']==314476
 print(json.dumps({'status':'passed','overlay_files_checked':len(index['files']),
  'exact_uploaded_sources_checked':len(source['files']),'script_version':'1.1.1',
  'existing_corpus_inventory_available':base_available,
  'scope':'Integrity and handoff structure only; no authenticated Google execution or primary-research validation.'},indent=2))
if __name__=='__main__':main()

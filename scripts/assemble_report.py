from pathlib import Path
r=Path(__file__).resolve().parents[1]/"research/2026-11-03"
annexes=[('Expanded-evidence synthesis', 'synthesis/SCALE_SYNTHESIS.md'), ('Retail data and offers', 'retail/findings.md'), ('Brand and campaign audit', 'brand_campaigns/findings.md'), ('Literature appraisal', 'literature/findings.md'), ('Dated history and public indicators', 'history_publicdata/findings.md'), ('Phase1 consumer methods', 'access_reviews/findings.md'), ('Full retailer review histories', 'scale_lazada/findings.md'), ('Full TryandReview histories', 'scale_reviews/findings.md'), ('Additional campaign records', 'scale_discovery/findings.md'), ('Reddit archive and episodes', 'scale_reddit/findings.md'), ('Python tools and public X tests', 'scale_tools/findings.md'), ('User-supplied repository audit', 'scale_tools/reverse_api_engineer_audit.md'), ('International large-corpus methods', 'scale_amazon/README.md'), ('Independent international corpus QA', 'scale_amazon/QA.md'), ('Reusable corpus architecture', 'scale_pipeline/README.md'), ('Final canonical snapshot', 'scale_pipeline/docs/SNAPSHOT.md'), ('Optional Apify configs', 'apify_handoff/apify_handoff.md')]
body=[(r/"PEPSODENT_DEEP_RESEARCH.md").read_text(),"\n\n# Evidence and methods annexes\n\nPhase1 counts describe the preserved earlier snapshot; final canonical counts govern the release. Do not add overlapping versions together.\n"]
for i,(title,path) in enumerate(annexes,1):
 text=(r/path).read_text()
 if Path(path).parent.name=="synthesis": text=text.replace("(../","(")
 body.append(f"\n\n# Annex {i}: {title}\n\nOriginal report: `{path}`.\n\n"+text)
(r/"REPORT_FULL.md").write_text("\n".join(body))
print("Assembled",len((r/"REPORT_FULL.md").read_text().split()),"words")

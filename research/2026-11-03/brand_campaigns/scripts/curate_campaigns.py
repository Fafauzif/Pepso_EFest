from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parents[1]
lookup={r['id']:r for r in json.loads((ROOT/'source_register.json').read_text())}
# Analyst paraphrases of inspected primary pages; line ranges identify supporting passage.
spec=[
('mission','BC-d5e1419461d7',101,112,None,None,'brand_purpose','Everyday oral health, prevention, accessible education and healthy smiles for everyone.','Mission framing is documented; audience adoption of this meaning is unmeasured.'),
('expert_selection','BC-ee958fd9d4d7',102,109,None,None,'owned_digital','Expert page directs visitors to an external dental self-check and professional design cues.','Existing diagnosis/selection assistance means a new scanner is not automatically novel.'),
('expert_regular_use','BC-ee958fd9d4d7',137,161,None,None,'owned_product_education','Gum product explanation includes sensory freshness and regular twice-daily use.','Continued-use messaging exists; comprehension and adherence remain unknown.'),
('ultra_landing','BC-40524b923c1e',99,121,None,None,'owned_digital','Ultra White combines whiteness and enamel-barrier cues with four variants and a spray.','Beauty and health promises coexist; do not treat all Premium as one product job.'),
('ultra_science','BC-f90637d518ca',99,119,None,None,'owned_video_education','Explainer content differentiates ingredients and notes variable visible change over weeks.','Potential expectation-management question; not evidence that shoppers read conflicting pages.'),
('shade_scan','BC-fefe1dab4203',99,104,None,None,'owned_interactive','A shade-visualization tool lets visitors preview a five-shade whitening appearance.','Simulation is existing brand activity; no efficacy or conversion outcome established.'),
('jfw_event','BC-0ad6b660892a',11,35,'2025-10-30','2025-10-30','experiential_partnership','Ultra White participated in an invitation fashion show with three designers.','Beauty-context repositioning was executed before H1 2026; reach, spend and repeat effects unknown.'),
('jfw_recap','BC-cca4c615e1d5',12,28,'2025-10-30','2025-10-30','organizer_recap','Organizer recap links smiles, confidence, fashion and Maudy Ayunda with Ultra White.','JFW edition name 2026 should not be mistaken for event year 2026.'),
('halodoc','BC-b09931194b68',99,119,'2024-08','2025-07','pack_linked_service','Special-marked participating packs granted a limited consultation discount with separate service fee.','Value-added access is already attempted; the program spans several tiers and is not exclusively Premium.'),
('bkgn2023','BC-f1c1f7b74911',47,64,'2023-09-12','2024-02','health_education_service','Annual program combined professional partners, family brushing education, and a Basic product relaunch.','Health habit activity is part of masterbrand support and not exclusive Premium justification.'),
('bkgn2024','BC-ee1d084f28f8',47,66,'2024-09-12',None,'health_education_digital','Program announced AI-enabled screening, teledentistry, professional partnerships and football affiliation.','Existing AI and expert-access work must be benchmarked before proposing new concepts.'),
('expert_relaunch2024','BC-7bead34a691f',63,67,'2024-04-24',None,'corporate_strategy','Company quarterly update names Sensitive Expert relaunch with upgraded benefits.','A dated innovation action is established; customer response or tier economics is not.'),
('enzim_position','BC-3496c4e001e5',55,95,None,None,'competitor_education','Enzim FAQ promotes no-detergent formulation, saliva-related rationale and multiple pack sizes.','These are manufacturer claims; avoid adopting universal anti-SLS clinical claims as established fact.'),
('sensodyne_position','BC-ba34d1c6fbb1',56,192,None,None,'competitor_selection','Sensitivity is the core problem; additional benefits organize product selection and repeated-use language.','Specialist benefit and freshness/whitening are complements rather than mutually exclusive positions.'),
('sensodyne_deep_clean','BC-6e0b1149c2d9',1,120,None,None,'competitor_product','Deep Clean offers additional foam and freshness alongside sensitivity protection.','Premium brands can promote opposing sensory cues; more foam is not a universal efficacy proxy.'),
('closeup_position','BC-e710a2d281de',1,100,None,None,'competitor_catalogue','Catalogue distinguishes whitening color correction, mineral stain removal and freshness experiences.','Compare by need state and claim, not simply which tube is priced as premium.'),
('oresa_sampling','BC-3698bac3a3fc',42,53,None,None,'sampling_cashback_reviews','Participation required purchase, survey, social interaction and reviews to earn cashback.','Incentivized review and marketplace/social cross-posting bias; 298 displayed reviews are not all organic.'),
('brand_linktree','BC-14c902c8453c',1,100,None,None,'social_link_hub','Brand-named link hub routes users toward promotion participation, a gum check and Shopee.','Identity consistent with branding, but storefront ownership and operator not established.')
]
# Resolve the Linktree row by observed URL, not a guessed ID.
link=next((r for r in lookup.values() if 'linktr.ee' in r['url']),None)
if link:spec[-1]=tuple(link['id'] if i==1 else x for i,x in enumerate(spec[-1]))
rows=[]
for i,(name,sid,start,end,event,enddate,channel,obs,limit) in enumerate(spec,1):
 r=lookup[sid];lines=(ROOT/r['text_file']).read_text().splitlines()
 rows.append(dict(observation_id=f'BCO-{i:03}',topic=name,source_id=sid,url=r['url'],event_or_start_date=event,event_end_date=enddate,collected_at_utc=r['collected_at_utc'],channel=channel,observation_paraphrase=obs,interpretation_boundary=limit,raw_file=r['raw_file'],text_file=r['text_file'],line_start=start,line_end=min(end,len(lines)),historical_status='dated_before_H1_2026' if event else 'current_page_historical_availability_unverified',paid_organic_status='unknown_or_not_applicable',evidence_authority='first_party_statement_or_campaign_record'))
(ROOT/'clean/campaign_observations.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
with (ROOT/'clean/campaign_observations.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows),'curated observations')

"""Build reviewed evidence tables from fetched public scholarly payloads; annotations are analyst judgments."""
import json,csv,re,xml.etree.ElementTree as E
from pathlib import Path
b=Path(__file__).resolve().parents[1]
candidates=json.loads((b/'clean/candidates_unique.json').read_text())
for p in sorted((b/'raw').glob('*.json')):
 try:d=json.loads(p.read_text())
 except:continue
 m=d.get('message',{}) if isinstance(d,dict) else {}
 if isinstance(m,dict) and m.get('DOI'):
  candidates.append({'doi':m['DOI'],'title':' '.join(m.get('title',[])),'authors':'; '.join((a.get('given','')+' '+a.get('family','')).strip() for a in m.get('author',[])),'year':m.get('published',m.get('issued',{})).get('date-parts',[[None]])[0][0],'abstract':m.get('abstract'),'abstract_available':bool(m.get('abstract')),'raw_file':str(p.relative_to(b)),'record_locator':'message','provider':'Crossref'})
lookup={}
for x in candidates:
 k=(x.get('doi') or '').lower()
 if k and (k not in lookup or (not lookup[k].get('abstract') and x.get('abstract'))):lookup[k]=x
# DOI, theme, read level, design/population, key finding, transfer limit, funding
entries=[
('10.1086/651235','choice','abstract','Meta-analysis:63 conditions,50 published/unpublished experiments,N5036','Average choice-overload effect was near zero with substantial variation.','Assortment alone does not establish overload; mixed experimental tasks, not Pepsodent buyers.','Not assessed from abstract.'),
('10.1016/j.jcps.2014.08.002','choice','abstract','Meta-analysis:99 observations,N7202','Choice complexity, task difficulty, uncertain preferences and effort minimization moderated overload.','Moderators sharpen a test; they do not establish which mechanism drives Indonesian downtrading.','Not assessed from abstract.'),
('10.1177/002224378902600206','promotion','abstract','Formal models, simulation and exploratory empirical analysis','Lower average repeat after a deal can arise from temporary recruitment of low-purchase-probability households.','Cohort composition is an alternative to a causal damage effect of discounts; verify comparable cohorts.','Not assessed from abstract.'),
('10.1287/mksc.1030.0040','promotion','abstract','Three field experiments;durables sold through direct-mail catalog','Deeper discounts increased subsequent purchasing for first-time customers but reduced it for established customers.','Counterexample to universal discount pessimism; durables/catalog context is not replenishment toothpaste.','Not assessed from abstract.'),
('10.1177/002224378802500402','promotion','abstract','IRI household scanner panel;regular ground coffee;purchase timing/brand/quantity models','Promotion lift can be separated into brand switching,purchase acceleration and quantity changes.','Reported coffee-specific proportions cannot be transferred to toothpaste; stockpiling was small in that application.','Not assessed from abstract.'),
('10.1287/mksc.4.2.147','promotion','abstract','Analytical framework applied to two product classes','Promotion-related acceleration includes larger quantities and shorter interpurchase times.','Purchase timing is different from consumption,preference or incremental category demand.','Not assessed from abstract.'),
('10.1177/002224379202900108','reference_price','abstract','Controlled experiment;direct elicitation of price expectations','Promotion frequency and discount depth affected expected prices;unexpected absence/presence of deals influenced choice.','Mechanism support,not proof Pepsodent regular prices are rejected because of reference prices.','Not assessed from abstract.'),
('10.1177/002224379002700301','reference_price','abstract','Scanner-panel brand-choice model;coffee market','Expected-price model fit better than a traditional choice model;responses to price losses exceeded gains.','Observational model fit and category transfer are limited;not a Pepsodent elasticity estimate.','Not assessed from abstract.'),
('10.1016/j.jcps.2013.08.001','pack_size','abstract','Multiple consumer experiments;packaged goods','Smaller packs could imply higher quality through higher unit-price perceptions;effect reversed under specified distraction/information conditions.','Small packs can communicate quality or cost;cannot presume a universal poor-value response.','Not assessed from abstract.'),
('10.1016/j.jretai.2013.06.002','pack_size','abstract','Household scanner panel;Chicago bulk ice cream;random-utility demand model','Consumers responded less to package-size changes than to price changes in this market.','No transfer of the reported elasticity ratio to Indonesian toothpaste;downsizing differs from distinct premium packs.','Not assessed from abstract.'),
('10.1108/13522750710754290','household','abstract','Mixed methods;18–25-year-olds establishing their first household','Family/friend guidance mattered in complex decisions;hypothetical competence exceeded observed decision competence.','Transition context supports asking actual behavior;does not estimate who funds Indonesian toothpaste.','Not assessed from abstract.'),
('10.1002/cb.1946','household','abstract','Meta-analysis:36 studies,194 relationships,29209 adolescents','Parents,peers and media influence consumer socialization;age and cultural context moderate relationships.','Adolescents are not the complete18–30target;brand influence is not purchase authority or payment.','Not assessed from abstract.'),
('10.1007/s00784-015-1535-z','sensory_vs_clinical','fulltext','RCT120 non-dental students18–34 in Amsterdam;116 completed8weeks','No significant between-formulation plaque/bleeding difference;SLS formulation rated higher for taste,freshness and foam.','No-difference test does not prove universal equivalence;formulations differ beyond a perfectly isolated SLS manipulation.','Sara Lee funded ACTA role;coauthor former Sara Lee/current Colgate-Palmolive.'),
('10.1111/idh.12201','sensory_vs_clinical','abstract','Double-blind RCT90volunteers;89evaluable;4weeks;three formulations','No significant plaque/gingivitis differences;SLS-containing formulations preferred for foam;test non-SLS formulation contained enzymes,colostrum,zinc.','Not an Enzim-brand trial;not proof more foam cleans better.','EuropePMC grant field:Department of Periodontology of ACTA;full disclosure not reviewed.'),
('10.1177/0022034520903036','sensitivity','abstract','Network meta-analysis125RCTs,12541patients;search throughFeb2019;GRADE','Benefits and evidence certainty differed by active ingredient and pain stimulus.','Clinical ingredient evidence is not brand switching,retention or a justification for Premium for everyone.','EuropePMC grants:CAPES,NCMIC Foundation,CNPq.'),
('10.1590/1678-7757-2021-0410','sensitivity','fulltext','Scoping review138RCTs,368formulations;search toAug2021','Formulations,actives,fluoride and abrasive combinations varied;more product names do not imply interchangeable formulations.','Ranks formulations using an earlier NMA;not an independent new effectiveness estimate or retention study.','See fulltext disclosure;do not infer none from missing API grant field.'),
('10.1016/j.jdent.2018.05.012','sensitivity','abstract','Systematic review/meta-analysis53RCTs,4796patients','Several desensitizing formulations reduced hypersensitivity relative to negative controls,with varying evidence quality.','Overlapping primary trials with later reviews;not an independent extra vote;not direct brand comparison.','Not assessed from abstract.'),
('10.1111/jtxs.70018','sensory','abstract','Sensory panel with rheological,tribological and surface measurements','Instrumental features predicted grittiness/particle-perception ratings in tested pastes.','Perception-model performance does not establish clinical cleaning or Indonesian consumer preference.','Not assessed from abstract.'),
('10.1111/jtxs.70036','sensory_pack','abstract','27panelists,eight modified toothpaste samples,instrumental squeeze tests','Acceptability varied with dispensing resistance;both excessive and insufficient resistance can be undesirable.','Ease of dispensing is a distinct pack experience;not proof small tubes cause faster consumption.','Not assessed from abstract.'),
('10.1111/jtxs.70110','sensory','abstract','15custom formulations;instrumental foam analysis linked to sensory panel','Foam characteristics correlated with reported sensory ratings.','Published Aug2026:post-case contextual evidence;no claim to explain H12026 causes or efficacy.','EuropePMC grant:Colgate-Palmolive Company.'),
('10.5005/jp-journals-10024-3859','sensory','abstract','Quasi-experiment152participants;one-week toothpaste-tablet use','Sensory acceptance was multidimensional;texture dislike coexisted with favorable responses on other dimensions.','Novel tablet format and stated intent do not establish clinical efficacy or actual tube-to-tube repurchase.','Not assessed from abstract.'),
('10.1111/joss.12120','sensory','abstract','160consumers,80blind/80informed;eight commercial toothpastes','Flavor acceptance and purchase intention reflected sensory attributes plus brand,price and labels.','Intention is not paid repeat;country and product mix must not be transferred automatically.','Not assessed from abstract.'),
('10.1111/j.1745-459X.2004.tb00143.x','sensory','abstract','Personal-construct interviews and time-intensity freshness ratings','Freshness combines multiple sensory/cognitive dimensions;immediate sensation differs from longer-term recollection.','A vocabulary/design guide,not a national clean-feeling measure or clinical endpoint.','Authors affiliated with Philips research/design;full funding not assessed.'),
('10.1038/bdjopen.2017.11','episodic_use','fulltext','Exploratory examiner-blind RCT76adults18–48;24weeks;continuous vs8on/8off/8on5%CSPS','No significant regimen difference was detected;small treatment response limited ability to detect regression during withdrawal.','Direct counterevidence to assuming inevitable quick relapse;does not prove equivalence or actual consumer discontinuation motives.','GSK-associated authors/institutional funding/editorial support.'),
('10.17358/jabm.8.3.758','indonesia_household_channel','fulltext','Convenience online survey Aug–Oct2021 Greater Jakarta;560responses,459complete;recent toothpaste buyers','Offline exceeded online in all reported age groups;sample and age/area differences can inform channel questions.','Sample skew,not representative;female respondent share does not measure payer authority;age bins cannot exactly recover18–30.','LPDP research grant per fulltext.')]
# Read XML metadata where not covered by API search.
for name in ['pmc_sls_fulltext','scoping_full','episodic_full']:
 p=b/'raw'/(name+'.xml');r=E.fromstring(p.read_bytes());ids={x.get('pub-id-type'):x.text for x in r.findall('.//article-meta/article-id')};doi=ids['doi'].lower()
 if doi not in lookup:lookup[doi]={'doi':doi,'title':' '.join(r.find('.//article-title').itertext()),'year':r.findtext('.//article-meta/pub-date/year'),'authors':'; '.join(' '.join(n.itertext()) for n in r.findall('.//article-meta/contrib-group/contrib/name')),'raw_file':str(p.relative_to(b)),'record_locator':'article/front/article-meta','provider':'EuropePMC fulltext','abstract':' '.join(r.find('.//abstract').itertext())}
rows=[]
for i,(doi,theme,level,design,finding,limit,funding) in enumerate(entries,1):
 x=lookup.get(doi.lower(),{})
 if not x:raise ValueError('Missing metadata '+doi)
 row={'study_id':f'LIT{i:03d}','doi':doi,'url':'https://doi.org/'+doi,'title':x['title'],'authors':x.get('authors'),'year':x.get('year'),'theme':theme,'read_level':level,'design_population':design,'finding_paraphrase':finding,'applicability_limit':limit,'funding_review':funding,'metadata_raw_file':x.get('raw_file'),'record_locator':x.get('record_locator'),'abstract_available':bool(x.get('abstract')),'is_post_case_publication':doi=='10.1111/jtxs.70110','evidence_origin':'external research;not team primary evidence'}
 if doi=='10.1086/651235':row['additional_read_source']='raw/web_choice_pack.json:University Basel abstract'
 if doi=='10.1016/j.jretai.2013.06.002':row['additional_read_source']='https://experts.umn.edu/en/publications/consumer-response-to-package-downsizing-evidence-from-the-chicago/:author institution abstract'
 if doi=='10.17358/jabm.8.3.758':row['fulltext_raw_file']='raw/jakarta_herbal.pdf';row['fulltext_locator']='printedpp760,763–764;PDFpp3,6–7;extractedraw/jakarta_herbal.txt'
 if doi=='10.1038/bdjopen.2017.11':row['fulltext_raw_file']='raw/episodic_full.xml';row['fulltext_locator']='article/body/sec:Results,Discussion'
 if doi=='10.1007/s00784-015-1535-z':row['fulltext_raw_file']='raw/pmc_sls_fulltext.xml';row['fulltext_locator']='article/body/sec:Material and methods,Results,Discussion;acknowledgements'
 if doi=='10.1590/1678-7757-2021-0410':row['fulltext_raw_file']='raw/scoping_full.xml';row['fulltext_locator']='article/body:Methods,Results,Discussion'
 rows.append(row)
(b/'clean/reviewed_evidence.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
keys=list(dict.fromkeys(k for r in rows for k in r))
with (b/'clean/reviewed_evidence.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
unique={}
for x in candidates:unique.setdefault((x.get('doi') or x['title']).lower(),x)
for d,x in lookup.items():unique.setdefault(d,x)
(b/'clean/candidates_all_unique.json').write_text(json.dumps(list(unique.values()),indent=2,ensure_ascii=False))
reviewed={r['doi'].lower() for r in rows}
triage=[]
for x in unique.values():
 doi=x.get('doi','') or '';triage.append({'doi':doi,'title':x['title'],'status':'retained_for_evidence_review' if doi.lower() in reviewed else 'discovery_only_not_deeply_appraised','raw_file':x.get('raw_file'),'record_locator':x.get('record_locator')})
(b/'clean/screening_log.json').write_text(json.dumps(triage,indent=2,ensure_ascii=False))
register=[]
for r in rows:register.append({k:r.get(k) for k in ['study_id','title','doi','url','read_level','metadata_raw_file','record_locator','fulltext_raw_file','fulltext_locator','additional_read_source']})
(b/'source_register.json').write_text(json.dumps(register,indent=2,ensure_ascii=False))
print(json.dumps({'unique_metadata_candidates':len(unique),'retained_reviewed_studies':len(rows),'fulltext_read':sum(r['read_level']=='fulltext' for r in rows),'abstract_read':sum(r['read_level']=='abstract' for r in rows)},indent=2))

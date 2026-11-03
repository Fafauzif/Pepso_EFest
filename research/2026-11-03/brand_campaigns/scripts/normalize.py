from pathlib import Path
from html.parser import HTMLParser
import json,re,html,csv,hashlib,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'clean').mkdir(exist_ok=True); (ROOT/'raw/text').mkdir(exist_ok=True)
class Text(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.out=[]
 def handle_starttag(self,t,a):
  if t in ['script','style','noscript']:self.skip+=1
  if not self.skip and t in ['p','div','h1','h2','h3','li','br','section','article']:self.out.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style','noscript']:self.skip=max(0,self.skip-1)
  if not self.skip and t in ['p','div','h1','h2','h3','li','section','article']:self.out.append('\n')
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
rows=[]
for f in sorted(ROOT.glob('source_register_*.json')):rows+=json.loads(f.read_text())
records=[]; artifacts=[];videos=[];seen=set()
for r in rows:
 if r['url'] in seen:continue
 seen.add(r['url']);r['source_type']='first_party_campaign' if 'oresa.id' in r['url'] or 'jakartafashionweek' in r['url'] else 'brand_owned_page'
 r['source_date']=None;r['time_class']='current_observation_historical_availability_unverified'
 if r.get('status')!=200:records.append(r);continue
 raw=(ROOT/r['raw_file']).read_text();p=Text();p.feed(raw)
 lines=[re.sub(r'\s+',' ',x).strip() for x in ''.join(p.out).splitlines()];lines=[x for x in lines if x]
 textpath=ROOT/'raw/text'/f"{r['id']}.txt";textpath.write_text('\n'.join(lines)+'\n');r['text_file']=str(textpath.relative_to(ROOT));r['text_line_count']=len(lines)
 def get(pattern):
  m=re.search(pattern,raw,re.S|re.I);return html.unescape(re.sub('<[^>]+>',' ',m.group(1))).strip() if m else None
 r['title']=get(r'<title>(.*?)</title>')
 r['canonical_url']=get(r'<link[^>]*rel="canonical"[^>]*href="([^"]*)"') or r['url']
 description=get(r'<meta[^>]*name="description"[^>]*content="([^"]*)"') or ''
 is_product=('/p/' in r['url'] or '/Portfolio/pasta-gigi/' in r['url'] or 'products-dr-enzim' in r['url'])
 placeholder=r['title'] in ['', '| Pepsodent', ' | Pepsodent'] or '{' in r['canonical_url']
 r['content_status']='placeholder_template' if placeholder else 'usable'
 sku=re.search(r'/([0-9]{14})(?:/|$)',r['url'])
 text=' '.join(lines).lower()
 tags=[]
 for name,pat in [('sensitivity','sensitif|sensitivity|ngilu'),('whitening','whitening|memutih|lebih putih'),('freshness','segar|mint|fresh'),('gum','gusi|gum'),('natural_ingredients','herbal|alami'),('regular_use','dua kali|2x sehari|sehari-hari|setiap hari'),('digital_tool','shadescan|scan ai|selfcheck'),('professional_evidence_cue','klinis|dokter|ilmiah'),('family','keluarga'),('incentivized_reviews','cashback')]:
  if re.search(pat,text):tags.append(name)
 # Tags are page-wide discovery flags (navigation may contaminate); do not use as main-body content analysis.
 row={'artifact_id':r['id'],'url':r['url'],'canonical_url':r['canonical_url'],'title':r['title'],'brand':('Pepsodent' if 'pepsodent' in r['url'].lower() or 'unilever' in r['url'] or 'jakartafashionweek' in r['url'] else 'Sensodyne' if 'sensodyne' in r['url'] else 'Closeup' if 'close-up' in r['url'] else 'Enzim' if 'enzim.com' in r['url'] else 'Pepsodent'), 'artifact_type':'product_page' if is_product else 'campaign_or_brand_page','gtin_from_url':sku.group(1) if sku else None,'source_date':None,'observed_at_utc':r['collected_at_utc'],'time_class':r['time_class'],'content_status':r['content_status'],'brand_claim_excerpt':' '.join(description.split()[:12]),'discovery_flags':tags,'raw_file':r['raw_file'],'text_file':r['text_file'],'source_line_start':1,'source_line_end':len(lines),'claim_validation':'brand_statement_not_independent_efficacy_proof','quote_and_tag_note':'excerpt <=12 words; page-wide discovery tags include navigation and are not consumer sentiment'}
 artifacts.append(row);records.append(r)
 for vid in sorted(set(re.findall(r'youtube.com/embed/([A-Za-z0-9_-]{11})',raw))):videos.append({'video_id':vid,'watch_url':'https://www.youtube.com/watch?v='+vid,'embedding_page':r['url'],'raw_file':r['raw_file'],'observed_at_utc':r['collected_at_utc'],'post_date':None,'channel_owner':'not_verified','comment_access':'not_tested'})
(ROOT/'source_register.json').write_text(json.dumps(records,indent=2,ensure_ascii=False))
for name,data in [('artifacts',artifacts),('video_targets',videos)]:
 (ROOT/'clean'/f'{name}.json').write_text(json.dumps(data,indent=2,ensure_ascii=False))
 with (ROOT/'clean'/f'{name}.csv').open('w',newline='') as f:
  if data:
   w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v for k,v in r.items()} for r in data)
# Unique canonical product records; template pages excluded, exact canonical collisions retained in artifacts only.
products=[];keys=set()
for r in artifacts:
 if r['artifact_type']=='product_page' and r['content_status']=='usable' and r['canonical_url'] not in keys:products.append(r);keys.add(r['canonical_url'])
(ROOT/'clean/products_unique.json').write_text(json.dumps(products,indent=2,ensure_ascii=False))
summary={'attempted_unique_urls':len(records),'http_success':sum(r.get('status')==200 for r in records),'failed':sum(r.get('status')!=200 for r in records),'usable_artifacts':sum(r.get('content_status')=='usable' for r in artifacts),'placeholder_templates':sum(r.get('content_status')=='placeholder_template' for r in artifacts),'unique_usable_product_pages':len(products),'video_targets':len(videos)}
(ROOT/'collection_summary.json').write_text(json.dumps(summary,indent=2));print(summary)

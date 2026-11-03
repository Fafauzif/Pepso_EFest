"""Normalize a bounded known-profile/post public SSR sample; preserve excerpts and extraction provenance."""
from pathlib import Path
from lxml import html
import json,csv,re,datetime
b=Path(__file__).resolve().parents[1];rows=[];seen=set();excluded=[]
for name in ['brand_linked','user_post_original']:
 root=html.fromstring((b/'raw'/(name+'.txt')).read_bytes())
 for i,a in enumerate(root.xpath('//article')):
  links=a.xpath('.//a[contains(@href,"/status/")]/@href');match=next((re.search(r'/([^/]+)/status/(\d+)',x) for x in links if re.search(r'/([^/]+)/status/(\d+)',x)),None)
  if not match:continue
  handle,ident=match.groups()
  if ident in seen:excluded.append({'source':name,'article_index':i,'reason':'duplicate_post_id','post_id':ident});continue
  seen.add(ident)
  el=a.xpath('.//div[@dir="auto" and contains(@class,"whitespace-pre-wrap")]');text='\n'.join(''.join(e.itertext()) for e in el)
  if name=='user_post_original' and ident!='2068234900491129031':excluded.append({'source':name,'article_index':i,'reason':'reply_not_substantively_toothpaste_related','post_id':ident});continue
  source_type='brand_owned_marketing' if name=='brand_linked' else 'self_reported_purchase_story'
  if source_type=='self_reported_purchase_story':
   excerpt='Tahu pasta gigi impor bernama Pasta Del Capitano? Sekarang, saya cukup pakai Pepsodent.'
   summary='Writer describes changing household spending and replacing an imported toothpaste with Pepsodent. Exact Pepsodent SKU and buyer age are not established.'
  else:excerpt=' '.join(text.split()[:25]);summary='Brand-post sensory/need framing;not an independent consumer experience.'
  row={'record_id':'XSSR-'+ident,'platform':'X','post_id':ident,'source_url':f'https://x.com/{handle}/status/{ident}','source_type':source_type,'text_excerpt':excerpt,'excerpt_is_truncated':len(text.split())>25,'original_word_count':len(text.split()),'summary_analyst':summary,'raw_file':'raw/'+name+'.txt','record_locator':f'//article[{i+1}]//div[@dir=auto][contains(@class,whitespace-pre-wrap)]','created_at_from_snowflake':datetime.datetime.fromtimestamp(((int(ident)>>22)+1288834974657)/1000,datetime.timezone.utc).isoformat(),'created_time_method':'derived_from_public_snowflake_ID;human display date checked','age_verified':False,'confirmed_pepsodent_premium_to_basic_switch':False,'paid_price_verified':False,'collection_scope':'known-profile or known-post public HTML;not keyword-search corpus'}
  rows.append(row)
(b/'clean/x_public_sample.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
with (b/'clean/x_public_sample.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
(b/'clean/extraction_exclusions.json').write_text(json.dumps(excluded,indent=2))
# Resolve manual review of HTTP200 shells/notice pages.
p=b/'raw/public_route_tests.json';log=json.loads(p.read_text())
notes={'x_search':'Redirected to login HTML shell;no posts.','x_brand':'Unrelated current account display;guessed handle not verified brand.','x_brand_alternate_name':'404;no account content.','syndication_profile':'Rate limited;not evidence account has no posts.','nitter_search':'Maintainer notice10Oct2026;HTTP200 is not a timeline.','xcancel_search':'Service suspension notice;HTTP451.','twscrape_login_source':'Source code inspected;not a post dataset.','ntscraper_source':'Source code inspected;not a post dataset.'}
for r in log:r.update({'usable_records':0,'inspection_required':False,'manual_inspection':notes[r['test']]})
p.write_text(json.dumps(log,indent=2))
print(json.dumps({'records':len(rows),'brand_posts':sum(r['source_type']=='brand_owned_marketing' for r in rows),'purchase_stories':sum(r['source_type']=='self_reported_purchase_story' for r in rows),'exclusions':excluded},indent=2))

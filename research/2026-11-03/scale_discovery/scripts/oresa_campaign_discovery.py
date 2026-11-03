from pathlib import Path
import urllib.request,urllib.parse,json,datetime,hashlib,concurrent.futures
B=Path(__file__).resolve().parents[1]
qs=['pepsodent','sensodyne','closeup','colgate','enzim','systema','ciptadent','formula']
def get(q):
 u='https://oresa.id/produk-sampel/ended-sampling?'+urllib.parse.urlencode({'page':1,'q':q,'sort':'','category':''});now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','X-Requested-With':'XMLHttpRequest'}),timeout=20) as f:b=f.read()
  p=B/'raw'/f'oresa_ended_{q}.json';p.write_bytes(b);d=json.loads(b);rows=[]
  for x in d['data']:
   rows.append({k:x.get(k) for k in ['project_detail_id','product_id','category','name','total_review','start_date_sampling','end_date_sampling','sampling_method','show_review','name_slug']})
  return {'query':q,'url':u,'status':'success','total_campaigns':d.get('total'),'raw_file':str(p.relative_to(B)),'retrieved_at_utc':now,'sha256':hashlib.sha256(b).hexdigest(),'campaigns':rows}
 except Exception as e:return {'query':q,'url':u,'status':'failed','error':str(e),'retrieved_at_utc':now}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:logs=list(ex.map(get,qs))
(B/'oresa_discovery_log.json').write_text(json.dumps(logs,indent=2));out=list({str(r['product_id']):r for l in logs for r in l.get('campaigns',[])}.values());(B/'clean/oresa_campaign_inventory.json').write_text(json.dumps(out,indent=2));print(out)

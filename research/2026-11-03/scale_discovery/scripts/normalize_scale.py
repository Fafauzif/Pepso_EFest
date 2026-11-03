from pathlib import Path
import json,csv,re,collections,datetime,hashlib,html
B=Path(__file__).resolve().parents[1]
rows=json.loads((B/'clean/oresa_new_reviews.json').read_text());campaigns={str(r['product_id']):r for r in json.loads((B/'clean/oresa_campaign_inventory.json').read_text())}
months={'Januari':'01','Februari':'02','Maret':'03','April':'04','Mei':'05','Juni':'06','Juli':'07','Agustus':'08','September':'09','Oktober':'10','November':'11','Desember':'12'}
patterns={'sensory':r'(?i)segar|kesat|keset|mint|pedas|busa|rasa|aftertaste','household':r'(?i)keluarga|suami|istri|orang tua|mama|ayah|ibu|bapak|anak','price_or_promotion':r'(?i)harga|mahal|murah|promo|diskon|cashback|hemat','repeat_intention':r'(?i)akan beli|bakal beli|mau beli|pasti beli|repurchase|beli lagi','preuse_wording_candidate':r'(?i)\bbelum (?:di)?coba\b|\bbelum (?:di)?pakai\b','use_timeline':r'(?i)hari|minggu|bulan','stock_wording':r'(?i)stok|stock|susah cari|sulit cari|habis di toko'}
flags=[];dates=[]
for r in rows:
 d=r.get('published_raw') or '';m=re.search(r'(\d{1,2}) ([A-Za-z]+) (\d{4})',d);date=None
 if m and m.group(2) in months:date=f'{m.group(3)}-{months[m.group(2)]}-{int(m.group(1)):02}'
 r['published_date']=date;r['published_timezone']='unknown_not_inferred';r['time_scope']='case_window_2022_H1_2026' if date and '2022-01-01'<=date<='2026-06-30' else 'after_case_H1_2026' if date and date>'2026-06-30' else 'before_case_2022' if date else 'date_unknown'
 pid=r['source_id'].split('-')[1];c=campaigns.get(pid,{})
 r['campaign_start_date']=c.get('start_date_sampling');r['campaign_end_date']=c.get('end_date_sampling');r['campaign_metadata_source']='raw/oresa_ended_pepsodent.json'
 r['incentive_status']='cashback_and_mandatory_reviews_explicit' if pid=='1017' else 'selected_sampling_mandatory_reviews_and_controlled_social_tasks_explicit' if pid=='1061' else 'sampling_campaign_context_specific_compensation_unverified'
 t=html.unescape(re.sub('<[^>]+>',' ',r['review_text'] or ''));r['text_sha256_normalized']=hashlib.sha256(re.sub(r'\s+',' ',t).strip().casefold().encode()).hexdigest()
 row={'record_id':r['record_id'],'product_name':r['product_name'],'time_scope':r['time_scope']}
 row.update({k:bool(re.search(p,t)) for k,p in patterns.items()});flags.append(row)
 if date:dates.append(date)
(B/'clean/oresa_new_reviews.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
with (B/'clean/oresa_new_reviews.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(B/'clean/oresa_lexical_flags.json').write_text(json.dumps(flags,indent=2,ensure_ascii=False))
counts=collections.Counter(r['product_name'] for r in rows);hashes=collections.Counter(r['text_sha256_normalized'] for r in rows)
summary={'new_oresa_records':len(rows),'unique_record_ids':len({r['record_id'] for r in rows}),'product_counts':dict(counts),'scope_counts':dict(collections.Counter(r['time_scope'] for r in rows)),'ratings':dict(collections.Counter(r['rating'] for r in rows)),'date_min':min(dates),'date_max':max(dates),'unique_normalized_texts':len(hashes),'duplicate_text_groups':sum(v>1 for v in hashes.values()),'lexical_flag_counts':{k:sum(r[k] for r in flags) for k in patterns},'lexical_caveat':'Overlapping exploratory word matches, not validated motives, sentiment, efficacy, unique people or prevalence. Campaign/sampling wording may be templated.','verified_18_30_switchers':0,'apify_runs':0,'paid_spend':0,'broader_research_datasets_screened_rows':209187,'broader_dataset_toothpaste_candidates':0}
(B/'quality_report.json').write_text(json.dumps(summary,indent=2));print(summary)
# Inspect eligible examples for manual follow-up; output short excerpts for internal QA only.
for flagname in ['household','price_or_promotion','stock_wording','preuse_wording_candidate']:
 print('\nFLAG',flagname)
 hit=0
 for r,f in zip(rows,flags):
  if f[flagname]: print(r['record_id'],r['product_name'],r['published_date'],r['review_text'][:350].replace('\n',' '));hit+=1
  if hit>=4:break

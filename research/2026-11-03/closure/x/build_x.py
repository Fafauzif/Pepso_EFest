#!/usr/bin/env python3
"""Offline, stdlib normalization of user-run X files. Original bytes remain external inputs."""
import argparse, collections, csv, datetime as dt, gzip, hashlib, io, json, random, re, unicodedata, os, tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
FILES=['dataset_x-tweet-scraper_2026-11-03_11-29-36-664.json','dataset_x-tweet-scraper_2026-11-03_11-35-46-217.json','dataset_x-tweet-scraper_2026-11-03_11-42-21-918.json','dataset_x-tweet-scraper_2026-11-03_11-49-14-919.json']
PATTERNS={
 'household_payer_candidate':r'\b(?:ortu|ort[uoy]|orang tua|bonyok|nyokap|bokap|mama|papa|ibu|bapak|keluarga|sekeluarga|dibeliin|dibelikan|anak kos|ngekos|kosan)\b',
 'price_promotion_candidate':r'\b(?:mahal|murah|harga|diskon|promo|budget|hemat|price|expensive|cost|discount)\b',
 'availability_replenishment_candidate':r'\b(?:habis|abis|kosong|stok|stock|indomaret|alfamart|warung|minimarket|watsons|guardian)\b|(?:susah|sulit|susahnya|sulitnya).{0,20}(?:cari|nyari|dapat|dapet|beli)',
 'sensory_experience_candidate':r'\b(?:rasa|rasanya|mint|busa|pahit|pedes|pedas|kering|keset|seger|segar|sariawan|licin|fresh|taste|aftertaste|foam|burning|clean)\b',
 'need_benefit_candidate':r'\b(?:ngilu|sensitif|sensitive|sensitivity|putih|whitening|kuning|karang|plak|gusi|gums|fluoride|fluorida)\b',
 'repeat_fit_candidate':r'\b(?:repeat|repurchase|langganan|cocok|selalu|bertahun)\b|beli lagi|udah lama|sudah lama|pake terus|pakai terus',
 'switching_candidate':r'\b(?:ganti|gonta|beralih|balik|kembali|pindah|switch|switched|switching)\b|dulu.{0,70}(?:sekarang|skrg)|(?:sekarang|skrg).{0,70}dulu',
 'first_person_candidate':r'\b(?:aku|gue|gw|saya|sy|gua|ku|i use|my toothpaste|i switched)\b',
 'question_candidate':r'\?|\b(?:rekomendasi|recommend|saran|bagusnya|mending|bagusan|rekomen)\b',
 'retail_commercial_marker':r'shopee\.(?:co|com)|shope\.ee|s\.shopee|lazada\.|tokopedia\.|tokopedia\.link|tiktokshop|checkout|check out|affiliate|affiliator|voucher|cashback|ready stock|ready stok|\b(?:jual|dijual|jualan|reseller)\b',
 'truck_transport_marker':r'\b(?:truk|truck|trucks|overload|overdimension|logistik|angkutan|tonase|muatan|kendaraan|trucking|dumptruck|dump truck|kecelakaan)\b',
 'figurative_marker':r'(?:senyum|senyumnya|smile|smiling).{0,50}pepsodent|pepsodent.{0,50}(?:senyum|senyumnya|smile|smiling)|kodomo.{0,25}(?:teman|sahabat)|(?:teman|sahabat).{0,25}kodomo',
 'boycott_candidate':r'\b(?:boikot|boycott|israel|palestina|palestine|zionis|zionist)\b'
 ,'commercial_listing_candidate':r'cek harga|cek:|link\s*:|beli (?:di sini|disini)|\bas low as\b|\bfree ongkir\b|\b(?:buy|beli)\s*\d+.{0,20}(?:get|gratis|free)|\brp\s*\d|🛒|🔗'
 ,'accessory_candidate':r'\b(?:dispenser|jepitan|gantungan|holder)\b|rak sikat|tempat (?:odol|sikat|pasta)|klip hanger'
 ,'possible_ad_jingle_meme':r'(?:pas|ketika|lagi).{0,40}(?:sendok|nyendok).{0,45}(?:es|mulut).{0,45}(?:ngilu|cu+)|berkat sensod(?:yne|en).{0,50}(?:sekarang|skrg|teman|temen)|(?:dokter|dr).{0,20}sarankan.{0,25}ibu.{0,20}sensod'
}
RX={k:re.compile(v,re.I|re.S) for k,v in PATTERNS.items()}
BRANDS=re.compile(r'pepsodent|sensodyne|sensoden|sensodin|enzim|enzym|close\s?up|colgate|marvis|darlie|zact|ciptadent|antipla[qc]|parodontax|kodomo|formula|ultra\s?white',re.I)
DENTAL=re.compile(r'pasta\s?gigi|toothpaste|\bgigi\b|\bsikat\b|\bngilu\b|\bsariawan\b|\bfluoride\b|\bfluorida\b|\bwhitening\b|\bgusi\b',re.I)
USE=re.compile(r'\b(?:pakai|pake|pakek|pakei|memakai|beli|nyoba|coba|odol|sikat)\b',re.I)

def sha(b):return hashlib.sha256(b).hexdigest()
def normalized(t):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',t)).strip().casefold()
def template(t):
 t=normalized(t);t=re.sub(r'https?://\S+','<URL>',t);t=re.sub(r'@[\w_]+','<USER>',t);t=re.sub(r'\b\d+(?:[.,]\d+)*\b','<NUM>',t)
 return t
def atomic_bytes(path,data):
 # Finish compression before writing: a stream-written gzip was once truncated
 # in this session (cause unknown). Atomic replace and byte comparison catch truncation.
 with tempfile.NamedTemporaryFile(dir=path.parent,prefix=path.name+'.',suffix='.tmp',delete=False) as f:
  tmp=Path(f.name);f.write(data);f.flush();os.fsync(f.fileno())
 os.replace(tmp,path)
 if path.read_bytes()!=data:raise IOError('Written bytes differ: '+str(path))
def jlines(path,rows):
 data=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode()
 compressed=gzip.compress(data,mtime=0);assert gzip.decompress(compressed)==data;atomic_bytes(path,compressed)
def csvgz(path,rows,fields):
 text=io.StringIO(newline='');w=csv.DictWriter(text,fieldnames=fields);w.writeheader()
 for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items() if k in fields})
 atomic_bytes(path,gzip.compress(text.getvalue().encode(),mtime=0))
def parse_date(t):
 try:return dt.datetime.strptime(t,'%a %b %d %H:%M:%S %z %Y').isoformat()
 except (ValueError,TypeError):return None
def load_bytes(p):return gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes()
def main():
 a=argparse.ArgumentParser();a.add_argument('--input-dir',type=Path);ns=a.parse_args()
 candidates=[ns.input_dir] if ns.input_dir else [REPO/'data/raw/user_runs',HERE.parent/'raw/user_runs',HERE.parent/'raw',REPO.parent/'upload']
 base=next((p for p in candidates if p and any((p/n).exists() or (p/(n+'.gz')).exists() for n in FILES)),None)
 if base is None:raise SystemExit('Specify --input-dir containing the four raw exports (.json or .json.gz).')
 records={};occ=[];inputs=[];seen=set();run_counts=[]
 for name in FILES:
  p=base/name
  if not p.exists():p=base/(name+'.gz')
  b=load_bytes(p);data=json.loads(b);idset={str(r['id']) for r in data}
  inputs.append({'filename':name,'sha256_original_bytes':sha(b),'bytes_original':len(b),'rows':len(data)})
  run_counts.append({'filename':name,'rows':len(data),'unique_ids':len(idset),'new_ids_in_order':len(idset-seen),'overlap_previous_ids':len(idset&seen)})
  seen|=idset
  for i,r in enumerate(data):
   ident=str(r['id']);t=r.get('text') or '';key='x:'+ident;author=r.get('author') or {};authorid=str(author.get('id') or author.get('username') or '')
   loc={'source_file':name,'json_index_zero_based':i,'text_sha256':sha(t.encode()),'payload_sha256':sha(json.dumps(r,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())}
   occ.append({'record_key':key,**loc})
   urls=[u.get('expanded_url') or u.get('url') for u in (r.get('entities') or {}).get('urls',[]) if isinstance(u,dict) and (u.get('expanded_url') or u.get('url'))]
   flags={k:bool(rx.search(t)) for k,rx in RX.items()};flags['retail_commercial_marker']=flags['retail_commercial_marker'] or bool(RX['retail_commercial_marker'].search(' '.join(urls)))
   dental=bool(DENTAL.search(t));brand=bool(BRANDS.search(t));use=bool(USE.search(t))
   if flags['truck_transport_marker'] and not (dental or (brand and use)):relevance='obvious_transport_nonoralcare'
   elif flags['figurative_marker'] and not (dental or (brand and use)):relevance='likely_figurative_nonexperience'
   elif flags['accessory_candidate'] and not brand:relevance='adjacent_accessory_candidate'
   elif dental or (brand and use):relevance='oralcare_candidate_not_individually_verified'
   elif brand:relevance='brand_ambiguous_or_context_missing'
   elif re.search(r'\bodol\b',t,re.I):relevance='odol_ambiguous'
   else:relevance='unresolved_other'
   date=parse_date(r.get('created_at'));scope='unknown_date' if not date else ('case_historical' if '2022-01-01'<=date<'2026-07-01' else 'outside_case_period')
   old=records.get(ident)
   records[ident]={'record_key':key,'platform':'x','source_record_id':ident,'source_url':r.get('url'),'text_original':t,'text_normalized':normalized(t),'outbound_expanded_urls':urls,'content_date':date,'date_raw':r.get('created_at'),'date_method':'actor_created_at_parsed_UTC','scope':scope,'language_actor':r.get('lang'),'author_pseudonym':'A-'+sha(authorid.encode())[:16] if authorid else None,'is_reply':r.get('is_reply'),'is_retweet':r.get('is_retweet'),'conversation_id':r.get('conversation_id'),'parent_post_id':r.get('in_reply_to_status_id'),'relevance_status':relevance,'dental_anchor':dental,'brand_string_match':brand,'text_nonempty':bool(t.strip()),'word_count':len(t.split()),'age_verified':False,'confirmed_pepsodent_premium_to_basic_switch':False,'geography_verified':False,'incentive_status':'not_established','selection_method':'user_run_search_nonprobability','candidate_tags':[k for k,v in flags.items() if v],'latest_source_file':name,'latest_json_index_zero_based':i,'raw_archive_path':'research/2026-11-03/closure/raw/user_runs/'+name+'.gz','first_source_file':old['first_source_file'] if old else name,'first_json_index_zero_based':old['first_json_index_zero_based'] if old else i,'source_occurrences':old['source_occurrences']+1 if old else 1,'like_count':r.get('like_count'),'reply_count':r.get('reply_count'),'retweet_count':r.get('retweet_count')}
 rows=sorted(records.values(),key=lambda r:r['source_record_id']);exact=collections.defaultdict(list);templates=collections.defaultdict(list)
 for r in rows:r['conversation_root_in_collected_set']=str(r['conversation_id']) in records
 for r in rows:
  if r['text_normalized']:exact[sha(r['text_normalized'].encode())].append(r['record_key'])
  temp=template(r['text_original'])
  if len(temp)>=40:templates[sha(temp.encode())].append(r['record_key'])
 groups=[{'group_kind':'normalized_exact_text','fingerprint':k,'size':len(ids),'record_keys':ids} for k,ids in exact.items() if len(ids)>1]
 template_groups=[{'group_kind':'possible_template_url_mention_number_normalized','fingerprint':k,'size':len(ids),'record_keys':ids} for k,ids in templates.items() if len(ids)>1]
 multi_text=collections.defaultdict(set)
 multi_payload=collections.defaultdict(set)
 for o in occ:
  multi_text[o['record_key']].add(o['text_sha256']);multi_payload[o['record_key']].add(o['payload_sha256'])
 context_info={'reply_posts':sum(bool(x['is_reply']) for x in rows),'reply_posts_with_conversation_root_in_collected_ids':sum(bool(x['is_reply']) and x['conversation_root_in_collected_set'] for x in rows),'direct_reply_parent_id_available':sum(bool(x['parent_post_id']) for x in rows),'same_id_multiple_payload_hashes':sum(len(s)>1 for s in multi_payload.values()),'source_occurrence_count':len(occ)}
 (HERE/'context_and_versions.json').write_text(json.dumps(context_info,indent=2)+'\n')
 author=collections.Counter(r['author_pseudonym'] for r in rows if r['author_pseudonym']);cnt=lambda key:dict(collections.Counter(r[key] for r in rows))
 old_path=REPO/'research/2026-11-03/scale_tools/clean/x_public_sample.json';legacy=json.loads(old_path.read_text()) if old_path.exists() else []
 legacy_info=[{'source_record_id':str(x['post_id']),'source_url':x['source_url'],'overlaps_new_exports':str(x['post_id']) in records,'text_is_excerpt':x.get('excerpt_is_truncated'),'source_type':x.get('source_type'),'original_record':x} for x in legacy]
 stats={'exported_rows':len(occ),'unique_post_ids':len(rows),'repeated_identity_occurrences':len(occ)-len(rows),'runs':run_counts,'source_inputs':inputs,'written_nonempty':sum(r['text_nonempty'] for r in rows),'retweets_flagged':sum(bool(r['is_retweet']) for r in rows),'replies_flagged':sum(bool(r['is_reply']) for r in rows),'date_scope':cnt('scope'),'language_actor':cnt('language_actor'),'relevance_rule_classes':cnt('relevance_status'),'candidate_tag_counts':dict(collections.Counter(t for r in rows for t in r['candidate_tags'])),'distinct_author_pseudonyms':len(author),'top_10_author_post_counts':author.most_common(10),'normalized_exact_text_duplicate_groups':len(groups),'posts_in_normalized_exact_text_duplicate_groups':sum(x['size'] for x in groups),'possible_template_groups':len(template_groups),'posts_in_possible_template_groups':sum(x['size'] for x in template_groups),'same_id_multiple_text_versions':sum(len(v)>1 for v in multi_text.values()),'legacy_records':len(legacy),'legacy_overlap':sum(x['overlaps_new_exports'] for x in legacy_info),'legacy_additional_ids':sum(not x['overlaps_new_exports'] for x in legacy_info),'combined_platform_ids_including_legacy':len(rows)+sum(not x['overlaps_new_exports'] for x in legacy_info),'age_verified_count':0,'target_switcher_verified_count':0,'new_export_geography_verified_count':0,'date_span':[min(r['content_date'] for r in rows if r['content_date']),max(r['content_date'] for r in rows if r['content_date'])]}
 (HERE/'stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
 jlines(HERE/'records.jsonl.gz',rows);cfields=list(rows[0]);csvgz(HERE/'records.csv.gz',rows,cfields);jlines(HERE/'occurrences.jsonl.gz',occ);jlines(HERE/'exact_text_groups.jsonl.gz',groups);jlines(HERE/'possible_template_groups.jsonl.gz',template_groups)
 (HERE/'legacy_x_overlap.json').write_text(json.dumps(legacy_info,ensure_ascii=False,indent=2)+'\n')
 # Reproducible sampling: random40 (whole export), then 60 purposive candidates across mechanisms.
 rng=random.Random(20261103);selected={r['source_record_id']:{'record_key':r['record_key'],'sampling_stratum':'random_40_all_unique_posts'} for r in rng.sample(rows,40)}
 themes=['household_payer_candidate','switching_candidate','repeat_fit_candidate','sensory_experience_candidate','availability_replenishment_candidate','price_promotion_candidate']
 for theme in themes:
  pool=[r for r in rows if r['source_record_id'] not in selected and r['relevance_status']=='oralcare_candidate_not_individually_verified' and theme in r['candidate_tags'] and 'first_person_candidate' in r['candidate_tags'] and 'retail_commercial_marker' not in r['candidate_tags'] and 'boycott_candidate' not in r['candidate_tags']]
  # deterministic random subset within eligible theme, not score ranked cherry-picking
  for r in rng.sample(pool,min(10,len(pool))):selected[r['source_record_id']]={'record_key':r['record_key'],'sampling_stratum':'purposive_theme_then_random_within_'+theme}
 fixed=HERE/'review_selection.json'
 if fixed.exists():selected={x['source_record_id']:{'record_key':'x:'+x['source_record_id'],'sampling_stratum':x['sampling_stratum']} for x in json.loads(fixed.read_text())['records']}
 sample=[{**records[k],**v} for k,v in selected.items()]
 (HERE/'review_sample.json').write_text(json.dumps(sample,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(stats,ensure_ascii=False,indent=2));print('review_sample_rows',len(sample))
if __name__=='__main__':main()

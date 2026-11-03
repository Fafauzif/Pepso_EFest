#!/usr/bin/env python3
"""Rebuild new Tokopedia/Shopee analysis from immutable exports; stdlib only."""
from __future__ import annotations
import argparse,collections,csv,datetime as dt,gzip,hashlib,io,json,pathlib,random,re,unicodedata
HERE=pathlib.Path(__file__).resolve().parent
REPO=HERE.parents[3]
NAMES=['dataset_tokopedia-reviews-scraper_2026-11-03_12-22-38-122.json','dataset_tokopedia-reviews-scraper_2026-11-03_12-27-31-721.json','dataset_shopee-reviews-scraper_2026-11-03_12-11-00-864.json','dataset_shopee-reviews-scraper_2026-11-03_12-18-09-957.json']
PATTERNS={
 'fulfilment_or_seller':r'kirim|sampai|sampe|packing|packaging|paket|seller|pelayanan|kurir|pesanan|kemasan|pengemas',
 'promotion_or_price':r'diskon|promo|harga|murah|miring|offers|ongkir',
 'sensory_candidate':r'rasa|mint|segar|seger|busa|pedas|mual|huek|nyaman|mulut|deterg|deterj',
 'reported_benefit_candidate':r'ngilu|sensitif|sensitive|sakit|sehat|putih|karang|gusi|dokter',
 'continued_use_candidate':r'selalu.*(?:pakai|pake)|sudah.*lama|sdh.*lama|rutin|udah thnan|sudah jadi pengguna|biasa.*(?:memakai|pake)|selama',
 'explicit_repeat_wording_candidate':r'repeat order|beli lagi|beli yg kbbrapa|pembelian.*kembali',
 'future_or_fit_expectation':r'semoga cocok|semoga.*cocok|next order|nex order|ga akan pindah|tidak mau ganti',
 'before_use_candidate':r'(?:belum|blm|blom)\s*(?:di\s*)?(?:coba|dicoba|dipakai|tau hasil|nyoba)',
 'household_candidate':r'keluarga|anak|serumah|suami|istri',
 'pack_or_travel_candidate':r'ukuran|size|travel|kecil|mini|190grm|bulan|min pembelian|min.*3',
}
GENERIC={'ok','oke','good','bagus','mantap','mantaps','nice','best','top','y','1','tob','ook','gud','sesuai','josjis','josjis','daebag','lyi','bsgus','recomended','recommended','mantap jiwa','terima kasih','terima kasih ya','terima kasih banyak'}
def h(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(name,inp):
 choices=[inp/name,inp/(name+'.gz')]
 for p in choices:
  if p.exists():
   b=gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes()
   return json.loads(b),{'original_filename':name,'original_sha256':hashlib.sha256(b).hexdigest(),'input_file_read':p.name,'bytes_uncompressed':len(b)}
 raise FileNotFoundError(str(choices))
def writejsonl(name,rows):
 with gzip.GzipFile(filename=str(HERE/name),mode='wb',mtime=0) as f:
  for x in rows:f.write((json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n').encode())
def csvwrite(name,rows):
 if not rows:return
 fields=list(dict.fromkeys(k for r in rows for k in r))
 with gzip.GzipFile(filename=str(HERE/name),mode='wb',mtime=0) as g:
  with io.TextIOWrapper(g,encoding='utf8',newline='') as f:
   w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
   for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
def scope(s):
 if not s:return 'unknown_date'
 return 'case_historical_by_unverified_reviewDate' if '2022-01-01'<=s<='2026-06-30' else ('current_context_by_unverified_reviewDate' if s>'2026-06-30' else 'outside_case_before_2022_by_unverified_reviewDate')
def pscope(name):
 if re.search(r'\bspray\b',name,re.I):return 'adjacent_whitening_spray'
 if re.search(r'\bgimmick\b',name,re.I):return 'toothpaste_gimmick_title_candidate'
 return 'toothpaste_title_candidate'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-dir',type=pathlib.Path);a=ap.parse_args()
 inp=a.input_dir
 if inp is None:
  candidates=[HERE.parent/'raw/user_runs',REPO/'data/raw/user_runs',REPO.parent/'upload']
  inp=next((p for p in candidates if (p/NAMES[0]).exists() or (p/(NAMES[0]+'.gz')).exists()),None)
 if inp is None:raise SystemExit('Specify --input-dir containing original .json or .json.gz exports')
 latest={};occ=[];products=[];notices=[];source=[];excluded=[];first={};payload_hashes=collections.defaultdict(set);review_order=[]
 for fn in NAMES:
  rows,meta=load(fn,inp);meta['row_count']=len(rows);meta['types']=dict(collections.Counter(x.get('type') for x in rows));source.append(meta)
  for i,r in enumerate(rows):
   loc={'source_filename':fn,'json_index_zero_based':i,'source_locator':f'{fn}#json[{i}]'}
   typ=r.get('type');ph=h(r)
   if 'shopee' in fn:
    excluded.append({**loc,'source_type':typ,'source_review_id':r.get('reviewId'),'reason':'wrong_target_UGREEN_Singapore' if typ=='review' else 'collection_error_no_delivered_review','raw_payload':r});continue
   if typ=='product':products.append({**r,**loc,'payload_sha256':ph,'product_scope':pscope(r.get('productName',''))});continue
   if typ=='notice':notices.append({**loc,**r});continue
   if typ!='product_review':raise ValueError(typ)
   k='tokopedia:'+str(r['reviewId']);payload_hashes[k].add(ph);first.setdefault(k,loc)
   occ.append({'record_key':k,**loc,'payload_sha256':ph,'raw_payload':r})
   latest[k]=(r,loc,ph)
   if fn==NAMES[1]:review_order.append(k)
 out=[]
 for k,(r,loc,ph) in latest.items():
  text=r.get('reviewText');norm=unicodedata.normalize('NFKC',text or '').strip();tags=[tag for tag,pat in PATTERNS.items() if re.search(pat,norm,re.I)]
  simple=re.sub(r'[^\w\s]','',norm.lower()).strip();tokens=re.findall(r'\w+',norm)
  if not norm:state='blank'
  elif not any(c.isalpha() for c in norm):state='symbol_or_numeric_only'
  elif simple in GENERIC:state='short_generic'
  else:state='contextual_text_candidate'
  name=r.get('productName') or '';ps=pscope(name);mis='bau badan' in norm.lower()
  rd=r.get('reviewDate');rt=r.get('reviewTime');disagreement=bool(rd and rt and rd!=(rt or '')[:10])
  o={'record_key':k,'platform':'tokopedia','source_record_id':str(r['reviewId']),'record_type':'review','product_id':str(r.get('productId')),'product_name':name,'product_scope':ps,'source_url':r.get('productUrl'),'text_original':text,'text_normalized':norm,'text_information_state':state,'rating':r.get('rating'),'date_raw_label':r.get('reviewTimeText'),'review_date_field':rd,'review_time_field':rt,'date_fields_disagree':disagreement,'date_quality':'source_reviewDate_unverified_actor_reviewTime_estimated_from_relative_label','scope':scope(rd),'incentive_status':('review_text_explicit_free_Pepsodent_item' if 'pepsodent gratis' in norm.lower() else ('gimmick_listing_context_incentive_not_established' if ps=='toothpaste_gimmick_title_candidate' else 'not_established')),'author_pseudonym':('tokopedia_author_'+hashlib.sha256(str(r.get('reviewerId')).encode()).hexdigest()[:12]) if str(r.get('reviewerId')) not in ['0','None',''] else None,'is_anonymous':r.get('isAnonymous'),'variant_name':r.get('variantName'),'possible_misassigned_text':mis,'eligible_written_toothpaste_candidate':bool(norm) and ps=='toothpaste_title_candidate' and not mis,'candidate_tags':tags,'age_verified':False,'premium_to_basic_verified':False,'last_source':loc,'first_source':first[k],'distinct_payload_versions':len(payload_hashes[k]),'canonical_policy':'last file occurrence; all original payload occurrences retained','payload_sha256':ph}
  out.append(o)
 writejsonl('reviews_clean.jsonl.gz',out);csvwrite('reviews_clean.csv.gz',out)
 writejsonl('review_occurrences.jsonl.gz',occ);writejsonl('product_observations.jsonl.gz',products);csvwrite('product_observations.csv.gz',products);writejsonl('excluded_shopee.jsonl.gz',excluded);writejsonl('billing_notices.jsonl.gz',notices)
 # Review sampling: 40 seeded random calibration records + purposeful indices documented before coding.
 random_indexes=set(random.Random(11262026).sample(range(len(review_order)),40))
 bykey={r['record_key']:r for r in out}
 anns=[]
 with (HERE/'manual_annotations.tsv').open() as f:
  for m in csv.DictReader(f,delimiter='\t'):
   ix=int(m['review_index']);r=bykey[review_order[ix]]
   anns.append({'annotation_id':f'TKQ-{len(anns)+1:03d}','record_key':r['record_key'],'selection':'seeded_random_calibration' if ix in random_indexes else 'purposive_mechanism_or_counterexample','sample_seed':11262026 if ix in random_indexes else None,'main_review_index_zero_based':ix,'codes':m['codes'].split(';'),'interpretation':m['interpretation'],'alternative_or_limit':m['alternative_or_limit'],'original_text':r['text_original'],'source_locator':r['last_source']['source_locator'],'product_name':r['product_name'],'source_url':r['source_url'],'rating':r['rating'],'scope':r['scope'],'review_date_field':r['review_date_field'],'date_fields_disagree':r['date_fields_disagree'],'reviewer':'assistant_close_reading_not_independent_human_fieldwork'})
 assert random_indexes.issubset({int(r['main_review_index_zero_based']) for r in anns})
 assert len({x['record_key'] for x in anns})==len(anns)
 writejsonl('qualitative_evidence.jsonl.gz',anns);csvwrite('qualitative_evidence.csv.gz',anns)
 (HERE/'qualitative_evidence.md').write_text('# Close-reading evidence ledger\n\nAssistant annotations; not independent human validation. Source locators are zero-based JSON array indexes of the immutable original files. Random calibration is distinct from purposive mechanism examples. None identifies confirmed young Premium-to-Basic switchers.\n\n'+'\n\n'.join(f"## {a['annotation_id']} — {a['record_key']}\n\nSelection: {a['selection']}; {a['scope']}.\n\n> "+(a['original_text'] or '').replace('\n','\n> ')+f"\n\nInterpretation: {a['interpretation']}\n\nLimit: {a['alternative_or_limit']}\n\nSource: `{a['source_locator']}`; [product]({a['source_url']})." for a in anns)+'\n',encoding='utf8')
 texts=collections.defaultdict(list)
 for r in out:
  if r['text_normalized']:texts[r['text_normalized'].casefold()].append(r['record_key'])
 dup=[{'normalized_text':t,'record_keys':ids,'count':len(ids)} for t,ids in texts.items() if len(ids)>1]
 writejsonl('duplicate_text_groups.jsonl.gz',dup)
 stats={'source_files':source,'tokopedia':{'export_rows':sum(s['row_count'] for s in source if 'tokopedia' in s['original_filename']),'review_occurrences':len(occ),'unique_review_ids':len(out),'repeated_identity_occurrences':len(occ)-len(out),'records_with_changed_payload_across_exports':sum(len(v)>1 for v in payload_hashes.values()),'product_observations':len(products),'unique_product_ids':len({r['productId'] for r in products}),'review_product_count':len({r['product_id'] for r in out}),'billing_notice_rows':len(notices),'nonempty_text':sum(bool(r['text_normalized']) for r in out),'text_information_state':dict(collections.Counter(r['text_information_state'] for r in out)),'ratings':dict(collections.Counter(r['rating'] for r in out)),'product_scope_reviews':dict(collections.Counter(r['product_scope'] for r in out)),'date_fields_both_present':sum(bool(r['review_date_field'] and r['review_time_field']) for r in out),'missing_reviewTime':sum(not r['review_time_field'] for r in out),'missing_reviewDate':sum(not r['review_date_field'] for r in out),'date_fields_disagree':sum(r['date_fields_disagree'] for r in out),'scope_by_unverified_reviewDate':dict(collections.Counter(r['scope'] for r in out)),'possible_misassigned_text':sum(r['possible_misassigned_text'] for r in out),'eligible_written_toothpaste_candidates':sum(r['eligible_written_toothpaste_candidate'] for r in out),'candidate_tag_counts_nonexclusive':dict(collections.Counter(t for r in out for t in r['candidate_tags'])),'exact_normalized_duplicate_text_groups':len(dup),'records_in_duplicate_text_groups':sum(len(x['record_keys']) for x in dup),'close_read_annotations':len(anns),'seeded_random_calibration':sum(a['selection']=='seeded_random_calibration' for a in anns),'purposive_annotations':sum(a['selection']!='seeded_random_calibration' for a in anns),'age_verified_count':0,'premium_to_basic_verified_count':0,'actor_reported_event_charges_usd':[float(re.search(r'\$(\d+\.\d+)',x['notice']).group(1)) for x in notices],'actor_reported_event_charge_sum_usd':round(sum(float(re.search(r'\$(\d+\.\d+)',x['notice']).group(1)) for x in notices),6),'charges_scope':'sum of notices; not account bill or independently audited cost'},'shopee':{'excluded_rows':len(excluded),'error_records':sum(r['source_type']=='error' for r in excluded),'irrelevant_UGREEN_reviews':sum(r['source_type']=='review' for r in excluded),'delivered_target_reviews':0,'UGREEN_nonempty_comments':sum(bool((r['raw_payload'].get('comment') or '').strip()) for r in excluded if r['source_type']=='review')},'caveats':['Unique record IDs are not unique people.','No target demographics or Premium-to-Basic switching verified.','Candidate lexical tags are not validated qualitative classifications or population estimates.','Current listed prices are not observed paid prices.','Dates are unresolved source fields; case-period slices are provisional.']}
 (HERE/'stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in stats['tokopedia'].items() if k!='source_files'},ensure_ascii=False))
if __name__=='__main__':main()

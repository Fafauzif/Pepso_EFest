#!/usr/bin/env python3
"""Portable written-record archive + descriptive candidate screening; stdlib.

This is a record inventory, not an eligible-consumer sample. No theme is a
validated behaviour merely because a string matches a pattern.
"""
import csv,gzip,hashlib,json,re
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter,defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
C=ROOT/'research/2026-11-03/closure'
OUT=C/'integrated'
PATTERNS={
 'household_payer':r'\b(parents?|family|families|household|mother|father|husband|wife|keluarga|ortu|bonyok|dibeliin|dibelikan|suami|istri|anak kos|dikosan|di kos|mamaku|ibuku|ayahku)\b',
 'price_promotion':r'\b(prices?|expensive|afford\w*|discount\w*|promo\w*|cheap\w*|mahal|murah|diskon|harga|hemat|cashback|voucher)\b',
 'repeat_continuation':r'\b(repurchase\w*|reorder\w*|repeat\w*|buy again|buying again|keep using|bought again|beli lagi|repeat order|langganan|selalu pak[ae]i?|sudah lama pak[ae]i?|sdh lama pak[ae]i?|bertahun|thnan)\b',
 'switching':r'\b(switch\w*|changed brands?|ganti|berganti|beralih|balik lagi|kembali ke|pindah)\b',
 'availability':r'\b(out of stock|in stock|hard to find|unavailable|availability|sold out|stok|stock|kosong|langka|langkah|susah cari|susah nyari|susah dicari|habis|alfamart|indomaret|warung|minimarket)\b',
 'sensory':r'\b(taste\w*|aftertaste|foam\w*|fresh\w*|dry\w*|irritat\w*|mint\w*|busa|rasa|segar|kering|perih|sariawan|pedes|pedas|asem|huek|mual)\b',
 'benefit_need':r'\b(sensitiv\w*|whiten\w*|pain|relief|sensitivity|ngilu|sensitif|putih|kuning|gusi|berlubang|bersih)\b',
}
RX={k:re.compile(v,re.I) for k,v in PATTERNS.items()}
def rows(path):
    with gzip.open(path,'rt',encoding='utf-8') as f:
        for line in f:
            if line.strip():yield json.loads(line)
def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def inputs():
    old=ROOT/'research/2026-11-03/scale_pipeline/clean/export/records.jsonl.gz'
    if not old.exists():raise SystemExit('Restore the legacy input first: python scripts/restore_large_files.py --only '+old.relative_to(ROOT).as_posix())
    yield 'earlier_integrated_store',old,rows(old)
    for label,rel in [('x_user_exports','x/records.jsonl.gz'),('tiktok_user_export','tiktok/clean/comments.jsonl.gz'),('tokopedia_user_exports','tokopedia/reviews_clean.jsonl.gz')]:
        p=C/rel;yield label,p,rows(p)
    p=C/'x/legacy_x_overlap.json'
    legacy=json.loads(p.read_text())
    def legacyrows():
        for item in legacy:
            if item['overlaps_new_exports']:continue
            r=item['original_record']
            yield {'record_key':'x:'+item['source_record_id'],'platform':'x','source_record_id':item['source_record_id'],'source_url':item['source_url'],'text_original':r['text_excerpt'],'record_type':'post_excerpt','content_date':r.get('created_at_from_snowflake'),'scope':'case_historical','relevance_status':'brand_owned_marketing_excerpt','incentive_status':'brand_owned_marketing','text_is_excerpt':True,'age_verified':False,'premium_to_basic_verified':False,'first_locator':{'source_file':'research/2026-11-03/scale_tools/clean/x_public_sample.json','record_id':r['record_id']}}
    yield 'earlier_nonoverlapping_x_excerpts',p,legacyrows()

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    for p in OUT.glob('records-*.jsonl.gz'):p.unlink()
    (OUT/'RULE_PATTERNS.json').write_text(json.dumps(PATTERNS,indent=2)+'\n')
    seen=set();platforms=Counter();scopes=Counter();incentives=Counter();tags=defaultdict(Counter);periods=defaultdict(Counter);fingerprints=defaultdict(list);sources=[];shards=[];fo=None;z=None;n=0
    def close_shard():
        nonlocal z,fo
        if z:
            z.close();fo.close();p=OUT/shards[-1]['path'];shards[-1].update(bytes=p.stat().st_size,sha256=sha(p));z=None;fo=None
    for label,path,stream in inputs():
        source={'label':label,'path':path.relative_to(ROOT).as_posix(),'sha256':sha(path),'rows_seen':0,'written_retained':0,'blank_excluded':0,'repeated_identity_excluded':0};sources.append(source)
        for r in stream:
            source['rows_seen']+=1;text=r.get('text_original') or ''
            if not text.strip():source['blank_excluded']+=1;continue
            key=r['record_key']
            if key in seen:source['repeated_identity_excluded']+=1;continue
            seen.add(key);source['written_retained']+=1
            platform=r['platform'].lower()
            scope=r.get('scope',r.get('case_scope','unknown_date'))
            r['unified_scope']=scope;r['source_specific_dataset']=path.relative_to(ROOT).as_posix();r['platform']=platform
            dt=r.get('content_date') or r.get('review_date_field')
            try:
                parsed=datetime.fromisoformat(dt.replace('Z','+00:00'))
                if parsed.tzinfo:parsed=parsed.astimezone(ZoneInfo('Asia/Jakarta'))
                day=parsed.date().isoformat()
                period='pre_2022' if day<'2022-01-01' else 'case_2022_H1_2026' if day<'2026-07-01' else 'post_H1_2026'
            except (ValueError,TypeError,AttributeError):period='unknown_date'
            r['calendar_period_jakarta']=period
            r['calendar_period_is_case_eligibility']=False
            r['calendar_date_quality']='unverified_reviewDate_field' if platform=='tokopedia' else 'preserve_source_specific_quality'
            periods[platform][period]+=1
            r['screening_tags']=[k for k,rx in RX.items() if rx.search(text)]
            r['screening_status']='lexical_candidates_not_individually_validated'
            r.setdefault('record_type','post' if platform=='x' else 'comment')
            r['age_verified']=bool(r.get('age_verified',False));r['premium_to_basic_verified']=bool(r.get('premium_to_basic_verified',r.get('confirmed_pepsodent_premium_to_basic_switch',False)))
            platforms[platform]+=1;scopes[scope]+=1;incentives[str(r.get('incentive_status','unknown'))]+=1
            for tag in r['screening_tags']:tags[platform][tag]+=1
            norm=' '.join(text.casefold().split());fingerprints[hashlib.sha256(norm.encode()).hexdigest()].append((key,platform))
            if n%20000==0:
                close_shard();name=f'records-{len(shards)+1:04d}.jsonl.gz';shards.append({'path':name,'rows':0});fo=(OUT/name).open('wb');z=gzip.GzipFile(filename='',fileobj=fo,mode='wb',mtime=0,compresslevel=6)
            z.write((json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n').encode());shards[-1]['rows']+=1;n+=1
    close_shard()
    copied=0;cross=0
    with gzip.open(OUT/'exact_text_groups.jsonl.gz','wt',encoding='utf-8') as f:
        for fingerprint,members in fingerprints.items():
            if len(members)<2:continue
            ps=sorted({p for _,p in members});copied+=1;cross+=len(ps)>1
            f.write(json.dumps({'text_fingerprint':fingerprint,'records':len(members),'platforms':ps,'record_keys':[k for k,_ in members],'interpretation':'identical normalized text; not proof of same person, paid promotion, or bot'},ensure_ascii=False)+'\n')
    stats={'written_records_all_retained_scopes':n,'platforms':dict(platforms),'scopes':dict(scopes),'calendar_period_jakarta_by_platform':{k:dict(v) for k,v in periods.items()},'incentive_status':dict(incentives),'sources':sources,'exact_normalized_text_groups':copied,'cross_platform_exact_text_groups':cross,'screening_tag_counts_by_platform':{k:dict(v) for k,v in tags.items()},'shards':shards,'verified_age_count':0,'verified_target_switcher_count':0,'interpretation':'Inventory of retained written records across eligible and ineligible scopes, not an independent-consumer or verified-toothpaste sample. Lexical tags are unvalidated candidates. Do not pool platform denominators or infer prevalence. Calendar period is not case applicability or demographic eligibility. Earlier narrow six-post X sample contributes five nonoverlapping marketing excerpts; its overlapping consumer story is represented once in the new X data.'}
    (OUT/'INVENTORY.json').write_text(json.dumps(stats,indent=2,ensure_ascii=False)+'\n')
    with (OUT/'screening_counts.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['platform','written_inventory_denominator','candidate_tag','candidate_record_count','status'])
        for p,counter in tags.items():
            for k,count in counter.items():w.writerow([p,platforms[p],k,count,'unvalidated_lexical_screening_not_prevalence'])
    print(json.dumps({'written_records':n,'platforms':dict(platforms),'shards':len(shards),'max_shard_bytes':max(s['bytes'] for s in shards),'exact_text_groups':copied,'cross_platform_groups':cross}))
if __name__=='__main__':main()

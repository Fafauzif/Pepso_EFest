#!/usr/bin/env python3
"""Rebuild TikTok normalized observations and transparent descriptive diagnostics.

Python stdlib only. Source remains immutable. Qualitative annotations are separate.
"""
import argparse
import collections
import csv
import datetime as dt
import gzip
import hashlib
import io
import json
from pathlib import Path
import random
import re

HERE = Path(__file__).resolve().parent
SOURCE_NAME = 'dataset_tiktok-comments-scraper_2026-11-03_12-02-32-061.json'
PATTERNS = {
    'household_payer_candidate': r'orang ?tua|ortu|orty|bonyok|dibeliin|keluarga|anak kos|dikosan|di kos|dirumah|di rumah|mama|mamah|suami|istri',
    'switch_repeat_candidate': r'ganti|beralih|balik|repeat|langganan|beli lagi|selalu pak|selalu pake|udah lama|sudah lama|habis.*beli|abis.*beli',
    'price_promo_candidate': r'mahal|murah|harga|pricey|diskon|promo|boros|hemat|[0-9]+\s?(?:rb|ribu|k)\b',
    'sensory_candidate': r'rasa|mint|segar|bersih|busa|kering|perih|asem|asam|pahit|pedas|pedes|enak|sensitif|ngilu|sariawan',
    'experience_result_candidate': r'aku pake|aku pakai|gue pake|gw pake|udah pake|sudah pakai|udah pakai|sudah pake|ga mempan|gamempan|gak mempan|ga ngaruh|gak ngaruh|ga ada perubahan|gak ada perubahan|gada perubahan|putih|kuning|cocok',
    'availability_candidate': r'indomaret|alfamart|watson|guardian|shopee|tokopedia|langka|langkah|susah.*(?:cari|beli)|ga ada dimana|gak ada dimana|gaada dimana|blm ada|belum ada',
    'recommendation_question_candidate': r'\?|rekomen|rekomendasi|saran|yang mana|yg mana|bagus mana|gimana|bagaimana',
    'explicit_offtopic_candidate': r'parfum|sepatu|cysteamine|niacinamide|naicinamide|vitamin c|skincare|vaseline|ettics|tesavara|memoi?re|sunscreen',
}
ORAL = re.compile(r'gigi|odol|tooth|pepsodent|sensodyne|sensoden|sensodin|colgate|close\s?up|enzim|marvis|darlie|zact|usmile|antiplaq|finest|fluor|ngilu|gusi|floss|floser|flosser|kumur|water ?floss|whitening',re.I)

def dump(path, obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def jsonlgz(path, rows):
    with path.open('wb') as raw, gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as z:
        for row in rows:z.write((json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n').encode())

def csvwrite(path, rows, fields):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for row in rows:
            w.writerow({k:json.dumps(row.get(k),ensure_ascii=False) if isinstance(row.get(k),(list,dict)) else row.get(k) for k in fields})

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path)
    args=parser.parse_args()
    candidates=[args.source] if args.source else []
    repo=HERE.parents[3]
    candidates += [repo/'research/2026-11-03/closure/raw/user_runs'/(SOURCE_NAME+'.gz'),repo/'data/raw/user_runs'/SOURCE_NAME,repo/'data/raw/user_runs'/(SOURCE_NAME+'.gz'),repo/'research/2026-11-03/closure/raw'/SOURCE_NAME,repo.parent/'upload'/SOURCE_NAME]
    source=next((p for p in candidates if p and p.exists()),None)
    if source is None:raise SystemExit('Source missing; pass --source PATH to the preserved JSON or JSON.gz')
    raw=gzip.decompress(source.read_bytes()) if source.suffix=='.gz' else source.read_bytes()
    payload=json.loads(raw); rawhash=hashlib.sha256(raw).hexdigest()
    by_id={};occurrences=[];conflicts=[]
    for i,r in enumerate(payload,1):
        cid=str(r['cid']);key='tiktok:'+cid
        if cid in by_id and r != by_id[cid][1]:conflicts.append({'record_key':key,'source_row_1based':i})
        by_id.setdefault(cid,(i,r));occurrences.append({'record_key':key,'source_file':SOURCE_NAME,'source_sha256':rawhash,'source_row_1based':i,'source_locator':f'{SOURCE_NAME}#row={i}'})
    ids=set(by_id);norm=[]
    for cid,(i,r) in by_id.items():
        text=r.get('text');s=text or '';parent=str(r['repliesToId']) if r.get('repliesToId') else None
        parsed=dt.datetime.fromisoformat(r['createTimeISO'].replace('Z','+00:00'))
        ts=dt.datetime.fromtimestamp(r['createTime'],tz=dt.timezone.utc)
        local=parsed.astimezone(dt.timezone(dt.timedelta(hours=7)))
        scope='case_2022_H1_2026' if '2022-01-01'<=local.date().isoformat()<'2026-07-01' else ('pre_2022_context' if local.year<2022 else 'post_H1_2026_context')
        scope_utc='case_2022_H1_2026' if '2022-01-01'<=parsed.date().isoformat()<'2026-07-01' else ('pre_2022_context' if parsed.year<2022 else 'post_H1_2026_context')
        video=r['videoWebUrl'].split('?')[0];vid=video.rsplit('/',1)[-1]
        tags=[k for k,p in PATTERNS.items() if re.search(p,s,re.I)]
        relevance='blank' if not s.strip() else ('explicit_offtopic_candidate' if 'explicit_offtopic_candidate' in tags else ('self_contained_oralcare_candidate' if ORAL.search(s) else 'context_dependent_unresolved'))
        norm.append({'record_key':'tiktok:'+cid,'platform':'tiktok','source_record_id':cid,'record_type':'reply' if parent else 'root_comment','text_original':text,'text_normalized':' '.join(s.split()),'text_present':bool(s.strip()),'text_substantive_not_established':True,'video_id':vid,'video_url':video,'source_url':video+'?comment_id='+cid,'parent_record_id':parent,'parent_in_export':parent in ids if parent else None,'content_date':r['createTimeISO'],'content_date_jakarta':local.isoformat(),'case_scope_utc':scope_utc,'timestamp_epoch_utc':r['createTime'],'date_fields_agree_to_second':parsed.replace(microsecond=0)==ts,'case_scope':scope,'relevance_candidate':relevance,'candidate_tags':tags,'author_pseudonym':'tt-'+hashlib.sha256(str(r.get('uid','')).encode()).hexdigest()[:16] if r.get('uid') else None,'like_count':r.get('diggCount'),'declared_replies':r.get('replyCommentTotal'),'age_verified':False,'premium_to_basic_verified':False,'incentive_status':'not_established','source_file':SOURCE_NAME,'source_row_1based':i,'source_locator':f'{SOURCE_NAME}#row={i}','source_sha256':rawhash})
    norm.sort(key=lambda r:r['source_row_1based'])
    groups=collections.defaultdict(list)
    for r in norm:
        if r['text_normalized']:groups[r['text_normalized'].casefold()].append(r['source_record_id'])
    dup=[{'normalized_text':t,'record_ids':v,'count':len(v)} for t,v in groups.items() if len(v)>1]
    video=[]
    for vid in sorted({r['video_id'] for r in norm}):
        rows=[r for r in norm if r['video_id']==vid];video.append({'video_id':vid,'video_url':rows[0]['video_url'],'exported_comments':len(rows),'roots':sum(r['parent_record_id'] is None for r in rows),'replies':sum(r['parent_record_id'] is not None for r in rows),'blank':sum(not r['text_present'] for r in rows),'reached_input_180_comment_cap':len(rows)>=180,'video_caption_available_in_export':False,'video_publication_date_available_in_export':False,'case_window_comments':sum(r['case_scope']=='case_2022_H1_2026' for r in rows),'self_contained_oralcare_candidate':sum(r['relevance_candidate']=='self_contained_oralcare_candidate' for r in rows)})
    stats={'source_file':SOURCE_NAME,'source_sha256':rawhash,'export_rows':len(payload),'unique_comment_ids':len(norm),'duplicate_id_occurrences':len(payload)-len(norm),'conflicting_id_payloads':len(conflicts),'written_nonblank':sum(r['text_present'] for r in norm),'blank':sum(not r['text_present'] for r in norm),'videos':len(video),'roots':sum(r['parent_record_id'] is None for r in norm),'replies':sum(r['parent_record_id'] is not None for r in norm),'reply_parent_present':sum(r['parent_in_export'] is True for r in norm),'reply_parent_missing':sum(r['parent_in_export'] is False for r in norm),'date_fields_disagree':sum(not r['date_fields_agree_to_second'] for r in norm),'date_span_utc':[min(r['content_date'] for r in norm),max(r['content_date'] for r in norm)],'case_scope':dict(collections.Counter(r['case_scope'] for r in norm)),'case_scope_timezone':'Asia/Jakarta UTC+07','case_scope_utc':dict(collections.Counter(r['case_scope_utc'] for r in norm)),'timezone_boundary_changed_records':[r['source_record_id'] for r in norm if r['case_scope']!=r['case_scope_utc']],'relevance_candidate':dict(collections.Counter(r['relevance_candidate'] for r in norm)),'candidate_tags':dict(collections.Counter(t for r in norm for t in r['candidate_tags'])),'videos_at_180_cap':sum(v['reached_input_180_comment_cap'] for v in video),'exact_normalized_copied_text_groups':len(dup),'records_in_copied_text_groups':sum(g['count'] for g in dup),'extra_occurrences_of_copied_text':sum(g['count']-1 for g in dup),'distinct_observed_uid_pseudonyms':len({r['author_pseudonym'] for r in norm if r['author_pseudonym']}),'top_author_comment_counts':collections.Counter(r['author_pseudonym'] for r in norm if r['author_pseudonym']).most_common(10),'verified_age_count':0,'verified_premium_to_basic_count':0,'interpretation':'All theme counts are transparent lexical candidates in a purposive 18-video export, not validated themes, people, prevalence, or efficacy.'}
    clean=HERE/'clean';clean.mkdir(parents=True,exist_ok=True)
    jsonlgz(clean/'comments.jsonl.gz',norm);jsonlgz(clean/'occurrences.jsonl.gz',occurrences)
    csvwrite(clean/'comments.csv',norm,list(norm[0]))
    with (clean/'comments.csv.gz').open('wb') as raw_out,gzip.GzipFile(fileobj=raw_out,mode='wb',mtime=0,filename='') as z:z.write((clean/'comments.csv').read_bytes())
    dump(HERE/'stats.json',stats);dump(clean/'copied_text_groups.json',dup);dump(clean/'conflicts.json',conflicts);csvwrite(clean/'video_coverage.csv',video,list(video[0]))
    # Fixed random calibration: two comments per video; additions are purposive lexical candidates.
    rng=random.Random(20261103);selected={};
    for v in video:
        candidates=[r for r in norm if r['video_id']==v['video_id']]
        for r in rng.sample(candidates,min(2,len(candidates))):selected[r['source_record_id']]=(r,'random_calibration_two_per_video')
    weighted=[]
    for r in norm:
        if r['source_record_id'] in selected:continue
        tags=r['candidate_tags'];score=5*('household_payer_candidate' in tags)+4*('switch_repeat_candidate' in tags)+2*('experience_result_candidate' in tags)+('price_promo_candidate' in tags)+('availability_candidate' in tags)
        if score:weighted.append((score,r))
    weighted.sort(key=lambda x:(-x[0],x[1]['source_row_1based']))
    pervideo=collections.Counter(r['video_id'] for r,_ in selected.values())
    for score,r in weighted:
        if len(selected)>=100:break
        if pervideo[r['video_id']]>=12:continue
        selected[r['source_record_id']]=(r,'purposive_mechanism_candidate_score_'+str(score));pervideo[r['video_id']]+=1
    sample=[]
    for r,method in sorted(selected.values(),key=lambda x:x[0]['source_row_1based']):
        sample.append({'sample_id':len(sample)+1,'source_record_id':r['source_record_id'],'source_row_1based':r['source_row_1based'],'source_locator':r['source_locator'],'video_id':r['video_id'],'source_url':r['source_url'],'content_date':r['content_date'],'case_scope':r['case_scope'],'text_original':r['text_original'],'selection_method':method,'candidate_tags':r['candidate_tags']})
    dump(HERE/'sample_selection.json',sample);dump(HERE/'rule_patterns.json',PATTERNS)
    print(json.dumps(stats,ensure_ascii=False,indent=2));print('Qualitative selection',len(sample))

if __name__=='__main__':main()

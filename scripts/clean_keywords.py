#!/usr/bin/env python3
"""Rebuild cleaned research data from immutable pasted inputs. Python 3.10+, stdlib only."""
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUTS = [
    ('source_01', 'Pasted text(20261102-164123).txt', 'tab_separated'),
    ('source_02', 'Pasted text(20261102-164734).txt', 'tab_separated'),
    ('source_03', 'Pasted text (3).txt', 'vertical_page'),
]
INTENTS = {'Informational', 'Navigational', 'Commercial', 'Transactional'}

def status(s):
    if not s.strip(): return 'blank'
    if s.strip().lower() in {'n/a', 'na', '-'}: return 'not_available'
    return 'zero' if float(s.replace(',', '')) == 0 else 'positive'

def number(s, integer=False):
    if status(s) in {'blank', 'not_available'}: return None
    v = float(s.replace(',', ''))
    return int(v) if integer else v

def normalize(s):
    return ' '.join(unicodedata.normalize('NFKC', s).casefold().split())

def tags(k):
    rules = {
        'sensitivity': ['sensitif', 'sensitive', 'sensitiv', 'ngilu', 'enamel', 'email gigi', 'hydroxyapatite'],
        'whitening': ['whit', 'putih', 'kuning', 'noda', 'charcoal', 'bleaching'],
        'gum_care': ['gusi', 'gum expert'],
        'freshness': ['bau mulut', 'nafas', 'napas', 'fresh', 'mint'],
        'price_promotion': ['harga', 'murah', 'mahal', 'promo', 'diskon', 'gratis', 'bundling', 'value pack'],
        'comparison_switching': [' vs ', 'alternatif', 'pengganti', 'ganti pasta', 'perbedaan'],
        'reviews_recommendations': ['review', 'ulasan', 'rekomendasi', 'terbaik', 'yang bagus'],
        'ingredients_safety_trust': ['kandungan', 'bahan', 'fluoride', 'sls', 'aman', 'halal', 'bpom', 'dokter', 'palsu', 'boikot'],
        'habits_usage': ['cara ', 'sikat gigi', 'menyikat', 'takaran', 'berkumur', 'berapa lama', 'setiap hari'],
        'adjacent_oral_care': ['scaling', 'bleaching', 'strip', 'floss', 'obat kumur', 'mouthwash', 'elektrik'],
    }
    return [t for t, terms in rules.items() if any(x in k for x in terms)] or ['general_or_other']

def brand(k):
    brands = ['pepsodent', 'sensodyne', 'colgate', 'darlie', 'close up', 'formula', 'ciptadent', 'enzim', 'systema', 'zact']
    return [b for b in brands if re.search(r'(?<!\w)' + re.escape(b) + r'(?!\w)', k)]

def parse_tab(text):
    output = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if not line.strip(): continue
        vals = next(csv.reader([line], delimiter='\t'))
        assert len(vals) == 7, (line_no, vals)
        keyword, intent, vol, kd, cpc, serp, updated = vals
        output.append(dict(keyword_raw=keyword, intent_raw=intent, volume_raw=vol,
                           kd_raw=kd, cpc_raw=cpc, serp_features_raw=serp,
                           trend_raw=None, updated_raw=updated,
                           source_line_start=line_no, source_line_end=line_no))
    return output

def parse_vertical(text):
    lines = text.splitlines()
    query_start = lines.index('100/100') + 1
    query_end = lines.index('Examples:')
    entered = [x.strip() for x in lines[query_start:query_end] if x.strip() and x.strip() != '\ufeff']
    start = lines.index('Selected:') + 2
    end = lines.index('Contact us', start)
    indexed = [(i+1, lines[i].strip()) for i in range(start, end) if lines[i].strip()]
    groups, current = [], []
    for item in indexed:
        current.append(item)
        if re.fullmatch(r'\d+\s+(?:min|month|months|day|days|hour|hours)|Now', item[1]):
            groups.append(current); current=[]
    assert not current, current
    out=[]
    for g in groups:
        tokens=[v for _,v in g]; keyword=tokens[0]; p=1; intents=[]
        while p < len(tokens) and tokens[p] in INTENTS:
            label=tokens[p]; intents.append(label); p+=1
            assert tokens[p] == label[0], (keyword, tokens)
            p+=1
        vals=tokens[p:-1]
        if len(vals)==3:
            vol,kd,cpc=vals; trend=None
        else:
            assert len(vals)==4 and vals[0]=='n/a' and vals[1]=='n/a', (keyword, vals)
            vol,trend,kd,cpc=vals
        out.append(dict(keyword_raw=keyword, intent_raw=', '.join(intents), volume_raw=vol,
                        kd_raw=kd, cpc_raw=cpc, serp_features_raw=None,
                        trend_raw=trend, updated_raw=tokens[-1],
                        source_line_start=g[0][0], source_line_end=g[-1][0]))
    assert len(entered)==100 and len(out)==100
    assert Counter(entered)==Counter(r['keyword_raw'] for r in out), 'Input list and result rows differ'
    return out

def write_csv(path, rows):
    assert rows
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def main():
    dest=ROOT/'data/clean';dest.mkdir(parents=True, exist_ok=True)
    observations=[];sources=[]
    for sid, filename, layout in INPUTS:
        path=ROOT/'data/raw'/filename
        data=path.read_bytes();text=data.decode('utf-8-sig')
        rows=parse_tab(text) if layout=='tab_separated' else parse_vertical(text)
        for n,r in enumerate(rows,1):
            k=normalize(r['keyword_raw']);flags=[]
            vol=number(r['volume_raw'],True);kd=number(r['kd_raw'],True);cpc=number(r['cpc_raw'])
            if kd is not None: assert 0<=kd<=100
            if vol is not None: assert vol>=0
            if layout=='tab_separated':flags+=['headers_inferred','cpc_currency_unconfirmed']
            if cpc is not None and cpc>100000:flags+=['cpc_numeric_outlier_gt_100000']
            if k in {'close up','formula','enzim'}:flags+=['ambiguous_generic_brand_term']
            if not r['intent_raw']:flags+=['intent_missing']
            record=dict(observation_id=f'{sid}_{n:03}',keyword=k,**r,
                search_volume=vol,volume_status=status(r['volume_raw']),kd_percent=kd,
                cpc_value=cpc,cpc_currency='IDR' if layout=='vertical_page' else None,
                cpc_analysis_value=cpc if layout=='vertical_page' and (cpc is None or cpc<=100000) else None,
                intents=[x.strip() for x in r['intent_raw'].split(',') if x.strip()],
                serp_features=[x.strip() for x in (r['serp_features_raw'] or '').split(',') if x.strip()],
                serp_capture_status='not_copied' if layout=='vertical_page' else 'copied',
                trend_capture_status='not_available' if r['trend_raw']=='n/a' else 'not_copied',
                country_requested='Indonesia',country_verified_in_capture=False,
                retrieval_date=None,packaged_date='2026-11-03',source_id=sid,
                source_file=f'data/raw/{filename}',layout=layout,
                brands=brand(k),theme_tags=tags(k),quality_flags=flags)
            observations.append(record)
        sources.append(dict(source_id=sid,path=str(path.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest(),
                            rows=len(rows),layout=layout,volume_status_counts=dict(Counter(status(r['volume_raw']) for r in rows))))
    grouped=defaultdict(list)
    for r in observations:grouped[r['keyword']].append(r)
    conflicts=[];unique=[]
    for k, group in sorted(grouped.items()):
        signatures={json.dumps({c:r[c] for c in ['search_volume','volume_status','kd_percent','cpc_value','intent_raw']},sort_keys=True) for r in group}
        if len(signatures)>1:
            conflicts.append({'keyword':k,'observation_ids':[r['observation_id'] for r in group]})
            continue
        row=dict(group[0]);row['observation_ids']=[r['observation_id'] for r in group];row['observation_count']=len(group);unique.append(row)
    def flat(rows):
        return [{k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in rows]
    write_csv(dest/'keyword_observations.csv',flat(observations))
    write_csv(dest/'keywords_unique.csv',flat(unique))
    (dest/'keyword_observations.json').write_text(json.dumps(observations,ensure_ascii=False,indent=2)+'\n')
    (dest/'keywords_unique.json').write_text(json.dumps(unique,ensure_ascii=False,indent=2)+'\n')
    (dest/'duplicate_conflicts.json').write_text(json.dumps(conflicts,ensure_ascii=False,indent=2)+'\n')
    issues=[{'observation_id':r['observation_id'],'keyword':r['keyword'],'quality_flags':'; '.join(r['quality_flags']),'cpc_raw':r['cpc_raw']} for r in observations if r['quality_flags']]
    write_csv(dest/'quality_flags.csv',issues)
    report=dict(observation_count=len(observations),unique_keyword_count=len(grouped),unique_view_rows=len(unique),
                duplicate_keyword_groups=sum(len(g)>1 for g in grouped.values()),conflict_groups=len(conflicts),
                volume_status_counts=dict(Counter(r['volume_status'] for r in observations)),
                cpc_outlier_count=sum('cpc_numeric_outlier_gt_100000' in r['quality_flags'] for r in observations),
                sources=sources,missing_sources=['Pasted text (2)(1).txt'],
                validation=['7 fields per tab row','100 query inputs match 100 vertical result rows','KD range 0-100',
                            'nonnegative volume','no null-to-zero imputation','normalized keys retain spelling variants'])
    (ROOT/'docs/quality_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()

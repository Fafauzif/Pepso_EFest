from pathlib import Path
from collections import Counter
import json,gzip,re,csv
R=Path(__file__).parent
patterns={'sensory_language':r'\b(taste|flavou?r|mint|foam|burn|aftertaste|fresh)\w*\b','price_value_language':r'\b(expensive|price|worth|cost|cheap)\w*\b','pack_language':r'\b(tubes?|caps?|size|small|large|pack)\w*\b','repeat_language':r'\b(repurchase|buy again|bought again|reorder|repeat)\w*\b','household_language':r'\b(husband|wife|family|daughter|son|mom|mother|dad|father|parents)\b','need_result_language':r'\b(whiten|sensitive|sensitivity|pain|results)\w*\b'}
regex={k:re.compile(v,re.I) for k,v in patterns.items()}
seen=set();counts=Counter();flags=Counter();years=Counter();ratings=Counter();examples={k:[] for k in patterns};scanned=0;retained=0
for d in [R,R/'health_household']:
 p=d/'clean/reviews_classified.jsonl.gz'
 if not p.exists(): continue
 with gzip.open(p,'rt',encoding='utf-8') as f:
  for line in f:
   x=json.loads(line);scanned+=1;k=x['canonical_identity']
   if k in seen:continue
   seen.add(k);counts[x['product_scope']]+=1
   if x['product_scope']!='adult_human_toothpaste_title_candidate':continue
   text=x.get('review_text') or ''
   if not text.strip():continue
   retained+=1;year=(x.get('published_at_utc') or 'unknown')[:4];years[year]+=1;ratings[str(x.get('rating'))]+=1
   for name,pat in regex.items():
    if pat.search(text):
     flags[name]+=1
     if len(examples[name])<30: examples[name].append({'record_id':x['record_id'],'product_id':x['product_id'],'product_name':x['product_name'],'published_at_utc':x.get('published_at_utc'),'source_line':x['source_line'],'source_url':x['source_url'],'scope':'nonIndonesia historical comparator; lexical candidate only'})
summary={'candidate_observations':scanned,'unique_candidate_identities':len(seen),'duplicate_observations':scanned-len(seen),'unique_scope_counts':dict(counts),'adult_title_candidate_written_reviews':retained,'exploratory_literal_cue_counts':dict(flags),'ratings_for_adult_title_candidate_written':dict(ratings),'years_for_adult_title_candidate_written':dict(sorted(years.items())),'patterns':patterns,'interpretation':'English lexical retrieval aids, NOT validated themes, effect sizes, sentiment or Indonesian switching prevalence; no manually read global corpus claimed'}
(R/'analysis_summary.json').write_text(json.dumps(summary,indent=2));(R/'lexical_example_locators.json').write_text(json.dumps(examples,indent=2))
print(json.dumps(summary,indent=2))

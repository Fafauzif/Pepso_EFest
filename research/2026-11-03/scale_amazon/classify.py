"""Conservative title-based scope strata; not clinical or demographic validation."""
from pathlib import Path
from collections import Counter
import json,re,gzip
ROOT=Path(__file__).parent
RULES=[('pet_or_nonhuman',r'\b(dogs?|puppy|puppies|cats?|pets?|canine|feline)\b'),('accessory_or_container',r'\b(squeezers?|dispensers?|holders?|racks?|organizers?|rollers?|refillable|empty)\b|toothpaste not included'),('child_or_infant',r'\b(kids?|children|child|toddlers?|baby|babies|paw patrol|training toothpaste)\b'),('adjacent_powder_or_alternative',r'\b(powder|tooth soap|toothsoap|tablets?|mouthwash|replacement)\b')]
def classify(t):
 for label,pat in RULES:
  if re.search(pat,t,re.I): return label
 if re.search(r'\b(tooth\s?paste|dentifrice)\b',t,re.I):return 'adult_human_toothpaste_title_candidate'
 return 'brand_matched_type_unresolved'
for d in [ROOT,ROOT/'health_household']:
 source=d/'clean/products.json'
 if not source.exists():continue
 ps=json.loads(source.read_text());categories={k:classify(v.get('title','')) for k,v in ps.items()}
 (d/'clean/product_scope.json').write_text(json.dumps(categories,indent=2))
 review=d/'clean/reviews.jsonl'
 if not review.exists():review=d/'clean/reviews.jsonl.gz'
 if not review.exists():continue
 summary=d/'summary.json'
 if not summary.exists():print('Collection not finalized:',d);continue
 counts=Counter();duplicates=0;seen=set();manual=[]
 dest=d/'clean/reviews_classified.jsonl.gz'
 with (gzip.open(review,'rt',encoding='utf-8') if review.suffix=='.gz' else review.open()) as f,gzip.open(dest,'wt',encoding='utf-8') as out:
  for line in f:
   x=json.loads(line);lab=categories[x['product_id']];x['product_scope']=lab;x['relevance_basis']='rule-based product title; not manual formulation verification';x['canonical_identity']='AMZ-'+x['record_id'].rsplit('-',1)[-1]
   if x['canonical_identity'] in seen:duplicates+=1
   seen.add(x['canonical_identity']);counts[lab]+=1
   out.write(json.dumps(x,ensure_ascii=False)+'\n')
 quality=dict(candidate_reviews=sum(counts.values()),unique_canonical_ids=len(seen),duplicate_ids=duplicates,review_scope_counts=dict(counts),candidate_products=len(ps),product_scope_counts=dict(Counter(categories.values())),rule_order=RULES,scope='historical international comparator only; no Indonesia inference; title classification not manual eligibility proof')
 (d/'classification_report.json').write_text(json.dumps(quality,indent=2))
 print(d.name,quality)

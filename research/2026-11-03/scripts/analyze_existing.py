"""Reproducible descriptive keyword and case-economics analysis. No new search volumes."""
from pathlib import Path
from collections import Counter
import json,csv,math
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/2026-11-03/synthesis'
OUT.mkdir(parents=True,exist_ok=True)
rows=json.loads((ROOT/'data/clean/keywords_unique.json').read_text())
summary={'unit':'keyword observation in existing purposive AI-seeded capture; not person',
 'newly_collected':False,'observations':len(rows),'volume_status':dict(Counter(r['volume_status'] for r in rows)),
 'country_verified':sum(r['country_verified_in_capture'] for r in rows),'overlapping_tags':dict(Counter(t for r in rows for t in r['theme_tags'])),
 'warnings':['No demand summation or market sizing','Location requested Indonesia but not verified','No inferred demographic, sentiment or causal switching evidence']}
(OUT/'existing_keywords_summary.json').write_text(json.dumps(summary,indent=2))
selected=sorted((r for r in rows if r['search_volume'] is not None),key=lambda x:x['search_volume'],reverse=True)
fields=['observation_id','keyword','search_volume','volume_status','source_file','source_line_start','source_line_end','country_verified_in_capture']
with (OUT/'existing_keyword_discovery.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:r[k] for k in fields} for r in selected)
# prices/weights below are organizer case facts; consumption assumptions illustrative only.
products=[('Basic case',24100,190),('Premium case regular',41900,100),('Premium case promo',23500,100)]
scenarios=[]
for name,price,g in products:
 for users in (1,2,4):
  for grams_per_brush in (0.5,1.0,1.5):
   daily=users*2*grams_per_brush
   scenarios.append(dict(product=name,price_idr=price,grams=g,users=users,brushing_per_day=2,assumed_grams_per_brush=grams_per_brush,modeled_days_per_tube=g/daily,modeled_30day_cost_idr=price/g*daily*30,price_per_100g=price/g*100,source='organizer case for price/grams; assumed usage for illustration; NOT dosing advice'))
with (OUT/'case_household_cost_scenarios.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(scenarios[0]));w.writeheader();w.writerows(scenarios)
financial={
 'basic_exact_price_per100g':24100/190*100,
 'premium_regular_unit_price_ratio':(41900/100)/(24100/190),
 'premium_promo_unit_price_ratio':(23500/100)/(24100/190),
 'case_premium_discount_percent':(1-23500/41900)*100,
 'case_premium_mix_decline_pp':27-20,
 'relative_mix_decline_percent':(1-20/27)*100,
 'brand_growth_needed_to_hold_absolute_premium_revenue_percent':(27/20-1)*100,
 'conditional_blended_margin_before_percent':27*.55+73*.38,
 'conditional_blended_margin_after_percent':20*.55+80*.38,
 'caveat':'Mix math assumes revenue basis, comparable periods, two representative tiers and fixed margins; not actual company margin or profit. Shelf price not manufacturer realization.'}
(OUT/'case_economics.json').write_text(json.dumps(financial,indent=2))
assert len(rows)==300 and sum(summary['volume_status'].values())==300
assert len(scenarios)==27
try:
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 plt.rcParams.update({'font.family':'DejaVu Sans','axes.spines.top':False,'axes.spines.right':False})
 fig,ax=plt.subplots(figsize=(9,5))
 names=['Basic\n190g','Premium regular\n100g','Premium promo\n100g']
 vals=[p/g*100 for _,p,g in products]
 bars=ax.bar(names,vals,color=['#64748b','#086f6b','#8cbab0'],width=.6)
 for b,v in zip(bars,vals):ax.text(b.get_x()+b.get_width()/2,v+700,f'Rp{v:,.0f}',ha='center',fontweight='bold')
 ax.set_ylim(0,49000);ax.set_ylabel('IDR per 100g');ax.set_title('A cheaper tube can still have a higher cost per gram',loc='left',fontweight='bold',pad=18)
 fig.text(.12,.01,'Source: organizer case examples; no current retail-price claim.\nPremium promo ticket: Rp23,500; Basic ticket: Rp24,100.',fontsize=9,color='#475569')
 fig.tight_layout(rect=(0,.08,1,1));fig.savefig(OUT/'case_unit_price.png',dpi=160);plt.close(fig)
except ImportError: pass
print(json.dumps({'summary':summary,'economics':financial},indent=2))

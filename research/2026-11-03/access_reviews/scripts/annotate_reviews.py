#!/usr/bin/env python3
"""Exploratory lexical flags plus a manually read, selected evidence table; no population inference."""
from pathlib import Path
import csv,collections,hashlib,json,re
B=Path(__file__).resolve().parents[1]
patterns={
 'sensory_language':r'mint|segar|bersih|busa|eneg|pedas|pedes|pahit|rasa|nyaman',
 'household_language':r'keluarga|suami|istri|ibu|emak|ortu|mama|mother|mom|dibeliin|dibelikan',
 'price_promotion_language':r'harga|diskon|promo|murah|hemat|bundl|voucher|ongkir|mahal',
 'pre_use_or_uncertain_result':r'belum dicoba|belum di coba|belum di buka|baru mau|semoga cocok|belum bisa di|blm di coba|belum tau hasil',
 'stock_availability_language':r'sering kosong|ready stock|susah cari|ga nemu|jarang.*ditemukan|harus ke watson',
 'repeat_language':r'sudah biasa pakai|sudah sering pakai|kesekian kalinya|beli lagi|repurchase|repeat order|langganan|balik ke',
 'sensitivity_language':r'ngilu|sensitif|sensitive|sensitivitas',
 'service_delivery_language':r'kurir|pengiriman|packing|paking|paket|seller|seler|pesanan',
}
selected={
 'LZD-1574262094522499':('satisfied_repeat_bundle_stock','Liked variant, buys bundle for savings, explicitly says it is often out of stock. One report cannot estimate stockout prevalence.'),
 'LZD-1200640450822499':('relief_and_episodic_expectation','Reports less sensitivity and intent to keep trying until symptoms resolve; does not say they later stopped.'),
 'LZD-2032630484394818':('household_sensory_experience','Reviewer relays husband experience: less nausea/foam and fresh mouth. Spouse reporting; payer and age unknown.'),
 'LZD-1324625217926021':('basic_to_complete8_counterexample','First Complete8 purchase after previously using red; an upgrade-direction narrative, no confirmed subsequent outcome.'),
 'LZD-1456695189922499':('discount_and_established_fit','Established use and perceived relief coexist with discounted purchase; discount is not necessarily low-value trial.'),
 'LZD-1551582562350987':('variant_substitution_after_runout','Sensodyne buyer tries whitening because usual deep clean ran out; availability/stock context not necessarily rejection.'),
 'LZD-1375814098174376':('buyer_user_separation','First purchase intended for mother with sensitivity; chooser/user separation explicit, age/payer unknown.'),
 'LZD-1539034206574376':('variant_trial_no_outcome','Usual Sensodyne whitening liked, this variant untried; positive rating cannot establish this variant effectiveness.'),
 'LZD-1182893951949424':('trial_sensory_expectations','Colgate trial buyer describes aroma and hopes for effect on coffee/tea stains; future hope is not result.'),
 'LZD-1260743078806602':('pack_mismatch_delivery','Ordered190g but reports receiving75gx2; fulfillment complaint rather than proof of wrong product performance.'),
 'LZD-1435074389156085':('large_pack_value','Basic buyer values two225g tubes at low price; package quantity enters perceived value.'),
 'LZD-1442732884978536':('stockpiling_before_use','Siwak reviewer stores product as reserve and has not tried it; purchase does not establish current consumption.'),
 'LZD-2004082758848866':('repeat_and_sensory_value','Complete8 buyer reports repeated use, low price and comfort in mouth.'),
 'LZD-2053090214326021':('brand_repeat_with_promotions','Pepsodent long-use claim and promo/free shipping value coexist; no exact tier history.'),
 'LZD-2059372864326021':('repeat_positive_counterexample','Complete8 buyer says repeated purchase; post-case date prevents explaining earlier decline.'),
 'REDDIT-1414a8a-L123':('parent_chooser_different_brand','Own purchases Closeup, parents choose regular/herbal Pepsodent; verify text and line bounds.'),
 'REDDIT-1414a8a-L189':('household_purchase_authority','Reports mother controls household bulk shopping and discourages separate purchases.'),
 'REDDIT-1414a8a-L411':('replenishment_family_fallback','Forgets to buy preferred sensitive product, uses mother-prepared supply on runout.'),
 'REDDIT-1414a8a-L205':('sensory_preferences_heterogeneous','Prefers subtle Enzim sensation, a rival to stronger-mint-is-always-better.'),
 'REDDIT-1414a8a-L436':('sensory_and_channel_friction','Strong mint sought even without sensitivity; disliked odor and specialist-channel effort matter.'),
 'REDDIT-1414a8a-L474':('local_variant_absence_report','Reports Closeup variant no longer found in nearby minimarkets; cannot infer all-channel absence.'),
 'REDDIT-1414a8a-L702':('price_duration_counterexample','Antiplaque initially felt expensive but perceived long duration justified ticket price.'),
}
allrows=[];counts={};curated=[]
for corpus in ['lazada_reviews','reddit_comments','oresa_incentivized_reviews','tryandreview_reviews']:
 rows=json.loads((B/'clean'/(corpus+'.json')).read_text());counter=collections.Counter()
 for r in rows:
  t=(r.get('review_text') or '').lower();tags=[k for k,v in patterns.items() if re.search(v,t)];counter.update(tags)
  allrows.append({'record_id':r['record_id'],'corpus':corpus,'exploratory_lexical_tags':tags,'tags_validated':False})
  if r['record_id'] in selected:
   theme,note=selected[r['record_id']];curated.append({**r,'analyst_mechanism':theme,'analyst_interpretation_and_boundary':note,'manual_read':True})
 counts[corpus]={'records':len(rows),'lexical_counts_not_prevalence':dict(counter),'incentive_counts':dict(collections.Counter(r.get('incentive_status','not_established') for r in rows))}
(B/'derived').mkdir(exist_ok=True)
(B/'derived'/'lexical_flags.json').write_text(json.dumps(allrows,ensure_ascii=False,indent=2))
(B/'derived'/'corpus_counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2))
(B/'derived'/'manually_read_evidence.json').write_text(json.dumps(curated,ensure_ascii=False,indent=2))
print('curated',len(curated),'requested',len(selected),'missing',set(selected)-{r['record_id'] for r in curated})
print(json.dumps(counts,indent=2))

"""Analyst-selected records inspected as examples, not prevalence coding."""
from pathlib import Path
import json,csv
r=Path(__file__).resolve().parents[1];rows=json.loads((r/'reddit_records.json').read_text());lookup={x['record_id'].split(':')[-1]:x for x in rows}
examples=[
('jmyhulz','sensory_cleanliness_cue','Mint sensation is explicitly linked to feeling fresh/feeling brushed.','Personal sensory evaluation; no clinical efficacy inference.'),
('jmyol7g','purchaser_user_separation','Person reports someone else repeatedly buying Herbal.','Buyer identity, age and payment source unspecified.'),
('jmyklul','sensory_rival','Prefers subtle, non-burning Enzim sensation.','Contradicts a universal stronger-mint preference.'),
('jmyycgk','foam_preference','User favors less foaming.','Foam preference is not clinical cleaning effectiveness.'),
('jmymt1g','brand_return_value','Reports returning to Pepsodent after other brands; sensitivity competitor viewed expensive.','Exact Pepsodent tier and actual purchase price unspecified; not confirmed Premium-to-Basic.'),
('jmytna4','family_purchase','Mother repeatedly buys Ciptadent.','Author attributes a possible reason jokingly; do not code inferred affordability as verified motivation.'),
('jmyoa3g','promotion_choice','Product choice described as whichever is discounted on shopping trip.','Statement, not transaction-level elasticity.'),
('jmyrku5','promotion_minimarket','Minimarket shopping choice described as discount-led.','No paid price, exact SKU or sequence.'),
('jmz6rv4','exact_variant_availability','Reports difficulty finding old red/blue Closeup locally.','Concerns Closeup, not evidence of absent Pepsodent; geographic location unspecified.'),
('jmz7mka','household_chooser_conflict','Wife buys mixed brands; author dislikes salty taste wife prefers.','Specific household example, not representative and no age verification.'),
('jmz9hrk','need_price_interaction','Sensitivity need combined with discount-dependent competitor or PepsodentSensitive choice.','Brand spelling preserved; no Premium-to-Basic purchase history.'),
('jmza2ip','household_fit_rival','One partner has restricted Enzim preference while purchaser otherwise changes with deals/new variants.','Specialist need could restrict choice; payer status unspecified.'),
('jmzc51f','promotion_default','Uses promotion as first rule, otherwise PepsodentHerbal fallback.','Herbal case tier classification needs explicit treatment; not automatically Basic.'),
('jmzcsd8','pack_usability','Cap-opening convenience explicitly affects choice.','Different from pack-size affordability; investigate actual tradeoff.'),
('jn2tqtk','family_pack_usability','Reply links mother’s Ciptadent loyalty to convenient cap.','Context-dependent endorsement; not brand-level incidence.'),
('jmzi5sd','specialist_success','Describes relief and continuing Sensodyne preference after research/social dentist content.','Consumer efficacy claim; potential rival to stop-after-relief story, no retention transaction panel.'),
('jmznzo2','cheap_promo','Explicit lowest-price/promotion preference.','Stated rule, not national demand or inability to pay.'),
('jn2d5tk','shared_specialist_rival','Household uses Systema because mother finds it comfortable for sensitive teeth.','Shared use may support specialization, rather than always penalize it.'),
('itfn8si','perceived_equivalence','Comment expresses perceived equivalence among toothpastes and costly professional whitening alternative.','A consumer belief, not clinical truth.'),
('nzq60pw','expectation_experience','Reports eight months of whitening-brand use without perceived effect.','Self-report and smoking context; no causal or laboratory result.'),
('l5dvmds','cross_category_promo','Hygiene routine includes Pepsodent or Darlie if on promotion.','Could reflect general deal shopping, not specific Premium rejection.'),
('l5flj8z','household_shared_products','Routine references sharing other products with mother and discount rule for toothpaste.','Do not infer toothpaste payer solely from sharing shampoo/deodorant.'),
('l5gjjk8','age_selfreport_promotion','Self-identifies26M and chooses on-sale fluoride toothpaste, usually Pepsodent.','Self-reported age, unverified; no prior Premium-to-Basic sequence.'),
('l5q18t2','age_selfreport_family_habit','Self-identifies30M and says household has used greenCloseup since childhood.','Self-reported age, unverified; brand-specific household habit not causal proof.')]
out=[]
for id,theme,interpretation,limit in examples:
 if id not in lookup:continue
 x=lookup[id];out.append(dict(example_id='RE'+str(len(out)+1).zfill(2),record_id=x['record_id'],theme=theme,interpretation=interpretation,limitation=limit,source_url=x['source_url'],created_at=x['created_at'],context_type=x['context_type'],scope=x['scope'],selection='analyst purposive example;not prevalence',raw_file=x['raw_file'],raw_record_index=x['raw_record_index']))
(r/'manual_evidence_examples.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
with (r/'manual_evidence_examples.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
print('Examples',len(out))

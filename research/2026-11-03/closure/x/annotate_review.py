#!/usr/bin/env python3
"""Apply assistant close-reading notes to fixed sample. No model/API dependency.

These are qualitative judgments, not automatically inferred labels or human validation.
"""
from pathlib import Path
import json,csv,gzip,collections
P=Path(__file__).resolve().parent
# Index is the fixed order in review_selection.json, not a raw-export row index.
NOTES=[
('incidental_oralcare','Brushing mishap: face wash instead of toothpaste. No purchase or variant evidence.'),
('media_or_clickbait','Personality-test headline about squeezing toothpaste. Exclude from experienced product-benefit analysis.'),
('humour_or_context_missing','Reply contrasts jokingly spelled household brands. Does not identify own toothpaste purchase.'),
('brand_event_or_fandom','Photo/event and college conversation, not toothpaste use. Student-looking language is not age verification.'),
('commercial_claim','Theramed sale/import copy and free shipping. Whitening/clinical claims are advertising, not measured outcomes.'),
('food_metaphor','Chocolate mint compared with toothpaste. Exclude from actual toothpaste taste experience.'),
('shopping_links','Systema brush/paste shopping links. No independent use or repeat statement.'),
('advice_or_hearsay','General claim that non-detergent brands cost more and need no rinsing. Do not treat as clinical guidance or paid-price observation.'),
('replenishment_context','Defends squeezing out remaining paste before refill as waste avoidance, not necessarily poverty. The portrayed person is not independently verified.'),
('accessory_listing','Tube clip/hanger product listing, not toothpaste formulation or purchase.'),
('recommendation_request','Asks an account for Enzim information. No purchase or experience established.'),
('accessory_listing','UV dispenser listing. Source language label sl illustrates metadata errors: the text is Indonesian-looking.'),
('non_Indonesia_commercial','Portuguese Colgate multipack subscription advertisement; separate international/commercial context.'),
('mixed_experience_promotion','Claims a month of use and improved colour plus intent to promote; shopping link present. Unnamed product and incentive unknown.'),
('nonoral_context','Gardening-hoax discussion mentions toothpaste as an ingredient. Exclude from oralcare experience.'),
('brand_event_or_fandom','Brand-ambassador joke/promotion. No first-person product use or purchase.'),
('nonoral_use','Reports toothpaste application around toenails. Exclude from oralcare benefit evidence; no medical endorsement.'),
('accessory_listing','Rack/soap/dispenser listing, not toothpaste.'),
('retailer_advertisement','Alfamidi Pepsodent price offer and dated promotion. Could support an advertised offer, not actual paid price, stock, or repeat.'),
('mixed_experience_promotion','Claims Malaysian product freshness, text ends mid-thought with link. Product and incentives not established.'),
('incidental_oralcare','Tube-cap habit. No replenishment or specialist-value mechanism.'),
('humour_or_context_missing','Sport/media compared with toothpaste advertisement. No consumption evidence.'),
('humour_or_context_missing','Balm/toothpaste mint comparison framed as absurd question. Not a product-use recommendation.'),
('humour_or_context_missing','Sexual joke involving Pepsodent. Exclude from purchase/use evidence.'),
('retailer_advertisement','TokopediaNOW replenishment-convenience marketing, not a consumer report of delivery performance.'),
('reported_switch','Reports household switching Pepsodent to Ciptadent alongside tea switching. Reason and exact Pepsodent tier unknown.'),
('reported_experience','Reports buying Click, enjoying it, and husband liking it. Supports co-user experience, not who paid or durable repeat.'),
('non_Indonesia_commercial','English dollar-denominated travel-paste/floss deal. Not Indonesian household willingness to pay.'),
('shopping_links','Multiple very-low-price shopping deals. No actual paid prices or use established.'),
('mixed_experience_promotion','Before/after whitening claim from changing paste, unnamed product. Promotional context and treatment confounders unresolved.'),
('accessory_listing','Dispenser price link. Exclude from toothpaste purchase analysis.'),
('humour_or_context_missing','Two-item reply lacks enough context to infer oral use or purchase.'),
('brand_event_or_fandom','Celebrity couple brand-ambassador speculation. No product experience.'),
('media_or_clickbait','Health headline promoting alternatives; unsupported clinical claims remain third-party media content.'),
('advice_or_hearsay','Recommends misspelled Sensodyne. No own experience or price recorded.'),
('food_metaphor','Peppermint tea compared with toothpaste. Not toothpaste experience.'),
('recommendation_request','Asks whether Click purchase includes celebrity photocards. Nonfunctional reward may matter; no actual purchase established.'),
('recommendation_request','Tea drinker asks for a suitable toothpaste. Need/selection question; not a switch or experienced benefit.'),
('retailer_advertisement','Pepsodent Herbal buy-one-get-one and price link. Historical advertised offer, not purchased price or case-defined premium tier.'),
('gift_fandom_context','Euthymol described as a gift from father and linked to a celebrity. Illustrates discovery through gifting/fandom; not sustained use.'),
('humour_or_context_missing','Discusses someone else not using soap/paste. No own purchase sequence.'),
('nonoral_use','Burn injury account mentions parents recommending toothpaste. Exclude from dental benefit analysis.'),
('repeated_advertising_style_wording','Repeated advertising-style Sensodyne ice-eating wording, consistent with a familiar commercial narrative; exact official source not independently verified. First-person grammar is not sufficient evidence of independent experience.'),
('childhood_household_context','Retrospective maternal fluoride/brushing oversight and dentist visits. Plausible family influence; not current target-payer prevalence.'),
('repeated_advertising_style_wording','Repeated Sensodyne ice-eating advertising-style wording with misspellings. Cannot establish independent product-effect experience.'),
('repeated_advertising_style_wording','Repeated Sensodyne advertising-style wording in first-person form. Do not count as verified individual benefit evidence.'),
('repeated_advertising_style_wording','Repeated Sensodyne advertising-style wording. Parent thread unknown; no independent use established.'),
('reported_switch','Family says other firms were cheaper and now switched from remaining Unilever product. Exact replacement and current motivation unclear.'),
('repeated_advertising_style_wording','More repeated Sensodyne advertising-style wording; not a verified unique personal outcome despite distinct post ID.'),
('fan_promotional_content','Click/NCT campaign-style call to switch and family slogan. Not confirmed paid promotion or actual retention.'),
('nonoral_use','Child weaning anecdote involving toothpaste, not oralcare purchase/use.'),
('intended_switch','Plans to finish existing Pepsodent then change; purchase sequence not completed. Exact motive in absent parent context unknown.'),
('intended_switch','Reports alternating Pepsodent/Ciptadent and intention to settle on Ciptadent after new information. Motivation and actual follow-through unverified.'),
('repeated_advertising_style_wording','Repeated ice-eating advertising-style narrative changes brand to Pepsodent. Treat as possible meme/copy rather than verified therapeutic success.'),
('adjacent_brush_promotion','Small-head toothbrush recommendation with sales links; not toothpaste variant switching.'),
('reported_switch','Reports switching to Enzim after detergent concerns. Belief motivates choice; does not verify ingredient harm or target-group prevalence.'),
('reported_switch','Reports nausea/vomiting while brushing ended after changing paste. Supports experiential mismatch hypothesis; product unidentified and causation unverified.'),
('mixed_experience_promotion','Purple/pink product comparison, perceived whitening, shopping-cart link. Identity/context and incentive uncertainty remain.'),
('mixed_experience_promotion','Reports Enzim use, less sensitivity and advice about dryness/rinsing; link present. Separate personal claim from clinical advice and commercial uncertainty.'),
('recommendation_request','Seeking toothpaste that does not cause nausea; intention to change, no completed switch.'),
('child_product_context','Parent discusses 1000-ppm paste for children, availability and imported-brand cost. Not an adult-user product comparison.'),
('incidental_oralcare','Carries brush/paste to brush after smoking while hiding smoking from spouse. Not product-choice evidence.'),
('mixed_experience_promotion','Whitening testimonial/disclaimer plus shopping-cart link; no independent outcome validation.'),
('mixed_experience_promotion','Claims long Dentiste use and superior effect to Marvis, with shopping links and oil pulling. Benefit confounding and incentives unclear.'),
('adjacent_brush_promotion','Doctor-recommended toothbrush shortlist with links. Exclude from toothpaste repeat analysis.'),
('reported_adverse_experience','Reports Pepsodent-associated sensitivity after brushing and possible loss of fit. SKU/tier and other causes unknown; not clinical diagnosis.'),
('humour_or_context_missing','Someone looks suitable for toothpaste advertisement. No actual product experience.'),
('fiction','Explicit fanfiction conversation involving toothpaste-model metaphor. Exclude from consumer evidence.'),
('reported_routine','Reports detergent-free paste, flossing, tongue cleaning and scaling. Multiple simultaneous practices prevent isolated benefit attribution.'),
('reported_retention_counterexample','Months without visible change yet continued use because comfortable/no mouth ulcers. Counters assumption that whitening disappointment always causes exit.'),
('food_metaphor','Chocolate-mint ice cream compared with toothpaste. Not oral-product taste feedback.'),
('food_metaphor','Chocolate-mint food disliked for toothpaste-like taste. Do not transfer to actual toothpaste preference.'),
('reported_experience','Reports trying to limit foam contact after advice, with some improvement. Missing parent context and symptom unspecified; no formulation-causality claim.'),
('nonoral_use','Helmet-cleaning instructions using toothpaste. Exclude from oralcare demand/benefit evidence.'),
('food_metaphor','Gelato/mint-food preference; not toothpaste sensory evaluation.'),
('alternative_oralcare_claim','Leaf chewing/brushing account with claimed plaque sensation. Alternative-care context, unverified clinical/safety claims.'),
('mixed_experience_promotion','Claims three large Darlie tubes used and compares mint/foam/sensitivity to 2080, with shopping link. Repeated-use claim useful; commercial independence unknown.'),
('mixed_experience_promotion','Repeated recommendation/whitening/freshness testimonial plus link. Product unidentified and no verified repeat purchase.'),
('alternative_oralcare_claim','Reports replacing paste with sirih pinang and 24-hour freshness. Not clinical evidence; do not recommend the practice from a post.'),
('promotional_claim','Darlie scientific-sounding feature copy in testimonial format. Brand benefit positioning rather than independent clinical outcome.'),
('humour_or_context_missing','Desired partner should close paste tube; incidental domestic habit, not toothpaste purchasing.'),
('humour_or_context_missing','Horror-story joke ends with convenience-store prices. Not reliable actual price/stock observation.'),
('reported_replacement_sequence','Reports whitening, replacement after running out, colour returning, then return to prior paste; also likes taste. Product unspecified; no premium/basic/age verification.'),
('fan_promotional_content','Whitening endorsement with celebrity sticker and branded review hashtags. Potential reward/fandom context; no proof of paid placement.'),
('nonoral_context','Demonstration anecdote about toothpaste on face; no toothpaste-purchase mechanism.'),
('food_metaphor','Family reacts to unusual food flavour compared with Closeup. Household words do not establish toothpaste chooser/payer roles.'),
('mixed_experience_promotion','Claims one tube improved coffee staining and moving to second, with link. Repeated use and price praise, but not independently validated.'),
('mixed_experience_promotion','Links plus detailed household whitening/baking-soda taste and foam comparison after two tubes. Mixed commercial/experience context; exact SKU not established here.'),
('food_metaphor','Tea/mocktail aftertaste compared with mint paste. Not actual toothpaste experience.'),
('reported_routine','Reports Colgate Optic White plus whitening strips, floss and mouthwash. Confounded routine; no isolated paste efficacy inference.'),
('reported_experience','Marvis recommendation from relative, claimed whitening and high price. No durable repeat or affordability threshold established.'),
('reported_purchase_context','Buys household toiletries as monthly stock and describes discounts. Paste-specific price/quantity and actual payer role beyond self-purchase unclear.'),
('reported_choice_context','Systema fits, sometimes pricier Colgate. Suggests repertoire/occasion-based choice rather than one-way ladder; actual transaction missing.'),
('mixed_experience_promotion','Claims two tubes, high price justified by perceived whitening; says no affiliate. Declaration alone does not verify independence.'),
('mixed_experience_promotion','Very similar no-affiliate/two-tube whitening text to another selected post. Possible repeated copy; not separate independent evidence of efficacy.'),
('reported_stockup','Claims buying four or five tubes when deeply discounted. Stock-up may change purchase timing; does not measure normal-price retention.'),
('childhood_payer_memory','Retrospective request for Closeup rejected by mother in favour of cheaper Ritadent. Direct payer-choice tension, but childhood memory not current target prevalence.'),
('price_context_incomplete','List includes Sensodyne beside inflation observations but gives no toothpaste price change. Do not assign listed rice inflation to toothpaste.'),
('reported_trial_value_context','Owns two small expensive tubes, postpones recommendation until trying them. Pack-size/value concern before outcome; ml cannot silently become grams.'),
('reported_uptrade_counterexample','After starting work reports switching from censored Pepsodent to pricier paste and fewer ulcers. Independence may enable uptrading; SKU/tier and causality unknown.')
]
SUPPLEMENT={
 '1979392212954943852':('shared_household_control','Reports shared Unilever paste persists because parents are loyal and hard to persuade. Supports household constraint, but exact brand/tier and youth age unknown.'),
 '1837850186682716603':('household_payer_counterexample','Reports contributing to parents and buying household bathroom/kitchen essentials including paste. Adult child can be the payer; no brand or target age verification.'),
 '2068274183105286615':('gift_price_knowledge_gap','Euthymol received from aunt; consumer does not know paid price, later sees high online asking price. Acquisition and willingness to pay differ; shopping link may be promotional.'),
 '1637420629669601280':('availability_convenience_counterexample','Contrasts childhood monthly supermarket stock-up with present walkable minimarkets. Availability can reduce stocking need; no specific premium SKU availability established.'),
 '1734190351676756381':('non_Indonesia_comparator','Malay wording reports switching Sensodyne/Oral-B to Systema due price and rural-supermarket difficulty. Country unverified; cannot treat as Indonesian stock evidence.'),
 '1547407056268709889':('sensory_positioning_counterexample','Reports dryness/rough mouth after brushing and questions Korean positioning beyond celebrity/pack text. Suspects SLS but does not establish cause.'),
 '1787355139172671734':('sampling_household_substitution','Gives free full-size Closeup to mother who will use available tube before buying. Supports stock substitution, not evidence of paid repeat after sampling.'),
 '1705010201483731333':('shared_consumption_context','Reports roommate using own toiletries and faster depletion. Shared consumption affects replacement timing; no product, pack, or paid-price detail.'),
 '2068234900491129031':('category_downtrade_not_case_tier_switch','Full post now available in new export; same ID as earlier truncated known-post sample. Reports imported Pasta Del Capitano to unspecified Pepsodent amid household budget changes. Do not label Pepsodent Premium-to-Basic, verify age, or treat this as an additional independent story.')
}
def main():
 sample=json.loads((P/'review_sample.json').read_text());assert len(sample)==len(NOTES)==100
 rows=[]
 for r,(code,note) in zip(sample,NOTES):
  rows.append({'record_key':r['record_key'],'source_record_id':r['source_record_id'],'source_url':r['source_url'],'sampling_stratum':r['sampling_stratum'],'qualitative_code':code,'interpretation_and_limits':note,'text_original':r['text_original'],'source_file':r['latest_source_file'],'json_index_zero_based':r['latest_json_index_zero_based'],'age_verified':False,'confirmed_pepsodent_premium_to_basic_switch':False,'reviewer_type':'assistant_close_reading_not_independent_human_validation'})
 corpus={r['source_record_id']:r for r in map(json.loads,gzip.open(P/'records.jsonl.gz','rt'))}
 for ident,(code,note) in SUPPLEMENT.items():
  r=corpus[ident];rows.append({'record_key':r['record_key'],'source_record_id':ident,'source_url':r['source_url'],'sampling_stratum':'supplementary_purposive_counterexample_search_not_random','qualitative_code':code,'interpretation_and_limits':note,'text_original':r['text_original'],'source_file':r['latest_source_file'],'json_index_zero_based':r['latest_json_index_zero_based'],'age_verified':False,'confirmed_pepsodent_premium_to_basic_switch':False,'reviewer_type':'assistant_close_reading_not_independent_human_validation'})
 (P/'evidence.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
 with (P/'evidence.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 counts={'close_read_records':len(rows),'random_sample_records':40,'theme_screened_random_within_purposive_records':60,'supplementary_purposive_records':len(SUPPLEMENT),'qualitative_codes':dict(collections.Counter(r['qualitative_code'] for r in rows)),'random40_qualitative_codes':dict(collections.Counter(r['qualitative_code'] for r in rows[:40])),'age_verified_count':0,'target_switcher_verified_count':0}
 (P/'review_stats.json').write_text(json.dumps(counts,indent=2)+'\n');print(json.dumps(counts,indent=2))
if __name__=='__main__':main()

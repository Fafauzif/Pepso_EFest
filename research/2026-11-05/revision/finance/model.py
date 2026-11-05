"""Three-year quarterly operating scenario. All commercial inputs are team estimates.
Does not import scenario effects from survey or foreign benchmarks.
"""
from pathlib import Path
import json, math, csv
ROOT=Path(__file__).parent
SCREEN=[5000,10000,15000,20000,25000,30000,30000,30000,30000,30000,30000,30000]
# 10 to 60 proposed touchpoint-equivalents, each 500 new, deduplicated screens/quarter.
BASE=dict(reach_factor=1.0,qualified=.4,first_t=.35,first_c=.25,retain_t=.70,retain_c=.60,packs_per_active_quarter=1.0,net_portfolio_contribution=6000,screen_cost=200,history_gate_cost_per_qualified=40,event_service_cost=350,event_message_cost=300,fixed_quarter=6000000,launch_cost=20000000,annual_real_hurdle=.12,working_capital_per_incremental_pack=2500)
CASES={
 'downside':dict(BASE,reach_factor=.75,first_t=.30,retain_t=.65,net_portfolio_contribution=4500,screen_cost=400,event_service_cost=450,event_message_cost=400),
 'base':BASE,
 'upside':dict(BASE,reach_factor=1.25,first_t=.40,retain_t=.75,net_portfolio_contribution=7500,screen_cost=180)
}
def run(p):
 t=c=0.; cumulative=-p['launch_cost']; cum_operating=-p['launch_cost']; last_wc=0.; npv=-p['launch_cost']; rows=[]; peak=p['launch_cost']; payback=None
 for i,n in enumerate(SCREEN):
  screened=n*p['reach_factor']; qualified=screened*p['qualified']; new_t=qualified*p['first_t'];new_c=qualified*p['first_c']; t=new_t+t*p['retain_t'];c=new_c+c*p['retain_c'];packs_t=t*p['packs_per_active_quarter'];packs_c=c*p['packs_per_active_quarter']; delta=packs_t-packs_c
  gross=delta*p['net_portfolio_contribution']; acquisition=screened*p['screen_cost']; service=packs_t*p['event_service_cost'];messaging=packs_t*p['event_message_cost']; fixed=p['fixed_quarter'];history=qualified*p['history_gate_cost_per_qualified'];cost=acquisition+service+messaging+fixed+history;operating=gross-cost
  wc=delta*p['working_capital_per_incremental_pack']; delta_wc=wc-last_wc;last_wc=wc;cash=operating-delta_wc;cumulative+=cash;cum_operating+=operating;npv+=cash/(1+p['annual_real_hurdle'])**((i+1)/4);peak=max(peak,-cumulative)
  if payback is None and cumulative>=0:payback=i+1
  rows.append(dict(period=f'T{1+i//4}Q{1+i%4}',quarter=i+1,screened=screened,qualified=qualified,new_first_paid_treatment=new_t,new_first_paid_comparator=new_c,paid_packs_treatment=packs_t,paid_packs_comparator=packs_c,incremental_paid_100g=delta,incremental_portfolio_contribution=gross,acquisition_and_channel_cost=acquisition,history_gate_cost=history,service_verification_cost=service,message_cost=messaging,fixed_operating_cost=fixed,program_cost=cost,operating_surplus=operating,working_capital_balance=wc,change_working_capital=delta_wc,program_cash_flow=cash,cumulative_program_cash=cumulative,cumulative_operating_after_launch=cum_operating))
 total=lambda k:sum(r[k] for r in rows)
 annual=[]
 for y in range(3):
  group=rows[y*4:(y+1)*4]
  annual.append(dict(year=y+1,**{k:sum(r[k] for r in group) for k in ['screened','qualified','paid_packs_treatment','paid_packs_comparator','incremental_paid_100g','incremental_portfolio_contribution','acquisition_and_channel_cost','history_gate_cost','service_verification_cost','message_cost','fixed_operating_cost','program_cost','operating_surplus','change_working_capital','program_cash_flow']},cumulative_program_cash=group[-1]['cumulative_program_cash']))
 return dict(assumptions=p,quarterly=rows,annual=annual,summary=dict(screened=total('screened'),qualified=total('qualified'),paid_packs_treatment=total('paid_packs_treatment'),paid_packs_comparator=total('paid_packs_comparator'),incremental_paid_100g=total('incremental_paid_100g'),contribution_before_program=total('incremental_portfolio_contribution'),operating_program_cost=total('program_cost'),launch_cost=p['launch_cost'],total_program_cost=p['launch_cost']+total('program_cost'),operating_surplus_after_launch=cum_operating,ending_working_capital=last_wc,cumulative_cash_after_launch=cumulative,npv=npv,payback_quarter=payback,peak_funding_need=peak,operating_roi=cum_operating/(total('program_cost')+p['launch_cost'])))
def threshold(key,low,high):
 # zero-NPV threshold, assumes monotone on provided interval.
 for _ in range(80):
  mid=(low+high)/2;a=run(dict(BASE,**{key:low}))['summary']['npv']; b=run(dict(BASE,**{key:mid}))['summary']['npv']
  if a*b<=0:high=mid
  else:low=mid
 return (low+high)/2
out={'status':'Estimasi tim; skenario investasi operasional sebelum pajak, bukan ramalan atau hasil uji','currency':'IDR konstan 2026','horizon':'12 kuartal sejak mulai program; T0 belanja awal','cases':{k:run(v) for k,v in CASES.items()},'thresholds_zero_npv':{
 'max_screen_cost_idr':threshold('screen_cost',0,2000),
 'min_contribution_per_incremental_100g_idr':threshold('net_portfolio_contribution',0,12000),
 'min_first_paid_treatment':threshold('first_t',.25,.5),
 'min_quarterly_continuation_treatment':threshold('retain_t',.6,.8),
 'min_reach_factor':threshold('reach_factor',.1,2),
},'sensitivity':[]}
for key,values in [('screen_cost',[200,300,400,600,1000]),('first_t',[.30,.325,.35,.375,.40]),('retain_t',[.60,.65,.70,.75]),('net_portfolio_contribution',[4500,5000,6000,7500]),('packs_per_active_quarter',[.75,1,1.25])]:
 for v in values:out['sensitivity'].append(dict(driver=key,value=v,**run(dict(BASE,**{key:v}))['summary']))
(ROOT/'finance.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
with (ROOT/'quarterly_base.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=out['cases']['base']['quarterly'][0].keys());writer.writeheader();writer.writerows(out['cases']['base']['quarterly'])
print(json.dumps({k:v['summary'] for k,v in out['cases'].items()},indent=2));print(out['thresholds_zero_npv'])
# exact independent aggregate check: incrementals equal per-cohort sums.
for case in out['cases'].values():
 p=case['assumptions'];ind=0
 for j,s in enumerate(SCREEN):
  for lag in range(12-j):ind+=s*p['reach_factor']*p['qualified']*(p['first_t']*p['retain_t']**lag-p['first_c']*p['retain_c']**lag)*p['packs_per_active_quarter']
 assert math.isclose(ind,case['summary']['incremental_paid_100g'],rel_tol=1e-12)
 assert math.isclose(case['summary']['operating_surplus_after_launch']-case['summary']['ending_working_capital'],case['summary']['cumulative_cash_after_launch'],abs_tol=1e-6)

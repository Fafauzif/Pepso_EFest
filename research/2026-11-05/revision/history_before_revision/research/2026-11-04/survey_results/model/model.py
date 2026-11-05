import json
from pathlib import Path
N=10000
cases={
 'downside':dict(qualified=.20,first_t=.30,first_c=.25,repeat_t=.45,repeat_c=.45,net_contribution_per_100g=3500),
 'base':dict(qualified=.40,first_t=.40,first_c=.25,repeat_t=.60,repeat_c=.45,net_contribution_per_100g=6000),
 'upside':dict(qualified=.60,first_t=.45,first_c=.25,repeat_t=.65,repeat_c=.45,net_contribution_per_100g=9000),
}
out={'unit':'IDR unless explicitly people or 100g paid-equivalent packs','model_status':'Authored sensitivity scenarios, not survey estimates or forecasts','screened_per_equivalent_arm':N,'observation_window_days':180,'cost_assumption':{'learning_fixed':30000000,'variable_total_per_equivalent_arm':10000000,'total':40000000},'scenarios':{}}
for name,s in cases.items():
 q=N*s['qualified'];a=q*s['first_t'];b=q*s['first_c'];r=a*s['repeat_t'];rc=b*s['repeat_c'];d=a+r-b-rc;cost=40000000
 out['scenarios'][name]={**s,'qualified_people':q,'first_paid_treatment':a,'first_paid_comparator':b,'second_paid_treatment':r,'second_paid_comparator':rc,'incremental_first_paid':a-b,'incremental_second_paid':r-rc,'incremental_paid_100g_equivalents':d,'incremental_contribution_before_program':d*s['net_contribution_per_100g'],'program_cost':cost,'net_after_program':d*s['net_contribution_per_100g']-cost,'break_even_total_program_cost':d*s['net_contribution_per_100g'],'break_even_variable_cost_per_screened_excluding_learning_fixed':d*s['net_contribution_per_100g']/N,'break_even_equivalent_packs':cost/s['net_contribution_per_100g']}
Path(__file__).with_name('scenarios.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

# Finance model for the revised Pepsodent proposal

## Audience-ready interpretation

Pada estimasi tim selama 12 kuartal, layanan menghasilkan tambahan 41.527 ekuivalen berbayar 100 g, kontribusi portofolio Rp249,16 juta, dan surplus operasional Rp29,53 juta setelah seluruh biaya program Rp219,63 juta. Setelah penyediaan modal kerja Rp15,05 juta yang masih terikat pada akhir periode, kas kumulatif bersih mencapai Rp14,48 juta. NPV sebelum pajak pada tingkat imbal hasil riil 12% sebesar Rp1,24 juta; pengembalian kas terjadi pada T3Q3. Kebutuhan pendanaan tertinggi adalah Rp46,40 juta. Hasil ini layak dipertimbangkan secara bersyarat: biaya per skrining tidak boleh melampaui sekitar Rp205 dan kontribusi tambahan per 100 g perlu setidaknya Rp5.962 pada asumsi lain yang tetap. Skenario bawah tetap merugi. Seluruh hasil adalah skenario estimasi tim, bukan keluaran survei atau hasil program yang telah berjalan.

Do not describe the base as robust, guaranteed, already profitable or a market forecast. It has limited headroom and depends on conversion/retention and owned-channel economics. A voluntary low-touch offer with paid trial replaces universal sampling. If the business needs paid broad-reach ads, a new application or universal free packs, recost and rerun it.

## Stable files

- `model.py`: executable standard-library Python scenario calculator.
- `finance.json`: canonical full assumptions, 12-quarter detail, annual summaries, three scenarios, sensitivities and zero-NPV thresholds.
- `quarterly_base.csv`: twelve base-quarter records, IDR unrounded.
- `finance_sources.json`: first-party source register. External facts and team estimates are separate.

## Units and core formulas

One unit is an independent purchasing unit (person or shared-tube household); prospective eligibility is ages18-30, previous identifiable Premium and now Basic, relevant stated additional need. Household sharing requires deduplication. Screens are new deduplicated units, not impressions. The survey supplies no estimate of qualification or switching rates.

For quarter t:

- `Q_t = screened_t × qualification_rate`
- `T_t = Q_t × first_paid_treatment + retention_treatment × T_(t-1)`
- `C_t = Q_t × first_paid_comparator + retention_comparator × C_(t-1)`
- `D_t = (T_t - C_t) × packs_per_active_quarter`
- `contribution_t = D_t × net_portfolio_contribution_per100g`
- `program_cost_t = screened_t × acquisition_cost + treatment_paid_packs_t × (service_cost + message_cost) + qualified_t × history_gate_cost + fixed_cost`
- `operating_surplus_t = contribution_t - program_cost_t`
- `working_capital_t = D_t × allowance_per_incremental_pack`
- `cash_t = operating_surplus_t - (working_capital_t - working_capital_(t-1))`
- `cumulative_cash_t = -launch + sum(cash_1..t)`
- `NPV = -launch + sum(cash_t/(1+0.12)^(t/4))`

Each cohort only remains active through the continuation probability; no assumed later reactivation, terminal customer value, third-party health saving or released end-period working capital is credited. One paid100g equivalent per active quarter is an authored commercial frequency, not a claim that every tube empties after90days. Model by actual grams at implementation.

Comparator is an equivalent business-as-usual trajectory for attribution. It is not an additional285k people who must be recruited. The launch research envelope below prices a bounded learning comparator cohort; the all-cohort comparator remains a modeled counterfactual until evidence is gathered. Routine cohort outcome capture is included in per-event costs. A full independently powered national trial is not implied.

Currency is constant2026IDR. Twelve quarters start only after approvals; T1Q1 is relative, not a promise of a calendar date. Real hurdle12% is a team investment criterion, not Unilever WACC. No financing, tax, depreciation, capex accounting, customer lifetime value or share-restoration forecast is claimed. Launch cost is expensed conservatively atT0; no residual asset value is credited. Program cash is an incremental contribution cash proxy after an explicit working-capital provision, not audited free cash flow of Unilever.

## Assumption register and operational basis

ALL commercial numbers below are `Estimasi tim`. No foreign study effect is used as a Pepsodent conversion rate.

| Driver | Base | Basis and interpretation |
|---|---:|---|
| New screens by quarter | 5k,10k,15k,20k,25k,30k then30k/q | 10,20,30,40,50,60 proposed touchpoint-equivalents ×500new screens per quarter; total285k. Includes owned web/retail/campus reach. These are planned capacity, not signed partners, TAM or measuredtraffic. Deduplicate acrossyears. |
| Relevant eligible units |40%| Qualification for priorPremium/currentBasic and relevantneed is not observed in survey; sampling check must test this. |
| First paid return |35% vs25%| Team treatment/comparator planning inputs;10pp improvement is unproven. |
| Quarterly continuation |70% vs60%| Team assumptions; continuing cohorts, not a further10pp independent additive salesclaim. |
| Frequency |1 ×100g/activequarter| Record grams; no automatic90dayreminders. |
| Net portfolio contribution |Rp6,000/incremental100g| Explicit hypothetical manufacturer bridge below; never shelfprice×casemargin. |
| Screen/channel cost |Rp200/newscreen| Rp100for QR/retail material allocation +Rp100for ownedmedia/placement opportunitycost. Assumes no masspaidCAC; this lowcostaccess is decisive and must be observed. |
| History/SKU eligibility gate |Rp40/qualifiedunit| Automatic exact-SKU history self-report with available evidence;2%manualhistoryaudit×2minutes +1%exceptions×1minute =0.05minute/qualifiedunit. AtRp40.5k/hour, labouraboutRp33.7 plusRp6.3storage. Planningworkloadassumption, not100%independentverification. |
| Service/verification |Rp350/treatmentpaidevent| Intended automated capture plus exception handling and independent receiptsampleaudit; never pretend every receipt manuallychecked forfree. Capacity note below. |
| Messaging |Rp300/treatmentpaidevent| 20%opt-in ×2billableoutboundmessages ×Rp750all-inplanningallowance; everymessagebudgeted, no relianceonfreequotas. Real category/BSPtariff andreplyusage requirequote; averagecostsensitive. |
| Fixed operations |Rp6m/quarter| Rp4.2mcoordination (0.2FTE ×Rp7mloadedmonthly ×3),Rp0.6mcontent/professionalQA,Rp0.6mhosting/security,Rp0.6mcohortanalysis. Shared brandassets are assignedcost, notfree. |
| Launch |Rp20m atT0| Rp5mexistingCMSconfiguration;Rp3mcatalogue/consent/dataSOP;Rp3mprofessionalreview/education;Rp3mQR/retailtraining;Rp6mbaseline/holdout/QA. No standalonenativeapp. |
| Working capital |Rp2,500/incrementalpack| Approx18.3%of incrementalmanufacturerrealization (Rp13,684/100g), netreceivable/inventory/payable allowance, notcompany DSO. UnrecoveredRp15.05m remains atQ12. |
| Real hurdle |12%/year| Team investment requirement; not claimed corporate WACC. |

### Hypothetical manufacturer contribution bridge

All values are team estimates. For Premium100g, manufacturer net realization Rp20,000 less production cost Rp10,500 and normal variable trade/logistics Rp1,000 gives Rp8,500. For Basic190g, net realization Rp12,000 less production Rp6,750 and trade/logistics Rp500 gives Rp4,750, equal toRp2,500/100g. Equalgram displacement therefore leavesRp6,000additional portfolio contribution. The target is currently Basic, so100%owndisplacement is allowedfor; do not subtract Basicagain. Normal promo/tradefunding belongs in netrealization orvariabletradecost once. The consolidated46.9%grossmargin is only a broad reasonableness comparator for the assumed manufacturing grossmargins47.5%Premium and43.75%Basic; it does not establish SKUmargin, prices orunitcosts.

### Staff and research capacity

Rp7mloadedmonthly is a team estimate above Jakarta2026UMP Rp5.729876m; it is not a salary quote or assertion that a fractionalfulltimeposition can be hired at any location. At an assumed173workinghours/month it implies aroundRp40.5k/hour. The Rp350/event variable service reserve budgets exceptionwork:5%receipts×2minutes +10%supportcases×3minutes =0.4minute perpaid event, aroundRp270labour/event plusRp80storage/processing. At peak13,435paid treatment events/q the expected handlingwork isabout90hours/q; fixedcoordination adds~104hours/q. These are taskallocations within existing teams or pricedcontractwork. Validate supporttake-up, fraudload and realprocessing time.

The launch research envelope Rp6m includes a proposed1000control units (recruitment2500screens×Rp200=Rp0.5m; up to1000receiptrecords×Rp350=Rp0.35m;100researchhours×Rp40k=Rp4m; protocol/dataQA Rp1.15m). Treatment routinecapture is already costed in operatingunitcosts. This is a bounded volunteeredstudy proposal, not an approvedsample, a guaranteedresponse rate, or a fullclinicaltrial. Power, householdclusters, recruitability, historyeligibility and consent must determineactualcohort/cost. If paidparticipation incentives, morefieldwork or higherverification are needed, add them ratherthan absorb them silently. Do not copy the previous1000/arm sample-size derivation into this new model without reconciling the outcome/rates.

## Scenario assumptions

- Downside:75%plannedreach; firstpaid30%vs25%;continuation65%vs60%;contributionRp4,500;screenRp400;serviceRp450;messageRp400. TotalcostRp231.30m, surplus−Rp167.51m, cash−Rp172.48m, NPV−Rp146.05m; no payback.
- Base: asregistered; totalcostRp219.63m, surplusRp29.53m,cashRp14.48m,NPVRp1.24m,paybackT3Q3.
- Upside:125%reach;firstpaid40%vs25%;continuation75%vs60%;contributionRp7,500;screenRp180;serviceRp350;messageRp300. TotalcostRp266.65m,surplusRp379.18m,cashRp346.75m,NPVRp260.93m,paybackT2Q2. Wideupsideresultsareassumptionpropagation, notprobabilisticconfidence.

## Decision thresholds

Holding otherbaseinputsconstant, NPV crosseszero atscreen costRp205.39;unitcontributionRp5,961.99; firstpaidtreatment34.89% (comparator25%); continuation69.84% (comparator60%); reach98.47% ofplanned. These areonevariableat-a-time thresholds, notmutuallyindependent guarantees. A quarter-of-a-tube-equivalent frequency reduction can materiallydefeat the case. Paidmedia atRp1,000/screen is not coveredby thepositivebase.

This replaces—not conceals—the original180dayscenario. That model remains historicallynegative. The new modelchangespaidtrial, operatingcost, repeatedcohorts, capacity, attribution andobservationhorizonexplicitly. Stage funding; do not commit the entirethree-yearcost before firstcohort and unitarithmetic are established.


## Revision after eligibility-cost review

History screening is now explicitly costed atRp40 perqualifiedunit in everyquarter andscenario:2%manualaudit×2minutes+1%exceptions×1minute=0.05min/unit;Rp40.5k/hour impliesRp33.7labour plusRp6.3storage. Histories remain exact-SKUself-report with evidencewhereavailable; theauditsubsetdoesnotmakeallhistoriesindependentlyverified. This addsRp4.56m overthreebaseyears. It reducesbaseNPV toRp1.24m, a verynarrowmargin: maxscreen costRp205.39, mincontributionRp5,961.99, firstpaidmin34.89%, continuationmin69.84%, reachmin98.47%ofplan. Addedcostisnotremovedtoforceapositiveresult. The1000controlunitreserveis alearningcomparator, notanassertedpoweredconfirmatorytrial.

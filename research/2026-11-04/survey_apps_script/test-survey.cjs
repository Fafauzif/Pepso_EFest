/* Local contract/integration tests against explicitly implemented Google service mocks.
 * Run: node test-survey.cjs. No account access, network calls, or real submissions.
 */
const fs=require('node:fs');const vm=require('node:vm');const assert=require('node:assert/strict');
const source=fs.readFileSync(__dirname+'/Code.gs','utf8');
let assertions=0;function check(fn){fn();assertions++;}
function runtime(){
 let nextId=1,constructionCount=0,failAt=0,failDestination=false;const forms={},books={},props={},triggers=[];
 class Choice{constructor(value,nav){this.value=value;this.nav=nav;}getValue(){return this.value;}getGotoPage(){return this.nav instanceof Item?this.nav:null;}getPageNavigationType(){return this.nav instanceof Item?'GO_TO_PAGE':this.nav||null;}}
 class Item{
  constructor(type){this.id=nextId++;this.type=type;this.title='';this.required=false;this.choices=[];}
  getId(){return this.id;}getType(){return this.type;}getTitle(){return this.title;}setTitle(x){this.title=x;return this;}
  setHelpText(x){this.help=x;return this;}setRequired(x){this.required=x;return this;}isRequired(){return this.required;}
  createChoice(x,n){return new Choice(x,n);}setChoiceValues(x){this.choices=x.map(v=>new Choice(v));return this;}
  setChoices(x){this.choices=x;return this;}getChoices(){return this.choices;}setValidation(x){this.validation=x;return this;}
  asMultipleChoiceItem(){assert.equal(this.type,'mc');return this;}asCheckboxItem(){assert.equal(this.type,'checks');return this;}
  asTextItem(){assert.equal(this.type,'text');return this;}asParagraphTextItem(){assert.equal(this.type,'paragraph');return this;}
 }
 class Form{
  constructor(title,published){this.id='form'+nextId++;this.title=title;this.published=published;this.items=[];this.responses=[];this.settings={};}
  getId(){return this.id;}getItems(){return this.items;}getResponses(){return this.responses;}isPublished(){return !!this.published;}
  add(type){constructionCount++;if(constructionCount===failAt)throw Error('simulated transient builder failure');const item=new Item(type);this.items.push(item);return item;}
  addPageBreakItem(){return this.add('page');}addSectionHeaderItem(){return this.add('header');}addTextItem(){return this.add('text');}
  addParagraphTextItem(){return this.add('paragraph');}addMultipleChoiceItem(){return this.add('mc');}addCheckboxItem(){return this.add('checks');}
  deleteItem(item){this.items.splice(this.items.indexOf(item),1);return this;}
  setDestination(type,id){if(failDestination)throw Error('simulated destination setup interruption');assert.equal(type,'SPREADSHEET');this.destination=id;const raw=new Sheet('Form Responses 1');raw.data=[['Timestamp','RAW MUST SURVIVE']];books[id].sheets.unshift(raw);return this;}getDestinationId(){if(!this.destination)throw Error('The form currently has no response destination.');return this.destination;}
  getEditUrl(){return 'https://docs.google.com/forms/d/'+this.id+'/edit';}getPublishedUrl(){return 'https://docs.google.com/forms/d/e/'+this.id+'/viewform';}
  setPublished(x){this.published=x;this.settings.AcceptingResponses=x;return this;}supportsAdvancedResponderPermissions(){return true;}
  collectsEmail(){return !!this.settings.CollectEmail;}hasLimitOneResponsePerUser(){return !!this.settings.LimitOneResponsePerUser;}
  isPublishingSummary(){return !!this.settings.PublishingSummary;}
 }
 ['AcceptingResponses','CollectEmail','LimitOneResponsePerUser','PublishingSummary','ShowLinkToRespondAgain','AllowResponseEdits',
  'ShuffleQuestions','ProgressBar','IsQuiz','CustomClosedFormMessage','Description','ConfirmationMessage'].forEach(key=>{
  Form.prototype['set'+key]=function(x){this.settings[key]=x;return this;};
 });
 class Range{
  constructor(sheet,r,c,h,w){Object.assign(this,{sheet,r,c,h,w});}
  setValues(rows){assert.equal(rows.length,this.h);rows.forEach((row,i)=>{assert.equal(row.length,this.w);for(let j=0;j<row.length;j++){
    const rowNo=this.r+i-1;this.sheet.data[rowNo]??=[];this.sheet.data[rowNo][this.c+j-1]=row[j];}});return this;}
  getValues(){return Array.from({length:this.h},(_,i)=>Array.from({length:this.w},(_,j)=>this.sheet.data[this.r+i-1]?.[this.c+j-1]??''));}
  setNote(x){return this;}setFontWeight(x){return this;}setBackground(x){return this;}setFontColor(x){return this;}setWrap(x){return this;}
 }
 class Sheet{
  constructor(name){this.name=name;this.data=[];this.cols=26;this.rows=1000;}
  setName(n){this.name=n;return this;}getName(){return this.name;}getRange(r,c,h=1,w=1){return new Range(this,r,c,h,w);}
  getMaxColumns(){return this.cols;}getMaxRows(){return this.rows;}getLastRow(){return this.data.length;}
  insertColumnsAfter(c,n){this.cols+=n;return this;}insertRowsAfter(r,n){this.rows+=n;return this;}
  clearContents(){this.data=[];return this;}setFrozenRows(n){return this;}setColumnWidths(a,b,c){return this;}setColumnWidth(a,b){return this;}
 }
 class Book{
  constructor(title){this.id='book'+nextId++;this.title=title;this.sheets=[new Sheet('Sheet1')];}
  getId(){return this.id;}getUrl(){return 'https://docs.google.com/spreadsheets/d/'+this.id+'/edit';}
  setSpreadsheetTimeZone(x){return this;}getSheets(){return this.sheets;}getSheetByName(x){return this.sheets.find(s=>s.name===x)||null;}
  insertSheet(name){const s=new Sheet(name);this.sheets.push(s);return s;}
 }
 function validation(){return {requireSelectAtMost(n){this.max=n;return this;},requireTextMatchesPattern(p){this.pattern=p;return this;},
   setHelpText(x){this.help=x;return this;},build(){return this;}};}
 Form.prototype.setCustomClosedFormMessage=function(){throw Error('Invalid data updating form.');};
 const env={console:{log(){}},FormApp:{PageNavigationType:{SUBMIT:'SUBMIT',CONTINUE:'CONTINUE'},DestinationType:{SPREADSHEET:'SPREADSHEET'},
  create:(title,pub)=>{const f=new Form(title,pub);forms[f.id]=f;return f;},openById:id=>{if(!forms[id])throw Error('Form missing');return forms[id];},
  createCheckboxValidation:validation,createTextValidation:validation},
  SpreadsheetApp:{create:title=>{const b=new Book(title);books[b.id]=b;return b;},openById:id=>books[id]},
  PropertiesService:{getScriptProperties:()=>({getProperty:k=>props[k]||null,setProperty:(k,v)=>{props[k]=v;}})},
  LockService:{getScriptLock:()=>({waitLock(){},releaseLock(){}})},
  ScriptApp:{getProjectTriggers:()=>triggers,deleteTrigger:t=>triggers.splice(triggers.indexOf(t),1),newTrigger:handler=>{
   const t={handler,getHandlerFunction(){return this.handler;},getTriggerSourceId(){return this.form;}};
   return {forForm(id){t.form=id;return this;},onFormSubmit(){return this;},create(){triggers.push(t);return t;}};}},
  Utilities:{formatDate:(date,tz,fmt)=>new Date(date.getTime()+7*3600000).toISOString().slice(0,19).replace('T',' ')}
 };
 const ctx=vm.createContext(env);vm.runInContext(source,ctx);
 return {ctx,forms,books,triggers,state:()=>JSON.parse(Object.values(props)[0]||'null'),
  failAfter:n=>{failAt=constructionCount+n;},failDestination:x=>{failDestination=x;},allow:()=>{failAt=0;}};
}
const r=runtime(),c=r.ctx;
check(()=>assert.equal(c.runSelfChecks(),true));
check(()=>assert.throws(()=>c.getSurveyLinks(),/createSurvey/));
c.createSurvey();let s=r.state();
check(()=>assert.equal(Object.keys(r.forms).length,2));check(()=>assert.equal(Object.keys(r.books).length,2));
check(()=>assert.equal(r.triggers.length,1));
check(()=>assert.equal(r.books[s.workbookId].getSheetByName('Form Responses 1').data[0][1],'RAW MUST SURVIVE'));
check(()=>assert.equal(r.forms[s.mainFormId].published,true));
check(()=>assert.equal(r.forms[s.mainFormId].settings.AcceptingResponses,true));
check(()=>assert.equal(c.verifySurvey(),true));
const firstIds=Object.keys(r.forms);c.createSurvey();
check(()=>assert.deepEqual(Object.keys(r.forms),firstIds));check(()=>assert.equal(r.triggers.length,1));
const main=r.forms[s.mainFormId];
// Navigate the ACTUAL mocked constructed choices, not just the source spec.
function path(answers){let page='consent',seen=[];const spec=c.mainSpecification_();
 for(let n=0;n<20;n++){
  seen.push(page);const index=spec.findIndex(p=>p.id===page),definition=spec[index];
  const nav=definition.items.find(q=>q.routes);
  if(nav){const item=main.items.find(i=>i.id===s.mainMeta.items[nav.code]);const choice=item.choices.find(x=>x.value===answers[nav.code]);assert.ok(choice);
   if(choice.nav==='SUBMIT')return seen;page=Object.keys(s.mainMeta.pages).find(k=>s.mainMeta.pages[k]===choice.nav.id);
  }else if(index===spec.length-1)return seen;else page=spec[index+1].id;
 }throw Error('Loop');}
const sp=c.mainSpecification_(),gates=['consent','age','scope','comparison_gate'];
const opts=gates.map(id=>sp.find(p=>p.id===id).items[0].choices);
let paths=0;
for(const consent of opts[0])for(const age of opts[1])for(const scope of opts[2])for(const gate of opts[3]){
 const a={consent,age,scope,comparison_gate:gate},p=path(a);paths++;
 check(()=>{
  if(consent!=='Ya, saya bersedia')assert.deepEqual(p,['consent']);
  else if(!['18–20 tahun','21–24 tahun','25–27 tahun','28–30 tahun'].includes(age))assert.deepEqual(p,['consent','age']);
  else if(scope!=='Ya')assert.deepEqual(p,['consent','age','scope']);
  else {assert.ok(p.includes('finish'));assert.equal(p.includes('comparison'),gate==='Ya');}
 });
}
const before=new Date();before.setDate(before.getDate()-1);
const valid={consent:'Ya, saya bersedia',age:'21–24 tahun',scope:'Ya',recall:'Cukup yakin dengan sebagian besar jawaban',
 chooser:'Saya sendiri',other_chooser:'Saya sendiri',comparison_gate:'Ya',
 tooth_deliberation:'Saya memilih tanpa membandingkan dengan produk lain',
 other_deliberation:'Saya membandingkan beberapa produk sebelum memilih',current_product:'Pepsodent pencegah gigi berlubang',
 previous_product:'Pepsodent Sensitive Expert',reason_open:'=IMPORTXML("x","y")'};
function response(id,date,a){return {getId:()=>id,getTimestamp:()=>date,getItemResponses:()=>Object.keys(a).map(k=>({
 getItem:()=>main.items.find(i=>i.id===s.mainMeta.items[k]),getResponse:()=>a[k]}))};}
check(()=>assert.equal(typeof c.openForPilot,'undefined'));
check(()=>assert.equal(typeof c.launchSurvey,'undefined'));
check(()=>assert.equal(r.forms[s.mainFormId].published,true));
main.responses.push(response('pilot1',before,valid));
check(()=>assert.equal(c.refreshResponses().included,0));
s=r.state();const launch=s.launchAt,after=new Date(new Date(launch).getTime()+1000);
main.responses.push(response('main1',after,valid));
main.responses.push(response('minor1',after,{consent:'Ya, saya bersedia',age:'Di bawah 18 tahun'}));
main.responses.push(response('decline1',after,{consent:'Tidak, saya tidak bersedia'}));
main.responses.push(response('unknownScope',after,{consent:'Ya, saya bersedia',age:'28–30 tahun',scope:'Tidak yakin'}));
const summary=c.refreshResponses();
check(()=>assert.equal(summary.total,5));check(()=>assert.equal(summary.included,1));check(()=>assert.equal(summary.paired,1));
const book=r.books[s.workbookId];const clean=book.getSheetByName('CLEAN').data;
const index=clean[0].indexOf('reason_open');
check(()=>assert.equal(clean.find(x=>x[0]==='main1')[index].charAt(0),"'"));
check(()=>assert.equal(clean.find(x=>x[0]==='main1')[clean[0].indexOf('manual_pathway')],'UNREVIEWED'));
book.getSheetByName('REVIEW').getRange(2,1,1,4).setValues([['main1','BASIC','PREMIUM','Case roster checked']]);
c.refreshResponses();
check(()=>assert.equal(book.getSheetByName('CLEAN').data.find(x=>x[0]==='main1')[clean[0].indexOf('manual_pathway')],'PREMIUM → BASIC'));
check(()=>assert.equal(book.getSheetByName('REVIEW').data[1][0],'main1'));
c.createSurvey();check(()=>assert.equal(r.state().launchAt,launch));
c.createSurvey();check(()=>assert.equal(main.responses.length,5));
check(()=>assert.equal(main.settings.AcceptingResponses,true));
c.closeSurvey();check(()=>assert.equal(main.settings.AcceptingResponses,false));
check(()=>assert.equal(r.forms[s.contactFormId].settings.AcceptingResponses,false));
check(()=>assert.equal(c.refreshResponses().included,1));
// Changing routing manually must be caught before opening.
const ageItem=main.items.find(i=>i.id===s.mainMeta.items.age);const original=ageItem.choices[0].nav;
ageItem.choices[0].nav=main.items.find(i=>i.id===s.mainMeta.pages.profile);
check(()=>assert.throws(()=>c.verifySurvey(),/route/));ageItem.choices[0].nav=original;
// Pure extraction corner cases and paired exclusion.
check(()=>assert.equal(c.normalizeRecord_('a',after,{...valid,chooser:'Orang tua atau keluarga'},s).comparable,false));
check(()=>assert.ok(c.normalizeRecord_('a',after,{...valid,paid_price:'99',price_certainty:'Produk itu gratis'},s).flags.includes('FREE_WITH_NONZERO_PRICE')));
check(()=>assert.ok(c.normalizeRecord_('a',new Date('2026-11-04T00:00:00Z'),{...valid,acquired_month:'12/2026'},s).flags.includes('MONTH_IN_FUTURE')));
check(()=>assert.equal(c.tierHint_('Pepsodent herbal'),'PEPSODENT_TIER_UNCLEAR'));
check(()=>assert.equal(c.tierHint_('Pepsodent'),'PEPSODENT_TIER_UNCLEAR'));
check(()=>assert.equal(c.deliberationValue_('Tidak ingat'),null));
const r2=runtime();r2.failAfter(13);
check(()=>assert.throws(()=>r2.ctx.createSurvey(),/transient/));
check(()=>assert.equal(Object.keys(r2.forms).length,2));
const legacy=r2.state();legacy.version='1.0.0';
r2.ctx.PropertiesService.getScriptProperties().setProperty('EFEST_TOOTHPASTE_SURVEY_V1',JSON.stringify(legacy));
Object.values(r2.forms).forEach(f=>{f.published=false;f.settings.AcceptingResponses=false;});
r2.allow();r2.ctx.createSurvey();
check(()=>assert.equal(r2.state().version,'1.1.1'));
check(()=>assert.equal(r2.forms[legacy.mainFormId].settings.AcceptingResponses,true));
check(()=>assert.equal(Object.keys(r2.forms).length,2));check(()=>assert.equal(r2.ctx.verifySurvey(),true));
check(()=>assert.equal(r2.triggers.length,1));
const r3=runtime();r3.ctx.ScriptApp.newTrigger=()=>{throw Error('Workspace trigger restriction');};
r3.ctx.createSurvey();
check(()=>assert.ok(r3.state().triggerWarning.includes('Workspace trigger restriction')));
check(()=>assert.equal(r3.ctx.refreshResponses().total,0));
check(()=>assert.notEqual(r.state().workbookId,r.state().contactWorkbookId));
check(()=>assert.equal(book.getSheetByName('Form Responses 1').data[0][1],'RAW MUST SURVIVE'));

// Regression for the user's second failure: both forms built, neither linked.
const r4=runtime();r4.failDestination(true);
check(()=>assert.throws(()=>r4.ctx.createSurvey(),/destination setup interruption/));
const failed=r4.state();
check(()=>assert.equal(failed.mainBuilt,true));
check(()=>assert.equal(failed.contactBuilt,true));
const itemIds=r4.forms[failed.mainFormId].items.map(x=>x.id);
check(()=>assert.throws(()=>r4.forms[failed.mainFormId].getDestinationId(),/no response destination/));
failed.version='1.1.0';
r4.ctx.PropertiesService.getScriptProperties().setProperty('EFEST_TOOTHPASTE_SURVEY_V1',JSON.stringify(failed));
r4.failDestination(false);r4.ctx.createSurvey();
check(()=>assert.equal(Object.keys(r4.forms).length,2));
check(()=>assert.deepEqual(r4.forms[failed.mainFormId].items.map(x=>x.id),itemIds));
check(()=>assert.equal(r4.forms[failed.mainFormId].getDestinationId(),failed.workbookId));
check(()=>assert.equal(r4.forms[failed.contactFormId].getDestinationId(),failed.contactWorkbookId));
check(()=>assert.equal(r4.forms[failed.mainFormId].settings.AcceptingResponses,true));
check(()=>assert.equal(r4.state().version,'1.1.1'));
check(()=>assert.throws(()=>r4.ctx.responseDestinationId_({getDestinationId(){throw Error('Permission denied');}}),/Permission denied/));
const linked=r4.forms[failed.mainFormId];let relinkCalls=0;const originalSet=linked.setDestination;
linked.setDestination=function(...args){relinkCalls++;return originalSet.apply(this,args);};
r4.ctx.createSurvey();check(()=>assert.equal(relinkCalls,0));

// Export the exact generated text as a human-readable questionnaire.
const lines=['# Kuesioner yang dibuat oleh Code.gs','',
 'Teks berikut diekstrak dari spesifikasi script yang diuji. Formulir utama tidak menyebut tier Premium/Basic atau tiga pilar di muka.',''];
sp.forEach(page=>{lines.push('## '+page.title,'');if(page.help)lines.push(page.help,'');page.items.forEach(q=>{
 lines.push('**'+q.title+'**'+(q.required?'':' (opsional)'),'');if(q.help)lines.push(q.help,'');
 (q.choices||[]).forEach((v,i)=>lines.push('- '+v+(q.routes?' → '+q.routes[i]:'')));lines.push('');});});
fs.writeFileSync(__dirname+'/KUESIONER.md',lines.join('\n'));
const report={environment:'Node.js '+process.version,scope:'Local mocked Google-service contract/integration checks; no authenticated Google execution',
 assertions,constructedRoutingCombinations:paths,mainQuestions:c.questions_(sp).length,mainPages:sp.length,
 maximumMainPathQuestions:sp.reduce((n,p)=>n+p.items.length,0),
 checks:['Syntax and pure self-checks','Idempotent form/workbook creation','126 eligibility and comparison routing combinations',
 'One-shot opening and legacy pre-start separation','Screenout and incomplete exclusion','Separate contact data destination','Manual review and raw Forms response sheet preserved',
 'Formula injection escape in derived sheets','Pairwise eligibility','Future-month and contradictory-price flags',
 'No automatic tier verification','First-run timestamp preserved','Closed forms','Modified-route detection','Interrupted-build recovery and failed-v1.0 migration','Closed-message failure regression: setter throws if called','Missing destination throws: handled and linked','Already-built v1.1 recovery preserves item IDs','Already-linked destination is not recreated','Permission errors are not hidden'],
 notTested:['Actual Google authorization','Actual Google service latency/quotas','Real browser rendering','Google Workspace responder permissions','Respondent comprehension or duration']};
fs.writeFileSync(__dirname+'/TEST_RESULTS.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));

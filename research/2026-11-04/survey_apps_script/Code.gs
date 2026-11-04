/**
 * Survei pasta gigi — E-Fest / v1.1.1 / 4 November 2026
 * Paste this ENTIRE file into Code.gs at script.google.com.
 * Run createSurvey ONCE. Copy SHARE_THIS_LINK from the execution log.
 * No deployment, external library, API key, or paid service required.
 * Forms are opened automatically when setup completes. No invitations or emails are sent.
 */
const SURVEY_CONFIG = Object.freeze({
  version: '1.1.1',
  propertyKey: 'EFEST_TOOTHPASTE_SURVEY_V1',
  title: 'Pasta gigi yang dipakai sehari-hari',
  timezone: 'Asia/Jakarta',
  // Change only before createSurvey(). The survey uses plain Indonesian.
  team: 'Tim studi E-Fest',
  estimatedMinutes: '8–10'
});

function mainSpecification_() {
  const role = ['Saya sendiri', 'Orang tua atau keluarga', 'Pasangan atau teman serumah',
    'Saya bersama orang lain', 'Orang lain', 'Tidak tahu / tidak ingat'];
  const deliberation = ['Saya tidak ikut memilih',
    'Saya memilih tanpa membandingkan dengan produk lain',
    'Saya membandingkan beberapa produk sebelum memilih',
    'Tidak ingat'];
  return [
    {id:'consent', title:'Sebelum mulai', items:[
      mc_('consent','Apakah Anda bersedia ikut survei ini?',
        ['Ya, saya bersedia','Tidak, saya tidak bersedia'], true, '',
        ['age','SUBMIT'])
    ]},
    {id:'age', title:'Tentang Anda', items:[
      mc_('age','Berapa usia Anda saat ini?',
        ['Di bawah 18 tahun','18–20 tahun','21–24 tahun','25–27 tahun','28–30 tahun',
         'Di atas 30 tahun','Memilih tidak menjawab'],true,'',
        ['SUBMIT','scope','scope','scope','scope','SUBMIT','SUBMIT'])
    ]},
    {id:'scope', title:'Penggunaan pasta gigi', items:[
      mc_('scope','Dalam 6 bulan terakhir, apakah Anda menggunakan pasta gigi saat tinggal di Indonesia?',
        ['Ya','Tidak','Tidak yakin'],true,'',['profile','SUBMIT','SUBMIT'])
    ]},
    {id:'profile', title:'Keseharian Anda', items:[
      mc_('living','Saat ini Anda tinggal dengan siapa?',
        ['Orang tua atau keluarga','Pasangan / keluarga yang saya bangun sendiri',
         'Sendiri, termasuk di kos','Teman kos, teman serumah, atau asrama',
         'Tempat tinggal saya berganti-ganti','Lainnya','Memilih tidak menjawab']),
      mc_('activity','Apa kegiatan utama Anda saat ini?',
        ['Sekolah / kuliah','Bekerja / berusaha','Kuliah sambil bekerja',
         'Sedang mencari pekerjaan','Mengurus rumah tangga','Lainnya','Memilih tidak menjawab']),
      text_('city','Di kota atau kabupaten mana Anda tinggal?',false,
        'Opsional. Cukup nama kota atau kabupaten, tanpa alamat lengkap.')
    ]},
    {id:'current', title:'Pasta gigi yang terakhir dibeli atau diterima',
      help:'Ingat satu kejadian paling baru ketika Anda membeli atau menerima pasta gigi untuk Anda gunakan. Jika orang lain yang membeli, jawab sebatas yang Anda tahu. Produk itu tidak harus sudah habis.',
      items:[
      text_('current_product','Apa merek dan varian pasta giginya?',true,
        'Tulis sesuai yang Anda ingat dari kemasan. Kalau hanya ingat mereknya, tulis mereknya. Kalau tidak tahu, tulis “tidak tahu”.'),
      text_('acquired_month','Kira-kira bulan dan tahun berapa produk itu dibeli atau diterima?',false,
        'Opsional. Gunakan MM/YYYY, misalnya 10/2026. Jika tidak ingat, kosongkan.', 'month'),
      text_('pack','Berapa ukuran dan jumlah kemasannya?',false,
        'Opsional. Misalnya 1 tabung 100 g atau 2 tabung 160 g. Kosongkan jika tidak tahu.'),
      mc_('chooser','Siapa yang memilih merek dan variannya?',role),
      mc_('payer','Siapa yang menyediakan uang untuk pembelian itu?',
        role.slice(0,5).concat(['Tidak ada pembayaran, misalnya sampel gratis','Tidak tahu / tidak ingat'])),
      mc_('shopper','Siapa yang melakukan pembelian atau pemesanan?',
        role.slice(0,5).concat(['Saya menerima sampel / hadiah, tidak tahu pembelinya','Tidak tahu / tidak ingat'])),
      mc_('users','Siapa yang memakai tabung yang sama?',
        ['Saya sendiri','Saya dan orang lain','Belum dipakai','Tidak tahu']),
      mc_('channel','Dari mana produk itu dibeli atau diperoleh?',
        ['Minimarket','Warung atau toko kelontong','Supermarket / hypermarket',
         'Apotek atau toko kesehatan / kecantikan','Marketplace / toko online',
         'Sampel atau hadiah','Tempat lain','Tidak tahu karena bukan saya yang membeli']),
      text_('paid_price','Kalau tahu, berapa total harga yang dibayar untuk kemasan tadi?',false,
        'Rupiah, angka saja tanpa titik. Misalnya 25000. Jika gratis, tulis 0. Jika tidak tahu, kosongkan.', 'price'),
      mc_('price_certainty','Seberapa yakin Anda dengan harga tersebut?',
        ['Saya ingat harganya / punya bukti pembelian','Perkiraan saja','Produk itu gratis','Saya tidak tahu harganya']),
      mc_('promo','Apakah saat itu ada promo atau potongan harga?',
        ['Ya','Tidak','Tidak tahu']),
      mc_('tooth_deliberation','Sebelum produk itu dibeli, bagaimana Anda ikut memilih?',deliberation),
      text_('expected_benefit','Apa yang Anda harapkan dari produk yang terakhir dibeli atau diterima tadi?',false,
        'Boleh singkat. Kalau tidak punya harapan khusus, tulis begitu.')
    ]},
    {id:'history', title:'Apa yang terjadi saat memilih penggantinya?', items:[
      text_('previous_product','Sebelum produk tadi, pasta gigi apa yang terakhir Anda gunakan?',true,
        'Tulis merek dan varian jika ingat. Boleh sama dengan produk tadi. Jika tidak tahu atau baru pertama memakai pasta gigi, tuliskan saja.'),
      mc_('previous_status','Saat produk yang baru mulai dipakai, bagaimana keadaan produk sebelumnya?',
        ['Sudah habis / hampir habis','Masih ada, tetapi saya berhenti memakainya',
         'Masih ada dan dipakai bergantian','Saya hanya memakai produk lain sementara',
         'Produk baru belum dipakai','Ini pertama kali saya menggunakan pasta gigi','Tidak ingat']),
      mc_('previous_experience','Mana yang paling menggambarkan pengalaman Anda dengan produk sebelumnya?',
        ['Ada manfaat yang terasa dan penting bagi saya','Ada manfaat yang terasa, tetapi tidak terlalu penting bagi saya',
         'Saya tidak merasakan perbedaan yang berarti','Saya merasa kurang nyaman memakainya',
         'Saya belum cukup lama memakai untuk menilai','Tidak punya harapan khusus','Tidak ingat']),
      text_('desired_product','Pada kejadian pembelian atau penerimaan terakhir tadi, produk apa yang sebenarnya Anda inginkan?',true,
        'Tulis merek dan varian jika ada. Jika tidak punya pilihan tertentu, tulis “tidak ada pilihan khusus”.'),
      paragraph_('reason_open','Apa yang paling menentukan produk mana yang akhirnya Anda pakai?',true,
        'Ceritakan singkat kejadian tadi. Kalau bukan Anda yang memutuskan, ceritakan sebatas yang Anda tahu.'),
      checks_('reasons','Dari hal-hal berikut, mana yang ikut memengaruhi kejadian tadi?',[
        'Harganya sesuai uang yang tersedia','Ada promo atau paket hemat',
        'Produk itu sudah biasa saya pakai','Saya membutuhkan manfaat tertentu',
        'Rasa atau kenyamanannya cocok','Produk sebelumnya tidak sesuai harapan',
        'Pilihan orang yang membeli / menyediakan','Memakai stok yang sudah ada di rumah',
        'Produk yang diinginkan tidak ditemukan','Saya lupa / belum sempat membeli produk yang biasanya',
        'Tidak punya kebutuhan tambahan di luar pasta gigi biasa','Ada alasan lain',
        'Saya tidak tahu / tidak ikut memutuskan'],3,
        'Pilih maksimal 3. Jika memilih “tidak tahu / tidak ikut memutuskan”, pilih itu saja.'),
      mc_('availability','Bagaimana dengan produk yang Anda inginkan pada kejadian itu?',[
        'Saya mendapat produk yang saya inginkan','Produknya tersedia, tetapi akhirnya memilih yang lain',
        'Saya mencari, tetapi tidak menemukannya','Saya tidak mencari karena memakai yang disediakan orang lain / stok rumah',
        'Saya tidak punya pilihan produk tertentu','Tidak tahu / tidak ingat'])
    ]},
    {id:'comparison_gate', title:'Satu produk perawatan diri lainnya', items:[
      mc_('comparison_gate','Dalam 3 bulan terakhir, apakah Anda membeli atau menerima produk perawatan diri selain pasta gigi?',
        ['Ya','Tidak','Tidak ingat'],true,
        'Misalnya pembersih wajah, sampo, sabun, deodoran, pelembap, atau parfum.',
        ['comparison','finish','finish'])
    ]},
    {id:'comparison', title:'Ingat produk perawatan diri yang paling baru',
      help:'Pilih yang paling baru dibeli atau diterima dalam 3 bulan terakhir, bukan yang paling mahal atau paling Anda sukai. Jika ada beberapa pada hari yang sama, pilih yang pertama Anda ingat.', items:[
      mc_('other_category','Produk apa itu?',
        ['Pembersih wajah / skincare','Sampo / perawatan rambut','Sabun mandi / perawatan tubuh',
         'Deodoran','Parfum / wewangian','Produk perawatan diri lainnya']),
      text_('other_product','Apa merek dan nama produknya?',false,
        'Opsional. Tulis sebatas yang Anda ingat.'),
      mc_('other_chooser','Siapa yang memilih produk tersebut?',role),
      mc_('other_deliberation','Sebelum produk tersebut dibeli, bagaimana Anda ikut memilih?',deliberation),
      text_('other_expected','Apa yang Anda harapkan dari produk tersebut?',false,
        'Boleh singkat. Jika tidak punya harapan khusus, tulis begitu.'),
      paragraph_('other_reason','Apa yang paling menentukan pilihan produk tersebut?',false,
        'Boleh satu kalimat. Jika bukan Anda yang memilih, jawab sebatas yang Anda tahu.')
    ]},
    {id:'finish', title:'Terakhir, sebelum dikirim', items:[
      mc_('recall','Seberapa yakin Anda mengingat kejadian pasta gigi yang tadi diceritakan?',
        ['Cukup yakin dengan sebagian besar jawaban','Ada beberapa bagian yang hanya perkiraan',
         'Banyak bagian yang tidak saya ingat']),
      paragraph_('note','Ada hal lain yang ingin ditambahkan?',false,
        'Opsional. Anda juga bisa menyebutkan bagian yang tadi kurang pasti.'),
      text_('followup_code','Jika bersedia dihubungi untuk obrolan lanjutan, buat kode Anda di sini.',false,
        'Opsional. Gunakan 6–12 huruf/angka acak dan simpan kodenya. Jangan gunakan nama, nomor telepon, atau tanggal lahir. Setelah mengirim survei, ada tautan formulir kontak terpisah. Kosongkan jika tidak berminat.', 'code')
    ]}
  ];
}

function contactSpecification_() {
  return [
    {id:'contact_consent',title:'Kontak untuk obrolan lanjutan',items:[
      mc_('contact_consent','Apakah Anda bersedia memberikan kontak untuk undangan obrolan lanjutan?',
        ['Ya, saya berusia 18–30 tahun, sudah menyelesaikan survei utama, dan bersedia dihubungi',
         'Tidak, saya tidak bersedia'],true,
        'Keikutsertaan tetap sukarela. Mengisi kontak tidak berarti Anda wajib mengikuti obrolan.',
        ['contact_details','SUBMIT'])
    ]},
    {id:'contact_details',title:'Kontak yang bisa dihubungi',items:[
      text_('followup_code','Kode yang Anda tulis di akhir survei utama',true,
        'Masukkan kode yang sama, 6–12 huruf/angka. Kode ini dipakai untuk mencocokkan kontak dengan jawaban Anda.', 'code'),
      text_('contact','Email atau nomor WhatsApp yang bisa dihubungi',true,
        'Cukup salah satu. Kontak hanya digunakan oleh tim studi untuk undangan dan penjadwalan obrolan.'),
      text_('contact_note','Kapan biasanya Anda bisa dihubungi?',false,
        'Opsional. Misalnya sore hari atau akhir pekan.')
    ]}
  ];
}

function mc_(code,title,choices,required,help,routes) {
  return {code:code,type:'mc',title:title,choices:choices,
    required:required!==false,help:help||'',routes:routes||null};
}
function text_(code,title,required,help,validation) {
  return {code:code,type:'text',title:title,required:!!required,
    help:help||'',validation:validation||null};
}
function paragraph_(code,title,required,help) {
  return {code:code,type:'paragraph',title:title,required:!!required,help:help||''};
}
function checks_(code,title,choices,max,help) {
  return {code:code,type:'checks',title:title,choices:choices,required:true,max:max,help:help||''};
}

/** Creates/reuses the same assets. Safe to rerun; does not reset responses. */
function createSurvey() {
  return withLock_(function() {
    runSelfChecks();
    const s = loadState_() || {version:SURVEY_CONFIG.version,phase:'DRAFT'};
    if (['1.0.0','1.1.0',SURVEY_CONFIG.version].indexOf(s.version)<0) throw new Error('Versi tidak dikenali. Jangan menghapus properti project lama.');
    s.version=SURVEY_CONFIG.version;
    if(!s.launchAt)s.launchAt=new Date().toISOString();
    saveState_(s);
    ensureAsset_(s,'mainFormId',function(){return FormApp.create(SURVEY_CONFIG.title);});
    ensureAsset_(s,'contactFormId',function(){return FormApp.create('Kontak lanjutan — studi pasta gigi');});
    ensureAsset_(s,'workbookId',function(){return SpreadsheetApp.create('Data survei pasta gigi — E-Fest');});
    ensureAsset_(s,'contactWorkbookId',function(){return SpreadsheetApp.create('Kontak terbatas — studi pasta gigi');});
    const main=FormApp.openById(s.mainFormId), contact=FormApp.openById(s.contactFormId);
    if (!s.mainBuilt) {
      resetUnfinishedForm_(main);
      configureForm_(main);
      main.setDescription('Kami sedang menyusun studi untuk kompetisi bisnis tentang cara orang memilih dan mendapatkan pasta gigi. '+
        'Kami ingin tahu pengalaman sehari-hari, termasuk jika produk dibeli oleh keluarga. Tidak ada jawaban benar atau salah.\n\n'+
        'Perkiraan waktu '+SURVEY_CONFIG.estimatedMinutes+' menit. Anda boleh berhenti kapan saja. '+
        'Survei utama tidak meminta nama, email, atau nomor telepon. Jawaban akan diringkas untuk studi dan presentasi tim. '+
        'Jika Anda bersedia ikut obrolan lanjutan, kontak diminta melalui formulir terpisah dan dapat dicocokkan lewat kode yang Anda buat.\n\n'+
        'Mohon isi satu kali berdasarkan pengalaman sendiri.\n'+SURVEY_CONFIG.team);
      s.mainMeta=buildForm_(main,mainSpecification_());
      s.mainBuilt=true; saveState_(s);
    }
    if (!s.contactBuilt) {
      resetUnfinishedForm_(contact); configureForm_(contact);
      contact.setDescription('Formulir ini terpisah dari survei utama dan hanya untuk peserta usia 18–30 tahun yang sudah menyelesaikannya. '+
        'Tim menggunakan kode untuk menghubungkan kontak dengan jawaban survei. Kontak tidak dimasukkan ke tabel analisis. '+
        'Tim studi dapat membaca kedua berkas; pemisahan ini bukan anonimitas penuh jika Anda memilih memberikan kontak. '+
        'Anda bebas menolak undangan berikutnya.');
      s.contactMeta=buildForm_(contact,contactSpecification_());
      contact.setConfirmationMessage('Terima kasih. Jika ada obrolan lanjutan yang sesuai, tim studi akan menghubungi Anda.');
      s.contactBuilt=true; saveState_(s);
    }
    ensureResponseDestination_(main,s.workbookId);
    ensureResponseDestination_(contact,s.contactWorkbookId);
    main.setConfirmationMessage('Terima kasih sudah mengisi. Jika Anda menyelesaikan survei utama, berusia 18–30 tahun, dan bersedia ikut obrolan lanjutan, '+
      'simpan kode yang tadi dibuat lalu isi formulir kontak berikut (opsional):\n'+contact.getPublishedUrl()+
      '\nJika tadi berhenti di pertanyaan awal, terima kasih; jawaban tersebut tidak masuk sampel utama.');
    const book=SpreadsheetApp.openById(s.workbookId); book.setSpreadsheetTimeZone(SURVEY_CONFIG.timezone);
    SpreadsheetApp.openById(s.contactWorkbookId).setSpreadsheetTimeZone(SURVEY_CONFIG.timezone);
    initializeWorkbook_(book,s);
    s.ready=true;saveState_(s);
    try {
      ensureTrigger_(s);s.triggerWarning='';
    } catch (error) {
      s.triggerWarning='Automatic refresh trigger could not be installed: '+error.message;
      console.log(s.triggerWarning+' — run refreshResponses() manually when needed.');
    }
    saveState_(s);
    verifySurvey_();
    setOpen_(s,true);
    s.phase='LIVE';saveState_(s);
    const links=logLinks_(s);
    console.log('SHARE_THIS_LINK: '+links.respondent);
    try {writeLinks_(book,s);refreshResponses_();}
    catch(error){console.log('Formulir sudah terbuka. Tabel ringkasan belum diperbarui: '+error.message+'. Jalankan refreshResponses bila diperlukan.');}
    return links;
  });
}

function closeSurvey() {
  return withLock_(function(){
    const s=requireReady_();setOpen_(s,false);s.phase='CLOSED';saveState_(s);
    writeLinks_(SpreadsheetApp.openById(s.workbookId),s);refreshResponses_();
    return logLinks_(s);
  });
}

/** Run any time to recover a missed trigger or rebuild derived sheets. Never changes raw responses. */
function refreshResponses() { return withLock_(refreshResponses_); }
function handleSurveySubmit(e) {
  if(!e || !e.source) throw new Error('Jangan jalankan handleSurveySubmit manual. Gunakan refreshResponses().');
  return refreshResponses();
}
function getSurveyLinks() { return logLinks_(requireReady_()); }
function verifySurvey() { return verifySurvey_(); }

function buildForm_(form,pages) {
  const meta={items:{},pages:{}}, instances={}, breaks={};
  pages.forEach(function(page,index){
    if(index>0) {
      const b=form.addPageBreakItem().setTitle(page.title);
      if(page.help)b.setHelpText(page.help);
      breaks[page.id]=b;meta.pages[page.id]=b.getId();
    } else form.addSectionHeaderItem().setTitle(page.title);
    page.items.forEach(function(q){
      let item;
      if(q.type==='mc') item=form.addMultipleChoiceItem();
      else if(q.type==='text') item=form.addTextItem();
      else if(q.type==='paragraph') item=form.addParagraphTextItem();
      else if(q.type==='checks') item=form.addCheckboxItem();
      else throw new Error('Unknown type: '+q.type);
      item.setTitle(q.title).setRequired(q.required);
      if(q.help)item.setHelpText(q.help);
      if(q.choices)item.setChoiceValues(q.choices);
      if(q.max)item.setValidation(FormApp.createCheckboxValidation().requireSelectAtMost(q.max)
        .setHelpText('Pilih maksimal '+q.max+' jawaban.').build());
      if(q.validation) {
        const patterns={price:'^[0-9]{1,7}$',month:'^(0[1-9]|1[0-2])/20[0-9]{2}$',code:'^[A-Za-z0-9]{6,12}$'};
        const messages={price:'Isi angka rupiah saja, misalnya 25000, atau kosongkan jika tidak tahu.',
          month:'Gunakan MM/YYYY, misalnya 10/2026, atau kosongkan jika tidak ingat.',
          code:'Gunakan 6–12 huruf atau angka, tanpa spasi.'};
        item.setValidation(FormApp.createTextValidation().requireTextMatchesPattern(patterns[q.validation])
          .setHelpText(messages[q.validation]).build());
      }
      meta.items[q.code]=item.getId();instances[q.code]=item;
    });
  });
  pages.forEach(function(page){page.items.forEach(function(q){
    if(!q.routes)return;
    const item=instances[q.code];
    item.setChoices(q.choices.map(function(value,index){
      return item.createChoice(value,q.routes[index]==='SUBMIT'?FormApp.PageNavigationType.SUBMIT:breaks[q.routes[index]]);
    }));
  });});
  return meta;
}

function configureForm_(form) {
  // The old failure occurred in the optional closed-message setter. Do not call it.
  // Recovered v1.0 drafts can be unpublished: publish before updating response state.
  if(form.supportsAdvancedResponderPermissions() && !form.isPublished())form.setPublished(true);
  form.setAcceptingResponses(false);
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setPublishingSummary(false);
  form.setShowLinkToRespondAgain(false);
  form.setAllowResponseEdits(false);
  form.setShuffleQuestions(false);
  form.setProgressBar(true);
}
function resetUnfinishedForm_(form) {
  if(form.getResponses().length)throw new Error('Formulir belum selesai dibuat tetapi sudah memiliki respons. Data tidak dihapus. Gunakan project baru atau periksa manual.');
  const items=form.getItems();for(let i=items.length-1;i>=0;i--)form.deleteItem(items[i]);
}
function setOpen_(s,enabled) {
  [s.mainFormId,s.contactFormId].forEach(function(id){
    const form=FormApp.openById(id);
    if(enabled && form.supportsAdvancedResponderPermissions() && !form.isPublished())form.setPublished(true);
    form.setAcceptingResponses(enabled);
  });
}
// Google throws, rather than returning null, when no destination is configured.
// Handle only this known absence; permission/service errors must remain visible.
function responseDestinationId_(form) {
  try { return form.getDestinationId(); }
  catch (error) {
    if (/no response destination/i.test(String(error))) return null;
    throw error;
  }
}
function ensureResponseDestination_(form,spreadsheetId) {
  if(responseDestinationId_(form)===spreadsheetId)return;
  form.setDestination(FormApp.DestinationType.SPREADSHEET,spreadsheetId);
  if(form.getDestinationId()!==spreadsheetId)throw new Error('Response destination did not link to the expected spreadsheet.');
}
function ensureAsset_(s,key,create) {
  if(!s[key]){s[key]=create().getId();saveState_(s);}
}
function ensureTrigger_(s) {
  const matches=ScriptApp.getProjectTriggers().filter(function(t){
    return t.getHandlerFunction()==='handleSurveySubmit' && t.getTriggerSourceId()===s.mainFormId;
  });
  if(!matches.length)ScriptApp.newTrigger('handleSurveySubmit').forForm(s.mainFormId).onFormSubmit().create();
  matches.slice(1).forEach(function(t){ScriptApp.deleteTrigger(t);});
}
function loadState_(){const value=PropertiesService.getScriptProperties().getProperty(SURVEY_CONFIG.propertyKey);return value?JSON.parse(value):null;}
function saveState_(s){PropertiesService.getScriptProperties().setProperty(SURVEY_CONFIG.propertyKey,JSON.stringify(s));}
function requireReady_(){const s=loadState_();if(!s||!s.ready)throw new Error('Jalankan createSurvey() sampai selesai terlebih dahulu.');return s;}
function withLock_(fn){const lock=LockService.getScriptLock();lock.waitLock(30000);try{return fn();}finally{lock.releaseLock();}}
function questions_(pages){return [].concat.apply([],pages.map(function(p){return p.items;}));}

function initializeWorkbook_(book,s) {
  // Never rename or overwrite any existing sheet: Forms may insert its raw tab first.
  if(!book.getSheetByName('PETUNJUK'))book.insertSheet('PETUNJUK');
  const dict=[['code','section','question','type','required','choices','routing']];
  mainSpecification_().forEach(function(p){p.items.forEach(function(q){
    dict.push([q.code,p.title,q.title,q.type,q.required?'yes':'no',(q.choices||[]).join(' | '),
      q.routes?q.routes.join(' | '):'']);
  });});
  writeTable_(book,'KAMUS',dict);
  if(!book.getSheetByName('REVIEW'))writeTable_(book,'REVIEW',[
    ['response_id','current_tier','previous_tier','review_note'],
    // Blank input rows are not fabricated respondents.
  ]);
  book.getSheetByName('REVIEW').getRange('B1:C1').setNote('Manual review only: BASIC, PREMIUM, OTHER, UNKNOWN. Use exact case SKU roster; do not infer from price or colour. Leave uncertain values UNKNOWN.');
}
function writeLinks_(book,s) {
  const main=FormApp.openById(s.mainFormId),contact=FormApp.openById(s.contactFormId);
  writeTable_(book,'PETUNJUK',[
    ['SURVEI PASTA GIGI — '+SURVEY_CONFIG.version,''],
    ['Status',s.phase],['Mulai sampel utama',s.launchAt||'Tidak diketahui'],
    ['Editor survei utama',main.getEditUrl()],['Tautan responden',main.getPublishedUrl()],
    ['Editor kontak terpisah',contact.getEditUrl()],['Formulir kontak',contact.getPublishedUrl()],
    ['Data kontak (akses terbatas)',SpreadsheetApp.openById(s.contactWorkbookId).getUrl()],
    ['Cara mulai','Jalankan createSurvey sekali. Bagikan SHARE_THIS_LINK dari Execution log.'],
    ['Cara perbarui tabel','refreshResponses; juga otomatis setelah respons baru jika trigger tersedia'],
    ['Status trigger',s.triggerWarning||'Trigger pembaruan otomatis terpasang'],
    ['Data asli','Tab respons bawaan Google Forms dipertahankan. Jangan mengubah atau menghapusnya.'],
    ['Tabel turunan','CLEAN dan RINGKASAN ditulis ulang saat refresh. Simpan catatan hanya di REVIEW atau tab baru.'],
    ['Klasifikasi tier','Isi REVIEW dengan BASIC / PREMIUM / OTHER / UNKNOWN dan alasan. Petunjuk otomatis bukan verifikasi.'],
    ['Keamanan akses','Jangan bagikan editor atau spreadsheet kepada responden. Bagikan tautan responden saja.'],
    ['Batas studi','Sampel kemudahan; angka hanya menggambarkan responden. Tidak mengestimasi prevalensi nasional atau sebab-akibat.'],
    ['Periode kasus','Catat tanggal kejadian. Pembelian setelah Juni 2026 tidak otomatis menjelaskan penurunan historis.'],
    ['Kontak','Berkas kontak terpisah, tetapi pemilik kedua berkas dapat menghubungkannya lewat kode. Batasi akses dan tentukan waktu penghapusan.'],
    ['Tidak ada A/B test','Perbandingan kategori berasal dari pengalaman orang yang sama, bukan eksperimen.'],
    ['Pemeriksaan manual','verifySurvey memeriksa struktur; uji tautan responden di browser tanpa login sebelum menyebarkan. Kebijakan Google Workspace dapat membatasi akses.']
  ]);
}
function logLinks_(s) {
  const result={status:s.phase,editor:FormApp.openById(s.mainFormId).getEditUrl(),
    respondent:FormApp.openById(s.mainFormId).getPublishedUrl(),
    responses:SpreadsheetApp.openById(s.workbookId).getUrl(),
    contactEditor:FormApp.openById(s.contactFormId).getEditUrl(),
    contactData:SpreadsheetApp.openById(s.contactWorkbookId).getUrl(),
    automaticRefresh:s.triggerWarning||'Installed'};
  console.log(JSON.stringify(result,null,2));return result;
}

function refreshResponses_() {
  const s=requireReady_(),book=SpreadsheetApp.openById(s.workbookId);
  const codes=questions_(mainSpecification_()).map(function(q){return q.code;});
  const byItem={};Object.keys(s.mainMeta.items).forEach(function(k){byItem[String(s.mainMeta.items[k])]=k;});
  const reviews=readReviews_(book);
  const records=FormApp.openById(s.mainFormId).getResponses().map(function(response){
    const a={};response.getItemResponses().forEach(function(ir){
      const code=byItem[String(ir.getItem().getId())];if(code)a[code]=ir.getResponse();
    });
    return normalizeRecord_(response.getId(),response.getTimestamp(),a,s,reviews[String(response.getId())]);
  });
  const codeCounts={};records.forEach(function(r){const code=String(r.answers.followup_code||'').toUpperCase();
    if(code)codeCounts[code]=(codeCounts[code]||0)+1;});
  records.forEach(function(r){const code=String(r.answers.followup_code||'').toUpperCase();
    if(code&&codeCounts[code]>1)r.flags.push('FOLLOWUP_CODE_REUSED_CHECK_MANUALLY');});
  const header=['response_id','submitted_at_wib','collection_phase','eligibility','completed','included_main',
    'current_tier_hint','previous_tier_hint','manual_pathway','comparison_eligible',
    'tooth_compared','other_compared','quality_flags'].concat(codes);
  const rows=[header];
  records.forEach(function(r){rows.push([
    r.id,Utilities.formatDate(r.timestamp,SURVEY_CONFIG.timezone,'yyyy-MM-dd HH:mm:ss'),r.phase,r.eligibility,
    r.completed,r.included,r.currentHint,r.previousHint,r.pathway,r.comparable,r.toothCompared,r.otherCompared,
    r.flags.join(' | ')
  ].concat(codes.map(function(k){return cellAnswer_(r.answers[k]);})));});
  writeTable_(book,'CLEAN',rows);
  const included=records.filter(function(r){return r.included;});
  const paired=included.filter(function(r){return r.comparable;});
  const summary=[['Ukuran / jawaban','Jumlah','Penyebut / catatan'],
    ['Semua respons terkirim',records.length,'Termasuk penolakan, di luar sasaran, dan pilot'],
    ['Respons utama lengkap yang memenuhi syarat',included.length,'Persetujuan + usia 18–30 + penggunaan di Indonesia + mencapai akhir + setelah launch'],
    ['Respons sebelum waktu mulai',records.filter(function(r){return r.phase==='BEFORE_START';}).length,'Hanya relevan jika melanjutkan project lama yang sudah berisi respons'],
    ['Perbandingan kategori yang dapat dibaca',paired.length,'Ikut memilih kedua kategori dan mengingat prosesnya'],
    ['Membandingkan kategori lain, tetapi tidak membandingkan pasta gigi',paired.filter(function(r){return r.otherCompared&&!r.toothCompared;}).length,'Penyebut: '+paired.length+' pasangan; bukan bukti daya beli'],
    ['Membandingkan pasta gigi, tetapi tidak membandingkan kategori lain',paired.filter(function(r){return r.toothCompared&&!r.otherCompared;}).length,'Penyebut: '+paired.length+' pasangan'],
    ['Pathway sudah ditinjau manual',included.filter(function(r){return r.pathway!=='UNREVIEWED'&&r.pathway!=='UNKNOWN';}).length,'Isi REVIEW; petunjuk kata pada nama produk tidak dihitung sebagai verifikasi'],
    ['Ada flag kualitas',included.filter(function(r){return r.flags.length>0;}).length,'Perlu dibaca; flag bukan alasan otomatis menghapus respons']];
  ['chooser','payer','previous_experience','availability'].forEach(function(code){
    const freq={};included.forEach(function(r){const value=cellAnswer_(r.answers[code])||'(kosong)';freq[value]=(freq[value]||0)+1;});
    Object.keys(freq).sort().forEach(function(v){summary.push([code+' — '+v,freq[v],'Penyebut: '+included.length+' respons utama']);});
  });
  const pf={};included.forEach(function(r){pf[r.pathway]=(pf[r.pathway]||0)+1;});
  Object.keys(pf).sort().forEach(function(k){summary.push(['Manual pathway — '+k,pf[k],'Dua nama produk saja tidak membuktikan penghentian permanen atau sebab-akibat']);});
  summary.push(['Terakhir diperbarui',Utilities.formatDate(new Date(),SURVEY_CONFIG.timezone,'yyyy-MM-dd HH:mm:ss'),'']);
  writeTable_(book,'RINGKASAN',summary);
  console.log('CLEAN dan RINGKASAN diperbarui. Respons utama lengkap: '+included.length);
  return {total:records.length,included:included.length,paired:paired.length};
}

function normalizeRecord_(id,timestamp,a,s,review) {
  const validAges=['18–20 tahun','21–24 tahun','25–27 tahun','28–30 tahun'];
  let eligibility='ELIGIBLE';
  if(a.consent!=='Ya, saya bersedia')eligibility='NO_CONSENT';
  else if(validAges.indexOf(a.age)<0)eligibility='AGE_OUT_OR_UNKNOWN';
  else if(a.scope!=='Ya')eligibility='SCOPE_OUT_OR_UNKNOWN';
  const completed=!!a.recall;
  const phase=s.launchAt && timestamp.getTime()>=new Date(s.launchAt).getTime()?'MAIN':'BEFORE_START';
  const flags=[];
  if(a.paid_price && a.price_certainty==='Saya tidak tahu harganya')flags.push('PRICE_ENTERED_BUT_UNKNOWN');
  if(a.price_certainty==='Produk itu gratis' && a.paid_price && Number(a.paid_price)!==0)flags.push('FREE_WITH_NONZERO_PRICE');
  if(a.paid_price!==undefined && a.paid_price!=='' && Number(a.paid_price)>500000)flags.push('PRICE_REVIEW');
  if(a.price_certainty && /Saya ingat|Perkiraan/.test(a.price_certainty) && !a.paid_price)flags.push('PRICE_MISSING');
  if(Array.isArray(a.reasons)&&a.reasons.length>1&&a.reasons.indexOf('Saya tidak tahu / tidak ikut memutuskan')>=0)flags.push('REASONS_CONFLICT');
  if(a.acquired_month) {
    const match=/^(0[1-9]|1[0-2])\/(20[0-9]{2})$/.exec(a.acquired_month);
    if(!match)flags.push('MONTH_INVALID');
    else {
      const jakarta=new Date(timestamp.getTime()+7*60*60*1000);
      if(Number(match[2])*12+Number(match[1])>jakarta.getUTCFullYear()*12+jakarta.getUTCMonth()+1)flags.push('MONTH_IN_FUTURE');
    }
  }
  const tooth=deliberationValue_(a.tooth_deliberation),other=deliberationValue_(a.other_deliberation);
  const involved=['Saya sendiri','Saya bersama orang lain'];
  const comparable=a.comparison_gate==='Ya'&&involved.indexOf(a.chooser)>=0&&involved.indexOf(a.other_chooser)>=0&&tooth!==null&&other!==null;
  const currentHint=tierHint_(a.current_product),previousHint=tierHint_(a.previous_product);
  let pathway='UNREVIEWED';
  if(review) {
    const allowed=['BASIC','PREMIUM','OTHER','UNKNOWN'];
    if(allowed.indexOf(review.current)<0||allowed.indexOf(review.previous)<0)pathway='UNKNOWN';
    else if(review.current==='UNKNOWN'||review.previous==='UNKNOWN')pathway='UNKNOWN';
    else pathway=review.previous+' → '+review.current;
  }
  return {id:String(id),timestamp:timestamp,answers:a,eligibility:eligibility,completed:completed,phase:phase,
    included:eligibility==='ELIGIBLE'&&completed&&phase==='MAIN',flags:flags,currentHint:currentHint,
    previousHint:previousHint,pathway:pathway,comparable:comparable,toothCompared:tooth,otherCompared:other};
}
function deliberationValue_(value) {
  if(value==='Saya membandingkan beberapa produk sebelum memilih')return true;
  if(value==='Saya memilih tanpa membandingkan dengan produk lain')return false;
  return null;
}
function tierHint_(value) {
  const t=String(value||'').toLowerCase();
  if(!t||/tidak tahu|tidak ingat/.test(t))return 'UNKNOWN';
  if(!/pepsodent/.test(t))return 'OTHER_OR_UNCLEAR';
  if(/sensitive.*expert|sensitif.*expert|ultra\s*white/.test(t))return 'PREMIUM_CANDIDATE_ONLY';
  if(/pencegah gigi berlubang|anti\s*cavity|anticavity/.test(t))return 'BASIC_CANDIDATE_ONLY';
  return 'PEPSODENT_TIER_UNCLEAR';
}
function readReviews_(book) {
  const sheet=book.getSheetByName('REVIEW'),map={};
  if(!sheet||sheet.getLastRow()<2)return map;
  sheet.getRange(2,1,sheet.getLastRow()-1,4).getValues().forEach(function(row){
    if(row[0])map[String(row[0])]={current:String(row[1]).trim().toUpperCase(),previous:String(row[2]).trim().toUpperCase(),note:String(row[3])};
  });return map;
}
function cellAnswer_(value){return value===undefined||value===null?'':Array.isArray(value)?value.join(' | '):String(value);}
function safeCell_(value){
  if(value===undefined||value===null)return '';
  if(typeof value==='string'&&/^[\s]*[=+@-]/.test(value))return "'"+value;
  return value;
}
function writeTable_(book,name,rows) {
  const sheet=book.getSheetByName(name)||book.insertSheet(name);
  const columns=rows[0].length;
  if(sheet.getMaxColumns()<columns)sheet.insertColumnsAfter(sheet.getMaxColumns(),columns-sheet.getMaxColumns());
  if(sheet.getMaxRows()<rows.length)sheet.insertRowsAfter(sheet.getMaxRows(),rows.length-sheet.getMaxRows());
  sheet.clearContents();
  sheet.getRange(1,1,rows.length,columns).setValues(rows.map(function(row){return row.map(safeCell_);}));
  sheet.setFrozenRows(1);
  sheet.getRange(1,1,1,columns).setFontWeight('bold').setBackground('#163b35').setFontColor('#ffffff');
  sheet.setColumnWidths(1,columns,180);
  if(columns>1)sheet.setColumnWidth(1,290);
  sheet.getRange(1,1,rows.length,Math.min(columns,3)).setWrap(true);
}

/** Pure checks: no Google files or responses created. */
function runSelfChecks() {
  [mainSpecification_(),contactSpecification_()].forEach(function(pages){
    const codes={},ids={};pages.forEach(function(p){assert_(!ids[p.id],'Duplicate page');ids[p.id]=true;});
    pages.forEach(function(p,pi){let navigators=0;p.items.forEach(function(q){
      assert_(!codes[q.code],'Duplicate code '+q.code);codes[q.code]=true;
      assert_(q.title&&q.type,'Missing title/type');
      if(q.choices)assert_(new Set(q.choices).size===q.choices.length,'Duplicate option '+q.code);
      if(q.routes){navigators++;assert_(q.routes.length===q.choices.length,'Route count '+q.code);
        assert_(pi<pages.length-1,'Routing on final page has no effect');
        q.routes.forEach(function(target){assert_(target==='SUBMIT'||!!ids[target],'Unknown route '+target);
          if(target!=='SUBMIT')assert_(pages.findIndex(function(x){return x.id===target;})>pi,'Backwards route');});}
    });assert_(navigators<=1,'Multiple navigation questions on a page');});
  });
  const s={launchAt:'2026-11-04T00:00:00.000Z'};
  const a={consent:'Ya, saya bersedia',age:'21–24 tahun',scope:'Ya',recall:'Cukup yakin dengan sebagian besar jawaban'};
  assert_(normalizeRecord_('x',new Date('2026-11-04T01:00:00Z'),a,s).included,'Eligible main excluded');
  assert_(!normalizeRecord_('x',new Date('2026-11-03T01:00:00Z'),a,s).included,'Before-start response included');
  assert_(!normalizeRecord_('x',new Date('2026-11-04T01:00:00Z'),Object.assign({},a,{age:'Di bawah 18 tahun'}),s).included,'Minor included');
  assert_(!normalizeRecord_('x',new Date('2026-11-04T01:00:00Z'),Object.assign({},a,{recall:''}),s).included,'Incomplete included');
  assert_(tierHint_('Pepsodent')==='PEPSODENT_TIER_UNCLEAR','Brand-only tier guessed');
  assert_(safeCell_('=IMPORTXML("x","y")').charAt(0)==="'",'Formula injection guard');
  assert_(deliberationValue_('Saya tidak ikut memilih')===null,'Nonchooser compared');
  console.log('Self-checks passed. Main questions: '+questions_(mainSpecification_()).length);
  return true;
}
function assert_(condition,message){if(!condition)throw new Error('CHECK FAILED: '+message);}
function verifySurvey_() {
  runSelfChecks();const s=requireReady_();
  [{id:s.mainFormId,meta:s.mainMeta,spec:mainSpecification_()},
   {id:s.contactFormId,meta:s.contactMeta,spec:contactSpecification_()}].forEach(function(entry){
    const form=FormApp.openById(entry.id),items={};form.getItems().forEach(function(item){items[String(item.getId())]=item;});
    questions_(entry.spec).forEach(function(q){
      const item=items[String(entry.meta.items[q.code])];assert_(!!item,'Missing item '+q.code);
      const typed=q.type==='mc'?item.asMultipleChoiceItem():q.type==='checks'?item.asCheckboxItem():
        q.type==='text'?item.asTextItem():item.asParagraphTextItem();
      assert_(typed.getTitle()===q.title,'Question was edited: '+q.code+'. Review script and form together.');
      assert_(typed.isRequired()===q.required,'Required setting changed: '+q.code);
      if(q.choices){const choices=typed.getChoices();
        assert_(JSON.stringify(choices.map(function(c){return c.getValue();}))===JSON.stringify(q.choices),'Choices changed: '+q.code);
        if(q.routes)choices.forEach(function(choice,index){
          const target=q.routes[index];
          if(target==='SUBMIT')assert_(choice.getPageNavigationType()===FormApp.PageNavigationType.SUBMIT,'Submit route changed');
          else assert_(choice.getGotoPage()&&String(choice.getGotoPage().getId())===String(entry.meta.pages[target]),'Page route changed: '+q.code);
        });
      }
    });
    assert_(!form.collectsEmail(),'Email collection is enabled');
    assert_(!form.hasLimitOneResponsePerUser(),'Login-based response limit is enabled');
    assert_(!form.isPublishingSummary(),'Public response summary is enabled');
  });
  console.log('Form structure and all branch choices passed verification. Test responder access in an incognito window.');
  return true;
}

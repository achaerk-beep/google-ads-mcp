const {chromium}=require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs'),path=require('path');
(async()=>{const b=await chromium.launch();const out=process.argv[2];
for(const f of fs.readdirSync('.').filter(f=>f.endsWith('.html')).sort()){
 const [w,h]=f.match(/_(\d+)x(\d+)/).slice(1).map(Number);
 const p=await b.newPage({viewport:{width:w,height:h}});
 await p.goto('file://'+path.resolve(f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
 await p.screenshot({path:path.join(out,f.replace('.html','.jpg')),type:'jpeg',quality:90});await p.close();}
await b.close();})();

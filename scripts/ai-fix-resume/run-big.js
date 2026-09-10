const fs=require('fs'),path=require('path');const SP=__dirname;
const slugs=JSON.parse(fs.readFileSync(path.join(SP,'batch-big.json'),'utf8'));
(async()=>{
  const out=[];
  for(let i=0;i<slugs.length;i++){
    const s=slugs[i];const t0=Date.now();
    try{
      const r=await fetch('https://us-central1-calctowork.cloudfunctions.net/aiFixCalcHttp',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({slug:s,targeted:true})});
      const j=await r.json();const e=j.engine||{};
      const comp=e.compute?(e.compute.ok===true?'OK':e.compute.ok===false?'FAIL':'-'):'-';
      console.log(`${i+1}/${slugs.length} ${s}: ui=${j.uiWrote||0} rc=${j.rcWrote||0} art=${j.contentLangs||0} math=${comp} pf=${e.presetsFixed||0} interp=${e.hasInterpretation?1:0}${j.error?' ERR:'+j.error:''} (${((Date.now()-t0)/1000).toFixed(0)}s)`);
      out.push({slug:s,ui:j.uiWrote,rc:j.rcWrote,art:j.contentLangs,compute:e.compute,presetsFixed:e.presetsFixed,genericUnits:e.genericUnits,hasInterpretation:e.hasInterpretation,error:j.error});
    }catch(err){ console.log(`${i+1}/${slugs.length} ${s}: REQ FAIL ${err.message}`); out.push({slug:s,error:err.message}); }
  }
  fs.writeFileSync(path.join(SP,'run-big-result.json'),JSON.stringify(out,null,1));
  const mf=out.filter(x=>x.compute&&x.compute.ok===false);
  const gu=out.filter(x=>(x.genericUnits||[]).length);
  const ni=out.filter(x=>x.hasInterpretation===false).length;
  const rf=out.filter(x=>x.error).length;
  console.log('\n=== SUMMARY total',out.length,'| req-fail',rf,'| presets-fixed',out.reduce((a,x)=>a+(x.presetsFixed||0),0));
  console.log('MATH FAIL:',mf.map(x=>x.slug).join(', ')||'none');
  console.log('GENERIC units:',gu.length,'| NO interpretation:',ni);
})();

// Autonomous "finish all" runner: walks the full slug list, POSTs aiFixCalcHttp
// targeted for each (already-clean ones skip fast), checkpoints progress so it can
// resume, and retries errored calcs in extra passes until none remain.
const fs = require('fs');
const DIR = 'C:/Microsaas/obra/scripts/ai-fix-resume';
const EP = 'https://us-central1-calctowork.cloudfunctions.net/aiFixCalcHttp';
const all = JSON.parse(fs.readFileSync(DIR + '/allslugs.json', 'utf8'));

const CKPT = DIR + '/checkpoint.json';
let done = {};
try { done = JSON.parse(fs.readFileSync(CKPT, 'utf8')); } catch (e) { done = {}; }

async function fix(slug) {
  for (let attempt = 0; attempt < 2; attempt++) {
    try {
      const r = await fetch(EP, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ slug, targeted: true }) });
      const j = await r.json();
      return j;
    } catch (e) { if (attempt === 1) return { ok: false, error: e.message }; await new Promise(r => setTimeout(r, 3000)); }
  }
}

(async () => {
  let n = 0;
  for (const slug of all) {
    n++;
    if (done[slug] && done[slug].ok && !done[slug].error) continue; // already completed OK
    const t0 = Date.now();
    const j = await fix(slug);
    const e = (j && j.engine) || {};
    const rec = {
      ok: !!(j && j.ok), error: j && j.error,
      ui: j && j.uiWrote, rc: j && j.rcWrote, art: j && j.contentLangs,
      math: e.compute ? e.compute.ok : null, mathMsg: e.compute && e.compute.msg,
      presetsFixed: e.presetsFixed, genericUnits: e.genericUnits, hasInterp: e.hasInterpretation,
      at: new Date().toISOString()
    };
    done[slug] = rec;
    fs.writeFileSync(CKPT, JSON.stringify(done));
    const mathTag = rec.math === false ? ' MATH=FAIL(' + rec.mathMsg + ')' : '';
    console.log(`${n}/${all.length} ${slug}: ok=${rec.ok ? 1 : 0} ui=${rec.ui || 0} rc=${rec.rc || 0} art=${rec.art || 0} pf=${rec.presetsFixed || 0}${rec.error ? ' ERR:' + rec.error : ''}${mathTag} (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
  }
  // retry passes for any errored
  for (let pass = 0; pass < 3; pass++) {
    const errored = all.filter(s => !done[s] || !done[s].ok || done[s].error);
    if (!errored.length) break;
    console.log(`\n--- retry pass ${pass + 1}: ${errored.length} errored ---`);
    for (const slug of errored) {
      const j = await fix(slug); const e = (j && j.engine) || {};
      done[slug] = { ok: !!(j && j.ok), error: j && j.error, math: e.compute ? e.compute.ok : null, mathMsg: e.compute && e.compute.msg, at: new Date().toISOString() };
      fs.writeFileSync(CKPT, JSON.stringify(done));
      console.log(`  retry ${slug}: ok=${done[slug].ok ? 1 : 0}${done[slug].error ? ' ERR:' + done[slug].error : ''}`);
    }
  }
  const okCount = all.filter(s => done[s] && done[s].ok && !done[s].error).length;
  const mathFails = all.filter(s => done[s] && done[s].math === false);
  const stillErr = all.filter(s => !done[s] || !done[s].ok || done[s].error);
  console.log('\n=== FINISHED ===');
  console.log('ok:', okCount, '/', all.length, '| still errored:', stillErr.length);
  console.log('MATH=FAIL:', mathFails.join(', ') || 'none');
  if (stillErr.length) console.log('STILL ERRORED:', stillErr.join(', '));
})();

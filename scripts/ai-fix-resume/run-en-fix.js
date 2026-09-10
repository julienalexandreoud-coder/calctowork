// Repair the ENGLISH canonical (raw-id labels, generic templated descriptions) and let the
// other 5 languages retranslate from it. content:false keeps it fast (skips article regen).
const fs = require('fs');
const DIR = 'C:/Microsaas/obra/scripts/ai-fix-resume';
const EP = 'https://us-central1-calctowork.cloudfunctions.net/aiFixCalcHttp';
const list = JSON.parse(fs.readFileSync(DIR + '/en-fix-list.json', 'utf8'));
const CK = DIR + '/en-fix-checkpoint.json';
let done = {}; try { done = JSON.parse(fs.readFileSync(CK, 'utf8')); } catch (e) {}

(async () => {
  let enTotal = 0, uiTotal = 0;
  for (let i = 0; i < list.length; i++) {
    const slug = list[i];
    if (done[slug] && done[slug].ok) continue;
    const t0 = Date.now();
    let j;
    try {
      const r = await fetch(EP, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ slug, targeted: true, content: false }) });
      j = await r.json();
    } catch (e) { console.log(`${i + 1}/${list.length} ${slug}: REQ FAIL ${e.message}`); continue; }
    done[slug] = { ok: !!j.ok, enFixed: j.enFixed, ui: j.uiWrote, err: j.error, at: new Date().toISOString() };
    fs.writeFileSync(CK, JSON.stringify(done));
    enTotal += (j.enFixed || 0); uiTotal += (j.uiWrote || 0);
    console.log(`${i + 1}/${list.length} ${slug}: en=${j.enFixed || 0} ui=${j.uiWrote || 0} rc=${j.rcWrote || 0} dep=${j.deployed ? 1 : 0}${j.error ? ' ERR:' + j.error : ''} (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
  }
  const okN = list.filter(s => done[s] && done[s].ok).length;
  console.log(`\n=== EN FIX DONE === ${okN}/${list.length} ok | english fields fixed: ${enTotal} | language label sets: ${uiTotal}`);
})();

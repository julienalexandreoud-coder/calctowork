// Give every calculator a real reading of the user's result via genInterpretationHttp.
// The endpoint validates before writing (bands ordered and covering the scale, every
// shipped preset landing inside it, no hardcoded numbers in an insight), so a calc it
// cannot do well is left exactly as it was and reported here.
//
// republish:false — a per-calc deploy clones the whole ~22k-file manifest, so we sweep
// once at the end with sweep-robust.js.
const fs = require('fs');
const DIR = __dirname;
const EP = 'https://us-central1-calctowork.cloudfunctions.net/genInterpretationHttp';
const LIST = process.argv[2] || DIR + '/allslugs.json';
const CK = DIR + '/interp-checkpoint.json';
const FORCE = process.argv.includes('--force');

const list = JSON.parse(fs.readFileSync(LIST, 'utf8'));
let done = {};
try { done = JSON.parse(fs.readFileSync(CK, 'utf8')); } catch (e) {}

const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  let bands = 0, insight = 0, fail = 0, skip = 0;
  for (let i = 0; i < list.length; i++) {
    const slug = list[i];
    if (done[slug] && done[slug].ok && !FORCE) { if (done[slug].mode === 'bands') bands++; else insight++; continue; }
    const t0 = Date.now();
    let j;
    try {
      const ctl = new AbortController();
      const timer = setTimeout(() => ctl.abort(), 540000);
      try {
        const r = await fetch(EP, {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ slug, republish: false, force: FORCE }),
          signal: ctl.signal,
        });
        j = await r.json();
      } finally { clearTimeout(timer); }
    } catch (e) {
      console.log(`${i + 1}/${list.length} ${slug}: REQ FAIL ${e.message}`);
      fail++; await sleep(3000); continue;
    }
    done[slug] = { ok: !!j.ok, mode: j.mode, skipped: j.skipped, err: j.error || j.detail, at: new Date().toISOString() };
    fs.writeFileSync(CK, JSON.stringify(done));
    const secs = ((Date.now() - t0) / 1000).toFixed(0);
    if (j.skipped) { skip++; console.log(`${i + 1}/${list.length} ${slug}: already had one (${secs}s)`); continue; }
    if (!j.ok) { fail++; console.log(`${i + 1}/${list.length} ${slug}: FAIL ${String(j.detail || j.error).slice(0, 95)} (${secs}s)`); continue; }
    if (j.mode === 'bands') { bands++; console.log(`${i + 1}/${list.length} ${slug}: BANDS [${(j.bands || []).join(' / ')}] (${secs}s)`); }
    else { insight++; console.log(`${i + 1}/${list.length} ${slug}: INSIGHT ${String(j.insight).slice(0, 90)} (${secs}s)`); }
  }
  console.log(`\n=== INTERPRETATIONS DONE === bands:${bands} insight:${insight} skipped:${skip} failed:${fail}`);
  const failed = Object.entries(done).filter(([, v]) => !v.ok && !v.skipped).map(([k]) => k);
  if (failed.length) {
    fs.writeFileSync(DIR + '/interp-failed.json', JSON.stringify(failed, null, 1));
    console.log(`failed slugs -> interp-failed.json (${failed.length})`);
  }
})();

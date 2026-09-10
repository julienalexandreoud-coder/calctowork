// Regenerate meaningless example presets (size tiers, "Caso N", all-zero rows, rows that
// break the formula) and fill in missing defaults, via the validated regenPresetsHttp
// endpoint. Nothing is written unless the generated scenarios actually compute.
//
// republish:false here — a per-calc deploy clones the whole ~22k-file hosting manifest,
// so we batch the republish once at the end with sweep-republish.js.
const fs = require('fs');
const DIR = __dirname;
const EP = 'https://us-central1-calctowork.cloudfunctions.net/regenPresetsHttp';
const LIST = process.argv[2] || DIR + '/preset-fix-list.json';
const CK = DIR + '/preset-checkpoint.json';

const list = JSON.parse(fs.readFileSync(LIST, 'utf8'));
let done = {};
try { done = JSON.parse(fs.readFileSync(CK, 'utf8')); } catch (e) {}

(async () => {
  let ok = 0, fail = 0, presets = 0, defs = 0;
  for (let i = 0; i < list.length; i++) {
    const slug = list[i];
    if (done[slug] && done[slug].ok) { ok++; continue; }
    const t0 = Date.now();
    let j;
    try {
      const r = await fetch(EP, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ slug, republish: false }),
      });
      j = await r.json();
    } catch (e) {
      console.log(`${i + 1}/${list.length} ${slug}: REQ FAIL ${e.message}`);
      done[slug] = { ok: false, err: 'req: ' + e.message };
      fs.writeFileSync(CK, JSON.stringify(done));
      fail++; continue;
    }
    done[slug] = { ok: !!j.ok, presets: j.presets, defaults: j.defaultsWritten, labels: j.labels, err: j.error, at: new Date().toISOString() };
    fs.writeFileSync(CK, JSON.stringify(done));
    if (j.ok) { ok++; presets += j.presets || 0; defs += j.defaultsWritten ? 1 : 0; }
    else fail++;
    const secs = ((Date.now() - t0) / 1000).toFixed(0);
    console.log(`${i + 1}/${list.length} ${slug}: ${j.ok ? `OK ${j.presets}p${j.defaultsWritten ? ' +defaults' : ''} [${(j.labels || []).slice(0, 3).join(' / ')}]` : 'FAIL ' + String(j.error || '').slice(0, 90)} (${secs}s)`);
  }
  console.log(`\n=== PRESETS DONE === ok:${ok} fail:${fail} | presets written:${presets} | calcs given defaults:${defs}`);
  const failed = Object.entries(done).filter(([, v]) => !v.ok).map(([k]) => k);
  if (failed.length) {
    fs.writeFileSync(DIR + '/preset-failed.json', JSON.stringify(failed, null, 1));
    console.log(`failed slugs -> preset-failed.json (${failed.length})`);
  }
})();

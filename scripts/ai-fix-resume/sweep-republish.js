// Republish every calc so the corrected static data (unit_category + de-mojibaked labels)
// reaches the live pages. deployAllCalcsHttp processes ~25 per call; loop until done.
const EP = 'https://us-central1-calctowork.cloudfunctions.net/deployAllCalcsHttp';
(async () => {
  let n = 0, totalCalcs = 0, totalFiles = 0;
  for (let i = 0; i < 60; i++) {
    let j;
    try {
      const r = await fetch(EP, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({}) });
      j = await r.json();
    } catch (e) { console.log('batch ' + (++n) + ': REQ FAIL ' + e.message); await new Promise(r => setTimeout(r, 5000)); continue; }
    n++;
    totalCalcs += (j.deployed_calcs || 0); totalFiles += (j.total_files || 0);
    console.log(`batch ${n}: scanned=${j.scanned} calcs=${j.deployed_calcs} files=${j.total_files} done=${j.done}${j.error ? ' ERR:' + j.error : ''}`);
    if (j.done) break;
  }
  console.log(`\n=== SWEEP FINISHED === batches=${n} calcs republished=${totalCalcs} files=${totalFiles}`);
})();

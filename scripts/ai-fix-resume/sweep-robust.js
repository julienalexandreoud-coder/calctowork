// Republish every calc. deployAllCalcsHttp processes ~25 per call and tracks its own
// cursor, so this is resumable and idempotent.
//
// Each call clones the full ~22k-file hosting manifest, so under back-to-back calls the
// function sometimes exceeds the socket timeout. The plain loop treated that as fatal;
// this one uses an explicit per-request timeout, exponential backoff, and a short pause
// between batches, and only gives up after several CONSECUTIVE failures.
const EP = 'https://us-central1-calctowork.cloudfunctions.net/deployAllCalcsHttp';
const REQ_TIMEOUT_MS = 540000;
const PAUSE_MS = 4000;
const MAX_CONSEC_FAIL = 6;

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function callBatch() {
  const ctl = new AbortController();
  const timer = setTimeout(() => ctl.abort(), REQ_TIMEOUT_MS);
  try {
    const r = await fetch(EP, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({}),
      signal: ctl.signal,
    });
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return await r.json();
  } finally { clearTimeout(timer); }
}

(async () => {
  let n = 0, calcs = 0, files = 0, consec = 0, fails = 0;
  for (let i = 0; i < 120; i++) {
    let j;
    try {
      j = await callBatch();
      consec = 0;
    } catch (e) {
      consec++; fails++;
      const backoff = Math.min(60000, 5000 * Math.pow(2, consec - 1));
      console.log(`batch ${n + 1}: FAIL (${e.message}) — consecutive ${consec}/${MAX_CONSEC_FAIL}, retrying in ${backoff / 1000}s`);
      if (consec >= MAX_CONSEC_FAIL) { console.log('giving up: too many consecutive failures'); break; }
      await sleep(backoff);
      continue;
    }
    n++;
    calcs += (j.deployed_calcs || 0);
    files += (j.total_files || 0);
    console.log(`batch ${n}: scanned=${j.scanned} calcs=${j.deployed_calcs} files=${j.total_files} done=${j.done}${j.error ? ' ERR:' + j.error : ''}`);
    if (j.done) break;
    await sleep(PAUSE_MS);
  }
  console.log(`\n=== SWEEP FINISHED === batches=${n} calcs=${calcs} files=${files} transient_failures=${fails}`);
})();

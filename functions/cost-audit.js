/**
 * costAuditHttp — read real usage from Cloud Monitoring using the project's own
 * service account.
 *
 * Written because the billing console needs an interactive Google login, which
 * is not available from here. Monitoring exposes the same underlying usage that
 * billing charges for, so it answers "which service is actually burning money"
 * without a password. Read-only.
 *
 * GET (optional ?days=30)
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const MON = "https://monitoring.googleapis.com/v3";

// [label, metric type, how to summarise]
//   delta  = per-interval counter, we want the total over the window
//   gauge  = point-in-time level, we want the most recent value
const METRICS = [
  ["function invocations",      "cloudfunctions.googleapis.com/function/execution_count",   "delta"],
  ["function CPU (GB-seconds)", "cloudfunctions.googleapis.com/function/user_memory_bytes", "gauge"],
  ["firestore reads",           "firestore.googleapis.com/document/read_count",             "delta"],
  ["firestore writes",          "firestore.googleapis.com/document/write_count",            "delta"],
  ["firestore deletes",         "firestore.googleapis.com/document/delete_count",           "delta"],
  ["hosting bytes sent",        "firebasehosting.googleapis.com/network/sent_bytes_count",  "delta"],
  ["GCS bucket size (bytes)",   "storage.googleapis.com/storage/total_bytes",               "gauge"],
  ["GCS object count",          "storage.googleapis.com/storage/object_count",              "gauge"],
];

async function fetchSeries(token, project, metricType, days) {
  const end = new Date();
  const start = new Date(Date.now() - days * 86400000);
  const params = new URLSearchParams({
    "filter": `metric.type="${metricType}"`,
    "interval.startTime": start.toISOString(),
    "interval.endTime": end.toISOString(),
    "aggregation.alignmentPeriod": "86400s",
    "aggregation.perSeriesAligner": "ALIGN_SUM",
    "view": "FULL",
  });
  const url = `${MON}/projects/${project}/timeSeries?${params.toString()}`;
  const r = await fetch(url, { headers: { Authorization: "Bearer " + token } });
  if (!r.ok) return { error: `${r.status} ${(await r.text()).slice(0, 200)}` };
  return await r.json();
}

function summarise(json, mode) {
  const series = (json && json.timeSeries) || [];
  const rows = [];
  let grand = 0;
  for (const s of series) {
    const pts = s.points || [];
    const vals = pts.map(p => {
      const v = p.value || {};
      return Number(v.int64Value != null ? v.int64Value : (v.doubleValue != null ? v.doubleValue : 0));
    });
    if (!vals.length) continue;
    // delta: total across the window. gauge: newest point (points are newest-first).
    const amount = mode === "delta" ? vals.reduce((a, b) => a + b, 0) : vals[0];
    const labels = Object.assign({}, s.resource && s.resource.labels, s.metric && s.metric.labels);
    const name = labels.function_name || labels.bucket_name || labels.service || labels.module_id || "(all)";
    rows.push({ name, amount });
    grand += amount;
  }
  // Collapse duplicate names, biggest first, keep the long tail out of the way.
  const byName = {};
  rows.forEach(r => { byName[r.name] = (byName[r.name] || 0) + r.amount; });
  const top = Object.entries(byName).sort((a, b) => b[1] - a[1]).slice(0, 15)
    .map(([name, amount]) => ({ name, amount: Math.round(amount) }));
  return { total: Math.round(grand), top };
}

exports.costAuditHttp = functions.runWith({ timeoutSeconds: 300, memory: "256MB" })
  .https.onRequest(async (req, res) => {
    res.set("Access-Control-Allow-Origin", "*");
    try {
      const days = Math.min(60, parseInt(req.query.days, 10) || 30);
      const project = process.env.GCLOUD_PROJECT || process.env.GCP_PROJECT || "calctowork";
      const tokenResult = await admin.app().options.credential.getAccessToken();
      const token = tokenResult.access_token;

      const out = {};
      for (const [label, type, mode] of METRICS) {
        try {
          const json = await fetchSeries(token, project, type, days);
          if (json.error) { out[label] = { error: json.error }; continue; }
          out[label] = summarise(json, mode);
        } catch (e) {
          out[label] = { error: e.message };
        }
      }

      return res.status(200).json({ project, windowDays: days, usage: out });
    } catch (e) {
      console.error("costAuditHttp error:", e);
      return res.status(500).json({ error: e.message });
    }
  });

/**
 * trafficSourcesHttp — read the daily source/browser/device rollup.
 *
 * Exists to answer "where do ~50 visitors a day come from when Google sends
 * ~1 click a day". analytics_daily_sources is written by the aggregator and
 * counts by UNIQUE SESSION, so it is not inflated by per-event rows.
 * GET ?days=14
 */
exports.trafficSourcesHttp = functions.runWith({ timeoutSeconds: 120, memory: "256MB" })
  .https.onRequest(async (req, res) => {
    res.set("Access-Control-Allow-Origin", "*");
    try {
      const days = Math.min(60, parseInt(req.query.days, 10) || 14);
      const start = new Date(Date.now() - days * 86400000).toISOString().slice(0, 10);
      const db = admin.firestore();
      const snap = await db.collection("analytics_daily_sources")
        .where(admin.firestore.FieldPath.documentId(), ">=", start)
        .get();
      const rows = [];
      snap.forEach(d => rows.push({ date: d.id, ...d.data() }));
      rows.sort((a, b) => a.date.localeCompare(b.date));
      return res.status(200).json({ days, count: rows.length, rows });
    } catch (e) {
      console.error("trafficSourcesHttp:", e);
      return res.status(500).json({ error: e.message });
    }
  });

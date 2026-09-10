/**
 * CalcToWork — Analytics Aggregator
 * Scheduled Firebase Function: aggregates raw analytics_events into daily summaries
 * Runs daily at 2 AM UTC
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const db = admin.firestore();

/**
 * Aggregate raw events into daily calculator-level summaries
 */
/**
 * Aggregate raw events into daily calculator-level summaries for ONE date.
 * Shared by the nightly cron and the on-demand endpoint so "today" can be refreshed
 * without waiting for 02:00 — the dashboard previously had no way to see the current
 * day at all, because the cron only ever aggregates yesterday.
 */
async function aggregateForDate(dateStr) {
  const startOfDay = new Date(dateStr + "T00:00:00.000Z");
  const endOfDay = new Date(startOfDay.getTime() + 86400000);

  console.log("[Aggregator] Running for " + dateStr);

  let allEvents = [];
  let lastDoc = null;
  let hasMore = true;
  while (hasMore) {
    let q = db.collection("analytics_events")
      .where("event_time", ">=", admin.firestore.Timestamp.fromDate(startOfDay))
      .where("event_time", "<", admin.firestore.Timestamp.fromDate(endOfDay))
      .orderBy("event_time", "asc")
      .limit(500);
    if (lastDoc) q = q.startAfter(lastDoc);
    const snap = await q.get();
    if (snap.empty) { hasMore = false; break; }
    snap.forEach(doc => { allEvents.push({ id: doc.id, ...doc.data() }); });
    lastDoc = snap.docs[snap.docs.length - 1];
  }
  console.log("[Aggregator] Total events: " + allEvents.length);

  const stats = {};
  allEvents.forEach(e => {
    const slug = e.calc_slug || "unknown";
    const lang = e.language || "unknown";
    const key = slug + "|" + lang;
    if (!stats[key]) {
      stats[key] = { slug, lang, views: 0, calcs: 0, copies: 0, shares: 0, times: [], users: new Set(), sessions: new Set(), sessionEvents: {} };
    }
    const st = stats[key];
    if (e.user_id) st.users.add(e.user_id);
    if (e.session_id) {
      st.sessions.add(e.session_id);
      if (!st.sessionEvents[e.session_id]) st.sessionEvents[e.session_id] = [];
      st.sessionEvents[e.session_id].push(e.event_name);
    }
    if (e.event_name === "page_view") st.views++;
    if (e.event_name === "calculation_completed") st.calcs++;
    if (e.event_name === "copy_results") st.copies++;
    if (e.event_name === "share_clicked") st.shares++;
    if (e.seconds) st.times.push(e.seconds);
  });

  // ── Traffic sources, browsers and devices, counted by unique session ──
  const srcSessions = {}, browserSessions = {}, deviceSessions = {}, seenSession = {};
  allEvents.forEach(e => {
    const sid = e.session_id;
    if (!sid || seenSession[sid]) return;
    seenSession[sid] = 1;                       // first event of the session decides
    const src = e.traffic_source || 'unknown';
    const br = e.browser || 'unknown';
    const dv = e.device_type || 'unknown';
    srcSessions[src] = (srcSessions[src] || 0) + 1;
    browserSessions[br] = (browserSessions[br] || 0) + 1;
    deviceSessions[dv] = (deviceSessions[dv] || 0) + 1;
  });
  // True site-wide counts. Summing the per-calculator analytics_daily rows
  // double-counts anyone who opened more than one calculator.
  const allUsers = new Set();
  allEvents.forEach(e => { if (e.user_id) allUsers.add(e.user_id); });

  await db.collection("analytics_daily_sources").doc(dateStr).set({
    date: dateStr,
    sessions: Object.keys(seenSession).length,
    unique_users_total: allUsers.size,
    page_views_total: allEvents.filter(e => e.event_name === "page_view").length,
    sources: srcSessions,
    browsers: browserSessions,
    devices: deviceSessions,
    updated_at: admin.firestore.FieldValue.serverTimestamp(),
  });

  let batch = db.batch();
  let count = 0, pending = 0;
  for (const st of Object.values(stats)) {
    let bounced = 0;
    Object.values(st.sessionEvents).forEach(evts => {
      const hasInteraction = evts.some(en =>
        en === "calculation_completed" || en === "copy_results" || en === "share_clicked" ||
        en === "scroll_depth" || en === "input_changed");
      if (!hasInteraction) bounced++;
    });
    const avgTime = st.times.length > 0 ? Math.round(st.times.reduce((x, y) => x + y, 0) / st.times.length) : 0;
    const docId = dateStr + "_" + st.slug.replace(/[\/\.\#\$\[\]]/g, "_") + "_" + st.lang;
    batch.set(db.collection("analytics_daily").doc(docId), {
      date: dateStr,
      calculator_slug: st.slug,
      language: st.lang,
      page_views: st.views,
      calculations: st.calcs,
      copies: st.copies,
      shares: st.shares,
      avg_time_seconds: avgTime,
      unique_users: st.users.size,
      sessions: st.sessions.size,
      bounced_sessions: bounced,
      bounce_rate: st.sessions.size > 0 ? +(bounced / st.sessions.size * 100).toFixed(1) : 0,
      conversion_rate: st.views > 0 ? +((st.calcs / st.views) * 100).toFixed(1) : 0,
      created_at: admin.firestore.FieldValue.serverTimestamp(),
    });
    count++; pending++;
    // Commit in chunks, and AWAIT it — the previous version fired .then() without
    // awaiting and then reused the same batch, so large days could lose writes.
    if (pending === 450) { await batch.commit(); batch = db.batch(); pending = 0; }
  }
  if (pending > 0) await batch.commit();

  const totals = Object.values(stats).reduce((t, st) => ({
    page_views: t.page_views + st.views,
    calculations: t.calculations + st.calcs,
    sessions: t.sessions + st.sessions.size,
  }), { page_views: 0, calculations: 0, sessions: 0 });

  console.log("[Aggregator] Done. " + count + " rows for " + dateStr);
  return { date: dateStr, rows: count, events: allEvents.length, ...totals, unique_users_total: allUsers.size, sources: srcSessions, browsers: browserSessions, devices: deviceSessions };
}

exports.aggregateDailyStats = functions
  .runWith({ timeoutSeconds: 540, memory: "512MB" })
  .pubsub
  .schedule("0 2 * * *")
  .timeZone("UTC")
  .onRun(async () => {
    const dateStr = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
    await aggregateForDate(dateStr);
    return null;
  });

/**
 * Refresh today (or any given date) on demand, so the dashboard is not a day behind.
 * POST { date?: "YYYY-MM-DD" } — defaults to TODAY.
 */
exports.aggregateOnDemand = functions
  .runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") {
    res.set("Access-Control-Allow-Methods", "POST");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    return res.status(204).send("");
  }
  try {
    const date = (req.body && req.body.date) || new Date().toISOString().slice(0, 10);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return res.status(400).json({ error: "date must be YYYY-MM-DD" });
    const result = await aggregateForDate(date);
    return res.status(200).json({ ok: true, ...result });
  } catch (e) {
    console.error("[Aggregator] on-demand failed:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Get aggregated daily data for the dashboard
 */
exports.getAggregatedData = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") {
    res.set("Access-Control-Allow-Methods", "GET");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    return res.status(204).send("");
  }

  try {
    const days = parseInt(req.query.days) || 30;
    const startDate = new Date(Date.now() - days * 86400000).toISOString().slice(0, 10);

    const snap = await db.collection("analytics_daily")
      .where("date", ">=", startDate)
      .orderBy("date", "desc")
      .limit(parseInt(req.query.limit) || 5000)
      .get();

    const rows = [];
    snap.forEach(doc => rows.push(doc.data()));
    return res.status(200).json(rows);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

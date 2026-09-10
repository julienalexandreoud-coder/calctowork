/**
 * Bing Webmaster Tools Data Collector
 * Fetches site stats, keywords, and page data from Bing Webmaster API.
 * Uses API key stored in functions.config().bing.key or BING_API_KEY env var.
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");
const db = admin.firestore();

const BING_API = "https://ssl.bing.com/webmaster/api/api";

function bingKey() {
  return (functions.config().bing && functions.config().bing.key) || process.env.BING_API_KEY || "";
}

function bingSiteUrl() {
  return (functions.config().bing && functions.config().bing.site_url) || "https://calcto.work";
}

/**
 * Fetch Bing site stats for a date range
 */
async function fetchBingStats(siteUrl, startDate, endDate) {
  const key = bingKey();
  if (!key) throw new Error("No Bing API key configured. Set functions.config().bing.key");
  
  const fetch = require("node-fetch");
  const url = `${BING_API}/GetSiteStats?siteUrl=${encodeURIComponent(siteUrl)}&startDate=${startDate}&endDate=${endDate}`;
  const r = await fetch(url, { headers: { "Content-Type": "application/json", "ApiKey": key }, timeout: 15000 });
  if (!r.ok) throw new Error(`Bing API error: ${r.status}`);
  return await r.json();
}

/**
 * Fetch Bing keywords for a date range
 */
async function fetchBingKeywords(siteUrl, startDate, endDate, limit = 200) {
  const key = bingKey();
  if (!key) throw new Error("No Bing API key configured");
  
  const fetch = require("node-fetch");
  const url = `${BING_API}/GetQueryStats?siteUrl=${encodeURIComponent(siteUrl)}&startDate=${startDate}&endDate=${endDate}&rowLimit=${limit}`;
  const r = await fetch(url, { headers: { "Content-Type": "application/json", "ApiKey": key }, timeout: 15000 });
  if (!r.ok) throw new Error(`Bing API error: ${r.status}`);
  return await r.json();
}

/**
 * Scheduled: fetch Bing data daily at 4 AM UTC
 */
exports.fetchBingData = functions.runWith({ timeoutSeconds: 300, memory: "256MB" })
  .pubsub.schedule("0 4 * * *").timeZone("UTC").onRun(async () => {
  const key = bingKey();
  if (!key) { console.log("[Bing] No API key — skipping"); return { skipped: true, reason: "no_key" }; }

  const siteUrl = bingSiteUrl();
  const today = new Date();
  const endDate = new Date(today - 3 * 86400000).toISOString().slice(0, 10);
  const startDate = new Date(today - 33 * 86400000).toISOString().slice(0, 10);

  console.log(`[Bing] Fetching ${startDate} to ${endDate}`);

  try {
    // 1. Site stats
    const stats = await fetchBingStats(siteUrl, startDate, endDate);
    if (stats && stats.SiteStatsList && stats.SiteStatsList.SiteStats) {
      const batch = db.batch();
      const siteStats = Array.isArray(stats.SiteStatsList.SiteStats) 
        ? stats.SiteStatsList.SiteStats 
        : [stats.SiteStatsList.SiteStats];
      
      for (const s of siteStats) {
        const date = s.Date;
        if (!date || date < "2020-01-01") continue;
        const ref = db.collection("bing_site_stats").doc(date);
        batch.set(ref, {
          date,
          site_url: siteUrl,
          clicks: s.Clicks || 0,
          impressions: s.Impressions || 0,
          ctr: s.CTR || 0,
          avg_position: s.AvgPosition || 0,
          pages_indexed: s.PagesIndexed || 0,
          pages_crawled: s.PagesCrawled || 0,
          fetched_at: admin.firestore.FieldValue.serverTimestamp(),
        });
      }
      await batch.commit();
      console.log(`[Bing] Stored ${siteStats.length} daily stats`);
    }

    // 2. Keyword data
    const keywords = await fetchBingKeywords(siteUrl, startDate, endDate, 200);
    if (keywords && keywords.QueryStatsList && keywords.QueryStatsList.QueryStats) {
      const batch = db.batch();
      const queries = Array.isArray(keywords.QueryStatsList.QueryStats) 
        ? keywords.QueryStatsList.QueryStats 
        : [keywords.QueryStatsList.QueryStats];
      
      for (const q of queries) {
        const docId = `${endDate}_${(q.Query || "unknown").replace(/[\/\.\#\$\[\]]/g, "_")}`;
        const ref = db.collection("bing_queries").doc(docId);
        batch.set(ref, {
          date: endDate,
          query: q.Query || "",
          clicks: q.Clicks || 0,
          impressions: q.Impressions || 0,
          ctr: q.CTR || 0,
          avg_position: q.AvgPosition || 0,
          site_url: siteUrl,
          fetched_at: admin.firestore.FieldValue.serverTimestamp(),
        });
      }
      await batch.commit();
      console.log(`[Bing] Stored ${queries.length} keywords`);
    }

    console.log("[Bing] Collection complete");
    return { stats: (stats && stats.SiteStatsList && stats.SiteStatsList.SiteStats) ? 
      (Array.isArray(stats.SiteStatsList.SiteStats) ? stats.SiteStatsList.SiteStats.length : 1) : 0 };
  } catch(e) {
    console.error("[Bing] Error:", e.message);
    throw e;
  }
});

/**
 * Get Bing data endpoint for dashboard
 */
exports.getBingData = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") { res.set("Access-Control-Allow-Methods", "GET"); return res.status(204).send(""); }

  try {
    const type = req.query.type || "stats";
    const days = parseInt(req.query.days) || 30;
    const cutoff = new Date(Date.now() - days * 86400000).toISOString().slice(0, 10);

    if (type === "stats") {
      const snap = await db.collection("bing_site_stats").where("date", ">=", cutoff).orderBy("date", "asc").get();
      const rows = []; snap.forEach(d => rows.push(d.data()));
      return res.status(200).json(rows);
    }

    if (type === "queries") {
      const snap = await db.collection("bing_queries").where("date", ">=", cutoff).orderBy("date", "desc").limit(parseInt(req.query.limit) || 200).get();
      const rows = []; snap.forEach(d => rows.push(d.data()));
      return res.status(200).json(rows);
    }

    return res.status(400).json({ error: "Unknown type. Use: stats, queries" });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

/**
 * Bing status check
 */
exports.getBingStatus = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method !== "GET") return res.status(405).json({ error: "GET only" });

  try {
    const key = bingKey();
    if (!key) return res.status(200).json({ configured: false, message: "No Bing API key. Set in Firebase config or env." });

    // Check latest data
    const snap = await db.collection("bing_site_stats").orderBy("date", "desc").limit(1).get();
    const lastData = snap.empty ? null : snap.docs[0].data().date;

    return res.status(200).json({
      configured: true,
      key_masked: key.slice(0, 4) + "••••" + key.slice(-4),
      site_url: bingSiteUrl(),
      last_data_date: lastData,
      fresh: lastData && (Date.now() - new Date(lastData).getTime()) < 86400000 * 2,
    });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

/**
 * Save Bing API key from dashboard
 */
exports.saveBingConfig = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const { apiKey, siteUrl } = req.body || {};
    if (!apiKey) return res.status(400).json({ error: "Missing apiKey" });
    
    // Store in Firestore (functions.config is deprecated)
    await db.collection("admin_prefs").doc("bing_config").set({
      api_key: apiKey,
      site_url: siteUrl || "https://calcto.work",
      updated_at: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });
    
    // Also set via functions config for backward compat
    // Note: functions.config() requires redeploy
    
    return res.status(200).json({ status: "ok", message: "Bing API key saved. Run fetchBingOnDemand to test." });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

/**
 * On-demand Bing data fetch
 */
exports.fetchBingOnDemand = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") { res.set("Access-Control-Allow-Methods", "GET"); return res.status(204).send(""); }

  try {
    // Try Firestore key first, then functions config
    const cfgDoc = await db.collection("admin_prefs").doc("bing_config").get();
    let key = bingKey();
    if (!key && cfgDoc.exists) key = cfgDoc.data().api_key;
    if (!key) return res.status(500).json({ error: "No Bing API key. Set via Settings or firebase functions:config:set bing.key" });

    const siteUrl = bingSiteUrl();
    const days = parseInt(req.query.days) || 30;
    const today = new Date();
    const endDate = new Date(today - 3 * 86400000).toISOString().slice(0, 10);
    const startDate = new Date(today - (days + 3) * 86400000).toISOString().slice(0, 10);

    // Override key for this call
    const fetch = require("node-fetch");
    let statsCount = 0, queriesCount = 0;

    // Stats
    const statsUrl = `${BING_API}/GetSiteStats?siteUrl=${encodeURIComponent(siteUrl)}&startDate=${startDate}&endDate=${endDate}`;
    const statsR = await fetch(statsUrl, { headers: { "Content-Type": "application/json", "ApiKey": key }, timeout: 15000 });
    if (statsR.ok) {
      const stats = await statsR.json();
      if (stats && stats.SiteStatsList && stats.SiteStatsList.SiteStats) {
        const batch = db.batch();
        const siteStats = Array.isArray(stats.SiteStatsList.SiteStats) ? stats.SiteStatsList.SiteStats : [stats.SiteStatsList.SiteStats];
        for (const s of siteStats) {
          if (!s.Date || s.Date < "2020-01-01") continue;
          batch.set(db.collection("bing_site_stats").doc(s.Date), {
            date: s.Date, site_url: siteUrl,
            clicks: s.Clicks || 0, impressions: s.Impressions || 0, ctr: s.CTR || 0,
            avg_position: s.AvgPosition || 0, pages_indexed: s.PagesIndexed || 0, pages_crawled: s.PagesCrawled || 0,
            fetched_at: admin.firestore.FieldValue.serverTimestamp(),
          });
        }
        await batch.commit();
        statsCount = siteStats.length;
      }
    }

    // Queries
    const queriesUrl = `${BING_API}/GetQueryStats?siteUrl=${encodeURIComponent(siteUrl)}&startDate=${startDate}&endDate=${endDate}&rowLimit=200`;
    const queriesR = await fetch(queriesUrl, { headers: { "Content-Type": "application/json", "ApiKey": key }, timeout: 15000 });
    if (queriesR.ok) {
      const keywords = await queriesR.json();
      if (keywords && keywords.QueryStatsList && keywords.QueryStatsList.QueryStats) {
        const batch = db.batch();
        const queries = Array.isArray(keywords.QueryStatsList.QueryStats) ? keywords.QueryStatsList.QueryStats : [keywords.QueryStatsList.QueryStats];
        for (const q of queries) {
          const docId = `${endDate}_${(q.Query || "unknown").replace(/[\/\.\#\$\[\]]/g, "_")}`;
          batch.set(db.collection("bing_queries").doc(docId), {
            date: endDate, query: q.Query || "", clicks: q.Clicks || 0, impressions: q.Impressions || 0,
            ctr: q.CTR || 0, avg_position: q.AvgPosition || 0, site_url: siteUrl,
            fetched_at: admin.firestore.FieldValue.serverTimestamp(),
          });
        }
        await batch.commit();
        queriesCount = queries.length;
      }
    }

    return res.status(200).json({ status: "ok", siteUrl, startDate, endDate, stats: statsCount, queries: queriesCount });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

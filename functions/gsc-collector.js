/**
 * CalcToWork — GSC Data Collector
 * Scheduled Firebase Function: fetches Search Console data daily at 3 AM UTC
 * Stores search analytics, page stats, site stats, and coverage data in Firestore
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");
const { google } = require("googleapis");

const db = admin.firestore();

// GSC OAuth2 client
function getSearchConsoleClient() {
  const oauth2Client = new google.auth.OAuth2(
    process.env.GSC_CLIENT_ID,
    process.env.GSC_CLIENT_SECRET
  );
  oauth2Client.setCredentials({
    refresh_token: process.env.GSC_REFRESH_TOKEN,
  });
  return google.searchconsole({ version: "v1", auth: oauth2Client });
}

/**
 * Query GSC search analytics
 * @param {string} siteUrl - Full GSC site URL
 * @param {string} startDate - YYYY-MM-DD
 * @param {string} endDate - YYYY-MM-DD
 * @param {string[]} dimensions - e.g. ["query"], ["page"], ["query","page"]
 * @param {number} rowLimit - Max rows
 */
async function queryGsc(siteUrl, startDate, endDate, dimensions, rowLimit = 25000) {
  const sc = getSearchConsoleClient();
  const body = {
    startDate,
    endDate,
    dimensions,
    rowLimit,
    aggregationType: "auto",
    startRow: 0,
  };

  let allRows = [];
  let startRow = 0;

  while (true) {
    body.startRow = startRow;
    const res = await sc.searchanalytics.query({ siteUrl, requestBody: body });
    const rows = res.data.rows || [];
    allRows = allRows.concat(rows);
    if (rows.length < rowLimit) break;
    startRow += rowLimit;
    if (startRow >= 50000) break; // GSC API limit
  }

  return allRows;
}

/**
 * Store query-level data in Firestore
 */
async function storeQueryData(siteUrl, startDate, endDate) {
  console.log(`[GSC] Fetching query data for ${siteUrl} (${startDate} to ${endDate})`);
  const rows = await queryGsc(siteUrl, startDate, endDate, ["query", "page", "country", "device", "date"]);

  const batch = db.batch();
  let count = 0;
  const seen = new Set();

  for (const row of rows) {
    const keys = row.keys || [];
    const docId = `${startDate}_${keys.join("_")}`.replace(/[\/\.\#\$\[\]]/g, "_");
    if (seen.has(docId)) continue;
    seen.add(docId);

    const docRef = db.collection("gsc_search_data").doc(docId);
    batch.set(docRef, {
      date: keys[4] || startDate,
      query: keys[0] || "",
      page: keys[1] || "",
      country: keys[2] || "",
      device: keys[3] || "",
      clicks: row.clicks || 0,
      impressions: row.impressions || 0,
      ctr: row.ctr || 0,
      position: row.position || 0,
      site_url: siteUrl,
      fetched_at: admin.firestore.FieldValue.serverTimestamp(),
    });
    count++;

    if (count % 500 === 0) {
      await batch.commit();
      console.log(`[GSC] Committed ${count} query rows`);
    }
  }

  if (count % 500 !== 0) {
    await batch.commit();
  }
  console.log(`[GSC] Stored ${count} total query rows`);
}

/**
 * Store page-level aggregated stats in Firestore
 */
async function storePageStats(siteUrl, startDate, endDate) {
  console.log(`[GSC] Fetching page stats for ${siteUrl}`);
  const rows = await queryGsc(siteUrl, startDate, endDate, ["page"], 10000);

  const batch = db.batch();
  let count = 0;

  for (const row of rows) {
    const page = (row.keys || [])[0] || "";
    const docId = `${startDate}_${page.replace(/[\/\.\#\$\[\]]/g, "_")}`;
    const docRef = db.collection("gsc_page_stats").doc(docId);

    batch.set(docRef, {
      date: startDate,
      page,
      total_clicks: row.clicks || 0,
      total_impressions: row.impressions || 0,
      avg_ctr: row.ctr || 0,
      avg_position: row.position || 0,
      site_url: siteUrl,
      fetched_at: admin.firestore.FieldValue.serverTimestamp(),
    });
    count++;
    if (count % 500 === 0) { await batch.commit(); }
  }

  if (count % 500 !== 0) { await batch.commit(); }
  console.log(`[GSC] Stored ${count} page stats`);
}

/**
 * Fetch site-level aggregate stats
 */
async function storeSiteStats(siteUrl, startDate, endDate) {
  console.log(`[GSC] Fetching site stats for ${siteUrl}`);
  const rows = await queryGsc(siteUrl, startDate, endDate, [], 1);
  const summary = rows[0] || {};

  const docId = `${startDate}_site`;
  await db.collection("gsc_site_stats").doc(docId).set({
    date: startDate,
    site_url: siteUrl,
    total_clicks: summary.clicks || 0,
    total_impressions: summary.impressions || 0,
    avg_ctr: summary.ctr || 0,
    avg_position: summary.position || 0,
    fetched_at: admin.firestore.FieldValue.serverTimestamp(),
  });
  console.log(`[GSC] Stored site stats: ${summary.clicks} clicks, ${summary.impressions} impressions`);
}

/**
 * Fetch coverage / indexation issues from GSC
 */
async function storeCoverageData(siteUrl) {
  console.log(`[GSC] Fetching coverage data for ${siteUrl}`);
  try {
    const sc = getSearchConsoleClient();
    const res = await sc.urlcrawlerrorssamples.list({
      siteUrl,
      category: "all",
      platform: "web",
    });
    const samples = res.data.urlCrawlErrorSamples || [];

    const batch = db.batch();
    for (const sample of samples) {
      const docId = sample.pageUrl.replace(/[\/\.\#\$\[\]]/g, "_").slice(0, 100);
      const docRef = db.collection("gsc_coverage").doc(docId);
      batch.set(docRef, {
        page_url: sample.pageUrl,
        last_crawled: sample.lastCrawled || null,
        response_code: sample.responseCode || null,
        issue_type: sample.urlCrawlErrorDetails?.category || "unknown",
        issue_detail: sample.urlCrawlErrorDetails?.platform || "",
        site_url: siteUrl,
        fetched_at: admin.firestore.FieldValue.serverTimestamp(),
      });
    }
    await batch.commit();
    console.log(`[GSC] Stored ${samples.length} coverage issues`);
  } catch (e) {
    console.error("[GSC] Coverage fetch failed:", e.message);
  }
}

/**
 * Main scheduled function — runs daily
 * Trigger: pubsub schedule "0 3 * * *" (3 AM UTC)
 */
exports.fetchGscData = functions.pubsub
  .schedule("0 3 * * *")
  .timeZone("UTC")
  .onRun(async (context) => {
    const siteUrl = process.env.GSC_SITE_URL || "sc-domain:calcto.work";
    const today = new Date();
    const endDate = new Date(today - 3 * 86400000).toISOString().slice(0, 10); // GSC 3-day lag
    const startDate = new Date(today - 93 * 86400000).toISOString().slice(0, 10); // 90 days back

    console.log(`[GSC] Starting collection: ${startDate} to ${endDate} for ${siteUrl}`);

    try {
      await storeQueryData(siteUrl, startDate, endDate);
      await storePageStats(siteUrl, startDate, endDate);
      await storeSiteStats(siteUrl, startDate, endDate);
      await storeCoverageData(siteUrl);
      console.log("[GSC] Collection complete");
    } catch (e) {
      console.error("[GSC] Collection failed:", e);
      throw e;
    }
  });

/**
 * On-demand GSC fetch — callable via HTTP
 * Trigger: HTTPS request with ?days=N parameter
 */
exports.fetchGscOnDemand = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") {
    res.set("Access-Control-Allow-Methods", "GET");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    return res.status(204).send("");
  }

  const siteUrl = req.query.site || process.env.GSC_SITE_URL || "sc-domain:calcto.work";
  const days = parseInt(req.query.days) || 30;
  const today = new Date();
  const endDate = new Date(today - 3 * 86400000).toISOString().slice(0, 10);
  const startDate = new Date(today - (days + 3) * 86400000).toISOString().slice(0, 10);

  try {
    await storeQueryData(siteUrl, startDate, endDate);
    await storePageStats(siteUrl, startDate, endDate);
    await storeSiteStats(siteUrl, startDate, endDate);
    res.status(200).json({ status: "ok", startDate, endDate, siteUrl });
  } catch (e) {
    res.status(500).json({ status: "error", message: e.message });
  }
});

/**
 * Get GSC data endpoint — for dashboard to query stored data
 * Trigger: HTTPS GET with query params
 */
exports.getGscData = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") {
    res.set("Access-Control-Allow-Methods", "GET");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    return res.status(204).send("");
  }

  try {
    const type = req.query.type || "queries";
    const days = parseInt(req.query.days) || 30;

    if (type === "queries") {
      const snap = await db.collection("gsc_search_data")
        .orderBy("clicks", "desc")
        .limit(parseInt(req.query.limit) || 100)
        .get();

      const rows = [];
      snap.forEach(doc => rows.push(doc.data()));
      return res.status(200).json(rows);
    }

    if (type === "pages") {
      const snap = await db.collection("gsc_page_stats")
        .orderBy("total_clicks", "desc")
        .limit(parseInt(req.query.limit) || 100)
        .get();

      const rows = [];
      snap.forEach(doc => rows.push(doc.data()));
      return res.status(200).json(rows);
    }

    if (type === "site_stats") {
      const snap = await db.collection("gsc_site_stats")
        .orderBy("date", "desc")
        .limit(parseInt(req.query.limit) || 90)
        .get();

      const rows = [];
      snap.forEach(doc => rows.push(doc.data()));
      return res.status(200).json(rows);
    }

    if (type === "coverage") {
      const snap = await db.collection("gsc_coverage")
        .limit(parseInt(req.query.limit) || 500)
        .get();

      const rows = [];
      snap.forEach(doc => rows.push(doc.data()));
      return res.status(200).json(rows);
    }

    res.status(400).json({ error: "Unknown type. Use: queries, pages, site_stats, coverage" });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

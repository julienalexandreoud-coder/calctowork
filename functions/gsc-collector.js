/**
 * CalcToWork — GSC Data Collector
 * Scheduled Firebase Function: fetches Search Console data daily at 3 AM UTC
 * Stores search analytics, page stats, site stats, and coverage data in Firestore
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");
const { google } = require("googleapis");

// Read GSC credentials from Firebase Functions config
function gscConfig() {
  const cfg = functions.config().gsc || {};
  return {
    clientId: cfg.client_id || process.env.GSC_CLIENT_ID,
    clientSecret: cfg.client_secret || process.env.GSC_CLIENT_SECRET,
    refreshToken: cfg.refresh_token || process.env.GSC_REFRESH_TOKEN,
    siteUrl: cfg.site_url || process.env.GSC_SITE_URL || "sc-domain:calcto.work",
  };
}

const db = admin.firestore();

// GSC OAuth2 client
function getSearchConsoleClient() {
  const { clientId, clientSecret, refreshToken } = gscConfig();
  const oauth2Client = new google.auth.OAuth2(clientId, clientSecret);
  oauth2Client.setCredentials({ refresh_token: refreshToken });
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

  let batch = db.batch();
  let count = 0;
  let batchCount = 0;
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
    batchCount++;

    if (batchCount === 499) {
      await batch.commit();
      console.log(`[GSC] Committed ${count} query rows`);
      batch = db.batch();
      batchCount = 0;
    }
  }

  if (batchCount > 0) await batch.commit();
  console.log(`[GSC] Stored ${count} total query rows`);
}

/**
 * Store page-level aggregated stats in Firestore
 */
async function storePageStats(siteUrl, startDate, endDate) {
  console.log(`[GSC] Fetching page stats for ${siteUrl}`);
  const rows = await queryGsc(siteUrl, startDate, endDate, ["page"], 10000);

  let batch = db.batch();
  let count = 0;
  let batchCount = 0;

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
    batchCount++;
    if (batchCount === 499) { await batch.commit(); batch = db.batch(); batchCount = 0; }
  }

  if (batchCount > 0) { await batch.commit(); }
  console.log(`[GSC] Stored ${count} page stats`);
}

/**
 * Fetch site-level stats per day (one Firestore doc per date)
 */
async function storeSiteStats(siteUrl, startDate, endDate) {
  console.log(`[GSC] Fetching daily site stats for ${siteUrl} (${startDate} to ${endDate})`);
  const rows = await queryGsc(siteUrl, startDate, endDate, ["date"], 90);

  let batch = db.batch();
  let count = 0;
  let batchCount = 0;

  for (const row of rows) {
    const date = (row.keys || [])[0] || startDate;
    const docId = `${date}_site`;
    batch.set(db.collection("gsc_site_stats").doc(docId), {
      date,
      site_url: siteUrl,
      total_clicks: row.clicks || 0,
      total_impressions: row.impressions || 0,
      avg_ctr: row.ctr || 0,
      avg_position: row.position || 0,
      fetched_at: admin.firestore.FieldValue.serverTimestamp(),
    });
    count++;
    batchCount++;
    if (batchCount === 499) { await batch.commit(); batch = db.batch(); batchCount = 0; }
  }

  if (batchCount > 0) await batch.commit();
  console.log(`[GSC] Stored ${count} daily site stat rows`);
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
    const siteUrl = gscConfig().siteUrl;
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

  const siteUrl = req.query.site || gscConfig().siteUrl;
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
    const cutoff = new Date(Date.now() - days * 86400000).toISOString().slice(0, 10);

    if (type === "queries") {
      const snap = await db.collection("gsc_search_data")
        .where("date", ">=", cutoff)
        .orderBy("date", "desc")
        .limit(parseInt(req.query.limit) || 500)
        .get();

      // Aggregate by query across the date range
      const byQuery = {};
      snap.forEach(doc => {
        const d = doc.data();
        const q = d.query || "";
        if (!byQuery[q]) byQuery[q] = { query: q, clicks: 0, impressions: 0, ctrSum: 0, posSum: 0, count: 0 };
        byQuery[q].clicks += d.clicks || 0;
        byQuery[q].impressions += d.impressions || 0;
        byQuery[q].ctrSum += d.ctr || 0;
        byQuery[q].posSum += d.position || 0;
        byQuery[q].count++;
      });
      const rows = Object.values(byQuery)
        .map(r => ({ query: r.query, clicks: r.clicks, impressions: r.impressions, ctr: r.count > 0 ? r.ctrSum / r.count : 0, position: r.count > 0 ? r.posSum / r.count : 0 }))
        .sort((a, b) => b.clicks - a.clicks)
        .slice(0, parseInt(req.query.limit) || 200);
      return res.status(200).json(rows);
    }

    if (type === "pages") {
      const snap = await db.collection("gsc_page_stats")
        .where("date", ">=", cutoff)
        .orderBy("date", "desc")
        .limit(parseInt(req.query.limit) || 500)
        .get();

      // Aggregate by page across the date range
      const byPage = {};
      snap.forEach(doc => {
        const d = doc.data();
        const p = d.page || "";
        if (!byPage[p]) byPage[p] = { page: p, total_clicks: 0, total_impressions: 0, ctrSum: 0, posSum: 0, count: 0 };
        byPage[p].total_clicks += d.total_clicks || 0;
        byPage[p].total_impressions += d.total_impressions || 0;
        byPage[p].ctrSum += d.avg_ctr || 0;
        byPage[p].posSum += d.avg_position || 0;
        byPage[p].count++;
      });
      const rows = Object.values(byPage)
        .map(r => ({ page: r.page, total_clicks: r.total_clicks, total_impressions: r.total_impressions, avg_ctr: r.count > 0 ? r.ctrSum / r.count : 0, avg_position: r.count > 0 ? r.posSum / r.count : 0 }))
        .sort((a, b) => b.total_clicks - a.total_clicks)
        .slice(0, parseInt(req.query.limit) || 200);
      return res.status(200).json(rows);
    }

    if (type === "site_stats") {
      const snap = await db.collection("gsc_site_stats")
        .where("date", ">=", cutoff)
        .orderBy("date", "asc")
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

/**
 * Ranking movement — compare positions this week vs last week per query
 */
exports.getMovement = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") {
    res.set("Access-Control-Allow-Methods", "GET");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    return res.status(204).send("");
  }
  try {
    const today = new Date();
    const lag = 3; // GSC data lag
    const nowEnd   = new Date(today - lag * 86400000).toISOString().slice(0, 10);
    const nowStart = new Date(today - (lag + 7) * 86400000).toISOString().slice(0, 10);
    const prevEnd  = nowStart;
    const prevStart= new Date(today - (lag + 14) * 86400000).toISOString().slice(0, 10);

    const [curSnap, prevSnap] = await Promise.all([
      db.collection("gsc_search_data").where("date", ">=", nowStart).where("date", "<=", nowEnd).limit(5000).get(),
      db.collection("gsc_search_data").where("date", ">=", prevStart).where("date", "<", prevEnd).limit(5000).get(),
    ]);

    const agg = (snap) => {
      const m = {};
      snap.forEach(doc => {
        const d = doc.data();
        const q = d.query || "";
        if (!m[q]) m[q] = { posSum: 0, n: 0, clicks: 0, impressions: 0 };
        m[q].posSum += d.position || 0; m[q].n++;
        m[q].clicks += d.clicks || 0; m[q].impressions += d.impressions || 0;
      });
      return m;
    };

    const cur = agg(curSnap), prev = agg(prevSnap);

    const rows = Object.entries(cur)
      .filter(([q]) => prev[q])
      .map(([q, c]) => {
        const curPos  = c.n  > 0 ? c.posSum  / c.n  : 0;
        const prevPos = prev[q].n > 0 ? prev[q].posSum / prev[q].n : 0;
        return {
          query: q,
          position: +curPos.toFixed(1),
          prev_position: +prevPos.toFixed(1),
          movement: +(prevPos - curPos).toFixed(1), // positive = improved
          clicks: c.clicks,
          impressions: c.impressions,
        };
      })
      .filter(r => Math.abs(r.movement) >= 0.3 && r.impressions >= 5)
      .sort((a, b) => Math.abs(b.movement) - Math.abs(a.movement))
      .slice(0, parseInt(req.query.limit) || 200);

    return res.status(200).json(rows);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

/**
 * Index coverage — GSC sitemaps list
 */
exports.getIndexCoverage = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") {
    res.set("Access-Control-Allow-Methods", "GET");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    return res.status(204).send("");
  }
  try {
    const siteUrl = gscConfig().siteUrl;
    const sc = getSearchConsoleClient();
    const sitemapsRes = await sc.sitemaps.list({ siteUrl });
    const sitemaps = (sitemapsRes.data.sitemap || []).map(s => ({
      path: s.path,
      lastSubmitted: s.lastSubmitted,
      lastDownloaded: s.lastDownloaded,
      warnings: s.warnings || 0,
      errors: s.errors || 0,
      contents: (s.contents || []).map(c => ({
        type: c.type,
        submitted: c.submitted || 0,
        indexed: c.indexed || 0,
      })),
    }));

    const today = new Date().toISOString().slice(0, 10);
    await db.collection("gsc_index_coverage").doc(today).set({
      date: today,
      sitemaps,
      fetched_at: admin.firestore.FieldValue.serverTimestamp(),
    });

    return res.status(200).json(sitemaps);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

/**
 * Weekly email digest — every Monday 8 AM UTC
 */
const nodemailer = require("nodemailer");

exports.sendWeeklyDigest = functions.pubsub
  .schedule("0 8 * * 1")
  .timeZone("UTC")
  .onRun(async () => {
    try {
      const emailCfg = functions.config().email || {};
      if (!emailCfg.user || !emailCfg.pass) {
        console.log("[Digest] Email not configured — set functions.config().email.user/pass/to");
        return;
      }
      const toEmail = emailCfg.to || emailCfg.user;
      const today = new Date();
      const weekAgo     = new Date(today - 7  * 86400000).toISOString().slice(0, 10);
      const twoWeeksAgo = new Date(today - 14 * 86400000).toISOString().slice(0, 10);

      const statsForRange = async (from, to) => {
        let clicks = 0, impr = 0;
        const snap = await db.collection("gsc_site_stats")
          .where("date", ">=", from).where("date", "<", to).get();
        snap.forEach(d => { clicks += d.data().total_clicks || 0; impr += d.data().total_impressions || 0; });
        return { clicks, impr };
      };

      const [thisWeek, lastWeek] = await Promise.all([
        statsForRange(weekAgo, today.toISOString().slice(0, 10)),
        statsForRange(twoWeeksAgo, weekAgo),
      ]);

      const pct = (a, b) => b > 0 ? ((a - b) / b * 100).toFixed(1) : "N/A";
      const arrow = v => parseFloat(v) >= 0 ? `▲ +${v}%` : `▼ ${v}%`;
      const clkPct = pct(thisWeek.clicks, lastWeek.clicks);
      const imrPct = pct(thisWeek.impr, lastWeek.impr);

      const topPagesSnap = await db.collection("gsc_page_stats")
        .where("date", ">=", weekAgo).orderBy("date", "desc").limit(300).get();
      const pm = {};
      topPagesSnap.forEach(d => {
        const data = d.data(); const p = data.page || "";
        if (!pm[p]) pm[p] = 0;
        pm[p] += data.total_clicks || 0;
      });
      const topPages = Object.entries(pm).sort((a, b) => b[1] - a[1]).slice(0, 5);

      // Load latest AI growth brief to include in digest
      const briefSnap = await db.collection("growth_reports").orderBy("generated_at", "desc").limit(1).get();
      let briefHtml = '';
      if (!briefSnap.empty) {
        try {
          const brief = JSON.parse(briefSnap.docs[0].data().brief || '{}');
          if (brief.headline) {
            const actions = [brief.action_1, brief.action_2, brief.action_3].filter(a => a?.what);
            briefHtml = `<h3 style="margin-bottom:8px">🧠 AI Growth Brief</h3>
              <div style="background:#fef3c7;border-left:3px solid #f97316;padding:12px 16px;border-radius:4px;margin-bottom:8px"><strong>${brief.headline}</strong></div>
              ${actions.length ? `<ol style="padding-left:20px;color:#334155">${actions.map(a => `<li style="margin-bottom:4px"><strong>${a.what}</strong>${a.why ? ' — ' + a.why : ''}</li>`).join('')}</ol>` : ''}`;
          }
        } catch(e) { /* brief unavailable — skip section */ }
      }

      const html = `<!DOCTYPE html><html><body style="font-family:sans-serif;color:#1e293b;max-width:520px;margin:0 auto;padding:24px">
        <h2 style="color:#f97316;margin-bottom:4px">📊 CalcToWork Weekly</h2>
        <p style="color:#64748b;margin-top:0">${weekAgo} → ${today.toISOString().slice(0,10)}</p>
        <table style="width:100%;border-collapse:collapse;margin:16px 0">
          <tr style="background:#f8fafc">
            <td style="padding:10px 14px;font-weight:600">Organic Clicks</td>
            <td style="padding:10px 14px;font-size:1.2em;font-weight:700">${thisWeek.clicks.toLocaleString()}</td>
            <td style="padding:10px 14px;color:${parseFloat(clkPct)>=0?'#16a34a':'#dc2626'}">${clkPct !== 'N/A' ? arrow(clkPct) : '—'} vs last week</td>
          </tr>
          <tr>
            <td style="padding:10px 14px;font-weight:600">Impressions</td>
            <td style="padding:10px 14px;font-size:1.2em;font-weight:700">${thisWeek.impr.toLocaleString()}</td>
            <td style="padding:10px 14px;color:${parseFloat(imrPct)>=0?'#16a34a':'#dc2626'}">${imrPct !== 'N/A' ? arrow(imrPct) : '—'} vs last week</td>
          </tr>
        </table>
        <h3 style="margin-bottom:8px">🏆 Top Pages This Week</h3>
        <ol style="padding-left:20px;color:#334155">
          ${topPages.map(([p, c]) => `<li style="margin-bottom:4px"><strong>${p.split('/').filter(Boolean).pop()||p}</strong> — ${c} clicks</li>`).join('')}
        </ol>
        ${briefHtml}
        <div style="margin-top:28px">
          <a href="https://calcto.work/admin/" style="background:#f97316;color:#fff;text-decoration:none;padding:11px 22px;border-radius:7px;font-weight:600;display:inline-block">Open Dashboard →</a>
        </div>
      </body></html>`;

      const transporter = nodemailer.createTransport({
        service: "gmail",
        auth: { user: emailCfg.user, pass: emailCfg.pass },
      });

      await transporter.sendMail({
        from: `CalcToWork Dashboard <${emailCfg.user}>`,
        to: toEmail,
        subject: `CalcToWork: ${thisWeek.clicks} clicks this week ${clkPct !== 'N/A' ? '(' + arrow(clkPct) + ')' : ''}`,
        html,
      });
      console.log("[Digest] Sent to", toEmail);
    } catch (e) {
      console.error("[Digest] Failed:", e.message);
    }
  });

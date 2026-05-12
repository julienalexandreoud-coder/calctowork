/**
 * CalcToWork — Alerting & Anomaly Detection
 * Scheduled Firebase Function: detects traffic anomalies daily at 4 AM UTC
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const db = admin.firestore();
const LANGS = ["en", "es", "fr", "de", "it", "pt"];

/**
 * Detect anomalies by comparing recent period vs previous period
 */
exports.checkAlerts = functions.pubsub
  .schedule("0 4 * * *")
  .timeZone("UTC")
  .onRun(async (context) => {
    console.log("[Alerts] Running anomaly detection");

    const today = new Date();
    const alerts = [];

    try {
      // ── 0. GSC data freshness check — alert if collector hasn't run in 48h ──
      try {
        const latestGscSnap = await db.collection("gsc_site_stats")
          .orderBy("date", "desc").limit(1).get();
        if (!latestGscSnap.empty) {
          const latestDate = latestGscSnap.docs[0].data().date;
          const ageHours = (Date.now() - new Date(latestDate).getTime()) / 3600000;
          // GSC has a built-in 3-day data lag; only alert after 5 days (120h) to avoid false positives
          if (ageHours > 120) {
            alerts.push({
              type: "data_pipeline_broken",
              severity: "high",
              title: `GSC data not updated in ${Math.round(ageHours)}h — last entry: ${latestDate}. Collector may be broken.`,
              metric: "gsc_freshness",
              current_value: Math.round(ageHours),
              previous_value: 0,
              change_pct: -100,
              period: "now",
            });
          }
        }
      } catch(freshnessErr) { console.warn("[Alerts] Freshness check error:", freshnessErr.message); }

      // ── 1. Check site-level traffic (today-3 vs today-10, to account for GSC lag) ──
      const recentDate = new Date(today - 4 * 86400000).toISOString().slice(0, 10);
      const prevDate = new Date(today - 11 * 86400000).toISOString().slice(0, 10);

      const recentSnap = await db.collection("gsc_site_stats")
        .where("date", "==", recentDate)
        .limit(1)
        .get();

      const prevSnap = await db.collection("gsc_site_stats")
        .where("date", "==", prevDate)
        .limit(1)
        .get();

      if (!recentSnap.empty && !prevSnap.empty) {
        const recent = recentSnap.docs[0].data();
        const prev = prevSnap.docs[0].data();

        const clickChange = prev.total_clicks > 0
          ? ((recent.total_clicks - prev.total_clicks) / prev.total_clicks * 100).toFixed(1)
          : 0;

        const imprChange = prev.total_impressions > 0
          ? ((recent.total_impressions - prev.total_impressions) / prev.total_impressions * 100).toFixed(1)
          : 0;

        const threshold = 25; // Configurable alert threshold percentage

        if (Math.abs(clickChange) >= threshold) {
          alerts.push({
            type: clickChange < 0 ? "traffic_drop" : "traffic_spike",
            severity: Math.abs(clickChange) >= 50 ? "high" : "medium",
            title: `Organic clicks ${clickChange < 0 ? "dropped" : "spiked"} ${Math.abs(clickChange)}% vs last week`,
            metric: "clicks",
            current_value: recent.total_clicks,
            previous_value: prev.total_clicks,
            change_pct: parseFloat(clickChange),
            period: "week",
          });
        }

        if (Math.abs(imprChange) >= threshold) {
          alerts.push({
            type: imprChange < 0 ? "impression_drop" : "impression_spike",
            severity: Math.abs(imprChange) >= 50 ? "high" : "medium",
            title: `Impressions ${imprChange < 0 ? "dropped" : "spiked"} ${Math.abs(imprChange)}% vs last week`,
            metric: "impressions",
            current_value: recent.total_impressions,
            previous_value: prev.total_impressions,
            change_pct: parseFloat(imprChange),
            period: "week",
          });
        }
      }

      // ── 2. Check CTR changes ──
      const ctrRecent = recentSnap.empty ? null : recentSnap.docs[0].data();
      const ctrPrev = prevSnap.empty ? null : prevSnap.docs[0].data();

      if (ctrRecent && ctrPrev) {
        const ctrChange = ctrPrev.avg_ctr > 0
          ? ((ctrRecent.avg_ctr - ctrPrev.avg_ctr) / ctrPrev.avg_ctr * 100).toFixed(1)
          : 0;

        if (Math.abs(ctrChange) >= 20) {
          alerts.push({
            type: "ctr_change",
            severity: "medium",
            title: `Average CTR ${ctrChange < 0 ? "dropped" : "improved"} ${Math.abs(ctrChange)}% vs last week`,
            metric: "ctr",
            current_value: ctrRecent.avg_ctr,
            previous_value: ctrPrev.avg_ctr,
            change_pct: parseFloat(ctrChange),
            period: "week",
          });
        }
      }

      // ── 3. Check for new coverage issues ──
      const coverageSnap = await db.collection("gsc_coverage")
        .orderBy("fetched_at", "desc")
        .limit(50)
        .get();

      if (!coverageSnap.empty) {
        const issues = [];
        coverageSnap.forEach(doc => {
          const d = doc.data();
          if (d.issue_type !== "unknown") {
            issues.push(d);
          }
        });

        if (issues.length > 10) {
          alerts.push({
            type: "indexation_issue",
            severity: issues.length > 30 ? "high" : "medium",
            title: `${issues.length} pages with coverage issues detected`,
            metric: "coverage_issues",
            current_value: issues.length,
            previous_value: 0,
            change_pct: issues.length,
            period: "now",
          });
        }
      }

      // ── 4. Check analytics event volume ──
      const todayStart = new Date(today.getFullYear(), today.getMonth(), today.getDate());
      const yesterdayStart = new Date(today - 86400000);
      yesterdayStart.setHours(0, 0, 0, 0);

      const todayEventsSnap = await db.collection("analytics_events")
        .where("event_time", ">=", admin.firestore.Timestamp.fromDate(todayStart))
        .limit(1)
        .get();

      const yesterdayEventsSnap = await db.collection("analytics_events")
        .where("event_time", ">=", admin.firestore.Timestamp.fromDate(yesterdayStart))
        .where("event_time", "<", admin.firestore.Timestamp.fromDate(todayStart))
        .limit(1)
        .get();

      // Note: full count requires aggregation. Simplified check.
      if (!yesterdayEventsSnap.empty && todayEventsSnap.empty) {
        alerts.push({
          type: "no_data",
          severity: "high",
          title: "No analytics events detected today. Tracking may be broken.",
          metric: "events",
          current_value: 0,
          previous_value: 0,
          change_pct: -100,
          period: "today",
        });
      }

      // ── 5. Per-page position drop alerts ──
      const cutoffRecent = new Date(today - 4*86400000).toISOString().slice(0,10);
      const cutoffPrevWk = new Date(today - 11*86400000).toISOString().slice(0,10);

      const [recentPageSnap, prevPageSnap] = await Promise.all([
        db.collection("gsc_page_stats").where("date",">=",cutoffRecent).limit(1000).get(),
        db.collection("gsc_page_stats").where("date",">=",cutoffPrevWk).where("date","<",cutoffRecent).limit(1000).get(),
      ]);

      const recentByPage = {};
      recentPageSnap.forEach(d => {
        const page = d.data().page; const pos = d.data().avg_position || d.data().position;
        if (!page || !pos) return;
        if (!recentByPage[page]) recentByPage[page] = { positions: [], impressions: 0 };
        recentByPage[page].positions.push(pos);
        recentByPage[page].impressions += d.data().total_impressions || d.data().impressions || 0;
      });
      const prevByPage = {};
      prevPageSnap.forEach(d => {
        const page = d.data().page; const pos = d.data().avg_position || d.data().position;
        if (!page || !pos) return;
        if (!prevByPage[page]) prevByPage[page] = [];
        prevByPage[page].push(pos);
      });

      const positionDrops = [];
      for (const [page, rData] of Object.entries(recentByPage)) {
        const prevPositions = prevByPage[page];
        if (!prevPositions || prevPositions.length === 0) continue;
        const currentPos = rData.positions.reduce((a,b)=>a+b)/rData.positions.length;
        const prevPos = prevPositions.reduce((a,b)=>a+b)/prevPositions.length;
        const drop = currentPos - prevPos;
        if (drop >= 5 && prevPos <= 15 && rData.impressions >= 20) {
          positionDrops.push({ page, prevPos: prevPos.toFixed(1), currentPos: currentPos.toFixed(1), drop: drop.toFixed(1) });
        }
      }
      positionDrops.sort((a,b) => parseFloat(b.drop) - parseFloat(a.drop));

      if (positionDrops.length > 0) {
        const top = positionDrops[0];
        const slug = top.page.replace("https://calcto.work/","").split("/").filter(Boolean).join("/");
        alerts.push({
          type: "position_drop",
          severity: parseFloat(top.drop) >= 10 ? "high" : "medium",
          title: `${positionDrops.length} page${positionDrops.length>1?"s":""} dropped in rankings. Worst: /${slug} fell from pos ${top.prevPos} → ${top.currentPos}`,
          metric: "position",
          current_value: parseFloat(top.currentPos),
          previous_value: parseFloat(top.prevPos),
          change_pct: parseFloat(top.drop),
          affected_pages: positionDrops.slice(0,5).map(p => ({ page: p.page, from: p.prevPos, to: p.currentPos })),
          period: "week",
          acknowledged: false,
        });
      }

      // ── 6. Keyword cannibalization detection ──
      try {
        const cannibSnap = await db.collection("gsc_search_data")
          .where("date", ">=", recentDate).limit(2000).get();
        const queryPageMap = {};
        cannibSnap.forEach(doc => {
          const d = doc.data();
          if (!d.query || !d.page || (d.position || 100) > 20) return;
          if (!queryPageMap[d.query]) queryPageMap[d.query] = new Set();
          queryPageMap[d.query].add(d.page);
        });
        const cannibalized = Object.entries(queryPageMap)
          .filter(([, pages]) => pages.size >= 2)
          .sort((a, b) => b[1].size - a[1].size)
          .slice(0, 10);
        if (cannibalized.length > 0) {
          const top = cannibalized[0];
          alerts.push({
            type: "cannibalization",
            severity: "medium",
            title: `${cannibalized.length} keyword${cannibalized.length > 1 ? "s" : ""} triggering multiple pages. Worst: "${top[0]}" (${top[1].size} pages competing)`,
            metric: "cannibalization",
            current_value: cannibalized.length,
            previous_value: 0,
            change_pct: cannibalized.length,
            period: "week",
            details: cannibalized.slice(0, 3).map(([q, pages]) => ({ query: q, pages: [...pages] })),
          });
        }
      } catch (cannibErr) {
        console.warn("[Alerts] Cannibalization check error:", cannibErr.message);
      }

      // ── 7. Hreflang completeness — published calcs missing lang slugs ──
      try {
        const hreflangSnap = await db.collection("calc_cms")
          .where("status", "==", "published").limit(300).get();
        const missingLangs = [];
        hreflangSnap.forEach(doc => {
          const data = doc.data();
          const missing = LANGS.filter(l => l !== "en" && !data.langs?.[l]?.slug);
          if (missing.length > 0) missingLangs.push({ slug: doc.id, missing });
        });
        if (missingLangs.length > 5) {
          alerts.push({
            type: "hreflang_gap",
            severity: missingLangs.length > 30 ? "high" : "medium",
            title: `${missingLangs.length} published calcs are missing hreflang entries for one or more languages`,
            metric: "hreflang_completeness",
            current_value: missingLangs.length,
            previous_value: 0,
            change_pct: missingLangs.length,
            period: "now",
            details: missingLangs.slice(0, 5).map(m => ({ slug: m.slug, missing: m.missing })),
          });
        }
      } catch(hreflangErr) { console.warn("[Alerts] Hreflang check error:", hreflangErr.message); }

      // ── Housekeeping: expire stale pending SEO suggestions (>60 days) ──
      try {
        const cutoff60 = admin.firestore.Timestamp.fromDate(new Date(Date.now() - 60 * 86400000));
        const staleSnap = await db.collection("seo_suggestions")
          .where("status", "==", "pending")
          .where("created_at", "<=", cutoff60)
          .limit(50).get();
        if (!staleSnap.empty) {
          const expireBatch = db.batch();
          staleSnap.forEach(d => expireBatch.update(d.ref, { status: "expired" }));
          await expireBatch.commit();
          console.log(`[Alerts] Expired ${staleSnap.size} stale SEO suggestions`);
        }
      } catch(expiryErr) { console.warn("[Alerts] Suggestion expiry error:", expiryErr.message); }

      // ── Write alerts to Firestore ──
      if (alerts.length > 0) {
        const batch = db.batch();
        alerts.forEach(alert => {
          const docRef = db.collection("dashboard_alerts").doc();
          const { acknowledged: _ack, ...alertData } = alert;
        batch.set(docRef, {
            ...alertData,
            created_at: admin.firestore.FieldValue.serverTimestamp(),
            acknowledged: false,
          });
        });
        await batch.commit();
        console.log(`[Alerts] ${alerts.length} alerts created`);
      } else {
        console.log("[Alerts] No anomalies detected");
      }

      return { alerts_created: alerts.length };
    } catch (e) {
      console.error("[Alerts] Error:", e);
      throw e;
    }
  });

/**
 * Get alerts for dashboard
 */
exports.getAlerts = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") {
    res.set("Access-Control-Allow-Methods", "GET,POST");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    return res.status(204).send("");
  }

  if (req.method === "POST") {
    // Acknowledge alert
    try {
      const { alertId } = req.body;
      await db.collection("dashboard_alerts").doc(alertId).update({ acknowledged: true });
      return res.status(200).json({ status: "ok" });
    } catch (e) {
      return res.status(500).json({ error: e.message });
    }
  }

  // GET: list alerts
  try {
    const unacknowledged = req.query.acknowledged !== "true";
    let q = db.collection("dashboard_alerts")
      .orderBy("created_at", "desc")
      .limit(parseInt(req.query.limit) || 100);

    if (unacknowledged) {
      q = q.where("acknowledged", "==", false);
    }

    const snap = await q.get();
    const rows = [];
    snap.forEach(doc => rows.push({ id: doc.id, ...doc.data() }));
    return res.status(200).json(rows);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

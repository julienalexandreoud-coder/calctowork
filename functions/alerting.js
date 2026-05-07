/**
 * CalcToWork — Alerting & Anomaly Detection
 * Scheduled Firebase Function: detects traffic anomalies daily at 4 AM UTC
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const db = admin.firestore();

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

      // ── Write alerts to Firestore ──
      if (alerts.length > 0) {
        const batch = db.batch();
        alerts.forEach(alert => {
          const docRef = db.collection("dashboard_alerts").doc();
          batch.set(docRef, {
            ...alert,
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

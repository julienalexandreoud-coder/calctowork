/**
 * eventStatsHttp — count analytics events by name over a window.
 *
 * Written to answer "how many people actually export a PDF?" before building a
 * paid PDF feature. Worth having generally: it is the only way to tell which
 * of the result-panel actions (copy, share, PDF, partner click) people use,
 * which is what should decide what gets built next.
 *
 * GET ?days=30[&event=pdf_export]
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

exports.eventStatsHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
    res.set("Access-Control-Allow-Origin", "*");
    try {
      const days = Math.min(120, parseInt(req.query.days, 10) || 30);
      const only = String(req.query.event || "");
      const since = admin.firestore.Timestamp.fromMillis(Date.now() - days * 86400000);
      const db = admin.firestore();

      let q = db.collection("analytics_events").where("event_time", ">=", since);
      if (only) q = q.where("event_name", "==", only);

      // Page through rather than one huge read, and cap the work.
      const byEvent = {};
      const bySlug = {};
      const sessions = new Set();
      let scanned = 0, last = null, guard = 0;

      while (guard++ < 60) {
        let page = q.orderBy("event_time").limit(2000);
        if (last) page = page.startAfter(last);
        const snap = await page.get();
        if (snap.empty) break;
        snap.forEach(d => {
          const v = d.data();
          scanned++;
          const n = v.event_name || "(none)";
          byEvent[n] = (byEvent[n] || 0) + 1;
          if (v.session_id) sessions.add(v.session_id);
          if (only && v.calc_slug) bySlug[v.calc_slug] = (bySlug[v.calc_slug] || 0) + 1;
        });
        last = snap.docs[snap.docs.length - 1];
        if (snap.size < 2000) break;
      }

      const events = Object.entries(byEvent).sort((a, b) => b[1] - a[1])
        .map(([name, count]) => ({ name, count }));
      const topSlugs = Object.entries(bySlug).sort((a, b) => b[1] - a[1]).slice(0, 15)
        .map(([slug, count]) => ({ slug, count }));

      return res.status(200).json({
        windowDays: days,
        filteredTo: only || null,
        scanned,
        complete: guard < 60,
        uniqueSessions: sessions.size,
        events,
        topSlugs: only ? topSlugs : undefined,
      });
    } catch (e) {
      console.error("eventStatsHttp:", e);
      return res.status(500).json({ error: e.message });
    }
  });

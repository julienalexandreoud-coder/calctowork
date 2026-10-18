/**
 * purgeGscHttp — delete the accumulated duplicate GSC rows.
 *
 * Both collections were filled by a document-id bug: ids were prefixed with
 * the collection window's START date, which moved forward daily, so every run
 * wrote a fresh copy of the same 93 days instead of overwriting. Months of
 * duplicates accumulated, which is what Firestore now bills as stored bytes
 * (EUR 3.69 of October's EUR 4.76).
 *
 * The id bug is fixed in gsc-collector.js, so these rows will not come back.
 * Nothing reads them today: _runAutoPilot is the only consumer and it is
 * halted by the kill switch. The collector rebuilds the last 7 days on its
 * next run.
 *
 * Safety:
 *   - PURGEABLE is a hardcoded allowlist. No other collection can be named,
 *     so this endpoint can never touch calc_cms, admin_prefs or analytics.
 *   - DRY RUN by default; nothing is deleted without ?apply=1.
 *   - Deletes in bounded pages so a runaway call cannot exceed its budget.
 *
 * GET ?collection=gsc_search_data&apply=1&max=20000
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

// Only these two. Deliberately not a parameter with a regex.
const PURGEABLE = ["gsc_search_data", "gsc_page_stats"];

const PAGE = 400;      // documents per batched delete
const HARD_CAP = 50000; // per invocation, so one call cannot run away

exports.purgeGscHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
    res.set("Access-Control-Allow-Origin", "*");
    try {
      const col = String(req.query.collection || "");
      if (PURGEABLE.indexOf(col) === -1) {
        return res.status(400).json({
          error: "collection must be one of: " + PURGEABLE.join(", "),
        });
      }
      const apply = req.query.apply === "1";
      const max = Math.min(HARD_CAP, parseInt(req.query.max, 10) || 20000);
      const db = admin.firestore();
      const ref = db.collection(col);

      if (!apply) {
        // Count by paging ids only — cheap relative to reading documents.
        let seen = 0, last = null, guard = 0;
        while (guard++ < 200) {
          let q = ref.orderBy(admin.firestore.FieldPath.documentId()).limit(1000);
          if (last) q = q.startAfter(last);
          const snap = await q.get();
          if (snap.empty) break;
          seen += snap.size;
          last = snap.docs[snap.docs.length - 1].id;
          if (snap.size < 1000) break;
        }
        const sample = await ref.limit(1).get();
        return res.status(200).json({
          dryRun: true,
          collection: col,
          documentsFound: seen,
          countComplete: guard < 200,
          sampleDoc: sample.empty ? null : { id: sample.docs[0].id },
          note: "pass &apply=1 to delete",
        });
      }

      let deleted = 0;
      while (deleted < max) {
        const snap = await ref.limit(PAGE).get();
        if (snap.empty) break;
        const batch = db.batch();
        snap.docs.forEach(d => batch.delete(d.ref));
        await batch.commit();
        deleted += snap.size;
        if (snap.size < PAGE) break;
      }

      const rest = await ref.limit(1).get();
      return res.status(200).json({
        applied: true,
        collection: col,
        deleted,
        emptyNow: rest.empty,
      });
    } catch (e) {
      console.error("purgeGscHttp:", e);
      return res.status(500).json({ error: e.message });
    }
  });

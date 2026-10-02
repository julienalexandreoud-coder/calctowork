/**
 * cleanupHostingVersionsHttp — delete stale Firebase Hosting versions.
 *
 * Hosting retains EVERY release forever and exposes no retention setting. A
 * cron job that bypassed the kill switch published 12-49 full-site versions a
 * day for three weeks, leaving 656 GB stored against 174 MB of actual monthly
 * downloads (~EUR 15/month). The only way to reclaim it is the REST API.
 *
 * Safety:
 *   - The version behind the current release is read from the API and is never
 *     deleted, whatever else happens.
 *   - The N newest versions are additionally kept for rollback (default 5).
 *   - DRY RUN by default. Nothing is deleted without ?apply=1.
 *
 * GET  ?apply=1&keep=5&max=200
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const HOSTING_SITE = "calctowork";
const HOSTING_API = "https://firebasehosting.googleapis.com/v1beta1";

const getToken = async () =>
  (await admin.app().options.credential.getAccessToken()).access_token;

// Bounded concurrency: serial would blow the 540s timeout on ~500 versions,
// unbounded gets us rate limited by the Hosting API.
async function pool(items, size, worker) {
  let i = 0;
  await Promise.all(
    Array.from({ length: Math.min(size, items.length) }, async () => {
      while (i < items.length) await worker(items[i++]);
    })
  );
}

exports.cleanupHostingVersionsHttp = functions
  .runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
    res.set("Access-Control-Allow-Origin", "*");
    try {
      const apply = req.query.apply === "1";
      const keep = Math.max(2, parseInt(req.query.keep, 10) || 5);
      const max = Math.min(400, parseInt(req.query.max, 10) || 200);

      const token = await getToken();
      const headers = { Authorization: "Bearer " + token };

      // 1. Identify the live version so it can never be a deletion candidate.
      const relRes = await fetch(
        `${HOSTING_API}/sites/${HOSTING_SITE}/releases?pageSize=1`,
        { headers }
      );
      if (!relRes.ok) {
        return res.status(500).json({ error: "releases: " + (await relRes.text()).slice(0, 300) });
      }
      const relData = await relRes.json();
      const liveVersion = (((relData.releases || [])[0] || {}).version || {}).name || "";
      if (!liveVersion) {
        return res.status(500).json({ error: "Could not determine live version — refusing to delete anything" });
      }

      // 2. Page through every version on the site.
      let pageToken = "";
      let all = [];
      let guard = 0;
      do {
        const url =
          `${HOSTING_API}/sites/${HOSTING_SITE}/versions?pageSize=100` +
          (pageToken ? `&pageToken=${encodeURIComponent(pageToken)}` : "");
        const r = await fetch(url, { headers });
        if (!r.ok) {
          return res.status(500).json({ error: "versions: " + (await r.text()).slice(0, 300) });
        }
        const d = await r.json();
        all = all.concat(d.versions || []);
        pageToken = d.nextPageToken || "";
      } while (pageToken && ++guard < 60);

      // Newest first.
      all.sort((a, b) =>
        String(b.createTime || "").localeCompare(String(a.createTime || ""))
      );

      const keepSet = new Set([liveVersion]);
      all.slice(0, keep).forEach((v) => keepSet.add(v.name));

      const deletable = all.filter(
        (v) => !keepSet.has(v.name) && v.status !== "DELETED"
      );

      if (!apply) {
        return res.status(200).json({
          dryRun: true,
          liveVersion,
          totalVersions: all.length,
          keeping: [...keepSet],
          wouldDelete: deletable.length,
          oldest: deletable.length ? deletable[deletable.length - 1].createTime : null,
          newestDeletable: deletable.length ? deletable[0].createTime : null,
        });
      }

      const batch = deletable.slice(0, max);
      let deleted = 0;
      const errors = [];
      await pool(batch, 8, async (v) => {
        try {
          const r = await fetch(`${HOSTING_API}/${v.name}`, { method: "DELETE", headers });
          if (r.ok) deleted++;
          else if (errors.length < 5) errors.push(v.name + ": " + (await r.text()).slice(0, 150));
        } catch (e) {
          if (errors.length < 5) errors.push(v.name + ": " + e.message);
        }
      });

      return res.status(200).json({
        applied: true,
        liveVersion,
        totalVersions: all.length,
        deleted,
        remaining: Math.max(0, deletable.length - deleted),
        errors,
      });
    } catch (e) {
      console.error("cleanupHostingVersionsHttp:", e);
      return res.status(500).json({ error: e.message });
    }
  });

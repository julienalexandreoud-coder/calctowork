/**
 * setTtlHttp — enable Firestore TTL on the collections that grow without bound.
 *
 * This is the "never think about it again" fix. The collector was rewritten to
 * key documents on their own date so re-runs overwrite in place, but it only
 * ever touches the last 7 days: once a date partition rolls out of that window
 * nothing revisits it, so the collections still creep upward forever. Same for
 * analytics_events, which is aggregated nightly into analytics_daily and then
 * kept indefinitely for no reason.
 *
 * With a TTL policy Google deletes expired documents itself, at no ongoing
 * effort and no scheduled function of ours. Storage settles at roughly
 * 120 days of data and stays there.
 *
 * Run once. Idempotent: re-enabling an existing policy is a no-op.
 * GET ?apply=1   (dry run otherwise)
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const API = "https://firestore.googleapis.com/v1";

// collection -> the timestamp field whose passing deletes the document.
const TTL_TARGETS = [
  ["gsc_search_data", "expires_at"],
  ["gsc_page_stats", "expires_at"],
  ["analytics_events", "expires_at"],
];

exports.setTtlHttp = functions.runWith({ timeoutSeconds: 300, memory: "256MB" })
  .https.onRequest(async (req, res) => {
    res.set("Access-Control-Allow-Origin", "*");
    try {
      const apply = req.query.apply === "1";
      const project = process.env.GCLOUD_PROJECT || process.env.GCP_PROJECT || "calctowork";
      const token = (await admin.app().options.credential.getAccessToken()).access_token;
      const headers = { Authorization: "Bearer " + token, "Content-Type": "application/json" };

      const out = [];
      for (const [collection, field] of TTL_TARGETS) {
        const url = `${API}/projects/${project}/databases/(default)/collectionGroups/`
          + `${encodeURIComponent(collection)}/fields/${encodeURIComponent(field)}`;

        // Read current state first so a dry run reports something truthful.
        let current = null;
        try {
          const g = await fetch(url, { headers });
          if (g.ok) {
            const j = await g.json();
            current = j.ttlConfig ? (j.ttlConfig.state || "SET") : null;
          }
        } catch (e) { /* reported below as unknown */ }

        if (!apply) {
          out.push({ collection, field, currentTtl: current, wouldEnable: !current });
          continue;
        }

        const r = await fetch(url + "?updateMask=ttlConfig", {
          method: "PATCH",
          headers,
          body: JSON.stringify({ ttlConfig: {} }),
        });
        const body = await r.text();
        out.push({
          collection, field,
          ok: r.ok,
          status: r.status,
          detail: r.ok ? "TTL enabled (may take time to take effect)" : body.slice(0, 250),
        });
      }

      return res.status(200).json({ dryRun: !apply, project, targets: out });
    } catch (e) {
      console.error("setTtlHttp:", e);
      return res.status(500).json({ error: e.message });
    }
  });

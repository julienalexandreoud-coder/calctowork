/**
 * setPartnerIdHttp — publish one affiliate id, with no code deploy.
 *
 * Affiliate ids used to live inside the bundled calculator.js, so adding one
 * meant editing source, copying to functions/assets, redeploying the function,
 * pushing the asset and verifying — a cycle that served a stale container
 * twice in one session. Four ids are arriving one at a time over the coming
 * weeks, so that path was wrong.
 *
 * Firestore is the source of truth; /partners.json on Hosting is the published
 * artefact that calculator.js fetches. Setting an id is one call.
 *
 * These are not secrets. They are public tracking tags that appear in the
 * outgoing links anyway, which is why serving them as a static file is fine.
 *
 * POST { key, value }   — value "" clears a slot
 * GET                   — show current ids (for checking what is live)
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");
const calcPage = require("./calc-page");

// Must match PARTNER_IDS in src/js/calculator.js. An unknown key is refused so
// a typo cannot silently publish a slot nothing reads.
const SLOTS = [
  "manomano_awin", "habitissimo",
  "amazon_es", "amazon_de", "amazon_fr", "amazon_it",
  "insurance_de", "insurance_es", "finance_de", "finance_en",
];

const DOC = () => admin.firestore().collection("admin_prefs").doc("partner_ids");

async function publish(ids) {
  const zlib = require("zlib"), util = require("util"), crypto = require("crypto");
  const gzip = util.promisify(zlib.gzip);
  const body = JSON.stringify(ids, null, 2) + "\n";
  const gzipped = await gzip(Buffer.from(body, "utf8"));
  const hash = crypto.createHash("sha256").update(gzipped).digest("hex");
  return await calcPage._deployPagesToHosting(
    { "/partners.json": { gzipped, hash } },
    "[Assets] partner ids"
  );
}

exports.setPartnerIdHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
    res.set("Access-Control-Allow-Origin", "*");
    res.set("Access-Control-Allow-Methods", "POST, GET, OPTIONS");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    if (req.method === "OPTIONS") return res.status(204).send("");

    try {
      const snap = await DOC().get();
      const ids = snap.exists ? (snap.data() || {}) : {};
      // Always present every slot so the published file is self-documenting.
      const full = {};
      SLOTS.forEach(k => { full[k] = typeof ids[k] === "string" ? ids[k] : ""; });

      if (req.method === "GET") {
        return res.status(200).json({
          ids: full,
          live: SLOTS.filter(k => full[k]),
          empty: SLOTS.filter(k => !full[k]),
        });
      }
      if (req.method !== "POST") return res.status(405).json({ error: "POST or GET" });

      const b = req.body || {};
      const key = String(b.key || "");
      const value = String(b.value == null ? "" : b.value).trim();
      if (SLOTS.indexOf(key) === -1) {
        return res.status(400).json({ error: "unknown slot", allowed: SLOTS });
      }
      // Tracking tags are short and alphanumeric-ish. Reject anything that
      // looks like a URL or markup rather than publishing it into live links.
      if (value && !/^[A-Za-z0-9_.:-]{2,64}$/.test(value)) {
        return res.status(400).json({ error: "value must be 2-64 chars of letters, digits, . _ : or -" });
      }

      full[key] = value;
      await DOC().set({ [key]: value, updated_at: admin.firestore.FieldValue.serverTimestamp() }, { merge: true });
      const result = await publish(full);
      if (result && result.error) return res.status(500).json({ error: result.error });

      return res.status(200).json({
        ok: true, key, value: value || "(cleared)",
        live: SLOTS.filter(k => full[k]),
        url: "https://calcto.work/partners.json",
        versionName: (result && result.versionName) || null,
      });
    } catch (e) {
      console.error("setPartnerIdHttp:", e);
      return res.status(500).json({ error: e.message });
    }
  });

/**
 * setSeoHttp — write a hand-tuned title and description for one calculator,
 * in one language, and mark it seo_locked so the generators stop overriding it.
 *
 * Why this exists: Bing shows 68,400 impressions over 90 days at 2.35% CTR,
 * with clusters stranded at position 2-4 and zero clicks — 184 impressions
 * across "zapata aislada" queries alone. The pages rank; the snippet is what
 * fails. Every page shares one templated title and a description cut off
 * mid-sentence with an ellipsis.
 *
 * Deliberately one calculator per call, with no bulk mode. Mass rewriting
 * titles and descriptions is what cost this site its Google index in
 * September, so the shape of this tool enforces working a few pages at a time.
 *
 * POST { slug, lang, title, description }
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const LANGS = ["en", "es", "de", "fr", "it", "pt"];

exports.setSeoHttp = functions.runWith({ timeoutSeconds: 120, memory: "256MB" })
  .https.onRequest(async (req, res) => {
    res.set("Access-Control-Allow-Origin", "*");
    res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    if (req.method === "OPTIONS") return res.status(204).send("");
    if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

    try {
      const b = req.body || {};
      const slug = String(b.slug || "");
      const lang = String(b.lang || "");
      const title = String(b.title || "").trim();
      const description = String(b.description || "").trim();

      if (!/^[a-z0-9-]+$/.test(slug)) return res.status(400).json({ error: "bad slug" });
      if (LANGS.indexOf(lang) === -1) return res.status(400).json({ error: "bad lang" });
      if (!title || !description) return res.status(400).json({ error: "title and description required" });

      // Search engines truncate past these, and a cut-off snippet is the exact
      // problem being fixed, so refuse rather than ship another truncation.
      if (title.length > 60) return res.status(400).json({ error: `title ${title.length} chars, max 60` });
      if (description.length > 158) return res.status(400).json({ error: `description ${description.length} chars, max 158` });
      if (/[.…]\s*$/.test(description) && description.endsWith("…")) {
        return res.status(400).json({ error: "description must not end in an ellipsis" });
      }

      const db = admin.firestore();
      const ref = db.collection("calc_cms").doc(slug);
      const doc = await ref.get();
      if (!doc.exists) return res.status(404).json({ error: "calculator not found: " + slug });
      const data = doc.data() || {};
      if (!data.langs || !data.langs[lang]) {
        return res.status(404).json({ error: `no ${lang} content for ${slug}` });
      }

      const prevTitle = data.langs[lang].seo_title || "";
      const prevDesc = data.langs[lang].seo_description || "";

      await ref.update({
        [`langs.${lang}.seo_title`]: title,
        [`langs.${lang}.seo_description`]: description,
        [`langs.${lang}.seo_locked`]: true,
        [`langs.${lang}.seo_tuned_at`]: admin.firestore.FieldValue.serverTimestamp(),
      });

      return res.status(200).json({
        ok: true, slug, lang,
        title, description,
        titleLen: title.length, descLen: description.length,
        previous: { title: prevTitle, description: prevDesc.slice(0, 120) },
      });
    } catch (e) {
      console.error("setSeoHttp:", e);
      return res.status(500).json({ error: e.message });
    }
  });

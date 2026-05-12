/**
 * calcPage — serves CMS-created calculator pages dynamically from Firestore
 * URL pattern: /{lang}/{slug}/ or /{lang}/{slug}  (Firebase rewrites handle both)
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const db = admin.firestore();

const LANGS = ["en", "es", "fr", "de", "it", "pt"];

const LANG_LABELS = { en:"EN", es:"ES", fr:"FR", de:"DE", it:"IT", pt:"PT" };

const CATEGORY_LABELS = {
  estructuras:"Structures", mamposteria:"Masonry", pavimentos:"Flooring",
  fontaneria:"Plumbing", electricidad:"Electrical", climatizacion:"HVAC",
  carpinteria:"Carpentry", pintura:"Painting", gestion:"Management",
  matematicas:"Mathematics", ciencia:"Science", salud:"Health",
  finanzas:"Finance", cotidiano:"Everyday", quimica:"Chemistry",
  electronica:"Electronics", clima:"Climate", utilidades:"Utilities",
  fotografia:"Photography", transporte:"Transport", fisica:"Physics",
  musica:"Music", industria:"Industry",
};

const SITE = "https://calcto.work";
const GA_ID = "G-FBFV87HD35";
const ADSENSE_ID = "ca-pub-3048983871829953";

function esc(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function buildHreflang(slug, data) {
  return LANGS.map(l => {
    const lData = data.langs && data.langs[l];
    if (!lData) return "";
    const lSlug = lData.slug || slug;
    return `  <link rel="alternate" hreflang="${l}" href="${SITE}/${l}/${lSlug}/">`;
  }).filter(Boolean).join("\n");
}

function buildLangSwitcher(slug, currentLang, data) {
  return LANGS.map(l => {
    const lData = data.langs && data.langs[l];
    if (!lData) return "";
    const lSlug = lData.slug || slug;
    const active = l === currentLang ? ' class="active"' : "";
    return `<a href="${SITE}/${l}/${lSlug}/"${active}>${LANG_LABELS[l]}</a>`;
  }).filter(Boolean).join("\n        ");
}

function renderInputsForm(inputs, langData) {
  const labels = (langData && langData.inputs_labels) || {};
  return inputs.map(inp => {
    const label = esc(labels[inp.id] || inp.id);
    const unitOpts = (inp.unit_options || [inp.unit]).filter(Boolean);
    const unitSel = unitOpts.length > 1
      ? `<select class="unit-select" name="${esc(inp.id)}_unit" aria-label="Unit for ${label}">
          ${unitOpts.map(u => `<option value="${esc(u)}"${u === inp.unit ? " selected" : ""}>${esc(u)}</option>`).join("")}
        </select>`
      : (inp.unit ? `<span class="unit-label">${esc(inp.unit)}</span>` : "");
    return `
        <div class="form-group">
          <label for="input-${esc(inp.id)}">${label}</label>
          <div class="input-with-unit">
            <input type="number" id="input-${esc(inp.id)}" name="${esc(inp.id)}"
              inputmode="decimal"
              ${inp.min !== undefined ? `min="${inp.min}"` : ""}
              ${inp.max !== undefined ? `max="${inp.max}"` : ""}
              ${inp.step !== undefined ? `step="${inp.step}"` : 'step="any"'}
              ${inp.default !== undefined ? `value="${inp.default}"` : ""}
              autocomplete="off">
            ${unitSel}
          </div>
        </div>`;
  }).join("\n");
}

function renderResults(outputs, langData) {
  const labels = (langData && langData.outputs_labels) || {};
  return outputs.map(out => {
    const label = esc(labels[out.id] || out.id);
    const cls = out.highlight ? "result-item result-highlight" : "result-item";
    return `<div class="${cls}" id="out-${esc(out.id)}" style="display:none">
        <span class="result-label">${label}</span>
        <span class="result-value" data-out="${esc(out.id)}">—</span>
        ${out.unit ? `<span class="result-unit">${esc(out.unit)}</span>` : ""}
      </div>`;
  }).join("\n");
}

function renderArticle(lang, langData, inputs) {
  if (!langData) return "";
  const steps = langData.steps || [];
  const mistakes = langData.mistakes || [];
  const hints = langData.range_hints || {};
  const faqItems = langData.faq || [];

  // Prefer pre-rendered long_content HTML when available
  if (langData.long_content) {
    const faqHtml = faqItems.length
      ? `<section class="faq-section"><h2>FAQ</h2>${faqItems.map(f =>
          `<details class="faq-item"><summary>${esc(f.q)}</summary><p>${esc(f.a)}</p></details>`
        ).join("")}</section>` : "";
    return `<div class="long-content">${langData.long_content}${faqHtml}</div>`;
  }

  // Fallback: render from structured fields
  const stepsHtml = steps.length
    ? `<h2>How to use it</h2><ol>${steps.map(s => `<li>${esc(s)}</li>`).join("")}</ol>` : "";

  const mistakesHtml = mistakes.length
    ? `<h2>Common mistakes</h2><ul>${mistakes.map(m => `<li>⚠️ ${esc(m)}</li>`).join("")}</ul>` : "";

  const exampleHtml = langData.example_label
    ? `<h2>Worked example</h2><p>${esc(langData.example_label)}</p>${
        langData.result_context ? `<p><em>${esc(langData.result_context)}</em></p>` : ""
      }` : "";

  const formulaHtml = langData.formula_display
    ? `<h2>Formula</h2><p><code>${esc(langData.formula_display)}</code></p>` : "";

  const hintRows = Object.entries(hints);
  const hintsHtml = hintRows.length
    ? `<h2>Input guide</h2><table class="comparison-table"><thead><tr><th>Field</th><th>Typical range</th></tr></thead><tbody>
        ${hintRows.map(([k, v]) => `<tr><td>${esc(k)}</td><td>${esc(v)}</td></tr>`).join("")}
      </tbody></table>` : "";

  const faqHtml = faqItems.length
    ? `<section class="faq-section"><h2>FAQ</h2>${faqItems.map(f =>
        `<details class="faq-item"><summary>${esc(f.q)}</summary><p>${esc(f.a)}</p></details>`
      ).join("")}</section>` : "";

  return `<div class="long-content">${stepsHtml}${mistakesHtml}${exampleHtml}${formulaHtml}${hintsHtml}${faqHtml}</div>`;
}

function buildPage(slug, lang, data) {
  const langData = (data.langs && data.langs[lang]) || {};
  const name = esc(langData.name || data.slug || slug);
  const desc = esc(langData.seo_description || langData.desc || "");
  const seoTitle = esc(langData.seo_title || `${name} — CalcToWork`);
  const category = data.category || "matematicas";
  const categoryLabel = esc(CATEGORY_LABELS[category] || category);
  const canonicalSlug = langData.slug || slug;
  const canonicalUrl = `${SITE}/${lang}/${canonicalSlug}/`;
  const today = new Date().toISOString().slice(0, 10);

  const inputs = data.inputs || [];
  const outputs = data.outputs || [];

  // Use explicit faq field if available, otherwise synthesise from steps/mistakes
  const faqItems = (langData.faq && langData.faq.length) ? langData.faq : [
    ...(langData.steps || []).slice(0, 2).map((s, i) => ({
      q: `Step ${i + 1}: How to use this calculator?`,
      a: s,
    })),
    ...(langData.mistakes || []).slice(0, 2).map((m, i) => ({
      q: `Common mistake ${i + 1}?`,
      a: m,
    })),
  ];

  const faqSchema = faqItems.length
    ? JSON.stringify({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        mainEntity: faqItems.map(f => ({
          "@type": "Question",
          name: f.q,
          acceptedAnswer: { "@type": "Answer", text: f.a },
        })),
      })
    : null;

  const howToSteps = (langData.steps || []).map((s, i) => ({
    "@type": "HowToStep",
    position: i + 1,
    text: s,
  }));

  const calcConfig = {
    slug,
    lang,
    inputs: inputs.map(i => ({
      id: i.id, min: i.min, max: i.max, step: i.step,
      default: i.default, unit: i.unit,
      unit_options: i.unit_options || [i.unit],
      unit_category: i.unit_category,
    })),
    outputs: outputs.map(o => ({ id: o.id, unit: o.unit, highlight: o.highlight })),
    formula: data.formula || "return {}",
  };

  return `<!DOCTYPE html>
<html lang="${lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script async src="https://www.googletagmanager.com/gtag/js?id=${GA_ID}"></script>
  <script>
    window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
    gtag('js',new Date());gtag('config','${GA_ID}',{'anonymize_ip':true,'cookie_flags':'SameSite=None;Secure'});
  </script>
  <title>${seoTitle}</title>
  <meta name="description" content="${desc}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#f97316">
  <link rel="preload" as="style" href="/css/styles.css">
  <link rel="preload" as="script" href="/js/calculator.js">
  <link rel="canonical" href="${canonicalUrl}">
${buildHreflang(slug, data)}
  <meta property="og:title" content="${seoTitle}">
  <meta property="og:description" content="${desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:site_name" content="CalcToWork">
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"SoftwareApplication","name":"${name}","description":"${desc}","url":"${canonicalUrl}","applicationCategory":"UtilitiesApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"inLanguage":"${lang}","isPartOf":{"@type":"WebSite","name":"CalcToWork","url":"${SITE}/"}}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"CalcToWork","item":"${SITE}/${lang}/"},{"@type":"ListItem","position":2,"name":"${categoryLabel}","item":"${SITE}/${lang}/${category}/"},{"@type":"ListItem","position":3,"name":"${name}","item":"${canonicalUrl}"}]}
  </script>
  ${faqSchema ? `<script type="application/ld+json">${faqSchema}</script>` : ""}
  ${howToSteps.length ? `<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"HowTo","name":"${name}","description":"${desc}","step":${JSON.stringify(howToSteps)}}
  </script>` : ""}
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/manifest.json">
  <link rel="stylesheet" href="/css/styles.css">
  <link rel="preconnect" href="https://pagead2.googlesyndication.com">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ADSENSE_ID}" crossorigin="anonymous"></script>
  <script>if(localStorage.getItem('ctw-theme')==='dark')document.documentElement.setAttribute('data-theme','dark');</script>
  <script>window.COOKIE_CONSENT_I18N={"privacy_path":"/${lang}/privacy/"};</script>
  <script src="/js/cookie-consent.js" defer></script>
</head>
<body>
<a href="#main-content" class="skip-link">Skip to content</a>

<header>
  <div class="header-inner">
    <a class="logo" href="/${lang}/">
      <img src="/favicon.svg" alt="" class="logo-icon" width="32" height="32">
      Calc<span>To</span>Work
    </a>
    <button class="menu-toggle" id="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-wrapper">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
    <div class="nav-wrapper" id="nav-wrapper">
      <nav>
        <a href="/${lang}/">Home</a>
        <a href="/${lang}/${category}/">${categoryLabel}</a>
      </nav>
      <div class="lang-switcher" aria-label="Language">
        ${buildLangSwitcher(slug, lang, data)}
        <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode" title="Toggle dark mode">&#9790;</button>
      </div>
    </div>
  </div>
</header>
<script>
(function(){var btn=document.getElementById('menu-toggle'),nav=document.getElementById('nav-wrapper');if(!btn||!nav)return;btn.addEventListener('click',function(){var open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open);btn.innerHTML=open?'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="4" y1="4" x2="20" y2="20"/><line x1="20" y1="4" x2="4" y2="20"/></svg>':'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';});document.addEventListener('click',function(e){if(!nav.contains(e.target)&&!btn.contains(e.target)&&nav.classList.contains('open')){nav.classList.remove('open');btn.setAttribute('aria-expanded','false');btn.innerHTML='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';}});})();
</script>

<div class="container">
  <div class="ad-slot ad-slot-banner"><ins class="adsbygoogle" style="display:block" data-ad-client="${ADSENSE_ID}" data-ad-format="auto" data-full-width-responsive="true"></ins>
  <script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div>
</div>

<main class="container" id="main-content">
  <nav class="breadcrumb" aria-label="breadcrumb">
    <a href="/${lang}/">Home</a>
    <span class="breadcrumb-sep" aria-hidden="true">›</span>
    <a href="/${lang}/${category}/">${categoryLabel}</a>
    <span class="breadcrumb-sep" aria-hidden="true">›</span>
    <span aria-current="page">${name}</span>
  </nav>

  <div class="calc-header">
    <div class="calc-header-text">
      <h1>${name}</h1>
      <p class="last-updated">Last updated: ${today}</p>
    </div>
  </div>

  ${langData.desc ? `<div class="calc-intro"><strong>${name}</strong> — ${esc(langData.desc)}</div>` : ""}

  <div class="content-main">
    <div class="calc-layout">
      <div class="card">
        <div class="card-title">Inputs</div>
        <form id="calc-form" novalidate>
          ${renderInputsForm(inputs, langData)}
          <div class="btn-row">
            <button type="submit" class="btn btn-primary">Calculate</button>
            <button type="button" class="btn btn-secondary" id="btn-reset">Reset</button>
          </div>
        </form>
      </div>

      <div class="card results-panel">
        <div class="card-title">Result</div>
        <div id="calc-results" aria-live="polite">
          <div class="result-placeholder">Enter values and press Calculate</div>
          ${renderResults(outputs, langData)}
        </div>
        <div class="results-actions">
          <button class="btn btn-secondary copy-btn" id="btn-copy" style="display:none;">Copy results</button>
          <button class="btn btn-secondary share-btn" id="btn-share" style="display:none;">🔗 Share</button>
          <button class="btn btn-secondary embed-btn" id="btn-embed" title="Embed this calculator">&#60;/&#62; Embed</button>
        </div>
        <div class="feedback-wrap">
          <span class="feedback-label">Was this helpful?</span>
          <button class="feedback-btn" data-val="yes" aria-label="Yes">&#128077;</button>
          <button class="feedback-btn" data-val="no" aria-label="No">&#128078;</button>
        </div>
      </div>
    </div>

    ${(data.comparison_presets || []).length ? `
    <div class="comparison-table-wrap" tabindex="0" role="region" aria-label="Comparison presets">
      <div class="comparison-table-title">Common Examples — Click to Fill</div>
      <table class="comparison-table" id="comparison-table">
        <thead><tr><th></th>${inputs.map(i => `<th>${esc((langData.inputs_labels || {})[i.id] || i.id)}</th>`).join("")}</tr></thead>
        <tbody>
          ${(data.comparison_presets || []).map(p => `<tr data-prefill='${JSON.stringify(p.inputs || {})}'>
            <td class="preset-label-cell">${esc(p.label || "")}</td>
            ${inputs.map(i => `<td>${p.inputs && p.inputs[i.id] !== undefined ? p.inputs[i.id] : "—"}</td>`).join("")}
          </tr>`).join("")}
        </tbody>
      </table>
    </div>` : ""}

    ${renderArticle(lang, langData, inputs)}

    ${data.trust_note ? `<p class="trust-note"><em>ℹ️ ${esc(data.trust_note)}</em></p>` : ""}

  </div>
</main>

<footer class="site-footer">
  <div class="footer-inner container">
    <div class="footer-brand">Calc<span>To</span>Work</div>
    <div class="footer-links">
      <a href="/${lang}/privacy/">Privacy</a>
      <a href="/${lang}/">Home</a>
    </div>
    <div class="footer-langs">
      ${LANGS.map(l => {
        const lData = data.langs && data.langs[l];
        if (!lData) return "";
        const lSlug = lData.slug || slug;
        return `<a href="${SITE}/${l}/${lSlug}/">${LANG_LABELS[l]}</a>`;
      }).filter(Boolean).join(" ")}
    </div>
  </div>
</footer>

<div class="embed-modal" id="embed-modal" style="display:none;" aria-modal="true" role="dialog" aria-labelledby="embed-modal-title">
  <div class="embed-modal-backdrop" id="embed-modal-backdrop"></div>
  <div class="embed-modal-content">
    <div class="embed-modal-header">
      <strong id="embed-modal-title">Embed this calculator</strong>
      <button class="embed-modal-close" id="embed-modal-close" aria-label="Close">&times;</button>
    </div>
    <div class="embed-modal-body">
      <p class="embed-modal-desc">Copy the code below to embed this calculator on your website.</p>
      <textarea class="embed-modal-code" id="embed-modal-code" readonly></textarea>
      <button class="btn btn-primary embed-modal-copy" id="embed-modal-copy">Copy embed code</button>
    </div>
  </div>
</div>
<script>
window.CALC_CONFIG = ${JSON.stringify(calcConfig)};
</script>
<script src="/js/calculator.js" defer></script>
<script src="/js/theme.js" defer></script>
</body>
</html>`;
}

exports.calcPage = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");

  // Parse /{lang}/{slug}/ from URL
  const parts = req.path.replace(/^\/|\/$/g, "").split("/");
  const lang = parts[0];
  const slug = parts[1];

  if (!slug || !LANGS.includes(lang)) {
    return res.status(404).send("Not found");
  }

  try {
    const doc = await db.collection("calc_cms").doc(slug).get();

    if (!doc.exists) {
      return res.status(404).send(`<html><body><h1>Calculator not found</h1><p>No calculator with slug "${esc(slug)}" exists.</p><a href="/${lang}/">← Home</a></body></html>`);
    }

    const data = doc.data();

    // Allow draft preview with ?preview=1 (for admin use)
    if (data.status !== "published" && req.query.preview !== "1") {
      return res.status(404).send(`<html><body><h1>Not published yet</h1><p>This calculator is a draft. <a href="?preview=1">Preview it anyway</a></p></body></html>`);
    }

    const html = buildPage(slug, lang, data);

    res.set("Cache-Control", "public, max-age=300, s-maxage=3600");
    res.set("Content-Type", "text/html; charset=utf-8");
    res.set("X-Robots-Tag", "index, follow");
    return res.status(200).send(html);
  } catch (e) {
    console.error("calcPage error:", e);
    return res.status(500).send("Internal Server Error");
  }
});

/**
 * translateCalc — auto-translates English calculator content to a target language using Claude
 * POST /translateCalc  { slug, targetLang }
 */
exports.translateCalc = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).send("Method Not Allowed");

  const { slug, targetLang } = req.body || {};
  if (!slug || !targetLang || !LANGS.includes(targetLang)) {
    return res.status(400).json({ error: "slug and targetLang required" });
  }

  try {
    const doc = await db.collection("calc_cms").doc(slug).get();
    if (!doc.exists) return res.status(404).json({ error: "Calculator not found" });

    const data = doc.data();
    const enContent = (data.langs && data.langs.en) || {};
    if (!enContent.name) return res.status(400).json({ error: "English content not set" });

    const langNames = { es:"Spanish", fr:"French", de:"German", it:"Italian", pt:"Portuguese" };
    const targetName = langNames[targetLang] || targetLang;

    const prompt = `Translate the following calculator content from English to ${targetName}.
Return ONLY valid JSON with the same structure. Translate all string values including the HTML in long_content. Keep {placeholder} tokens unchanged. Preserve all HTML tags in long_content exactly.

Input JSON:
${JSON.stringify({
  name: enContent.name,
  desc: enContent.desc || "",
  seo_title: enContent.seo_title || "",
  seo_description: enContent.seo_description || "",
  example_label: enContent.example_label || "",
  result_context: enContent.result_context || "",
  formula_display: enContent.formula_display || "",
  steps: enContent.steps || [],
  mistakes: enContent.mistakes || [],
  long_content: enContent.long_content || "",
  faq: enContent.faq || [],
}, null, 2)}`;

    // Use configured AI provider (callAI logic inline to avoid HTTP round-trip)
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key || (functions.config().anthropic && functions.config().anthropic.key);
    if (!apiKey) return res.status(500).json({ error: `No API key configured for provider: ${provider}. Go to AI Settings to add one.` });

    let text;
    if (provider === "anthropic" || !cfg.active_provider) {
      const r = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
        body: JSON.stringify({ model: provCfg.model || "claude-haiku-4-5-20251001", max_tokens: 4000, messages: [{ role: "user", content: prompt }] }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.content && d.content[0] && d.content[0].text;
    } else if (provider === "openai" || provider === "deepseek") {
      const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
      const r = await fetch(`${baseUrl}/chat/completions`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
        body: JSON.stringify({ model: provCfg.model || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini"), messages: [{ role: "user", content: prompt }], max_tokens: 4000 }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
    }

    const jsonMatch = text && text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) return res.status(500).json({ error: "Could not parse AI response" });

    const translated = JSON.parse(jsonMatch[0]);

    // Preserve input/output labels (translate those separately if needed)
    translated.inputs_labels = enContent.inputs_labels || {};
    translated.outputs_labels = enContent.outputs_labels || {};
    translated.range_hints = enContent.range_hints || {};
    translated.slug = enContent.slug || slug;

    return res.status(200).json({ translated });
  } catch (e) {
    console.error("translateCalc error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * generateLongContent — generates long_content HTML + faq for a CMS calc in a given language
 * POST /generateLongContent  { slug, lang }
 */
exports.generateLongContent = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).send("Method Not Allowed");

  const { slug, lang = "en" } = req.body || {};
  if (!slug) return res.status(400).json({ error: "slug required" });

  try {
    const doc = await db.collection("calc_cms").doc(slug).get();
    if (!doc.exists) return res.status(404).json({ error: "Calculator not found" });
    const data = doc.data();
    const enData = (data.langs && data.langs.en) || {};
    const langNames = { en: "English", es: "Spanish", fr: "French", de: "German", it: "Italian", pt: "Portuguese" };
    const langName = langNames[lang] || lang;
    const calcName = enData.name || slug;
    const formula = data.formula || "";
    const inputs = (data.inputs || []).map(i => i.id + (i.unit ? " (" + i.unit + ")" : "")).join(", ");
    const outputs = (data.outputs || []).map(o => o.id + (o.unit ? " (" + o.unit + ")" : "")).join(", ");

    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key || (functions.config().anthropic && functions.config().anthropic.key);
    if (!apiKey) return res.status(500).json({ error: "No API key configured" });

    const prompt = `You are writing high-quality calculator content in ${langName} for a calculator website.

Calculator: "${calcName}"
Formula: ${formula || "n/a"}
Inputs: ${inputs || "n/a"}
Outputs: ${outputs || "n/a"}

Write a complete long-form article in ${langName} with:
- A TL;DR first sentence directly answering how to use this calculator
- 6 H2 sections: "How to Use", "Formula Explained", "Practical Examples" (3 real examples with numbers), "When to Use This Calculator", "Tips and Common Mistakes", "Understanding the Results"
- Each section must have at least 2 full paragraphs
- Total: 800–1200 words
- Use single quotes for any HTML attributes

Also write 4 FAQ items in ${langName} that users would realistically search for.

Return ONLY valid JSON:
{
  "long_content": "<h2>...</h2><p>...</p>...",
  "faq": [{"q": "...", "a": "..."},{"q": "...", "a": "..."},{"q": "...", "a": "..."},{"q": "...", "a": "..."}]
}`;

    let text;
    if (provider === "anthropic" || !cfg.active_provider) {
      const r = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
        body: JSON.stringify({ model: provCfg.model || "claude-haiku-4-5-20251001", max_tokens: 6000, messages: [{ role: "user", content: prompt }] }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.content && d.content[0] && d.content[0].text;
    } else {
      const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
      const r = await fetch(`${baseUrl}/chat/completions`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
        body: JSON.stringify({ model: provCfg.model || "gpt-4o-mini", messages: [{ role: "user", content: prompt }], max_tokens: 6000 }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
    }

    const jsonMatch = text && text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) return res.status(500).json({ error: "Could not parse AI response" });
    const parsed = JSON.parse(jsonMatch[0]);
    return res.status(200).json({ long_content: parsed.long_content || "", faq: parsed.faq || [] });
  } catch (e) {
    console.error("generateLongContent error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * retranslateLongContent — retranslates English long_content + faq to a target language
 * POST /retranslateLongContent  { slug, lang, en_long_content, en_faq }
 */
exports.retranslateLongContent = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).send("Method Not Allowed");

  const { slug, lang, en_long_content, en_faq = [] } = req.body || {};
  if (!lang || !en_long_content) return res.status(400).json({ error: "lang and en_long_content required" });

  const langNames = { es: "Spanish", fr: "French", de: "German", it: "Italian", pt: "Portuguese" };
  const langName = langNames[lang] || lang;

  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key || (functions.config().anthropic && functions.config().anthropic.key);
    if (!apiKey) return res.status(500).json({ error: "No API key configured" });

    const prompt = `Translate the following HTML article and FAQ from English to ${langName}.

Rules:
- Translate all text content to natural, fluent ${langName} — not word-for-word
- Keep ALL HTML tags intact: <h2>, <p>, <strong>, <ul>, <li>, etc.
- Do NOT translate proper nouns, brand names, URLs, or numeric values
- Keep units (m, kg, ft, lb) unchanged
- Use single quotes for any HTML attributes to keep JSON valid
- The FAQ answers should sound natural in ${langName}, not translated

Return ONLY valid JSON:
{
  "long_content": "...(translated HTML)...",
  "faq": [{"q":"...", "a":"..."}]
}

English long_content:
${en_long_content}

English FAQ:
${JSON.stringify(en_faq)}`;

    let text;
    if (provider === "anthropic" || !cfg.active_provider) {
      const r = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
        body: JSON.stringify({ model: provCfg.model || "claude-haiku-4-5-20251001", max_tokens: 8000, messages: [{ role: "user", content: prompt }] }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.content && d.content[0] && d.content[0].text;
    } else {
      const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
      const r = await fetch(`${baseUrl}/chat/completions`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
        body: JSON.stringify({ model: provCfg.model || "gpt-4o-mini", messages: [{ role: "user", content: prompt }], max_tokens: 8000 }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
    }

    const jsonMatch = text && text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) return res.status(500).json({ error: "Could not parse AI response" });
    const parsed = JSON.parse(jsonMatch[0]);
    return res.status(200).json({ long_content: parsed.long_content || "", faq: parsed.faq || [] });
  } catch (e) {
    console.error("retranslateLongContent error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * getCalcData — returns a static calculator's full JSON data for the admin CMS editor
 * GET /getCalcData?id=001
 */
exports.getCalcData = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  const id = req.query.id;
  if (!id || !/^[a-z0-9_-]+$/i.test(id)) return res.status(400).json({ error: "Invalid id" });

  const fs = require("fs");
  const path = require("path");

  // Calculators are in ../src/calculators/ relative to functions/ at deploy time,
  // but also check ./calcs/ (bundled copy) for production.
  const candidateDirs = [
    path.join(__dirname, "calcs", id),
    path.join(__dirname, "..", "src", "calculators", id),
  ];

  let calcDir = null;
  for (const d of candidateDirs) {
    if (fs.existsSync(d)) { calcDir = d; break; }
  }

  if (!calcDir) return res.status(404).json({ error: "Calculator not found: " + id });

  try {
    const calcJsonPath = path.join(calcDir, "calc.json");
    if (!fs.existsSync(calcJsonPath)) return res.status(404).json({ error: "calc.json not found" });

    const calcData = JSON.parse(fs.readFileSync(calcJsonPath, "utf8"));
    const result = { ...calcData };
    result.langs = {};

    for (const lang of LANGS) {
      const langPath = path.join(calcDir, `${lang}.json`);
      if (fs.existsSync(langPath)) {
        result.langs[lang] = JSON.parse(fs.readFileSync(langPath, "utf8"));
      }
    }

    res.set("Cache-Control", "public, max-age=3600");
    return res.status(200).json(result);
  } catch (e) {
    console.error("getCalcData error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * publishCalcToHosting — replaces static calculator pages in Firebase Hosting
 * with CMS-edited versions, making edits live without a full redeploy.
 * POST /publishCalcToHosting  { slug }
 */
/**
 * generateCalcFromPrompt — creates a full calculator from a text description
 * POST /generateCalcFromPrompt  { prompt, category? }
 */
exports.generateCalcFromPrompt = functions.runWith({ timeoutSeconds: 120, memory: '256MB' })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  const { prompt, category } = req.body || {};
  if (!prompt) return res.status(400).json({ error: "prompt required" });

  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(400).json({ error: "No AI API key configured. Go to Settings → AI Provider Settings." });

    const systemPrompt = `You are an expert calculator builder for a multilingual engineering and science calculator website.
Generate a complete calculator JSON from a user description. Be technically accurate.
Return ONLY valid JSON — no markdown, no explanation, just the JSON object.

JSON structure:
{
  "slug": "kebab-case-slug",
  "category": "one of: estructuras, mamposteria, pavimentos, fontaneria, electricidad, climatizacion, carpinteria, pintura, matematicas, ciencia, salud, finanzas, cotidiano, quimica, electronica, clima, utilidades, fotografia, transporte, fisica, musica, industria",
  "standard": "engineering standard if applicable, e.g. EN 206, Eurocode 2, ACI 318, or empty string",
  "trust_note": "key assumption or limitation, or empty string",
  "inputs": [
    { "id": "snake_case_id", "label_en": "English Label", "min": 0, "max": 10000, "step": 0.01, "default": 1, "unit": "m", "unit_options": ["m","ft","cm"], "unit_category": "length" }
  ],
  "outputs": [
    { "id": "snake_case_id", "label_en": "English Label", "unit": "m²", "highlight": true }
  ],
  "formula": "valid JavaScript using inputs.field_id syntax, return { output_id: value }",
  "example_inputs": { "field_id": 5 },
  "langs": {
    "en": {
      "name": "Calculator Name",
      "desc": "One sentence description",
      "seo_title": "Calculator Name — CalcToWork",
      "seo_description": "155-char meta description",
      "formula_display": "human readable equation e.g. Area = Length × Width",
      "example_label": "2-sentence worked example",
      "result_context": "The result is {output_id} unit",
      "steps": ["Step 1 (actionable, specific)", "Step 2", "Step 3", "Step 4"],
      "mistakes": ["Common mistake 1", "Common mistake 2"],
      "long_content": "<h2>How to Use</h2><p>Detailed paragraph (80+ words) explaining step by step how to use this calculator, what inputs mean, and what the result represents.</p><h2>Formula Explained</h2><p>Explain the math formula in plain language (80+ words). Define every variable. Show why the formula works.</p><h2>Practical Examples</h2><p>Give 2-3 concrete real-world examples with actual numbers (100+ words). Walk through each calculation.</p><h2>When to Use This Calculator</h2><p>Describe common use cases and professions that rely on this calculation (80+ words).</p><h2>Tips and Common Mistakes</h2><p>Give expert tips for getting accurate results (80+ words). Warn about unit mismatches, rounding errors, edge cases.</p><h2>Understanding the Results</h2><p>Help the user interpret the output. What does a high vs low result mean? What are typical values? (80+ words).</p>",
      "faq": [{"q": "Question?", "a": "Detailed answer of at least 2 sentences."},{"q": "Question 2?", "a": "Detailed answer of at least 2 sentences."},{"q": "Question 3?", "a": "Detailed answer of at least 2 sentences."}]
    }
  }
}

Rules:
- input id and output id must match exactly what the formula uses
- formula is pure JS: use parseFloat(inputs.x)||0 to read inputs, return object
- steps should be practical and specific to this calculator
- mistakes should be real errors users commonly make
- unit_category: length, area, volume, mass, temperature, time, speed, pressure, force, energy, power, or empty
- highlight: true for the most important output only
- long_content MUST be at least 600 words of rich, useful HTML. Use 6 h2 sections minimum: How to Use, Formula Explained, Practical Examples, When to Use This Calculator, Tips and Common Mistakes, Understanding the Results. Each section must have at least 2 full paragraphs. Use single quotes for any HTML attributes inside long_content to avoid breaking JSON
- faq must have at least 3 real questions users would ask, each answer at least 2 sentences long`;

    const userMsg = `Create a calculator for: ${prompt}${category ? `\nPreferred category: ${category}` : ""}`;

    let text;
    if (provider === "anthropic") {
      const r = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
        body: JSON.stringify({ model: provCfg.model || "claude-sonnet-4-6", max_tokens: 7000, system: systemPrompt, messages: [{ role: "user", content: userMsg }] }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.content && d.content[0] && d.content[0].text;
    } else if (provider === "openai" || provider === "deepseek") {
      const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
      const r = await fetch(`${baseUrl}/chat/completions`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
        body: JSON.stringify({ model: provCfg.model || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o"), messages: [{ role: "system", content: systemPrompt }, { role: "user", content: userMsg }], max_tokens: 7000 }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
    } else if (provider === "gemini") {
      const mdl = provCfg.model || "gemini-1.5-flash";
      const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${mdl}:generateContent?key=${apiKey}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ contents: [{ parts: [{ text: systemPrompt + "\n\n" + userMsg }] }] }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.candidates && d.candidates[0] && d.candidates[0].content && d.candidates[0].content.parts && d.candidates[0].content.parts[0] && d.candidates[0].content.parts[0].text;
    }

    if (!text) return res.status(500).json({ error: "Empty AI response" });
    // Strip DeepSeek <think>...</think> reasoning block if present
    text = text.replace(/<think>[\s\S]*?<\/think>/g, "").trim();
    const match = text.match(/\{[\s\S]*\}/);
    if (!match) return res.status(500).json({ error: "AI did not return valid JSON", raw: text.slice(0, 500) });
    let calc;
    try {
      calc = JSON.parse(match[0]);
    } catch(parseErr) {
      // Try sanitizing common AI JSON issues: trailing commas, unescaped chars in HTML strings
      const cleaned = match[0]
        .replace(/,\s*([}\]])/g, '$1') // trailing commas
        .replace(/[ -]/g, ' '); // control chars
      try {
        calc = JSON.parse(cleaned);
      } catch(e2) {
        // Last resort: strip long_content and faq which are most likely to have bad chars
        const stripped = match[0].replace(/"long_content"\s*:\s*"(?:[^"\\]|\\.)*"/g, '"long_content":""')
          .replace(/"faq"\s*:\s*\[[\s\S]*?\]/g, '"faq":[]');
        try { calc = JSON.parse(stripped); } catch(e3) {
          return res.status(500).json({ error: "Could not parse AI JSON: " + parseErr.message, raw: match[0].slice(0, 300) });
        }
      }
    }
    // Validate formula server-side before returning
    if (calc.formula) {
      try {
        const vm = require("vm");
        const exampleInputs = calc.example_inputs || {};
        // Fill any missing inputs with default values
        (calc.inputs || []).forEach(inp => { if (!(inp.id in exampleInputs)) exampleInputs[inp.id] = inp.default || 0; });
        const script = new vm.Script(`(function(inputs){ ${calc.formula} })`);
        const fn = script.runInContext(vm.createContext({ Math, parseFloat, parseInt, isNaN, isFinite, Number }));
        const output = fn(exampleInputs);
        if (!output || typeof output !== "object" || Object.keys(output).length === 0) {
          return res.status(400).json({ error: "Formula validation failed: returns empty or non-object. Check the formula." });
        }
        const allNaN = Object.values(output).every(v => v === null || v === undefined || (typeof v === "number" && isNaN(v)));
        if (allNaN) return res.status(400).json({ error: "Formula validation failed: all outputs are NaN with example inputs. Fix the formula or example_inputs." });
      } catch(vmErr) {
        return res.status(400).json({ error: "Formula syntax error: " + vmErr.message });
      }
    }
    return res.status(200).json({ calc });
  } catch (e) {
    console.error("generateCalcFromPrompt error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * callAI — unified AI gateway supporting Anthropic, OpenAI, DeepSeek, Gemini
 * POST /callAI  { messages, system?, maxTokens? }
 * API keys and active provider stored in Firestore admin_prefs/ai_config
 */
exports.callAI = functions.runWith({ timeoutSeconds: 120, memory: '256MB' })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  const { messages, system, maxTokens = 2000 } = req.body || {};
  if (!messages || !Array.isArray(messages)) return res.status(400).json({ error: "messages array required" });

  try {
    // Read AI config from Firestore
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const providers = cfg.providers || {};
    const provCfg = providers[provider] || {};
    const apiKey = provCfg.api_key;
    const model = provCfg.model;

    if (!apiKey) return res.status(400).json({ error: `No API key configured for provider: ${provider}. Set it in the AI Settings tab.` });

    let responseText;

    if (provider === "anthropic") {
      const payload = { model: model || "claude-haiku-4-5-20251001", max_tokens: maxTokens, messages };
      if (system) payload.system = system;
      const r = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!r.ok) throw new Error("Anthropic error: " + await r.text());
      const d = await r.json();
      responseText = d.content && d.content[0] && d.content[0].text;

    } else if (provider === "openai" || provider === "deepseek") {
      const baseUrl = provider === "deepseek"
        ? "https://api.deepseek.com/v1"
        : "https://api.openai.com/v1";
      const defaultModel = provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini";
      const msgs = system ? [{ role: "system", content: system }, ...messages] : messages;
      const r = await fetch(`${baseUrl}/chat/completions`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
        body: JSON.stringify({ model: model || defaultModel, messages: msgs, max_tokens: maxTokens }),
      });
      if (!r.ok) throw new Error(`${provider} error: ` + await r.text());
      const d = await r.json();
      const msg = d.choices && d.choices[0] && d.choices[0].message;
      // deepseek-reasoner returns content in reasoning_content when content is empty
      responseText = msg && (msg.content || msg.reasoning_content);

    } else if (provider === "gemini") {
      const mdl = model || "gemini-1.5-flash";
      const parts = [];
      if (system) parts.push({ text: system + "\n\n" });
      messages.forEach(m => parts.push({ text: (m.role === "user" ? "" : "Assistant: ") + m.content }));
      const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${mdl}:generateContent?key=${apiKey}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ contents: [{ parts }] }),
      });
      if (!r.ok) throw new Error("Gemini error: " + await r.text());
      const d = await r.json();
      responseText = d.candidates && d.candidates[0] && d.candidates[0].content && d.candidates[0].content.parts && d.candidates[0].content.parts[0] && d.candidates[0].content.parts[0].text;

    } else {
      return res.status(400).json({ error: "Unknown provider: " + provider });
    }

    if (!responseText) return res.status(500).json({ error: "Empty response from AI provider" });
    return res.status(200).json({ text: responseText, provider, model: model || "default" });

  } catch (e) {
    console.error("callAI error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * saveAIConfig — saves AI provider config to Firestore admin_prefs/ai_config
 * POST /saveAIConfig  { active_provider, providers: { anthropic: { api_key, model }, ... } }
 */
exports.saveAIConfig = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  const { active_provider, providers } = req.body || {};
  if (!active_provider || !providers) return res.status(400).json({ error: "active_provider and providers required" });

  const VALID = ["anthropic", "openai", "deepseek", "gemini"];
  if (!VALID.includes(active_provider)) return res.status(400).json({ error: "Invalid provider" });

  try {
    await db.collection("admin_prefs").doc("ai_config").set({
      active_provider,
      providers,
      updated_at: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });
    return res.status(200).json({ success: true });
  } catch (e) {
    console.error("saveAIConfig error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * getAIConfig — returns AI config (with keys masked) for display in admin
 * GET /getAIConfig
 */
exports.getAIConfig = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method !== "GET") return res.status(405).json({ error: "GET only" });
  try {
    const doc = await db.collection("admin_prefs").doc("ai_config").get();
    if (!doc.exists) return res.status(200).json({ active_provider: null, providers: {} });
    const data = doc.data();
    // Mask API keys for display
    const masked = {};
    for (const [k, v] of Object.entries(data.providers || {})) {
      masked[k] = { ...v, api_key: v.api_key ? v.api_key.slice(0, 8) + "••••••••" + v.api_key.slice(-4) : "" };
    }
    return res.status(200).json({ active_provider: data.active_provider, providers: masked });
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

exports.publishCalcToHosting = functions.runWith({ timeoutSeconds: 300, memory: '512MB' })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  const { slug } = req.body || {};
  if (!slug || !/^[a-z0-9-]+$/.test(slug)) return res.status(400).json({ error: "Invalid slug" });

  const crypto = require("crypto");
  const zlib = require("zlib");
  const util = require("util");
  const gzip = util.promisify(zlib.gzip);

  const SITE = "calctowork";
  const HOSTING_BASE = "https://firebasehosting.googleapis.com/v1beta1";

  try {
    // 1. Read CMS data from Firestore
    const doc = await db.collection("calc_cms").doc(slug).get();
    if (!doc.exists) return res.status(404).json({ error: "CMS doc not found for slug: " + slug });
    const data = doc.data();
    if (data.status !== "published") return res.status(400).json({ error: "Calculator must be published first" });

    // 2. Generate HTML for all available languages
    const newFiles = {}; // { "/en/slug/": htmlBuffer, ... }
    for (const lang of LANGS) {
      if (!data.langs || !data.langs[lang] || !data.langs[lang].name) continue;
      const langSlug = (data.langs[lang] && data.langs[lang].slug) || slug;
      const html = buildPage(slug, lang, data);
      const gzipped = await gzip(Buffer.from(html, "utf8"));
      const hash = crypto.createHash("sha256").update(gzipped).digest("hex");
      newFiles[`/${lang}/${langSlug}/`] = { gzipped, hash };
    }

    if (Object.keys(newFiles).length === 0) {
      return res.status(400).json({ error: "No language content available to publish" });
    }

    // 3. Get OAuth token
    const tokenResult = await admin.app().options.credential.getAccessToken();
    const token = tokenResult.access_token;
    const headers = { "Authorization": "Bearer " + token, "Content-Type": "application/json" };

    // 4. Get current release to clone its version
    const releasesRes = await fetch(`${HOSTING_BASE}/sites/${SITE}/releases?pageSize=1`, { headers });
    if (!releasesRes.ok) throw new Error("Failed to get releases: " + await releasesRes.text());
    const releasesData = await releasesRes.json();
    const currentVersionName = releasesData.releases && releasesData.releases[0] && releasesData.releases[0].version && releasesData.releases[0].version.name;
    if (!currentVersionName) throw new Error("Could not determine current version");
    const currentConfig = releasesData.releases[0].version.config || {};

    // 5. Collect ALL current file hashes (paginated)
    const allCurrentFiles = {};
    let pageToken = null;
    do {
      const url = `${HOSTING_BASE}/${currentVersionName}/files?pageSize=1000${pageToken ? "&pageToken=" + pageToken : ""}`;
      const filesRes = await fetch(url, { headers });
      if (!filesRes.ok) throw new Error("Failed to list files: " + await filesRes.text());
      const filesData = await filesRes.json();
      (filesData.files || []).forEach(f => { allCurrentFiles[f.path] = f.hash; });
      pageToken = filesData.nextPageToken || null;
    } while (pageToken);

    // 6. Build merged file map: old files + new CMS pages (overwrite old static ones)
    const mergedFiles = { ...allCurrentFiles };
    for (const [path, { hash }] of Object.entries(newFiles)) {
      mergedFiles[path] = hash;
      // Also remove trailing-slash variant if present (Firebase uses both)
      const withoutSlash = path.replace(/\/$/, "");
      if (withoutSlash !== path && mergedFiles[withoutSlash]) mergedFiles[withoutSlash] = hash;
    }

    // 7. Create new version with same config
    const createRes = await fetch(`${HOSTING_BASE}/sites/${SITE}/versions`, {
      method: "POST",
      headers,
      body: JSON.stringify({ config: currentConfig }),
    });
    if (!createRes.ok) throw new Error("Failed to create version: " + await createRes.text());
    const newVersion = await createRes.json();
    const newVersionName = newVersion.name;

    // 8. Populate files
    const populateRes = await fetch(`${HOSTING_BASE}/${newVersionName}:populateFiles`, {
      method: "POST",
      headers,
      body: JSON.stringify({ files: mergedFiles }),
    });
    if (!populateRes.ok) throw new Error("Failed to populate files: " + await populateRes.text());
    const populateData = await populateRes.json();
    const uploadUrl = populateData.uploadUrl;
    const uploadRequired = populateData.uploadRequiredHashes || [];

    // 9. Upload only the new files that Firebase doesn't have cached
    for (const [path, { gzipped, hash }] of Object.entries(newFiles)) {
      if (!uploadRequired.includes(hash)) continue;
      const uploadRes = await fetch(`${uploadUrl}/${hash}`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + token, "Content-Type": "application/octet-stream" },
        body: gzipped,
      });
      if (!uploadRes.ok) throw new Error(`Failed to upload ${path}: ${await uploadRes.text()}`);
    }

    // 10. Finalize version
    const finalizeRes = await fetch(`${HOSTING_BASE}/${newVersionName}?update_mask=status`, {
      method: "PATCH",
      headers,
      body: JSON.stringify({ status: "FINALIZED" }),
    });
    if (!finalizeRes.ok) throw new Error("Failed to finalize version: " + await finalizeRes.text());

    // 11. Create release
    const releaseRes = await fetch(`${HOSTING_BASE}/sites/${SITE}/releases?versionName=${newVersionName}`, {
      method: "POST",
      headers,
      body: JSON.stringify({}),
    });
    if (!releaseRes.ok) throw new Error("Failed to create release: " + await releaseRes.text());

    const pagesUpdated = Object.keys(newFiles);
    console.log("publishCalcToHosting success:", slug, pagesUpdated);
    return res.status(200).json({ success: true, pagesUpdated, versionName: newVersionName });

  } catch (e) {
    console.error("publishCalcToHosting error:", e);
    return res.status(500).json({ error: e.message });
  }
});

// ─────────────────────────────────────────────────────────────
// AUTONOMOUS GROWTH FUNCTIONS
// ─────────────────────────────────────────────────────────────

/**
 * sitemap — dynamic XML sitemap combining static + CMS calculators
 * GET /sitemap.xml
 */
exports.sitemap = functions.https.onRequest(async (req, res) => {
  res.set("Cache-Control", "public, max-age=3600, s-maxage=86400");
  try {
    const SITE = "https://calcto.work";
    const now = new Date().toISOString().slice(0, 10);

    // Load CMS published calculators
    const cmsSnap = await db.collection("calc_cms").where("status", "==", "published").get();
    const cmsCalcs = [];
    cmsSnap.forEach(doc => cmsCalcs.push({ slug: doc.id, ...doc.data() }));

    const urls = [];

    // CMS calcs (priority 0.9 — freshly generated, autopilot-maintained)
    for (const calc of cmsCalcs) {
      const updated = calc.updated_at ? new Date(calc.updated_at.seconds * 1000).toISOString().slice(0, 10) : now;
      for (const lang of LANGS) {
        const lSlug = calc.langs?.[lang]?.slug || calc.slug;
        if (!lSlug || !calc.langs?.[lang]?.name) continue;
        urls.push(`  <url><loc>${SITE}/${lang}/${lSlug}/</loc><lastmod>${updated}</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>`);
      }
    }

    // Static home + utility pages
    ["", "about", "privacy", "contact"].forEach(p => {
      urls.push(`  <url><loc>${SITE}/${p ? p + "/" : ""}</loc><changefreq>monthly</changefreq><priority>${p ? "0.5" : "1.0"}</priority></url>`);
    });

    const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.join("\n")}\n</urlset>`;
    res.set("Content-Type", "application/xml");
    return res.status(200).send(xml);
  } catch (e) {
    console.error("sitemap error:", e);
    return res.status(500).send("Sitemap error: " + e.message);
  }
});

/**
 * findKeywordOpportunities — Monday 6 AM: scan GSC for gaps, generate draft calculators
 * Also exposed as HTTP endpoint for manual trigger
 */
exports.findKeywordOpportunities = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .pubsub.schedule("0 6 * * 1").timeZone("UTC").onRun(async () => {
  await _findKeywordOpportunities();
});

exports.findKeywordOpportunitiesHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  try {
    const result = await _findKeywordOpportunities();
    return res.status(200).json(result);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

async function _findKeywordOpportunities() {
  const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
  const cfg = cfgDoc.exists ? cfgDoc.data() : {};
  const provider = cfg.active_provider || "anthropic";
  const provCfg = (cfg.providers || {})[provider] || {};
  const apiKey = provCfg.api_key;
  if (!apiKey) { console.log("findKeywordOpportunities: no AI key configured"); return { skipped: true }; }

  // Get 28-day window
  const cutoff = new Date(Date.now() - 28 * 86400000);

  // Read GSC queries with impressions ≥ 10, position > 5
  const gscSnap = await db.collection("gsc_search_data")
    .where("date", ">=", cutoff.toISOString().slice(0, 10))
    .orderBy("date", "desc")
    .limit(5000)
    .get();

  // Aggregate by query — also build 7d trend buckets to surface fast-rising terms
  const cutoffStr = cutoff.toISOString().slice(0,10);
  const cutoff7Str = new Date(Date.now() - 7*86400000).toISOString().slice(0,10);
  const cutoff14Str = new Date(Date.now() - 14*86400000).toISOString().slice(0,10);
  const queryMap = {};
  const recent7 = {};
  const prior7 = {};
  gscSnap.forEach(doc => {
    const d = doc.data();
    const q = (d.query || "").toLowerCase().trim();
    if (!q || q.length < 5) return;
    if (!queryMap[q]) queryMap[q] = { impressions: 0, clicks: 0, positions: [] };
    queryMap[q].impressions += d.impressions || 0;
    queryMap[q].clicks += d.clicks || 0;
    queryMap[q].positions.push(d.position || 50);
    const dateStr = d.date || "";
    if (dateStr >= cutoff7Str) recent7[q] = (recent7[q]||0) + (d.impressions||0);
    else if (dateStr >= cutoff14Str) prior7[q] = (prior7[q]||0) + (d.impressions||0);
  });

  // Get existing pages to filter out covered queries
  const pagesSnap = await db.collection("gsc_page_stats").limit(2000).get();
  const existingSlugs = new Set();
  pagesSnap.forEach(doc => {
    const page = doc.data().page || "";
    const parts = page.replace("https://calcto.work/", "").split("/");
    if (parts.length >= 2) existingSlugs.add(parts[1]);
  });

  // Also get CMS slugs and names for deduplication
  const cmsSnap = await db.collection("calc_cms").get();
  const cmsNames = new Set();
  cmsSnap.forEach(doc => {
    existingSlugs.add(doc.id);
    const name = (doc.data().langs?.en?.name || "").toLowerCase();
    name.split(/\s+/).filter(w => w.length > 4).forEach(w => cmsNames.add(w));
  });

  // Also collect queries already in pending pipeline (avoid re-generating same topics)
  const pendingPipelineSnap = await db.collection("calc_pipeline").where("status","==","pending").get();
  const pendingQueryWords = new Set();
  pendingPipelineSnap.forEach(doc => {
    (doc.data().source_queries || []).forEach(q =>
      q.split(/\s+/).filter(w=>w.length>4).forEach(w => pendingQueryWords.add(w.toLowerCase()))
    );
  });

  // Filter: impressions ≥ 8, position > 4, no existing page, not already in pipeline
  // trendMultiplier boosts queries growing ≥50% last 7d vs prior 7d (capped at 3×)
  const gaps = Object.entries(queryMap)
    .map(([q, d]) => {
      const r7 = recent7[q] || 0;
      const p7 = prior7[q] || 1;
      const trendMultiplier = r7 >= 3 ? Math.min(r7 / p7, 3) : 1;
      return { query: q, impressions: d.impressions, clicks: d.clicks, trendMultiplier,
               avgPos: d.positions.reduce((a,b)=>a+b,0)/d.positions.length };
    })
    .filter(g => g.impressions >= 8 && g.avgPos > 4)
    .filter(g => !Array.from(existingSlugs).some(s => s && g.query.includes(s.replace(/-/g," ").slice(0,8))))
    // Dedup: skip if key words already covered by CMS calcs or pending pipeline
    .filter(g => {
      const words = g.query.split(/\s+/).filter(w => w.length > 4);
      const inCms = words.filter(w => cmsNames.has(w)).length >= 2;
      const inPipeline = words.filter(w => pendingQueryWords.has(w)).length >= 2;
      return !inCms && !inPipeline;
    })
    // Score by impressions × trend × (1/position): trending keywords near page 1 rank highest
    .sort((a, b) => (b.impressions * b.trendMultiplier / b.avgPos) - (a.impressions * a.trendMultiplier / a.avgPos))
    .slice(0, 15);

  // Cluster into 3 groups by keyword overlap
  const clusters = [];
  const used = new Set();
  for (const gap of gaps) {
    if (used.has(gap.query) || clusters.length >= 3) break;
    const words = new Set(gap.query.split(/\s+/).filter(w => w.length > 3));
    const cluster = [gap];
    for (const other of gaps) {
      if (used.has(other.query) || other.query === gap.query) continue;
      const otherWords = other.query.split(/\s+/).filter(w => w.length > 3);
      if (otherWords.some(w => words.has(w))) {
        cluster.push(other);
        used.add(other.query);
      }
    }
    used.add(gap.query);
    clusters.push({ queries: cluster.map(c => c.query), totalImpressions: cluster.reduce((s,c)=>s+c.impressions,0), avgPos: gap.avgPos });
  }

  // Read brain strategy to steer AI brainstorm in the right direction
  const brainStratDoc = await db.collection("ai_brain").doc("strategy").get();
  const brainStrat = brainStratDoc.exists ? brainStratDoc.data() : {};
  const focusAreas = (brainStrat.focus_areas || []).join(", ");
  const avoidTopics = (brainStrat.avoid_topics || []).join(", ");

  // AI suggests 2 additional ideas based on top categories + brain strategy
  let aiIdeas = [];
  try {
    const topCats = await db.collection("analytics_daily").orderBy("views","desc").limit(100).get();
    const catMap = {};
    topCats.forEach(d => { const c = d.data().category || ""; catMap[c] = (catMap[c]||0)+1; });
    const topCatList = Object.entries(catMap).sort((a,b)=>b[1]-a[1]).slice(0,3).map(([c])=>c).join(", ");
    const r = await _callAIRaw(apiKey, provider, provCfg.model,
      `Suggest 8 calculator ideas for a multilingual calculator site. Each must be distinct, specific, and have real search demand.
Top traffic categories: ${topCatList || "construction, math, health"}
${focusAreas ? `PRIORITY focus areas (prefer these): ${focusAreas}` : ""}
${avoidTopics ? `AVOID these topics (they haven't worked): ${avoidTopics}` : ""}
Requirements: specific tool (not generic), clear inputs/outputs, useful to a real person.
Return JSON array only: [{"prompt":"describe the calculator in 1 sentence","category":"category_slug"}]`, 600);
    const m = r && r.match(/\[[\s\S]*\]/);
    if (m) aiIdeas = JSON.parse(m[0]).slice(0, 8);
  } catch(e) { console.warn("AI ideas failed:", e.message); }

  // Generate full calculators for each opportunity
  const saved = [];
  const allOpps = [
    ...clusters.map(c => ({ prompt: c.queries.join(" / "), source: "gsc", queries: c.queries, impressions: c.totalImpressions, avgPos: c.avgPos })),
    ...aiIdeas.map(i => ({ prompt: i.prompt, source: "ai_brainstorm", queries: [], impressions: 0, avgPos: null })),
  ].slice(0, 15);

  for (const opp of allOpps) {
    try {
      const calcRes = await _generateCalcRaw(apiKey, provider, provCfg.model, opp.prompt);
      if (!calcRes) continue;
      // Auto-translate all languages
      const langs = calcRes.langs || {};
      for (const lang of LANGS) {
        if (lang === "en" || langs[lang]?.name) continue;
        try {
          const translated = await _translateRaw(apiKey, provider, provCfg.model, langs.en, lang);
          if (translated) langs[lang] = translated;
        } catch(e) {}
      }
      calcRes.langs = langs;
      const docRef = db.collection("calc_pipeline").doc();
      const passesQuality = calcRes.inputs?.length > 0 && calcRes.outputs?.length > 0 &&
        calcRes.formula && calcRes.langs?.en?.name && calcRes.slug;
      const isHighConfidence = passesQuality && (
        (opp.source === "gsc" && ((opp.impressions || 0) >= 10 || (opp.trendMultiplier || 1) >= 1.5)) ||
        (opp.source === "ai_brainstorm" && passesQuality)
      );

      await docRef.set({
        status: isHighConfidence ? "auto_approved" : "pending",
        source: opp.source,
        source_queries: opp.queries,
        total_impressions: opp.impressions,
        avg_position: opp.avgPos,
        prompt: opp.prompt,
        generated_calc: calcRes,
        created_at: admin.firestore.FieldValue.serverTimestamp(),
      });

      if (isHighConfidence) {
        try {
          await db.collection("calc_cms").doc(calcRes.slug).set({
            ...calcRes, status: "published",
            created_at: admin.firestore.FieldValue.serverTimestamp(),
            updated_at: admin.firestore.FieldValue.serverTimestamp(),
          });
          const projectId = process.env.GCLOUD_PROJECT || "calctowork";
          const fetch = require("node-fetch");
          await fetch(`https://us-central1-${projectId}.cloudfunctions.net/publishCalcToHosting`, {
            method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ slug: calcRes.slug }),
          }).catch(e => console.warn("publishCalcToHosting self-call failed:", e.message));
          const sitemapUrl = "https://calcto.work/sitemap.xml";
          await Promise.allSettled([
            fetch(`https://www.google.com/ping?sitemap=${sitemapUrl}`),
            fetch(`https://www.bing.com/ping?sitemap=${encodeURIComponent(sitemapUrl)}`),
          ]);
          console.log("[AutoApprove] Auto-published:", calcRes.slug, `(${opp.impressions} impressions)`);
        } catch(e) { console.warn("Auto-approve failed:", calcRes.slug, e.message); }
      }

      saved.push(docRef.id);
    } catch(e) { console.warn("Failed to generate calc for:", opp.prompt, e.message); }
  }
  console.log("findKeywordOpportunities done:", saved.length, "drafts saved");
  return { drafts: saved.length, opportunities: allOpps.length };
}

/**
 * generateSEOSuggestions — Monday 7 AM: find underperforming pages, AI writes better titles
 */
exports.generateSEOSuggestions = functions.runWith({ timeoutSeconds: 300, memory: "256MB" })
  .pubsub.schedule("0 7 * * 1").timeZone("UTC").onRun(async () => {
  await _generateSEOSuggestions();
});

exports.generateSEOSuggestionsHttp = functions.runWith({ timeoutSeconds: 300, memory: "256MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  try {
    const result = await _generateSEOSuggestions();
    return res.status(200).json(result);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

async function _generateSEOSuggestions() {
  const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
  const cfg = cfgDoc.exists ? cfgDoc.data() : {};
  const provider = cfg.active_provider || "anthropic";
  const provCfg = (cfg.providers || {})[provider] || {};
  const apiKey = provCfg.api_key;
  if (!apiKey) return { skipped: true };

  // Load brain learnings + strategy so AI applies CTR patterns and respects focus areas
  const [learningsDoc, strategyDoc] = await Promise.all([
    db.collection("ai_brain").doc("learnings").get(),
    db.collection("ai_brain").doc("strategy").get(),
  ]);
  const learnings = learningsDoc.exists ? learningsDoc.data() : {};
  const strategy = strategyDoc.exists ? strategyDoc.data() : {};
  const ctrPatterns = [...(learnings.what_works||[]), ...(learnings.site_patterns||[])].slice(0,3).join(". ");
  const focusWords = (strategy.focus_areas||[]).flatMap(a=>a.toLowerCase().split(/[\s,]+/)).filter(w=>w.length>3);
  const avoidWords = (strategy.avoid_topics||[]).flatMap(a=>a.toLowerCase().split(/[\s,]+/)).filter(w=>w.length>3);

  const cutoff = new Date(Date.now() - 28 * 86400000).toISOString().slice(0, 10);

  // Build reverse slug map: {lang: {langSlug → cmsDocId}} so non-English pages resolve correctly
  const allCmsSnap = await db.collection("calc_cms").get();
  const slugMap = {};
  LANGS.forEach(l => slugMap[l] = {});
  allCmsSnap.forEach(doc => {
    slugMap.en[doc.id] = doc.id;
    LANGS.forEach(l => {
      if (l !== "en") {
        const langSlug = doc.data().langs?.[l]?.slug;
        if (langSlug) slugMap[l][langSlug] = doc.id;
      }
    });
  });

  // Aggregate page stats last 28 days — track lang + langSlug separately
  const snap = await db.collection("gsc_page_stats")
    .where("date", ">=", cutoff).orderBy("date","desc").limit(5000).get();

  const pageMap = {};
  snap.forEach(doc => {
    const d = doc.data();
    const parts = (d.page || "").replace("https://calcto.work/","").split("/").filter(Boolean);
    if (parts.length < 2) return;
    const [lang, langSlug] = parts;
    if (!LANGS.includes(lang)) return;
    const key = `${lang}::${langSlug}`;
    if (!pageMap[key]) pageMap[key] = { lang, langSlug, clicks:0, impressions:0, positions:[], ctrs:[] };
    pageMap[key].clicks += d.total_clicks || d.clicks || 0;
    pageMap[key].impressions += d.total_impressions || d.impressions || 0;
    if (d.avg_position || d.position) pageMap[key].positions.push(d.avg_position || d.position);
    if (d.avg_ctr || d.ctr) pageMap[key].ctrs.push(d.avg_ctr || d.ctr);
  });

  const avgCTR = Object.values(pageMap).reduce((s,p) => s + (p.ctrs[0]||0), 0) / Math.max(Object.keys(pageMap).length, 1);

  // Fetch existing pending suggestions to avoid duplicates (keyed as lang::cmsDocId)
  const existingSugSnap = await db.collection("seo_suggestions").where("status","==","pending").get();
  const existingSugKeys = new Set(existingSugSnap.docs.map(d => `${d.data().lang||"en"}::${d.data().slug}`).filter(Boolean));

  // Find position 5-20, CTR below average, ≥ 50 impressions — weighted by brain strategy
  const candidates = Object.values(pageMap)
    .map(d => {
      const position = d.positions.length ? d.positions.reduce((a,b)=>a+b)/d.positions.length : 50;
      const ctr = d.ctrs.length ? d.ctrs.reduce((a,b)=>a+b)/d.ctrs.length : 0;
      const cmsDocId = d.lang === "en" ? d.langSlug : (slugMap[d.lang]?.[d.langSlug] || null);
      if (!cmsDocId) return null;
      const slugWords = cmsDocId.split("-");
      const stratBoost = focusWords.length && focusWords.some(kw=>slugWords.some(w=>w.includes(kw))) ? 1.8 : 1;
      const avoidPenalty = avoidWords.length && avoidWords.some(kw=>slugWords.some(w=>w.includes(kw))) ? 0.15 : 1;
      return { lang: d.lang, langSlug: d.langSlug, cmsDocId, clicks: d.clicks, impressions: d.impressions, position, ctr, _score: d.impressions * stratBoost * avoidPenalty };
    })
    .filter(p => p && p.position >= 5 && p.position <= 20 && p.ctr < avgCTR && p.impressions >= 50)
    .filter(p => !existingSugKeys.has(`${p.lang}::${p.cmsDocId}`))
    .sort((a,b) => b._score - a._score)
    .slice(0, 12);

  const saved = [];
  for (const p of candidates) {
    try {
      let title = "", desc = "";
      const cmsDoc = await db.collection("calc_cms").doc(p.cmsDocId).get();
      if (cmsDoc.exists) {
        const langData = (cmsDoc.data().langs || {})[p.lang] || {};
        title = langData.seo_title || langData.name || "";
        desc = langData.seo_description || "";
      }

      const pageUrl = `https://calcto.work/${p.lang}/${p.langSlug}/`;
      const querySnap = await db.collection("gsc_search_data")
        .where("page", "==", pageUrl).where("date",">=",cutoff)
        .orderBy("impressions","desc").limit(5).get();
      const topQueries = querySnap.docs.map(d => d.data().query).filter(Boolean);

      const langLabel = { en:"English", fr:"French", de:"German", es:"Spanish", it:"Italian", pt:"Portuguese" }[p.lang] || p.lang;
      const prompt = `Rewrite the SEO title and meta description for this ${langLabel} calculator page to improve click-through rate. It currently ranks at position ${p.position.toFixed(1)} with ${(p.ctr*100).toFixed(1)}% CTR (below average).

Current title: "${title || p.langSlug}"
Current description: "${desc || "No description"}"
Impressions last 28 days: ${p.impressions}
Top search queries: ${topQueries.length ? topQueries.map(q=>`"${q}"`).join(", ") : "unknown"}
${ctrPatterns ? `\nKnown CTR patterns (apply these): ${ctrPatterns}` : ""}

Write the title and description IN ${langLabel.toUpperCase()}. Title under 60 chars, description under 155 chars.
Return JSON only: {"title":"new title","description":"new description","reasoning":"1 sentence why this will improve CTR"}`;

      const text = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 300);
      const m = text && text.replace(/<think>[\s\S]*?<\/think>/g,"").match(/\{[\s\S]*\}/);
      if (!m) continue;
      const suggestion = JSON.parse(m[0]);

      await db.collection("seo_suggestions").add({
        status: "pending",
        slug: p.cmsDocId,
        lang: p.lang,
        lang_slug: p.langSlug,
        current_title: title,
        current_desc: desc,
        current_position: p.position,
        current_ctr: p.ctr,
        impressions: p.impressions,
        suggested_title: suggestion.title,
        suggested_desc: suggestion.description,
        reasoning: suggestion.reasoning,
        created_at: admin.firestore.FieldValue.serverTimestamp(),
      });
      saved.push(`${p.lang}::${p.cmsDocId}`);
    } catch(e) { console.warn("SEO suggestion failed for", p.lang, p.cmsDocId, e.message); }
  }
  console.log("generateSEOSuggestions done:", saved.length, "across", new Set(saved.map(s=>s.split("::")[0])).size, "languages");

  // Auto-apply high-confidence stale suggestions: position > 12, impressions > 200, pending > 7 days
  let autoApplied = 0;
  try {
    const cutoff7d = admin.firestore.Timestamp.fromDate(new Date(Date.now() - 7 * 86400000));
    const staleSnap = await db.collection("seo_suggestions")
      .where("status", "==", "pending")
      .where("created_at", "<=", cutoff7d)
      .limit(20).get();

    const highConfidence = staleSnap.docs
      .filter(d => (d.data().current_position || 50) > 12 && (d.data().impressions || 0) > 200)
      .sort((a, b) => (b.data().impressions || 0) - (a.data().impressions || 0))
      .slice(0, 3);

    for (const sugDoc of highConfidence) {
      const s = sugDoc.data();
      if (!s.slug || !s.lang || !s.suggested_title) continue;
      try {
        const cmsDoc = await db.collection("calc_cms").doc(s.slug).get();
        if (!cmsDoc.exists) continue;
        const langData = (cmsDoc.data().langs || {})[s.lang] || {};
        const updatedLang = {
          ...langData,
          seo_title: s.suggested_title,
          ...(s.suggested_desc ? { seo_description: s.suggested_desc } : {}),
        };
        await cmsDoc.ref.update({
          [`langs.${s.lang}`]: updatedLang,
          updated_at: admin.firestore.FieldValue.serverTimestamp(),
        });
        await sugDoc.ref.update({
          status: "applied",
          applied_at: admin.firestore.FieldValue.serverTimestamp(),
          applied_by: "auto",
          position_at_apply: s.current_position,
        });
        autoApplied++;
        console.log(`[SEO Auto-apply] ${s.lang}::${s.slug} pos=${s.current_position?.toFixed(1)} imp=${s.impressions}`);
      } catch(e) { console.warn("[SEO Auto-apply] failed:", s.slug, e.message); }
    }
  } catch(e) { console.warn("[SEO Auto-apply] query error:", e.message); }

  return { suggestions: saved.length, auto_applied: autoApplied };
}

/**
 * generateGrowthReport — Monday 9 AM: AI reads all data and writes growth brief
 */
exports.generateGrowthReport = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .pubsub.schedule("0 9 * * 1").timeZone("UTC").onRun(async () => {
  await _generateGrowthReport();
});

exports.generateGrowthReportHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  try {
    const result = await _generateGrowthReport();
    return res.status(200).json(result);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

async function _measureSEOOutcomes() {
  try {
    // Find applied suggestions not yet measured
    const appliedSnap = await db.collection("seo_suggestions")
      .where("status","==","applied").orderBy("applied_at","desc").limit(30).get();
    if (appliedSnap.empty) return [];

    const outcomes = [];
    for (const doc of appliedSnap.docs) {
      const d = doc.data();
      if (d.outcome_measured || !d.slug) continue;
      // Only measure after 4 weeks have passed since application
      const appliedAt = d.applied_at?.toDate ? d.applied_at.toDate() : new Date(d.applied_at || d.reviewed_at || 0);
      if (Date.now() - appliedAt.getTime() < 28*86400000) continue;

      // Get recent GSC position for this slug — try both URL formats
      const [snap1, snap2] = await Promise.all([
        db.collection("gsc_page_stats").where("page","==",`https://calcto.work/en/${d.slug}/`).orderBy("date","desc").limit(14).get(),
        db.collection("gsc_page_stats").where("page","==",`https://calcto.work/en/${d.slug}`).orderBy("date","desc").limit(14).get(),
      ]);
      const allDocs = [...snap1.docs, ...snap2.docs];
      if (!allDocs.length) continue;

      const positions = allDocs.map(r => r.data().avg_position || r.data().position).filter(Boolean);
      const currentPos = positions.reduce((a,b)=>a+b,0) / positions.length;
      const positionBefore = d.position_at_apply || d.current_position;
      const delta = positionBefore ? Math.round((positionBefore - currentPos) * 10) / 10 : null;

      await doc.ref.update({ outcome_measured: true, position_after: parseFloat(currentPos.toFixed(1)), position_delta: delta });

      if (delta !== null) {
        outcomes.push({ slug: d.slug, before: positionBefore, after: parseFloat(currentPos.toFixed(1)), delta, improved: delta > 0 });
      }
    }

    if (outcomes.length) {
      const learningsDoc = await db.collection("ai_brain").doc("learnings").get();
      const existing = learningsDoc.exists ? (learningsDoc.data().seo_outcomes || []) : [];
      const newNotes = outcomes.map(o =>
        `${o.slug}: position ${o.before}→${o.after} (${o.improved ? "improved +" : "declined "}${Math.abs(o.delta)})`
      );
      await db.collection("ai_brain").doc("learnings").set({
        ...(learningsDoc.exists ? learningsDoc.data() : {}),
        seo_outcomes: [...newNotes, ...existing].slice(0, 15),
        last_updated: admin.firestore.FieldValue.serverTimestamp(),
      });
      console.log("measureSEOOutcomes:", outcomes.length, "outcomes recorded");
    }
    return outcomes;
  } catch(e) {
    console.warn("measureSEOOutcomes error:", e.message);
    return [];
  }
}

function _weekKey(offsetWeeks = 0) {
  const d = new Date(Date.now() - offsetWeeks * 7 * 86400000);
  return `${d.getFullYear()}-W${String(Math.ceil((d - new Date(d.getFullYear(),0,1))/604800000)).padStart(2,"0")}`;
}

async function _generateGrowthReport() {
  const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
  const cfg = cfgDoc.exists ? cfgDoc.data() : {};
  const provider = cfg.active_provider || "anthropic";
  const provCfg = (cfg.providers || {})[provider] || {};
  const apiKey = provCfg.api_key;
  if (!apiKey) return { skipped: true };

  // Measure SEO outcomes first so updated learnings are available below
  await _measureSEOOutcomes();

  const weekKey = _weekKey(0);
  const lastWeekKey = _weekKey(1);
  const cutoff14 = new Date(Date.now() - 14*86400000).toISOString().slice(0,10);
  const cutoff7 = new Date(Date.now() - 7*86400000).toISOString().slice(0,10);
  const monthStart = new Date(); monthStart.setDate(1); monthStart.setHours(0,0,0,0);

  // Load everything in parallel: brain memory + last week's report + current data
  const [strategyDoc, learningsDoc, lastWeekDoc, siteSnap, alertsSnap, pipelineSnap, cmsSnap, seoSnap, newCalcsSnap, dailySnap, querySnap] = await Promise.all([
    db.collection("ai_brain").doc("strategy").get(),
    db.collection("ai_brain").doc("learnings").get(),
    db.collection("growth_reports").doc(lastWeekKey).get(),
    db.collection("gsc_site_stats").where("date",">=",cutoff14).orderBy("date","desc").limit(14).get(),
    db.collection("dashboard_alerts").where("acknowledged","==",false).limit(10).get(),
    db.collection("calc_pipeline").where("status","==","pending").limit(10).get(),
    db.collection("calc_cms").where("status","==","published").orderBy("updated_at","desc").limit(5).get(),
    db.collection("seo_suggestions").where("status","==","pending").limit(5).get(),
    db.collection("calc_cms").where("status","==","published").where("created_at",">=",monthStart).get(),
    db.collection("analytics_daily").where("date",">=",cutoff7).limit(200).get(),
    db.collection("gsc_search_data").where("date",">=",cutoff7).orderBy("date","desc").limit(1000).get(),
  ]);

  const strategy = strategyDoc.exists ? strategyDoc.data() : {};
  const learnings = learningsDoc.exists ? learningsDoc.data() : {};
  const lastWeek = lastWeekDoc.exists ? lastWeekDoc.data() : null;

  // Auto-update monthly goal current counts so the AI sees accurate progress
  const newCalcsThisMonth = newCalcsSnap.size;
  if (strategy.monthly_goals?.length) {
    strategy.monthly_goals = strategy.monthly_goals.map(g => {
      if ((g.unit === "calcs" || (g.description||"").toLowerCase().includes("publish")) && typeof g.target === "number") {
        return { ...g, current: newCalcsThisMonth };
      }
      return g;
    });
  }

  // Evaluate last week's recommendations — try both URL formats to avoid miss
  let outcomeEval = "No previous recommendations to evaluate.";
  if (lastWeek?.recommendations?.length) {
    const outcomes = await Promise.all(lastWeek.recommendations.map(async rec => {
      if (!rec.slug) return `"${rec.action}": no slug tracked`;
      const [snap1, snap2] = await Promise.all([
        db.collection("gsc_page_stats").where("page","==",`https://calcto.work/en/${rec.slug}/`).where("date",">=",cutoff7).limit(14).get(),
        db.collection("gsc_page_stats").where("page","==",`https://calcto.work/en/${rec.slug}`).where("date",">=",cutoff7).limit(14).get(),
      ]);
      const allDocs = [...snap1.docs, ...snap2.docs];
      const impressions = allDocs.reduce((s,d)=>s+(d.data().total_impressions||d.data().impressions||0),0);
      const clicks = allDocs.reduce((s,d)=>s+(d.data().total_clicks||d.data().clicks||0),0);
      const status = impressions > 0 ? `got ${impressions} impressions, ${clicks} clicks` : "no GSC data yet (too new or not indexed)";
      return `"${rec.action}" (${rec.slug}): ${status} | expected: ${rec.expected_outcome||"not specified"}`;
    }));
    outcomeEval = outcomes.filter(Boolean).join("\n");
  }

  // Traffic data: last 7d vs prior 7d
  const siteData = [];
  siteSnap.forEach(d => siteData.push(d.data()));
  const last7data = siteData.filter(d => d.date >= cutoff7);
  const prior7data = siteData.filter(d => d.date >= cutoff14 && d.date < cutoff7);
  const clicks7 = last7data.reduce((s,d)=>s+(d.total_clicks||0),0);
  const impressions7 = last7data.reduce((s,d)=>s+(d.total_impressions||0),0);
  const clicksPrior7 = prior7data.reduce((s,d)=>s+(d.total_clicks||0),0);
  const impressionsPrior7 = prior7data.reduce((s,d)=>s+(d.total_impressions||0),0);
  const clicksChange = clicksPrior7 > 0 ? Math.round((clicks7-clicksPrior7)/clicksPrior7*100) : null;
  const impressionsChange = impressionsPrior7 > 0 ? Math.round((impressions7-impressionsPrior7)/impressionsPrior7*100) : null;

  const pageSnap = await db.collection("gsc_page_stats").where("date",">=",cutoff7).orderBy("date","desc").limit(500).get();
  const pageClicks = {};
  pageSnap.forEach(d => {
    const slug = (d.data().page||"").replace("https://calcto.work/","").split("/")[1]||"";
    if (slug) pageClicks[slug] = (pageClicks[slug]||0) + (d.data().total_clicks||d.data().clicks||0);
  });
  const topPages = Object.entries(pageClicks).sort((a,b)=>b[1]-a[1]).slice(0,5).map(([s,c])=>`${s}(${c})`).join(", ");

  // Category-level traffic aggregation so the AI can make strategy decisions by domain
  const CATEGORY_KEYWORDS = {
    construction: ["beam","pipe","concrete","rebar","steel","weight","load","bolt","weld","truss","soil","brick","timber","roof"],
    finance: ["tax","mortgage","loan","interest","roi","profit","margin","salary","pension","vat","depreciation","budget","investment"],
    health: ["bmi","calorie","calories","heart","pregnancy","blood","medication","dose","sleep","fitness","body","age"],
    math: ["area","volume","circle","triangle","percentage","fraction","prime","factorial","matrix","geometry","perimeter"],
    engineering: ["voltage","current","power","ohm","flow","pressure","temperature","torque","rpm","resistance","energy"],
  };
  const catClicks = {};
  Object.entries(pageClicks).forEach(([slug, clicks]) => {
    const slugWords = slug.toLowerCase().split("-");
    for (const [cat, keywords] of Object.entries(CATEGORY_KEYWORDS)) {
      if (keywords.some(kw => slugWords.includes(kw))) { catClicks[cat] = (catClicks[cat]||0) + clicks; break; }
    }
  });
  const topCategories = Object.entries(catClicks).filter(([,c])=>c>0).sort((a,b)=>b[1]-a[1])
    .map(([cat,c])=>`${cat}(${c} clicks)`).join(", ");

  const alerts = [];
  alertsSnap.forEach(d => alerts.push(d.data().message || d.data().title || "alert"));
  const recentCms = [];
  cmsSnap.forEach(d => recentCms.push(d.data().langs?.en?.name || d.id));

  // analytics_daily: calculation rate and engagement by page slug
  const slugEngagement = {};
  dailySnap.forEach(d => {
    const dd = d.data();
    const slug = dd.slug || dd.calc_slug || dd.page_slug || "";
    if (!slug) return;
    if (!slugEngagement[slug]) slugEngagement[slug] = { views: 0, calcs: 0 };
    slugEngagement[slug].views += dd.pageviews || dd.views || 0;
    slugEngagement[slug].calcs += dd.calcs || dd.calculations || 0;
  });
  // Top 5 by calculation rate (min 10 views)
  const topByEngagement = Object.entries(slugEngagement)
    .filter(([, v]) => v.views >= 10)
    .map(([slug, v]) => ({ slug, rate: Math.round(v.calcs / v.views * 100), views: v.views, calcs: v.calcs }))
    .sort((a, b) => b.rate - a.rate).slice(0, 5);
  // Overall site calculation rate
  const totalViews = Object.values(slugEngagement).reduce((s, v) => s + v.views, 0);
  const totalCalcs = Object.values(slugEngagement).reduce((s, v) => s + v.calcs, 0);
  const siteCalcRate = totalViews > 0 ? Math.round(totalCalcs / totalViews * 100) : null;

  // gsc_search_data: top queries with high impressions but no matching calculator (gaps)
  const queryMap = {};
  querySnap.forEach(d => {
    const dd = d.data();
    const q = (dd.query || "").toLowerCase().trim();
    if (!q || q.length < 4) return;
    if (!queryMap[q]) queryMap[q] = { impressions: 0, clicks: 0, position: [] };
    queryMap[q].impressions += dd.impressions || 0;
    queryMap[q].clicks += dd.clicks || 0;
    if (dd.position) queryMap[q].position.push(dd.position);
  });
  const topQueries = Object.entries(queryMap)
    .sort((a, b) => b[1].impressions - a[1].impressions).slice(0, 20)
    .map(([q, v]) => {
      const avgPos = v.position.length ? (v.position.reduce((a, b) => a + b) / v.position.length).toFixed(1) : "?";
      const ctr = v.impressions > 0 ? (v.clicks / v.impressions * 100).toFixed(1) : "0";
      return `"${q}" (${v.impressions} imp, pos ${avgPos}, ${ctr}% CTR)`;
    }).join(", ");
  // Identify query gaps: high impressions, position > 15 (not yet ranking well)
  const queryGaps = Object.entries(queryMap)
    .filter(([, v]) => v.impressions >= 50 && v.position.length && (v.position.reduce((a, b) => a + b) / v.position.length) > 15)
    .sort((a, b) => b[1].impressions - a[1].impressions).slice(0, 5)
    .map(([q, v]) => `"${q}" (${v.impressions} imp, no strong ranking)`).join(", ");

  const trafficChangeStr = clicksChange !== null ? `${clicksChange>0?"+":""}${clicksChange}% clicks` : "first week of data";

  // Build the full brain-aware prompt
  const prompt = `You are the AI growth brain for CalcToWork, a multilingual calculator site (461+ calculators, 6 languages). You have persistent memory of past decisions and their outcomes. Use it to make smarter decisions this week.

═══ PERSISTENT MEMORY ═══
STRATEGY (what you decided to focus on):
${Object.keys(strategy).length ? JSON.stringify(strategy, null, 2) : "No strategy set yet — this is your first run. Derive one from the data below."}

ACCUMULATED LEARNINGS (what you've discovered works/doesn't):
${Object.keys(learnings).length ? JSON.stringify(learnings, null, 2) : "No learnings yet — start building them."}

═══ LAST WEEK OUTCOME ═══
${outcomeEval}

═══ THIS WEEK'S DATA ═══
Clicks: ${clicks7}${clicksChange !== null ? ` (${clicksChange>0?"+":""}${clicksChange}% vs last week)` : " (first data point)"}
Impressions: ${impressions7}${impressionsChange !== null ? ` (${impressionsChange>0?"+":""}${impressionsChange}% vs last week)` : ""}
Top pages by clicks: ${topPages || "no data yet"}
Traffic by category: ${topCategories || "no data yet"}
New calcs published this month: ${newCalcsThisMonth}
Unread alerts: ${alerts.length ? alerts.join("; ") : "none"}
Pipeline drafts awaiting approval: ${pipelineSnap.size}
SEO suggestions pending: ${seoSnap.size}
Recently published CMS calcs: ${recentCms.join(", ") || "none"}

═══ USER ENGAGEMENT (analytics_daily) ═══
Site-wide calculation rate: ${siteCalcRate !== null ? siteCalcRate + "% of visitors actually complete a calculation" : "no data yet"}
Top calculators by engagement rate (calcs/views):
${topByEngagement.length ? topByEngagement.map(e => `  - ${e.slug}: ${e.rate}% calc rate (${e.calcs} calcs from ${e.views} views)`).join("\n") : "  No engagement data yet"}
NOTE: High calc rate = users find this calculator useful and complete it. Focus on these categories for new calcs.

═══ SEARCH QUERY INTELLIGENCE (gsc_search_data) ═══
Top queries driving traffic: ${topQueries || "no query data yet"}
HIGH-OPPORTUNITY GAPS (high impressions, not ranking well — build these calculators):
${queryGaps || "No clear gaps identified yet — need more GSC data"}
NOTE: Query gaps = users are searching for these but we don't have a strong calculator for them yet.

═══ INSTRUCTIONS ═══
1. Evaluate: Did last week's recommendations work? Update your learnings accordingly.
2. Revise strategy if the category data shows a better direction.
3. Set 3 concrete actions for this week that build on the strategy — not generic advice.
4. Make recommendations with specific calculator slugs/keywords so outcomes can be measured next week.

Return raw JSON only (no markdown fences):
{
  "brief": {
    "headline": "One punchy sentence",
    "traffic_change": "${trafficChangeStr}",
    "top_win": "Best thing this week",
    "top_problem": "Biggest issue + what to do",
    "action_1": {"what":"","why":"","how":""},
    "action_2": {"what":"","why":"","how":""},
    "action_3": {"what":"","why":"","how":""},
    "calc_idea": "Specific calculator to create and why"
  },
  "updated_strategy": {
    "focus_areas": ["list of 2-4 topic areas to double down on"],
    "avoid_topics": ["topics that aren't working"],
    "known_patterns": ["data-backed patterns you've observed"],
    "monthly_goals": [{"id":"","description":"","target":0,"current":0,"unit":"","deadline":"YYYY-MM-DD"}]
  },
  "updated_learnings": {
    "what_works": ["specific findings about what drives traffic/CTR"],
    "what_doesnt": ["specific findings about what wastes effort"],
    "site_patterns": ["measurable patterns about this site"],
    "seo_outcomes": ["keep existing SEO outcome entries from learnings — add new ones if applicable"]
  },
  "recommendations": [
    {"action":"","expected_outcome":"","metric":"gsc_impressions|gsc_clicks|ctr","slug":"calculator-slug-if-applicable"}
  ]
}`;

  const raw = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 2500);
  if (!raw) return { skipped: true };

  // Parse AI response (strip think blocks, extract JSON)
  let text = raw.replace(/<think>[\s\S]*?<\/think>/g, "").trim();
  const match = text.match(/\{[\s\S]*\}/);
  if (!match) { console.error("Brain: no JSON in AI response"); return { skipped: true }; }
  let parsed;
  try { parsed = JSON.parse(match[0]); }
  catch(e) {
    try { parsed = JSON.parse(match[0].replace(/,\s*([}\]])/g,"$1")); }
    catch(e2) { console.error("Brain: JSON parse failed", e2.message); return { skipped: true }; }
  }

  const briefJson = JSON.stringify(parsed.brief || parsed);

  // Write brief + save updated brain memory
  await Promise.all([
    db.collection("growth_reports").doc(weekKey).set({
      week: weekKey,
      generated_at: admin.firestore.FieldValue.serverTimestamp(),
      brief: briefJson,
      recommendations: parsed.recommendations || [],
      data_snapshot: { clicks_7d: clicks7, impressions_7d: impressions7, clicks_change_pct: clicksChange, alerts_count: alerts.length, pipeline_count: pipelineSnap.size, seo_count: seoSnap.size },
    }),
    parsed.updated_strategy && db.collection("ai_brain").doc("strategy").set({
      ...parsed.updated_strategy,
      last_updated: admin.firestore.FieldValue.serverTimestamp(),
    }),
    parsed.updated_learnings && db.collection("ai_brain").doc("learnings").set({
      ...parsed.updated_learnings,
      last_updated: admin.firestore.FieldValue.serverTimestamp(),
    }),
  ].filter(Boolean));

  // Auto-create pipeline entry from AI's calc_idea so Monday's insight feeds Tuesday's pipeline
  const calcIdea = parsed.brief?.calc_idea;
  if (calcIdea && typeof calcIdea === "string" && calcIdea.length > 10) {
    try {
      const ideaCalc = await _generateCalcRaw(apiKey, provider, provCfg.model, calcIdea);
      if (ideaCalc?.slug && ideaCalc?.langs?.en?.name) {
        // Auto-translate all languages
        const ideaLangs = ideaCalc.langs || {};
        for (const lang of LANGS) {
          if (lang === "en" || ideaLangs[lang]?.name) continue;
          try {
            const tr = await _translateRaw(apiKey, provider, provCfg.model, ideaLangs.en, lang);
            if (tr) ideaLangs[lang] = tr;
          } catch(e) {}
        }
        ideaCalc.langs = ideaLangs;
        await db.collection("calc_pipeline").add({
          status: "pending",
          source: "growth_report_idea",
          source_queries: [],
          prompt: calcIdea,
          generated_calc: ideaCalc,
          week: weekKey,
          created_at: admin.firestore.FieldValue.serverTimestamp(),
        });
        console.log("[GrowthReport] calc_idea auto-added to pipeline:", ideaCalc.slug);
      }
    } catch(ideaErr) { console.warn("[GrowthReport] calc_idea pipeline failed:", ideaErr.message); }
  }

  console.log("generateGrowthReport done:", weekKey, "| brain updated:", !!parsed.updated_strategy);
  return { week: weekKey, brief: briefJson };
}

/**
 * runAutoPilotHttp — background additive-only improvements (no approval needed)
 */
exports.runAutoPilotHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  try {
    const result = await _runAutoPilot();
    return res.status(200).json(result);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

exports.runAutoPilot = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .pubsub.schedule("0 10 * * 1").timeZone("UTC").onRun(async () => {
  await _runAutoPilot();
});

const ENGLISH_LEAKAGE_WORDS = ["calculator", " the ", " and ", " of ", " for ", " to ", " with ", " a calculator"];

async function _autoPilotProcessDoc(doc, apiKey, provider, model, results, calcNameMap = {}, trafficBySlug = {}) {
  const data = doc.data();
  const langs = data.langs || {};
  const inputs = data.inputs || [];
  if (!langs.en?.name) return;
  let updated = false;
  const updatedLangs = { ...langs };

  // 1. Translate missing languages with quality check
  for (const lang of LANGS) {
    if (lang === "en" || updatedLangs[lang]?.name) continue;
    try {
      await new Promise(r => setTimeout(r, 500));
      const translated = await _translateRaw(apiKey, provider, model, langs.en, lang);
      if (translated) {
        const nameLC = (translated.name || "").toLowerCase();
        const hasLeakage = ENGLISH_LEAKAGE_WORDS.some(w => nameLC.includes(w));
        if (hasLeakage) {
          console.warn(`[AutoPilot QA] ${doc.id} ${lang} name="${translated.name}" — possible English leakage, flagged`);
          updatedLangs[lang] = { ...translated, qa_warning: true };
        } else {
          updatedLangs[lang] = translated;
        }
        updated = true; results.translations++;
      }
    } catch(e) { console.warn("translate failed:", doc.id, lang, e.message); }
  }

  if (!langs.en.seo_description && langs.en.name) {
    try {
      const descHint = langs.en.desc ? ` It ${langs.en.desc.slice(0, 120)}.` : '';
      const formulaHint = data.formula ? ` Uses the formula: ${data.formula}.` : '';
      const desc = await _callAIRaw(apiKey, provider, model,
        `Write a compelling meta description (max 155 chars) for a web calculator called "${langs.en.name}".${descHint}${formulaHint} Include a benefit and a call to action. Return only the description text, no quotes.`, 160);
      if (desc) { updatedLangs.en = { ...updatedLangs.en, seo_description: desc.trim().slice(0,155) }; updated = true; results.metaFixed++; }
    } catch(e) {}
  }

  const contentAge = data.updated_at?.toDate ? Date.now() - data.updated_at.toDate().getTime() : 0;
  const isStale = langs.en.long_content && langs.en.long_content.length >= 800 &&
    contentAge > 180 * 86400000 && (trafficBySlug[doc.id] || 0) > 0;
  if ((!langs.en.long_content || langs.en.long_content.length < 800 || isStale) && langs.en.name) {
    try {
      // Build a rich context object from all available calc data so the AI writes accurate, specific content
      const inputFields = (data.inputs || []).map(i => `${i.id}${i.unit ? ' (' + i.unit + ')' : ''}`).join(', ') || 'see calculator inputs';
      const outputFields = (data.outputs || []).map(o => `${o.id}${o.unit ? ' (' + o.unit + ')' : ''}`).join(', ') || 'see calculator outputs';
      const formula = data.formula || langs.en.formula_display || '';
      const desc = langs.en.desc || '';
      const steps = (langs.en.steps || []).filter(Boolean).join(' → ') || '';
      const mistakes = (langs.en.mistakes || []).filter(Boolean).slice(0, 3).join('; ') || '';
      const exampleLabel = langs.en.example_label || '';
      const resultCtx = langs.en.result_context || '';

      const longContentPrompt = `You are a technical writer creating a high-quality, SEO-optimised article for a calculator page. This content must be optimised for both Google search snippets and AI answer engines (ChatGPT, Perplexity, Gemini) — meaning it must answer the user's question DIRECTLY and IMMEDIATELY in the first sentence.

Calculator: "${langs.en.name}"
Description: ${desc || 'A practical calculator tool'}
Inputs: ${inputFields}
Outputs: ${outputFields}
${formula ? `Formula: ${formula}` : ''}
${steps ? `How it works: ${steps}` : ''}
${exampleLabel ? `Example scenario: ${exampleLabel}` : ''}
${resultCtx ? `Result context: ${resultCtx}` : ''}
${mistakes ? `Common mistakes to address: ${mistakes}` : ''}

Write a thorough 1000+ word HTML article. Requirements:
- Use ONLY these HTML tags: <h2>, <h3>, <p>, <ul>, <ol>, <li>, <strong>, <em>, <table>, <thead>, <tbody>, <tr>, <th>, <td>
- Use single quotes in any HTML attributes (e.g. class='...')
- NO <html>, <head>, <body>, <div> wrapper tags — just the content
- Include these sections in order:
  1. <p><strong>TL;DR:</strong> One sentence that directly answers "how to calculate [this]" — include the formula or key insight immediately. This is the featured snippet target.</p>
  2. <h2>What Is the ${langs.en.name}?</h2> — explain what it calculates and who needs it (2–3 paragraphs, real-world context)
  3. <h2>How to Use the Calculator</h2> — step-by-step numbered list using the actual input fields listed above
  4. <h2>Formula and Calculation Method</h2> — explain the formula in plain language, show it, walk through a concrete worked example with real numbers
  5. <h2>Practical Examples</h2> — 2–3 realistic scenarios with different inputs and what the result means (use a table if helpful)
  6. <h2>Tips for Accurate Results</h2> — specific tips based on the actual inputs, common pitfalls, unit gotchas
  7. <h2>Frequently Asked Questions</h2> — 3 specific questions someone would actually search for, with detailed answers

Write accurate, specific content using the formula and field names provided. Do not invent features that don't exist. Do not be vague.`;

      const html = await _callAIRaw(apiKey, provider, model, longContentPrompt, 6000);
      if (html && html.length > 600) { updatedLangs.en = { ...updatedLangs.en, long_content: html.trim() }; updated = true; results.longContentFixed++; }
    } catch(e) { console.warn("long_content gen failed:", doc.id, e.message); }
  }

  if (inputs.length > 0 && !langs.en.inputs_labels) {
    try {
      const idList = inputs.map(i => i.id).join(", ");
      const raw = await _callAIRaw(apiKey, provider, model,
        `For a calculator called "${langs.en.name}", convert these field IDs to short human-readable English labels (2-4 words each, include unit if obvious from the ID): ${idList}. Return JSON object: {"field_id":"Label (unit)"}`, 200);
      const m = raw && raw.match(/\{[\s\S]*\}/);
      if (m) { updatedLangs.en = { ...updatedLangs.en, inputs_labels: JSON.parse(m[0]) }; updated = true; results.labelsFixed++; }
    } catch(e) {}
  }

  // 5. Generate missing or thin FAQ (needed for FAQPage JSON-LD rich snippets)
  if (langs.en.name && (!langs.en.faq || langs.en.faq.length < 3)) {
    try {
      const raw = await _callAIRaw(apiKey, provider, model,
        `Write 4 FAQ items for a calculator called "${langs.en.name}". Each answer must be at least 2 full sentences. Return JSON array only: [{"q":"Question?","a":"Answer."}]`, 600);
      const m = raw && raw.replace(/<think>[\s\S]*?<\/think>/g,"").match(/\[[\s\S]*\]/);
      if (m) {
        const faq = JSON.parse(m[0]);
        if (Array.isArray(faq) && faq.length >= 3) {
          updatedLangs.en = { ...updatedLangs.en, faq };
          updated = true; results.faqFixed = (results.faqFixed || 0) + 1;
        }
      }
    } catch(e) { console.warn("FAQ gen failed:", doc.id, e.message); }
  }

  // 6. Translate FAQ to langs that have a translation but no FAQ yet
  const enFaqNow = updatedLangs.en?.faq;
  if (enFaqNow && enFaqNow.length >= 3) {
    const langNames = { es:"Spanish", fr:"French", de:"German", it:"Italian", pt:"Portuguese" };
    for (const lang of LANGS) {
      if (lang === "en" || !updatedLangs[lang]?.name || (updatedLangs[lang].faq && updatedLangs[lang].faq.length >= 3)) continue;
      try {
        await new Promise(r => setTimeout(r, 300));
        const raw = await _callAIRaw(apiKey, provider, model,
          `Translate these FAQ items to ${langNames[lang]}. Return only a JSON array with the same structure: ${JSON.stringify(enFaqNow)}`, 800);
        const m = raw && raw.replace(/<think>[\s\S]*?<\/think>/g,"").match(/\[[\s\S]*\]/);
        if (m) {
          const translatedFaq = JSON.parse(m[0]);
          if (Array.isArray(translatedFaq) && translatedFaq.length >= 3) {
            updatedLangs[lang] = { ...updatedLangs[lang], faq: translatedFaq };
            updated = true; results.faqTranslated = (results.faqTranslated || 0) + 1;
          }
        }
      } catch(e) { console.warn("FAQ translate failed:", doc.id, lang, e.message); }
    }
  }

  // 7. Smart internal linking — score candidates by keyword overlap + category + traffic
  if (updatedLangs.en?.long_content && Object.keys(calcNameMap).length > 2) {
    try {
      const myWords = new Set(doc.id.split('-').filter(w => w.length > 3));
      const myCategory = doc.data().category || "";
      const candidates = Object.entries(calcNameMap)
        .filter(([slug]) => slug !== doc.id)
        .map(([slug, name]) => {
          const slugWords = slug.split('-');
          const overlap = slugWords.filter(w => myWords.has(w)).length;
          const traffic = trafficBySlug[slug] || 0;
          // score: keyword overlap (most important) + traffic bonus + category match
          const score = (overlap * 3) + (traffic > 0 ? 1 : 0) + (name.category === myCategory ? 1 : 0);
          return { slug, name: typeof name === "string" ? name : name.name || slug, score, overlap };
        })
        .filter(c => c.score >= 1)
        .sort((a, b) => b.score - a.score)
        .slice(0, 5);

      if (candidates.length >= 2) {
        // Replace "Related Calculators" section if exists, else append
        const top5 = candidates.slice(0, 5);
        const relSection = `<h2>Related Calculators</h2><ul>${top5.map(c => `<li><a href='/en/${c.slug}/'>${c.name}</a></li>`).join('')}</ul>`;
        let lc = updatedLangs.en.long_content;
        if (lc.includes('Related Calculators')) {
          lc = lc.replace(/<h2>Related Calculators<\/h2>[\s\S]*?<\/ul>/, relSection);
        } else {
          lc = lc + relSection;
        }
        // Also inject one contextual link into the first paragraph if possible
        const top1 = candidates[0];
        const linkText = top1.name;
        const linkHtml = `<a href='/en/${top1.slug}/'>${linkText}</a>`;
        if (!lc.includes(`href='/en/${top1.slug}/'`)) {
          // Find first </p> and try to insert a sentence before it
          lc = lc.replace(/(<\/p>)/, ` See also our ${linkHtml}.$1`);
        }
        updatedLangs.en = { ...updatedLangs.en, long_content: lc };
        updated = true; results.linksAdded = (results.linksAdded || 0) + 1;
      }
    } catch(e) { console.warn("internal linking failed:", doc.id, e.message); }
  }

  if (updated) {
    await doc.ref.update({ langs: updatedLangs, updated_at: admin.firestore.FieldValue.serverTimestamp() });
  }
}

/**
 * Rising Pages Audit — detects pages spiking in real-time analytics and fixes quality issues
 * before Google's ranking window closes. Uses analytics_events (not GSC — no lag).
 */
async function _auditRisingPages() {
  const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
  const cfg = cfgDoc.exists ? cfgDoc.data() : {};
  const provider = cfg.active_provider || "anthropic";
  const provCfg = (cfg.providers || {})[provider] || {};
  const apiKey = provCfg.api_key;
  if (!apiKey) return { skipped: true };

  // Compare last 24h vs same 24h one week ago to detect anomalies
  const now = new Date();
  const h24ago  = new Date(now - 24 * 3600000);
  const h48ago  = new Date(now - 48 * 3600000);
  const h192ago = new Date(now - (24 + 168) * 3600000); // 24h window, 7 days back
  const h216ago = new Date(now - (48 + 168) * 3600000);

  const toTS = d => admin.firestore.Timestamp.fromDate(d);

  const [recentSnap, baselineSnap] = await Promise.all([
    db.collection("analytics_events")
      .where("event_time", ">=", toTS(h24ago))
      .where("event_name", "==", "page_view")
      .limit(3000).get(),
    db.collection("analytics_events")
      .where("event_time", ">=", toTS(h192ago))
      .where("event_time", "<", toTS(h216ago))
      .where("event_name", "==", "page_view")
      .limit(3000).get(),
  ]);

  // Aggregate page views by calc_slug
  const recent = {};
  recentSnap.forEach(d => {
    const slug = d.data().calc_slug;
    if (slug) recent[slug] = (recent[slug] || 0) + 1;
  });

  const baseline = {};
  baselineSnap.forEach(d => {
    const slug = d.data().calc_slug;
    if (slug) baseline[slug] = (baseline[slug] || 0) + 1;
  });

  // Find rising pages: ≥5 views today AND ≥60% more than baseline
  const rising = Object.entries(recent)
    .map(([slug, views]) => {
      const base = baseline[slug] || 0;
      const growth = base > 0 ? (views - base) / base : views >= 10 ? 1 : 0;
      return { slug, views, base, growth };
    })
    .filter(p => p.views >= 5 && p.growth >= 0.6)
    .sort((a, b) => b.growth - a.growth)
    .slice(0, 8);

  if (rising.length === 0) {
    console.log("[RisingAudit] No rising pages detected today");
    return { rising: 0, fixed: 0 };
  }

  console.log(`[RisingAudit] ${rising.length} rising pages: ${rising.map(p => `${p.slug}(+${Math.round(p.growth*100)}%)`).join(", ")}`);

  // Build reverse slug map for non-EN languages
  const allCmsSnap = await db.collection("calc_cms").where("status","==","published").get();
  const slugToCmsId = {};
  allCmsSnap.forEach(doc => {
    slugToCmsId[`en/${doc.id}`] = doc.id;
    LANGS.forEach(l => {
      const lSlug = doc.data().langs?.[l]?.slug;
      if (lSlug) slugToCmsId[`${l}/${lSlug}`] = doc.id;
    });
  });

  const calcNameMap = {};
  allCmsSnap.forEach(d => { if (d.data().langs?.en?.name) calcNameMap[d.id] = d.data().langs.en.name; });

  let fixedCount = 0;
  const auditLog = [];

  for (const page of rising) {
    const cmsId = slugToCmsId[page.slug];
    if (!cmsId) {
      // Static page — log for visibility but can't auto-fix
      auditLog.push({ slug: page.slug, type: "static", growth: page.growth, views: page.views, issues: ["static page — manual review needed"] });
      continue;
    }

    const doc = await db.collection("calc_cms").doc(cmsId).get();
    if (!doc.exists) continue;
    const data = doc.data();
    const langs = data.langs || {};
    const issues = [];

    // Audit quality
    if (!data.formula || data.formula.length < 10)         issues.push("missing formula");
    if (!data.inputs || data.inputs.length < 1)             issues.push("no inputs defined");
    if (!langs.en?.long_content || langs.en.long_content.length < 800) issues.push("thin long_content (<800 chars)");
    if (!langs.en?.faq || langs.en.faq.length < 3)         issues.push("missing FAQ");
    const missingLangs = LANGS.filter(l => !langs[l]?.name);
    if (missingLangs.length > 0)                            issues.push(`missing translations: ${missingLangs.join(",")}`);
    const langSlugs = LANGS.filter(l => langs[l]?.name && !langs[l]?.slug);
    if (langSlugs.length > 0)                               issues.push(`missing slugs: ${langSlugs.join(",")}`);

    auditLog.push({ slug: page.slug, cmsId, growth: Math.round(page.growth * 100), views: page.views, issues });

    if (issues.length === 0) {
      console.log(`[RisingAudit] ${page.slug} — no issues found, already high quality`);
      continue;
    }

    console.log(`[RisingAudit] ${page.slug} rising +${Math.round(page.growth*100)}% — fixing: ${issues.join("; ")}`);

    // Fix via autopilot logic — pass a synthetic doc wrapper
    try {
      const results = { translations: 0, metaFixed: 0, longContentFixed: 0, labelsFixed: 0, faqFixed: 0, faqTranslated: 0, linksAdded: 0 };
      await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, calcNameMap, {});
      fixedCount++;
      console.log(`[RisingAudit] ${cmsId} fixed:`, results);
    } catch(e) { console.warn(`[RisingAudit] Fix failed for ${cmsId}:`, e.message); }
  }

  // Save audit to Firestore so dashboard can show it
  await db.collection("rising_page_audits").add({
    created_at: admin.firestore.FieldValue.serverTimestamp(),
    rising_count: rising.length,
    fixed_count: fixedCount,
    pages: auditLog,
  });

  // Create dashboard alert if issues were found
  const pagesWithIssues = auditLog.filter(p => p.issues && p.issues.length > 0);
  if (pagesWithIssues.length > 0) {
    await db.collection("dashboard_alerts").add({
      type: "rising_page_quality",
      severity: "medium",
      title: `${pagesWithIssues.length} rising page${pagesWithIssues.length > 1 ? "s" : ""} had quality issues — autopilot fixed them. Top: ${pagesWithIssues[0].slug} (+${pagesWithIssues[0].growth}% views)`,
      metric: "page_quality",
      current_value: fixedCount,
      previous_value: 0,
      change_pct: 0,
      period: "today",
      acknowledged: false,
      details: pagesWithIssues.slice(0, 5),
      created_at: admin.firestore.FieldValue.serverTimestamp(),
    });
  }

  return { rising: rising.length, fixed: fixedCount, issues_found: pagesWithIssues.length };
}

exports.auditRisingPagesHttp = functions.runWith({ timeoutSeconds: 300, memory: "256MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  try {
    const result = await _auditRisingPages();
    return res.status(200).json(result);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

// Run daily at 14:00 UTC — catches morning traffic spikes with enough data
exports.auditRisingPages = functions.runWith({ timeoutSeconds: 300, memory: "256MB" })
  .pubsub.schedule("0 14 * * *").timeZone("UTC").onRun(async () => {
  await _auditRisingPages();
});

async function _runAutoPilot() {
  const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
  const cfg = cfgDoc.exists ? cfgDoc.data() : {};
  const provider = cfg.active_provider || "anthropic";
  const provCfg = (cfg.providers || {})[provider] || {};
  const apiKey = provCfg.api_key;
  if (!apiKey) return { skipped: true };

  const results = { translations: 0, metaFixed: 0, longContentFixed: 0, labelsFixed: 0, faqFixed: 0, faqTranslated: 0, linksAdded: 0 };
  const processedSlugs = new Set();
  let batchNum = 0;
  const MAX_BATCHES = 5; // up to 100 calcs total

  // Phase 1: Process high-traffic calcs first (sorted by real GSC clicks)
  const cutoff30 = new Date(Date.now()-30*86400000).toISOString().slice(0,10);
  const [trafficSnap, nameSnap] = await Promise.all([
    db.collection("gsc_page_stats").where("date",">=",cutoff30).limit(5000).get(),
    db.collection("calc_cms").where("status","==","published").limit(200).get(),
  ]);
  const trafficBySlug = {};
  trafficSnap.forEach(d => {
    const slug = (d.data().page||"").replace("https://calcto.work/","").split("/")[1]||"";
    if (slug) trafficBySlug[slug] = (trafficBySlug[slug]||0) + (d.data().total_clicks||d.data().clicks||0);
  });
  const calcNameMap = {};
  nameSnap.forEach(d => { if (d.data().langs?.en?.name) calcNameMap[d.id] = d.data().langs.en.name; });

  // Build position velocity map: pages at pos 11-20 that dropped ≥3 positions week-over-week
  const cutoff14 = new Date(Date.now()-14*86400000).toISOString().slice(0,10);
  const cutoff7 = new Date(Date.now()-7*86400000).toISOString().slice(0,10);
  const velocitySnap = await db.collection("gsc_page_stats").where("date",">=",cutoff14).limit(3000).get();
  const vel7 = {}, velPrior = {};
  velocitySnap.forEach(d => {
    const slug = (d.data().page||"").replace("https://calcto.work/","").split("/")[1]||"";
    const date = d.data().date || "";
    const pos = d.data().avg_position || d.data().position || 0;
    if (!slug || !pos) return;
    if (date >= cutoff7) { if (!vel7[slug]) vel7[slug] = []; vel7[slug].push(pos); }
    else { if (!velPrior[slug]) velPrior[slug] = []; velPrior[slug].push(pos); }
  });
  const fallingPages = new Set();
  for (const [slug, positions] of Object.entries(vel7)) {
    const recent = positions.reduce((a,b)=>a+b)/positions.length;
    const prior = velPrior[slug]?.length ? velPrior[slug].reduce((a,b)=>a+b)/velPrior[slug].length : null;
    if (prior && recent >= 11 && recent <= 25 && (recent - prior) >= 3) fallingPages.add(slug);
  }
  console.log(`[AutoPilot] ${fallingPages.size} pages detected as falling in rankings — prioritizing`);

  // Phase 0: Process falling pages first so they get content refresh before budget runs out
  if (fallingPages.size > 0) {
    const fallingDocs = await Promise.all([...fallingPages].slice(0,10).map(s => db.collection("calc_cms").doc(s).get()));
    for (const doc of fallingDocs) {
      if (!doc.exists || doc.data().status !== "published" || processedSlugs.has(doc.id)) continue;
      // Force stale so autopilot refreshes long_content even if it was generated recently
      await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, calcNameMap, trafficBySlug);
      processedSlugs.add(doc.id);
    }
  }

  const rankedSlugs = Object.entries(trafficBySlug).sort((a,b)=>b[1]-a[1]).map(([s])=>s).slice(0,60);

  for (let i = 0; i < rankedSlugs.length && batchNum < 3; i += 20) {
    const slugBatch = rankedSlugs.slice(i, i+20);
    const docs = await Promise.all(slugBatch.map(s => db.collection("calc_cms").doc(s).get()));
    for (const doc of docs) {
      if (!doc.exists || doc.data().status !== "published" || processedSlugs.has(doc.id)) continue;
      await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, calcNameMap, trafficBySlug);
      processedSlugs.add(doc.id);
    }
    batchNum++;
  }

  // Phase 2: Fill remaining budget with unprioritized calcs via pagination
  let lastDoc = null;
  while (batchNum < MAX_BATCHES) {
    let query = db.collection("calc_cms").where("status","==","published").limit(20);
    if (lastDoc) query = query.startAfter(lastDoc);
    const snap = await query.get();
    if (snap.empty) break;
    lastDoc = snap.docs[snap.docs.length - 1];
    batchNum++;
    for (const doc of snap.docs) {
      if (processedSlugs.has(doc.id)) continue;
      await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, calcNameMap, trafficBySlug);
      processedSlugs.add(doc.id);
    }
    if (snap.size < 20) break;
  }

  // Phase 3: Refresh thin static pages (not in CMS)
  const cmsSlugs = new Set(nameSnap.docs.map(d => d.id));
  await _refreshStaticPages(apiKey, provider, provCfg.model, trafficBySlug, cmsSlugs, results);

  // Ping Google + Bing to recrawl updated pages via sitemap
  try {
    const fetch = require("node-fetch");
    const sitemapUrl = "https://calcto.work/sitemap.xml";
    await Promise.allSettled([
      fetch(`https://www.google.com/ping?sitemap=${sitemapUrl}`),
      fetch(`https://www.bing.com/ping?sitemap=${encodeURIComponent(sitemapUrl)}`),
    ]);
    console.log("[AutoPilot] Google + Bing pinged for sitemap recrawl");
  } catch(e) { console.warn("[AutoPilot] Sitemap ping failed:", e.message); }

  console.log("runAutoPilot done:", results);
  return results;
}

async function _refreshStaticPages(apiKey, provider, model, trafficBySlug, cmsSlugs, results) {
  const fetch = require("node-fetch");
  // Top 8 static pages by traffic that are NOT CMS calcs
  const candidates = Object.entries(trafficBySlug)
    .filter(([slug]) => !cmsSlugs.has(slug))
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)
    .map(([slug]) => slug);

  if (candidates.length === 0) return;

  const crypto = require("crypto");
  const zlib = require("zlib");
  const util = require("util");
  const gzip = util.promisify(zlib.gzip);

  const SITE = "calctowork";
  const HOSTING_BASE = "https://firebasehosting.googleapis.com/v1beta1";
  const patchedFiles = {}; // { "/en/slug/": htmlString }

  for (const slug of candidates) {
    try {
      const url = `https://calcto.work/en/${slug}/`;
      const r = await fetch(url, { timeout: 10000 });
      if (!r.ok) continue;
      const html = await r.text();

      // Measure existing long content text length
      const lcMatch = html.match(/<section class="long-content">([\s\S]*?)<\/section>/);
      const existingText = lcMatch ? lcMatch[1].replace(/<[^>]+>/g, "") : "";
      if (existingText.trim().length >= 500) continue; // Already substantial — skip

      // Extract name from <h1>
      const h1Match = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/);
      const calcName = h1Match ? h1Match[1].replace(/<[^>]+>/g, "").trim() : slug.replace(/-/g, " ");

      await new Promise(r => setTimeout(r, 400));
      const contentPrompt = `Write a comprehensive 800+ word HTML article for a calculator called "${calcName}".
Rules:
- Use ONLY: <h2>, <h3>, <p>, <ul>, <ol>, <li>, <strong>, <em>, <table>, <thead>, <tbody>, <tr>, <th>, <td>
- Single quotes for any HTML attributes (e.g. class='highlight')
- No wrapper divs, no <html>/<body>/<head>
- Start with: <p><strong>Quick answer:</strong> [one sentence directly answering how to calculate this]</p>
Sections required:
1. What Is [Calculator Name] and Who Needs It? (2 paragraphs, real-world context)
2. How to Use the Calculator (numbered steps, specific)
3. The Formula Explained (plain language + worked example with real numbers)
4. Practical Examples (2-3 scenarios in a table or list)
5. Tips for Accurate Results (specific to this calculation)
6. FAQ (3 questions users actually search for, detailed answers)
Write accurate, helpful content — do not invent features. Minimum 800 words.`;

      const newLC = await _callAIRaw(apiKey, provider, model, contentPrompt, 5000);
      if (!newLC || newLC.replace(/<[^>]+>/g, "").length < 400) continue;

      const newSection = `<section class="long-content">\n${newLC.trim()}\n</section>`;
      let patched;
      if (lcMatch) {
        patched = html.replace(/<section class="long-content">[\s\S]*?<\/section>/, newSection);
      } else {
        // Inject before </main>
        patched = html.replace(/(<\/main>)/, `<div class="long-content-wrap">${newSection}</div>\n$1`);
      }
      if (patched === html) continue;

      patchedFiles[`/en/${slug}/`] = patched;
      results.staticRefreshed++;
      console.log(`[AutoPilot] Static refresh: ${slug} (was ${existingText.trim().length} chars)`);
    } catch(e) { console.warn(`[AutoPilot] Static refresh failed for ${slug}:`, e.message); }
  }

  if (Object.keys(patchedFiles).length === 0) return;

  // Publish patches via Firebase Hosting REST API (same pattern as publishCalcToHosting)
  try {
    const tokenResult = await admin.app().options.credential.getAccessToken();
    const token = tokenResult.access_token;
    const headers = { "Authorization": "Bearer " + token, "Content-Type": "application/json" };

    const releasesRes = await fetch(`${HOSTING_BASE}/sites/${SITE}/releases?pageSize=1`, { headers });
    if (!releasesRes.ok) throw new Error("releases fetch failed");
    const releasesData = await releasesRes.json();
    const currentVersionName = releasesData.releases?.[0]?.version?.name;
    const currentConfig = releasesData.releases?.[0]?.version?.config || {};
    if (!currentVersionName) throw new Error("no current version");

    // Collect all current file hashes (paginated)
    const allCurrentFiles = {};
    let pageToken = null;
    do {
      const url = `${HOSTING_BASE}/${currentVersionName}/files?pageSize=1000${pageToken ? "&pageToken=" + pageToken : ""}`;
      const filesRes = await fetch(url, { headers });
      if (!filesRes.ok) throw new Error("files list failed");
      const filesData = await filesRes.json();
      (filesData.files || []).forEach(f => { allCurrentFiles[f.path] = f.hash; });
      pageToken = filesData.nextPageToken || null;
    } while (pageToken);

    // Gzip new files and compute hashes
    const newFileData = {};
    for (const [path, html] of Object.entries(patchedFiles)) {
      const gz = await gzip(Buffer.from(html, "utf8"));
      const hash = crypto.createHash("sha256").update(gz).digest("hex");
      newFileData[path] = { gz, hash };
    }

    const mergedFiles = { ...allCurrentFiles };
    for (const [path, { hash }] of Object.entries(newFileData)) mergedFiles[path] = hash;

    const createRes = await fetch(`${HOSTING_BASE}/sites/${SITE}/versions`, {
      method: "POST", headers, body: JSON.stringify({ config: currentConfig }),
    });
    if (!createRes.ok) throw new Error("create version failed");
    const { name: newVersionName } = await createRes.json();

    const populateRes = await fetch(`${HOSTING_BASE}/${newVersionName}:populateFiles`, {
      method: "POST", headers, body: JSON.stringify({ files: mergedFiles }),
    });
    if (!populateRes.ok) throw new Error("populate files failed");
    const populateData = await populateRes.json();
    const uploadUrl = populateData.uploadUrl;
    const uploadRequired = populateData.uploadRequiredHashes || [];

    for (const [, { gz, hash }] of Object.entries(newFileData)) {
      if (!uploadRequired.includes(hash)) continue;
      await fetch(`${uploadUrl}/${hash}`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + token, "Content-Type": "application/octet-stream" },
        body: gz,
      });
    }

    await fetch(`${HOSTING_BASE}/${newVersionName}?update_mask=status`, {
      method: "PATCH", headers, body: JSON.stringify({ status: "FINALIZED" }),
    });
    await fetch(`${HOSTING_BASE}/sites/${SITE}/releases?versionName=${newVersionName}`, {
      method: "POST", headers, body: JSON.stringify({}),
    });
    console.log(`[AutoPilot] Static pages published: ${Object.keys(patchedFiles).join(", ")}`);
  } catch(e) { console.warn("[AutoPilot] Static publish failed:", e.message); }
}

// ─────────────────────────────────────────────────────────────
// SHARED AI HELPERS
// ─────────────────────────────────────────────────────────────

async function _callAIRaw(apiKey, provider, model, prompt, maxTokens = 2000) {
  if (!apiKey) return null;
  const fetch = require("node-fetch");
  // deepseek-reasoner is a slow thinking model — force deepseek-chat for background tasks
  const effectiveModel = (provider === "deepseek" && model === "deepseek-reasoner") ? "deepseek-chat" : model;
  if (provider === "openai" || provider === "deepseek") {
    const baseURL = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
    const m = effectiveModel || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini");
    const r = await fetch(`${baseURL}/chat/completions`, {
      method: "POST",
      headers: { "Authorization": `Bearer ${apiKey}`, "Content-Type": "application/json" },
      body: JSON.stringify({ model: m, messages: [{ role: "user", content: prompt }], max_tokens: maxTokens }),
      timeout: 120000,
    });
    const data = await r.json();
    const msg = data?.choices?.[0]?.message;
    return msg?.content || msg?.reasoning_content || null;
  } else if (provider === "gemini") {
    const m = model || "gemini-1.5-flash";
    const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${m}:generateContent?key=${apiKey}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }], generationConfig: { maxOutputTokens: maxTokens } }),
      timeout: 120000,
    });
    const data = await r.json();
    return data?.candidates?.[0]?.content?.parts?.[0]?.text || null;
  } else {
    // anthropic (default)
    const m = model || "claude-haiku-4-5-20251001";
    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "Content-Type": "application/json" },
      body: JSON.stringify({ model: m, max_tokens: maxTokens, messages: [{ role: "user", content: prompt }] }),
      timeout: 120000,
    });
    const data = await r.json();
    return data?.content?.[0]?.text || null;
  }
}

async function _generateCalcRaw(apiKey, provider, model, prompt) {
  const systemPrompt = `You are a calculator builder. Given a description, generate a complete calculator specification as JSON. Return ONLY valid JSON with this structure:
{
  "slug": "kebab-case-slug",
  "category": "category_slug",
  "formula_js": "function calculate(inputs){return {result: inputs.value * 2};}",
  "inputs": [{"id":"value","label":"Value","type":"number","unit":"","placeholder":"","required":true}],
  "outputs": [{"id":"result","label":"Result","format":"number","unit":""}],
  "langs": {
    "en": {
      "name": "Calculator Name",
      "seo_title": "SEO Title (max 60 chars) | CalcToWork",
      "seo_description": "Meta description max 155 chars",
      "desc": "One sentence what this calculates",
      "formula_display": "Result = Value × 2",
      "steps": ["Enter the value","Click calculate","Read the result"],
      "mistakes": ["Common mistake 1","Common mistake 2"],
      "faq": [{"q":"Frequently asked question?","a":"Detailed answer."},{"q":"Another question?","a":"Another answer."}],
      "long_content": "<h2>How to Use This Calculator</h2><p>Detailed explanation of how to use the calculator with practical guidance.</p><h2>Formula and Methodology</h2><p>Explanation of the underlying formula and when to use it.</p><h2>Practical Examples</h2><p>Real-world examples with numbers.</p><h2>Tips and Best Practices</h2><p>Expert tips for getting accurate results.</p>"
    }
  }
}

Important: long_content must be at least 300 words of helpful HTML content covering usage, formula explanation, examples, and tips.`;
  let text = await _callAIRaw(apiKey, provider, model,
    `${systemPrompt}\n\nCalculator to build: ${prompt}`, 4000);
  if (!text) return null;
  text = text.replace(/<think>[\s\S]*?<\/think>/g, "").trim();
  const m = text.match(/\{[\s\S]*\}/s);
  if (!m) return null;
  try { return JSON.parse(m[0]); } catch(e) {
    try {
      const cleaned = m[0].replace(/,\s*([}\]])/g, '$1');
      return JSON.parse(cleaned);
    } catch(e2) {
      const stripped = m[0].replace(/"long_content"\s*:\s*"(?:[^"\\]|\\.)*"/g, '"long_content":""').replace(/"faq"\s*:\s*\[[\s\S]*?\]/g, '"faq":[]');
      try { return JSON.parse(stripped); } catch(e3) { return null; }
    }
  }
}

async function _translateRaw(apiKey, provider, model, enContent, targetLang) {
  const langNames = { es:"Spanish", fr:"French", de:"German", it:"Italian", pt:"Portuguese" };
  const langName = langNames[targetLang] || targetLang;
  const contentToTranslate = {
    name: enContent.name || "",
    desc: enContent.desc || "",
    seo_title: enContent.seo_title || "",
    seo_description: enContent.seo_description || "",
    example_label: enContent.example_label || "",
    result_context: enContent.result_context || "",
    formula_display: enContent.formula_display || "",
    steps: enContent.steps || [],
    mistakes: enContent.mistakes || [],
    long_content: enContent.long_content || "",
    faq: enContent.faq || [],
  };
  const prompt = `Translate the following calculator content from English to ${langName}. Preserve all HTML tags exactly. Translate all text including the HTML content in long_content. Keep {placeholder} tokens unchanged. Return ONLY valid JSON with the same structure as input.

Input:
${JSON.stringify(contentToTranslate, null, 2)}`;
  const text = await _callAIRaw(apiKey, provider, model, prompt, 4096);
  if (!text) return null;
  const m = text.match(/\{[\s\S]*\}/s);
  if (!m) return null;
  try {
    const translated = JSON.parse(m[0]);
    // Preserve non-translatable fields
    translated.inputs_labels = enContent.inputs_labels || {};
    translated.outputs_labels = enContent.outputs_labels || {};
    translated.range_hints = enContent.range_hints || {};
    translated.slug = enContent.slug || "";
    return translated;
  } catch(e) { return null; }
}

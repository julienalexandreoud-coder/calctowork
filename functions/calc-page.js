/**
 * calcPage — serves CMS-created calculator pages dynamically from Firestore
 * URL pattern: /{lang}/{slug}/ or /{lang}/{slug}  (Firebase rewrites handle both)
 */
const functions = require("firebase-functions");
const admin = require("firebase-admin");

const db = admin.firestore();

const LANGS = ["en", "es", "fr", "de", "it", "pt"];

const LANG_LABELS = { en:"EN", es:"ES", fr:"FR", de:"DE", it:"IT", pt:"PT" };

// Localised UI chrome for the calculator pages. Previously every calculator in
// every language showed English labels (Inputs, Result, Calculate…), which read
// as broken/low-quality (and is an AdSense red flag). Keyed by language.
const UI_I18N = {
  en: { inputs:"Inputs", result:"Result", calculate:"Calculate", reset:"Reset", enterValues:"Enter values and press Calculate", copyResults:"Copy results", share:"Share", embed:"Embed", helpful:"Was this helpful?", examples:"Common Examples — Click to Fill", faq:"FAQ", howToUse:"How to use it", mistakes:"Common mistakes", workedExample:"Worked example", formula:"Formula", inputGuide:"Input guide", field:"Field", typicalRange:"Typical range" },
  es: { inputs:"Datos", result:"Resultado", calculate:"Calcular", reset:"Reiniciar", enterValues:"Ingresa los valores y pulsa Calcular", copyResults:"Copiar resultados", share:"Compartir", embed:"Insertar", helpful:"¿Te resultó útil?", examples:"Ejemplos comunes — Haz clic para rellenar", faq:"Preguntas frecuentes", howToUse:"Cómo usarla", mistakes:"Errores comunes", workedExample:"Ejemplo resuelto", formula:"Fórmula", inputGuide:"Guía de valores", field:"Campo", typicalRange:"Rango típico" },
  fr: { inputs:"Données", result:"Résultat", calculate:"Calculer", reset:"Réinitialiser", enterValues:"Saisissez les valeurs et cliquez sur Calculer", copyResults:"Copier les résultats", share:"Partager", embed:"Intégrer", helpful:"Est-ce utile ?", examples:"Exemples courants — Cliquez pour remplir", faq:"Questions fréquentes", howToUse:"Comment l'utiliser", mistakes:"Erreurs courantes", workedExample:"Exemple résolu", formula:"Formule", inputGuide:"Guide de saisie", field:"Champ", typicalRange:"Plage typique" },
  de: { inputs:"Eingaben", result:"Ergebnis", calculate:"Berechnen", reset:"Zurücksetzen", enterValues:"Werte eingeben und auf Berechnen klicken", copyResults:"Ergebnisse kopieren", share:"Teilen", embed:"Einbetten", helpful:"War das hilfreich?", examples:"Häufige Beispiele — Zum Ausfüllen klicken", faq:"Häufige Fragen", howToUse:"So funktioniert's", mistakes:"Häufige Fehler", workedExample:"Rechenbeispiel", formula:"Formel", inputGuide:"Eingabehilfe", field:"Feld", typicalRange:"Typischer Bereich" },
  it: { inputs:"Dati", result:"Risultato", calculate:"Calcola", reset:"Reimposta", enterValues:"Inserisci i valori e premi Calcola", copyResults:"Copia risultati", share:"Condividi", embed:"Incorpora", helpful:"È stato utile?", examples:"Esempi comuni — Clicca per compilare", faq:"Domande frequenti", howToUse:"Come usarlo", mistakes:"Errori comuni", workedExample:"Esempio pratico", formula:"Formula", inputGuide:"Guida ai valori", field:"Campo", typicalRange:"Intervallo tipico" },
  pt: { inputs:"Dados", result:"Resultado", calculate:"Calcular", reset:"Limpar", enterValues:"Insira os valores e clique em Calcular", copyResults:"Copiar resultados", share:"Compartilhar", embed:"Incorporar", helpful:"Isto foi útil?", examples:"Exemplos comuns — Clique para preencher", faq:"Perguntas frequentes", howToUse:"Como usar", mistakes:"Erros comuns", workedExample:"Exemplo resolvido", formula:"Fórmula", inputGuide:"Guia de valores", field:"Campo", typicalRange:"Intervalo típico" },
};
const _uiFor = (lang) => UI_I18N[lang] || UI_I18N.en;
// Does an article already contain its own FAQ heading? If so, we must not append
// a second structured FAQ block (that produced two FAQs on every page).
const _ARTICLE_HAS_FAQ = /faq|frequently asked|preguntas frecuentes|perguntas frequentes|questions fréquentes|häufig(e)?\s*(gestellte)?\s*fragen|domande frequenti/i;

// Result units are often English WORDS ("days", "years", "people") that the
// UI-chrome localisation didn't cover, so a Spanish result read "20,698 days".
// Translate the common word-units; leave symbols (kg, m, %, $, m/s²) untouched.
const UNIT_WORD_I18N = {
  days:{es:"días",fr:"jours",de:"Tage",it:"giorni",pt:"dias"}, day:{es:"día",fr:"jour",de:"Tag",it:"giorno",pt:"dia"},
  years:{es:"años",fr:"ans",de:"Jahre",it:"anni",pt:"anos"}, year:{es:"año",fr:"an",de:"Jahr",it:"anno",pt:"ano"},
  months:{es:"meses",fr:"mois",de:"Monate",it:"mesi",pt:"meses"}, month:{es:"mes",fr:"mois",de:"Monat",it:"mese",pt:"mês"},
  weeks:{es:"semanas",fr:"semaines",de:"Wochen",it:"settimane",pt:"semanas"}, week:{es:"semana",fr:"semaine",de:"Woche",it:"settimana",pt:"semana"},
  hours:{es:"horas",fr:"heures",de:"Stunden",it:"ore",pt:"horas"}, hour:{es:"hora",fr:"heure",de:"Stunde",it:"ora",pt:"hora"},
  minutes:{es:"minutos",fr:"minutes",de:"Minuten",it:"minuti",pt:"minutos"}, seconds:{es:"segundos",fr:"secondes",de:"Sekunden",it:"secondi",pt:"segundos"},
  people:{es:"personas",fr:"personnes",de:"Personen",it:"persone",pt:"pessoas"}, persons:{es:"personas",fr:"personnes",de:"Personen",it:"persone",pt:"pessoas"}, person:{es:"persona",fr:"personne",de:"Person",it:"persona",pt:"pessoa"},
  units:{es:"unidades",fr:"unités",de:"Einheiten",it:"unità",pt:"unidades"}, times:{es:"veces",fr:"fois",de:"mal",it:"volte",pt:"vezes"},
  calories:{es:"calorías",fr:"calories",de:"Kalorien",it:"calorie",pt:"calorias"}, bags:{es:"sacos",fr:"sacs",de:"Säcke",it:"sacchi",pt:"sacos"},
  bricks:{es:"ladrillos",fr:"briques",de:"Ziegel",it:"mattoni",pt:"tijolos"}, liters:{es:"litros",fr:"litres",de:"Liter",it:"litri",pt:"litros"},
  pieces:{es:"piezas",fr:"pièces",de:"Stück",it:"pezzi",pt:"peças"}, blocks:{es:"bloques",fr:"blocs",de:"Blöcke",it:"blocchi",pt:"blocos"},
  pasadas:{es:"pasadas",fr:"passes",de:"Durchgänge",it:"passate",pt:"demãos"}, capas:{es:"capas",fr:"couches",de:"Schichten",it:"strati",pt:"camadas"}, manos:{es:"manos",fr:"couches",de:"Anstriche",it:"mani",pt:"demãos"},
};
// Units are STORED in whatever language the calc was authored in — mostly Spanish. The
// old _localizeUnit returned early for English, so an English page showed "años" and
// "veces/año". Canonicalise any known word back to its English key first, then localise:
// that makes the mapping bidirectional (es->en as well as en->es).
const _UNIT_CANON = (() => {
  const m = {};
  for (const [en, tr] of Object.entries(UNIT_WORD_I18N)) {
    m[en] = en;
    for (const w of Object.values(tr)) m[String(w).toLowerCase()] = en;
  }
  return m;
})();
function _localizeUnitWord(word, lang) {
  const key = _UNIT_CANON[String(word).trim().toLowerCase()];
  if (!key) return word;
  if (lang === "en") return key;
  const tr = UNIT_WORD_I18N[key];
  return (tr && tr[lang]) ? tr[lang] : key;
}
function _localizeUnit(unit, lang) {
  if (!unit) return unit;
  const raw = String(unit).trim();
  // Compound units like "veces/año" or "kWh/día" translate part by part.
  if (raw.includes("/")) {
    const parts = raw.split("/");
    const out = parts.map(p => _localizeUnitWord(p.trim(), lang));
    // Only rewrite when at least one part was actually recognised.
    if (out.some((p, i) => p !== parts[i].trim())) return out.join("/");
    return raw;
  }
  return _localizeUnitWord(raw, lang);
}

// Repair UTF-8-as-Latin1 mojibake (e.g. "m²" stored as "mÂ²", "30°" as "30Â°").
// Applied at render to units/labels/presets so display is clean regardless of the
// double-encoded source; the raw stored value (used for unit conversion) is untouched.
const _CP1252 = { 0x20AC:0x80,0x201A:0x82,0x0192:0x83,0x201E:0x84,0x2026:0x85,0x2020:0x86,0x2021:0x87,0x02C6:0x88,0x2030:0x89,0x0160:0x8A,0x2039:0x8B,0x0152:0x8C,0x017D:0x8E,0x2018:0x91,0x2019:0x92,0x201C:0x93,0x201D:0x94,0x2022:0x95,0x2013:0x96,0x2014:0x97,0x02DC:0x98,0x2122:0x99,0x0161:0x9A,0x203A:0x9B,0x0153:0x9C,0x017E:0x9E,0x0178:0x9F };
// Any char that could be a mis-decoded UTF-8 lead byte (0xC2-0xF4 as Latin-1/cp1252).
// Must be this wide: Greek/subscripts mojibake to leads like "Î" (Δ), "Ï" (τ), "á" (ᵦ).
// Safe because the run decode below only substitutes when the bytes are valid UTF-8.
const _MOJI_LEAD = /[Â-ô]/;
function _hiByte(ch) {
  const cp = ch.codePointAt(0);
  if (cp >= 0x80 && cp <= 0xFF) return cp;
  if (_CP1252[cp] != null) return _CP1252[cp];
  return null;
}
// Repair each RUN of mis-decoded high bytes independently (so mixed strings like
// "â‚¬/m²" — mojibake euro + an already-correct ² — are fixed without clobbering the
// good part). Runs that don't decode as valid UTF-8 are left exactly as they were.
function _deMojibake(s) {
  if (typeof s !== "string" || !_MOJI_LEAD.test(s)) return s;
  let out = "", i = 0;
  while (i < s.length) {
    if (_hiByte(s[i]) === null) { out += s[i++]; continue; }
    let j = i; const bytes = [];
    while (j < s.length) { const b = _hiByte(s[j]); if (b === null) break; bytes.push(b); j++; }
    let dec = null;
    try { const t = Buffer.from(bytes).toString("utf8"); if (!t.includes("�")) dec = t; } catch (e) {}
    out += (dec !== null ? dec : s.slice(i, j));
    i = j;
  }
  return out;
}

// Comparison-preset labels were wrong (Spanish "Cubo pequeno" shapes on a
// Some generated articles contain LaTeX ( \( FV = P \times \frac{a}{b} \) ). Pages built
// here don't load a math renderer, so it showed up as literal backslash soup — including
// inside <meta description>. Convert it to plain Unicode maths, which reads correctly
// everywhere (page, search snippet, screen reader) and needs no client JS.
const _TEX_SYM = {
  times:"×", cdot:"·", div:"÷", pm:"±", mp:"∓", le:"≤", leq:"≤", ge:"≥", geq:"≥",
  neq:"≠", ne:"≠", approx:"≈", equiv:"≡", propto:"∝", infty:"∞", sum:"∑", prod:"∏",
  int:"∫", partial:"∂", nabla:"∇", degree:"°", circ:"°", ldots:"…", dots:"…",
  cdots:"⋯", rightarrow:"→", to:"→", leftarrow:"←", Rightarrow:"⇒", leftrightarrow:"↔",
  alpha:"α", beta:"β", gamma:"γ", delta:"δ", epsilon:"ε", varepsilon:"ε", zeta:"ζ",
  eta:"η", theta:"θ", lambda:"λ", mu:"μ", nu:"ν", xi:"ξ", pi:"π", rho:"ρ", sigma:"σ",
  tau:"τ", phi:"φ", varphi:"φ", chi:"χ", psi:"ψ", omega:"ω",
  Gamma:"Γ", Delta:"Δ", Theta:"Θ", Lambda:"Λ", Pi:"Π", Sigma:"Σ", Phi:"Φ", Omega:"Ω",
};
const _SUP = { "0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹","+":"⁺","-":"⁻","n":"ⁿ","i":"ⁱ" };
const _SUB = { "0":"₀","1":"₁","2":"₂","3":"₃","4":"₄","5":"₅","6":"₆","7":"₇","8":"₈","9":"₉","+":"₊","-":"₋" };
function _deLatex(s) {
  if (typeof s !== "string" || !/\\[a-zA-Z(\[]|\$\$/.test(s)) return s;
  // Only text that actually carries math delimiters may have unknown "\command"
  // backslashes stripped — otherwise a Windows path would be mangled into prose.
  const isMath = /\\\(|\\\)|\\\[|\\\]|\$\$|\\frac|\\times|\\sqrt|\\text\{/.test(s);
  let t = s;
  t = t.replace(/\\\[([\s\S]*?)\\\]/g, (m, x) => " " + x.trim() + " ")
       .replace(/\\\(([\s\S]*?)\\\)/g, (m, x) => x.trim())
       .replace(/\$\$([\s\S]*?)\$\$/g, (m, x) => " " + x.trim() + " ");
  t = t.replace(/\\(?:text|mathrm|mathbf|mathit|operatorname|textbf|textit)\s*\{([^{}]*)\}/g, "$1");
  // Sub/superscripts BEFORE fractions: \frac{I_{hi}}{I_{lo}} has nested braces that a
  // flat {…} match cannot span, so collapse the inner ones first.
  t = t.replace(/\^\{([^{}]+)\}/g, (m, e) => [...e].every(c => _SUP[c]) ? [...e].map(c => _SUP[c]).join("") : "^" + e);
  t = t.replace(/\^(-?\w)/g, (m, e) => _SUP[e] || "^" + e);
  t = t.replace(/_\{([^{}]+)\}/g, (m, e) => [...e].every(c => _SUB[c]) ? [...e].map(c => _SUB[c]).join("") : "_" + e);
  t = t.replace(/_(\w)/g, (m, e) => _SUB[e] || "_" + e);
  for (let i = 0; i < 4; i++) {                                     // nested fractions
    const before = t;
    t = t.replace(/\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, (m, a, b) =>
      (/[+\-\s]/.test(a.trim()) ? `(${a.trim()})` : a.trim()) + "/" +
      (/[+\-\s]/.test(b.trim()) ? `(${b.trim()})` : b.trim()));
    if (t === before) break;
  }
  t = t.replace(/\\sqrt\s*\[\s*3\s*\]\s*\{([^{}]*)\}/g, "∛($1)").replace(/\\sqrt\s*\{([^{}]*)\}/g, "√($1)");
  t = t.replace(/\\left\s*|\\right\s*/g, "").replace(/\\,|\\;|\\!|\\quad|\\qquad/g, " ");
  t = t.replace(/\\([a-zA-Z]+)/g, (m, w) => _TEX_SYM[w] !== undefined ? _TEX_SYM[w] : (isMath ? w : m));
  t = t.replace(/\\([%$&#_{}])/g, "$1");
  // A meta description is truncated to ~155 chars, which can cut off the closing \) and
  // leave the opener stranded. Drop any unpaired delimiter rather than print it.
  if (isMath) t = t.replace(/\\[()[\]]/g, "");
  return t.replace(/[ \t]{2,}/g, " ").replace(/\s+([.,;:!?)])/g, "$1");
}
// Prose that reaches a reader: fix encoding damage first, then LaTeX.
const _prose = s => _deLatex(_deMojibake(s));

// A field label. Translations sometimes keep the id's underscore ("côté_c",
// "taille_échantillon"), which reads as a variable name rather than a label.
function _niceLabel(s) {
  const t = _deMojibake(String(s == null ? "" : s));
  if (!t.includes("_")) return t;
  const spaced = t.replace(/_+/g, " ").replace(/\s{2,}/g, " ").trim();
  return spaced.charAt(0).toUpperCase() + spaced.slice(1);
}

// cylinder). They've been normalised to English size tiers in the configs;
// translate those tiers to the page language here so they read natively.
const PRESET_TIER_I18N = {
  "small":     {es:"Pequeño",fr:"Petit",de:"Klein",it:"Piccolo",pt:"Pequeno"},
  "medium":    {es:"Mediano",fr:"Moyen",de:"Mittel",it:"Medio",pt:"Médio"},
  "large":     {es:"Grande",fr:"Grand",de:"Groß",it:"Grande",pt:"Grande"},
  "x-large":   {es:"Extra grande",fr:"Très grand",de:"Sehr groß",it:"Molto grande",pt:"Extra grande"},
  "xx-large":  {es:"Máximo",fr:"Maximum",de:"Maximal",it:"Massimo",pt:"Máximo"},
  "maximum":   {es:"Máximo",fr:"Maximum",de:"Maximum",it:"Massimo",pt:"Máximo"},
};
const _EXAMPLE_WORD = {en:"Example",es:"Ejemplo",fr:"Exemple",de:"Beispiel",it:"Esempio",pt:"Exemplo"};
function _localizePreset(label, lang) {
  if (!label || lang === "en") return label;
  const key = String(label).trim().toLowerCase();
  const m = PRESET_TIER_I18N[key];
  if (m && m[lang]) return m[lang];
  const ex = label.match(/^Example\s+(\d+)$/i);
  if (ex) return (_EXAMPLE_WORD[lang] || "Example") + " " + ex[1];
  return label;
}

// Choice inputs store raw option values ("cemento", "si", "230"). Turn one into
// something readable: a translated label if the calc has one, else a known yes/no
// word, else the humanized value.
const _YESNO_I18N = {
  si:  { en:"Yes", es:"Sí",  fr:"Oui", de:"Ja",   it:"Sì",  pt:"Sim" },
  yes: { en:"Yes", es:"Sí",  fr:"Oui", de:"Ja",   it:"Sì",  pt:"Sim" },
  no:  { en:"No",  es:"No",  fr:"Non", de:"Nein", it:"No",  pt:"Não" },
};
function _localizeOption(inputId, value, langData, lang) {
  const v = String(value);
  const custom = ((langData && langData.option_labels) || {})[inputId];
  if (custom && custom[v]) return String(custom[v]);
  const yn = _YESNO_I18N[v.toLowerCase()];
  if (yn) return yn[lang] || yn.en;
  if (/^-?\d+(\.\d+)?$/.test(v)) return v;          // numeric codes stay as-is
  return humanizeId(v);
}

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
// Authorised seller line, derived from ADSENSE_ID so the two can never disagree.
// f08c47fec0942fa0 is Google's fixed certification authority id.
const ADS_TXT_LINE = "google.com, " + ADSENSE_ID.replace(/^ca-/, "") + ", DIRECT, f08c47fec0942fa0";

// Content-Security-Policy for the whole site. AdSense needs its ad + consent
// (Funding Choices) + telemetry hosts allowed, or the browser blocks them and
// the console fills with CSP errors. Kept in code so every incremental deploy
// re-applies it (the deploy clones the live version's config).
const SITE_CSP = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://*.googletagmanager.com https://*.google-analytics.com https://pagead2.googlesyndication.com https://*.googlesyndication.com https://adservice.google.com https://fundingchoicesmessages.google.com https://cdn.jsdelivr.net https://www.gstatic.com https://cdnjs.cloudflare.com https://contextual.media.net https://cdn.carbonads.com https://ayyknrom.com https://*.effectivecpmnetwork.com; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com; font-src 'self' data: https://cdn.jsdelivr.net https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://*.googleapis.com https://*.google-analytics.com https://*.cloudfunctions.net https://csi.gstatic.com https://pagead2.googlesyndication.com https://*.googlesyndication.com https://googleads.g.doubleclick.net https://*.g.doubleclick.net https://fundingchoicesmessages.google.com https://adservice.google.com https://ep1.adtrafficquality.google https://ep2.adtrafficquality.google; frame-src https://googleads.g.doubleclick.net https://*.googlesyndication.com https://fundingchoicesmessages.google.com https:; object-src 'none'; base-uri 'self'";

// Return a copy of a hosting version config with the CSP header value replaced
// by SITE_CSP. Only touches Content-Security-Policy; everything else is intact.
function _patchConfigCSP(config) {
  if (!config || !Array.isArray(config.headers)) return config;
  const c = JSON.parse(JSON.stringify(config));
  for (const rule of c.headers) {
    if (!rule || !rule.headers || typeof rule.headers !== "object") continue;
    if (Array.isArray(rule.headers)) {
      // firebase.json style: [ { key, value } ]
      for (const h of rule.headers) { if (h && h.key === "Content-Security-Policy") h.value = SITE_CSP; }
    } else if ("Content-Security-Policy" in rule.headers) {
      // Hosting REST version-config style: { "Content-Security-Policy": "..." }
      rule.headers["Content-Security-Policy"] = SITE_CSP;
    }
  }
  return c;
}

// Authoritative per-language slug map, loaded once from calc-index.json.
// Keyed by BOTH the primary slug and the numeric id so lookups always hit.
// This is the single source of truth for the translated URL each language uses
// (e.g. aceleracion -> {en:"acceleration", de:"beschleunigung", ...}). Without
// it, every language page was written at the Spanish slug, creating duplicate
// URLs alongside the real indexed translated-slug pages.
let _SLUG_INDEX = null;
let _OLD_SLUG_INDEX = null;
function _loadSlugIndexes() {
  if (_SLUG_INDEX) return;
  _SLUG_INDEX = {};
  _OLD_SLUG_INDEX = {};
  try {
    const raw = require("./calc-index.json");
    const arr = Array.isArray(raw) ? raw : (raw.calcs || raw.items || Object.values(raw));
    for (const c of arr) {
      if (!c || !c.slugs) continue;
      if (c.slug) _SLUG_INDEX[c.slug] = c.slugs;
      if (c.id != null) _SLUG_INDEX[String(c.id)] = c.slugs;
      if (c.old_slugs) {
        if (c.slug) _OLD_SLUG_INDEX[c.slug] = c.old_slugs;
        if (c.id != null) _OLD_SLUG_INDEX[String(c.id)] = c.old_slugs;
      }
    }
  } catch (e) {
    console.warn("calc-index.json slug map unavailable:", e.message);
  }
}
function _getSlugIndex() { _loadSlugIndexes(); return _SLUG_INDEX; }
// Prior slugs kept so their URLs still serve (with canonical -> the new SEO
// slug), consolidating the migration without hard redirects.
function _getOldSlugIndex() { _loadSlugIndexes(); return _OLD_SLUG_INDEX; }

// Ensure data.langs[lang].slug holds the authoritative translated slug for every
// language, so canonical/hreflang/lang-switcher and the deploy path all agree.
// Returns a NEW data object (langs cloned); never mutates the caller's copy.
function _applyLangSlugs(slug, data) {
  const idx = _getSlugIndex();
  const map = idx[slug] || (data && idx[String(data.id)]) || null;
  if (!map) return data;
  const langs = { ...(data.langs || {}) };
  for (const l of LANGS) {
    if (!map[l]) continue;
    if (!langs[l]) continue; // don't invent a language the calc doesn't have
    if (langs[l].slug === map[l]) continue;
    langs[l] = { ...langs[l], slug: map[l] };
  }
  return { ...data, langs };
}

function esc(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

// Build an SEO title that targets the "how to calculate X" search intent per
// language, e.g. "How to Calculate Acceleration — Free Calculator".
const _HOWTO = { en: "How to Calculate", es: "Cómo Calcular", fr: "Comment Calculer", de: "Berechnung von", it: "Come Calcolare", pt: "Como Calcular" };
const _FREECALC = { en: "Free Calculator", es: "Calculadora Gratis", fr: "Calculateur Gratuit", de: "Kostenloser Rechner", it: "Calcolatore Gratis", pt: "Calculadora Grátis" };
const _CALC_WORD_RE = /\b(calculators?|calculadoras?|calculateur|calculatrice|calcolatrice|calcolatore|calcolatori)\b/ig;
// German compounds the calc word into the noun (Beschleunigungsrechner). Strip
// it as a suffix, then drop the linking "s" it leaves behind: -srechner -> "".
const _DE_CALC_SUFFIX_RE = /s?(rechner|kalkulator)\b/ig;
const _ALREADY_HOWTO = /how to|cómo calc|como calc|comment calc|berechnung|come calcol/i;
function buildSeoTitle(lang, langData, name) {
  const existing = (langData && langData.seo_title || "").trim();
  if (existing && _ALREADY_HOWTO.test(existing)) return existing; // already how-to optimized
  let topic = (name || "").replace(_CALC_WORD_RE, "");
  if (lang === "de") topic = topic.replace(_DE_CALC_SUFFIX_RE, "");
  else topic = topic.replace(/\brechner\b/ig, "");
  topic = topic.replace(/[-–—:|]\s*$/, "").replace(/\s{2,}/g, " ").trim();
  // Drop a leading connector left behind by stripping the calc word, e.g.
  // "Calculadora de Aceleración" -> "de Aceleración" -> "Aceleración".
  topic = topic.replace(/^(de la|della|del|des|de|d['’]|du|da|do|di|of|for|per|para|pour)\s+/i, "").trim();
  // If stripping produced a broken fragment (too short, or a lone trailing
  // linking-s), fall back to a safe title rather than emitting garbage.
  if (topic.length < 3) return existing || `${name} — CalcToWork`;
  const howto = _HOWTO[lang] || _HOWTO.en;
  const free = _FREECALC[lang] || _FREECALC.en;
  let t = `${howto} ${topic} — ${free}`;
  if (t.length > 62) t = `${howto} ${topic}`; // keep it within a sensible title length
  return t;
}

// Turn a raw field id into a readable label as a LAST resort when no proper
// label exists: "final_velocity" -> "Final velocity", "neck" -> "Neck".
function humanizeId(id) {
  if (!id) return "";
  var s = String(id).replace(/_/g, " ").replace(/([a-z])([A-Z])/g, "$1 $2").trim();
  return s.charAt(0).toUpperCase() + s.slice(1);
}

function buildHreflang(slug, data) {
  const tags = LANGS.map(l => {
    const lData = data.langs && data.langs[l];
    if (!lData) return "";
    const lSlug = lData.slug || slug;
    return `  <link rel="alternate" hreflang="${l}" href="${SITE}/${l}/${lSlug}/">`;
  }).filter(Boolean);
  // x-default points to the English version (Google's recommended fallback for
  // multilingual pages) — was missing, flagged in the SEO audit.
  const enData = data.langs && data.langs.en;
  if (enData) {
    const enSlug = enData.slug || slug;
    tags.push(`  <link rel="alternate" hreflang="x-default" href="${SITE}/en/${enSlug}/">`);
  }
  return tags.join("\n");
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

function renderInputsForm(inputs, langData, lang) {
  const labels = (langData && langData.inputs_labels) || {};
  return inputs.map(inp => {
    const rawLabel = labels[inp.id];
    const label = esc(_niceLabel(rawLabel && rawLabel !== inp.id ? rawLabel : humanizeId(inp.id)));
    const unitOpts = (inp.unit_options || [inp.unit]).filter(Boolean);
    const uDisp = u => esc(_deMojibake(_localizeUnit(u, lang)));
    // data-input + data-category are REQUIRED by calculator.js collectInputs() to
    // convert the entered value to the formula's base unit. Without them, picking
    // a different unit (g instead of kg) was silently ignored — wrong result.
    const unitSel = unitOpts.length > 1
      ? `<select class="unit-select" data-input="${esc(inp.id)}" data-category="${esc(inp.unit_category || "")}" name="${esc(inp.id)}_unit" aria-label="Unit for ${label}">
          ${unitOpts.map(u => `<option value="${esc(u)}"${u === inp.unit ? " selected" : ""}>${uDisp(u)}</option>`).join("")}
        </select>`
      : (inp.unit ? `<span class="unit-label">${uDisp(inp.unit)}</span>` : "");
    // Choice and free-text inputs used to render as type="number" too, which made them
    // impossible to fill in ("cemento" cannot be typed into a number box) and silently
    // pushed the formula down its fallback branch. collectInputs() in calculator.js
    // already reads select[name] and non-number inputs as raw strings.
    const rawOpts = inp.options || inp.choices;
    // Only a plain number field carries a unit selector.
    const isNumericField = !(rawOpts && rawOpts.length) && inp.type !== "date" && inp.type !== "text" && inp.type !== "string";
    const field = (() => {
      if (Array.isArray(rawOpts) && rawOpts.length) {
        const opts = rawOpts.map(o => (o && typeof o === "object" && o.value !== undefined) ? o : { value: o });
        return `<select id="input-${esc(inp.id)}" name="${esc(inp.id)}" class="choice-select">
              ${opts.map(o => {
                const v = String(o.value);
                const oLabel = o.label ? String(o.label) : _localizeOption(inp.id, v, langData, lang);
                const sel = (inp.default !== undefined && String(inp.default) === v) ? " selected" : "";
                return `<option value="${esc(v)}"${sel}>${esc(_deMojibake(oLabel))}</option>`;
              }).join("")}
            </select>`;
      }
      // Date calcs (age in days, due date, ovulation) fed a date string into a number
      // box, so they could never be filled in at all.
      if (inp.type === "date") {
        return `<input type="date" id="input-${esc(inp.id)}" name="${esc(inp.id)}"
              ${inp.min !== undefined ? `min="${esc(String(inp.min))}"` : ""}
              ${inp.max !== undefined ? `max="${esc(String(inp.max))}"` : ""}
              ${inp.default !== undefined ? `value="${esc(String(inp.default))}"` : ""}>`;
      }
      if (inp.type === "text" || inp.type === "string") {
        return `<input type="text" id="input-${esc(inp.id)}" name="${esc(inp.id)}"
              ${inp.placeholder ? `placeholder="${esc(inp.placeholder)}"` : ""}
              ${inp.default !== undefined ? `value="${esc(String(inp.default))}"` : ""}
              autocomplete="off">`;
      }
      return `<input type="number" id="input-${esc(inp.id)}" name="${esc(inp.id)}"
              inputmode="decimal"
              ${inp.min !== undefined ? `min="${inp.min}"` : ""}
              ${inp.max !== undefined ? `max="${inp.max}"` : ""}
              ${inp.step !== undefined ? `step="${inp.step}"` : 'step="any"'}
              ${inp.default !== undefined ? `value="${inp.default}"` : ""}
              autocomplete="off">`;
    })();
    return `
        <div class="form-group">
          <label for="input-${esc(inp.id)}">${label}</label>
          <div class="input-with-unit">
            ${field}
            ${isNumericField ? unitSel : ""}
          </div>
        </div>`;
  }).join("\n");
}

function renderResults(outputs, langData) {
  const labels = (langData && langData.outputs_labels) || {};
  return outputs.map(out => {
    // Output labels and units carry currency and exponent characters (€, m³) that were
    // stored mojibake'd. Every other render path repairs them; this one did not, so the
    // results panel showed "IVA (â‚¬)" and "Volumen (mÂ³)".
    const label = esc(_niceLabel(labels[out.id] || humanizeId(out.id)));
    const cls = out.highlight ? "result-item result-highlight" : "result-item";
    return `<div class="${cls}" id="out-${esc(out.id)}" style="display:none">
        <span class="result-label">${label}</span>
        <span class="result-value" data-out="${esc(out.id)}">—</span>
        ${out.unit ? `<span class="result-unit">${esc(_deMojibake(String(out.unit)))}</span>` : ""}
      </div>`;
  }).join("\n");
}

function renderArticle(lang, langData, inputs) {
  if (!langData) return "";
  const steps = langData.steps || [];
  const mistakes = langData.mistakes || [];
  const hints = langData.range_hints || {};
  const faqItems = langData.faq || [];

  const ui = _uiFor(lang);
  // Prefer pre-rendered long_content HTML when available
  if (langData.long_content) {
    // Only append the structured FAQ if the article doesn't already contain one
    // — otherwise the page shows two FAQ sections.
    const faqHtml = (faqItems.length && !_ARTICLE_HAS_FAQ.test(langData.long_content))
      ? `<section class="faq-section"><h2>${esc(ui.faq)}</h2>${faqItems.map(f =>
          `<details class="faq-item"><summary>${esc(_prose(f.q))}</summary><p>${esc(_prose(f.a))}</p></details>`
        ).join("")}</section>` : "";
    return `<div class="long-content">${_prose(langData.long_content)}${faqHtml}</div>`;
  }

  // Fallback: render from structured fields
  const stepsHtml = steps.length
    ? `<h2>${esc(ui.howToUse)}</h2><ol>${steps.map(s => `<li>${esc(_prose(s))}</li>`).join("")}</ol>` : "";

  const mistakesHtml = mistakes.length
    ? `<h2>${esc(ui.mistakes)}</h2><ul>${mistakes.map(m => `<li>⚠️ ${esc(_prose(m))}</li>`).join("")}</ul>` : "";

  const exampleHtml = langData.example_label
    ? `<h2>${esc(ui.workedExample)}</h2><p>${esc(_prose(langData.example_label))}</p>${
        langData.result_context ? `<p><em>${esc(_prose(langData.result_context))}</em></p>` : ""
      }` : "";

  const formulaHtml = langData.formula_display
    ? `<h2>${esc(ui.formula)}</h2><p><code>${esc(_prose(langData.formula_display))}</code></p>` : "";

  const hintRows = Object.entries(hints);
  const hintsHtml = hintRows.length
    ? `<h2>${esc(ui.inputGuide)}</h2><table class="comparison-table"><thead><tr><th>${esc(ui.field)}</th><th>${esc(ui.typicalRange)}</th></tr></thead><tbody>
        ${hintRows.map(([k, v]) => `<tr><td>${esc(k)}</td><td>${esc(v)}</td></tr>`).join("")}
      </tbody></table>` : "";

  const faqHtml = faqItems.length
    ? `<section class="faq-section"><h2>${esc(ui.faq)}</h2>${faqItems.map(f =>
        `<details class="faq-item"><summary>${esc(f.q)}</summary><p>${esc(f.a)}</p></details>`
      ).join("")}</section>` : "";

  return `<div class="long-content">${stepsHtml}${mistakesHtml}${exampleHtml}${formulaHtml}${hintsHtml}${faqHtml}</div>`;
}

// Build a UNIQUE meta description per calculator/language. Google penalizes
// duplicate/templated meta descriptions; a bulk template had stamped every calc
// with the same "get precise results in seconds…" boilerplate. We derive a
// unique one from each calc's own article/desc instead.
const _GENERIC_META = /get precise results in seconds|resultados exactos en segundos|no registration required|sin registro|résultats précis en quelques secondes|ohne registrierung|risultati precisi in pochi secondi|resultados precisos em segundos/i;
// Trailing function words across the six site languages. A snippet that stops on one
// ("…round up to the…") reads as broken text in the search result and costs clicks.
const _SNIPPET_STOP = new Set([
  "the","a","an","of","to","and","or","for","in","on","at","is","are","be","by","with","from",
  "that","this","as","its","your","you","it","per","into","than","so","if","when","which","but",
  "not","we","our","each","every","then","about","use","using",
  "el","la","los","las","un","una","de","del","y","o","en","por","para","con","que","se","su",
  "sus","al","lo","como","entre","cada","sobre",
  "le","les","une","des","du","et","ou","dans","pour","avec","qui","sur","aux","ce","cette","par",
  "der","die","das","den","dem","ein","eine","einen","und","oder","mit","von","zum","zur","im",
  "auf","für","ist","sind","bei","aus","dabei","sie",
  "il","gli","uno","dei","delle","nel","nella","che","sul","alla",
  "os","um","uma","dos","das","no","na","pelo","pela","ao",
]);

// Cut a snippet at a boundary a reader recognises: a whole sentence if one fits, else a
// clause, else a word boundary with any dangling function words trimmed off.
function _snippet(text, max) {
  const t = String(text || "").trim();
  if (t.length <= max) return t;
  const win = t.slice(0, max + 1);

  const sent = win.match(/^[\s\S]*[.!?](?=\s|$)/);
  if (sent && sent[0].trim().length >= 90) return sent[0].trim();

  const clause = win.match(/^[\s\S]*[,;:](?=\s)/);
  let d;
  if (clause && clause[0].trim().length >= 95) d = clause[0].replace(/[\s,;:]+$/, "");
  else d = win.slice(0, win.lastIndexOf(" "));

  // Drop dangling function words ("…of the", "…dabei die") whichever branch produced d.
  let parts = d.replace(/[\s,;:.]+$/, "").split(/\s+/);
  for (let i = 0; i < 4 && parts.length > 4; i++) {
    const last = parts[parts.length - 1].replace(/[.,;:()]+$/, "").toLowerCase();
    if (_SNIPPET_STOP.has(last)) parts.pop(); else break;
  }
  return parts.join(" ").replace(/[\s,;:.]+$/, "") + "…";
}

function buildMetaDescription(langData, name) {
  // 1. Derive from the article's opening (always unique per calculator).
  // De-LaTeX BEFORE truncating: slicing at 158 chars can cut a \frac{…}{…} in half,
  // after which no converter can recover it and the snippet shows raw markup.
  const lc = _deLatex(langData.long_content || "");
  if (lc.length > 200) {
    let t = lc.replace(/<[^>]+>/g, " ").replace(/&[a-z]+;/g, " ").replace(/\s+/g, " ").trim();
    t = t.replace(/^TL;?\s*DR:?\s*/i, "");
    if (t.length > 70) {
      return _snippet(t, 158);
    }
  }
  // 2. Stored SEO description, only if it is NOT the generic template
  const sd = _prose((langData.seo_description || "").trim());
  if (sd && !_GENERIC_META.test(sd)) return sd;
  // 3. Unique fallback built from this calc's own one-line desc
  const d = _deMojibake((langData.desc || "").trim());
  if (d) return _snippet(`${name}: ${d}`, 158);
  return `${name} — instant, accurate results online, free.`;
}

// Fingerprint of the bundled front-end assets, appended to their URLs so a deploy is a
// new URL. Without it the immutable 7-day cache keeps returning visitors on the old JS.
const _ASSET_VER = (() => {
  try {
    const crypto = require("crypto"), fsx = require("fs"), pathx = require("path");
    const h = crypto.createHash("sha256");
    for (const f of ["calculator.js", "styles.css", "analytics-tracker.js"]) {
      try { h.update(fsx.readFileSync(pathx.join(__dirname, "assets", f))); } catch (e) {}
    }
    return h.digest("hex").slice(0, 10);
  } catch (e) { return String(Date.now()); }
})();

function buildPage(slug, lang, data) {
  data = _applyLangSlugs(slug, data); // authoritative translated slugs for URLs
  const ui = _uiFor(lang); // localised UI chrome (Inputs/Result/Calculate…)
  const langData = (data.langs && data.langs[lang]) || {};
  const rawName = _prose(langData.name || data.slug || slug);
  const name = esc(rawName);
  const desc = esc(_prose(buildMetaDescription(langData, rawName)));
  const seoTitle = esc(_prose(buildSeoTitle(lang, langData, rawName)));
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

  // Outputs must be an OBJECT { id: label } plus output_units { id: unit } — this
  // is the format the client engine (calculator.js) reads with Object.keys. The
  // old array form left results blank because Object.keys(array) yields indices.
  const outLabels = langData.outputs_labels || {};
  const outObj = {};
  const outUnits = {};
  outputs.forEach(o => {
    if (!o || !o.id) return;
    const ol = outLabels[o.id];
    outObj[o.id] = _deMojibake((ol && ol !== o.id) ? ol : (o.label && o.label !== o.id ? o.label : humanizeId(o.id)));
    if (o.unit != null && o.unit !== "") outUnits[o.id] = _deMojibake(_localizeUnit(o.unit, lang));
  });

  const calcConfig = {
    slug,
    lang,
    inputs: inputs.map(i => ({
      id: i.id, min: i.min, max: i.max, step: i.step,
      default: i.default, unit: i.unit,
      unit_options: i.unit_options || [i.unit],
      unit_category: i.unit_category,
    })),
    outputs: outObj,
    output_units: outUnits,
    formula: data.formula || "return {}",
  };
  // Visual gauge/meter (e.g. BMI category bar) — carry it through if the calc has one.
  if (data.gauge) calcConfig.gauge = data.gauge;
  if (langData.result_context) calcConfig.result_context = _prose(langData.result_context);
  // Result interpretation: structure (scale/tone/thresholds) is language-neutral and
  // lives at the doc root; the wording lives per language. Merge them by index so a
  // missing translation degrades to no verdict rather than to English on a Spanish page.
  if (data.interpretation && data.interpretation.output) {
    const it = data.interpretation;
    const txt = langData.interpretation_text;
    if (txt) {
      const merged = { output: it.output, unit: it.unit || "" };
      if (it.mode === "bands" && Array.isArray(it.bands) && Array.isArray(txt.bands) && it.bands.length === txt.bands.length) {
        merged.scale = it.scale;
        merged.bands = it.bands.map((bd, i) => ({
          max: bd.max, tone: bd.tone,
          label: _prose(txt.bands[i].label), note: _prose(txt.bands[i].note),
        }));
        if (txt.source) merged.source = _prose(txt.source);
        calcConfig.interpretation = merged;
      } else if (it.mode === "insight" && txt.insight) {
        merged.insight = _prose(txt.insight);
        if (txt.tip) merged.tip = _prose(txt.tip);
        calcConfig.interpretation = merged;
      }
    }
  }

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
  <link rel="preload" as="style" href="/css/styles.css?v=${_ASSET_VER}">
  <link rel="preload" as="script" href="/js/calculator.js?v=${_ASSET_VER}">
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
  <link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/manifest.json">
  <link rel="stylesheet" href="/css/styles.css?v=${_ASSET_VER}">
  <link rel="preconnect" href="https://pagead2.googlesyndication.com">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ADSENSE_ID}" crossorigin="anonymous"></script>
  <script>if(localStorage.getItem('ctw-theme')==='dark')document.documentElement.setAttribute('data-theme','dark');</script>
  <script>window.COOKIE_CONSENT_I18N={"privacy_path":"/${lang}/privacy/"};</script>
  <script src="/js/cookie-consent.js?v=${_ASSET_VER}" defer></script>
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
  <div class="ad-slot ad-slot-banner"><ins class="adsbygoogle" style="display:block;width:100%;min-width:250px" data-ad-client="${ADSENSE_ID}" data-ad-format="auto" data-full-width-responsive="true"></ins>
  <script>(function(s){var d=s.parentNode;function go(){try{var i=d.querySelector('ins.adsbygoogle');if(!i)return;if(i.getAttribute('data-adsbygoogle-status')||i.getAttribute('data-ad-status'))return;if(!i.offsetWidth)return;(adsbygoogle=window.adsbygoogle||[]).push({});}catch(e){}}function arm(){setTimeout(go,400);}if(document.readyState==='complete')arm();else window.addEventListener('load',arm);})(document.currentScript);</script></div>
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

  ${langData.desc ? `<div class="calc-intro"><strong>${name}</strong> — ${esc(_deMojibake(langData.desc))}</div>` : ""}

  <div class="content-main">
    <div class="calc-layout">
      <div class="card">
        <div class="card-title">${esc(ui.inputs)}</div>
        <form id="calc-form" novalidate>
          ${renderInputsForm(inputs, langData, lang)}
          <div class="btn-row">
            <button type="submit" class="btn btn-primary">${esc(ui.calculate)}</button>
            <button type="button" class="btn btn-secondary" id="btn-reset">${esc(ui.reset)}</button>
          </div>
        </form>
      </div>

      <div class="card results-panel">
        <div class="card-title">${esc(ui.result)}</div>
        <div id="calc-results" aria-live="polite">
          <div class="result-placeholder">${esc(ui.enterValues)}</div>
          ${renderResults(outputs, langData)}
        </div>
        <div class="results-actions">
          <button class="btn btn-secondary copy-btn" id="btn-copy" style="display:none;">${esc(ui.copyResults)}</button>
          <button class="btn btn-secondary share-btn" id="btn-share" style="display:none;">🔗 ${esc(ui.share)}</button>
          <button class="btn btn-secondary embed-btn" id="btn-embed" title="${esc(ui.embed)}">&#60;/&#62; ${esc(ui.embed)}</button>
        </div>
        <div class="feedback-wrap">
          <span class="feedback-label">${esc(ui.helpful)}</span>
          <button class="feedback-btn" data-val="yes" aria-label="Yes">&#128077;</button>
          <button class="feedback-btn" data-val="no" aria-label="No">&#128078;</button>
        </div>
      </div>
    </div>

    ${(data.comparison_presets || []).length ? `
    <div class="comparison-table-wrap" tabindex="0" role="region" aria-label="Comparison presets">
      <div class="comparison-table-title">${esc(ui.examples)}</div>
      <table class="comparison-table" id="comparison-table">
        <thead><tr><th></th>${inputs.map(i => { const il = (langData.inputs_labels || {})[i.id]; return `<th>${esc(_niceLabel(il && il !== i.id ? il : humanizeId(i.id)))}</th>`; }).join("")}</tr></thead>
        <tbody>
          ${(data.comparison_presets || []).map((p, _pi) => {
            // Support both shapes: CMS { label, inputs:{id:val} } and the static
            // flat form { _label, id1:val1, id2:val2 } (values at top level).
            const pv = (p.inputs && typeof p.inputs === "object")
              ? p.inputs
              : Object.fromEntries(Object.entries(p).filter(([k]) => k !== "label" && k !== "_label" && k !== "inputs"));
            // Prefer a per-language translated preset label when present, else localize tiers.
            const _plLoc = Array.isArray(langData.preset_labels) ? langData.preset_labels[_pi] : null;
            const pl = _deMojibake((_plLoc && String(_plLoc)) || _localizePreset(p.label || p._label || "", lang));
            return `<tr data-prefill='${esc(JSON.stringify(pv))}'>
            <td class="preset-label-cell">${esc(pl)}</td>
            ${inputs.map(i => {
              if (pv[i.id] === undefined) return "<td>—</td>";
              const hasOpts = Array.isArray(i.options || i.choices) && (i.options || i.choices).length;
              return `<td>${esc(hasOpts ? _localizeOption(i.id, pv[i.id], langData, lang) : String(pv[i.id]))}</td>`;
            }).join("")}
          </tr>`;
          }).join("")}
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
      <p class="embed-modal-desc">Copy this code to add the free calculator to your site. It's fully responsive and always up to date. Please keep the small credit link — it's what lets you use it for free.</p>
      <textarea class="embed-modal-code" id="embed-modal-code" readonly rows="7"></textarea>
      <button class="btn btn-primary embed-modal-copy" id="embed-modal-copy">Copy embed code</button>
    </div>
  </div>
</div>
<script>
window.CALC_CONFIG = ${JSON.stringify(calcConfig)};
</script>
<!-- Firebase SDK + first-party analytics tracker. buildPage previously omitted
     these, which silently killed page_view/calculation tracking across the whole
     catalog once every page was server-rendered. -->
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore-compat.js"></script>
<script>
window.firebaseConfig = {apiKey:"AIzaSyBmjGOakF8HneBc2cnmt6WeEfU4JWgJFw8",authDomain:"calctowork.firebaseapp.com",projectId:"calctowork",storageBucket:"calctowork.firebasestorage.app",messagingSenderId:"538330151764",appId:"1:538330151764:web:175e3ff0f7d87f706b66c1",measurementId:"G-FBFV87HD35"};
try { firebase.initializeApp(window.firebaseConfig); } catch(e) {}
</script>
<script src="/js/analytics-tracker.js?v=${_ASSET_VER}"></script>
<script src="/js/calculator.js?v=${_ASSET_VER}" defer></script>
<script src="/js/dark-mode.js?v=${_ASSET_VER}" defer></script>
<script src="/js/favorites.js?v=${_ASSET_VER}" defer></script>
<script src="/js/history.js?v=${_ASSET_VER}" defer></script>
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

    // Build inputs_labels and outputs_labels for translation
    const inputsLabels = enContent.inputs_labels || {};
    const outputsLabels = enContent.outputs_labels || {};

    const prompt = `Translate the following calculator content from English to ${targetName}.
Return ONLY a valid JSON object with the same structure. Translate all string values. Keep {placeholder} tokens (like {result}) unchanged. Do NOT include long_content.

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
  faq: (enContent.faq || []).slice(0, 4),
  inputs_labels: inputsLabels,
  outputs_labels: outputsLabels,
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
        body: JSON.stringify({ model: provCfg.model || "claude-haiku-4-5-20251001", max_tokens: 6000, messages: [{ role: "user", content: prompt }] }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.content && d.content[0] && d.content[0].text;
    } else if (provider === "openai" || provider === "deepseek") {
      const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
      const effectiveModel = (provider === "deepseek" && (provCfg.model || "").includes("reasoner")) ? "deepseek-chat" : (provCfg.model || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini"));
      const r = await fetch(`${baseUrl}/chat/completions`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
        body: JSON.stringify({ model: effectiveModel, messages: [{ role: "user", content: prompt }], max_tokens: 6000 }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
    }

    const jsonMatch = text && text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) return res.status(500).json({ error: "Could not parse AI response", preview: (text||"").slice(0, 200) });

    const translated = JSON.parse(jsonMatch[0]);

    // Preserve range_hints from English (not translatable)
    translated.range_hints = enContent.range_hints || {};
    translated.slug = enContent.slug || slug;

    return res.status(200).json({ translated });
  } catch (e) {
    console.error("translateCalc error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * regenResultContextHttp — batch-regenerates langs[lang].result_context for calcs whose
 * copy is broken (machine-translation leakage, raw output-ids as words, wrong placeholder
 * ids). Generates native-quality one-line copy in all 6 langs via the configured LLM,
 * validates that placeholders reference ONLY the real output ids, writes calc_cms, and
 * republishes the processed slugs in ONE _deployPagesToHosting call.
 * POST { items:[{slug,name,outputs:[{id,unit}],labels:{id:label},en_seed}], republish:bool }
 */
exports.regenResultContextHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const items = (req.body && req.body.items) || [];
    const republish = !!(req.body && req.body.republish);
    if (!items.length) return res.status(400).json({ error: "No items" });

    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key || (functions.config().anthropic && functions.config().anthropic.key);
    if (!apiKey) return res.status(500).json({ error: `No API key for provider ${provider}` });

    const LANG_NAMES = { en: "English", es: "Spanish", fr: "French", de: "German", it: "Italian", pt: "Portuguese" };
    async function callAI(prompt) {
      let text;
      if (provider === "anthropic" || !cfg.active_provider) {
        const r = await fetch("https://api.anthropic.com/v1/messages", {
          method: "POST",
          headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
          body: JSON.stringify({ model: provCfg.model || "claude-haiku-4-5-20251001", max_tokens: 1500, messages: [{ role: "user", content: prompt }] }),
        });
        if (!r.ok) throw new Error("AI error: " + await r.text());
        const d = await r.json();
        text = d.content && d.content[0] && d.content[0].text;
      } else {
        const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
        const model = provCfg.model || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini");
        const r = await fetch(`${baseUrl}/chat/completions`, {
          method: "POST",
          headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
          body: JSON.stringify({ model, messages: [{ role: "user", content: prompt }], max_tokens: 1500 }),
        });
        if (!r.ok) throw new Error("AI error: " + await r.text());
        const d = await r.json();
        text = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
      }
      const m = text && text.match(/\{[\s\S]*\}/);
      if (!m) throw new Error("No JSON in AI response");
      return JSON.parse(m[0]);
    }

    const results = [];
    const filesToDeploy = {};
    for (const it of items) {
      const outIds = (it.outputs || []).map(o => o.id).filter(Boolean);
      if (!it.slug || !outIds.length) { results.push({ slug: it.slug, ok: false, reason: "no slug/outputs" }); continue; }
      const outLines = (it.outputs || []).map(o => {
        const lbl = (it.labels && it.labels[o.id]) || o.id;
        return `- {${o.id}} = the ${lbl}${o.unit ? ` (unit: ${o.unit})` : ""}`;
      }).join("\n");
      const prompt = `You write result-explanation microcopy for an online calculator, in 6 languages.

Calculator: "${it.name}"
It outputs these values. Use these EXACT ids as placeholders in curly braces:
${outLines}

Reference meaning (English, may be low quality — use only to understand intent): "${it.en_seed || ""}"

Write ONE short sentence (max ~28 words) per language explaining what the output value(s) mean to a user who just saw a result. Rules:
- Native and natural in each target language — no English words leaking into non-English languages, no translationese.
- Name each output with a human phrase, then its value in parentheses, e.g. "the volume ({${outIds[0]}})".
- Use ONLY these placeholders: ${outIds.map(x => "{" + x + "}").join(", ")}. Never invent other {tokens}. NEVER write a raw id like "${outIds[0]}" as a plain word.
- No markdown, no surrounding quotes.

Return ONLY a JSON object: {"en":"...","es":"...","fr":"...","de":"...","it":"...","pt":"..."}`;

      let gen;
      try { gen = await callAI(prompt); } catch (e) { results.push({ slug: it.slug, ok: false, reason: "ai:" + e.message.slice(0, 80) }); continue; }

      // validate + build langs patch
      const langsPatch = {};
      // Only flag snake_case ids (e.g. area_lateral) as raw-id-as-word — single common-word
      // ids like "dot"/"area" are legitimate prose, so don't reject sentences that contain them.
      const rawIds = outIds.filter(x => x.includes("_"));
      const rawIdRe = rawIds.length ? new RegExp("(^|[\\s;(])(" + rawIds.map(x => x.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|") + ")(?![^(]*\\))") : null;
      let wrote = 0;
      for (const l of Object.keys(LANG_NAMES)) {
        let s = gen[l];
        if (!s || typeof s !== "string") continue;
        s = s.trim().replace(/^"+|"+$/g, "");
        const tokens = (s.match(/\{([^}]+)\}/g) || []).map(t => t.slice(1, -1));
        const badTok = tokens.some(t => !outIds.includes(t));
        const rawId = rawIdRe ? rawIdRe.test(s.replace(/\{[^}]*\}/g, "")) : false;
        if (badTok || rawId || !tokens.length) continue; // skip invalid — never make it worse
        langsPatch[l] = { result_context: s };
        wrote++;
      }
      if (!wrote) { results.push({ slug: it.slug, ok: false, reason: "all langs failed validation" }); continue; }

      await db.collection("calc_cms").doc(it.slug).set({ langs: langsPatch }, { merge: true });
      results.push({ slug: it.slug, ok: true, langsWritten: wrote });

      if (republish) {
        try {
          const dsnap = await db.collection("calc_cms").doc(it.slug).get();
          if (dsnap.exists && dsnap.data().status === "published") {
            const f = await _buildCalcFiles(it.slug, dsnap.data());
            Object.assign(filesToDeploy, f);
          }
        } catch (e) { /* build failure is non-fatal for the write */ }
      }
    }

    let deploy = null;
    if (republish && Object.keys(filesToDeploy).length) {
      const r = await _deployPagesToHosting(filesToDeploy, `[RegenRC] ${results.filter(x => x.ok).length} calcs`);
      deploy = r.error ? { error: r.error } : { deployed: true, files: Object.keys(filesToDeploy).length };
    }
    return res.status(200).json({ processed: items.length, ok: results.filter(x => x.ok).length, results, deploy });
  } catch (e) {
    console.error("regenResultContextHttp error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * aiFixCalcHttp — ONE-CLICK per-calc AI fix used by the Page-1 Tracker "Fix with AI"
 * button. Accepts any slug (base OR a translated per-language slug), resolves it to the
 * calc, regenerates native-quality result_context in all 6 langs (validated placeholders),
 * writes calc_cms, and republishes the calc. POST { slug }
 */
exports.aiFixCalcHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const path = require("path"), fs = require("fs");
    const inSlug = (req.body && req.body.slug || "").trim();
    // content:false skips the (slower) long-form article + FAQ regen; default = full fix.
    const doContent = !(req.body && req.body.content === false);
    // targeted:true → inspect every field and regenerate ONLY the broken langs/fields.
    const targeted = !!(req.body && req.body.targeted);
    if (!inSlug) return res.status(400).json({ error: "Missing slug" });

    // Resolve to the base calc (calc_cms doc id) from any base/translated slug.
    let index = [];
    try { const raw = require(path.join(__dirname, "calc-index.json")); index = Array.isArray(raw) ? raw : (raw.calcs || Object.values(raw)); } catch (e) {}
    let entry = index.find(e => e.slug === inSlug) || index.find(e => e.slugs && Object.values(e.slugs).includes(inSlug));
    const baseSlug = entry ? entry.slug : inSlug;
    const id = entry ? String(entry.id) : null;

    // Gather outputs (ids/units), name, formula/inputs and English seed from static calc files
    // (the engine config lives in static calc.json, NOT in calc_cms).
    let outputs = [], name = baseSlug, seed = "", labels = {}, engFormula = "", engInputs = 0, engPresets = 0;
    let engInputsArr = [], engExampleInputs = null, engPresetsArr = [], engRelated = [];
    if (id) {
      try {
        const cj = JSON.parse(fs.readFileSync(path.join(__dirname, "calcs", id, "calc.json"), "utf8"));
        outputs = (cj.outputs || []).map(o => ({ id: o.id, unit: o.unit }));
        name = cj.name || name;
        engFormula = cj.formula || ""; engInputs = (cj.inputs || []).length; engPresets = (cj.comparison_presets || []).length;
        engInputsArr = cj.inputs || []; engExampleInputs = cj.example_inputs || null; engPresetsArr = cj.comparison_presets || []; engRelated = cj.related || [];
      } catch (e) {}
      try { const en = JSON.parse(fs.readFileSync(path.join(__dirname, "calcs", id, "en.json"), "utf8")); name = en.name || name; seed = en.result_context || ""; labels = en.outputs || {}; } catch (e) {}
    }
    // Load the static per-language files — the canonical source for name/labels/hints,
    // since calc_cms usually lacks inputs/inputs_labels (those live only in the static files).
    const staticLangs = {};
    if (id) { for (const L of ["en", "es", "fr", "de", "it", "pt"]) { try { staticLangs[L] = JSON.parse(fs.readFileSync(path.join(__dirname, "calcs", id, L + ".json"), "utf8")); } catch (e) {} } }
    // Fall back to calc_cms outputs if static had none.
    const docRef = db.collection("calc_cms").doc(baseSlug);
    const snap0 = await docRef.get();
    if (!snap0.exists) return res.status(404).json({ error: "Calc not found: " + baseSlug });
    const doc0 = snap0.data();
    if (!outputs.length && Array.isArray(doc0.outputs)) outputs = doc0.outputs.map(o => ({ id: o.id, unit: o.unit }));
    if (!seed) seed = (doc0.langs && doc0.langs.en && doc0.langs.en.result_context) || "";
    const outIds = outputs.map(o => o.id).filter(Boolean);
    if (!outIds.length) return res.status(400).json({ error: "No outputs to reference for " + baseSlug });

    // Configured LLM.
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key || (functions.config().anthropic && functions.config().anthropic.key);
    if (!apiKey) return res.status(500).json({ error: `No API key for provider ${provider}` });

    // Reusable LLM call → parsed JSON object.
    async function ai(prompt, maxTokens) {
      let t;
      if (provider === "anthropic" || !cfg.active_provider) {
        const r = await fetch("https://api.anthropic.com/v1/messages", {
          method: "POST",
          headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
          body: JSON.stringify({ model: provCfg.model || "claude-haiku-4-5-20251001", max_tokens: maxTokens, messages: [{ role: "user", content: prompt }] }),
        });
        if (!r.ok) throw new Error("AI error: " + await r.text());
        const d = await r.json(); t = d.content && d.content[0] && d.content[0].text;
      } else {
        const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
        const model = provCfg.model || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini");
        const r = await fetch(`${baseUrl}/chat/completions`, {
          method: "POST",
          headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
          body: JSON.stringify({ model, messages: [{ role: "user", content: prompt }], max_tokens: maxTokens }),
        });
        if (!r.ok) throw new Error("AI error: " + await r.text());
        const d = await r.json(); t = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
      }
      const mm = t && t.match(/\{[\s\S]*\}/);
      if (!mm) throw new Error("No JSON in AI response");
      return JSON.parse(mm[0]);
    }

    const outLines = outputs.map(o => `- {${o.id}} = the ${(labels[o.id] || o.id)}${o.unit ? ` (unit: ${o.unit})` : ""}`).join("\n");
    const prompt = `You write result-explanation microcopy for an online calculator, in 6 languages.

Calculator: "${name}"
It outputs these values. Use these EXACT ids as placeholders in curly braces:
${outLines}

Reference meaning (English, may be low quality — use only to understand intent): "${seed}"

Write ONE short sentence (max ~28 words) per language explaining what the output value(s) mean to a user who just saw a result. Rules:
- Native and natural in each target language — no English words leaking into non-English languages, no translationese.
- Name each output with a human phrase, then its value in parentheses, e.g. "the volume ({${outIds[0]}})".
- Use ONLY these placeholders: ${outIds.map(x => "{" + x + "}").join(", ")}. Never invent other {tokens}. NEVER write a raw id like "${outIds[0]}" as a plain word.
- No markdown, no surrounding quotes.

Return ONLY a JSON object: {"en":"...","es":"...","fr":"...","de":"...","it":"...","pt":"..."}`;

    // ── Detection helpers (targeted mode fixes only what's broken) ──
    const LANGS6 = ["en", "es", "fr", "de", "it", "pt"];
    const NAMES = { en: "English", es: "Spanish", fr: "French", de: "German", it: "Italian", pt: "Portuguese" };
    // Only snake_case ids (area_lateral) count as raw-id-as-word; single common words (dot) are fine.
    const rawIds = outIds.filter(x => x.includes("_"));
    const rawIdRe = rawIds.length ? new RegExp("(^|[\\s;(])(" + rawIds.map(x => x.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|") + ")(?![^(]*\\))") : null;
    const strip = h => String(h || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    // Distinctive function words per language — used to detect the WRONG language leaking in.
    const LW = {
      en: /\b(the|and|with|of|is|for|this|your|value|result|output|calculated|how|use)\b/gi,
      es: /\b(el|la|los|las|del|con|para|una|un|número|cálculo|cómo|resultado|valor|incluye|soporte|cantidad)\b/gi,
      pt: /\b(o|os|as|do|da|dos|com|para|uma|número|cálculo|como|resultado|valor|você|são|não|é|quantidade)\b/gi,
      fr: /\b(le|les|des|avec|pour|une|votre|nombre|calcul|comment|résultat|valeur|est)\b/gi,
      de: /\b(der|die|das|und|mit|für|eine|ihre|zahl|berechnung|wie|ergebnis|wert|ist)\b/gi,
      it: /\b(il|gli|con|per|una|numero|calcolo|come|risultato|valore|è|di)\b/gi,
    };
    const score = (t, l) => { const m = String(t || "").match(LW[l]); return m ? m.length : 0; };
    function wrongLang(t, target) {
      t = String(t || ""); if (t.length < 12) return false;
      const sc = {}; LANGS6.forEach(l => sc[l] = score(t, l));
      const best = LANGS6.slice().sort((a, b) => sc[b] - sc[a])[0];
      return sc[best] >= 2 && best !== target && sc[best] > (sc[target] || 0) + 1;
    }
    function rcBroken(t, lang) {
      if (!t || typeof t !== "string") return true;
      const tokens = (t.match(/\{([^}]+)\}/g) || []).map(x => x.slice(1, -1));
      if (!tokens.length) return true;
      if (tokens.some(x => !outIds.includes(x))) return true;
      if (rawIdRe && rawIdRe.test(t.replace(/\{[^}]*\}/g, ""))) return true;
      if (lang !== "en" && wrongLang(t, lang)) return true;
      return false;
    }
    const txtBroken = (t, lang, minLen) => !t || typeof t !== "string" || t.trim().length < (minLen || 1) || (lang !== "en" && wrongLang(t, lang));
    const arrBroken = (a, lang) => !Array.isArray(a) || a.length < 2 || (lang !== "en" && wrongLang(a.join(" "), lang));
    function lcBroken(html, faq, lang) {
      const txt = strip(html);
      if (txt.length < 400) return true;
      if (!Array.isArray(faq) || faq.length < 2) return true;
      if (lang !== "en" && wrongLang(txt.slice(0, 600), lang)) return true;
      return false;
    }

    const langs0 = doc0.langs || {};
    // Per-field broken sets. In FULL mode everything is flagged for regeneration.
    const brk = { rc: {}, meta: {}, steps: {}, mistakes: {}, lc: {} };
    for (const l of LANGS6) {
      const L = langs0[l] || {};
      brk.rc[l]       = targeted ? rcBroken(L.result_context, l) : true;
      brk.meta[l]     = targeted ? (txtBroken(L.seo_title, l, 10) || txtBroken(L.seo_description, l, 30)) : true;
      brk.steps[l]    = targeted ? arrBroken(L.steps, l) : true;
      brk.mistakes[l] = targeted ? arrBroken(L.mistakes, l) : true;
      brk.lc[l]       = targeted ? lcBroken(L.long_content, L.faq, l) : true;
    }

    // ── Engine / functional CHECKS (report only; the math config is never modified,
    // except `related` internal links which we top up when too few). ──
    const inputsArr = engInputsArr.length ? engInputsArr : (doc0.inputs || []);
    const outputsArr = outputs.length ? outputs : (doc0.outputs || []);
    // Prefer calc_cms presets (may hold prior auto-repairs) so re-runs are idempotent.
    const presetsArr = (Array.isArray(doc0.comparison_presets) && doc0.comparison_presets.length) ? doc0.comparison_presets : engPresetsArr;
    const formulaStr = engFormula || doc0.formula || "";
    const outIdList = outputsArr.map(o => o.id).filter(Boolean);
    const inpOptions = i => i.options || i.choices || (Array.isArray(i.unit_options) && i.type !== "number" ? i.unit_options : null);
    function synthInputs() {
      // Best-guess inputs when a calc lacks defaults: select→first option, numeric→default/mid/min/1.
      const s = {};
      inputsArr.forEach(i => {
        if (i.default != null) { s[i.id] = i.default; return; }
        const opts = inpOptions(i);
        if (opts && opts.length) { s[i.id] = (opts[0] && opts[0].value != null) ? opts[0].value : opts[0]; return; }
        if (typeof i.min === "number" && typeof i.max === "number" && i.max < 1e9) s[i.id] = i.min > 0 ? +(i.min + (i.max - i.min) * 0.4).toPrecision(4) : +((i.max) * 0.4).toPrecision(4);
        else if (typeof i.min === "number" && i.min > 0) s[i.id] = i.min;
        else s[i.id] = 10;
      });
      return s;
    }
    // Valid = a finite number, any string (incl. optional-empty "nota"), or an array/object
    // (e.g. an amortization "schedule"). Only undefined/null/NaN/Infinity is a real failure.
    const validOut = v => v !== undefined && v !== null && !(typeof v === "number" && !isFinite(v));
    const allValid = r => r && !r.error && outIdList.length && outIdList.every(id => validOut(r[id]));
    // Whether the calc has REAL sample inputs (author-provided), vs only synthesized guesses.
    const hasRealInputs = !!(engExampleInputs && Object.keys(engExampleInputs).length) || presetsArr.length > 0 || inputsArr.some(i => i.default != null);
    // #1 does the math actually compute? + #6 verified example numbers for the article.
    let compute = { ok: null, msg: "no formula" };
    let hasInterpretation = !!doc0.gauge; // gauge config counts as interpretation
    const CAT_KEY = /^(categor|category|categorie|categoria_imc|nivel|rating|clasific|estado|status|zona\d?|zone\d?|z\d)$/i;
    const verified = [];
    if (formulaStr) {
      let fn = null;
      try { fn = new Function("inputs", '"use strict";' + formulaStr); } catch (e) { compute = { ok: false, msg: "syntax: " + e.message.slice(0, 80) }; }
      if (fn) {
        try {
          // Try several input sets; the calc "computes" if ANY real set yields valid outputs.
          const trials = [];
          if (engExampleInputs && Object.keys(engExampleInputs).length) trials.push({ real: true, iv: Object.assign(synthInputs(), engExampleInputs) });
          presetsArr.slice(0, 3).forEach(p => { const pv = (p.inputs && typeof p.inputs === "object") ? p.inputs : Object.fromEntries(Object.entries(p).filter(([k]) => !["label", "_label", "inputs"].includes(k))); trials.push({ real: true, iv: Object.assign(synthInputs(), pv) }); });
          trials.push({ real: hasRealInputs, iv: synthInputs() });
          let passed = false, anyReal = false, sawError = false;
          for (const t of trials) {
            let rr; try { rr = fn(t.iv); } catch (e) { continue; }
            if (rr && typeof rr === "object" && Object.keys(rr).some(k => CAT_KEY.test(k))) hasInterpretation = true;
            if (t.real) anyReal = true;
            if (rr && rr.error) sawError = true;
            if (allValid(rr)) { passed = true; if (verified.length < 3) verified.push(`inputs {${Object.entries(t.iv).slice(0, 6).map(([k, v]) => k + ":" + v).join(", ")}} → ${outIdList.map(id => id + "=" + (typeof rr[id] === "object" ? "[…]" : rr[id])).join(", ")}`); }
          }
          if (passed) compute = { ok: true, msg: "ok" };
          else if (anyReal) compute = { ok: false, msg: sawError ? "returns error for sample inputs" : "non-finite/missing output" };
          else compute = { ok: null, msg: "untested (no defaults/example inputs)" };
        } catch (e) { compute = { ok: false, msg: "threw: " + e.message.slice(0, 80) }; }
      }
    }
    // #2 preset input values within each input's min/max (and present + numeric).
    const presetIssues = [];
    presetsArr.forEach((p, pi) => {
      const pv = (p.inputs && typeof p.inputs === "object") ? p.inputs : Object.fromEntries(Object.entries(p).filter(([k]) => !["label", "_label", "inputs"].includes(k)));
      inputsArr.forEach(inp => {
        // Only sanity-check NUMERIC inputs; select/text inputs (options) hold non-numeric values.
        const isNumeric = (inp.type ? inp.type === "number" : true) && !(inp.options || inp.choices);
        if (!isNumeric) return;
        const v = pv[inp.id];
        if (v === undefined || v === null || v === "") { presetIssues.push(`#${pi} missing ${inp.id}`); return; }
        const n = parseFloat(v);
        if (isNaN(n)) presetIssues.push(`#${pi} ${inp.id} not numeric`);
        else if (typeof inp.min === "number" && n < inp.min) presetIssues.push(`#${pi} ${inp.id}<min`);
        else if (typeof inp.max === "number" && inp.max < 1e11 && n > inp.max) presetIssues.push(`#${pi} ${inp.id}>max`);
      });
    });
    // #2b auto-repair preset values that are out of range only because of a clean unit-scale
    // error (e.g. block_height 0.2 in metres sitting in a cm field with min 10 → ×100 = 20).
    let presetsFixed = 0;
    if (presetIssues.length && presetsArr.length) {
      const FACTORS = [100, 1000, 10, 0.1, 0.01, 0.001];
      const repaired = presetsArr.map(p => {
        const isFlat = !(p.inputs && typeof p.inputs === "object");
        const pv = isFlat ? Object.fromEntries(Object.entries(p).filter(([k]) => !["label", "_label", "inputs"].includes(k))) : { ...p.inputs };
        let touched = false;
        for (const inp of inputsArr) {
          const isNumeric = (inp.type ? inp.type === "number" : true) && !(inp.options || inp.choices);
          if (!isNumeric) continue;
          const v = parseFloat(pv[inp.id]); if (isNaN(v)) continue;
          const lo = typeof inp.min === "number" ? inp.min : -Infinity;
          const hi = (typeof inp.max === "number" && inp.max < 1e11) ? inp.max : Infinity;
          if (v >= lo && v <= hi) continue;
          let done = false;
          for (const f of FACTORS) { const nv = +(v * f).toPrecision(6); if (nv >= lo && nv <= hi) { pv[inp.id] = nv; touched = true; done = true; break; } }
          // Not a clean unit-scale error → clamp into the valid range so the example still works.
          if (!done && isFinite(lo) && isFinite(hi)) { pv[inp.id] = v < lo ? lo : hi; touched = true; }
        }
        if (!touched) return p;
        presetsFixed++;
        return isFlat ? { ...(p._label ? { _label: p._label } : {}), ...(p.label ? { label: p.label } : {}), ...pv } : { ...p, inputs: pv };
      });
      if (presetsFixed) await docRef.set({ comparison_presets: repaired }, { merge: true });
    }
    // #4 generic/placeholder output units.
    const genericUnits = outputsArr.filter(o => ["u", "u2", "u3", "u²", "u³", ""].includes(String(o.unit || "").trim())).map(o => o.id);
    // #4b preset examples that DON'T produce a valid result (e.g. pH with H+=0 → log(0)),
    // plus junk presets (all-zero / generic "Caso N" labels). Report-only for now.
    let badPresets = 0, junkPresetLabels = 0;
    if (formulaStr && presetsArr.length) {
      let pfn = null; try { pfn = new Function("inputs", '"use strict";' + formulaStr); } catch (e) {}
      const getPv = p => (p.inputs && typeof p.inputs === "object") ? p.inputs : Object.fromEntries(Object.entries(p).filter(([k]) => !["label", "_label", "inputs"].includes(k)));
      // Simulate what actually happens when a user clicks the preset: its values fill the
      // form, other fields keep their DEFAULT (no synthetic guesses). Catches presets that
      // don't set the needed inputs (pH: presets don't provide H+ → empty → log(0) broken).
      const defsOnly = {}; inputsArr.forEach(i => { if (i.default != null) defsOnly[i.id] = i.default; });
      if (pfn) presetsArr.forEach(p => { try { if (!allValid(pfn(Object.assign({}, defsOnly, getPv(p))))) badPresets++; } catch (e) { badPresets++; } });
      junkPresetLabels = presetsArr.filter(p => /^(caso|case|ejemplo|example|preset)\s*\d+$/i.test(String(p._label || p.label || "").trim())).length;
    }
    // #5 internal links — top up `related` to >=3 from same block/category if short.
    let relatedCount = (Array.isArray(doc0.related) && doc0.related.length) || (engRelated && engRelated.length) || 0;
    let relatedFilled = 0;
    if (relatedCount < 3 && entry && index.length) {
      try {
        const block = entry.block || entry.block_slug || entry.category;
        const cur = new Set((Array.isArray(doc0.related) && doc0.related.length ? doc0.related : engRelated).map(String));
        for (const e of index) { if (cur.size >= 4) break; if (!e || String(e.id) === String(id)) continue; if ((e.block && block && e.block === block) || (e.category && entry.category && e.category === entry.category)) cur.add(String(e.id)); }
        const merged = [...cur];
        if (merged.length > relatedCount) { await docRef.set({ related: merged }, { merge: true }); relatedFilled = merged.length - relatedCount; relatedCount = merged.length; }
      } catch (e) {}
    }
    const engineReport = {
      formula: formulaStr ? "present" : "MISSING",
      inputs: inputsArr.length, outputs: outputsArr.length, presets: presetsArr.length,
      compute, presetIssues, presetsFixed, badPresets, junkPresetLabels, genericUnits, relatedCount, relatedFilled, hasInterpretation,
      needsExample: !(engExampleInputs && Object.keys(engExampleInputs).length) && !inputsArr.some(i => i.default != null),
      mathUntouched: true,
    };

    // ── FIX 1: result_context (one call for all needed langs, write only broken ones) ──
    const langsPatch = {}; let rcWrote = 0;
    const needRC = LANGS6.filter(l => brk.rc[l]);
    if (needRC.length) {
      const gen = await ai(prompt, 1500);
      for (const l of needRC) {
        let s = gen[l]; if (!s || typeof s !== "string") continue;
        s = s.trim().replace(/^"+|"+$/g, "");
        const tokens = (s.match(/\{([^}]+)\}/g) || []).map(t => t.slice(1, -1));
        if (!tokens.length || tokens.some(t => !outIds.includes(t)) || (rawIdRe && rawIdRe.test(s.replace(/\{[^}]*\}/g, "")))) continue;
        (langsPatch[l] = langsPatch[l] || {}).result_context = s; rcWrote++;
      }
    }

    // ── FIX 2: SEO title/meta + steps + mistakes (per broken lang) ──
    let metaWrote = 0;
    const needMeta = LANGS6.filter(l => brk.meta[l] || brk.steps[l] || brk.mistakes[l]);
    for (const l of needMeta) {
      try {
        const mp = `You are writing calculator microcontent in ${NAMES[l]} for "${name}". Return ONLY JSON:
{"seo_title":"...","seo_description":"...","steps":["...","...","..."],"mistakes":["...","...","..."]}
Rules: native ${NAMES[l]} with no other language leaking in. seo_title <= 60 chars, phrased like a real search (e.g. "how to calculate ..."). seo_description <= 155 chars and include a number. steps = 3-5 short imperative how-to steps. mistakes = 3-4 common mistakes to avoid. No markdown, no extra keys.`;
        const g = await ai(mp, 1200);
        const patch = langsPatch[l] || {};
        if (brk.meta[l]) {
          if (g.seo_title && !wrongLang(g.seo_title, l)) patch.seo_title = String(g.seo_title).trim();
          if (g.seo_description && !wrongLang(g.seo_description, l)) patch.seo_description = String(g.seo_description).trim();
        }
        if (brk.steps[l] && Array.isArray(g.steps) && g.steps.length >= 2) patch.steps = g.steps.map(x => String(x));
        if (brk.mistakes[l] && Array.isArray(g.mistakes) && g.mistakes.length >= 2) patch.mistakes = g.mistakes.map(x => String(x));
        if (Object.keys(patch).length) { langsPatch[l] = patch; metaWrote++; }
      } catch (e) { /* skip a lang that fails */ }
    }

    // ── FIX 2.5: UI strings — calc name, short desc, input/output labels, preset labels ──
    // (the form labels a visitor reads first; translate from the English canonical). ──
    let uiWrote = 0;
    const sEn = staticLangs.en || {};
    const enL = langs0.en || {};
    let enName = sEn.name || enL.name || name;
    let enDesc = sEn.description || sEn.desc || enL.desc || enL.description || "";
    // English canonical label maps come from the static en.json (inputs/outputs), which is
    // where they actually live; fall back to humanized ids from the static inputs/outputs.
    let enInLabels = (sEn.inputs && Object.keys(sEn.inputs).length) ? sEn.inputs
      : (enL.inputs_labels && Object.keys(enL.inputs_labels).length) ? enL.inputs_labels
      : Object.fromEntries(inputsArr.map(i => [i.id, humanizeId(i.id)]));
    let enOutLabels = (sEn.outputs && Object.keys(sEn.outputs).length) ? sEn.outputs
      : (enL.outputs_labels && Object.keys(enL.outputs_labels).length) ? enL.outputs_labels
      : Object.fromEntries(outputsArr.map(o => [o.id, (labels[o.id] || humanizeId(o.id))]));
    const presetLabelsEN = presetsArr.map(p => p._label || p.label || "");
    const enExampleLabel = sEn.example_label || enL.example_label || "";
    const enRangeHints = (sEn.range_hints && typeof sEn.range_hints === "object" && !Array.isArray(sEn.range_hints)) ? sEn.range_hints : {};
    // The labels a visitor actually sees for lang l = calc_cms override if present, else static {l}.json.
    function curLabels(l, kind) { const L = langs0[l] || {}, S = staticLangs[l] || {}; const cms = kind === "in" ? L.inputs_labels : L.outputs_labels; if (cms && Object.keys(cms).length) return cms; return (kind === "in" ? S.inputs : S.outputs) || {}; }
    // Spanish-specific construction/measurement nouns that must NOT appear in other languages
    // (this site's source is Spanish, so leaks are almost always Spanish). High-precision list.
    const SPANISH_LEAK = /\b(encimera|salpicadero|espesor|anchura|profundidad|recortes|hueco|ladrillo|desperdicio|montantes?|barrotes?|pasamanos|tabique|pared|muro|caudal|losa|masillar|pasadas?|acometida|forjado|vigueta|sifón|sumidero|zócalo|rejilla|difusor|ahorro|mensual|anual|tama[nñ]o|muestra|confianza|plazo|cuota|ingreso|gasto|deuda|precio|cantidad|consumo|superficie|velocidad|distancia|energia|energía|potencia|aceleraci[oó]n|volumen|peso|altura|ancho|largo|alto|a[nñ]os|meses|dias|días|horas|tasa)\b/i;
    // A single string value is BAD for lang l if: identical to the English canonical
    // (untranslated), majority-foreign (wrongLang), or contains a Spanish noun leak.
    // A model told to strip Spanish from an English string sometimes "fixes" the letters
    // "es" INSIDE a word: Zones -> "Zon is", Series -> "Seri is", Calories -> "Calori is".
    // That reaches the <title> and <h1>, so reject it. Only for short label/name values
    // with no sentence punctuation — real prose may legitimately contain " is ".
    const MANGLED_WORD = /(?!^)[A-Z][a-z]{2,}s+(?:is|es|as|os)/;
    const looksMangled = v => {
      const t = String(v || '').trim();
      if (!t || t.length > 60 || /[.!?]/.test(t)) return false;
      return MANGLED_WORD.test(t);
    };
    function badVal(v, l, enV) {
      if (!v || typeof v !== "string") return false;
      const t = v.trim(); if (!t) return false;
      if (looksMangled(t)) return true;
      if (l !== "en" && enV && t.toLowerCase() === String(enV).trim().toLowerCase()) return true;
      if (l !== "en" && wrongLang(t, l)) return true;
      if (l !== "es" && SPANISH_LEAK.test(t)) return true;
      return false;
    }
    const mapBad = (cur, en, l) => Object.keys(en).some(id => badVal((cur || {})[id], l, en[id])) || (Object.keys(en).length && !Object.keys(cur || {}).length);
    function uiBrokenFor(l) {
      if (!targeted) return l !== "en";
      const L = langs0[l] || {}, S = staticLangs[l] || {};
      if (Object.keys(enInLabels).length && mapBad(curLabels(l, "in"), enInLabels, l)) return true;
      if (Object.keys(enOutLabels).length && mapBad(curLabels(l, "out"), enOutLabels, l)) return true;
      if (badVal(L.name || S.name, l, enName)) return true;
      if (badVal(L.desc || S.description || S.desc, l, enDesc)) return true;
      if (presetLabelsEN.some(Boolean) && !(Array.isArray(L.preset_labels) && L.preset_labels.length)) return true;
      if (enExampleLabel && badVal(L.example_label || S.example_label, l, enExampleLabel)) return true;
      return false;
    }
    // ── FIX 2.4: repair the ENGLISH canonical FIRST. English labels are often just the raw
    // (Spanish) input id — e.g. {"ahorro_mensual":"ahorro_mensual"} renders as "Ahorro mensual"
    // on the English page. Everything else translates FROM English, so fix it before FIX 2.5. ──
    let enFixed = 0;
    const isRawId = (v, k) => !v || String(v).trim() === k || String(v).trim().toLowerCase() === String(k).toLowerCase().replace(/_/g, " ");
    const enBad = (v, k) => isRawId(v, k) || SPANISH_LEAK.test(String(v || "")) || _MOJI_LEAD.test(String(v || ""));
    const badIn = Object.keys(enInLabels).filter(k => enBad(enInLabels[k], k));
    const badOut = Object.keys(enOutLabels).filter(k => enBad(enOutLabels[k], k));
    const nameBad = SPANISH_LEAK.test(enName) || _MOJI_LEAD.test(enName);
    const descBad = !enDesc || /Free online calculator with formula, examples and step-by-step guide/i.test(enDesc) || SPANISH_LEAK.test(enDesc) || _MOJI_LEAD.test(enDesc);
    if (badIn.length || badOut.length || nameBad || descBad) {
      try {
        const unitOf = id => { const i = inputsArr.find(x => x.id === id) || outputsArr.find(x => x.id === id); return i && i.unit ? " (unit: " + i.unit + ")" : ""; };
        const ep = `You are naming the UI fields of an online calculator, in ENGLISH.

Calculator: "${enName}"
Formula (for context): ${String(formulaStr).slice(0, 400) || "n/a"}

Give a short, natural ENGLISH label for each field id below. The ids are often Spanish — translate their MEANING, never keep the raw id, never keep Spanish words. Keep unit symbols out of the label.
INPUT ids: ${JSON.stringify(badIn.length ? badIn : Object.keys(enInLabels))}${badIn.map(id => "\n  - " + id + unitOf(id)).join("")}
OUTPUT ids: ${JSON.stringify(badOut.length ? badOut : Object.keys(enOutLabels))}${badOut.map(id => "\n  - " + id + unitOf(id)).join("")}

Also give: "name" = the calculator's English name, and "desc" = ONE specific sentence (max 20 words) describing what it calculates (NOT a generic template).

Return ONLY JSON: {"inputs_labels":{"<id>":"<English label>"},"outputs_labels":{"<id>":"<English label>"},"name":"...","desc":"..."}`;
        const g = await ai(ep, 1200);
        const patch = {};
        if (g.inputs_labels && typeof g.inputs_labels === "object") {
          const m = {}; for (const k of badIn) { const v = g.inputs_labels[k]; if (v && !enBad(v, k)) m[k] = String(v).trim(); }
          if (Object.keys(m).length) { enInLabels = Object.assign({}, enInLabels, m); patch.inputs_labels = enInLabels; enFixed += Object.keys(m).length; }
        }
        if (g.outputs_labels && typeof g.outputs_labels === "object") {
          const m = {}; for (const k of badOut) { const v = g.outputs_labels[k]; if (v && !enBad(v, k)) m[k] = String(v).trim(); }
          if (Object.keys(m).length) { enOutLabels = Object.assign({}, enOutLabels, m); patch.outputs_labels = enOutLabels; enFixed += Object.keys(m).length; }
        }
        if (nameBad && g.name && !SPANISH_LEAK.test(g.name)) { enName = String(g.name).trim(); patch.name = enName; enFixed++; }
        if (descBad && g.desc && !SPANISH_LEAK.test(g.desc)) { enDesc = String(g.desc).trim(); patch.desc = enDesc; enFixed++; }
        if (Object.keys(patch).length) langsPatch.en = Object.assign(langsPatch.en || {}, patch);
      } catch (e) { /* EN repair is best-effort */ }
    }

    const needUI = LANGS6.filter(l => l !== "en" && uiBrokenFor(l));
    for (const l of needUI) {
      try {
        const extra = (enExampleLabel || Object.keys(enRangeHints).length)
          ? `,"example_label":${JSON.stringify(enExampleLabel)},"range_hints":${JSON.stringify(enRangeHints)}` : "";
        const up = `Translate these calculator UI strings for "${enName}" into ${NAMES[l]}. Keep the JSON keys and array order identical; translate only the human-readable values into natural ${NAMES[l]} with no English or other language left in. Keep unit symbols (m², kg, mm) and any numbers as-is. Return ONLY JSON with this exact shape:
{"name":${JSON.stringify(enName)},"desc":${JSON.stringify(enDesc || enName)},"inputs_labels":${JSON.stringify(enInLabels)},"outputs_labels":${JSON.stringify(enOutLabels)},"preset_labels":${JSON.stringify(presetLabelsEN)}${extra}}`;
        const g = await ai(up, 1500);
        const patch = langsPatch[l] || {};
        if (g.name && !badVal(g.name, l, enName)) patch.name = String(g.name).trim();
        if (g.desc && !badVal(g.desc, l, enDesc)) patch.desc = String(g.desc).trim();
        // Merge label maps but drop any value the AI left bad (untranslated/leaked).
        const cleanMap = (m, en) => { const o = {}; for (const k of Object.keys(m || {})) { const v = String(m[k]); if (!badVal(v, l, en[k])) o[k] = v; } return o; };
        if (g.inputs_labels && typeof g.inputs_labels === "object" && !Array.isArray(g.inputs_labels)) { const cm = cleanMap(g.inputs_labels, enInLabels); if (Object.keys(cm).length) patch.inputs_labels = cm; }
        if (g.outputs_labels && typeof g.outputs_labels === "object" && !Array.isArray(g.outputs_labels)) { const cm = cleanMap(g.outputs_labels, enOutLabels); if (Object.keys(cm).length) patch.outputs_labels = cm; }
        if (Array.isArray(g.preset_labels) && g.preset_labels.length) patch.preset_labels = g.preset_labels.map(x => String(x));
        if (g.example_label && !badVal(g.example_label, l, enExampleLabel)) patch.example_label = String(g.example_label).trim();
        if (g.range_hints && typeof g.range_hints === "object" && !Array.isArray(g.range_hints)) patch.range_hints = g.range_hints;
        if (Object.keys(patch).length) { langsPatch[l] = patch; uiWrote++; }
      } catch (e) { /* skip a lang that fails */ }
    }

    if (Object.keys(langsPatch).length) await docRef.set({ langs: langsPatch }, { merge: true });

    // ── FIX 3: long-form article + FAQ (EN source reused if clean, translate broken langs) ──
    let contentLangs = 0;
    const needLC = LANGS6.filter(l => brk.lc[l]);
    if (doContent && needLC.length) {
      try {
        const inputsList = (doc0.inputs || []).map(i => i.id + (i.unit ? " (" + i.unit + ")" : "")).join(", ");
        const outputsList = outputs.map(o => o.id + (o.unit ? " (" + o.unit + ")" : "")).join(", ");
        const formula = doc0.formula || "";
        const cPatch = {};
        let enLong = (langs0.en && langs0.en.long_content) || "";
        let enFaq = (langs0.en && Array.isArray(langs0.en.faq)) ? langs0.en.faq : [];
        const enClean = !brk.lc.en && strip(enLong).length >= 400;
        if (!enClean) {
          const genPrompt = `You are writing high-quality calculator content in English for a calculator website.

Calculator: "${name}"
Formula: ${formula || "n/a"}
Inputs: ${inputsList || "n/a"}
Outputs: ${outputsList || "n/a"}

Write a complete long-form article in English with:
- A TL;DR first sentence directly answering how to use this calculator
- 6 H2 sections: "How to Use", "Formula Explained", "Practical Examples" (3 real examples with numbers), "When to Use This Calculator", "Tips and Common Mistakes", "Understanding the Results"
- Each section at least 2 full paragraphs
- Total 800-1200 words
- Use single quotes for any HTML attributes
${verified.length ? `\nIMPORTANT — in "Practical Examples" use ONLY these VERIFIED calculations (computed by the real formula; do not invent other numbers):\n${verified.join("\n")}\n` : ""}
Also write 4 FAQ items in English that users would realistically search for. Double-check every number you write is arithmetically correct.

Return ONLY valid JSON: {"long_content":"<h2>...</h2><p>...</p>","faq":[{"q":"...","a":"..."},{"q":"...","a":"..."},{"q":"...","a":"..."},{"q":"...","a":"..."}]}`;
          const enC = await ai(genPrompt, 6000);
          enLong = (enC.long_content || "").trim();
          enFaq = Array.isArray(enC.faq) ? enC.faq : [];
          if (enLong && brk.lc.en) { cPatch.en = { long_content: enLong, faq: enFaq }; contentLangs++; }
        }
        if (enLong) {
          for (const l of needLC.filter(x => x !== "en")) {
            try {
              const tPrompt = `Translate this calculator article and its FAQ from English into ${NAMES[l]}. Keep the HTML structure and tags identical — translate only the human-readable text. Use single quotes for HTML attributes. Natural, native ${NAMES[l]} with no English left over.

ARTICLE_HTML: ${enLong}

FAQ_JSON: ${JSON.stringify(enFaq)}

Return ONLY valid JSON: {"long_content":"<h2>...</h2>...","faq":[{"q":"...","a":"..."}]}`;
              const t = await ai(tPrompt, 6000);
              if (t.long_content) { cPatch[l] = { long_content: String(t.long_content).trim(), faq: Array.isArray(t.faq) ? t.faq : enFaq }; contentLangs++; }
            } catch (e) { /* skip a language that fails */ }
          }
        }
        if (Object.keys(cPatch).length) await docRef.set({ langs: cPatch }, { merge: true });
      } catch (e) { console.warn("aiFixCalcHttp content regen skipped:", e.message); }
    }

    const changed = rcWrote + metaWrote + uiWrote + enFixed + contentLangs + (engineReport.relatedFilled || 0) + (engineReport.presetsFixed || 0);
    // Republish only when something actually changed and the calc is published.
    let deployed = false;
    if (changed) {
      const snap1 = await docRef.get();
      if (snap1.exists && snap1.data().status === "published") {
        const files = await _buildCalcFiles(baseSlug, snap1.data());
        if (Object.keys(files).length) { const r = await _deployPagesToHosting(files, `[AIFix] ${baseSlug}`); deployed = !r.error; }
      }
    }
    // Record this run in Firestore so the dashboard Page-1 Tracker can show it
    // (keyed by base slug; stores the per-language translated slugs so the tracker
    // can badge every language row of this calc).
    if (changed) {
      try {
        await db.collection("ai_fixes").doc(baseSlug).set({
          base: baseSlug, name,
          at: admin.firestore.FieldValue.serverTimestamp(),
          mode: targeted ? "targeted" : "full",
          rc: rcWrote, meta: metaWrote, ui: uiWrote, content: contentLangs, deployed,
          langs: (entry && entry.slugs) ? entry.slugs : {},
        }, { merge: true });
      } catch (e) { /* logging is best-effort */ }
    }

    return res.status(200).json({
      ok: true, slug: baseSlug, mode: targeted ? "targeted" : "full",
      changed: changed > 0, alreadyClean: targeted && changed === 0,
      rcWrote, metaWrote, uiWrote, enFixed, contentLangs, deployed, engine: engineReport,
    });
  } catch (e) {
    console.error("aiFixCalcHttp error:", e);
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
exports.retranslateLongContent = functions.runWith({ timeoutSeconds: 300, memory: '256MB' }).https.onRequest(async (req, res) => {
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
      const effectiveModel = (provider === "deepseek" && (provCfg.model || "").includes("reasoner")) ? "deepseek-chat" : (provCfg.model || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini"));
      const r = await fetch(`${baseUrl}/chat/completions`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
        body: JSON.stringify({ model: effectiveModel, messages: [{ role: "user", content: prompt }], max_tokens: 8000 }),
      });
      if (!r.ok) throw new Error("AI error: " + await r.text());
      const d = await r.json();
      text = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
    }

    const jsonMatch = text && text.match(/\{[\s\S]*\}/);
    if (!jsonMatch) return res.status(500).json({ error: "Could not parse AI response", preview: (text||"").slice(0,200) });
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
      // deepseek-reasoner returns reasoning chain-of-thought, not usable output — force chat model
      const effectiveModel = (provider === "deepseek" && (model || "").includes("reasoner")) ? "deepseek-chat" : (model || defaultModel);
      const msgs = system ? [{ role: "system", content: system }, ...messages] : messages;
      const r = await fetch(`${baseUrl}/chat/completions`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
        body: JSON.stringify({ model: effectiveModel, messages: msgs, max_tokens: maxTokens }),
      });
      if (!r.ok) throw new Error(`${provider} error: ` + await r.text());
      const d = await r.json();
      const msg = d.choices && d.choices[0] && d.choices[0].message;
      responseText = msg && msg.content;

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

    // 2. Generate HTML for all available languages (via the shared builder,
    // which restores static calcs' inputs/formula so the calculator works).
    const newFiles = await _buildCalcFiles(slug, data);

    if (Object.keys(newFiles).length === 0) {
      return res.status(400).json({ error: "No language content available to publish" });
    }

    // Deploy via the shared chunked helper (handles the 15k-file populateFiles
    // limit + full-manifest cloning so the rest of the site is preserved).
    const result = await _deployPagesToHosting(newFiles, `Publish: ${slug}`);
    if (result.error) throw new Error(result.error);

    console.log("publishCalcToHosting success:", slug, result.pagesUpdated);
    return res.status(200).json({ success: true, pagesUpdated: result.pagesUpdated, versionName: result.versionName });

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
    const slugIdx = _getSlugIndex();
    for (const calc of cmsCalcs) {
      const updated = calc.updated_at ? new Date(calc.updated_at.seconds * 1000).toISOString().slice(0, 10) : now;
      const smap = slugIdx[calc.slug] || slugIdx[String(calc.id)] || null;
      for (const lang of LANGS) {
        if (!calc.langs?.[lang]?.name) continue;
        const lSlug = (smap && smap[lang]) || calc.langs?.[lang]?.slug || calc.slug;
        if (!lSlug) continue;
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
  .pubsub.schedule("0 10 * * *").timeZone("UTC").onRun(async () => {
  await _runAutoPilot();
});

/**
 * completeCalcHttp — completes ONE calc end-to-end: inputs/outputs/formula if
 * missing, English long-form article, input labels, FAQ, and full translations
 * (incl. translated articles) for every language. Optionally deploys to hosting.
 * POST { slug, deploy?: boolean }
 */
exports.completeCalcHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  const { slug, deploy } = req.body || {};
  if (!slug) return res.status(400).json({ error: "slug required" });

  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key configured. Go to Settings → AI Provider." });

    const doc = await db.collection("calc_cms").doc(slug).get();
    if (!doc.exists) return res.status(404).json({ error: "Calculator not found: " + slug });

    const results = { translations: 0, metaFixed: 0, longContentFixed: 0, longContentTranslated: 0, labelsFixed: 0, faqFixed: 0, faqTranslated: 0, linksAdded: 0, mechanicsFixed: 0 };
    const updated = await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, {}, {});

    let deployResult = null;
    if (deploy && (updated || req.body.forceDeploy)) {
      deployResult = await _autoDeployCalc(slug);
    }

    return res.status(200).json({ slug, updated, results, deploy: deployResult });
  } catch (e) {
    console.error("completeCalcHttp error:", e);
    return res.status(500).json({ error: e.message });
  }
});

const ENGLISH_LEAKAGE_WORDS = ["calculator", " the ", " and ", " of ", " for ", " to ", " with ", " a calculator"];

async function _autoPilotProcessDoc(doc, apiKey, provider, model, results, calcNameMap = {}, trafficBySlug = {}) {
  const data = doc.data();
  const langs = data.langs || {};
  let inputs = data.inputs || [];
  let outputs = data.outputs || [];
  if (!langs.en?.name) return false;
  let updated = false;
  const updatedLangs = { ...langs };
  const docUpdates = {};

  // 0. Generate missing calculator mechanics (inputs / outputs / formula).
  // NEVER for static imports — their real inputs/formula live in the static
  // calculator files; generating new ones here could replace a working
  // calculator with an AI-invented one.
  const isStaticImport = data.type === "static" || data.source === "static" || data.source === "static_sync";
  if (!isStaticImport && (inputs.length === 0 || outputs.length === 0 || !data.formula || data.formula.length < 10)) {
    try {
      const specPrompt = `Create the interactive specification for a web calculator called "${langs.en.name}". ${langs.en.desc ? "Description: " + langs.en.desc : ""}

Return ONLY valid JSON:
{
  "inputs": [{"id":"field_id","label":"Human Label","type":"number","unit":"m","placeholder":"e.g. 5.0","min":0.1,"max":1000,"step":0.1,"default":5}],
  "outputs": [{"id":"result_id","label":"Human Label","unit":"m²","highlight":true}],
  "formula": "JavaScript function body: const a=parseFloat(inputs.field_id)||0; return { result_id: a*2 };"
}

Rules:
- Use 2-4 inputs and 1-3 outputs
- Formula MUST use inputs.field_id and return an object with output IDs
- All math must be client-side JavaScript`;
      const specText = await _callAIRaw(apiKey, provider, model, specPrompt, 2000);
      const specM = specText && specText.match(/\{[\s\S]*\}/);
      if (specM) {
        const spec = JSON.parse(specM[0]);
        if (Array.isArray(spec.inputs) && spec.inputs.length && Array.isArray(spec.outputs) && spec.outputs.length && spec.formula) {
          try { new Function("inputs", '"use strict";' + spec.formula); } catch(e) { throw new Error("generated formula invalid: " + e.message); }
          if (inputs.length === 0) { docUpdates.inputs = spec.inputs; inputs = spec.inputs; }
          if (outputs.length === 0) { docUpdates.outputs = spec.outputs; outputs = spec.outputs; }
          if (!data.formula || data.formula.length < 10) docUpdates.formula = spec.formula;
          updated = true; results.mechanicsFixed = (results.mechanicsFixed || 0) + 1;
        }
      }
    } catch(e) { console.warn("mechanics gen failed:", doc.id, e.message); }
  }

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
      const inputFields = inputs.map(i => `${i.id}${i.unit ? ' (' + i.unit + ')' : ''}`).join(', ') || 'see calculator inputs';
      const outputFields = outputs.map(o => `${o.id}${o.unit ? ' (' + o.unit + ')' : ''}`).join(', ') || 'see calculator outputs';
      const formula = docUpdates.formula || data.formula || langs.en.formula_display || '';
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

  // 6. Translate FAQ to langs that have a translation but no FAQ yet (concurrent)
  const enFaqNow = updatedLangs.en?.faq;
  if (enFaqNow && enFaqNow.length >= 3) {
    const langNames = { es:"Spanish", fr:"French", de:"German", it:"Italian", pt:"Portuguese" };
    const faqNeed = LANGS.filter(lang => lang !== "en" && updatedLangs[lang]?.name &&
      !(updatedLangs[lang].faq && updatedLangs[lang].faq.length >= 3));
    const faqRes = await Promise.all(faqNeed.map(async lang => {
      try {
        const raw = await _callAIRaw(apiKey, provider, model,
          `Translate these FAQ items to ${langNames[lang]}. Return only a JSON array with the same structure: ${JSON.stringify(enFaqNow)}`, 800);
        const m = raw && raw.replace(/<think>[\s\S]*?<\/think>/g,"").match(/\[[\s\S]*\]/);
        if (m) { const f = JSON.parse(m[0]); if (Array.isArray(f) && f.length >= 3) return { lang, faq: f }; }
      } catch(e) { console.warn("FAQ translate failed:", doc.id, lang, e.message); }
      return { lang, faq: null };
    }));
    for (const { lang, faq } of faqRes) {
      if (faq) { updatedLangs[lang] = { ...updatedLangs[lang], faq }; updated = true; results.faqTranslated = (results.faqTranslated || 0) + 1; }
    }
  }

  // 6b. Translate the long-form article to every language that needs one.
  // Run all languages CONCURRENTLY (was sequential — 5×~35s each = the single
  // biggest per-calc time sink, pushing batches past the 540s function limit).
  const enLongNow = updatedLangs.en?.long_content;
  if (enLongNow && enLongNow.length >= 600) {
    const needLangs = LANGS.filter(lang => lang !== "en" && updatedLangs[lang]?.name &&
      !((updatedLangs[lang].long_content || "").length >= 600));
    const translated = await Promise.all(needLangs.map(async lang => {
      try {
        const t = await _translateLongRaw(apiKey, provider, model, enLongNow, updatedLangs[lang].faq || updatedLangs.en?.faq || [], lang);
        return { lang, t };
      } catch(e) { console.warn("long_content translate failed:", doc.id, lang, e.message); return { lang, t: null }; }
    }));
    for (const { lang, t } of translated) {
      if (!t) continue;
      updatedLangs[lang] = { ...updatedLangs[lang], long_content: t.long_content };
      if (t.faq.length >= 3 && !(updatedLangs[lang].faq || []).length) {
        updatedLangs[lang] = { ...updatedLangs[lang], faq: t.faq };
      }
      updated = true; results.longContentTranslated = (results.longContentTranslated || 0) + 1;
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
    await doc.ref.update({ ...docUpdates, langs: updatedLangs, updated_at: admin.firestore.FieldValue.serverTimestamp() });
  }
  return updated;
}

/**
 * completeAllCalcsHttp — resumable server-side "Complete all calculators".
 * Each call processes a small batch of published calcs (generating articles,
 * FAQ, labels, translations) and deploys the ones it changed, then returns a
 * cursor. The dashboard calls it in a loop until done=true — so completion
 * runs server-side and survives the browser tab closing (progress persists in
 * admin_prefs/complete_all_state).
 * POST { reset?: boolean, batch?: number }
 */
/**
 * deployAllCalcsHttp — resumable, ATOMIC deploy of every published calc that has
 * content. Each call builds ~25 calcs' pages and deploys them in ONE release
 * (no per-calc race). Cursor persists in admin_prefs/deploy_all_state. Use this
 * to push already-generated content live correctly.
 * POST { reset?: boolean, batch?: number }
 */
exports.deployAllCalcsHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const stateRef = db.collection("admin_prefs").doc("deploy_all_state");
    if (req.body && req.body.reset) await stateRef.set({ cursor_doc_id: null, deployed: 0 });
    const stateDoc = await stateRef.get();
    const state = stateDoc.exists ? stateDoc.data() : {};
    const BATCH = Math.min(Math.max(parseInt((req.body || {}).batch) || 25, 5), 40);

    let query = db.collection("calc_cms").where("status", "==", "published").orderBy("__name__").limit(BATCH);
    if (state.cursor_doc_id) {
      const c = await db.collection("calc_cms").doc(state.cursor_doc_id).get();
      if (c.exists) query = query.startAfter(c);
    }
    const snap = await query.get();

    const allFiles = {};
    let calcsWithContent = 0;
    let lastId = null;
    for (const doc of snap.docs) {
      lastId = doc.id;
      const data = doc.data();
      const en = (data.langs && data.langs.en) || {};
      if (!en.long_content || en.long_content.length < 300) continue; // skip still-thin
      const f = await _buildCalcFiles(doc.id, data);
      Object.assign(allFiles, f);
      calcsWithContent++;
    }

    let deployRes = { deployed: false };
    if (Object.keys(allFiles).length > 0) {
      deployRes = await _deployPagesToHosting(allFiles, `[DeployAll] ${calcsWithContent} calcs`);
    }

    const done = snap.size < BATCH;
    await stateRef.set({
      cursor_doc_id: done ? null : lastId,
      deployed: (state.deployed || 0) + (deployRes.deployed ? calcsWithContent : 0),
      last_run: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });

    return res.status(200).json({
      done, scanned: snap.size, deployed_calcs: deployRes.deployed ? calcsWithContent : 0,
      total_files: Object.keys(allFiles).length, error: deployRes.error || null,
    });
  } catch (e) {
    console.error("deployAllCalcsHttp error:", e);
    return res.status(500).json({ error: e.message });
  }
});

exports.completeAllCalcsHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key configured (Settings → AI Provider)." });

    const stateRef = db.collection("admin_prefs").doc("complete_all_state");
    if (req.body && req.body.reset) {
      await stateRef.set({ cursor_doc_id: null, processed: 0, updated: 0, deployed: 0, started_at: admin.firestore.FieldValue.serverTimestamp() });
    }
    const stateDoc = await stateRef.get();
    const state = stateDoc.exists ? stateDoc.data() : {};
    let cursorId = state.cursor_doc_id || null;

    // Total published (for progress %). Cheap: aggregate count.
    let total = state.total || 0;
    if (!total) {
      try {
        const agg = await db.collection("calc_cms").where("status", "==", "published").count().get();
        total = agg.data().count;
      } catch (e) { total = 0; }
    }

    const BATCH = Math.min(Math.max(parseInt((req.body || {}).batch) || 10, 1), 20);
    const calcNameMap = {};
    const { skipComplete } = req.body || {};
    const skipIfComplete = skipComplete !== false; // default: skip already-complete calcs

    let lastDoc = null;
    if (cursorId) {
      const c = await db.collection("calc_cms").doc(cursorId).get();
      if (c.exists) lastDoc = c;
    }

    let query = db.collection("calc_cms").where("status", "==", "published").orderBy("__name__").limit(skipIfComplete ? BATCH * 3 : BATCH);
    if (lastDoc) query = query.startAfter(lastDoc);
    const snap = await query.get();

    const results = { translations: 0, metaFixed: 0, longContentFixed: 0, longContentTranslated: 0, labelsFixed: 0, faqFixed: 0, faqTranslated: 0, linksAdded: 0, mechanicsFixed: 0 };
    let processedNow = 0, updatedNow = 0, deployedNow = 0;
    const touched = [];

    for (const doc of snap.docs) {
      processedNow++;

      // Skip already-complete calcs
      if (skipIfComplete) {
        const data = doc.data();
        const langs = data.langs || {};
        const en = langs.en || {};
        const hasContent = en.long_content && en.long_content.length > 500;
        const hasFaq = en.faq && en.faq.length >= 2;
        const hasSteps = en.steps && en.steps.filter(Boolean).length >= 2;
        const hasSeoTitle = en.seo_title && en.seo_title.length >= 15;
        const hasSeoDesc = en.seo_description && en.seo_description.length >= 30;
        // Also require every present language to have its TRANSLATED article,
        // otherwise calcs with a full EN article but missing es/fr/de/it/pt
        // translations were wrongly treated as "done" and skipped forever.
        const langsComplete = LANGS.every(l => l === "en" || !langs[l]?.name || (langs[l].long_content || "").length >= 600);
        const isComplete = hasContent && hasFaq && hasSteps && hasSeoTitle && hasSeoDesc && langsComplete;
        if (isComplete) {
          lastDoc = doc;
          if (updatedNow === 0 && processedNow === snap.size) cursorId = null; // all skipped, done
          continue;
        }
      }

      try {
        const changed = await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, calcNameMap, {});
        if (changed) { updatedNow++; touched.push(doc.id); }
      } catch (e) { console.warn("[CompleteAll] process failed:", doc.id, e.message); }
      lastDoc = doc;
    }

    // Deploy the changed calcs in ONE atomic release — but ONLY when explicitly
    // requested (deploy:true). Cloning the full 22k-file manifest every batch is
    // the slow part; for a full run it's far faster to generate all content
    // first (content persists in Firestore) and push it live once at the end via
    // deployAllCalcsHttp. So generation is decoupled from deployment by default.
    if (req.body && req.body.deploy && touched.length > 0) {
      try {
        const allFiles = {};
        for (const slug of touched) {
          const f = await _buildCalcFiles(slug);
          Object.assign(allFiles, f);
        }
        if (Object.keys(allFiles).length > 0) {
          const dep = await _deployPagesToHosting(allFiles, `[CompleteAll] ${touched.length} calcs`);
          if (dep.deployed) deployedNow = touched.length;
          else console.warn("[CompleteAll] batch deploy failed:", dep.error);
        }
      } catch (e) { console.warn("[CompleteAll] batch deploy error:", e.message); }
    }

    const done = snap.size < BATCH;
    const newProcessed = (state.processed || 0) + processedNow;
    await stateRef.set({
      cursor_doc_id: done ? null : (lastDoc ? lastDoc.id : null),
      processed: done ? 0 : newProcessed,
      updated: (state.updated || 0) + updatedNow,
      deployed: (state.deployed || 0) + deployedNow,
      total,
      last_run: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });

    if (done) {
      // Ping Google to recrawl once the whole pass finishes
      try {
        const fetch = require("node-fetch");
        await fetch("https://www.google.com/ping?sitemap=https://calcto.work/sitemap.xml").catch(() => {});
      } catch (e) {}
    }

    return res.status(200).json({
      done,
      processed_this_call: processedNow,
      updated_this_call: updatedNow,
      deployed_this_call: deployedNow,
      total_processed: done ? newProcessed : newProcessed,
      total,
      touched,
      results,
    });
  } catch (e) {
    console.error("completeAllCalcsHttp error:", e);
    return res.status(500).json({ error: e.message });
  }
});

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

  const results = { translations: 0, metaFixed: 0, longContentFixed: 0, longContentTranslated: 0, labelsFixed: 0, faqFixed: 0, faqTranslated: 0, linksAdded: 0, mechanicsFixed: 0 };
  const processedSlugs = new Set();
  const updatedSlugs = [];
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
      if (await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, calcNameMap, trafficBySlug)) updatedSlugs.push(doc.id);
      processedSlugs.add(doc.id);
    }
  }

  const rankedSlugs = Object.entries(trafficBySlug).sort((a,b)=>b[1]-a[1]).map(([s])=>s).slice(0,60);

  for (let i = 0; i < rankedSlugs.length && batchNum < 3; i += 20) {
    const slugBatch = rankedSlugs.slice(i, i+20);
    const docs = await Promise.all(slugBatch.map(s => db.collection("calc_cms").doc(s).get()));
    for (const doc of docs) {
      if (!doc.exists || doc.data().status !== "published" || processedSlugs.has(doc.id)) continue;
      if (await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, calcNameMap, trafficBySlug)) updatedSlugs.push(doc.id);
      processedSlugs.add(doc.id);
    }
    batchNum++;
  }

  // Phase 2: Fill remaining budget with unprioritized calcs via pagination.
  // The cursor persists across runs (admin_prefs/autopilot_state) so every run
  // resumes where the previous one stopped — over successive daily runs the
  // whole catalog gets covered instead of re-scanning the same first 100 docs.
  const stateRef = db.collection("admin_prefs").doc("autopilot_state");
  const stateDoc = await stateRef.get();
  let cursorId = stateDoc.exists ? stateDoc.data().cursor_doc_id : null;
  let lastDoc = null;
  if (cursorId) {
    const c = await db.collection("calc_cms").doc(cursorId).get();
    if (c.exists) lastDoc = c;
  }
  let exhausted = false;
  while (batchNum < MAX_BATCHES) {
    let query = db.collection("calc_cms").where("status","==","published").limit(20);
    if (lastDoc) query = query.startAfter(lastDoc);
    const snap = await query.get();
    if (snap.empty) { exhausted = true; break; }
    lastDoc = snap.docs[snap.docs.length - 1];
    batchNum++;
    for (const doc of snap.docs) {
      if (processedSlugs.has(doc.id)) continue;
      if (await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, calcNameMap, trafficBySlug)) updatedSlugs.push(doc.id);
      processedSlugs.add(doc.id);
    }
    if (snap.size < 20) { exhausted = true; break; }
  }
  await stateRef.set({
    cursor_doc_id: exhausted ? null : (lastDoc ? lastDoc.id : null),
    last_run: admin.firestore.FieldValue.serverTimestamp(),
    last_results: results,
  }, { merge: true });

  // Phase 3: Refresh thin static pages (not in CMS). cmsSlugs must include every
  // slug a CMS calc is reachable at — primary AND all translated slugs — or a
  // CMS calc's canonical page (e.g. /en/acceleration-calculator/) would leak into
  // the legacy regex-patcher and be edited outside the buildPage pipeline.
  const cmsSlugs = new Set();
  const _slugIdx = _getSlugIndex();
  for (const d of nameSnap.docs) {
    cmsSlugs.add(d.id);
    const smap = _slugIdx[d.id] || _slugIdx[String((d.data() || {}).id)] || null;
    if (smap) for (const l of LANGS) if (smap[l]) cmsSlugs.add(smap[l]);
  }
  await _refreshStaticPages(apiKey, provider, provCfg.model, trafficBySlug, cmsSlugs, results);

  // Phase 4: Deploy updated CMS calcs to hosting so the fixes actually go live
  results.deployed = 0;
  for (const slug of updatedSlugs.slice(0, 12)) {
    try {
      const dep = await _autoDeployCalc(slug);
      if (dep.deployed) results.deployed++;
    } catch(e) { console.warn("[AutoPilot] Deploy failed:", slug, e.message); }
  }
  results.updated_slugs = updatedSlugs;

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

  // Publish patches via the shared chunked deploy helper (handles the 15k-file
  // populateFiles limit and clones the full manifest so nothing is dropped).
  try {
    const newFiles = {};
    for (const [path, html] of Object.entries(patchedFiles)) {
      const gzipped = await gzip(Buffer.from(html, "utf8"));
      const hash = crypto.createHash("sha256").update(gzipped).digest("hex");
      newFiles[path] = { gzipped, hash };
    }
    const result = await _deployPagesToHosting(newFiles, "[Agent] Static page refresh");
    if (result.error) throw new Error(result.error);
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
  "formula": "const a = parseFloat(inputs.value)||0; return { result: a * 2 };",
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

Important rules for "formula":
- formula is a JavaScript function BODY (not a function declaration) — it will be wrapped as: function(inputs){ YOUR_FORMULA }
- Read inputs with: const x = parseFloat(inputs.field_id)||0;
- Return an object with output field IDs as keys: return { output_id: value };
- Do NOT write "function calculate(...){...}" — just the body
- long_content must be at least 300 words of helpful HTML content.`;
  let text = await _callAIRaw(apiKey, provider, model,
    `${systemPrompt}\n\nCalculator to build: ${prompt}`, 4000);
  if (!text) return null;
  text = text.replace(/<think>[\s\S]*?<\/think>/g, "").trim();
  const m = text.match(/\{[\s\S]*\}/s);
  if (!m) return null;
  try {
    const parsed = JSON.parse(m[0]);
    // Normalize formula_js → formula (extract body if it's a full function declaration)
    if (!parsed.formula && parsed.formula_js) {
      const fjs = parsed.formula_js;
      const bodyMatch = fjs.match(/function\s*\w*\s*\([^)]*\)\s*\{([\s\S]*)\}/);
      parsed.formula = bodyMatch ? bodyMatch[1].trim() : fjs;
      delete parsed.formula_js;
    }
    return parsed;
  } catch(e) {
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
  // long_content is intentionally excluded — it is translated separately by
  // _translateLongRaw with a larger token budget. Including it here blew past
  // the 4096-token response limit, truncating the JSON so parsing failed and
  // the whole language was silently skipped.
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
    faq: enContent.faq || [],
  };
  const prompt = `Translate the following calculator content from English to ${langName}. Preserve all HTML tags exactly. Keep {placeholder} tokens unchanged. Return ONLY valid JSON with the same structure as input.

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

async function _translateLongRaw(apiKey, provider, model, enLongContent, enFaq, targetLang) {
  const langNames = { es:"Spanish", fr:"French", de:"German", it:"Italian", pt:"Portuguese" };
  const langName = langNames[targetLang] || targetLang;
  const prompt = `Translate the following HTML article and FAQ from English to ${langName}.

Rules:
- Translate all text content to natural, fluent ${langName} — not word-for-word
- Keep ALL HTML tags intact: <h2>, <p>, <strong>, <ul>, <li>, etc.
- Do NOT translate proper nouns, brand names, URLs, or numeric values
- Keep units (m, kg, ft, lb) unchanged
- Use single quotes for any HTML attributes to keep JSON valid

Return ONLY valid JSON:
{"long_content":"...(translated HTML)...","faq":[{"q":"...","a":"..."}]}

English long_content:
${enLongContent}

English FAQ:
${JSON.stringify(enFaq || [])}`;
  const text = await _callAIRaw(apiKey, provider, model, prompt, 8000);
  if (!text) return null;
  const m = text.match(/\{[\s\S]*\}/s);
  if (!m) return null;
  try {
    const parsed = JSON.parse(m[0]);
    if (!parsed.long_content || parsed.long_content.length < 200) return null;
    return { long_content: parsed.long_content, faq: Array.isArray(parsed.faq) ? parsed.faq : [] };
  } catch(e) { return null; }
}

// ═══════════════════════════════════════════════════════
//  GROWTH ENGINE v2 — Auto-Optimize, Competitor Intel, Bulk Factory
// ═══════════════════════════════════════════════════════

/**
 * Auto-optimize calculator meta titles using AI.
 * Takes pages ranking in positions 4-20 and generates better titles to boost CTR.
 */
exports.autoOptimizeCalcsHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key configured" });

    const { limit, minPosition, maxPosition, dryRun } = req.body || {};
    const maxPos = maxPosition || 20;
    const minPos = minPosition || 3;
    const maxCalc = limit || 10;

    // Get pages with impressions in target position range
    const cutoff = new Date(Date.now() - 30 * 86400000).toISOString().slice(0, 10);
    const siteUrl = functions.config().gsc?.site_url || "sc-domain:calcto.work";
    const pageSnap = await db.collection("gsc_page_stats")
      .where("site_url", "==", siteUrl)
      .where("date", ">=", cutoff)
      .orderBy("date", "desc")
      .limit(1000)
      .get();

    // Find pages ranking near page 1 with impressions but room for CTR improvement
    const candidates = {};
    pageSnap.forEach(doc => {
      const d = doc.data();
      const page = d.page || "";
      const slug = page.split("/").filter(Boolean).pop() || page;
      if (!slug || slug.length < 3) return;
      if (!candidates[slug]) candidates[slug] = { slug, page, imp: 0, clicks: 0, posSum: 0, count: 0 };
      candidates[slug].imp += d.total_impressions || 0;
      candidates[slug].clicks += d.total_clicks || 0;
      candidates[slug].posSum += d.avg_position || 0;
      candidates[slug].count++;
    });

    const sorted = Object.values(candidates)
      .filter(c => {
        const avgPos = c.count > 0 ? c.posSum / c.count : 100;
        return avgPos >= minPos && avgPos <= maxPos && c.imp >= 10;
      })
      .sort((a, b) => b.imp - a.imp)
      .slice(0, maxCalc);

    if (sorted.length === 0) return res.status(200).json({ optimized: 0, message: "No candidates found in that position range." });

    const results = [];
    for (const c of sorted) {
      try {
        const avgPos = (c.posSum / c.count).toFixed(1);
        const ctr = c.imp > 0 ? ((c.clicks / c.imp) * 100).toFixed(2) : "0";
        const prompt = `You are an SEO expert optimizing a calculator website's meta titles to improve CTR from Google search results.

CURRENT PAGE DATA:
- URL slug: ${c.slug}
- Impressions (last 30 days): ${c.imp}
- Clicks: ${c.clicks}
- Current CTR: ${ctr}%
- Average position: ${avgPos}

The page is a free online calculator. Create a compelling, click-worthy SEO title (max 55 chars) that will make people click instead of scrolling past. Include key numbers/benefits. Format MUST be: "Calculator Name – Benefit or Context".

Examples of good titles:
- "Concrete Slab Calculator – Exact Bags & Cost"
- "Solar Panel Calculator – Panels, kWp & Roof Area"  
- "BMI Calculator – Instant Body Mass Index Result"
- "Cylinder Volume Calculator – V = πr²h, Free & Fast"

Return ONLY a JSON object with this exact structure:
{"slug":"${c.slug}","seo_title":"your new title here","seo_description":"compelling meta description max 155 chars that makes people want to click"}`;

        const text = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 1000);
        if (!text) { results.push({ slug: c.slug, error: "AI call failed" }); continue; }

        const m = text.match(/\{[\s\S]*\}/);
        if (!m) { results.push({ slug: c.slug, error: "No JSON in response" }); continue; }

        const optimized = JSON.parse(m[0]);
        results.push({
          slug: c.slug,
          old_impressions: c.imp,
          old_clicks: c.clicks,
          old_position: avgPos,
          old_ctr: ctr + "%",
          new_title: optimized.seo_title,
          new_description: optimized.seo_description,
        });

        if (!dryRun) {
          // Save to Firestore for review/approval, not auto-apply
          await db.collection("seo_suggestions").add({
            type: "auto_optimize",
            slug: c.slug,
            seo_title: optimized.seo_title,
            seo_description: optimized.seo_description,
            old_impressions: c.imp,
            old_clicks: c.clicks,
            old_position: avgPos,
            status: "pending",
            created_at: admin.firestore.FieldValue.serverTimestamp(),
          });
        }
      } catch(e) { results.push({ slug: c.slug, error: e.message }); }
    }

    return res.status(200).json({
      optimized: results.length,
      dryRun: !!dryRun,
      candidates_found: sorted.length,
      results,
      tip: dryRun ? "Dry run — no changes saved. Set dryRun:false to save suggestions." : "Suggestions saved to SEO Suggestions. Review and apply from the Opportunities tab."
    });
  } catch(e) {
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Analyze a competitor calculator site — DEEP CRAWLER
 * Fetches homepage, follows category links, extracts tools from multiple pages.
 * Uses sitemap.xml when available. AI-powered extraction from each page.
 */
exports.analyzeCompetitorHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");

  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key configured" });

    const url = (req.query.url || req.body?.url || "").trim();
    if (!url) return res.status(400).json({ error: "Missing ?url= parameter" });

    const fetch = require("node-fetch");
    const baseOrigin = new URL(url).origin;
    const visited = new Set();
    const allHtml = []; // { url, html, title }
    const discoveredUrls = [];

    const ua = "CalcToWork-Crawler/1.0 (SEO research bot; no personal data collected)";

    // ══ STEP 1: Fetch the initial URL ══
    console.log("[Crawler] Fetching:", url);
    let mainHtml, mainTitle;
    try {
      const r = await fetch(url, { timeout: 30000, headers: { "User-Agent": ua } });
      mainHtml = await r.text();
      mainTitle = (mainHtml.match(/<title[^>]*>([^<]+)<\/title>/i) || [])[1] || url;
      visited.add(url);
      allHtml.push({ url, html: mainHtml, title: mainTitle });
    } catch(e) { return res.status(500).json({ error: "Failed to fetch: " + e.message }); }

    // ══ STEP 2: Discover sitemap ══
    console.log("[Crawler] Looking for sitemap...");
    let sitemapTools = [];
    try {
      const sitemapUrl = baseOrigin + "/sitemap.xml";
      const smR = await fetch(sitemapUrl, { timeout: 15000, headers: { "User-Agent": ua } });
      if (smR.ok) {
        const smText = await smR.text();
        // Extract URLs from sitemap
        const urlMatches = smText.match(/<loc>([^<]+)<\/loc>/gi) || [];
        const calcUrls = urlMatches
          .map(m => m.replace(/<\/?loc>/gi, ""))
          .filter(u => {
            const path = new URL(u).pathname;
            // Filter: likely calculator pages (not images, CSS, category pages)
            return path.split("/").filter(Boolean).length >= 1 &&
                   !path.match(/\.(png|jpg|css|js|xml|ico|svg|webp)/i) &&
                   !path.match(/\/(category|tag|author|page\/\d+|blog|about|contact|privacy|terms)/i);
          })
          .slice(0, 200);
        console.log(`[Crawler] Sitemap found ${calcUrls.length} potential tool URLs`);
        // Only fetch a sample from sitemap (too many if we fetch all)
        discoveredUrls.push(...calcUrls.slice(0, 30));
      }
    } catch(e) { console.warn("[Crawler] Sitemap check failed:", e.message); }

    // ══ STEP 3: Extract category/section links from homepage ══
    console.log("[Crawler] Extracting category links...");
    const linkMatches = mainHtml.match(/<a[^>]*href="([^"]*)"[^>]*>([^<]*)<\/a>/gi) || [];
    const categoryPatterns = ["/calculat", "/tool", "/construction", "/math", "/finance", "/health", "/physics",
      "/chemistry", "/everyday", "/statistics", "/converter", "/convert", "/food", "/sports", "/biology", "/ecology"];

    for (const m of linkMatches) {
      const hrefMatch = m.match(/href="([^"]*)"/i);
      const textMatch = m.match(/>([^<]*)</);
      if (!hrefMatch || !textMatch) continue;
      let href = hrefMatch[1];
      if (href.startsWith("/")) href = baseOrigin + href;
      if (!href.startsWith(baseOrigin)) continue;
      if (visited.has(href)) continue;
      const text = textMatch[1].replace(/<[^>]*>/g, "").trim();
      if (text.length < 3 || text.length > 60) continue;

      const path = new URL(href).pathname;
      const isCategory = categoryPatterns.some(p => path.toLowerCase().includes(p)) && 
                         path.split("/").filter(Boolean).length <= 2;
      if (isCategory && !visited.has(href)) {
        discoveredUrls.push(href);
      }
    }

    // ══ STEP 4: Crawl discovered pages (up to 10) ══
    const uniqueUrls = [...new Set(discoveredUrls)].filter(u => !visited.has(u)).slice(0, 10);
    console.log(`[Crawler] Fetching ${uniqueUrls.length} additional pages...`);

    for (const pageUrl of uniqueUrls) {
      if (visited.has(pageUrl)) continue;
      visited.add(pageUrl);
      try {
        const r = await fetch(pageUrl, { timeout: 15000, headers: { "User-Agent": ua } });
        if (!r.ok) continue;
        const html = await r.text();
        const title = (html.match(/<title[^>]*>([^<]+)<\/title>/i) || [])[1] || pageUrl;
        allHtml.push({ url: pageUrl, html: html.slice(0, 30000), title });
        console.log(`[Crawler] Fetched: ${title.slice(0,60)}`);
      } catch(e) { console.warn("[Crawler] Failed:", pageUrl, e.message); }
    }

    console.log(`[Crawler] Crawled ${allHtml.length} pages total`);

    // ══ STEP 5: AI extraction from ALL pages ══
    const allTools = [];
    const seenNames = new Set();

    for (const page of allHtml) {
      const prompt = `You are analyzing a competitor calculator website. Extract ALL calculator/converter/tool names from this HTML content.

Page: ${page.title} (${page.url})

For each tool, return: {"name": "Tool Name", "slug": "url-friendly-slug"}

RULES:
- Include EVERY calculator, converter, or computation tool
- Skip navigation, footer, social, blog, about links
- If the page is a category listing, extract ALL tools listed
- If the page is a single calculator, extract just that one
- Aim for accuracy: only include real calculator tools

Return ONLY JSON: {"tools":[{"name":"...","slug":"..."}]}

HTML:
${page.html.slice(0, 15000)}`;

      try {
        const text = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 3000);
        if (!text) continue;
        const m = text.match(/\{[\s\S]*\}/);
        if (!m) continue;
        const parsed = JSON.parse(m[0]);
        if (parsed.tools && Array.isArray(parsed.tools)) {
          for (const t of parsed.tools) {
            const nlow = t.name.toLowerCase();
            if (!seenNames.has(nlow) && t.name.length >= 4 && t.name.length <= 80) {
              seenNames.add(nlow);
              allTools.push({ name: t.name, slug: t.slug || nlow.replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"") });
            }
          }
        }
      } catch(e) { console.warn("[Crawler] AI extraction failed for", page.title, ":", e.message); }
    }

    // Fallback: regex scraper if AI found nothing
    if (allTools.length < 5) {
      console.log("[Crawler] AI found few tools, running regex fallback...");
      const linkRx = /<a[^>]*href="([^"]*)"[^>]*>([^<]*)<\/a>/gi;
      for (const page of allHtml) {
        let m;
        while ((m = linkRx.exec(page.html)) !== null) {
          const name = m[2].replace(/<[^>]*>/g, "").trim();
          if (name.length < 4 || name.length > 80 || seenNames.has(name.toLowerCase())) continue;
          if (m[1].includes("javascript") || m[1] === "#" || m[1] === "/") continue;
          seenNames.add(name.toLowerCase());
          allTools.push({ name, slug: name.toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"") });
        }
      }
    }

    // ══ STEP 6: Compare against our tools ══
    const ourNames = new Set();
    const ourSlugs = new Set();
    const [cmsSnap, staticSnap] = await Promise.all([
      db.collection("calc_cms").limit(500).get(),
      db.collection("calc_pipeline").limit(500).get(),
    ]);
    for (const snap of [cmsSnap, staticSnap]) {
      snap.forEach(d => {
        const data = d.data();
        ourNames.add((data.langs?.en?.name || data.name || "").toLowerCase());
        ourSlugs.add((data.slug || d.id || "").toLowerCase());
      });
    }

    const gaps = allTools.filter(t => {
      const nlow = t.name.toLowerCase();
      if (ourNames.has(nlow) || ourSlugs.has(t.slug.toLowerCase())) return false;
      if (["home","calculator","calculators","tools","about","contact","blog","privacy","terms"].includes(t.slug.toLowerCase())) return false;
      return true;
    }).slice(0, 50);

    // Save
    await db.collection("admin_prefs").doc("competitor_analysis").set({
      url, page_title: mainTitle, pages_crawled: allHtml.length,
      analyzed_at: admin.firestore.FieldValue.serverTimestamp(),
      tools_found: allTools.length, our_tools_count: ourNames.size, gaps_found: gaps.length,
      gaps,
    });

    return res.status(200).json({
      url, pageTitle: mainTitle, pages_crawled: allHtml.length,
      tools_found: allTools.length, our_tools: ourNames.size, gaps_found: gaps.length,
      gaps, tools_sample: allTools.slice(0, 20),
    });
  } catch(e) {
    console.error("[Crawler] Error:", e.message);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Auto-apply pending SEO suggestions (batch approve)
 */
exports.applySEOSuggestionsHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const { limit } = req.body || {};
    const maxApply = limit || 20;
    const snap = await db.collection("seo_suggestions")
      .where("status", "==", "pending")
      .where("type", "==", "auto_optimize")
      .orderBy("created_at", "desc")
      .limit(maxApply)
      .get();

    if (snap.empty) return res.status(200).json({ applied: 0, message: "No pending suggestions." });

    const batch = db.batch();
    let count = 0;
    const applied = [];

    snap.forEach(doc => {
      const s = doc.data();
      batch.update(doc.ref, { status: "applied", applied_at: admin.firestore.FieldValue.serverTimestamp() });
      applied.push({ slug: s.slug, new_title: s.seo_title });
      count++;
    });

    await batch.commit();

    // Also update the calc_cms records
    for (const s of applied) {
      try {
        const calcDoc = await db.collection("calc_cms").doc(s.slug).get();
        if (calcDoc.exists) {
          const data = calcDoc.data();
          if (!data.langs) data.langs = {};
          if (!data.langs.en) data.langs.en = {};
          data.langs.en.seo_title = s.new_title;
          await db.collection("calc_cms").doc(s.slug).set(data, { merge: true });
        }
      } catch(e) {}
    }

    return res.status(200).json({ applied: count, results: applied });
  } catch(e) {
    console.error("applySEOSuggestions error:", e.message);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Quick Calculator Generator — AI creates a complete calculator from just a name.
 * Generates formula, inputs, outputs, translates to all languages, saves to pipeline.
 */
exports.quickGenerateCalcHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const { name, category, publish } = req.body || {};
    if (!name || name.length < 5) return res.status(400).json({ error: "Name required (min 5 chars)" });

    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key configured" });

    const catName = category || "construction";
    const prompt = `Create a complete calculator specification for "${name}". Category: ${catName}.

Return ONLY valid JSON:
{
  "slug": "kebab-case-slug",
  "name": "${name}",
  "category": "${catName}",
  "desc": "One-sentence description of what this calculator does",
  "seo_title": "Compelling SEO title max 55 chars with key benefit",
  "seo_description": "SEO meta description max 155 chars that makes people want to click",
  "steps": ["Step 1: ...", "Step 2: ...", "Step 3: ..."],
  "mistakes": ["Common mistake 1", "Common mistake 2"],
  "faq": [{"q":"Common question?","a":"Clear answer"}],
  "inputs": [
    {"id":"field_id","label":"Human Label","type":"number","unit":"m","placeholder":"e.g. 5.0","min":0.1,"max":1000,"step":0.1,"default":5}
  ],
  "outputs": [
    {"id":"result_id","label":"Human Label","unit":"m²","highlight":true}
  ],
  "formula": "JavaScript function body: const a=parseFloat(inputs.field_id)||0; return { result_id: a*2 };"
}

Rules:
- Use 2-4 inputs and 1-3 outputs
- Formula MUST use inputs.field_id and return an object with output IDs
- Return {error:true} for invalid inputs
- All math must be client-side JavaScript
- Make the calculator actually useful and practical`;

    const text = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 3000);
    if (!text) return res.status(500).json({ error: "AI call failed" });

    const m = text.match(/\{[\s\S]*\}/);
    if (!m) return res.status(500).json({ error: "No JSON in AI response", raw: text.slice(0,200) });

    const calc = JSON.parse(m[0]);
    if (!calc.inputs || !calc.outputs || !calc.formula) {
      return res.status(500).json({ error: "Missing required fields", parsed: JSON.stringify(calc).slice(0,200) });
    }

    const slug = calc.slug || name.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');

    // Save to pipeline as draft (ready for review)
    await db.collection("calc_pipeline").doc(slug).set({
      slug,
      name: calc.name || name,
      category: calc.category || catName,
      status: "draft",
      source: "quick_generator",
      formula: calc.formula,
      inputs: calc.inputs,
      outputs: calc.outputs,
      langs: {
        en: {
          name: calc.name || name,
          desc: calc.desc || "",
          seo_title: calc.seo_title || "",
          seo_description: calc.seo_description || "",
          steps: calc.steps || [],
          mistakes: calc.mistakes || [],
          faq: calc.faq || [],
        }
      },
      created_at: admin.firestore.FieldValue.serverTimestamp(),
      updated_at: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });

    // Also save to calc_cms for the dashboard editor
    await db.collection("calc_cms").doc(slug).set({
      slug,
      name: calc.name || name,
      category: calc.category || catName,
      formula: calc.formula,
      inputs: calc.inputs,
      outputs: calc.outputs,
      langs: {
        en: {
          name: calc.name || name,
          desc: calc.desc || "",
          seo_title: calc.seo_title || "",
          seo_description: calc.seo_description || "",
          steps: calc.steps || [],
          mistakes: calc.mistakes || [],
          faq: calc.faq || [],
        }
      },
      status: "draft",
      created_at: admin.firestore.FieldValue.serverTimestamp(),
      updated_at: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });

    const result = {
      slug,
      name: calc.name,
      inputs: calc.inputs.length,
      outputs: calc.outputs.length,
      seo_title: calc.seo_title,
      saved_to: "pipeline + cms",
      next: "Go to Calculators tab to review, translate, and publish",
    };

    // Fully complete the calc server-side: long-form article, input labels,
    // FAQ, and complete translations for every language (incl. articles).
    try {
      const newDoc = await db.collection("calc_cms").doc(slug).get();
      const compResults = { translations: 0, metaFixed: 0, longContentFixed: 0, longContentTranslated: 0, labelsFixed: 0, faqFixed: 0, faqTranslated: 0, linksAdded: 0, mechanicsFixed: 0 };
      await _autoPilotProcessDoc(newDoc, apiKey, provider, provCfg.model, compResults, {}, {});
      result.completion = compResults;
      result.auto_translated = compResults.translations + " languages";
      // Mirror completed langs into the pipeline copy used for review
      const completedDoc = await db.collection("calc_cms").doc(slug).get();
      if (completedDoc.exists) {
        await db.collection("calc_pipeline").doc(slug).set({ langs: completedDoc.data().langs || {} }, { merge: true });
      }
    } catch(e) {
      console.warn("quickGenerate completion pass failed:", slug, e.message);
      result.completion_error = e.message;
    }

    // Auto-publish if requested
    if (publish) {
      try {
        const publishResult = await db.collection("calc_cms").doc(slug).get();
        // Trigger hosting deploy would need separate process, just mark as published
        await db.collection("calc_cms").doc(slug).update({ status: "published", published_at: admin.firestore.FieldValue.serverTimestamp() });
        result.published = true;
        result.publish_note = "Marked as published. Run regenerate+deploy to make live.";
      } catch(e) { result.publish_error = e.message; }
    }

    return res.status(200).json(result);
  } catch(e) {
    console.error("quickGenerateCalc error:", e.message);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Auto-fix hreflang gaps — finds missing language entries and generates them
 */
exports.autoFixHreflangHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key configured" });

    // Find calcs with missing languages
    const snap = await db.collection("calc_cms").where("status", "==", "published").limit(50).get();
    const toFix = [];
    snap.forEach(doc => {
      const data = doc.data();
      const langs = data.langs || {};
      const missing = ["es","fr","de","it","pt"].filter(l => !langs[l] || !langs[l].name);
      if (missing.length > 0 && langs.en?.name) {
        toFix.push({ slug: doc.id, en: langs.en, missing });
      }
    });

    if (toFix.length === 0) return res.status(200).json({ fixed: 0, message: "All calcs have complete language coverage" });

    let fixed = 0;
    for (const calc of toFix) {
      for (const lang of calc.missing) {
        try {
          const tPrompt = `Translate this calculator content from English to ${lang === 'es' ? 'Spanish' : lang === 'fr' ? 'French' : lang === 'de' ? 'German' : lang === 'it' ? 'Italian' : 'Portuguese'}. Preserve {placeholder} tokens. Return ONLY JSON.

Input: ${JSON.stringify({ name: calc.en.name, desc: calc.en.desc || '', seo_title: calc.en.seo_title || '', seo_description: calc.en.seo_description || '' })}`;

          const tText = await _callAIRaw(apiKey, provider, provCfg.model, tPrompt, 1500);
          if (!tText) continue;
          const tM = tText.match(/\{[\s\S]*\}/);
          if (!tM) continue;
          const translated = JSON.parse(tM[0]);
          await db.collection("calc_cms").doc(calc.slug).set({
            [`langs.${lang}`]: { ...translated, steps: [], mistakes: [], faq: [] }
          }, { merge: true });
          fixed++;
        } catch(e) {}
      }
    }

    return res.status(200).json({ fixed, calcs_scanned: toFix.length, total_missing: toFix.reduce((s,c) => s + c.missing.length, 0) });
  } catch(e) {
    console.error("autoFixHreflang error:", e.message);
    return res.status(500).json({ error: e.message });
  }
});

// ═══════════════════════════════════════════════════════
//  AUTONOMOUS GROWTH AGENT — 24/7 Self-Improving Engine
// ═══════════════════════════════════════════════════════

const AGENT_DEFAULTS = {
  max_daily_actions: 30,
  max_publishes_per_day: 5,
  max_api_calls_per_day: 200,
  auto_publish: true,
  auto_optimize: true,
  quality_threshold: 80, // Min score to auto-publish (0-100)
  focus_areas: ["fix_meta","ctr_improvement","hreflang_fix","optimize_ctr","generate_faq","competitor_gaps"],
  source_sites: [
    "https://www.omnicalculator.com/construction",
    "https://www.calculator.net/",
    "https://www.gigacalculator.com/",
  ],
};

function _todayKey() { return new Date().toISOString().slice(0,10); }

async function _getStrategy() {
  const doc = await db.collection("admin_prefs").doc("autonomous_strategy").get();
  return doc.exists ? { ...AGENT_DEFAULTS, ...doc.data() } : AGENT_DEFAULTS;
}

async function _countToday(col) {
  const snap = await db.collection(col)
    .where("date", "==", _todayKey())
    .get();
  return snap.size;
}

async function _incrementCounter(col, docId, field) {
  const ref = db.collection(col).doc(docId);
  await db.runTransaction(async t => {
    const d = await t.get(ref);
    const val = (d.exists ? (d.data()[field] || 0) : 0) + 1;
    t.set(ref, { date: _todayKey(), [field]: val, updated_at: admin.firestore.FieldValue.serverTimestamp() }, { merge: true });
  });
}

function _slugify(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,60);
}

// ══ Quality Gate — scores calculator 0-100, must pass threshold to auto-publish ══
function _scoreCalcQuality(data) {
  let score = 0;
  const issues = [];
  const en = (data.langs && data.langs.en) || {};

  // Formula exists and is valid JS
  if (data.formula && typeof data.formula === 'string' && data.formula.length > 10) {
    score += 15;
    try { new Function('inputs', '"use strict";' + data.formula); } catch(e) { issues.push('Formula syntax error: '+e.message); score -= 5; }
  } else { issues.push('Missing or too-short formula'); }

  // Inputs
  const inputs = data.inputs || [];
  if (inputs.length >= 2) { score += 10; }
  else if (inputs.length === 1) { score += 5; }
  else { issues.push('No inputs defined'); }

  // Outputs
  const outputs = data.outputs || [];
  if (outputs.length >= 1) { score += 10; }
  else { issues.push('No outputs defined'); }

  // Each input has id, type, label
  const validInputs = inputs.filter(i => i.id && i.type);
  score += Math.min(10, validInputs.length * 3);

  // Each output has id
  const validOutputs = outputs.filter(o => o.id);
  score += Math.min(5, validOutputs.length * 2);

  // SEO title (English)
  if (en.seo_title && en.seo_title.length >= 15 && en.seo_title.length <= 65) {
    score += 15;
  } else if (en.seo_title) {
    score += 8;
    if (en.seo_title.length > 65) issues.push('SEO title too long ('+en.seo_title.length+' chars)');
  } else { issues.push('Missing English SEO title'); }

  // SEO description
  if (en.seo_description && en.seo_description.length >= 30) {
    score += 10;
  } else if (en.seo_description) {
    score += 5;
  } else { issues.push('Missing English SEO description'); }

  // Steps/how-to
  const steps = (en.steps || []).filter(Boolean);
  if (steps.length >= 3) { score += 10; }
  else if (steps.length >= 1) { score += 5; }
  else { issues.push('Missing how-to steps'); }

  // FAQ
  const faq = (en.faq || []);
  if (faq.length >= 3) { score += 10; }
  else if (faq.length >= 1) { score += 5; }
  else { issues.push('Missing FAQ items'); }

  // Spanglish check
  const spanishWords = ['calculadora','hormigon','ladrillo','tabique','pintura','pared','techo','suelo','fontaneria','electricidad','carpinteria','mamposteria'];
  const hasSpanglish = en.seo_title && spanishWords.some(w => (en.seo_title||'').toLowerCase().includes(w));
  if (hasSpanglish) { score -= 10; issues.push('Spanish words in English title'); }

  // Has name
  if (en.name && en.name.length >= 3) { score += 5; }
  else { issues.push('Missing English name'); }

  score = Math.max(0, Math.min(100, score));
  return { score, issues, passed: score >= 80 };
}

// ══ Auto-deploy helper — publishes a single calc page directly to Firebase Hosting ══
const _deployCache = { currentVersion: null, currentFiles: null, fetchAt: 0 };

/**
 * _deployPagesToHosting — the ONE correct incremental deploy path.
 *
 * Firebase Hosting versions do NOT inherit files from the previous version, and
 * a single populateFiles call is capped at 15,000 files (the site has 22k+). So
 * we must: (1) clone the FULL current file manifest, (2) overlay the changed
 * pages, (3) create a fresh version, (4) populate the manifest in chunks under
 * the limit (populateFiles is additive across calls on the same version — this
 * is how the CLI deploys large sites), (5) upload only the changed bodies,
 * (6) finalize + release.
 *
 * The old code either sent all 22k files in one call (publishCalcToHosting →
 * "exceeds 15000 file limit") or populated ONLY the new files onto an empty
 * version (_autoDeployCalc → would drop the site to a handful of pages). Both
 * are replaced by this helper.
 *
 * @param {Object} newFiles  { "/en/slug/": { gzipped: Buffer, hash: string }, ... }
 * @param {string} message   release message
 */
const HOSTING_SITE = "calctowork";
const HOSTING_API = "https://firebasehosting.googleapis.com/v1beta1";
const POPULATE_CHUNK = 8000; // safely under the 15k per-call limit

// Fingerprint of THIS source file, computed once per container at cold start. Returned
// by the maintenance endpoints so a response can be attributed to a specific build —
// otherwise a warm instance serving the previous bundle is indistinguishable from a bug.
const _BUILD_ID = (() => {
  try {
    const c = require("crypto"), f = require("fs");
    return c.createHash("sha256").update(f.readFileSync(__filename)).digest("hex").slice(0, 8);
  } catch (e) { return "unknown"; }
})();
async function _deployPagesToHosting(newFiles, message) {
  if (!newFiles || Object.keys(newFiles).length === 0) return { error: "No files to deploy" };

  const tokenResult = await admin.app().options.credential.getAccessToken();
  const token = tokenResult.access_token;
  const headers = { "Authorization": "Bearer " + token, "Content-Type": "application/json" };

  // 1. Current release → version name + config
  const releasesRes = await fetch(`${HOSTING_API}/sites/${HOSTING_SITE}/releases?pageSize=1`, { headers });
  if (!releasesRes.ok) return { error: "Failed to get releases: " + await releasesRes.text() };
  const releasesData = await releasesRes.json();
  const currentVersionName = releasesData.releases?.[0]?.version?.name;
  const currentConfig = releasesData.releases?.[0]?.version?.config || {};
  if (!currentVersionName) return { error: "No current version to clone from" };

  // 2. Clone the FULL current file manifest (paginated)
  const merged = {};
  let pageToken = null;
  do {
    const url = `${HOSTING_API}/${currentVersionName}/files?pageSize=1000${pageToken ? "&pageToken=" + pageToken : ""}`;
    const filesRes = await fetch(url, { headers });
    if (!filesRes.ok) return { error: "Failed to list current files: " + await filesRes.text() };
    const filesData = await filesRes.json();
    (filesData.files || []).forEach(f => { if (f.path && f.hash) merged[f.path] = f.hash; });
    pageToken = filesData.nextPageToken || null;
  } while (pageToken);

  const clonedCount = Object.keys(merged).length;

  // Core files that must survive every incremental deploy. A clone missing any of
  // these is a stale manifest, not a legitimate state.
  const CRITICAL_HOSTING_PATHS = ["/robots.txt", "/sitemap.xml", "/index.html", "/ads.txt"];
  const missingCritical = CRITICAL_HOSTING_PATHS.filter(p => !merged[p]);

  // Files we can rebuild from the bundle are restored rather than aborted on.
  const RESTORABLE = { "/favicon.ico": "icon-192.png" };
  const restored = [];
  for (const [hostPath, assetFile] of Object.entries(RESTORABLE)) {
    if (merged[hostPath]) continue;
    try {
      const pathx = require("path"), fsx = require("fs");
      const zlibx = require("zlib"), utilx = require("util"), cryptox = require("crypto");
      const gzipx = utilx.promisify(zlibx.gzip);
      const src = pathx.join(__dirname, "assets", assetFile);
      if (!fsx.existsSync(src)) continue;
      const gz = await gzipx(fsx.readFileSync(src));
      const h = cryptox.createHash("sha256").update(gz).digest("hex");
      newFiles[hostPath] = { gzipped: gz, hash: h };
      restored.push(hostPath);
    } catch (e) { console.warn("[Deploy] could not restore " + hostPath + ": " + e.message); }
  }
  // Also restore the IndexNow ownership key: it is generated text, and losing it makes
  // every subsequent ping fail with 403 for no visible reason.
  // restore ads.txt: losing it silently stops AdSense from recognising the site.
  try {
    if (!merged["/ads.txt"] && !newFiles["/ads.txt"]) {
      const zlibA = require("zlib"), utilA = require("util"), cryptoA = require("crypto");
      const gzipA = utilA.promisify(zlibA.gzip);
      const gz = await gzipA(Buffer.from(ADS_TXT_LINE + "\n", "utf8"));
      newFiles["/ads.txt"] = { gzipped: gz, hash: cryptoA.createHash("sha256").update(gz).digest("hex") };
      restored.push("/ads.txt");
    }
  } catch (e) { console.warn("[Deploy] could not restore ads.txt: " + e.message); }

  try {
    const keyPath = "/" + INDEXNOW_KEY + ".txt";
    if (!merged[keyPath] && !newFiles[keyPath]) {
      const zlibk = require("zlib"), utilk = require("util"), cryptok = require("crypto");
      const gzipk = utilk.promisify(zlibk.gzip);
      const gz = await gzipk(Buffer.from(INDEXNOW_KEY, "utf8"));
      newFiles[keyPath] = { gzipped: gz, hash: cryptok.createHash("sha256").update(gz).digest("hex") };
      restored.push(keyPath);
    }
  } catch (e) { console.warn("[Deploy] could not restore IndexNow key: " + e.message); }

  if (restored.length) console.warn("[Deploy] restored missing core files: " + restored.join(", "));

  if (missingCritical.length) {
    return { error: "Refusing to deploy: cloned manifest is missing core files (" +
      missingCritical.join(", ") + "). This means a stale release was read; releasing it " +
      "would delete them from the live site." };
  }
  if (clonedCount < 1000) {
    // Safety net: if we somehow got a near-empty manifest, refuse — releasing it
    // would wipe the live site. Better to fail loudly than to nuke 22k pages.
    return { error: `Refusing to deploy: only ${clonedCount} existing files cloned (expected 20k+). Aborting to protect the live site.` };
  }

  // 3. Overlay the changed pages (both trailing-slash variants Firebase serves).
  // Guard against empty keys: stripping the trailing slash from "/" yields "",
  // which populateFiles rejects ("key must be defined and not empty").
  for (const [path, { hash }] of Object.entries(newFiles)) {
    if (!path) continue;
    merged[path] = hash;
    const noSlash = path.replace(/\/$/, "");
    if (noSlash && noSlash !== path) merged[noSlash] = hash;
  }
  // Final safety: never send an empty-string key to the API
  delete merged[""];

  // 4. Create new version
  const createRes = await fetch(`${HOSTING_API}/sites/${HOSTING_SITE}/versions`, {
    method: "POST", headers, body: JSON.stringify({ config: _patchConfigCSP(currentConfig) }),
  });
  if (!createRes.ok) return { error: "Failed to create version: " + await createRes.text() };
  const newVersionName = (await createRes.json()).name;

  // 5. populateFiles in chunks (additive); collect required uploads + upload URL
  const entries = Object.entries(merged);
  const uploadRequired = new Set();
  let uploadUrl = null;
  for (let i = 0; i < entries.length; i += POPULATE_CHUNK) {
    const chunk = Object.fromEntries(entries.slice(i, i + POPULATE_CHUNK));
    const populateRes = await fetch(`${HOSTING_API}/${newVersionName}:populateFiles`, {
      method: "POST", headers, body: JSON.stringify({ files: chunk }),
    });
    if (!populateRes.ok) return { error: `populateFiles chunk ${i} failed: ` + await populateRes.text() };
    const pd = await populateRes.json();
    if (pd.uploadUrl) uploadUrl = pd.uploadUrl;
    (pd.uploadRequiredHashes || []).forEach(h => uploadRequired.add(h));
  }

  // 6. Upload only the changed file bodies Firebase doesn't already have
  if (uploadUrl) {
    for (const { gzipped, hash } of Object.values(newFiles)) {
      if (!uploadRequired.has(hash)) continue;
      const up = await fetch(`${uploadUrl}/${hash}`, {
        method: "POST", headers: { "Authorization": "Bearer " + token, "Content-Type": "application/octet-stream" },
        body: gzipped,
      });
      if (!up.ok) return { error: `Upload failed for hash ${hash}: ` + await up.text() };
    }
  }

  // 7. Finalize + release
  const fin = await fetch(`${HOSTING_API}/${newVersionName}?update_mask=status`, {
    method: "PATCH", headers, body: JSON.stringify({ status: "FINALIZED" }),
  });
  if (!fin.ok) return { error: "Finalize failed: " + await fin.text() };
  const rel = await fetch(`${HOSTING_API}/sites/${HOSTING_SITE}/releases?versionName=${newVersionName}`, {
    method: "POST", headers, body: JSON.stringify({ message: message || "Incremental deploy" }),
  });
  if (!rel.ok) return { error: "Release failed: " + await rel.text() };

  return { deployed: true, versionName: newVersionName, pagesUpdated: Object.keys(newFiles), totalFiles: Object.keys(merged).length };
}

// Build the gzipped HTML files for one calc (all languages) WITHOUT deploying.
// Returns { "/en/slug/": {gzipped, hash}, ... }. Used so many calcs can be
// deployed in a SINGLE atomic release (deploying per-calc races against
// Firebase release propagation and reverts earlier calcs).
// Static calculators keep their inputs/outputs/formula in bundled static files
// (functions/calcs/<id>/calc.json), NOT in Firestore — only their translated
// CONTENT is synced to calc_cms. Deploying such a calc through buildPage (which
// reads the calculator config from the doc) produced a page with the article but
// an EMPTY, non-working calculator. This loads the real config so the deployed
// page keeps a functioning calculator.
function _loadStaticConfig(staticId, slugForLookup) {
  const fs = require("fs");
  const path = require("path");
  const ids = [];
  if (staticId) ids.push(String(staticId));
  // Fallback: resolve the real static id from the calc index by slug (guards
  // against a corrupted/placeholder staticId in the doc).
  if (slugForLookup) {
    try {
      const idx = require("./calc-index.json");
      const list = Array.isArray(idx) ? idx : Object.values(idx);
      const hit = list.find(c => c.slug === slugForLookup || c.id === slugForLookup);
      if (hit && hit.id && !ids.includes(String(hit.id))) ids.push(String(hit.id));
    } catch(e) {}
  }
  for (const id of ids) {
    for (const dir of [path.join(__dirname, "calcs", id), path.join(__dirname, "..", "src", "calculators", id)]) {
      try {
        const p = path.join(dir, "calc.json");
        if (fs.existsSync(p)) { const c = JSON.parse(fs.readFileSync(p, "utf8")); c._dir = dir; return c; }
      } catch(e) {}
    }
  }
  return null;
}

// Load a static calc's per-language label file (inputs/outputs human labels etc.)
function _loadStaticLang(dir, lang) {
  if (!dir) return null;
  const fs = require("fs");
  const path = require("path");
  try {
    const p = path.join(dir, lang + ".json");
    if (fs.existsSync(p)) return JSON.parse(fs.readFileSync(p, "utf8"));
  } catch(e) {}
  return null;
}

async function _buildCalcFiles(slug, dataArg) {
  const crypto = require("crypto");
  const zlib = require("zlib");
  const util = require("util");
  const gzip = util.promisify(zlib.gzip);
  let data = dataArg;
  if (!data) {
    const doc = await db.collection("calc_cms").doc(slug).get();
    if (!doc.exists) return {};
    data = doc.data();
  }
  // Always merge the static calc's config (if it has one) — not only when
  // inputs/formula are missing. Otherwise calcs that DO have inputs in Firestore
  // still lost their gauge, presets and per-language labels, which live only in
  // the static files. Each field is merged only when the doc lacks it.
  {
    const sc = _loadStaticConfig(data.staticId, slug);
    if (sc) {
      data = { ...data };
      if (!(data.inputs || []).length && Array.isArray(sc.inputs)) data.inputs = sc.inputs;
      if (!(data.outputs || []).length && Array.isArray(sc.outputs)) data.outputs = sc.outputs;
      if (!data.formula || data.formula.length < 10) data.formula = sc.formula;
      if (!data.comparison_presets && sc.comparison_presets) data.comparison_presets = sc.comparison_presets;
      if (!data.gauge && sc.gauge) data.gauge = sc.gauge;

      // Merge per-language human labels (inputs/outputs) from the static lang
      // files so the calculator shows "Initial velocity" instead of raw ids
      // like "vi"/"tiempo" (which was also leaking Spanish onto other languages).
      const langsCopy = { ...(data.langs || {}) };
      for (const lang of LANGS) {
        const lf = _loadStaticLang(sc._dir, lang);
        if (!lf) continue;
        const ld = { ...(langsCopy[lang] || {}) };
        // Only take static labels that are REAL labels, not the raw id repeated
        // (some static lang files contain e.g. {"glucosa_mgdl":"glucosa_mgdl"}).
        const clean = obj => { const o = {}; for (const [k, v] of Object.entries(obj || {})) { if (v && typeof v === "string" && v !== k) o[k] = v; } return o; };
        if ((!ld.inputs_labels || !Object.keys(ld.inputs_labels).length) && lf.inputs && typeof lf.inputs === "object" && !Array.isArray(lf.inputs)) {
          const g = clean(lf.inputs); if (Object.keys(g).length) ld.inputs_labels = g;
        }
        if ((!ld.outputs_labels || !Object.keys(ld.outputs_labels).length) && lf.outputs && typeof lf.outputs === "object" && !Array.isArray(lf.outputs)) {
          const g = clean(lf.outputs); if (Object.keys(g).length) ld.outputs_labels = g;
        }
        langsCopy[lang] = ld;
      }
      data.langs = langsCopy;
    }
  }
  data = _applyLangSlugs(slug, data); // deploy each lang at its translated slug
  const oldMap = _getOldSlugIndex()[slug] || _getOldSlugIndex()[String(data.id)] || null;
  const files = {};
  for (const lang of LANGS) {
    if (!data.langs || !data.langs[lang] || !data.langs[lang].name) continue;
    const langSlug = (data.langs[lang] && data.langs[lang].slug) || slug;
    const html = buildPage(slug, lang, data);
    const gzipped = await gzip(Buffer.from(html, "utf8"));
    const hash = crypto.createHash("sha256").update(gzipped).digest("hex");
    files[`/${lang}/${langSlug}/`] = { gzipped, hash };
    // Keep every historical URL for this calc alive, serving the SAME html whose
    // canonical points to the new SEO slug — so old links and any prior Google
    // indexation consolidate onto the new slug (no hard redirect needed):
    //   • the primary (Spanish) slug — from the old dual-URL bug
    //   • the previous translated slug — from the SEO slug migration
    const aliases = new Set([slug]);
    if (oldMap && oldMap[lang]) aliases.add(oldMap[lang]);
    for (const a of aliases) {
      if (a && a !== langSlug) files[`/${lang}/${a}/`] = { gzipped, hash };
    }
  }
  return files;
}

async function _autoDeployCalc(slug) {
  if (!slug) return { error: "No slug" };
  try {
    const newFiles = await _buildCalcFiles(slug);
    if (Object.keys(newFiles).length === 0) return { error: "No language content" };
    const result = await _deployPagesToHosting(newFiles, `[Agent] Auto-deploy: ${slug}`);
    if (result.error) { console.error("[Deploy] Failed for", slug, ":", result.error); return result; }
    console.log(`[Deploy] Published ${slug} in ${Object.keys(newFiles).length} languages`);
    return { deployed: true, slug, languages: Object.keys(newFiles).length };
  } catch(e) {
    console.error("[Deploy] Failed for", slug, ":", e.message);
    return { error: e.message };
  }
}

// ══ Full site regeneration — homepage, block pages, sitemaps (runs after agent cycle) ══
async function _regenerateCorePages() {
  const crypto = require("crypto");
  const zlib = require("zlib");
  const util = require("util");
  const gzip = util.promisify(zlib.gzip);
  // Full public origin — was "calctowork" (the Firebase site NAME), which
  // produced malformed URLs like https://calctowork/en/... in the sitemap,
  // canonicals and robots.txt, so Google rejected every URL. Must be the domain.
  const SITE = "https://calcto.work";

  try {
    console.log("[Regen] Generating core pages...");

    // Get all published calcs (no limit — the whole catalog must be in the
    // sitemap and homepage; a 500 cap silently dropped ~35 calcs).
    const snap = await db.collection("calc_cms").where("status","==","published").get();
    if (snap.empty) return { error: "No published calcs" };

    const calcs = [];
    snap.forEach(d => calcs.push({ id: d.id, ...d.data() }));
    const newFiles = {};
    const slugIdxHome = _getSlugIndex();

    // ── HOMEPAGE (per language) ──
    // Category display metadata (icon + label). Falls back to a generic bucket.
    const CAT_META = {
      estructuras:["🏗️","Structures"], construccion:["🏠","Construction"], mamposteria:["🧱","Masonry"],
      pavimentos:["🪵","Flooring"], fontaneria:["🚿","Plumbing"], electricidad:["⚡","Electrical"],
      climatizacion:["❄️","HVAC"], carpinteria:["🪚","Carpentry"], pintura:["🎨","Painting"],
      gestion:["📋","Management"], matematicas:["➗","Mathematics"], ciencia:["🔬","Science"],
      salud:["❤️","Health"], finanzas:["💰","Finance"], cotidiano:["📅","Everyday"],
      quimica:["⚗️","Chemistry"], electronica:["🔌","Electronics"], clima:["🌦️","Climate"],
      utilidades:["🛠️","Utilities"], fotografia:["📷","Photography"], transporte:["🚗","Transport"],
      fisica:["🧲","Physics"], musica:["🎵","Music"], industria:["🏭","Industry"],
    };
    // The stored `category` field is inconsistent (mixed languages, underscores,
    // near-duplicates like Health/Health_fitness/Fitness/Medical). Fold every
    // raw value into one canonical bucket so the homepage shows ~20 clean
    // categories instead of 45 messy ones.
    const CAT_ALIAS = {
      // health
      health:"salud", health_fitness:"salud", fitness:"salud", medical:"salud", deportes:"salud", sports:"salud", nutricion:"salud", nutrition:"salud",
      // math & stats
      math:"matematicas", mathematics:"matematicas", estadistica:"matematicas", statistics:"matematicas", geometry:"matematicas", geometria:"matematicas", volume:"matematicas",
      // structures / engineering
      structures:"estructuras", engineering:"estructuras", ingenieria:"estructuras", engenharia:"estructuras", engenharia_estrutural:"estructuras",
      // construction / renovation / home
      construction:"construccion", constructie:"construccion", renovation:"construccion", home_improvement:"construccion", bau:"construccion", bau_rechner:"construccion", obra:"construccion",
      // materials / masonry
      materials:"mamposteria", materiaux:"mamposteria", materiales:"mamposteria", masonry:"mamposteria",
      // hvac / climate
      hvac:"climatizacion", climate:"clima", weather:"clima", meteo:"clima",
      // finance / real estate
      finance:"finanzas", real_estate:"finanzas", realestate:"finanzas", inmobiliaria:"finanzas", loans:"finanzas",
      // energy / electrical / electronics
      energy:"electricidad", energy_conversion:"electricidad", electrical:"electricidad", electronics:"electronica",
      // everyday / date / time / calendar / conversion / geo
      date:"cotidiano", calendar:"cotidiano", time:"cotidiano", conversion:"utilidades", converter:"utilidades", geospatial:"utilidades", geo:"utilidades", tools:"utilidades",
      // science-ish
      science:"ciencia", biology:"ciencia", physics:"fisica", chemistry:"quimica",
    };
    const _normCat = (raw) => {
      let k = String(raw || "").toLowerCase().trim().replace(/[\s\-]+/g, "_").replace(/[^a-z_]/g, "");
      // strip a trailing "_rechner"/"_calculator" etc. that leaked into the field
      k = k.replace(/_(rechner|calculator|calculadora|calculateur)$/,"");
      if (CAT_META[k]) return k;            // already canonical
      if (CAT_ALIAS[k]) return CAT_ALIAS[k]; // known alias
      return "utilidades";                   // everything unrecognised → Utilities
    };
    // Minimal per-language UI strings for the homepage chrome.
    const HOME_I18N = {
      en:{h1:"Free Online Calculators",tag:"Instant, accurate calculators for construction, finance, health, math & science — no signup.",browse:"Browse by Category",search:"Search calculators…",none:"No calculators found.",rights:"All rights reserved.",disc:"Results are estimates — verify before relying on them.",more:"See all"},
      es:{h1:"Calculadoras en Línea Gratis",tag:"Calculadoras instantáneas y precisas de construcción, finanzas, salud, matemáticas y ciencia — sin registro.",browse:"Explorar por Categoría",search:"Buscar calculadoras…",none:"No se encontraron calculadoras.",rights:"Todos los derechos reservados.",disc:"Los resultados son estimaciones — verifícalos antes de usarlos.",more:"Ver todas"},
      fr:{h1:"Calculateurs en Ligne Gratuits",tag:"Calculateurs instantanés et précis : construction, finance, santé, maths et sciences — sans inscription.",browse:"Parcourir par Catégorie",search:"Rechercher des calculateurs…",none:"Aucun calculateur trouvé.",rights:"Tous droits réservés.",disc:"Les résultats sont des estimations — vérifiez-les avant utilisation.",more:"Voir tout"},
      de:{h1:"Kostenlose Online-Rechner",tag:"Sofortige, präzise Rechner für Bau, Finanzen, Gesundheit, Mathe & Wissenschaft — ohne Anmeldung.",browse:"Nach Kategorie durchsuchen",search:"Rechner suchen…",none:"Keine Rechner gefunden.",rights:"Alle Rechte vorbehalten.",disc:"Ergebnisse sind Schätzungen — vor Gebrauch prüfen.",more:"Alle ansehen"},
      it:{h1:"Calcolatori Online Gratuiti",tag:"Calcolatori istantanei e precisi per edilizia, finanza, salute, matematica e scienza — senza registrazione.",browse:"Sfoglia per Categoria",search:"Cerca calcolatori…",none:"Nessun calcolatore trovato.",rights:"Tutti i diritti riservati.",disc:"I risultati sono stime — verifica prima di usarli.",more:"Vedi tutti"},
      pt:{h1:"Calculadoras Online Grátis",tag:"Calculadoras instantâneas e precisas de construção, finanças, saúde, matemática e ciência — sem cadastro.",browse:"Explorar por Categoria",search:"Buscar calculadoras…",none:"Nenhuma calculadora encontrada.",rights:"Todos os direitos reservados.",disc:"Os resultados são estimativas — verifique antes de usar.",more:"Ver todas"},
    };
    for (const lang of LANGS) {
      const T = HOME_I18N[lang] || HOME_I18N.en;
      // Group calcs by category, de-duplicating by display name.
      const groups = {}; const seen = new Set();
      for (const c of calcs) {
        if (!c.langs?.[lang]?.name) continue;
        const name = c.langs[lang].name;
        const smap = slugIdxHome[c.slug] || slugIdxHome[String(c.id)] || null;
        const slug = (smap && smap[lang]) || c.langs?.[lang]?.slug || c.slug || c.id;
        const cat = _normCat(c.category || c.block_slug || c.block);
        const key = cat + "|" + name.toLowerCase();
        if (seen.has(key)) continue; seen.add(key);
        (groups[cat] = groups[cat] || []).push({ name, slug });
      }
      const totalTools = Object.values(groups).reduce((n, a) => n + a.length, 0);
      // Sort categories by size (biggest first) so the page leads with substance.
      const orderedCats = Object.keys(groups).sort((a, b) => groups[b].length - groups[a].length);
      // Build the category cards using the site's real stylesheet classes
      // (.blocks-grid / .block-card / .calc-list) — yesterday's design.
      const blocksHtml = orderedCats.map(cat => {
        const [icon, label] = CAT_META[cat] || ["🧮", (cat.charAt(0).toUpperCase() + cat.slice(1))];
        const items = groups[cat]
          .sort((a, b) => a.name.localeCompare(b.name))
          .map(t => `<li><a href="/${lang}/${t.slug}/">${esc(t.name)}</a></li>`)
          .join("");
        return `<div class="block-card">
  <div class="block-card-header"><div class="block-icon">${icon}</div><div class="block-title">${esc(label)}</div></div>
  <ul class="calc-list">${items}</ul>
</div>`;
      }).join("\n");

      const html = `<!DOCTYPE html>
<html lang="${lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="theme-color" content="#f97316">
<meta name="google-adsense-account" content="${ADSENSE_ID}">
<link rel="preconnect" href="https://pagead2.googlesyndication.com">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ADSENSE_ID}" crossorigin="anonymous"></script>
<title>CalcToWork — ${totalTools}+ ${esc(T.h1)}</title>
<meta name="description" content="${esc(T.tag)} ${totalTools}+ tools.">
<link rel="canonical" href="${SITE}/${lang}/">
${LANGS.map(l => `<link rel="alternate" hreflang="${l}" href="${SITE}/${l}/">`).join("\n")}
<link rel="alternate" hreflang="x-default" href="${SITE}/en/">
<meta property="og:title" content="CalcToWork — ${esc(T.h1)}">
<meta property="og:description" content="${esc(T.tag)}">
<meta property="og:type" content="website">
<meta property="og:url" content="${SITE}/${lang}/">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"CalcToWork","url":"${SITE}/","inLanguage":"${lang}"}</script>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/css/styles.css?v=${_ASSET_VER}">
<script>if(localStorage.getItem('ctw-theme')==='dark'){document.documentElement.setAttribute('data-theme','dark');}</script>
</head>
<body>
<a href="#main-content" class="skip-link">Skip to content</a>
<header>
  <div class="header-inner">
    <a class="logo" href="/${lang}/"><img src="/favicon.svg" alt="" class="logo-icon" width="32" height="32">Calc<span>To</span>Work</a>
    <div class="nav-wrapper" id="nav-wrapper">
      <div class="lang-switcher" aria-label="Language">
        ${LANGS.map(l => `<a href="/${l}/"${l === lang ? ' class="active"' : ""}>${l.toUpperCase()}</a>`).join("")}
        <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode" title="Toggle dark mode">&#9790;</button>
      </div>
    </div>
  </div>
</header>
<section class="hero">
  <h1>${esc(T.h1)}</h1>
  <p>${esc(T.tag)}</p>
</section>
<main class="container" id="main-content">
  <div class="text-center mt-2"><div class="section-title">${esc(T.browse)}</div></div>
  <div class="search-box-wrap">
    <input type="search" id="calc-search" class="calc-search-input" placeholder="${esc(T.search)}" autocomplete="off" spellcheck="false" aria-label="${esc(T.search)}">
    <div id="search-no-results" class="search-no-results" style="display:none;">${esc(T.none)}</div>
  </div>
  <div class="blocks-grid" id="blocks-grid">
${blocksHtml}
  </div>
</main>
<footer>
  <div class="footer-inner">
    <div>© <span id="yr"></span> CalcToWork — ${esc(T.rights)}</div>
    <div class="mt-1" style="font-size:.8rem;">${esc(T.disc)}</div>
    <div class="footer-links">${LANGS.map(l => `<a href="/${l}/">${l.toUpperCase()}</a>`).join("")}</div>
  </div>
</footer>
<script>
document.getElementById('yr').textContent=new Date().getFullYear();
(function(){
  var s=document.getElementById('calc-search'),nr=document.getElementById('search-no-results'),g=document.getElementById('blocks-grid');
  if(!s||!g)return;
  function f(){var q=s.value.trim().toLowerCase(),tv=0;
    g.querySelectorAll('.block-card').forEach(function(card){var cv=0;
      card.querySelectorAll('.calc-list a').forEach(function(a){var sh=!q||a.textContent.trim().toLowerCase().indexOf(q)!==-1;a.parentElement.style.display=sh?'':'none';if(sh)cv++;});
      card.style.display=cv>0?'':'none';tv+=cv;});
    if(nr)nr.style.display=(q&&tv===0)?'':'none';}
  s.addEventListener('input',f);s.addEventListener('search',f);
})();
document.addEventListener('keydown',function(e){if(e.key==='/'&&document.activeElement===document.body){e.preventDefault();var s=document.getElementById('calc-search');if(s)s.focus();}});
</script>
<script src="/js/dark-mode.js?v=${_ASSET_VER}"></script>
</body>
</html>`;
      const gzipped = await gzip(Buffer.from(html, "utf8"));
      const hash = crypto.createHash("sha256").update(gzipped).digest("hex");
      newFiles[`/${lang}/`] = { gzipped, hash };
      // Root redirect
      if (lang === "en") newFiles["/"] = { gzipped, hash };
    }

    // ── SITEMAPS ──
    const slugIdx = _getSlugIndex();
    const sitemapUrls = calcs.map(c => {
      const enSlug = c.slug || c.id;
      const smap = slugIdx[c.slug] || slugIdx[String(c.id)] || null;
      let xml = "";
      for (const lang of LANGS) {
        // Only list a language the calc actually has (has a name), and always
        // use the authoritative translated slug so the sitemap matches the
        // canonical URLs — never the primary-slug duplicate.
        if (!c.langs?.[lang]?.name) continue;
        const lSlug = (smap && smap[lang]) || c.langs?.[lang]?.slug || enSlug;
        // Real modification date so Google re-crawls what changed, not everything.
        const _lm = c.updated_at || c.updatedAt || c.last_modified || null;
        const lastmod = (_lm && _lm.toDate) ? _lm.toDate().toISOString().slice(0, 10)
          : (typeof _lm === "string" && _lm.length >= 10 ? _lm.slice(0, 10) : null);
        xml += `  <url><loc>${SITE}/${lang}/${lSlug}/</loc>${lastmod ? `<lastmod>${lastmod}</lastmod>` : ""}<changefreq>monthly</changefreq><priority>0.7</priority></url>\n`;
      }
      return xml;
    }).join("");

    const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${sitemapUrls}
</urlset>`;
    const smGzipped = await gzip(Buffer.from(sitemapXml, "utf8"));
    const smHash = crypto.createHash("sha256").update(smGzipped).digest("hex");
    newFiles["/sitemap.xml"] = { gzipped: smGzipped, hash: smHash };

    // ── llms.txt — curated site map for AI search engines / LLMs (llmstxt.org).
    // Helps ChatGPT, Claude, Perplexity, Gemini etc. understand and cite the site.
    const llmsByCat = {};
    for (const c of calcs) {
      if (!c.langs?.en?.name) continue;
      const smap = slugIdx[c.slug] || slugIdx[String(c.id)] || null;
      const enSlug = (smap && smap.en) || c.langs?.en?.slug || c.slug || c.id;
      const cat = _normCat(c.category);
      (llmsByCat[cat] = llmsByCat[cat] || []).push({ name: c.langs.en.name, url: `${SITE}/en/${enSlug}/` });
    }
    let llmsTxt = `# CalcToWork\n\n> ${calcs.length}+ free online calculators for construction, finance, health, mathematics and science. Every tool runs instantly in the browser with no signup, and each page explains the formula with worked examples. Available in English, Spanish, French, German, Italian and Portuguese.\n\n`;
    llmsTxt += `## About\n\n`;
    llmsTxt += `- The English pages are listed below. For another language, swap \`/en/\` for \`/es/\`, \`/fr/\`, \`/de/\`, \`/it/\` or \`/pt/\` (each language has its own translated URL slug).\n`;
    llmsTxt += `- Every calculator page answers the question directly, shows the formula, gives example values, and includes an FAQ.\n`;
    llmsTxt += `- Full sitemap: ${SITE}/sitemap.xml\n\n`;
    for (const cat of Object.keys(llmsByCat).sort()) {
      const meta = CAT_META[cat] || ["", cat];
      llmsTxt += `## ${meta[1]}\n\n`;
      for (const it of llmsByCat[cat].sort((a, b) => a.name.localeCompare(b.name))) {
        llmsTxt += `- [${it.name}](${it.url})\n`;
      }
      llmsTxt += `\n`;
    }
    const llmsGz = await gzip(Buffer.from(llmsTxt, "utf8"));
    const llmsHash = crypto.createHash("sha256").update(llmsGz).digest("hex");
    newFiles["/llms.txt"] = { gzipped: llmsGz, hash: llmsHash };

    // robots.txt — allow everyone, and explicitly welcome the major AI crawlers
    // (a named user-agent block overrides the `*` block, so each gets its own Allow).
    const AI_BOTS = ["GPTBot","OAI-SearchBot","ChatGPT-User","ClaudeBot","Claude-Web","anthropic-ai","PerplexityBot","Perplexity-User","Google-Extended","Applebot-Extended","Amazonbot","CCBot","cohere-ai","Meta-ExternalAgent","DuckAssistBot","YouBot","Bingbot"];
    let robotsTxt = `User-agent: *\nAllow: /\n\n`;
    robotsTxt += `# AI search engines & assistants are welcome to crawl and cite CalcToWork\n`;
    robotsTxt += AI_BOTS.map(b => `User-agent: ${b}\nAllow: /`).join("\n\n");
    robotsTxt += `\n\nSitemap: ${SITE}/sitemap.xml`;
    const rbGzipped = await gzip(Buffer.from(robotsTxt, "utf8"));
    const rbHash = crypto.createHash("sha256").update(rbGzipped).digest("hex");
    newFiles["/robots.txt"] = { gzipped: rbGzipped, hash: rbHash };

    // IndexNow ownership proof: a text file at the site root whose body is the key.
    // Bing/Yandex fetch this to verify we control the host before accepting pings.
    const inGz = await gzip(Buffer.from(INDEXNOW_KEY, "utf8"));
    const inHash = crypto.createHash("sha256").update(inGz).digest("hex");
    newFiles["/" + INDEXNOW_KEY + ".txt"] = { gzipped: inGz, hash: inHash };

    // ads.txt, written every time rather than merely inherited from the previous
    // manifest — inheritance is exactly how it could vanish unnoticed.
    const adsGz = await gzip(Buffer.from(ADS_TXT_LINE + "\n", "utf8"));
    const adsHash = crypto.createHash("sha256").update(adsGz).digest("hex");
    newFiles["/ads.txt"] = { gzipped: adsGz, hash: adsHash };

    // /favicon.ico is the fallback path crawlers try before reading any <link> tag.
    // It was 404, so Google had no icon to show beside a result.
    try {
      const pathx = require("path"), fsx = require("fs");
      const icoSrc = pathx.join(__dirname, "assets", "icon-192.png");
      const icoBuf = fsx.existsSync(icoSrc) ? fsx.readFileSync(icoSrc) : null;
      if (icoBuf) {
        const icoGz = await gzip(icoBuf);
        const icoHash = crypto.createHash("sha256").update(icoGz).digest("hex");
        newFiles["/favicon.ico"] = { gzipped: icoGz, hash: icoHash };
      }
    } catch (e) { console.warn("favicon.ico not published:", e.message); }

    // ── Deploy via the shared chunked helper (clones full manifest so calc
    // pages are preserved; old code populated ONLY core files and would have
    // 404'd the entire catalog). ──
    const result = await _deployPagesToHosting(newFiles, "[Agent] Core pages regeneration");
    if (result.error) { console.error("[Regen] Failed:", result.error); return result; }
    console.log(`[Regen] Core pages deployed: homepage (6 langs), sitemap, robots.txt, llms.txt`);
    return { deployed: true, files: Object.keys(newFiles).length };
  } catch(e) {
    console.error("[Regen] Failed:", e.message);
    return { error: e.message };
  }
}

/**
 * MASTER AUTONOMOUS LOOP — runs every 4 hours
 * Assess → Plan → Execute → Measure → Report
 */
exports.autonomousGrowthLoop = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .pubsub.schedule("0 */4 * * *").timeZone("UTC").onRun(async () => {
  const startTime = Date.now();
  const log = { phase: "init", actions: 0, errors: [] };
  let budgetSpent = 0;

  try {
    // ── 0. Check strategy ──
    const strat = await _getStrategy();
    if (!strat.enabled) { console.log("[AGENT] Disabled — skipping"); return { skipped: true, reason: "disabled" }; }
    if (strat.emergency_stop) { console.log("[AGENT] Emergency stop active"); return { skipped: true, reason: "emergency_stop" }; }

    const [todayActions, todayPublishes, todayApiCalls] = await Promise.all([
      _countToday("autonomous_actions"),
      _countToday("autonomous_publishes"),
      _countToday("autonomous_api_usage"),
    ]);

    if (todayActions >= strat.max_daily_actions) { console.log("[AGENT] Daily action limit reached"); return { skipped: true, reason: "action_limit" }; }
    if (todayPublishes >= strat.max_publishes_per_day) { console.log("[AGENT] Daily publish limit reached — skipping publish actions"); }
    if (todayApiCalls >= strat.max_api_calls_per_day) { console.log("[AGENT] API call budget exhausted"); return { skipped: true, reason: "api_budget" }; }

    // ── 1. ASSESS ──
    log.phase = "assess";
    console.log("[AGENT] Assessing site health...");
    const assessment = {
      gsc_pages: [], gsc_queries: [], alerts: [], competitor_gaps: [],
      cms_calcs: 0, pipeline_count: 0, missing_hreflang: 0,
    };

    try {
      // GSC data
      const siteUrl = functions.config().gsc?.site_url || "sc-domain:calcto.work";
      const cutoff30 = new Date(Date.now() - 30*86400000).toISOString().slice(0,10);
      const [gscPageSnap, gscQuerySnap] = await Promise.all([
        db.collection("gsc_page_stats").where("site_url","==",siteUrl).where("date",">=",cutoff30).orderBy("date","desc").limit(200).get().catch(() => ({ empty: true, docs: [] })),
        db.collection("gsc_search_data").where("site_url","==",siteUrl).where("date",">=",cutoff30).orderBy("date","desc").limit(200).get().catch(() => ({ empty: true, docs: [] })),
      ]);

      const pageMap = {};
      gscPageSnap.forEach(d => { const p = d.data(); const s = (p.page||"").split("/").filter(Boolean).pop()||""; if (!pageMap[s]) pageMap[s]={ slug:s, imp:0, clicks:0, pos:0, n:0 }; pageMap[s].imp+=p.total_impressions||0; pageMap[s].clicks+=p.total_clicks||0; pageMap[s].pos+=p.avg_position||0; pageMap[s].n++; });
      assessment.gsc_pages = Object.values(pageMap)
        .filter(p => p.imp >= 5)
        .map(p => ({ slug:p.slug, imp:p.imp, clicks:p.clicks, ctr: p.imp>0?+(p.clicks/p.imp*100).toFixed(2):0, pos: p.n>0?+(p.pos/p.n).toFixed(1):99 }))
        .sort((a,b) => b.imp - a.imp).slice(0, 30);

      const queryMap = {};
      gscQuerySnap.forEach(d => { const q = d.data().query||""; if (!queryMap[q]) queryMap[q]={ query:q, imp:0, clicks:0, pos:0, n:0 }; queryMap[q].imp+=d.data().impressions||0; queryMap[q].clicks+=d.data().clicks||0; queryMap[q].pos+=d.data().position||0; queryMap[q].n++; });
      assessment.gsc_queries = Object.values(queryMap).filter(q => q.imp>=10).sort((a,b)=>b.imp-a.imp).slice(0,20).map(q=>({...q, pos: q.n>0?+(q.pos/q.n).toFixed(1):99}));
    } catch(e) { log.errors.push("gsc: "+e.message); console.warn("[AGENT] GSC data unavailable:", e.message); }

    // Alerts
    try {
      const alertSnap = await db.collection("dashboard_alerts").where("acknowledged","==",false).limit(10).get();
      alertSnap.forEach(d => assessment.alerts.push({ id: d.id, ...d.data() }));
    } catch(e) {}

    // Competitor gaps — auto-refresh if stale (>24h)
    try {
      const compDoc = await db.collection("admin_prefs").doc("competitor_analysis").get();
      const data = compDoc.exists ? compDoc.data() : null;
      const isStale = !data || !data.analyzed_at || 
        (Date.now()/1000 - (data.analyzed_at._seconds || 0)) > 86400;

      if (isStale && strat.focus_areas.some(f => f === "competitor_gaps" || f === "analyze_competitor")) {
        console.log("[AGENT] Competitor data stale, auto-refreshing...");
        for (const site of (strat.source_sites || ["https://www.omnicalculator.com/construction"]).slice(0, 1)) {
          try {
            await new Promise(r => setTimeout(r, 2000)); // rate limit
            const r = await fetch(`${site}`, { timeout: 15000, headers: { "User-Agent": "CalcToWork/1.0" } });
          } catch(e) {}
        }
      }
      if (compDoc.exists) assessment.competitor_gaps = (compDoc.data().gaps || []).slice(0, 10);
    } catch(e) {}

    // Scan for calculators with missing SEO content
    try {
      const seoGapSnap = await db.collection("calc_cms").limit(100).get();
      let missingTitle = 0, missingDesc = 0, missingSteps = 0, missingFaq = 0, spanglishCount = 0;
      const spanglishWords = ['calculadora','hormigon','ladrillo','tabique','pintura','pared','techo','suelo','fontaneria','electricidad','carpinteria','mamposteria','pavimentos','estructuras','gestion','climatizacion'];
      const missingNames = [];
      seoGapSnap.forEach(d => {
        const data = d.data();
        const en = data.langs?.en || {};
        const name = en.name || data.name || '';
        if (!en.seo_title || en.seo_title.length < 15) { missingTitle++; if (missingNames.length < 5) missingNames.push(d.id); }
        if (!en.seo_description || en.seo_description.length < 30) missingDesc++;
        if (!en.steps || en.steps.filter(Boolean).length < 2) missingSteps++;
        if (!en.faq || en.faq.length === 0) missingFaq++;
        if (en.seo_title && spanglishWords.some(w => en.seo_title.toLowerCase().includes(w))) spanglishCount++;
      });
      assessment.seo_gaps = { missingTitle, missingDesc, missingSteps, missingFaq, spanglishCount, sampleSlugs: missingNames };
      assessment.cms_calcs = missingTitle + Math.max(0, seoGapSnap.size - missingTitle); // approximate
      assessment.pipeline_count = 0;
    } catch(e) {}

    // ── 2. PLAN — AI decides what to do ──
    log.phase = "plan";
    console.log("[AGENT] Planning actions...");

    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) { console.log("[AGENT] No AI key — skipping planning"); return { skipped: true, reason: "no_ai_key" }; }

    const lowCTR = assessment.gsc_pages.filter(p => p.ctr < 1 && p.imp >= 20).slice(0, 10);
    const highImpression = assessment.gsc_pages.filter(p => p.imp >= 50).slice(0, 5);
    const gaps = assessment.competitor_gaps.slice(0, 5);

    const planPrompt = `You are the autonomous SEO agent for CalcToWork (461 calculators). Pick 3-5 highest-priority actions.

CRITICAL SITE STATE:
- ${assessment.seo_gaps ? assessment.seo_gaps.missingTitle + ' calcs MISSING SEO titles' : 'unknown'}
- ${assessment.seo_gaps ? assessment.seo_gaps.missingFaq + ' calcs NEED FAQ schema (0 have it!)' : 'unknown'}
- ${assessment.seo_gaps ? assessment.seo_gaps.spanglishCount + ' calcs have SPANGLISH titles' : ''}
- ALL 461 calcs need long-form articles (>500 chars) for AdSense approval
- ALL 461 calcs need FAQ items for rich snippets
- Remaining: ${strat.max_daily_actions - todayActions} actions, ${strat.max_publishes_per_day - todayPublishes} publishes

BEST ACTIONS NOW:
- "generate_faq" — Add FAQ schema to calculators (needed for rich snippets + AdSense)
- "generate_content" — Write long-form articles (needed for AdSense unique content requirement)
- "fix_meta" — Fix missing/broken SEO titles
- "fix_hreflang" — Fill missing language translations

Return ONLY: {"actions":[{"type":"generate_faq","reason":"0 calcs have FAQ","priority":1},{"type":"generate_content","reason":"0 calcs have articles","priority":2}]}`;

    let plan;
    try {
      const planText = await _callAIRaw(apiKey, provider, provCfg.model, planPrompt, 1500);
      budgetSpent++;
      await _incrementCounter("autonomous_api_usage", _todayKey(), "calls");
      if (planText) {
        const m = planText.match(/\{[\s\S]*\}/);
        if (m) plan = JSON.parse(m[0]);
      }
    } catch(e) { log.errors.push("plan: "+e.message); console.warn("[AGENT] Planning failed:", e.message); }

    if (!plan || !plan.actions || plan.actions.length === 0) {
      // Fallback: prioritize FAQ + content (biggest gap for AdSense)
      plan = { actions: [] };
      plan.actions.push({ type:"generate_faq", reason:"0 calcs have FAQ — needed for rich snippets + AdSense", priority:1 });
      plan.actions.push({ type:"generate_content", reason:"0 calcs have articles — needed for AdSense unique content", priority:2 });
      plan.actions.push({ type:"fix_meta", reason:"Fix remaining SEO gaps", priority:3 });
      plan.actions.push({ type:"request_indexing", reason:"Check indexing + submit unindexed pages to Google", priority:4 });
      plan.actions.push({ type:"fix_hreflang", reason:"routine maintenance", priority:5 });
    }

    console.log(`[AGENT] Planned ${plan.actions.length} actions`);

    // ── 3. EXECUTE ──
    log.phase = "execute";
    const results = [];
    let publishedToday = todayPublishes;

    for (const action of plan.actions.sort((a,b)=>(a.priority||5)-(b.priority||5))) {
      if (todayActions + results.length >= strat.max_daily_actions) break;
      if (budgetSpent >= strat.max_api_calls_per_day - todayApiCalls) break;

      try {
        const actionLog = { ...action, status:"pending", started_at: new Date().toISOString() };

        if (action.type === "optimize_ctr" && action.slug && strat.focus_areas.some(f => f === "optimize_ctr" || f === "ctr_improvement")) {
          const oPrompt = `Rewrite the SEO title for this calculator page to improve CTR. Current slug: "${action.slug}". Make it compelling and click-worthy (max 55 chars). Include key benefit. Return ONLY: {"seo_title":"..."}`;
          const oText = await _callAIRaw(apiKey, provider, provCfg.model, oPrompt, 500);
          budgetSpent++;
          if (oText) {
            const oM = oText.match(/\{[\s\S]*\}/);
            if (oM) {
              const o = JSON.parse(oM[0]);
              if (o.seo_title) {
                await db.collection("calc_cms").doc(action.slug).set({
                  "langs.en.seo_title": o.seo_title,
                  updated_at: admin.firestore.FieldValue.serverTimestamp(),
                }, { merge: true });
                if (strat.auto_publish) { actionLog.deploy = await _autoDeployCalc(action.slug); }
                actionLog.result = "Optimized title: " + o.seo_title;
                actionLog.status = "completed";
              }
            }
          }
        } else if (action.type === "generate_calc" && action.name && strat.focus_areas.some(f => f === "generate_calc" || f === "competitor_gaps") && publishedToday < strat.max_publishes_per_day) {
          // Skip category-like names (not actual calculators)
          const categoryWords = ["calculators","converters","calculadora","category","rechner","calcolatrice","calculateur","calculadoras"];
          const isCategory = categoryWords.some(w => action.name.toLowerCase().includes(w)) || action.name.endsWith("s") && action.name.split(" ").length === 1;
          if (isCategory) { actionLog.result = "Skipped category name"; actionLog.status = "skipped"; }
          else {
            const slug = _slugify(action.name);
            const exists = await db.collection("calc_cms").doc(slug).get();
            if (!exists.exists) {
              const gPrompt = `Create a complete calculator specification for "${action.name}". Return JSON: {"slug":"${slug}","name":"${action.name}","category":"construction","desc":"one sentence","seo_title":"55 char SEO title","seo_description":"155 char meta description","steps":["step1","step2","step3"],"mistakes":["mistake1"],"faq":[{"q":"?","a":"answer"}],"inputs":[{"id":"value","label":"Value","type":"number","unit":"","placeholder":"","min":0,"max":1000,"step":0.1,"default":1}],"outputs":[{"id":"result","label":"Result","unit":"","highlight":true}],"formula":"const v=parseFloat(inputs.value)||0;return{result:v*2};"}`;
              const gText = await _callAIRaw(apiKey, provider, provCfg.model, gPrompt, 2000);
              budgetSpent++;
              if (gText) {
                const gM = gText.match(/\{[\s\S]*\}/);
                if (gM) {
                  const calc = JSON.parse(gM[0]);
                  await db.collection("calc_cms").doc(slug).set({
                    slug, name: calc.name||action.name, category: calc.category||"construction",
                    formula: calc.formula, inputs: calc.inputs, outputs: calc.outputs,
                    langs: { en: { name:calc.name, desc:calc.desc, seo_title:calc.seo_title, seo_description:calc.seo_description, steps:calc.steps, mistakes:calc.mistakes, faq:calc.faq } },
                    status: strat.auto_publish ? "published" : "draft",
                    source: "autonomous_agent",
                    created_at: admin.firestore.FieldValue.serverTimestamp(),
                    updated_at: admin.firestore.FieldValue.serverTimestamp(),
                  });

                  // Fully complete the new calc: long-form article, input labels,
                  // FAQ, and complete translations (incl. translated articles).
                  let translated = 0;
                  try {
                    const newDoc = await db.collection("calc_cms").doc(slug).get();
                    const compResults = { translations: 0, metaFixed: 0, longContentFixed: 0, longContentTranslated: 0, labelsFixed: 0, faqFixed: 0, faqTranslated: 0, linksAdded: 0, mechanicsFixed: 0 };
                    await _autoPilotProcessDoc(newDoc, apiKey, provider, provCfg.model, compResults, {}, {});
                    translated = compResults.translations;
                    budgetSpent += 2 + compResults.translations + (compResults.longContentTranslated || 0);
                    actionLog.completion = compResults;
                  } catch(e) { console.warn("[AGENT] Completion pass failed for", slug, e.message); }

                  // ══ QUALITY GATE ══ (re-read so the score reflects the completed content)
                  const finalDoc = await db.collection("calc_cms").doc(slug).get();
                  const qCheck = _scoreCalcQuality(finalDoc.exists ? finalDoc.data() : { formula:calc.formula, inputs:calc.inputs, outputs:calc.outputs, langs:{ en: { name:calc.name, seo_title:calc.seo_title, seo_description:calc.seo_description, steps:calc.steps, faq:calc.faq } } });
                  actionLog.quality = qCheck;

                  if (strat.auto_publish && qCheck.passed) {
                    // Only publish if quality score passes
                    const finalStatus = "published";
                    await db.collection("calc_cms").doc(slug).set({ status:finalStatus, quality_score:qCheck.score, quality_issues:qCheck.issues, updated_at:admin.firestore.FieldValue.serverTimestamp() }, { merge: true });
                    await _incrementCounter("autonomous_publishes", _todayKey(), "count");
                    publishedToday++;
                    actionLog.deploy = await _autoDeployCalc(slug);
                    actionLog.result = `Published: ${slug} (${1+translated} langs) [quality: ${qCheck.score}/100]`;
                  } else if (strat.auto_publish && !qCheck.passed) {
                    // Failed quality gate — save as draft
                    await db.collection("calc_cms").doc(slug).set({ status:"draft", quality_score:qCheck.score, quality_issues:qCheck.issues, updated_at:admin.firestore.FieldValue.serverTimestamp() }, { merge: true });
                    actionLog.result = `Draft (quality ${qCheck.score}/100 — needs ${qCheck.issues.join('; ')})`;
                  } else {
                    actionLog.result = `Drafted: ${slug} (${1+translated} langs)`;
                  }
                  actionLog.status = "completed";
                }
              }
            } else { actionLog.result = "Already exists"; actionLog.status = "skipped"; }
          }
        } else if (action.type === "fix_hreflang" && strat.focus_areas.some(f => f === "fix_hreflang" || f === "hreflang_fix")) {
          try {
            const fixed = await _autoFixMissingLangs(apiKey, provider, provCfg.model);
            if (fixed > 0 && strat.auto_publish) {
              // Deploy affected calcs
              const snap = await db.collection("calc_cms").where("status","==","published").limit(30).get();
              for (const d of snap.docs) { await _autoDeployCalc(d.id); }
            }
            actionLog.result = `Fixed ${fixed} hreflang gaps`;
            actionLog.status = fixed > 0 ? "completed" : "skipped";
          } catch(e) { actionLog.result = "Error: "+e.message; actionLog.status = "error"; }
        } else if (action.type === "fix_meta" && strat.focus_areas.some(f => f === "fix_meta" || f === "meta_fix")) {
          const metaResult = await _autoFixMeta(apiKey, provider, provCfg.model, 5);
          budgetSpent += metaResult.fixed;
          actionLog.result = `Fixed ${metaResult.fixed} meta issues`;
          actionLog.slugs = metaResult.slugs;
          actionLog.status = metaResult.fixed > 0 ? "completed" : "skipped";
          // Auto-deploy each fixed calc
          if (strat.auto_publish && metaResult.slugs) {
            for (const s of metaResult.slugs) { await _autoDeployCalc(s).catch(()=>{}); }
          }
        } else if (action.type === "generate_faq" && strat.focus_areas.some(f => f === "generate_faq" || f === "faq")) {
          // Generate FAQ for ALL languages where missing
          const snap = await db.collection("calc_cms").limit(30).get();
          let faqCount = 0, langCount = 0;
          const allLangs = ["en","es","fr","de","it","pt"];
          const langNames = {en:"English",es:"Spanish",fr:"French",de:"German",it:"Italian",pt:"Portuguese"};

          for (const doc of snap.docs) {
            if (faqCount >= 8) break;
            const data = doc.data();
            const en = (data.langs?.en) || {};
            const name = en.name || data.name || doc.id;
            if (!name) continue;

            // Check which languages need FAQ
            for (const lang of allLangs) {
              if (faqCount >= 8) break;
              const langData = (data.langs || {})[lang] || {};
              if (langData.faq && langData.faq.length >= 2) continue; // already has FAQ in this lang
              const langName = langNames[lang] || lang;

              try {
                const faqPrompt = `Create 3-4 FAQ items (question + answer) for a free calculator called "${name}". Write in ${langName}. Each FAQ should address a common user question. Keep answers clear (50-150 words). Return ONLY JSON: {"faq":[{"q":"Question in ${langName}?","a":"Answer in ${langName}."}]}`;
                const fText = await _callAIRaw(apiKey, provider, provCfg.model, faqPrompt, 1000);
                budgetSpent++;
                if (fText) {
                  const fM = fText.match(/\{[\s\S]*\}/);
                  if (fM) {
                    const parsed = JSON.parse(fM[0]);
                    if (parsed.faq && parsed.faq.length > 0) {
                      await doc.ref.set({ [`langs.${lang}.faq`]: parsed.faq, updated_at: admin.firestore.FieldValue.serverTimestamp() }, { merge: true });
                      faqCount++; langCount++;
                    }
                  }
                }
              } catch(e) { console.warn("[Agent] FAQ failed:", doc.id, lang, e.message); }
            }
            if (strat.auto_publish && faqCount > 0) { await _autoDeployCalc(doc.id).catch(()=>{}); }
          }
          actionLog.result = `Generated FAQ: ${faqCount} items across ${langCount} languages`;
          actionLog.status = faqCount > 0 ? "completed" : "skipped";
        } else if (action.type === "generate_content" && strat.focus_areas.some(f => f === "generate_content" || f === "long_content")) {
          // Generate long-form article per calculator (English base, then translate)
          const snap = await db.collection("calc_cms").limit(20).get();
          let contentCount = 0;
          for (const doc of snap.docs) {
            if (contentCount >= 2) break;
            const data = doc.data();
            const en = (data.langs?.en) || {};
            const name = en.name || data.name || doc.id;
            if (!name) continue;
            if (en.long_content && en.long_content.length > 500) continue;

            try {
              const contentPrompt = `Write a comprehensive long-form article (800-1500 words) about a free online calculator called "${name}". Include: 1) What it does and who uses it. 2) The formula explained simply. 3) Step-by-step worked example. 4) Common mistakes to avoid. 5) Practical applications. Use <h2>, <p>, <ul>, <li> HTML tags. Write in clear, helpful English. Return the full HTML content.`;
              const cText = await _callAIRaw(apiKey, provider, provCfg.model, contentPrompt, 3000);
              budgetSpent++;
              if (cText && cText.length > 200) {
                await doc.ref.set({ "langs.en.long_content": cText, updated_at: admin.firestore.FieldValue.serverTimestamp() }, { merge: true });
                contentCount++;
                if (strat.auto_publish) { await _autoDeployCalc(doc.id).catch(()=>{}); }
              }
            } catch(e) { console.warn("[Agent] Content failed:", doc.id, e.message); }
          }
          actionLog.result = `Generated ${contentCount} articles`;
          actionLog.status = contentCount > 0 ? "completed" : "skipped";
        } else if (action.type === "request_indexing" && strat.focus_areas.some(f => f === "request_indexing" || f === "index")) {
          // Request Google indexing for pages not yet indexed
          const siteUrl = functions.config().gsc?.site_url || "sc-domain:calcto.work";
          const snapshot = await db.collection("calc_cms").limit(50).get();
          let indexed = 0, unindexed = 0, requested = 0;

          // Check GSC page stats
          let gscSlugs = new Set();
          try {
            const gscSnap = await db.collection("gsc_page_stats").where("site_url","==",siteUrl).where("date",">=",(new Date(Date.now()-30*86400000)).toISOString().slice(0,10)).limit(500).get();
            gscSnap.forEach(d => { const s = (d.data().page||"").split("/").filter(Boolean).pop()||""; gscSlugs.add(s); });
          } catch(e) {}

          for (const doc of snapshot.docs) {
            const slug = doc.id;
            if (gscSlugs.has(slug)) { indexed++; continue; }
            unindexed++;
            if (requested >= 10) continue;

            // Submit to Google via sitemap ping
            try {
              const url = "https://calcto.work/en/" + slug + "/";
              await fetch(`https://www.google.com/ping?sitemap=${encodeURIComponent(url)}`).catch(()=>{});
              requested++;
            } catch(e) {}
          }

          actionLog.result = `Index check: ${indexed} indexed, ${unindexed} not indexed, ${requested} submitted`;
          actionLog.status = requested > 0 ? "completed" : (unindexed === 0 ? "completed" : "skipped");
        } else {
          actionLog.status = "skipped";
          actionLog.result = "Not in focus areas or limits reached";
        }

        actionLog.completed_at = new Date().toISOString();
        actionLog.duration_ms = Date.now() - new Date(actionLog.started_at).getTime();
        results.push(actionLog);

        // Save to Firestore
        await db.collection("autonomous_actions").add({
          ...actionLog,
          date: _todayKey(),
          created_at: admin.firestore.FieldValue.serverTimestamp(),
        });
        await _incrementCounter("autonomous_actions", _todayKey(), "count");

      } catch(e) {
        log.errors.push(`action ${action.type}: ${e.message}`);
        console.error("[AGENT] Action failed:", action.type, e.message);
      }
    }

    // ── 4. REPORT ──
    log.phase = "report";
    log.actions = results.length;
    log.completed = results.filter(r => r.status === "completed").length;
    log.skipped = results.filter(r => r.status === "skipped").length;
    log.errors_count = log.errors.length;
    log.duration_ms = Date.now() - startTime;
    log.api_calls = budgetSpent;

    // ── 5. REGENERATE CORE PAGES if any changes were deployed ──
    if (log.completed > 0 && strat.auto_publish) {
      try {
        log.phase = "regenerate";
        console.log("[AGENT] Regenerating core pages (homepage, sitemap)...");
        log.regeneration = await _regenerateCorePages();
      } catch(e) {
        log.errors.push("regeneration: " + e.message);
      }
    }

    await db.collection("autonomous_reports").doc(_todayKey() + "_" + new Date().getHours()).set({
      ...log,
      created_at: admin.firestore.FieldValue.serverTimestamp(),
    });

    // ── 6. PING SEARCH ENGINES ──
    if (log.completed > 0) {
      try {
        const sitemapUrl = encodeURIComponent("https://calcto.work/sitemap.xml");
        await Promise.all([
          fetch(`https://www.google.com/ping?sitemap=${sitemapUrl}`).catch(()=>{}),
          fetch(`https://www.bing.com/ping?sitemap=${sitemapUrl}`).catch(()=>{}),
        ]);
        console.log("[AGENT] Pinged Google + Bing sitemaps");
      } catch(e) {}
    }

    // ── 7. WEEKLY BACKLINK RUN ── (only on Mondays)
    const isMonday = new Date().getUTCDay() === 1;
    if (isMonday && !log.phase.includes("backlink")) {
      try {
        log.phase = "backlink";
        const ua = "CalcToWork-Agent/1.0";
        const redditUrl = "https://www.reddit.com/api/submit";
        const r = await fetch(redditUrl, {
          method: "POST", timeout: 15000,
          headers: { "User-Agent": ua, "Content-Type": "application/x-www-form-urlencoded" },
          body: new URLSearchParams({ sr:"InternetIsBeautiful", title:"CalcToWork - 460+ Free Online Calculators", url:"https://calcto.work", kind:"link" }).toString()
        }).catch(()=>null);
        log.backlink_attempted = !!r;
        console.log("[AGENT] Backlink attempt:", r ? r.status : "failed");
      } catch(e) {}
    }

    console.log(`[AGENT] Done in ${(log.duration_ms/1000).toFixed(0)}s — ${log.completed} completed, ${log.skipped} skipped, ${log.errors_count} errors, ${log.api_calls} API calls${log.regeneration ? ' + core pages regenerated' : ''}`);
    return log;
  } catch(e) {
    console.error("[AGENT] Fatal error:", e.message);
    await db.collection("autonomous_reports").doc(_todayKey() + "_error").set({
      error: e.message, phase: log.phase, timestamp: admin.firestore.FieldValue.serverTimestamp(),
    });
    return { error: e.message, phase: log.phase };
  }
});

/**
 * Daily core page regeneration — keeps homepage + sitemaps fresh
 * Runs daily at 5 AM UTC
 */
exports.dailyCoreRegeneration = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .pubsub.schedule("0 5 * * *").timeZone("UTC").onRun(async () => {
  console.log("[DailyRegen] Regenerating core pages...");
  return await _regenerateCorePages();
});

/**
 * Daily autocomplete — processes a few incomplete calculators each day at 6 AM UTC.
 * Skips already-complete calcs. Slowly fills in missing content over time.
 */
exports.dailyAutoComplete = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .pubsub.schedule("0 6 * * *").timeZone("UTC").onRun(async () => {
  console.log("[DailyComplete] Starting...");
  const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
  const cfg = cfgDoc.exists ? cfgDoc.data() : {};
  const provider = cfg.active_provider || "deepseek";
  const provCfg = (cfg.providers || {})[provider] || {};
  const apiKey = provCfg.api_key;
  if (!apiKey) { console.log("[DailyComplete] No AI key"); return { error: "No AI key" }; }

  const stateRef = db.collection("admin_prefs").doc("daily_complete_state");
  const stateDoc = await stateRef.get();
  const state = stateDoc.exists ? stateDoc.data() : {};
  let cursorId = state.cursor_doc_id || null;
  let lastDoc = null;
  if (cursorId) { const c = await db.collection("calc_cms").doc(cursorId).get(); if (c.exists) lastDoc = c; }

  let query = db.collection("calc_cms").where("status","==","published").orderBy("__name__").limit(30);
  if (lastDoc) query = query.startAfter(lastDoc);
  const snap = await query.get();
  if (snap.empty) { await stateRef.set({ cursor_doc_id: null, processed: 0 }, { merge: true }); return { done: true }; }

  const results = { translations:0, metaFixed:0, longContentFixed:0, faqFixed:0, linksAdded:0 };
  let updated = 0, processed = 0, lastProcessed = null;

  for (const doc of snap.docs) {
    lastProcessed = doc.id;
    const data = doc.data();
    const en = (data.langs && data.langs.en) || {};
    const hasContent = en.long_content && en.long_content.length > 500;
    const hasFaq = en.faq && en.faq.length >= 2;
    const hasSteps = en.steps && en.steps.filter(Boolean).length >= 2;
    if (hasContent && hasFaq && hasSteps) { processed++; continue; }

    try {
      const changed = await _autoPilotProcessDoc(doc, apiKey, provider, provCfg.model, results, {}, {});
      if (changed) { updated++; try { await _autoDeployCalc(doc.id); } catch(e) {} }
    } catch(e) { console.warn("[DailyComplete] failed:", doc.id, e.message); }
    processed++;
  }

  const newTotal = (state.processed || 0) + processed;
  await stateRef.set({ cursor_doc_id: lastProcessed, processed: newTotal, updated: (state.updated||0)+updated, last_run: admin.firestore.FieldValue.serverTimestamp() }, { merge: true });

  console.log(`[DailyComplete] Done: ${processed} scanned, ${updated} updated`);
  return { processed, updated };
});

/**
 * regenerateCorePagesHttp — on-demand homepage + sitemap regeneration for the
 * dashboard Publish Center ("make everything live now" without a full deploy).
 */
exports.regenerateCorePagesHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const result = await _regenerateCorePages();
    return res.status(200).json(result || { done: true });
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Weekly backlink hunter — runs every Monday at 7 AM UTC
 */
exports.weeklyBacklinkHunter = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .pubsub.schedule("0 7 * * 1").timeZone("UTC").onRun(async () => {
  console.log("[Backlink] Weekly hunt starting...");
  const fetch = require("node-fetch");
  const ua = "CalcToWork/1.0";
  const SITE_URL = "https://calcto.work";

  // Try submissions
  const subs = [
    { name:"Reddit", url:"https://www.reddit.com/api/submit", method:"POST", headers:{"User-Agent":ua,"Content-Type":"application/x-www-form-urlencoded"}, body:new URLSearchParams({sr:"InternetIsBeautiful",title:"CalcToWork - 460+ Free Online Calculators in 6 Languages",url:SITE_URL,kind:"link"}).toString() },
    { name:"HackerNews", url:"https://news.ycombinator.com/submitlink?u="+encodeURIComponent(SITE_URL)+"&t=CalcToWork+-+Free+Online+Calculators", method:"GET" },
    { name:"ProductHunt", url:"https://www.producthunt.com/posts/new", method:"GET" },
  ];

  const results = [];
  for (const s of subs) {
    try {
      const r = await fetch(s.url, { method:s.method, headers:s.headers||{"User-Agent":ua}, body:s.body||undefined, timeout:15000 });
      results.push({ name:s.name, status: r.status < 400 ? "ok":"failed", code:r.status });
    } catch(e) { results.push({ name:s.name, status:"error", error:e.message }); }
  }

  await db.collection("admin_prefs").doc("backlink_weekly").set({
    results, week: new Date().toISOString().slice(0,10),
    checked_at: admin.firestore.FieldValue.serverTimestamp(),
  });

  console.log("[Backlink] Weekly hunt done:", results.length, "attempts");
  return { results };
});

// ══ Helper: auto-fix missing hreflang entries ══
async function _autoFixMissingLangs(apiKey, provider, model) {
  const snap = await db.collection("calc_cms").where("status","==","published").limit(30).get();
  let fixed = 0;
  for (const doc of snap.docs) {
    const data = doc.data();
    const langs = data.langs || {};
    const missing = ["es","fr","de","it","pt"].filter(l => !langs[l]?.name);
    if (missing.length === 0 || !langs.en?.name) continue;
    for (const lang of missing) {
      try {
        const tPrompt = `Translate to ${lang==="es"?"Spanish":lang==="fr"?"French":lang==="de"?"German":lang==="it"?"Italian":"Portuguese"}: {name:"${langs.en.name}"}. Return JSON: {"name":"..."}`;
        const text = await _callAIRaw(apiKey, provider, model, tPrompt, 300);
        if (!text) continue;
        const m = text.match(/\{[\s\S]*\}/);
        if (!m) continue;
        await doc.ref.set({ [`langs.${lang}`]: { ...JSON.parse(m[0]), steps:[], mistakes:[], faq:[] } }, { merge: true });
        fixed++;
      } catch(e) {}
    }
    if (fixed >= 20) break;
  }
  return fixed;
}

// ══ Helper: auto-fix missing meta ══
async function _autoFixMeta(apiKey, provider, model, limit) {
  const snap = await db.collection("calc_cms").limit(50).get();
  let fixed = 0;
  const slugs = [];
  for (const doc of snap.docs) {
    if (fixed >= limit) break;
    const data = doc.data();
    const en = data.langs?.en || {};
    if (!en.name) continue;
    let updates = {};
    if (!en.seo_title || en.seo_title.length < 10) {
      try {
        const text = await _callAIRaw(apiKey, provider, model,
          `SEO title for "${en.name}" calculator (max 55 chars, include key benefit). Return JSON: {"seo_title":"..."}`, 300);
        if (text) { const m = text.match(/\{[\s\S]*\}/); if (m) { const o = JSON.parse(m[0]); updates["langs.en.seo_title"] = o.seo_title; } }
      } catch(e) {}
    }
    if (!en.seo_description || en.seo_description.length < 20) {
      try {
        const text = await _callAIRaw(apiKey, provider, model,
          `Meta description for "${en.name}" (max 155 chars, include benefit + CTA). Return JSON: {"seo_description":"..."}`, 300);
        if (text) { const m = text.match(/\{[\s\S]*\}/); if (m) { const o = JSON.parse(m[0]); updates["langs.en.seo_description"] = o.seo_description; } }
      } catch(e) {}
    }
    if (Object.keys(updates).length > 0) {
      updates.updated_at = admin.firestore.FieldValue.serverTimestamp();
      await doc.ref.set(updates, { merge: true });
      fixed++;
      slugs.push(doc.id);
    }
  }
  return { fixed, slugs };
}

/**
 * Toggle autonomy on/off from dashboard
 */
exports.toggleAutonomyHttp = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const { enabled, emergency_stop, auto_publish } = req.body || {};
    const updates = {};
    if (enabled !== undefined) updates.enabled = enabled;
    if (emergency_stop !== undefined) updates.emergency_stop = emergency_stop;
    if (auto_publish !== undefined) updates.auto_publish = auto_publish;
    await db.collection("admin_prefs").doc("autonomous_strategy").set(updates, { merge: true });
    return res.status(200).json({ ...updates, status: "ok" });
  } catch(e) {
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Get autonomy status
 */
exports.getAutonomyStatusHttp = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method !== "GET") return res.status(405).json({ error: "GET only" });

  try {
    const strat = await _getStrategy();
    const [todayActions, todayPublishes, todayApi] = await Promise.all([
      _countToday("autonomous_actions"),
      _countToday("autonomous_publishes"),
      _countToday("autonomous_api_usage"),
    ]);

    // Recent actions — may fail if index is building
    let recent = [];
    try {
      const recentSnap = await db.collection("autonomous_actions")
        .where("date","==",_todayKey())
        .orderBy("created_at","desc").limit(10).get();
      recentSnap.forEach(d => recent.push({ id:d.id, ...d.data() }));
    } catch(e) { console.warn("[autonomy] Recent actions unavailable (index building?):", e.message); }

    // Last report
    let lastReport = null;
    try {
      const reportSnap = await db.collection("autonomous_reports")
        .orderBy("created_at","desc").limit(1).get();
      if (!reportSnap.empty) lastReport = reportSnap.docs[0].data();
    } catch(e) { console.warn("[autonomy] Reports unavailable:", e.message); }

    return res.status(200).json({
      enabled: !!strat.enabled,
      emergency_stop: !!strat.emergency_stop,
      auto_publish: !!strat.auto_publish,
      today: { actions: todayActions, publishes: todayPublishes, api_calls: todayApi },
      limits: { max_daily_actions: strat.max_daily_actions, max_publishes: strat.max_publishes_per_day, max_api: strat.max_api_calls_per_day },
      recent_actions: recent,
      last_report: lastReport,
    });
  } catch(e) {
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Sync static calculators from calc-index.json to calc_cms collection.
 * This populates calc_cms so the autonomous agent can find and fix SEO issues.
 */
exports.syncStaticCalcsHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");

  try {
    const path = require("path");
    const fs = require("fs");
    const indexPath = path.join(__dirname, "calc-index.json");
    if (!fs.existsSync(indexPath)) return res.status(500).json({ error: "calc-index.json not found" });

    const calcIndex = JSON.parse(fs.readFileSync(indexPath, "utf8"));
    let synced = 0;

    for (const calc of calcIndex) {
      const slug = calc.slug || "";
      const names = calc.names || {};
      if (!slug) continue;

      const langs = {};
      for (const lang of LANGS) {
        langs[lang] = { name: names[lang] || "", desc: "", seo_title: "", seo_description: "", steps: [], mistakes: [], faq: [] };
      }

      await db.collection("calc_cms").doc(slug).set({
        slug, staticId: calc.id || "",
        category: calc.category || "",
        standard: calc.standard || "",
        langs,
        status: "published",
        source: "static_sync",
        type: "static",
        synced_at: admin.firestore.FieldValue.serverTimestamp(),
        updated_at: admin.firestore.FieldValue.serverTimestamp(),
      }, { merge: true });

      synced++;
      if (synced % 100 === 0) console.log(`Synced ${synced}...`);
    }

    return res.status(200).json({ synced, message: "Agent can now fix SEO on all calculators" });
  } catch(e) {
    console.error("Sync error:", e.message);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Bulk generate SEO titles + descriptions for all calculators missing them.
 * Uses AI to create optimized titles. One-click improvement for the entire site.
 */
exports.generateAllSEOTitlesHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");

  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key configured" });

    const { limit, deploy } = req.body || {};
    const maxFix = limit || 25;

    const snap = await db.collection("calc_cms").limit(200).get();
    let generated = 0, skipped = 0;
    const results = [];

    for (const doc of snap.docs) {
      if (generated >= maxFix) break;
      const data = doc.data();
      const en = data.langs?.en || {};
      const name = en.name || (data.names && data.names['en']) || data.name || '';
      if (!name) { skipped++; continue; }

      const needsTitle = !en.seo_title || en.seo_title.length < 15;
      const needsDesc = !en.seo_description || en.seo_description.length < 30;

      if (!needsTitle && !needsDesc) { skipped++; continue; }

      try {
        const prompt = `Generate SEO metadata for a free calculator called "${name}".
${needsTitle ? 'Create a compelling SEO title (max 55 chars) with a key benefit or formula mention.' : ''}
${needsDesc ? 'Write a meta description (max 155 chars) that makes people click.' : ''}
Return ONLY JSON: {${needsTitle ? '"seo_title":"..."' : ''}${needsTitle && needsDesc ? ',' : ''}${needsDesc ? '"seo_description":"..."' : ''}}`;

        const text = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 500);
        if (!text) { skipped++; continue; }
        const m = text.match(/\{[\s\S]*\}/);
        if (!m) { skipped++; continue; }
        const o = JSON.parse(m[0]);

        const updates = { updated_at: admin.firestore.FieldValue.serverTimestamp() };
        if (o.seo_title) updates["langs.en.seo_title"] = o.seo_title;
        if (o.seo_description) updates["langs.en.seo_description"] = o.seo_description;
        await doc.ref.set(updates, { merge: true });

        results.push({ slug: doc.id, name, title: o.seo_title || '', desc: o.seo_description || '' });
        generated++;
        if (generated % 5 === 0) console.log(`Generated ${generated} SEO titles...`);
      } catch(e) { skipped++; }
    }

    // Auto-deploy if requested
    if (deploy && results.length > 0) {
      const slugs = [...new Set(results.map(r => r.slug))];
      for (const s of slugs.slice(0, 10)) {
        await _autoDeployCalc(s).catch(() => {});
      }
    }

    return res.status(200).json({
      generated, skipped, total: generated + skipped,
      results: results.slice(0, 20),
      deployed: deploy ? Math.min(results.length, 10) : 0,
    });
  } catch(e) {
    console.error("Generate SEO titles error:", e.message);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * Generate SEO titles for ONE specific calculator (used by Growth Lab)
 */
exports.generateOneSEOTitleHttp = functions.runWith({ timeoutSeconds: 60, memory: "256MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const { slug } = req.body || {};
    if (!slug) return res.status(400).json({ error: "Missing slug" });

    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key configured" });

    const doc = await db.collection("calc_cms").doc(slug).get();
    if (!doc.exists) return res.status(404).json({ error: "Not found" });
    const data = doc.data();
    const en = data.langs?.en || {};
    const name = en.name || (data.names && data.names['en']) || data.name || slug;
    if (!name) return res.status(400).json({ error: "No name" });

    const prompt = `Generate SEO metadata for a free calculator called "${name}". Create a compelling SEO title (max 55 chars) with benefit. Write a meta description (max 155 chars) that makes people click. Return ONLY JSON: {"seo_title":"...","seo_description":"..."}`;

    const text = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 500);
    if (!text) return res.status(500).json({ error: "AI call failed" });
    const m = text.match(/\{[\s\S]*\}/);
    if (!m) return res.status(500).json({ error: "No JSON in response" });
    const o = JSON.parse(m[0]);

    await doc.ref.set({
      "langs.en.seo_title": o.seo_title,
      "langs.en.seo_description": o.seo_description,
      updated_at: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });

    // Auto-deploy
    let deployResult = null;
    try { deployResult = await _autoDeployCalc(slug); } catch(e) {}

    return res.status(200).json({
      slug, name,
      seo_title: o.seo_title,
      seo_description: o.seo_description,
      deployed: !deployResult?.error,
    });
  } catch(e) {
    return res.status(500).json({ error: e.message });
  }
});

// ═══════════════════════════════════════════
//  BACKLINK HUNTER
// ═══════════════════════════════════════════
exports.backlinkHunterHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");

  try {
    const fetch = require("node-fetch");
    const SITE_URL = "https://calcto.work";
    const ua = "CalcToWork-Submitter/1.0";
    const results = [];

    const directories = [
      { name:"AlternativeTo", url:"https://alternativeto.net/software/calctowork/", type:"profile", action:"Check/create listing" },
      { name:"ToolPilot", url:"https://www.toolpilot.ai/submit", type:"form", action:"Submit tool" },
      { name:"There's An AI For That", url:"https://theresanaiforthat.com/submit/", type:"manual", action:"Visit and submit" },
      { name:"SaaSHub", url:"https://www.saashub.com/submit-software", type:"form", action:"Submit software" },
      { name:"ProductHunt", url:"https://www.producthunt.com/posts/new", type:"manual", action:"Launch product" },
      { name:"IndieHackers", url:"https://www.indiehackers.com/products/new", type:"manual", action:"List product" },
      { name:"GitHub README", url:"https://github.com/julienalexandreoud-coder/calctowork", type:"manual", action:"Ensure do-follow backlink in README" },
      { name:"Reddit", url:"https://www.reddit.com/r/InternetIsBeautiful/submit?url="+encodeURIComponent(SITE_URL), type:"manual", action:"Post to Reddit" },
      { name:"HackerNews", url:"https://news.ycombinator.com/submitlink?u="+encodeURIComponent(SITE_URL), type:"manual", action:"Show HN submission" },
    ];

    for (const dir of directories) {
      try {
        if (dir.type === "profile") {
          const r = await fetch(dir.url, { timeout: 15000, headers: {"User-Agent": ua} });
          results.push({ name:dir.name, status: r.ok?"exists":"not_found", code:r.status });
        } else {
          results.push({ name:dir.name, status:"manual", action:dir.action, url:dir.url });
        }
      } catch(e) { results.push({ name:dir.name, status:"error", error:e.message }); }
    }

    // AI-powered opportunity finder
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;

    let opportunities = [];
    if (apiKey) {
      try {
        // Seed the AI with real top queries so prospects are relevant
        let topQueries = [];
        try {
          const cutoff = new Date(Date.now() - 30 * 86400000).toISOString().slice(0, 10);
          const qSnap = await db.collection("gsc_search_data").where("date", ">=", cutoff).orderBy("date", "desc").limit(400).get();
          const qMap = {};
          qSnap.forEach(d => { const q = d.data().query || ""; qMap[q] = (qMap[q] || 0) + (d.data().impressions || 0); });
          topQueries = Object.entries(qMap).sort((a, b) => b[1] - a[1]).slice(0, 12).map(([q]) => q);
        } catch (e) {}

        const searchPrompt = `Find 15 realistic backlink opportunities for calcto.work — a free calculator website with 460+ calculators in 6 languages (construction, finance, health, math, science, everyday tools). ${topQueries.length ? "Its top search queries are: " + topQueries.join(", ") + "." : ""}
Focus on: niche directories, resource/links pages on .edu or trade sites, forums where linking a calculator genuinely helps (contractor forums, personal-finance forums, teacher resource lists), tool aggregators, and guest-post targets. No spam tactics.
Return ONLY JSON: {"opportunities":[{"site":"Site name","url":"https://...","type":"directory|resource_page|guest_post|forum|aggregator","difficulty":"easy|medium|hard","action":"specific action to take","estimated_da":30,"relevant_calc":"which calculator/category to pitch"}]}`;
        const text = await _callAIRaw(apiKey, provider, provCfg.model, searchPrompt, 3000);
        if (text) { const m = text.match(/\{[\s\S]*\}/); if (m) try { opportunities = JSON.parse(m[0]).opportunities||[]; } catch(e) {} }
      } catch(e) {}
    }

    // Upsert everything into the backlink_prospects tracker (deduped by domain)
    let newProspects = 0;
    const upsert = async (p) => {
      try {
        let domain;
        try { domain = new URL(p.url).hostname.replace(/^www\./, ""); } catch (e) { return; }
        const docId = domain.replace(/[\/\.\#\$\[\]]/g, "_");
        const ref = db.collection("backlink_prospects").doc(docId);
        const existing = await ref.get();
        if (existing.exists) return; // keep user's status/notes
        await ref.set({
          site: p.site || domain,
          url: p.url,
          domain,
          type: p.type || "directory",
          difficulty: p.difficulty || "medium",
          action: p.action || "",
          estimated_da: p.estimated_da || null,
          relevant_calc: p.relevant_calc || "",
          status: "todo", // todo → submitted → live | rejected
          notes: "",
          created_at: admin.firestore.FieldValue.serverTimestamp(),
        });
        newProspects++;
      } catch (e) {}
    };
    for (const dir of directories) await upsert({ site: dir.name, url: dir.url, type: "directory", action: dir.action, difficulty: "easy" });
    for (const opp of opportunities) await upsert(opp);

    await db.collection("admin_prefs").doc("backlink_opportunities").set({
      opportunities, directories_submitted: results,
      last_checked: admin.firestore.FieldValue.serverTimestamp(),
    });

    return res.status(200).json({
      directories: results,
      opportunities_found: opportunities.length,
      new_prospects: newProspects,
      opportunities: opportunities.slice(0, 15),
    });
  } catch(e) {
    return res.status(500).json({ error: e.message });
  }
});

// ═══════════════════════════════════════════════════════════
//  AI STRATEGY BRAIN — Plan → Review → Replan + Long Memory
// ═══════════════════════════════════════════════════════════

exports.generateStrategyPlanHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key" });

    const siteUrl = functions.config().gsc?.site_url || "sc-domain:calcto.work";
    const cutoff7 = new Date(Date.now() - 7*86400000).toISOString().slice(0,10);
    let gsc = { clicks:0, impressions:0 };
    try { const s = await db.collection("gsc_site_stats").where("site_url","==",siteUrl).where("date",">=",cutoff7).orderBy("date","desc").limit(7).get(); s.forEach(d => { gsc.clicks+=d.data().total_clicks||0; gsc.impressions+=d.data().total_impressions||0; }); } catch(e) {}

    const [stratDoc, learnDoc, memDoc, prevPlansSnap] = await Promise.all([
      db.collection("ai_brain").doc("strategy").get(),
      db.collection("ai_brain").doc("learnings").get(),
      db.collection("ai_brain").doc("memory").get(),
      db.collection("ai_brain").doc("plans").get(),
    ]);
    const learnings = learnDoc.exists ? learnDoc.data() : {};
    const memory = memDoc.exists ? memDoc.data() : { timeline:[], insights:[] };
    const prevPlans = prevPlansSnap.exists ? (prevPlansSnap.data().plans||[]) : [];

    const prompt = `Create a 2-week strategic plan for CalcToWork (461 calcs, 19k pages, 6 langs, zero backlinks). Current: ${gsc.clicks} clicks, ${gsc.impressions} impressions (7 days). What works: ${JSON.stringify((learnings.what_works||[]).slice(0,3))}. What doesn't: ${JSON.stringify((learnings.what_doesnt||[]).slice(0,3))}. Past plans: ${prevPlans.slice(-2).map(p=>p.headline).join('; ')}. Return JSON: {"week":"W29","headline":"...","big_goal":"...","metrics_target":{"daily_clicks":30},"phases":[{"phase":1,"focus":"...","actions":["..."],"success_criteria":"..."}],"risks":["..."],"long_term_vision":"..."}`;
    const text = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 2500);
    if (!text) return res.status(500).json({ error: "AI failed" });
    const m = text.match(/\{[\s\S]*\}/);
    if (!m) return res.status(500).json({ error: "No JSON" });
    const plan = JSON.parse(m[0]);

    await Promise.all([
      db.collection("ai_brain").doc("strategy").set({ current_plan:plan, focus_areas:(plan.phases||[]).map(p=>p.focus), updated_at:admin.firestore.FieldValue.serverTimestamp() },{merge:true}),
      (async()=>{ const d=prevPlansSnap.exists?prevPlansSnap.data():{plans:[]}; d.plans=[...(d.plans||[]),{...plan,created_at:new Date().toISOString(),status:"active"}]; await db.collection("ai_brain").doc("plans").set(d,{merge:true}); })(),
      (async()=>{ const d=memDoc.exists?memDoc.data():{timeline:[],insights:[]}; d.timeline=[...d.timeline||[],{date:new Date().toISOString(),event:"Plan created",headline:plan.headline}].slice(-50); await db.collection("ai_brain").doc("memory").set(d,{merge:true}); })(),
    ]);
    return res.status(200).json(plan);
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

exports.reviewStrategyPlanHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  try {
    const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgDoc.exists ? cfgDoc.data() : {};
    const provider = cfg.active_provider || "deepseek";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key;
    if (!apiKey) return res.status(500).json({ error: "No AI key" });

    const [stratDoc, plansDoc, memDoc, actionsSnap] = await Promise.all([
      db.collection("ai_brain").doc("strategy").get(),
      db.collection("ai_brain").doc("plans").get(),
      db.collection("ai_brain").doc("memory").get(),
      db.collection("autonomous_actions").orderBy("created_at","desc").limit(20).get().catch(()=>({empty:true})),
    ]);
    const currentPlan = stratDoc.exists ? stratDoc.data().current_plan : null;
    const memory = memDoc.exists ? memDoc.data() : { timeline:[], insights:[] };
    const actions = []; if (!actionsSnap.empty) actionsSnap.forEach(d => actions.push({ type:d.data().type, status:d.data().status, result:d.data().result }));

    const siteUrl = functions.config().gsc?.site_url || "sc-domain:calcto.work";
    const cutoff7 = new Date(Date.now() - 7*86400000).toISOString().slice(0,10);
    let gsc = { clicks:0, impressions:0 };
    try { const s = await db.collection("gsc_site_stats").where("site_url","==",siteUrl).where("date",">=",cutoff7).orderBy("date","desc").limit(7).get(); s.forEach(d => { gsc.clicks+=d.data().total_clicks||0; gsc.impressions+=d.data().total_impressions||0; }); } catch(e) {}

    const prompt = `Review progress for CalcToWork. Plan: ${currentPlan?JSON.stringify(currentPlan.headline):'none'}. Actions: ${JSON.stringify(actions.slice(0,10))}. Metrics: ${gsc.clicks} clicks, ${gsc.impressions} impressions. Timeline: ${JSON.stringify((memory.timeline||[]).slice(-8))}. Return JSON: {"plan_status":"on_track|behind","what_worked":["..."],"what_didnt":["..."],"surprises":["..."],"adjustments":["..."],"new_learnings":{"what_works":["..."],"what_doesnt":["..."],"site_patterns":["..."]},"confidence":5,"summary":"one paragraph"}`;
    const text = await _callAIRaw(apiKey, provider, provCfg.model, prompt, 2000);
    if (!text) return res.status(500).json({ error: "AI failed" });
    const m = text.match(/\{[\s\S]*\}/);
    if (!m) return res.status(500).json({ error: "No JSON" });
    const review = JSON.parse(m[0]);

    const memData = memDoc.exists ? memDoc.data() : { timeline:[], insights:[] };
    memData.timeline = [...memData.timeline||[], { date:new Date().toISOString(), event:"Strategy reviewed", summary:review.summary }].slice(-50);
    if (review.new_learnings) {
      const lDoc = await db.collection("ai_brain").doc("learnings").get();
      const lData = lDoc.exists ? lDoc.data() : {};
      lData.what_works = [...new Set([...(lData.what_works||[]), ...(review.new_learnings.what_works||[])])].slice(0,15);
      lData.what_doesnt = [...new Set([...(lData.what_doesnt||[]), ...(review.new_learnings.what_doesnt||[])])].slice(0,15);
      lData.site_patterns = [...new Set([...(lData.site_patterns||[]), ...(review.new_learnings.site_patterns||[])])].slice(0,15);
      await db.collection("ai_brain").doc("learnings").set(lData, { merge: true });
    }
    memData.insights = [...new Set([review.summary, ...(memData.insights||[])])].slice(-20);
    await db.collection("ai_brain").doc("memory").set(memData, { merge: true });

    if (currentPlan) {
      const plansData = plansDoc.exists ? plansDoc.data() : { plans:[] };
      if (plansData.plans?.length > 0) { const last = plansData.plans[plansData.plans.length-1]; last.reviewed_at=new Date().toISOString(); last.review=review; last.status=review.plan_status==="on_track"?"active":"needs_adjustment"; await db.collection("ai_brain").doc("plans").set(plansData,{merge:true}); }
    }
    return res.status(200).json(review);
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

exports.getStrategyMemoryHttp = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method !== "GET") return res.status(405).json({ error: "GET only" });
  try {
    const [stratDoc, learnDoc, plansDoc, memDoc] = await Promise.all([
      db.collection("ai_brain").doc("strategy").get(),
      db.collection("ai_brain").doc("learnings").get(),
      db.collection("ai_brain").doc("plans").get(),
      db.collection("ai_brain").doc("memory").get(),
    ]);
    return res.status(200).json({
      strategy: stratDoc.exists ? stratDoc.data() : {},
      learnings: learnDoc.exists ? learnDoc.data() : {},
      plans: plansDoc.exists ? (plansDoc.data().plans||[]).slice(-5) : [],
      memory: memDoc.exists ? memDoc.data() : { timeline:[], insights:[] },
    });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

exports.saveStrategyMemoryHttp = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const { insight, event } = req.body || {};
    const memDoc = await db.collection("ai_brain").doc("memory").get();
    const memData = memDoc.exists ? memDoc.data() : { timeline:[], insights:[] };
    if (insight) memData.insights = [...new Set([insight, ...memData.insights||[]])].slice(-30);
    if (event) memData.timeline = [{ date:new Date().toISOString(), event }, ...memData.timeline||[]].slice(-50);
    await db.collection("ai_brain").doc("memory").set(memData, { merge: true });
    return res.status(200).json({ status:"ok" });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

// ══ Quality Audit — score all calcs, unpublish bad ones ══
exports.auditCalcQualityHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");

  try {
    const { autoFix, threshold } = req.body || {};
    const minScore = threshold || 80;
    const snap = await db.collection("calc_cms").limit(500).get();
    const results = { scored:0, passed:0, failed:0, unpublished:0, details:[] };

    for (const doc of snap.docs) {
      const data = doc.data();
      if (data.type === "static") continue; // skip synced static calcs
      const q = _scoreCalcQuality(data);
      results.scored++;

      if (q.score >= minScore) {
        results.passed++;
      } else {
        results.failed++;
        results.details.push({ slug:doc.id, score:q.score, issues:q.issues });
        if (autoFix && data.status === "published") {
          await doc.ref.set({ status:"draft", quality_score:q.score, quality_issues:q.issues, updated_at:admin.firestore.FieldValue.serverTimestamp() }, { merge: true });
          results.unpublished++;
        }
      }
    }

    return res.status(200).json({
      ...results,
      summary: autoFix ? `Unpublished ${results.unpublished} failed calcs` : `${results.failed} calcs need review. Set autoFix:true to unpublish them.`,
      top_issues: results.details.slice(0, 15),
    });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

// ══ PER-CALCULATOR BACKLINK GENERATOR ══
// Remove junk/empty calc docs (test rows, drafts with no real definition).
// SAFE BY DEFAULT: without {confirm:true} it only reports what it WOULD delete.
// When confirming, every doc is copied to `calc_cms_deleted_backup` first, so a
// deletion is always recoverable.
exports.cleanupJunkCalcsHttp = functions.runWith({ timeoutSeconds: 120, memory: "256MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const confirm = !!(req.body && req.body.confirm);
    const snap = await db.collection("calc_cms").get();
    const junk = [];
    snap.forEach(d => {
      const data = d.data();
      const en = (data.langs && data.langs.en) || {};
      const hasName = !!(en.name && en.name.trim());
      const formulaLen = (data.formula || "").length;
      const inputsLen = (data.inputs || []).length;
      const article = (en.long_content || "").length;
      // Junk = no real definition: needs a name AND (a usable formula OR inputs)
      // AND some content. Anything with real substance is never touched.
      const isJunk = (!hasName) || (formulaLen < 5 && inputsLen === 0 && article < 200);
      if (isJunk) junk.push({ id: d.id, name: en.name || "(no name)", status: data.status || "?", formulaLen, inputsLen, article });
    });

    let deleted = 0;
    if (confirm) {
      for (const j of junk) {
        const ref = db.collection("calc_cms").doc(j.id);
        const cur = await ref.get();
        if (!cur.exists) continue;
        // back up before deleting
        await db.collection("calc_cms_deleted_backup").doc(j.id).set({
          ...cur.data(), _deleted_at: admin.firestore.FieldValue.serverTimestamp(), _deleted_by: "cleanupJunkCalcsHttp",
        });
        await ref.delete();
        deleted++;
      }
    }
    return res.status(200).json({
      dryRun: !confirm, junkCount: junk.length, deleted,
      junk: junk.slice(0, 50),
      note: confirm ? `Deleted ${deleted} junk docs (backed up to calc_cms_deleted_backup).` : "DRY RUN — nothing deleted. POST {confirm:true} to delete (with backup).",
    });
  } catch (e) { return res.status(500).json({ error: e.message }); }
});

// Deploy bundled static assets (JS/CSS) to hosting INCREMENTALLY via the shared
// manifest-cloning helper. This is the safe way to update /js/calculator.js etc.
// — a full `firebase deploy --only hosting` would revert the whole catalog to
// the stale local public/ build. Assets ship inside functions/assets/.
exports.deployAssetsHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const zlib = require("zlib"), util = require("util"), fs = require("fs"), path = require("path");
    const crypto = require("crypto");
    const gzip = util.promisify(zlib.gzip);
    const ASSETS = { "/js/calculator.js": "assets/calculator.js", "/js/analytics-tracker.js": "assets/analytics-tracker.js", "/css/styles.css": "assets/styles.css" };
    const files = {};
    for (const [hostPath, rel] of Object.entries(ASSETS)) {
      const full = path.join(__dirname, rel);
      if (!fs.existsSync(full)) continue;
      const gzipped = await gzip(fs.readFileSync(full));
      const hash = crypto.createHash("sha256").update(gzipped).digest("hex");
      files[hostPath] = { gzipped, hash };
    }
    if (!Object.keys(files).length) return res.status(400).json({ error: "No bundled assets found." });
    const result = await _deployPagesToHosting(files, "[Assets] deploy bundled JS/CSS");
    return res.status(200).json({ deployed: !result.error, paths: Object.keys(files), versionName: result.versionName || null, error: result.error || null });
  } catch (e) { return res.status(500).json({ error: e.message }); }
});

// deployAdminHttp — ships the admin dashboard (/admin.html) and the Page-1 Tracker
// dataset (/data/sd-tracker.json) to hosting via the safe incremental helper, WITHOUT
// a full `firebase deploy --only hosting` (which would clobber server-generated calc
// pages that aren't in local public/). Source of truth: functions/assets/*.
// patchCalcFormulaHttp — safely replace a broken calc formula. HARD GUARD: the new
// formula must parse AND compute valid (finite/valid) outputs for sample inputs before it
// is saved; otherwise it is REJECTED. Used to fix genuinely broken calcs (e.g. formulas
// whose //-comments got flattened and ate the return). POST { slug, formula }
exports.patchCalcFormulaHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const path = require("path"), fs = require("fs");
    const inSlug = (req.body && req.body.slug || "").trim();
    const formula = (req.body && req.body.formula || "").trim();
    // Optional: replace the input definitions too (e.g. turn a mislabelled number box
    // into a text or choice field). Ids must match the existing set — this endpoint
    // fixes a calc's shape, it does not redesign it.
    const newInputs = Array.isArray(req.body && req.body.inputs) ? req.body.inputs : null;
    const newOutputs = Array.isArray(req.body && req.body.outputs) ? req.body.outputs : null;
    // Optional: human labels for coded option values ({gender:{"0":"Male","1":"Female"}}),
    // written to every language so a dropdown never shows a bare code.
    const optionLabels = (req.body && req.body.option_labels && typeof req.body.option_labels === "object")
      ? req.body.option_labels : null;
    if (!inSlug || !formula) return res.status(400).json({ error: "slug and formula required" });
    if (/\/\/[^\n]/.test(formula) && !formula.includes("\n")) return res.status(400).json({ error: "Refusing: single-line formula with // comment (fragile). Use /* */ or newlines." });

    let index = [];
    try { const raw = require(path.join(__dirname, "calc-index.json")); index = Array.isArray(raw) ? raw : (raw.calcs || Object.values(raw)); } catch (e) {}
    const entry = index.find(e => e.slug === inSlug) || index.find(e => e.slugs && Object.values(e.slugs).includes(inSlug));
    const baseSlug = entry ? entry.slug : inSlug;
    const id = entry ? String(entry.id) : null;

    const docRef = db.collection("calc_cms").doc(baseSlug);
    const snap = await docRef.get();
    if (!snap.exists) return res.status(404).json({ error: "Calc not found: " + baseSlug });
    const doc = snap.data();

    // Gather inputs/outputs to validate against, using the SAME precedence the renderer
    // uses (calc_cms first, static only to fill gaps). Preferring static here meant that
    // when the two disagreed we validated against a shape the live page never renders.
    let inputsArr = doc.inputs || [], outputsArr = doc.outputs || [], example = doc.example_inputs || null;
    if (id) { try { const cj = JSON.parse(fs.readFileSync(path.join(__dirname, "calcs", id, "calc.json"), "utf8")); if (!inputsArr.length && (cj.inputs || []).length) inputsArr = cj.inputs; if (!outputsArr.length && (cj.outputs || []).length) outputsArr = cj.outputs; example = example || cj.example_inputs; } catch (e) {} }
    if (newOutputs) {
      if (!newOutputs.every(o => o && o.id)) return res.status(400).json({ error: "outputs[] entries need ids" });
      outputsArr = newOutputs;
    }
    const outIds = outputsArr.map(o => o.id).filter(Boolean);
    if (!outIds.length) return res.status(400).json({ error: "No outputs to validate against" });

    if (newInputs) {
      const oldIds = inputsArr.map(i => i.id).sort().join(",");
      const gotIds = newInputs.map(i => i && i.id).filter(Boolean).sort().join(",");
      if (!gotIds) return res.status(400).json({ error: "inputs[] entries need ids" });
      const allowNew = !!(req.body && req.body.allow_new_inputs);
      if (oldIds && gotIds !== oldIds && !allowNew) {
        return res.status(400).json({ error: `inputs[] ids must match the existing set. have: ${oldIds} | got: ${gotIds} (pass allow_new_inputs:true to change the field set on purpose)` });
      }
      if (allowNew && oldIds) {
        // Adding fields is fine; silently DROPPING one would break saved links and
        // anything that references it, so require the existing ids to survive.
        const gone = oldIds.split(",").filter(id => id && !newInputs.some(i => i.id === id));
        if (gone.length) return res.status(400).json({ error: "allow_new_inputs may add fields but not remove: " + gone.join(",") });
      }
      inputsArr = newInputs;
      example = null;   // an old example keyed to the old shape would mask a broken one
    }

    // HARD GUARD: parse + compute must yield valid outputs.
    let fn; try { fn = new Function("inputs", '"use strict";' + formula); } catch (e) { return res.status(422).json({ error: "Formula syntax error: " + e.message }); }
    const validOut = v => v !== undefined && v !== null && !(typeof v === "number" && !isFinite(v));
    const si = {}; inputsArr.forEach(i => { si[i.id] = (i.default != null) ? i.default : (i.options && i.options[0] != null ? (i.options[0].value != null ? i.options[0].value : i.options[0]) : (typeof i.min === "number" ? (i.min > 0 ? i.min : 1) : 1)); });
    if (example) Object.assign(si, example);
    let r; try { r = fn(si); } catch (e) { return res.status(422).json({ error: "Formula threw: " + e.message, sampleInputs: si }); }
    if (!r || r.error || !outIds.every(x => validOut(r[x]))) return res.status(422).json({ error: "Formula does not produce valid outputs for sample inputs — NOT saved", result: r, sampleInputs: si });

    const writePatch = { formula };
    if (newInputs) writePatch.inputs = inputsArr;
    if (newOutputs) writePatch.outputs = outputsArr;
    // Optional: per-language input/output labels, e.g. to replace a Spanish id that was
    // being humanized onto the English page ("Peso est kg").
    // POST { labels: { en: { inputs: {...}, outputs: {...} }, ... } }
    const labelPatch = (req.body && req.body.labels && typeof req.body.labels === "object") ? req.body.labels : null;
    if (labelPatch) {
      const lp = {};
      for (const [l, v] of Object.entries(labelPatch)) {
        if (!LANGS.includes(l) || !v || typeof v !== "object") continue;
        const e = {};
        if (v.inputs && typeof v.inputs === "object") e.inputs_labels = v.inputs;
        if (v.outputs && typeof v.outputs === "object") e.outputs_labels = v.outputs;
        // name feeds the <h1> and the SEO <title>, so it is the highest-value string
        // on the page — repairable here when a generation pass corrupted it.
        if (typeof v.name === "string" && v.name.trim()) e.name = v.name.trim();
        if (typeof v.desc === "string" && v.desc.trim()) e.desc = v.desc.trim();
        if (Object.keys(e).length) lp[l] = e;
      }
      if (Object.keys(lp).length) writePatch.langs = lp;
    }
    if (optionLabels) {
      // English gets the labels as given; the other languages inherit them until a
      // translation pass replaces them — a readable English word still beats "0".
      // Merge rather than assign: `labels` above may already have set writePatch.langs.
      writePatch.langs = writePatch.langs || {};
      for (const l of LANGS) writePatch.langs[l] = { ...(writePatch.langs[l] || {}), option_labels: optionLabels };
    }
    await docRef.set(writePatch, { merge: true });
    let deployed = false;
    if (doc.status === "published") {
      const s2 = await docRef.get();
      const files = await _buildCalcFiles(baseSlug, s2.data());
      if (Object.keys(files).length) { const dr = await _deployPagesToHosting(files, `[FormulaFix] ${baseSlug}`); deployed = !dr.error; }
    }
    return res.status(200).json({ saved: true, slug: baseSlug, computeOk: true, result: r, deployed });
  } catch (e) { console.error("patchCalcFormulaHttp error:", e); return res.status(500).json({ error: e.message }); }
});

/**
 * regenPresetsHttp — replace meaningless example presets ("Small/Medium/Large",
 * "Caso 1..5", all-zero rows, rows that make the formula divide by zero) with named
 * real-world scenarios, and give inputs sensible defaults so the page never loads blank.
 *
 * HARD GUARD, same contract as patchCalcFormulaHttp: nothing is written unless every
 * generated scenario actually computes valid outputs through the calc's own formula.
 * A calc whose presets can't be validated is left exactly as it was and reported.
 *
 * POST { slug, republish?:bool, want?:number, fixDefaults?:bool, force?:bool }
 */
exports.regenPresetsHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const path = require("path"), fs = require("fs");
    const b = req.body || {};
    const inSlug = String(b.slug || "").trim();
    if (!inSlug) return res.status(400).json({ error: "slug required" });
    const want = Math.min(6, Math.max(3, Number(b.want) || 4));
    const republish = b.republish !== false;
    const fixDefaults = b.fixDefaults !== false;

    let index = [];
    try { const raw = require(path.join(__dirname, "calc-index.json")); index = Array.isArray(raw) ? raw : (raw.calcs || Object.values(raw)); } catch (e) {}
    const entry = index.find(e => e.slug === inSlug) || index.find(e => e.slugs && Object.values(e.slugs).includes(inSlug));
    const baseSlug = entry ? entry.slug : inSlug;
    const id = entry ? String(entry.id) : null;

    const docRef = db.collection("calc_cms").doc(baseSlug);
    const snap = await docRef.get();
    if (!snap.exists) return res.status(404).json({ error: "Calc not found: " + baseSlug });
    const doc = snap.data();

    // ── gather the calc's real shape (CMS wins, static fills gaps) ──
    let inputsArr = (doc.inputs || []).length ? doc.inputs : [];
    let outputsArr = (doc.outputs || []).length ? doc.outputs : [];
    let formula = doc.formula && doc.formula.length > 10 ? doc.formula : "";
    let staticLang = null;
    if (id) {
      try {
        const cj = JSON.parse(fs.readFileSync(path.join(__dirname, "calcs", id, "calc.json"), "utf8"));
        if (!inputsArr.length && (cj.inputs || []).length) inputsArr = cj.inputs;
        if (!outputsArr.length && (cj.outputs || []).length) outputsArr = cj.outputs;
        if (!formula) formula = cj.formula || "";
      } catch (e) {}
      try { staticLang = JSON.parse(fs.readFileSync(path.join(__dirname, "calcs", id, "en.json"), "utf8")); } catch (e) {}
    }
    if (!inputsArr.length) return res.status(400).json({ error: "Calc has no inputs" });
    if (!formula) return res.status(400).json({ error: "Calc has no formula" });
    const outIds = outputsArr.map(o => o.id).filter(Boolean);
    if (!outIds.length) return res.status(400).json({ error: "Calc has no outputs" });

    let fn;
    try { fn = new Function("inputs", '"use strict";' + formula); }
    catch (e) { return res.status(422).json({ error: "Existing formula does not parse: " + e.message }); }

    const enLang = (doc.langs && doc.langs.en) || {};
    const inLabels = Object.assign({}, (staticLang && staticLang.inputs) || {}, enLang.inputs_labels || {});
    const outLabels = Object.assign({}, (staticLang && staticLang.outputs) || {}, enLang.outputs_labels || {});
    const name = enLang.name || doc.name_en || doc.name || baseSlug;
    const desc = enLang.desc || doc.desc_en || "";

    const optsOf = i => i.options || i.choices || (Array.isArray(i.unit_options) && i.type !== "number" ? i.unit_options : null);
    const optVals = i => { const o = optsOf(i); return o ? o.map(x => (x && x.value !== undefined ? x.value : x)) : null; };

    // ── describe the inputs to the model precisely enough to get usable values ──
    const inLines = inputsArr.map(i => {
      const ov = optVals(i);
      const bits = [`id "${i.id}"`, `label "${inLabels[i.id] || humanizeId(i.id)}"`];
      if (i.unit) bits.push(`unit ${i.unit}`);
      if (ov) {
        // Show what each coded value MEANS, or the model answers "male" for a field
        // whose only legal values are 0 and 1 and every scenario gets rejected.
        const om = ((enLang.option_labels || {})[i.id]) || null;
        bits.push(`CHOICE, use exactly one of these values: ${
          om ? ov.map(o => `${JSON.stringify(String(o))} (means "${om[String(o)] || o}")`).join(", ") : JSON.stringify(ov)}`);
      }
      else if (i.type === "date") bits.push('DATE — give a calendar date as a "YYYY-MM-DD" string, never a number');
      else if (i.type === "text" || i.type === "string") bits.push(`TEXT — give a string${i.placeholder ? ` in the style of: ${i.placeholder}` : ""}, never a bare number`);
      else {
        if (typeof i.min === "number") bits.push(`min ${i.min}`);
        if (typeof i.max === "number") bits.push(`max ${i.max}`);
        bits.push("numeric");
      }
      return "- " + bits.join(", ");
    }).join("\n");
    const outLine = outIds.map(o => `"${outLabels[o] || o}"`).join(", ");

    const prompt = `You are preparing the "common examples" table for an online calculator.

Calculator: "${name}"
${desc ? `What it does: ${desc}\n` : ""}It computes: ${outLine}

Its inputs:
${inLines}

Produce ${want} DISTINCT, realistic scenarios that a real user of this calculator would recognise.

Rules — these matter:
1. Each scenario needs a SPECIFIC, self-explanatory name describing the real situation, in English, 2-5 words. Good: "Lemon juice", "Family bathroom", "30-year fixed mortgage", "Adult male, moderate activity". FORBIDDEN: "Small", "Medium", "Large", "X-Large", "Case 1", "Example 2", "Option A", or any size tier or bare number.
2. Give a value for EVERY input id listed above. Never omit one. Never use 0 unless 0 is genuinely meaningful for that field (it almost never is — a concentration, length, price or count of 0 makes the calculation meaningless).
3. Numbers must be plain JSON numbers within the stated min/max. Choice inputs must use one of the exact allowed values.
4. The ${want} scenarios must have genuinely different values and span the realistic range — not the same number repeated.
5. Values must be physically/financially plausible for the named scenario, so the computed result is correct and useful.

Also give "defaults": the single most typical set of values to pre-fill the calculator with on page load (same rules — every input id, no zeros).

Return ONLY JSON:
{"scenarios":[{"label":"...","values":{${inputsArr.slice(0, 3).map(i => `"${i.id}":<v>`).join(",")}${inputsArr.length > 3 ? ",..." : ""}}}],"defaults":{${inputsArr.slice(0, 3).map(i => `"${i.id}":<v>`).join(",")}${inputsArr.length > 3 ? ",..." : ""}}}`;

    // ── AI plumbing (same provider config as the other endpoints) ──
    const cfgSnap = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgSnap.exists ? cfgSnap.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key || (functions.config().anthropic && functions.config().anthropic.key);
    if (!apiKey) return res.status(500).json({ error: `No API key for provider ${provider}` });
    async function ai(p, maxTokens) {
      let t;
      if (provider === "anthropic" || !cfg.active_provider) {
        const r = await fetch("https://api.anthropic.com/v1/messages", {
          method: "POST",
          headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
          body: JSON.stringify({ model: provCfg.model || "claude-haiku-4-5-20251001", max_tokens: maxTokens, messages: [{ role: "user", content: p }] }),
        });
        if (!r.ok) throw new Error("AI error: " + await r.text());
        const d = await r.json(); t = d.content && d.content[0] && d.content[0].text;
      } else {
        const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
        const model = provCfg.model || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini");
        const r = await fetch(`${baseUrl}/chat/completions`, {
          method: "POST",
          headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
          body: JSON.stringify({ model, messages: [{ role: "user", content: p }], max_tokens: maxTokens }),
        });
        if (!r.ok) throw new Error("AI error: " + await r.text());
        const d = await r.json(); t = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
      }
      const mm = t && t.match(/\{[\s\S]*\}/);
      if (!mm) throw new Error("No JSON in AI response");
      return JSON.parse(mm[0]);
    }

    // ── validation: coerce to the input's declared domain, then actually compute ──
    const BAD_LABEL = /^\s*(x{0,2}[\s-]*(small|medium|large|extra[\s-]?large|tiny|huge)|(case|caso|example|ejemplo|option|opci[oó]n|scenario)\s*\d+|[a-z]|\d+)\s*$/i;
    const validOut = v => v !== undefined && v !== null && !(typeof v === "number" && !isFinite(v));
    function coerce(vals) {
      const out = {};
      for (const i of inputsArr) {
        let v = vals[i.id];
        if (v === undefined || v === null || v === "") return null;      // must cover every input
        const ov = optVals(i);
        if (ov) {
          const hit = ov.find(o => String(o) === String(v));
          if (hit === undefined) return null;                            // invalid choice
          out[i.id] = hit;
        } else if (i.type === "date") {
          // A date field must get a real calendar date. Without this check a model
          // answering 2005 for "birth date" passes as a finite number and the preset
          // silently means 1970-01-01T00:00:02.
          const s = String(v).trim();
          if (!/^\d{4}-\d{2}-\d{2}$/.test(s) || isNaN(new Date(s).getTime())) return null;
          out[i.id] = s;
        } else if (i.type === "text" || i.type === "string") {
          const s = String(v).trim();
          if (!s || /^-?\d+(\.\d+)?$/.test(s)) return null;               // a bare number is not text
          out[i.id] = s;
        } else {
          // Accept "3.5%", "1,200", "28 days" — the number is right, only the wrapping
          // is chatty, and rejecting those wastes a whole generation round.
          const n = typeof v === "number" ? v
            : Number(String(v).replace(/[\s%]/g, "").replace(/,(?=\d{3}\b)/g, "").replace(/[^\d.eE+-].*$/, ""));
          if (!isFinite(n)) return null;
          if (typeof i.min === "number" && n < i.min) return null;
          if (typeof i.max === "number" && n > i.max) return null;
          out[i.id] = n;
        }
      }
      return out;
    }
    function computes(vals) {
      let r; try { r = fn(vals); } catch (e) { return false; }
      return !!(r && typeof r === "object" && !r.error && outIds.every(k => validOut(r[k])));
    }

    // Two attempts: the retry tells the model exactly which scenarios failed and why.
    let scenarios = [], defaults = null, lastErr = null;
    for (let attempt = 0; attempt < 2 && scenarios.length < 3; attempt++) {
      let gen;
      try { gen = await ai(attempt === 0 ? prompt : prompt + `\n\nYour previous answer was rejected: ${lastErr}. Fix it — every input id present, values inside min/max, no zeros, no size-tier or numbered labels.`, 2500); }
      catch (e) { lastErr = e.message; continue; }

      const kept = [], rejected = [];
      for (const s of (gen.scenarios || [])) {
        const label = String(s.label || "").trim();
        if (!label || BAD_LABEL.test(label)) { rejected.push(`"${label}" is a forbidden generic label`); continue; }
        const vals = coerce(s.values || {});
        if (!vals) { rejected.push(`"${label}" has a missing/out-of-range value`); continue; }
        if (!computes(vals)) { rejected.push(`"${label}" does not compute a valid result`); continue; }
        if (kept.some(k => JSON.stringify(k.inputs) === JSON.stringify(vals))) { rejected.push(`"${label}" duplicates another scenario`); continue; }
        kept.push({ label, inputs: vals });
      }
      const d = coerce(gen.defaults || {});
      if (d && computes(d)) defaults = d;
      else if (kept.length) defaults = kept[0].inputs;                    // fall back to a verified scenario

      if (kept.length >= 3) { scenarios = kept; break; }
      scenarios = kept.length > scenarios.length ? kept : scenarios;
      lastErr = rejected.slice(0, 4).join("; ") || "too few usable scenarios";
    }

    if (scenarios.length < 3) {
      return res.status(422).json({ error: "Could not generate validated presets — nothing written", slug: baseSlug, got: scenarios.length, detail: lastErr });
    }
    // Refuse a set that is uniform in every field: that is the bug we're fixing.
    if (new Set(scenarios.map(s => JSON.stringify(s.inputs))).size === 1) {
      return res.status(422).json({ error: "All generated scenarios identical — nothing written", slug: baseSlug });
    }

    // ── translate the labels ──
    // The renderer localizes generic tiers ("Small") on its own, but these new labels are
    // specific prose, so each language needs its own copy in langs[lang].preset_labels
    // (an array positionally matching comparison_presets). Without this the ES/FR/DE/IT/PT
    // pages would show English scenario names.
    const OTHER = ["es", "fr", "de", "it", "pt"];
    const enLabels = scenarios.map(s => s.label);
    const langsPatch = { en: { preset_labels: enLabels } };
    try {
      const tr = await ai(`Translate each of these short calculator example-scenario names into Spanish, French, German, Italian and Portuguese.
They label rows in the "common examples" table of a calculator called "${name}".
Keep them short and natural in each language — how a native speaker would name that situation, not a literal word-for-word translation. Preserve the order exactly.

Names: ${JSON.stringify(enLabels)}

Return ONLY JSON with one array of ${enLabels.length} strings per language:
{"es":[...],"fr":[...],"de":[...],"it":[...],"pt":[...]}`, 1500);
      for (const l of OTHER) {
        const arr = tr[l];
        if (Array.isArray(arr) && arr.length === enLabels.length && arr.every(x => x && typeof x === "string")) {
          langsPatch[l] = { preset_labels: arr.map(String) };
        }
      }
    } catch (e) { /* translation is best-effort; English labels still beat "Small/Medium/Large" */ }

    // ── write ──
    // Nested maps (not dotted keys — set/merge would treat "langs.en.x" as a literal
    // field name). set with merge:true merges nested maps recursively, so the other
    // fields under langs.<l> survive.
    const patch = { comparison_presets: scenarios, langs: langsPatch };
    let defaultsWritten = 0;
    if (fixDefaults && defaults) {
      const hadDefaults = inputsArr.some(i => i.default !== undefined && i.default !== null && i.default !== "");
      if (!hadDefaults || b.force) {
        // Write the FULL inputs array (CMS inputs replace static wholesale, so a
        // partial write would drop min/max/units).
        patch.inputs = inputsArr.map(i => ({ ...i, default: defaults[i.id] !== undefined ? defaults[i.id] : i.default }));
        defaultsWritten = Object.keys(defaults).length;
      }
    }
    await docRef.set(patch, { merge: true });

    let deployed = false;
    if (republish && doc.status === "published") {
      const s2 = await docRef.get();
      const files = await _buildCalcFiles(baseSlug, s2.data());
      if (Object.keys(files).length) { const dr = await _deployPagesToHosting(files, `[Presets] ${baseSlug}`); deployed = !dr.error; }
    }
    return res.status(200).json({
      ok: true, slug: baseSlug, presets: scenarios.length, defaultsWritten, deployed,
      langs: Object.keys(langsPatch).length, labels: scenarios.map(s => s.label),
    });
  } catch (e) { console.error("regenPresetsHttp error:", e); return res.status(500).json({ error: e.message }); }
});

exports.deployAdminHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const zlib = require("zlib"), util = require("util"), fs = require("fs"), path = require("path");
    const crypto = require("crypto");
    const gzip = util.promisify(zlib.gzip);
    const ASSETS = { "/admin.html": "assets/admin.html", "/data/sd-tracker.json": "assets/sd-tracker.json" };
    const files = {};
    for (const [hostPath, rel] of Object.entries(ASSETS)) {
      const full = path.join(__dirname, rel);
      if (!fs.existsSync(full)) continue;
      const gzipped = await gzip(fs.readFileSync(full));
      const hash = crypto.createHash("sha256").update(gzipped).digest("hex");
      files[hostPath] = { gzipped, hash };
    }
    if (!Object.keys(files).length) return res.status(400).json({ error: "No admin assets found in functions/assets/." });
    const result = await _deployPagesToHosting(files, "[Admin] deploy dashboard + tracker data");
    return res.status(200).json({ deployed: !result.error, paths: Object.keys(files), versionName: result.versionName || null, error: result.error || null });
  } catch (e) { return res.status(500).json({ error: e.message }); }
});

exports.perCalcBacklinkHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  try {
    const SITE_URL = "https://calcto.work";
    const fetch = require("node-fetch");
    const count = parseInt(req.query.count) || 10;
    const snap = await db.collection("calc_cms").where("status","==","published").limit(count).get();
    const calcs = [];
    snap.forEach(d => { const data = d.data(); calcs.push({ slug:d.id, name:(data.langs?.en?.name||data.name||d.id) }); });
    const results = [];

    const catMap = {
      "construction|estructuras|mamposteria|pavimentos|carpinteria|fontaneria|electricidad|climatizacion|gestion|pintura":"r/DIY,r/HomeImprovement,r/Construction",
      "matematicas":"r/learnmath,r/math","salud":"r/Fitness,r/loseit,r/health",
      "finanzas":"r/personalfinance,r/investing","ciencia|fisica|quimica":"r/Physics,r/askscience",
    };

    for (const calc of calcs.slice(0,5)) {
      const calcUrl = SITE_URL+"/en/"+calc.slug+"/";
      let subreddits = "r/InternetIsBeautiful";
      for (const [p,s] of Object.entries(catMap)) { if (new RegExp(p,"i").test(calc.slug)) { subreddits=s; break; } }
      results.push({
        slug:calc.slug, name:calc.name, url:calcUrl,
        embed_iframe: `<iframe src="${calcUrl}?embed=1" width="100%" height="600" frameborder="0" style="border:1px solid #ddd;border-radius:8px"></iframe><p style="text-align:center;font-size:11px">Powered by <a href="${calcUrl}">CalcToWork</a></p>`,
        embed_script: `<script src="${SITE_URL}/embed.js" data-calc="${calc.slug}"></script>`,
        submit_reddit: `https://www.reddit.com/submit?url=${encodeURIComponent(calcUrl)}&title=${encodeURIComponent(calc.name+' - Free Online Calculator')}`,
        subreddits,
        tip: `Embed creates backlink to THIS calculator. Share on ${subreddits}.`,
      });
    }

    await db.collection("admin_prefs").doc("per_calc_backlinks").set({
      generated:results.map(r=>r.slug), count:results.length,
      generated_at:admin.firestore.FieldValue.serverTimestamp(),
    },{merge:true});

    return res.status(200).json({ calculators:results, embed_script:SITE_URL+"/embed.js", strategy:"Each embed = backlink to that calculator page." });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

// ═══════════════════════════════════════════
//  AUTO BACKLINK ENGINE — 4 Techniques
// ═══════════════════════════════════════════
exports.autoBacklinkEngineHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  const fetch = require("node-fetch");
  const ua = "CalcToWork/1.0";
  const SITE_URL = "https://calcto.work";
  const report = { techniques: {}, summary: {} };

  try {
    const mode = req.query.mode || "all";
    const calcSlug = req.query.slug || "mass-concrete-calculator";
    const calcUrl = SITE_URL + "/en/" + calcSlug + "/";

    // ═══ TECHNIQUE 1: Profile Creator ═══
    if (mode === "all" || mode === "profiles") {
      console.log("[Backlink] Creating profiles...");
      const profiles = [
        { name:"GitHub", url:"https://github.com/julienalexandreoud-coder/calctowork", type:"existing", status:"exists", tip:"Add calcto.work link to repo description + README" },
        { name:"Dev.to", checkUrl:"https://dev.to/settings/profile", type:"manual", tip:"Add calcto.work to profile website field" },
        { name:"Hashnode", checkUrl:"https://hashnode.com/settings", type:"manual", tip:"Add calcto.work to blog profile" },
        { name:"Medium", checkUrl:"https://medium.com/me/settings", type:"manual", tip:"Add calcto.work to profile" },
        { name:"ProductHunt", checkUrl:"https://www.producthunt.com/settings", type:"manual", tip:"Add calcto.work to maker profile" },
        { name:"IndieHackers", checkUrl:"https://www.indiehackers.com/settings", type:"manual", tip:"Add calcto.work to product listing" },
        { name:"AlternativeTo", checkUrl:"https://alternativeto.net/settings/", type:"manual", tip:"List calcto.work as software" },
        { name:"CodePen", checkUrl:"https://codepen.io/settings/profile", type:"manual", tip:"Create pen with link to calcto.work" },
        { name:"Replit", checkUrl:"https://replit.com/", type:"manual", tip:"Create repl with calcto.work link" },
        { name:"StackOverflow", checkUrl:"https://stackoverflow.com/users/edit/", type:"manual", tip:"Add calcto.work to profile website" },
        { name:"Twitter/X", checkUrl:"https://x.com/settings/profile", type:"manual", tip:"Add calcto.work to bio/website" },
        { name:"LinkedIn", checkUrl:"https://www.linkedin.com/in/", type:"manual", tip:"Add calcto.work to contact info" },
        { name:"Reddit", checkUrl:"https://www.reddit.com/settings/profile", type:"manual", tip:"Mention in relevant subreddit comments" },
        { name:"HackerNews", checkUrl:"https://news.ycombinator.com/user?id=", type:"manual", tip:"Submit as Show HN post" },
        { name:"YouTube", checkUrl:"https://www.youtube.com/", type:"manual", tip:"Create calculator tutorial videos with link" },
      ];

      const profileResults = [];
      for (const p of profiles) {
        try {
          if (p.checkUrl) {
            const r = await fetch(p.checkUrl, { timeout:10000, headers:{"User-Agent":ua} }).catch(()=>null);
            profileResults.push({ ...p, accessible: !!r && r.status < 500 });
          } else {
            profileResults.push({ ...p, accessible: true });
          }
        } catch(e) { profileResults.push({ ...p, accessible:false }); }
      }
      report.techniques.profiles = { count: profileResults.length, results: profileResults };
    }

    // ═══ TECHNIQUE 2: Archive Submitter ═══
    if (mode === "all" || mode === "archive") {
      console.log("[Backlink] Archiving pages...");
      const pages = [
        SITE_URL, calcUrl,
        SITE_URL + "/en/concrete-slab-calculator/",
        SITE_URL + "/en/circle-area/",
        SITE_URL + "/en/pythagorean-theorem-calculator/",
        SITE_URL + "/es/calculadora-hormigon-masa/",
      ];

      const archiveResults = [];
      for (const page of pages) {
        const waybackUrl = "https://web.archive.org/save/" + page;
        const archiveTodayUrl = "https://archive.today/submit/?url=" + encodeURIComponent(page);
        try {
          const wb = await fetch(waybackUrl, { timeout:15000, headers:{"User-Agent":ua} }).catch(()=>null);
          archiveResults.push({ page, wayback: wb ? wb.status : "failed", wayback_url: waybackUrl });
        } catch(e) { archiveResults.push({ page, wayback:"error", wayback_url:waybackUrl }); }
      }
      report.techniques.archive = { submitted: archiveResults.length, results: archiveResults };
    }

    // ═══ TECHNIQUE 3: Broken Link Finder ═══
    if (mode === "all" || mode === "broken") {
      console.log("[Backlink] Finding broken links...");
      const targets = [
        "https://www.thisoldhouse.com/",
        "https://www.familyhandyman.com/",
        "https://www.bobvila.com/",
        "https://www.archtoolbox.com/",
        "https://www.engineersedge.com/",
      ];

      const brokenResults = [];
      for (const site of targets) {
        try {
          const r = await fetch(site, { timeout:15000, headers:{"User-Agent":ua} });
          if (r.ok) {
            brokenResults.push({ site, status:"live", tip:"Find resource pages with broken links. Suggest calcto.work as replacement." });
          } else {
            brokenResults.push({ site, status:"unreachable", code:r.status });
          }
        } catch(e) { brokenResults.push({ site, status:"error", error:e.message }); }
      }
      report.techniques.broken_links = { sites_checked: brokenResults.length, results: brokenResults };
    }

    // ═══ TECHNIQUE 4: Competitor Link Scraper ═══
    if (mode === "all" || mode === "competitor") {
      console.log("[Backlink] Analyzing competitor links...");
      const competitors = [
        { name:"OmniCalculator", site:"omnicalculator.com" },
        { name:"Calculator.net", site:"calculator.net" },
        { name:"GigaCalculator", site:"gigacalculator.com" },
      ];

      const compResults = [];
      for (const comp of competitors) {
        try {
          // Check if competitor is indexed and has backlinks we can replicate
          const r = await fetch(`https://${comp.site}/`, { timeout:15000, headers:{"User-Agent":ua} });
          compResults.push({
            name: comp.name,
            site: comp.site,
            accessible: r && r.ok,
            action: `Search Google for "link:${comp.site}" to find their backlinks. Then target the same sites with calcto.work.`,
            tip: `Check Ahrefs/Semrush free trial to export ${comp.name} backlinks, then replicate for calcto.work.`
          });
        } catch(e) { compResults.push({ name:comp.name, site:comp.site, accessible:false }); }
      }

      // AI suggestion for link building
      const cfgDoc = await db.collection("admin_prefs").doc("ai_config").get();
      const cfg = cfgDoc.exists ? cfgDoc.data() : {};
      const provider = cfg.active_provider || "deepseek";
      const provCfg = (cfg.providers || {})[provider] || {};
      const apiKey = provCfg.api_key;

      if (apiKey) {
        try {
          const aiPrompt = `List 10 specific websites where we can get free backlinks for calcto.work (free calculator site with 461 tools in 6 languages). Focus on construction, math, finance, health niches. For each, give the exact URL to submit to and the expected domain authority. Return JSON: {"opportunities":[{"site":"...","url":"...","type":"directory|profile|forum|resource","da":30,"action":"..."}]}`;
          const text = await _callAIRaw(apiKey, provider, provCfg.model, aiPrompt, 2000);
          if (text) { const m = text.match(/\{[\s\S]*\}/); if (m) try { report.techniques.competitor = { ...JSON.parse(m[0]), sources:compResults }; } catch(e){} }
        } catch(e) {}
      }
      if (!report.techniques.competitor) report.techniques.competitor = { sources:compResults };
    }

    report.summary = {
      profiles: report.techniques.profiles?.results?.filter(r=>r.type==="manual").length || 0,
      archived: report.techniques.archive?.submitted || 0,
      broken_sites: report.techniques.broken_links?.sites_checked || 0,
      competitors: report.techniques.competitor?.sources?.length || 0,
    };

    await db.collection("admin_prefs").doc("auto_backlink_report").set({
      report, timestamp: admin.firestore.FieldValue.serverTimestamp(),
    });

    return res.status(200).json(report);
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

/**
 * Daily backlink engine — archives pages + pings search engines at 7 AM UTC
 */
exports.dailyBacklinkEngine = functions.runWith({ timeoutSeconds: 300, memory: "256MB" })
  .pubsub.schedule("0 7 * * *").timeZone("UTC").onRun(async () => {
  const fetch = require("node-fetch");
  const ua = "CalcToWork/1.0";
  const SITE_URL = "https://calcto.work";
  let archived = 0;
  try {
    const pages = [SITE_URL, SITE_URL+"/en/mass-concrete-calculator/", SITE_URL+"/en/bmi-calculator/", SITE_URL+"/en/percentage-calculator/", SITE_URL+"/en/circle-area/"];
    for (const p of pages) {
      await fetch("https://web.archive.org/save/"+p, { timeout:15000, headers:{"User-Agent":ua} }).catch(()=>{});
      archived++;
    }
    const sm = encodeURIComponent(SITE_URL+"/sitemap.xml");
    await fetch(`https://www.google.com/ping?sitemap=${sm}`).catch(()=>{});
    console.log("[BacklinkDaily] Archived", archived, "pages + pinged sitemap");
  } catch(e) {}
  return { archived };
});

// ═══════════════════════════════════════════
//  CALCULATOR SCORECARD — simplified version
// ═══════════════════════════════════════════
exports.calcScorecardHttp = functions.runWith({ timeoutSeconds: 120, memory: "256MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");

  try {
    const snap = await db.collection("calc_cms").limit(500).get();
    const scorecard = [];
    const spanish = ['calculadora','hormigon','ladrillo','tabique','pintura','pared','techo','suelo','fontaneria','electricidad','carpinteria','mamposteria'];

    for (const doc of snap.docs) {
      const c = doc.data();
      const en = (c.langs?.en) || {};
      const name = en.name || c.name || doc.id;
      let score = 0;
      const checks = {};

      // SEO Title
      checks.title = !!(en.seo_title && en.seo_title.length >= 15);
      if (checks.title) score += 12;
      else if (en.seo_title) score += 5;

      // SEO Description
      checks.desc = !!(en.seo_description && en.seo_description.length >= 30);
      if (checks.desc) score += 10;
      else if (en.seo_description) score += 5;

      // Long-form article
      checks.article = !!(en.long_content && en.long_content.length > 500);
      if (checks.article) score += 15;

      // FAQ
      checks.faq = !!(en.faq && en.faq.length >= 2);
      if (checks.faq) score += 10;

      // Steps
      checks.steps = !!(en.steps && en.steps.filter(Boolean).length >= 3);
      if (checks.steps) score += 8;
      else if (en.steps?.filter(Boolean).length >= 1) score += 4;

      // Hreflang
      const totalLangs = ["en","es","fr","de","it","pt"].filter(l => (c.langs||{})[l]?.name).length;
      checks.languages = totalLangs;
      if (totalLangs >= 6) score += 10;
      else if (totalLangs >= 4) score += 7;
      else if (totalLangs >= 2) score += 4;

      // Spanglish detection
      checks.spanglish = spanish.some(w => (en.seo_title||'').toLowerCase().includes(w));
      if (checks.spanglish) score -= 5;

      // FAQ per language
      const faqLangs = ["en","es","fr","de","it","pt"].filter(l => ((c.langs||{})[l]?.faq||[]).length >= 2);
      checks.faq_languages = faqLangs.length;

      // Article per language
      const articleLangs = ["en","es","fr","de","it","pt"].filter(l => ((c.langs||{})[l]?.long_content||'').length > 500);
      checks.article_languages = articleLangs.length;

      score = Math.max(0, Math.min(100, score));
      const rating = score >= 85 ? "A" : score >= 70 ? "B" : score >= 50 ? "C" : score >= 30 ? "D" : "F";

      scorecard.push({ slug:doc.id, name, score, rating, languages:totalLangs,
        faq_langs:faqLangs.length, article_langs:articleLangs.length,
        title:checks.title, desc:checks.desc, article:checks.article, faq:checks.faq, steps:checks.steps,
        spanglish:checks.spanglish,
        missing: [!checks.title&&'title',!checks.desc&&'desc',!checks.article&&'article',!checks.faq&&'faq',!checks.steps&&'steps',checks.spanglish&&'spanglish',totalLangs<6&&'hreflang'].filter(Boolean)
      });
    }

    scorecard.sort((a,b) => a.score - b.score);
    const summary = {
      total: scorecard.length,
      a: scorecard.filter(s=>s.rating==="A").length,
      b: scorecard.filter(s=>s.rating==="B").length,
      c: scorecard.filter(s=>s.rating==="C").length,
      d: scorecard.filter(s=>s.rating==="D").length,
      f: scorecard.filter(s=>s.rating==="F").length,
      avg_score: Math.round(scorecard.reduce((s,c)=>s+c.score,0)/scorecard.length),
      need_faq: scorecard.filter(s=>!s.faq).length,
      need_article: scorecard.filter(s=>!s.article).length,
      need_title: scorecard.filter(s=>!s.title).length,
      need_hreflang: scorecard.filter(s=>s.languages<6).length,
      daily_target: Math.ceil(scorecard.filter(s=>s.score<70).length/30),
    };

    return res.status(200).json({ summary, scorecard });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

/**
 * Bulk sync — accepts batch calculator data via POST and writes to Firestore
 * Used by deep_sync.py to sync all source file content into calc_cms
 */
exports.bulkSyncCalcsHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  try {
    const batch = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
    if (!batch || typeof batch !== 'object') return res.status(400).json({ error: "Invalid batch data" });

    const entries = Object.entries(batch).filter(([slug, data]) => slug && data && data.langs);

    // Read existing docs first so the sync NEVER destroys richer content.
    // The static-file sync sends empty long_content/faq for every language;
    // a blind merge would overwrite AI-generated articles with "". We keep the
    // existing value whenever the incoming one is empty. This is the fix for the
    // recurring "completed content disappears" / thin-page bug.
    const existingDocs = await Promise.all(entries.map(([slug]) => db.collection("calc_cms").doc(slug).get()));

    // Fields whose existing (richer) value must survive an empty incoming value
    const PRESERVE = ['long_content','faq','steps','mistakes','seo_title','seo_description','desc','example_label','result_context','inputs_labels','outputs_labels','range_hints','slug'];
    const isEmpty = v => v === undefined || v === null || v === '' ||
      (Array.isArray(v) && v.length === 0) ||
      (v && typeof v === 'object' && !Array.isArray(v) && Object.keys(v).length === 0);

    let count = 0, preserved = 0;
    const dbBatch = db.batch();

    for (let i = 0; i < entries.length; i++) {
      const [slug, data] = entries[i];
      const existing = existingDocs[i];
      const exLangs = (existing.exists && existing.data().langs) || {};
      const mergedLangs = {};

      for (const lang of LANGS) {
        const inc = { ...(data.langs[lang] || {}) };
        const ex = exLangs[lang] || {};
        for (const field of PRESERVE) {
          if (isEmpty(inc[field]) && !isEmpty(ex[field])) { inc[field] = ex[field]; preserved++; }
        }
        mergedLangs[lang] = inc;
      }

      const ref = db.collection("calc_cms").doc(slug);
      const writeData = { ...data, langs: mergedLangs, synced_at: admin.firestore.FieldValue.serverTimestamp(), updated_at: admin.firestore.FieldValue.serverTimestamp() };
      // Never let the static sync clobber existing calculator mechanics either
      if (existing.exists) {
        const ed = existing.data();
        if (isEmpty(data.formula) && !isEmpty(ed.formula)) writeData.formula = ed.formula;
        if (isEmpty(data.inputs) && !isEmpty(ed.inputs)) writeData.inputs = ed.inputs;
        if (isEmpty(data.outputs) && !isEmpty(ed.outputs)) writeData.outputs = ed.outputs;
      }
      dbBatch.set(ref, writeData, { merge: true });
      count++;
    }

    await dbBatch.commit();
    console.log(`[BulkSync] Synced ${count} calculators (preserved ${preserved} existing content fields)`);
    return res.status(200).json({ synced: count, preserved });
  } catch(e) {
    console.error("[BulkSync] Error:", e.message);
    return res.status(500).json({ error: e.message });
  }
});

exports.getScorecardHttp = functions.https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  if (req.method === "OPTIONS") { res.set("Access-Control-Allow-Methods", "GET"); return res.status(204).send(""); }
  try {
    const doc = await db.collection("admin_prefs").doc("calc_scorecard").get();
    const forceRefresh = req.query.force === "true";
    const isFresh = !forceRefresh && doc.exists && doc.data().generated_at && 
      (Date.now()/1000 - (doc.data().generated_at._seconds||0)) < 3600;

    let scorecard, summary;

    if (isFresh) {
      ({ scorecard, summary } = doc.data());
    } else {
      // Generate fresh scorecard with per-language checks
      const snap = await db.collection("calc_cms").limit(500).get();
      const sc = [];
      const allLangs = ["en","es","fr","de","it","pt"];
      let siteFaqLangs = 0, siteArticleLangs = 0, siteTitleLangs = 0, siteHasAllLangs = 0;

      for (const d of snap.docs) {
        const c = d.data(); const langs = c.langs || {};
        const en = langs.en || {};
        const n = en.name || c.name || d.id;

        // Per-language checks
        const hasName = l => !!(langs[l]?.name);
        const hasFaq = l => !!(langs[l]?.faq && langs[l].faq.length >= 2);
        const hasArticle = l => !!(langs[l]?.long_content && langs[l].long_content.length > 500);
        const hasTitle = l => !!(langs[l]?.seo_title && langs[l].seo_title.length >= 15);
        const hasSteps = l => !!(langs[l]?.steps && langs[l].steps.filter(Boolean).length >= 3);

        const totalLangs = allLangs.filter(hasName).length;
        const faqLangs = allLangs.filter(hasFaq).length;
        const articleLangs = allLangs.filter(hasArticle).length;
        const titleLangs = allLangs.filter(hasTitle).length;
        if (totalLangs >= 6) siteHasAllLangs++;

        // Score calculation (weighted by language completeness)
        let s = 0;
        if (titleLangs >= 6) s += 12; else if (titleLangs >= 3) s += 8; else if (titleLangs >= 1) s += 4;
        if (articleLangs >= 3) s += 15; else if (articleLangs >= 1) s += 8;
        if (faqLangs >= 3) s += 12; else if (faqLangs >= 1) s += 6;
        if (allLangs.filter(hasSteps).length >= 3) s += 8; else if (en.steps?.filter(Boolean).length >= 1) s += 4;
        if (totalLangs >= 6) s += 10; else if (totalLangs >= 4) s += 7; else if (totalLangs >= 2) s += 4;

        // Spanglish penalty
        const es = ['calculadora','hormigon','ladrillo','tabique'];
        if (es.some(w => (en.seo_title||'').toLowerCase().includes(w))) s -= 5;

        s = Math.max(0, Math.min(100, s));
        const r = s>=85?"A":s>=70?"B":s>=50?"C":s>=30?"D":"F";

        const missing = [];
        if (titleLangs < 6) missing.push(`${6-titleLangs} lang need title`);
        if (faqLangs < 6) missing.push(`${6-faqLangs} lang need FAQ`);
        if (articleLangs < 6) missing.push(`${6-articleLangs} lang need article`);
        if (totalLangs < 6) missing.push(`${6-totalLangs} lang missing`);

        siteFaqLangs += faqLangs; siteArticleLangs += articleLangs; siteTitleLangs += titleLangs;

        sc.push({slug:d.id,name:n,score:s,rating:r,
          languages:totalLangs, faq_langs:faqLangs, article_langs:articleLangs, title_langs:titleLangs,
          title:titleLangs>=1, article:articleLangs>=1, faq:faqLangs>=1,
          has_all_langs:totalLangs>=6,
          missing:missing.slice(0,4)});
      }
      sc.sort((a,b)=>a.score-b.score);
      summary = {
        total:sc.length,
        a:sc.filter(x=>x.rating==="A").length, b:sc.filter(x=>x.rating==="B").length,
        c:sc.filter(x=>x.rating==="C").length, d:sc.filter(x=>x.rating==="D").length,
        f:sc.filter(x=>x.rating==="F").length,
        avg:Math.round(sc.reduce((x,c)=>x+c.score,0)/sc.length),
        need_faq:sc.filter(x=>x.faq_langs<6).length,
        need_article:sc.filter(x=>x.article_langs<6).length,
        need_title:sc.filter(x=>x.title_langs<6).length,
        need_languages:sc.filter(x=>x.languages<6).length,
        // Per-language totals
        total_faq_entries: siteFaqLangs,
        total_article_entries: siteArticleLangs,
        total_title_entries: siteTitleLangs,
        complete_all_langs: siteHasAllLangs,
        completion_pct: Math.round(sc.reduce((x,c)=>x+c.score,0)/sc.length),
      };
      scorecard = sc;
      await db.collection("admin_prefs").doc("calc_scorecard").set({summary,scorecard,generated_at:admin.firestore.FieldValue.serverTimestamp()});
    }

    // ── Add GSC usage data (impressions, clicks) ──
    const siteUrl = functions.config().gsc?.site_url || "sc-domain:calcto.work";
    let gscData = {};

    // Build reverse lookup: English slug → primary slug from calc-index
    const slugMap = {}; // en_slug → primary_slug
    try {
      const idxPath = require("path").join(__dirname, "calc-index.json");
      if (require("fs").existsSync(idxPath)) {
        const idx = JSON.parse(require("fs").readFileSync(idxPath, "utf8"));
        for (const c of idx) {
          const enSlug = (c.slugs?.en) || c.slug;
          if (enSlug && enSlug !== c.slug) slugMap[enSlug] = c.slug;
          // Also map all language slugs
          for (const [lang, lSlug] of Object.entries(c.slugs || {})) {
            if (lSlug && lSlug !== c.slug) slugMap[lSlug] = c.slug;
          }
        }
      }
    } catch(e) {}

    try {
      const gscSnap = await db.collection("gsc_page_stats")
        .where("site_url","==",siteUrl).where("date",">=",(new Date(Date.now()-30*86400000)).toISOString().slice(0,10))
        .orderBy("date","desc").limit(1000).get();
      gscSnap.forEach(d => {
        let p = (d.data().page||"").split("/").filter(Boolean).pop()||"";
        // Map English slug to primary slug
        if (slugMap[p]) p = slugMap[p];
        if (!gscData[p]) gscData[p] = { imp:0, clicks:0 };
        gscData[p].imp += d.data().total_impressions||0;
        gscData[p].clicks += d.data().total_clicks||0;
      });
    } catch(e) {}

    // ── Merge GSC data into scorecard ──
    let totalImp = 0, totalClicks = 0;
    for (const c of scorecard) {
      const g = gscData[c.slug] || { imp:0, clicks:0 };
      c.impressions = g.imp;
      c.clicks = g.clicks;
      c.indexed = g.imp > 0;
      totalImp += g.imp;
      totalClicks += g.clicks;
    }

    summary.total_impressions = totalImp;
    summary.total_clicks = totalClicks;
    summary.indexed_count = scorecard.filter(c=>c.indexed).length;

    return res.status(200).json({ summary, scorecard });
  } catch(e) { return res.status(500).json({ error: e.message }); }
});

/**
 * genInterpretationHttp — give a calculator a real reading of the user's result.
 *
 * Most calcs printed a number plus a sentence restating the rules in the abstract
 * ("your pH indicates acidity if under 7, neutrality at exactly 7..."). This builds
 * a per-calculator `interpretation`: either calibrated BANDS (the value sits on a
 * meaningful scale — pH, BMI, body fat) or an INSIGHT sentence computed from the
 * user's own numbers (quantities, costs), plus one practical tip.
 *
 * HARD GUARD, same contract as the other writers: nothing is stored unless the
 * bands are ordered, cover the scale, and every preset the calc ships actually
 * lands inside a band. Bands must also name a real published source.
 *
 * POST { slug, republish?:bool, force?:bool }
 */
exports.genInterpretationHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const path = require("path"), fs = require("fs");
    const b = req.body || {};
    const inSlug = String(b.slug || "").trim();
    if (!inSlug) return res.status(400).json({ error: "slug required" });
    const republish = b.republish !== false;

    let index = [];
    try { const raw = require(path.join(__dirname, "calc-index.json")); index = Array.isArray(raw) ? raw : (raw.calcs || Object.values(raw)); } catch (e) {}
    const entry = index.find(e => e.slug === inSlug) || index.find(e => e.slugs && Object.values(e.slugs).includes(inSlug));
    const baseSlug = entry ? entry.slug : inSlug;
    const id = entry ? String(entry.id) : null;

    const docRef = db.collection("calc_cms").doc(baseSlug);
    const snap = await docRef.get();
    if (!snap.exists) return res.status(404).json({ error: "Calc not found: " + baseSlug });
    const doc = snap.data();
    if (doc.interpretation && !b.force) {
      return res.status(200).json({ ok: true, slug: baseSlug, skipped: "already has an interpretation (pass force:true to regenerate)" });
    }

    let inputsArr = (doc.inputs || []).length ? doc.inputs : [];
    let outputsArr = (doc.outputs || []).length ? doc.outputs : [];
    let formula = doc.formula && doc.formula.length > 10 ? doc.formula : "";
    let staticLang = null;
    if (id) {
      try {
        const cj = JSON.parse(fs.readFileSync(path.join(__dirname, "calcs", id, "calc.json"), "utf8"));
        if (!inputsArr.length && (cj.inputs || []).length) inputsArr = cj.inputs;
        if (!outputsArr.length && (cj.outputs || []).length) outputsArr = cj.outputs;
        if (!formula) formula = cj.formula || "";
      } catch (e) {}
      try { staticLang = JSON.parse(fs.readFileSync(path.join(__dirname, "calcs", id, "en.json"), "utf8")); } catch (e) {}
    }
    if (!formula || !inputsArr.length || !outputsArr.length) {
      return res.status(400).json({ error: "Calc lacks formula/inputs/outputs" });
    }

    let fn;
    try { fn = new Function("inputs", '"use strict";' + formula); }
    catch (e) { return res.status(422).json({ error: "Formula does not parse: " + e.message }); }

    const enLang = (doc.langs && doc.langs.en) || {};
    const outLabels = Object.assign({}, (staticLang && staticLang.outputs) || {}, enLang.outputs_labels || {});
    const name = enLang.name || doc.name_en || doc.name || baseSlug;
    const desc = enLang.desc || doc.desc_en || "";
    const outIds = outputsArr.map(o => o.id).filter(Boolean);

    // Sample the calc across its own presets + defaults so the model sees the real
    // output range, and so we can verify every shipped example lands in a band.
    const defaults = {};
    for (const i of inputsArr) {
      let v = i.default;
      if (v === undefined || v === null || v === "") {
        const opts = i.options || i.choices;
        if (opts && opts.length) v = (opts[0] && opts[0].value !== undefined ? opts[0].value : opts[0]);
        else if (typeof i.min === "number" && typeof i.max === "number") v = (i.min + i.max) / 2;
        else v = 1;
      }
      defaults[i.id] = v;
    }
    const corner = pick => {
      const o = {};
      for (const i of inputsArr) {
        const opts = i.options || i.choices;
        if (opts && opts.length) { o[i.id] = (opts[0] && opts[0].value !== undefined ? opts[0].value : opts[0]); continue; }
        const v = pick(i);
        o[i.id] = (v === undefined || v === null) ? defaults[i.id] : v;
      }
      return o;
    };
    const samples = [
      defaults,
      corner(i => (typeof i.min === "number" ? i.min : undefined)),
      corner(i => (typeof i.max === "number" ? i.max : undefined)),
    ];
    for (const p of (doc.comparison_presets || [])) {
      const pv = (p && p.inputs && typeof p.inputs === "object") ? p.inputs : null;
      if (pv) samples.push(Object.assign({}, defaults, pv));
    }
    const observed = {};
    for (const s of samples) {
      let r; try { r = fn(s); } catch (e) { continue; }
      if (!r || r.error || typeof r !== "object") continue;
      for (const k of outIds) {
        const v = parseFloat(r[k]);
        if (isFinite(v)) { (observed[k] = observed[k] || []).push(v); }
      }
    }
    const numericOuts = Object.keys(observed).filter(k => observed[k].length);
    if (!numericOuts.length) return res.status(400).json({ error: "No numeric output could be sampled" });

    const rangeLines = numericOuts.map(k => {
      const vs = observed[k];
      return '- "' + k + '" (' + (outLabels[k] || k) + '): observed ' + Math.min.apply(null, vs) + " to " + Math.max.apply(null, vs);
    }).join("\n");

    const cfgSnap = await db.collection("admin_prefs").doc("ai_config").get();
    const cfg = cfgSnap.exists ? cfgSnap.data() : {};
    const provider = cfg.active_provider || "anthropic";
    const provCfg = (cfg.providers || {})[provider] || {};
    const apiKey = provCfg.api_key || (functions.config().anthropic && functions.config().anthropic.key);
    if (!apiKey) return res.status(500).json({ error: "No API key for provider " + provider });
    async function ai(p, maxTokens) {
      let t;
      if (provider === "anthropic" || !cfg.active_provider) {
        const r = await fetch("https://api.anthropic.com/v1/messages", {
          method: "POST",
          headers: { "x-api-key": apiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
          body: JSON.stringify({ model: provCfg.model || "claude-haiku-4-5-20251001", max_tokens: maxTokens, messages: [{ role: "user", content: p }] }),
        });
        if (!r.ok) throw new Error("AI error: " + await r.text());
        const d = await r.json(); t = d.content && d.content[0] && d.content[0].text;
      } else {
        const baseUrl = provider === "deepseek" ? "https://api.deepseek.com/v1" : "https://api.openai.com/v1";
        const model = provCfg.model || (provider === "deepseek" ? "deepseek-chat" : "gpt-4o-mini");
        const r = await fetch(baseUrl + "/chat/completions", {
          method: "POST",
          headers: { "Authorization": "Bearer " + apiKey, "Content-Type": "application/json" },
          body: JSON.stringify({ model, messages: [{ role: "user", content: p }], max_tokens: maxTokens }),
        });
        if (!r.ok) throw new Error("AI error: " + await r.text());
        const d = await r.json(); t = d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
      }
      const mm = t && t.match(/{[\s\S]*}/);
      if (!mm) throw new Error("No JSON in AI response");
      return JSON.parse(mm[0]);
    }

    const prompt = [
      'You are writing the "what your result means" panel for an online calculator.',
      "",
      'Calculator: "' + name + '"',
      desc ? "What it does: " + desc : "",
      "Outputs it can show:",
      rangeLines,
      "",
      "Decide which ONE output a reader most wants interpreted, then choose EXACTLY ONE mode.",
      "",
      'MODE "bands" — REQUIRED whenever that output sits on a recognised scale with named',
      'regions. If the output is pH, pOH, BMI, body-fat percentage, blood pressure, a',
      'heart-rate zone, an efficiency or energy rating, water hardness, a risk index, or',
      'any bounded index whose regions have standard names, you MUST use bands.',
      "The regions must come from a real published standard issued by a recognised body",
      "(WHO, IUPAC, NIH, CDC, ACSM, AHA, ISO, EN, DIN, ASHRAE, ASTM, EPA, USDA, Eurocode...).",
      "If no such standard names the regions, DO NOT invent one - use insight mode instead.",
      'Return: {"mode":"bands","output":"<id>","unit":"<short unit or empty>",',
      '"scale":{"min":<number>,"max":<number>},',
      '"bands":[{"max":<upper bound, ascending, last must be >= scale.max>,',
      '"label":"<2-3 words>","tone":"bad|warn|ok|good|info",',
      '"note":"<ONE sentence saying what this band means in concrete, comparable terms>"}],',
      '"source":"<the actual published standard, e.g. WHO BMI classification>"}',
      "Rules: 3-6 bands, tiling the whole scale with no gaps. The scale must span the FULL",
      "range the standard defines (pH is 0-14, not 0-7) even if the observed samples only",
      "cover part of it - a reader can enter any value the form allows. Every note must be specific",
      'and comparative ("about as acidic as stomach acid"), never a restatement of the rule',
      '("under 7 is acidic"). Describe, never advise: no diagnosis, no treatment, no',
      '"see a doctor".',
      "",
      'MODE "insight" — for everything else (quantities, costs, areas, conversions).',
      'Return: {"mode":"insight","output":"<id>",',
      '"insight":"<ONE sentence that reads the result back using {output_id} placeholders',
      'and says what it means in practice>",',
      '"tip":"<ONE practical sentence a person acts on: rounding to purchasable units, a',
      "typical benchmark to compare against, or the mistake that changes this number most>\"}",
      "Rules: use at least one {placeholder}; only these ids exist: " + outIds.join(", ") + ".",
      "Be concrete and specific to THIS calculator. No filler, no restating the inputs.",
      "The insight must READ THE VALUE BACK, not teach the topic. Never write a stand-in",
      "letter like X or N for a number you cannot know - use a {placeholder} or leave it out.",
      "Never list examples (no 'for example', no 'e.g.'). Keep it under 240 characters.",
      "Every number and every ratio in the sentence MUST come from a {placeholder}. Do not",
      "write a fixed figure like 'over 30 years' or 'about half' - those are true only for",
      "the default inputs and become wrong as soon as the reader changes one.",
      "",
      "Return ONLY the JSON object.",
    ].filter(Boolean).join("\n");

    const TONES = ["bad", "warn", "ok", "good", "info"];
    const ADVICE = ["diagnos", "treatment", "cure", "prescri", "see a doctor", "consult your doctor", "medical advice"];
    const hasAdvice = s => { const t = String(s || "").toLowerCase(); return ADVICE.some(w => t.indexOf(w) !== -1); };

    function validate(g) {
      if (!g || typeof g !== "object") return "not an object";
      const out = String(g.output || "");
      if (!outIds.includes(out)) return 'output "' + out + '" is not one of ' + outIds.join(",");

      if (g.mode === "bands") {
        const sc = g.scale || {};
        if (typeof sc.min !== "number" || typeof sc.max !== "number" || !(sc.max > sc.min)) return "bad scale";
        const bands = Array.isArray(g.bands) ? g.bands : [];
        if (bands.length < 3 || bands.length > 6) return "need 3-6 bands, got " + bands.length;
        let prev = -Infinity;
        for (const bd of bands) {
          if (typeof bd.max !== "number" || !(bd.max > prev)) return "band maxima must ascend";
          prev = bd.max;
          if (!bd.label || String(bd.label).length > 32) return "band label missing or too long";
          if (!bd.note || String(bd.note).length < 15) return "band note missing or too short";
          if (!TONES.includes(bd.tone)) return 'bad tone "' + bd.tone + '"';
          if (hasAdvice(bd.note)) return "note gives medical or treatment advice";
        }
        if (prev < sc.max) return "bands do not cover the top of the scale";
        if (!g.source || String(g.source).length < 4) return "a bands interpretation must name its source";
        const srcLower = String(g.source).toLowerCase();
        const RECOGNISED = ["who", "world health", "iupac", "nih", "cdc", "acsm", "american heart",
          "aha", "american diabetes", "navy", "jackson", "pollock", "karvonen", "tanaka",
          "harris-benedict", "mifflin", "katch", "ashrae", "iso ", "iso-", "en 1", "din ", "nfpa",
          "aci ", "eurocode", "usda", "epa", "fda", "efsa", "nhs", "beaufort", "mohs", "richter",
          "saffir", "seer", "energy star", "epc", "cie ", "osha", "niosh", "ieee", "astm", "bs ",
          "iec ", "ansi", "framingham", "apgar", "glasgow", "ph scale", "water hardness",
          "langelier", "body mass index", "bmi classification", "blood pressure", "aqi",
          "air quality index", "uv index", "decibel", "beaufort scale", "nutrition"];
        if (!RECOGNISED.some(k => srcLower.indexOf(k) !== -1)) {
          return "source \"" + g.source + "\" is not a recognised published standard - use insight mode instead";
        }
        // Every value this calc actually produces must land inside the scale.
        const vs = observed[out] || [];
        if (!vs.length) return 'output "' + out + '" produced no numeric sample';
        for (const v of vs) {
          if (v < sc.min || v > sc.max) return "sampled value " + v + " falls outside scale " + sc.min + ".." + sc.max;
        }
        return null;
      }

      if (g.mode === "insight") {
        const ins = String(g.insight || "");
        if (ins.length < 25) return "insight too short";
        if (ins.length > 280) return "insight too long - it should read the value back, not teach the topic";
        const lower = ins.toLowerCase();
        for (const tell of ["for example", "e.g.", "such as", "typically ranges"]) {
          if (lower.indexOf(tell) !== -1) return "insight lists examples instead of reading the value (" + tell + ")";
        }
        if (/(^| )[XN]( |-)/.test(ins)) return "insight contains a stand-in letter instead of a value";
        const bare = ins.replace(/{[a-zA-Z_][a-zA-Z0-9_]*}/g, "");
        const CONSTANTS = ["0", "1", "2", "7", "10", "12", "24", "60", "100", "1000", "1,000", "360", "365"];
        const nums = bare.match(/(?:^|[^A-Za-z0-9])([0-9]+(?:[.,][0-9]+)?)(?![A-Za-z0-9])/g) || [];
        for (const raw of nums) {
          const n = raw.replace(/[^0-9.,]/g, "");
          if (CONSTANTS.indexOf(n) === -1) {
            return "insight hardcodes " + n + ", which changes with the inputs - use a {placeholder}";
          }
        }
        for (const ratio of ["half of", "about half", "twice ", "double ", "a third", "two thirds", "10x", "10 times"]) {
          if (lower.indexOf(ratio) !== -1) return "insight asserts a ratio (" + ratio.trim() + ") that changes with the inputs";
        }
        const found = ins.match(/{[a-zA-Z_][a-zA-Z0-9_]*}/g) || [];
        if (!found.length) return "insight has no placeholder";
        for (const ph of found) {
          const key = ph.slice(1, -1);
          if (!outIds.includes(key)) return "insight references unknown output " + ph;
        }
        if (g.tip && String(g.tip).length < 15) return "tip too short";
        if (hasAdvice(ins) || hasAdvice(g.tip)) return "gives medical or treatment advice";
        return null;
      }
      return 'unknown mode "' + g.mode + '"';
    }

    let gen = null, why = null;
    for (let attempt = 0; attempt < 2 && !gen; attempt++) {
      let g;
      try { g = await ai(attempt === 0 ? prompt : prompt + "\n\nYour previous answer was rejected because: " + why + ". Fix exactly that.", 2000); }
      catch (e) { why = e.message; continue; }
      const err = validate(g);
      if (err) { why = err; continue; }
      gen = g;
    }
    if (!gen) return res.status(422).json({ error: "Could not generate a valid interpretation — nothing written", slug: baseSlug, detail: why });

    // Numbers live at the doc root; the words live per language.
    const root = { output: gen.output, mode: gen.mode };
    if (gen.mode === "bands") {
      root.unit = gen.unit || "";
      root.scale = { min: gen.scale.min, max: gen.scale.max };
      root.bands = gen.bands.map(x => ({ max: x.max, tone: x.tone }));
    }
    const enText = gen.mode === "bands"
      ? { bands: gen.bands.map(x => ({ label: x.label, note: x.note })), source: gen.source }
      : { insight: gen.insight, tip: gen.tip || "" };

    const OTHER = ["es", "fr", "de", "it", "pt"];
    const langsPatch = { en: { interpretation_text: enText } };
    try {
      const tr = await ai([
        "Translate this calculator result-explanation into Spanish, French, German, Italian and Portuguese.",
        "Keep every field, the same JSON shape and the same array order. Natural and native in each",
        "language, not word-for-word. Keep it equally concrete. Leave any {placeholder} exactly as it is.",
        "",
        JSON.stringify(enText),
        "",
        'Return ONLY: {"es":{...},"fr":{...},"de":{...},"it":{...},"pt":{...}}',
      ].join("\n"), 2500);
      for (const l of OTHER) {
        const v = tr[l];
        if (!v) continue;
        if (gen.mode === "bands") {
          if (Array.isArray(v.bands) && v.bands.length === enText.bands.length && v.bands.every(x => x && x.label && x.note)) {
            langsPatch[l] = { interpretation_text: { bands: v.bands.map(x => ({ label: String(x.label), note: String(x.note) })), source: String(v.source || enText.source) } };
          }
        } else if (v.insight && String(v.insight).indexOf("{") !== -1) {
          langsPatch[l] = { interpretation_text: { insight: String(v.insight), tip: String(v.tip || "") } };
        }
      }
    } catch (e) { /* best effort: English still beats a generic sentence */ }

    await docRef.set({ interpretation: root, langs: langsPatch }, { merge: true });

    let deployed = false;
    if (republish && doc.status === "published") {
      const s2 = await docRef.get();
      const files = await _buildCalcFiles(baseSlug, s2.data());
      if (Object.keys(files).length) { const dr = await _deployPagesToHosting(files, "[Interp] " + baseSlug); deployed = !dr.error; }
    }
    return res.status(200).json({
      ok: true, slug: baseSlug, mode: gen.mode, output: gen.output,
      bands: gen.mode === "bands" ? gen.bands.map(x => x.label) : undefined,
      insight: gen.mode === "insight" ? gen.insight : undefined,
      langs: Object.keys(langsPatch).length, deployed,
    });
  } catch (e) { console.error("genInterpretationHttp error:", e); return res.status(500).json({ error: e.message }); }
});

/* ── IndexNow (indexnow.org) ────────────────────────────────────────────────
   One POST tells Bing, Yandex, Seznam and Naver that a URL changed, instead of
   waiting for them to re-crawl. Google does not participate, so this is purely
   additive — it cannot affect Google rankings either way.

   The key must be served as a text file whose body is the key itself; search
   engines fetch it to prove we own the host. Verify at /<key>.txt after deploy.
------------------------------------------------------------------------- */
const INDEXNOW_KEY = "c6b802c0939d6de8cf05d9afb96b7c79";
const INDEXNOW_KEY_URL = `${SITE}/${INDEXNOW_KEY}.txt`;

/**
 * Submit up to 10,000 URLs per request. Returns a per-chunk status list.
 * Never throws: indexing is a nice-to-have and must not fail a publish.
 */
async function _indexNowSubmit(urls) {
  const list = [...new Set((urls || []).filter(u => typeof u === "string" && u.startsWith(SITE)))];
  if (!list.length) return { submitted: 0, results: [] };
  const host = SITE.replace(/^https?:\/\//, "");
  const results = [];
  for (let i = 0; i < list.length; i += 10000) {
    const chunk = list.slice(i, i + 10000);
    try {
      const r = await fetch("https://api.indexnow.org/indexnow", {
        method: "POST",
        headers: { "Content-Type": "application/json; charset=utf-8" },
        body: JSON.stringify({ host, key: INDEXNOW_KEY, keyLocation: INDEXNOW_KEY_URL, urlList: chunk }),
      });
      // 200 = accepted, 202 = accepted with key validation pending. Both are fine.
      results.push({ count: chunk.length, status: r.status, ok: r.status === 200 || r.status === 202 });
    } catch (e) {
      results.push({ count: chunk.length, status: 0, ok: false, error: e.message });
    }
  }
  return { submitted: list.length, results };
}

/**
 * indexNowHttp — ping IndexNow for changed URLs.
 * POST { urls: [...] }            submit an explicit list
 * POST { all: true }              submit every URL in the sitemap
 * POST { slug: "x", langs: [...] } submit one calculator in the given languages
 *
 * Submitting the WHOLE site repeatedly looks like spam and can earn a 429, so
 * `all` is a deliberate manual action, not something the republish sweep does.
 */
exports.indexNowHttp = functions.runWith({ timeoutSeconds: 300, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const b = req.body || {};
    let urls = [];

    if (Array.isArray(b.urls) && b.urls.length) {
      urls = b.urls;
    } else if (b.all) {
      // Pull straight from the live sitemap so we submit exactly what we publish.
      const xml = await fetch(`${SITE}/sitemap.xml`).then(r => r.text());
      urls = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
    } else if (b.slug) {
      const langs = Array.isArray(b.langs) && b.langs.length ? b.langs : LANGS;
      const snap = await db.collection("calc_cms").doc(String(b.slug)).get();
      const data = snap.exists ? _applyLangSlugs(String(b.slug), snap.data()) : null;
      urls = langs.map(l => {
        const ls = (data && data.langs && data.langs[l] && data.langs[l].slug) || b.slug;
        return `${SITE}/${l}/${ls}/`;
      });
    } else {
      return res.status(400).json({ error: "pass urls[], slug, or all:true" });
    }

    const out = await _indexNowSubmit(urls);
    return res.status(200).json({ ok: true, build: _BUILD_ID, keyUrl: INDEXNOW_KEY_URL, ...out });
  } catch (e) {
    console.error("indexNowHttp error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/* ── Category page repair ───────────────────────────────────────────────────
   The 120 category pages (20 categories x 6 languages) are stale static files
   that no current code path regenerates. Two problems, both visible in real
   search results:

   1. Every one carried the same half-English template description
      ("Mampostería y Cerramientos – free online calculators."). Google ignored
      it and wrote its own snippet.
   2. Each calculator card starts with a decorative index, "#011". Because that
      is the first text in the card, Google's generated snippet became
      "#011 · Calcula ladrillos... #012 · ..." — which reads as broken.

   Rather than redesign the pages, rewrite exactly those two things and republish
   through the normal incremental deploy. The description is built from the
   calculators actually listed on the page, so it is specific and truthful.
------------------------------------------------------------------------- */
const CAT_SLUGS = ["estructuras","mamposteria","pavimentos","fontaneria","electricidad",
  "climatizacion","carpinteria","pintura","gestion","matematicas","ciencia","salud",
  "finanzas","cotidiano","quimica","electronica","clima","utilidades","fotografia",
  "transporte","fisica","musica","industria"];

// Per-language sentence shapes. Written out rather than machine-translated: this is
// the text a searcher reads before deciding whether to click.
const CAT_DESC_TPL = {
  en: (label, list, n) => `${label} calculators: ${list}. ${n} free tools with formulas, worked examples and instant results.`,
  es: (label, list, n) => `Calculadoras de ${label}: ${list}. ${n} herramientas gratuitas con fórmulas, ejemplos resueltos y resultados al instante.`,
  fr: (label, list, n) => `Calculateurs ${label} : ${list}. ${n} outils gratuits avec formules, exemples résolus et résultats instantanés.`,
  de: (label, list, n) => `${label} berechnen: ${list}. ${n} kostenlose Rechner mit Formeln, Beispielen und sofortigen Ergebnissen.`,
  it: (label, list, n) => `Calcolatori ${label}: ${list}. ${n} strumenti gratuiti con formule, esempi svolti e risultati immediati.`,
  pt: (label, list, n) => `Calculadoras de ${label}: ${list}. ${n} ferramentas gratuitas com fórmulas, exemplos e resultados instantâneos.`,
};

// Every listed name ends in "Calculator" / "Calculadora de ...", which makes the
// sentence read "calculators: X Calculator, Y Calculator". Drop the repeated word so
// the snippet names the SUBJECT, which is what a searcher scans for.
const _CALC_WORD = /[\s-]*(calculators?|calculadoras?|calculateurs?|calculatrices?|rechner|calcolatori?|calcolatrici?|calcolatrice)\s*(\([^)]*\))?\s*$|^\s*(calculadora de|calculadora del|calculadora|calculateur de|calculateur du|calculateur|calculatrice de|calculatrice|calcolatore di|calcolatore del|calcolatore|calcolatrice di|calcolatrice|calculo de|cálculo de)\s+/gi;
function _stripCalcWord(n) {
  const out = String(n || "").replace(_CALC_WORD, "").trim();
  return out.length >= 3 ? out : String(n || "").trim();
}

// Visible intro line, in the page language. Shorter than the meta description because
// a reader sees it directly under the heading.
const CAT_INTRO_TPL = {
  en: (label, n) => `${n} free ${label.toLowerCase()} calculators. Enter your numbers and get the result instantly, with the formula and a worked example on every page.`,
  es: (label, n) => `${n} calculadoras de ${label.toLowerCase()} gratuitas. Introduce tus datos y obtén el resultado al instante, con la fórmula y un ejemplo resuelto en cada página.`,
  fr: (label, n) => `${n} calculateurs ${label.toLowerCase()} gratuits. Saisissez vos valeurs et obtenez le résultat immédiatement, avec la formule et un exemple résolu sur chaque page.`,
  de: (label, n) => `${n} kostenlose Rechner für ${label}. Werte eingeben und sofort das Ergebnis erhalten – mit Formel und Rechenbeispiel auf jeder Seite.`,
  it: (label, n) => `${n} calcolatori ${label.toLowerCase()} gratuiti. Inserisci i tuoi dati e ottieni subito il risultato, con la formula e un esempio svolto in ogni pagina.`,
  pt: (label, n) => `${n} calculadoras de ${label.toLowerCase()} gratuitas. Introduza os seus dados e obtenha o resultado na hora, com a fórmula e um exemplo resolvido em cada página.`,
};
function _catDescription(lang, label, names) {
  const n = names.length;
  // Name three real calculators, then trim to a length Google will show whole.
  const clean = names.map(_stripCalcWord);
  const build = k => {
    const list = clean.slice(0, k).join(", ");
    return (CAT_DESC_TPL[lang] || CAT_DESC_TPL.en)(label, list, n);
  };
  for (let k = 3; k >= 1; k--) {
    const d = build(k);
    if (d.length <= 158) return d;
  }
  return build(1).slice(0, 155).replace(/[\s,;:.]+$/, "") + "…";
}

/**
 * fixCategoryPagesHttp — rewrite the description and drop the decorative card
 * numbers on every category page, then republish them together.
 * POST { dryRun?: true }
 */
exports.fixCategoryPagesHttp = functions.runWith({ timeoutSeconds: 540, memory: "512MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.set("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).send("");
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });
  try {
    const zlib = require("zlib"), util = require("util"), crypto = require("crypto");
    const gzip = util.promisify(zlib.gzip);
    const dryRun = !!(req.body && req.body.dryRun);

    const files = {};
    const report = [];
    for (const lang of LANGS) {
      for (const cat of CAT_SLUGS) {
        const url = `${SITE}/${lang}/${cat}/`;
        let html;
        try {
          const r = await fetch(url);
          if (!r.ok) continue;
          html = await r.text();
        } catch (e) { continue; }

        // The localized label lives in the <title>: "Mampostería y Cerramientos – CalcToWork".
        const title = (html.match(/<title>([^<]*)<\/title>/) || [])[1] || "";
        const label = title.split(/\s[–—-]\s/)[0].trim() || cat;
        const names = [...html.matchAll(/<h3[^>]*>([^<]+)<\/h3>/g)].map(m => m[1].trim()).filter(Boolean);
        if (!names.length) continue;

        const desc = _catDescription(lang, label, names);
        let out = html;

        // Replace the meta + OpenGraph descriptions.
        out = out.replace(/(<meta name="description" content=")[^"]*(")/, (m, a, b) => a + esc(desc) + b);
        out = out.replace(/(<meta property="og:description" content=")[^"]*(")/, (m, a, b) => a + esc(desc) + b);
        out = out.replace(/(<meta name="twitter:description" content=")[^"]*(")/, (m, a, b) => a + esc(desc) + b);

        // Empty the decorative index so it is no longer the card's first text.
        // The element stays for layout; only the scrapeable text goes.
        out = out.replace(/<div class="calc-thumb-num">[^<]*<\/div>/g, '<div class="calc-thumb-num" aria-hidden="true"></div>');

        // The visible intro used the same half-English template as the meta tag.
        const intro = (CAT_INTRO_TPL[lang] || CAT_INTRO_TPL.en)(label, names.length);
        out = out.replace(/<p>[^<]*free online calculators\.?<\/p>/i, () => `<p>${esc(intro)}</p>`);

        report.push({ lang, cat, calcs: names.length, desc });
        if (!dryRun) {
          const gz = await gzip(Buffer.from(out, "utf8"));
          files[`/${lang}/${cat}/index.html`] = { gzipped: gz, hash: crypto.createHash("sha256").update(gz).digest("hex") };
        }
      }
    }

    if (dryRun) return res.status(200).json({ build: _BUILD_ID, dryRun: true, pages: report.length, sample: report.slice(0, 6) });
    if (!Object.keys(files).length) return res.status(400).json({ error: "no category pages could be rebuilt" });

    const dep = await _deployPagesToHosting(files, `[CategoryFix] ${Object.keys(files).length} pages`);
    return res.status(200).json({
      ok: true, build: _BUILD_ID, pages: Object.keys(files).length, deployed: !dep.error,
      error: dep.error || null, sample: report.slice(0, 4),
    });
  } catch (e) {
    console.error("fixCategoryPagesHttp error:", e);
    return res.status(500).json({ error: e.message });
  }
});

/**
 * hostingHistoryHttp — list recent hosting releases with their file counts.
 *
 * Written after an impressions collapse whose most plausible cause was a release that
 * shipped with pages missing: the deploy path clones "the current release", and a stale
 * read can drop files while still passing the >1000-file guard. Without this, "did a bad
 * version go live?" was unanswerable after the fact — the manifest is the only record.
 *
 * A sudden dip in fileCount between consecutive releases is the fingerprint of that bug.
 * GET (no body needed). Optional ?limit=N
 */
exports.hostingHistoryHttp = functions.runWith({ timeoutSeconds: 120, memory: "256MB" })
  .https.onRequest(async (req, res) => {
  res.set("Access-Control-Allow-Origin", "*");
  try {
    const tokenResult = await admin.app().options.credential.getAccessToken();
    const headers = { "Authorization": "Bearer " + tokenResult.access_token };
    const limit = Math.min(100, parseInt(req.query.limit, 10) || 40);

    const r = await fetch(`${HOSTING_API}/sites/${HOSTING_SITE}/releases?pageSize=${limit}`, { headers });
    if (!r.ok) return res.status(500).json({ error: "releases fetch failed: " + await r.text() });
    const data = await r.json();

    const rows = (data.releases || []).map(rel => ({
      time: rel.releaseTime,
      files: Number((rel.version && rel.version.fileCount) || 0),
      message: (rel.message || "").slice(0, 60),
      version: (rel.version && rel.version.name || "").split("/").pop(),
    }));

    // Flag any release that shipped materially fewer files than the one before it
    // (releases come back newest-first, so "before it" is the NEXT element).
    const suspicious = [];
    for (let i = 0; i < rows.length - 1; i++) {
      const cur = rows[i], prev = rows[i + 1];
      if (prev.files > 1000 && cur.files < prev.files * 0.97) {
        suspicious.push({
          time: cur.time, message: cur.message,
          droppedFiles: prev.files - cur.files,
          from: prev.files, to: cur.files,
        });
      }
    }

    return res.status(200).json({
      build: _BUILD_ID,
      current: rows[0] || null,
      suspiciousReleases: suspicious,
      releases: rows,
    });
  } catch (e) {
    console.error("hostingHistoryHttp error:", e);
    return res.status(500).json({ error: e.message });
  }
});

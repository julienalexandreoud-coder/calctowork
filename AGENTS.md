# CalcToWork — Agent Guide

## Project Reality (updated 2026-07-21)

**Repo:** `C:\Users\julie\calctowork` (canonical) — GitHub: `github.com/julienalexandreoud-coder/calctowork`
**Live site:** https://calcto.work · **Dashboard:** https://calctowork.web.app/admin.html
**Generator:** `scripts/generate_calctowork.py` → `public/` (19,362 URLs)
**Python:** `C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe`
**Deploy:** `firebase deploy --only hosting` / `firebase deploy --only functions` (from repo root)

> ⚠️ `C:\Microsaas\obra` is a STALE clone of the same repo. Do NOT build/deploy from it.
> On 2026-07-21 its uncommitted work (full functions source incl. autopilot, Strategy tab,
> noindex-on-parametric revert, sync scripts) was merged INTO this repo and pushed.

## Data Model (current)

Each calculator = one directory `src/calculators/{id}/`:
- `calc.json` — formula (JS), inputs, outputs, block
- `{lang}.json` — per-language metadata: name, desc, seo_title, seo_description, input/output labels (langs: es, en, fr, de, it, pt)
- `{lang}.html` — per-language long-form article (900–1,400 words). **461 calcs × 6 langs = 2,766 articles**

Slugs + parametric variants: `scripts/tools_config.py` (TOOLS list).

## Content Fallback Chain (build-time)

`generate_calctowork.py` line ~1784:
1. `src/calculators/{id}/{lang}.html` — **PRIMARY** (the articles)
2. `long_content` inside `{lang}.json` — rare
3. `generate_long_content()` in `calc_content.py` — **FALLBACK ONLY**, generic template

**Rule:** never delete `{lang}.html` files in bulk. Regenerate only with validation (see fix_content.py).

## Content Quality & the Audit Pipeline

```bash
# 1. Uniqueness audit (exact dup, near-dup jaccard, template groups, wrong-lang, thin, tpl markers)
$PYTHON scripts/audit_uniqueness.py        # → audit/uniqueness_report.csv + uniqueness_summary.txt

# 2. Fix wrong-article / wrong-language files (translate correct sibling or generate fresh)
$PYTHON scripts/fix_content.py --apply --workers 4

# 3. Rewrite boilerplate-templated files (>=70% shared sentences)
$PYTHON scripts/fix_content.py --boilerplate --apply --workers 4
```

`fix_content.py` calls the **`callAI` Cloud Function** (DeepSeek backend, key stays server-side in
Firestore `admin_prefs/ai_config`). Every generation is validated (language purity, calc-name
presence, 650–2,200 words, no `<h1>`/`formula-section`, jaccard-vs-source) before writing.
Log: `audit/fix_log.jsonl` (resumable — FIXED entries are skipped on re-run).

> ⚠️ **2026-07-21 status:** DeepSeek balance exhausted mid-run. 910/2,300 broken-or-templated
> articles rewritten & deployed. Remainder resumes with `fix_content.py --boilerplate --apply`
> after topping up DeepSeek (deepseek.com) or switching provider in dashboard AI Settings.

## ⚠️ CRITICAL WARNINGS

### Functions deploys can DELETE production functions
The repo's `functions/` now contains the full source (51 exports, incl. autopilot/AI brain).
If `firebase deploy --only functions` ever warns "the following functions will be deleted",
**ABORT** — the local source is stale again. Recover from git history first.

### Policy: parametric variant pages are `noindex, follow`
Variants are inherently near-duplicate (same calc, different numbers) — indexing them risks
thin/doorway-page penalties (AdSense was rejected once for this). Template:
`calculator.html.j2` line 9 — `{% if is_parametric_variant %}noindex, follow{% else %}index, follow{% endif %}`.
`test_build.py` asserts this. Do not flip without an AdSense-safe reason.

### Never commit secrets
`firebase functions:config:get` shows live GSC OAuth credentials. `admin_prefs/ai_config`
holds the DeepSeek key. Neither belongs in git.

### Known open security issue
`callAI` (and several `*Http` functions) are **publicly callable without auth** — anyone can
burn the DeepSeek quota. Add a shared-secret header check when convenient.

## Build & Test Process

```bash
PYTHON = C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe

$PYTHON -m pip install -r requirements.txt   # once
$PYTHON scripts/generate_calctowork.py       # build → public/
$PYTHON scripts/tests/test_build.py          # build verification (ads.txt, sitemaps, noindex, meta, content>400w)
$PYTHON scripts/tests/test_encoding.py       # mojibake guard
firebase deploy --only hosting               # site
firebase deploy --only functions             # dashboard/autopilot backend
firebase deploy --only firestore:indexes     # after changing firestore.indexes.json
```

**Output:** ~2,916 base pages + 16,422 parametric variants + 24 static + 2,766 redirects = 19,362 URLs.

## Dashboard / Autogrowth Architecture

- **Frontend:** `src/admin.html` (single-page, tabs: Overview, Search Console, Content, Traffic,
  Conversions, Technical SEO, Opportunities, Alerts, Calculators CMS, Autopilot, Growth Lab,
  Strategy, AI Tools, Settings). Copied to `public/admin.html` on build.
- **Backend:** `functions/` — 51 Cloud Functions (Node 22):
  - GSC pipeline: `fetchGscData` (daily 3AM), `fetchGscOnDemand`, `getGscData` (types: queries,
    queries_raw, pages, site_stats, coverage), `getMovement`, `getIndexCoverage`
  - Analytics: `analytics` (event intake), `aggregateDailyStats` (daily 2AM), `getAggregatedData`
  - Alerts: `checkAlerts` (daily 4AM), `getAlerts`
  - CMS: `calcPage`, `sitemap`, `getCalcData`, `translateCalc`, `generateLongContent`, …
  - Autopilot brain: `runAutoPilot`, `autonomousGrowthLoop`, `dailyCoreRegeneration`,
    `findKeywordOpportunities`, `generateAllSEOTitlesHttp`, `backlinkHunterHttp`, …
- **Firestore collections:** `analytics_events`, `analytics_daily`, `gsc_search_data`,
  `gsc_page_stats` (90-day snapshots stamped with **endDate** — readers must use the LATEST
  snapshot only, never sum across dates), `gsc_site_stats`, `gsc_coverage`, `dashboard_alerts`,
  `calc_cms`, `seo_suggestions`, `admin_prefs`.

### Dashboard troubleshooting
- `getGscData` 500 → missing Firestore composite index. Check `firestore.indexes.json`,
  `firebase deploy --only firestore:indexes`.
- Pages tab empty → `gsc_page_stats` must be stamped with endDate (fixed 2026-07-21).
  Re-run `fetchGscOnDemand?days=30` after fixing.
- GSC data looks "stale" → GSC API has a 2–3 day lag. Normal.
- Hosting deploy 429 (storage quota) → Firebase Console → Hosting → Release settings →
  retain last 5 versions. See `docs/REACTIVATE_DEPLOY.md`.

## Duplicate Calculators (known, decision pending)

83 pairs of calc IDs are the SAME tool under two URLs (e.g. 023 & 1107 = laminate flooring,
200 & 501 & 932 = percentage). List: session of 2026-07-21, derivable from
`audit/truly_wrong.json` analysis. SEO-safe fix: pick a canonical ID per pair, 301-redirect
the other, remove from TOOLS. **Needs owner decision** — do not delete unilaterally.

## Session Log (recent)

### 2026-07-21 — Infrastructure + content uniqueness overhaul
- Reconciled repo fork (`C:\Users\julie\calctowork` vs `C:\Microsaas\obra`); canonical = this repo
- Fixed dashboard: added `gsc_site_stats` ASC index, fixed `gsc_page_stats` endDate stamping +
  latest-snapshot reads, recovered full autopilot function source, deployed all 51 functions
- Deployed Strategy-tab dashboard, noindex-on-parametric restored
- Audited 2,766 articles: fixed 470 wrong-article/wrong-language files, rewrote 440
  boilerplate articles (AI + validation). Remaining ~1,330 blocked on DeepSeek balance
- Found 83 duplicate-calculator pairs (decision pending)

# CalcToWork — Agent Guide

## ⚠️ CRITICAL WARNINGS

### NEVER Delete `src/content/` Files
The `src/content/{lang}/` directories contain **handcrafted, high-quality long-form articles** for each calculator. These are the site's most valuable SEO asset.

- **DO NOT** delete them to "regenerate" or "cache-bust".
- **DO NOT** run bulk scripts that remove `.html` files from `src/content/`.
- If a file is accidentally deleted, recover it immediately from Git history before running the build.

> **Historical Note:** On 2026-04-29, commit `3e89b42` deleted 2,228 non-EN content files, causing AdSense rejection due to thin content. They were recovered from commit `2b8e748`.

### Content Fallback Chain (Build-Time)
The generator uses this priority for long-form content:
1. `src/content/{lang}/{id}.html` — **PRIMARY** — Handcrafted articles
2. `LONG_CONTENT` dict in `calc_content.py` — 107 entries, mostly `es`/`en`
3. `CALC_FACTS` + `build_article_v2()` — **FALLBACK ONLY** — Category-based templates

**Rule:** If #1 exists, it is always used. Only delete or overwrite #1 if you have a BETTER replacement ready.

## Project Architecture

```
C:\Microsaas\obra
├── src/
│   ├── calculators/
│   │   └── calculators.json      # 441 calculator definitions (inputs, formulas, outputs)
│   ├── content/
│   │   ├── en/                   # 447 handcrafted EN articles (DO NOT DELETE)
│   │   ├── es/                   # 447 handcrafted ES articles (DO NOT DELETE)
│   │   ├── fr/                   # 447 handcrafted FR articles (DO NOT DELETE)
│   │   ├── de/                   # 443 handcrafted DE articles (DO NOT DELETE)
│   │   ├── it/                   # 447 handcrafted IT articles (DO NOT DELETE)
│   │   └── pt/                   # 444 handcrafted PT articles (DO NOT DELETE)
│   ├── i18n/
│   │   └── {es,en,fr,de,it,pt}.json   # UI translations + calc metadata
│   ├── templates/
│   │   ├── calculator.html.j2    # Main calculator page template
│   │   ├── index.html.j2         # Homepage template
│   │   ├── block.html.j2         # Category listing template
│   │   ├── static_page.html.j2   # Legal pages template
│   │   ├── sitemap.xml.j2        # Sitemap template
│   │   └── sitemap_index.xml.j2  # Sitemap index template
│   ├── css/
│   │   └── styles.css            # Global styles (dark mode supported)
│   ├── js/
│   │   ├── calculator.js         # Calculator engine v8.0
│   │   ├── dark-mode.js          # Theme toggle
│   │   └── favorites.js          # Favorites/bookmarks
│   ├── robots.txt                # Crawler directives
│   └── ads.txt                   # AdSense authorized sellers
├── scripts/
│   ├── generate_calctowork.py    # MAIN BUILD SCRIPT
│   ├── calc_content.py           # Content generation module
│   ├── tools_config.py           # Tool configurations + parametric variants
│   ├── fix_i18n.py               # I18n mojibake + description fixer
│   └── tests/                    # Automated tests
├── public/                       # Build output (generated, ephemeral)
├── firebase.json                 # Firebase Hosting config
└── AGENTS.md                     # This file
```

## Build Process

```bash
# Python path (required — Python 3.11+)
PYTHON = C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe

# 1. Install dependencies
$PYTHON -m pip install -r requirements.txt

# 2. Run the build
$PYTHON scripts/generate_calctowork.py

# 3. Verify output
$PYTHON scripts/verify_build.py

# 4. Deploy
firebase deploy --only hosting
```

**Output:**
- `public/` is wiped and regenerated
- ~2,916 base pages (461 calculators × 6 languages + block pages + index)
- ~16,422 parametric variant pages
- 24 legal/static pages
- ~19,362 total URLs across 6 per-language sitemaps

## Content Quality Tiers

| Tier | Source | Count | Quality | AdSense Risk |
|------|--------|-------|---------|--------------|
| A | `src/content/{lang}/` | ~2,680 files | Excellent, handcrafted, 1,000–3,000 words | Low |
| B | `LONG_CONTENT` dict | 107 entries | Good, manually written | Low |
| C | `build_article_v2()` | Fallback | Category-templated, ~800–1,100 words | Medium |

**Goal:** Maintain 100% Tier A coverage. Tier C should only be used for new calculators before their handcrafted article is ready.

## AdSense Compliance Checklist

Before every deploy, verify:
- [ ] `public/ads.txt` exists
- [ ] `public/sitemap.xml` exists
- [ ] Parametric variant pages have `<meta name="robots" content="noindex, follow">`
- [ ] All `seo_description` fields are non-empty and > 50 characters
- [ ] No double-encoded UTF-8 in i18n files
- [ ] `build_article_v2()` fallback usage is < 1% of pages

## Adding a New Calculator

1. Add definition to `src/calculators/calculators.json`
2. Add i18n metadata to `src/i18n/{lang}.json` for all 6 languages
3. Write long-form article to `src/content/{lang}/{id}.html` for all 6 languages
4. Run build and tests
5. Deploy

## Troubleshooting

### "Low-value content" AdSense rejection
- Check `src/content/` file counts per language
- Run `python scripts/check_en_quality.py` to find templated files
- If non-EN files are missing, restore from Git: `git checkout 2b8e748 -- src/content/{lang}/`

### Broken characters (�, Ã, etc.)
- Run `python scripts/fix_i18n.py`
- Verify with `python scripts/tests/test_encoding.py`

### Missing ads.txt after build
- Ensure `src/ads.txt` exists
- Check `copy_assets()` in `generate_calctowork.py` includes `"ads.txt"`

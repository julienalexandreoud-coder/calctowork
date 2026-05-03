# CalcToWork Full Audit Report
**Date:** 2026-05-02
**Site:** https://calcto.work
**Build Output:** ~450 MB | ~23,862 HTML pages | 6 languages

---

## Executive Summary

CalcToWork is a mature, well-architected programmatic SEO calculator site with **excellent content quality** (handcrafted long-form articles in 6 languages) and solid technical foundations. However, there are **critical gaps in performance optimization, monetization readiness, and conversion infrastructure** that are likely limiting revenue and growth.

**Overall Grade: B+** — Strong content, solid SEO, but under-optimized for speed, monetization, and user conversion.

---

## 1. SEO & Content Quality

### What's Working Well
- **Tier-A content coverage:** ~464 handcrafted HTML articles per language (exceeds calculator count)
- **Rich schema markup:** SoftwareApplication, Article, BreadcrumbList, FAQPage, HowTo structured data present
- **Hreflang implementation:** Proper alternate links across all 6 languages
- **Canonical URLs:** Correctly implemented on all page types
- **Meta descriptions:** Present and generally >50 characters
- **Sitemap architecture:** Clean per-language sitemaps with ~3,563 URLs each
- **Parametric variants:** Correctly noindexed to avoid thin content penalties
- **Breadcrumb navigation:** Visible and schema-backed
- **Open Graph & Twitter Cards:** Implemented consistently

### Issues Found
| Severity | Issue | Impact |
|----------|-------|--------|
| **Medium** | `datePublished` is block-based, not calculator-based. All calculators in block 1 show "2024-06-01" regardless of when they were actually added. | Freshness signals to Google are diluted |
| **Medium** | No `dateModified` updates in content files — articles appear stale even when updated | Crawlers may deprioritize "old" content |
| **Medium** | OG images (`/og/{block_slug}.png`) are **missing from build output** | Social shares show broken/missing images |
| **Low** | No `speakable` schema for voice search optimization | Missed opportunity for Google Assistant/Alexa |
| **Low** | No `VideoObject` schema (no video content at all) | Rich results eligibility gap |
| **Low** | Article schema `author` is generic Organization — no Person schema for E-E-A-T | Slightly weaker authority signals |
| **Low** | Missing `mainEntity` linkage between Article and SoftwareApplication schemas | Weaker entity understanding |

### Recommended Actions (SEO)
1. **Generate OG images** for all 17 block categories (1200×630 PNG) — currently missing entirely
2. **Implement per-calculator `datePublished`** and auto-update `dateModified` on each build
3. **Add `speakable` sections** to long-form content for voice search
4. **Create a video strategy:** Even simple 60-second screen recordings of calculators would unlock VideoObject schema
5. **Add Person schema** for a fictional "head of content" to boost E-E-A-T signals

---

## 2. Performance & Core Web Vitals

### Current State
| Asset | Size | Status |
|-------|------|--------|
| styles.css | 34 KB | Not minified |
| calculator.js | 31 KB | Not minified |
| analytics-tracker.js | 6.9 KB | Not minified |
| Total JS (all) | ~44 KB | No tree-shaking |
| HTML per page | ~15-25 KB | Not minified |
| Build total | ~450 MB | Very large |

### Issues Found
| Severity | Issue | Impact |
|----------|-------|--------|
| **Critical** | **HTML, CSS, and JS are NOT minified** in production build. `csscompressor` and `rjsmin` are imported but never actually used in the build pipeline. | +20-30% file sizes, slower LCP |
| **High** | **No image optimization pipeline.** No WebP/AVIF generation. No responsive images. OG images missing entirely. | Poor LCP on slow connections |
| **High** | **No lazy loading** on most assets. KaTeX CSS/JS loaded synchronously on every page with formulas, even when formulas are simple. | Unnecessary render-blocking |
| **High** | **No resource preloading.** Critical CSS is not inlined. Fonts (system fonts used, so this is okay) but no `preload` for CSS/JS. | Slower FCP |
| **Medium** | **Firebase cache headers:** HTML cached for only 1 hour (`max-age=3600`). For a static site, this is unnecessarily short. | Higher hosting costs, slower repeat visits |
| **Medium** | **No service worker / PWA.** No offline capability. No add-to-homescreen prompt. | Missed engagement opportunity |
| **Medium** | **No HTTP/2 Server Push** (not configurable on Firebase Hosting anyway, but worth noting) | — |
| **Low** | `analytics-tracker.js` fires `setInterval` every 10 seconds for time-on-page tracking | Slight battery drain on mobile |

### Recommended Actions (Performance)
1. **Enable minification:** Actually call `csscompressor.compress()` and `rjsmin.jsmin()` in `generate_calctowork.py`
2. **Inline critical CSS** for above-the-fold content (header, hero, calculator form)
3. **Add `loading="lazy"`** to all non-critical images (already on diagrams, but missing elsewhere)
4. **Generate WebP/AVIF OG images** and use `<picture>` elements where applicable
5. **Increase HTML cache to 24h** and add `immutable` to versioned assets
6. **Implement a service worker** for offline calculator usage (huge UX win for a tool site)
7. **Defer non-critical KaTeX** — only load when math elements are actually present

---

## 3. Monetization & Revenue

### Current State
- AdSense publisher ID configured (`ca-pub-3048983871829953`)
- 3 ad slots defined (banner, in-article, responsive) but **NO slot IDs configured**
- 10 affiliate offers mapped to specific calculators
- Email capture form present for "PDF report" but **no actual PDF generation**

### Issues Found
| Severity | Issue | Impact |
|----------|-------|--------|
| **Critical** | **AdSense slot IDs are empty.** `ADSENSE_SLOT_BANNER`, `ADSENSE_SLOT_INARTICLE`, `ADSENSE_SLOT_RESPONSIVE` all rely on environment variables that appear unset. Ads may not render correctly or at all. | **Zero ad revenue potential** |
| **Critical** | **Email capture promises a PDF that is never generated.** The `email-capture.js` just sends data to a webhook (also unconfigured) and shows a fake "Check your inbox" message. | **User trust destruction, potential fraud complaints** |
| **High** | **Only 10 calculators have affiliate offers** out of 461. Massive untapped monetization. | Leaving money on the table |
| **High** | **No affiliate disclosure** in footer — only a small "Ad" badge on the CTA box. FTC/EU compliance risk. | Legal liability |
| **Medium** | **No premium/upselld positioning.** No "Pro" features, no email list building, no lead magnets beyond the fake PDF. | No recurring revenue stream |
| **Medium** | **No Amazon Associates** or commerce-focused affiliates for construction material calculators (huge opportunity). | Missed high-intent buyer traffic |
| **Low** | **Ad refresh on calculate** has 30s cooldown but no viewability check before refresh. | Potential AdSense policy violation |

### Recommended Actions (Monetization)
1. **URGENT:** Set actual AdSense slot IDs in environment variables or hardcode them
2. **URGENT:** Either implement real PDF generation (via `html2pdf.js` or serverless function) or remove the email capture entirely
3. **Expand affiliates:** Add Amazon Associates links for construction materials, tools, fitness equipment, financial services
4. **Add proper disclosure:** "CalcToWork earns commissions from qualifying purchases" in footer
5. **Create a real lead magnet:** "Construction Materials Checklist PDF" or "Kitchen Renovation Budget Template"
6. **Add a "Pro" tier concept:** Save calculations to account, multi-project tracking, export to Excel

---

## 4. UX/UI & Conversion

### What's Working Well
- Clean, modern design with dark mode support
- Responsive layout (mobile-first)
- Unit conversion system is robust
- Favorites/bookmarks system via localStorage
- Calculator sharing (WhatsApp, Twitter, Facebook)
- Copy results to clipboard
- Comparison tables for preset sizes
- Sticky TOC on long-form articles

### Issues Found
| Severity | Issue | Impact |
|----------|-------|--------|
| **High** | **No search results page / no search index.** Search is purely client-side filtering of the homepage grid. No deep search across calculator descriptions. | Poor discoverability for 461 calculators |
| **Medium** | **Project Tally feature is half-built.** UI exists but "Add to Project" button shows/hides but there's no project management logic in `calculator.js`. | Broken user expectation |
| **Medium** | **No calculator history / recent calculations.** Users lose their work on page refresh. | Friction for power users |
| **Medium** | **Feedback buttons (👍/👎) are non-functional.** They show a "Thanks!" message but don't actually send data anywhere. | Missed qualitative data |
| **Medium** | **Cookie consent banner is English-only** and hardcoded. Shows "Learn more" link to `/en/privacy/` regardless of user language. | GDPR compliance risk for non-EN users |
| **Low** | **No keyboard shortcuts** (e.g., Ctrl+Enter to calculate). | Accessibility gap |
| **Low** | **No print styles.** Printing a calculator page includes ads, headers, footers. | Poor offline usability |
| **Low** | **No onboarding for first-time users.** 461 calculators is overwhelming with no guidance. | Higher bounce rate |

### Recommended Actions (UX)
1. **Implement a real search index** (lunr.js or Pagefind) for full-text search across all calculators
2. **Either finish Project Tally** or remove the UI elements entirely
3. **Add recent calculations** to localStorage (last 10 calculations per user)
4. **Wire up feedback buttons** to Firestore or at least GA4 events
5. **Localize cookie consent** per language with correct privacy policy links
6. **Add `Ctrl+Enter` shortcut** for calculate
7. **Create a "Getting Started" guided tour** for new visitors

---

## 5. Technical Architecture

### What's Working Well
- Clean static site generator (Python + Jinja2)
- Multi-language architecture is robust
- Content fallback chain (handcrafted → LONG_CONTENT → generated)
- Automated tests for build verification
- Firebase Hosting with proper security headers (X-Content-Type-Options, X-Frame-Options)
- Firestore analytics backend with batch writes
- Legacy URL redirects handled

### Issues Found
| Severity | Issue | Impact |
|----------|-------|--------|
| **High** | **Firebase config (API key) is exposed in client-side HTML.** While this is standard for Firebase, there's no domain restriction configured. | Abuse risk — anyone can use your Firebase project |
| **Medium** | **No Content Security Policy (CSP) header.** No protection against XSS via injected scripts. | Security vulnerability |
| **Medium** | **No HSTS header** in Firebase config. | MITM attack risk |
| **Medium** | **Cloud Function has no rate limiting or authentication.** The `/analytics` endpoint accepts unlimited POSTs from any origin. | Cost abuse, data poisoning |
| **Medium** | **No input validation/sanitization** in the analytics Cloud Function. Events are written directly to Firestore without schema validation. | Data corruption |
| **Low** | **No CI/CD pipeline.** No GitHub Actions for build + test + deploy automation. | Human error risk, slow deployments |
| **Low** | **No automated broken link checker.** With 23,862 pages, broken internal links are inevitable. | SEO crawl budget waste |
| **Low** | **No automated visual regression testing.** | Design bugs slip through |
| **Low** | **Build script imports optional minifiers but doesn't use them.** Dead code. | Maintenance clutter |

### Recommended Actions (Technical)
1. **Add Firebase App Check** or domain restriction to prevent API key abuse
2. **Add CSP header** to Firebase config: `script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://pagead2.googletagmanager.com https://cdn.jsdelivr.net https://www.gstatic.com;`
3. **Add HSTS header:** `Strict-Transport-Security: max-age=31536000; includeSubDomains`
4. **Rate-limit the analytics endpoint** (max 100 requests/IP/minute)
5. **Add schema validation** to Cloud Function before writing to Firestore
6. **Set up GitHub Actions CI/CD:** Build → Test → Deploy on push to main
7. **Add broken link checker** to build pipeline (e.g., `htmltest`)
8. **Remove unused minifier imports** or actually implement them

---

## 6. Analytics & Data

### What's Working Well
- GA4 configured with anonymized IPs
- Custom events: calculate, copy, share, scroll_depth, ad_view, affiliate_click
- Firestore event tracking with session/user IDs
- Scroll depth tracking (25/50/75/100%)
- Ad viewability tracking via IntersectionObserver
- Exit intent detection

### Issues Found
| Severity | Issue | Impact |
|----------|-------|--------|
| **Medium** | **Duplicate tracking systems.** Both GA4 (via gtag) and Firestore (via analytics-tracker.js) track the same events. Data discrepancy risk. | Inconsistent reporting |
| **Medium** | **Firestore writes happen on EVERY page** for every user (no sampling). At scale, this will be expensive. | Cost explosion at high traffic |
| **Medium** | **No conversion goals defined in GA4.** No funnel tracking from search → calculator → calculate → affiliate click. | Can't optimize conversion paths |
| **Low** | **Time-on-page tracking uses `setInterval` every 10 seconds** rather than `sendBeacon` on unload. | Inaccurate session duration |
| **Low** | **No A/B testing framework** (Google Optimize sunset, no replacement). | Can't test copy/layout changes |
| **Low** | **No heatmap or session recording** (Hotjar, Clarity). | No qualitative UX insights |

### Recommended Actions (Analytics)
1. **Consolidate tracking:** Use GA4 as primary, send Firestore only for "important" events (calculate, affiliate_click) with 10% sampling
2. **Set up GA4 conversion events:** `calculate`, `affiliate_click`, `email_capture`
3. **Add Microsoft Clarity** (free) for heatmaps and session recordings
4. **Implement `navigator.sendBeacon`** for reliable exit tracking
5. **Create a simple A/B test framework** using URL parameters + localStorage

---

## 7. Security & Compliance

### Issues Found
| Severity | Issue | Impact |
|----------|-------|--------|
| **High** | **No CSP header** (see Technical section) | XSS vulnerability |
| **Medium** | **Cookie consent is not GDPR-compliant** for non-EN users and lacks granular control (no "Analytics only" vs "Ads only" option). | Regulatory risk in EU |
| **Medium** | **Privacy policy hardcoded in build script** rather than as editable content files. Updates require code changes. | Compliance maintenance burden |
| **Low** | **No DMCA or takedown policy page.** | Legal exposure |

### Recommended Actions
1. Implement granular cookie consent (Essential / Analytics / Advertising toggles)
2. Move legal pages to editable markdown/content files
3. Add a DMCA/Takedown page

---

## 8. Content Gaps & Expansion Opportunities

### Identified Gaps
1. **Missing calculators:** No roofing, no solar panel sizing, no concrete slump test, no drywall mud calculator, no staircase stringer calculator
2. **No blog/news section** for topical content (e.g., "How inflation affects construction costs in 2026")
3. **No glossary/tooltip system** for technical terms (E-E-A-T opportunity)
4. **No user-generated content** (reviews, tips, alternative methods)
5. **No country/region-specific versions** beyond language (e.g., building codes differ Spain vs Mexico)

### Recommended Actions
1. Add 20-30 high-demand calculators based on GSC zero-CTR queries
2. Create a "Blog" or "Guides" section for long-tail SEO
3. Add tooltip definitions for technical terms (automatically linked)

---

## Priority Action Matrix

| Priority | Action | Effort | Expected Impact |
|----------|--------|--------|-----------------|
| **P0** | Fix AdSense slot IDs | 15 min | Revenue unlock |
| **P0** | Fix or remove fake PDF email capture | 30 min | Trust/legal fix |
| **P1** | Enable HTML/CSS/JS minification | 1 hour | +10-15% page speed |
| **P1** | Generate OG images for all blocks | 2 hours | Social sharing boost |
| **P1** | Add Firebase App Check / domain restriction | 1 hour | Security |
| **P1** | Localize cookie consent banner | 1 hour | GDPR compliance |
| **P2** | Implement real search index | 4 hours | UX + engagement |
| **P2** | Expand affiliate coverage to 50+ calculators | 4 hours | Revenue |
| **P2** | Add CSP + HSTS headers | 1 hour | Security |
| **P2** | Fix Project Tally or remove it | 2 hours | UX |
| **P3** | Add service worker for offline use | 4 hours | Engagement + PWA |
| **P3** | Implement real PDF generation | 8 hours | Lead gen |
| **P3** | Set up CI/CD pipeline | 3 hours | Dev velocity |
| **P3** | Add Microsoft Clarity | 30 min | UX insights |

---

## Quick Wins (Do Today)
1. Set `ADSENSE_SLOT_BANNER`, `ADSENSE_SLOT_INARTICLE`, `ADSENSE_SLOT_RESPONSIVE` env vars
2. Remove or implement the email-capture PDF promise
3. Add `csscompressor.compress()` and `rjsmin.jsmin()` calls to the build script
4. Generate 17 OG images (one per block category)
5. Localize the cookie consent banner for all 6 languages
6. Wire up feedback buttons to at least send a GA4 event
7. Add CSP and HSTS headers to `firebase.json`

---

*This audit was generated by analyzing the full CalcToWork codebase including build scripts, templates, frontend code, Firebase configuration, and content structure.*

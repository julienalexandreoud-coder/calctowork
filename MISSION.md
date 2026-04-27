# CalcToWork — Project Mission & Roadmap

**Goal:** Become the #1 free calculator site in Spanish + 5 other languages, matching and eventually surpassing OmniCalculator (3,842 calculators, 14 categories) in content depth and tool breadth.

**Live site:** https://calcto.work  
**Tech stack:** Python static site generator (Jinja2) → Firebase Hosting  
**Languages:** es, en, fr, pt, de, it  
**Generator:** `C:\Microsaas\obra\scripts\generate_calctowork.py`  
**Python path:** `C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe`  
**Deploy cmd:** `firebase deploy --only hosting` (from `C:\Microsaas\obra`)

---

## Current State (as of 2026-04-23)

| Metric | Value |
|--------|-------|
| Base calculators | 103 |
| Parametric variant pages | 18,558 |
| Total URLs in sitemap | 19,236 |
| Categories | 9 (all construction) |
| Google-indexed pages | ~50 (was 50/17k — indexation bugs fixed 2026-04-22) |
| Languages | 6 (es, en, fr, pt, de, it) |

### Current Categories (all construction)
1. `estructuras` — Concrete & structures
2. `mamposteria` — Masonry & walls
3. `pavimentos` — Floors & tiling
4. `fontaneria` — Plumbing & water
5. `electricidad` — Electrical
6. `climatizacion` — HVAC & climate
7. `carpinteria` — Carpentry & joinery
8. `pintura` — Paint & coatings
9. `gestion` — Project management & costs

---

## Target State

| Metric | Target |
|--------|--------|
| Base calculators | 3,800+ |
| Parametric variants | 100,000+ |
| Total URLs | 500,000+ |
| Categories | 20+ |
| Google impressions/day | 10,000+ |

### Target Categories (matching OmniCalculator)
| # | Category | OmniCalc count | Our target |
|---|----------|---------------|-----------|
| 1 | Math | 679 | 300+ |
| 2 | Finance | 602 | 250+ |
| 3 | Health | 436 | 200+ |
| 4 | Physics | 537 | 150+ |
| 5 | Statistics | 194 | 100+ |
| 6 | Everyday life | 281 | 200+ |
| 7 | Conversion | 318 | 150+ |
| 8 | Construction (existing) | 156 | 150+ |
| 9 | Biology | 107 | 80+ |
| 10 | Chemistry | 107 | 80+ |
| 11 | Food | 70 | 60+ |
| 12 | Sports | 110 | 80+ |
| 13 | Ecology | 34 | 40+ |
| 14 | Other | 211 | 100+ |

---

## Feature Gap vs OmniCalculator

### Missing Features (priority order)

#### P1 — Critical for SEO & UX
- [ ] **Long educational content per calculator** (500–3,500 words): "What is X", formula explanation, worked example, when to use it. Currently only block-level generic content exists. Need per-calculator long_content in calc_content.py.
- [ ] **Per-calculator FAQ** (not just block-level): 4–6 specific Q&As per calculator keyed by calc ID.
- [ ] **Unit switching**: metric ↔ imperial toggle on inputs (OmniCalc shows e.g. m/ft, kg/lb simultaneously)
- [ ] **Table of contents**: Anchored links to sections on long content pages

#### P2 — Important for UX
- [ ] **Multiple calculation modes**: Some calculators solve for different unknowns (e.g. "what area can I paint?" vs "how much paint do I need?"). Currently only one direction.
- [ ] **Graphs/charts**: Amortization chart, pie chart of results (mortgage, finance calcs)
- [ ] **Dropdown/select inputs**: Some inputs should be dropdowns (material type, loan frequency, etc.)
- [ ] **Slider inputs**: Good UX for percentage, years, etc.
- [ ] **Save/share results**: URL-encoded state sharing (currently basic share button exists)
- [ ] **Embed functionality**: `<iframe>` embed code for third-party sites

#### P3 — Nice to have
- [ ] **Author attribution**: Expert reviewer name/credentials
- [ ] **Tags/filters**: Filter calculators by topic
- [ ] **Search**: Site-wide calculator search
- [ ] **Dark mode**: Already have CSS vars, just need toggle
- [ ] **Print-friendly results**: CSS print styles

---

## Implementation Roadmap

### Phase 1: Expand to 200 calculators + long content (CURRENT PHASE)
**Goal:** Add 97 new calculators across 6 new categories. Add long content infrastructure.

**New categories to add:**
- `matematicas` — Math (percentage, fractions, geometry, algebra)
- `finanzas` — Finance (mortgage, loan, interest, salary, tax, tip)
- `salud` — Health (BMI, calories, heart rate, water intake)
- `cotidiano` — Everyday life (age, date diff, tip, unit converter)
- `estadistica` — Statistics (mean, std dev, probability)
- `ciencia` — Science / Physics (speed, density, energy)

**Content:** Add `CALC_LONG_CONTENT` dict in calc_content.py with per-calculator long HTML content (es + en + fr + pt + de + it). Start with top 30 highest-volume calculators.

**Status:** IN PROGRESS (session 2026-04-23)

---

### Phase 2: COMPLETE (2026-04-25)
- 188 calculators across 17 categories
- Long-form SEO articles (es+en) for top 20 calculators — ~1,500 words per page
- Block-aware intro templates fixed (no more "construction professionals" for math/health)
- 1,236 base pages, 19,794 total URLs, deployed to https://calcto.work

### Phase 3: Expand to 500 calculators (next session)
- Add long-form content for remaining 168 calculators (50 words → 500 words each)
- Add remaining math subcategories (algebra, trigonometry, sequences)
- Add full finance suite (investment, retirement, equity)
- Add biology, chemistry, food calculators

### Phase 3: Expand to 1,000 calculators
- Add biology, chemistry, ecology calculators
- Add food calculators (cooking measurements, nutrition)
- Add physics simulators
- Implement unit switching (metric/imperial toggle)
- Add graphs for mortgage, loan amortization

### Phase 4: Expand to 2,000+ calculators
- Programmatic generation from formula templates
- Parametric variants dramatically expand long-tail pages
- Target: 50k+ indexed pages

### Phase 5: Expand to 3,800+ calculators
- Full parity with OmniCalculator
- Add remaining niche calculators
- Full long content for all calculators
- Expert review attribution

---

## Key Technical Files

| File | Purpose |
|------|---------|
| `scripts/generate_calctowork.py` | Main generator — builds all HTML pages |
| `scripts/calc_content.py` | Content: how-to steps, FAQs, formulas, intros, long content |
| `scripts/tools_config.py` | TOOLS list (calc IDs + 6-lang slugs) + PARAMETRIC_VARIANTS |
| `src/calculators/calculators.json` | Calculator definitions: formula (JS), inputs, outputs |
| `src/i18n/{lang}.json` | Translations: name, description, SEO title/desc, input/output labels |
| `src/templates/calculator.html.j2` | Jinja2 page template |
| `src/css/styles.css` | All styles |

---

## Calculator ID Ranges

| Range | Category |
|-------|---------|
| 001–100 | Construction (estructuras, mamposteria, etc.) |
| 101–200 | Pool, garden, fence + reserved |
| 200–299 | Math (matematicas) |
| 300–399 | Finance (finanzas) |
| 400–499 | Health (salud) |
| 500–599 | Everyday life (cotidiano) |
| 600–699 | Statistics (estadistica) |
| 700–799 | Science / Physics (ciencia) |
| 800–899 | Conversion (conversion) |
| 900–999 | Sports (deportes) |
| 1000+ | Additional categories |

---

## Session Log

### 2026-04-22 — Session 1: Foundation fixes
- Fixed empty parametric page content (was blank → now has intro text)
- Fixed wrong canonicals on variant pages (all pointed to parent → now point to own URL)
- Added popular combos grid to base calculator pages (crawler discovery)
- Split sitemap by language (6 files + index)
- Added pre-computed quick answers to variant page intros
- Added 3 new calculators: Swimming Pool Volume (101), Garden Topsoil (102), Fence Posts (103)
- Result: 18,558 variant pages generated, deployed

### 2026-04-23 — Session 2: Indexation analysis + Phase 1 start
- Fixed NameError in generator (chunks reference after sitemap refactor)
- Deployed 19,236 URLs successfully
- Identified feature gap vs OmniCalculator
- Created MISSION.md (this file)
- **STARTED PHASE 1**: Adding math, finance, health, everyday life categories

---

## Session 2 Progress (2026-04-23) — STOPPED MID-IMPLEMENTATION

### ✅ Completed this session
1. Created this MISSION.md
2. Added 20 new calculators to `src/calculators/calculators.json`:
   - 200 porcentaje, 201 cambio-porcentual, 202 area-rectangulo, 203 pitagoras, 204 regla-de-tres
   - 300 hipoteca, 301 prestamo, 302 interes-compuesto, 303 interes-simple, 304 calculadora-iva, 305 salario-neto, 306 descuento, 307 punto-de-equilibrio
   - 400 imc-bmi, 401 calorias-diarias, 402 peso-ideal, 403 agua-diaria
   - 500 propina, 501 calculadora-edad, 502 diferencia-fechas
3. Added all 20 entries to `scripts/tools_config.py` TOOLS list (with 6-lang slugs for each)

### ✅ ALL DONE — Phase 1 complete (2026-04-24)

### Phase 2 — start here next session

**STEP 1 (do first): Add i18n entries to all 6 language files**

Each of the 6 files (`src/i18n/es.json`, `en.json`, `fr.json`, `pt.json`, `de.json`, `it.json`) needs:

A) New `block_slugs` entries:
```json
"matematicas": "Matemáticas",
"finanzas": "Finanzas",
"salud": "Salud",
"cotidiano": "Vida Cotidiana"
```

B) New `block_descriptions` entries (one paragraph per block per language)

C) 20 new calculator entries under `"calculators"` key — each needs:
- `name`, `desc`, `seo_title`, `seo_desc`, `inputs` (obj), `outputs` (obj)

The 20 calculator IDs to add: 200, 201, 202, 203, 204, 300, 301, 302, 303, 304, 305, 306, 307, 400, 401, 402, 403, 500, 501, 502

**STEP 2: Add calc_content.py block content for 4 new blocks**

File: `scripts/calc_content.py`
Add to HOWTO, FAQS, FORMULA_EXPLAINED dicts for:
- `"matematicas"` — math how-to steps + FAQ
- `"finanzas"` — finance how-to steps + FAQ  
- `"salud"` — health how-to steps + FAQ
- `"cotidiano"` — everyday life how-to steps + FAQ

**STEP 3: Add long content infrastructure**

Add a `LONG_CONTENT` dict in calc_content.py keyed by calc_id for the top 10 calcs.
Add a `long_content` section to `src/templates/calculator.html.j2`.

**STEP 4: Regenerate, test, deploy**
```
cd C:\Microsaas\obra
C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe scripts/generate_calctowork.py
firebase deploy --only hosting
```

**STEP 5: Git commit all changes**

**STEP 6 (future sessions): Add more calculators**
Next batch: statistics (600s), science/physics (700s), conversions (800s), sports (900s)
Target: 500 calculators by end of Phase 2

---

## Notes for AI Assistant

- Always use full Python path: `C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe`
- Write JSON files with UTF-8 without BOM: `[System.IO.File]::WriteAllText(path, content, [System.Text.Encoding]::UTF8)` — PowerShell's default adds BOM which breaks JSON parsing
- The generator writes to `C:\Microsaas\obra\public\` — deploy from `C:\Microsaas\obra` with `firebase deploy --only hosting`
- Calculator IDs in tools_config.py TOOLS list must match IDs in calculators.json
- Each new block needs: HOWTO, FAQS, FORMULA_EXPLAINED entries in calc_content.py (all 6 langs)
- i18n structure per calc: `name`, `desc`, `seo_title`, `seo_desc`, `inputs` (obj), `outputs` (obj)
- Parametric variants expand base pages × N combinations — use them for high-volume keyword clusters

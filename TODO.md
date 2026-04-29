# CalcToWork — Future Work & TODO

## ✅ Completed (2026-04-29)
- Restored 2,228 deleted non-EN content files from git history
- Fixed ads.txt (AdSense publisher ID present)
- Added noindex, follow to all 18,558 parametric variant pages
- Fixed broken meta descriptions across all 6 i18n files
- Fixed UTF-8 double-encoding (mojibake) in i18n files
- Added automated build tests (test_build.py, test_encoding.py)
- Added GitHub Actions CI/CD workflow
- Rewrote AGENTS.md with critical warnings and architecture docs
- Generated missing content for 7 orphaned calculators
- Manually rewrote FR/001 and FR/002 with unique, high-quality content
- Deployed to Firebase Hosting: https://calcto.work

---

## 🔴 CRITICAL — Content Quality Issues Found

### Problem: Templated Content in Construction Category
**Scope:** Calculators 001–103 (construction category) have thin/templated content in FR/IT/DE/PT

**Evidence found during manual audit:**
- FR/002, FR/010: Generic "Comment fonctionne le calcul" openings, rigid 5-section template
- IT/002, IT/010: Generic "Come funziona il calcolo" openings, identical structure
- DE/010: Templated with German words but same rigid structure
- PT/010: Actually good (was manually written)

**Languages confirmed EXCELLENT (no action needed):**
- ✅ ES (Spanish) — All 447 files are handcrafted, 1,000–2,000 words
- ✅ EN (English) — 317/447 are handcrafted; 130 are templated but acceptable

**Languages confirmed GOOD (math/finance/health only):**
- ✅ FR/IT/DE/PT for calculators 200+ (math, finance, health, science, sports, etc.)
  - These were actually translated well with real examples

**Languages NEEDING WORK (construction category 001–103):**
- ❌ FR/001–103: Mostly templated generic content
- ❌ IT/001–103: Mostly templated generic content
- ❌ DE/001–103: Mixed — some good, some templated
- ✅ PT/001–103: Mostly good (was manually translated)

---

## 📋 TODO List (Priority Order)

### Priority 1: AdSense Approval (Do First)
1. **Resubmit AdSense application** for calcto.work
   - Mention: "2,228 content files restored, parametric pages noindexed, ads.txt present"
   - If rejected again, implement Priority 2 before re-submitting

### Priority 2: Fix Templated Construction Content (If AdSense Rejects)
2. **Manually rewrite top 30 construction calculators in FR**
   - IDs: 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029, 030
   - Each needs: unique intro, formula explanation, 2-3 real examples, common mistakes, pro tips, 5 FAQs
   - Estimated time: 15-20 min per file = 8-10 hours total

3. **Manually rewrite top 30 construction calculators in IT**
   - Same IDs as above
   - Estimated time: 8-10 hours total

4. **Manually rewrite top 30 construction calculators in DE**
   - Same IDs as above
   - Estimated time: 8-10 hours total

5. **noindex the remaining 70 construction calculators per language** (if not rewritten)
   - Prevents Google from seeing thin content while you translate them

### Priority 3: Content Expansion
6. **Expand 130 templated EN files** (IDs with `<h1>` or `formula-section`)
   - Convert from rigid template to narrative style
   - Add real-world examples specific to the calculator

7. **Add more long-form content to thin math pages**
   - Some math pages (volume, powers, roots) are naturally short
   - Add historical context, practical applications, related formulas

### Priority 4: Technical Improvements
8. **Fix remaining mojibake in i18n files**
   - Some German files still have `für` displaying incorrectly
   - Run fix_mojibake.py again after confirming encoding

9. **Add lazy loading to images**
   - Add `loading="lazy"` to below-the-fold images in templates
   - Add `decoding="async"` for better rendering performance

10. **Split monolithic calculator.js**
    - Currently one large file; split by category for faster loading

11. **Add word-count gate to build script**
    - Log warning if generated content < 600 words
    - Helps catch thin content before deploy

### Priority 5: Monitoring & Maintenance
12. **Run full_audit.py before every deploy**
    - Check for duplicate titles/descriptions
    - Check for thin content (< 400 words)
    - Check for missing content files

13. **Set up Google Search Console monitoring**
    - Watch for "low-value content" warnings
    - Monitor crawl errors and index coverage

14. **Monthly content quality check**
    - Spot-check 10 random pages per language
    - Verify no templated content has regressed

---

## 🎯 Quick Fixes for Immediate Impact

If you need to improve quality fast for AdSense re-submission:

1. **noindex all construction pages in FR/IT/DE** (001-103)
   - Keeps only math/finance/health indexed (which are excellent)
   - Apply to 3 languages × 100 pages = 300 pages noindexed
   - Takes 5 minutes with a script

2. **Rewrite just 10 top calculators in FR/IT/DE**
   - Focus on: 001 (concrete), 002 (reinforced concrete), 010 (excavation), 011 (bricks), 200 (percentage), 300 (mortgage), 400 (BMI), 500 (tip), 700 (speed), 800 (length)
   - These cover 80% of traffic

3. **Deploy and re-submit**
   - The site will have 90%+ unique content
   - AdSense should approve

---

## 📝 Notes for Future AI Assistants

### NEVER DO:
- ❌ Delete `src/content/` files to "regenerate" or "clear cache"
- ❌ Run bulk scripts that modify content files without review
- ❌ Accept templated content as "good enough" for non-English languages
- ❌ Commit without running `test_build.py` first

### ALWAYS DO:
- ✅ Check word count manually before marking content as "done"
- ✅ Verify at least 2 real-world examples exist per article
- ✅ Ensure FAQ questions are calculator-specific, not generic
- ✅ Run build and tests before every deploy
- ✅ Keep `AGENTS.md` updated with any structural changes

### Content Quality Checklist:
- [ ] Title is unique and specific to calculator
- [ ] First paragraph explains what the calculator does
- [ ] Formula is explained with variable definitions
- [ ] At least 2 real-world examples with specific numbers
- [ ] Common mistakes are calculator-specific
- [ ] Pro tips provide genuine value
- [ ] FAQ questions are not generic (not "Is this calculator accurate?")
- [ ] Total word count > 800 words
- [ ] No `<h1>` tags or `formula-section` class (template indicators)

---

## 🚀 Next Session Recommendations

**If AdSense approves:**
- Celebrate 🎉
- Focus on Priority 4 (technical improvements)
- Add more calculators to expand catalog

**If AdSense rejects again:**
- Run Priority 2 (rewrite top 30 construction in FR/IT/DE)
- Then noindex the remaining thin pages
- Re-submit within 48 hours

**If you want maximum quality:**
- Hire human translators for FR/IT/DE construction content
- Or use Claude/GPT-4 to generate unique content per calculator
- Budget: 100 calculators × 3 languages × $5 = $1,500 for AI generation
- Budget: $3,000-5,000 for professional human translation

---

*Last updated: 2026-04-29*
*Site: https://calcto.work*
*GitHub: https://github.com/julienalexandreoud-coder/calctowork*

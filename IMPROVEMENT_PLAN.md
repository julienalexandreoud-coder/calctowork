# CalcToWork — #1 Calculator Site Improvement Plan

## Problem
407/441 calculators use identical 5-section template content. Google penalizes templated/thin content. To rank #1, every page must be genuinely unique, valuable, and substantial.

## Phase 1: Unique Rich Content Engine (HIGHEST PRIORITY)
Goal: Every calculator gets 1000+ words of genuinely unique content per language.

### 1.1 Upgrade `build_article_from_facts()` → `build_article_v2()`
- **Varied section structures**: 8+ different article layouts (not 1 template)
  - Math calculators: Formula → Real Example → Common Mistakes → Applications → FAQ
  - Health calculators: Why It Matters → How To Measure → Understanding Results → Ranges → FAQ  
  - Finance calculators: Formula → Real-World Example → Tips → Tax Implications → FAQ
  - Physics calculators: Theory → Lab Example → Unit Conversions → Safety → FAQ
  - Each category gets its OWN section headings and paragraph templates
- **Multiple examples** (not just 1): 2-3 worked examples per calculator
- **Contextual paragraphs**: Calculator-specific intro (not "This calculation is fundamental in science...")
- **Common mistakes section**: Unique per calculator type
- **Pro tips / expert advice**: Unique per category
- **Related formulas section**: Link to related calculators
- **Real-world application stories**: Mini scenario per category
- **Extended FAQ**: 4-6 questions per calculator (not 2)
- **Target**: ~800-1200 words per article

### 1.2 Write LONG_CONTENT for Top 30 Calculators
Hand-craft 1500+ word articles for the highest-traffic calculators:
- 200 (Percentage), 201 (Percentage Change), 202 (Rectangle Area), 203 (Triangle Area)
- 204 (Rule of Three), 205 (Pythagorean), 210 (Circle Area), 300 (BMI), etc.
- Each gets unique section headers, 3+ examples, expert tips, common mistakes
- Spanish versions get full Spanish content (not translated template text)

### 1.3 Eliminate ALL Generic Phrases
Audit and replace patterns like:
- "This calculation is fundamental in science, engineering, medicine, and education"
- "Understanding the formula lets you verify results"
- "If the result seems incorrect, check that you have entered the correct units"

## Phase 2: Structured Data for Rich Results
### 2.1 JSON-LD SoftwareApplication
Add to every calculator page:
```json
{
  "@type": "SoftwareApplication",
  "name": "Calculator Name",
  "applicationCategory": "UtilityApplication",
  "operatingSystem": "Web",
  "offers": { "@type": "Offer", "price": "0" }
}
```

### 2.2 JSON-LD HowTo
Add step-by-step instructions:
```json
{
  "@type": "HowTo",
  "name": "How to use [Calculator Name]",
  "step": [
    { "@type": "HowToStep", "text": "Enter [input1]..." },
    { "@type": "HowToStep", "text": "The calculator applies the formula..." },
    { "@type": "HowToStep", "text": "Review your result: [output]..." }
  ]
}
```

### 2.3 JSON-LD FAQPage
Expose the FAQ accordion as structured data for rich snippets.

## Phase 3: UX Improvements
### 3.1 Slider Inputs
Add range sliders for numeric inputs with min/max/step from calculators.json
- Shows current value next to slider
- Mobile-friendly touch slider
- Visual feedback on drag

### 3.2 Bookmark/Favorites
- Heart icon on each calculator
- "My Calculators" section on homepage
- localStorage persistence
- Sort by most-used

### 3.3 Copy Results Enhancement
- "Copy all results" button
- Formatted text output (not just raw numbers)
- Share via link (already exists, enhance)

### 3.4 Visual Feedback
- Result area highlights on calculation
- Animated number transitions
- Color-coded result ranges (green=good, yellow=moderate, red=concerning) for health calculators

## Phase 4: SEO & Indexing
### 4.1 Google Search Console
- Submit sitemap.xml
- Request indexing for all calculator pages
- Monitor crawl errors

### 4.2 Internal Linking
- "Related calculators" section on every page (already partially exists)
- Cross-link within article content
- Breadcrumb structured data

### 4.3 Page Speed
- Preload critical CSS
- Lazy load below-fold content
- Optimize images (if any)

## Phase 5: Continuous Improvement Loop
- Monitor GA4 for top calculators by traffic
- A/B test content structures
- Add LONG_CONTENT for next batch of popular calculators
- Monitor search rankings and adjust content
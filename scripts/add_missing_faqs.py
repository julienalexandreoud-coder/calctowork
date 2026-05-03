#!/usr/bin/env python3
"""Add basic FAQ sections to EN content files that lack them entirely."""
import glob
import re
from pathlib import Path

CONTENT_DIR = Path("src/content/en")
CALCS_JSON = Path("src/calculators/calculators.json")
I18N_EN = Path("src/i18n/en.json")

import json
with open(CALCS_JSON, 'r', encoding='utf-8') as f:
    calcs = {c["id"]: c for c in json.load(f)["calculators"]}
with open(I18N_EN, 'r', encoding='utf-8') as f:
    i18n = json.load(f)
calcs_i18n = i18n.get("calculators", {})

faq_patterns = re.compile(r'faq|frequently asked|questions &amp; answers|common questions', re.I)
added = 0
for path in sorted(CONTENT_DIR.glob("*.html")):
    html = path.read_text(encoding="utf-8")
    if faq_patterns.search(html):
        continue
    cid = path.stem
    calc = calcs.get(cid)
    ci = calcs_i18n.get(cid, {}) if calc else {}
    name = ci.get("name", calc.get("slug", "").replace("-", " ").title()) if calc else ""
    formula_display = calc.get("formula_display", "") if calc else ""
    result_context = calc.get("result_context", "") if calc else ""
    if not name:
        continue

    faqs = []
    faqs.append('<h2>Frequently Asked Questions</h2>')
    faqs.append(f'<div class="faq-item"><button class="faq-q" aria-expanded="false">What is the {name} used for?</button><div class="faq-a"><p>{result_context or "This calculator helps you compute " + name.lower() + " quickly and accurately."}</p></div></div>')
    if formula_display:
        faqs.append(f'<div class="faq-item"><button class="faq-q" aria-expanded="false">What is the formula?</button><div class="faq-a"><p>The formula is: {formula_display}</p></div></div>')
    else:
        faqs.append(f'<div class="faq-item"><button class="faq-q" aria-expanded="false">How does this calculator work?</button><div class="faq-a"><p>Enter the required inputs and press Calculate to get the result instantly.</p></div></div>')
    faqs.append(f'<div class="faq-item"><button class="faq-q" aria-expanded="false">What units does this calculator support?</button><div class="faq-a"><p>The calculator supports the most common units for each input. You can switch units using the dropdown next to each field.</p></div></div>')

    # Insert before </section> if present, else append
    if "</section>" in html:
        html = html.replace("</section>", "\n" + "\n".join(faqs) + "\n</section>", 1)
    else:
        html = html.rstrip() + "\n" + "\n".join(faqs) + "\n"
    path.write_text(html, encoding="utf-8")
    added += 1
    print(f"Added FAQ to {cid}")

print(f"\nAdded FAQs to {added} files.")

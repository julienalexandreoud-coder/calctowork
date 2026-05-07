#!/usr/bin/env python3
"""Remove duplicated <section class="related-calcs"> and repeated FAQ items from content files."""
import glob
import os
import re

for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
    files = glob.glob(f'src/content/{lang}/*.html')
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        original = html
        # Dedupe related-calcs sections
        sections = re.findall(r'<section class="related-calcs">.*?</section>', html, re.DOTALL)
        if len(sections) > 1:
            for s in sections[1:]:
                html = html.replace(s, '', 1)
        # Dedupe FAQ items by h3 text
        faq_items = re.findall(r'(<div class="faq-item">.*?<h3>.*?</h3>.*?</div>)', html, re.DOTALL)
        seen = set()
        for item in faq_items:
            h3 = re.search(r'<h3>(.*?)</h3>', item)
            text = h3.group(1).strip() if h3 else ''
            if text in seen:
                html = html.replace(item, '', 1)
            else:
                seen.add(text)
        if html != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'Fixed {path}')
print('Done deduping content sections.')

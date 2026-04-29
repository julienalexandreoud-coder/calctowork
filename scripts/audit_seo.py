import json
import re
from pathlib import Path
from collections import defaultdict

PUBLIC = Path('public')
LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt']

# Only check base calculator pages (not parametric subdirs)
titles = defaultdict(list)
descs = defaultdict(list)

print("Checking SEO uniqueness on base calculator pages...")

for lang in LANGS:
    lang_dir = PUBLIC / lang
    if not lang_dir.exists():
        continue
    # Only direct subdirs (no nested parametric dirs)
    for page in lang_dir.glob('*/index.html'):
        # Skip if parent has subdirs (indicates parametric base)
        slug = page.parent.name
        content = page.read_text(encoding='utf-8')
        
        m = re.search(r'<title>(.*?)</title>', content)
        if m:
            titles[m.group(1)].append(f'{lang}/{slug}')
        
        m = re.search(r'<meta name="description" content="([^"]*)"', content)
        if m:
            descs[m.group(1)].append(f'{lang}/{slug}')

dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
dup_descs = {k: v for k, v in descs.items() if len(v) > 1}

print(f"\nTotal base pages checked: {sum(len(v) for v in titles.values())}")
print(f"Duplicate titles: {len(dup_titles)} (affecting {sum(len(v) for v in dup_titles.values())} pages)")
for title, pages in sorted(dup_titles.items(), key=lambda x: -len(x[1]))[:5]:
    print(f"  '{title[:60]}...' -> {len(pages)} pages")

print(f"\nDuplicate descriptions: {len(dup_descs)} (affecting {sum(len(v) for v in dup_descs.values())} pages)")
for desc, pages in sorted(dup_descs.items(), key=lambda x: -len(x[1]))[:5]:
    print(f"  '{desc[:60]}...' -> {len(pages)} pages")

# Save
report = {"dup_titles": dup_titles, "dup_descs": dup_descs}
with open("audit_seo.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print("\nSaved to audit_seo.json")

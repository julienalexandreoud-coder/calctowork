# -*- coding: utf-8 -*-
"""Search public HTML for mistakes."""
import os, re

PUBLIC = r"C:\Microsaas\obra\public"

issues = 0
for root, dirs, files in os.walk(PUBLIC):
    for fname in files:
        if not fname.endswith(".html"):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                c = f.read()
        except:
            continue

        rel = os.path.relpath(fpath, PUBLIC)

        # Double-encoded HTML entities
        if "&amp;amp;" in c:
            print(f"DOUBLE ENCODED: {rel}")
            issues += 1

        # Check for empty title tags
        if "<title></title>" in c:
            print(f"EMPTY TITLE: {rel}")
            issues += 1

        # Check for missing meta description
        if '<meta name="description" content=""' in c:
            print(f"EMPTY META DESC: {rel}")
            issues += 1

        if issues > 15:
            break

    if issues > 15:
        break

print(f"\nTotal issues: {issues}")

# Also check a few calculator pages specifically
print("\n=== SAMPLE CALCULATOR PAGES ===")
import glob
samples = glob.glob(os.path.join(PUBLIC, "es", "*/index.html"))[:5]
for sp in samples:
    with open(sp, "r", encoding="utf-8") as f:
        c = f.read()
    title = re.search(r"<title>(.*?)</title>", c)
    desc = re.search(r'<meta name="description" content="(.*?)"', c)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", c)
    rel = os.path.relpath(sp, PUBLIC)
    print(f"\n  {rel}")
    if title:
        print(f"    title: {title.group(1)[:100]}")
    if desc:
        print(f"    desc:  {desc.group(1)[:120]}")
    if h1:
        print(f"    h1:    {h1.group(1)[:100]}")

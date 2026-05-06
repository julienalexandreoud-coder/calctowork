# -*- coding: utf-8 -*-
"""Find encoding issues and other mistakes in generated public pages."""
import os, re, glob
from collections import Counter

PUBLIC = r"C:\Microsaas\obra\public"
SRC = r"C:\Microsaas\obra\src"

MOJIBAKE = [
    (r"Ã±", "ñ"), (r"Ã¡", "á"), (r"Ã©", "é"), (r"Ã­", "í"),
    (r"Ã³", "ó"), (r"Ãº", "ú"), (r"Ã¼", "ü"),
    (r"Ã‘", "Ñ"), (r"Ã", "Á"), (r"Ã‰", "É"), (r"Ã“", "Ó"),
    (r"â‚¬", "€"), (r"Â°", "°"), (r"Â²", "²"), (r"Â³", "³"),
    (r"â€œ", "\""), (r"â€", "\""), (r"â€™", "'"),
    (r"â€"", "—"), (r"â€“", "–"), (r"â€¦", "…"),
    (r"Â¿", "¿"), (r"Â¡", "¡"),
    (r"Ã—", "×"), (r"Ã·", "÷"),
]

# Search public HTML
print("=== PUBLIC HTML MOJIBAKE ===")
pub_found = Counter()
for root, dirs, files in os.walk(PUBLIC):
    for fname in files:
        if not fname.endswith(('.html', '.xml', '.json', '.css', '.js')):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            continue
        for pattern, correct in MOJIBAKE:
            matches = re.findall(pattern, content)
            if matches:
                pub_found[pattern] += len(matches)

for pattern, count in pub_found.most_common(15):
    correct = dict(MOJIBAKE)[pattern]
    print(f"  {count:>6}x {pattern} (should be {correct})")

if not pub_found:
    print("  None found in public/")

# Search source files (JSON, templates, JS, CSS)
print("\n=== SOURCE MOJIBAKE ===")
src_found = Counter()
for root, dirs, files in os.walk(SRC):
    for fname in files:
        if not fname.endswith(('.json', '.html', '.j2', '.js', '.css')):
            continue
        fpath = os.path.join(root, fname)
        if "node_modules" in fpath:
            continue
        try:
            with open(fpath, "r", encoding="utf-8-sig") as f:
                content = f.read()
        except:
            continue
        for pattern, correct in MOJIBAKE:
            matches = re.findall(pattern, content)
            if matches:
                src_found[pattern] += len(matches)

for pattern, count in src_found.most_common(15):
    correct = dict(MOJIBAKE)[pattern]
    print(f"  {count:>6}x {pattern} (should be {correct})")

if not src_found:
    print("  None found in src/")

# Search for other weird symbols
print("\n=== OTHER WEIRD SYMBOLS ===")
WEIRD = [
    (r"\?[^>\s]{1,3}", "replacement chars"),
    (r"\xef\xbf\xbd", "Unicode replacement char"),
]
for root, dirs, files in os.walk(PUBLIC):
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except:
            continue
        if "\ufffd" in content:
            print(f"  REPLACEMENT CHAR in {fpath}")
            break  # Just report first one

print("\nDone.")

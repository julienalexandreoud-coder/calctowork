# -*- coding: utf-8 -*-
"""Deep search for bugs and errors across the entire project."""

import os, json, glob, re

PUBLIC = r"C:\Microsaas\obra\public"
SRC = r"C:\Microsaas\obra\src"
CALC_DIR = r"C:\Microsaas\obra\src\calculators"

issues = 0

# 1. Check generated pages for broken script/image references
print("=== BROKEN REFERENCES ===")
found = 0
for lang in ["es", "en", "fr", "pt", "de", "it"]:
    lang_dir = os.path.join(PUBLIC, lang)
    if not os.path.exists(lang_dir):
        continue
    for subdir in os.listdir(lang_dir):
        page = os.path.join(lang_dir, subdir, "index.html")
        if not os.path.exists(page):
            continue
        with open(page, "r", encoding="utf-8") as f:
            c = f.read()
        for ref in re.findall(r'(?:src|href)="(/[^"]*)"', c):
            ref_clean = ref.split("?")[0].split("#")[0]
            ref_path = os.path.join(PUBLIC, ref_clean.lstrip("/"))
            if not os.path.exists(ref_path):
                rel = os.path.relpath(page, PUBLIC)
                found += 1
                if found <= 5:
                    print(f"  BROKEN: {rel} -> {ref}")
                issues += 1
                if found > 5:
                    break
        if found > 5:
            break
    if found > 5:
        break
if found == 0:
    print("  None found")

# 2. Check JSON validity of config files
print("\n=== CONFIG FILES ===")
for fname in ["firebase.json", ".firebaserc", "firestore.indexes.json"]:
    fpath = os.path.join(r"C:\Microsaas\obra", fname)
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            json.load(f)
        print(f"  {fname}: valid")
    except Exception as e:
        print(f"  {fname}: INVALID - {e}")
        issues += 1

# 3. Check for duplicate calculator IDs
print("\n=== DUPLICATE IDs ===")
ids_seen = {}
dup_ids = []
for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    if "bak" in fp or "monolithic" in fp:
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        c = json.load(f)
    cid = c.get("id", "?")
    if cid in ids_seen:
        dup_ids.append(f"{cid}: {ids_seen[cid]} and {os.path.basename(fp)}")
    else:
        ids_seen[cid] = os.path.basename(fp)
if dup_ids:
    for d in dup_ids:
        print(f"  DUPLICATE: {d}")
        issues += 1
else:
    print("  None")

# 4. Check for empty source files
print("\n=== EMPTY FILES ===")
empty = False
for root, dirs, files in os.walk(SRC):
    for fname in files:
        fpath = os.path.join(root, fname)
        if os.path.getsize(fpath) == 0:
            print(f"  EMPTY: {os.path.relpath(fpath, SRC)}")
            issues += 1
            empty = True
if not empty:
    print("  None")

# 5. Check for missing output unit in calculator definitions
print("\n=== MISSING OUTPUT UNITS ===")
missing_units = 0
for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    if "bak" in fp or "monolithic" in fp:
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        c = json.load(f)
    for out in c.get("outputs", []):
        if "unit" not in out:
            missing_units += 1
            if missing_units <= 3:
                print(f"  {c['id']} {os.path.basename(fp)}: output '{out.get('id','?')}' missing unit")
if missing_units == 0:
    print("  None")

# 6. Check for invalid input type values
print("\n=== INVALID INPUT TYPES ===")
valid_types = {"number", "select", "text", "checkbox", "range", "date"}
bad_types = 0
for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    if "bak" in fp or "monolithic" in fp:
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        c = json.load(f)
    for inp in c.get("inputs", []):
        t = inp.get("type", "number")
        if t not in valid_types:
            bad_types += 1
            if bad_types <= 3:
                print(f"  {c['id']} {os.path.basename(fp)}: input '{inp.get('id','?')}' has invalid type '{t}'")
if bad_types == 0:
    print("  None")

# 7. Check service worker
print("\n=== SERVICE WORKER ===")
sw_path = os.path.join(SRC, "sw.js")
with open(sw_path, "r", encoding="utf-8") as f:
    sw = f.read()
sw_cached = re.findall(r"'([^']+)'", sw.split("SHELL = [")[1].split("]")[0])
for ref in sw_cached:
    ref_path = os.path.join(PUBLIC, ref.lstrip("/"))
    if not os.path.exists(ref_path):
        print(f"  SW CACHES MISSING: {ref}")
        issues += 1
    else:
        print(f"  SW cache OK: {ref}")

# 8. Check for NaN/undefined in formula that would crash
print("\n=== FORMULA SAFETY ===")
unsafe = 0
for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    if "bak" in fp or "monolithic" in fp:
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        c = json.load(f)
    formula = c.get("formula", "")
    if ".toFixed(" in formula and "parseFloat" not in formula and "||0" not in formula:
        unsafe += 1
        if unsafe <= 3:
            print(f"  {c['id']} {os.path.basename(fp)}: .toFixed() without input validation")
if unsafe == 0:
    print("  All formulas have input validation")

print(f"\n=== TOTAL ISSUES: {issues} ===")

#!/usr/bin/env python3
"""
Fast comprehensive audit of all calculator pages.
"""
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
PUBLIC = ROOT / "public"
SRC = ROOT / "src"
I18N_DIR = SRC / "i18n"
CONTENT_DIR = SRC / "content"

LANGS = ["es", "en", "fr", "de", "it", "pt"]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html)

def audit_all():
    print("Loading data...")
    calculators = load_json(SRC / "calculators" / "calculators.json")["calculators"]
    
    translations = {}
    for lang in LANGS:
        translations[lang] = load_json(I18N_DIR / f"{lang}.json")
    
    thin_content = []
    templated_content = []
    missing_content = []
    missing_i18n = []
    
    print(f"Checking {len(calculators)} calculators × {len(LANGS)} languages...")
    
    for calc in calculators:
        cid = calc["id"]
        
        for lang in LANGS:
            # Check content file
            cf = CONTENT_DIR / lang / f"{cid}.html"
            if cf.exists():
                text = strip_tags(cf.read_text(encoding="utf-8"))
                words = len(text.split())
                if words < 400:
                    thin_content.append((lang, cid, words))
                if 'formula-section' in text or '<h1>' in text:
                    templated_content.append((lang, cid, words))
            else:
                missing_content.append((lang, cid))
            
            # Check i18n
            i18n = translations[lang].get("calculators", {}).get(cid, {})
            if not i18n.get("name") or not i18n.get("desc"):
                missing_i18n.append(f"{lang}/{cid}")
    
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Thin content (<400w): {len(thin_content)}")
    print(f"Templated content: {len(templated_content)}")
    print(f"Missing content files: {len(missing_content)}")
    print(f"Missing i18n: {len(missing_i18n)}")
    
    if thin_content:
        print("\nThin content samples:")
        for item in thin_content[:20]:
            print(f"  {item}")
    
    if templated_content:
        print("\nTemplated content samples:")
        for item in templated_content[:20]:
            print(f"  {item}")
    
    if missing_content:
        print("\nMissing content files (first 20):")
        for item in missing_content[:20]:
            print(f"  {item}")
    
    # Save
    report = {
        "thin": thin_content,
        "templated": templated_content,
        "missing_content": missing_content,
        "missing_i18n": missing_i18n,
    }
    with open(ROOT / "audit_fast.json", "w") as f:
        json.dump(report, f)
    print("\nSaved to audit_fast.json")

if __name__ == "__main__":
    audit_all()

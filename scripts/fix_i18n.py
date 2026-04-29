#!/usr/bin/env python3
"""
Fix i18n JSON files:
1. Fix mojibake (double/triple UTF-8 encoding via cp1252)
2. Fix broken/truncated meta descriptions
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent / "src" / "i18n"

def fix_mojibake(text: str) -> str:
    """Reverse cp1252↔UTF-8 mojibake by iteratively decoding."""
    if not isinstance(text, str):
        return text
    # Only try fixing if we see common mojibake patterns
    if not re.search(r'[ÃÂƒ±]', text):
        return text
    for _ in range(3):  # max 3 rounds for triple-encoding
        try:
            new_text = text.encode('cp1252').decode('utf-8')
            if new_text == text:
                break
            text = new_text
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
    return text

def fix_description(desc: str, name: str) -> str:
    """Fix broken/truncated meta descriptions."""
    if not desc:
        return desc
    # Fix trailing fragments
    desc = re.sub(r'\s+Herramienta gratuita con formula y\.?$', '.', desc, flags=re.IGNORECASE)
    desc = re.sub(r'\s+with formula and\.?$', '.', desc, flags=re.IGNORECASE)
    desc = re.sub(r'\s+avec formule et\.?$', '.', desc, flags=re.IGNORECASE)
    desc = re.sub(r'\s+mit Formel und\.?$', '.', desc, flags=re.IGNORECASE)
    desc = re.sub(r'\s+con formula e\.?$', '.', desc, flags=re.IGNORECASE)
    desc = re.sub(r'\s+com fórmula e\.?$', '.', desc, flags=re.IGNORECASE)
    # Fix generic repetition
    desc = re.sub(r'(Herramienta gratuita.*?)(Herramienta gratuita.*)', r'\1', desc, flags=re.IGNORECASE)
    # Ensure it ends properly
    desc = desc.strip()
    if desc.endswith(' y') or desc.endswith(' with') or desc.endswith(' et') or desc.endswith(' und') or desc.endswith(' e'):
        desc = desc.rsplit(' ', 1)[0] + '.'
    # If too short, generate from name
    if len(desc) < 50 and name:
        desc = f"{name}. Free online calculator with formula, examples and step-by-step guide."
    # Ensure reasonable length
    if len(desc) > 170:
        desc = desc[:167].rsplit(' ', 1)[0] + '...'
    return desc

def process_value(value, name=""):
    """Recursively process JSON values."""
    if isinstance(value, str):
        value = fix_mojibake(value)
        # Fix descriptions if key context suggests it
        return value
    if isinstance(value, dict):
        return {k: process_value(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [process_value(v) for v in value]
    return value

def post_fix_descriptions(data):
    """Fix seo_desc and seo_description fields specifically."""
    calcs = data.get("calculators", {})
    for cid, calc in calcs.items():
        name = calc.get("name", "")
        for key in ("seo_desc", "seo_description"):
            if key in calc:
                calc[key] = fix_description(calc[key], name)
        # Also fix desc if present
        if "desc" in calc:
            calc["desc"] = fix_description(calc["desc"], name)
    return data

def main():
    for lang_file in sorted(ROOT.glob("*.json")):
        print(f"Processing {lang_file.name}...")
        with open(lang_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        data = process_value(data)
        data = post_fix_descriptions(data)
        with open(lang_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"  Saved {lang_file.name}")
    print("Done.")

if __name__ == "__main__":
    main()

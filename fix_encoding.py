#!/usr/bin/env python3
"""Fix broken Unicode characters across all JSON files."""
import json
import os
import re

BASE = r"C:\Microsaas\obra"
FILES = [
    "src/i18n/es.json", "src/i18n/en.json", "src/i18n/fr.json",
    "src/i18n/pt.json", "src/i18n/de.json", "src/i18n/it.json",
    "src/calculators/calculators.json",
]

# Character fix map - what we see corrupt -> what it should be
FIXES = {
    "\u00c3\u2014": "\u00d7",       # Ã— -> × (multiplication)
    "\u00c3\u2013": "\u00f7",       # Ã· -> ÷ (division)
    "\u00c3\u0083\u2014": "\u00d7", # Ãƒ— -> ×
    "\u00c3\u2014": "\u00d7",
    "\u00cf\u20ac": "\u03c0",       # Ï€ -> π
    "\u00cf\u20ac\u0161": "\u03c0",
    "\u00e2\u02c6\u0161": "\u221a", # âˆš -> √
    "\u00c3\u0178": "\u00b2",       # Ã² -> ²
    "\u00c3\u201c": "\u00b3",       # Ã³ -> ³
    "\u00c3\u2018": "\u00b0",       # Ã° -> °
    "\u00c3\u201a\u00ac": "\u20ac", # â‚¬ -> €
    "\u00c3\u00a2\u00e2\u201a\u00ac": "\u20ac",  # multiple byte €
    "\u00c3\u201a\u00b0": "\u00b0", # Â° -> °
    "\u00e2\u20ac\u201c": "\u2013",  # â€" -> –
    "\u00e2\u20ac\u201d": "\u2014",  # â€" -> —
    "\u00e2\u20ac\u0153": "\u201c",  # â€œ -> "
    "\u00e2\u20ac\u009d": "\u201d",  # â€ -> "
    "\u00e2\u20ac\u2122": "\u2019",  # â€™ -> '
    "\u00e2\u20ac\u00a6": "\u2026",  # â€¦ -> …
    "\u00e2\u20ac\u00a2": "\u2022",  # â€¢ -> •
    "\u00c3\u00b1": "\u00f1",       # Ã± -> ñ
    "\u00c3\u00a1": "\u00e1",       # Ã¡ -> á
    "\u00c3\u00a9": "\u00e9",       # Ã© -> é
    "\u00c3\u00ad": "\u00ed",       # Ã­ -> í
    "\u00c3\u00b3": "\u00f3",       # Ã³ -> ó
    "\u00c3\u00ba": "\u00fa",       # Ãº -> ú
    "\u00c3\u0081": "\u00c1",       # Ã -> Á
    "\u00c3\u0089": "\u00c9",       # Ã -> É
    "\u00c3\u008d": "\u00cd",       # Ã -> Í
    "\u00c3\u0093": "\u00d3",       # Ã -> Ó
    "\u00c3\u009a": "\u00da",       # Ã -> Ú
    "\u00c3\u0091": "\u00d1",       # Ã -> Ñ
    "\u00c3\u00bc": "\u00fc",       # Ã¼ -> ü
    "\u00ce\u0094": "\u0394",       # Î -> Δ
    "\u00ce\u00b1": "\u03b1",       # Î± -> α
    "\u00ce\u00b2": "\u03b2",       # Î² -> β
    "\u00ce\u00b8": "\u03b8",       # Î¸ -> θ
    "\u00ce\u00bb": "\u03bb",       # Î» -> λ
    "\u00ce\u00bc": "\u03bc",       # Î¼ -> μ
    "\u00ce\u00bd": "\u03bd",       # Î½ -> ν
    "\u00cf\u0081": "\u03c1",       # Ï -> ρ
    "\u00cf\u0083": "\u03c3",       # Ï -> σ
    "\u00cf\u0084": "\u03c4",       # Ï -> τ
    "\u00cf\u0085": "\u03c5",       # Ï -> υ
    "\u00cf\u0086": "\u03c6",       # Ï -> φ
    "\u00cf\u0089": "\u03c9",       # Ï -> ω
    "\u00c3\u2014": "\u00d7",
    "\u00ce\u0098": "\u0398",       # Î -> Θ
    "\u00ce\u009e": "\u039e",       # Î -> Ξ
    "\u00ce\u00a3": "\u03a3",       # Î£ -> Σ
    "\u00ce\u00a9": "\u03a9",       # Î© -> Ω
}

def fix_text(text):
    """Replace all broken character sequences."""
    for broken, fixed in FIXES.items():
        text = text.replace(broken, fixed)
    # Also fix common patterns that survived
    text = text.replace("â€¢", "•")
    text = text.replace("â€¦", "…")
    text = text.replace("â€œ", '"')
    text = text.replace("â€\u009d", '"')
    text = text.replace("â€™", "'")
    text = text.replace("â€˜", "'")


    text = text.replace("Â°", "°")
    text = text.replace("Â²", "²")
    text = text.replace("Â³", "³")
    text = text.replace("Â±", "±")
    text = text.replace("Ã—", "×")
    text = text.replace("Ã·", "÷")
    text = text.replace("Ã¢â€š¬", "€")
    text = text.replace("â€š¬", "€")
    return text

def fix_all_strings(obj):
    """Recursively fix all strings in a dict/list."""
    if isinstance(obj, str):
        return fix_text(obj)
    elif isinstance(obj, dict):
        return {k: fix_all_strings(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [fix_all_strings(v) for v in obj]
    return obj

for filepath in FILES:
    full_path = os.path.join(BASE, filepath)
    print(f"Processing {filepath}...")
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    content = fix_text(content)
    
    if content != original:
        # Verify it's valid JSON
        try:
            json.loads(content)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            changed = sum(1 for a, b in zip(original, content) if a != b)
            print(f"  Fixed! {changed} characters changed")
        except json.JSONDecodeError as e:
            print(f"  WARNING: Would break JSON at {e}")
            # Try the recursive approach instead
            with open(full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            data = fix_all_strings(data)
            with open(full_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  Fixed via JSON parse/write instead")
    else:
        print(f"  No changes needed")

print("\nAll done!")

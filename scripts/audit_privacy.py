#!/usr/bin/env python3
"""Audit privacy pages across 6 languages for required disclosures."""
import glob
import re
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIVACY_DIR = ROOT / "public"
OUT_DIR = ROOT / "audit"
OUT_DIR.mkdir(exist_ok=True)

required_clauses = [
    ("cookies", r'cookie|consent|banner'),
    ("adsense", r'adsense|ad.sense|google.ads'),
    ("analytics", r'analytics|firebase|firestore'),
    ("email_capture", r'email|lead|pdf.report|webhook'),
    ("gdpr_rights", r'access|delete|portability|right[s]?'),
]

rows = []
for lang in ["en", "es", "fr", "de", "it", "pt"]:
    path = PRIVACY_DIR / lang / "privacy" / "index.html"
    if path.exists():
        text = path.read_text(encoding="utf-8").lower()
        missing = [name for name, pat in required_clauses if not re.search(pat, text)]
        rows.append({"lang": lang, "path": str(path), "missing_clauses": ", ".join(missing)})
    else:
        rows.append({"lang": lang, "path": str(path), "missing_clauses": "PAGE MISSING"})

with open(OUT_DIR / "privacy_gaps.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["lang", "path", "missing_clauses"])
    writer.writeheader()
    writer.writerows(rows)

print("Privacy audit written to audit/privacy_gaps.csv")
for r in rows:
    print(f"  {r['lang']}: {r['missing_clauses']}")

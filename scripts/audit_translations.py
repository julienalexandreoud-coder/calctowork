#!/usr/bin/env python3
"""Audit translation gaps across all 6 languages. Output CSV."""
import json
import os
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALCS_JSON = ROOT / "src" / "calculators" / "calculators.json"
CONTENT_DIR = ROOT / "src" / "content"
OUT_DIR = ROOT / "audit"
OUT_DIR.mkdir(exist_ok=True)

with open(CALCS_JSON, 'r', encoding='utf-8') as f:
    calcs = json.load(f)["calculators"]

langs = ["en", "es", "fr", "de", "it", "pt"]
rows = []
for c in calcs:
    cid = c["id"]
    slug = c.get("slug", "")
    sizes = {}
    for lang in langs:
        path = CONTENT_DIR / lang / f"{cid}.html"
        sizes[lang] = path.stat().st_size / 1024 if path.exists() else 0
    en_kb = sizes["en"]
    ratios = {lang: (sizes[lang] / en_kb if en_kb else 0) for lang in langs if lang != "en"}
    min_ratio = min(ratios.values()) if ratios else 1.0
    flag = "STUB" if min_ratio < 0.5 else ""
    rows.append({
        "id": cid,
        "slug": slug,
        "en_kb": round(en_kb, 1),
        "es_kb": round(sizes["es"], 1),
        "fr_kb": round(sizes["fr"], 1),
        "de_kb": round(sizes["de"], 1),
        "it_kb": round(sizes["it"], 1),
        "pt_kb": round(sizes["pt"], 1),
        "min_ratio": round(min_ratio, 2),
        "flag": flag,
    })

with open(OUT_DIR / "translation_gaps.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["id", "slug", "en_kb", "es_kb", "fr_kb", "de_kb", "it_kb", "pt_kb", "min_ratio", "flag"])
    writer.writeheader()
    writer.writerows(rows)

stub_count = sum(1 for r in rows if r["flag"] == "STUB")
print(f"Audit complete. {stub_count} files flagged as stubs (<50% of EN size).")
print(f"Output: {OUT_DIR / 'translation_gaps.csv'}")

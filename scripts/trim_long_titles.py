#!/usr/bin/env python3
"""Trim seo_title > 60 chars to use the shorter 'name' field instead."""
import json
from pathlib import Path

I18N_DIR = Path("src/i18n")

for lang in ["es", "fr", "de", "it", "pt"]:
    path = I18N_DIR / f"{lang}.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    calcs = data.get("calculators", {})
    trimmed = 0
    for cid, c in calcs.items():
        t = c.get("seo_title", "")
        if len(t) > 60:
            name = c.get("name", "")
            if name and len(name) <= 60:
                c["seo_title"] = name
                trimmed += 1
    if trimmed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"{lang}: trimmed {trimmed} titles")
    else:
        print(f"{lang}: no titles to trim")

#!/usr/bin/env python3
"""Migrate calculator files to v4 clean format."""

import json
import os
import glob
from pathlib import Path

CALC_DIR = Path(r"C:\Microsaas\obra\src\calculators")
LANGS = ["es", "en", "fr", "pt", "de", "it"]

TOP_LEVEL_CRUFT = [
    "example_label", "range_hints", "result_context",
    "formula_display", "steps", "mistakes", "input_type_review",
]
TOP_LEVEL_CRUFT += [f"result_context_{l}" for l in LANGS]

I18N_CRUFT = ["input_type_review", "seo_desc"]

STRUCTURAL_KEYS = {
    "id", "slug", "block", "block_slug",
    "inputs", "outputs", "formula", "related",
    "comparison_presets", "example_inputs",
    "units", "diagram", "standard", "trust_note",
    "buying_units", "i18n", "wastage_default",
    "wastage_label", "show_wastage", "net_label",
    "total_label", "presets",
}

def migrate_file(filepath):
    with open(filepath, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    changed = False

    for key in TOP_LEVEL_CRUFT:
        if key in data:
            del data[key]
            changed = True

    i18n = data.get("i18n", {})
    for lang in LANGS:
        if lang not in i18n:
            continue
        entry = i18n[lang]

        for key in I18N_CRUFT:
            if key in entry:
                del entry[key]
                changed = True

        if "desc" in entry and "description" not in entry:
            entry["description"] = entry.pop("desc")
            changed = True

    unknown = [k for k in data if k not in STRUCTURAL_KEYS and k not in LANGS]
    if unknown:
        print(f"  [WARN] {os.path.basename(filepath)}: unknown keys: {unknown}")

    if changed:
        with open(filepath, "w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    return False


def main():
    files = sorted(
        f for f in glob.glob(str(CALC_DIR / "*.json"))
        if os.path.basename(f) not in ("calculators.json",)
        and "bak" not in f and "monolithic" not in f
    )

    migrated = 0
    skipped = 0
    errors = 0

    for filepath in files:
        try:
            if migrate_file(filepath):
                migrated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  [ERROR] {os.path.basename(filepath)}: {e}")
            errors += 1

    print(f"\nDone. Migrated: {migrated}, Skipped (already clean): {skipped}, Errors: {errors}")


if __name__ == "__main__":
    main()

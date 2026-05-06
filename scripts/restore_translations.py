#!/usr/bin/env python3
"""Restore clean i18n input/output labels from commit 1444b1b into current individual calc files."""

import json, os, glob, subprocess
from pathlib import Path

CALC_DIR = Path(r"C:\Microsaas\obra\src\calculators")
LANGS = ["es", "en", "fr", "pt", "de", "it"]
SOURCE_COMMIT = "1444b1b"
REPO_DIR = r"C:\Microsaas\obra"


def load_old_i18n(lang):
    """Extract calculator i18n data from old i18n/{lang}.json at SOURCE_COMMIT."""
    result = subprocess.run(
        ["git", "show", f"{SOURCE_COMMIT}:src/i18n/{lang}.json"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        cwd=REPO_DIR,
    )
    if result.returncode != 0:
        print(f"  ERROR: cannot load old i18n/{lang}.json: {result.stderr[:100]}")
        return {}
    data = json.loads(result.stdout)
    return data.get("calculators", {})


def main():
    files = sorted(
        f for f in glob.glob(str(CALC_DIR / "*.json"))
        if os.path.basename(f) not in ("calculators.json",)
        and "bak" not in f and "monolithic" not in f
    )

    print(f"Loading old i18n from commit {SOURCE_COMMIT}...")
    old_i18n = {}
    for lang in LANGS:
        old_i18n[lang] = load_old_i18n(lang)
        print(f"  {lang}: {len(old_i18n[lang])} calculator entries")

    updated = 0
    fixed_labels = {lang: 0 for lang in LANGS}

    for filepath in files:
        name = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)

        calc_id = calc.get("id", "")
        if not calc_id:
            continue

        changed = False

        for lang in LANGS:
            old_entry = old_i18n[lang].get(calc_id, {})
            if not old_entry:
                continue

            current = calc.get("i18n", {}).get(lang, {})
            if not current:
                continue

            # Restore inputs labels
            old_inputs = old_entry.get("inputs", {})
            cur_inputs = current.get("inputs", {})
            for inp_id, old_label in old_inputs.items():
                if not isinstance(old_label, str) or not old_label:
                    continue
                cur_label = cur_inputs.get(inp_id, "")
                if cur_label != old_label:
                    cur_inputs[inp_id] = old_label
                    fixed_labels[lang] += 1
                    changed = True

            # Restore outputs labels
            old_outputs = old_entry.get("outputs", {})
            cur_outputs = current.get("outputs", {})
            for out_id, old_label in old_outputs.items():
                if not isinstance(old_label, str) or not old_label:
                    continue
                cur_label = cur_outputs.get(out_id, "")
                if cur_label != old_label:
                    cur_outputs[out_id] = old_label
                    changed = True

            # Restore steps if old ones are better (non-empty and not matching ES)
            old_steps = old_entry.get("steps", [])
            if old_steps and isinstance(old_steps, list):
                cur_steps = current.get("steps", [])
                old_es_steps = old_i18n["es"].get(calc_id, {}).get("steps", [])
                # Only copy if old steps differ from Spanish (meaning they're translated)
                if old_steps != old_es_steps:
                    if cur_steps != old_steps:
                        current["steps"] = old_steps
                        changed = True

            # Restore mistakes
            old_mistakes = old_entry.get("mistakes", [])
            if old_mistakes and isinstance(old_mistakes, list):
                cur_mistakes = current.get("mistakes", [])
                old_es_mistakes = old_i18n["es"].get(calc_id, {}).get("mistakes", [])
                if old_mistakes != old_es_mistakes:
                    if cur_mistakes != old_mistakes:
                        current["mistakes"] = old_mistakes
                        changed = True

            # Restore result_context
            old_rc = old_entry.get("result_context", "")
            if isinstance(old_rc, str) and old_rc:
                cur_rc = current.get("result_context", "")
                old_es_rc = old_i18n["es"].get(calc_id, {}).get("result_context", "")
                if old_rc != old_es_rc and cur_rc != old_rc:
                    current["result_context"] = old_rc
                    changed = True

            # Restore formula_display
            old_fd = old_entry.get("formula_display", "")
            if isinstance(old_fd, str) and old_fd:
                cur_fd = current.get("formula_display", "")
                old_es_fd = old_i18n["es"].get(calc_id, {}).get("formula_display", "")
                if old_fd != old_es_fd and cur_fd != old_fd:
                    current["formula_display"] = old_fd
                    changed = True

            # Restore example_label
            old_el = old_entry.get("example_label", "")
            if isinstance(old_el, str) and old_el:
                cur_el = current.get("example_label", "")
                old_es_el = old_i18n["es"].get(calc_id, {}).get("example_label", "")
                if old_el != old_es_el and cur_el != old_el:
                    current["example_label"] = old_el
                    changed = True

        if changed:
            with open(filepath, "w", encoding="utf-8", newline="\n") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            updated += 1

    print(f"\nUpdated {updated}/{len(files)} calculator files")
    print("Fixed labels per language:")
    for lang in LANGS:
        print(f"  {lang}: {fixed_labels[lang]} labels restored")


if __name__ == "__main__":
    main()

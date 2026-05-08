#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 1: Fix UTF-8 encoding corruption (mojibake) across all calculator content files.
Handles both single and double-encoded UTF-8 (e.g. Ã© -> e with acute, Ã¢â€šÂ¬ -> euro).
Run from project root: py scripts/fix_encoding_all.py [--dry-run]
"""
import sys
from pathlib import Path

CALC_DIR = Path("src/calculators")
LANGS = ["en", "de", "es", "fr", "it", "pt"]


def fix_mojibake(text: str) -> str:
    """Fix double-encoded UTF-8. Apply up to 3 decode passes."""
    for _ in range(3):
        try:
            candidate = text.encode("latin-1").decode("utf-8")
            if candidate == text:
                break
            text = candidate
        except (UnicodeDecodeError, UnicodeEncodeError):
            break
    return text


def fix_file(path: Path, dry_run: bool = False) -> bool:
    try:
        content = path.read_text(encoding="utf-8-sig")  # utf-8-sig strips BOM
    except UnicodeDecodeError:
        print(f"  [SKIP-ENCODING] {path}")
        return False

    try:
        fixed = fix_mojibake(content)
    except Exception as e:
        print(f"  [ERROR] {path}: {e}")
        return False

    if fixed == content:
        return False

    if not dry_run:
        path.write_text(fixed, encoding="utf-8")
    return True


def main(dry_run: bool = False) -> None:
    if not CALC_DIR.exists():
        print(f"ERROR: {CALC_DIR} not found. Run from project root.")
        sys.exit(1)

    total = changed = 0

    for calc_dir in sorted(CALC_DIR.iterdir()):
        if not calc_dir.is_dir():
            continue

        # Fix lang HTML and JSON files
        for lang in LANGS:
            for ext in (".html", ".json"):
                fpath = calc_dir / f"{lang}{ext}"
                if fpath.exists():
                    total += 1
                    if fix_file(fpath, dry_run):
                        changed += 1

        # Fix calc.json
        calc_json = calc_dir / "calc.json"
        if calc_json.exists():
            total += 1
            if fix_file(calc_json, dry_run):
                changed += 1

    label = "would fix" if dry_run else "fixed"
    print(f"\nPhase 1 done. {label} {changed}/{total} files.")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN -- no files will be written.\n")
    main(dry_run)

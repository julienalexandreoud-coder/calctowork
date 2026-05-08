#!/usr/bin/env python3
"""
Phase 2: Remove English placeholder text left in non-English HTML files during bulk generation.
The phrase "ensure all values use a single consistent unit system." was never translated
and appears mid-sentence in step-by-step <li> items for calculators 015+.
Also cleans up any trailing English instruction fragments in other languages.
Run from project root: python scripts/fix_placeholders.py [--dry-run]
"""
import re
import sys
from pathlib import Path

CALC_DIR = Path("src/calculators")
ALL_LANGS = ["en", "de", "es", "fr", "it", "pt"]

# English fragments that should NOT appear in non-English files
ENGLISH_FRAGMENTS = [
    # Primary placeholder — separator + phrase
    re.compile(
        r"\s*[—–\-]+\s*ensure all values use a single consistent unit system\.",
        re.IGNORECASE,
    ),
    # Standalone phrase (no separator)
    re.compile(
        r"\s*ensure all values use a single consistent unit system\.",
        re.IGNORECASE,
    ),
]

# Also clean from English files (some slipped in)
ENGLISH_FILES_ONLY_FRAGMENT = re.compile(
    r"ensure all values use a single consistent unit system\.",
    re.IGNORECASE,
)


def fix_content(content: str, lang: str) -> tuple[str, int]:
    total = 0
    for pattern in ENGLISH_FRAGMENTS:
        new, n = pattern.subn("", content)
        total += n
        content = new
    return content, total


def fix_file(path: Path, lang: str, dry_run: bool = False) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"  [SKIP-ENCODING] {path}")
        return False

    fragment = "ensure all values use a single consistent unit system"
    if fragment.lower() not in content.lower():
        return False

    fixed, count = fix_content(content, lang)
    if fixed == content:
        return False

    if not dry_run:
        path.write_text(fixed, encoding="utf-8")
    print(f"  FIXED ({count}x): {path.parent.name}/{path.name}")
    return True


def main(dry_run: bool = False) -> None:
    if not CALC_DIR.exists():
        print(f"ERROR: {CALC_DIR} not found. Run from project root.")
        sys.exit(1)

    total = changed = 0

    for calc_dir in sorted(CALC_DIR.iterdir()):
        if not calc_dir.is_dir():
            continue
        for lang in ALL_LANGS:
            fpath = calc_dir / f"{lang}.html"
            if fpath.exists():
                total += 1
                if fix_file(fpath, lang, dry_run):
                    changed += 1

    label = "would fix" if dry_run else "fixed"
    print(f"\nPhase 2 done. {label} {changed}/{total} files.")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN — no files will be written.\n")
    main(dry_run)

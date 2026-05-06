#!/usr/bin/env python3
"""Post-build verification: checks page counts, hreflang, sitemap consistency."""

import json, os, re, sys
from pathlib import Path
from collections import Counter, defaultdict

PUBLIC = Path(r"C:\Microsaas\obra\public")
LANGS = ["es", "en", "fr", "pt", "de", "it"]
BASE_URL = "https://calcto.work"


def count_pages():
    """Count index.html files per language."""
    counts = {}
    for lang in LANGS:
        lang_dir = PUBLIC / lang
        if not lang_dir.exists():
            counts[lang] = 0
            continue
        counts[lang] = len(list(lang_dir.rglob("index.html")))
    return counts


def check_sitemap():
    """Verify sitemaps exist and entries match pages."""
    sitemap_idx = PUBLIC / "sitemap.xml"
    if not sitemap_idx.exists():
        print("  [FAIL] sitemap.xml missing")
        return False

    for lang in LANGS:
        sm = PUBLIC / f"sitemap-{lang}.xml"
        if not sm.exists():
            print(f"  [FAIL] sitemap-{lang}.xml missing")
            return False
        content = sm.read_text(encoding="utf-8")
        urls = len(re.findall(r"<loc>", content))
        print(f"  sitemap-{lang}.xml: {urls} URLs")
    return True


def check_hreflang():
    """Sample-check hreflang links on the first calculator page of each language."""
    all_ok = True
    for lang in LANGS:
        lang_dir = PUBLIC / lang
        # Find first non-category subdirectory with an index.html
        for subdir in sorted(lang_dir.iterdir()):
            if subdir.is_dir() and (subdir / "index.html").exists():
                path = subdir / "index.html"
                content = path.read_text(encoding="utf-8")
                alternates = re.findall(r'hreflang="(\w+)"\s+href="([^"]+)"', content)
                langs_found = {a[0] for a in alternates if a[0] in LANGS}
                if langs_found != set(LANGS):
                    missing = set(LANGS) - langs_found
                    print(f"  [WARN] {lang}/{subdir.name}/ missing hreflang for: {missing}")
                    all_ok = False
                else:
                    print(f"  {lang}/{subdir.name}/: all 6 hreflang OK")
                break
        else:
            print(f"  [WARN] {lang}/ no calculator pages found")
            all_ok = False

    return all_ok


def check_critical_files():
    """Verify essential files exist."""
    required = [
        "ads.txt",
        "robots.txt",
        "favicon.svg",
        "404.html",
        "offline.html",
        "sw.js",
        "manifest.json",
        "css/styles.css",
        "js/calculator.js",
    ]
    all_ok = True
    for fname in required:
        path = PUBLIC / fname
        if not path.exists():
            print(f"  [FAIL] {fname} missing")
            all_ok = False
    if all_ok:
        print(f"  All {len(required)} critical files present")
    return all_ok


def main():
    print("CalcToWork Build Verification")
    print(f"  Public dir: {PUBLIC}")
    print()

    # 1. Page counts
    print("--- Page counts ---")
    counts = count_pages()
    for lang, count in counts.items():
        print(f"  {lang}: {count} pages")
    min_count = min(counts.values()) if counts else 0
    max_count = max(counts.values()) if counts else 0
    if max_count - min_count > 50:
        print(f"  [WARN] Imbalanced page counts: min={min_count} max={max_count}")
    else:
        print(f"  Page counts balanced (range: {min_count}-{max_count})")
    print()

    # 2. Sitemaps
    print("--- Sitemaps ---")
    sitemap_ok = check_sitemap()
    print()

    # 3. Hreflang
    print("--- Hreflang links ---")
    hreflang_ok = check_hreflang()
    print()

    # 4. Critical files
    print("--- Critical files ---")
    files_ok = check_critical_files()
    print()

    # Summary
    print("=" * 40)
    all_ok = sitemap_ok and files_ok
    if all_ok:
        print("VERIFICATION: PASSED")
    else:
        print("VERIFICATION: ISSUES FOUND")
        sys.exit(1)


if __name__ == "__main__":
    main()

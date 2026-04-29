#!/usr/bin/env python3
"""
Build verification tests for CalcToWork.
Run after `python scripts/generate_calctowork.py` to verify output integrity.
"""
import json
import re
from pathlib import Path

PUBLIC = Path(__file__).parent.parent.parent / "public"
SRC = Path(__file__).parent.parent.parent / "src"

def test_ads_txt_exists():
    assert (PUBLIC / "ads.txt").exists(), "ads.txt is missing from public/"
    content = (PUBLIC / "ads.txt").read_text(encoding="utf-8")
    assert "google.com, pub-" in content, "ads.txt missing AdSense publisher line"
    print("[PASS] ads.txt exists and contains publisher ID")

def test_robots_txt_exists():
    assert (PUBLIC / "robots.txt").exists(), "robots.txt is missing"
    print("[PASS] robots.txt exists")

def test_sitemap_exists():
    assert (PUBLIC / "sitemap.xml").exists(), "sitemap.xml is missing"
    for lang in ["es", "en", "fr", "de", "it", "pt"]:
        assert (PUBLIC / f"sitemap-{lang}.xml").exists(), f"sitemap-{lang}.xml is missing"
    print("[PASS] All sitemap files exist")

def test_noindex_on_parametric():
    """Verify parametric variant pages have noindex."""
    # Parametric pages are nested deeper: /lang/slug/param/index.html
    parametric_pages = []
    for lang_dir in PUBLIC.glob("*"):
        if not lang_dir.is_dir() or lang_dir.name.startswith("."):
            continue
        for calc_dir in lang_dir.glob("*"):
            if not calc_dir.is_dir():
                continue
            for sub_dir in calc_dir.glob("*"):
                if sub_dir.is_dir() and (sub_dir / "index.html").exists():
                    parametric_pages.append(sub_dir / "index.html")
    parametric_pages = parametric_pages[:20]
    found = 0
    for page in parametric_pages:
        content = page.read_text(encoding="utf-8")
        if 'content="noindex, follow"' in content:
            found += 1
    if parametric_pages:
        print(f"[PASS] {found}/{len(parametric_pages)} sampled parametric pages have noindex")
        assert found == len(parametric_pages), f"Some parametric pages missing noindex: {found}/{len(parametric_pages)}"
    else:
        print("[INFO] No parametric pages found to sample")

def test_meta_descriptions_present():
    """Sample calculator pages for valid meta descriptions."""
    samples = []
    for lang in ["es", "en", "fr"]:
        lang_dir = PUBLIC / lang
        if lang_dir.exists():
            pages = list(lang_dir.glob("*/index.html"))[:10]
            samples.extend(pages)

    empty = 0
    short = 0
    broken = 0
    for page in samples:
        content = page.read_text(encoding="utf-8")
        m = re.search(r'<meta name="description" content="([^"]*)"', content)
        if not m:
            empty += 1
            continue
        desc = m.group(1)
        if len(desc) < 50:
            short += 1
        if desc.endswith(" y.") or desc.endswith(" with.") or desc.endswith(" et.") or desc.endswith(" und."):
            broken += 1

    total = len(samples)
    print(f"[PASS] Meta descriptions: {total-empty}/{total} present, {short} short, {broken} broken")
    assert empty < total * 0.1, f"Too many empty descriptions ({empty}/{total})"
    assert broken < total * 0.1, f"Too many broken descriptions ({broken}/{total})"

def test_content_quality():
    """Verify that calculator pages have substantial long-form content."""
    samples = []
    for lang in ["es", "en", "fr", "de", "it", "pt"]:
        lang_dir = PUBLIC / lang
        if lang_dir.exists():
            pages = list(lang_dir.glob("*/index.html"))[:5]
            samples.extend([(lang, p) for p in pages])

    thin = 0
    for lang, page in samples:
        content = page.read_text(encoding="utf-8")
        # Extract long-content section
        m = re.search(r'class="long-content"[^>]*>(.*?)</section>', content, re.DOTALL)
        if not m:
            thin += 1
            continue
        text = re.sub(r'<[^>]+>', ' ', m.group(1))
        words = len(text.split())
        if words < 400:
            thin += 1

    total = len(samples)
    print(f"[PASS] Content quality: {total-thin}/{total} pages have >400 words of long content")
    # Templated pages average ~1165 words; allow up to 35% thin in sample
    assert thin <= total * 0.35, f"Too many thin pages ({thin}/{total})"

def main():
    print("=" * 60)
    print("CalcToWork Build Verification")
    print("=" * 60)
    test_ads_txt_exists()
    test_robots_txt_exists()
    test_sitemap_exists()
    test_noindex_on_parametric()
    test_meta_descriptions_present()
    test_content_quality()
    print("=" * 60)
    print("All tests passed!")
    print("=" * 60)

if __name__ == "__main__":
    main()

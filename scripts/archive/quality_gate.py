# -*- coding: utf-8 -*-
"""
AdSense Quality Gate — Detects thin content, duplicate text, and low-value signals.
Optimized with sampling for large sites. Ignores headings and short phrases.
Run: python scripts/quality_gate.py [--sample 0.1]
"""
import argparse, json, re, random
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).parent.parent
PUBLIC = ROOT / "public"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

THIN_CONTENT_MIN_WORDS = 80
DUPLICATE_THRESHOLD = 3
SUBSTANTIVE_MIN_CHARS = 100

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html)

def get_substantive_paragraphs(html):
    """Extract paragraphs that are not headings and are substantive."""
    # Remove headings
    body = re.sub(r'<h[1-6][^>]*>.*?</h[1-6]>', ' ', html, flags=re.S)
    text = strip_tags(body)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) >= SUBSTANTIVE_MIN_CHARS]

def analyze(sample_rate=1.0):
    issues = []
    para_counter = Counter()
    page_word_counts = []
    generic_phrases = [
        "below, we explain the mathematical foundation",
        "walk through real-world applications",
        "answer frequently asked questions",
        "with complete confidence",
        "technology moves fast",
        "your calculations should keep up",
    ]

    pages = []
    for lang in LANGS:
        lang_dir = PUBLIC / lang
        if not lang_dir.exists():
            continue
        for calc_dir in lang_dir.iterdir():
            if not calc_dir.is_dir():
                continue
            idx = calc_dir / "index.html"
            if idx.exists():
                pages.append((lang, calc_dir, idx))

    if sample_rate < 1.0:
        sample_size = max(1, int(len(pages) * sample_rate))
        pages = random.sample(pages, sample_size)
        print(f"Sampling {sample_size} of {len(pages)} pages ({sample_rate*100:.0f}%)...")

    for lang, calc_dir, idx in pages:
        try:
            html = idx.read_text(encoding="utf-8")
        except Exception:
            continue
        body_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.S)
        body = body_match.group(1) if body_match else html

        words = len(strip_tags(body).split())
        page_word_counts.append((str(calc_dir), words))
        if words < THIN_CONTENT_MIN_WORDS:
            issues.append(("THIN_CONTENT", str(calc_dir), f"Only {words} words"))

        paras = get_substantive_paragraphs(body)
        for p in paras:
            norm = re.sub(r'\d+', '#', p.lower())
            para_counter[norm] += 1

        text_lower = html.lower()
        for phrase in generic_phrases:
            if phrase in text_lower:
                issues.append(("GENERIC_TEMPLATE", str(calc_dir), phrase))
                break

    duplicate_paras = {p: c for p, c in para_counter.items() if c >= DUPLICATE_THRESHOLD}
    for p, c in duplicate_paras.items():
        issues.append(("DUPLICATE_TEXT", f"Seen on {c} pages", p[:120] + "..."))

    thin = [i for i in issues if i[0] == "THIN_CONTENT"]
    dups = [i for i in issues if i[0] == "DUPLICATE_TEXT"]
    gens = [i for i in issues if i[0] == "GENERIC_TEMPLATE"]

    print("=" * 70)
    print("ADSENSE QUALITY GATE REPORT")
    print("=" * 70)
    print(f"Pages analyzed:                               {len(pages)}")
    print(f"Thin content pages (<{THIN_CONTENT_MIN_WORDS} words): {len(thin)}")
    print(f"Duplicate paragraph signals:                  {len(dups)}")
    print(f"Pages with generic template text:             {len(gens)}")
    print("-" * 70)

    if thin:
        print("\nTHIN CONTENT samples:")
        for _, path, reason in thin[:5]:
            print(f"  - {path}: {reason}")
    if dups:
        print("\nDUPLICATE TEXT samples:")
        for _, count, text in dups[:5]:
            print(f"  - {count}: {text}")
    if gens:
        print("\nGENERIC TEMPLATE samples:")
        for _, path, phrase in gens[:5]:
            print(f"  - {path}: '{phrase}'")

    total_issues = len(thin) + len(dups) + len(gens)
    print("-" * 70)
    if total_issues == 0:
        print("PASS: QUALITY GATE PASSED - No thin content detected.")
        return 0
    else:
        print(f"FAIL: QUALITY GATE FAILED - {total_issues} issues found.")
        return 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", type=float, default=1.0, help="Fraction of pages to analyze (0.0-1.0)")
    args = parser.parse_args()
    exit(analyze(sample_rate=args.sample))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Live site verification - checks deployed site for calculator functionality,
template integrity, SEO uniqueness, and content quality.
"""
import json
import re
from pathlib import Path
from collections import defaultdict
import urllib.request
import urllib.error

BASE_URL = "https://calcto.work"
PUBLIC = Path("public")
LANGS = ["es", "en", "fr", "de", "it", "pt"]

def fetch_or_read(url_path, use_live=False):
    """Fetch from live site or read from local public/."""
    if use_live:
        try:
            url = f"{BASE_URL}{url_path}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"ERROR: {e}"
    else:
        local_path = PUBLIC / url_path.lstrip('/').rstrip('/')
        if local_path.is_file():
            return local_path.read_text(encoding='utf-8')
        index_path = local_path / "index.html"
        if index_path.is_file():
            return index_path.read_text(encoding='utf-8')
        return f"ERROR: File not found: {local_path}"

def check_calculator_page(lang, slug, use_live=False):
    """Comprehensive check of a single calculator page."""
    path = f"/{lang}/{slug}/"
    html = fetch_or_read(path, use_live)
    
    if html.startswith("ERROR:"):
        return {"status": "error", "message": html}
    
    issues = []
    
    # 1. Basic structure
    if '<!DOCTYPE html>' not in html:
        issues.append("Missing DOCTYPE")
    if f'<html lang="{lang}">' not in html:
        issues.append(f"Wrong/missing html lang attribute")
    
    # 2. Meta tags
    title_match = re.search(r'<title>(.*?)</title>', html)
    if not title_match:
        issues.append("Missing <title>")
    else:
        title = title_match.group(1)
        if len(title) < 10 or len(title) > 70:
            issues.append(f"Title length issue: {len(title)} chars")
    
    desc_match = re.search(r'<meta name="description" content="([^"]*)"', html)
    if not desc_match:
        issues.append("Missing meta description")
    else:
        desc = desc_match.group(1)
        if len(desc) < 50 or len(desc) > 160:
            issues.append(f"Description length issue: {len(desc)} chars")
    
    # 3. Canonical
    if '<link rel="canonical"' not in html:
        issues.append("Missing canonical tag")
    
    # 4. Calculator functionality
    if 'calculator.js' not in html:
        issues.append("Missing calculator.js")
    if 'id="calculator-form"' not in html and 'class="calc-form"' not in html:
        issues.append("Missing calculator form")
    
    # 5. Content quality
    long_match = re.search(r'class="long-content"[^>]*>(.*?)</section>', html, re.DOTALL)
    if not long_match:
        issues.append("No long-content section")
        word_count = 0
    else:
        text = re.sub(r'<[^>]+>', ' ', long_match.group(1))
        word_count = len(text.split())
        if word_count < 300:
            issues.append(f"Thin content: {word_count} words")
    
    # 6. Structured data
    if '"SoftwareApplication"' not in html:
        issues.append("Missing SoftwareApplication schema")
    
    # 7. Ads
    if 'adsbygoogle' not in html and lang != "en":  # Some pages might not have ads
        pass  # Not all pages have ads
    
    # 8. Hreflang
    hreflang_count = len(re.findall(r'rel="alternate" hreflang="', html))
    if hreflang_count < 5:
        issues.append(f"Missing hreflang tags (found {hreflang_count})")
    
    return {
        "status": "ok" if not issues else "issues",
        "issues": issues,
        "word_count": word_count if 'word_count' in dir() else 0,
        "title": title_match.group(1) if title_match else "",
        "description": desc_match.group(1) if desc_match else "",
    }

def verify_site(sample_size=100, use_live=False):
    """Verify a sample of calculator pages across all languages."""
    import json
    
    with open("src/calculators/calculators.json", "r", encoding="utf-8") as f:
        calculators = json.load(f)["calculators"]
    
    # Sample calculators evenly across the range
    step = max(1, len(calculators) // (sample_size // 6))
    sampled = calculators[::step][:sample_size // 6]
    
    all_issues = []
    titles = defaultdict(list)
    descriptions = defaultdict(list)
    word_counts = []
    
    total_checked = 0
    
    for calc in sampled:
        slug = calc["slug"]
        for lang in LANGS:
            total_checked += 1
            result = check_calculator_page(lang, slug, use_live)
            
            if result["status"] == "error":
                all_issues.append(f"[{lang}/{slug}] {result['message']}")
                continue
            
            if result["issues"]:
                for issue in result["issues"]:
                    all_issues.append(f"[{lang}/{slug}] {issue}")
            
            if result["title"]:
                titles[result["title"]].append(f"{lang}/{slug}")
            if result["description"]:
                descriptions[result["description"]].append(f"{lang}/{slug}")
            
            word_counts.append(result["word_count"])
            
            if total_checked % 50 == 0:
                print(f"  Checked {total_checked} pages...")
    
    # Analysis
    print("\n" + "=" * 80)
    print("VERIFICATION RESULTS")
    print("=" * 80)
    print(f"Total pages checked: {total_checked}")
    print(f"Pages with issues: {len([i for i in all_issues if not i.startswith('[') or 'ERROR' not in i])}")
    
    # Duplicate analysis
    dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
    dup_descs = {k: v for k, v in descriptions.items() if len(v) > 1}
    
    print(f"\nDuplicate titles: {len(dup_titles)} (affecting {sum(len(v) for v in dup_titles.values())} pages)")
    print(f"Duplicate descriptions: {len(dup_descs)} (affecting {sum(len(v) for v in dup_descs.values())} pages)")
    
    if word_counts:
        avg_words = sum(word_counts) / len(word_counts)
        print(f"\nContent word counts: avg={avg_words:.0f}, min={min(word_counts)}, max={max(word_counts)}")
    
    print(f"\nIssues found: {len(all_issues)}")
    for issue in all_issues[:30]:
        print(f"  {issue}")
    
    if len(all_issues) > 30:
        print(f"  ... and {len(all_issues) - 30} more")
    
    return all_issues

if __name__ == "__main__":
    print("Checking local build (set use_live=True to check deployed site)...")
    verify_site(sample_size=120, use_live=False)

#!/usr/bin/env python3
"""
Verify all built calculator pages in public/ directory.
"""
import re
from pathlib import Path
from collections import defaultdict

PUBLIC = Path("public")
LANGS = ["es", "en", "fr", "de", "it", "pt"]

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html)

def check_page(path):
    """Check a single HTML page."""
    html = path.read_text(encoding='utf-8')
    issues = []
    
    # 1. Meta title
    m = re.search(r'<title>(.*?)</title>', html)
    title = m.group(1) if m else ""
    if not title:
        issues.append("Missing title")
    elif len(title) < 10:
        issues.append(f"Title too short: {len(title)}")
    
    # 2. Meta description
    m = re.search(r'<meta name="description" content="([^"]*)"', html)
    desc = m.group(1) if m else ""
    if not desc:
        issues.append("Missing description")
    elif len(desc) < 50:
        issues.append(f"Description too short: {len(desc)}")
    
    # 3. Long content
    m = re.search(r'class="long-content"[^>]*>(.*?)</section>', html, re.DOTALL)
    if m:
        text = strip_tags(m.group(1))
        words = len(text.split())
        if words < 300:
            issues.append(f"Thin content: {words}w")
    else:
        words = 0
        issues.append("No long-content")
    
    # 4. Calculator JS
    if 'calculator.js' not in html:
        issues.append("Missing calculator.js")
    
    # 5. Schema
    if '"SoftwareApplication"' not in html:
        issues.append("Missing SoftwareApplication schema")
    
    return {"title": title, "desc": desc, "words": words, "issues": issues}

def verify_all():
    print("Scanning all built pages in public/...")
    
    all_issues = []
    titles = defaultdict(list)
    descs = defaultdict(list)
    word_counts = []
    checked = 0
    
    for lang in LANGS:
        lang_dir = PUBLIC / lang
        if not lang_dir.exists():
            continue
        
        for page in lang_dir.glob("*/index.html"):
            slug = page.parent.name
            if slug in ('about', 'contact', 'privacy', 'terms'):
                continue
            
            checked += 1
            result = check_page(page)
            
            if result["title"]:
                titles[result["title"]].append(f"{lang}/{slug}")
            if result["desc"]:
                descs[result["desc"]].append(f"{lang}/{slug}")
            word_counts.append(result["words"])
            
            for issue in result["issues"]:
                all_issues.append(f"[{lang}/{slug}] {issue}")
            
            if checked % 500 == 0:
                print(f"  Checked {checked} pages...")
    
    # Analyze duplicates
    dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
    dup_descs = {k: v for k, v in descs.items() if len(v) > 1}
    
    print("\n" + "=" * 80)
    print("VERIFICATION RESULTS")
    print("=" * 80)
    print(f"Total pages checked: {checked}")
    print(f"Pages with issues: {len([i for i in all_issues if 'ERROR' not in i])}")
    
    print(f"\nDuplicate titles: {len(dup_titles)} (affecting {sum(len(v) for v in dup_titles.values())} pages)")
    if dup_titles:
        for title, pages in sorted(dup_titles.items(), key=lambda x: -len(x[1]))[:10]:
            print(f"  '{title[:60]}' -> {len(pages)} pages")
    
    print(f"\nDuplicate descriptions: {len(dup_descs)} (affecting {sum(len(v) for v in dup_descs.values())} pages)")
    if dup_descs:
        for desc, pages in sorted(dup_descs.items(), key=lambda x: -len(x[1]))[:10]:
            print(f"  '{desc[:60]}' -> {len(pages)} pages")
    
    if word_counts:
        print(f"\nWord counts: avg={sum(word_counts)/len(word_counts):.0f}, min={min(word_counts)}, max={max(word_counts)}")
    
    print(f"\nAll issues ({len(all_issues)}):")
    for issue in sorted(all_issues)[:50]:
        print(f"  {issue}")
    if len(all_issues) > 50:
        print(f"  ... and {len(all_issues) - 50} more")
    
    return all_issues

if __name__ == "__main__":
    verify_all()

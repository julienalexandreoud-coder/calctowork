#!/usr/bin/env python3
"""
Fast verification of base calculator pages only.
"""
import re
from pathlib import Path
from collections import defaultdict

PUBLIC = Path("public")
LANGS = ["es", "en", "fr", "de", "it", "pt"]

def verify_fast():
    print("Scanning base calculator pages...")
    
    all_issues = []
    titles = defaultdict(list)
    descs = defaultdict(list)
    thin = []
    checked = 0
    
    for lang in LANGS:
        lang_dir = PUBLIC / lang
        if not lang_dir.exists():
            continue
        
        # Only direct subdirs (base pages, not parametric)
        for subdir in lang_dir.iterdir():
            if not subdir.is_dir():
                continue
            slug = subdir.name
            if slug in ('about', 'contact', 'privacy', 'terms'):
                continue
            # Skip if has subdirs (parametric base)
            has_subdirs = any(d.is_dir() for d in subdir.iterdir())
            
            page = subdir / "index.html"
            if not page.exists():
                continue
            
            checked += 1
            html = page.read_text(encoding='utf-8')
            
            # Title
            m = re.search(r'<title>(.*?)</title>', html)
            title = m.group(1) if m else ""
            if title:
                titles[title].append(f"{lang}/{slug}")
            else:
                all_issues.append(f"[{lang}/{slug}] Missing title")
            
            # Description
            m = re.search(r'<meta name="description" content="([^"]*)"', html)
            desc = m.group(1) if m else ""
            if desc:
                descs[desc].append(f"{lang}/{slug}")
                if len(desc) < 50:
                    all_issues.append(f"[{lang}/{slug}] Short desc: {len(desc)}")
            else:
                all_issues.append(f"[{lang}/{slug}] Missing description")
            
            # Content (quick check)
            if 'long-content' not in html:
                all_issues.append(f"[{lang}/{slug}] No long-content")
            
            # Calculator JS
            if 'calculator.js' not in html:
                all_issues.append(f"[{lang}/{slug}] Missing calculator.js")
            
            if checked % 500 == 0:
                print(f"  Checked {checked} pages...")
    
    # Duplicates
    dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
    dup_descs = {k: v for k, v in descs.items() if len(v) > 1}
    
    print("\n" + "=" * 80)
    print("VERIFICATION RESULTS")
    print("=" * 80)
    print(f"Base pages checked: {checked}")
    print(f"Issues: {len(all_issues)}")
    print(f"Duplicate titles: {len(dup_titles)}")
    print(f"Duplicate descriptions: {len(dup_descs)}")
    
    if dup_titles:
        print("\nTop duplicate titles:")
        for title, pages in sorted(dup_titles.items(), key=lambda x: -len(x[1]))[:10]:
            print(f"  '{title[:60]}' -> {len(pages)} pages")
    
    if dup_descs:
        print("\nTop duplicate descriptions:")
        for desc, pages in sorted(dup_descs.items(), key=lambda x: -len(x[1]))[:10]:
            print(f"  '{desc[:60]}' -> {len(pages)} pages")
    
    if all_issues:
        print("\nSample issues:")
        for issue in sorted(all_issues)[:30]:
            print(f"  {issue}")
        if len(all_issues) > 30:
            print(f"  ... and {len(all_issues) - 30} more")
    
    return all_issues

if __name__ == "__main__":
    verify_fast()

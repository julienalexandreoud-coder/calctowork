#!/usr/bin/env python3
"""
Comprehensive audit of all 2,646 calculator pages across 6 languages.
Checks: functionality, SEO uniqueness, content quality, i18n completeness.
"""
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
PUBLIC = ROOT / "public"
SRC = ROOT / "src"
I18N_DIR = SRC / "i18n"
CONTENT_DIR = SRC / "content"
CALCULATORS_JSON = SRC / "calculators" / "calculators.json"

LANGS = ["es", "en", "fr", "de", "it", "pt"]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html)

def audit_all():
    print("=" * 80)
    print("COMPREHENSIVE SITE AUDIT - All 2,646 Pages")
    print("=" * 80)
    
    # Load data
    calculators = load_json(CALCULATORS_JSON)["calculators"]
    calc_by_id = {c["id"]: c for c in calculators}
    
    translations = {}
    for lang in LANGS:
        translations[lang] = load_json(I18N_DIR / f"{lang}.json")
    
    # Tracking structures
    issues = []
    meta_titles = defaultdict(list)
    meta_descriptions = defaultdict(list)
    thin_content = []
    templated_content = []
    missing_content_files = []
    missing_i18n_fields = []
    duplicate_titles_list = []
    duplicate_descs_list = []
    formula_issues = []
    
    total_pages = 0
    pages_with_content = 0
    pages_without_content = 0
    
    for calc in calculators:
        cid = calc["id"]
        slug = calc["slug"]
        
        for lang in LANGS:
            total_pages += 1
            if total_pages % 500 == 0:
                print(f"  Audited {total_pages} pages...")
            
            # 1. Check content file exists (PRIMARY quality source)
            content_file = CONTENT_DIR / lang / f"{cid}.html"
            if content_file.exists():
                pages_with_content += 1
                content_html = content_file.read_text(encoding="utf-8")
                text = strip_tags(content_html)
                words = len(text.split())
                
                if words < 400:
                    thin_content.append((lang, cid, slug, words))
                
                # Check for templated indicators
                if 'class="formula-section"' in content_html or '<h1>' in content_html:
                    templated_content.append((lang, cid, slug, words))
            else:
                pages_without_content += 1
                missing_content_files.append((lang, cid, slug))
            
            # 2. Check i18n completeness
            i18n_calc = translations[lang].get("calculators", {}).get(cid, {})
            if not i18n_calc:
                missing_i18n_fields.append(f"[{lang}/{cid}] Missing entire i18n entry")
            else:
                required_fields = ["name", "desc", "inputs", "outputs"]
                for field in required_fields:
                    val = i18n_calc.get(field)
                    if not val or (isinstance(val, str) and not val.strip()):
                        missing_i18n_fields.append(f"[{lang}/{cid}] Empty i18n field: {field}")
                
                # Check SEO fields
                seo_desc = i18n_calc.get("seo_description") or i18n_calc.get("seo_desc", "")
                if not seo_desc or len(seo_desc) < 50:
                    missing_i18n_fields.append(f"[{lang}/{cid}] Short/missing seo_description: '{seo_desc[:50]}'")
            
            # 3. Check public HTML for SEO
            page_path = PUBLIC / lang / slug / "index.html"
            if page_path.exists():
                html = page_path.read_text(encoding="utf-8")
                
                # Meta title
                title_match = re.search(r'<title>(.*?)</title>', html)
                if title_match:
                    title = title_match.group(1)
                    meta_titles[title].append(f"{lang}/{cid}/{slug}")
                else:
                    issues.append(f"[{lang}/{cid}] Missing <title>")
                
                # Meta description
                desc_match = re.search(r'<meta name="description" content="([^"]*)"', html)
                if desc_match:
                    desc = desc_match.group(1)
                    if len(desc) < 50:
                        issues.append(f"[{lang}/{cid}] Meta description too short ({len(desc)} chars)")
                    meta_descriptions[desc].append(f"{lang}/{cid}/{slug}")
                else:
                    issues.append(f"[{lang}/{cid}] Missing meta description")
                
                # Calculator JS loaded
                if 'calculator.js' not in html:
                    issues.append(f"[{lang}/{cid}] Missing calculator.js reference")
                
                # Structured data
                if '"SoftwareApplication"' not in html:
                    issues.append(f"[{lang}/{cid}] Missing SoftwareApplication schema")
            else:
                issues.append(f"[{lang}/{cid}] HTML page not found in public/")
            
            # 4. Check formula validity
            if lang == "es":  # Only check once per calculator
                formula = calc.get("formula", "")
                if not formula:
                    formula_issues.append(f"[{cid}] Missing formula")
    
    # Analyze duplicates
    dup_titles = {k: v for k, v in meta_titles.items() if len(v) > 1}
    dup_descs = {k: v for k, v in meta_descriptions.items() if len(v) > 1}
    
    # Print results
    print("\n" + "=" * 80)
    print("AUDIT RESULTS SUMMARY")
    print("=" * 80)
    print(f"\nTotal calculators: {len(calculators)}")
    print(f"Total pages (calc × 6 langs): {total_pages}")
    print(f"Pages with content files: {pages_with_content}")
    print(f"Pages missing content files: {pages_without_content}")
    
    print(f"\n--- CONTENT QUALITY ---")
    print(f"Thin content (< 400 words): {len(thin_content)} pages")
    print(f"Templated content (rigid structure): {len(templated_content)} pages")
    print(f"Missing content files: {len(missing_content_files)} pages")
    
    print(f"\n--- SEO UNIQUENESS ---")
    print(f"Duplicate meta titles: {len(dup_titles)} titles affecting {sum(len(v) for v in dup_titles.values())} pages")
    print(f"Duplicate meta descriptions: {len(dup_descs)} descriptions affecting {sum(len(v) for v in dup_descs.values())} pages")
    
    print(f"\n--- I18N COMPLETENESS ---")
    print(f"Missing/empty i18n fields: {len(missing_i18n_fields)}")
    
    print(f"\n--- FORMULA VALIDITY ---")
    print(f"Formula issues: {len(formula_issues)}")
    
    print(f"\n--- OTHER ISSUES ---")
    print(f"Other HTML/structural issues: {len(issues)}")
    
    # Detailed reports
    print("\n" + "=" * 80)
    print("TOP ISSUES BY CATEGORY")
    print("=" * 80)
    
    if thin_content:
        print("\nTHIN CONTENT (worst 20):")
        for lang, cid, slug, words in sorted(thin_content, key=lambda x: x[3])[:20]:
            print(f"  [{lang}/{cid}/{slug}]: {words} words")
    
    if templated_content:
        print("\nTEMPLATED CONTENT (first 20):")
        for lang, cid, slug, words in templated_content[:20]:
            print(f"  [{lang}/{cid}/{slug}]: {words} words")
    
    if missing_content_files:
        print("\nMISSING CONTENT FILES (first 20):")
        for lang, cid, slug in missing_content_files[:20]:
            print(f"  [{lang}/{cid}/{slug}]")
    
    if dup_titles:
        print("\nDUPLICATE TITLES (worst 10):")
        for title, pages in sorted(dup_titles.items(), key=lambda x: -len(x[1]))[:10]:
            print(f"  '{title[:70]}' -> {len(pages)} pages")
            for p in pages[:3]:
                print(f"    - {p}")
    
    if dup_descs:
        print("\nDUPLICATE DESCRIPTIONS (worst 10):")
        for desc, pages in sorted(dup_descs.items(), key=lambda x: -len(x[1]))[:10]:
            print(f"  '{desc[:70]}' -> {len(pages)} pages")
            for p in pages[:3]:
                print(f"    - {p}")
    
    if missing_i18n_fields:
        print("\nMISSING I18N (first 20):")
        for item in missing_i18n_fields[:20]:
            print(f"  {item}")
    
    if formula_issues:
        print("\nFORMULA ISSUES:")
        for item in formula_issues:
            print(f"  {item}")
    
    if issues:
        print("\nOTHER ISSUES (first 20):")
        for issue in issues[:20]:
            print(f"  {issue}")
    
    # Save report
    report_path = ROOT / "audit_comprehensive.json"
    report = {
        "total_pages": total_pages,
        "pages_with_content": pages_with_content,
        "pages_without_content": pages_without_content,
        "thin_content": thin_content,
        "templated_content": templated_content,
        "missing_content_files": missing_content_files,
        "duplicate_titles": {k: v for k, v in dup_titles.items()},
        "duplicate_descriptions": {k: v for k, v in dup_descs.items()},
        "missing_i18n": missing_i18n_fields,
        "formula_issues": formula_issues,
        "other_issues": issues,
    }
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\nDetailed report saved to: {report_path}")
    print("=" * 80)

if __name__ == "__main__":
    audit_all()

#!/usr/bin/env python3
"""Fix broken related calculator links across all language content files."""
import re, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tools_config import TOOL_BY_ID

CONTENT_DIR = Path(r'C:\Microsaas\obra\src\content')
LANGS = ['en', 'es', 'fr', 'de', 'it', 'pt']

# Build mapping from English calculator name to calculator ID
i18n_en = json.load(open(CONTENT_DIR.parent / 'i18n' / 'en.json', encoding='utf-8'))
calcs = i18n_en.get('calculators', {})

name_to_id = {}
for cid, data in calcs.items():
    name = data.get('name', '').lower().strip()
    if name:
        name_to_id[name] = cid

# Manual overrides for names that don't match automatically
NAME_OVERRIDES = {
    'Z Score Calculator': '609',
    'Z-Score Calculator': '609',
    'Investment Calculator': '310',
    'Construction Signage Calculator': '089',
    'Natural Logarithm Calculator': '131',
    'Quadratic Polynomial Derivative Calculator': '118',
    'Midrange Calculator': '136',
    'Break Even Calculator': '307',
}

def find_cid(name_text):
    """Find calculator ID for a given link text."""
    name_lower = name_text.lower().strip()
    
    # Check manual overrides first
    if name_text in NAME_OVERRIDES:
        return NAME_OVERRIDES[name_text]
    
    # Direct match
    if name_lower in name_to_id:
        return name_to_id[name_lower]
    
    # Fuzzy match
    for calc_name, cid in name_to_id.items():
        if name_lower == calc_name:
            return cid
        if len(name_lower) > 8 and (name_lower in calc_name or calc_name in name_lower):
            # Avoid false matches like "Construction Signage" matching "Age"
            words = set(name_lower.split())
            calc_words = set(calc_name.split())
            common = words & calc_words
            if len(common) >= 2:
                return cid
    
    return None

def get_slug(cid, lang):
    """Get slug for calculator in given language."""
    if cid in TOOL_BY_ID:
        slug_info = TOOL_BY_ID[cid].get('slugs', {})
        if lang in slug_info:
            return slug_info[lang]
    return None

def main():
    total_fixed = 0
    
    for lang in LANGS:
        ld = CONTENT_DIR / lang
        if not ld.exists():
            continue
        
        fixed_files = 0
        for f in sorted(ld.glob('*.html')):
            content = f.read_text(encoding='utf-8')
            if '/en/ohms-law/' not in content:
                continue
            
            def replace_link(m):
                href = m.group(1)
                text = m.group(2)
                if '/en/ohms-law/' not in href:
                    return m.group(0)
                
                cid = find_cid(text)
                if cid:
                    slug = get_slug(cid, lang)
                    if slug:
                        new_href = f'/{lang}/{slug}/'
                        full_orig = m.group(0)
                        full_new = full_orig.replace(href, new_href)
                        return full_new
                
                # If no match found, just point to the calculator search
                return m.group(0)
            
            new_content = re.sub(r'<a\s+href="([^"]*)"\s*>([^<]*)</a>', replace_link, content)
            
            if new_content != content:
                f.write_text(new_content, encoding='utf-8')
                fixed_files += 1
                total_fixed += 1
        
        if fixed_files:
            print(f'{lang}: fixed {fixed_files} files')
    
    print(f'\nTotal: {total_fixed} files fixed across all languages')

if __name__ == '__main__':
    main()

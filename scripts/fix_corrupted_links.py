"""Fix corrupted see-also links using proper slug mapping."""
import re, sys, json
from pathlib import Path

sys.path.insert(0, str(Path(r'C:\Microsaas\obra\scripts')))
from tools_config import TOOL_BY_ID

d = Path(r'C:\Microsaas\obra\src\content')
i18n_en = json.load(open(d.parent / 'i18n' / 'en.json', encoding='utf-8'))
calcs = i18n_en.get('calculators', {})

# Build name-to-ID mapping
name_to_id = {}
for cid, data in calcs.items():
    name = data.get('name', '').lower().strip()
    if name:
        name_to_id[name] = cid

NAME_OVERRIDES = {
    'Construction Signage Calculator': '089',
}

def find_cid(name_text):
    name_lower = name_text.lower().strip()
    if name_text in NAME_OVERRIDES:
        return NAME_OVERRIDES[name_text]
    if name_lower in name_to_id:
        return name_to_id[name_lower]
    return None

def get_slug(cid, lang):
    if cid in TOOL_BY_ID:
        slugs = TOOL_BY_ID[cid].get('slugs', {})
        if lang in slugs:
            return slugs[lang]
    return None

# Step 1: Clean corrupted href patterns
for lang in ['es', 'fr', 'de', 'it', 'pt']:
    ld = d / lang
    for f in ld.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        original = content
        # Remove the broken regex artifact
        content = re.sub(r'href="/[a-z]{2}/" \+ r"[^"]*"', 'href="/' + lang + '/"', content)
        if content != original:
            f.write_text(content, encoding='utf-8')

print('Step 1: Cleaned corrupted href patterns')

# Step 2: Re-map all see-also backlinks to proper slugs
total = 0
for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
    ld = d / lang
    if not ld.exists():
        continue
    n = 0
    for f in ld.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        original = content
        
        def replace_link(m):
            href = m.group(1)
            text = m.group(2)
            if href == '/' + lang + '/':
                cid = find_cid(text)
                if cid:
                    slug = get_slug(cid, lang)
                    if slug:
                        return m.group(0).replace(href, '/' + lang + '/' + slug + '/')
            return m.group(0)
        
        content = re.sub(r'<a\s+href="([^"]*)"\s*>([^<]*)</a>', replace_link, content)
        if content != original:
            f.write_text(content, encoding='utf-8')
            n += 1
    total += n
    print(f'  {lang}: {n} files')

print(f'Step 2: Re-mapped links in {total} files')

# Verify
print('\nVerification:')
for lang in ['fr', 'de']:
    f = d / lang / '097.html'
    if f.exists():
        content = f.read_text(encoding='utf-8')
        see = re.search(r'<p class="see-also">.*?</p>', content, re.DOTALL)
        if see:
            print(f'{lang}: {see.group(0)[:250]}')

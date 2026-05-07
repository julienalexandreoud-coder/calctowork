"""Fix broken links in content files."""
import os, re, json, glob
from difflib import get_close_matches

id_to_slug = {}
id_to_block = {}
tool_slugs = {}

for fp in glob.glob('src/calculators/*.json'):
    with open(fp,'r',encoding='utf-8') as f:
        d = json.load(f)
    id_to_slug[d['id']] = d['slug']
    id_to_block[d['id']] = d['block_slug']

config_path = 'config/tools_config.py'
if os.path.exists(config_path):
    with open(config_path,'r',encoding='utf-8') as f:
        ttext = f.read()
    # Match tool entries with per-language slugs
    for m in re.finditer(r'"id":\s*"(\d+)".*?"slugs":\s*\{([^}]+)\}', ttext, re.DOTALL):
        tid = m.group(1)
        slug_block = m.group(2)
        for lang_match in re.finditer(r'"(\w+)":\s*"([^"]+)"', slug_block):
            lang = lang_match.group(1)
            slug = lang_match.group(2)
            tool_slugs[(tid, lang)] = slug

valid_slugs = set()
for lang_dir in os.listdir('public'):
    lang_path = os.path.join('public', lang_dir)
    if not os.path.isdir(lang_path) or lang_dir.startswith('.'):
        continue
    for item in os.listdir(lang_path):
        if os.path.isdir(os.path.join(lang_path, item)):
            valid_slugs.add(item)

for slug in id_to_slug.values():
    valid_slugs.add(slug)

slug_to_id = {}
for cid, slug in id_to_slug.items():
    slug_to_id[slug] = cid

# Build per-language valid slug sets
lang_valid_slugs = {}
for lang_dir in os.listdir('public'):
    lang_path = os.path.join('public', lang_dir)
    if not os.path.isdir(lang_path) or lang_dir.startswith('.'):
        continue
    slugs = set()
    for item in os.listdir(lang_path):
        if os.path.isdir(os.path.join(lang_path, item)):
            slugs.add(item)
    lang_valid_slugs[lang_dir] = slugs

def resolve_slug(lang, ref):
    ref = ref.rstrip('/')
    # Check if ref exists in THIS language's public dir
    if lang in lang_valid_slugs and ref in lang_valid_slugs[lang]:
        return ref
    if ref.isdigit():
        tid = ref
        key = (tid, lang)
        if key in tool_slugs:
            return tool_slugs[key]
        if tid in id_to_slug:
            return id_to_slug[tid]
    # Try looking up ref as slug in any language -> find ID -> resolve to target
    if ref in slug_to_id:
        tid = slug_to_id[ref]
        key = (tid, lang)
        if key in tool_slugs:
            return tool_slugs[key]
        if tid in id_to_slug:
            target_slug = id_to_slug[tid]
            if lang in lang_valid_slugs and target_slug in lang_valid_slugs[lang]:
                return target_slug
    # Fuzzy fallback against THIS language's slugs
    if lang in lang_valid_slugs:
        matches = get_close_matches(ref, list(lang_valid_slugs[lang]), n=1, cutoff=0.35)
        if matches:
            return matches[0]
    return None

total_fixed = 0

def fix_file(fp, lang_dir):
    global total_fixed
    with open(fp, 'r', encoding='utf-8-sig') as f:
        text = f.read()
    
    changed = False
    
    def fix_href(m):
        nonlocal changed
        href = m.group(1)
        clean = href.rstrip('/')
        for prefix in ('es/','en/','fr/','pt/','de/','it/'):
            if clean.startswith(prefix):
                lang_prefix = prefix
                clean = clean[len(prefix):]
                break
        else:
            lang_prefix = f'{lang_dir}/'
        
        if clean in ('css/styles.css','js/calculator.js','js/dark-mode.js','js/favorites.js',
                    'js/history.js','js/cookie-consent.js','js/email-capture.js',
                    'js/analytics-tracker.js','sw.js','manifest.json','favicon.svg',
                    'apple-touch-icon.png','privacy','terms','contact','about'):
            return m.group(0)
        if clean in ('es','en','fr','pt','de','it'):
            return m.group(0)
        
        if lang_dir in lang_valid_slugs and clean in lang_valid_slugs[lang_dir]:
            return m.group(0)
        
        new_slug = resolve_slug(lang_dir, clean)
        if new_slug:
            changed = True
            return f'href="/{lang_prefix}{new_slug}/"'
        
        return m.group(0)
    
    text = re.sub(r'href="/([^"]*)"', fix_href, text)
    
    if changed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(text)
        total_fixed += 1
        return True
    return False

for lang_dir in os.listdir('src/content'):
    lang_path = os.path.join('src/content', lang_dir)
    if not os.path.isdir(lang_path) or lang_dir.startswith('.'):
        continue
    for fp in sorted(glob.glob(os.path.join(lang_path, '*.html'))):
        if fix_file(fp, lang_dir):
            print(f'  Fixed: {fp}')

print(f'\nTotal files fixed: {total_fixed}')

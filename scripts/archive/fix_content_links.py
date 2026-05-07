"""Fix broken internal links in long-form content files."""
import glob, re, os

CONTENT_DIR = "src/content"

good_prefixes = ('css/', 'js/', 'img/', 'sw.js', 'manifest.json', 'favicon.svg', 'apple-touch-icon.png')
langs = ('es/', 'en/', 'fr/', 'pt/', 'de/', 'it/')
all_good = good_prefixes + langs

total_fixed = 0

def fix_file(fp, lang_prefix):
    global total_fixed
    with open(fp, 'r', encoding='utf-8-sig') as f:
        text = f.read()
    
    original = text
    changed = False
    
    def fix_href(m):
        nonlocal changed
        path = m.group(1)
        if path.startswith(all_good):
            return m.group(0)
        changed = True
        return f'href="/{lang_prefix}{path}"'
    
    text = re.sub(r'href="/([^"]*)"', fix_href, text)
    
    def fix_src(m):
        nonlocal changed
        path = m.group(1)
        if path.startswith(all_good):
            return m.group(0)
        changed = True
        return f'src="/{lang_prefix}{path}"'
    
    text = re.sub(r'src="/([^"]*)"', fix_src, text)
    
    if changed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(text)
        total_fixed += 1
        return True
    return False

for lang_dir in os.listdir(CONTENT_DIR):
    lang_path = os.path.join(CONTENT_DIR, lang_dir)
    if not os.path.isdir(lang_path) or lang_dir.startswith('.'):
        continue
    
    lang_prefix = lang_dir + '/'
    
    for fp in sorted(glob.glob(os.path.join(lang_path, '*.html'))):
        if fix_file(fp, lang_prefix):
            print(f'  Fixed: {fp}')

print(f'\nTotal files fixed: {total_fixed}')

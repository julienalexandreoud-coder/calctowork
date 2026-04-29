import json
from pathlib import Path
from collections import defaultdict

# Check i18n for duplicates (fast - just JSON)
LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt']
I18N_DIR = Path('src/i18n')

print("Checking i18n for duplicate descriptions...")

dup_descs = defaultdict(list)
short_descs = []
missing_fields = []

for lang in LANGS:
    data = json.load(open(I18N_DIR / f'{lang}.json', encoding='utf-8'))
    calcs = data.get('calculators', {})
    for cid, calc in calcs.items():
        desc = calc.get('seo_description', '') or calc.get('seo_desc', '')
        if desc:
            dup_descs[desc].append(f'{lang}/{cid}')
            if len(desc) < 50:
                short_descs.append(f'{lang}/{cid}: {desc[:50]}')
        else:
            missing_fields.append(f'{lang}/{cid}: missing desc')
        
        if not calc.get('name'):
            missing_fields.append(f'{lang}/{cid}: missing name')
        if not calc.get('inputs'):
            missing_fields.append(f'{lang}/{cid}: missing inputs')

# Report
dupes = {k: v for k, v in dup_descs.items() if len(v) > 1}
print(f"Duplicate descriptions: {len(dupes)} strings affecting {sum(len(v) for v in dupes.values())} entries")
for desc, pages in sorted(dupes.items(), key=lambda x: -len(x[1]))[:10]:
    print(f"  '{desc[:60]}' -> {len(pages)} entries: {', '.join(pages[:3])}")

print(f"\nShort descriptions: {len(short_descs)}")
print(f"Missing fields: {len(missing_fields)}")
for item in missing_fields[:10]:
    print(f"  {item}")

# Check content files word counts (sample)
print("\nChecking content file word counts...")
CONTENT_DIR = Path('src/content')
thin = []
for lang in ['en', 'es']:
    lang_dir = CONTENT_DIR / lang
    if not lang_dir.exists():
        continue
    for f in lang_dir.glob('*.html'):
        text = f.read_text(encoding='utf-8')
        words = len(text.split())
        if words < 400:
            thin.append((lang, f.stem, words))

print(f"Thin content files (<400 words): {len(thin)}")
for item in sorted(thin, key=lambda x: x[2])[:20]:
    print(f"  {item}")

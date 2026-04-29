import re, json
from pathlib import Path

PUBLIC_DIR = Path(__file__).parent.parent / 'public'
I18N_DIR = Path(__file__).parent.parent / 'src' / 'i18n'
SKIP = {
    'about','contact','privacy','terms','ciencia','clima','climatizacion',
    'cotidiano','deportes','electricidad','electronica','estadistica',
    'estructuras','finanzas','fontaneria','gestion','ingenieria',
    'mamposteria','matematicas','pavimentos','pintura','carpinteria',
    'quimica','salud','transporte','utilidades','fotografia','conversion',
}

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html)

# FAQ duplicates in EN
print('=== EN FAQ DUPLICATES ===')
en_dir = PUBLIC_DIR / 'en'
faq_q_map = {}
for html_file in en_dir.glob('*/index.html'):
    slug = html_file.parent.name
    if slug in SKIP:
        continue
    content = html_file.read_text(encoding='utf-8')
    faq_sec = re.search(r'class=.faq-section.>(.*?)</section>', content, re.DOTALL)
    if not faq_sec:
        continue
    questions = re.findall(r'class=.faq-q.[^>]*>(.*?)</button>', faq_sec.group(1), re.DOTALL)
    questions = [strip_tags(q).strip() for q in questions]
    for q in questions:
        if q not in faq_q_map:
            faq_q_map[q] = []
        faq_q_map[q].append(slug)

dupes = {q: s for q, s in faq_q_map.items() if len(s) > 1}
print(f'Total unique FAQ Qs: {len(faq_q_map)}')
print(f'Duplicate FAQ Qs: {len(dupes)}')
for q, slugs in sorted(dupes.items(), key=lambda x: -len(x[1]))[:15]:
    print(f'  [{len(slugs)}x] "{q[:80]}"')
    print(f'       calcs: {", ".join(slugs[:4])}{"..." if len(slugs)>4 else ""}')

# I18N quality
print()
print('=== I18N SEO_DESCRIPTION QUALITY ===')
GENERIC = [
    'Free online tool with formula and worked',
    'professional-grade formula',
    'Accurate, fast calculation with clear',
    'Easy-to-use calculator with formula',
    'Enter your values and get precise',
]
for lang in ['en','es','fr','pt','de','it']:
    fpath = I18N_DIR / f'{lang}.json'
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    generic_count = 0
    good_count = 0
    short_count = 0
    dupe_seo = {}
    
    for cid, ci in calcs.items():
        desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        name = ci.get('name', '')
        if desc not in dupe_seo:
            dupe_seo[desc] = 0
        dupe_seo[desc] += 1
    
    dupe_count = sum(1 for d, c in dupe_seo.items() if c > 1 and d)
    print(f'{lang}: good={good_count}, generic={generic_count}, short={short_count}, dupe_seo_descs={dupe_count}')

print()
print('=== EN GENERIC/PADDED SEO DESCRIPTIONS ===')
fpath = I18N_DIR / 'en.json'
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']
count = 0
for cid, ci in calcs.items():
    desc = ci.get('seo_description', '')
    for p in GENERIC:
        if p in desc:
            count += 1
            if count <= 10:
                print(f'  [{cid}] {ci.get("name","")}: {desc[-100:]}')
            break
print(f'Total generic/padded: {count}/441')

# Check "desc" field quality (short descriptions)
print()
print('=== SHORT desc FIELD (i18n) ===')
for lang in ['en']:
    fpath = I18N_DIR / f'{lang}.json'
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    very_short = []
    for cid, ci in calcs.items():
        desc = ci.get('desc', '')
        if len(desc) < 40:
            very_short.append((cid, ci.get('name',''), desc))
    
    print(f'EN: {len(very_short)} calculators with desc < 40 chars')
    for cid, name, d in very_short[:10]:
        print(f'  [{cid}] {name}: "{d}"')

import os, re, json
from pathlib import Path

PUBLIC_DIR = Path(__file__).parent.parent / 'public'
I18N_DIR = Path(__file__).parent.parent / 'src' / 'i18n'
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

SKIP = {
    'about','contact','privacy','terms','ciencia','clima','climatizacion',
    'cotidiano','deportes','electricidad','electronica','estadistica',
    'estructuras','finanzas','fontaneria','gestion','ingenieria',
    'mamposteria','matematicas','pavimentos','pintura','carpinteria',
    'quimica','salud','transporte','utilidades','fotografia','conversion',
}

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html)

def analyze_lang(lang):
    lang_dir = PUBLIC_DIR / lang
    if not lang_dir.exists():
        return
    
    total = 0
    has_long = 0
    has_faq = 0
    has_howto = 0
    has_faq_schema = 0
    has_related = 0
    word_counts = []
    short_content = []
    
    for html_file in lang_dir.glob('*/index.html'):
        slug = html_file.parent.name
        if slug in SKIP:
            continue
        total += 1
        content = html_file.read_text(encoding='utf-8')
        
        if 'long-content-wrap' in content:
            has_long += 1
            m = re.search(r'class=.long-content.>(.*?)</section>', content, re.DOTALL)
            if m:
                text = strip_tags(m.group(1))
                words = len(text.split())
                word_counts.append(words)
                if words < 300:
                    short_content.append((slug, words))
        
        if 'faq-section' in content and 'faq-q' in content:
            has_faq += 1
        if '"HowTo"' in content:
            has_howto += 1
        if '"FAQPage"' in content:
            has_faq_schema += 1
        if 'related-section' in content:
            has_related += 1
    
    avg_w = sum(word_counts) / len(word_counts) if word_counts else 0
    print(f'--- {lang} ---')
    print(f'  total={total}, long_content={has_long} ({has_long*100//max(total,1)}%), no_long={total-has_long}')
    print(f'  faq_html={has_faq}, faq_schema={has_faq_schema}, howto_schema={has_howto}, related={has_related}')
    print(f'  words: avg={avg_w:.0f}, min={min(word_counts, default=0)}, max={max(word_counts, default=0)}')
    if short_content:
        print(f'  thin_content (<300w): {len(short_content)} - {short_content[:5]}')
    print()

for lang in LANGS:
    analyze_lang(lang)

# EN deep dive: FAQ duplicates, content quality
print('=== EN FAQ DUPLICATES ===')
en_dir = PUBLIC_DIR / 'en'
faq_q_map = {}
count = 0
for html_file in en_dir.glob('*/index.html'):
    slug = html_file.parent.name
    if slug in SKIP:
        continue
    count += 1
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
print(f'Duplicate FAQ Qs (shared across calcs): {len(dupes)}')
for q, slugs in sorted(dupes.items(), key=lambda x: -len(x[1]))[:10]:
    print(f'  "{q[:70]}" -> {len(slugs)} calcs: {", ".join(slugs[:3])}')

# I18N seo_description quality
print()
print('=== I18N SEO_DESCRIPTION QUALITY ===')
GENERIC = [
    'Free online tool with formula and worked',
    'professional-grade formula',
    'Accurate, fast calculation with clear',
    'Easy-to-use calculator with formula',
    'Enter your values and get precise',
]
for lang in LANGS:
    fpath = I18N_DIR / f'{lang}.json'
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    generic_count = 0
    good_count = 0
    short_count = 0
    dupe_descs = {}
    
    for cid, ci in calcs.items():
        desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        if desc not in dupe_descs:
            dupe_descs[desc] = 0
        dupe_descs[desc] += 1
        
        if any(p in desc for p in GENERIC):
            generic_count += 1
        elif len(desc) < 120:
            short_count += 1
        else:
            good_count += 1
    
    dupe_count = sum(1 for d, c in dupe_descs.items() if c > 1 and d)
    print(f'{lang}: good={good_count}, generic={generic_count}, short={short_count}, dupe_seo_descs={dupe_count}')

# Generic tail details for EN
print()
print('=== EN GENERIC TAILS ===')
fpath = I18N_DIR / 'en.json'
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']
for cid, ci in calcs.items():
    desc = ci.get('seo_description', '')
    for p in GENERIC:
        if p in desc:
            print(f'  [{cid}] {ci.get("name","")}: ...{desc[-80:]}')
            break

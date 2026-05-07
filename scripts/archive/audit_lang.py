import os, re, json
from pathlib import Path

PUBLIC_DIR = Path(__file__).parent.parent / 'public'
SKIP = {
    'about','contact','privacy','terms','ciencia','clima','climatizacion',
    'cotidiano','deportes','electricidad','electronica','estadistica',
    'estructuras','finanzas','fontaneria','gestion','ingenieria',
    'mamposteria','matematicas','pavimentos','pintura','carpinteria',
    'quimica','salud','transporte','utilidades','fotografia','conversion',
}

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html)

lang = os.environ.get('AUDIT_LANG', 'en')
lang_dir = PUBLIC_DIR / lang

total = 0
has_long = 0
has_faq = 0
has_howto = 0
has_faq_schema = 0
has_related = 0
word_counts = []
short_content = []
no_long = []

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
    else:
        no_long.append(slug)
    
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
print(f'total={total}, long_content={has_long} ({has_long*100//max(total,1)}%), no_long={total-has_long}')
print(f'faq_html={has_faq}, faq_schema={has_faq_schema}, howto_schema={has_howto}, related={has_related}')
print(f'words: avg={avg_w:.0f}, min={min(word_counts, default=0)}, max={max(word_counts, default=0)}')
if short_content:
    print(f'thin_content (<300w): {len(short_content)}')
    for s, w in short_content[:5]:
        print(f'  {s}: {w}w')
if no_long:
    print(f'NO_LONG_CONTENT ({len(no_long)}): {no_long[:20]}')

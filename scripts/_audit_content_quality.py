"""Check EVERY long-form content file: topic match + language purity."""
import json, glob, os, re
from difflib import SequenceMatcher
from collections import defaultdict

CALC_DIR = "src/calculators"
CONTENT_DIR = "src/content"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

# Build calculator keyword sets per language
calc_info = {}
for fp in glob.glob(f"{CALC_DIR}/*.json"):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    cid = d['id']
    calc_info[cid] = {}
    for lang in LANGS:
        i18n = d.get('i18n', {}).get(lang, {})
        text = ' '.join([
            i18n.get('name', ''),
            i18n.get('description', '') or i18n.get('desc', ''),
            ' '.join(i18n.get('inputs', {}).values()),
            ' '.join(i18n.get('outputs', {}).values()),
        ]).lower()
        words = set(re.findall(r'[a-zäöüßéèêëàâîïôûùçñáéíóú]{4,}', text))
        calc_info[cid][lang] = words

# Spanish indicators for non-Spanish text detection
SP_WORDS = {'de','del','los','las','una','por','para','con','como','entre',
    'hasta','desde','muy','mucho','solo','y','o','se','le','lo','su','al',
    'más','menos','cada','otro','este','esta','también','volumen','largo',
    'ancho','altura','hormigón','cálculo','valor','metros','cúbicos',
    'cuadrados','sacos','arena','grava','calcular','resultado','fórmula',
    'mezcla','resistencia','necesario','cimentación','losa','desperdicio',
    'espesor','calculadora','multiplicar','sumar','restar','dividir',
    'superficial','materiales','gratuita','herramienta','pedir','medida',
    'típica','mínimo','máximo','confundir','considerar','usar',
    'cálculo','calculado','requiere','estándar','ejemplo','insuficiente',
    'derrames','nivelación','grietas','causar','puede'}

results = {
    'topic_match': 0,      # content matches calculator topic
    'topic_mismatch': 0,   # content is for a different calculator
    'topic_weak': 0,       # weak match
    'no_content': 0,       # no content file
    'spanish_mix': 0,      # Spanish words in non-Spanish content
    'broken_links': 0,     # links to non-existent pages
}

mismatch_examples = []
spanish_examples = []

# Build valid slug set for link checking
valid_slugs = set()
for d in calc_info.values():
    pass
for fp in glob.glob(f"{CALC_DIR}/*.json"):
    with open(fp, 'r', encoding='utf-8') as f:
        valid_slugs.add(json.load(f)['slug'])

for cid, cdata in sorted(calc_info.items(), key=lambda x: int(x[0])):
    for lang in ['en']:  # Focus on English first (most content files)
        content_path = f"{CONTENT_DIR}/{lang}/{cid}.html"
        if not os.path.exists(content_path):
            results['no_content'] += 1
            continue
        
        with open(content_path, 'r', encoding='utf-8-sig') as f:
            text = f.read(8000)
        
        # Strip HTML
        plain = re.sub(r'<[^>]+>', ' ', text).lower()
        content_words = set(re.findall(r'[a-z]{4,}', plain))
        
        # Check topic match
        target_words = calc_info[cid].get(lang, set())
        if target_words:
            overlap = len(content_words & target_words)
            ratio = overlap / len(target_words) if target_words else 0
            if ratio >= 0.15:
                results['topic_match'] += 1
            elif ratio >= 0.05:
                results['topic_weak'] += 1
                if len(mismatch_examples) < 5:
                    name = json.load(open(f"{CALC_DIR}/{next(f for f in os.listdir(CALC_DIR) if f.endswith('.json') and json.load(open(os.path.join(CALC_DIR,f),'r',encoding='utf-8')).get('id')==cid)}",'r',encoding='utf-8')).get('i18n',{}).get('en',{}).get('name','')
                    # Extract content title
                    h2m = re.search(r'<h2>(.*?)</h2>', text)
                    content_title = h2m.group(1) if h2m else '(no h2)'
                    mismatch_examples.append(f"  [{cid}] Calc: {name[:50]}\n       Content: {content_title[:80]}\n       Overlap: {overlap}/{len(target_words)} keywords ({ratio:.0%})")
            else:
                results['topic_mismatch'] += 1
                if len(mismatch_examples) < 10:
                    # Find calculator JSON
                    calc_name = ''
                    for fp2 in glob.glob(f"{CALC_DIR}/*.json"):
                        with open(fp2,'r',encoding='utf-8') as f2:
                            d2 = json.load(f2)
                        if d2['id'] == cid:
                            calc_name = d2.get('i18n',{}).get('en',{}).get('name','')
                            break
                    h2m = re.search(r'<h2>(.*?)</h2>', text)
                    content_title = h2m.group(1) if h2m else '(no h2)'
                    mismatch_examples.append(f"  [{cid}] Calc: {calc_name[:50]}\n       Content: {content_title[:80]}\n       Overlap: {overlap}/{len(target_words)} keywords ({ratio:.0%})")
        
        # Check for Spanish words in English content
        sp_found = content_words & SP_WORDS
        if len(sp_found) >= 5:
            results['spanish_mix'] += 1
            if len(spanish_examples) < 5:
                spanish_examples.append(f"  [{cid}] Spanish in EN content: {sorted(sp_found)[:8]}")

# Also check ALL languages for Spanish mix
for lang in ['en','fr','pt','de','it']:
    lang_spanish = 0
    for cid in calc_info:
        content_path = f"{CONTENT_DIR}/{lang}/{cid}.html"
        if not os.path.exists(content_path):
            continue
        with open(content_path, 'r', encoding='utf-8-sig') as f:
            text = f.read(5000)
        plain = re.sub(r'<[^>]+>', ' ', text).lower()
        content_words = set(re.findall(r'[a-záéíóúñüäöüßç]{4,}', plain))
        sp_found = content_words & SP_WORDS
        if len(sp_found) >= 5:
            lang_spanish += 1
    print(f"  {lang}: {lang_spanish} files with Spanish words mixed in")

print(f"\n=== ENGLISH CONTENT AUDIT ===")
print(f"  Topic matches:   {results['topic_match']}")
print(f"  Weak matches:    {results['topic_weak']}")
print(f"  TOPIC MISMATCH:  {results['topic_mismatch']}")
print(f"  No content file: {results['no_content']}")
print(f"  Spanish mixed:   {results['spanish_mix']}")

if mismatch_examples:
    print(f"\n=== TOPIC MISMATCH EXAMPLES ===")
    for ex in mismatch_examples[:10]:
        print(ex)

if spanish_examples:
    print(f"\n=== SPANISH IN CONTENT EXAMPLES ===")
    for ex in spanish_examples[:5]:
        print(ex)

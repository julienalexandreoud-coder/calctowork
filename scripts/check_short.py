import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs_i18n = data['calculators']
    
    short = [(cid, ci.get('seo_description', '') or ci.get('seo_desc', ''), len(ci.get('seo_description', '') or ci.get('seo_desc', ''))) 
             for cid, ci in calcs_i18n.items() if len(ci.get('seo_description', '') or ci.get('seo_desc', '')) < 120]
    
    if short:
        print(f"\n{lang}: {len(short)} still short")
        for cid, desc, l in short[:5]:
            print(f"  {cid}: ({l}c) {desc[:80]}...")
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

for lang in ['de', 'it', 'en', 'es', 'fr', 'pt']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    changed = 0
    
    for cid, ci in calcs.items():
        desc = ci.get('seo_description', '')
        if len(desc) > 155:
            # Truncate at last sentence/space before 155
            truncated = desc[:154]
            last_period = truncated.rfind('.')
            last_space = truncated.rfind(' ')
            cut_at = last_period if last_period > 100 else last_space
            if cut_at > 100:
                new_desc = desc[:cut_at + 1].strip()
            else:
                new_desc = truncated.rsplit(' ', 1)[0].strip()
            if len(new_desc) >= 120:
                ci['seo_description'] = new_desc
                changed += 1
            # If still over 155 (shouldn't happen), just hard truncate
            elif len(ci.get('seo_description', '')) > 155:
                ci['seo_description'] = desc[:155].rsplit(' ', 1)[0].strip()
                changed += 1
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    
    # Audit
    short = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) < 120)
    good = sum(1 for ci in calcs.values() if 120 <= len(ci.get('seo_description', '')) <= 155)
    long = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) > 155)
    print(f'  {lang}: truncated={changed}, <120c={short}, 120-155c={good}, >155c={long}')
from pathlib import Path
import json

d = Path(r'C:\Microsaas\obra\src\calculators')
files = [f for f in d.iterdir() if f.is_file() and not f.suffix]
print(f'Files without ext: {len(files)}')

if files:
    fp = files[0]
    print(f'First file: {fp.name}')
    data = json.load(open(fp, encoding='utf-8'))
    print(f'Keys: {list(data.keys())}')
    print(f'i18n: {list(data.get("i18n", {}).keys())}')
    
    i18n = data.get('i18n', {})
    for lang in ['en','fr','de','it','pt']:
        if lang in i18n:
            ld = i18n[lang]
            rh = ld.get('range_hints', {})
            print(f'\n{lang} range_hints: {type(rh).__name__}')
            if isinstance(rh, dict):
                for k, v in list(rh.items())[:3]:
                    print(f'  {k}: {repr(v)[:60]}')

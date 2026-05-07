import json
d = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))
blocks = d.get('blocks', {})
for k, v in sorted(blocks.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999):
    print(f'{k}: {v}')
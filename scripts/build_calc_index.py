"""
Generates public/data/calc-index.json from src/calculators/ and scripts/tools_config.py
One entry per calculator with id, slug, category, name per lang, status.
"""
import json, os, sys

# Add scripts dir to path so we can import tools_config
sys.path.insert(0, os.path.dirname(__file__))
from tools_config import TOOLS

SRC = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators')
OUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'calc-index.json')
LANGS = ['en', 'es', 'fr', 'de', 'it', 'pt']

# Build slug lookup from tools_config: { id -> { lang -> slug } }
slug_map = {}
for tool in TOOLS:
    tid = str(tool.get('id', '')).zfill(3) if str(tool.get('id', '')).isdigit() else str(tool.get('id', ''))
    slug_map[tid] = tool.get('slugs', {})

calcs = []
for calc_id in sorted(os.listdir(SRC)):
    calc_dir = os.path.join(SRC, calc_id)
    if not os.path.isdir(calc_dir):
        continue
    calc_json_path = os.path.join(calc_dir, 'calc.json')
    if not os.path.exists(calc_json_path):
        continue
    try:
        with open(calc_json_path, encoding='utf-8') as f:
            calc = json.load(f)
    except Exception:
        continue

    # Per-language slugs: prefer tools_config, fall back to lang.json, then calc.json slug
    tool_slugs = slug_map.get(calc_id, {})

    names = {}
    slugs = {}
    for lang in LANGS:
        lang_path = os.path.join(calc_dir, f'{lang}.json')
        if os.path.exists(lang_path):
            try:
                with open(lang_path, encoding='utf-8') as f:
                    ld = json.load(f)
                names[lang] = ld.get('name', '')
            except Exception:
                pass
        # Use tools_config slug first (most accurate), then fall back
        slugs[lang] = tool_slugs.get(lang) or calc.get('slug', '')

    entry = {
        'id': calc_id,
        'slug': calc.get('slug', ''),
        'category': calc.get('block_slug', calc.get('category', '')),
        'standard': calc.get('standard', ''),
        'names': names,
        'slugs': slugs,
        'inputs_count': len(calc.get('inputs', [])),
        'outputs_count': len(calc.get('outputs', [])),
    }
    calcs.append(entry)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(calcs, f, ensure_ascii=False, separators=(',', ':'))

print(f'Written {len(calcs)} calculators to {OUT}')

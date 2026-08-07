"""
Sync all 461 static calculators to Firestore calc_cms collection.
This lets the autonomous agent find and fix SEO issues on ALL calculators.
"""
import json, os
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CALC_DIR = BASE / "src" / "calculators"

# Load calc index for static calcs
index_path = BASE / "public" / "data" / "calc-index.json"
if not index_path.exists():
    # Build it first
    import subprocess
    subprocess.run(["py", str(BASE / "scripts" / "build_calc_index.py")], cwd=str(BASE))
    print("Built calc-index.json")

with open(index_path, 'r', encoding='utf-8') as f:
    calc_index = json.load(f)

print(f"Found {len(calc_index)} calculators in index")

# Build output JSON for Firestore import
output = {}

for calc in calc_index:
    cid = calc.get('id', '')
    slug = calc.get('slug', '')
    names = calc.get('names', {})
    slugs = calc.get('slugs', {})
    category = calc.get('category', '')
    standard = calc.get('standard', '')
    input_count = calc.get('inputs_count', 0)
    output_count = calc.get('outputs_count', 0)
    
    # Try to load per-language JSON files
    calc_dir = CALC_DIR / cid
    langs = {}
    
    if calc_dir.exists():
        for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
            lang_file = calc_dir / f"{lang}.json"
            if lang_file.exists():
                try:
                    with open(lang_file, 'r', encoding='utf-8') as f:
                        lang_data = json.load(f)
                    langs[lang] = {
                        'name': lang_data.get('name', names.get(lang, '')),
                        'desc': lang_data.get('description', ''),
                        'seo_title': lang_data.get('seo_title', ''),
                        'seo_description': lang_data.get('seo_description', ''),
                        'steps': lang_data.get('steps', []),
                        'mistakes': lang_data.get('mistakes', []),
                        'faq': lang_data.get('faq', []),
                    }
                except Exception as e:
                    print(f"  WARN: {cid}/{lang}.json: {e}")
    
    # Fallback: use names from calc-index if no JSON
    for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
        if lang not in langs:
            langs[lang] = {'name': names.get(lang, ''), 'desc': '', 'seo_title': '', 'seo_description': '', 'steps': [], 'mistakes': [], 'faq': []}
    
    output[slug] = {
        'slug': slug,
        'staticId': cid,
        'category': category,
        'standard': standard or '',
        'inputs_count': input_count,
        'outputs_count': output_count,
        'langs': langs,
        'status': 'published',
        'source': 'static_sync',
        'type': 'static',
    }
    
    if len(output) % 100 == 0:
        print(f"  Processed {len(output)} calculators...")

print(f"\nPrepared {len(output)} calculators for sync")

# Write to JSON file for manual import or use Firestore batch
out_file = BASE / "scripts" / "sync_data.json"
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Wrote sync data to {out_file}")
print(f"\nTo sync to Firestore, use:")
print(f"  firebase firestore:import --collection calc_cms scripts/sync_data.json --project calctowork")
print(f"\nOr import programmatically via Admin SDK.")

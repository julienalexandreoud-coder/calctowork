"""Fast sync: reads all source files, sends to Cloud Function in batches."""
import json, os, sys
from pathlib import Path
import urllib.request

BASE = Path(__file__).resolve().parent.parent
CALC_DIR = BASE / "src" / "calculators"

# Build calc index
import subprocess
subprocess.run(["py", str(BASE / "scripts" / "build_calc_index.py")], cwd=str(BASE), capture_output=True)

with open(BASE / "public" / "data" / "calc-index.json", 'r', encoding='utf-8') as f:
    calc_index = json.load(f)

print(f"Processing {len(calc_index)} calculators...")

batch = {}
count = 0

for calc in calc_index:
    cid = calc.get('id', '')
    slug = calc.get('slug', '')
    if not cid or not slug:
        continue
    
    names = calc.get('names', {})
    category = calc.get('category', '')
    standard = calc.get('standard', '')
    
    langs = {}
    calc_dir = CALC_DIR / cid
    
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
                        'example_label': lang_data.get('example_label', ''),
                        'result_context': lang_data.get('result_context', ''),
                        'long_content': lang_data.get('long_content', ''),
                        'range_hints': lang_data.get('range_hints', {}),
                    }
                except Exception as e:
                    print(f"  WARN: {cid}/{lang}.json: {e}")
    
    for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
        if lang not in langs:
            langs[lang] = {'name': names.get(lang, ''), 'desc': '', 'seo_title': '', 'seo_description': '', 'steps': [], 'mistakes': [], 'faq': [], 'long_content': ''}
    
    batch[slug] = {
        'slug': slug, 'staticId': cid, 'category': category, 'standard': standard or '',
        'langs': langs, 'status': 'published', 'source': 'deep_sync', 'type': 'static',
    }
    count += 1

    # Send batch every 50 calculators
    if len(batch) >= 50:
        data = json.dumps(batch).encode('utf-8')
        req = urllib.request.Request(
            'https://us-central1-calctowork.cloudfunctions.net/bulkSyncCalcsHttp',
            data=data,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        try:
            resp = urllib.request.urlopen(req, timeout=120)
            result = json.loads(resp.read())
            print(f"  Synced {count}/{len(calc_index)}: {result.get('synced',0)} saved")
        except Exception as e:
            print(f"  ERROR at {count}: {e}")
        batch = {}

# Send remaining
if batch:
    data = json.dumps(batch).encode('utf-8')
    req = urllib.request.Request(
        'https://us-central1-calctowork.cloudfunctions.net/bulkSyncCalcsHttp',
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        resp = urllib.request.urlopen(req, timeout=120)
        result = json.loads(resp.read())
        print(f"  Final: {result.get('synced',0)} saved")
    except Exception as e:
        print(f"  Final ERROR: {e}")

print(f"\nDone! Synced {count} calculators with full content to Firestore.")

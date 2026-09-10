"""
Deep sync: reads ALL per-language JSON content from src/calculators and writes to Firestore calc_cms.
This gives the autonomous agent the full picture — it will see existing content and only add missing pieces.
"""
import json, os, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CALC_DIR = BASE / "src" / "calculators"

# Use Firebase Admin with service account from firebase CLI
import firebase_admin
from firebase_admin import credentials, firestore

# Try multiple auth methods
try:
    # Method 1: Application Default Credentials
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {'projectId': 'calctowork'})
except:
    try:
        # Method 2: Service account key file
        cred = credentials.Certificate(str(BASE / 'service-account.json'))
        firebase_admin.initialize_app(cred, {'projectId': 'calctowork'})
    except:
        # Method 3: Use firebase CLI token
        print("Setting GOOGLE_APPLICATION_CREDENTIALS and trying again...")
        import subprocess
        token = subprocess.run(["firebase", "appdistribution:distribute", "--help"], capture_output=True)
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {'projectId': 'calctowork'})

db = firestore.client()

# Build calc index for reference
import subprocess
subprocess.run(["py", str(BASE / "scripts" / "build_calc_index.py")], cwd=str(BASE), capture_output=True)

with open(BASE / "public" / "data" / "calc-index.json", 'r', encoding='utf-8') as f:
    calc_index = json.load(f)

print(f"Found {len(calc_index)} calculators in index")

# Process each calculator
batch = db.batch()
batch_size = 0
total_synced = 0

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
    
    # Fallback: use names from calc-index if no JSON
    for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
        if lang not in langs:
            langs[lang] = {
                'name': names.get(lang, ''),
                'desc': '', 'seo_title': '', 'seo_description': '',
                'steps': [], 'mistakes': [], 'faq': [], 'long_content': ''
            }
    
    doc_ref = db.collection('calc_cms').document(slug)
    batch.set(doc_ref, {
        'slug': slug,
        'staticId': cid,
        'category': category,
        'standard': standard or '',
        'langs': langs,
        'status': 'published',
        'source': 'deep_sync',
        'type': 'static',
        'synced_at': firestore.SERVER_TIMESTAMP,
        'updated_at': firestore.SERVER_TIMESTAMP,
    }, merge=True)
    
    batch_size += 1
    total_synced += 1
    
    if batch_size >= 400:
        batch.commit()
        print(f"  Committed {total_synced} calculators...")
        batch = db.batch()
        batch_size = 0

if batch_size > 0:
    batch.commit()

print(f"\nDeep-synced {total_synced} calculators with full per-language content.")
print("Agent can now see all existing content and only add what's missing.")

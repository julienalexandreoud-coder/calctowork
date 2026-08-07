"""
Sync static calculator content to Firestore calc_cms collection.
This populates calc_cms so the autonomous agent can find and fix SEO issues.
"""
import json, os, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
CALC_DIR = BASE / "src" / "calculators"

# Build calc index if needed
import subprocess
subprocess.run(["py", str(BASE / "scripts" / "build_calc_index.py")], cwd=str(BASE), capture_output=True)

with open(BASE / "public" / "data" / "calc-index.json", 'r', encoding='utf-8') as f:
    calc_index = json.load(f)

print(f"Loading {len(calc_index)} calculators...")

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore

# Use application default credentials (works because we're authenticated via firebase CLI)
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {'projectId': 'calctowork'})
db = firestore.client()

batch = db.batch()
count = 0
batch_size = 0

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
                    }
                except Exception as e:
                    pass
    
    for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
        if lang not in langs:
            langs[lang] = {'name': names.get(lang, ''), 'desc': '', 'seo_title': '', 'seo_description': '', 'steps': [], 'mistakes': [], 'faq': []}
    
    doc_ref = db.collection('calc_cms').document(slug)
    batch.set(doc_ref, {
        'slug': slug,
        'staticId': cid,
        'category': category,
        'standard': standard or '',
        'langs': langs,
        'status': 'published',
        'source': 'static_sync',
        'type': 'static',
        'synced_at': firestore.SERVER_TIMESTAMP,
        'updated_at': firestore.SERVER_TIMESTAMP,
    }, merge=True)
    
    batch_size += 1
    count += 1
    
    if batch_size >= 400:
        batch.commit()
        print(f"  Committed {count} calculators...")
        batch = db.batch()
        batch_size = 0

if batch_size > 0:
    batch.commit()

print(f"\nSynced {count} calculators to calc_cms. Agent can now fix their SEO issues.")

"""Direct comparison: content h2 vs calculator name for all EN files."""
import json, re
from pathlib import Path

base = Path(r'C:\Microsaas\obra')
calcs_dir = base / 'src' / 'calculators'
en_content_dir = base / 'src' / 'content' / 'en'

# Load all calculator EN names
calc_names = {}
for calc_dir in sorted(calcs_dir.iterdir()):
    if not calc_dir.is_dir():
        continue
    cid = calc_dir.name
    en_json = calc_dir / 'en.json'
    if en_json.exists():
        with open(en_json, encoding='utf-8') as f:
            i18n = json.load(f)
        calc_names[cid] = i18n.get('name', '').lower()

# Also load from central en.json for comparison
import json as j
with open(base / 'src' / 'i18n' / 'en.json', encoding='utf-8') as f:
    central = j.load(f)
central_calcs = central.get('calculators', {})

print('Checking ALL EN content files...\n')
mismatches = []

for en_file in sorted(en_content_dir.glob('*.html')):
    cid = en_file.stem
    
    # Get calculator info
    calc_name = calc_names.get(cid, '').lower()
    central_name = central_calcs.get(cid, {}).get('name', '').lower()
    name = central_name or calc_name
    
    # Read content h2
    content = en_file.read_text(encoding='utf-8')
    h2 = re.search(r'<h2>(.*?)</h2>', content)
    h2_text = h2.group(1).lower() if h2 else ''
    
    h1 = re.search(r'<h1>(.*?)</h1>', content)
    h1_text = h1.group(1).lower() if h1 else ''
    
    heading = h1_text or h2_text
    
    if not heading or not name:
        continue
    
    # Skip very generic headings like "Common Mistakes", "How It Works" etc
    generic = ['common mistakes', 'pro tips', 'faqs', 'frequently asked', 'related', 'how it works', 'formula explained', 'formulas explained', 'step-by-step']
    if heading in generic:
        continue
    
    # Extract key topic words from heading
    # Remove "what is", "what is a", "the", "calculator" etc
    heading_clean = re.sub(r'^(what is a |what is the |what is an |what is |the |a |an )', '', heading)
    heading_clean = re.sub(r' calculator$', '', heading_clean).strip()
    
    # Extract key words from calculator name
    name_clean = re.sub(r' calculator$', '', name).strip()
    
    # Compare: do they share at least one significant word (>4 chars)?
    heading_words = set(w for w in heading_clean.split() if len(w) > 3)
    name_words = set(w for w in name_clean.split() if len(w) > 3)
    
    common = heading_words & name_words
    
    if not common and heading_words and name_words:
        # This is a potential mismatch
        mismatches.append((cid, name[:60], heading[:80], content[:200]))

print(f'Found {len(mismatches)} potential content mismatches:\n')
for cid, name, heading, snippet in sorted(mismatches, key=lambda x: int(x[0])):
    print(f'ID {cid}: calc="{name}"')
    print(f'  Heading: "{heading}"')
    print(f'  Content start: {re.sub(r"<[^>]+>", "", snippet)[:150]}')
    print()

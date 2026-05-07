"""Map finance block content to correct IDs."""
import json, glob, os

# Get finance calculator names (IDs 300-339)
finance = {}
for fp in glob.glob('src/calculators/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    cid = d['id']
    if 300 <= int(cid) <= 340:
        finance[cid] = d['i18n']['en']['name']

print("Finance calculators:")
for cid in sorted(finance.keys(), key=int):
    print(f"  {cid}: {finance[cid]}")

# Check what content each file has
import re
print("\nContent file -> content topic:")
for cid in sorted(finance.keys(), key=int):
    fp = f'src/content/en/{cid}.html'
    if not os.path.exists(fp):
        print(f"  {cid}: NO CONTENT FILE")
        continue
    with open(fp, 'r', encoding='utf-8-sig') as f:
        text = f.read(3000)
    h2m = re.search(r'<h2>(.*?)</h2>', text)
    topic = h2m.group(1) if h2m else '(no h2)'
    print(f"  {cid}: {topic[:80]}")

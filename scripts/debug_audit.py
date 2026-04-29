import json
from pathlib import Path

calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']
calc_by_id = {c['id']: c for c in calcs}

print("=== MISSING CONTENT FILES ===")
missing_ids = ['700', '800', '802', '900']
for cid in missing_ids:
    c = calc_by_id.get(cid)
    if c:
        print(f"ID {cid}: {c['slug']} (block: {c.get('block_slug', '')})")

print("\n=== THIN CONTENT IDS ===")
thin_ids = ['089', '212', '213', '214', '215', '216', '217', '702', '703', '704', '705', '706', '708', '709']
for cid in thin_ids:
    c = calc_by_id.get(cid)
    if c:
        print(f"ID {cid}: {c['slug']}")

# Check content quality for these
print("\n=== CHECKING CONTENT QUALITY ===")
for cid in thin_ids[:5]:
    for lang in ['de', 'pt']:
        cf = Path(f'src/content/{lang}/{cid}.html')
        if cf.exists():
            text = cf.read_text(encoding='utf-8')
            words = len(text.split())
            print(f"[{lang}/{cid}]: {words} words")
            break

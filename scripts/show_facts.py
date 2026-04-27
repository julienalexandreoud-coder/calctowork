import json
from calc_content import CALC_FACTS

# Map block IDs to category types
CATEGORY_MAP = {
    "1": "construction", "2": "construction", "3": "construction",
    "4": "construction", "5": "construction", "6": "construction",
    "7": "construction", "8": "construction", "9": "finance",
    "10": "math", "11": "finance", "12": "health",
    "13": "everyday", "14": "math", "15": "science",
    "16": "conversion", "17": "sports", "18": "math",
    "matematicas": "math", "ciencia": "science", "salud": "health",
    "finanzas": "finance", "quimica": "science", "electronica": "science",
    "transporte": "everyday", "ingenieria": "science", "clima": "science",
    "utilidades": "everyday", "deportes": "sports", "fotografia": "science",
}

# Load calculators to get block info
calcs = json.load(open('src/calculators/calculators.json', 'r', encoding='utf-8'))['calculators']
calc_by_id = {str(c['id']): c for c in calcs}

# Show sample CALC_FACTS per category
seen_cats = set()
for cid, facts in sorted(CALC_FACTS.items()):
    calc = calc_by_id.get(cid, {})
    block = str(calc.get('block', ''))
    cat = CATEGORY_MAP.get(block, 'other')
    if cat not in seen_cats:
        seen_cats.add(cat)
        en = facts.get('en', {})
        print(f"\n--- {cat} (id={cid}, block={block}) ---")
        print(f"  f: {en.get('f', '')}")
        print(f"  ei: {en.get('ei', '')}")
        print(f"  eo: {en.get('eo', '')}")
        print(f"  u: {en.get('u', [])}")

print(f"\nTotal CALC_FACTS entries: {len(CALC_FACTS)}")
print(f"Categories seen: {sorted(seen_cats)}")
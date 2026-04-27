import json

calcs = json.load(open('src/calculators/calculators.json', 'r', encoding='utf-8'))['calculators']
cats = {}
for c in calcs:
    b = c.get('block', 'unknown')
    if b not in cats:
        cats[b] = 0
    cats[b] += 1

print("Categories/blocks:")
for k, v in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v} calculators")

print(f"\nTotal calculators: {len(calcs)}")
print(f"\nSample calculator (first entry):")
print(json.dumps(calcs[0], indent=2, ensure_ascii=False)[:800])
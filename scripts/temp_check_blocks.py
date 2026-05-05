import json

with open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

target_ids = ['001','002','003','004','005','006','007','008','009','010','1101','1102','1104','1116','1119','415','425','144','1024','1029','1030','1039']
print("=== Target calculators ===")
for c in data['calculators']:
    if c['id'] in target_ids:
        print(f"{c['id']}: block={c.get('block')}, block_slug={c.get('block_slug'):15s} slug={c['slug']}")

print("\n=== ALL Block 1 (estructuras) calculators ===")
for c in data['calculators']:
    if c.get('block_slug') == 'estructuras':
        print(f"  {c['id']}: {c['slug']}")

print("\n=== Block 'salud' calculators ===")
for c in data['calculators']:
    if c.get('block_slug') == 'salud':
        print(f"  {c['id']}: {c['slug']}")

print("\n=== Block 'ciencia' calculators ===")
for c in data['calculators']:
    if c.get('block_slug') == 'ciencia':
        print(f"  {c['id']}: {c['slug']}")

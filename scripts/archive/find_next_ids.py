import json

d = json.load(open('c:/Microsaas/obra/src/calculators/calculators.json', encoding='utf-8'))
ids = [int(c['id']) for c in d['calculators']]
print(f"Total calculators: {len(d['calculators'])}")
print(f"Max ID: {max(ids)}")
print(f"Next available IDs: {max(ids)+1} to {max(ids)+20}")

# Find existing slugs to avoid duplicates
slugs = [c['slug'] for c in d['calculators']]
print(f"\nSample slugs: {slugs[:10]}")

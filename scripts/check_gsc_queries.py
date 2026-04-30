import csv

with open('c:/Microsaas/obra/gsc_data/Consultas.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f'Total rows: {len(rows)}')
print(f'Columns: {list(rows[0].keys()) if rows else "none"}')

# Map Spanish column names
query_col = 'Consultas principales'
imp_col = 'Impresiones'
pos_col = 'Posición'
ctr_col = 'CTR'
clicks_col = 'Clics'

# Search all rows for tile/bmr/cop
tile_queries = [r for r in rows if 'tile' in r.get(query_col,'').lower() or 'ceramic' in r.get(query_col,'').lower()]
bmr_queries = [r for r in rows if 'bmr' in r.get(query_col,'').lower() or 'metabolic' in r.get(query_col,'').lower() or 'basal' in r.get(query_col,'').lower()]
cop_queries = [r for r in rows if 'cop' in r.get(query_col,'').lower() or 'eer' in r.get(query_col,'').lower() or 'seer' in r.get(query_col,'').lower()]

print(f'\nTile queries: {len(tile_queries)}')
print(f'BMR queries: {len(bmr_queries)}')
print(f'COP/EER queries: {len(cop_queries)}')

if tile_queries:
    print('\n=== TOP TILE QUERIES ===')
    for q in sorted(tile_queries, key=lambda x: -int(x.get(imp_col,0) or 0))[:10]:
        print(f"  pos={q.get(pos_col,'?'):>6} imp={q.get(imp_col,'?'):>5} | {q.get(query_col,'')}")

if bmr_queries:
    print('\n=== TOP BMR QUERIES ===')
    for q in sorted(bmr_queries, key=lambda x: -int(x.get(imp_col,0) or 0))[:10]:
        print(f"  pos={q.get(pos_col,'?'):>6} imp={q.get(imp_col,'?'):>5} | {q.get(query_col,'')}")

if cop_queries:
    print('\n=== TOP COP/EER QUERIES ===')
    for q in sorted(cop_queries, key=lambda x: -int(x.get(imp_col,0) or 0))[:10]:
        print(f"  pos={q.get(pos_col,'?'):>6} imp={q.get(imp_col,'?'):>5} | {q.get(query_col,'')}")

# Show top 20 queries overall
print('\n=== TOP 20 QUERIES BY IMPRESSIONS ===')
for q in sorted(rows, key=lambda x: -int(x.get(imp_col,0) or 0))[:20]:
    print(f"  pos={q.get(pos_col,'?'):>6} imp={q.get(imp_col,'?'):>6} ctr={q.get(ctr_col,'?'):>6} | {q.get(query_col,'')}")

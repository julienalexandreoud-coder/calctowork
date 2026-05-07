import csv

with open('c:/Microsaas/obra/gsc_data/Consultas.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

query_col = 'Consultas principales'
imp_col = 'Impresiones'
pos_col = 'Posición'

# Spanish queries
print('=== TOP SPANISH QUERIES ===')
es_queries = [r for r in rows if any(c in r.get(query_col,'').lower() for c in 'áéíóúñ')]
for q in sorted(es_queries, key=lambda x: -int(x.get(imp_col,0) or 0))[:25]:
    print(f"  pos={q.get(pos_col,'?'):>6} imp={q.get(imp_col,'?'):>5} | {q.get(query_col,'')}")

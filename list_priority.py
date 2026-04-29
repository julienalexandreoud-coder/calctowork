import json

thin = json.load(open('audit_thin.json', encoding='utf-8'))

# Health calculators
salud = [c for c in thin if c['block'] == 'salud']
print("=== SALUD (Health) - 34 calculators ===")
for c in salud:
    print(f"ID {c['id']}: {c['name']} ({c['words']} words)")

# Math calculators  
matematicas = [c for c in thin if c['block'] == 'matematicas']
print(f"\n=== MATEMATICAS (Math) - {len(matematicas)} calculators ===")
for c in matematicas[:20]:
    print(f"ID {c['id']}: {c['name']} ({c['words']} words)")
print(f"... and {len(matematicas)-20} more")

# Finance calculators
finanzas = [c for c in thin if c['block'] == 'finanzas']
print(f"\n=== FINANZAS (Finance) - {len(finanzas)} calculators ===")
for c in finanzas[:20]:
    print(f"ID {c['id']}: {c['name']} ({c['words']} words)")
print(f"... and {len(finanzas)-20} more")

# Conversion calculators
conversion = [c for c in thin if c['block'] == 'conversion']
print(f"\n=== CONVERSION - {len(conversion)} calculators ===")
for c in conversion:
    print(f"ID {c['id']}: {c['name']} ({c['words']} words)")

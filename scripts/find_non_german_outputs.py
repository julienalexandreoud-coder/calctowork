"""Find actually non-German output labels (English/Spanish words in labels)."""
import json, glob, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))

# English/Spanish marker words that should NOT appear in German labels
non_german_markers = [
    'result', 'value', 'total', 'number', 'amount', 'calculate',
    'volume', 'area', 'weight', 'length', 'width', 'height', 'depth',
    'speed', 'distance', 'time', 'temperature', 'pressure', 'force',
    'energy', 'power', 'current', 'voltage', 'resistance',
    'years', 'months', 'days', 'hours', 'minutes', 'seconds',
    'category', 'score', 'count', 'sum', 'average', 'range',
    'resultado', 'valor', 'cantidad', 'número', 'calcular',
    'volumen', 'área', 'peso', 'longitud', 'altura', 'anchura',
    'tiempo', 'temperatura', 'presión', 'fuerza', 'energía',
    'años', 'meses', 'días', 'horas', 'minutos', 'segundos',
]

# But these are fine if embedded in a German compound word
german_ok_patterns = [
    'Ergebnis', 'Fläche', 'Gesamt', 'Volumen', 'Gewicht', 'Länge',
    'Breite', 'Höhe', 'Tiefe', 'Geschwindigkeit', 'Entfernung',
    'Zeit', 'Temperatur', 'Druck', 'Kraft', 'Energie', 'Leistung',
    'Strom', 'Spannung', 'Widerstand', 'Jahre', 'Monate', 'Tage',
    'Stunden', 'Minuten', 'Sekunden', 'Kategorie', 'Wert', 'Anzahl',
    'Summe', 'Durchschnitt', 'Spannweite', 'Kalorien', 'Kosten',
    'Preis', 'Menge', 'Gewinn', 'Verlust', 'Rabatt', 'Steuer',
    'Zinsen', 'Kapital', 'Schulden', 'Rate', 'Zahlung',
]

problems = {}

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    de = data.get('i18n', {}).get('de', {})
    if not de:
        continue
    outputs = de.get('outputs', {})
    for key, val in outputs.items():
        if not val or not isinstance(val, str):
            continue
        val_lower = val.lower()
        is_german = any(gp.lower() in val for gp in german_ok_patterns)
        has_non_german = any(ngm in val_lower for ngm in non_german_markers)
        if has_non_german and not is_german:
            es_val = data.get('i18n', {}).get('es', {}).get('outputs', {}).get(key, '')
            if val not in problems:
                problems[val] = {'count': 0, 'es': es_val, 'files': []}
            problems[val]['count'] += 1
            if len(problems[val]['files']) < 3:
                problems[val]['files'].append(os.path.basename(f))

print("Output labels with English/Spanish words that are not in a German word:")
print("=" * 60)
for label, info in sorted(problems.items(), key=lambda x: x[1]['count'], reverse=True):
    files_str = ', '.join(info['files'])
    print(f"  [{info['count']}x] '{label}' <- ES: '{info['es']}' ({files_str})")

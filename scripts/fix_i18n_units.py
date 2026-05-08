"""
Fix i18n files: de.json unit_labels/table_headers, currency symbols in all files.
"""
import json, sys
from pathlib import Path

I18N_DIR = Path(r'C:\Microsaas\obra\src\i18n')

# German unit_labels (properly localized)
DE_UNITS = {
    "m": "m", "m2": "m²", "m3": "m³", "m²": "m²", "m³": "m³",
    "kg": "kg", "cm": "cm", "mm": "mm", "km": "km",
    "L": "l", "l": "l", "mL": "ml", "ml": "ml",
    "g": "g", "mg": "mg",
    "kW": "kW", "W": "W", "kWh": "kWh", "kWh/year": "kWh/Jahr",
    "V": "V", "A": "A", "Hz": "Hz",
    "€": "€", "$": "$", "£": "£",
    "%": "%",
    "h": "h", "h/day": "h/Tag", "min": "min", "s": "s",
    "day": "Tag", "days": "Tage", "month": "Monat", "year": "Jahr",
    "°C": "°C", "°F": "°F", "K": "K",
    "kg/m3": "kg/m³", "kg/m²": "kg/m²",
    "kN": "kN", "N": "N", "J": "J", "kJ": "kJ",
    "bar": "bar", "Pa": "Pa", "hPa": "hPa",
    "m/s": "m/s", "km/h": "km/h", "mph": "mph",
    "cal": "kcal", "kcal": "kcal",
    "cm2": "cm²", "mm2": "mm²",
    "lt/min": "l/min",
    "m2/box": "m²/Packung", "m3/box": "m³/Packung",
    "ud": "Stk.", "uds": "Stk.",
    "sacos": "Säcke", "saco": "Sack",
    "personas": "Personen",
    "years": "Jahre", "months": "Monate",
    "m2/box": "m²/Packung",
    "W/m2": "W/m²",
}

# German table_headers
DE_TABLE = {
    "year": "Jahr",
    "interest": "Zinsen",
    "balance": "Guthaben",
    "period": "Zeitraum",
    "payment": "Zahlung",
    "principal": "Kapital",
    "total_paid": "Gesamt gezahlt",
    "total_interest": "Gesamtzinsen",
    "remaining": "Restbetrag",
    "month": "Monat",
    "monthly": "Monatlich",
    "annual": "Jährlich",
    "cumulative": "Kumuliert",
}

# Currency symbols for ALL languages
CURRENCIES = {
    "€": "€",
    "$": "$",
    "£": "£",
}

def fix_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)
    
    lang = filepath.stem  # 'en', 'es', etc.
    changed = False
    
    # Fix 1: Add missing currency symbols to unit_labels
    if 'unit_labels' not in data:
        data['unit_labels'] = {}
        changed = True
    
    for sym, val in CURRENCIES.items():
        if sym not in data['unit_labels']:
            data['unit_labels'][sym] = val
            changed = True
    
    # Fix 2: Add common measurement units if missing
    common_units = {
        'm2': 'm²', 'm3': 'm³',
        'kg/m3': 'kg/m³', 'kg/m2': 'kg/m²',
    }
    for k, v in common_units.items():
        if k not in data['unit_labels']:
            data['unit_labels'][k] = v
            changed = True
    
    # Fix 3: DE-specific fixes
    if lang == 'de':
        # Fix empty unit_labels
        if not data.get('unit_labels') or len(data['unit_labels']) < 10:
            data['unit_labels'] = DE_UNITS
            changed = True
        
        # Fix empty table_headers
        if 'table_headers' not in data or not data.get('table_headers'):
            data['table_headers'] = DE_TABLE
            changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f'Fixed {filepath.name}')
    else:
        print(f'{filepath.name}: no changes needed')

# Fix all 6 files
for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
    fix_file(I18N_DIR / f'{lang}.json')

print('\nDone!')

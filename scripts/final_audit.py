"""
Final audit: Verify German content quality across all layers.
"""
import json, glob, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
DE_CONTENT = r"C:\Microsaas\obra\src\content\de"
DE_JSON = r"C:\Microsaas\obra\src\i18n\de.json"

print("=" * 60)
print("FINAL GERMAN QUALITY AUDIT")
print("=" * 60)

# --- 1. Calculator JSONs ---
print("\n1. Calculator JSON files (i18n.de):")
files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))

# Check for remaining English/Spanish in outputs
en_outputs = 0
es_outputs = 0
garbled_names = 0
en_tags = 0

garbled_markers = ['calcudiet', 'calcudie', 'furterminar', 'furcolocar',
                   'absonne', 'bund ', 'repristints', 'inergia',
                   'mofurrada', 'diist ']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    de = data.get('i18n', {}).get('de', {})
    
    name = de.get('name', '')
    if ' (EN)' in name or ' (ES)' in name:
        en_tags += 1
    
    if any(m in name.lower() for m in garbled_markers):
        garbled_names += 1
    
    outputs = de.get('outputs', {})
    for val in outputs.values():
        if any(w in str(val).lower() for w in ['result', 'value', 'total', 'amount', 'calculate']):
            # Check if it's actually a German word containing these letters
            german_words = ['Ergebnis', 'Wert', 'Gesamt', 'Betrag', 'Berechnen',
                           'Volumen', 'Fläche', 'Gewicht', 'Länge', 'Breite',
                           'Höhe', 'Tiefe', 'Geschwindigkeit', 'Druck', 'Temperatur',
                           'Kalorien', 'Kosten', 'Preis', 'Summe', 'Menge',
                           'Zinsen', 'Kapital', 'Rate', 'Zahlung', 'Gewinn',
                           'Verlust', 'Rabatt', 'Steuer', 'Trinkgeld', 'Leistung',
                           'Strom', 'Spannung', 'Widerstand', 'Frequenz', 'Energie',
                           'Kraft', 'Masse', 'Dichte', 'Durchmesser', 'Radius',
                           'Umfang', 'Oberfläche', 'Grundfläche', 'Mantelfläche',
                           'Kategorie', 'Anzahl', 'Durchschnitt', 'Spannweite']
            if not any(gw.lower() in str(val) for gw in german_words):
                en_outputs += 1
                break

print(f"  Total: {len(files)}")
print(f"  Names with (EN)/(ES) tag: {en_tags}")
print(f"  Garbled names: {garbled_names}")
print(f"  Files with English output labels: {en_outputs}")

# --- 2. Content HTML ---
print("\n2. Content HTML files (src/content/de/):")
content_files = sorted(glob.glob(os.path.join(DE_CONTENT, "*.html")))
eng_phrase = 0
no_content = 0

for cf in content_files:
    with open(cf, 'r', encoding='utf-8') as f:
        content = f.read().lower()
    if not content.strip():
        no_content += 1
    if 'ensure all values' in content:
        eng_phrase += 1

# Check for known issues
spanish_in_content = 0
for cf in content_files:
    with open(cf, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'calcular ' in content.lower() or 'ingresar ' in content.lower():
        spanish_in_content += 1

print(f"  Total: {len(content_files)}")
print(f"  Empty files: {no_content}")
print(f"  English phrase remaining: {eng_phrase}")
print(f"  Spanish words remaining: {spanish_in_content}")

# --- 3. de.json ---
print("\n3. de.json:")
with open(DE_JSON, 'r', encoding='utf-8') as f:
    de_i18n = json.load(f)

# Check site-wide strings for non-German
non_de_strings = []
site_keys_to_check = ['site_description', 'site_title', 'home_title', 'home_description']

for key in site_keys_to_check:
    val = de_i18n.get(key, '')
    if val:
        # Simple check: if contains common English words not typical in German
        eng_words = ['free calculator', 'tools for', 'online tool']
        for ew in eng_words:
            if ew in val.lower():
                non_de_strings.append(f"  {key}: contains '{ew}'")

if non_de_strings:
    print("  Non-German site strings:")
    for s in non_de_strings:
        print(s)
else:
    print("  Site strings: OK")

# Check blocks for German
blocks = de_i18n.get('blocks', {})
non_de_blocks = []
eng_block_words = ['calculator', 'calculate', 'computation']
for name in blocks.values():
    for ew in eng_block_words:
        if ew in str(name).lower():
            non_de_blocks.append(f"  Block '{name}' contains '{ew}'")

if non_de_blocks:
    print("  Block names with English:")
    for s in non_de_blocks[:5]:
        print(s)
else:
    print("  Block names: OK")

# --- 4. Templates ---
print("\n4. Templates:")
import glob as g2
templates = sorted(g2.glob(r"C:\Microsaas\obra\src\templates\*.html.j2"))
skip_eng = 0
for tpl in templates:
    with open(tpl, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'Skip to content' in content:
        skip_eng += 1
print(f"  'Skip to content' remaining: {skip_eng}")

# --- 5. Build script ---
print("\n5. Build script (generate_calctowork.py):")
build = r"C:\Microsaas\obra\scripts\generate_calctowork.py"
with open(build, 'r', encoding='utf-8') as f:
    build_content = f.read()
issues = []
if 'kommerlle' in build_content:
    issues.append("'kommerlle' still present")
if 'wie besehen' in build_content:
    issues.append("'wie besehen' still present")
if not issues:
    print("  OK - typos fixed")
else:
    for i in issues:
        print(f"  {i}")

print("\n" + "=" * 60)
print("AUDIT COMPLETE")
print("=" * 60)

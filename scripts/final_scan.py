"""Final scan: find any remaining template files across all languages."""
from pathlib import Path
from bs4 import BeautifulSoup
d = Path(r'C:\Microsaas\obra\src\content')

# Template h2 markers per language
TEMPLATE_H2 = {
    'es': ['Cómo funciona el cálculo', 'Datos de entrada', 'Resultados'],
    'fr': ['Comment fonctionne le calcul', 'La formule', 'La formule financiere', 'Exemple de calcul'],
    'de': ['So funktioniert die Berechnung', 'Die Formel', 'Die finanzmathematische', 'Schritt-für-Schritt'],
    'it': ['Come funziona il calcolo', 'La formula', 'Esempio di calcolo'],
    'pt': ['Como funciona o cálculo', 'A formula', 'Exemplo de cálculo'],
}

for lang, markers in TEMPLATE_H2.items():
    ld = d / lang
    if not ld.exists(): continue
    template_files = []
    for f in ld.glob('*.html'):
        s = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
        h2 = s.find('h2')
        if h2:
            h2t = h2.get_text(strip=True)
            for m in markers:
                if m.lower() in h2t.lower():
                    template_files.append((f.name, h2t[:60]))
                    break
    
    if template_files:
        print(f'{lang}: {len(template_files)} template files remaining')
        for fn, h2t in template_files[:10]:
            print(f'  {fn}: "{h2t}"')
    else:
        print(f'{lang}: 0 template files remaining')

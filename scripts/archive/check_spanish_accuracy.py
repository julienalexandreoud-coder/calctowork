"""Quick check: how many Spanish detections have accented chars?"""
import json, re
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
I18N_EN = SRC / "i18n" / "en.json"

spanish_patterns = {
    ('example_label', False): re.compile(r'^(Calcular?|Dimensionar|Ejemplo|Introduc[ei]|Pulsa|Interpreta|Calcula\b|Obten|Resultados?:|El resultado|Este valor|La cifra|Los resultado|Medida t[ií]pica|Seg[úu]n)\b'),
    ('steps', True): re.compile(r'^(Introduce|Pulsa|Interpreta|Calcula\b|Identifica|Estima|Asigna|Determina|Mide|Coloca|Resta\b|Suma\b|Divide\b|Multiplica|Convierte|Proyecta|No considerar|Sobreestimar|Olvidar|Calcular ROI|Dimensionar|Calcular volumen|Calcular el|Aseg[uú]rate|Verifica|Comprueba|Recuerda|No olvides|Considera|Ten en cuenta|A[nñ]ade)\b'),
    ('mistakes', True): re.compile(r'^(No considerar|Sobreestimar|Olvidar|Comparar|No tener|Usar\b|Medir\b|Confundir|Calcular\b|Asumir|Utilizar|Redondear|Sumar\b|Restar\b|Ignorar|Pensar|Creer|Aplicar|Elegir|Escoger|Mezclar|Pisar|Pintar|Apretar|Cortar\b|Colocar|Verter|Encender|No utilizar|No medir|No comprobar|No verificar|No tener en cuenta)\b'),
    ('range_hints', False): re.compile(r'^(Valor entre|Valor|Medida t[ií]pica|Seg[úu]n|Entre)\b'),
    ('result_context', False): re.compile(r'^(Resultados?:|El resultado|Este valor|La cifra|Los resultado|Interpreta)\b'),
}

def has_accents(text):
    return bool(re.search(r'[áéíóúñÁÉÍÓÚÑ]', text))

with open(I18N_EN, 'r', encoding='utf-8') as f:
    en = json.load(f)

results = {}
for (field_name, is_list), _ in spanish_patterns.items():
    results[field_name] = {'with_accent': 0, 'without_accent': 0, 'total': 0}

for calc_id, calc in en['calculators'].items():
    for (field_name, is_list), pattern in spanish_patterns.items():
        value = calc.get(field_name)
        if not value:
            continue
        
        items = value if is_list else [value]
        for item in items:
            if not isinstance(item, str) or not item.strip():
                continue
            if pattern.search(item):
                accent = has_accents(item)
                results[field_name]['total'] += 1
                if accent:
                    results[field_name]['with_accent'] += 1
                else:
                    results[field_name]['without_accent'] += 1

for field_name, data in results.items():
    print(f"{field_name}: total={data['total']}, with_accents={data['with_accent']}, without={data['without_accent']}")

total_no_accent = sum(d['without_accent'] for d in results.values())
total_all = sum(d['total'] for d in results.values())
print(f"\nTotal flagged: {total_all}")
print(f"Without accents: {total_no_accent}")

if total_no_accent > 0:
    print("\nWARNING: Some detections lack Spanish accents - possible false positives!")
    # Show samples without accents
    for (field_name, is_list), pattern in spanish_patterns.items():
        if results[field_name]['without_accent'] > 0:
            print(f"\n  {field_name} samples without accents:")
            count = 0
            for calc_id, calc in en['calculators'].items():
                value = calc.get(field_name)
                if not value:
                    continue
                items = value if is_list else [value]
                for item in items:
                    if isinstance(item, str) and item.strip() and pattern.search(item) and not has_accents(item):
                        print(f"    [{calc_id}] {item[:70]}")
                        count += 1
                        if count >= 3:
                            break
                if count >= 3:
                    break
else:
    print("\nAll detections have Spanish accents - patterns are safe!")

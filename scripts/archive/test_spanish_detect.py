#!/usr/bin/env python3
"""Quick test of Spanish detection patterns"""
import re

spanish_patterns = {
    'step': r'^(Introduce|Pulsa|Interpreta|Calcula\b|Identifica|Estima|Asigna|Determina|Mide|Coloca|Resta|Suma|Divide|Multiplica|Convierte|Proyecta|No considerar|Sobreestimar|Olvidar|Calcular ROI|Dimensionar|Calcular volumen|Calcular el|Aseg[uú]rate|Verifica|Comprueba|Recuerda|No olvides|Considera|Ten en cuenta|A[nñ]ade)\b',
    'mistake': r'^(No considerar|Sobreestimar|Olvidar|Comparar|No tener|Usar\b|Medir|Confundir|Calcular|Asumir|Utilizar|Redondear|Sumar|Restar|Ignorar|Pensar|Creer|Aplicar|Elegir|Escoger|Mezclar|Pisar|Pintar|Apretar|Cortar|Colocar|Verter|Encender|No utilizar|No medir|No comprobar|No verificar|No tener en cuenta)\b',
    'example_label': r'^(Calcular?|Dimensionar|Ejemplo|Introduc[ei]|Pulsa|Interpreta|Calcula\b|Obten|Resultados?:|El resultado|Este valor|La cifra|Los resultado|Medida t[ií]pica|Seg[úu]n)\b',
    'range_hint': r'^(Valor entre|Valor|Medida t[ií]pica|Seg[úu]n|Entre)\b',
    'result_context': r'^(Resultados?:|El resultado|Este valor|La cifra|Los resultado|Interpreta)\b',
}

test_cases = [
    # (text, field_type, expected)
    ("Calculate the area of the circle.", "step", False),        # English
    ("Identifica la herramienta y su coste.", "step", True),      # Spanish
    ("Resta los valores dados.", "step", True),                   # Spanish
    ("Forgetting to add waste factor.", "mistake", False),        # English
    ("No considerar las pérdidas en obra.", "mistake", True),     # Spanish
    ("Usar unidades incorrectas.", "mistake", True),              # Spanish
    ("Using wrong units is a common error.", "mistake", False),   # English
    ("Calcular ROI de la herramienta.", "example_label", True),   # Spanish
    ("Calculate fence posts for 20m boundary.", "example_label", False), # English
    ("Ejemplo para decking calculator.", "example_label", True),  # Spanish
    ("Enter your measurements carefully.", "step", False),        # English
    ("Determine load before selecting wire gauge.", "step", False),# English
    ("Forgetting to account for thermal expansion.", "mistake", False), # English
    ("Using incorrect gauge wire for the amperage.", "mistake", False), # English
    ("Sample calculation with default values.", "example_label", False), # English
]

print("Testing Spanish detection patterns:")
print("=" * 70)
errors = 0
for text, field_type, expected in test_cases:
    pattern = spanish_patterns.get(field_type, "")
    result = bool(re.search(pattern, text))
    status = "OK" if result == expected else "FAIL"
    if status == "FAIL":
        errors += 1
    print(f"  [{status}] [{field_type:15}] '{text[:55]}...' => Spanish={result} (expected={expected})")

print(f"\nErrors: {errors}")
if errors > 0:
    print("FIX NEEDED!")
else:
    print("All patterns work correctly!")

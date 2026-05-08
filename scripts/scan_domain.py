"""Compare calculator inputs/outputs/domain with content topic."""
import json, re
from pathlib import Path

base = Path(r'C:\Microsaas\obra')
calcs_dir = base / 'src' / 'calculators'
en_content_dir = base / 'src' / 'content' / 'en'

# Map input field keywords to calculator domains
DOMAIN_KEYWORDS = {
    'construction': ['largo', 'ancho', 'altura', 'espesor', 'hormigon', 'cemento', 'arena', 'grava', 'ladrillo', 'bloque', 'acero', 'encofrado', 'muro', 'viga', 'losa', 'forjado', 'cimentacion', 'excavacion', 'solado', 'azulejo', 'mortero', 'pintura', 'revestimiento', 'aislamiento', 'cubierta', 'teja', 'madera', 'carpinteria', 'fontaneria', 'electricidad', 'climatizacion'],
    'finance': ['capital', 'interes', 'prestamo', 'hipoteca', 'cuota', 'ahorro', 'inversion', 'salario', 'sueldo', 'iva', 'impuesto', 'descuento', 'rentabilidad', 'dividendo', 'cagr', 'apr', 'annuity', 'wacc', 'sharpe', 'inflation', 'retirement', 'pension', 'tax', 'vat', 'revenue', 'profit', 'break-even'],
    'health': ['peso', 'altura', 'edad', 'imc', 'bmi', 'calorias', 'tdee', 'bmr', 'grasa', 'cintura', 'cadera', 'agua', 'hidratacion', 'sueno', 'corazon', 'frecuencia', 'proteinas', 'fibras', 'embarazo', 'crecimiento', 'percentil'],
    'math': ['porcentaje', 'fraccion', 'area', 'volumen', 'pitagoras', 'teorema', 'exponente', 'logaritmo', 'factorial', 'combinacion', 'permutacion', 'media', 'mediana', 'desviacion', 'probabilidad', 'ecuacion'],
    'conversion': ['convertir', 'unidad', 'longitud', 'temperatura', 'velocidad', 'presion', 'energia', 'almacenamiento'],
    'physics': ['velocidad', 'aceleracion', 'fuerza', 'masa', 'newton', 'energia', 'trabajo', 'densidad', 'presion', 'caida', 'libre', 'cinetica', 'potencial'],
    'sports': ['carrera', 'ritmo', 'calorias', 'ejercicio', 'pasos', 'nadar', 'ciclismo', 'vo2', 'frecuencia', 'cardiaca'],
}

mismatches = []

for en_file in sorted(en_content_dir.glob('*.html')):
    cid = en_file.stem
    calc_dir = calcs_dir / cid
    if not calc_dir.exists():
        continue
    
    calc_json = calc_dir / 'calc.json'
    if not calc_json.exists():
        continue
    
    with open(calc_json, encoding='utf-8') as f:
        cd = json.load(f)
    
    # Get inputs and formula
    inputs = [i.get('id', '') for i in cd.get('inputs', [])]
    formula = cd.get('formula', '')
    input_keywords = ' '.join(inputs).lower()
    
    # Detect domain from inputs
    detected_domain = None
    for domain, kws in DOMAIN_KEYWORDS.items():
        for kw in kws:
            if kw in input_keywords:
                detected_domain = domain
                break
        if detected_domain:
            break
    
    if not detected_domain:
        continue
    
    # Read content
    content = en_file.read_text(encoding='utf-8')
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text).strip().lower()
    
    # Check if content is about the same domain
    content_domain = None
    for domain, kws in DOMAIN_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                content_domain = domain
                break
        if content_domain:
            break
    
    if content_domain and content_domain != detected_domain:
        mismatches.append((cid, detected_domain, content_domain, text[:150]))

print(f'Found {len(mismatches)} domain mismatches:\n')
for cid, calc_domain, content_domain, snippet in sorted(mismatches, key=lambda x: int(x[0])):
    print(f'ID {cid}: calc={calc_domain}, content={content_domain}')
    print(f'  Content: {snippet}')
    print()

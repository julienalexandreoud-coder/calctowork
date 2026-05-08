"""Find ES content with COMPLETELY WRONG calculator (cross-domain mismatch)."""
import json, re
from pathlib import Path

d = Path(r'C:\Microsaas\obra\src\calculators')

# Map calculator domains to their content keywords
DOMAINS = {
    'construction': ['hormigón','cemento','ladrillo','bloque','muro','viga','losa','forjado','cimentación','excavación','solado','azulejo','mortero','pintura','aislamiento','cubierta','tarima','deck','valla','moqueta','mantillo','encimera','salpicadero','moldura','rodapié','pladur','yeso','grava','escalón','tarima','parquet','laminado','carpintería','fontanería','electricidad','climatización'],
    'finance': ['hipoteca','préstamo','interés','ahorro','inversión','salario','sueldo','iva','impuesto','descuento','rentabilidad','dividendo','cagr','apr','annuity','wacc','sharpe','inflación','jubilación','pensión','capital','ganancia','comisión','divisa','presupuesto','amortización','seguro','margen','beneficio','equilibrio'],
    'health_fitness': ['imc','bmi','caloría','tdee','tmb','bmr','grasa corporal','cintura','cadera','agua','hidratación','sueño','corazón','frecuencia cardíaca','proteína','fibra','embarazo','ovulación','crecimiento','percentil','peso ideal','ritmo carrera','pace','vo2','ejercicio','met'],
    'math': ['porcentaje','fracción','área','volumen','pitágoras','teorema','exponente','logaritmo','factorial','combinación','permutación','media','mediana','desviación','probabilidad','ecuación','triángulo','círculo'],
    'conversion': ['convertir','unidad','longitud','temperatura','velocidad','presión','energía'],
    'physics': ['velocidad','aceleración','fuerza','masa','newton','energía','trabajo','densidad','presión','caída','cinética','potencial','onda','lente','torque','momento','fluido'],
    'stats': ['media','mediana','desviación','varianza','probabilidad','combinación','permutación','confianza','coeficiente','regresión','correlación'],
}

def detect_domain(text):
    text_lower = text.lower()
    scores = {}
    for domain, keywords in DOMAINS.items():
        score = sum(1 for kw in keywords if kw in text_lower)
        if score > 0:
            scores[domain] = score
    return max(scores, key=scores.get) if scores else None

wrong = []

for cdir in sorted(d.iterdir(), key=lambda x: int(x.name) if x.name.isdigit() else 9999):
    if not cdir.is_dir(): continue
    es_html = cdir / 'es.html'
    es_json = cdir / 'es.json'
    if not es_html.exists() or not es_json.exists(): continue
    
    with open(es_json, encoding='utf-8') as f:
        calc_name = json.load(f).get('name','')
    
    content = es_html.read_text(encoding='utf-8')
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text).strip()[:500]
    
    calc_domain = detect_domain(calc_name)
    content_domain = detect_domain(text)
    
    if calc_domain and content_domain and calc_domain != content_domain:
        h2 = re.search(r'<h2>(.*?)</h2>', content)
        h2t = h2.group(1) if h2 else 'N/A'
        wrong.append((cdir.name, calc_name[:60], calc_domain, content_domain, h2t[:80]))

print(f'WRONG DOMAIN ({len(wrong)} files):')
print('='*80)
for cid, cname, cd, cod, h2t in sorted(wrong, key=lambda x: int(x[0]) if x[0].isdigit() else 9999):
    print(f'ID {cid}: calc="{cname}" ({cd})')
    print(f'  Content is about: {cod}')
    print(f'  h2: {h2t}')
    print()

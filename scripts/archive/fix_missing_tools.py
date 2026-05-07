# -*- coding: utf-8 -*-
"""Generate TOOLS entries for missing calculators and insert them into tools_config.py."""
import json
import re

with open('src/calculators/calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load all i18n files to get translated slugs where available
langs = ['es', 'en', 'fr', 'pt', 'de', 'it']
i18n = {}
for lang in langs:
    with open(f'src/i18n/{lang}.json', 'r', encoding='utf-8') as f:
        i18n[lang] = json.load(f)

# CAT mapping by block
BLOCK_CAT = {
    'matematicas': 'A',
    'finanzas': 'C',
    'salud': 'B',
    'cotidiano': 'D',
    'estadistica': 'A',
    'ciencia': 'E',
    'conversion': 'A',
    'deportes': 'B',
}

# Slug translation helpers (fallback rules)
def translate_slug(base_slug, lang):
    """Create a language-appropriate slug from the Spanish base."""
    # Use simple prefix/suffix replacements
    replacements = {
        'en': {
            'calculadora-': '',
            'convertidor-': '',
            'area-': 'area-',
            'volumen-': 'volume-',
            'potencias': 'power-calculator',
            'raiz': 'square-root',
            'logaritmo': 'logarithm',
            'factorial': 'factorial',
            'ecuacion-segundo-grado': 'quadratic-equation',
            'mcm-mcd': 'lcm-gcd',
            'roi': 'roi',
            'ahorro-compuesto': 'compound-savings',
            'inflacion': 'inflation',
            'subida-salarial': 'salary-raise',
            'plan-jubilacion': 'retirement-plan',
            'regla-72': 'rule-of-72',
            'deposito-plazo': 'fixed-deposit',
            'retorno-acciones': 'stock-return',
            'ratio-deuda': 'debt-ratio',
            'punto-equilibrio-unidades': 'break-even-units',
            'metabolismo-basal': 'bmr',
            'frecuencia-cardiaca-max-salud': 'max-heart-rate',
            'horas-sueno': 'sleep-hours',
            'porcentaje-grasa': 'body-fat-percentage',
            'rango-peso-saludable': 'healthy-weight-range',
            'media': 'mean',
            'mediana': 'median',
            'desviacion-estandar': 'standard-deviation',
            'probabilidad': 'probability',
            'combinaciones': 'combinations',
            'permutaciones': 'permutations',
            'intervalo-confianza': 'confidence-interval',
            'coeficiente-variacion': 'coefficient-variation',
            'varianza': 'variance',
            'puntuacion-z': 'z-score',
            'velocidad': 'speed',
            'densidad': 'density',
            'fuerza': 'force',
            'energia-cinetica': 'kinetic-energy',
            'energia-potencial': 'potential-energy',
            'presion': 'pressure',
            'trabajo-mecanico': 'mechanical-work',
            'ley-ohm': 'ohms-law',
            'potencia-electrica': 'electric-power',
            'aceleracion': 'acceleration',
            'longitud': 'length',
            'peso': 'weight',
            'temperatura': 'temperature',
            'volumen': 'volume',
            'area': 'area',
            'velocidad-unidades': 'speed-units',
            'datos-digitales': 'digital-data',
            'presion-unidades': 'pressure-units',
            'tiempo-unidades': 'time-units',
            'energia-unidades': 'energy-units',
            'ritmo-carrera': 'running-pace',
            'calorias-ejercicio': 'exercise-calories',
            'frecuencia-cardiaca-max': 'max-heart-rate',
            'zonas-cardiacas': 'heart-rate-zones',
            'vo2-max': 'vo2-max',
            'pasos-calorias': 'steps-calories',
            'ritmo-natacion': 'swimming-pace',
            'ritmo-ciclismo': 'cycling-pace',
            'imc-deportista': 'athlete-bmi',
            'tiempo-pista': 'track-time',
        },
        'fr': {
            'calculadora-': '',
            'convertidor-': '',
            'area-': 'aire-',
            'volumen-': 'volume-',
            'potencias': 'puissance',
            'raiz': 'racine-carree',
            'logaritmo': 'logarithme',
            'factorial': 'factorielle',
            'ecuacion-segundo-grado': 'equation-second-degre',
            'mcm-mcd': 'ppcm-pgcd',
            'roi': 'roi',
            'ahorro-compuesto': 'epargne-composee',
            'inflacion': 'inflation',
            'subida-salarial': 'augmentation-salaire',
            'plan-jubilacion': 'plan-retraite',
            'regla-72': 'regle-72',
            'deposito-plazo': 'depot-a-terme',
            'retorno-acciones': 'rendement-actions',
            'ratio-deuda': 'ratio-dette',
            'punto-equilibrio-unidades': 'seuil-rentabilite-unites',
            'metabolismo-basal': 'metabolisme-basal',
            'frecuencia-cardiaca-max-salud': 'fcmax-sante',
            'horas-sueno': 'heures-sommeil',
            'porcentaje-grasa': 'pourcentage-graisse',
            'rango-peso-saludable': 'plage-poids-sante',
            'media': 'moyenne',
            'mediana': 'mediane',
            'desviacion-estandar': 'ecart-type',
            'probabilidad': 'probabilite',
            'combinaciones': 'combinaisons',
            'permutaciones': 'permutations',
            'intervalo-confianza': 'intervalle-confiance',
            'coeficiente-variacion': 'coefficient-variation',
            'varianza': 'variance',
            'puntuacion-z': 'score-z',
            'velocidad': 'vitesse',
            'densidad': 'densite',
            'fuerza': 'force',
            'energia-cinetica': 'energie-cinetique',
            'energia-potencial': 'energie-potentielle',
            'presion': 'pression',
            'trabajo-mecanico': 'travail-mecanique',
            'ley-ohm': 'loi-ohm',
            'potencia-electrica': 'puissance-electrique',
            'aceleracion': 'acceleration',
            'longitud': 'longueur',
            'peso': 'poids',
            'temperatura': 'temperature',
            'volumen': 'volume',
            'area': 'aire',
            'velocidad-unidades': 'vitesse-unites',
            'datos-digitales': 'donnees-numeriques',
            'presion-unidades': 'pression-unites',
            'tiempo-unidades': 'temps-unites',
            'energia-unidades': 'energie-unites',
            'ritmo-carrera': 'allure-course',
            'calorias-ejercicio': 'calories-exercice',
            'frecuencia-cardiaca-max': 'fcmax',
            'zonas-cardiacas': 'zones-cardiaques',
            'vo2-max': 'vo2max',
            'pasos-calorias': 'pas-calories',
            'ritmo-natacion': 'allure-natation',
            'ritmo-ciclismo': 'allure-cyclisme',
            'imc-deportista': 'imc-athlete',
            'tiempo-pista': 'temps-piste',
        },
        'pt': {
            'calculadora-': '',
            'convertidor-': '',
            'area-': 'area-',
            'volumen-': 'volume-',
            'potencias': 'potencias',
            'raiz': 'raiz-quadrada',
            'logaritmo': 'logaritmo',
            'factorial': 'fatorial',
            'ecuacion-segundo-grado': 'equacao-segundo-grau',
            'mcm-mcd': 'mmc-mdc',
            'roi': 'roi',
            'ahorro-compuesto': 'poupanca-composta',
            'inflacion': 'inflacao',
            'subida-salarial': 'aumento-salarial',
            'plan-jubilacion': 'plano-aposentadoria',
            'regla-72': 'regra-72',
            'deposito-plazo': 'deposito-prazo',
            'retorno-acciones': 'retorno-acoes',
            'ratio-deuda': 'ratio-divida',
            'punto-equilibrio-unidades': 'ponto-equilibrio-unidades',
            'metabolismo-basal': 'metabolismo-basal',
            'frecuencia-cardiaca-max-salud': 'fcmax-saude',
            'horas-sueno': 'horas-sono',
            'porcentaje-grasa': 'percentual-gordura',
            'rango-peso-saludable': 'faixa-peso-saudavel',
            'media': 'media',
            'mediana': 'mediana',
            'desviacion-estandar': 'desvio-padrao',
            'probabilidad': 'probabilidade',
            'combinaciones': 'combinacoes',
            'permutaciones': 'permutacoes',
            'intervalo-confianza': 'intervalo-confianca',
            'coeficiente-variacion': 'coeficiente-variacao',
            'varianza': 'variancia',
            'puntuacion-z': 'pontuacao-z',
            'velocidad': 'velocidade',
            'densidad': 'densidade',
            'fuerza': 'forca',
            'energia-cinetica': 'energia-cinetica',
            'energia-potencial': 'energia-potencial',
            'presion': 'pressao',
            'trabajo-mecanico': 'trabalho-mecanico',
            'ley-ohm': 'lei-ohm',
            'potencia-electrica': 'potencia-eletrica',
            'aceleracion': 'aceleracao',
            'longitud': 'comprimento',
            'peso': 'peso',
            'temperatura': 'temperatura',
            'volumen': 'volume',
            'area': 'area',
            'velocidad-unidades': 'velocidade-unidades',
            'datos-digitales': 'dados-digitais',
            'presion-unidades': 'pressao-unidades',
            'tiempo-unidades': 'tempo-unidades',
            'energia-unidades': 'energia-unidades',
            'ritmo-carrera': 'ritmo-corrida',
            'calorias-ejercicio': 'calorias-exercicio',
            'frecuencia-cardiaca-max': 'fcmax',
            'zonas-cardiacas': 'zonas-cardiacas',
            'vo2-max': 'vo2max',
            'pasos-calorias': 'passos-calorias',
            'ritmo-natacion': 'ritmo-natacao',
            'ritmo-ciclismo': 'ritmo-ciclismo',
            'imc-deportista': 'imc-atleta',
            'tiempo-pista': 'tempo-pista',
        },
        'de': {
            'calculadora-': '',
            'convertidor-': '',
            'area-': 'flache-',
            'volumen-': 'volumen-',
            'potencias': 'potenzen',
            'raiz': 'quadratwurzel',
            'logaritmo': 'logarithmus',
            'factorial': 'fakultat',
            'ecuacion-segundo-grado': 'quadratische-gleichung',
            'mcm-mcd': 'kgv-ggt',
            'roi': 'roi',
            'ahorro-compuesto': 'zinseszins-sparen',
            'inflacion': 'inflation',
            'subida-salarial': 'gehaltserhohung',
            'plan-jubilacion': 'rentenplan',
            'regla-72': 'regel-72',
            'deposito-plazo': 'festgeld',
            'retorno-acciones': 'aktienrendite',
            'ratio-deuda': 'schuldenquote',
            'punto-equilibrio-unidades': 'gewinnschwelle-einheiten',
            'metabolismo-basal': 'grundumsatz',
            'frecuencia-cardiaca-max-salud': 'maximale-herzfrequenz',
            'horas-sueno': 'schlafstunden',
            'porcentaje-grasa': 'korperfettanteil',
            'rango-peso-saludable': 'gesundes-gewicht',
            'media': 'mittelwert',
            'mediana': 'median',
            'desviacion-estandar': 'standardabweichung',
            'probabilidad': 'wahrscheinlichkeit',
            'combinaciones': 'kombinationen',
            'permutaciones': 'permutationen',
            'intervalo-confianza': 'konfidenzintervall',
            'coeficiente-variacion': 'variationskoeffizient',
            'varianza': 'varianz',
            'puntuacion-z': 'z-wert',
            'velocidad': 'geschwindigkeit',
            'densidad': 'dichte',
            'fuerza': 'kraft',
            'energia-cinetica': 'kinetische-energie',
            'energia-potencial': 'potentielle-energie',
            'presion': 'druck',
            'trabajo-mecanico': 'mechanische-arbeit',
            'ley-ohm': 'ohmsches-gesetz',
            'potencia-electrica': 'elektrische-leistung',
            'aceleracion': 'beschleunigung',
            'longitud': 'lange',
            'peso': 'gewicht',
            'temperatura': 'temperatur',
            'volumen': 'volumen',
            'area': 'flache',
            'velocidad-unidades': 'geschwindigkeit-einheiten',
            'datos-digitales': 'digitale-daten',
            'presion-unidades': 'druck-einheiten',
            'tiempo-unidades': 'zeit-einheiten',
            'energia-unidades': 'energie-einheiten',
            'ritmo-carrera': 'lauftempo',
            'calorias-ejercicio': 'ubungskalorien',
            'frecuencia-cardiaca-max': 'maximale-herzfrequenz',
            'zonas-cardiacas': 'herzfrequenzzonen',
            'vo2-max': 'vo2max',
            'pasos-calorias': 'schritte-kalorien',
            'ritmo-natacion': 'schwimmtempo',
            'ritmo-ciclismo': 'fahrradtempo',
            'imc-deportista': 'sportler-bmi',
            'tiempo-pista': 'bahnzeit',
        },
        'it': {
            'calculadora-': '',
            'convertidor-': '',
            'area-': 'area-',
            'volumen-': 'volume-',
            'potencias': 'potenze',
            'raiz': 'radice-quadrata',
            'logaritmo': 'logaritmo',
            'factorial': 'fattoriale',
            'ecuacion-segundo-grado': 'equazione-secondo-grado',
            'mcm-mcd': 'mcm-mcd',
            'roi': 'roi',
            'ahorro-compuesto': 'risparmio-composto',
            'inflacion': 'inflazione',
            'subida-salarial': 'aumento-stipendio',
            'plan-jubilacion': 'piano-pensione',
            'regla-72': 'regola-72',
            'deposito-plazo': 'deposito-vincolato',
            'retorno-acciones': 'rendimento-azioni',
            'ratio-deuda': 'rapporto-debito',
            'punto-equilibrio-unidades': 'punto-pareggio-unita',
            'metabolismo-basal': 'metabolismo-basale',
            'frecuencia-cardiaca-max-salud': 'fcmax-salute',
            'horas-sueno': 'ore-sonno',
            'porcentaje-grasa': 'percentuale-grasso',
            'rango-peso-saludable': 'intervallo-peso-salubre',
            'media': 'media',
            'mediana': 'mediana',
            'desviacion-estandar': 'deviazione-standard',
            'probabilidad': 'probabilita',
            'combinaciones': 'combinazioni',
            'permutaciones': 'permutazioni',
            'intervalo-confianza': 'intervallo-confidenza',
            'coeficiente-variacion': 'coefficiente-variazione',
            'varianza': 'varianza',
            'puntuacion-z': 'punteggio-z',
            'velocidad': 'velocita',
            'densidad': 'densita',
            'fuerza': 'forza',
            'energia-cinetica': 'energia-cinetica',
            'energia-potencial': 'energia-potenziale',
            'presion': 'pressione',
            'trabajo-mecanico': 'lavoro-meccanico',
            'ley-ohm': 'legge-ohm',
            'potencia-electrica': 'potenza-elettrica',
            'aceleracion': 'accelerazione',
            'longitud': 'lunghezza',
            'peso': 'peso',
            'temperatura': 'temperatura',
            'volumen': 'volume',
            'area': 'area',
            'velocidad-unidades': 'velocita-unita',
            'datos-digitales': 'dati-digitali',
            'presion-unidades': 'pressione-unita',
            'tiempo-unidades': 'tempo-unita',
            'energia-unidades': 'energia-unita',
            'ritmo-carrera': 'ritmo-corsa',
            'calorias-ejercicio': 'calorie-esercizio',
            'frecuencia-cardiaca-max': 'fcmax',
            'zonas-cardiacas': 'zone-cardiache',
            'vo2-max': 'vo2max',
            'pasos-calorias': 'passi-calorie',
            'ritmo-natacion': 'ritmo-nuoto',
            'ritmo-ciclismo': 'ritmo-ciclismo',
            'imc-deportista': 'bmi-atleta',
            'tiempo-pista': 'tempo-pista',
        },
    }

    if lang == 'es':
        return base_slug

    mapping = replacements.get(lang, {})
    if base_slug in mapping:
        return mapping[base_slug]

    # Try to strip prefix and append calculator type
    if base_slug.startswith('calculadora-'):
        suffix = base_slug[len('calculadora-'):]
        if suffix in mapping:
            return mapping[suffix]
        return f'{suffix}-calculator'
    if base_slug.startswith('convertidor-'):
        suffix = base_slug[len('convertidor-'):]
        if suffix in mapping:
            return mapping[suffix]
        return f'{suffix}-converter'

    return base_slug


missing_ranges = list(range(210,220)) + list(range(310,320)) + list(range(410,415)) + list(range(600,610)) + list(range(700,710)) + list(range(800,810)) + list(range(900,910))
missing_ids = [f'{i:03d}' for i in missing_ranges]

entries = []
for calc in data['calculators']:
    if calc['id'] in missing_ids:
        cid = calc['id']
        block = calc['block_slug']
        base_slug = calc['slug']
        cat = BLOCK_CAT.get(block, 'E')

        slugs = {}
        for lang in langs:
            slugs[lang] = translate_slug(base_slug, lang)

        entry = {
            "id": cid,
            "cat": cat,
            "block": block,
            "slugs": slugs,
        }
        entries.append(entry)

# Generate Python code lines
lines = ["\n    # ── PHASE 2 MISSING CALCULATORS ───────────────────────────────────────"]
for e in entries:
    slug_parts = []
    for lang in langs:
        slug_parts.append(f'"{lang}": "{e["slugs"][lang]}"')
    slugs_str = ", ".join(slug_parts)
    lines.append(f'    {{"id": "{e["id"]}", "cat": "{e["cat"]}", "block": "{e["block"]}", "slugs": {{{slugs_str}}}}},')

# Read current tools_config.py
with open('scripts/tools_config.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the closing ] of TOOLS list (before TOOL_BY_ID)
insert_marker = "\n]\n\n# Quick lookup\nTOOL_BY_ID"
if insert_marker not in content:
    print("ERROR: Could not find insertion marker")
    exit(1)

new_content = content.replace(
    insert_marker,
    "\n".join(lines) + insert_marker
)

with open('scripts/tools_config.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Added {len(entries)} TOOLS entries.")

"""
Fix Spanish text in calc JSON i18n fields. Safe approach: parse JSON, only modify known text fields.
"""
import json
from pathlib import Path

CALCS_DIR = Path(r'C:\Microsaas\obra\src\calculators')

REPLACE = {
    'en': [
        (' del ', ' of the '), (' de ', ' of '), (' para ', ' for '), (' por ', ' per '),
        (' con ', ' with '), (' entre ', ' between '), (' según ', ' according to '),
        (' sin ', ' without '), (' sobre ', ' about '), (' desde ', ' from '),
        (' hasta ', ' to '), (' y ', ' and '), (' o ', ' or '),
        (' cada ', ' each '), (' donde ', ' where '),
        (' resultado ', ' result '), (' resultados ', ' results '),
        (' valor ', ' value '), (' valores ', ' values '),
        (' fórmula ', ' formula '), (' formula ', ' formula '),
        (' típico ', ' typical '), (' típica ', ' typical '),
        (' común ', ' common '), (' comunes ', ' common '),
        (' cantidad ', ' quantity '), (' número ', ' number '),
        (' unidad ', ' unit '), (' unidades ', ' units '),
        (' total ', ' total '), (' promedio ', ' average '),
        (' masa ', ' mass '), (' peso ', ' weight '),
        (' altura ', ' height '), (' longitud ', ' length '),
        (' ancho ', ' width '), (' profundidad ', ' depth '),
        (' espesor ', ' thickness '), (' diámetro ', ' diameter '),
        (' radio ', ' radius '), (' superficie ', ' area '),
        (' volumen ', ' volume '), (' densidad ', ' density '),
        (' potencia ', ' power '), (' energía ', ' energy '),
        (' velocidad ', ' speed '), (' tiempo ', ' time '),
        (' saludable ', ' healthy '),
        (' indica ', ' indicates '), (' categoría ', ' category '),
        (' como ', ' as '), (' se ', ' is '),
        (' más ', ' more '), (' menos ', ' less '),
        (' durante ', ' during '), (' siempre ', ' always '),
        (' debe ', ' must '),
        ('ingresados', 'entered'), ('tepical', 'typical'),
        ('paemint', 'payment'), ('recommindid', 'recommended'),
        ('currint', 'current'), ('eears', 'years'),
        ('origen', 'source'), ('sistema', 'system'),
        ('paramento a aislar', 'wall to insulate'),
        ('planchas de isolation', 'insulation boards'),
        ('Ejemplo', 'Example'), ('ejemplo', 'example'),
        ('Pasos', 'Steps'), ('pasos', 'steps'),
        ('Paso', 'Step'), ('paso', 'step'),
        ('Calcula', 'Calculate'), ('Introduce', 'Enter'),
        ('Selecciona', 'Select'), ('selecciona', 'select'),
        ('Ajusta', 'Adjust'),
        ('fachadas', 'facades'), ('cubiertas', 'roofs'),
        ('Aislamiento', 'Insulation'), ('aislamiento', 'insulation'),
    ],
    'fr': [
        (' del ', ' du '), (' y ', ' et '), (' para ', ' pour '), (' por ', ' par '),
        (' con ', ' avec '), (' según ', ' selon '), (' sin ', ' sans '),
        (' sobre ', ' sur '), (' desde ', ' depuis '), (' hasta ', " jusqu'à "),
        (' resultado ', ' résultat '), (' resultados ', ' résultats '),
        (' valor ', ' valeur '), (' valores ', ' valeurs '),
        (' típico ', ' typique '), (' típica ', ' typique '),
        (' común ', ' courant '), (' masa ', ' masse '), (' peso ', ' poids '),
        (' altura ', ' hauteur '), (' longitud ', ' longueur '),
        (' ancho ', ' largeur '), (' profundidad ', ' profondeur '),
        (' espesor ', ' épaisseur '), (' diámetro ', ' diamètre '),
        (' radio ', ' rayon '), (' superficie ', ' surface '),
        (' volumen ', ' volume '), (' densidad ', ' densité '),
        (' potencia ', ' puissance '), (' velocidad ', ' vitesse '),
        (' tiempo ', ' temps '), (' cantidad ', ' quantité '),
        (' número ', ' nombre '), (' unidad ', ' unité '),
        ('indica', 'indique'), ('categoría', 'catégorie'),
        ('saludable', 'sain'),
        ('ingresados', 'saisis'), ('origen', 'source'),
        ('sistema', 'système'),
        ('fachadas', 'façades'), ('cubiertas', 'toits'),
        ('tepical', 'typique'),
        ('necesario', 'nécessaire'),
        ('Ejemplo', 'Exemple'), ('ejemplo', 'exemple'),
        ('Pasos', 'Étapes'), ('pasos', 'étapes'),
        ('Paso', 'Étape'), ('paso', 'étape'),
        ('Calcula', 'Calculez'), ('Introduce', 'Saisissez'),
        ('Selecciona', 'Sélectionnez'),
    ],
    'de': [
        (' del ', ' vom '), (' y ', ' und '), (' para ', ' für '), (' por ', ' pro '),
        (' con ', ' mit '), (' según ', ' nach '), (' sin ', ' ohne '),
        (' sobre ', ' über '), (' desde ', ' ab '), (' hasta ', ' bis '),
        (' resultado ', ' Ergebnis '), (' resultados ', ' Ergebnisse '),
        (' valor ', ' Wert '), (' valores ', ' Werte '),
        (' típico ', ' typisch '), (' típica ', ' typisch '),
        (' común ', ' üblich '), (' masa ', ' Masse '), (' peso ', ' Gewicht '),
        (' altura ', ' Höhe '), (' longitud ', ' Länge '),
        (' ancho ', ' Breite '), (' profundidad ', ' Tiefe '),
        (' espesor ', ' Dicke '), (' diámetro ', ' Durchmesser '),
        (' radio ', ' Radius '), (' superficie ', ' Fläche '),
        (' volumen ', ' Volumen '), (' densidad ', ' Dichte '),
        (' potencia ', ' Leistung '), (' velocidad ', ' Geschwindigkeit '),
        (' tiempo ', ' Zeit '), (' cantidad ', ' Menge '),
        (' número ', ' Anzahl '), (' unidad ', ' Einheit '),
        (' total ', ' Gesamt '),
        ('indica', 'zeigt'), ('categoría', 'Kategorie'),
        ('saludable', 'gesund'),
        ('ingresados', 'eingegeben'),
        ('tepical', 'typisch'),
        ('Ejemplo', 'Beispiel'), ('ejemplo', 'beispiel'),
        ('Calcula', 'Berechnen'), ('Introduce', 'Eingeben'),
        ('fachadas', 'Fassaden'), ('cubiertas', 'Dächer'),
        ('lados', 'Seiten'),
        ('pagar', 'zahlen'), ('anualmente', 'jährlich'),
        ('fraccionado', 'ratenweise'),
        ('mensualidades', 'Monatsraten'),
        ('recargo', 'Aufschlag'),
    ],
    'it': [
        (' y ', ' e '), (' para ', ' per '), (' según ', ' secondo '),
        (' sin ', ' senza '), (' sobre ', ' su '), (' desde ', ' da '),
        (' hasta ', ' fino a '),
        (' resultado ', ' risultato '), (' resultados ', ' risultati '),
        (' valor ', ' valore '), (' valores ', ' valori '),
        (' típico ', ' tipico '), (' típica ', ' tipica '),
        (' común ', ' comune '), (' masa ', ' massa '),
        (' altura ', ' altezza '), (' longitud ', ' lunghezza '),
        (' ancho ', ' larghezza '), (' profundidad ', ' profondità '),
        (' espesor ', ' spessore '), (' diámetro ', ' diametro '),
        (' radio ', ' raggio '), (' superficie ', ' superficie '),
        (' volumen ', ' volume '), (' densidad ', ' densità '),
        ('indica', 'indica'), ('categoría', 'categoria'),
        ('saludable', 'sano'),
        ('ingresados', 'inseriti'), ('origen', 'origine'),
        ('sistema', 'sistema'), ('tepical', 'tipico'),
        ('fachadas', 'facciate'), ('cubiertas', 'coperture'),
        ('Ejemplo', 'Esempio'), ('Calcula', 'Calcola'),
        ('Introduce', 'Inserisci'),
        ('pagar', 'pagare'), ('anualmente', 'annualmente'),
        ('fraccionado', 'rateizzato'),
        ('mensualidades', 'rate mensili'),
        ('recargo', 'supplemento'),
    ],
    'pt': [
        (' del ', ' do '), (' y ', ' e '), (' según ', ' segundo '),
        (' sin ', ' sem '), (' desde ', ' desde '), (' hasta ', ' até '),
        (' típico ', ' típico '), (' típica ', ' típica '),
        (' común ', ' comum '), (' profundidad ', ' profundidade '),
        (' espesor ', ' espessura '), (' diámetro ', ' diâmetro '),
        (' radio ', ' raio '), (' superficie ', ' superfície '),
        (' densidad ', ' densidade '), (' potencia ', ' potência '),
        (' velocidad ', ' velocidade '),
        ('indica', 'indica'), ('categoría', 'categoria'),
        ('saludable', 'saudável'),
        ('ingresados', 'inseridos'), ('origen', 'origem'),
        ('tepical', 'típico'),
        ('Ejemplo', 'Exemplo'),
        ('fachadas', 'fachadas'), ('cubiertas', 'coberturas'),
    ],
}

def fix_text(val, lang):
    if isinstance(val, str):
        for old, new in REPLACE.get(lang, []):
            val = val.replace(old, new)
        return val
    elif isinstance(val, list):
        return [fix_text(v, lang) for v in val]
    elif isinstance(val, dict):
        return {k: fix_text(v, lang) for k, v in val.items()}
    return val

total = 0
for fpath in sorted(CALCS_DIR.glob('*.json')):
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    orig = json.dumps(data, ensure_ascii=False)
    
    i18n = data.get('i18n', {})
    for lang in ['en','fr','de','it','pt']:
        if lang not in i18n:
            continue
        ld = i18n[lang]
        for field in ['range_hints','result_context','example_label','steps','mistakes']:
            if field in ld:
                ld[field] = fix_text(ld[field], lang)
    
    new = json.dumps(data, ensure_ascii=False)
    if new != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        total += 1

print(f'Fixed {total} calc JSON files')

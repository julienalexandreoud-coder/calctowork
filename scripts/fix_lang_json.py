"""Fix Spanish text in calculator per-language JSON files."""
import json
from pathlib import Path

BASE = Path(r'C:\Microsaas\obra\src\calculators')
SPANISH_WORDS = [' del ', ' de ', ' para ', ' por ', ' con ', ' según ', ' sin ',
                 ' sobre ', ' desde ', ' hasta ', ' y ', ' o ', ' cada ', ' donde ',
                 ' mide ', ' introduce ', ' ingresa ', ' pulsa ',
                 ' resultado ', ' resultados ',
                 ' valor ', ' valores ', ' fórmula ',
                 ' típico ', ' típica ', ' común ', ' comunes ',
                 ' cantidad ', ' número ', ' unidad ', ' unidades ',
                 ' total ', ' promedio ', ' masa ', ' peso ',
                 ' altura ', ' longitud ', ' ancho ', ' profundidad ',
                 ' espesor ', ' diámetro ', ' radio ',
                 ' superficie ', ' volumen ', ' densidad ',
                 ' potencia ', ' energía ', ' velocidad ', ' tiempo ',
                 ' saludable ', ' indica ', ' categoría ',
                 ' como ', ' se ', ' más ', ' menos ',
                 ' durante ', ' siempre ', ' debe ',
                 'ingresados', 'tepical', 'origen', 'sistema',
                 'fachadas', 'cubiertas', 'lados',
                 'pagar', 'anualmente', 'fraccionado',
                 'mensualidades', 'recargo',
                 'Ejemplo', 'ejemplo', 'Pasos', 'pasos',
                 'Paso', 'paso', 'Calcula', 'Introduce',
                 'Selecciona', 'selecciona', 'Ajusta',
                 'paramento a aislar', 'planchas de isolation',
                 'La media aritmética', 'estadísticos básicos',
                 'IMC calculado', 'El IMC calculado', 'The IMC calculado']

# Translations per language for common Spanish patterns
TRANSLATIONS = {
    'en': {
        ' del ': ' of the ', ' de ': ' of ', ' para ': ' for ', ' por ': ' per ',
        ' con ': ' with ', ' según ': ' according to ', ' sin ': ' without ',
        ' sobre ': ' about ', ' desde ': ' from ', ' hasta ': ' to ',
        ' y ': ' and ', ' o ': ' or ',
        ' masa ': ' mass ', ' peso ': ' weight ',
        ' altura ': ' height ', ' longitud ': ' length ',
        ' ancho ': ' width ', ' profundidad ': ' depth ',
        ' espesor ': ' thickness ', ' diámetro ': ' diameter ',
        ' radio ': ' radius ', ' superficie ': ' area ',
        ' volumen ': ' volume ', ' densidad ': ' density ',
        ' potencia ': ' power ', ' energía ': ' energy ',
        ' velocidad ': ' speed ', ' tiempo ': ' time ',
        ' resultado ': ' result ', ' resultados ': ' results ',
        ' valor ': ' value ', ' valores ': ' values ',
        ' cantidad ': ' quantity ',
        ' típico ': ' typical ', ' típica ': ' typical ',
        ' común ': ' common ', ' comunes ': ' common ',
        'Introduce': 'Enter', 'Selecciona': 'Select',
        'Calcula': 'Calculate',
        'ingresados': 'entered', 'tepical': 'typical',
        'fachadas': 'facades', 'cubiertas': 'roofs',
        'Aislamiento': 'Insulation', 'aislamiento': 'insulation',
        'IMC calculado': 'calculated BMI',
        'El IMC calculado': 'The calculated BMI',
        'The IMC calculado': 'The calculated BMI',
    },
    'fr': {
        ' del ': ' du ', ' y ': ' et ',
        ' para ': ' pour ', ' por ': ' par ',
        ' con ': ' avec ', ' según ': ' selon ',
        ' sin ': ' sans ', ' sobre ': ' sur ',
        ' desde ': ' depuis ', ' hasta ': " jusqu'à ",
        ' típico ': ' typique ', ' típica ': ' typique ',
        ' masa ': ' masse ', ' peso ': ' poids ',
        ' altura ': ' hauteur ', ' longitud ': ' longueur ',
        ' ancho ': ' largeur ', ' profundidad ': ' profondeur ',
        ' espesor ': ' épaisseur ', ' diámetro ': ' diamètre ',
        ' radio ': ' rayon ', ' superficie ': ' surface ',
        ' volumen ': ' volume ', ' densidad ': ' densité ',
        ' potencia ': ' puissance ', ' velocidad ': ' vitesse ',
        ' tiempo ': ' temps ',
        'ingresados': 'saisis', 'tepical': 'typique',
        'Calcula': 'Calculez', 'Introduce': 'Saisissez',
        'Ejemplo': 'Exemple', 'ejemplo': 'exemple',
        'IMC calculado': 'IMC calculé',
        'El IMC calculado': "L'IMC calculé",
    },
    'de': {
        ' del ': ' vom ', ' y ': ' und ',
        ' para ': ' für ', ' por ': ' pro ',
        ' con ': ' mit ', ' según ': ' nach ',
        ' sin ': ' ohne ', ' sobre ': ' über ',
        ' desde ': ' ab ', ' hasta ': ' bis ',
        ' típico ': ' typisch ', ' típica ': ' typisch ',
        ' masa ': ' Masse ', ' peso ': ' Gewicht ',
        ' altura ': ' Höhe ', ' longitud ': ' Länge ',
        ' ancho ': ' Breite ', ' profundidad ': ' Tiefe ',
        ' espesor ': ' Dicke ', ' diámetro ': ' Durchmesser ',
        ' radio ': ' Radius ', ' superficie ': ' Fläche ',
        ' volumen ': ' Volumen ', ' densidad ': ' Dichte ',
        ' potencia ': ' Leistung ', ' velocidad ': ' Geschwindigkeit ',
        ' tiempo ': ' Zeit ', ' cantidad ': ' Menge ',
        ' número ': ' Anzahl ', ' total ': ' Gesamt ',
        'ingresados': 'eingegeben', 'tepical': 'typisch',
        'Calcula': 'Berechnen', 'Introduce': 'Eingeben',
        'IMC calculado': 'berechneter BMI',
        'El IMC calculado': 'Der berechnete BMI',
        'lados': 'Seiten', 'pagar': 'zahlen',
        'anualmente': 'jährlich', 'fraccionado': 'ratenweise',
        'recargo': 'Aufschlag',
    },
    'it': {
        ' y ': ' e ',
        ' para ': ' per ',
        ' según ': ' secondo ',
        ' sin ': ' senza ', ' sobre ': ' su ',
        ' desde ': ' da ', ' hasta ': ' fino a ',
        ' típico ': ' tipico ', ' típica ': ' tipica ',
        ' masa ': ' massa ',
        ' altura ': ' altezza ', ' longitud ': ' lunghezza ',
        ' ancho ': ' larghezza ', ' profundidad ': ' profondità ',
        ' espesor ': ' spessore ', ' diámetro ': ' diametro ',
        ' radio ': ' raggio ',
        'ingresados': 'inseriti', 'tepical': 'tipico',
        'Ejemplo': 'Esempio', 'Calcula': 'Calcola',
        'Introduce': 'Inserisci',
        'IMC calculado': 'IMC calcolato',
        'El IMC calculado': "L'IMC calcolato",
        'fachadas': 'facciate', 'cubiertas': 'coperture',
        'pagar': 'pagare', 'anualmente': 'annualmente',
        'fraccionado': 'rateizzato', 'recargo': 'supplemento',
    },
    'pt': {
        ' del ': ' do ', ' y ': ' e ',
        ' según ': ' segundo ',
        ' sin ': ' sem ', ' desde ': ' desde ', ' hasta ': ' até ',
        ' típico ': ' típico ', ' típica ': ' típica ',
        ' profundidad ': ' profundidade ',
        ' espesor ': ' espessura ', ' diámetro ': ' diâmetro ',
        ' radio ': ' raio ', ' superficie ': ' superfície ',
        ' densidad ': ' densidade ', ' potencia ': ' potência ',
        ' velocidad ': ' velocidade ',
        'ingresados': 'inseridos', 'tepical': 'típico',
        'Ejemplo': 'Exemplo',
        'IMC calculado': 'IMC calculado',
        'El IMC calculado': 'O IMC calculado',
    },
}

def fix_text(text, lang):
    if not isinstance(text, str):
        if isinstance(text, list):
            return [fix_text(t, lang) for t in text]
        if isinstance(text, dict):
            return {k: fix_text(v, lang) for k, v in text.items()}
        return text
    
    replacements = TRANSLATIONS.get(lang, {})
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

total = 0
# Iterate over calc directories
for calc_dir in sorted(BASE.iterdir()):
    if not calc_dir.is_dir():
        continue
    
    for lang in ['en', 'fr', 'de', 'it', 'pt']:
        lang_file = calc_dir / f'{lang}.json'
        if not lang_file.exists():
            continue
        
        try:
            with open(lang_file, encoding='utf-8') as f:
                data = json.load(f)
            
            orig = json.dumps(data, ensure_ascii=False)
            
            for field in ['range_hints', 'result_context', 'example_label', 'steps', 'mistakes']:
                if field in data:
                    data[field] = fix_text(data[field], lang)
            
            new = json.dumps(data, ensure_ascii=False)
            if new != orig:
                with open(lang_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                total += 1
        except Exception as e:
            print(f'  ERR {calc_dir.name}/{lang}.json: {e}')

print(f'Fixed {total} language JSON files')

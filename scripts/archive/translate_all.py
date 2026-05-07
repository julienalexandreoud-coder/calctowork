import json, glob, os, copy

CALC_DIR = r'C:\Microsaas\obra\src\calculators'

def translate_calculator(data, filepath):
    """Generate proper translations for all non-Spanish languages based on Spanish source."""
    i18n = data.get('i18n', {})
    es = i18n.get('es', {})
    
    if not es:
        return False
    
    changed = False
    
    # Build templates from Spanish and translate them
    calc_slug = data.get('slug', '')
    calc_name = es.get('name', '')
    calc_desc = es.get('description', '')
    
    # Input and output units for this calculator
    inputs = data.get('inputs', [])
    outputs = data.get('outputs', [])
    output_ids = [o['id'] for o in outputs]
    
    # Prepare output variable string for result_context
    output_vars = ', '.join('{' + o + '}' for o in output_ids[:4])
    
    # Detect calculator type from slug
    is_footing = 'zapata' in calc_slug or 'ciment' in calc_slug or 'pilar' in calc_slug
    is_concrete = 'hormigon' in calc_slug or 'hormigón' in calc_slug or 'losa' in calc_slug or 'forjado' in calc_slug
    is_masonry = 'ladrillo' in calc_slug or 'mampost' in calc_slug or 'bloque' in calc_slug or 'tabique' in calc_slug
    is_wall = 'enfoscado' in calc_slug or 'revoco' in calc_slug or 'mortero' in calc_slug or 'guarnec' in calc_slug
    is_flooring = 'solado' in calc_slug or 'porcelanico' in calc_slug or 'laminado' in calc_slug or 'parquet' in calc_slug or 'marmol' in calc_slug or 'terrazo' in calc_slug or 'azulejo' in calc_slug or 'mosaico' in calc_slug or 'adhesivo' in calc_slug or 'lechada' in calc_slug
    is_plumbing = 'tuberia' in calc_slug or 'presion' in calc_slug or 'deposito' in calc_slug or 'calentador' in calc_slug or 'caldera' in calc_slug or 'radiador' in calc_slug or 'suelo-radiante' in calc_slug or 'riego' in calc_slug or 'sifon' in calc_slug or 'acometida' in calc_slug or 'depuradora' in calc_slug or 'piscina' in calc_slug
    is_electrical = 'cable' in calc_slug or 'caida' in calc_slug or 'luminar' in calc_slug or 'puntos' in calc_slug or 'cuadro' in calc_slug or 'solar' in calc_slug or 'bateria' in calc_slug or 'trifasica' in calc_slug or 'instalacion' in calc_slug
    is_excavation = 'excavacion' in calc_slug
    is_roof = 'cubierta' in calc_slug or 'teja' in calc_slug
    is_muro = 'muro' in calc_slug
    
    for lang in ['en', 'fr', 'de', 'it']:
        if lang not in i18n:
            continue
        
        ld = i18n[lang]
        es_ld = copy.deepcopy(es)
        
        # Translate name
        if 'name' in ld and ld['name']:
            ld['name'] = translate_name(es['name'], lang, calc_slug)
            changed = True
        
        # Translate description
        if 'description' in ld:
            ld['description'] = translate_desc(es['description'], lang, calc_slug)
            changed = True
        
        # Translate seo_description
        if 'seo_description' in ld and ld['seo_description']:
            ld['seo_description'] = translate_seo_desc(es.get('seo_description', ''), lang, calc_slug)
            changed = True
        
        # Translate example_label
        if 'example_label' in ld:
            ld['example_label'] = translate_example(es.get('example_label', ''), lang, calc_slug)
            changed = True
        
        # Translate result_context
        if 'result_context' in ld:
            ld['result_context'] = translate_context(es.get('result_context', ''), lang, calc_slug)
            changed = True
        
        # Translate formula_display
        if 'formula_display' in ld:
            ld['formula_display'] = es.get('formula_display', '')
            changed = True
        
        # Translate steps
        if 'steps' in ld:
            ld['steps'] = translate_steps(es.get('steps', []), lang, calc_slug)
            changed = True
        
        # Translate mistakes
        if 'mistakes' in ld:
            ld['mistakes'] = translate_mistakes(es.get('mistakes', []), lang, calc_slug)
            changed = True
        
        # Translate range_hints
        if 'range_hints' in ld:
            ld['range_hints'] = translate_range_hints(es.get('range_hints', {}), lang)
            changed = True
        
        # Translate input/output labels
        if 'inputs' in ld:
            for k in ld['inputs']:
                ld['inputs'][k] = translate_label(es.get('inputs', {}).get(k, k), lang, calc_slug)
            changed = True
        if 'outputs' in ld:
            for k in ld['outputs']:
                ld['outputs'][k] = translate_label(es.get('outputs', {}).get(k, k), lang, calc_slug)
            changed = True
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return True


def translate_name(name, lang, slug):
    """Translate calculator name."""
    if lang == 'en':
        return name.replace('Calculadora de', 'Calculator:').replace('Calculadora', 'Calculator').replace('Cálculo de', 'Calculation of').replace('Cálculo', 'Calculation')
    elif lang == 'fr':
        return name.replace('Calculadora de', 'Calculateur de').replace('Calculadora', 'Calculateur').replace('Cálculo de', 'Calcul de').replace('Cálculo', 'Calcul')
    elif lang == 'de':
        return name.replace('Calculadora de', 'Rechner für').replace('Calculadora', 'Rechner').replace('Cálculo de', 'Berechnung von').replace('Cálculo', 'Berechnung')
    elif lang == 'it':
        return name.replace('Calculadora de', 'Calcolatore per').replace('Calculadora', 'Calcolatore').replace('Cálculo de', 'Calcolo di').replace('Cálculo', 'Calcolo')
    return name


EN_MAP = {
    'calcula': 'calculates', 'Calcula': 'Calculates', 'Calcular': 'Calculate', 'calcular': 'calculate',
    'el volumen': 'the volume', 'los materiales': 'the materials',
    'la cantidad': 'the quantity', 'las dimensiones': 'the dimensions',
    'el consumo': 'the consumption', 'la potencia': 'the power',
    'necesario': 'needed', 'necesaria': 'needed', 'necesarios': 'needed',
    'hormigón': 'concrete', 'hormigon': 'concrete', 'Hormigón': 'Concrete',
    'mortero': 'mortar', 'encofrado': 'formwork', 'Encofrado': 'Formwork',
    'acero': 'steel', 'Acero': 'Steel', 'cemento': 'cement',
    'ladrillos': 'bricks', 'ladrillo': 'brick',
    'zapatas': 'footings', 'zapata': 'footing',
    'pilares': 'pillars', 'pilar': 'pillar',
    'aislada': 'isolated', 'aisladas': 'isolated',
    'cimentación': 'foundation', 'muro': 'wall',
    'tubería': 'pipe', 'tuberia': 'pipe', 'Tubería': 'Pipe',
    'instalación': 'installation', 'instalacion': 'installation',
    'presión': 'pressure', 'presion': 'pressure',
    'agua': 'water', 'aire': 'air',
    'calefacción': 'heating', 'refrigeración': 'cooling',
    'eléctrico': 'electrical', 'eléctrica': 'electrical',
    'eléctricos': 'electrical', 'electrico': 'electrical',
    'térmica': 'thermal', 'térmico': 'thermal',
    'calentador': 'water heater', 'caldera': 'boiler',
    'radiador': 'radiator', 'suelo': 'floor',
    'conducto': 'duct', 'conductos': 'ducts',
    'ventilación': 'ventilation', 'mecánica': 'mechanical',
    'piscina': 'pool', 'depuradora': 'filter',
    'iluminación': 'lighting', 'luminaria': 'light fixture',
    'luminarias': 'light fixtures', 'lúmenes': 'lumens',
    'cable': 'cable', 'sección': 'cross-section',
    'tensión': 'voltage', 'caída': 'drop',
    'batería': 'battery', 'baterías': 'batteries',
    'autonomía': 'autonomy', 'autonomia': 'autonomy',
    'solar': 'solar', 'placa': 'panel',
    'trifásica': 'three-phase', 'trifásico': 'three-phase',
    'cuadro': 'panel', 'eléctrico': 'electrical panel',
    'puntos': 'points', 'luz': 'light', 'habitación': 'room',
    'habitaciones': 'rooms', 'para': 'for', 'por': 'per',
    'según': 'according to', 'con': 'with',
    'canto': 'depth', 'altura': 'height',
    'largo': 'length', 'ancho': 'width',
    'profundidad': 'depth', 'espesor': 'thickness',
    'diámetro': 'diameter', 'diametro': 'diameter',
    'superficie': 'surface', 'superficie': 'area',
    'volumen': 'volume', 'caudal': 'flow rate',
    'peso': 'weight', 'masa': 'mass',
    'densidad': 'density', 'cantidad': 'quantity',
    'rendimiento': 'performance', 'eficiencia': 'efficiency',
    'consumo': 'consumption', 'consumo': 'consumption',
    'energía': 'energy', 'energia': 'energy',
    'ahorro': 'savings', 'coste': 'cost',
    'material': 'material', 'materiales': 'materials',
    'estructuras': 'structures', 'obra': 'construction',
    'resistencia': 'resistance', 'carga': 'load',
    'resultado': 'result', 'resultados': 'results',
    'obtén': 'get', 'obtener': 'obtain',
    'introduce': 'enter', 'calcular': 'calculate',
    'pulsa': 'press', 'utiliza': 'use',
    'herramienta': 'tool', 'fácil': 'easy',
    'rápido': 'quick', 'online': 'online',
    'gratis': 'free', 'profesional': 'professional',
    'profesionales': 'professionals', 'estudiantes': 'students',
    'paso a paso': 'step by step', 'fórmula': 'formula',
}


def translate_desc(text, lang, slug):
    """Translate description."""
    if not text:
        return ''
    
    if lang == 'en':
        return simple_translate(text, EN_MAP)
    elif lang == 'fr':
        return text.replace('Calcula', 'Calculez').replace('calcula', 'calculez').replace('el ', 'le ').replace('la ', 'la ').replace('los ', 'les ').replace('las ', 'les ').replace('para ', 'pour ').replace('con ', 'avec ').replace('en ', 'en ').replace('de ', 'de ').replace('del ', 'du ')
    elif lang == 'de':
        return text.replace('Calcula', 'Berechnet').replace('calcula', 'berechnet').replace('el ', 'das ').replace('la ', 'die ').replace('los ', 'die ').replace('para ', 'für ')
    elif lang == 'it':
        return text.replace('Calcula', 'Calcola').replace('calcula', 'calcola').replace('el ', 'il ').replace('la ', 'la ').replace('los ', 'i ').replace('las ', 'le ').replace('para ', 'per ').replace('con ', 'con ')
    return text


def simple_translate(text, mapping):
    """Simple word-by-word translation using a mapping."""
    result = text
    for es_word, en_word in sorted(mapping.items(), key=lambda x: -len(x[0])):
        result = result.replace(es_word, en_word)
    return result


def translate_example(text, lang, slug):
    """Translate example_label."""
    if not text:
        return ''
    if lang == 'en':
        return simple_translate(text, EN_MAP)
    elif lang == 'fr':
        return text.replace('Calcular', 'Calculer').replace('para', 'pour').replace('con', 'avec').replace('de', 'de').replace('del', 'du').replace('y', 'et')
    elif lang == 'de':
        return text.replace('Calcular', 'Berechnen').replace('para', 'für').replace('con', 'mit').replace('de', 'von').replace('y', 'und')
    elif lang == 'it':
        return text.replace('Calcular', 'Calcolare').replace('para', 'per').replace('con', 'con').replace('de', 'di').replace('y', 'e')
    return text


def translate_context(text, lang, slug):
    """Translate result_context preserving {variables}."""
    if not text:
        return ''
    
    if lang == 'en':
        # Use hardcoded good translations based on common patterns
        context_en = simple_translate(text, EN_MAP)
        return context_en
    elif lang == 'fr':
        # French translations
        result = text
        result = result.replace('requiere', 'nécessite').replace('requieren', 'nécessitent')
        result = result.replace('Para', 'Pour').replace('para', 'pour')
        result = result.replace('con', 'avec').replace('Con', 'Avec')
        result = result.replace(' del ', ' du ').replace(' de ', ' de ')
        result = result.replace(' y ', ' et ').replace(' Y ', ' Et ')
        result = result.replace(' en ', ' en ').replace(' por ', ' par ')
        result = result.replace(' total', ' total').replace('Total', 'Total')
        result = result.replace(' cada ', ' chaque ').replace('Cada ', 'Chaque ')
        result = result.replace(' m³ ', ' m³ ').replace(' m² ', ' m² ')
        result = result.replace(' kg ', ' kg ').replace(' mm ', ' mm ')
        result = result.replace(' kW ', ' kW ').replace(' V ', ' V ')
        result = result.replace('horas', 'heures').replace('días', 'jours')
        result = result.replace('meses', 'mois').replace('años', 'ans')
        result = result.replace('necesita', 'nécessite').replace('necesitan', 'nécessitent')
        result = result.replace('equivale', 'équivaut').replace('equivalen', 'équivalent')
        result = result.replace('resultado', 'résultat').replace('Resultado', 'Résultat')
        result = result.replace('unidad', 'unité').replace('unidades', 'unités')
        result = result.replace('metro', 'mètre').replace('metros', 'mètres')
        result = result.replace('cuadrado', 'carré').replace('cuadrados', 'carrés')
        result = result.replace('cúbico', 'cube').replace('cúbicos', 'cubes')
        result = result.replace('sacos', 'sacs').replace('saco', 'sac')
        result = result.replace(' litros', ' litres').replace('Litros', 'Litres')
        return result
    elif lang == 'de':
        result = text
        result = result.replace('requiere', 'benötigt').replace('requieren', 'benötigen')
        result = result.replace('Para', 'Für').replace('para', 'für')
        result = result.replace('con', 'mit').replace('Con', 'Mit')
        result = result.replace(' del ', ' vom ').replace(' de ', ' von ')
        result = result.replace(' y ', ' und ').replace(' Y ', ' Und ')
        result = result.replace(' en ', ' in ').replace(' por ', ' pro ')
        result = result.replace(' total', ' insgesamt').replace('Total', 'Insgesamt')
        result = result.replace(' cada ', ' pro ').replace('Cada ', 'Jede ')
        result = result.replace(' m³ ', ' m³ ').replace(' m² ', ' m² ')
        result = result.replace(' kg ', ' kg ').replace(' mm ', ' mm ')
        result = result.replace(' kW ', ' kW ').replace(' V ', ' V ')
        result = result.replace('horas', 'Stunden').replace('días', 'Tage')
        result = result.replace('meses', 'Monate').replace('años', 'Jahre')
        result = result.replace('necesita', 'benötigt').replace('necesitan', 'benötigen')
        result = result.replace('equivale', 'entspricht').replace('equivalen', 'entsprechen')
        result = result.replace('resultado', 'Ergebnis').replace('Resultado', 'Ergebnis')
        result = result.replace('unidad', 'Einheit').replace('unidades', 'Einheiten')
        result = result.replace('metro', 'Meter').replace('metros', 'Meter')
        result = result.replace('cuadrado', 'Quadrat-').replace('cuadrados', 'Quadrat-')
        result = result.replace('cúbico', 'Kubik-').replace('cúbicos', 'Kubik-')
        result = result.replace('sacos', 'Säcke').replace('saco', 'Sack')
        result = result.replace(' litros', ' Liter').replace('Litros', 'Liter')
        return result
    elif lang == 'it':
        result = text
        result = result.replace('requiere', 'richiede').replace('requieren', 'richiedono')
        result = result.replace('Para', 'Per').replace('para', 'per')
        result = result.replace('con', 'con').replace('Con', 'Con')
        result = result.replace(' del ', ' del ').replace(' de ', ' di ')
        result = result.replace(' y ', ' e ').replace(' Y ', ' E ')
        result = result.replace(' en ', ' in ').replace(' por ', ' per ')
        result = result.replace(' total', ' totale').replace('Total', 'Totale')
        result = result.replace(' cada ', ' ogni ').replace('Cada ', 'Ogni ')
        result = result.replace(' m³ ', ' m³ ').replace(' m² ', ' m² ')
        result = result.replace(' kg ', ' kg ').replace(' mm ', ' mm ')
        result = result.replace(' kW ', ' kW ').replace(' V ', ' V ')
        result = result.replace('horas', 'ore').replace('días', 'giorni')
        result = result.replace('meses', 'mesi').replace('años', 'anni')
        result = result.replace('necesita', 'necessita').replace('necesitan', 'necessitano')
        result = result.replace('equivale', 'equivale').replace('equivalen', 'equivalgono')
        result = result.replace('resultado', 'risultato').replace('Resultado', 'Risultato')
        result = result.replace('unidad', 'unità').replace('unidades', 'unità')
        result = result.replace('metro', 'metro').replace('metros', 'metri')
        result = result.replace('cuadrado', 'quadrato').replace('cuadrados', 'quadrati')
        result = result.replace('cúbico', 'cubo').replace('cúbicos', 'cubi')
        result = result.replace('sacos', 'sacchi').replace('saco', 'sacco')
        result = result.replace(' litros', ' litri').replace('Litros', 'Litri')
        return result
    return text


def translate_steps(steps, lang, slug):
    """Translate calculation steps."""
    if not steps:
        return []
    
    result = []
    for step in steps:
        translated = step
        if lang == 'en':
            translated = simple_translate(step, EN_MAP)
        elif lang == 'fr':
            translated = step.replace('Calcular', 'Calculer').replace('Identificar', 'Identifier').replace('Obtener', 'Obtenir')
            translated = translated.replace(' de ', ' de ').replace(' del ', ' du ').replace(' por ', ' par ')
            translated = translated.replace(' y ', ' et ').replace(' = ', ' = ').replace(' ÷ ', ' ÷ ')
            translated = translated.replace('horas', 'heures').replace('minutos', 'minutes')
        elif lang == 'de':
            translated = step.replace('Calcular', 'Berechnen').replace('Identificar', 'Identifizieren').replace('Obtener', 'Erhalten')
            translated = translated.replace(' de ', ' von ').replace(' del ', ' vom ').replace(' por ', ' pro ')
            translated = translated.replace(' y ', ' und ').replace(' = ', ' = ')
            translated = translated.replace('horas', 'Stunden').replace('minutos', 'Minuten')
        elif lang == 'it':
            translated = step.replace('Calcular', 'Calcolare').replace('Identificar', 'Identificare').replace('Obtener', 'Ottenere')
            translated = translated.replace(' de ', ' di ').replace(' del ', ' del ').replace(' por ', ' per ')
            translated = translated.replace(' y ', ' e ').replace(' = ', ' = ')
            translated = translated.replace('horas', 'ore').replace('minutos', 'minuti')
        result.append(translated)
    return result


def translate_mistakes(mistakes, lang, slug):
    """Translate common mistakes."""
    if not mistakes:
        return []
    
    result = []
    for mist in mistakes:
        translated = mist
        if lang == 'en':
            translated = simple_translate(mist, EN_MAP)
        elif lang == 'fr':
            translated = mist.replace('No ', 'Ne pas ').replace('no ', 'ne pas ')
            translated = translated.replace(' de ', ' de ').replace(' del ', ' du ').replace(' por ', ' par ')
            translated = translated.replace(' y ', ' et ').replace(' en ', ' en ')
            translated = translated.replace(' entre ', ' entre ').replace(' sobre ', ' sur ')
            translated = translated.replace(' que ', ' que ').replace(' con ', ' avec ')
            translated = translated.replace('La ', 'La ').replace('El ', 'Le ').replace('Los ', 'Les ')
        elif lang == 'de':
            translated = mist.replace('No ', 'Nicht ').replace('no ', 'nicht ')
            translated = translated.replace(' de ', ' von ').replace(' del ', ' vom ').replace(' por ', ' pro ')
            translated = translated.replace(' y ', ' und ').replace(' en ', ' in ')
            translated = translated.replace(' entre ', ' zwischen ').replace(' sobre ', ' über ')
            translated = translated.replace(' que ', ' dass ').replace(' con ', ' mit ')
            translated = translated.replace('La ', 'Die ').replace('El ', 'Der ').replace('Los ', 'Die ')
        elif lang == 'it':
            translated = mist.replace('No ', 'Non ').replace('no ', 'non ')
            translated = translated.replace(' de ', ' di ').replace(' del ', ' del ').replace(' por ', ' per ')
            translated = translated.replace(' y ', ' e ').replace(' en ', ' in ')
            translated = translated.replace(' entre ', ' tra ').replace(' sobre ', ' su ')
            translated = translated.replace(' que ', ' che ').replace(' con ', ' con ')
            translated = translated.replace('La ', 'La ').replace('El ', 'Il ').replace('Los ', 'I ')
        result.append(translated)
    return result


def translate_range_hints(hints, lang):
    """Translate range hints."""
    if not hints:
        return {}
    
    result = {}
    for k, v in hints.items():
        translated = v
        if lang == 'en':
            translated = simple_translate(v, EN_MAP)
        elif lang == 'fr':
            translated = v.replace(' de ', ' de ').replace(' por ', ' par ').replace(' entre ', ' entre ').replace(' y ', ' et ').replace(' según ', ' selon ')
            translated = translated.replace('Valor típico', 'Valeur typique').replace('Rango', 'Plage')
        elif lang == 'de':
            translated = v.replace(' de ', ' von ').replace(' por ', ' pro ').replace(' entre ', ' zwischen ').replace(' y ', ' und ').replace(' según ', ' nach ')
            translated = translated.replace('Valor típico', 'Typischer Wert').replace('Rango', 'Bereich')
        elif lang == 'it':
            translated = v.replace(' de ', ' di ').replace(' por ', ' per ').replace(' entre ', ' tra ').replace(' y ', ' e ').replace(' según ', ' secondo ')
            translated = translated.replace('Valor típico', 'Valore tipico').replace('Rango', 'Intervallo')
        result[k] = translated
    return result


def translate_label(label, lang, slug):
    """Translate individual input/output label."""
    if not label:
        return label
    
    if lang == 'en':
        return simple_translate(label, EN_MAP)
    elif lang == 'fr':
        return label.replace(' de ', ' de ').replace(' del ', ' du ').replace(' por ', ' par ').replace('metros', 'mètres').replace('cuadrado', 'carré').replace('cúbico', 'cube').replace('sacos', 'sacs').replace('litros', 'litres')
    elif lang == 'de':
        return label.replace(' de ', ' von ').replace(' del ', ' vom ').replace('metros', 'Meter').replace('sacos', 'Säcke').replace('litros', 'Liter')
    elif lang == 'it':
        return label.replace(' de ', ' di ').replace(' del ', ' del ').replace('metros', 'metri').replace('sacos', 'sacchi').replace('litros', 'litri')
    return label


def translate_seo_desc(text, lang, slug):
    """Translate SEO description."""
    if not text:
        return ''
    if lang == 'en':
        return simple_translate(text, EN_MAP)[:157].rstrip()
    elif lang == 'fr':
        result = text.replace('Calcula', 'Calculez').replace(' de ', ' de ').replace(' del ', ' du ').replace(' para ', ' pour ').replace(' con ', ' avec ').replace(' en ', ' en ').replace(' por ', ' par ')
        result = result.replace('online', 'en ligne').replace('gratis', 'gratuit')
        return result[:157].rstrip()
    elif lang == 'de':
        result = text.replace('Calcula', 'Berechnet').replace(' de ', ' von ').replace(' del ', ' vom ').replace(' para ', ' für ').replace(' con ', ' mit ')
        result = result.replace('online', 'online').replace('gratis', 'kostenlos')
        return result[:157].rstrip()
    elif lang == 'it':
        result = text.replace('Calcula', 'Calcola').replace(' de ', ' di ').replace(' del ', ' del ').replace(' para ', ' per ').replace(' con ', ' con ')
        result = result.replace('online', 'online').replace('gratis', 'gratuito')
        return result[:157].rstrip()
    return text[:157].rstrip()


if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(CALC_DIR, '*.json')))
    fixed = 0
    
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            cid = int(data.get('id', '999'))
            if cid > 50:
                continue
            
            translate_calculator(data, f)
            fixed += 1
            print(f'Translated: {cid:03d} {data["slug"]}')
        except Exception as e:
            import traceback
            print(f'Error {f}: {e}')
            traceback.print_exc()
    
    print(f'\nTotal translated: {fixed}')

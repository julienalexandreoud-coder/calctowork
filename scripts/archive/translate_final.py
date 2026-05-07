"""
Comprehensive calculator translation fixer.
Generates proper translations for all 50 calculators across 6 languages.
"""
import json, glob, os

CALC_DIR = r'C:\Microsaas\obra\src\calculators'

# ============================================================
# PER-CALCULATOR TRANSLATIONS (ID 001-050)
# ============================================================

def get_translations(cid, slug, data):
    """Return i18n block with proper translations for all languages."""
    i18n = data.get('i18n', {})
    es = i18n.get('es', {})
    
    # Build translation using the Spanish version but ensuring proper language
    result = {'es': es}
    
    for lang in ['en', 'fr', 'de', 'it', 'pt']:
        if lang in i18n:
            result[lang] = fix_language_block(i18n[lang], es, lang, slug, cid, data)
    
    return result


def fix_language_block(current, es, lang, slug, cid, data):
    """Fix a language block by correcting Spanish text and ensuring proper translations."""
    import copy
    result = copy.deepcopy(current)
    
    # Helper: get proper translation key based on language
    if lang == 'pt':
        # Portuguese is close to Spanish - mostly clean up
        return fix_portuguese(result, es, slug)
    
    if lang == 'en':
        return fix_english(result, es, slug, cid, data)
    
    if lang == 'fr':
        return fix_french(result, es, slug, cid, data)
    
    if lang == 'de':
        return fix_german(result, es, slug, cid, data)
    
    if lang == 'it':
        return fix_italian(result, es, slug, cid, data)
    
    return result


# ===== ENGLISH FIX =====
def fix_english(ld, es, slug, cid, data):
    """Fix English translation block."""
    
    calc_name_es = es.get('name', '')
    calc_name_en = calc_name_es.replace('Calculadora de', 'Calculator').replace('Cálculo de', 'Calculation of').replace('Cálculo', 'Calculation')
    
    ld['name'] = calc_name_en
    
    # Fix description
    ld['description'] = generate_english_description(slug, cid, data)
    
    # Fix example_label
    ld['example_label'] = generate_english_example(slug, es, data)
    
    # Fix result_context
    ld['result_context'] = generate_english_context(slug, es, data)
    
    # Fix steps
    ld['steps'] = generate_english_steps(slug, es, data)
    
    # Fix mistakes
    ld['mistakes'] = generate_english_mistakes(slug, es, data)
    
    # Fix seo_description
    ld['seo_description'] = generate_english_seo(slug, es, data)
    
    # Fix input labels
    inputs = data.get('inputs', [])
    for inp in inputs:
        iid = inp['id']
        if 'inputs' not in ld:
            ld['inputs'] = {}
        ld['inputs'][iid] = generate_english_input_label(iid, slug, inp)
    
    # Fix output labels
    outputs = data.get('outputs', [])
    for out in outputs:
        oid = out['id']
        if 'outputs' not in ld:
            ld['outputs'] = {}
        ld['outputs'][oid] = generate_english_output_label(oid, slug, out)
    
    # Fix range_hints
    if 'range_hints' in ld:
        ld['range_hints'] = {}
        for k, v in es.get('range_hints', {}).items():
            ld['range_hints'][k] = clean_english(v)
    
    # Fix seo_title
    if len(ld.get('seo_title', '')) > 60:
        ld['seo_title'] = ld['seo_title'][:57].rstrip() + '...'
    
    return ld


def generate_english_description(slug, cid, data):
    """Generate English description."""
    inputs = data.get('inputs', [])
    outputs = data.get('outputs', [])
    input_id_names = {i['id']: i.get('unit', i['id']) for i in inputs}
    output_id_names = {o['id']: o.get('unit', o['id']) for o in outputs}
    output_ids = [o['id'] for o in outputs]
    output_units = {o['id']: o.get('unit', '') for o in outputs}
    
    # Build a simple description
    output_str = ', '.join(output_units.get(o, o) for o in output_ids[:3])
    
    cat = get_category(slug)
    
    descs = {
        1: f"Calculate concrete volume, cement bags, steel reinforcement, and formwork for mass concrete elements.",
        2: f"Calculate concrete volume, steel reinforcement, cement, and formwork for reinforced concrete structures.",
        3: f"Calculate concrete, formwork, and steel for isolated footings in column foundations.",
        4: f"Calculate concrete volume, formwork area, and steel reinforcement for retaining walls.",
        5: f"Calculate concrete and formwork for reinforced concrete pillars.",
        6: f"Calculate concrete, formwork, and steel for reinforced concrete beams.",
        7: f"Calculate materials for beam-and-block floor slabs including concrete volume and reinforcement.",
        8: f"Calculate concrete volume, reinforcement, and formwork for concrete floor slabs.",
        9: f"Calculate concrete volume and excavation for strip foundations.",
        10: f"Calculate excavation volume and soil removal for trenches and foundations.",
        11: f"Calculate number of hollow bricks, mortar, and material requirements for brick walls.",
        12: f"Calculate facing bricks, mortar, and material needs for exposed brick walls.",
        13: f"Calculate concrete blocks, mortar, and materials for block walls.",
        14: f"Calculate plasterboard panels, metal studs, and insulation for drywall partitions.",
        15: f"Calculate insulation thickness, material, and surface area for thermal insulation.",
        16: f"Calculate cement consumption and material for sprayed plaster finish.",
        17: f"Calculate cement, sand, and water for mortar mixes by volume.",
        18: f"Calculate gypsum plaster and materials for wall and ceiling finishes.",
        19: f"Calculate stone, mortar, and materials for rubble stone masonry walls.",
        20: f"Calculate tiles, battens, and materials for pitched tile roofs.",
        21: f"Calculate ceramic floor tiles, adhesive, and grout for flooring installations.",
        22: f"Calculate porcelain tiles, adhesive, and grout for large-format flooring.",
        23: f"Calculate laminate flooring planks, underlay, and accessories for floating floors.",
        24: f"Calculate wood parquet flooring, adhesive, and finishing materials.",
        25: f"Calculate marble or granite slabs, adhesive, and joint material for luxury flooring.",
        26: f"Calculate terrazzo tiles, mortar bed, and materials for terrazzo flooring.",
        27: f"Calculate wall tiles, adhesive, and grout for ceramic wall tiling.",
        28: f"Calculate mosaic tiles, adhesive, and grout for decorative mosaic installations.",
        29: f"Calculate ceramic tile adhesive consumption based on area and trowel type.",
        30: f"Calculate tile grout quantity based on joint width, depth, and tile dimensions.",
        31: f"Calculate PVC pipe diameters, slopes, and materials for plumbing drainage systems.",
        32: f"Calculate copper and PEX pipe diameters, lengths, and fittings for plumbing.",
        33: f"Calculate water pressure in pipes, head loss, and flow characteristics.",
        34: f"Calculate water tank capacity, dimensions, and supply autonomy.",
        35: f"Calculate water heater capacity, recovery time, and energy consumption.",
        36: f"Calculate gas boiler power, efficiency, and fuel consumption.",
        37: f"Calculate aluminum radiator power, element count, and heat output.",
        38: f"Calculate radiant floor heating pipe length, circuit layout, and heat output.",
        39: f"Calculate drip irrigation flow rate, emitter spacing, and system design.",
        40: f"Calculate water service connection pipe diameter, flow rate, and pressure.",
        41: f"Calculate pool filter pump requirements, turnover rate, and filtration capacity.",
        42: f"Calculate floor drain and trap dimensions, flow capacity, and ventilation.",
        43: f"Calculate electrical cable cross-section based on current, length, and voltage drop.",
        44: f"Calculate voltage drop in electrical cables and verify compliance with standards.",
        45: f"Calculate the number of light fixtures and lumens needed per room.",
        46: f"Calculate the number of electrical outlets and light points per room.",
        47: f"Calculate electrical panel capacity, breaker sizing, and load distribution.",
        48: f"Calculate solar panel requirements, battery capacity, and system sizing.",
        49: f"Calculate battery bank autonomy, capacity, and backup time.",
        50: f"Calculate three-phase power, current, and apparent power for electrical systems.",
    }
    
    return descs.get(cid, f"Calculate {output_str} for {slug.replace('-', ' ')} projects.")


def get_category(slug):
    """Get calculator category from slug."""
    cats = {
        'hormigon-masa': 'concrete', 'hormigon-armado': 'concrete',
        'zapata-aislada': 'foundation', 'muro-contencion': 'retaining',
        'pilares-hormigon': 'structural', 'vigas-hormigon': 'structural',
        'forjado-vigueta': 'structural', 'losa-hormigon': 'structural',
        'cimiento-corrido': 'foundation', 'excavacion-tierra': 'earthwork',
        'ladrillo-hueco': 'masonry', 'ladrillo-cara-vista': 'masonry',
        'bloque-hormigon': 'masonry', 'tabique-pladur': 'drywall',
        'aislamiento-termico': 'insulation', 'revoco-proyectado': 'plaster',
        'mortero-cemento': 'mortar', 'enfoscado-guarnecido': 'plaster',
        'mamposteria-piedra': 'masonry', 'cubierta-teja': 'roofing',
        'solado-ceramico': 'flooring', 'porcelanico': 'flooring',
        'laminado-flotante': 'flooring', 'parquet-madera': 'flooring',
        'marmol-granito': 'flooring', 'terrazo': 'flooring',
        'azulejo-pared': 'tiling', 'mosaico': 'tiling',
        'adhesivo-ceramico': 'tiling', 'lechada-junta': 'tiling',
        'tuberia-pvc-saneamiento': 'plumbing', 'tuberia-cobre-pex': 'plumbing',
        'presion-agua': 'plumbing', 'deposito-agua': 'plumbing',
        'calentador-agua': 'plumbing', 'caldera-gas': 'plumbing',
        'radiador-aluminio': 'plumbing', 'suelo-radiante': 'plumbing',
        'riego-goteo': 'plumbing', 'acometida-agua': 'plumbing',
        'depuradora-piscina': 'plumbing', 'sifon-sumidero': 'plumbing',
        'cable-electrico-seccion': 'electrical', 'caida-tension': 'electrical',
        'luminarias-lumenes': 'electrical', 'puntos-luz-habitacion': 'electrical',
        'cuadro-electrico': 'electrical', 'instalacion-solar': 'electrical',
        'baterias-autonomia': 'electrical', 'trifasica-potencia': 'electrical',
    }
    return cats.get(slug, 'general')


def generate_english_example(slug, es, data):
    """Generate English example_label."""
    # Just do basic cleanup of Spanish text
    text = es.get('example_label', '')
    return clean_english(text)


def generate_english_context(slug, es, data):
    """Generate English result_context preserving {variables}."""
    text = es.get('result_context', '')
    return clean_english(text)


def generate_english_steps(slug, es, data):
    """Generate English steps."""
    steps = es.get('steps', [])
    return [clean_english(s) for s in steps]


def generate_english_mistakes(slug, es, data):
    """Generate English mistakes."""
    mistakes = es.get('mistakes', [])
    return [clean_english(m) for m in mistakes]


def generate_english_seo(slug, es, data):
    """Generate English SEO description."""
    text = es.get('seo_description', '')
    result = clean_english(text)
    if len(result) > 160:
        result = result[:157].rstrip() + '...'
    return result


def generate_english_input_label(iid, slug, inp):
    """Generate English input label."""
    unit = inp.get('unit', '')
    label_es = ''  # Will be filled from esa
    
    # Common input label translations
    label_map = {
        'largo': 'Length',
        'ancho': 'Width',
        'longitud': 'Length',
        'altura': 'Height',
        'profundidad': 'Depth',
        'espesor': 'Thickness',
        'canto': 'Depth / Height',
        'radio': 'Radius',
        'diametro': 'Diameter',
        'diámetro': 'Diameter',
        'cantidad': 'Quantity',
        'superficie': 'Surface area',
        'volumen': 'Volume',
        'masa': 'Mass',
        'peso': 'Weight',
        'densidad': 'Density',
        'presion': 'Pressure',
        'presión': 'Pressure',
        'temperatura': 'Temperature',
        'caudal': 'Flow rate',
        'potencia': 'Power',
        'tension': 'Voltage',
        'tensión': 'Voltage',
        'corriente': 'Current',
        'intensidad': 'Current intensity',
        'resistencia': 'Resistance',
        'frecuencia': 'Frequency',
        'factor_potencia': 'Power factor',
        'horas': 'Hours',
        'dias': 'Days',
        'días': 'Days',
        'anos': 'Years',
        'años': 'Years',
        'porcentaje': 'Percentage',
        'numero': 'Number',
        'núcleos': 'Cores',
        'metros': 'Metres',
        'litros': 'Litres',
        'kg': 'kg',
        'sacos': 'Bags',
    }
    
    if iid in label_map:
        return label_map[iid]
    
    return iid.replace('_', ' ').title()


def generate_english_output_label(oid, slug, out):
    """Generate English output label."""
    unit = out.get('unit', '')
    
    label_map = {
        'volumen': 'Volume',
        'vol_unitario': 'Unit volume',
        'vol_total': 'Total volume',
        'resistencia_total': 'Total resistance',
        'num_luminarias': 'Number of fixtures',
        'lumenes_totales': 'Total lumens',
        'potencia_total': 'Total power',
        'corriente_total': 'Total current',
        'ahorro': 'Savings',
        'coste': 'Cost',
        'consumo': 'Consumption',
        'rendimiento': 'Efficiency',
        'cop': 'COP',
        'eer': 'EER',
        'caudal': 'Flow rate',
        'presion': 'Pressure',
        'temperatura': 'Temperature',
        'peso': 'Weight',
        'superficie': 'Surface area',
        'perimetro': 'Perimeter',
        'longitud': 'Length',
        'altura': 'Height',
        'ancho': 'Width',
        'diametro': 'Diameter',
        'cantidad': 'Quantity',
        'unidades': 'Units',
        'tiempo': 'Time',
        'velocidad': 'Speed',
        'distancia': 'Distance',
        'fuerza': 'Force',
        'energia': 'Energy',
        'potencia_activa': 'Active power',
        'potencia_reactiva': 'Reactive power',
        'potencia_aparente': 'Apparent power',
        'factor_potencia': 'Power factor',
        'seccion': 'Cross-section',
        'caida_tension': 'Voltage drop',
        'autonomia': 'Autonomy',
        'capacidad': 'Capacity',
        'bateria': 'Battery',
        'sacos': 'Bags',
        'kg': 'kg',
    }
    
    if oid in label_map:
        return label_map[oid]
    
    return oid.replace('_', ' ').title()


def clean_english(text):
    """Clean Spanish words from text and convert to English."""
    if not text:
        return text
    
    # Step 1: Replace common Spanish words/phrases with English equivalents
    replacements = [
        # Prepositions and articles
        (r'\bdel\b', 'of the'), (r'\bde\b', 'of'), (r'\bpara\b', 'for'),
        (r'\bpor\b', 'per'), (r'\ben\b', 'in'), (r'\bcon\b', 'with'),
        (r'\bsegún\b', 'according to'), (r'\bentre\b', 'between'),
        (r'\bhasta\b', 'to'), (r'\bdesde\b', 'from'),
        (r'\bsin\b', 'without'), (r'\bsobre\b', 'over'),
        (r'\by\b', 'and'), (r'\bo\b', 'or'),
        (r'\bcada\b', 'each'), (r'\bCada\b', 'Each'),
        # Units and quantities
        (r'\bsacos\b', 'bags'), (r'\bsaco\b', 'bag'),
        (r'\blitros\b', 'liters'), (r'\blitro\b', 'liter'),
        (r'\bmetros\b', 'metres'), (r'\bmetro\b', 'metre'),
        (r'\bhoras\b', 'hours'), (r'\bhora\b', 'hour'),
        (r'\bdías\b', 'days'), (r'\bdía\b', 'day'),
        (r'\bmeses\b', 'months'), (r'\bmes\b', 'month'),
        (r'\baños\b', 'years'), (r'\baño\b', 'year'),
        (r'\bcuadrado\b', 'square'), (r'\bcúbico\b', 'cubic'),
        # Construction
        (r'\bhormigón\b', 'concrete'), (r'\bmortero\b', 'mortar'),
        (r'\blosa\b', 'slab'), (r'\bzapata\b', 'footing'),
        (r'\bzapatas\b', 'footings'), (r'\bviga\b', 'beam'),
        (r'\bvigas\b', 'beams'), (r'\bpilar\b', 'pillar'),
        (r'\bpilares\b', 'pillars'), (r'\bmuro\b', 'wall'),
        (r'\bcimiento\b', 'foundation'), (r'\bladrillo\b', 'brick'),
        (r'\bladrillos\b', 'bricks'), (r'\bencofrado\b', 'formwork'),
        (r'\bacero\b', 'steel'), (r'\bcemento\b', 'cement'),
        (r'\barena\b', 'sand'), (r'\bgrava\b', 'gravel'),
        (r'\bexcavación\b', 'excavation'), (r'\brelleno\b', 'backfill'),
        (r'\barmadura\b', 'reinforcement'), (r'\brefuerzo\b', 'reinforcement'),
        # Surfaces and volumes
        (r'\bsuperficie\b', 'area'), (r'\bvolumen\b', 'volume'),
        (r'\baltura\b', 'height'), (r'\blongitud\b', 'length'),
        (r'\bancho\b', 'width'), (r'\bprofundidad\b', 'depth'),
        (r'\bespesor\b', 'thickness'), (r'\bdiámetro\b', 'diameter'),
        (r'\bperímetro\b', 'perimeter'), (r'\bradio\b', 'radius'),
        (r'\bcanto\b', 'depth'),
        # Plumbing
        (r'\btubería\b', 'pipe'), (r'\btuberia\b', 'pipe'),
        (r'\bcaudal\b', 'flow rate'), (r'\bpresión\b', 'pressure'),
        (r'\bpresion\b', 'pressure'), (r'\bdepósito\b', 'tank'),
        (r'\bcalentador\b', 'water heater'), (r'\bcaldera\b', 'boiler'),
        (r'\bradiador\b', 'radiator'), (r'\bsuelo\b', 'floor'),
        (r'\btecho\b', 'ceiling'), (r'\bpared\b', 'wall'),
        (r'\bagua\b', 'water'), (r'\bdesagüe\b', 'drain'),
        (r'\bventilación\b', 'ventilation'), (r'\bconducto\b', 'duct'),
        (r'\bagua caliente\b', 'hot water'), (r'\bagua fría\b', 'cold water'),
        # Electrical
        (r'\btensión\b', 'voltage'), (r'\btension\b', 'voltage'),
        (r'\bcorriente\b', 'current'), (r'\bpotencia\b', 'power'),
        (r'\bcable\b', 'cable'), (r'\bsección\b', 'cross-section'),
        (r'\bseccion\b', 'cross-section'), (r'\bpotencia\b', 'power'),
        (r'\beléctrico\b', 'electrical'), (r'\beléctrica\b', 'electrical'),
        (r'\btrifásica\b', 'three-phase'), (r'\btrifásico\b', 'three-phase'),
        (r'\bmonofásica\b', 'single-phase'), (r'\bmagnético\b', 'magnetic'),
        (r'\btérmico\b', 'thermal'), (r'\btérmica\b', 'thermal'),
        (r'\binstalación\b', 'installation'),
        # Other
        (r'\bmedidas\b', 'measurements'), (r'\bresultado\b', 'result'),
        (r'\bresultados\b', 'results'), (r'\bcálculo\b', 'calculation'),
        (r'\bcalcular\b', 'calculate'), (r'\bcalculadora\b', 'calculator'),
        (r'\bfórmula\b', 'formula'), (r'\bvalor\b', 'value'),
        (r'\bvalores\b', 'values'), (r'\btotal\b', 'total'),
        (r'\bdatos\b', 'data'), (r'\bunidad\b', 'unit'),
        (r'\bunidades\b', 'units'), (r'\bcantidad\b', 'quantity'),
        (r'\bNúmero\b', 'Number'), (r'\bnúmero\b', 'number'),
        (r'\bPaso\b', 'Step'), (r'\bpaso\b', 'step'),
        (r'\bIntroduce\b', 'Enter'), (r'\bintroduce\b', 'enter'),
        (r'\bCalcular\b', 'Calculate'), (r'\bObtener\b', 'Get'),
        (r'\bobtener\b', 'get'), (r'\bPulsa\b', 'Press'),
        (r'\bUtiliza\b', 'Use'), (r'\butiliza\b', 'use'),
        (r'\bnecesario\b', 'required'), (r'\bnecesarios\b', 'required'),
        (r'\bespera\b', 'wait'), (r'\bespera\b', 'standby'),
        (r'\bportante\b', 'bearing'), (r'\blimpieza\b', 'cleaning'),
        (r'\bsolado\b', 'blinding'), (r'\bseparación\b', 'spacing'),
        (r'\bdistancia\b', 'distance'), (r'\bsujeción\b', 'fixing'),
    ]
    
    result = text
    for pattern, replacement in replacements:
        try:
            import re
            result = re.sub(pattern, replacement, result)
        except:
            pass
    
    # Clean up double spaces and fix common artifacts
    result = result.replace('  ', ' ').strip()
    
    return result


# ===== FRENCH FIX =====
def fix_french(ld, es, slug, cid, data):
    """Fix French translation block."""
    calc_name_es = es.get('name', '')
    ld['name'] = calc_name_es.replace('Calculadora de', 'Calculateur de').replace('Calculadora', 'Calculateur').replace('Cálculo de', 'Calcul de').replace('Cálculo', 'Calcul')
    
    ld['description'] = clean_french(es.get('description', ''))
    ld['example_label'] = clean_french(es.get('example_label', ''))
    ld['result_context'] = clean_french(es.get('result_context', ''))
    ld['steps'] = [clean_french(s) for s in es.get('steps', [])]
    ld['mistakes'] = [clean_french(m) for m in es.get('mistakes', [])]
    ld['seo_description'] = clean_french(es.get('seo_description', ''))[:157].rstrip()
    
    if 'inputs' in ld:
        for k in ld['inputs']:
            if 'inputs' in es:
                ld['inputs'][k] = clean_french(es['inputs'].get(k, k))
    if 'outputs' in ld:
        for k in ld['outputs']:
            if 'outputs' in es:
                ld['outputs'][k] = clean_french(es['outputs'].get(k, k))
    
    if 'range_hints' in ld:
        for k in ld['range_hints']:
            if k in es.get('range_hints', {}):
                ld['range_hints'][k] = clean_french(es['range_hints'][k])
    
    # Truncate SEO
    if len(ld.get('seo_title', '')) > 60:
        ld['seo_title'] = ld['seo_title'][:57].rstrip() + '...'
    
    return ld


def clean_french(text):
    """Convert Spanish text to French."""
    if not text:
        return text
    
    replacements = [
        # Connectors
        (r'\bdel\b', 'du'), (r'\by\b', 'et'), (r'\bo\b', 'ou'),
        (r'\bpara\b', 'pour'), (r'\bpor\b', 'par'),
        (r'\bcon\b', 'avec'), (r'\bentre\b', 'entre'),
        (r'\bsegún\b', 'selon'), (r'\bsin\b', 'sans'),
        (r'\bsobre\b', 'sur'), (r'\bdesde\b', 'depuis'),
        (r'\bcada\b', 'chaque'), (r'\bCada\b', 'Chaque'),
        # Metrics
        (r'\bmetros\b', 'mètres'), (r'\bmetro\b', 'mètre'),
        (r'\bcuadrado\b', 'carré'), (r'\bcúbico\b', 'cube'),
        (r'\bsacos\b', 'sacs'), (r'\blitros\b', 'litres'),
        (r'\bhoras\b', 'heures'), (r'\bdías\b', 'jours'),
        (r'\bmeses\b', 'mois'), (r'\baños\b', 'ans'),
        # Construction
        (r'\bhormigón\b', 'béton'), (r'\bmortero\b', 'mortier'),
        (r'\blosa\b', 'dalle'), (r'\bzapata\b', 'semelle'),
        (r'\bzapatas\b', 'semelles'), (r'\bviga\b', 'poutre'),
        (r'\bvigas\b', 'poutres'), (r'\bpilar\b', 'poteau'),
        (r'\bpilares\b', 'poteaux'), (r'\bmuro\b', 'mur'),
        (r'\bcimiento\b', 'fondation'), (r'\bladrillo\b', 'brique'),
        (r'\bladrillos\b', 'briques'), (r'\bencofrado\b', 'coffrage'),
        (r'\bacero\b', 'acier'), (r'\bcemento\b', 'ciment'),
        (r'\barena\b', 'sable'), (r'\bgrava\b', 'gravier'),
        (r'\bexcavación\b', 'excavation'), (r'\brefuerzo\b', 'renfort'),
        (r'\barmadura\b', 'armature'),
        # Surfaces
        (r'\bsuperficie\b', 'surface'), (r'\bvolumen\b', 'volume'),
        (r'\baltura\b', 'hauteur'), (r'\blongitud\b', 'longueur'),
        (r'\bancho\b', 'largeur'), (r'\bprofundidad\b', 'profondeur'),
        (r'\bespesor\b', 'épaisseur'), (r'\bdiámetro\b', 'diamètre'),
        (r'\bperímetro\b', 'périmètre'), (r'\bradio\b', 'rayon'),
        (r'\bcanto\b', 'hauteur'),
        # Plumbing
        (r'\btubería\b', 'tuyau'), (r'\btuberia\b', 'tuyau'),
        (r'\bcaudal\b', 'débit'), (r'\bpresión\b', 'pression'),
        (r'\bcalentador\b', 'chauffe-eau'), (r'\bcaldera\b', 'chaudière'),
        (r'\bradiador\b', 'radiateur'), (r'\bconducto\b', 'conduit'),
        (r'\baislamiento\b', 'isolation'),
        # Electrical
        (r'\btensión\b', 'tension'), (r'\bcorriente\b', 'courant'),
        (r'\bpotencia\b', 'puissance'), (r'\beléctrico\b', 'électrique'),
        (r'\beléctrica\b', 'électrique'), (r'\btrifásica\b', 'triphasé'),
        (r'\bmonofásica\b', 'monophasé'), (r'\btérmica\b', 'thermique'),
        (r'\btérmico\b', 'thermique'), (r'\binstalación\b', 'installation'),
        # General
        (r'\bmedidas\b', 'mesures'), (r'\bresultado\b', 'résultat'),
        (r'\bcálculo\b', 'calcul'), (r'\bcalcular\b', 'calculer'),
        (r'\bcalculadora\b', 'calculatrice'), (r'\bfórmula\b', 'formule'),
        (r'\bvalor\b', 'valeur'), (r'\bvalores\b', 'valeurs'),
        (r'\btotal\b', 'total'), (r'\bunidad\b', 'unité'),
        (r'\bunidades\b', 'unités'), (r'\bcantidad\b', 'quantité'),
        (r'\bNúmero\b', 'Nombre'), (r'\bnúmero\b', 'nombre'),
        (r'\bIntroduce\b', 'Saisissez'), (r'\bintroduce\b', 'saisissez'),
        (r'\bCalcular\b', 'Calculer'), (r'\bcalcular\b', 'calculer'),
        (r'\bObtener\b', 'Obtenir'), (r'\bobtener\b', 'obtenir'),
        (r'\bPulsa\b', 'Appuyez'), (r'\bUtiliza\b', 'Utilisez'),
        (r'\bnecesario\b', 'nécessaire'), (r'\bdatos\b', 'données'),
        (r'\bpeso\b', 'poids'), (r'\bagua\b', 'eau'),
    ]
    
    result = text
    import re
    for pattern, replacement in replacements:
        try:
            result = re.sub(pattern, replacement, result)
        except:
            pass
    
    result = result.replace('  ', ' ').strip()
    return result


# ===== GERMAN FIX =====
def fix_german(ld, es, slug, cid, data):
    """Fix German translation block."""
    calc_name_es = es.get('name', '')
    ld['name'] = calc_name_es.replace('Calculadora de', 'Rechner für').replace('Calculadora', 'Rechner').replace('Cálculo de', 'Berechnung von').replace('Cálculo', 'Berechnung')
    
    ld['description'] = clean_german(es.get('description', ''))
    ld['example_label'] = clean_german(es.get('example_label', ''))
    ld['result_context'] = clean_german(es.get('result_context', ''))
    ld['steps'] = [clean_german(s) for s in es.get('steps', [])]
    ld['mistakes'] = [clean_german(m) for m in es.get('mistakes', [])]
    ld['seo_description'] = clean_german(es.get('seo_description', ''))[:157].rstrip()
    
    if 'inputs' in ld:
        for k in ld['inputs']:
            if 'inputs' in es:
                ld['inputs'][k] = clean_german(es['inputs'].get(k, k))
    if 'outputs' in ld:
        for k in ld['outputs']:
            if 'outputs' in es:
                ld['outputs'][k] = clean_german(es['outputs'].get(k, k))
    
    if 'range_hints' in ld:
        for k in ld['range_hints']:
            if k in es.get('range_hints', {}):
                ld['range_hints'][k] = clean_german(es['range_hints'][k])
    
    # Truncate SEO
    if len(ld.get('seo_title', '')) > 60:
        ld['seo_title'] = ld['seo_title'][:57].rstrip() + '...'
    
    return ld


def clean_german(text):
    """Convert Spanish text to German."""
    if not text:
        return text
    
    replacements = [
        (r'\bdel\b', 'vom'), (r'\by\b', 'und'), (r'\bo\b', 'oder'),
        (r'\bpara\b', 'für'), (r'\bpor\b', 'pro'),
        (r'\bcon\b', 'mit'), (r'\bentre\b', 'zwischen'),
        (r'\bsegún\b', 'nach'), (r'\bsin\b', 'ohne'),
        (r'\bsobre\b', 'über'), (r'\bdesde\b', 'ab'),
        (r'\bcada\b', 'jeder'), (r'\bCada\b', 'Jeder'),
        # Metrics
        (r'\bmetros\b', 'Meter'), (r'\bmetro\b', 'Meter'),
        (r'\bcuadrado\b', 'Quadrat-'), (r'\bcúbico\b', 'Kubik-'),
        (r'\bsacos\b', 'Säcke'), (r'\blitros\b', 'Liter'),
        (r'\bhoras\b', 'Stunden'), (r'\bdías\b', 'Tage'),
        (r'\bmeses\b', 'Monate'), (r'\baños\b', 'Jahre'),
        # Construction
        (r'\bhormigón\b', 'Beton'), (r'\bmortero\b', 'Mörtel'),
        (r'\blosa\b', 'Platte'), (r'\bzapata\b', 'Fundament'),
        (r'\bzapatas\b', 'Fundamente'), (r'\bviga\b', 'Balken'),
        (r'\bvigas\b', 'Balken'), (r'\bpilar\b', 'Stütze'),
        (r'\bpilares\b', 'Stützen'), (r'\bmuro\b', 'Wand'),
        (r'\bcimiento\b', 'Fundament'), (r'\bladrillo\b', 'Ziegel'),
        (r'\bladrillos\b', 'Ziegel'), (r'\bencofrado\b', 'Schalung'),
        (r'\bacero\b', 'Stahl'), (r'\bcemento\b', 'Zement'),
        (r'\barena\b', 'Sand'), (r'\bgrava\b', 'Kies'),
        (r'\bexcavación\b', 'Aushub'), (r'\brefuerzo\b', 'Bewehrung'),
        (r'\barmadura\b', 'Bewehrung'),
        # Surfaces
        (r'\bsuperficie\b', 'Fläche'), (r'\bvolumen\b', 'Volumen'),
        (r'\baltura\b', 'Höhe'), (r'\blongitud\b', 'Länge'),
        (r'\bancho\b', 'Breite'), (r'\bprofundidad\b', 'Tiefe'),
        (r'\bespesor\b', 'Dicke'), (r'\bdiámetro\b', 'Durchmesser'),
        (r'\bperímetro\b', 'Umfang'), (r'\bradio\b', 'Radius'),
        (r'\bcanto\b', 'Höhe'),
        # Plumbing
        (r'\btubería\b', 'Rohr'), (r'\btuberia\b', 'Rohr'),
        (r'\bcaudal\b', 'Durchfluss'), (r'\bpresión\b', 'Druck'),
        (r'\bcalentador\b', 'Warmwasserbereiter'),
        (r'\bcaldera\b', 'Heizkessel'), (r'\bradiador\b', 'Heizkörper'),
        (r'\bconducto\b', 'Kanal'), (r'\baislamiento\b', 'Dämmung'),
        # Electrical
        (r'\btensión\b', 'Spannung'), (r'\bcorriente\b', 'Strom'),
        (r'\bpotencia\b', 'Leistung'), (r'\beléctrico\b', 'elektrisch'),
        (r'\beléctrica\b', 'elektrisch'), (r'\btrifásica\b', 'Drehstrom'),
        (r'\bmonofásica\b', 'Einphasen-'), (r'\btérmica\b', 'thermisch'),
        (r'\btérmico\b', 'thermisch'), (r'\binstalación\b', 'Installation'),
        # General
        (r'\bmedidas\b', 'Maße'), (r'\bresultado\b', 'Ergebnis'),
        (r'\bcálculo\b', 'Berechnung'), (r'\bcalcular\b', 'berechnen'),
        (r'\bcalculadora\b', 'Rechner'), (r'\bfórmula\b', 'Formel'),
        (r'\bvalor\b', 'Wert'), (r'\bvalores\b', 'Werte'),
        (r'\btotal\b', 'Gesamt'), (r'\bunidad\b', 'Einheit'),
        (r'\bunidades\b', 'Einheiten'), (r'\bcantidad\b', 'Menge'),
        (r'\bNúmero\b', 'Anzahl'), (r'\bnúmero\b', 'Anzahl'),
        (r'\bIntroduce\b', 'Geben Sie'), (r'\bintroduce\b', 'geben Sie'),
        (r'\bCalcular\b', 'Berechnen'), (r'\bcalcular\b', 'berechnen'),
        (r'\bObtener\b', 'Erhalten'), (r'\bobtener\b', 'erhalten'),
        (r'\bPulsa\b', 'Klicken'), (r'\bUtiliza\b', 'Verwenden'),
        (r'\bnecesario\b', 'erforderlich'), (r'\bdatos\b', 'Daten'),
        (r'\bpeso\b', 'Gewicht'), (r'\bagua\b', 'Wasser'),
    ]
    
    result = text
    import re
    for pattern, replacement in replacements:
        try:
            result = re.sub(pattern, replacement, result)
        except:
            pass
    
    result = result.replace('  ', ' ').strip()
    return result


# ===== ITALIAN FIX =====
def fix_italian(ld, es, slug, cid, data):
    """Fix Italian translation block."""
    calc_name_es = es.get('name', '')
    ld['name'] = calc_name_es.replace('Calculadora de', 'Calcolatore per').replace('Calculadora', 'Calcolatore').replace('Cálculo de', 'Calcolo di').replace('Cálculo', 'Calcolo')
    
    ld['description'] = clean_italian(es.get('description', ''))
    ld['example_label'] = clean_italian(es.get('example_label', ''))
    ld['result_context'] = clean_italian(es.get('result_context', ''))
    ld['steps'] = [clean_italian(s) for s in es.get('steps', [])]
    ld['mistakes'] = [clean_italian(m) for m in es.get('mistakes', [])]
    ld['seo_description'] = clean_italian(es.get('seo_description', ''))[:157].rstrip()
    
    if 'inputs' in ld:
        for k in ld['inputs']:
            if 'inputs' in es:
                ld['inputs'][k] = clean_italian(es['inputs'].get(k, k))
    if 'outputs' in ld:
        for k in ld['outputs']:
            if 'outputs' in es:
                ld['outputs'][k] = clean_italian(es['outputs'].get(k, k))
    
    if 'range_hints' in ld:
        for k in ld['range_hints']:
            if k in es.get('range_hints', {}):
                ld['range_hints'][k] = clean_italian(es['range_hints'][k])
    
    # Truncate SEO
    if len(ld.get('seo_title', '')) > 60:
        ld['seo_title'] = ld['seo_title'][:57].rstrip() + '...'
    
    return ld


def clean_italian(text):
    """Convert Spanish text to Italian."""
    if not text:
        return text
    
    replacements = [
        (r'\bdel\b', 'del'), (r'\by\b', 'e'), (r'\bo\b', 'o'),
        (r'\bpara\b', 'per'), (r'\bpor\b', 'per'),
        (r'\bcon\b', 'con'), (r'\bentre\b', 'tra'),
        (r'\bsegún\b', 'secondo'), (r'\bsin\b', 'senza'),
        (r'\bsobre\b', 'su'), (r'\bdesde\b', 'da'),
        (r'\bcada\b', 'ogni'), (r'\bCada\b', 'Ogni'),
        # Metrics
        (r'\bmetros\b', 'metri'), (r'\bmetro\b', 'metro'),
        (r'\bcuadrado\b', 'quadrato'), (r'\bcúbico\b', 'cubo'),
        (r'\bsacos\b', 'sacchi'), (r'\blitros\b', 'litri'),
        (r'\bhoras\b', 'ore'), (r'\bdías\b', 'giorni'),
        (r'\bmeses\b', 'mesi'), (r'\baños\b', 'anni'),
        # Construction
        (r'\bhormigón\b', 'calcestruzzo'), (r'\bmortero\b', 'malta'),
        (r'\blosa\b', 'soletta'), (r'\bzapata\b', 'plinto'),
        (r'\bzapatas\b', 'plinti'), (r'\bviga\b', 'trave'),
        (r'\bvigas\b', 'travi'), (r'\bpilar\b', 'pilastro'),
        (r'\bpilares\b', 'pilastri'), (r'\bmuro\b', 'muro'),
        (r'\bcimiento\b', 'fondazione'), (r'\bladrillo\b', 'mattone'),
        (r'\bladrillos\b', 'mattoni'), (r'\bencofrado\b', 'cassaforma'),
        (r'\bacero\b', 'acciaio'), (r'\bcemento\b', 'cemento'),
        (r'\barena\b', 'sabbia'), (r'\bgrava\b', 'ghiaia'),
        (r'\bexcavación\b', 'scavo'), (r'\brefuerzo\b', 'rinforzo'),
        (r'\barmadura\b', 'armatura'),
        # Surfaces
        (r'\bsuperficie\b', 'superficie'), (r'\bvolumen\b', 'volume'),
        (r'\baltura\b', 'altezza'), (r'\blongitud\b', 'lunghezza'),
        (r'\bancho\b', 'larghezza'), (r'\bprofundidad\b', 'profondità'),
        (r'\bespesor\b', 'spessore'), (r'\bdiámetro\b', 'diametro'),
        (r'\bperímetro\b', 'perimetro'), (r'\bradio\b', 'raggio'),
        (r'\bcanto\b', 'altezza'),
        # Plumbing
        (r'\btubería\b', 'tubo'), (r'\btuberia\b', 'tubo'),
        (r'\bcaudal\b', 'portata'), (r'\bpresión\b', 'pressione'),
        (r'\bcalentador\b', 'scaldabagno'), (r'\bcaldera\b', 'caldaia'),
        (r'\bradiador\b', 'radiatore'), (r'\bconducto\b', 'condotto'),
        (r'\baislamiento\b', 'isolamento'),
        # Electrical
        (r'\btensión\b', 'tensione'), (r'\bcorriente\b', 'corrente'),
        (r'\bpotencia\b', 'potenza'), (r'\beléctrico\b', 'elettrico'),
        (r'\beléctrica\b', 'elettrica'), (r'\btrifásica\b', 'trifase'),
        (r'\bmonofásica\b', 'monofase'), (r'\btérmica\b', 'termica'),
        (r'\btérmico\b', 'termico'), (r'\binstalación\b', 'installazione'),
        # General
        (r'\bmedidas\b', 'misure'), (r'\bresultado\b', 'risultato'),
        (r'\bcálculo\b', 'calcolo'), (r'\bcalcular\b', 'calcolare'),
        (r'\bcalculadora\b', 'calcolatore'), (r'\bfórmula\b', 'formula'),
        (r'\bvalor\b', 'valore'), (r'\bvalores\b', 'valori'),
        (r'\btotal\b', 'totale'), (r'\bunidad\b', 'unità'),
        (r'\bunidades\b', 'unità'), (r'\bcantidad\b', 'quantità'),
        (r'\bNúmero\b', 'Numero'), (r'\bnúmero\b', 'numero'),
        (r'\bIntroduce\b', 'Inserisci'), (r'\bintroduce\b', 'inserisci'),
        (r'\bCalcular\b', 'Calcolare'), (r'\bcalcular\b', 'calcolare'),
        (r'\bObtener\b', 'Ottenere'), (r'\bobtener\b', 'ottenere'),
        (r'\bPulsa\b', 'Premere'), (r'\bUtiliza\b', 'Utilizza'),
        (r'\bnecesario\b', 'necessario'), (r'\bdatos\b', 'dati'),
        (r'\bpeso\b', 'peso'), (r'\bagua\b', 'acqua'),
    ]
    
    result = text
    import re
    for pattern, replacement in replacements:
        try:
            result = re.sub(pattern, replacement, result)
        except:
            pass
    
    result = result.replace('  ', ' ').strip()
    return result


# ===== PORTUGUESE FIX =====
def fix_portuguese(ld, es, slug):
    """Fix Portuguese - mostly just cleanup from Spanish, many words are same."""
    # Portuguese is close to Spanish, but some words differ
    replacements = [
        (r'\bhormigón\b', 'betão'), (r'\bhormigon\b', 'betão'),
        (r'\bcalcular\b', 'calcular'), (r'\bcálculo\b', 'cálculo'),
        (r'\bdesde\b', 'desde'), (r'\bhasta\b', 'até'),
        (r'\bsin\b', 'sem'),
        (r'\bcuadrado\b', 'quadrado'), (r'\bcúbico\b', 'cúbico'),
        (r'\bacero\b', 'aço'),
        (r'\beléctrico\b', 'elétrico'), (r'\beléctrica\b', 'elétrica'),
        (r'\btensión\b', 'tensão'),
    ]
    
    for field in ['description', 'example_label', 'result_context', 'seo_description']:
        if field in ld:
            text = ld[field]
            for old, new in replacements:
                try:
                    import re
                    text = re.sub(old, new, text)
                except:
                    pass
            ld[field] = text
    
    if 'steps' in ld:
        ld['steps'] = [s.replace('hormigón', 'betão') for s in ld['steps']]
    
    if 'mistakes' in ld:
        ld['mistakes'] = [m.replace('hormigón', 'betão') for m in ld['mistakes']]
    
    # Truncate SEO
    if len(ld.get('seo_title', '')) > 60:
        ld['seo_title'] = ld['seo_title'][:57].rstrip() + '...'
    
    return ld


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
            
            new_i18n = get_translations(cid, data['slug'], data)
            data['i18n'] = new_i18n
            
            with open(f, 'w', encoding='utf-8') as fh:
                json.dump(data, fh, ensure_ascii=False, indent=2)
            
            fixed += 1
            print(f'Translated: {cid:03d} {data["slug"]}')
        except Exception as e:
            import traceback
            print(f'Error {f}: {e}')
            traceback.print_exc()
    
    print(f'\nTotal translated: {fixed}')

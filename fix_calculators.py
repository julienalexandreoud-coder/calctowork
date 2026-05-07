import json, os, glob, re, copy

CALC_DIR = r'C:\Microsaas\obra\src\calculators'
LANGS = ['es', 'en', 'fr', 'pt', 'de', 'it']

# Maps for common Spanish -> target language words
# These are conservative - only replace clear Spanish words in non-Spanish contexts
SPANISH_TO_EN = {
    '\bde\b': 'of', '\bdel\b': 'of the', '\bla\b': 'the', '\bel\b': 'the',
    '\blos\b': 'the', '\blas\b': 'the', '\bun\b': 'a', '\buna\b': 'a',
    '\by\b': 'and', '\bcon\b': 'with', '\bpara\b': 'for', '\bpor\b': 'per',
    '\ben\b': 'in', '\bque\b': 'that', '\bes\b': 'is', '\bson\b': 'are',
    '\bcomo\b': 'as', '\bmás\b': 'more', '\beste\b': 'this', '\besta\b': 'this',
    '\bdesde\b': 'from', '\bhasta\b': 'to', '\bentre\b': 'between', '\bsegún\b': 'according to',
    '\bsin\b': 'without', '\bsobre\b': 'over', '\bcada\b': 'each', '\bo\b': 'or',
    '\bse\b': 'is', '\bsu\b': 'its',
    '\bcálculo\b': 'calculation', '\bcalcular\b': 'calculate',
    '\bresultado\b': 'result', '\bresultados\b': 'results',
    '\bvalor\b': 'value', '\bvalores\b': 'values',
    '\bintroduce\b': 'enter', '\bintroducir\b': 'enter',
    '\bobtener\b': 'obtain', '\bpulsa\b': 'press', '\bcalculo\b': 'calculation',
    '\bpotencia\b': 'power', '\btensión\b': 'voltage', '\btension\b': 'voltage',
    '\bcorriente\b': 'current', '\bcalculadora\b': 'calculator',
    '\butil\b': 'useful', '\beléctrico\b': 'electrical',
    '\beléctrica\b': 'electrical', '\btérmica\b': 'thermal',
    '\btérmico\b': 'thermal', '\bdimensionar\b': 'size',
    '\bdimensionado\b': 'sizing', '\bconsumo\b': 'consumption',
    '\brendimiento\b': 'performance', '\beficiencia\b': 'efficiency',
    '\bsección\b': 'cross-section', '\bseccion\b': 'cross-section',
    '\bcable\b': 'cable', '\btubería\b': 'pipe', '\btuberia\b': 'pipe',
    '\binstalación\b': 'installation', '\binstalacion\b': 'installation',
    '\bvivienda\b': 'home', '\bpresión\b': 'pressure', '\bpresion\b': 'pressure',
    '\btemperatura\b': 'temperature', '\bvolumen\b': 'volume',
    '\bsuperficie\b': 'surface', '\baltura\b': 'height',
    '\bfrente\b': 'against', '\bresistencia\b': 'resistance',
    '\benergética\b': 'energy', '\benergético\b': 'energy',
    '\bclase\b': 'class', '\bclasificar\b': 'classify',
    '\bmodo\b': 'mode', '\bcalor\b': 'heat', '\bfrío\b': 'cooling',
    '\bestacional\b': 'seasonal', '\bnominal\b': 'nominal',
    '\bcarga\b': 'load', '\bmáxima\b': 'maximum', '\bmaxima\b': 'maximum',
    '\banual\b': 'annual', '\bcatálogo\b': 'catalog',
    '\bensayo\b': 'test', '\bcondiciones\b': 'conditions',
    '\breal\b': 'real', '\binferior\b': 'lower',
    '\bconfundir\b': 'confuse', '\busar\b': 'use',
    '\bignorar\b': 'ignore', '\bverificar\b': 'verify',
    '\bdato\b': 'data', '\bdatos\b': 'data',
    '\bhora\b': 'hour', '\bhoras\b': 'hours', '\bdía\b': 'day', '\bdías\b': 'days',
    '\bformula\b': 'formula', '\bunidad\b': 'unit', '\bunidades\b': 'units',
    '\bcalcular\b': 'calculate', '\bcalcula\b': 'calculates',
    '\bcaudal\b': 'flow rate', '\bdiametro\b': 'diameter',
    '\burgencia\b': 'urgency', '\bemergencia\b': 'emergency',
    '\bcalefacción\b': 'heating', '\brefrigeración\b': 'cooling',
    '\bsuelo\b': 'floor', '\btecho\b': 'ceiling',
    '\bpared\b': 'wall', '\bparedes\b': 'walls',
    '\bpuerta\b': 'door', '\bventana\b': 'window',
    '\bcerámico\b': 'ceramic', '\bazulejo\b': 'tile',
    '\bcemento\b': 'cement', '\bhormigón\b': 'concrete', '\bhormigon\b': 'concrete',
    '\bladrillo\b': 'brick', '\bladrillos\b': 'bricks',
    '\bmortero\b': 'mortar', '\bencofrado\b': 'formwork',
    '\bacero\b': 'steel', '\barmadura\b': 'reinforcement',
    '\bzapata\b': 'footing', '\bpilar\b': 'pillar', '\bpilares\b': 'pillars',
    '\bviga\b': 'beam', '\bvigas\b': 'beams',
    '\blosa\b': 'slab', '\bforjado\b': 'slab',
    '\bmuro\b': 'wall', '\bcimiento\b': 'foundation',
    '\bagua\b': 'water', '\bdepósito\b': 'tank',
    '\bpeso\b': 'weight', '\blongitud\b': 'length',
    '\bancho\b': 'width', '\bradio\b': 'radius',
    '\bdiámetro\b': 'diameter', '\bespesor\b': 'thickness',
    '\bgravedad\b': 'gravity', '\bvelocidad\b': 'speed',
    '\bdistancia\b': 'distance', '\bfuerza\b': 'force',
}

SPANISH_TO_FR = {
    '\bde\b': 'de', '\bdel\b': 'du', '\bla\b': 'la', '\bel\b': 'le',
    '\blos\b': 'les', '\blas\b': 'les', '\bun\b': 'un', '\buna\b': 'une',
    '\by\b': 'et', '\bcon\b': 'avec', '\bpara\b': 'pour', '\bpor\b': 'par',
    '\ben\b': 'en', '\bque\b': 'que', '\bes\b': 'est', '\bson\b': 'sont',
    '\bcomo\b': 'comme', '\bmás\b': 'plus',
    '\bdesde\b': 'depuis', '\bhasta\b': 'jusqu\'à', '\bentre\b': 'entre',
    '\bsin\b': 'sans', '\bsobre\b': 'sur', '\bcada\b': 'chaque', '\bo\b': 'ou',
    '\bse\b': 'se', '\bsu\b': 'son',
    '\bcálculo\b': 'calcul', '\bcalcular\b': 'calculer', '\bcalculo\b': 'calcul',
    '\bresultado\b': 'résultat', '\bresultados\b': 'résultats',
    '\bvalor\b': 'valeur', '\bvalores\b': 'valeurs',
    '\bintroduce\b': 'saisissez', '\bintroducir\b': 'saisir',
    '\bobtener\b': 'obtenir', '\bpulsa\b': 'appuyez',
    '\bformula\b': 'formule',
    '\bcalculadora\b': 'calculatrice',
    '\bpotencia\b': 'puissance', '\btensión\b': 'tension',
    '\bcorriente\b': 'courant', '\butil\b': 'utile',
    '\beléctrico\b': 'électrique', '\beléctrica\b': 'électrique',
    '\btérmica\b': 'thermique', '\bconsumo\b': 'consommation',
    '\brendimiento\b': 'rendement', '\beficiencia\b': 'efficacité',
    '\bcable\b': 'câble', '\btubería\b': 'tuyau', '\btuberia\b': 'tuyau',
    '\binstalación\b': 'installation',
    '\bpresión\b': 'pression', '\bpresion\b': 'pression',
    '\btemperatura\b': 'température', '\bvolumen\b': 'volume',
    '\bsuperficie\b': 'surface', '\baltura\b': 'hauteur',
    '\bfrente\b': 'contre', '\bresistencia\b': 'résistance',
    '\benergética\b': 'énergétique',
    '\bclase\b': 'classe', '\bclasificar\b': 'classer',
    '\bmodo\b': 'mode', '\bcalor\b': 'chaleur',
    '\bestacional\b': 'saisonnier', '\bnominal\b': 'nominal',
    '\bcarga\b': 'charge', '\bmáxima\b': 'maximale', '\bmaxima\b': 'maximale',
    '\banual\b': 'annuel', '\bcatálogo\b': 'catalogue',
    '\bensayo\b': 'essai', '\bcondiciones\b': 'conditions',
    '\breal\b': 'réel', '\binferior\b': 'inférieur',
    '\bconfundir\b': 'confondre', '\busar\b': 'utiliser',
    '\bignorar\b': 'ignorer', '\bverificar\b': 'vérifier',
    '\busados\b': 'utilisé', '\bdatos\b': 'données',
    '\bhora\b': 'heure', '\bhoras\b': 'heures',
    '\bdimensionar\b': 'dimensionner',
    '\bunidad\b': 'unité', '\bunidades\b': 'unités',
    '\baire\b': 'air', '\bcalefacción\b': 'chauffage',
    '\brefrigeración\b': 'refroidissement',
}

SPANISH_TO_DE = {
    '\bde\b': 'von', '\bdel\b': 'vom', '\bla\b': 'die', '\bel\b': 'der',
    '\blos\b': 'die', '\blas\b': 'die', '\bun\b': 'ein', '\buna\b': 'eine',
    '\by\b': 'und', '\bcon\b': 'mit', '\bpara\b': 'für', '\bpor\b': 'pro',
    '\ben\b': 'in', '\bque\b': 'dass', '\bes\b': 'ist', '\bson\b': 'sind',
    '\bcomo\b': 'wie', '\bmás\b': 'mehr',
    '\bdesde\b': 'ab', '\bhasta\b': 'bis', '\bentre\b': 'zwischen',
    '\bsin\b': 'ohne', '\bsobre\b': 'über', '\bcada\b': 'jeder', '\bo\b': 'oder',
    '\bse\b': 'wird', '\bsu\b': 'seine',
    '\bcálculo\b': 'Berechnung', '\bcalcular\b': 'berechnen', '\bcalculo\b': 'Berechnung',
    '\bresultado\b': 'Ergebnis', '\bresultados\b': 'Ergebnisse',
    '\bvalor\b': 'Wert', '\bvalores\b': 'Werte',
    '\bintroduce\b': 'Geben Sie', '\bintroducir\b': 'eingeben',
    '\bobtener\b': 'erhalten', '\bpulsa\b': 'Klicken Sie',
    '\bpotencia\b': 'Leistung', '\btensión\b': 'Spannung',
    '\bcorriente\b': 'Strom', '\bcalculadora\b': 'Rechner',
    '\butil\b': 'Nutz-', '\beléctrico\b': 'elektrisch',
    '\beléctrica\b': 'elektrisch', '\btérmica\b': 'thermisch',
    '\btérmico\b': 'thermisch', '\bdimensionar\b': 'dimensionieren',
    '\bdimensionado\b': 'Dimensionierung', '\bconsumo\b': 'Verbrauch',
    '\brendimiento\b': 'Leistung', '\beficiencia\b': 'Effizienz',
    '\bsección\b': 'Querschnitt', '\bseccion\b': 'Querschnitt',
    '\bcable\b': 'Kabel', '\btubería\b': 'Rohr', '\btuberia\b': 'Rohr',
    '\binstalación\b': 'Installation', '\binstalacion\b': 'Installation',
    '\bvivienda\b': 'Wohnung', '\bpresión\b': 'Druck',
    '\btemperatura\b': 'Temperatur', '\bvolumen\b': 'Volumen',
    '\bsuperficie\b': 'Fläche', '\baltura\b': 'Höhe',
    '\bfrente\b': 'gegen', '\bresistencia\b': 'Widerstand',
    '\benergética\b': 'Energie', '\benergético\b': 'Energie',
    '\bclase\b': 'Klasse', '\bclasificar\b': 'klassifizieren',
    '\bmodo\b': 'Modus', '\bcalor\b': 'Wärme',
    '\bfrío\b': 'Kälte', '\bestacional\b': 'saisonal',
    '\bnominal\b': 'Nenn-', '\bcarga\b': 'Last',
    '\bmáxima\b': 'maximal', '\bmaxima\b': 'maximal',
    '\banual\b': 'jährlich', '\bcatálogo\b': 'Katalog',
    '\bensayo\b': 'Test', '\bcondiciones\b': 'Bedingungen',
    '\breal\b': 'real', '\binferior\b': 'niedriger',
    '\bconfundir\b': 'verwechseln', '\busar\b': 'verwenden',
    '\bignorar\b': 'ignorieren', '\bverificar\b': 'überprüfen',
    '\busados\b': 'verwendet', '\bdatos\b': 'Daten',
    '\bhora\b': 'Stunde', '\bhoras\b': 'Stunden', '\bdía\b': 'Tag',
    '\bdías\b': 'Tage', '\bformula\b': 'Formel',
    '\bunidad\b': 'Einheit', '\bunidades\b': 'Einheiten',
}

SPANISH_TO_IT = {
    '\bde\b': 'di', '\bdel\b': 'del', '\bla\b': 'la', '\bel\b': 'il',
    '\blos\b': 'i', '\blas\b': 'le', '\bun\b': 'un', '\buna\b': 'una',
    '\by\b': 'e', '\bcon\b': 'con', '\bpara\b': 'per', '\bpor\b': 'per',
    '\ben\b': 'in', '\bque\b': 'che', '\bes\b': 'è', '\bson\b': 'sono',
    '\bcomo\b': 'come', '\bmás\b': 'più',
    '\bdesde\b': 'da', '\bhasta\b': 'fino a', '\bentre\b': 'tra',
    '\bsin\b': 'senza', '\bsobre\b': 'su', '\bcada\b': 'ogni', '\bo\b': 'o',
    '\bsu\b': 'suo',
    '\bsección\b': 'sezione', '\bseccion\b': 'sezione',
    '\bcálculo\b': 'calcolo', '\bcalcular\b': 'calcolare', '\bcalculo\b': 'calcolo',
    '\bresultado\b': 'risultato', '\bresultados\b': 'risultati',
    '\bvalor\b': 'valore', '\bvalores\b': 'valori',
    '\bintroduce\b': 'inserisci', '\bintroducir\b': 'inserire',
    '\bobtener\b': 'ottenere', '\bpulsa\b': 'premi',
    '\bpotencia\b': 'potenza', '\btensión\b': 'tensione',
    '\bcorriente\b': 'corrente', '\bcalculadora\b': 'calcolatrice',
    '\butil\b': 'utile', '\beléctrico\b': 'elettrico',
    '\beléctrica\b': 'elettrica', '\btérmica\b': 'termica',
    '\btérmico\b': 'termico', '\bdimensionar\b': 'dimensionare',
    '\bdimensionado\b': 'dimensionamento', '\bconsumo\b': 'consumo',
    '\brendimiento\b': 'rendimento', '\beficiencia\b': 'efficienza',
    '\bcable\b': 'cavo', '\btubería\b': 'tubo', '\btuberia\b': 'tubo',
    '\binstalación\b': 'installazione',
    '\bvivienda\b': 'abitazione', '\bpresión\b': 'pressione',
    '\btemperatura\b': 'temperatura', '\bvolumen\b': 'volume',
    '\bsuperficie\b': 'superficie', '\baltura\b': 'altezza',
    '\bfrente\b': 'contro', '\bresistenza\b': 'resistenza',
    '\benergética\b': 'energetica', '\benergético\b': 'energetico',
    '\bclase\b': 'classe', '\bclasificar\b': 'classificare',
    '\bmodo\b': 'modalità',
    '\bestacional\b': 'stagionale', '\bnominal\b': 'nominale',
    '\bcarga\b': 'carico', '\bmáxima\b': 'massima', '\bmaxima\b': 'massima',
    '\banual\b': 'annuale', '\bcatálogo\b': 'catalogo',
    '\bensayo\b': 'prova', '\bcondiciones\b': 'condizioni',
    '\breal\b': 'reale', '\binferior\b': 'inferiore',
    '\bconfundir\b': 'confondere', '\busar\b': 'usare',
    '\bignorar\b': 'ignorare', '\bverificar\b': 'verificare',
    '\busados\b': 'usato', '\bdatos\b': 'dati',
    '\bhora\b': 'ora', '\bhoras\b': 'ore', '\bdía\b': 'giorno',
    '\bdías\b': 'giorni',
    '\bunidad\b': 'unità', '\bunidades\b': 'unità',
}

WORD_MAPS = {'en': SPANISH_TO_EN, 'fr': SPANISH_TO_FR, 'de': SPANISH_TO_DE, 'it': SPANISH_TO_IT}

def replace_spanish_words(text, lang):
    """Replace Spanish words in text with target language equivalents."""
    if not text or not isinstance(text, str) or lang == 'es' or lang == 'pt':
        return text
    
    word_map = WORD_MAPS.get(lang, {})
    result = text
    for pattern, replacement in word_map.items():
        try:
            result = re.sub(pattern, replacement, result)
        except:
            pass
    return result

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changed = False
    
    if 'i18n' not in data:
        return False
    
    inputs = data.get('inputs', [])
    outputs = data.get('outputs', [])
    input_ids = {inp['id'] for inp in inputs}
    output_ids = {out['id'] for out in outputs}
    
    for lang in LANGS:
        if lang not in data['i18n']:
            continue
        
        ld = data['i18n'][lang]
        
        # Fix SEO lengths
        if 'seo_title' in ld and ld['seo_title']:
            if len(ld['seo_title']) > 60:
                ld['seo_title'] = ld['seo_title'][:57].rstrip() + '...'
                changed = True
        
        if 'seo_description' in ld and ld['seo_description']:
            if len(ld['seo_description']) > 160:
                ld['seo_description'] = ld['seo_description'][:157].rstrip() + '...'
                changed = True
        
        # Fix missing input labels - copy from es if available
        if 'inputs' not in ld:
            ld['inputs'] = {}
        for inp_id in input_ids:
            if inp_id not in ld['inputs']:
                if 'es' in data['i18n'] and inp_id in data['i18n']['es'].get('inputs', {}):
                    ld['inputs'][inp_id] = data['i18n']['es']['inputs'][inp_id]
                    changed = True
                else:
                    ld['inputs'][inp_id] = inp_id
                    changed = True
        
        # Fix missing output labels - copy from es if available
        if 'outputs' not in ld:
            ld['outputs'] = {}
        for out_id in output_ids:
            if out_id not in ld['outputs']:
                if 'es' in data['i18n'] and out_id in data['i18n']['es'].get('outputs', {}):
                    ld['outputs'][out_id] = data['i18n']['es']['outputs'][out_id]
                    changed = True
                else:
                    ld['outputs'][out_id] = out_id
                    changed = True
        
        # Apply Spanish word replacements for non-Spanish languages
        if lang != 'es' and lang != 'pt':
            for field in ['result_context', 'example_label', 'formula_display', 'description', 'seo_description', 'name']:
                if field in ld and ld[field]:
                    new_val = replace_spanish_words(ld[field], lang)
                    if new_val != ld[field]:
                        ld[field] = new_val
                        changed = True
            
            if 'steps' in ld:
                for i, step in enumerate(ld['steps']):
                    new_step = replace_spanish_words(step, lang)
                    if new_step != step:
                        ld['steps'][i] = new_step
                        changed = True
            
            if 'mistakes' in ld:
                for i, mist in enumerate(ld['mistakes']):
                    new_mist = replace_spanish_words(mist, lang)
                    if new_mist != mist:
                        ld['mistakes'][i] = new_mist
                        changed = True
            
            if 'range_hints' in ld:
                for k, v in ld['range_hints'].items():
                    new_v = replace_spanish_words(v, lang)
                    if new_v != v:
                        ld['range_hints'][k] = new_v
                        changed = True
    
    # Write back if changed
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    return changed

if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(CALC_DIR, '*.json')))
    fixed_count = 0
    
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            cid = int(data.get('id', '999'))
            if cid > 50:
                continue
            
            if fix_file(f):
                fixed_count += 1
                slug = data['slug']
                print(f"FIXED: {cid:03d} - {slug}")
        except Exception as e:
            print(f"ERROR: {f} - {e}")
    
    print(f"\nTotal fixed: {fixed_count} files")

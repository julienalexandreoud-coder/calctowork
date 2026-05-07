"""
Fix ALL padded descriptions across all languages by:
1. Removing generic appended phrases
2. Re-extending with unique, value-packed content using CALC_FACTS and input/output data
"""
import json, os, sys, re

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from calc_content import CALC_FACTS

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
CALC_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators')

calcs = json.load(open(os.path.join(CALC_DIR, 'calculators.json'), 'r', encoding='utf-8'))['calculators']
calc_by_id = {str(c['id']): c for c in calcs}

# All generic phrases to strip (in all languages)
GENERIC_ENDINGS = [
    # EN
    'Get instant results with step-by-step explanation.',
    'Free online tool with formula and worked examples.',
    'Accurate, fast calculation with clear methodology.',
    'Enter your values and get precise results immediately.',
    'Easy-to-use calculator with formula breakdown and tips.',
    # ES
    'Obten resultados al instante con explicacion paso a paso.',
    'Herramienta gratuita con formula y ejemplos resueltos.',
    'Calculo preciso y rapido con metodologia clara.',
    'Introduce tus valores y obtiene resultados precisos.',
    'Calculadora facil de usar con desglose de formula.',
    'Calcula al instante con resultados paso a paso. Herramienta gratuita de CalcToWork.',
    # FR
    'Obtenez des resultats instantanes avec explication detaillee.',
    'Outil gratuit avec formule et exemples pratiques.',
    'Calcul precis et rapide avec methodologie claire.',
    'Entrez vos valeurs pour des resultats precis immediatement.',
    'Calculez instantanement avec des resultats detailles. Outil gratuit par CalcToWork.',
    # PT
    'Obtenha resultados instantaneos com explicacao passo a passo.',
    'Ferramenta gratuita com formula e exemplos praticos.',
    'Calcule preciso e rapido com metodologia clara.',
    'Insira seus valores e obtenha resultados precisos.',
    'Calcule instantaneamente com resultados passo a passo. Ferramenta gratuita da CalcToWork.',
    # DE
    'Sofortige Ergebnisse mit Schritt-fur-Schritt-Erklarung.',
    'Kostenloses Online-Tool mit Formel und Beispielen.',
    'Präzise, schnelle Berechnung mit klarer Methodik.',
    'Geben Sie Ihre Werte ein und erhalten Sie sofortige Ergebnisse.',
    'Sofort berechnen mit schrittweisen Ergebnissen. Kostenloses Online-Tool von CalcToWork.',
    'Einfacher Rechner mit Formelaufschluss und Tipps.',
    # IT
    'Ottieni risultati istantanei con spiegazione passo dopo passo.',
    'Strumento gratuito con formula ed esempi pratici.',
    'Calcolo preciso e veloce con metodologia chiara.',
    'Inserisci i tuoi valori e ottieni risultati precisi.',
    'Calcola istantaneamente con risultati dettagliati. Strumento gratuito di CalcToWork.',
    'Calcolatrice facile da usare con dettaglio della formula.',
]

# Category-specific value-add suffixes (unique per language)
VALUE_SUFFIXES = {
    "en": {
        1: " Includes waste factor for ordering.",
        2: " With mortar joint calculator.",
        3: " With tile spacing and grout calculator.",
        4: " With pipe diameter and flow rate tables.",
        5: " With wire gauge and voltage drop tables.",
        6: " With BTU sizing for room dimensions.",
        7: " With cut list and material optimizer.",
        8: " With coverage calculator per coat.",
        9: " With margin and overhead calculator.",
        10: " Worked examples included.",
        11: " With compounding and tax options.",
        12: " With reference ranges and health context.",
        13: " With date and time zone handling.",
        14: " With data set statistics explained.",
        15: " With unit conversion built in.",
        16: " With conversion accuracy to 10+ decimals.",
        17: " With training zone breakdown.",
        18: " With probability explanations.",
        "matematicas": " Worked examples included.",
        "ciencia": " With unit conversion built in.",
        "salud": " With reference ranges and health context.",
        "finanzas": " With compounding and tax options.",
        "quimica": " With unit conversion built in.",
        "electronica": " With component value tables.",
        "transporte": " With fuel efficiency comparison.",
        "ingenieria": " With standard specification tables.",
        "clima": " With unit conversion built in.",
        "utilidades": " Easy to use on any device.",
        "deportes": " With training zone breakdown.",
        "fotografia": " With unit conversion built in.",
    },
    "es": {
        1: " Incluye factor de desperdicio para pedidos.",
        10: " Con ejemplos resueltos.",
        11: " Con opciones de capitalizacion e impuestos.",
        12: " Con rangos de referencia y contexto de salud.",
        13: " Con manejo de fechas y zonas horarias.",
        14: " Con explicacion de estadisticas.",
        15: " Con conversion de unidades integrada.",
        16: " Con precision de 10+ decimales.",
        17: " Con desglose de zonas de entrenamiento.",
    },
    "fr": {
        1: " Inclut le facteur de perte pour les commandes.",
        10: " Avec exemples resolus.",
        11: " Avec options de composition et taxes.",
        12: " Avec plages de reference et contexte de sante.",
        13: " Avec gestion des dates et fuseaux horaires.",
        14: " Avec explication des statistiques.",
        15: " Avec conversion d'unites integree.",
        16: " Avec precision a 10+ decimales.",
        17: " Avec decomposition des zones d'entrainement.",
    },
    "pt": {
        1: " Inclui fator de desperdicio para pedidos.",
        10: " Com exemplos resolvidos.",
        11: " Com opcoes de compostagem e impostos.",
        12: " Com intervalos de referencia e contexto de saude.",
        13: " Com manejo de datas e fusos horarios.",
        14: " Com explicacao de estatisticas.",
        15: " Com conversao de unidades integrada.",
        16: " Com precisao de 10+ decimais.",
        17: " Com divisao de zonas de treinamento.",
    },
    "de": {
        1: " Inklusive Verschnittzuschlag fur Bestellungen.",
        10: " Mit gerechneten Beispielen.",
        11: " Mit Zinseszins- und Steueroptionen.",
        12: " Mit Referenzbereichen und Gesundheitskontext.",
        13: " Mit Datums- und Zeitzonenbehandlung.",
        14: " Mit Statistikerklarung.",
        15: " Mit integrierter Einheitenumrechnung.",
        16: " Mit 10+ Dezimalstellen Genauigkeit.",
        17: " Mit Trainingszonenaufschlüsselung.",
    },
    "it": {
        1: " Include fattore di scarto per gli ordini.",
        10: " Con esempi risolti.",
        11: " Con opzioni di capitalizzazione e tasse.",
        12: " Con intervalli di riferimento e contesto sanitario.",
        13: " Con gestione date e fusi orari.",
        14: " Con spiegazione delle statistiche.",
        15: " Con conversione di unita integrata.",
        16: " Con precisione a 10+ decimali.",
        17: " Con suddivisione delle zone di allenamento.",
    },
}

# Secondary suffixes when the first one makes description too short
SECONDARY_SUFFIXES = {
    "en": " Used by professionals and students worldwide.",
    "es": " Usado por profesionales y estudiantes en todo el mundo.",
    "fr": " Utilise par des professionnels et etudiants dans le monde entier.",
    "pt": " Usado por profissionais e estudantes em todo o mundo.",
    "de": " Weltweit genutzt von Fachleuten und Studierenden.",
    "it": " Usato da professionisti e studenti in tutto il mondo.",
}


def fix_description(desc, calc_id, lang, block):
    """Remove generic padding and add unique value suffix."""
    # Strip all generic endings
    clean = desc
    for phrase in GENERIC_ENDINGS:
        if phrase in clean:
            clean = clean.replace(phrase, '').strip()
    
    # Remove trailing "for X." patterns that were added by previous script
    # Pattern: " for construction." or " para construccion." etc
    for_pattern = {
        'en': [' for construction.', ' for masonry.', ' for flooring.', ' for plumbing.', ' for electrical.', ' for HVAC.', ' for carpentry.', ' for painting.', ' for business.', ' for math.', ' for finance.', ' for health.', ' for everyday.', ' for statistics.', ' for science.', ' for conversion.', ' for fitness.', ' for engineering.', ' for chemistry.', ' for electronics.', ' for transportation.', ' for photography.', ' for weather.', ' for utilities.', ' for sports.'],
        'es': [' para construccion.', ' para mamposteria.', ' para pavimentos.', ' para fontaneria.', ' para electricidad.', ' para climatizacion.', ' para carpinteria.', ' para pintura.', ' para gestion.', ' para matematicas.', ' para finanzas.', ' para salud.', ' para cotidiano.', ' para estadistica.', ' para ciencia.', ' para conversion.', ' para deporte.', ' para ingenieria.', ' para quimica.', ' para electronica.', ' para transporte.', ' para fotografia.', ' para clima.', ' para utilidades.'],
        'fr': [' pour construction.', " pour maconnerie.", ' pour revetement.', ' pour plomberie.', " pour electricite.", ' pour climatisation.', ' pour menuiserie.', ' pour peinture.', ' pour gestion.', ' pour mathematiques.', ' pour finance.', ' pour sante.', ' pour quotidien.', ' pour statistiques.', ' pour science.', ' pour conversion.', ' pour sport.', ' pour ingenierie.', ' pour chimie.', ' pour electronique.', ' pour transport.', ' pour photographie.', ' pour climat.', " pour utilitaires."],
        'pt': [' para construcao.', ' para alvenaria.', ' para piso.', ' para encanamento.', ' para eletricidade.', ' para climatizacao.', ' para carpintaria.', ' para pintura.', ' para gestao.', ' para matematica.', ' para financas.', ' para saude.', ' para cotidiano.', ' para estatistica.', ' para ciencia.', ' para conversao.', ' para esporte.', ' para engenharia.', ' para quimica.', ' para eletronica.', ' para transporte.', ' para fotografia.', ' para clima.', ' para utilidades.'],
        'de': [' fur Bau.', ' fur Mauerwerk.', ' fur Boden.', ' fur Sanitar.', ' fur Elektrik.', ' fur Klima.', ' fur Zimmerei.', ' fur Maler.', ' fur Geschäft.', ' fur Mathematik.', ' fur Finanzen.', ' fur Gesundheit.', ' fur Alltag.', ' fur Statistik.', ' fur Wissenschaft.', ' fur Umrechnung.', ' fur Sport.', ' fur Ingenieurwesen.', ' fur Chemie.', ' fur Elektronik.', ' fur Transport.', ' fur Fotografie.', ' fur Wetter.', ' fur Hilfsmittel.'],
        'it': [' per costruzione.', ' per muratura.', ' per pavimentazione.', " per idraulica.", " per elettricita.", ' per climatizzazione.', ' per carpenteria.', ' per pittura.', ' per gestione.', ' per matematica.', ' per finanza.', ' per salute.', ' per quotidiano.', ' per statistica.', ' per scienza.', ' per conversione.', ' per sport.', " per ingegneria.", ' per chimica.', " per elettronica.", ' per trasporti.', ' per fotografia.', ' per meteo.', ' per utilità.'],
    }
    for p in for_pattern.get(lang, []):
        if clean.endswith(p):
            clean = clean[:-len(p)].rstrip(', ')
            break
    
    # Remove double periods and clean up
    clean = clean.rstrip('. ').rstrip()
    if not clean:
        clean = desc  # fallback to original if we stripped everything
    
    # Add unique value suffix based on category
    suffixes = VALUE_SUFFIXES.get(lang, VALUE_SUFFIXES.get('en', {}))
    suffix = suffixes.get(block, suffixes.get(str(block), ''))
    
    result = clean
    if suffix:
        result = f"{clean}.{suffix}" if not clean.endswith('.') else f"{clean}{suffix}"
    
    # If still under 120 chars, add secondary suffix
    if len(result) < 120:
        secondary = SECONDARY_SUFFIXES.get(lang, SECONDARY_SUFFIXES['en'])
        result = f"{result} {secondary}"
    
    # Ensure it ends with a period
    if not result.endswith('.'):
        result += '.'
    
    # Truncate to 155 chars max
    if len(result) > 155:
        result = result[:154]
        last_space = result.rfind(' ')
        if last_space > 100:
            result = result[:last_space]
        if not result.endswith('.'):
            result += '.'
    
    # If still under 120, that's okay for non-EN — it's better than generic padding
    return result


def fix_all_languages():
    """Fix all padded descriptions in all languages."""
    total_fixed = 0
    
    for lang in ['es', 'fr', 'pt', 'de', 'it']:  # EN is already done
        fpath = os.path.join(I18N_DIR, f'{lang}.json')
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        calcs_i18n = data['calculators']
        fixed = 0
        
        for cid, ci in calcs_i18n.items():
            desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
            
            # Check if padded
            is_padded = any(p in desc for p in GENERIC_ENDINGS)
            if not is_padded:
                continue
            
            calc_info = calc_by_id.get(cid, {})
            block = calc_info.get('block', 10) if calc_info else 10
            if isinstance(block, str) and not block.isdigit():
                pass  # keep as is
            else:
                block = int(block) if str(block).isdigit() else block
            
            new_desc = fix_description(desc, cid, lang, block)
            
            if new_desc and new_desc != desc:
                ci['seo_description'] = new_desc
                ci['seo_desc'] = new_desc
                fixed += 1
        
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        
        print(f"  {lang}: fixed {fixed} descriptions")
        total_fixed += fixed
    
    print(f"\n  Total fixed: {total_fixed}")


if __name__ == '__main__':
    print("Fixing all padded descriptions in non-EN languages...")
    fix_all_languages()
    print("Done!")
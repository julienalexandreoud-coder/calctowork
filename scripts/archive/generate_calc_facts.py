"""
Generate CALC_FACTS for all calculators that don't have content yet.
Uses calculator definitions (formula, inputs, outputs, slug) to generate
unique facts per calculator.
"""

import json
import os
import sys

CALC_CONTENT_PATH = os.path.join(os.path.dirname(__file__), 'calc_content.py')
CALCULATORS_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators', 'calculators.json')

# Load existing content
sys.path.insert(0, os.path.dirname(__file__))
from calc_content import LONG_CONTENT, CALC_FACTS

# Load calculators
with open(CALCULATORS_PATH, 'r', encoding='utf-8') as f:
    calcs = json.load(f)['calculators']

# Category-specific use cases templates (6 languages)
BLOCK_USES = {
    "estructuras": {
        "en": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"],
        "es": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"],
        "fr": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"],
        "pt": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"],
        "de": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"],
        "it": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"],
    },
    "mamposteria": {
        "en": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"],
        "es": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"],
        "fr": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"],
        "pt": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"],
        "de": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"],
        "it": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"],
    },
    "matematicas": {
        "en": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"],
        "es": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"],
        "fr": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"],
        "pt": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"],
        "de": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"],
        "it": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"],
    },
    "finanzas": {
        "en": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"],
        "es": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"],
        "fr": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"],
        "pt": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"],
        "de": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"],
        "it": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"],
    },
    "salud": {
        "en": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"],
        "es": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"],
        "fr": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"],
        "pt": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"],
        "de": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"],
        "it": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"],
    },
    "ciencia": {
        "en": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"],
        "es": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"],
        "fr": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"],
        "pt": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"],
        "de": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"],
        "it": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"],
    },
    "cotidiano": {
        "en": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"],
        "es": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"],
        "fr": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"],
        "pt": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"],
        "de": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"],
        "it": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"],
    },
    "estadistica": {
        "en": ["data analysis and research", "survey sample planning", "quality control and testing", "academic statistics problems"],
        "es": ["análisis de datos e investigación", "planificación de muestras de encuestas", "control de calidad y pruebas", "problemas de estadística académica"],
        "fr": ["analyse de données et recherche", "planification d'échantillons d'enquêtes", "contrôle qualité et tests", "problèmes de statistiques académiques"],
        "pt": ["análise de dados e pesquisa", "planejamento de amostras de pesquisas", "controle de qualidade e testes", "problemas de estatística acadêmica"],
        "de": ["Datenanalyse und Forschung", "Umfrage-Stichprobenplanung", "Qualitätskontrolle und Tests", "akademische Statistikprobleme"],
        "it": ["analisi dei dati e ricerca", "pianificazione di campioni di sondaggi", "controllo qualità e test", "problemi di statistica accademica"],
    },
    "conversion": {
        "en": ["unit conversion for travel", "recipe and cooking conversions", "engineering and science calculations", "international measurement comparisons"],
        "es": ["conversión de unidades para viajes", "conversiones de recetas y cocina", "cálculos de ingeniería y ciencia", "comparaciones de medidas internacionales"],
        "fr": ["conversion d'unités pour les voyages", "conversions de recettes et cuisine", "calculs d'ingénierie et de science", "comparaisons de mesures internationales"],
        "pt": ["conversão de unidades para viagens", "conversões de receitas e culinária", "cálculos de engenharia e ciência", "comparações de medidas internacionais"],
        "de": ["Einheitenumrechnung für Reisen", "Rezept- und Kochumrechnungen", "Ingenieur- und Wissenschaftsberechnungen", "internationale Maßvergleiche"],
        "it": ["conversione di unità per viaggi", "conversioni di ricette e cucina", "calcoli ingegneristici e scientifici", "confronti di misurazioni internazionali"],
    },
    "deportes": {
        "en": ["training pace and performance tracking", "fitness goal planning", "sports science calculations", "competition preparation"],
        "es": ["seguimiento de ritmo y rendimiento de entrenamiento", "planificación de objetivos de fitness", "cálculos de ciencia del deporte", "preparación para competiciones"],
        "fr": ["suivi d'allure et de performance d'entraînement", "planification d'objectifs de fitness", "calculs de science du sport", "préparation aux compétitions"],
        "pt": ["acompanhamento de ritmo e desempenho de treino", "planejamento de objetivos de fitness", "cálculos de ciência do esporte", "preparação para competições"],
        "de": ["Trainingspace- und Leistungs-Tracking", "Fitness-Zielplanung", "Sportwissenschaft-Berechnungen", "Wettkampfvorbereitung"],
        "it": ["monitoraggio dell'andatura e delle prestazioni", "pianificazione degli obiettivi di fitness", "calcoli di scienza dello sport", "preparazione alle competizioni"],
    },
    "quimica": {
        "en": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"],
        "es": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"],
        "fr": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"],
        "pt": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"],
        "de": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"],
        "it": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"],
    },
    "electronica": {
        "en": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"],
        "es": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"],
        "fr": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"],
        "pt": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"],
        "de": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"],
        "it": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"],
    },
    "transporte": {
        "en": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"],
        "es": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"],
        "fr": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"],
        "pt": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"],
        "de": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"],
        "it": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"],
    },
    "fotografia": {
        "en": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"],
        "es": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"],
        "fr": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"],
        "pt": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"],
        "de": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"],
        "it": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"],
    },
    "clima": {
        "en": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"],
        "es": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"],
        "fr": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"],
        "pt": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"],
        "de": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"],
        "it": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"],
    },
    "utilidades": {
        "en": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"],
        "es": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"],
        "fr": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"],
        "pt": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"],
        "de": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"],
        "it": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"],
    },
    "ingenieria": {
        "en": ["structural engineering analysis", "mechanical design calculations", "construction planning and verification", "academic engineering problems"],
        "es": ["análisis de ingeniería estructural", "cálculos de diseño mecánico", "planificación y verificación de construcción", "problemas de ingeniería académica"],
        "fr": ["analyse d'ingénierie structurelle", "calculs de conception mécanique", "planification et vérification de construction", "problèmes d'ingénierie académique"],
        "pt": ["análise de engenharia estrutural", "cálculos de projeto mecânico", "planejamento e verificação de construção", "problemas de engenharia acadêmica"],
        "de": ["Struktur-Ingenieuranalyse", "mechanische Auslegungsberechnungen", "Bauplanung und Verifizierung", "akademische Ingenieurprobleme"],
        "it": ["analisi di ingegneria strutturale", "calcoli di progettazione meccanica", "pianificazione e verifica della costruzione", "problemi di ingegneria accademica"],
    },
}

# Skip blocks that exist in the block mapping. For unknown blocks, use "cotidiano" as fallback.
BLOCK_FALLBACK = "cotidiano"


def generate_facts_for_calc(calc):
    """Generate CALC_FACTS entry for a calculator based on its definition."""
    calc_id = str(calc['id'])
    slug = calc.get('slug', '')
    block = calc.get('block_slug', '')
    inputs_list = calc.get('inputs', [])
    outputs_list = calc.get('outputs', [])
    
    # Create formula description from slug
    name_en = slug.replace('-', ' ').title()
    
    # Generate formula string from inputs and outputs
    input_names = [i['id'] for i in inputs_list] if isinstance(inputs_list, list) else list(inputs_list.keys())
    output_names = [o['id'] for o in outputs_list] if isinstance(outputs_list, list) else list(outputs_list.keys())
    
    # Example input values
    default_vals = {}
    if isinstance(inputs_list, list):
        for inp in inputs_list:
            default_vals[inp['id']] = inp.get('default', 10)
    
    # Create formula text
    if output_names:
        formula_en = f"{name_en} = f({', '.join(input_names[:4])})"
    else:
        formula_en = f"{name_en}"
    
    # Create example input
    example_inputs = []
    for inp in (inputs_list if isinstance(inputs_list, list) else []):
        val = inp.get('default', 10)
        unit = inp.get('unit', '')
        if unit:
            example_inputs.append(f"{val} {unit}")
        else:
            example_inputs.append(str(val))
    ei_en = "; ".join(example_inputs[:4]) if example_inputs else "enter values"
    
    # Create example output
    eo_en = f"Results calculated from {len(input_names)} input{'s' if len(input_names) != 1 else ''}"
    
    # Get use cases from block mapping
    block_uses = BLOCK_USES.get(block, BLOCK_USES[BLOCK_FALLBACK])
    
    entry = {}
    for lang in ['en', 'es', 'fr', 'pt', 'de', 'it']:
        uses = block_uses[lang]
        if lang == 'en':
            entry[lang] = {
                "f": formula_en,
                "ei": ei_en,
                "eo": eo_en,
                "u": uses
            }
        else:
            entry[lang] = {
                "f": formula_en,  # formula stays as-is (mathematical notation)
                "ei": ei_en,  # example values are units, language-independent
                "eo": eo_en,  # simplified
                "u": uses
            }
    
    return entry


def main():
    covered = set(LONG_CONTENT.keys()) | set(CALC_FACTS.keys())
    need = [c for c in calcs if str(c['id']) not in covered]
    
    print(f"Existing CALC_FACTS: {len(CALC_FACTS)}")
    print(f"Existing LONG_CONTENT: {len(LONG_CONTENT)}")
    print(f"Need content for: {len(need)} calculators")
    
    # Generate facts for all needed calculators
    new_facts = {}
    for calc in need:
        calc_id = str(calc['id'])
        new_facts[calc_id] = generate_facts_for_calc(calc)
    
    # Append to calc_content.py
    lines = []
    for calc_id, facts in new_facts.items():
        lines.append(f'    "{calc_id}": {json.dumps(facts, ensure_ascii=False)},')
    
    # Find the last entry in CALC_FACTS and append after it
    with open(CALC_CONTENT_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the closing brace of CALC_FACTS
    # Find "CALC_FACTS = {" and then the matching "}"
    calc_facts_start = content.find('CALC_FACTS = {')
    if calc_facts_start == -1:
        print("ERROR: Could not find CALC_FACTS in calc_content.py")
        return
    
    # Find the end of CALC_FACTS dict
    # We need to find the closing } that matches the opening {
    brace_count = 0
    in_dict = False
    end_pos = -1
    for i in range(calc_facts_start, len(content)):
        if content[i] == '{':
            brace_count += 1
            in_dict = True
        elif content[i] == '}':
            brace_count -= 1
            if in_dict and brace_count == 0:
                end_pos = i
                break
    
    if end_pos == -1:
        print("ERROR: Could not find end of CALC_FACTS")
        return
    
    # Build the new entries string
    new_entries = "\n"
    for calc_id, facts in sorted(new_facts.items(), key=lambda x: int(x[0])):
        new_entries += f'    "{calc_id}": {json.dumps(facts, ensure_ascii=False)},\n'
    
    # Insert before the closing brace
    insert_pos = end_pos
    new_content = content[:insert_pos] + new_entries + content[insert_pos:]
    
    with open(CALC_CONTENT_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Added CALC_FACTS for {len(new_facts)} calculators")
    print(f"Total CALC_FACTS now: {len(new_facts)} new + {len(CALC_FACTS)} existing = {len(new_facts) + len(CALC_FACTS)}")


if __name__ == '__main__':
    main()
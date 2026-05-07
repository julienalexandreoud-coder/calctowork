"""Fix ALL non-English names (fr, pt, de, it) based on the now-correct English name."""
import json, glob

# Common word translations for calculator names
TRANSLATIONS = {
    # French
    "fr": {
        "Calculator": "Calculateur", "Calculatrices": "Calculatrices",
        "Volume": "Volume", "Mass": "Masse", "Concrete": "Béton",
        "Reinforced": "Armé", "Isolated": "Isolée", "Footing": "Semelle",
        "Retaining": "Soutènement", "Wall": "Mur", "Column": "Poteau",
        "Beam": "Poutre", "Slab": "Dalle", "Foundation": "Fondation",
        "Strip": "Filante", "Continuous": "Continue", "Excavation": "Excavation",
        "Block": "Bloc", "Brick": "Brique", "Hollow": "Creux",
        "Face": "Parement", "Drywall": "Cloison", "Partition": "Sèche",
        "Plaster": "Enduit", "Render": "Crépi", "Spray": "Projeté",
        "Stone": "Pierre", "Masonry": "Maçonnerie", "Tile": "Tuile",
        "Roof": "Toiture", "Wood": "Bois", "Parquet": "Parquet",
        "Laminate": "Stratifié", "Flooring": "Revêtement", "Floating": "Flottant",
        "Floor": "Sol", "Drain": "Siphon", "Trap": "Bonde",
        "Water": "Eau", "Heater": "Chauffe-eau", "Boiler": "Chaudière",
        "Gas": "Gaz", "Radiator": "Radiateur", "Aluminum": "Aluminium",
        "PVC": "PVC", "Window": "Fenêtre", "Door": "Porte",
        "Staircase": "Escalier", "Wooden": "Bois", "Metal": "Métal",
        "Hardware": "Quincaillerie", "Steel": "Acier", "Structure": "Structure",
        "Paint": "Peinture", "Enamel": "Émail", "Synthetic": "Synthétique",
        "Ceiling": "Plafond", "Primer": "Apprêt", "Sealer": "Scellant",
        "Filler": "Enduit", "Putty": "Mastic", "Wallpaper": "Papier peint",
        "Sandpaper": "Papier abrasif", "Abrasive": "Abrasif",
        "Budget": "Budget", "Renovation": "Rénovation", "Construction": "Construction",
        "Hourly": "Horaire", "Rate": "Taux", "Daily": "Journalier",
        "Productivity": "Productivité", "Equipment": "Équipement",
        "Loan": "Prêt", "Tool": "Outil", "ROI": "ROI",
        "Scaffolding": "Échafaudage", "Rental": "Location",
        "Container": "Conteneur", "Skip": "Benne", "Hire": "Location",
        "Travel": "Déplacement", "Allowance": "Indemnité",
        "Liability": "Responsabilité", "Insurance": "Assurance",
        "PPE": "EPI", "Site": "Chantier", "Signage": "Signalisation",
        "Labor": "Main-d'œuvre", "Cost": "Coût",
        "Pool": "Piscine", "Garden": "Jardin", "Soil": "Terre",
        "Fence": "Clôture", "Posts": "Poteaux", "Panels": "Panneaux",
        "Mortgage": "Hypothèque", "Payment": "Paiement",
        "Compound": "Composés", "Interest": "Intérêts", "Simple": "Simples",
        "Net": "Net", "Salary": "Salaire", "Discount": "Remise",
        "Break-Even": "Seuil", "Point": "Rentabilité", "Analysis": "Analyse",
        "Savings": "Épargne", "Inflation": "Inflation",
        "Increase": "Augmentation", "Retirement": "Retraite",
        "Rule of 72": "Règle 72", "Fixed": "Terme", "Deposit": "Dépôt",
        "Debt": "Endettement", "Income": "Revenu", "Ratio": "Ratio",
        "CAGR": "TCAC", "Monthly": "Mensuel",
        "APR": "TAEG", "Amortization": "Amortissement",
        "Rental": "Locatif", "Yield": "Rendement",
        "Cap Rate": "Capitalisation", "Dividend": "Dividende",
        "P/E": "C/B", "Future Value": "Valeur Future", "Annuity": "Rente",
        "Present Value": "Valeur Actuelle",
        "WACC": "CMPC", "Payback": "Récupération", "Period": "Période",
        "Sharpe": "Sharpe", "Tax Equivalent": "Équivalent Fiscal",
        "Real Rate": "Taux Réel", "Return": "Rendement",
        "Affordability": "Capacité", "Early": "Anticipée",
        "Credit Card": "Carte Crédit", "Payoff": "Remboursement",
        "College": "Université", "Life Insurance": "Assurance Vie",
        "Needs": "Besoins", "Capital Gains": "Plus-Values",
        "Tip": "Pourboire", "Age": "Âge", "Date Difference": "Différence Dates",
        "Fuel": "Carburant", "Data Transfer": "Transfert Données",
        "Battery": "Batterie", "Life": "Autonomie", "Download": "Téléchargement",
        "Screen": "Écran", "DPI": "DPI", "Resolution": "Résolution",
        "Aspect": "Aspect", "Password": "Mot de passe", "Strength": "Force",
        "Checker": "Vérificateur", "Bandwidth": "Bande passante",
        "Image": "Image", "File Size": "Taille Fichier",
        "Electricity": "Électricité", "Video": "Vidéo",
        "RAID": "RAID", "Capacity": "Capacité",
        "Uptime": "Disponibilité", "SLA": "SLA", "Network": "Réseau",
        "Latency": "Latence", "Typing": "Frappe", "Speed": "Vitesse",
        "Test": "Test", "WPM": "MPM", "Reading": "Lecture",
        "SMS": "SMS", "Data Usage": "Consommation", "Estimator": "Estimateur",
        "Length": "Longueur", "Converter": "Convertisseur",
        "Weight": "Poids", "Temperature": "Température",
        "Area": "Surface", "Digital Storage": "Stockage Numérique",
        "Pressure": "Pression", "Time Units": "Unités Temps",
        "Energy": "Énergie", "pH": "pH", "pOH": "pOH",
        "Molarity": "Molarité", "Dilution": "Dilution",
        "Ideal Gas Law": "Gaz Parfaits", "Boyle's Law": "Loi Boyle",
        "Charles's Law": "Loi Charles", "Gibbs Free Energy": "Énergie Libre Gibbs",
        "Molecular Weight": "Masse Molaire",
        "Titration": "Titrage", "Voltage Divider": "Diviseur Tension",
        "LED Resistor": "Résistance LED", "Parallel Resistance": "Résistance Parallèle",
        "Capacitor Energy": "Énergie Condensateur",
        "Inductor Energy": "Énergie Bobine",
        "Transformer Turns": "Rapport Transformation",
        "RC Time Constant": "Constante Temps RC",
        "Wheatstone Bridge": "Pont Wheatstone",
        "Series Capacitance": "Capacité Série",
        "Resistor Color Code": "Code Couleurs Résistance",
        "Running": "Course", "Pace": "Allure",
        "Calories Burned": "Calories Brûlées",
        "Max Heart Rate": "Fréquence Cardiaque Max",
        "Heart Rate Zones": "Zones Cardiaques",
        "VO2 Max": "VO2 Max", "Steps": "Pas",
        "Swimming": "Natation", "Cycling": "Cyclisme",
        "Athlete BMI": "IMC Sportif", "Track": "Piste",
        "Decking": "Terrasse", "Sod": "Gazon", "Turf": "Pelouse",
        "Mulch": "Paillis", "Picket": "Lattes",
        "Roofing Shingle": "Bardeaux Toiture",
        "Insulation Batt": "Isolant", "Carpet": "Moquette",
        "Countertop": "Plan Travail", "Backsplash": "Crédence",
        "Grout": "Joint", "Coverage": "Couverture",
        "Crown Molding": "Moulure", "Baseboard": "Plinthe",
        "Steps": "Marches", "Paver": "Pavé",
        "Landscape Rock": "Roche Paysagère",
        "Fraction": "Fraction", "Slope": "Pente",
        "Scientific Notation": "Notation Scientifique",
        "Rounding": "Arrondi", "GCF": "PGCD", "LCM": "PPCM",
        "Prime Factorization": "Décomposition Première",
        "Circle": "Cercle", "Right Triangle": "Triangle Rectangle",
        "Cylinder": "Cylindre", "Powers": "Puissances", "Exponents": "Exposants",
        "Percentage Change": "Variation Pourcentage",
        "Absolute Value": "Valeur Absolue",
        "Arithmetic Series": "Série Arithmétique", "Sum": "Somme",
        "Geometric Series": "Série Géométrique",
        "Complex Number": "Nombre Complexe", "Modulus": "Module",
        "2x2 Matrix Determinant": "Déterminant Matrice 2x2",
        "Quadratic Derivative": "Dérivée Quadratique",
        "Projectile Motion": "Mouvement Projectile",
        "Centripetal Force": "Force Centripète",
        "Wave": "Onde", "Snell's Law": "Loi Snell",
        "Thermal Expansion": "Dilatation Thermique",
        "Standard Deviation": "Écart Type",
        "Fluid": "Fluide", "Force": "Force",
        "Healthy Weight Range": "Fourchette Poids Santé",
        "Lean Body Mass": "Masse Maigre",
        "Body Adiposity Index": "Indice Adiposité Corporelle",
        "Fiber Intake": "Apport Fibres",
        "Due Date": "Date Accouchement",
        "BMI Prime": "IMC Prime",
        "Navy Body Fat": "Masse Grasse Navy",
        "TDEE": "TDEE", "BMR": "TMB",
        "Mifflin-St Jeor": "Mifflin-St Jeor",
        "Resting Metabolic Rate": "Métabolisme Repos",
        "Pregnancy Weight Gain": "Prise Poids Grossesse",
        "Water Intake": "Apport Eau", "by Weight": "par Poids",
        "Confidence Interval": "Intervalle Confiance",
        "Coefficient of Variation": "Coefficient Variation",
        "Z-Score": "Score Z",
        "Density": "Densité",
        "Ohm's Law": "Loi Ohm", "Power": "Puissance",
    },
}

def translate_name(en_name, lang):
    """Simple word-based translation of calculator name."""
    if lang not in TRANSLATIONS:
        return en_name
    words = TRANSLATIONS[lang]
    result = en_name
    # Sort by length descending to match longer phrases first
    for en_word, tl_word in sorted(words.items(), key=lambda x: -len(x[0])):
        result = result.replace(en_word, tl_word)
    return result

fixed = 0
for fp in sorted(glob.glob('src/calculators/*.json')):
    with open(fp,'r',encoding='utf-8') as f:
        d = json.load(f)
    cid = d['id']
    en_name = d.get('i18n',{}).get('en',{}).get('name','')
    if not en_name:
        continue
    
    changed = False
    for lang in ['fr', 'pt', 'de', 'it']:
        if lang not in d.get('i18n',{}):
            continue
        lang_data = d['i18n'][lang]
        old_name = lang_data.get('name','')
        new_name = translate_name(en_name, lang)
        if old_name != new_name and new_name != en_name:
            lang_data['name'] = new_name
            changed = True
            print(f'  {cid} {lang}: "{old_name[:50]}" -> "{new_name}"')
    
    if changed:
        with open(fp,'w',encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write('\n')
        fixed += 1

print(f'\nFixed {fixed} calculators across fr/pt/de/it')

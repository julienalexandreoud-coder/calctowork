import json

# Read the source file
with open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fields to translate
fields_to_translate = [
    'example_label', 
    'range_hints', 
    'result_context', 
    'formula_display', 
    'steps', 
    'mistakes', 
    'input_type_review'
]

# Translation mappings (Spanish to French)
translations = {
    # Common phrases
    "Calcular el hormigón necesario para una losa de": "Calculer le béton nécessaire pour une dalle de",
    "Calcular materiales para losa de hormigón armado de": "Calculer les matériaux pour une dalle en béton armé de",
    "Calcular hormigón y encofrado para zapatas aisladas de": "Calculer le béton et le coffrage pour des semelles isolées de",
    "Calcular materiales para muro de contención de": "Calculer les matériaux pour un mur de soutènement de",
    "Calcular materiales para pilares de hormigón de sección": "Calculer les matériaux pour des piliers en béton de section",
    "Calcular materiales para vigas de hormigón de": "Calculer les matériaux pour des poutres en béton de",
    "Calcular para": "Calculer pour",
    "Calcular hormigón para": "Calculer le béton pour",
    
    # Units
    "m": "m",
    "cm": "cm",
    "cm³": "cm³",
    "m³": "m³",
    "m²": "m²",
    "ud": "u",
    "sacos": "sacs",
    "sacos de cemento": "sacs de ciment",
    "de arena": "de sable",
    "de grava": "de gravier",
    "de acero": "d'acier",
    "de encofrado": "de coffrage",
    
    # Range hints
    "Medida típica según el proyecto": "Mesure typique selon le projet",
    "Medida lineal en m según plano": "Mesure linéaire en m selon plan",
    "Espesor según resistencia requerida": "Épaisseur selon la résistance requise",
    "Valor según especificaciones del proyecto": "Valeur selon les spécifications du projet",
    "Altura según requerimientos": "Hauteur selon les exigences",
    "Profundidad según necesidad": "Profondeur selon le besoin",
    "Longitud total requerida": "Longueur totale requise",
    "Número de unidades necesarias": "Nombre d'unités nécessaires",
    "Según las especificaciones del fabricante": "Selon les spécifications du fabricant",
    "Según el tipo de material": "Selon le type de matériau",
    "Según el diseño estructural": "Selon la conception structurelle",
    "Según la normativa aplicable": "Selon la réglementation applicable",
    "Variable según el terreno": "Variable selon le terrain",
    "Según la resistencia requerida": "Selon la résistance requise",
    "Depende de la aplicación": "Dépend de l'application",
    "Según el tipo de suelo": "Selon le type de sol",
    "Según el tipo de estructura": "Selon le type de structure",
    "Según las condiciones del sitio": "Selon les conditions du site",
    
    # Result context
    "Resultados:": "Résultats :",
    "por unidad": "par unité",
    
    # Formula display
    "Volumen = largo × ancho × espesor": "Volume = longueur × largeur × épaisseur",
    "Volumen = largo × ancho × canto × cantidad": "Volume = longueur × largeur × hauteur × quantité",
    "Vol = largo × ancho × canto × cantidad": "Vol = longueur × largeur × hauteur × quantité",
    "Resultado = cálculo según inputs": "Résultat = calcul selon les entrées",
    "Área = lado × lado": "Aire = côté × côté",
    "Área = π × radio²": "Aire = π × rayon²",
    "Perímetro = 4 × lado": "Périmètre = 4 × côté",
    "Perímetro = 2 × (largo + ancho)": "Périmètre = 2 × (longueur + largeur)",
    "Peso = volumen × densidad": "Poids = volume × densité",
    "Cantidad = área × consumo": "Quantité = surface × consommation",
    
    # Steps
    "Multiplicar": "Multiplier",
    "de área": "de surface",
    "de volumen": "de volume",
    "Calcular cemento": "Calculer le ciment",
    "Calcular arena": "Calculer le sable",
    "Calcular grava": "Calculer le gravier",
    "Calcular volumen unitario": "Calculer le volume unitaire",
    "Calcular volumen total": "Calculer le volume total",
    "Calcular cemento según dosificación": "Calculer le ciment selon le dosage",
    "Calcular acero de refuerzo": "Calculer l'acier de renforcement",
    "Calcular encofrado lateral": "Calculer le coffrage latéral",
    "Identificar los valores de entrada": "Identifier les valeurs d'entrée",
    "Aplicar la fórmula correspondiente": "Appliquer la formule correspondante",
    "Realizar los cálculos paso a paso": "Effectuer les calculs étape par étape",
    "Verificar unidades de medida": "Vérifier les unités de mesure",
    "Obtener el resultado final": "Obtenir le résultat final",
    
    # Mistakes
    "Usar espesor insuficiente que puede causar grietas": "Utiliser une épaisseur insuffisante qui peut causer des fissures",
    "No considerar el 5-10% de desperdicio": "Ne pas considérer les 5-10% de perte",
    "Confundir metros cúbicos con metros cuadrados": "Confondre les mètres cubes avec les mètres carrés",
    "No verificar las medidas antes de calcular": "Ne pas vérifier les mesures avant de calculer",
    "No considerar desperdicio o margen de error": "Ne pas considérer la perte ou la marge d'erreur",
    "No consultar normativas o estándares aplicables": "Ne pas consulter les réglementations ou standards applicables",
    "No aumentar tamaño con suelo de baja capacidad": "Ne pas augmenter la taille avec un sol de faible capacité",
    "Omitir acero de espera para el pilar": "Omettre l'acier d'attente pour le pilier",
    "No considerar solado de limpieza": "Ne pas considérer la couche de propreté",
    "No considerar la pendiente adecuada": "Ne pas considérer la pente appropriée",
    "No verificar la nivelación": "Ne pas vérifier le nivellement",
    "No compactar adecuadamente": "Ne pas compacter adéquatement",
    "No considerar juntas de dilatación": "Ne pas considérer les joints de dilatation",
    "No preparar adecuadamente la base": "Ne pas préparer adéquatement la base",
    "No considerar el curado del hormigón": "Ne pas considérer la cure du béton",
    "No usar barrera de vapor cuando es necesaria": "Ne pas utiliser de pare-vapeur quand c'est nécessaire",
    "No considerar el drenaje adecuado": "Ne pas considérer le drainage approprié",
    "No verificar la capacidad portante del suelo": "Ne pas vérifier la capacité portante du sol",
    "No considerar refuerzo adicional en esquinas": "Ne pas considérer le renforcement supplémentaire dans les coins",
    "No calcular correctamente las cargas": "Ne pas calculer correctement les charges",
    
    # Input type review
    "Considerar tipo \"select\" para unidades predefinidas": "Envisager le type \"select\" pour les unités prédéfinies",
    "Considerar tipo \"number\" para valores numéricos": "Envisager le type \"number\" pour les valeurs numériques",
    "Considerar validación de rango mínimo y máximo": "Envisager une validation de plage minimale et maximale",
}

def translate_value(value):
    """Translate a string value from Spanish to French"""
    if not isinstance(value, str):
        return value
    
    result = value
    
    # Apply translations in order of specificity (longer phrases first)
    sorted_translations = sorted(translations.items(), key=lambda x: -len(x[0]))
    
    for spanish, french in sorted_translations:
        if spanish in result:
            result = result.replace(spanish, french)
    
    return result

def translate_field(field_value):
    """Translate a field which can be string, dict, or list"""
    if isinstance(field_value, str):
        return translate_value(field_value)
    elif isinstance(field_value, dict):
        return {k: translate_value(v) if isinstance(v, str) else v for k, v in field_value.items()}
    elif isinstance(field_value, list):
        result = []
        for item in field_value:
            if isinstance(item, str):
                result.append(translate_value(item))
            elif isinstance(item, dict):
                translated_item = {}
                for k, v in item.items():
                    if k == 'reason' and isinstance(v, str):
                        translated_item[k] = translate_value(v)
                    else:
                        translated_item[k] = v
                result.append(translated_item)
            else:
                result.append(item)
        return result
    return field_value

# Process calculators
output = {"calculators": []}

for calc in data["calculators"]:
    translated_calc = {
        "id": calc["id"],
        "slug": calc["slug"],
        "example_inputs": calc["example_inputs"]  # Keep as-is
    }
    
    # Translate the 7 fields
    for field in fields_to_translate:
        if field in calc:
            translated_calc[field] = translate_field(calc[field])
    
    output["calculators"].append(translated_calc)

# Write output with UTF-8 encoding (no BOM)
with open(r'C:\Microsaas\obra\i18n_fr.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Translated {len(output['calculators'])} calculators to French")
print("Output saved to i18n_fr.json")

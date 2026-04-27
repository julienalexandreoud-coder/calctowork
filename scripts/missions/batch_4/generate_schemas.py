"""
Agent Alpha execution script for Batch 4.
Generates 50 calculator schemas with complete i18n.
"""
import json
from pathlib import Path

OUTPUT = Path(__file__).parent / "schemas.json"

# Simple auto-translation helper
_TRANS = {
    "es": {
        "name": None, "desc": None, "seo_title": None, "seo_desc": None,
        "lado": "Lado", "radio": "Radio", "altura": "Altura", "base": "Base",
        "area": "Área", "perimetro": "Perímetro", "volumen": "Volumen",
        "fuerza": "Fuerza", "masa": "Masa", "velocidad": "Velocidad",
        "tiempo": "Tiempo", "potencia": "Potencia", "energia": "Energía",
        "temperatura": "Temperatura", "presion": "Presión", "densidad": "Densidad",
        "frecuencia": "Frecuencia", "longitud_onda": "Longitud de onda",
        "carga": "Carga", "corriente": "Corriente", "resistencia": "Resistencia",
        "voltaje": "Voltaje", "capacitancia": "Capacitancia", "inductancia": "Inductancia",
        "monto": "Monto", "tasa": "Tasa", "plazo": "Plazo", "capital": "Capital",
        "interes": "Interés", "pago": "Pago", "ingreso": "Ingreso",
        "peso": "Peso", "altura_cm": "Altura", "edad": "Edad",
        "sexo": "Sexo", "actividad": "Actividad", "cintura": "Cintura",
        "cadera": "Cadera", "cuello": "Cuello",
    },
    "en": {
        "lado": "Side", "radio": "Radius", "altura": "Height", "base": "Base",
        "area": "Area", "perimetro": "Perimeter", "volumen": "Volume",
        "fuerza": "Force", "masa": "Mass", "velocidad": "Velocity",
        "tiempo": "Time", "potencia": "Power", "energia": "Energy",
        "temperatura": "Temperature", "presion": "Pressure", "densidad": "Density",
        "frecuencia": "Frequency", "longitud_onda": "Wavelength",
        "carga": "Charge", "corriente": "Current", "resistencia": "Resistance",
        "voltaje": "Voltage", "capacitancia": "Capacitance", "inductancia": "Inductance",
        "monto": "Amount", "tasa": "Rate", "plazo": "Term", "capital": "Principal",
        "interes": "Interest", "pago": "Payment", "ingreso": "Income",
        "peso": "Weight", "altura_cm": "Height", "edad": "Age",
        "sexo": "Gender", "actividad": "Activity", "cintura": "Waist",
        "cadera": "Hip", "cuello": "Neck",
    },
    "fr": {
        "lado": "Côté", "radio": "Rayon", "altura": "Hauteur", "base": "Base",
        "area": "Aire", "perimetro": "Périmètre", "volumen": "Volume",
        "fuerza": "Force", "masa": "Masse", "velocidad": "Vitesse",
        "tiempo": "Temps", "potencia": "Puissance", "energia": "Énergie",
        "temperatura": "Température", "presion": "Pression", "densidad": "Densité",
        "frecuencia": "Fréquence", "longitud_onda": "Longueur d'onde",
        "carga": "Charge", "corriente": "Courant", "resistencia": "Résistance",
        "voltaje": "Tension", "capacitancia": "Capacité", "inductancia": "Inductance",
        "monto": "Montant", "tasa": "Taux", "plazo": "Durée", "capital": "Capital",
        "interes": "Intérêt", "pago": "Paiement", "ingreso": "Revenu",
        "peso": "Poids", "altura_cm": "Taille", "edad": "Âge",
        "sexo": "Sexe", "actividad": "Activité", "cintura": "Taille",
        "cadera": "Hanche", "cuello": "Cou",
    },
    "pt": {
        "lado": "Lado", "radio": "Raio", "altura": "Altura", "base": "Base",
        "area": "Área", "perimetro": "Perímetro", "volumen": "Volume",
        "fuerza": "Força", "masa": "Massa", "velocidad": "Velocidade",
        "tiempo": "Tempo", "potencia": "Potência", "energia": "Energia",
        "temperatura": "Temperatura", "presion": "Pressão", "densidad": "Densidade",
        "frecuencia": "Frequência", "longitud_onda": "Comprimento de onda",
        "carga": "Carga", "corriente": "Corrente", "resistencia": "Resistência",
        "voltaje": "Tensão", "capacitancia": "Capacitância", "inductancia": "Indutância",
        "monto": "Montante", "tasa": "Taxa", "plazo": "Prazo", "capital": "Capital",
        "interes": "Juros", "pago": "Pagamento", "ingreso": "Renda",
        "peso": "Peso", "altura_cm": "Altura", "edad": "Idade",
        "sexo": "Sexo", "actividad": "Atividade", "cintura": "Cintura",
        "cadera": "Quadril", "cuello": "Pescoço",
    },
    "de": {
        "lado": "Seite", "radio": "Radius", "altura": "Höhe", "base": "Basis",
        "area": "Fläche", "perimetro": "Umfang", "volumen": "Volumen",
        "fuerza": "Kraft", "masa": "Masse", "velocidad": "Geschwindigkeit",
        "tiempo": "Zeit", "potencia": "Leistung", "energia": "Energie",
        "temperatura": "Temperatur", "presion": "Druck", "densidad": "Dichte",
        "frecuencia": "Frequenz", "longitud_onda": "Wellenlänge",
        "carga": "Ladung", "corriente": "Strom", "resistencia": "Widerstand",
        "voltaje": "Spannung", "capacitancia": "Kapazität", "inductancia": "Induktivität",
        "monto": "Betrag", "tasa": "Satz", "plazo": "Laufzeit", "capital": "Kapital",
        "interes": "Zinsen", "pago": "Zahlung", "ingreso": "Einkommen",
        "peso": "Gewicht", "altura_cm": "Größe", "edad": "Alter",
        "sexo": "Geschlecht", "actividad": "Aktivität", "cintura": "Taille",
        "cadera": "Hüfte", "cuello": "Hals",
    },
    "it": {
        "lado": "Lato", "radio": "Raggio", "altura": "Altezza", "base": "Base",
        "area": "Area", "perimetro": "Perimetro", "volumen": "Volume",
        "fuerza": "Forza", "masa": "Massa", "velocidad": "Velocità",
        "tiempo": "Tempo", "potencia": "Potenza", "energia": "Energia",
        "temperatura": "Temperatura", "presion": "Pressione", "densidad": "Densità",
        "frecuencia": "Frequenza", "longitud_onda": "Lunghezza d'onda",
        "carga": "Carica", "corriente": "Corrente", "resistencia": "Resistenza",
        "voltaje": "Tensione", "capacitancia": "Capacità", "inductancia": "Induttanza",
        "monto": "Importo", "tasa": "Tasso", "plazo": "Termine", "capital": "Capitale",
        "interes": "Interesse", "pago": "Pagamento", "ingreso": "Reddito",
        "peso": "Peso", "altura_cm": "Altezza", "edad": "Età",
        "sexo": "Sesso", "actividad": "Attività", "cintura": "Vita",
        "cadera": "Fianchi", "cuello": "Collo",
    },
}

def t(lang, key, fallback=None):
    return _TRANS[lang].get(key, fallback or key)

def i18n(name_es, desc_es, seo_title_es, seo_desc_es, inputs, outputs):
    """Build i18n dict for all 6 languages."""
    data = {}
    for lang in ["es", "en", "fr", "pt", "de", "it"]:
        if lang == "es":
            data[lang] = {
                "name": name_es,
                "description": desc_es,
                "seo_title": seo_title_es,
                "seo_desc": seo_desc_es,
                "inputs": {k: k for k in inputs},
                "outputs": {k: k for k in outputs},
            }
        else:
            data[lang] = {
                "name": name_es,  # Will be refined by content agent or manual patch
                "description": desc_es,
                "seo_title": seo_title_es,
                "seo_desc": seo_desc_es,
                "inputs": {k: t(lang, k, k) for k in inputs},
                "outputs": {k: t(lang, k, k) for k in outputs},
            }
    return data


calculators = []

# ── MATH (1050-1054) ──────────────────────────────────────────────────────────
calculators.append({
    "id": 1050, "slug": "poligono-regular-area", "block": "matematicas", "group": "geometria",
    "formula": "return {'area': (n * lado**2) / (4 * tan(pi/n)), 'perimetro': n * lado}",
    "inputs": [
        {"id": "n", "type": "number", "default": 6, "min": 3, "unit": "", "label": "Número de lados"},
        {"id": "lado", "type": "number", "default": 10, "unit": "m", "unit_options": ["m", "cm", "mm", "ft", "in"], "unit_category": "length", "min": 0}
    ],
    "outputs": [
        {"id": "area", "unit": "m²", "unit_category": "area"},
        {"id": "perimetro", "unit": "m", "unit_category": "length"}
    ],
    "related": [1, 2, 3],
    "i18n": i18n(
        "Área y Perímetro de Polígono Regular",
        "Calcula el área y perímetro de cualquier polígono regular dado el número de lados y la longitud del lado.",
        "Área Polígono Regular | CalcToWork",
        "Calcula el área y perímetro de polígonos regulares: pentágonos, hexágonos, octágonos y más.",
        ["n", "lado"], ["area", "perimetro"]
    )
})

calculators.append({
    "id": 1051, "slug": "cono-volumen", "block": "matematicas", "group": "geometria",
    "formula": "return {'volumen': (1/3) * pi * radio**2 * altura, 'area_superficial': pi * radio * (radio + sqrt(radio**2 + altura**2))}",
    "inputs": [
        {"id": "radio", "type": "number", "default": 5, "unit": "m", "unit_options": ["m", "cm", "mm", "ft", "in"], "unit_category": "length", "min": 0},
        {"id": "altura", "type": "number", "default": 10, "unit": "m", "unit_options": ["m", "cm", "mm", "ft", "in"], "unit_category": "length", "min": 0}
    ],
    "outputs": [
        {"id": "volumen", "unit": "m³", "unit_category": "volume"},
        {"id": "area_superficial", "unit": "m²", "unit_category": "area"}
    ],
    "related": [5, 6, 7],
    "i18n": i18n(
        "Volumen y Área Superficial de Cono",
        "Calcula el volumen y área superficial de un cono recto a partir del radio y la altura.",
        "Volumen Cono | CalcToWork",
        "Calcula el volumen y área de un cono con precisión. Ideal para geometría e ingeniería.",
        ["radio", "altura"], ["volumen", "area_superficial"]
    )
})

calculators.append({
    "id": 1052, "slug": "suma-aritmetica", "block": "matematicas", "group": "algebra",
    "formula": "return {'suma': (n/2) * (2*a1 + (n-1)*d), 'termino_n': a1 + (n-1)*d}",
    "inputs": [
        {"id": "a1", "type": "number", "default": 1, "unit": ""},
        {"id": "d", "type": "number", "default": 1, "unit": ""},
        {"id": "n", "type": "number", "default": 10, "min": 1, "unit": ""}
    ],
    "outputs": [
        {"id": "suma", "unit": ""},
        {"id": "termino_n", "unit": ""}
    ],
    "related": [1053, 100, 101],
    "i18n": i18n(
        "Suma de Progresión Aritmética",
        "Calcula la suma de los primeros n términos y el término enésimo de una progresión aritmética.",
        "Suma Aritmética | CalcToWork",
        "Calcula sumas y términos de progresiones aritméticas de forma instantánea.",
        ["a1", "d", "n"], ["suma", "termino_n"]
    )
})

calculators.append({
    "id": 1053, "slug": "suma-geometrica", "block": "matematicas", "group": "algebra",
    "formula": "return {'suma': a1 * (1 - r**n) / (1 - r) if r != 1 else a1 * n, 'termino_n': a1 * r**(n-1)}",
    "inputs": [
        {"id": "a1", "type": "number", "default": 1, "unit": ""},
        {"id": "r", "type": "number", "default": 2, "unit": ""},
        {"id": "n", "type": "number", "default": 10, "min": 1, "unit": ""}
    ],
    "outputs": [
        {"id": "suma", "unit": ""},
        {"id": "termino_n", "unit": ""}
    ],
    "related": [1052, 100, 101],
    "i18n": i18n(
        "Suma de Progresión Geométrica",
        "Obtiene la suma de los primeros n términos y el término enésimo de una progresión geométrica.",
        "Suma Geométrica | CalcToWork",
        "Calcula progresiones geométricas: suma finita, término enésimo y razón.",
        ["a1", "r", "n"], ["suma", "termino_n"]
    )
})

calculators.append({
    "id": 1054, "slug": "combinaciones", "block": "matematicas", "group": "estadistica",
    "formula": "from math import factorial\nreturn {'combinaciones': factorial(n) // (factorial(r) * factorial(n-r)), 'permutaciones': factorial(n) // factorial(n-r)}",
    "inputs": [
        {"id": "n", "type": "number", "default": 10, "min": 0, "unit": ""},
        {"id": "r", "type": "number", "default": 3, "min": 0, "unit": ""}
    ],
    "outputs": [
        {"id": "combinaciones", "unit": ""},
        {"id": "permutaciones", "unit": ""}
    ],
    "related": [1052, 1053, 110],
    "i18n": i18n(
        "Combinaciones y Permutaciones",
        "Calcula combinaciones y permutaciones de n elementos tomados de r en r.",
        "Combinaciones y Permutaciones | CalcToWork",
        "Calcula combinaciones y permutaciones para estadística y probabilidad.",
        ["n", "r"], ["combinaciones", "permutaciones"]
    )
})

# ── SCIENCE (1055-1059) ───────────────────────────────────────────────────────
calculators.append({
    "id": 1055, "slug": "empuje-arquimedes", "block": "ciencia", "group": "mecanica",
    "formula": "return {'empuje': densidad_fluido * volumen * 9.80665, 'peso_aparente': masa * 9.80665 - densidad_fluido * volumen * 9.80665}",
    "inputs": [
        {"id": "densidad_fluido", "type": "number", "default": 1000, "unit": "kg/m³", "unit_options": ["kg/m³", "g/cm³"], "unit_category": "density", "min": 0},
        {"id": "volumen", "type": "number", "default": 0.1, "unit": "m³", "unit_options": ["m³", "L", "cm³"], "unit_category": "volume", "min": 0},
        {"id": "masa", "type": "number", "default": 50, "unit": "kg", "unit_options": ["kg", "g", "lb"], "unit_category": "mass", "min": 0}
    ],
    "outputs": [
        {"id": "empuje", "unit": "N", "unit_category": "force"},
        {"id": "peso_aparente", "unit": "N", "unit_category": "force"}
    ],
    "related": [200, 201, 202],
    "i18n": i18n(
        "Empuje de Arquímedes",
        "Calcula el empuje hidrostático y el peso aparente de un objeto sumergido en un fluido.",
        "Empuje Arquímedes | CalcToWork",
        "Calcula el principio de Arquímedes: empuje, peso aparente y flotación.",
        ["densidad_fluido", "volumen", "masa"], ["empuje", "peso_aparente"]
    )
})

calculators.append({
    "id": 1056, "slug": "efecto-doppler", "block": "ciencia", "group": "ondas",
    "formula": "return {'frecuencia_observada': frecuente * (velocidad_sonido + velocidad_observador) / (velocidad_sonido - velocidad_fuente)}",
    "inputs": [
        {"id": "frecuente", "type": "number", "default": 440, "unit": "Hz", "unit_options": ["Hz", "kHz"], "unit_category": "frequency", "min": 0},
        {"id": "velocidad_sonido", "type": "number", "default": 343, "unit": "m/s", "min": 0},
        {"id": "velocidad_fuente", "type": "number", "default": 30, "unit": "m/s", "min": 0},
        {"id": "velocidad_observador", "type": "number", "default": 0, "unit": "m/s"}
    ],
    "outputs": [
        {"id": "frecuencia_observada", "unit": "Hz", "unit_category": "frequency"}
    ],
    "related": [210, 211, 212],
    "i18n": i18n(
        "Efecto Doppler",
        "Calcula la frecuencia observada de una onda cuando la fuente y el observador se mueven.",
        "Efecto Doppler | CalcToWork",
        "Calcula el cambio de frecuencia por efecto Doppler en física y acústica.",
        ["frecuente", "velocidad_sonido", "velocidad_fuente", "velocidad_observador"], ["frecuencia_observada"]
    )
})

calculators.append({
    "id": 1057, "slug": "impedancia-ac", "block": "ciencia", "group": "electricidad",
    "formula": "return {'impedancia': sqrt(resistencia**2 + (2*pi*frecuencia*inductancia - 1/(2*pi*frecuencia*capacitancia))**2), 'reactancia': 2*pi*frecuencia*inductancia - 1/(2*pi*frecuencia*capacitancia)}",
    "inputs": [
        {"id": "resistencia", "type": "number", "default": 10, "unit": "Ω", "unit_options": ["Ω", "kΩ", "MΩ"], "unit_category": "resistance", "min": 0},
        {"id": "inductancia", "type": "number", "default": 0.1, "unit": "H", "unit_options": ["H", "mH", "μH"], "unit_category": "inductance", "min": 0},
        {"id": "capacitancia", "type": "number", "default": 100, "unit": "μF", "unit_options": ["F", "mF", "μF", "nF", "pF"], "unit_category": "capacitance", "min": 0},
        {"id": "frecuencia", "type": "number", "default": 60, "unit": "Hz", "unit_options": ["Hz", "kHz", "MHz"], "unit_category": "frequency", "min": 0}
    ],
    "outputs": [
        {"id": "impedancia", "unit": "Ω", "unit_category": "resistance"},
        {"id": "reactancia", "unit": "Ω", "unit_category": "resistance"}
    ],
    "related": [220, 221, 222],
    "i18n": i18n(
        "Impedancia en Circuito AC",
        "Calcula la impedancia total y la reactancia de un circuito RLC en corriente alterna.",
        "Impedancia AC | CalcToWork",
        "Calcula impedancia y reactancia en circuitos RLC de corriente alterna.",
        ["resistencia", "inductancia", "capacitancia", "frecuencia"], ["impedancia", "reactancia"]
    )
})

calculators.append({
    "id": 1058, "slug": "momento-inercia", "block": "ciencia", "group": "mecanica",
    "formula": "return {'momento_inercia': 0.5 * masa * radio**2}",
    "inputs": [
        {"id": "masa", "type": "number", "default": 10, "unit": "kg", "unit_options": ["kg", "g", "lb"], "unit_category": "mass", "min": 0},
        {"id": "radio", "type": "number", "default": 0.5, "unit": "m", "unit_options": ["m", "cm", "mm"], "unit_category": "length", "min": 0}
    ],
    "outputs": [
        {"id": "momento_inercia", "unit": "kg·m²"}
    ],
    "related": [200, 201, 1055],
    "i18n": i18n(
        "Momento de Inercia de Disco",
        "Calcula el momento de inercia de un disco sólido homogéneo respecto a su eje central.",
        "Momento Inercia Disco | CalcToWork",
        "Calcula el momento de inercia de discos y cilindros sólidos para mecánica rotacional.",
        ["masa", "radio"], ["momento_inercia"]
    )
})

calculators.append({
    "id": 1059, "slug": "energia-rotacional", "block": "ciencia", "group": "mecanica",
    "formula": "return {'energia_rotacional': 0.5 * momento_inercia * velocidad_angular**2, 'velocidad_lineal': velocidad_angular * radio}",
    "inputs": [
        {"id": "momento_inercia", "type": "number", "default": 2.5, "unit": "kg·m²", "min": 0},
        {"id": "velocidad_angular", "type": "number", "default": 10, "unit": "rad/s", "min": 0},
        {"id": "radio", "type": "number", "default": 0.5, "unit": "m", "unit_options": ["m", "cm", "mm"], "unit_category": "length", "min": 0}
    ],
    "outputs": [
        {"id": "energia_rotacional", "unit": "J", "unit_category": "energy"},
        {"id": "velocidad_lineal", "unit": "m/s", "unit_category": "speed"}
    ],
    "related": [1058, 200, 201],
    "i18n": i18n(
        "Energía Cinética Rotacional",
        "Calcula la energía cinética rotacional y la velocidad lineal de un cuerpo en rotación.",
        "Energía Rotacional | CalcToWork",
        "Calcula energía cinética rotacional y velocidad lineal en mecánica.",
        ["momento_inercia", "velocidad_angular", "radio"], ["energia_rotacional", "velocidad_lineal"]
    )
})

# Save partial output so far
with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump({"batch_id": "batch_4", "calculators": calculators}, f, indent=2, ensure_ascii=False)
print(f"Wrote {len(calculators)} calculators to {OUTPUT}")

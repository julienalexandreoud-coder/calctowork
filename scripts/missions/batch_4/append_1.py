# Append remaining calculators to batch_4 schemas
import json, math
from pathlib import Path

OUTPUT = Path(r"C:\Microsaas\obra\scripts\missions\batch_4\schemas.json")
with open(OUTPUT, "r", encoding="utf-8") as f:
    data = json.load(f)
calculators = data["calculators"]

def i18n(name_es, desc_es, seo_title_es, seo_desc_es, inputs, outputs):
    trans = {
        "es": {"name": name_es, "description": desc_es, "seo_title": seo_title_es, "seo_desc": seo_desc_es,
               "inputs": {k: k for k in inputs}, "outputs": {k: k for k in outputs}},
        "en": {"name": name_es, "description": desc_es, "seo_title": seo_title_es, "seo_desc": seo_desc_es,
               "inputs": {k: k for k in inputs}, "outputs": {k: k for k in outputs}},
        "fr": {"name": name_es, "description": desc_es, "seo_title": seo_title_es, "seo_desc": seo_desc_es,
               "inputs": {k: k for k in inputs}, "outputs": {k: k for k in outputs}},
        "pt": {"name": name_es, "description": desc_es, "seo_title": seo_title_es, "seo_desc": seo_desc_es,
               "inputs": {k: k for k in inputs}, "outputs": {k: k for k in outputs}},
        "de": {"name": name_es, "description": desc_es, "seo_title": seo_title_es, "seo_desc": seo_desc_es,
               "inputs": {k: k for k in inputs}, "outputs": {k: k for k in outputs}},
        "it": {"name": name_es, "description": desc_es, "seo_title": seo_title_es, "seo_desc": seo_desc_es,
               "inputs": {k: k for k in inputs}, "outputs": {k: k for k in outputs}},
    }
    return trans

# ── HEALTH (1060-1064) ────────────────────────────────────────────────────────
calculators.append({"id": 1060, "slug": "grasa-corporal-marina", "block": "salud", "group": "fitness",
    "formula": "return {'grasa_corporal': 495 / (1.0324 - 0.19077 * log10(cintura - cuello) + 0.15456 * log10(altura_cm)) - 450 if sexo == 'hombre' else 495 / (1.29579 - 0.35004 * log10(cintura + cadera - cuello) + 0.22100 * log10(altura_cm)) - 450}",
    "inputs": [
        {"id": "cintura", "type": "number", "default": 80, "unit": "cm", "unit_options": ["cm", "in"], "unit_category": "length", "min": 0},
        {"id": "cuello", "type": "number", "default": 35, "unit": "cm", "unit_options": ["cm", "in"], "unit_category": "length", "min": 0},
        {"id": "altura_cm", "type": "number", "default": 170, "unit": "cm", "unit_options": ["cm", "ft"], "unit_category": "length", "min": 0},
        {"id": "sexo", "type": "select", "options": [{"value": "hombre", "label": "Hombre"}, {"value": "mujer", "label": "Mujer"}]},
        {"id": "cadera", "type": "number", "default": 90, "unit": "cm", "unit_options": ["cm", "in"], "unit_category": "length", "min": 0}
    ],
    "outputs": [{"id": "grasa_corporal", "unit": "%"}],
    "related": [300, 301, 302], "i18n": i18n("Grasa Corporal Método Marina", "Estima el porcentaje de grasa corporal con el método de la Marina de EE.UU.", "Grasa Corporal Marina | CalcToWork", "Calcula tu porcentaje de grasa corporal con la fórmula de la Marina de EE.UU.", ["cintura", "cuello", "altura_cm", "sexo", "cadera"], ["grasa_corporal"])})

calculators.append({"id": 1061, "slug": "tasa-metabolica-mifflin", "block": "salud", "group": "fitness",
    "formula": "return {'tmb': (10 * peso + 6.25 * altura_cm - 5 * edad + 5) if sexo == 'hombre' else (10 * peso + 6.25 * altura_cm - 5 * edad - 161)}",
    "inputs": [
        {"id": "peso", "type": "number", "default": 70, "unit": "kg", "unit_options": ["kg", "lb"], "unit_category": "mass", "min": 0},
        {"id": "altura_cm", "type": "number", "default": 170, "unit": "cm", "unit_options": ["cm", "ft"], "unit_category": "length", "min": 0},
        {"id": "edad", "type": "number", "default": 30, "unit": "años", "min": 0},
        {"id": "sexo", "type": "select", "options": [{"value": "hombre", "label": "Hombre"}, {"value": "mujer", "label": "Mujer"}]}
    ],
    "outputs": [{"id": "tmb", "unit": "kcal/día"}],
    "related": [300, 301, 417], "i18n": i18n("Tasa Metabólica Basal Mifflin-St Jeor", "Calcula la TMB con la ecuación de Mifflin-St Jeor, más precisa que Harris-Benedict.", "TMB Mifflin-St Jeor | CalcToWork", "Calcula tu metabolismo basal con la fórmula más precisa de Mifflin-St Jeor.", ["peso", "altura_cm", "edad", "sexo"], ["tmb"])})

calculators.append({"id": 1062, "slug": "agua-diaria", "block": "salud", "group": "bienestar",
    "formula": "return {'agua_recomendada': peso * 0.033 + (tiempo_ejercicio * 0.5) + (temperatura > 25) * 0.5}",
    "inputs": [
        {"id": "peso", "type": "number", "default": 70, "unit": "kg", "unit_options": ["kg", "lb"], "unit_category": "mass", "min": 0},
        {"id": "tiempo_ejercicio", "type": "number", "default": 30, "unit": "min", "unit_options": ["min", "h"], "unit_category": "time", "min": 0},
        {"id": "temperatura", "type": "number", "default": 20, "unit": "°C", "unit_options": ["°C", "°F"], "unit_category": "temperature"}
    ],
    "outputs": [{"id": "agua_recomendada", "unit": "L", "unit_category": "volume"}],
    "related": [300, 301, 1061], "i18n": i18n("Ingesta Diaria de Agua", "Calcula la cantidad de agua recomendada según peso, ejercicio y temperatura ambiental.", "Agua Diaria Recomendada | CalcToWork", "Calcula cuánta agua debes beber al día según tu peso y actividad.", ["peso", "tiempo_ejercicio", "temperatura"], ["agua_recomendada"])})

calculators.append({"id": 1063, "slug": "repeticion-maxima-brzycki", "block": "salud", "group": "fitness",
    "formula": "return {'rm': peso_levantado / (1.0278 - 0.0278 * repeticiones)}",
    "inputs": [
        {"id": "peso_levantado", "type": "number", "default": 80, "unit": "kg", "unit_options": ["kg", "lb"], "unit_category": "mass", "min": 0},
        {"id": "repeticiones", "type": "number", "default": 5, "min": 1, "max": 12, "unit": ""}
    ],
    "outputs": [{"id": "rm", "unit": "kg", "unit_category": "mass"}],
    "related": [300, 301, 1060], "i18n": i18n("Repetición Máxima Brzycki", "Estima tu 1RM (repetición máxima) a partir del peso levantado y las repeticiones.", "1RM Brzycki | CalcToWork", "Calcula tu repetición máxima con la fórmula de Brzycki para entrenamiento de fuerza.", ["peso_levantado", "repeticiones"], ["rm"])})

calculators.append({"id": 1064, "slug": "proteina-diaria", "block": "salud", "group": "nutricion",
    "formula": "return {'proteina_min': peso * 0.8, 'proteina_max': peso * 2.0, 'proteina_recomendada': peso * 1.6}",
    "inputs": [
        {"id": "peso", "type": "number", "default": 70, "unit": "kg", "unit_options": ["kg", "lb"], "unit_category": "mass", "min": 0},
        {"id": "objetivo", "type": "select", "options": [{"value": "mantener", "label": "Mantener"}, {"value": "ganar_musculo", "label": "Ganar músculo"}, {"value": "perder_grasa", "label": "Perder grasa"}]}
    ],
    "outputs": [
        {"id": "proteina_min", "unit": "g", "unit_category": "mass"},
        {"id": "proteina_max", "unit": "g", "unit_category": "mass"},
        {"id": "proteina_recomendada", "unit": "g", "unit_category": "mass"}
    ],
    "related": [300, 301, 1061], "i18n": i18n("Proteína Diaria Recomendada", "Calcula la ingesta diaria de proteína según tu peso y objetivo físico.", "Proteína Diaria | CalcToWork", "Calcula cuánta proteína necesitas al día para ganar músculo o perder grasa.", ["peso", "objetivo"], ["proteina_min", "proteina_max", "proteina_recomendada"])})

# ── FINANCE (1065-1069) ───────────────────────────────────────────────────────
calculators.append({"id": 1065, "slug": "rentabilidad-dividendo", "block": "finanzas", "group": "inversion",
    "formula": "return {'dividend_yield': (dividendo_anual / precio_accion) * 100}",
    "inputs": [
        {"id": "dividendo_anual", "type": "number", "default": 2, "unit": "€", "min": 0},
        {"id": "precio_accion", "type": "number", "default": 50, "unit": "€", "min": 0}
    ],
    "outputs": [{"id": "dividend_yield", "unit": "%"}],
    "related": [400, 401, 402], "i18n": i18n("Rentabilidad por Dividendo", "Calcula el dividend yield de una acción a partir del dividendo anual y el precio.", "Dividend Yield | CalcToWork", "Calcula la rentabilidad por dividendo de acciones e inversiones.", ["dividendo_anual", "precio_accion"], ["dividend_yield"])})

calculators.append({"id": 1066, "slug": "periodo-recuperacion", "block": "finanzas", "group": "inversion",
    "formula": "return {'periodo': inversion_inicial / flujo_anual}",
    "inputs": [
        {"id": "inversion_inicial", "type": "number", "default": 10000, "unit": "€", "min": 0},
        {"id": "flujo_anual", "type": "number", "default": 2000, "unit": "€", "min": 0}
    ],
    "outputs": [{"id": "periodo", "unit": "años"}],
    "related": [400, 401, 1065], "i18n": i18n("Periodo de Recuperación", "Calcula el payback period: tiempo necesario para recuperar una inversión inicial.", "Payback Period | CalcToWork", "Calcula el periodo de recuperación de inversiones y proyectos.", ["inversion_inicial", "flujo_anual"], ["periodo"])})

calculators.append({"id": 1067, "slug": "impuesto-ganancias-capital", "block": "finanzas", "group": "impuestos",
    "formula": "return {'ganancia': precio_venta - precio_compra, 'impuesto': max(0, (precio_venta - precio_compra) * tasa_impuesto / 100)}",
    "inputs": [
        {"id": "precio_compra", "type": "number", "default": 100, "unit": "€", "min": 0},
        {"id": "precio_venta", "type": "number", "default": 150, "unit": "€", "min": 0},
        {"id": "tasa_impuesto", "type": "number", "default": 19, "unit": "%", "min": 0}
    ],
    "outputs": [
        {"id": "ganancia", "unit": "€"},
        {"id": "impuesto", "unit": "€"}
    ],
    "related": [400, 401, 402], "i18n": i18n("Impuesto sobre Ganancias de Capital", "Calcula el impuesto a pagar por la venta de un activo con plusvalía.", "Impuesto Ganancias Capital | CalcToWork", "Calcula el impuesto sobre ganancias de capital en inversiones y bienes.", ["precio_compra", "precio_venta", "tasa_impuesto"], ["ganancia", "impuesto"])})

calculators.append({"id": 1068, "slug": "tipo-cambio-comision", "block": "finanzas", "group": "cambio",
    "formula": "return {'monto_recibido': monto * tipo_cambio * (1 - comision / 100)}",
    "inputs": [
        {"id": "monto", "type": "number", "default": 1000, "unit": "€", "min": 0},
        {"id": "tipo_cambio", "type": "number", "default": 1.08, "unit": ""},
        {"id": "comision", "type": "number", "default": 1.5, "unit": "%", "min": 0}
    ],
    "outputs": [{"id": "monto_recibido", "unit": "$"}],
    "related": [400, 401, 402], "i18n": i18n("Tipo de Cambio con Comisión", "Calcula el monto recibido en una conversión de divisas incluyendo comisiones.", "Cambio Divisa Comisión | CalcToWork", "Calcula conversiones de moneda con comisiones incluidas de forma transparente.", ["monto", "tipo_cambio", "comision"], ["monto_recibido"])})

calculators.append({"id": 1069, "slug": "punto-equilibrio", "block": "finanzas", "group": "empresa",
    "formula": "return {'punto_equilibrio': costes_fijos / (precio_venta - coste_variable), 'ingreso_necesario': costes_fijos / (1 - coste_variable / precio_venta)}",
    "inputs": [
        {"id": "costes_fijos", "type": "number", "default": 5000, "unit": "€", "min": 0},
        {"id": "precio_venta", "type": "number", "default": 50, "unit": "€", "min": 0},
        {"id": "coste_variable", "type": "number", "default": 30, "unit": "€", "min": 0}
    ],
    "outputs": [
        {"id": "punto_equilibrio", "unit": "unidades"},
        {"id": "ingreso_necesario", "unit": "€"}
    ],
    "related": [400, 401, 402], "i18n": i18n("Punto de Equilibrio", "Calcula el punto de equilibrio de un negocio: unidades a vender para cubrir costes.", "Punto Equilibrio | CalcToWork", "Calcula el break-even point de tu negocio o proyecto.", ["costes_fijos", "precio_venta", "coste_variable"], ["punto_equilibrio", "ingreso_necesario"])})

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump({"batch_id": "batch_4", "calculators": calculators}, f, indent=2, ensure_ascii=False)
print(f"Wrote {len(calculators)} calculators to {OUTPUT}")

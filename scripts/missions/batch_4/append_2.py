# Append remaining 30 calculators to batch_4 schemas
import json
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

# ── CHEMISTRY (1070-1074) ─────────────────────────────────────────────────────
calculators.append({"id": 1070, "slug": "masa-molar", "block": "quimica", "group": "moles",
    "formula": "return {'masa_molar': sum(float(x) for x in str(formula_quimica).split('+'))}",
    "inputs": [
        {"id": "formula_quimica", "type": "text", "default": "18", "unit": "g/mol"}
    ],
    "outputs": [{"id": "masa_molar", "unit": "g/mol"}],
    "related": [1000, 1001, 1002], "i18n": i18n("Masa Molar", "Calcula la masa molar de un compuesto a partir de la suma de masas atómicas.", "Masa Molar | CalcToWork", "Calcula la masa molar de compuestos químicos para reacciones y laboratorio.", ["formula_quimica"], ["masa_molar"])})

calculators.append({"id": 1071, "slug": "ph-hidrogeno", "block": "quimica", "group": "acidos",
    "formula": "from math import log10\nreturn {'ph': -log10(concentracion_h), 'poh': 14 + log10(concentracion_h)}",
    "inputs": [
        {"id": "concentracion_h", "type": "number", "default": 1e-7, "unit": "mol/L", "min": 0}
    ],
    "outputs": [
        {"id": "ph", "unit": ""},
        {"id": "poh", "unit": ""}
    ],
    "related": [1000, 1001, 1070], "i18n": i18n("pH y pOH", "Calcula el pH y pOH de una solución a partir de la concentración de iones hidrógeno.", "pH pOH | CalcToWork", "Calcula el pH y pOH de soluciones químicas de forma precisa.", ["concentracion_h"], ["ph", "poh"])})

calculators.append({"id": 1072, "slug": "gas-ideal", "block": "quimica", "group": "gases",
    "formula": "return {'volumen': (moles * 0.0821 * temperatura) / presion, 'presion': (moles * 0.0821 * temperatura) / volumen_gas, 'moles': (presion * volumen_gas) / (0.0821 * temperatura)}",
    "inputs": [
        {"id": "presion", "type": "number", "default": 1, "unit": "atm", "unit_options": ["atm", "Pa", "bar"], "unit_category": "pressure", "min": 0},
        {"id": "volumen_gas", "type": "number", "default": 22.4, "unit": "L", "unit_options": ["L", "mL", "m³"], "unit_category": "volume", "min": 0},
        {"id": "moles", "type": "number", "default": 1, "unit": "mol", "min": 0},
        {"id": "temperatura", "type": "number", "default": 273, "unit": "K", "unit_options": ["K", "°C"], "unit_category": "temperature", "min": 0}
    ],
    "outputs": [
        {"id": "volumen", "unit": "L", "unit_category": "volume"},
        {"id": "presion_out", "unit": "atm", "unit_category": "pressure"},
        {"id": "moles_out", "unit": "mol"}
    ],
    "related": [1000, 1001, 1070], "i18n": i18n("Ley de los Gases Ideales", "Calcula presión, volumen, moles o temperatura con la ecuación PV = nRT.", "Gas Ideal PV=nRT | CalcToWork", "Calcula variables de gases ideales con la ley de PV=nRT.", ["presion", "volumen_gas", "moles", "temperatura"], ["volumen", "presion_out", "moles_out"])})

calculators.append({"id": 1073, "slug": "molaridad", "block": "quimica", "group": "concentracion",
    "formula": "return {'molaridad': moles / volumen, 'molalidad': moles / (masa_solvente / 1000)}",
    "inputs": [
        {"id": "moles", "type": "number", "default": 1, "unit": "mol", "min": 0},
        {"id": "volumen", "type": "number", "default": 1, "unit": "L", "unit_options": ["L", "mL"], "unit_category": "volume", "min": 0},
        {"id": "masa_solvente", "type": "number", "default": 1000, "unit": "g", "unit_options": ["g", "kg"], "unit_category": "mass", "min": 0}
    ],
    "outputs": [
        {"id": "molaridad", "unit": "mol/L"},
        {"id": "molalidad", "unit": "mol/kg"}
    ],
    "related": [1000, 1001, 1070], "i18n": i18n("Molaridad y Molalidad", "Calcula la molaridad y molalidad de una solución química.", "Molaridad Molalidad | CalcToWork", "Calcula concentraciones químicas: molaridad, molalidad y normalidad.", ["moles", "volumen", "masa_solvente"], ["molaridad", "molalidad"])})

calculators.append({"id": 1074, "slug": "dilucion", "block": "quimica", "group": "concentracion",
    "formula": "return {'volumen_final': (concentracion_inicial * volumen_inicial) / concentracion_final, 'concentracion_final': (concentracion_inicial * volumen_inicial) / volumen_final}",
    "inputs": [
        {"id": "concentracion_inicial", "type": "number", "default": 1, "unit": "M", "min": 0},
        {"id": "volumen_inicial", "type": "number", "default": 100, "unit": "mL", "unit_options": ["L", "mL"], "unit_category": "volume", "min": 0},
        {"id": "concentracion_final", "type": "number", "default": 0.1, "unit": "M", "min": 0},
        {"id": "volumen_final", "type": "number", "default": 1000, "unit": "mL", "unit_options": ["L", "mL"], "unit_category": "volume", "min": 0}
    ],
    "outputs": [
        {"id": "volumen_final", "unit": "mL", "unit_category": "volume"},
        {"id": "concentracion_final", "unit": "M"}
    ],
    "related": [1000, 1001, 1073], "i18n": i18n("Dilución C1V1=C2V2", "Calcula diluciones químicas con la ecuación C1V1 = C2V2.", "Dilución Química | CalcToWork", "Calcula diluciones de soluciones químicas con C1V1=C2V2.", ["concentracion_inicial", "volumen_inicial", "concentracion_final", "volumen_final"], ["volumen_final", "concentracion_final"])})

# ── ELECTRONICS (1075-1079) ───────────────────────────────────────────────────
calculators.append({"id": 1075, "slug": "codigo-colores-resistencia", "block": "electronica", "group": "componentes",
    "formula": "return {'resistencia': banda1 * 10 + banda2, 'tolerancia': banda3}",
    "inputs": [
        {"id": "banda1", "type": "select", "options": [{"value": 0, "label": "Negro"}, {"value": 1, "label": "Marrón"}, {"value": 2, "label": "Rojo"}, {"value": 3, "label": "Naranja"}, {"value": 4, "label": "Amarillo"}, {"value": 5, "label": "Verde"}, {"value": 6, "label": "Azul"}, {"value": 7, "label": "Violeta"}, {"value": 8, "label": "Gris"}, {"value": 9, "label": "Blanco"}]},
        {"id": "banda2", "type": "select", "options": [{"value": 0, "label": "Negro"}, {"value": 1, "label": "Marrón"}, {"value": 2, "label": "Rojo"}, {"value": 3, "label": "Naranja"}, {"value": 4, "label": "Amarillo"}, {"value": 5, "label": "Verde"}, {"value": 6, "label": "Azul"}, {"value": 7, "label": "Violeta"}, {"value": 8, "label": "Gris"}, {"value": 9, "label": "Blanco"}]},
        {"id": "banda3", "type": "select", "options": [{"value": 1, "label": "±1%"}, {"value": 2, "label": "±2%"}, {"value": 0.5, "label": "±0.5%"}, {"value": 0.25, "label": "±0.25%"}, {"value": 0.1, "label": "±0.1%"}, {"value": 0.05, "label": "±0.05%"}, {"value": 5, "label": "±5%"}, {"value": 10, "label": "±10%"}]}
    ],
    "outputs": [
        {"id": "resistencia", "unit": "Ω"},
        {"id": "tolerancia", "unit": "%"}
    ],
    "related": [1020, 1021, 1022], "i18n": i18n("Código de Colores de Resistencia", "Decodifica el valor y tolerancia de una resistencia por su código de colores.", "Código Colores Resistencia | CalcToWork", "Decodifica resistencias por código de colores de 4 y 5 bandas.", ["banda1", "banda2", "banda3"], ["resistencia", "tolerancia"])})

calculators.append({"id": 1076, "slug": "energia-capacitor", "block": "electronica", "group": "componentes",
    "formula": "return {'energia': 0.5 * capacitancia * voltaje**2}",
    "inputs": [
        {"id": "capacitancia", "type": "number", "default": 100, "unit": "μF", "unit_options": ["F", "mF", "μF", "nF", "pF"], "unit_category": "capacitance", "min": 0},
        {"id": "voltaje", "type": "number", "default": 12, "unit": "V", "unit_options": ["V", "mV", "kV"], "unit_category": "voltage", "min": 0}
    ],
    "outputs": [{"id": "energia", "unit": "J", "unit_category": "energy"}],
    "related": [1020, 1021, 1075], "i18n": i18n("Energía Almacenada en Capacitor", "Calcula la energía eléctrica almacenada en un capacitor.", "Energía Capacitor | CalcToWork", "Calcula la energía almacenada en condensadores y capacitores.", ["capacitancia", "voltaje"], ["energia"])})

calculators.append({"id": 1077, "slug": "divisor-voltaje", "block": "electronica", "group": "circuitos",
    "formula": "return {'voltaje_salida': voltaje_entrada * (r2 / (r1 + r2)), 'corriente': voltaje_entrada / (r1 + r2)}",
    "inputs": [
        {"id": "voltaje_entrada", "type": "number", "default": 12, "unit": "V", "unit_options": ["V", "mV", "kV"], "unit_category": "voltage", "min": 0},
        {"id": "r1", "type": "number", "default": 1000, "unit": "Ω", "unit_options": ["Ω", "kΩ", "MΩ"], "unit_category": "resistance", "min": 0},
        {"id": "r2", "type": "number", "default": 2000, "unit": "Ω", "unit_options": ["Ω", "kΩ", "MΩ"], "unit_category": "resistance", "min": 0}
    ],
    "outputs": [
        {"id": "voltaje_salida", "unit": "V", "unit_category": "voltage"},
        {"id": "corriente", "unit": "A", "unit_category": "current"}
    ],
    "related": [1020, 1021, 1076], "i18n": i18n("Divisor de Voltaje", "Calcula el voltaje de salida y la corriente en un divisor de voltaje resistivo.", "Divisor Voltaje | CalcToWork", "Calcula divisores de voltaje para circuitos electrónicos.", ["voltaje_entrada", "r1", "r2"], ["voltaje_salida", "corriente"])})

calculators.append({"id": 1078, "slug": "constante-tiempo-rc", "block": "electronica", "group": "circuitos",
    "formula": "return {'tau': resistencia * capacitancia, 'tiempo_carga': 5 * resistencia * capacitancia}",
    "inputs": [
        {"id": "resistencia", "type": "number", "default": 1000, "unit": "Ω", "unit_options": ["Ω", "kΩ", "MΩ"], "unit_category": "resistance", "min": 0},
        {"id": "capacitancia", "type": "number", "default": 100, "unit": "μF", "unit_options": ["F", "mF", "μF", "nF", "pF"], "unit_category": "capacitance", "min": 0}
    ],
    "outputs": [
        {"id": "tau", "unit": "s", "unit_category": "time"},
        {"id": "tiempo_carga", "unit": "s", "unit_category": "time"}
    ],
    "related": [1020, 1021, 1077], "i18n": i18n("Constante de Tiempo RC", "Calcula la constante de tiempo tau y el tiempo de carga de un circuito RC.", "Constante RC | CalcToWork", "Calcula la constante de tiempo de circuitos RC para electrónica.", ["resistencia", "capacitancia"], ["tau", "tiempo_carga"])})

calculators.append({"id": 1079, "slug": "puente-wheatstone", "block": "electronica", "group": "instrumentacion",
    "formula": "return {'resistencia_desconocida': (r2 / r1) * r3}",
    "inputs": [
        {"id": "r1", "type": "number", "default": 100, "unit": "Ω", "unit_options": ["Ω", "kΩ", "MΩ"], "unit_category": "resistance", "min": 0},
        {"id": "r2", "type": "number", "default": 100, "unit": "Ω", "unit_options": ["Ω", "kΩ", "MΩ"], "unit_category": "resistance", "min": 0},
        {"id": "r3", "type": "number", "default": 100, "unit": "Ω", "unit_options": ["Ω", "kΩ", "MΩ"], "unit_category": "resistance", "min": 0}
    ],
    "outputs": [{"id": "resistencia_desconocida", "unit": "Ω", "unit_category": "resistance"}],
    "related": [1020, 1021, 1078], "i18n": i18n("Puente de Wheatstone", "Calcula una resistencia desconocida con el puente de Wheatstone equilibrado.", "Puente Wheatstone | CalcToWork", "Calcula resistencias desconocidas con el puente de Wheatstone.", ["r1", "r2", "r3"], ["resistencia_desconocida"])})

# ── TRANSPORT (1080-1084) ─────────────────────────────────────────────────────
calculators.append({"id": 1080, "slug": "consumo-combustible", "block": "transporte", "group": "vehiculos",
    "formula": "return {'litros_100km': (litros / km) * 100, 'mpg_us': (km / litros) * 2.352, 'mpg_uk': (km / litros) * 2.825}",
    "inputs": [
        {"id": "litros", "type": "number", "default": 50, "unit": "L", "unit_options": ["L", "gal"], "unit_category": "volume", "min": 0},
        {"id": "km", "type": "number", "default": 500, "unit": "km", "unit_options": ["km", "mi"], "unit_category": "length", "min": 0}
    ],
    "outputs": [
        {"id": "litros_100km", "unit": "L/100km"},
        {"id": "mpg_us", "unit": "mpg"},
        {"id": "mpg_uk", "unit": "mpg"}
    ],
    "related": [1040, 1041, 1042], "i18n": i18n("Consumo de Combustible", "Convierte entre L/100km, MPG (US) y MPG (UK) para cualquier vehículo.", "Consumo Combustible | CalcToWork", "Calcula el consumo de combustible en L/100km y MPG.", ["litros", "km"], ["litros_100km", "mpg_us", "mpg_uk"])})

calculators.append({"id": 1081, "slug": "distancia-frenado", "block": "transporte", "group": "seguridad",
    "formula": "return {'distancia': (velocidad_ms**2) / (2 * coeficiente * 9.80665)}",
    "inputs": [
        {"id": "velocidad_ms", "type": "number", "default": 20, "unit": "m/s", "unit_options": ["m/s", "km/h", "mph"], "unit_category": "speed", "min": 0},
        {"id": "coeficiente", "type": "number", "default": 0.7, "unit": "", "min": 0}
    ],
    "outputs": [{"id": "distancia", "unit": "m", "unit_category": "length"}],
    "related": [1040, 1041, 1080], "i18n": i18n("Distancia de Frenado", "Calcula la distancia de frenado de un vehículo según velocidad y coeficiente de fricción.", "Distancia Frenado | CalcToWork", "Calcula la distancia de frenado según velocidad y adherencia.", ["velocidad_ms", "coeficiente"], ["distancia"])})

calculators.append({"id": 1082, "slug": "cilindrada-motor", "block": "transporte", "group": "mecanica",
    "formula": "return {'cilindrada': (pi / 4) * (diametro_cilindro**2) * carrera * numero_cilindros}",
    "inputs": [
        {"id": "diametro_cilindro", "type": "number", "default": 80, "unit": "mm", "unit_options": ["mm", "cm", "in"], "unit_category": "length", "min": 0},
        {"id": "carrera", "type": "number", "default": 90, "unit": "mm", "unit_options": ["mm", "cm", "in"], "unit_category": "length", "min": 0},
        {"id": "numero_cilindros", "type": "number", "default": 4, "min": 1, "unit": ""}
    ],
    "outputs": [{"id": "cilindrada", "unit": "cm³"}],
    "related": [1040, 1041, 1080], "i18n": i18n("Cilindrada del Motor", "Calcula la cilindrada total de un motor de combustión interna.", "Cilindrada Motor | CalcToWork", "Calcula la cilindrada de motores de gasolina y diésel.", ["diametro_cilindro", "carrera", "numero_cilindros"], ["cilindrada"])})

calculators.append({"id": 1083, "slug": "presion-neumaticos", "block": "transporte", "group": "mantenimiento",
    "formula": "return {'presion_recomendada': presion_base + (carga_extra * 0.02)}",
    "inputs": [
        {"id": "presion_base", "type": "number", "default": 2.2, "unit": "bar", "unit_options": ["bar", "psi", "kPa"], "unit_category": "pressure", "min": 0},
        {"id": "carga_extra", "type": "number", "default": 200, "unit": "kg", "unit_options": ["kg", "lb"], "unit_category": "mass", "min": 0}
    ],
    "outputs": [{"id": "presion_recomendada", "unit": "bar", "unit_category": "pressure"}],
    "related": [1040, 1041, 1082], "i18n": i18n("Presión de Neumáticos", "Calcula la presión recomendada de neumáticos según carga adicional del vehículo.", "Presión Neumáticos | CalcToWork", "Calcula la presión adecuada de neumáticos según carga.", ["presion_base", "carga_extra"], ["presion_recomendada"])})

calculators.append({"id": 1084, "slug": "tiempo-vuelo-viento", "block": "transporte", "group": "aereo",
    "formula": "return {'tiempo_ida': distancia / (velocidad_avion + velocidad_viento), 'tiempo_vuelta': distancia / (velocidad_avion - velocidad_viento)}",
    "inputs": [
        {"id": "distancia", "type": "number", "default": 1000, "unit": "km", "unit_options": ["km", "mi", "nmi"], "unit_category": "length", "min": 0},
        {"id": "velocidad_avion", "type": "number", "default": 900, "unit": "km/h", "unit_options": ["km/h", "mph", "knots"], "unit_category": "speed", "min": 0},
        {"id": "velocidad_viento", "type": "number", "default": 50, "unit": "km/h", "unit_options": ["km/h", "mph", "knots"], "unit_category": "speed", "min": 0}
    ],
    "outputs": [
        {"id": "tiempo_ida", "unit": "h", "unit_category": "time"},
        {"id": "tiempo_vuelta", "unit": "h", "unit_category": "time"}
    ],
    "related": [1040, 1041, 1080], "i18n": i18n("Tiempo de Vuelo con Viento", "Calcula el tiempo de vuelo considerando la velocidad del viento de frente o de cola.", "Tiempo Vuelo Viento | CalcToWork", "Calcula tiempos de vuelo con viento en contra y a favor.", ["distancia", "velocidad_avion", "velocidad_viento"], ["tiempo_ida", "tiempo_vuelta"])})

# ── PHOTOGRAPHY (1085-1086) ───────────────────────────────────────────────────
calculators.append({"id": 1085, "slug": "profundidad-campo", "block": "fotografia", "group": "optica",
    "formula": "return {'dof': (2 * distancia**2 * apertura * 0.03) / (longitud_focal**2)}",
    "inputs": [
        {"id": "longitud_focal", "type": "number", "default": 50, "unit": "mm", "unit_options": ["mm", "cm"], "unit_category": "length", "min": 0},
        {"id": "apertura", "type": "number", "default": 2.8, "unit": "f/", "min": 0},
        {"id": "distancia", "type": "number", "default": 3, "unit": "m", "unit_options": ["m", "ft"], "unit_category": "length", "min": 0}
    ],
    "outputs": [{"id": "dof", "unit": "m", "unit_category": "length"}],
    "related": [1030, 1031, 1032], "i18n": i18n("Profundidad de Campo", "Calcula la profundidad de campo aproximada para una configuración de cámara.", "Profundidad Campo | CalcToWork", "Calcula la profundidad de campo en fotografía según apertura y distancia.", ["longitud_focal", "apertura", "distancia"], ["dof"])})

calculators.append({"id": 1086, "slug": "numero-guia-flash", "block": "fotografia", "group": "iluminacion",
    "formula": "return {'distancia_maxima': numero_guia / apertura}",
    "inputs": [
        {"id": "numero_guia", "type": "number", "default": 36, "unit": "", "min": 0},
        {"id": "apertura", "type": "number", "default": 4, "unit": "f/", "min": 0}
    ],
    "outputs": [{"id": "distancia_maxima", "unit": "m", "unit_category": "length"}],
    "related": [1030, 1031, 1085], "i18n": i18n("Número Guía del Flash", "Calcula la distancia máxima de iluminación de un flash según su número guía.", "Número Guía Flash | CalcToWork", "Calcula el alcance de iluminación de flashes con el número guía.", ["numero_guia", "apertura"], ["distancia_maxima"])})

# ── WEATHER (1087-1089) ───────────────────────────────────────────────────────
calculators.append({"id": 1087, "slug": "indice-calor", "block": "clima", "group": "temperatura",
    "formula": "return {'indice_calor': -42.379 + 2.04901523*temperatura + 10.14333127*humedad - 0.22475541*temperatura*humedad - 6.83783e-3*temperatura**2 - 5.481717e-2*humedad**2 + 1.22874e-3*temperatura**2*humedad + 8.5282e-4*temperatura*humedad**2 - 1.99e-6*temperatura**2*humedad**2}",
    "inputs": [
        {"id": "temperatura", "type": "number", "default": 30, "unit": "°F", "unit_options": ["°F", "°C"], "unit_category": "temperature"},
        {"id": "humedad", "type": "number", "default": 60, "unit": "%", "min": 0, "max": 100}
    ],
    "outputs": [{"id": "indice_calor", "unit": "°F", "unit_category": "temperature"}],
    "related": [1045, 1046, 1047], "i18n": i18n("Índice de Calor", "Calcula el índice de calor (heat index) a partir de temperatura y humedad relativa.", "Índice Calor | CalcToWork", "Calcula el índice de calor y sensación térmica por humedad.", ["temperatura", "humedad"], ["indice_calor"])})

calculators.append({"id": 1088, "slug": "sensacion-frio-viento", "block": "clima", "group": "temperatura",
    "formula": "return {'sensacion_frio': 35.74 + 0.6215*temperatura_f - 35.75*(velocidad_viento**0.16) + 0.4275*temperatura_f*(velocidad_viento**0.16)}",
    "inputs": [
        {"id": "temperatura_f", "type": "number", "default": 20, "unit": "°F", "unit_options": ["°F", "°C"], "unit_category": "temperature"},
        {"id": "velocidad_viento", "type": "number", "default": 10, "unit": "mph", "unit_options": ["mph", "km/h", "m/s"], "unit_category": "speed", "min": 0}
    ],
    "outputs": [{"id": "sensacion_frio", "unit": "°F", "unit_category": "temperature"}],
    "related": [1045, 1046, 1087], "i18n": i18n("Sensación de Frío por Viento", "Calcula el wind chill: sensación térmica por efecto del viento en frío.", "Wind Chill | CalcToWork", "Calcula la sensación de frío por viento en climas fríos.", ["temperatura_f", "velocidad_viento"], ["sensacion_frio"])})

calculators.append({"id": 1089, "slug": "humedad-relativa-rocio", "block": "clima", "group": "humedad",
    "formula": "from math import exp\nreturn {'humedad_relativa': 100 * (exp((17.625 * punto_rocio) / (243.04 + punto_rocio)) / exp((17.625 * temperatura) / (243.04 + temperatura)))}",
    "inputs": [
        {"id": "temperatura", "type": "number", "default": 20, "unit": "°C", "unit_options": ["°C", "°F"], "unit_category": "temperature"},
        {"id": "punto_rocio", "type": "number", "default": 15, "unit": "°C", "unit_options": ["°C", "°F"], "unit_category": "temperature"}
    ],
    "outputs": [{"id": "humedad_relativa", "unit": "%"}],
    "related": [1045, 1046, 1087], "i18n": i18n("Humedad Relativa desde Punto de Rocío", "Calcula la humedad relativa a partir de la temperatura y el punto de rocío.", "Humedad Relativa Rocío | CalcToWork", "Calcula la humedad relativa con temperatura y punto de rocío.", ["temperatura", "punto_rocio"], ["humedad_relativa"])})

# ── UTILITIES (1090-1092) ─────────────────────────────────────────────────────
calculators.append({"id": 1090, "slug": "entropia-contrasena", "block": "utilidades", "group": "seguridad",
    "formula": "from math import log2\nreturn {'entropia': longitud * log2(conjunto_caracteres), 'fuerza': 'Débil' if longitud * log2(conjunto_caracteres) < 40 else ('Media' if longitud * log2(conjunto_caracteres) < 60 else 'Fuerte')}",
    "inputs": [
        {"id": "longitud", "type": "number", "default": 12, "min": 1, "unit": "caracteres"},
        {"id": "conjunto_caracteres", "type": "number", "default": 62, "min": 1, "unit": ""}
    ],
    "outputs": [
        {"id": "entropia", "unit": "bits"},
        {"id": "fuerza", "unit": ""}
    ],
    "related": [1048, 1049, 1050], "i18n": i18n("Entropía de Contraseña", "Calcula la entropía y fuerza de una contraseña según longitud y caracteres usados.", "Entropía Contraseña | CalcToWork", "Calcula la seguridad de contraseñas por entropía de información.", ["longitud", "conjunto_caracteres"], ["entropia", "fuerza"])})

calculators.append({"id": 1091, "slug": "contador-caracteres-texto", "block": "utilidades", "group": "texto",
    "formula": "return {'con_espacios': len(texto), 'sin_espacios': len(texto.replace(' ', '')), 'palabras': len(texto.split())}",
    "inputs": [
        {"id": "texto", "type": "text", "default": "Hola mundo", "unit": ""}
    ],
    "outputs": [
        {"id": "con_espacios", "unit": "caracteres"},
        {"id": "sin_espacios", "unit": "caracteres"},
        {"id": "palabras", "unit": "palabras"}
    ],
    "related": [1048, 1049, 1090], "i18n": i18n("Contador de Caracteres", "Cuenta caracteres, palabras y espacios de cualquier texto.", "Contador Caracteres | CalcToWork", "Cuenta caracteres con y sin espacios, y palabras en textos.", ["texto"], ["con_espacios", "sin_espacios", "palabras"])})

calculators.append({"id": 1092, "slug": "dias-habiles", "block": "utilidades", "group": "fechas",
    "formula": "return {'dias_habiles': dias_totales - (dias_totales // 7) * 2 - festivos}",
    "inputs": [
        {"id": "dias_totales", "type": "number", "default": 30, "min": 0, "unit": "días"},
        {"id": "festivos", "type": "number", "default": 2, "min": 0, "unit": "días"}
    ],
    "outputs": [{"id": "dias_habiles", "unit": "días"}],
    "related": [1048, 1049, 1091], "i18n": i18n("Días Hábiles", "Calcula los días hábiles restando fines de semana y festivos de un periodo.", "Días Hábiles | CalcToWork", "Calcula días laborables restando fines de semana y festivos.", ["dias_totales", "festivos"], ["dias_habiles"])})

# ── ENGINEERING (1093-1096) ───────────────────────────────────────────────────
calculators.append({"id": 1093, "slug": "deflexion-viga", "block": "ingenieria", "group": "estructuras",
    "formula": "return {'deflexion': (carga * longitud**3) / (3 * modulo_elastico * momento_inercia)}",
    "inputs": [
        {"id": "carga", "type": "number", "default": 1000, "unit": "N", "unit_options": ["N", "kN", "lbf"], "unit_category": "force", "min": 0},
        {"id": "longitud", "type": "number", "default": 2, "unit": "m", "unit_options": ["m", "cm", "mm", "ft"], "unit_category": "length", "min": 0},
        {"id": "modulo_elastico", "type": "number", "default": 200e9, "unit": "Pa", "unit_options": ["Pa", "GPa"], "unit_category": "pressure", "min": 0},
        {"id": "momento_inercia", "type": "number", "default": 1e-6, "unit": "m⁴", "min": 0}
    ],
    "outputs": [{"id": "deflexion", "unit": "m", "unit_category": "length"}],
    "related": [1, 2, 3], "i18n": i18n("Deflexión de Viga en Voladizo", "Calcula la deflexión máxima de una viga en voladizo con carga puntual.", "Deflexión Viga | CalcToWork", "Calcula la deflexión de vigas en voladizo para ingeniería civil.", ["carga", "longitud", "modulo_elastico", "momento_inercia"], ["deflexion"])})

calculators.append({"id": 1094, "slug": "par-apriete-tornillo", "block": "ingenieria", "group": "mecanica",
    "formula": "return {'par_apriete': coeficiente * diametro * carga_precarga}",
    "inputs": [
        {"id": "diametro", "type": "number", "default": 10, "unit": "mm", "unit_options": ["mm", "cm", "in"], "unit_category": "length", "min": 0},
        {"id": "carga_precarga", "type": "number", "default": 50000, "unit": "N", "unit_options": ["N", "kN"], "unit_category": "force", "min": 0},
        {"id": "coeficiente", "type": "number", "default": 0.2, "unit": "", "min": 0}
    ],
    "outputs": [{"id": "par_apriete", "unit": "N·m", "unit_category": "torque"}],
    "related": [1, 2, 1093], "i18n": i18n("Par de Apriete de Tornillo", "Calcula el par de apriete necesario para un tornillo según diámetro y precarga.", "Par Apriete Tornillo | CalcToWork", "Calcula el torque de apriete para tornillería industrial.", ["diametro", "carga_precarga", "coeficiente"], ["par_apriete"])})

calculators.append({"id": 1095, "slug": "constante-resorte", "block": "ingenieria", "group": "mecanica",
    "formula": "return {'constante': fuerza / deformacion, 'energia_almacenada': 0.5 * (fuerza / deformacion) * deformacion**2}",
    "inputs": [
        {"id": "fuerza", "type": "number", "default": 100, "unit": "N", "unit_options": ["N", "kN", "lbf"], "unit_category": "force", "min": 0},
        {"id": "deformacion", "type": "number", "default": 0.01, "unit": "m", "unit_options": ["m", "cm", "mm"], "unit_category": "length", "min": 0}
    ],
    "outputs": [
        {"id": "constante", "unit": "N/m", "unit_category": "spring_constant"},
        {"id": "energia_almacenada", "unit": "J", "unit_category": "energy"}
    ],
    "related": [1, 2, 1094], "i18n": i18n("Constante del Resorte", "Calcula la constante elástica y energía almacenada de un resorte por Ley de Hooke.", "Constante Resorte | CalcToWork", "Calcula la constante de resorte y energía por la Ley de Hooke.", ["fuerza", "deformacion"], ["constante", "energia_almacenada"])})

calculators.append({"id": 1096, "slug": "numero-reynolds", "block": "ingenieria", "group": "fluidos",
    "formula": "return {'reynolds': (densidad * velocidad * diametro) / viscosidad}",
    "inputs": [
        {"id": "densidad", "type": "number", "default": 1000, "unit": "kg/m³", "unit_options": ["kg/m³", "g/cm³"], "unit_category": "density", "min": 0},
        {"id": "velocidad", "type": "number", "default": 1, "unit": "m/s", "unit_options": ["m/s", "km/h"], "unit_category": "speed", "min": 0},
        {"id": "diametro", "type": "number", "default": 0.1, "unit": "m", "unit_options": ["m", "cm", "mm"], "unit_category": "length", "min": 0},
        {"id": "viscosidad", "type": "number", "default": 0.001, "unit": "Pa·s", "min": 0}
    ],
    "outputs": [{"id": "reynolds", "unit": ""}],
    "related": [1, 2, 1095], "i18n": i18n("Número de Reynolds", "Calcula el número de Reynolds para determinar el régimen de flujo laminar o turbulento.", "Número Reynolds | CalcToWork", "Calcula el número de Reynolds para flujo de fluidos en tuberías.", ["densidad", "velocidad", "diametro", "viscosidad"], ["reynolds"])})

# ── SPORTS (1097-1099) ────────────────────────────────────────────────────────
calculators.append({"id": 1097, "slug": "ritmo-carrera", "block": "deportes", "group": "running",
    "formula": "return {'ritmo_min_km': (tiempo_min / distancia), 'velocidad_kmh': (distancia / tiempo_min) * 60}",
    "inputs": [
        {"id": "distancia", "type": "number", "default": 10, "unit": "km", "unit_options": ["km", "mi", "m"], "unit_category": "length", "min": 0},
        {"id": "tiempo_min", "type": "number", "default": 50, "unit": "min", "unit_options": ["min", "h"], "unit_category": "time", "min": 0}
    ],
    "outputs": [
        {"id": "ritmo_min_km", "unit": "min/km"},
        {"id": "velocidad_kmh", "unit": "km/h", "unit_category": "speed"}
    ],
    "related": [300, 301, 302], "i18n": i18n("Ritmo de Carrera", "Calcula tu ritmo por kilómetro y velocidad media en carrera.", "Ritmo Carrera | CalcToWork", "Calcula el ritmo de carrera por km y velocidad media.", ["distancia", "tiempo_min"], ["ritmo_min_km", "velocidad_kmh"])})

calculators.append({"id": 1098, "slug": "handicap-golf", "block": "deportes", "group": "golf",
    "formula": "return {'handicap': ((score - rating) * 113) / slope}",
    "inputs": [
        {"id": "score", "type": "number", "default": 90, "min": 0, "unit": ""},
        {"id": "rating", "type": "number", "default": 72, "min": 0, "unit": ""},
        {"id": "slope", "type": "number", "default": 113, "min": 55, "unit": ""}
    ],
    "outputs": [{"id": "handicap", "unit": ""}],
    "related": [300, 301, 1097], "i18n": i18n("Handicap de Golf", "Calcula tu handicap de golf a partir del score, rating y slope del campo.", "Handicap Golf | CalcToWork", "Calcula el handicap de golf según score y dificultad del campo.", ["score", "rating", "slope"], ["handicap"])})

calculators.append({"id": 1099, "slug": "quemar-calorias-met", "block": "deportes", "group": "fitness",
    "formula": "return {'calorias': (met * 3.5 * peso / 200) * duracion_min}",
    "inputs": [
        {"id": "met", "type": "number", "default": 8, "min": 0, "unit": ""},
        {"id": "peso", "type": "number", "default": 70, "unit": "kg", "unit_options": ["kg", "lb"], "unit_category": "mass", "min": 0},
        {"id": "duracion_min", "type": "number", "default": 60, "min": 0, "unit": "min", "unit_options": ["min", "h"], "unit_category": "time"}
    ],
    "outputs": [{"id": "calorias", "unit": "kcal"}],
    "related": [300, 301, 1097], "i18n": i18n("Calorías Quemadas por MET", "Calcula las calorías quemadas en una actividad según el valor MET.", "Calorías MET | CalcToWork", "Calcula calorías quemadas con valores MET de actividades físicas.", ["met", "peso", "duracion_min"], ["calorias"])})

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump({"batch_id": "batch_4", "calculators": calculators}, f, indent=2, ensure_ascii=False)
print(f"Wrote {len(calculators)} calculators to {OUTPUT}")

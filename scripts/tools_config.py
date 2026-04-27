"""
CalcToWork – Tools configuration
100 tools: category (A-E), block, localized SEO slugs, input group rules.

Categories:
  A – Tiling & Flooring      (room dims + tile dims + wastage)
  B – Painting & Coatings    (surface + product settings + wastage)
  C – Masonry & Structure    (geometry + mix/material + wastage)
  D – Liquid / Volume        (volume/flow/technical – no wastage)
  E – Budgeting & Mgmt       (financial/time fields – no wastage)
"""

# ---------------------------------------------------------------------------
# Field-name patterns → group assignment
# ---------------------------------------------------------------------------

DIMENSION_KEYS = {
    "largo", "ancho", "alto", "altura", "espesor", "longitud",
    "profundidad", "canto", "area", "area_m2", "area_planta",
    "perimetro", "intereje", "canto_forjado", "luz_m",
    "longitud_nave_m", "espesor_base", "espesor_corona",
    "altura_total_m", "ancho_m", "alto_m", "longitud_m",
    "longitud_pared_m", "altura_m", "separacion_montantes_m",
}

MATERIAL_KEYS = {
    "tam_pieza_cm", "formato", "m2_por_caja", "piezas_por_caja",
    "tam_malla_cm", "ancho_rollo_m", "longitud_rollo_m",
    "kg_acero_m3", "kg_acero_m2", "dosificacion",
    "tipo_placa", "aislamiento", "tipo_teja", "incluye_mortero",
    "tipo_vidrio", "merma_pct", "tipo_colocacion", "tipo_adhesivo",
    "colocacion", "carga_kn_m2", "espesor_cm", "espesor_mm",
    "ancho_junta_mm", "grosor_pieza_mm", "pendiente_pct",
}

PRODUCT_KEYS = {
    "manos", "rendimiento_m2_l", "color", "tipo_madera", "tipo_soporte",
    "tipo_textura", "grano_inicial", "num_granos", "pasadas", "tipo",
}

COUNT_KEYS = {
    "cantidad", "tramos", "puntos_suministro", "circuitos_max_m",
    "separacion_cm", "separacion_lineas_m", "separacion_goteros_cm",
    "num_ventanas", "num_puertas", "num_aparatos", "num_trabajadores",
    "uso", "orientacion", "tipo_dieta", "tipo_reforma", "tipo_actividad",
    "tipo_licencia", "tipo_pica", "tipo_gas", "tipo_limpieza", "tipo_obra",
}

MATH_KEYS = {
    "x", "a", "b", "c", "d", "n", "r", "a1", "d_in", "real", "imag",
    "vx", "vy", "vz", "ax", "ay", "az", "bx", "by", "bz",
    "x_val", "fa", "fb", "approx", "sum", "det", "mag", "dot",
    "cx", "cy", "cz", "derivative", "magnitude",
}

HEALTH_KEYS = {
    "weight", "height", "age", "gender", "waist", "neck", "bfp", "lbm",
    "activity", "creatinine", "crcl", "protein_min", "protein_max",
    "water", "bmr", "tdee", "rmr", "met", "duration", "steps", "distance",
    "age_months", "percentile", "grasa_pct", "peso_kg", "altura_cm", "edad",
    "sexo",
}

PHYSICS_KEYS = {
    "v0", "angle", "h0", "range", "max_height", "flight_time",
    "m", "v", "force", "m1", "m2", "k", "energy", "dt", "q",
    "f", "wavelength", "focal", "obj_dist", "img_dist", "magnification",
    "theta", "torque", "L", "rho", "g", "h", "pressure", "v_wave",
    "wl", "u", "img", "mag", "tau", "p", "t_flight", "vx", "vy",
    "wl_m", "lambda", "cop", "u_muros", "u_techo", "t_ext", "t_int",
    "hsp", "consumo_dia", "autonomia", "caudal", "presion_entrada",
    "dotacion", "habitantes", "dias", "temperatura", "humedad",
    "potencia", "voltaje", "longitud_cable", "caida_max",
}

FINANCIAL_KEYS = {
    "coste_eur", "precio_dia_eur", "precio_m2_semana", "precio_m2",
    "facturacion_anual_eur", "beneficio_deseado_pct", "capital_asegurado_eur",
    "valor_residual_pct", "importe_eur", "base_imponible_eur",
    "precio_hora_eur", "coste_hora_eur", "precio_venta_eur",
    "costes_fijos_eur", "costes_variables_eur", "precio_venta_ud",
    "coste_variable_ud", "coste_herramienta_eur", "coste_total_eur",
    "precio_l", "presupuesto_obra_eur", "ahorro_horas_mes",
}

TIME_KEYS = {
    "horas_dia", "horas_facturables_mes", "horas_jornada",
    "dias_obra", "dias_alquiler", "dias_autonomia", "semanas",
    "anos_vida_util", "plazo_meses", "km_anuales",
    "meses_obra", "vida_util_anos", "km_diarios",
}


def classify_input(key: str) -> str:
    """Return group id for a formula input key."""
    if key in DIMENSION_KEYS or any(
        key.startswith(p) for p in ("largo", "ancho", "alto", "altura", "espesor",
                                     "longitud", "profundidad", "canto", "area",
                                     "perimetro", "luz_", "ancho_m", "alto_m")
    ):
        return "dims"
    if key in MATERIAL_KEYS or any(
        p in key for p in ("tam_pieza", "formato", "m2_por", "piezas_por",
                            "tam_malla", "rollo", "kg_acero", "dosificacion",
                            "tipo_placa", "tipo_teja", "tipo_vidrio",
                            "espesor_cm", "espesor_mm", "merma_pct",
                            "pendiente_pct", "tipo_colocacion", "tipo_adhesivo")
    ):
        return "material"
    if key in PRODUCT_KEYS or any(
        p in key for p in ("manos", "rendimiento", "grano_inicial", "num_granos",
                            "pasadas", "tipo_textura", "tipo_madera", "tipo_soporte")
    ):
        return "product"
    if key in FINANCIAL_KEYS or any(
        p in key for p in ("coste_", "precio_", "facturacion", "beneficio",
                            "_eur", "importe", "base_imponible", "capital_",
                            "valor_residual", "presupuesto_obra", "ahorro_horas")
    ):
        return "financial"
    if key in TIME_KEYS or any(
        p in key for p in ("horas_", "dias_", "_dias", "semanas", "anos_vida",
                            "plazo_", "km_anuales", "meses_obra", "vida_util",
                            "km_diarios")
    ):
        return "time"
    if key in COUNT_KEYS or any(
        p in key for p in ("cantidad", "tramos", "separacion", "num_ventanas",
                            "num_puertas", "num_aparatos", "num_trabajadores",
                            "orientacion", "uso", "tipo_")
    ):
        return "count"
    if key in MATH_KEYS:
        return "math"
    if key in HEALTH_KEYS:
        return "health"
    if key in PHYSICS_KEYS:
        return "physics"
    return "other"


# Group labels per language
GROUP_LABELS = {
    "dims": {
        "es": "Dimensiones", "en": "Dimensions",
        "fr": "Dimensions",  "pt": "Dimensões",
        "de": "Abmessungen", "it": "Dimensioni",
    },
    "material": {
        "es": "Material / Producto", "en": "Material / Product",
        "fr": "Matériau / Produit",  "pt": "Material / Produto",
        "de": "Material / Produkt",  "it": "Materiale / Prodotto",
    },
    "product": {
        "es": "Configuración del producto", "en": "Product Settings",
        "fr": "Paramètres du produit",       "pt": "Configurações do produto",
        "de": "Produkteinstellungen",         "it": "Impostazioni prodotto",
    },
    "count": {
        "es": "Cantidades y tipo", "en": "Quantities & Type",
        "fr": "Quantités et type", "pt": "Quantidades e tipo",
        "de": "Mengen & Typ",      "it": "Quantità e tipo",
    },
    "financial": {
        "es": "Datos económicos", "en": "Financial Data",
        "fr": "Données financières", "pt": "Dados financeiros",
        "de": "Finanzdaten",       "it": "Dati economici",
    },
    "time": {
        "es": "Tiempo y jornada", "en": "Time & Schedule",
        "fr": "Temps et planning", "pt": "Tempo e jornada",
        "de": "Zeit & Zeitplan",   "it": "Tempo e pianificazione",
    },
    "other": {
        "es": "Parámetros técnicos", "en": "Technical Parameters",
        "fr": "Paramètres techniques", "pt": "Parâmetros técnicos",
        "de": "Technische Parameter",  "it": "Parametri tecnici",
    },
    "math": {
        "es": "Valores", "en": "Values",
        "fr": "Valeurs", "pt": "Valores",
        "de": "Werte",  "it": "Valori",
    },
    "health": {
        "es": "Datos corporales", "en": "Body Data",
        "fr": "Données corporelles", "pt": "Dados corporais",
        "de": "Körperdaten",  "it": "Dati corporei",
    },
    "physics": {
        "es": "Parámetros físicos", "en": "Physical Parameters",
        "fr": "Paramètres physiques", "pt": "Parâmetros físicos",
        "de": "Physikalische Parameter",  "it": "Parametri fisici",
    },
}

GROUP_ICONS = {
    "dims": "📐", "material": "🧱", "product": "🪣",
    "count": "🔢", "financial": "💶", "time": "🕐", "other": "⚙️",
    "math": "🔢", "health": "❤️", "physics": "⚛️",
}

# Wastage defaults per category
WASTAGE_DEFAULTS = {"A": 10, "B": 5, "C": 7, "D": 0, "E": 0}
SHOW_WASTAGE = {"A": True, "B": True, "C": True, "D": False, "E": False}

# Unit labels appended to input field labels
UNIT_LABELS = {
    "largo": "m", "ancho": "m", "alto": "m", "altura": "m",
    "longitud": "m", "longitud_m": "m", "longitud_pared_m": "m",
    "profundidad": "m", "canto": "m", "base": "m",
    "area": "m²", "area_m2": "m²", "area_planta": "m²", "area_cubierta": "m²",
    "perimetro": "m", "luz_m": "m", "altura_total_m": "m",
    "ancho_m": "m", "alto_m": "m", "longitud_nave_m": "m",
    "separacion_montantes_m": "m", "ancho_rollo_m": "m", "longitud_rollo_m": "m",
    "intereje": "m", "canto_forjado": "m",
    "espesor": "m", "espesor_base": "m", "espesor_corona": "m",
    "espesor_cm": "cm", "espesor_mm": "mm",
    "grosor_pieza_mm": "mm", "ancho_junta_mm": "mm",
    "tam_pieza_cm": "cm", "tam_malla_cm": "cm",
    "kg_acero_m3": "kg/m³", "kg_acero_m2": "kg/m²", "carga_kn_m2": "kN/m²",
    "rendimiento_m2_l": "m²/L",
    "separacion_cm": "cm", "separacion_lineas_m": "m", "separacion_goteros_cm": "cm",
    "coste_eur": "€", "precio_dia_eur": "€/day", "precio_m2_semana": "€/m²/wk",
    "precio_m2": "€/m²", "precio_hora_eur": "€/h", "coste_hora_eur": "€/h",
    "precio_venta_eur": "€", "costes_fijos_eur": "€", "costes_variables_eur": "€",
    "coste_variable_ud": "€/unit", "importe_eur": "€", "base_imponible_eur": "€",
    "capital_asegurado_eur": "€", "presupuesto_obra_eur": "€",
    "coste_herramienta_eur": "€", "coste_total_eur": "€",
    "precio_l": "€/L", "precio_venta_ud": "€/unit",
    "facturacion_anual_eur": "€/yr", "valor_residual_pct": "%",
    "horas_dia": "h/day", "horas_facturables_mes": "h/mo",
    "horas_jornada": "h", "dias_obra": "days", "dias_alquiler": "days",
    "dias_autonomia": "days", "semanas": "wk", "anos_vida_util": "yr",
    "plazo_meses": "mo", "meses_obra": "mo", "vida_util_anos": "yr",
    "km_anuales": "km/yr", "km_diarios": "km/day",
    "temperatura": "°C", "t_ext": "°C", "t_int": "°C",
    "potencia": "W", "voltaje": "V", "longitud_cable": "m", "caida_max": "%",
    "caudal": "L/min", "presion_entrada": "bar",
    "pendiente_pct": "%", "merma_pct": "%", "beneficio_deseado_pct": "%",
    "hsp": "h/day", "consumo_dia": "Wh/day", "autonomia": "days",
    "cop": "COP", "lambda": "W/m·K", "u_muros": "W/m²K", "u_techo": "W/m²K",
}


# ---------------------------------------------------------------------------
# Tools configuration – 100 entries
# ---------------------------------------------------------------------------

TOOLS = [
    # ── ESTRUCTURAS (001-010) ─────────────────────────────────────────────
    {"id": "001", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-hormigon-masa",
        "en": "mass-concrete-calculator",
        "fr": "calculateur-beton-masse",
        "pt": "calculadora-concreto-massa",
        "de": "stampfbeton-rechner",
        "it": "calcolatore-calcestruzzo-massa",
    }},
    {"id": "002", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-hormigon-armado",
        "en": "reinforced-concrete-calculator",
        "fr": "calculateur-beton-arme",
        "pt": "calculadora-concreto-armado",
        "de": "stahlbeton-rechner",
        "it": "calcolatore-calcestruzzo-armato",
    }},
    {"id": "003", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-zapata-aislada",
        "en": "isolated-footing-calculator",
        "fr": "calculateur-semelle-isolee",
        "pt": "calculadora-sapata-isolada",
        "de": "einzelfundament-rechner",
        "it": "calcolatore-fondazione-isolata",
    }},
    {"id": "004", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-muro-contencion",
        "en": "retaining-wall-calculator",
        "fr": "calculateur-mur-soutenement",
        "pt": "calculadora-muro-contencao",
        "de": "stuetzmauer-rechner",
        "it": "calcolatore-muro-contenimento",
    }},
    {"id": "005", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-pilares-hormigon",
        "en": "concrete-column-calculator",
        "fr": "calculateur-poteaux-beton",
        "pt": "calculadora-pilares-concreto",
        "de": "betonstaender-rechner",
        "it": "calcolatore-pilastri-calcestruzzo",
    }},
    {"id": "006", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-vigas-hormigon",
        "en": "concrete-beam-calculator",
        "fr": "calculateur-poutres-beton",
        "pt": "calculadora-vigas-concreto",
        "de": "betontraeger-rechner",
        "it": "calcolatore-travi-calcestruzzo",
    }},
    {"id": "007", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-forjado-vigueta",
        "en": "joist-floor-calculator",
        "fr": "calculateur-plancher-poutrelles",
        "pt": "calculadora-laje-vigota",
        "de": "rippendecke-rechner",
        "it": "calcolatore-solaio-travetti",
    }},
    {"id": "008", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-losa-hormigon",
        "en": "concrete-slab-calculator",
        "fr": "calculateur-dalle-beton",
        "pt": "calculadora-laje-concreto",
        "de": "betonplatte-rechner",
        "it": "calcolatore-soletta-calcestruzzo",
    }},
    {"id": "009", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-cimiento-corrido",
        "en": "strip-foundation-calculator",
        "fr": "calculateur-semelle-filante",
        "pt": "calculadora-fundacao-corrida",
        "de": "streifenfundament-rechner",
        "it": "calcolatore-fondazione-continua",
    }},
    {"id": "010", "cat": "C", "block": "estructuras", "slugs": {
        "es": "calculadora-excavacion-tierra",
        "en": "earthwork-excavation-calculator",
        "fr": "calculateur-terrassement",
        "pt": "calculadora-escavacao-terra",
        "de": "erdaushub-rechner",
        "it": "calcolatore-scavo-terra",
    }},
    # ── MAMPOSTERÍA (011-020) ─────────────────────────────────────────────
    {"id": "011", "cat": "C", "block": "mamposteria", "slugs": {
        "es": "calculadora-ladrillo-hueco",
        "en": "hollow-brick-calculator",
        "fr": "calculateur-brique-creuse",
        "pt": "calculadora-tijolo-furado",
        "de": "hohlziegel-rechner",
        "it": "calcolatore-mattone-forato",
    }},
    {"id": "012", "cat": "C", "block": "mamposteria", "slugs": {
        "es": "calculadora-ladrillo-cara-vista",
        "en": "face-brick-calculator",
        "fr": "calculateur-brique-de-parement",
        "pt": "calculadora-tijolo-aparente",
        "de": "verblendmauerwerk-rechner",
        "it": "calcolatore-mattone-facciavista",
    }},
    {"id": "013", "cat": "C", "block": "mamposteria", "slugs": {
        "es": "calculadora-bloque-hormigon",
        "en": "concrete-block-calculator",
        "fr": "calculateur-parpaing-beton",
        "pt": "calculadora-bloco-concreto",
        "de": "betonblock-rechner",
        "it": "calcolatore-blocco-calcestruzzo",
    }},
    {"id": "014", "cat": "C", "block": "mamposteria", "slugs": {
        "es": "calculadora-tabique-pladur",
        "en": "drywall-partition-calculator",
        "fr": "calculateur-cloison-placoplatre",
        "pt": "calculadora-divisoria-drywall",
        "de": "trockenbau-trennwand-rechner",
        "it": "calcolatore-parete-cartongesso",
    }},
    {"id": "015", "cat": "B", "block": "mamposteria", "slugs": {
        "es": "calculadora-aislamiento-termico",
        "en": "thermal-insulation-calculator",
        "fr": "calculateur-isolation-thermique",
        "pt": "calculadora-isolamento-termico",
        "de": "waermedaemmung-rechner",
        "it": "calcolatore-isolamento-termico",
    }},
    {"id": "016", "cat": "B", "block": "mamposteria", "slugs": {
        "es": "calculadora-revoco-proyectado",
        "en": "spray-render-calculator",
        "fr": "calculateur-enduit-projete",
        "pt": "calculadora-reboco-projetado",
        "de": "spritzputz-rechner",
        "it": "calcolatore-intonaco-proiettato",
    }},
    {"id": "017", "cat": "C", "block": "mamposteria", "slugs": {
        "es": "calculadora-mortero-cemento",
        "en": "cement-mortar-calculator",
        "fr": "calculateur-mortier-ciment",
        "pt": "calculadora-argamassa-cimento",
        "de": "zementmoertel-rechner",
        "it": "calcolatore-malta-cemento",
    }},
    {"id": "018", "cat": "B", "block": "mamposteria", "slugs": {
        "es": "calculadora-enfoscado-guarnecido",
        "en": "plaster-render-calculator",
        "fr": "calculateur-enduit-platre",
        "pt": "calculadora-reboco-gesso",
        "de": "putz-rechner",
        "it": "calcolatore-intonaco-gesso",
    }},
    {"id": "019", "cat": "C", "block": "mamposteria", "slugs": {
        "es": "calculadora-mamposteria-piedra",
        "en": "stone-masonry-calculator",
        "fr": "calculateur-maconnerie-pierre",
        "pt": "calculadora-alvenaria-pedra",
        "de": "steinmauerwerk-rechner",
        "it": "calcolatore-muratura-pietra",
    }},
    {"id": "020", "cat": "A", "block": "mamposteria", "slugs": {
        "es": "calculadora-cubierta-teja",
        "en": "roof-tile-calculator",
        "fr": "calculateur-tuiles-toiture",
        "pt": "calculadora-telha-cobertura",
        "de": "dachziegel-rechner",
        "it": "calcolatore-tegole-copertura",
    }},
    # ── PAVIMENTOS (021-030) ──────────────────────────────────────────────
    {"id": "021", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-solado-ceramico",
        "en": "ceramic-tile-calculator",
        "fr": "calculateur-carrelage-ceramique",
        "pt": "calculadora-azulejo-ceramico",
        "de": "keramikfliesen-rechner",
        "it": "calcolatore-pavimento-ceramica",
    }},
    {"id": "022", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-gres-porcelanico",
        "en": "porcelain-tile-calculator",
        "fr": "calculateur-gres-cerame",
        "pt": "calculadora-porcelanato",
        "de": "feinsteinzeug-rechner",
        "it": "calcolatore-gres-porcellanato",
    }},
    {"id": "023", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-laminado-flotante",
        "en": "laminate-flooring-calculator",
        "fr": "calculateur-sol-stratifie",
        "pt": "calculadora-piso-laminado",
        "de": "laminatboden-rechner",
        "it": "calcolatore-pavimento-laminato",
    }},
    {"id": "024", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-parquet-madera",
        "en": "hardwood-parquet-calculator",
        "fr": "calculateur-parquet-bois",
        "pt": "calculadora-parquet-madeira",
        "de": "parkett-rechner",
        "it": "calcolatore-parquet-legno",
    }},
    {"id": "025", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-marmol-granito",
        "en": "marble-granite-calculator",
        "fr": "calculateur-marbre-granit",
        "pt": "calculadora-marmore-granito",
        "de": "marmor-granit-rechner",
        "it": "calcolatore-marmo-granito",
    }},
    {"id": "026", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-terrazo",
        "en": "terrazzo-floor-calculator",
        "fr": "calculateur-terrazzo",
        "pt": "calculadora-piso-terrazo",
        "de": "terrazzo-rechner",
        "it": "calcolatore-pavimento-terrazzo",
    }},
    {"id": "027", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-azulejo-pared",
        "en": "wall-tile-calculator",
        "fr": "calculateur-faience-murale",
        "pt": "calculadora-azulejo-parede",
        "de": "wandfliesen-rechner",
        "it": "calcolatore-piastrelle-parete",
    }},
    {"id": "028", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-mosaico",
        "en": "mosaic-tile-calculator",
        "fr": "calculateur-mosaique",
        "pt": "calculadora-mosaico",
        "de": "mosaik-rechner",
        "it": "calcolatore-mosaico",
    }},
    {"id": "029", "cat": "B", "block": "pavimentos", "slugs": {
        "es": "calculadora-adhesivo-ceramico",
        "en": "tile-adhesive-calculator",
        "fr": "calculateur-colle-carrelage",
        "pt": "calculadora-cola-ceramica",
        "de": "fliesenkleber-rechner",
        "it": "calcolatore-adesivo-piastrelle",
    }},
    {"id": "030", "cat": "A", "block": "pavimentos", "slugs": {
        "es": "calculadora-lechada-junta",
        "en": "tile-grout-calculator",
        "fr": "calculateur-coulis-joint",
        "pt": "calculadora-rejunte",
        "de": "fugenmasse-rechner",
        "it": "calcolatore-stucco-fughe",
    }},
    # ── FONTANERÍA (031-042) ──────────────────────────────────────────────
    {"id": "031", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-tuberia-saneamiento",
        "en": "drainage-pipe-calculator",
        "fr": "calculateur-tuyau-assainissement",
        "pt": "calculadora-tubulacao-saneamento",
        "de": "abwasserrohr-rechner",
        "it": "calcolatore-tubo-scarico",
    }},
    {"id": "032", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-tuberia-cobre-pex",
        "en": "copper-pex-pipe-calculator",
        "fr": "calculateur-tube-cuivre-pex",
        "pt": "calculadora-tubo-cobre-pex",
        "de": "kupfer-pex-rohr-rechner",
        "it": "calcolatore-tubo-rame-pex",
    }},
    {"id": "033", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-presion-agua",
        "en": "water-pressure-calculator",
        "fr": "calculateur-pression-eau",
        "pt": "calculadora-pressao-agua",
        "de": "wasserdruck-rechner",
        "it": "calcolatore-pressione-acqua",
    }},
    {"id": "034", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-deposito-agua",
        "en": "water-tank-calculator",
        "fr": "calculateur-reservoir-eau",
        "pt": "calculadora-reservatorio-agua",
        "de": "wassertank-rechner",
        "it": "calcolatore-serbatoio-acqua",
    }},
    {"id": "035", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-calentador-agua",
        "en": "water-heater-calculator",
        "fr": "calculateur-chauffe-eau",
        "pt": "calculadora-aquecedor-agua",
        "de": "warmwasserbereiter-rechner",
        "it": "calcolatore-scaldacqua",
    }},
    {"id": "036", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-caldera-gas",
        "en": "gas-boiler-calculator",
        "fr": "calculateur-chaudiere-gaz",
        "pt": "calculadora-caldeira-gas",
        "de": "gasheizkessel-rechner",
        "it": "calcolatore-caldaia-gas",
    }},
    {"id": "037", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-radiador-aluminio",
        "en": "aluminium-radiator-calculator",
        "fr": "calculateur-radiateur-aluminium",
        "pt": "calculadora-radiador-aluminio",
        "de": "aluminiumheizkörper-rechner",
        "it": "calcolatore-radiatore-alluminio",
    }},
    {"id": "038", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-suelo-radiante",
        "en": "underfloor-heating-calculator",
        "fr": "calculateur-plancher-chauffant",
        "pt": "calculadora-piso-radiante",
        "de": "fussbodenheizung-rechner",
        "it": "calcolatore-riscaldamento-pavimento",
    }},
    {"id": "039", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-riego-goteo",
        "en": "drip-irrigation-calculator",
        "fr": "calculateur-irrigation-goutte-a-goutte",
        "pt": "calculadora-irrigacao-gotejo",
        "de": "tropfbewaesserung-rechner",
        "it": "calcolatore-irrigazione-goccia",
    }},
    {"id": "040", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-acometida-agua",
        "en": "water-service-connection-calculator",
        "fr": "calculateur-branchement-eau",
        "pt": "calculadora-ramal-agua",
        "de": "wasseranschluss-rechner",
        "it": "calcolatore-allacciamento-acqua",
    }},
    {"id": "041", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-depuradora-piscina",
        "en": "pool-pump-filter-calculator",
        "fr": "calculateur-pompe-piscine",
        "pt": "calculadora-bomba-piscina",
        "de": "poolfilter-rechner",
        "it": "calcolatore-pompa-piscina",
    }},
    {"id": "042", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-sifon-sumidero",
        "en": "drain-trap-calculator",
        "fr": "calculateur-siphon-drain",
        "pt": "calculadora-sifao-ralo",
        "de": "geruchsverschluss-rechner",
        "it": "calcolatore-sifone-scarico",
    }},
    # ── ELECTRICIDAD (043-052) ────────────────────────────────────────────
    {"id": "043", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-seccion-cable-electrico",
        "en": "electrical-cable-section-calculator",
        "fr": "calculateur-section-cable-electrique",
        "pt": "calculadora-secao-cabo-eletrico",
        "de": "kabelquerschnitt-rechner",
        "it": "calcolatore-sezione-cavo-elettrico",
    }},
    {"id": "044", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-caida-tension",
        "en": "voltage-drop-calculator",
        "fr": "calculateur-chute-tension",
        "pt": "calculadora-queda-tensao",
        "de": "spannungsabfall-rechner",
        "it": "calcolatore-caduta-tensione",
    }},
    {"id": "045", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-luminarias-lumenes",
        "en": "lighting-lumens-calculator",
        "fr": "calculateur-luminaires-lumens",
        "pt": "calculadora-luminarias-lumens",
        "de": "beleuchtungsstaerke-rechner",
        "it": "calcolatore-illuminazione-lumen",
    }},
    {"id": "046", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-puntos-luz-habitacion",
        "en": "room-lighting-points-calculator",
        "fr": "calculateur-points-eclairage",
        "pt": "calculadora-pontos-luz-ambiente",
        "de": "lichtpunkte-zimmer-rechner",
        "it": "calcolatore-punti-luce-stanza",
    }},
    {"id": "047", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-cuadro-electrico",
        "en": "electrical-panel-calculator",
        "fr": "calculateur-tableau-electrique",
        "pt": "calculadora-quadro-eletrico",
        "de": "schaltschrank-rechner",
        "it": "calcolatore-quadro-elettrico",
    }},
    {"id": "048", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-instalacion-solar-fotovoltaica",
        "en": "solar-pv-installation-calculator",
        "fr": "calculateur-installation-solaire-photovoltaique",
        "pt": "calculadora-instalacao-solar-fotovoltaica",
        "de": "photovoltaik-rechner",
        "it": "calcolatore-impianto-fotovoltaico",
    }},
    {"id": "049", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-baterias-autonomia",
        "en": "battery-autonomy-calculator",
        "fr": "calculateur-autonomie-batteries",
        "pt": "calculadora-autonomia-baterias",
        "de": "batterie-autonomie-rechner",
        "it": "calcolatore-autonomia-batterie",
    }},
    {"id": "050", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-potencia-trifasica",
        "en": "three-phase-power-calculator",
        "fr": "calculateur-puissance-triphasee",
        "pt": "calculadora-potencia-trifasica",
        "de": "drehstromleistung-rechner",
        "it": "calcolatore-potenza-trifase",
    }},
    {"id": "051", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-puesta-tierra",
        "en": "earthing-grounding-calculator",
        "fr": "calculateur-mise-a-la-terre",
        "pt": "calculadora-aterramento",
        "de": "erdungsanlage-rechner",
        "it": "calcolatore-messa-terra",
    }},
    {"id": "052", "cat": "E", "block": "electricidad", "slugs": {
        "es": "calculadora-consumo-electrico-mensual",
        "en": "monthly-electricity-cost-calculator",
        "fr": "calculateur-consommation-electrique-mensuelle",
        "pt": "calculadora-consumo-eletrico-mensal",
        "de": "monatlicher-stromkosten-rechner",
        "it": "calcolatore-consumo-elettrico-mensile",
    }},
    # ── CLIMATIZACIÓN (053-060) ───────────────────────────────────────────
    {"id": "053", "cat": "D", "block": "climatizacion", "slugs": {
        "es": "calculadora-aire-acondicionado-btu",
        "en": "air-conditioner-btu-calculator",
        "fr": "calculateur-climatiseur-btu",
        "pt": "calculadora-ar-condicionado-btu",
        "de": "klimaanlage-btu-rechner",
        "it": "calcolatore-condizionatore-btu",
    }},
    {"id": "054", "cat": "D", "block": "climatizacion", "slugs": {
        "es": "calculadora-conductos-aire",
        "en": "air-duct-sizing-calculator",
        "fr": "calculateur-dimensionnement-gaine",
        "pt": "calculadora-dimensionamento-duto",
        "de": "luftkanal-rechner",
        "it": "calcolatore-dimensionamento-condotto",
    }},
    {"id": "055", "cat": "D", "block": "climatizacion", "slugs": {
        "es": "calculadora-ventilacion-mecanica",
        "en": "mechanical-ventilation-calculator",
        "fr": "calculateur-ventilation-mecanique",
        "pt": "calculadora-ventilacao-mecanica",
        "de": "lueftungsanlage-rechner",
        "it": "calcolatore-ventilazione-meccanica",
    }},
    {"id": "056", "cat": "D", "block": "climatizacion", "slugs": {
        "es": "calculadora-bomba-calor-aerotermia",
        "en": "air-source-heat-pump-calculator",
        "fr": "calculateur-pompe-chaleur-aerothermie",
        "pt": "calculadora-bomba-calor-aerotermia",
        "de": "luftwaermepumpe-rechner",
        "it": "calcolatore-pompa-calore-aerotermia",
    }},
    {"id": "057", "cat": "D", "block": "climatizacion", "slugs": {
        "es": "calculadora-cop-eer-climatizacion",
        "en": "cop-eer-hvac-calculator",
        "fr": "calculateur-cop-eer-climatisation",
        "pt": "calculadora-cop-eer-climatizacao",
        "de": "cop-eer-klimaanlage-rechner",
        "it": "calcolatore-cop-eer-climatizzazione",
    }},
    {"id": "058", "cat": "D", "block": "climatizacion", "slugs": {
        "es": "calculadora-dimensionado-conducto-hvac",
        "en": "hvac-duct-sizing-calculator",
        "fr": "calculateur-dimensionnement-conduit-hvac",
        "pt": "calculadora-dimensionamento-duto-hvac",
        "de": "hvac-kanalgroesse-rechner",
        "it": "calcolatore-dimensionamento-canale-hvac",
    }},
    {"id": "059", "cat": "D", "block": "climatizacion", "slugs": {
        "es": "calculadora-rejillas-difusores",
        "en": "air-grille-diffuser-calculator",
        "fr": "calculateur-grilles-diffuseurs",
        "pt": "calculadora-grelhas-difusores",
        "de": "luftgitter-diffusor-rechner",
        "it": "calcolatore-griglie-diffusori",
    }},
    {"id": "060", "cat": "D", "block": "climatizacion", "slugs": {
        "es": "calculadora-carga-gas-refrigerante",
        "en": "refrigerant-charge-calculator",
        "fr": "calculateur-charge-gaz-refrigerant",
        "pt": "calculadora-carga-gas-refrigerante",
        "de": "kuehlmittelladung-rechner",
        "it": "calcolatore-carica-gas-refrigerante",
    }},
    # ── CARPINTERÍA (061-068) ─────────────────────────────────────────────
    {"id": "061", "cat": "C", "block": "carpinteria", "slugs": {
        "es": "calculadora-ventanas-aluminio-pvc",
        "en": "aluminium-pvc-window-calculator",
        "fr": "calculateur-fenetres-aluminium-pvc",
        "pt": "calculadora-janelas-aluminio-pvc",
        "de": "aluminium-pvc-fenster-rechner",
        "it": "calcolatore-finestre-alluminio-pvc",
    }},
    {"id": "062", "cat": "C", "block": "carpinteria", "slugs": {
        "es": "calculadora-puertas-paso",
        "en": "interior-door-calculator",
        "fr": "calculateur-portes-interieures",
        "pt": "calculadora-portas-internas",
        "de": "zimmertuer-rechner",
        "it": "calcolatore-porte-interne",
    }},
    {"id": "063", "cat": "C", "block": "carpinteria", "slugs": {
        "es": "calculadora-puertas-correderas",
        "en": "sliding-door-calculator",
        "fr": "calculateur-portes-coulissantes",
        "pt": "calculadora-portas-corredicas",
        "de": "schiebetuer-rechner",
        "it": "calcolatore-porte-scorrevoli",
    }},
    {"id": "064", "cat": "C", "block": "carpinteria", "slugs": {
        "es": "calculadora-escalera-madera",
        "en": "wooden-staircase-calculator",
        "fr": "calculateur-escalier-bois",
        "pt": "calculadora-escada-madeira",
        "de": "holztreppe-rechner",
        "it": "calcolatore-scala-legno",
    }},
    {"id": "065", "cat": "C", "block": "carpinteria", "slugs": {
        "es": "calculadora-barandilla-metalica",
        "en": "metal-railing-calculator",
        "fr": "calculateur-garde-corps-metallique",
        "pt": "calculadora-guarda-corpo-metalico",
        "de": "metallgelaender-rechner",
        "it": "calcolatore-ringhiera-metallica",
    }},
    {"id": "066", "cat": "C", "block": "carpinteria", "slugs": {
        "es": "calculadora-estructuras-metalicas",
        "en": "steel-structure-calculator",
        "fr": "calculateur-structures-metalliques",
        "pt": "calculadora-estruturas-metalicas",
        "de": "stahlbau-rechner",
        "it": "calcolatore-strutture-metalliche",
    }},
    {"id": "067", "cat": "C", "block": "carpinteria", "slugs": {
        "es": "calculadora-cerrajeria-puerta",
        "en": "door-metalwork-calculator",
        "fr": "calculateur-ferronnerie-porte",
        "pt": "calculadora-ferragens-porta",
        "de": "tuerbeschlag-rechner",
        "it": "calcolatore-ferramenta-porta",
    }},
    {"id": "068", "cat": "A", "block": "carpinteria", "slugs": {
        "es": "calculadora-vidrio-cristal",
        "en": "glass-panel-calculator",
        "fr": "calculateur-verre-vitrage",
        "pt": "calculadora-vidro-cristal",
        "de": "glas-verglasung-rechner",
        "it": "calcolatore-vetro-cristallo",
    }},
    # ── PINTURA (069-077) ─────────────────────────────────────────────────
    {"id": "069", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-pintura-plastica-paredes",
        "en": "interior-wall-paint-calculator",
        "fr": "calculateur-peinture-murale-interieure",
        "pt": "calculadora-tinta-paredes-internas",
        "de": "innenfarbe-rechner",
        "it": "calcolatore-pittura-pareti-interne",
    }},
    {"id": "070", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-pintura-techo",
        "en": "ceiling-paint-calculator",
        "fr": "calculateur-peinture-plafond",
        "pt": "calculadora-tinta-teto",
        "de": "deckenfarbe-rechner",
        "it": "calcolatore-pittura-soffitto",
    }},
    {"id": "071", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-esmalte-sintetico",
        "en": "synthetic-enamel-paint-calculator",
        "fr": "calculateur-email-synthetique",
        "pt": "calculadora-esmalte-sintetico",
        "de": "kunstharzlack-rechner",
        "it": "calcolatore-smalto-sintetico",
    }},
    {"id": "072", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-barniz-exterior-madera",
        "en": "exterior-wood-varnish-calculator",
        "fr": "calculateur-vernis-bois-exterieur",
        "pt": "calculadora-verniz-externo-madeira",
        "de": "aussen-holzlack-rechner",
        "it": "calcolatore-vernice-legno-esterno",
    }},
    {"id": "073", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-papel-pintado",
        "en": "wallpaper-calculator",
        "fr": "calculateur-papier-peint",
        "pt": "calculadora-papel-de-parede",
        "de": "tapeten-rechner",
        "it": "calcolatore-carta-da-parati",
    }},
    {"id": "074", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-acabado-texturado",
        "en": "textured-coating-calculator",
        "fr": "calculateur-enduit-texture",
        "pt": "calculadora-acabamento-texturado",
        "de": "strukturputz-rechner",
        "it": "calcolatore-intonaco-texturato",
    }},
    {"id": "075", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-imprimacion-sellador",
        "en": "primer-sealer-calculator",
        "fr": "calculateur-primaire-appret",
        "pt": "calculadora-primer-selador",
        "de": "grundierung-rechner",
        "it": "calcolatore-primer-fondo",
    }},
    {"id": "076", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-masilla-filler",
        "en": "filler-putty-calculator",
        "fr": "calculateur-enduit-rebouche",
        "pt": "calculadora-massa-corrida",
        "de": "spachtel-fuellmasse-rechner",
        "it": "calcolatore-stucco-filler",
    }},
    {"id": "077", "cat": "B", "block": "pintura", "slugs": {
        "es": "calculadora-lija-abrasivo",
        "en": "sandpaper-abrasive-calculator",
        "fr": "calculateur-papier-abrasif",
        "pt": "calculadora-lixa-abrasivo",
        "de": "schleifpapier-rechner",
        "it": "calcolatore-carta-abrasiva",
    }},
    # ── GESTIÓN (078-100) ─────────────────────────────────────────────────
    {"id": "078", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-presupuesto-reforma",
        "en": "renovation-budget-calculator",
        "fr": "calculateur-devis-renovation",
        "pt": "calculadora-orcamento-reforma",
        "de": "renovierungsbudget-rechner",
        "it": "calcolatore-preventivo-ristrutturazione",
    }},
    {"id": "079", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-precio-hora-trabajo",
        "en": "hourly-rate-calculator",
        "fr": "calculateur-taux-horaire",
        "pt": "calculadora-preco-hora-trabalho",
        "de": "stundensatz-rechner",
        "it": "calcolatore-tariffa-oraria",
    }},
    {"id": "080", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-amortizacion-maquinaria",
        "en": "machinery-depreciation-calculator",
        "fr": "calculateur-amortissement-materiel",
        "pt": "calculadora-amortizacao-maquinario",
        "de": "maschinenabschreibung-rechner",
        "it": "calcolatore-ammortamento-macchinari",
    }},
    {"id": "081", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-amortizacion-vehiculo",
        "en": "vehicle-depreciation-calculator",
        "fr": "calculateur-amortissement-vehicule",
        "pt": "calculadora-depreciacao-veiculo",
        "de": "fahrzeugabschreibung-rechner",
        "it": "calcolatore-ammortamento-veicolo",
    }},
    {"id": "082", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-coste-combustible",
        "en": "fuel-cost-calculator",
        "fr": "calculateur-cout-carburant",
        "pt": "calculadora-custo-combustivel",
        "de": "kraftstoffkosten-rechner",
        "it": "calcolatore-costo-carburante",
    }},
    {"id": "083", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-dietas-desplazamiento",
        "en": "travel-subsistence-calculator",
        "fr": "calculateur-frais-deplacement",
        "pt": "calculadora-diarias-deslocamento",
        "de": "reisespesen-rechner",
        "it": "calcolatore-indennita-trasferta",
    }},
    {"id": "084", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-alquiler-contenedor",
        "en": "skip-hire-calculator",
        "fr": "calculateur-location-benne",
        "pt": "calculadora-aluguel-cacamba",
        "de": "containermiete-rechner",
        "it": "calcolatore-noleggio-container",
    }},
    {"id": "085", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-alquiler-andamio",
        "en": "scaffolding-hire-calculator",
        "fr": "calculateur-location-echafaudage",
        "pt": "calculadora-aluguel-andaime",
        "de": "geruest-miete-rechner",
        "it": "calcolatore-noleggio-ponteggio",
    }},
    {"id": "086", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-limpieza-obra",
        "en": "construction-cleaning-calculator",
        "fr": "calculateur-nettoyage-chantier",
        "pt": "calculadora-limpeza-obra",
        "de": "baustellenreinigung-rechner",
        "it": "calcolatore-pulizia-cantiere",
    }},
    {"id": "087", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-seguro-responsabilidad-civil",
        "en": "liability-insurance-calculator",
        "fr": "calculateur-assurance-responsabilite-civile",
        "pt": "calculadora-seguro-responsabilidade-civil",
        "de": "haftpflichtversicherung-rechner",
        "it": "calcolatore-assicurazione-responsabilita",
    }},
    {"id": "088", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-epi-equipos-proteccion",
        "en": "ppe-equipment-calculator",
        "fr": "calculateur-epi-equipements-protection",
        "pt": "calculadora-epi-equipamentos-protecao",
        "de": "persoenliche-schutzausruestung-rechner",
        "it": "calcolatore-dpi-dispositivi-protezione",
    }},
    {"id": "089", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-senalizacion-obra",
        "en": "construction-signage-calculator",
        "fr": "calculateur-signalisation-chantier",
        "pt": "calculadora-sinalizacao-obra",
        "de": "baustellenbeschilderung-rechner",
        "it": "calcolatore-segnaletica-cantiere",
    }},
    {"id": "090", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-rendimiento-diario-obra",
        "en": "daily-work-output-calculator",
        "fr": "calculateur-rendement-journalier-chantier",
        "pt": "calculadora-rendimento-diario-obra",
        "de": "tagesleistung-bau-rechner",
        "it": "calcolatore-rendimento-giornaliero-cantiere",
    }},
    {"id": "091", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-planificacion-obra",
        "en": "construction-schedule-calculator",
        "fr": "calculateur-planification-chantier",
        "pt": "calculadora-planejamento-obra",
        "de": "bauzeitplan-rechner",
        "it": "calcolatore-pianificazione-cantiere",
    }},
    {"id": "092", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-licencias-municipales",
        "en": "building-permit-cost-calculator",
        "fr": "calculateur-permis-construire",
        "pt": "calculadora-licencas-municipais",
        "de": "baugenehmigungskosten-rechner",
        "it": "calcolatore-licenze-edilizie",
    }},
    {"id": "093", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-iva-irpf-factura",
        "en": "vat-income-tax-invoice-calculator",
        "fr": "calculateur-tva-impot-facture",
        "pt": "calculadora-iva-irpf-fatura",
        "de": "mehrwertsteuer-einkommensteuer-rechner",
        "it": "calcolatore-iva-irpef-fattura",
    }},
    {"id": "094", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-prestamo-equipo",
        "en": "equipment-loan-calculator",
        "fr": "calculateur-pret-equipement",
        "pt": "calculadora-financiamento-equipamento",
        "de": "ausruestungskredit-rechner",
        "it": "calcolatore-prestito-attrezzatura",
    }},
    {"id": "095", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-margen-beneficio",
        "en": "profit-margin-calculator",
        "fr": "calculateur-marge-beneficiaire",
        "pt": "calculadora-margem-lucro",
        "de": "gewinnmarge-rechner",
        "it": "calcolatore-margine-profitto",
    }},
    {"id": "096", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-punto-equilibrio",
        "en": "break-even-calculator",
        "fr": "calculateur-seuil-rentabilite",
        "pt": "calculadora-ponto-equilibrio",
        "de": "gewinnschwelle-rechner",
        "it": "calcolatore-punto-pareggio",
    }},
    {"id": "097", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-consumo-agua-obra",
        "en": "construction-water-consumption-calculator",
        "fr": "calculateur-consommation-eau-chantier",
        "pt": "calculadora-consumo-agua-obra",
        "de": "wasserverbrauch-baustelle-rechner",
        "it": "calcolatore-consumo-acqua-cantiere",
    }},
    {"id": "098", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-factor-merma-material",
        "en": "material-waste-factor-calculator",
        "fr": "calculateur-facteur-perte-materiau",
        "pt": "calculadora-fator-perda-material",
        "de": "materialverlust-faktor-rechner",
        "it": "calcolatore-fattore-perdita-materiale",
    }},
    {"id": "099", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-coste-mano-obra",
        "en": "labour-cost-calculator",
        "fr": "calculateur-cout-main-oeuvre",
        "pt": "calculadora-custo-mao-de-obra",
        "de": "arbeitskosten-rechner",
        "it": "calcolatore-costo-manodopera",
    }},
    {"id": "100", "cat": "E", "block": "gestion", "slugs": {
        "es": "calculadora-roi-herramienta",
        "en": "tool-roi-calculator",
        "fr": "calculateur-roi-outil",
        "pt": "calculadora-roi-ferramenta",
        "de": "werkzeug-roi-rechner",
        "it": "calcolatore-roi-strumento",
    }},
    {"id": "101", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-volumen-piscina",
        "en": "swimming-pool-volume-calculator",
        "fr": "calculateur-volume-piscine",
        "pt": "calculadora-volume-piscina",
        "de": "schwimmbad-volumen-rechner",
        "it": "calcolatore-volume-piscina",
    }},
    {"id": "102", "cat": "D", "block": "fontaneria", "slugs": {
        "es": "calculadora-tierra-jardin",
        "en": "garden-topsoil-calculator",
        "fr": "calculateur-terre-jardin",
        "pt": "calculadora-terra-jardim",
        "de": "gartenerde-rechner",
        "it": "calcolatore-terra-giardino",
    }},
    {"id": "103", "cat": "C", "block": "mamposteria", "slugs": {
        "es": "calculadora-postes-valla",
        "en": "fence-post-calculator",
        "fr": "calculateur-cloture-poteaux",
        "pt": "calculadora-postes-cerca",
        "de": "zaunpfosten-rechner",
        "it": "calcolatore-pali-recinzione",
    }},

    # ── MATEMÁTICAS (200-204) ─────────────────────────────────────────────
    {"id": "200", "cat": "E", "block": "matematicas", "slugs": {
        "es": "calculadora-porcentaje",
        "en": "percentage-calculator",
        "fr": "calculateur-pourcentage",
        "pt": "calculadora-porcentagem",
        "de": "prozent-rechner",
        "it": "calcolatore-percentuale",
    }},
    {"id": "201", "cat": "E", "block": "matematicas", "slugs": {
        "es": "calculadora-cambio-porcentual",
        "en": "percentage-change-calculator",
        "fr": "calculateur-variation-pourcentage",
        "pt": "calculadora-variacao-percentual",
        "de": "prozentuale-anderung-rechner",
        "it": "calcolatore-variazione-percentuale",
    }},
    {"id": "202", "cat": "E", "block": "matematicas", "slugs": {
        "es": "calculadora-area-rectangulo",
        "en": "rectangle-area-calculator",
        "fr": "calculateur-aire-rectangle",
        "pt": "calculadora-area-retangulo",
        "de": "rechteck-flache-rechner",
        "it": "calcolatore-area-rettangolo",
    }},
    {"id": "203", "cat": "E", "block": "matematicas", "slugs": {
        "es": "calculadora-pitagoras",
        "en": "pythagorean-theorem-calculator",
        "fr": "calculateur-theoreme-pythagore",
        "pt": "calculadora-teorema-pitagoras",
        "de": "satz-des-pythagoras-rechner",
        "it": "calcolatore-teorema-pitagora",
    }},
    {"id": "204", "cat": "E", "block": "matematicas", "slugs": {
        "es": "calculadora-regla-de-tres",
        "en": "rule-of-three-calculator",
        "fr": "calculateur-regle-de-trois",
        "pt": "calculadora-regra-de-tres",
        "de": "dreisatz-rechner",
        "it": "calcolatore-regola-del-tre",
    }},

    # ── FINANZAS (300-307) ────────────────────────────────────────────────
    {"id": "300", "cat": "E", "block": "finanzas", "slugs": {
        "es": "calculadora-hipoteca",
        "en": "mortgage-calculator",
        "fr": "calculateur-hypotheque",
        "pt": "calculadora-hipoteca",
        "de": "hypotheken-rechner",
        "it": "calcolatore-mutuo",
    }},
    {"id": "301", "cat": "E", "block": "finanzas", "slugs": {
        "es": "calculadora-prestamo",
        "en": "loan-calculator",
        "fr": "calculateur-pret",
        "pt": "calculadora-emprestimo",
        "de": "kredit-rechner",
        "it": "calcolatore-prestito",
    }},
    {"id": "302", "cat": "E", "block": "finanzas", "slugs": {
        "es": "calculadora-interes-compuesto",
        "en": "compound-interest-calculator",
        "fr": "calculateur-interet-compose",
        "pt": "calculadora-juros-compostos",
        "de": "zinseszins-rechner",
        "it": "calcolatore-interesse-composto",
    }},
    {"id": "303", "cat": "E", "block": "finanzas", "slugs": {
        "es": "calculadora-interes-simple",
        "en": "simple-interest-calculator",
        "fr": "calculateur-interet-simple",
        "pt": "calculadora-juros-simples",
        "de": "einfache-zinsen-rechner",
        "it": "calcolatore-interesse-semplice",
    }},
    {"id": "304", "cat": "E", "block": "finanzas", "slugs": {
        "es": "calculadora-iva",
        "en": "vat-calculator",
        "fr": "calculateur-tva",
        "pt": "calculadora-iva",
        "de": "mehrwertsteuer-rechner",
        "it": "calcolatore-iva",
    }},
    {"id": "305", "cat": "E", "block": "finanzas", "slugs": {
        "es": "calculadora-salario-neto",
        "en": "net-salary-calculator",
        "fr": "calculateur-salaire-net",
        "pt": "calculadora-salario-liquido",
        "de": "nettolohn-rechner",
        "it": "calcolatore-stipendio-netto",
    }},
    {"id": "306", "cat": "E", "block": "finanzas", "slugs": {
        "es": "calculadora-descuento",
        "en": "discount-calculator",
        "fr": "calculateur-remise",
        "pt": "calculadora-desconto",
        "de": "rabatt-rechner",
        "it": "calcolatore-sconto",
    }},
    {"id": "307", "cat": "E", "block": "finanzas", "slugs": {
        "es": "calculadora-punto-equilibrio",
        "en": "break-even-calculator",
        "fr": "calculateur-seuil-rentabilite",
        "pt": "calculadora-ponto-equilibrio",
        "de": "gewinnschwellen-rechner",
        "it": "calcolatore-punto-pareggio",
    }},

    # ── SALUD (400-403) ───────────────────────────────────────────────────
    {"id": "400", "cat": "E", "block": "salud", "slugs": {
        "es": "calculadora-imc",
        "en": "bmi-calculator",
        "fr": "calculateur-imc",
        "pt": "calculadora-imc",
        "de": "bmi-rechner",
        "it": "calcolatore-bmi",
    }},
    {"id": "401", "cat": "E", "block": "salud", "slugs": {
        "es": "calculadora-calorias-diarias",
        "en": "daily-calorie-calculator",
        "fr": "calculateur-calories-journalieres",
        "pt": "calculadora-calorias-diarias",
        "de": "tageskalorien-rechner",
        "it": "calcolatore-calorie-giornaliere",
    }},
    {"id": "402", "cat": "E", "block": "salud", "slugs": {
        "es": "calculadora-peso-ideal",
        "en": "ideal-weight-calculator",
        "fr": "calculateur-poids-ideal",
        "pt": "calculadora-peso-ideal",
        "de": "idealgewicht-rechner",
        "it": "calcolatore-peso-ideale",
    }},
    {"id": "403", "cat": "E", "block": "salud", "slugs": {
        "es": "calculadora-agua-diaria",
        "en": "daily-water-intake-calculator",
        "fr": "calculateur-eau-quotidienne",
        "pt": "calculadora-agua-diaria",
        "de": "wasserbedarfs-rechner",
        "it": "calcolatore-acqua-giornaliera",
    }},

    # ── COTIDIANO (500-502) ───────────────────────────────────────────────
    {"id": "500", "cat": "E", "block": "cotidiano", "slugs": {
        "es": "calculadora-propina",
        "en": "tip-calculator",
        "fr": "calculateur-pourboire",
        "pt": "calculadora-gorjeta",
        "de": "trinkgeld-rechner",
        "it": "calcolatore-mancia",
    }},
    {"id": "501", "cat": "E", "block": "cotidiano", "slugs": {
        "es": "calculadora-edad",
        "en": "age-calculator",
        "fr": "calculateur-age",
        "pt": "calculadora-idade",
        "de": "altersrechner",
        "it": "calcolatore-eta",
    }},
    {"id": "502", "cat": "E", "block": "cotidiano", "slugs": {
        "es": "calculadora-diferencia-fechas",
        "en": "date-difference-calculator",
        "fr": "calculateur-difference-dates",
        "pt": "calculadora-diferenca-datas",
        "de": "datums-differenz-rechner",
        "it": "calcolatore-differenza-date",
    }},

    # ── NEW CALCULATORS (910-962) ─────────────────────────────────────────
    {"id": "910", "cat": "A", "block": "matematicas", "slugs": {"es": "fraction-calculator", "en": "fraction-calculator", "fr": "fraction-calculator", "pt": "fraction-calculator", "de": "fraction-calculator", "it": "fraction-calculator"}},
    {"id": "911", "cat": "A", "block": "matematicas", "slugs": {"es": "slope-calculator", "en": "slope-calculator", "fr": "slope-calculator", "pt": "slope-calculator", "de": "slope-calculator", "it": "slope-calculator"}},
    {"id": "912", "cat": "A", "block": "matematicas", "slugs": {"es": "scientific-notation", "en": "scientific-notation", "fr": "scientific-notation", "pt": "scientific-notation", "de": "scientific-notation", "it": "scientific-notation"}},
    {"id": "913", "cat": "A", "block": "matematicas", "slugs": {"es": "rounding-calculator", "en": "rounding-calculator", "fr": "rounding-calculator", "pt": "rounding-calculator", "de": "rounding-calculator", "it": "rounding-calculator"}},
    {"id": "914", "cat": "A", "block": "matematicas", "slugs": {"es": "gcf-lcm-calculator", "en": "gcf-lcm-calculator", "fr": "gcf-lcm-calculator", "pt": "gcf-lcm-calculator", "de": "gcf-lcm-calculator", "it": "gcf-lcm-calculator"}},
    {"id": "915", "cat": "A", "block": "matematicas", "slugs": {"es": "prime-factorization", "en": "prime-factorization", "fr": "prime-factorization", "pt": "prime-factorization", "de": "prime-factorization", "it": "prime-factorization"}},
    {"id": "916", "cat": "A", "block": "matematicas", "slugs": {"es": "circle-calculator", "en": "circle-calculator", "fr": "circle-calculator", "pt": "circle-calculator", "de": "circle-calculator", "it": "circle-calculator"}},
    {"id": "917", "cat": "A", "block": "matematicas", "slugs": {"es": "right-triangle-calculator", "en": "right-triangle-calculator", "fr": "right-triangle-calculator", "pt": "right-triangle-calculator", "de": "right-triangle-calculator", "it": "right-triangle-calculator"}},
    {"id": "918", "cat": "A", "block": "matematicas", "slugs": {"es": "heron-triangle-area", "en": "heron-triangle-area", "fr": "heron-triangle-area", "pt": "heron-triangle-area", "de": "heron-triangle-area", "it": "heron-triangle-area"}},
    {"id": "919", "cat": "A", "block": "matematicas", "slugs": {"es": "rectangle-calculator", "en": "rectangle-calculator", "fr": "rectangle-calculator", "pt": "rectangle-calculator", "de": "rectangle-calculator", "it": "rectangle-calculator"}},
    {"id": "920", "cat": "A", "block": "matematicas", "slugs": {"es": "square-calculator", "en": "square-calculator", "fr": "square-calculator", "pt": "square-calculator", "de": "square-calculator", "it": "square-calculator"}},
    {"id": "921", "cat": "A", "block": "matematicas", "slugs": {"es": "trapezoid-calculator", "en": "trapezoid-calculator", "fr": "trapezoid-calculator", "pt": "trapezoid-calculator", "de": "trapezoid-calculator", "it": "trapezoid-calculator"}},
    {"id": "922", "cat": "A", "block": "matematicas", "slugs": {"es": "cylinder-volume", "en": "cylinder-volume", "fr": "cylinder-volume", "pt": "cylinder-volume", "de": "cylinder-volume", "it": "cylinder-volume"}},
    {"id": "923", "cat": "A", "block": "matematicas", "slugs": {"es": "cone-volume", "en": "cone-volume", "fr": "cone-volume", "pt": "cone-volume", "de": "cone-volume", "it": "cone-volume"}},
    {"id": "924", "cat": "A", "block": "matematicas", "slugs": {"es": "pyramid-volume", "en": "pyramid-volume", "fr": "pyramid-volume", "pt": "pyramid-volume", "de": "pyramid-volume", "it": "pyramid-volume"}},
    {"id": "925", "cat": "A", "block": "matematicas", "slugs": {"es": "sphere-calculator", "en": "sphere-calculator", "fr": "sphere-calculator", "pt": "sphere-calculator", "de": "sphere-calculator", "it": "sphere-calculator"}},
    {"id": "926", "cat": "B", "block": "salud", "slugs": {"es": "bmr-harris-benedict", "en": "bmr-harris-benedict", "fr": "bmr-harris-benedict", "pt": "bmr-harris-benedict", "de": "bmr-harris-benedict", "it": "bmr-harris-benedict"}},
    {"id": "927", "cat": "B", "block": "salud", "slugs": {"es": "bmr-katch-mcardle", "en": "bmr-katch-mcardle", "fr": "bmr-katch-mcardle", "pt": "bmr-katch-mcardle", "de": "bmr-katch-mcardle", "it": "bmr-katch-mcardle"}},
    {"id": "928", "cat": "B", "block": "salud", "slugs": {"es": "macro-calculator", "en": "macro-calculator", "fr": "macro-calculator", "pt": "macro-calculator", "de": "macro-calculator", "it": "macro-calculator"}},
    {"id": "929", "cat": "B", "block": "salud", "slugs": {"es": "blood-pressure", "en": "blood-pressure", "fr": "blood-pressure", "pt": "blood-pressure", "de": "blood-pressure", "it": "blood-pressure"}},
    {"id": "930", "cat": "B", "block": "salud", "slugs": {"es": "waist-hip-ratio", "en": "waist-hip-ratio", "fr": "waist-hip-ratio", "pt": "waist-hip-ratio", "de": "waist-hip-ratio", "it": "waist-hip-ratio"}},
    {"id": "931", "cat": "B", "block": "salud", "slugs": {"es": "waist-height-ratio", "en": "waist-height-ratio", "fr": "waist-height-ratio", "pt": "waist-height-ratio", "de": "waist-height-ratio", "it": "waist-height-ratio"}},
    {"id": "932", "cat": "B", "block": "salud", "slugs": {"es": "weight-loss-percentage", "en": "weight-loss-percentage", "fr": "weight-loss-percentage", "pt": "weight-loss-percentage", "de": "weight-loss-percentage", "it": "weight-loss-percentage"}},
    {"id": "933", "cat": "B", "block": "salud", "slugs": {"es": "heart-rate-zones", "en": "heart-rate-zones", "fr": "heart-rate-zones", "pt": "heart-rate-zones", "de": "heart-rate-zones", "it": "heart-rate-zones"}},
    {"id": "934", "cat": "C", "block": "finanzas", "slugs": {"es": "salary-to-hourly", "en": "salary-to-hourly", "fr": "salary-to-hourly", "pt": "salary-to-hourly", "de": "salary-to-hourly", "it": "salary-to-hourly"}},
    {"id": "935", "cat": "C", "block": "finanzas", "slugs": {"es": "hourly-to-salary", "en": "hourly-to-salary", "fr": "hourly-to-salary", "pt": "hourly-to-salary", "de": "hourly-to-salary", "it": "hourly-to-salary"}},
    {"id": "936", "cat": "C", "block": "finanzas", "slugs": {"es": "mortgage-calculator", "en": "mortgage-calculator", "fr": "mortgage-calculator", "pt": "mortgage-calculator", "de": "mortgage-calculator", "it": "mortgage-calculator"}},
    {"id": "937", "cat": "C", "block": "finanzas", "slugs": {"es": "debt-payoff", "en": "debt-payoff", "fr": "debt-payoff", "pt": "debt-payoff", "de": "debt-payoff", "it": "debt-payoff"}},
    {"id": "938", "cat": "C", "block": "finanzas", "slugs": {"es": "savings-calculator", "en": "savings-calculator", "fr": "savings-calculator", "pt": "savings-calculator", "de": "savings-calculator", "it": "savings-calculator"}},
    {"id": "939", "cat": "C", "block": "finanzas", "slugs": {"es": "profit-margin", "en": "profit-margin", "fr": "profit-margin", "pt": "profit-margin", "de": "profit-margin", "it": "profit-margin"}},
    {"id": "940", "cat": "C", "block": "finanzas", "slugs": {"es": "npv-calculator", "en": "npv-calculator", "fr": "npv-calculator", "pt": "npv-calculator", "de": "npv-calculator", "it": "npv-calculator"}},
    {"id": "941", "cat": "C", "block": "finanzas", "slugs": {"es": "emergency-fund", "en": "emergency-fund", "fr": "emergency-fund", "pt": "emergency-fund", "de": "emergency-fund", "it": "emergency-fund"}},
    {"id": "942", "cat": "D", "block": "cotidiano", "slugs": {"es": "age-calculator-advanced", "en": "age-calculator-advanced", "fr": "age-calculator-advanced", "pt": "age-calculator-advanced", "de": "age-calculator-advanced", "it": "age-calculator-advanced"}},
    {"id": "943", "cat": "D", "block": "cotidiano", "slugs": {"es": "date-difference", "en": "date-difference", "fr": "date-difference", "pt": "date-difference", "de": "date-difference", "it": "date-difference"}},
    {"id": "944", "cat": "D", "block": "cotidiano", "slugs": {"es": "tip-calculator-advanced", "en": "tip-calculator-advanced", "fr": "tip-calculator-advanced", "pt": "tip-calculator-advanced", "de": "tip-calculator-advanced", "it": "tip-calculator-advanced"}},
    {"id": "945", "cat": "D", "block": "cotidiano", "slugs": {"es": "double-discount", "en": "double-discount", "fr": "double-discount", "pt": "double-discount", "de": "double-discount", "it": "double-discount"}},
    {"id": "946", "cat": "E", "block": "ciencia", "slugs": {"es": "kinetic-energy", "en": "kinetic-energy", "fr": "kinetic-energy", "pt": "kinetic-energy", "de": "kinetic-energy", "it": "kinetic-energy"}},
    {"id": "947", "cat": "E", "block": "ciencia", "slugs": {"es": "potential-energy", "en": "potential-energy", "fr": "potential-energy", "pt": "potential-energy", "de": "potential-energy", "it": "potential-energy"}},
    {"id": "948", "cat": "E", "block": "ciencia", "slugs": {"es": "work-power", "en": "work-power", "fr": "work-power", "pt": "work-power", "de": "work-power", "it": "work-power"}},
    {"id": "949", "cat": "E", "block": "ciencia", "slugs": {"es": "ohms-law-power", "en": "ohms-law-power", "fr": "ohms-law-power", "pt": "ohms-law-power", "de": "ohms-law-power", "it": "ohms-law-power"}},
    {"id": "950", "cat": "E", "block": "ciencia", "slugs": {"es": "newtons-second-law", "en": "newtons-second-law", "fr": "newtons-second-law", "pt": "newtons-second-law", "de": "newtons-second-law", "it": "newtons-second-law"}},
    {"id": "951", "cat": "B", "block": "deportes", "slugs": {"es": "one-rep-max", "en": "one-rep-max", "fr": "one-rep-max", "pt": "one-rep-max", "de": "one-rep-max", "it": "one-rep-max"}},
    {"id": "952", "cat": "B", "block": "deportes", "slugs": {"es": "running-pace-predictor", "en": "running-pace-predictor", "fr": "running-pace-predictor", "pt": "running-pace-predictor", "de": "running-pace-predictor", "it": "running-pace-predictor"}},
    {"id": "953", "cat": "B", "block": "deportes", "slugs": {"es": "vo2-max-estimator", "en": "vo2-max-estimator", "fr": "vo2-max-estimator", "pt": "vo2-max-estimator", "de": "vo2-max-estimator", "it": "vo2-max-estimator"}},
    {"id": "954", "cat": "A", "block": "conversion", "slugs": {"es": "angle-converter", "en": "angle-converter", "fr": "angle-converter", "pt": "angle-converter", "de": "angle-converter", "it": "angle-converter"}},
    {"id": "955", "cat": "A", "block": "conversion", "slugs": {"es": "temperature-full", "en": "temperature-full", "fr": "temperature-full", "pt": "temperature-full", "de": "temperature-full", "it": "temperature-full"}},
    {"id": "956", "cat": "A", "block": "conversion", "slugs": {"es": "energy-converter", "en": "energy-converter", "fr": "energy-converter", "pt": "energy-converter", "de": "energy-converter", "it": "energy-converter"}},
    {"id": "957", "cat": "A", "block": "estadistica", "slugs": {"es": "combinations-permutations", "en": "combinations-permutations", "fr": "combinations-permutations", "pt": "combinations-permutations", "de": "combinations-permutations", "it": "combinations-permutations"}},
    {"id": "958", "cat": "A", "block": "estadistica", "slugs": {"es": "z-score-percentile", "en": "z-score-percentile", "fr": "z-score-percentile", "pt": "z-score-percentile", "de": "z-score-percentile", "it": "z-score-percentile"}},
    {"id": "959", "cat": "A", "block": "estadistica", "slugs": {"es": "sample-size-confidence", "en": "sample-size-confidence", "fr": "sample-size-confidence", "pt": "sample-size-confidence", "de": "sample-size-confidence", "it": "sample-size-confidence"}},
    {"id": "960", "cat": "B", "block": "salud", "slugs": {"es": "bsa-ideal-weight", "en": "bsa-ideal-weight", "fr": "bsa-ideal-weight", "pt": "bsa-ideal-weight", "de": "bsa-ideal-weight", "it": "bsa-ideal-weight"}},
    {"id": "961", "cat": "B", "block": "salud", "slugs": {"es": "a1c-estimator", "en": "a1c-estimator", "fr": "a1c-estimator", "pt": "a1c-estimator", "de": "a1c-estimator", "it": "a1c-estimator"}},
    {"id": "962", "cat": "B", "block": "salud", "slugs": {"es": "cholesterol-ldl", "en": "cholesterol-ldl", "fr": "cholesterol-ldl", "pt": "cholesterol-ldl", "de": "cholesterol-ldl", "it": "cholesterol-ldl"}},
    # ── PHASE 2 MISSING CALCULATORS ───────────────────────────────────────
    {"id": "210", "cat": "A", "block": "matematicas", "slugs": {"es": "area-circulo", "en": "area-circulo", "fr": "area-circulo", "pt": "area-circulo", "de": "area-circulo", "it": "area-circulo"}},
    {"id": "211", "cat": "A", "block": "matematicas", "slugs": {"es": "area-triangulo", "en": "area-triangulo", "fr": "area-triangulo", "pt": "area-triangulo", "de": "area-triangulo", "it": "area-triangulo"}},
    {"id": "212", "cat": "A", "block": "matematicas", "slugs": {"es": "volumen-esfera", "en": "volumen-esfera", "fr": "volumen-esfera", "pt": "volumen-esfera", "de": "volumen-esfera", "it": "volumen-esfera"}},
    {"id": "213", "cat": "A", "block": "matematicas", "slugs": {"es": "volumen-cilindro", "en": "volumen-cilindro", "fr": "volumen-cilindro", "pt": "volumen-cilindro", "de": "volumen-cilindro", "it": "volumen-cilindro"}},
    {"id": "214", "cat": "A", "block": "matematicas", "slugs": {"es": "potencias", "en": "power-calculator", "fr": "puissance", "pt": "potencias", "de": "potenzen", "it": "potenze"}},
    {"id": "215", "cat": "A", "block": "matematicas", "slugs": {"es": "raiz", "en": "square-root", "fr": "racine-carree", "pt": "raiz-quadrada", "de": "quadratwurzel", "it": "radice-quadrata"}},
    {"id": "216", "cat": "A", "block": "matematicas", "slugs": {"es": "logaritmo", "en": "logarithm", "fr": "logarithme", "pt": "logaritmo", "de": "logarithmus", "it": "logaritmo"}},
    {"id": "217", "cat": "A", "block": "matematicas", "slugs": {"es": "factorial", "en": "factorial", "fr": "factorielle", "pt": "fatorial", "de": "fakultat", "it": "fattoriale"}},
    {"id": "218", "cat": "A", "block": "matematicas", "slugs": {"es": "ecuacion-segundo-grado", "en": "quadratic-equation", "fr": "equation-second-degre", "pt": "equacao-segundo-grau", "de": "quadratische-gleichung", "it": "equazione-secondo-grado"}},
    {"id": "219", "cat": "A", "block": "matematicas", "slugs": {"es": "mcm-mcd", "en": "lcm-gcd", "fr": "ppcm-pgcd", "pt": "mmc-mdc", "de": "kgv-ggt", "it": "mcm-mcd"}},
    {"id": "310", "cat": "C", "block": "finanzas", "slugs": {"es": "roi", "en": "roi", "fr": "roi", "pt": "roi", "de": "roi", "it": "roi"}},
    {"id": "311", "cat": "C", "block": "finanzas", "slugs": {"es": "ahorro-compuesto", "en": "compound-savings", "fr": "epargne-composee", "pt": "poupanca-composta", "de": "zinseszins-sparen", "it": "risparmio-composto"}},
    {"id": "312", "cat": "C", "block": "finanzas", "slugs": {"es": "inflacion", "en": "inflation", "fr": "inflation", "pt": "inflacao", "de": "inflation", "it": "inflazione"}},
    {"id": "313", "cat": "C", "block": "finanzas", "slugs": {"es": "subida-salarial", "en": "salary-raise", "fr": "augmentation-salaire", "pt": "aumento-salarial", "de": "gehaltserhohung", "it": "aumento-stipendio"}},
    {"id": "314", "cat": "C", "block": "finanzas", "slugs": {"es": "plan-jubilacion", "en": "retirement-plan", "fr": "plan-retraite", "pt": "plano-aposentadoria", "de": "rentenplan", "it": "piano-pensione"}},
    {"id": "315", "cat": "C", "block": "finanzas", "slugs": {"es": "regla-72", "en": "rule-of-72", "fr": "regle-72", "pt": "regra-72", "de": "regel-72", "it": "regola-72"}},
    {"id": "316", "cat": "C", "block": "finanzas", "slugs": {"es": "deposito-plazo", "en": "fixed-deposit", "fr": "depot-a-terme", "pt": "deposito-prazo", "de": "festgeld", "it": "deposito-vincolato"}},
    {"id": "317", "cat": "C", "block": "finanzas", "slugs": {"es": "retorno-acciones", "en": "stock-return", "fr": "rendement-actions", "pt": "retorno-acoes", "de": "aktienrendite", "it": "rendimento-azioni"}},
    {"id": "318", "cat": "C", "block": "finanzas", "slugs": {"es": "ratio-deuda", "en": "debt-ratio", "fr": "ratio-dette", "pt": "ratio-divida", "de": "schuldenquote", "it": "rapporto-debito"}},
    {"id": "319", "cat": "C", "block": "finanzas", "slugs": {"es": "punto-equilibrio-unidades", "en": "break-even-units", "fr": "seuil-rentabilite-unites", "pt": "ponto-equilibrio-unidades", "de": "gewinnschwelle-einheiten", "it": "punto-pareggio-unita"}},
    {"id": "410", "cat": "B", "block": "salud", "slugs": {"es": "metabolismo-basal", "en": "bmr", "fr": "metabolisme-basal", "pt": "metabolismo-basal", "de": "grundumsatz", "it": "metabolismo-basale"}},
    {"id": "411", "cat": "B", "block": "salud", "slugs": {"es": "frecuencia-cardiaca-max-salud", "en": "max-heart-rate", "fr": "fcmax-sante", "pt": "fcmax-saude", "de": "maximale-herzfrequenz", "it": "fcmax-salute"}},
    {"id": "412", "cat": "B", "block": "salud", "slugs": {"es": "horas-sueno", "en": "sleep-hours", "fr": "heures-sommeil", "pt": "horas-sono", "de": "schlafstunden", "it": "ore-sonno"}},
    {"id": "413", "cat": "B", "block": "salud", "slugs": {"es": "porcentaje-grasa", "en": "body-fat-percentage", "fr": "pourcentage-graisse", "pt": "percentual-gordura", "de": "korperfettanteil", "it": "percentuale-grasso"}},
    {"id": "414", "cat": "B", "block": "salud", "slugs": {"es": "rango-peso-saludable", "en": "healthy-weight-range", "fr": "plage-poids-sante", "pt": "faixa-peso-saudavel", "de": "gesundes-gewicht", "it": "intervallo-peso-salubre"}},
    {"id": "600", "cat": "A", "block": "estadistica", "slugs": {"es": "media", "en": "mean", "fr": "moyenne", "pt": "media", "de": "mittelwert", "it": "media"}},
    {"id": "601", "cat": "A", "block": "estadistica", "slugs": {"es": "mediana", "en": "median", "fr": "mediane", "pt": "mediana", "de": "median", "it": "mediana"}},
    {"id": "602", "cat": "A", "block": "estadistica", "slugs": {"es": "desviacion-estandar", "en": "standard-deviation", "fr": "ecart-type", "pt": "desvio-padrao", "de": "standardabweichung", "it": "deviazione-standard"}},
    {"id": "603", "cat": "A", "block": "estadistica", "slugs": {"es": "probabilidad", "en": "probability", "fr": "probabilite", "pt": "probabilidade", "de": "wahrscheinlichkeit", "it": "probabilita"}},
    {"id": "604", "cat": "A", "block": "estadistica", "slugs": {"es": "combinaciones", "en": "combinations", "fr": "combinaisons", "pt": "combinacoes", "de": "kombinationen", "it": "combinazioni"}},
    {"id": "605", "cat": "A", "block": "estadistica", "slugs": {"es": "permutaciones", "en": "permutations", "fr": "permutations", "pt": "permutacoes", "de": "permutationen", "it": "permutazioni"}},
    {"id": "606", "cat": "A", "block": "estadistica", "slugs": {"es": "intervalo-confianza", "en": "confidence-interval", "fr": "intervalle-confiance", "pt": "intervalo-confianca", "de": "konfidenzintervall", "it": "intervallo-confidenza"}},
    {"id": "607", "cat": "A", "block": "estadistica", "slugs": {"es": "coeficiente-variacion", "en": "coefficient-variation", "fr": "coefficient-variation", "pt": "coeficiente-variacao", "de": "variationskoeffizient", "it": "coefficiente-variazione"}},
    {"id": "608", "cat": "A", "block": "estadistica", "slugs": {"es": "varianza", "en": "variance", "fr": "variance", "pt": "variancia", "de": "varianz", "it": "varianza"}},
    {"id": "609", "cat": "A", "block": "estadistica", "slugs": {"es": "puntuacion-z", "en": "z-score", "fr": "score-z", "pt": "pontuacao-z", "de": "z-wert", "it": "punteggio-z"}},
    {"id": "700", "cat": "E", "block": "ciencia", "slugs": {"es": "velocidad", "en": "speed", "fr": "vitesse", "pt": "velocidade", "de": "geschwindigkeit", "it": "velocita"}},
    {"id": "701", "cat": "E", "block": "ciencia", "slugs": {"es": "densidad", "en": "density", "fr": "densite", "pt": "densidade", "de": "dichte", "it": "densita"}},
    {"id": "702", "cat": "E", "block": "ciencia", "slugs": {"es": "fuerza", "en": "force", "fr": "force", "pt": "forca", "de": "kraft", "it": "forza"}},
    {"id": "703", "cat": "E", "block": "ciencia", "slugs": {"es": "energia-cinetica", "en": "kinetic-energy", "fr": "energie-cinetique", "pt": "energia-cinetica", "de": "kinetische-energie", "it": "energia-cinetica"}},
    {"id": "704", "cat": "E", "block": "ciencia", "slugs": {"es": "energia-potencial", "en": "potential-energy", "fr": "energie-potentielle", "pt": "energia-potencial", "de": "potentielle-energie", "it": "energia-potenziale"}},
    {"id": "705", "cat": "E", "block": "ciencia", "slugs": {"es": "presion", "en": "pressure", "fr": "pression", "pt": "pressao", "de": "druck", "it": "pressione"}},
    {"id": "706", "cat": "E", "block": "ciencia", "slugs": {"es": "trabajo-mecanico", "en": "mechanical-work", "fr": "travail-mecanique", "pt": "trabalho-mecanico", "de": "mechanische-arbeit", "it": "lavoro-meccanico"}},
    {"id": "707", "cat": "E", "block": "ciencia", "slugs": {"es": "ley-ohm", "en": "ohms-law", "fr": "loi-ohm", "pt": "lei-ohm", "de": "ohmsches-gesetz", "it": "legge-ohm"}},
    {"id": "708", "cat": "E", "block": "ciencia", "slugs": {"es": "potencia-electrica", "en": "electric-power", "fr": "puissance-electrique", "pt": "potencia-eletrica", "de": "elektrische-leistung", "it": "potenza-elettrica"}},
    {"id": "709", "cat": "E", "block": "ciencia", "slugs": {"es": "aceleracion", "en": "acceleration", "fr": "acceleration", "pt": "aceleracao", "de": "beschleunigung", "it": "accelerazione"}},
    {"id": "800", "cat": "A", "block": "conversion", "slugs": {"es": "longitud", "en": "length", "fr": "longueur", "pt": "comprimento", "de": "lange", "it": "lunghezza"}},
    {"id": "801", "cat": "A", "block": "conversion", "slugs": {"es": "peso", "en": "weight", "fr": "poids", "pt": "peso", "de": "gewicht", "it": "peso"}},
    {"id": "802", "cat": "A", "block": "conversion", "slugs": {"es": "temperatura", "en": "temperature", "fr": "temperature", "pt": "temperatura", "de": "temperatur", "it": "temperatura"}},
    {"id": "803", "cat": "A", "block": "conversion", "slugs": {"es": "volumen", "en": "volume", "fr": "volume", "pt": "volume", "de": "volumen", "it": "volume"}},
    {"id": "804", "cat": "A", "block": "conversion", "slugs": {"es": "area", "en": "area", "fr": "aire", "pt": "area", "de": "flache", "it": "area"}},
    {"id": "805", "cat": "A", "block": "conversion", "slugs": {"es": "velocidad-unidades", "en": "speed-units", "fr": "vitesse-unites", "pt": "velocidade-unidades", "de": "geschwindigkeit-einheiten", "it": "velocita-unita"}},
    {"id": "806", "cat": "A", "block": "conversion", "slugs": {"es": "datos-digitales", "en": "digital-data", "fr": "donnees-numeriques", "pt": "dados-digitais", "de": "digitale-daten", "it": "dati-digitali"}},
    {"id": "807", "cat": "A", "block": "conversion", "slugs": {"es": "presion-unidades", "en": "pressure-units", "fr": "pression-unites", "pt": "pressao-unidades", "de": "druck-einheiten", "it": "pressione-unita"}},
    {"id": "808", "cat": "A", "block": "conversion", "slugs": {"es": "tiempo-unidades", "en": "time-units", "fr": "temps-unites", "pt": "tempo-unidades", "de": "zeit-einheiten", "it": "tempo-unita"}},
    {"id": "809", "cat": "A", "block": "conversion", "slugs": {"es": "energia-unidades", "en": "energy-units", "fr": "energie-unites", "pt": "energia-unidades", "de": "energie-einheiten", "it": "energia-unita"}},
    {"id": "900", "cat": "B", "block": "deportes", "slugs": {"es": "ritmo-carrera", "en": "running-pace", "fr": "allure-course", "pt": "ritmo-corrida", "de": "lauftempo", "it": "ritmo-corsa"}},
    {"id": "901", "cat": "B", "block": "deportes", "slugs": {"es": "calorias-ejercicio", "en": "exercise-calories", "fr": "calories-exercice", "pt": "calorias-exercicio", "de": "ubungskalorien", "it": "calorie-esercizio"}},
    {"id": "902", "cat": "B", "block": "deportes", "slugs": {"es": "frecuencia-cardiaca-max", "en": "max-heart-rate", "fr": "fcmax", "pt": "fcmax", "de": "maximale-herzfrequenz", "it": "fcmax"}},
    {"id": "903", "cat": "B", "block": "deportes", "slugs": {"es": "zonas-cardiacas", "en": "heart-rate-zones", "fr": "zones-cardiaques", "pt": "zonas-cardiacas", "de": "herzfrequenzzonen", "it": "zone-cardiache"}},
    {"id": "904", "cat": "B", "block": "deportes", "slugs": {"es": "vo2-max", "en": "vo2-max", "fr": "vo2max", "pt": "vo2max", "de": "vo2max", "it": "vo2max"}},
    {"id": "905", "cat": "B", "block": "deportes", "slugs": {"es": "pasos-calorias", "en": "steps-calories", "fr": "pas-calories", "pt": "passos-calorias", "de": "schritte-kalorien", "it": "passi-calorie"}},
    {"id": "906", "cat": "B", "block": "deportes", "slugs": {"es": "ritmo-natacion", "en": "swimming-pace", "fr": "allure-natation", "pt": "ritmo-natacao", "de": "schwimmtempo", "it": "ritmo-nuoto"}},
    {"id": "907", "cat": "B", "block": "deportes", "slugs": {"es": "ritmo-ciclismo", "en": "cycling-pace", "fr": "allure-cyclisme", "pt": "ritmo-ciclismo", "de": "fahrradtempo", "it": "ritmo-ciclismo"}},
    {"id": "908", "cat": "B", "block": "deportes", "slugs": {"es": "imc-deportista", "en": "athlete-bmi", "fr": "imc-athlete", "pt": "imc-atleta", "de": "sportler-bmi", "it": "bmi-atleta"}},
    {"id": "909", "cat": "B", "block": "deportes", "slugs": {"es": "tiempo-pista", "en": "track-time", "fr": "temps-piste", "pt": "tempo-pista", "de": "bahnzeit", "it": "tempo-pista"}},
    {"id": "110", "cat": "A", "block": "matematicas", "slugs": {"es": "valor-absoluto", "en": "absolute-value", "fr": "valeur-absolue", "pt": "valor-absoluto", "de": "absoluter-wert", "it": "valore-assoluto"}},
    {"id": "111", "cat": "A", "block": "matematicas", "slugs": {"es": "suma-progresion-aritmetica", "en": "arithmetic-sequence-sum", "fr": "somme-suite-arithmetique", "pt": "soma-progressao-aritmetica", "de": "arithmetische-reihe-summe", "it": "somma-sequenza-aritmetica"}},
    {"id": "112", "cat": "A", "block": "matematicas", "slugs": {"es": "suma-progresion-geometrica", "en": "geometric-sequence-sum", "fr": "somme-suite-geometrique", "pt": "soma-progressao-geometrica", "de": "geometrische-reihe-summe", "it": "somma-sequenza-geometrica"}},
    {"id": "113", "cat": "A", "block": "matematicas", "slugs": {"es": "modulo-complejo", "en": "complex-number-magnitude", "fr": "module-nombre-complexe", "pt": "modulo-numero-complexo", "de": "komplexe-betrag", "it": "modulo-numero-complesso"}},
    {"id": "114", "cat": "A", "block": "matematicas", "slugs": {"es": "determinante-matriz-2x2", "en": "matrix-2x2-determinant", "fr": "determinant-matrice-2x2", "pt": "determinante-matriz-2x2", "de": "determinante-2x2-matrix", "it": "determinante-matrice-2x2"}},
    {"id": "115", "cat": "A", "block": "matematicas", "slugs": {"es": "magnitud-vector-3d", "en": "vector-magnitude-3d", "fr": "norme-vecteur-3d", "pt": "magnitude-vetor-3d", "de": "vektor-betrag-3d", "it": "modulo-vettore-3d"}},
    {"id": "116", "cat": "A", "block": "matematicas", "slugs": {"es": "producto-escalar", "en": "dot-product-calculator", "fr": "produit-scalaire", "pt": "produto-escalar", "de": "skalarprodukt", "it": "prodotto-scalare"}},
    {"id": "117", "cat": "A", "block": "matematicas", "slugs": {"es": "producto-vectorial", "en": "cross-product-calculator", "fr": "produit-vectoriel", "pt": "produto-vetorial", "de": "kreuzprodukt", "it": "prodotto-vettoriale"}},
    {"id": "118", "cat": "A", "block": "matematicas", "slugs": {"es": "derivada-polinomio", "en": "polynomial-derivative", "fr": "derivee-polynome", "pt": "derivada-polinomio", "de": "polynom-ableitung", "it": "derivata-polinomio"}},
    {"id": "119", "cat": "A", "block": "matematicas", "slugs": {"es": "regla-trapecios-integral", "en": "trapezoidal-rule-integral", "fr": "regle-trapezes-integrale", "pt": "regra-trapezios-integral", "de": "trapezregel-integral", "it": "regola-trapezi-integrale"}},
    {"id": "120", "cat": "E", "block": "ciencia", "slugs": {"es": "movimiento-proyectil", "en": "projectile-motion", "fr": "mouvement-projectile", "pt": "movimento-projetil", "de": "wurfbewegung", "it": "moto-proiettile"}},
    {"id": "121", "cat": "E", "block": "ciencia", "slugs": {"es": "fuerza-centripeta", "en": "centripetal-force", "fr": "force-centripete", "pt": "forca-centripeta", "de": "zentripetalkraft", "it": "forza-centripeta"}},
    {"id": "122", "cat": "E", "block": "ciencia", "slugs": {"es": "fuerza-gravitatoria", "en": "gravitational-force", "fr": "force-gravitationnelle", "pt": "forca-gravitacional", "de": "gravitationskraft", "it": "forza-gravitazionale"}},
    {"id": "123", "cat": "E", "block": "ciencia", "slugs": {"es": "energia-potencial-elastica", "en": "elastic-potential-energy", "fr": "energie-potentielle-elastique", "pt": "energia-potencial-elastic", "de": "elastische-potentielle-energie", "it": "energia-potenziale-elastica"}},
    {"id": "124", "cat": "E", "block": "ciencia", "slugs": {"es": "calor-especifico", "en": "specific-heat-capacity", "fr": "capacite-thermique-massique", "pt": "calor-especifico", "de": "spezifische-warmekapazitat", "it": "calore-specifico"}},
    {"id": "125", "cat": "E", "block": "ciencia", "slugs": {"es": "velocidad-onda", "en": "wave-speed-calculator", "fr": "vitesse-onde", "pt": "velocidade-onda", "de": "wellengeschwindigkeit", "it": "velocita-onda"}},
    {"id": "126", "cat": "E", "block": "ciencia", "slugs": {"es": "ecuacion-lente-delgada", "en": "thin-lens-equation", "fr": "equation-lentille-mince", "pt": "equacao-lente-fina", "de": "duenne-linsen-gleichung", "it": "equazione-lente-sottile"}},
    {"id": "127", "cat": "E", "block": "ciencia", "slugs": {"es": "torque-momento-fuerza", "en": "torque-calculator", "fr": "calcul-couple", "pt": "calculadora-torque", "de": "drehmoment-rechner", "it": "calcolatore-coppia"}},
    {"id": "128", "cat": "E", "block": "ciencia", "slugs": {"es": "momento-angular", "en": "angular-momentum", "fr": "moment-angulaire", "pt": "momento-angular", "de": "drehimpuls", "it": "momento-angolare"}},
    {"id": "129", "cat": "E", "block": "ciencia", "slugs": {"es": "presion-fluido", "en": "fluid-pressure", "fr": "pression-fluide", "pt": "pressao-fluido", "de": "fluid-druck", "it": "pressione-fluido"}},
    {"id": "320", "cat": "C", "block": "finanzas", "slugs": {"es": "tasa-crecimiento-anual-compuesto", "en": "cagr-calculator", "fr": "taux-croissance-annuel-compose", "pt": "calculadora-cagr", "de": "cagr-rechner", "it": "calcolatore-cagr"}},
    {"id": "321", "cat": "C", "block": "finanzas", "slugs": {"es": "tasa-anual-efectiva", "en": "apr-calculator", "fr": "taux-annuel-effectif", "pt": "calculadora-tae", "de": "effektiver-jahreszins", "it": "calcolatore-taeg"}},
    {"id": "322", "cat": "C", "block": "finanzas", "slugs": {"es": "amortizacion-prestamo", "en": "loan-amortization", "fr": "amortissement-pret", "pt": "amortizacao-emprestimo", "de": "kredittilgung", "it": "ammortamento-prestito"}},
    {"id": "323", "cat": "C", "block": "finanzas", "slugs": {"es": "rentabilidad-alquiler", "en": "rental-yield", "fr": "rendement-locatif", "pt": "rentabilidade-aluguel", "de": "mietrendite", "it": "rendimento-affitto"}},
    {"id": "324", "cat": "C", "block": "finanzas", "slugs": {"es": "tasa-capitalizacion", "en": "cap-rate", "fr": "taux-capitalisation", "pt": "taxa-capitalizacao", "de": "cap-rate", "it": "tasso-capitale"}},
    {"id": "325", "cat": "C", "block": "finanzas", "slugs": {"es": "dividend-yield", "en": "dividend-yield", "fr": "rendement-dividende", "pt": "dividend-yield", "de": "dividendenrendite", "it": "dividend-yield"}},
    {"id": "326", "cat": "C", "block": "finanzas", "slugs": {"es": "ratio-per", "en": "pe-ratio", "fr": "ratio-per", "pt": "indice-pe", "de": "kgv-rechner", "it": "rapporto-pe"}},
    {"id": "327", "cat": "C", "block": "finanzas", "slugs": {"es": "valor-futuro-anualidad", "en": "future-value-annuity", "fr": "valeur-future-rente", "pt": "valor-futuro-anuidade", "de": "zukunftswert-rente", "it": "valore-futuro-rendita"}},
    {"id": "328", "cat": "C", "block": "finanzas", "slugs": {"es": "valor-actual-anualidad", "en": "present-value-annuity", "fr": "valeur-actuelle-rente", "pt": "valor-presente-anuidade", "de": "barwert-rente", "it": "valore-attuale-rendita"}},
    {"id": "329", "cat": "C", "block": "finanzas", "slugs": {"es": "wacc", "en": "wacc-calculator", "fr": "cmpc", "pt": "wacc", "de": "kalkulatorischer-zins", "it": "wacc"}},
    {"id": "415", "cat": "B", "block": "salud", "slugs": {"es": "masa-magra", "en": "lean-body-mass", "fr": "masse-maigre", "pt": "massa-magra", "de": "fettfreie-masse", "it": "massa-magra"}},
    {"id": "416", "cat": "B", "block": "salud", "slugs": {"es": "indice-adiposidad-corporal", "en": "body-adiposity-index", "fr": "indice-adiposite", "pt": "indice-adiposidade", "de": "körperadipositas-index", "it": "indice-adiposita"}},
    {"id": "417", "cat": "B", "block": "salud", "slugs": {"es": "ingesta-proteica", "en": "protein-intake", "fr": "apport-proteique", "pt": "ingestao-proteica", "de": "eiweissbedarf", "it": "assunzione-proteine"}},
    {"id": "418", "cat": "B", "block": "salud", "slugs": {"es": "ingesta-fibra", "en": "fiber-intake", "fr": "apport-fibres", "pt": "ingestao-fibra", "de": "faserbedarf", "it": "assunzione-fibre"}},
    {"id": "419", "cat": "B", "block": "salud", "slugs": {"es": "frecuencia-cardiaca-karvonen", "en": "karvonen-heart-rate", "fr": "fc-reserve-karvonen", "pt": "frequencia-cardiaca-karvonen", "de": "karvonen-herzfrequenz", "it": "frequenza-cardiaca-karvonen"}},
    {"id": "420", "cat": "B", "block": "salud", "slugs": {"es": "zonas-frecuencia-cardiaca", "en": "heart-rate-zones", "fr": "zones-frequencia-cardiaque", "pt": "zonas-frequencia-cardiaca", "de": "herzfrequenzzonen", "it": "zone-frequenza-cardiaca"}},
    {"id": "421", "cat": "B", "block": "salud", "slugs": {"es": "aclaramiento-creatinina", "en": "creatinine-clearance", "fr": "clairance-creatinine", "pt": "clearance-creatinina", "de": "kreatinin-clearance", "it": "clearance-creatinina"}},
    {"id": "422", "cat": "B", "block": "salud", "slugs": {"es": "bmi-prime", "en": "bmi-prime", "fr": "bmi-prime", "pt": "imc-prime", "de": "bmi-prime", "it": "bmi-prime"}},
    {"id": "423", "cat": "B", "block": "salud", "slugs": {"es": "fecha-parto", "en": "due-date-calculator", "fr": "date-accouchement", "pt": "data-parto", "de": "entbindungstermin", "it": "data-parto"}},
    {"id": "424", "cat": "B", "block": "salud", "slugs": {"es": "calculadora-ovulacion", "en": "ovulation-calculator", "fr": "calculateur-ovulation", "pt": "calculadora-ovulacao", "de": "eisprung-rechner", "it": "calcolatore-ovulazione"}},
    {"id": "503", "cat": "D", "block": "cotidiano", "slugs": {"es": "coste-combustible", "en": "fuel-cost", "fr": "cout-carburant", "pt": "custo-combustivel", "de": "kraftstoffkosten", "it": "costo-carburante"}},
    {"id": "504", "cat": "D", "block": "cotidiano", "slugs": {"es": "tiempo-transferencia-datos", "en": "data-transfer-time", "fr": "temps-transfert-donnees", "pt": "tempo-transferencia-dados", "de": "datenuebertragungszeit", "it": "tempo-trasferimento-dati"}},
    {"id": "505", "cat": "D", "block": "cotidiano", "slugs": {"es": "duracion-bateria", "en": "battery-life", "fr": "duree-batterie", "pt": "duracao-bateria", "de": "akkulaufzeit", "it": "durata-batteria"}},
    {"id": "506", "cat": "D", "block": "cotidiano", "slugs": {"es": "tiempo-descarga", "en": "download-time", "fr": "temps-telechargement", "pt": "tempo-download", "de": "download-zeit", "it": "tempo-download"}},
    {"id": "507", "cat": "D", "block": "cotidiano", "slugs": {"es": "dpi-pantalla", "en": "screen-dpi", "fr": "dpi-ecran", "pt": "dpi-tela", "de": "bildschirm-dpi", "it": "dpi-schermo"}},
    {"id": "508", "cat": "D", "block": "cotidiano", "slugs": {"es": "relacion-aspecto", "en": "aspect-ratio", "fr": "rapport-aspect", "pt": "proporcao-tela", "de": "seitenverhaeltnis", "it": "rapporto-aspetto"}},
    {"id": "509", "cat": "D", "block": "cotidiano", "slugs": {"es": "entropia-contrasena", "en": "password-entropy", "fr": "entropie-mot-passe", "pt": "entropia-senha", "de": "passwort-entropie", "it": "entropia-password"}},
    {"id": "510", "cat": "D", "block": "cotidiano", "slugs": {"es": "ancho-banda", "en": "bandwidth-calculator", "fr": "calcul-bandwidth", "pt": "largura-banda", "de": "bandbreite", "it": "larghezza-banda"}},
    {"id": "511", "cat": "D", "block": "cotidiano", "slugs": {"es": "tamano-archivo", "en": "file-size", "fr": "taille-fichier", "pt": "tamanho-arquivo", "de": "dateigroesse", "it": "dimensione-file"}},
    {"id": "512", "cat": "D", "block": "cotidiano", "slugs": {"es": "coste-consumo-electrico", "en": "power-cost", "fr": "cout-consommation", "pt": "custo-consumo", "de": "stromkosten", "it": "costo-consumo"}},

    {"id": "130", "cat": "A", "block": "matematicas", "slugs": {"es": "logaritmo", "en": "logarithm-calculator", "fr": "logarithme", "pt": "logaritmo", "de": "logarithmus", "it": "logaritmo"}},
    {"id": "131", "cat": "A", "block": "matematicas", "slugs": {"es": "logaritmo-natural", "en": "natural-logarithm", "fr": "logarithme-neperien", "pt": "logaritmo-natural", "de": "natuerlicher-logarithmus", "it": "logaritmo-naturale"}},
    {"id": "132", "cat": "A", "block": "matematicas", "slugs": {"es": "crecimiento-exponencial", "en": "exponential-growth", "fr": "croissance-exponentielle", "pt": "crescimento-exponencial", "de": "exponentielles-wachstum", "it": "crescita-esponenziale"}},
    {"id": "133", "cat": "A", "block": "matematicas", "slugs": {"es": "factorial", "en": "factorial-calculator", "fr": "factorielle", "pt": "fatorial", "de": "fakultaet", "it": "fattoriale"}},
    {"id": "134", "cat": "A", "block": "matematicas", "slugs": {"es": "permutaciones", "en": "permutations-calculator", "fr": "permutations", "pt": "permutacoes", "de": "permutationen", "it": "permutazioni"}},
    {"id": "135", "cat": "A", "block": "matematicas", "slugs": {"es": "combinaciones", "en": "combinations-calculator", "fr": "combinaisons", "pt": "combinacoes", "de": "kombinationen", "it": "combinazioni"}},
    {"id": "136", "cat": "A", "block": "matematicas", "slugs": {"es": "desviacion-estandar", "en": "standard-deviation", "fr": "ecart-type", "pt": "desvio-padrao", "de": "standardabweichung", "it": "deviazione-standard"}},
    {"id": "137", "cat": "A", "block": "matematicas", "slugs": {"es": "varianza", "en": "variance-calculator", "fr": "variance", "pt": "variancia", "de": "varianz", "it": "varianza"}},
    {"id": "138", "cat": "A", "block": "matematicas", "slugs": {"es": "mediana", "en": "median-calculator", "fr": "mediane", "pt": "mediana", "de": "median", "it": "mediana"}},
    {"id": "139", "cat": "A", "block": "matematicas", "slugs": {"es": "cuartiles", "en": "quartile-calculator", "fr": "quartiles", "pt": "quartis", "de": "quartile", "it": "quartili"}},
    {"id": "140", "cat": "E", "block": "ciencia", "slugs": {"es": "ecuacion-bernoulli", "en": "bernoulli-equation", "fr": "equation-bernoulli", "pt": "equacao-bernoulli", "de": "bernoulli-gleichung", "it": "equazione-bernoulli"}},
    {"id": "141", "cat": "E", "block": "ciencia", "slugs": {"es": "efecto-doppler", "en": "doppler-effect", "fr": "effet-doppler", "pt": "efeito-doppler", "de": "doppler-effekt", "it": "effetto-doppler"}},
    {"id": "142", "cat": "E", "block": "ciencia", "slugs": {"es": "ley-snell", "en": "snells-law", "fr": "loi-de-snell", "pt": "lei-de-snell", "de": "snellius-gesetz", "it": "legge-di-snell"}},
    {"id": "143", "cat": "E", "block": "ciencia", "slugs": {"es": "fuerza-coulomb", "en": "coulomb-force", "fr": "force-coulomb", "pt": "forca-coulomb", "de": "coulomb-kraft", "it": "forza-coulomb"}},
    {"id": "144", "cat": "E", "block": "ciencia", "slugs": {"es": "fuerza-magnetica-carga", "en": "magnetic-force-charge", "fr": "force-magnetique-charge", "pt": "forca-magnetica-carga", "de": "magnetische-kraft-ladung", "it": "forza-magnetica-carica"}},
    {"id": "145", "cat": "E", "block": "ciencia", "slugs": {"es": "dilatacion-termica", "en": "thermal-expansion", "fr": "dilatation-thermique", "pt": "dilatacao-termica", "de": "waermeausdehnung", "it": "dilatazione-termica"}},
    {"id": "146", "cat": "E", "block": "ciencia", "slugs": {"es": "ley-stefan-boltzmann", "en": "stefan-boltzmann-law", "fr": "loi-stefan-boltzmann", "pt": "lei-stefan-boltzmann", "de": "stefan-boltzmann-gesetz", "it": "legge-stefan-boltzmann"}},
    {"id": "147", "cat": "E", "block": "ciencia", "slugs": {"es": "circuito-rl", "en": "rl-circuit", "fr": "circuit-rl", "pt": "circuito-rl", "de": "rl-schaltung", "it": "circuito-rl"}},
    {"id": "148", "cat": "E", "block": "ciencia", "slugs": {"es": "circuito-rc", "en": "rc-circuit", "fr": "circuit-rc", "pt": "circuito-rc", "de": "rc-schaltung", "it": "circuito-rc"}},
    {"id": "149", "cat": "E", "block": "ciencia", "slugs": {"es": "ley-gases-ideales", "en": "ideal-gas-law", "fr": "loi-gaz-parfaits", "pt": "lei-gases-ideais", "de": "ideale-gasgleichung", "it": "legge-gas-ideali"}},
    {"id": "330", "cat": "C", "block": "finanzas", "slugs": {"es": "periodo-recuperacion", "en": "payback-period", "fr": "delai-recuperation", "pt": "periodo-retorno", "de": "amortisationsdauer", "it": "periodo-ritorno"}},
    {"id": "331", "cat": "C", "block": "finanzas", "slugs": {"es": "ratio-sharpe", "en": "sharpe-ratio", "fr": "ratio-sharpe", "pt": "indice-sharpe", "de": "sharpe-ratio", "it": "indice-sharpe"}},
    {"id": "332", "cat": "C", "block": "finanzas", "slugs": {"es": "rendimiento-equivalente-impuestos", "en": "tax-equivalent-yield", "fr": "rendement-equivalent-impo", "pt": "rendimento-equivalente-imposto", "de": "steueraequivalente-rendite", "it": "rendimento-equivalente-tasse"}},
    {"id": "333", "cat": "C", "block": "finanzas", "slugs": {"es": "tasa-real-retorno", "en": "real-rate-return", "fr": "taux-reel-rendement", "pt": "taxa-real-retorno", "de": "reale-rendite", "it": "tasso-reale-rendimento"}},
    {"id": "334", "cat": "C", "block": "finanzas", "slugs": {"es": "prestamo-afordable", "en": "loan-affordability", "fr": "capacite-emprunt", "pt": "capacidade-emprestimo", "de": "kreditfaehigkeit", "it": "capacita-prestito"}},
    {"id": "335", "cat": "C", "block": "finanzas", "slugs": {"es": "liquidacion-hipoteca", "en": "mortgage-payoff", "fr": "remboursement-anticipe", "pt": "quitacao-hipoteca", "de": "hypothekentilgung", "it": "estinzione-mutuo"}},
    {"id": "336", "cat": "C", "block": "finanzas", "slugs": {"es": "liquidacion-tarjeta-credito", "en": "credit-card-payoff", "fr": "remboursement-carte", "pt": "quitacao-cartao", "de": "kreditkarten-tilgung", "it": "estinzione-carta-credito"}},
    {"id": "337", "cat": "C", "block": "finanzas", "slugs": {"es": "ahorro-universidad", "en": "college-savings", "fr": "epargne-etudes", "pt": "poupanca-faculdade", "de": "studien-sparen", "it": "risparmio-universita"}},
    {"id": "338", "cat": "C", "block": "finanzas", "slugs": {"es": "necesidades-seguro-vida", "en": "life-insurance-needs", "fr": "besoins-assurance-vie", "pt": "necessidades-seguro-vida", "de": "lebensversicherungsbedarf", "it": "necessita-assicurazione-vita"}},
    {"id": "339", "cat": "C", "block": "finanzas", "slugs": {"es": "cagr-mensual", "en": "cagr-monthly", "fr": "cagr-mensuel", "pt": "cagr-mensal", "de": "cagr-monatlich", "it": "cagr-mensile"}},
    {"id": "425", "cat": "B", "block": "salud", "slugs": {"es": "grasa-corporal-navy", "en": "body-fat-navy", "fr": "graisse-corporelle-navy", "pt": "gordura-corporal-navy", "de": "koerperfett-navy", "it": "grasso-corpo-navy"}},
    {"id": "426", "cat": "B", "block": "salud", "slugs": {"es": "gasto-energetico-total", "en": "tdee-calculator", "fr": "depense-energetique-totale", "pt": "gasto-energetico-total", "de": "tdee", "it": "tdee"}},
    {"id": "427", "cat": "B", "block": "salud", "slugs": {"es": "tasa-metabolica-basal-mifflin", "en": "bmr-mifflin-st-jeor", "fr": "tmb-mifflin-st-jeor", "pt": "tmb-mifflin-st-jeor", "de": "bmr-mifflin-st-jeor", "it": "bmr-mifflin-st-jeor"}},
    {"id": "428", "cat": "B", "block": "salud", "slugs": {"es": "metabolismo-en-reposo", "en": "rmr-calculator", "fr": "metabolisme-au-repos", "pt": "taxa-metabolica-repouso", "de": "ruheumsatz", "it": "metabolismo-a-riposo"}},
    {"id": "429", "cat": "B", "block": "salud", "slugs": {"es": "mets-actividad", "en": "mets-calculator", "fr": "mets-activite", "pt": "mets-atividade", "de": "mets-aktivitaet", "it": "mets-attivita"}},
    {"id": "430", "cat": "B", "block": "salud", "slugs": {"es": "peso-objetivo", "en": "target-weight", "fr": "poids-cible", "pt": "peso-alvo", "de": "zielgewicht", "it": "peso-obiettivo"}},
    {"id": "431", "cat": "B", "block": "salud", "slugs": {"es": "aumento-peso-embarazo", "en": "pregnancy-weight-gain", "fr": "prise-poids-grossesse", "pt": "ganho-peso-gravidez", "de": "schwangerschaftsgewicht", "it": "aumento-peso-gravidanza"}},
    {"id": "432", "cat": "B", "block": "salud", "slugs": {"es": "calorias-caminar", "en": "calories-burned-walking", "fr": "calories-marche", "pt": "calorias-caminhada", "de": "kalorien-verbrauch-wandern", "it": "calorie-bruciate-camminare"}},
    {"id": "433", "cat": "B", "block": "salud", "slugs": {"es": "percentil-crecimiento-infantil", "en": "child-growth-percentile", "fr": "percentile-croissance-enfant", "pt": "percentil-crescimento-infantil", "de": "kind-wachstumsperzentile", "it": "percentile-crescita-bambino"}},
    {"id": "434", "cat": "B", "block": "salud", "slugs": {"es": "agua-por-peso", "en": "water-intake-by-weight", "fr": "eau-par-poids", "pt": "agua-por-peso", "de": "wasserbedarf-nach-gewicht", "it": "acqua-per-peso"}},
    {"id": "513", "cat": "D", "block": "cotidiano", "slugs": {"es": "resolucion-pantalla", "en": "screen-resolution", "fr": "resolution-ecran", "pt": "resolucao-tela", "de": "bildschirmaufloesung", "it": "risoluzione-schermo"}},
    {"id": "514", "cat": "D", "block": "cotidiano", "slugs": {"es": "tamano-archivo-video", "en": "video-file-size", "fr": "taille-fichier-video", "pt": "tamanho-arquivo-video", "de": "videodateigroesse", "it": "dimensione-file-video"}},
    {"id": "515", "cat": "D", "block": "cotidiano", "slugs": {"es": "capacidad-raid", "en": "raid-capacity", "fr": "capacite-raid", "pt": "capacidade-raid", "de": "raid-kapazitaet", "it": "capacita-raid"}},
    {"id": "516", "cat": "D", "block": "cotidiano", "slugs": {"es": "tiempo-actividad", "en": "server-uptime", "fr": "disponibilite-serveur", "pt": "uptime-servidor", "de": "server-verfuegbarkeit", "it": "uptime-server"}},
    {"id": "517", "cat": "D", "block": "cotidiano", "slugs": {"es": "latencia-ping", "en": "ping-latency", "fr": "latence-ping", "pt": "latencia-ping", "de": "ping-latenz", "it": "latenza-ping"}},
    {"id": "518", "cat": "D", "block": "cotidiano", "slugs": {"es": "palabras-por-minuto", "en": "typing-speed-wpm", "fr": "mots-par-minute", "pt": "palavras-por-minuto", "de": "worte-pro-minute", "it": "parole-al-minuto"}},
    {"id": "519", "cat": "D", "block": "cotidiano", "slugs": {"es": "tiempo-lectura", "en": "reading-time", "fr": "temps-de-lecture", "pt": "tempo-leitura", "de": "lesezeit", "it": "tempo-lettura"}},
    {"id": "520", "cat": "D", "block": "cotidiano", "slugs": {"es": "coste-sms", "en": "sms-cost", "fr": "cout-sms", "pt": "custo-sms", "de": "sms-kosten", "it": "costo-sms"}},
    {"id": "521", "cat": "D", "block": "cotidiano", "slugs": {"es": "estimador-datos", "en": "data-usage-estimator", "fr": "estimateur-donnees", "pt": "estimador-dados", "de": "datennutzung-schaetzer", "it": "stimatore-dati"}},
    {"id": "522", "cat": "D", "block": "cotidiano", "slugs": {"es": "brillo-pantalla-nits", "en": "screen-brightness-nits", "fr": "luminosite-ecran-nits", "pt": "brilho-tela-nits", "de": "bildschirmhelligkeit-nits", "it": "luminosita-schermo-nits"}},

    {"id": "1000", "cat": "E", "block": "quimica", "slugs": {"es": "calculadora-ph", "en": "ph-calculator", "fr": "calculateur-ph", "pt": "calculadora-ph", "de": "ph-rechner", "it": "calcolatore-ph"}},
    {"id": "1001", "cat": "E", "block": "quimica", "slugs": {"es": "calculadora-poh", "en": "poh-calculator", "fr": "calculateur-poh", "pt": "calculadora-poh", "de": "poh-rechner", "it": "calcolatore-poh"}},
    {"id": "1002", "cat": "E", "block": "quimica", "slugs": {"es": "molaridad", "en": "molarity-calculator", "fr": "molarite", "pt": "molaridade", "de": "molaritaet", "it": "molarita"}},
    {"id": "1003", "cat": "E", "block": "quimica", "slugs": {"es": "dilucion", "en": "dilution-calculator", "fr": "dilution", "pt": "diluicao", "de": "verduennung", "it": "diluizione"}},
    {"id": "1004", "cat": "E", "block": "quimica", "slugs": {"es": "ley-gases-ideales", "en": "ideal-gas-law", "fr": "loi-gaz-parfaits", "pt": "lei-gases-ideais", "de": "ideale-gasgleichung", "it": "legge-gas-ideali"}},
    {"id": "1005", "cat": "E", "block": "quimica", "slugs": {"es": "ley-boyle", "en": "boyles-law", "fr": "loi-de-boyle", "pt": "lei-de-boyle", "de": "boyle-mariotte-gesetz", "it": "legge-di-boyle"}},
    {"id": "1006", "cat": "E", "block": "quimica", "slugs": {"es": "ley-charles", "en": "charless-law", "fr": "loi-de-charles", "pt": "lei-de-charles", "de": "charles-gesetz", "it": "legge-di-charles"}},
    {"id": "1007", "cat": "E", "block": "quimica", "slugs": {"es": "energia-libre-gibbs", "en": "gibbs-free-energy", "fr": "energie-libre-gibbs", "pt": "energia-livre-gibbs", "de": "gibbs-energie", "it": "energia-libera-gibbs"}},
    {"id": "1008", "cat": "E", "block": "quimica", "slugs": {"es": "peso-molecular", "en": "molecular-weight", "fr": "poids-moleculaire", "pt": "peso-molecular", "de": "molekulargewicht", "it": "peso-molecolare"}},
    {"id": "1009", "cat": "E", "block": "quimica", "slugs": {"es": "titulacion", "en": "titration-calculator", "fr": "titrage", "pt": "titulacao", "de": "titration", "it": "titolazione"}},
    {"id": "1010", "cat": "E", "block": "electronica", "slugs": {"es": "divisor-tension", "en": "voltage-divider", "fr": "diviseur-tension", "pt": "divisor-tensao", "de": "spannungsteiler", "it": "partitore-tensione"}},
    {"id": "1011", "cat": "E", "block": "electronica", "slugs": {"es": "resistencia-led", "en": "led-resistor", "fr": "resistance-led", "pt": "resistencia-led", "de": "led-vorwiderstand", "it": "resistenza-led"}},
    {"id": "1012", "cat": "E", "block": "electronica", "slugs": {"es": "resistencia-paralelo", "en": "parallel-resistance", "fr": "resistance-parallele", "pt": "resistencia-paralelo", "de": "parallelwiderstand", "it": "resistenza-parallelo"}},
    {"id": "1013", "cat": "E", "block": "electronica", "slugs": {"es": "energia-condensador", "en": "capacitor-energy", "fr": "energie-condensateur", "pt": "energia-capacitor", "de": "kondensator-energie", "it": "energia-condensatore"}},
    {"id": "1014", "cat": "E", "block": "electronica", "slugs": {"es": "energia-bobina", "en": "inductor-energy", "fr": "energie-bobine", "pt": "energia-indutor", "de": "spulen-energie", "it": "energia-induttore"}},
    {"id": "1015", "cat": "E", "block": "electronica", "slugs": {"es": "relacion-transformador", "en": "transformer-turns-ratio", "fr": "rapport-transformateur", "pt": "relacao-transformador", "de": "uebersetzungsverhaeltnis", "it": "rapporto-transformer"}},
    {"id": "1016", "cat": "E", "block": "electronica", "slugs": {"es": "constante-tiempo-rc", "en": "rc-time-constant", "fr": "constante-temps-rc", "pt": "constante-tempo-rc", "de": "rc-zeitkonstante", "it": "costante-tempo-rc"}},
    {"id": "1017", "cat": "E", "block": "electronica", "slugs": {"es": "puente-wheatstone", "en": "wheatstone-bridge", "fr": "pont-wheatstone", "pt": "ponte-wheatstone", "de": "wheatstone-bruecke", "it": "ponte-wheatstone"}},
    {"id": "1018", "cat": "E", "block": "electronica", "slugs": {"es": "capacitancia-serie", "en": "series-capacitance", "fr": "capacite-serie", "pt": "capacitancia-serie", "de": "reihenkapazitaet", "it": "capacita-serie"}},
    {"id": "1019", "cat": "E", "block": "electronica", "slugs": {"es": "codigo-colores-resistencia", "en": "resistor-color-code", "fr": "code-couleur-resistance", "pt": "codigo-cores-resistor", "de": "widerstands-farbcode", "it": "codice-colori-resistenza"}},
    {"id": "1020", "cat": "E", "block": "clima", "slugs": {"es": "punto-rocio", "en": "dew-point-calculator", "fr": "point-rosee", "pt": "ponto-orvalho", "de": "taupunkt", "it": "punto-rugiada"}},
    {"id": "1021", "cat": "E", "block": "clima", "slugs": {"es": "indice-calor", "en": "heat-index-calculator", "fr": "indice-chaleur", "pt": "indice-calor", "de": "hitzeindex", "it": "indice-calore"}},
    {"id": "1022", "cat": "E", "block": "clima", "slugs": {"es": "sensacion-termica-viento", "en": "wind-chill-calculator", "fr": "refroidissement-eolien", "pt": "sensacao-termica-vento", "de": "windchill", "it": "percepita-vento"}},
    {"id": "1023", "cat": "E", "block": "clima", "slugs": {"es": "humedad-relativa", "en": "relative-humidity-calculator", "fr": "humidite-relative", "pt": "umidade-relativa", "de": "relative-luftfeuchtigkeit", "it": "umidita-relativa"}},
    {"id": "1024", "cat": "E", "block": "clima", "slugs": {"es": "indice-calidad-aire", "en": "air-quality-index", "fr": "indice-qualite-air", "pt": "indice-qualidade-ar", "de": "luftqualitaetsindex", "it": "indice-qualita-aria"}},
    {"id": "1025", "cat": "E", "block": "clima", "slugs": {"es": "amanecer-atardecer", "en": "sunrise-sunset-calculator", "fr": "lever-coucher-soleil", "pt": "nascer-por-sol", "de": "sonnenauf-untergang", "it": "alba-tramonto"}},
    {"id": "1026", "cat": "E", "block": "clima", "slugs": {"es": "tiempo-exposicion-uv", "en": "uv-exposure-time", "fr": "temps-exposition-uv", "pt": "tempo-exposicao-uv", "de": "uv-expositionszeit", "it": "tempo-esposizione-uv"}},
    {"id": "1027", "cat": "E", "block": "clima", "slugs": {"es": "altitud-presion", "en": "pressure-altitude", "fr": "altitude-pression", "pt": "altitude-pressao", "de": "druckhoehe", "it": "altitudine-pressione"}},
    {"id": "1028", "cat": "E", "block": "clima", "slugs": {"es": "volumen-lluvia", "en": "rainfall-volume", "fr": "volume-pluie", "pt": "volume-chuva", "de": "regenmenge", "it": "volume-pioggia"}},
    {"id": "1029", "cat": "E", "block": "clima", "slugs": {"es": "evapotranspiracion", "en": "evapotranspiration", "fr": "evapotranspiration", "pt": "evapotranspiracao", "de": "evapotranspiration", "it": "evapotraspirazione"}},
    {"id": "1030", "cat": "D", "block": "utilidades", "slugs": {"es": "dia-del-ano", "en": "day-of-year", "fr": "jour-de-lannee", "pt": "dia-do-ano", "de": "tag-des-jahres", "it": "giorno-dellanno"}},
    {"id": "1031", "cat": "D", "block": "utilidades", "slugs": {"es": "numero-semana", "en": "week-number", "fr": "numero-semaine", "pt": "numero-semana", "de": "kalenderwoche", "it": "numero-settimana"}},
    {"id": "1032", "cat": "D", "block": "utilidades", "slugs": {"es": "edad-en-dias", "en": "age-in-days", "fr": "age-en-jours", "pt": "idade-em-dias", "de": "alter-in-tagen", "it": "eta-in-giorni"}},
    {"id": "1033", "cat": "D", "block": "utilidades", "slugs": {"es": "tiempo-lectura", "en": "reading-time", "fr": "temps-de-lecture", "pt": "tempo-leitura", "de": "lesezeit", "it": "tempo-lettura"}},
    {"id": "1034", "cat": "D", "block": "utilidades", "slugs": {"es": "generador-contrasenas", "en": "password-generator", "fr": "generateur-mot-passe", "pt": "gerador-senhas", "de": "passwort-generator", "it": "generatore-password"}},
    {"id": "1035", "cat": "D", "block": "utilidades", "slugs": {"es": "numero-aleatorio", "en": "random-number", "fr": "nombre-aleatoire", "pt": "numero-aleatorio", "de": "zufallszahl", "it": "numero-casuale"}},
    {"id": "1036", "cat": "D", "block": "utilidades", "slugs": {"es": "lanzador-dados", "en": "dice-roller", "fr": "lanceur-des", "pt": "lancador-dados", "de": "wuerfel", "it": "lancio-dadi"}},
    {"id": "1037", "cat": "D", "block": "utilidades", "slugs": {"es": "cara-cruz", "en": "coin-flip", "fr": "pile-ou-face", "pt": "cara-ou-coroa", "de": "muenzwurf", "it": "testa-o-croce"}},
    {"id": "1038", "cat": "D", "block": "utilidades", "slugs": {"es": "hex-a-rgb", "en": "hex-to-rgb", "fr": "hex-a-rgb", "pt": "hex-para-rgb", "de": "hex-zu-rgb", "it": "hex-a-rgb"}},
    {"id": "1039", "cat": "D", "block": "fotografia", "slugs": {"es": "valor-exposicion", "en": "exposure-value", "fr": "valeur-exposition", "pt": "valor-exposicao", "de": "belichtungswert", "it": "valore-esposizione"}},
    {"id": "1040", "cat": "D", "block": "fotografia", "slugs": {"es": "profundidad-campo", "en": "depth-of-field", "fr": "profondeur-champ", "pt": "profundidade-campo", "de": "schaerfentiefe", "it": "profondita-campo"}},
    {"id": "1041", "cat": "D", "block": "fotografia", "slugs": {"es": "distancia-hiperfocal", "en": "hyperfocal-distance", "fr": "distance-hyperfocale", "pt": "distancia-hiperfocal", "de": "hyperfokale-distanz", "it": "distanza-iperfocale"}},
    {"id": "1042", "cat": "D", "block": "fotografia", "slugs": {"es": "suma-decibelios", "en": "decibel-addition", "fr": "addition-decibels", "pt": "adicao-decibeis", "de": "dezibel-addition", "it": "addizione-decibel"}},
    {"id": "1043", "cat": "D", "block": "fotografia", "slugs": {"es": "nivel-sonoro-distancia", "en": "spl-distance", "fr": "niveau-sonore-distance", "pt": "nivel-sonoro-distancia", "de": "schalldruckabstand", "it": "livello-sonoro-distanza"}},
    {"id": "1044", "cat": "D", "block": "fotografia", "slugs": {"es": "relacion-contraste", "en": "contrast-ratio", "fr": "rapport-contraste", "pt": "proporcao-contraste", "de": "kontrastverhaeltnis", "it": "rapporto-contrasto"}},
    {"id": "1045", "cat": "D", "block": "transporte", "slugs": {"es": "viento-cruzado", "en": "crosswind-component", "fr": "vent-de-traverse", "pt": "componente-vento", "de": "seitenwindkomponente", "it": "vento-trasversale"}},
    {"id": "1046", "cat": "D", "block": "transporte", "slugs": {"es": "consumo-combustible", "en": "fuel-burn", "fr": "consommation-carburant", "pt": "consumo-combustivel", "de": "kraftstoffverbrauch", "it": "consumo-carburante"}},
    {"id": "1047", "cat": "D", "block": "transporte", "slugs": {"es": "velocidad-verdadera", "en": "true-airspeed", "fr": "vitesse-aire-vraie", "pt": "velocidade-ar-verdadeira", "de": "wahre-fluggeschwindigkeit", "it": "velocita-aria-vera"}},
    {"id": "1048", "cat": "D", "block": "transporte", "slugs": {"es": "velocidad-casco", "en": "hull-speed", "fr": "vitesse-coque", "pt": "velocidade-casco", "de": "rumpfgeschwindigkeit", "it": "velocita-scafo"}},
    {"id": "1049", "cat": "D", "block": "transporte", "slugs": {"es": "distancia-ortodromica", "en": "great-circle-distance", "fr": "distance-orthodromique", "pt": "distancia-ortodromica", "de": "orthodrome", "it": "distanza-ortodromica"}},

    # ── BATCH 4 (1050-1099) ─────────────────────────────────────────────
    {"id": "1050", "cat": "E", "block": "matematicas", "slugs": {
        "es": "poligono-regular-area",
        "en": "poligono-regular-area",
        "fr": "poligono-regular-area",
        "pt": "poligono-regular-area",
        "de": "poligono-regular-area",
        "it": "poligono-regular-area",
    }},
    {"id": "1051", "cat": "E", "block": "matematicas", "slugs": {
        "es": "cono-volumen",
        "en": "cono-volumen",
        "fr": "cono-volumen",
        "pt": "cono-volumen",
        "de": "cono-volumen",
        "it": "cono-volumen",
    }},
    {"id": "1052", "cat": "E", "block": "matematicas", "slugs": {
        "es": "suma-aritmetica",
        "en": "suma-aritmetica",
        "fr": "suma-aritmetica",
        "pt": "suma-aritmetica",
        "de": "suma-aritmetica",
        "it": "suma-aritmetica",
    }},
    {"id": "1053", "cat": "E", "block": "matematicas", "slugs": {
        "es": "suma-geometrica",
        "en": "suma-geometrica",
        "fr": "suma-geometrica",
        "pt": "suma-geometrica",
        "de": "suma-geometrica",
        "it": "suma-geometrica",
    }},
    {"id": "1054", "cat": "E", "block": "matematicas", "slugs": {
        "es": "combinaciones",
        "en": "combinaciones",
        "fr": "combinaciones",
        "pt": "combinaciones",
        "de": "combinaciones",
        "it": "combinaciones",
    }},
    {"id": "1055", "cat": "E", "block": "ciencia", "slugs": {
        "es": "empuje-arquimedes",
        "en": "empuje-arquimedes",
        "fr": "empuje-arquimedes",
        "pt": "empuje-arquimedes",
        "de": "empuje-arquimedes",
        "it": "empuje-arquimedes",
    }},
    {"id": "1056", "cat": "E", "block": "ciencia", "slugs": {
        "es": "efecto-doppler",
        "en": "efecto-doppler",
        "fr": "efecto-doppler",
        "pt": "efecto-doppler",
        "de": "efecto-doppler",
        "it": "efecto-doppler",
    }},
    {"id": "1057", "cat": "E", "block": "ciencia", "slugs": {
        "es": "impedancia-ac",
        "en": "impedancia-ac",
        "fr": "impedancia-ac",
        "pt": "impedancia-ac",
        "de": "impedancia-ac",
        "it": "impedancia-ac",
    }},
    {"id": "1058", "cat": "E", "block": "ciencia", "slugs": {
        "es": "momento-inercia",
        "en": "momento-inercia",
        "fr": "momento-inercia",
        "pt": "momento-inercia",
        "de": "momento-inercia",
        "it": "momento-inercia",
    }},
    {"id": "1059", "cat": "E", "block": "ciencia", "slugs": {
        "es": "energia-rotacional",
        "en": "energia-rotacional",
        "fr": "energia-rotacional",
        "pt": "energia-rotacional",
        "de": "energia-rotacional",
        "it": "energia-rotacional",
    }},
    {"id": "1060", "cat": "E", "block": "salud", "slugs": {
        "es": "grasa-corporal-marina",
        "en": "grasa-corporal-marina",
        "fr": "grasa-corporal-marina",
        "pt": "grasa-corporal-marina",
        "de": "grasa-corporal-marina",
        "it": "grasa-corporal-marina",
    }},
    {"id": "1061", "cat": "E", "block": "salud", "slugs": {
        "es": "tasa-metabolica-mifflin",
        "en": "tasa-metabolica-mifflin",
        "fr": "tasa-metabolica-mifflin",
        "pt": "tasa-metabolica-mifflin",
        "de": "tasa-metabolica-mifflin",
        "it": "tasa-metabolica-mifflin",
    }},
    {"id": "1062", "cat": "E", "block": "salud", "slugs": {
        "es": "agua-diaria",
        "en": "agua-diaria",
        "fr": "agua-diaria",
        "pt": "agua-diaria",
        "de": "agua-diaria",
        "it": "agua-diaria",
    }},
    {"id": "1063", "cat": "E", "block": "salud", "slugs": {
        "es": "repeticion-maxima-brzycki",
        "en": "repeticion-maxima-brzycki",
        "fr": "repeticion-maxima-brzycki",
        "pt": "repeticion-maxima-brzycki",
        "de": "repeticion-maxima-brzycki",
        "it": "repeticion-maxima-brzycki",
    }},
    {"id": "1064", "cat": "E", "block": "salud", "slugs": {
        "es": "proteina-diaria",
        "en": "proteina-diaria",
        "fr": "proteina-diaria",
        "pt": "proteina-diaria",
        "de": "proteina-diaria",
        "it": "proteina-diaria",
    }},
    {"id": "1065", "cat": "E", "block": "finanzas", "slugs": {
        "es": "rentabilidad-dividendo",
        "en": "rentabilidad-dividendo",
        "fr": "rentabilidad-dividendo",
        "pt": "rentabilidad-dividendo",
        "de": "rentabilidad-dividendo",
        "it": "rentabilidad-dividendo",
    }},
    {"id": "1066", "cat": "E", "block": "finanzas", "slugs": {
        "es": "periodo-recuperacion",
        "en": "periodo-recuperacion",
        "fr": "periodo-recuperacion",
        "pt": "periodo-recuperacion",
        "de": "periodo-recuperacion",
        "it": "periodo-recuperacion",
    }},
    {"id": "1067", "cat": "E", "block": "finanzas", "slugs": {
        "es": "impuesto-ganancias-capital",
        "en": "impuesto-ganancias-capital",
        "fr": "impuesto-ganancias-capital",
        "pt": "impuesto-ganancias-capital",
        "de": "impuesto-ganancias-capital",
        "it": "impuesto-ganancias-capital",
    }},
    {"id": "1068", "cat": "E", "block": "finanzas", "slugs": {
        "es": "tipo-cambio-comision",
        "en": "tipo-cambio-comision",
        "fr": "tipo-cambio-comision",
        "pt": "tipo-cambio-comision",
        "de": "tipo-cambio-comision",
        "it": "tipo-cambio-comision",
    }},
    {"id": "1069", "cat": "E", "block": "finanzas", "slugs": {
        "es": "punto-equilibrio",
        "en": "punto-equilibrio",
        "fr": "punto-equilibrio",
        "pt": "punto-equilibrio",
        "de": "punto-equilibrio",
        "it": "punto-equilibrio",
    }},
    {"id": "1070", "cat": "E", "block": "quimica", "slugs": {
        "es": "masa-molar",
        "en": "masa-molar",
        "fr": "masa-molar",
        "pt": "masa-molar",
        "de": "masa-molar",
        "it": "masa-molar",
    }},
    {"id": "1071", "cat": "E", "block": "quimica", "slugs": {
        "es": "ph-hidrogeno",
        "en": "ph-hidrogeno",
        "fr": "ph-hidrogeno",
        "pt": "ph-hidrogeno",
        "de": "ph-hidrogeno",
        "it": "ph-hidrogeno",
    }},
    {"id": "1072", "cat": "E", "block": "quimica", "slugs": {
        "es": "gas-ideal",
        "en": "gas-ideal",
        "fr": "gas-ideal",
        "pt": "gas-ideal",
        "de": "gas-ideal",
        "it": "gas-ideal",
    }},
    {"id": "1073", "cat": "E", "block": "quimica", "slugs": {
        "es": "molaridad",
        "en": "molaridad",
        "fr": "molaridad",
        "pt": "molaridad",
        "de": "molaridad",
        "it": "molaridad",
    }},
    {"id": "1074", "cat": "E", "block": "quimica", "slugs": {
        "es": "dilucion",
        "en": "dilucion",
        "fr": "dilucion",
        "pt": "dilucion",
        "de": "dilucion",
        "it": "dilucion",
    }},
    {"id": "1075", "cat": "E", "block": "electronica", "slugs": {
        "es": "codigo-colores-resistencia",
        "en": "codigo-colores-resistencia",
        "fr": "codigo-colores-resistencia",
        "pt": "codigo-colores-resistencia",
        "de": "codigo-colores-resistencia",
        "it": "codigo-colores-resistencia",
    }},
    {"id": "1076", "cat": "E", "block": "electronica", "slugs": {
        "es": "energia-capacitor",
        "en": "energia-capacitor",
        "fr": "energia-capacitor",
        "pt": "energia-capacitor",
        "de": "energia-capacitor",
        "it": "energia-capacitor",
    }},
    {"id": "1077", "cat": "E", "block": "electronica", "slugs": {
        "es": "divisor-voltaje",
        "en": "divisor-voltaje",
        "fr": "divisor-voltaje",
        "pt": "divisor-voltaje",
        "de": "divisor-voltaje",
        "it": "divisor-voltaje",
    }},
    {"id": "1078", "cat": "E", "block": "electronica", "slugs": {
        "es": "constante-tiempo-rc",
        "en": "constante-tiempo-rc",
        "fr": "constante-tiempo-rc",
        "pt": "constante-tiempo-rc",
        "de": "constante-tiempo-rc",
        "it": "constante-tiempo-rc",
    }},
    {"id": "1079", "cat": "E", "block": "electronica", "slugs": {
        "es": "puente-wheatstone",
        "en": "puente-wheatstone",
        "fr": "puente-wheatstone",
        "pt": "puente-wheatstone",
        "de": "puente-wheatstone",
        "it": "puente-wheatstone",
    }},
    {"id": "1080", "cat": "E", "block": "transporte", "slugs": {
        "es": "consumo-combustible",
        "en": "consumo-combustible",
        "fr": "consumo-combustible",
        "pt": "consumo-combustible",
        "de": "consumo-combustible",
        "it": "consumo-combustible",
    }},
    {"id": "1081", "cat": "E", "block": "transporte", "slugs": {
        "es": "distancia-frenado",
        "en": "distancia-frenado",
        "fr": "distancia-frenado",
        "pt": "distancia-frenado",
        "de": "distancia-frenado",
        "it": "distancia-frenado",
    }},
    {"id": "1082", "cat": "E", "block": "transporte", "slugs": {
        "es": "cilindrada-motor",
        "en": "cilindrada-motor",
        "fr": "cilindrada-motor",
        "pt": "cilindrada-motor",
        "de": "cilindrada-motor",
        "it": "cilindrada-motor",
    }},
    {"id": "1083", "cat": "E", "block": "transporte", "slugs": {
        "es": "presion-neumaticos",
        "en": "presion-neumaticos",
        "fr": "presion-neumaticos",
        "pt": "presion-neumaticos",
        "de": "presion-neumaticos",
        "it": "presion-neumaticos",
    }},
    {"id": "1084", "cat": "E", "block": "transporte", "slugs": {
        "es": "tiempo-vuelo-viento",
        "en": "tiempo-vuelo-viento",
        "fr": "tiempo-vuelo-viento",
        "pt": "tiempo-vuelo-viento",
        "de": "tiempo-vuelo-viento",
        "it": "tiempo-vuelo-viento",
    }},
    {"id": "1085", "cat": "E", "block": "fotografia", "slugs": {
        "es": "profundidad-campo",
        "en": "profundidad-campo",
        "fr": "profundidad-campo",
        "pt": "profundidad-campo",
        "de": "profundidad-campo",
        "it": "profundidad-campo",
    }},
    {"id": "1086", "cat": "E", "block": "fotografia", "slugs": {
        "es": "numero-guia-flash",
        "en": "numero-guia-flash",
        "fr": "numero-guia-flash",
        "pt": "numero-guia-flash",
        "de": "numero-guia-flash",
        "it": "numero-guia-flash",
    }},
    {"id": "1087", "cat": "E", "block": "clima", "slugs": {
        "es": "indice-calor",
        "en": "indice-calor",
        "fr": "indice-calor",
        "pt": "indice-calor",
        "de": "indice-calor",
        "it": "indice-calor",
    }},
    {"id": "1088", "cat": "E", "block": "clima", "slugs": {
        "es": "sensacion-frio-viento",
        "en": "sensacion-frio-viento",
        "fr": "sensacion-frio-viento",
        "pt": "sensacion-frio-viento",
        "de": "sensacion-frio-viento",
        "it": "sensacion-frio-viento",
    }},
    {"id": "1089", "cat": "E", "block": "clima", "slugs": {
        "es": "humedad-relativa-rocio",
        "en": "humedad-relativa-rocio",
        "fr": "humedad-relativa-rocio",
        "pt": "humedad-relativa-rocio",
        "de": "humedad-relativa-rocio",
        "it": "humedad-relativa-rocio",
    }},
    {"id": "1090", "cat": "E", "block": "utilidades", "slugs": {
        "es": "entropia-contrasena",
        "en": "entropia-contrasena",
        "fr": "entropia-contrasena",
        "pt": "entropia-contrasena",
        "de": "entropia-contrasena",
        "it": "entropia-contrasena",
    }},
    {"id": "1091", "cat": "E", "block": "utilidades", "slugs": {
        "es": "contador-caracteres-texto",
        "en": "contador-caracteres-texto",
        "fr": "contador-caracteres-texto",
        "pt": "contador-caracteres-texto",
        "de": "contador-caracteres-texto",
        "it": "contador-caracteres-texto",
    }},
    {"id": "1092", "cat": "E", "block": "utilidades", "slugs": {
        "es": "dias-habiles",
        "en": "dias-habiles",
        "fr": "dias-habiles",
        "pt": "dias-habiles",
        "de": "dias-habiles",
        "it": "dias-habiles",
    }},
    {"id": "1093", "cat": "E", "block": "ingenieria", "slugs": {
        "es": "deflexion-viga",
        "en": "deflexion-viga",
        "fr": "deflexion-viga",
        "pt": "deflexion-viga",
        "de": "deflexion-viga",
        "it": "deflexion-viga",
    }},
    {"id": "1094", "cat": "E", "block": "ingenieria", "slugs": {
        "es": "par-apriete-tornillo",
        "en": "par-apriete-tornillo",
        "fr": "par-apriete-tornillo",
        "pt": "par-apriete-tornillo",
        "de": "par-apriete-tornillo",
        "it": "par-apriete-tornillo",
    }},
    {"id": "1095", "cat": "E", "block": "ingenieria", "slugs": {
        "es": "constante-resorte",
        "en": "constante-resorte",
        "fr": "constante-resorte",
        "pt": "constante-resorte",
        "de": "constante-resorte",
        "it": "constante-resorte",
    }},
    {"id": "1096", "cat": "E", "block": "ingenieria", "slugs": {
        "es": "numero-reynolds",
        "en": "numero-reynolds",
        "fr": "numero-reynolds",
        "pt": "numero-reynolds",
        "de": "numero-reynolds",
        "it": "numero-reynolds",
    }},
    {"id": "1097", "cat": "E", "block": "deportes", "slugs": {
        "es": "ritmo-carrera",
        "en": "ritmo-carrera",
        "fr": "ritmo-carrera",
        "pt": "ritmo-carrera",
        "de": "ritmo-carrera",
        "it": "ritmo-carrera",
    }},
    {"id": "1098", "cat": "E", "block": "deportes", "slugs": {
        "es": "handicap-golf",
        "en": "handicap-golf",
        "fr": "handicap-golf",
        "pt": "handicap-golf",
        "de": "handicap-golf",
        "it": "handicap-golf",
    }},
    {"id": "1099", "cat": "E", "block": "deportes", "slugs": {
        "es": "quemar-calorias-met",
        "en": "quemar-calorias-met",
        "fr": "quemar-calorias-met",
        "pt": "quemar-calorias-met",
        "de": "quemar-calorias-met",
        "it": "quemar-calorias-met",
    }},
]

# Quick lookup
TOOL_BY_ID = {t["id"]: t for t in TOOLS}

# ---------------------------------------------------------------------------
# Parametric variant matrices — cartesian product → pre-filled SEO pages
# Each key is a calc ID.
# "inputs": {field: [values…]}  — all combinations will be generated
# "url_template": f-string using input keys (dots replaced with hyphens)
# "title_template": per-language f-string using input keys
# "desc_template": per-language (falls back to "en")
# ---------------------------------------------------------------------------

def _fmt(v):
    """Format a numeric value for use in URLs (0.2 → 0-2, 10 → 10)."""
    s = str(v).replace(".", "-")
    return s


import math as _math

def _tile_result(size_cm, area_m2, wastage_pct, lang):
    """Pre-compute tile count for a parametric variant."""
    tile_m2 = (size_cm / 100) ** 2
    total_area = area_m2 * (1 + wastage_pct / 100)
    tiles = _math.ceil(total_area / tile_m2)
    msgs = {
        "es": f"necesitas aproximadamente <strong>{tiles} baldosas</strong> ({int(area_m2 / tile_m2)} neto + {wastage_pct}% merma)",
        "en": f"you need approximately <strong>{tiles} tiles</strong> ({int(area_m2 / tile_m2)} net + {wastage_pct}% wastage)",
        "fr": f"il vous faut environ <strong>{tiles} carreaux</strong> ({int(area_m2 / tile_m2)} net + {wastage_pct}% perte)",
        "pt": f"você precisa de aproximadamente <strong>{tiles} peças</strong> ({int(area_m2 / tile_m2)} líquido + {wastage_pct}% perda)",
        "de": f"Sie benötigen etwa <strong>{tiles} Fliesen</strong> ({int(area_m2 / tile_m2)} netto + {wastage_pct}% Verschnitt)",
        "it": f"servono circa <strong>{tiles} piastrelle</strong> ({int(area_m2 / tile_m2)} nette + {wastage_pct}% scarto)",
    }
    return msgs.get(lang, msgs["en"])


def _paint_result(area_m2, coats, wastage_pct, lang):
    """Pre-compute paint litres for a parametric variant."""
    coverage = 12.0  # m²/L typical
    litres = area_m2 * coats / coverage * (1 + wastage_pct / 100)
    litres_rounded = round(litres, 1)
    msgs = {
        "es": f"necesitas aproximadamente <strong>{litres_rounded} litros</strong> de pintura",
        "en": f"you need approximately <strong>{litres_rounded} litres</strong> of paint",
        "fr": f"il vous faut environ <strong>{litres_rounded} litres</strong> de peinture",
        "pt": f"você precisa de aproximadamente <strong>{litres_rounded} litros</strong> de tinta",
        "de": f"Sie benötigen etwa <strong>{litres_rounded} Liter</strong> Farbe",
        "it": f"servono circa <strong>{litres_rounded} litri</strong> di vernice",
    }
    return msgs.get(lang, msgs["en"])


def _brick_result(largo_m, alto_m, wastage_pct, lang):
    """Pre-compute hollow brick count for a parametric variant."""
    brick_area = 0.30 * 0.155  # standard hollow brick with 10mm joint
    wall_area = largo_m * alto_m
    bricks = _math.ceil(wall_area / brick_area * (1 + wastage_pct / 100))
    msgs = {
        "es": f"necesitas aproximadamente <strong>{bricks} ladrillos huecos</strong>",
        "en": f"you need approximately <strong>{bricks} hollow bricks</strong>",
        "fr": f"il vous faut environ <strong>{bricks} briques creuses</strong>",
        "pt": f"você precisa de aproximadamente <strong>{bricks} tijolos furados</strong>",
        "de": f"Sie benötigen etwa <strong>{bricks} Hohlziegel</strong>",
        "it": f"servono circa <strong>{bricks} mattoni forati</strong>",
    }
    return msgs.get(lang, msgs["en"])


def _pool_result(largo_m, ancho_m, prof_m, lang):
    litros = round(largo_m * ancho_m * prof_m * 1000)
    msgs = {
        "es": f"tu piscina tiene aproximadamente <strong>{litros:,} litros</strong> ({largo_m * ancho_m * prof_m:.1f} m³)",
        "en": f"your pool holds approximately <strong>{litros:,} litres</strong> ({largo_m * ancho_m * prof_m:.1f} m³)",
        "fr": f"votre piscine contient environ <strong>{litros:,} litres</strong> ({largo_m * ancho_m * prof_m:.1f} m³)",
        "pt": f"sua piscina tem aproximadamente <strong>{litros:,} litros</strong> ({largo_m * ancho_m * prof_m:.1f} m³)",
        "de": f"Ihr Pool fasst etwa <strong>{litros:,} Liter</strong> ({largo_m * ancho_m * prof_m:.1f} m³)",
        "it": f"la tua piscina contiene circa <strong>{litros:,} litri</strong> ({largo_m * ancho_m * prof_m:.1f} m³)",
    }
    return msgs.get(lang, msgs["en"])


def _topsoil_result(largo_m, ancho_m, prof_cm, lang):
    vol = round(largo_m * ancho_m * prof_cm / 100, 3)
    bags_40 = _math.ceil(vol / 0.040)
    msgs = {
        "es": f"necesitas aproximadamente <strong>{vol} m³</strong> de tierra ({bags_40} sacos de 40L)",
        "en": f"you need approximately <strong>{vol} m³</strong> of topsoil ({bags_40} × 40L bags)",
        "fr": f"il vous faut environ <strong>{vol} m³</strong> de terreau ({bags_40} sacs de 40L)",
        "pt": f"você precisa de aproximadamente <strong>{vol} m³</strong> de terra ({bags_40} sacos de 40L)",
        "de": f"Sie benötigen etwa <strong>{vol} m³</strong> Gartenerde ({bags_40} × 40L-Säcke)",
        "it": f"servono circa <strong>{vol} m³</strong> di terra ({bags_40} sacchi da 40L)",
    }
    return msgs.get(lang, msgs["en"])


def _fence_result(longitud_m, separacion_m, lang):
    postes = _math.ceil(longitud_m / separacion_m) + 1
    paneles = _math.ceil(longitud_m / separacion_m)
    msgs = {
        "es": f"necesitas <strong>{postes} postes</strong> y <strong>{paneles} paneles</strong>",
        "en": f"you need <strong>{postes} posts</strong> and <strong>{paneles} panels</strong>",
        "fr": f"il vous faut <strong>{postes} poteaux</strong> et <strong>{paneles} panneaux</strong>",
        "pt": f"você precisa de <strong>{postes} postes</strong> e <strong>{paneles} painéis</strong>",
        "de": f"Sie benötigen <strong>{postes} Pfosten</strong> und <strong>{paneles} Paneele</strong>",
        "it": f"servono <strong>{postes} pali</strong> e <strong>{paneles} pannelli</strong>",
    }
    return msgs.get(lang, msgs["en"])


PARAMETRIC_VARIANTS = {
    # ── 021 Ceramic floor tiles ── tile size × room area
    "021": {
        "inputs": {
            "tam_pieza_cm": [20, 30, 45, 60, 75, 90],
            "area": [5, 8, 10, 12, 15, 20, 25, 30, 40, 50],
        },
        "url_fn": lambda p: f"{int(p['tam_pieza_cm'])}x{int(p['tam_pieza_cm'])}-{int(p['area'])}m2",
        "title_template": {
            "en": "How Many {s}×{s}cm Tiles for {a}m²?",
            "es": "¿Cuántas Baldosas {s}×{s}cm para {a}m²?",
            "fr": "Combien de Carreaux {s}×{s}cm pour {a}m²?",
            "pt": "Quantas Cerâmicas {s}×{s}cm para {a}m²?",
            "de": "Wie Viele {s}×{s}cm Fliesen für {a}m²?",
            "it": "Quante Piastrelle {s}×{s}cm per {a}m²?",
        },
        "title_fn": lambda p, tpl: tpl.format(s=int(p["tam_pieza_cm"]), a=int(p["area"])),
        "desc_template": {
            "en": "Calculate exactly how many {s}×{s}cm ceramic tiles you need to cover {a}m², including adhesive, grout and {w}% wastage.",
            "es": "Calcula cuántas baldosas cerámicas de {s}×{s}cm necesitas para {a}m², incluyendo adhesivo, lechada y un {w}% de merma.",
            "fr": "Calculez le nombre exact de carreaux céramique {s}×{s}cm pour {a}m², avec colle, joint et {w}% de perte.",
            "pt": "Calcule quantas cerâmicas {s}×{s}cm você precisa para cobrir {a}m², com cola, rejunte e {w}% de perda.",
            "de": "Berechnen Sie, wie viele {s}×{s}cm Fliesen Sie für {a}m² brauchen, inklusive Kleber, Fuge und {w}% Verschnitt.",
            "it": "Calcola quante piastrelle {s}×{s}cm servono per {a}m², inclusi colla, stucco e {w}% di scarto.",
        },
        "desc_fn": lambda p, tpl: tpl.format(s=int(p["tam_pieza_cm"]), a=int(p["area"]), w=10),
        "result_fn": lambda p, lang: _tile_result(p["tam_pieza_cm"], p["area"], 10, lang),
        "wastage_default": 10,
    },

    # ── 027 Wall tiles (bathroom) ── tile size × wall area
    "027": {
        "inputs": {
            "tam_pieza_cm": [20, 30, 45, 60],
            "area": [3, 5, 8, 10, 12, 15, 20, 25],
        },
        "url_fn": lambda p: f"{int(p['tam_pieza_cm'])}x{int(p['tam_pieza_cm'])}-{int(p['area'])}m2",
        "title_template": {
            "en": "How Many {s}×{s}cm Wall Tiles for {a}m²?",
            "es": "¿Cuántos Azulejos {s}×{s}cm para {a}m²?",
            "fr": "Combien d'Azulejos {s}×{s}cm pour {a}m²?",
            "pt": "Quantos Revestimentos {s}×{s}cm para {a}m²?",
            "de": "Wie Viele {s}×{s}cm Wandfliesen für {a}m²?",
            "it": "Quante Piastrelle Muro {s}×{s}cm per {a}m²?",
        },
        "title_fn": lambda p, tpl: tpl.format(s=int(p["tam_pieza_cm"]), a=int(p["area"])),
        "desc_template": {
            "en": "Calculate how many {s}×{s}cm wall tiles, adhesive and grout you need for a {a}m² bathroom wall.",
            "es": "Calcula cuántos azulejos de {s}×{s}cm, adhesivo y lechada necesitas para una pared de {a}m².",
            "fr": "Calculez le nombre d'azulejos {s}×{s}cm, colle et joint pour {a}m² de mur de salle de bain.",
            "pt": "Calcule quantos revestimentos {s}×{s}cm, cola e rejunte para {a}m² de parede de banheiro.",
            "de": "Berechnen Sie Wandfliesen {s}×{s}cm, Kleber und Fuge für {a}m² Badezimmerwand.",
            "it": "Calcola piastrelle muro {s}×{s}cm, colla e stucco per {a}m² di parete bagno.",
        },
        "desc_fn": lambda p, tpl: tpl.format(s=int(p["tam_pieza_cm"]), a=int(p["area"])),
        "result_fn": lambda p, lang: _tile_result(p["tam_pieza_cm"], p["area"], 10, lang),
        "wastage_default": 10,
    },

    # ── 020 Roof tiles ── roof area × pitch
    "020": {
        "inputs": {
            "area_planta": [20, 30, 40, 50, 60, 80, 100, 120, 150, 200],
            "pendiente_pct": [15, 25, 35, 45],
        },
        "url_fn": lambda p: f"{int(p['area_planta'])}m2-{int(p['pendiente_pct'])}pct",
        "title_template": {
            "en": "How Many Roof Tiles for {a}m² at {p}% Pitch?",
            "es": "¿Cuántas Tejas para {a}m² con Pendiente {p}%?",
            "fr": "Combien de Tuiles pour {a}m² à {p}% de Pente?",
            "pt": "Quantas Telhas para {a}m² com {p}% de Inclinação?",
            "de": "Wie Viele Dachziegel für {a}m² bei {p}% Neigung?",
            "it": "Quante Tegole per {a}m² con Pendenza {p}%?",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_planta"]), p=int(p["pendiente_pct"])),
        "desc_template": {
            "en": "Calculate how many roof tiles and battens you need for a {a}m² roof plan with a {p}% pitch slope.",
            "es": "Calcula cuántas tejas y rastreles necesitas para una cubierta de {a}m² de planta con pendiente del {p}%.",
            "fr": "Calculez les tuiles et lattes pour une toiture de {a}m² avec {p}% de pente.",
            "pt": "Calcule telhas e ripas para telhado de {a}m² com inclinação de {p}%.",
            "de": "Berechnen Sie Dachziegel und Latten für ein {a}m² Dach mit {p}% Neigung.",
            "it": "Calcola tegole e listelli per un tetto di {a}m² con pendenza del {p}%.",
        },
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_planta"]), p=int(p["pendiente_pct"])),
        "wastage_default": 7,
    },

    # ── 069 Wall paint ── room area × number of coats
    "069": {
        "inputs": {
            "area": [10, 15, 20, 25, 30, 40, 50, 60, 80, 100],
            "manos": [1, 2, 3],
        },
        "url_fn": lambda p: f"{int(p['area'])}m2-{int(p['manos'])}c",
        "title_template": {
            "en": "Wall Paint for {a}m² with {m} Coat{mp} – Litres",
            "es": "Pintura para {a}m² con {m} Mano{mp} – Litros",
            "fr": "Peinture pour {a}m² en {m} Couche{mp} – Litres",
            "pt": "Tinta para {a}m² com {m} Demão{mp} – Litros",
            "de": "Wandfarbe für {a}m² mit {m} Anstrich{mp}",
            "it": "Vernice per {a}m² con {m} Mano{mp} – Litri",
        },
        "title_fn": lambda p, tpl: tpl.format(
            a=int(p["area"]), m=int(p["manos"]),
            mp="s" if int(p["manos"]) > 1 else ""
        ),
        "desc_template": {
            "en": "Calculate how many litres of wall paint you need for {a}m² with {m} coat{mp}, including 10% extra.",
            "es": "Calcula los litros de pintura para {a}m² con {m} mano{mp}, incluyendo un 10% extra.",
            "fr": "Calculez les litres de peinture pour {a}m² en {m} couche{mp}, avec 10% de marge.",
            "pt": "Calcule os litros de tinta para {a}m² com {m} demão{mp}, incluindo 10% a mais.",
            "de": "Berechnen Sie Liter Wandfarbe für {a}m² mit {m} Anstrich{mp}, inkl. 10% Reserve.",
            "it": "Calcola i litri di vernice per {a}m² con {m} mano{mp}, incluso 10% extra.",
        },
        "desc_fn": lambda p, tpl: tpl.format(
            a=int(p["area"]), m=int(p["manos"]),
            mp="s" if int(p["manos"]) > 1 else ""
        ),
        "result_fn": lambda p, lang: _paint_result(p["area"], p["manos"], 5, lang),
        "wastage_default": 5,
    },

    # ── 070 Ceiling paint ── ceiling area × coats
    "070": {
        "inputs": {
            "area_m2": [8, 10, 12, 15, 18, 20, 25, 30, 40, 50],
            "manos": [1, 2, 3],
        },
        "url_fn": lambda p: f"{int(p['area_m2'])}m2-{int(p['manos'])}c",
        "title_template": {
            "en": "Ceiling Paint for {a}m² – {m} Coat{mp}",
            "es": "Pintura Techo {a}m² – {m} Mano{mp}",
            "fr": "Peinture Plafond {a}m² – {m} Couche{mp}",
            "pt": "Tinta Teto {a}m² – {m} Demão{mp}",
            "de": "Deckenfarbe {a}m² – {m} Anstrich{mp}",
            "it": "Vernice Soffitto {a}m² – {m} Mano{mp}",
        },
        "title_fn": lambda p, tpl: tpl.format(
            a=int(p["area_m2"]), m=int(p["manos"]),
            mp="s" if int(p["manos"]) > 1 else ""
        ),
        "desc_template": {
            "en": "Calculate litres of ceiling paint for a {a}m² ceiling with {m} coat{mp}.",
            "es": "Calcula litros de pintura para un techo de {a}m² con {m} mano{mp}.",
            "fr": "Calculez les litres de peinture plafond pour {a}m² en {m} couche{mp}.",
            "pt": "Calcule litros de tinta teto para {a}m² com {m} demão{mp}.",
            "de": "Liter Deckenfarbe für {a}m² Decke mit {m} Anstrich{mp}.",
            "it": "Calcola litri di vernice soffitto per {a}m² con {m} mano{mp}.",
        },
        "desc_fn": lambda p, tpl: tpl.format(
            a=int(p["area_m2"]), m=int(p["manos"]),
            mp="s" if int(p["manos"]) > 1 else ""
        ),
        "wastage_default": 5,
    },

    # ── 073 Wallpaper rolls ── wall dimensions
    "073": {
        "inputs": {
            "longitud_pared_m": [2, 3, 4, 5, 6, 8, 10, 12],
            "altura_m": [2.4, 2.6, 2.8, 3.0],
        },
        "url_fn": lambda p: f"{_fmt(p['longitud_pared_m'])}x{_fmt(p['altura_m'])}m",
        "title_template": {
            "en": "How Many Wallpaper Rolls for {l}m × {h}m Wall?",
            "es": "¿Cuántos Rollos para Pared de {l}m × {h}m?",
            "fr": "Combien de Rouleaux pour Mur {l}m × {h}m?",
            "pt": "Quantos Rolos para Parede de {l}m × {h}m?",
            "de": "Wie Viele Tapetenrollen für {l}m × {h}m Wand?",
            "it": "Quanti Rotoli Carta da Parati per {l}m × {h}m?",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["longitud_pared_m"], h=p["altura_m"]),
        "desc_template": {
            "en": "Calculate the number of wallpaper rolls needed for a {l}m wide by {h}m high wall, including 10% wastage.",
            "es": "Calcula los rollos de papel pintado para una pared de {l}m de ancho por {h}m de alto.",
            "fr": "Calculez le nombre de rouleaux de papier peint pour un mur de {l}m × {h}m.",
            "pt": "Calcule os rolos de papel de parede para uma parede de {l}m × {h}m.",
            "de": "Berechnen Sie Tapetenrollen für eine {l}m × {h}m Wand.",
            "it": "Calcola i rotoli di carta da parati per un muro di {l}m × {h}m.",
        },
        "desc_fn": lambda p, tpl: tpl.format(l=p["longitud_pared_m"], h=p["altura_m"]),
        "wastage_default": 10,
    },

    # ── 001 Mass concrete ── slab dimensions
    "001": {
        "inputs": {
            "largo": [2, 3, 4, 5, 6, 8, 10],
            "ancho": [2, 3, 4, 5],
            "espesor": [0.10, 0.15, 0.20, 0.25, 0.30],
        },
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['ancho'])}x{_fmt(p['espesor'])}m",
        "title_template": {
            "en": "Concrete for {l}×{a}m Slab {e}m Thick – Calculator",
            "es": "Hormigón para Solera {l}×{a}m Espesor {e}m",
            "fr": "Béton pour Dalle {l}×{a}m Épaisseur {e}m",
            "pt": "Concreto para Laje {l}×{a}m Espessura {e}m",
            "de": "Beton für {l}×{a}m Platte {e}m Stark",
            "it": "Calcestruzzo per Soletta {l}×{a}m Spessore {e}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], e=p["espesor"]),
        "desc_template": {
            "en": "Calculate cement bags, sand and gravel for a {l}m × {a}m concrete slab {e}m thick.",
            "es": "Calcula sacos de cemento, arena y grava para una solera de {l}m × {a}m con {e}m de espesor.",
            "fr": "Calculez ciment, sable et gravier pour une dalle {l}m × {a}m de {e}m d'épaisseur.",
            "pt": "Calcule cimento, areia e brita para uma laje de {l}m × {a}m com {e}m de espessura.",
            "de": "Berechnen Sie Zement, Sand und Kies für eine {l}m × {a}m Betonplatte mit {e}m Stärke.",
            "it": "Calcola cemento, sabbia e ghiaia per una soletta {l}m × {a}m di {e}m di spessore.",
        },
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], e=p["espesor"]),
        "wastage_default": 7,
    },

    # ── 011 Hollow brick wall ── wall dimensions
    "011": {
        "inputs": {
            "largo": [2, 3, 4, 5, 6, 8, 10, 12],
            "alto":  [2.2, 2.5, 2.8, 3.0, 3.5],
        },
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['alto'])}m",
        "title_template": {
            "en": "How Many Bricks for {l}m × {h}m Wall? Calculator",
            "es": "¿Cuántos Ladrillos para Pared {l}×{h}m?",
            "fr": "Combien de Briques pour Mur {l}×{h}m?",
            "pt": "Quantos Tijolos para Parede {l}×{h}m?",
            "de": "Wie Viele Ziegel für {l}×{h}m Wand?",
            "it": "Quanti Mattoni per Muro {l}×{h}m?",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"]),
        "desc_template": {
            "en": "Calculate the exact number of hollow bricks and mortar needed for a {l}m wide, {h}m high wall.",
            "es": "Calcula el número exacto de ladrillos huecos y mortero para una pared de {l}m × {h}m.",
            "fr": "Calculez le nombre de briques creuses et mortier pour un mur de {l}m × {h}m.",
            "pt": "Calcule tijolos furados e argamassa para parede de {l}m × {h}m.",
            "de": "Berechnen Sie Hohlziegel und Mörtel für eine {l}m × {h}m Wand.",
            "it": "Calcola mattoni forati e malta per un muro di {l}m × {h}m.",
        },
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"]),
        "result_fn": lambda p, lang: _brick_result(p["largo"], p["alto"], 7, lang),
        "wastage_default": 7,
    },

    # ── 053 Air conditioning BTU ── room area × ceiling height
    "053": {
        "inputs": {
            "area_m2": [10, 12, 15, 18, 20, 25, 30, 35, 40, 50],
            "altura_techo": [2.4, 2.6, 2.8, 3.0],
        },
        "url_fn": lambda p: f"{int(p['area_m2'])}m2-{_fmt(p['altura_techo'])}m",
        "title_template": {
            "en": "AC BTU for {a}m² Room with {h}m Ceiling",
            "es": "BTU Aire Acondicionado para {a}m² y {h}m Techo",
            "fr": "BTU Climatiseur pour Pièce {a}m² Hauteur {h}m",
            "pt": "BTU Ar-Condicionado para {a}m² Teto {h}m",
            "de": "Klimaanlage BTU für {a}m² Raum {h}m Decke",
            "it": "BTU Climatizzatore per {a}m² Soffitto {h}m",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"]), h=p["altura_techo"]),
        "desc_template": {
            "en": "Calculate the BTU and kW power needed for an air conditioner in a {a}m² room with {h}m ceiling height.",
            "es": "Calcula los BTU y kW necesarios para un aire acondicionado en una habitación de {a}m² con techo de {h}m.",
            "fr": "Calculez les BTU et kW pour climatiser une pièce de {a}m² avec {h}m de plafond.",
            "pt": "Calcule BTU e kW para ar-condicionado em cômodo de {a}m² com teto de {h}m.",
            "de": "Berechnen Sie BTU und kW für eine Klimaanlage in einem {a}m² Raum mit {h}m Deckenhöhe.",
            "it": "Calcola BTU e kW per climatizzatore in una stanza di {a}m² con soffitto di {h}m.",
        },
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"]), h=p["altura_techo"]),
        "wastage_default": 0,
    },

    # ── 045 LED lighting lumen ── room area × room type
    "045": {
        "inputs": {
            "area_m2": [8, 10, 12, 15, 18, 20, 25, 30, 40],
            "tipo_habitacion": [1, 2, 3],  # 1=living, 2=kitchen, 3=bedroom
        },
        "url_fn": lambda p: f"{int(p['area_m2'])}m2-t{int(p['tipo_habitacion'])}",
        "title_template": {
            "en": "LED Lumens for {a}m² Room – Lighting Calculator",
            "es": "Lúmenes LED para Habitación de {a}m²",
            "fr": "Lumens LED pour Pièce de {a}m²",
            "pt": "Lumens LED para Cômodo de {a}m²",
            "de": "LED Lumen für {a}m² Raum",
            "it": "Lumen LED per Stanza di {a}m²",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "desc_template": {
            "en": "Calculate how many lumens and LED watts you need to light a {a}m² room correctly.",
            "es": "Calcula los lúmenes y vatios LED necesarios para iluminar correctamente una habitación de {a}m².",
            "fr": "Calculez les lumens et watts LED pour éclairer correctement une pièce de {a}m².",
            "pt": "Calcule lumens e watts LED para iluminar um cômodo de {a}m².",
            "de": "Berechnen Sie Lumen und LED-Watt für einen {a}m² Raum.",
            "it": "Calcola lumen e watt LED per illuminare una stanza di {a}m².",
        },
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "wastage_default": 0,
    },

    # ── 015 Thermal insulation ── wall area × thickness
    "015": {
        "inputs": {
            "largo": [3, 4, 5, 6, 8, 10],
            "alto":  [2.5, 2.8, 3.0, 3.5],
            "espesor_cm": [4, 6, 8, 10, 12],
        },
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['alto'])}m-{int(p['espesor_cm'])}cm",
        "title_template": {
            "en": "Insulation for {l}×{h}m Wall – {e}cm Thick",
            "es": "Aislamiento Pared {l}×{h}m – Espesor {e}cm",
            "fr": "Isolation Mur {l}×{h}m – Épaisseur {e}cm",
            "pt": "Isolamento Parede {l}×{h}m – Espessura {e}cm",
            "de": "Dämmung Wand {l}×{h}m – {e}cm Stärke",
            "it": "Isolamento Muro {l}×{h}m – Spessore {e}cm",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"], e=int(p["espesor_cm"])),
        "desc_template": {
            "en": "Calculate m² and volume of thermal insulation for a {l}m × {h}m wall with {e}cm EPS or mineral wool.",
            "es": "Calcula m² y volumen de aislamiento térmico para una pared de {l}m × {h}m con {e}cm de espesor.",
            "fr": "Calculez m² et volume d'isolant pour un mur {l}m × {h}m avec {e}cm d'épaisseur.",
            "pt": "Calcule m² e volume de isolamento para parede {l}m × {h}m com {e}cm de espessura.",
            "de": "Berechnen Sie m² und Volumen Wärmedämmung für eine {l}m × {h}m Wand mit {e}cm Dicke.",
            "it": "Calcola m² e volume di isolamento per muro {l}m × {h}m con {e}cm di spessore.",
        },
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"], e=int(p["espesor_cm"])),
        "wastage_default": 5,
    },

    # ── 002 Reinforced concrete slab ── dimensions × steel ratio
    "002": {
        "inputs": {"largo": [3,5,8,10], "ancho": [2,3,5], "espesor": [0.15,0.20,0.25,0.30]},
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['ancho'])}x{_fmt(p['espesor'])}m",
        "title_template": {
            "en": "Reinforced Concrete {l}×{a}m Slab {e}m Thick",
            "es": "Hormigón Armado {l}×{a}m Espesor {e}m",
            "fr": "Béton Armé Dalle {l}×{a}m Épaisseur {e}m",
            "pt": "Concreto Armado Laje {l}×{a}m Esp. {e}m",
            "de": "Stahlbeton {l}×{a}m Platte {e}m Stark",
            "it": "Cemento Armato {l}×{a}m Spessore {e}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], e=p["espesor"]),
        "desc_template": {"en": "Calculate cement, steel and aggregates for a {l}×{a}m reinforced concrete slab {e}m thick."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], e=p["espesor"]),
        "wastage_default": 7,
    },

    # ── 003 Isolated footings ── size × quantity
    "003": {
        "inputs": {"largo": [1.0,1.2,1.5,1.8,2.0], "ancho": [1.0,1.2,1.5,1.8], "cantidad": [2,4,6,8,10]},
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['ancho'])}m-{int(p['cantidad'])}ud",
        "title_template": {
            "en": "Footing {l}×{a}m – {n} Footings Concrete",
            "es": "Zapata {l}×{a}m – {n} Zapatas Aisladas",
            "fr": "Semelles {l}×{a}m – {n} Semelles Isolées",
            "pt": "Sapata {l}×{a}m – {n} Sapatas Isoladas",
            "de": "Fundament {l}×{a}m – {n} Einzelfundamente",
            "it": "Platea {l}×{a}m – {n} Fondazioni Isolate",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], n=int(p["cantidad"])),
        "desc_template": {"en": "Calculate concrete and steel for {n} isolated footings of {l}×{a}m."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], n=int(p["cantidad"])),
        "wastage_default": 7,
    },

    # ── 004 Retaining wall ── length × height
    "004": {
        "inputs": {"largo": [3,5,8,10,15,20], "altura": [1.0,1.5,2.0,2.5,3.0]},
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['altura'])}m",
        "title_template": {
            "en": "Retaining Wall {l}m Long {h}m High – Concrete",
            "es": "Muro Contención {l}m Largo {h}m Alto",
            "fr": "Mur de Soutènement {l}m × {h}m",
            "pt": "Muro de Arrimo {l}m × {h}m",
            "de": "Stützmauer {l}m Länge {h}m Höhe",
            "it": "Muro di Contenimento {l}m × {h}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["altura"]),
        "desc_template": {"en": "Calculate concrete and steel for a {l}m long, {h}m high retaining wall."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["altura"]),
        "wastage_default": 7,
    },

    # ── 005 Concrete columns ── size × quantity
    "005": {
        "inputs": {"ancho": [0.25,0.30,0.35,0.40], "altura": [2.5,3.0,3.5,4.0], "cantidad": [2,4,6,8,10]},
        "url_fn": lambda p: f"{_fmt(p['ancho'])}x{_fmt(p['ancho'])}m-h{_fmt(p['altura'])}m-{int(p['cantidad'])}ud",
        "title_template": {
            "en": "Concrete Columns {s}×{s}m, {h}m High – {n} Columns",
            "es": "Pilares Hormigón {s}×{s}m, {h}m Alto – {n} Pilares",
            "fr": "Poteaux Béton {s}×{s}m, {h}m Hauteur – {n}",
            "pt": "Pilares Concreto {s}×{s}m, {h}m Alto – {n}",
            "de": "Betonpfeiler {s}×{s}m, {h}m Hoch – {n} Stützen",
            "it": "Pilastri Cemento {s}×{s}m, {h}m Alto – {n}",
        },
        "title_fn": lambda p, tpl: tpl.format(s=p["ancho"], h=p["altura"], n=int(p["cantidad"])),
        "desc_template": {"en": "Calculate concrete, formwork and steel for {n} columns of {s}×{s}m section and {h}m height."},
        "desc_fn": lambda p, tpl: tpl.format(s=p["ancho"], h=p["altura"], n=int(p["cantidad"])),
        "wastage_default": 7,
    },

    # ── 006 Concrete beams ── section × length
    "006": {
        "inputs": {"ancho": [0.20,0.25,0.30], "canto": [0.40,0.50,0.60], "longitud": [3,4,5,6,8], "cantidad": [2,4,6]},
        "url_fn": lambda p: f"{_fmt(p['ancho'])}x{_fmt(p['canto'])}m-{_fmt(p['longitud'])}m-{int(p['cantidad'])}ud",
        "title_template": {
            "en": "Concrete Beams {w}×{d}m Section {l}m Long – {n}",
            "es": "Vigas Hormigón {w}×{d}m Sección {l}m Longitud",
            "fr": "Poutres Béton {w}×{d}m Section {l}m Longueur",
            "pt": "Vigas Concreto {w}×{d}m Seção {l}m",
            "de": "Betonträger {w}×{d}m Querschnitt {l}m Lang",
            "it": "Travi Cemento {w}×{d}m Sezione {l}m",
        },
        "title_fn": lambda p, tpl: tpl.format(w=p["ancho"], d=p["canto"], l=p["longitud"], n=int(p["cantidad"])),
        "desc_template": {"en": "Calculate concrete and steel for {n} beams with {w}×{d}m section and {l}m span."},
        "desc_fn": lambda p, tpl: tpl.format(w=p["ancho"], d=p["canto"], l=p["longitud"], n=int(p["cantidad"])),
        "wastage_default": 7,
    },

    # ── 008 Concrete flat slab ── dimensions
    "008": {
        "inputs": {"largo": [4,5,6,8,10], "ancho": [3,4,5,6], "espesor": [0.15,0.20,0.25,0.30]},
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['ancho'])}x{_fmt(p['espesor'])}m",
        "title_template": {
            "en": "Flat Slab {l}×{a}m, {e}m Thick – Concrete Calc",
            "es": "Losa Maciza {l}×{a}m Espesor {e}m",
            "fr": "Dalle Pleine {l}×{a}m Épaisseur {e}m",
            "pt": "Laje Maciça {l}×{a}m Espessura {e}m",
            "de": "Flachdecke {l}×{a}m, {e}m Stark",
            "it": "Soletta Piena {l}×{a}m Spessore {e}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], e=p["espesor"]),
        "desc_template": {"en": "Calculate concrete volume and steel reinforcement for a {l}×{a}m flat slab {e}m thick."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], e=p["espesor"]),
        "wastage_default": 7,
    },

    # ── 009 Strip foundation ── length × width × depth
    "009": {
        "inputs": {"longitud": [5,10,15,20,30], "ancho": [0.4,0.5,0.6,0.8], "profundidad": [0.4,0.5,0.6,0.8]},
        "url_fn": lambda p: f"{_fmt(p['longitud'])}x{_fmt(p['ancho'])}x{_fmt(p['profundidad'])}m",
        "title_template": {
            "en": "Strip Foundation {l}m Long {w}m Wide {d}m Deep",
            "es": "Zapata Corrida {l}m Largo {w}m Ancho {d}m Profundo",
            "fr": "Semelle Filante {l}m Longueur {w}m Largeur",
            "pt": "Sapata Corrida {l}m Comprimento {w}m Largura",
            "de": "Streifenfundament {l}m Lang {w}m Breit {d}m Tief",
            "it": "Fondazione Continua {l}m × {w}m × {d}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["longitud"], w=p["ancho"], d=p["profundidad"]),
        "desc_template": {"en": "Calculate concrete and steel for a {l}m long strip foundation, {w}m wide and {d}m deep."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["longitud"], w=p["ancho"], d=p["profundidad"]),
        "wastage_default": 7,
    },

    # ── 010 Excavation ── dimensions
    "010": {
        "inputs": {"largo": [3,5,8,10,15], "ancho": [2,3,4,5,6], "profundidad": [0.5,1.0,1.5,2.0,2.5]},
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['ancho'])}x{_fmt(p['profundidad'])}m",
        "title_template": {
            "en": "Excavation {l}×{a}m, {d}m Deep – Volume & Trucks",
            "es": "Excavación {l}×{a}m Profundidad {d}m",
            "fr": "Terrassement {l}×{a}m Profondeur {d}m",
            "pt": "Escavação {l}×{a}m Profundidade {d}m",
            "de": "Erdaushub {l}×{a}m Tiefe {d}m",
            "it": "Scavo {l}×{a}m Profondità {d}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], d=p["profundidad"]),
        "desc_template": {"en": "Calculate excavation volume and number of trucks for a {l}×{a}m pit {d}m deep."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], a=p["ancho"], d=p["profundidad"]),
        "wastage_default": 0,
    },

    # ── 012 Face brick ── wall dimensions
    "012": {
        "inputs": {"largo": [2,3,4,5,6,8,10], "alto": [2.2,2.5,2.8,3.0]},
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['alto'])}m",
        "title_template": {
            "en": "How Many Face Bricks for {l}m × {h}m Wall?",
            "es": "¿Cuántos Ladrillos Cara Vista para {l}×{h}m?",
            "fr": "Combien de Briques Parement pour {l}×{h}m?",
            "pt": "Quantos Tijolos Aparentes para {l}×{h}m?",
            "de": "Wie Viele Klinker für {l}×{h}m Wand?",
            "it": "Quanti Mattoni Faccia Vista per {l}×{h}m?",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"]),
        "desc_template": {"en": "Calculate face bricks and mortar for a {l}m wide, {h}m high wall."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"]),
        "wastage_default": 7,
    },

    # ── 013 Concrete block wall ── dimensions
    "013": {
        "inputs": {"largo": [2,3,5,6,8,10,12], "alto": [2.2,2.5,2.8,3.0,3.5]},
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['alto'])}m",
        "title_template": {
            "en": "How Many CMU Blocks for {l}m × {h}m Wall?",
            "es": "¿Cuántos Bloques para Pared {l}×{h}m?",
            "fr": "Combien de Blocs Béton pour {l}×{h}m?",
            "pt": "Quantos Blocos de Concreto para {l}×{h}m?",
            "de": "Wie Viele Betonblöcke für {l}×{h}m Wand?",
            "it": "Quanti Blocchi per Muro {l}×{h}m?",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"]),
        "desc_template": {"en": "Calculate the number of concrete blocks and mortar for a {l}m × {h}m wall."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"]),
        "wastage_default": 7,
    },

    # ── 016 Sprayed plaster ── area × thickness
    "016": {
        "inputs": {"area": [10,20,30,50,80,100,150], "espesor_mm": [10,15,20,25]},
        "url_fn": lambda p: f"{int(p['area'])}m2-{int(p['espesor_mm'])}mm",
        "title_template": {
            "en": "Sprayed Plaster for {a}m² at {e}mm Thick",
            "es": "Revoco Proyectado {a}m² Espesor {e}mm",
            "fr": "Enduit Projeté {a}m² Épaisseur {e}mm",
            "pt": "Reboco Projetado {a}m² Espessura {e}mm",
            "de": "Aufgespritzter Putz {a}m² Stärke {e}mm",
            "it": "Intonaco Proiettato {a}m² Spessore {e}mm",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area"]), e=int(p["espesor_mm"])),
        "desc_template": {"en": "Calculate kg of sprayed plaster mortar for {a}m² at {e}mm application thickness."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area"]), e=int(p["espesor_mm"])),
        "wastage_default": 5,
    },

    # ── 017 Cement mortar ── area × thickness
    "017": {
        "inputs": {"area": [10,20,30,50,80,100], "espesor_cm": [1,2,3,4,5]},
        "url_fn": lambda p: f"{int(p['area'])}m2-{int(p['espesor_cm'])}cm",
        "title_template": {
            "en": "Cement Mortar for {a}m², {e}cm Layer",
            "es": "Mortero de Cemento {a}m² Capa {e}cm",
            "fr": "Mortier Ciment {a}m² Couche {e}cm",
            "pt": "Argamassa Cimento {a}m² Camada {e}cm",
            "de": "Zementmörtel {a}m² Schicht {e}cm",
            "it": "Malta Cementizia {a}m² Strato {e}cm",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area"]), e=int(p["espesor_cm"])),
        "desc_template": {"en": "Calculate cement, sand and water for a {a}m² mortar layer {e}cm thick."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area"]), e=int(p["espesor_cm"])),
        "wastage_default": 5,
    },

    # ── 019 Stone masonry ── wall dimensions
    "019": {
        "inputs": {"largo": [2,3,5,6,8,10], "alto": [1.0,1.5,2.0,2.5,3.0]},
        "url_fn": lambda p: f"{_fmt(p['largo'])}x{_fmt(p['alto'])}m",
        "title_template": {
            "en": "Stone Masonry Wall {l}m × {h}m – Stone & Mortar",
            "es": "Mampostería Piedra Pared {l}×{h}m",
            "fr": "Maçonnerie Pierre Mur {l}×{h}m",
            "pt": "Alvenaria Pedra Parede {l}×{h}m",
            "de": "Natursteinmauer {l}m × {h}m",
            "it": "Muratura in Pietra {l}×{h}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"]),
        "desc_template": {"en": "Calculate stone and mortar quantities for a {l}m × {h}m stone masonry wall."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo"], h=p["alto"]),
        "wastage_default": 7,
    },

    # ── 022 Porcelain stoneware ── area
    "022": {
        "inputs": {"area": [5,8,10,15,20,25,30,40,50,60]},
        "url_fn": lambda p: f"{int(p['area'])}m2",
        "title_template": {
            "en": "Porcelain Tile Calculator for {a}m²",
            "es": "Gres Porcelánico para {a}m²",
            "fr": "Carrelage Grès Cérame pour {a}m²",
            "pt": "Porcelanato para {a}m²",
            "de": "Feinsteinzeug für {a}m²",
            "it": "Gres Porcellanato per {a}m²",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "desc_template": {"en": "Calculate boxes, adhesive and grout for {a}m² of porcelain stoneware flooring."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "wastage_default": 10,
    },

    # ── 023 Laminate flooring ── area
    "023": {
        "inputs": {"area": [5,8,10,12,15,20,25,30,40,50]},
        "url_fn": lambda p: f"{int(p['area'])}m2",
        "title_template": {
            "en": "How Many Laminate Flooring Boxes for {a}m²?",
            "es": "¿Cuántas Cajas de Suelo Laminado para {a}m²?",
            "fr": "Combien de Boîtes Parquet Laminé pour {a}m²?",
            "pt": "Quantas Caixas de Laminado para {a}m²?",
            "de": "Wie Viele Laminatboden-Kartons für {a}m²?",
            "it": "Quante Confezioni Laminato per {a}m²?",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "desc_template": {"en": "Calculate the number of laminate flooring boxes, underlay and skirting for {a}m²."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "wastage_default": 10,
    },

    # ── 024 Wood parquet ── area
    "024": {
        "inputs": {"area": [5,8,10,12,15,20,25,30,40,50]},
        "url_fn": lambda p: f"{int(p['area'])}m2",
        "title_template": {
            "en": "How Many Parquet Boxes for {a}m²?",
            "es": "¿Cuántas Cajas de Parquet para {a}m²?",
            "fr": "Combien de Boîtes Parquet pour {a}m²?",
            "pt": "Quantas Caixas de Parquet para {a}m²?",
            "de": "Wie Viele Parkett-Pakete für {a}m²?",
            "it": "Quante Confezioni Parquet per {a}m²?",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "desc_template": {"en": "Calculate parquet boxes, varnish and underlay for {a}m² of wood flooring."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "wastage_default": 10,
    },

    # ── 025 Marble and granite ── area
    "025": {
        "inputs": {"area": [5,8,10,15,20,25,30,40,50]},
        "url_fn": lambda p: f"{int(p['area'])}m2",
        "title_template": {
            "en": "Marble & Granite for {a}m² – Weight & Adhesive",
            "es": "Mármol y Granito para {a}m²",
            "fr": "Marbre et Granit pour {a}m²",
            "pt": "Mármore e Granito para {a}m²",
            "de": "Marmor und Granit für {a}m²",
            "it": "Marmo e Granito per {a}m²",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "desc_template": {"en": "Calculate the weight and adhesive for {a}m² of marble or granite flooring."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "wastage_default": 10,
    },

    # ── 026 Terrazzo ── area × tile size
    "026": {
        "inputs": {"area": [5,10,15,20,25,30,40,50], "tam_pieza_cm": [20,30,40,50]},
        "url_fn": lambda p: f"{int(p['tam_pieza_cm'])}x{int(p['tam_pieza_cm'])}-{int(p['area'])}m2",
        "title_template": {
            "en": "Terrazzo {s}×{s}cm Tiles for {a}m²",
            "es": "Terrazo {s}×{s}cm para {a}m²",
            "fr": "Terrazzo {s}×{s}cm pour {a}m²",
            "pt": "Granilite {s}×{s}cm para {a}m²",
            "de": "Terrazzo {s}×{s}cm für {a}m²",
            "it": "Graniglia {s}×{s}cm per {a}m²",
        },
        "title_fn": lambda p, tpl: tpl.format(s=int(p["tam_pieza_cm"]), a=int(p["area"])),
        "desc_template": {"en": "Calculate terrazzo tiles and bedding mortar for {a}m² with {s}×{s}cm pieces."},
        "desc_fn": lambda p, tpl: tpl.format(s=int(p["tam_pieza_cm"]), a=int(p["area"])),
        "wastage_default": 10,
    },

    # ── 028 Mosaic ── area
    "028": {
        "inputs": {"area": [2,3,5,8,10,15,20]},
        "url_fn": lambda p: f"{int(p['area'])}m2",
        "title_template": {
            "en": "Mosaic Tiles for {a}m² – Sheets & Adhesive",
            "es": "Mosaico para {a}m² – Mallas y Cola",
            "fr": "Mosaïque pour {a}m² – Treillis et Colle",
            "pt": "Mosaico para {a}m² – Malhas e Cola",
            "de": "Mosaikfliesen für {a}m² – Matten",
            "it": "Mosaico per {a}m² – Reti e Colla",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "desc_template": {"en": "Calculate mosaic mesh sheets, adhesive and grout for {a}m²."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area"])),
        "wastage_default": 10,
    },

    # ── 030 Tile grout ── area × tile size
    "030": {
        "inputs": {"area": [5,10,15,20,25,30,40,50], "tam_pieza_cm": [20,30,45,60,90]},
        "url_fn": lambda p: f"{int(p['tam_pieza_cm'])}cm-{int(p['area'])}m2",
        "title_template": {
            "en": "Grout for {a}m² with {s}cm Tiles – kg Needed",
            "es": "Lechada para {a}m² con Baldosas {s}cm",
            "fr": "Joint pour {a}m² avec Carreaux {s}cm",
            "pt": "Rejunte para {a}m² com Cerâmica {s}cm",
            "de": "Fugenmörtel für {a}m² mit {s}cm Fliesen",
            "it": "Stucco per {a}m² con Piastrelle {s}cm",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area"]), s=int(p["tam_pieza_cm"])),
        "desc_template": {"en": "Calculate kg of grout for {a}m² of {s}cm tiles."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area"]), s=int(p["tam_pieza_cm"])),
        "wastage_default": 5,
    },

    # ── 031 PVC drainage pipe ── length
    "031": {
        "inputs": {"longitud": [5,10,15,20,30,40,50]},
        "url_fn": lambda p: f"{int(p['longitud'])}m",
        "title_template": {
            "en": "PVC Drain Pipe for {l}m – Pipes & Fittings",
            "es": "Tubería PVC Saneamiento {l}m",
            "fr": "Tuyaux PVC Évacuation {l}m",
            "pt": "Tubos PVC Esgoto {l}m",
            "de": "PVC-Abwasserrohr {l}m",
            "it": "Tubi PVC Scarico {l}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=int(p["longitud"])),
        "desc_template": {"en": "Calculate PVC pipes and fittings needed for a {l}m drainage run."},
        "desc_fn": lambda p, tpl: tpl.format(l=int(p["longitud"])),
        "wastage_default": 0,
    },

    # ── 032 Copper / PEX pipe ── length
    "032": {
        "inputs": {"longitud": [5,10,15,20,25,30,40,50]},
        "url_fn": lambda p: f"{int(p['longitud'])}m",
        "title_template": {
            "en": "Plumbing Pipe for {l}m – Copper or PEX",
            "es": "Tubería Fontanería {l}m – Cobre o PEX",
            "fr": "Tuyaux Plomberie {l}m – Cuivre ou PEX",
            "pt": "Tubulação Hidráulica {l}m – Cobre ou PEX",
            "de": "Heizungsrohr {l}m – Kupfer oder PEX",
            "it": "Tubi Impianto Idraulico {l}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=int(p["longitud"])),
        "desc_template": {"en": "Calculate copper or PEX pipe and fittings for a {l}m plumbing installation."},
        "desc_fn": lambda p, tpl: tpl.format(l=int(p["longitud"])),
        "wastage_default": 0,
    },

    # ── 034 Water tank ── people × days
    "034": {
        "inputs": {"personas": [1,2,3,4,5,6,8,10], "dias_autonomia": [1,2,3,5,7]},
        "url_fn": lambda p: f"{int(p['personas'])}p-{int(p['dias_autonomia'])}d",
        "title_template": {
            "en": "Water Tank for {p} People, {d} Day{dp} Autonomy",
            "es": "Depósito Agua para {p} Personas, {d} Día{dp}",
            "fr": "Cuve d'Eau pour {p} Personnes, {d} Jour{dp}",
            "pt": "Caixa d'Água para {p} Pessoas, {d} Dia{dp}",
            "de": "Wassertank für {p} Personen, {d} Tag{dp}",
            "it": "Cisterna per {p} Persone, {d} Giorno{dp}",
        },
        "title_fn": lambda p, tpl: tpl.format(p=int(p["personas"]), d=int(p["dias_autonomia"]), dp="s" if int(p["dias_autonomia"]) > 1 else ""),
        "desc_template": {"en": "Calculate the water tank capacity needed for {p} people with {d} day{dp} of autonomy."},
        "desc_fn": lambda p, tpl: tpl.format(p=int(p["personas"]), d=int(p["dias_autonomia"]), dp="s" if int(p["dias_autonomia"]) > 1 else ""),
        "wastage_default": 0,
    },

    # ── 036 Gas boiler ── room area
    "036": {
        "inputs": {"area_m2": [50,75,100,120,150,180,200,250]},
        "url_fn": lambda p: f"{int(p['area_m2'])}m2",
        "title_template": {
            "en": "Gas Boiler kW for {a}m² Home",
            "es": "Caldera Gas kW para Vivienda de {a}m²",
            "fr": "Chaudière Gaz kW pour Maison {a}m²",
            "pt": "Caldeira Gás kW para Casa de {a}m²",
            "de": "Gasheizkessel kW für {a}m² Haus",
            "it": "Caldaia Gas kW per Casa di {a}m²",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "desc_template": {"en": "Calculate the gas boiler kW power needed to heat a {a}m² home."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "wastage_default": 0,
    },

    # ── 038 Underfloor heating ── area
    "038": {
        "inputs": {"area_m2": [10,15,20,25,30,40,50,60,80,100]},
        "url_fn": lambda p: f"{int(p['area_m2'])}m2",
        "title_template": {
            "en": "Underfloor Heating for {a}m² – Pipe Length",
            "es": "Suelo Radiante para {a}m² – Metros de Tubería",
            "fr": "Plancher Chauffant pour {a}m² – Longueur Tuyau",
            "pt": "Piso Aquecido para {a}m² – Metros de Tubo",
            "de": "Fußbodenheizung für {a}m² – Rohrlänge",
            "it": "Riscaldamento a Pavimento {a}m² – Lunghezza Tubo",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "desc_template": {"en": "Calculate pipe length and number of circuits for underfloor heating in {a}m²."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "wastage_default": 0,
    },

    # ── 041 Pool filter ── pool dimensions
    "041": {
        "inputs": {"largo_m": [4,5,6,8,10,12], "ancho_m": [2,3,4,5]},
        "url_fn": lambda p: f"{_fmt(p['largo_m'])}x{_fmt(p['ancho_m'])}m",
        "title_template": {
            "en": "Pool Filter for {l}×{a}m Pool – Pump Size",
            "es": "Filtro Piscina para {l}×{a}m – Tamaño Bomba",
            "fr": "Filtre Piscine pour {l}×{a}m",
            "pt": "Filtro Piscina para {l}×{a}m",
            "de": "Poolfilter für {l}×{a}m Schwimmbad",
            "it": "Filtro Piscina per {l}×{a}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo_m"], a=p["ancho_m"]),
        "desc_template": {"en": "Calculate the filter and pump size for a {l}×{a}m swimming pool."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo_m"], a=p["ancho_m"]),
        "wastage_default": 0,
    },

    # ── 043 Cable cross-section ── current × length
    "043": {
        "inputs": {"corriente_a": [6,10,16,20,25,32,40], "longitud_m": [5,10,15,20,30,40,50]},
        "url_fn": lambda p: f"{int(p['corriente_a'])}a-{int(p['longitud_m'])}m",
        "title_template": {
            "en": "Cable Size for {i}A, {l}m Circuit – mm²",
            "es": "Sección Cable para {i}A y {l}m – mm²",
            "fr": "Section Câble pour {i}A et {l}m – mm²",
            "pt": "Seção do Cabo para {i}A e {l}m – mm²",
            "de": "Kabelquerschnitt für {i}A, {l}m – mm²",
            "it": "Sezione Cavo per {i}A e {l}m – mm²",
        },
        "title_fn": lambda p, tpl: tpl.format(i=int(p["corriente_a"]), l=int(p["longitud_m"])),
        "desc_template": {"en": "Calculate the cable cross-section in mm² for a {i}A circuit over {l}m."},
        "desc_fn": lambda p, tpl: tpl.format(i=int(p["corriente_a"]), l=int(p["longitud_m"])),
        "wastage_default": 0,
    },

    # ── 044 Voltage drop ── section × length
    "044": {
        "inputs": {"seccion_mm2": [1.5,2.5,4,6,10,16], "longitud_m": [5,10,20,30,50]},
        "url_fn": lambda p: f"{_fmt(p['seccion_mm2'])}mm2-{int(p['longitud_m'])}m",
        "title_template": {
            "en": "Voltage Drop {s}mm² Cable, {l}m Circuit",
            "es": "Caída de Tensión Cable {s}mm², {l}m",
            "fr": "Chute de Tension Câble {s}mm², {l}m",
            "pt": "Queda de Tensão Cabo {s}mm², {l}m",
            "de": "Spannungsfall Kabel {s}mm², {l}m",
            "it": "Caduta di Tensione Cavo {s}mm², {l}m",
        },
        "title_fn": lambda p, tpl: tpl.format(s=p["seccion_mm2"], l=int(p["longitud_m"])),
        "desc_template": {"en": "Calculate voltage drop in % and volts for a {s}mm² cable over {l}m."},
        "desc_fn": lambda p, tpl: tpl.format(s=p["seccion_mm2"], l=int(p["longitud_m"])),
        "wastage_default": 0,
    },

    # ── 048 Solar panels ── daily consumption
    "048": {
        "inputs": {"consumo_diario_kwh": [3,5,8,10,12,15,20,25,30]},
        "url_fn": lambda p: f"{_fmt(p['consumo_diario_kwh'])}kwh-day",
        "title_template": {
            "en": "Solar Panels for {c}kWh/Day Consumption",
            "es": "Paneles Solares para {c}kWh/Día",
            "fr": "Panneaux Solaires pour {c}kWh/Jour",
            "pt": "Painéis Solares para {c}kWh/Dia",
            "de": "Solarmodule für {c}kWh/Tag Verbrauch",
            "it": "Pannelli Solari per {c}kWh/Giorno",
        },
        "title_fn": lambda p, tpl: tpl.format(c=p["consumo_diario_kwh"]),
        "desc_template": {"en": "Calculate how many solar panels you need for {c}kWh daily consumption."},
        "desc_fn": lambda p, tpl: tpl.format(c=p["consumo_diario_kwh"]),
        "wastage_default": 0,
    },

    # ── 049 Battery storage ── consumption × autonomy
    "049": {
        "inputs": {"consumo_diario_kwh": [3,5,8,10,15,20], "dias_autonomia": [1,2,3]},
        "url_fn": lambda p: f"{_fmt(p['consumo_diario_kwh'])}kwh-{int(p['dias_autonomia'])}d",
        "title_template": {
            "en": "Solar Batteries for {c}kWh/Day, {d} Day Autonomy",
            "es": "Baterías Solares para {c}kWh/Día, {d} Día",
            "fr": "Batteries Solaires pour {c}kWh/Jour, {d}j",
            "pt": "Baterias Solares para {c}kWh/Dia, {d}d",
            "de": "Solarbatterien für {c}kWh/Tag, {d} Tag",
            "it": "Batterie Solari per {c}kWh/Giorno, {d}g",
        },
        "title_fn": lambda p, tpl: tpl.format(c=p["consumo_diario_kwh"], d=int(p["dias_autonomia"])),
        "desc_template": {"en": "Calculate how many solar batteries you need for {c}kWh daily with {d} day autonomy."},
        "desc_fn": lambda p, tpl: tpl.format(c=p["consumo_diario_kwh"], d=int(p["dias_autonomia"])),
        "wastage_default": 0,
    },

    # ── 052 Electricity monthly cost ── power × hours
    "052": {
        "inputs": {"potencia_w": [500,1000,1500,2000,3000,4000,5000], "horas_dia": [1,2,4,6,8,12]},
        "url_fn": lambda p: f"{int(p['potencia_w'])}w-{int(p['horas_dia'])}h",
        "title_template": {
            "en": "Electricity Cost: {w}W for {h}h/Day – Monthly Bill",
            "es": "Coste Electricidad: {w}W, {h}h/Día",
            "fr": "Coût Électricité: {w}W, {h}h/Jour",
            "pt": "Custo Eletricidade: {w}W, {h}h/Dia",
            "de": "Stromkosten: {w}W für {h}h/Tag",
            "it": "Costo Elettricità: {w}W, {h}h/Giorno",
        },
        "title_fn": lambda p, tpl: tpl.format(w=int(p["potencia_w"]), h=int(p["horas_dia"])),
        "desc_template": {"en": "Calculate the monthly electricity cost for a {w}W appliance running {h} hours per day."},
        "desc_fn": lambda p, tpl: tpl.format(w=int(p["potencia_w"]), h=int(p["horas_dia"])),
        "wastage_default": 0,
    },

    # ── 061 Windows ── quantity × dimensions
    "061": {
        "inputs": {"num_ventanas": [1,2,3,4,5,6,8,10], "ancho_m": [0.8,1.0,1.2,1.5], "alto_m": [1.0,1.2,1.5]},
        "url_fn": lambda p: f"{int(p['num_ventanas'])}ud-{_fmt(p['ancho_m'])}x{_fmt(p['alto_m'])}m",
        "title_template": {
            "en": "{n} Windows {w}×{h}m – PVC Aluminium Cost",
            "es": "{n} Ventanas {w}×{h}m – Precio PVC Aluminio",
            "fr": "{n} Fenêtres {w}×{h}m – Prix PVC Aluminium",
            "pt": "{n} Janelas {w}×{h}m – Preço PVC Alumínio",
            "de": "{n} Fenster {w}×{h}m – PVC Aluminium",
            "it": "{n} Finestre {w}×{h}m – PVC Alluminio",
        },
        "title_fn": lambda p, tpl: tpl.format(n=int(p["num_ventanas"]), w=p["ancho_m"], h=p["alto_m"]),
        "desc_template": {"en": "Calculate the total m² and glass area for {n} windows of {w}×{h}m."},
        "desc_fn": lambda p, tpl: tpl.format(n=int(p["num_ventanas"]), w=p["ancho_m"], h=p["alto_m"]),
        "wastage_default": 0,
    },

    # ── 062 Interior doors ── quantity
    "062": {
        "inputs": {"num_puertas": [1,2,3,4,5,6,8,10], "ancho_m": [0.70,0.82,0.90,1.00]},
        "url_fn": lambda p: f"{int(p['num_puertas'])}ud-{_fmt(p['ancho_m'])}m",
        "title_template": {
            "en": "{n} Interior Doors {w}m Wide – Frames & Hinges",
            "es": "{n} Puertas Interior {w}m – Marcos y Bisagras",
            "fr": "{n} Portes Intérieures {w}m – Cadres",
            "pt": "{n} Portas Internas {w}m – Marcos",
            "de": "{n} Innentüren {w}m Breit – Zargen",
            "it": "{n} Porte Interne {w}m – Telai",
        },
        "title_fn": lambda p, tpl: tpl.format(n=int(p["num_puertas"]), w=p["ancho_m"]),
        "desc_template": {"en": "Calculate frames, hinges and hardware for {n} interior doors of {w}m width."},
        "desc_fn": lambda p, tpl: tpl.format(n=int(p["num_puertas"]), w=p["ancho_m"]),
        "wastage_default": 0,
    },

    # ── 064 Wooden staircase ── height
    "064": {
        "inputs": {"altura_total_m": [2.2,2.4,2.6,2.8,3.0,3.2,3.5,4.0]},
        "url_fn": lambda p: f"h{_fmt(p['altura_total_m'])}m",
        "title_template": {
            "en": "Wooden Staircase for {h}m Floor Height – Steps",
            "es": "Escalera Madera Altura {h}m – Peldaños",
            "fr": "Escalier Bois Hauteur {h}m – Marches",
            "pt": "Escada Madeira Altura {h}m – Degraus",
            "de": "Holztreppe Geschosshöhe {h}m – Stufen",
            "it": "Scala in Legno Altezza {h}m – Gradini",
        },
        "title_fn": lambda p, tpl: tpl.format(h=p["altura_total_m"]),
        "desc_template": {"en": "Calculate treads, risers and wood for a staircase with {h}m total height."},
        "desc_fn": lambda p, tpl: tpl.format(h=p["altura_total_m"]),
        "wastage_default": 0,
    },

    # ── 065 Metal railing ── length × height
    "065": {
        "inputs": {"longitud_m": [2,3,5,6,8,10,12,15,20], "altura_m": [0.9,1.0,1.1,1.2]},
        "url_fn": lambda p: f"{_fmt(p['longitud_m'])}x{_fmt(p['altura_m'])}m",
        "title_template": {
            "en": "Metal Railing {l}m Long, {h}m High – Steel",
            "es": "Barandilla Metálica {l}m Longitud {h}m Alto",
            "fr": "Garde-Corps Métal {l}m × {h}m",
            "pt": "Corrimão Metálico {l}m × {h}m",
            "de": "Metallgeländer {l}m Lang {h}m Hoch",
            "it": "Ringhiera Metallica {l}m × {h}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["longitud_m"], h=p["altura_m"]),
        "desc_template": {"en": "Calculate posts, handrail and balusters for a {l}m metal railing at {h}m height."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["longitud_m"], h=p["altura_m"]),
        "wastage_default": 0,
    },

    # ── 069 Wall paint (with rendimiento field) ── area × coats
    # Note: calc 069 uses area_m2 + manos + rendimiento_m2_l
    # Already handled above as "069" with area+manos; keep consistent

    # ── 071 Synthetic enamel ── area × coats
    "071": {
        "inputs": {"area_m2": [5,8,10,15,20,25,30,40,50], "manos": [1,2,3]},
        "url_fn": lambda p: f"{int(p['area_m2'])}m2-{int(p['manos'])}c",
        "title_template": {
            "en": "Enamel Paint for {a}m² with {m} Coat{mp}",
            "es": "Esmalte Sintético {a}m² con {m} Mano{mp}",
            "fr": "Laque Synthétique {a}m² en {m} Couche{mp}",
            "pt": "Esmalte Sintético {a}m² com {m} Demão{mp}",
            "de": "Lack {a}m² mit {m} Anstrich{mp}",
            "it": "Smalto Sintetico {a}m² con {m} Mano{mp}",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"]), m=int(p["manos"]), mp="s" if int(p["manos"]) > 1 else ""),
        "desc_template": {"en": "Calculate litres of synthetic enamel for {a}m² with {m} coat{mp}."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"]), m=int(p["manos"]), mp="s" if int(p["manos"]) > 1 else ""),
        "wastage_default": 5,
    },

    # ── 072 Exterior varnish ── area × coats
    "072": {
        "inputs": {"area_m2": [5,8,10,15,20,25,30,40], "manos": [2,3,4]},
        "url_fn": lambda p: f"{int(p['area_m2'])}m2-{int(p['manos'])}c",
        "title_template": {
            "en": "Wood Varnish for {a}m² – {m} Coats",
            "es": "Barniz Madera {a}m² – {m} Manos",
            "fr": "Vernis Bois {a}m² – {m} Couches",
            "pt": "Verniz Madeira {a}m² – {m} Demãos",
            "de": "Holzlasur {a}m² – {m} Anstriche",
            "it": "Verniciatura Legno {a}m² – {m} Mani",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"]), m=int(p["manos"])),
        "desc_template": {"en": "Calculate litres of exterior wood varnish for {a}m² with {m} coats."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"]), m=int(p["manos"])),
        "wastage_default": 5,
    },

    # ── 074 Textured finish ── area
    "074": {
        "inputs": {"area_m2": [10,15,20,30,40,50,60,80,100]},
        "url_fn": lambda p: f"{int(p['area_m2'])}m2",
        "title_template": {
            "en": "Textured Finish for {a}m² – kg Needed",
            "es": "Textura Paredes para {a}m² – kg",
            "fr": "Enduit Décoratif pour {a}m² – kg",
            "pt": "Textura Parede para {a}m² – kg",
            "de": "Strukturputz für {a}m² – kg",
            "it": "Finitura Decorativa per {a}m² – kg",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "desc_template": {"en": "Calculate kg of textured coating for {a}m² of wall."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "wastage_default": 5,
    },

    # ── 075 Primer ── area
    "075": {
        "inputs": {"area_m2": [10,15,20,30,40,50,60,80,100]},
        "url_fn": lambda p: f"{int(p['area_m2'])}m2",
        "title_template": {
            "en": "Primer & Sealer for {a}m² – Litres",
            "es": "Imprimación para {a}m² – Litros",
            "fr": "Primaire d'Accrochage pour {a}m² – Litres",
            "pt": "Selador para {a}m² – Litros",
            "de": "Grundierung für {a}m² – Liter",
            "it": "Primer per {a}m² – Litri",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "desc_template": {"en": "Calculate litres of primer or sealer needed for {a}m² of wall."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"])),
        "wastage_default": 5,
    },

    # ── 076 Filler / putty ── area × coats
    "076": {
        "inputs": {"area_m2": [10,15,20,30,40,50,80,100], "pasadas": [1,2,3]},
        "url_fn": lambda p: f"{int(p['area_m2'])}m2-{int(p['pasadas'])}p",
        "title_template": {
            "en": "Filler for {a}m² Wall – {p} Pass{pp}",
            "es": "Masilla para {a}m² – {p} Mano{pp}",
            "fr": "Enduit de Lissage {a}m² – {p} Passe{pp}",
            "pt": "Massa Corrida {a}m² – {p} Demão{pp}",
            "de": "Spachtelmasse {a}m² – {p} Lage{pp}",
            "it": "Rasatura {a}m² – {p} Mano{pp}",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"]), p=int(p["pasadas"]), pp="es" if int(p["pasadas"]) > 1 else ""),
        "desc_template": {"en": "Calculate kg of filler or putty for {a}m² wall with {p} pass{pp}."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["area_m2"]), p=int(p["pasadas"]), pp="es" if int(p["pasadas"]) > 1 else ""),
        "wastage_default": 5,
    },

    # ── 082 Fuel cost ── distance × consumption
    "082": {
        "inputs": {"km_viaje": [10,20,30,50,80,100,150,200], "consumo_l100km": [6,7,8,10,12]},
        "url_fn": lambda p: f"{int(p['km_viaje'])}km-{_fmt(p['consumo_l100km'])}l",
        "title_template": {
            "en": "Fuel Cost for {k}km Trip at {c}L/100km",
            "es": "Coste Combustible Viaje {k}km, {c}L/100km",
            "fr": "Coût Carburant {k}km à {c}L/100km",
            "pt": "Custo Combustível {k}km a {c}L/100km",
            "de": "Kraftstoffkosten {k}km bei {c}L/100km",
            "it": "Costo Carburante {k}km a {c}L/100km",
        },
        "title_fn": lambda p, tpl: tpl.format(k=int(p["km_viaje"]), c=p["consumo_l100km"]),
        "desc_template": {"en": "Calculate fuel cost for a {k}km trip with a vehicle consuming {c}L/100km."},
        "desc_fn": lambda p, tpl: tpl.format(k=int(p["km_viaje"]), c=p["consumo_l100km"]),
        "wastage_default": 0,
    },

    # ── 085 Scaffolding ── length × height × weeks
    "085": {
        "inputs": {"longitud_m": [4,6,8,10,12,15,20], "altura_m": [3,4,6,8,10,12], "semanas": [1,2,3,4,6,8]},
        "url_fn": lambda p: f"{_fmt(p['longitud_m'])}x{_fmt(p['altura_m'])}m-{int(p['semanas'])}w",
        "title_template": {
            "en": "Scaffolding {l}×{h}m for {w} Week{wp} – Cost",
            "es": "Andamio {l}×{h}m durante {w} Semana{wp}",
            "fr": "Échafaudage {l}×{h}m pour {w} Semaine{wp}",
            "pt": "Andaime {l}×{h}m por {w} Semana{wp}",
            "de": "Gerüst {l}×{h}m für {w} Woche{wp}",
            "it": "Ponteggio {l}×{h}m per {w} Settimana{wp}",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["longitud_m"], h=p["altura_m"], w=int(p["semanas"]), wp="s" if int(p["semanas"]) > 1 else ""),
        "desc_template": {"en": "Calculate rental cost for {l}m × {h}m scaffolding for {w} week{wp}."},
        "desc_fn": lambda p, tpl: tpl.format(l=p["longitud_m"], h=p["altura_m"], w=int(p["semanas"]), wp="s" if int(p["semanas"]) > 1 else ""),
        "wastage_default": 0,
    },

    # ── 090 Labour productivity ── workers × hours × productivity
    "090": {
        "inputs": {"operarios": [1,2,3,4,5,6,8], "horas_dia": [6,7,8,10], "rendimiento_m2_h": [3,4,5,6,8,10]},
        "url_fn": lambda p: f"{int(p['operarios'])}op-{int(p['horas_dia'])}h-{_fmt(p['rendimiento_m2_h'])}m2h",
        "title_template": {
            "en": "{n} Workers, {h}h/Day at {r}m²/h – Daily Output",
            "es": "{n} Operarios, {h}h/Día a {r}m²/h – Rendimiento",
            "fr": "{n} Ouvriers, {h}h/Jour à {r}m²/h – Production",
            "pt": "{n} Operários, {h}h/Dia a {r}m²/h – Produção",
            "de": "{n} Arbeiter, {h}h/Tag bei {r}m²/h – Leistung",
            "it": "{n} Operai, {h}h/Giorno a {r}m²/h – Resa",
        },
        "title_fn": lambda p, tpl: tpl.format(n=int(p["operarios"]), h=int(p["horas_dia"]), r=p["rendimiento_m2_h"]),
        "desc_template": {"en": "Calculate daily m² output for {n} workers at {h}h/day with {r}m²/h productivity."},
        "desc_fn": lambda p, tpl: tpl.format(n=int(p["operarios"]), h=int(p["horas_dia"]), r=p["rendimiento_m2_h"]),
        "wastage_default": 0,
    },

    # ── 094 Equipment loan ── amount × rate × term
    "094": {
        "inputs": {"importe_eur": [5000,10000,15000,20000,30000,50000], "plazo_meses": [12,24,36,48,60]},
        "url_fn": lambda p: f"{int(p['importe_eur'])}eur-{int(p['plazo_meses'])}m",
        "title_template": {
            "en": "Equipment Loan €{a} over {m} Months – Monthly Payment",
            "es": "Préstamo Equipo €{a} en {m} Meses – Cuota",
            "fr": "Crédit Matériel {a}€ sur {m} Mois – Mensualité",
            "pt": "Financiamento Equipamento €{a} em {m} Meses",
            "de": "Maschinenkredit {a}€ über {m} Monate – Rate",
            "it": "Finanziamento Attrezzatura €{a} in {m} Mesi",
        },
        "title_fn": lambda p, tpl: tpl.format(a=int(p["importe_eur"]), m=int(p["plazo_meses"])),
        "desc_template": {"en": "Calculate monthly payment for a €{a} equipment loan over {m} months."},
        "desc_fn": lambda p, tpl: tpl.format(a=int(p["importe_eur"]), m=int(p["plazo_meses"])),
        "wastage_default": 0,
    },

    # ── 095 Profit margin ── cost × price
    "095": {
        "inputs": {"coste_total_eur": [1000,2000,5000,8000,10000,15000,20000], "precio_venta_eur": [1200,2500,6000,10000,12000,18000,25000]},
        "url_fn": lambda p: f"cost-{int(p['coste_total_eur'])}-price-{int(p['precio_venta_eur'])}",
        "title_template": {
            "en": "Profit Margin: Cost €{c} → Price €{p}",
            "es": "Margen Beneficio: Coste €{c} → Precio €{p}",
            "fr": "Marge Bénéficiaire: Coût {c}€ → Prix {p}€",
            "pt": "Margem de Lucro: Custo €{c} → Preço €{p}",
            "de": "Gewinnmarge: Kosten {c}€ → Preis {p}€",
            "it": "Margine Profitto: Costo €{c} → Prezzo €{p}",
        },
        "title_fn": lambda p, tpl: tpl.format(c=int(p["coste_total_eur"]), p=int(p["precio_venta_eur"])),
        "desc_template": {"en": "Calculate profit margin and markup when cost is €{c} and selling price is €{p}."},
        "desc_fn": lambda p, tpl: tpl.format(c=int(p["coste_total_eur"]), p=int(p["precio_venta_eur"])),
        "wastage_default": 0,
    },

    # ── 099 Workforce cost ── workers × days × rate
    "099": {
        "inputs": {"operarios": [1,2,3,4,5,6], "dias_obra": [5,10,15,20,30], "coste_hora_eur": [18,20,22,25,30]},
        "url_fn": lambda p: f"{int(p['operarios'])}op-{int(p['dias_obra'])}d-{int(p['coste_hora_eur'])}eurh",
        "title_template": {
            "en": "{n} Workers, {d} Days at €{r}/h – Labour Cost",
            "es": "{n} Operarios, {d} Días a €{r}/h – Coste Mano de Obra",
            "fr": "{n} Ouvriers, {d} Jours à {r}€/h – Main d'Œuvre",
            "pt": "{n} Operários, {d} Dias a €{r}/h – Custo",
            "de": "{n} Arbeiter, {d} Tage à {r}€/h – Lohnkosten",
            "it": "{n} Operai, {d} Giorni a €{r}/h – Costo",
        },
        "title_fn": lambda p, tpl: tpl.format(n=int(p["operarios"]), d=int(p["dias_obra"]), r=int(p["coste_hora_eur"])),
        "desc_template": {"en": "Calculate total labour cost for {n} workers over {d} days at €{r}/hour."},
        "desc_fn": lambda p, tpl: tpl.format(n=int(p["operarios"]), d=int(p["dias_obra"]), r=int(p["coste_hora_eur"])),
        "wastage_default": 0,
    },

    # ── 101 Swimming pool volume ── length × width × depth
    "101": {
        "inputs": {
            "largo_m": [4, 5, 6, 8, 10, 12],
            "ancho_m": [2, 3, 4, 5, 6],
            "profundidad_m": [1.2, 1.5, 1.8, 2.0],
        },
        "url_fn": lambda p: f"{_fmt(p['largo_m'])}x{_fmt(p['ancho_m'])}x{_fmt(p['profundidad_m'])}m",
        "title_template": {
            "es": "Piscina {l}×{a}m Profundidad {d}m – Volumen y Cloro",
            "en": "{l}×{a}m Pool {d}m Deep – Volume & Chlorine",
            "fr": "Piscine {l}×{a}m Profondeur {d}m – Volume et Chlore",
            "pt": "Piscina {l}×{a}m Prof. {d}m – Volume e Cloro",
            "de": "Pool {l}×{a}m Tiefe {d}m – Volumen und Chlor",
            "it": "Piscina {l}×{a}m Profondità {d}m – Volume e Cloro",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo_m"], a=p["ancho_m"], d=p["profundidad_m"]),
        "desc_template": {
            "es": "Calcula los litros, m³ y cloro necesarios para una piscina de {l}m × {a}m con profundidad de {d}m.",
            "en": "Calculate litres, m³ and chlorine needed for a {l}m × {a}m pool with {d}m depth.",
            "fr": "Calculez les litres, m³ et chlore pour une piscine de {l}m × {a}m avec {d}m de profondeur.",
            "pt": "Calcule litros, m³ e cloro para uma piscina de {l}m × {a}m com {d}m de profundidade.",
            "de": "Berechnen Sie Liter, m³ und Chlor für einen {l}m × {a}m Pool mit {d}m Tiefe.",
            "it": "Calcola litri, m³ e cloro per una piscina di {l}m × {a}m con profondità {d}m.",
        },
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo_m"], a=p["ancho_m"], d=p["profundidad_m"]),
        "result_fn": lambda p, lang: _pool_result(p["largo_m"], p["ancho_m"], p["profundidad_m"], lang),
        "wastage_default": 0,
    },

    # ── 102 Garden topsoil ── area × depth
    "102": {
        "inputs": {
            "largo_m": [1, 2, 3, 4, 5, 6, 8, 10],
            "ancho_m": [1, 2, 3, 4, 5],
            "profundidad_cm": [10, 15, 20, 25, 30],
        },
        "url_fn": lambda p: f"{_fmt(p['largo_m'])}x{_fmt(p['ancho_m'])}m-{int(p['profundidad_cm'])}cm",
        "title_template": {
            "es": "Tierra para Jardín {l}×{a}m – {d}cm Profundidad",
            "en": "Topsoil for {l}×{a}m Garden Bed – {d}cm Deep",
            "fr": "Terreau pour {l}×{a}m – {d}cm de Profondeur",
            "pt": "Terra para Jardim {l}×{a}m – {d}cm de Profundidade",
            "de": "Gartenerde für {l}×{a}m – {d}cm Tiefe",
            "it": "Terra da Giardino {l}×{a}m – {d}cm Profondità",
        },
        "title_fn": lambda p, tpl: tpl.format(l=p["largo_m"], a=p["ancho_m"], d=int(p["profundidad_cm"])),
        "desc_template": {
            "es": "Calcula los m³ y sacos de tierra vegetal para una zona de {l}m × {a}m con {d}cm de profundidad.",
            "en": "Calculate m³ and bags of topsoil for a {l}m × {a}m area with {d}cm depth.",
            "fr": "Calculez les m³ et sacs de terreau pour {l}m × {a}m avec {d}cm de profondeur.",
            "pt": "Calcule m³ e sacos de terra vegetal para {l}m × {a}m com {d}cm de profundidade.",
            "de": "Berechnen Sie m³ und Säcke Gartenerde für {l}m × {a}m mit {d}cm Tiefe.",
            "it": "Calcola m³ e sacchi di terra per {l}m × {a}m con {d}cm di profondità.",
        },
        "desc_fn": lambda p, tpl: tpl.format(l=p["largo_m"], a=p["ancho_m"], d=int(p["profundidad_cm"])),
        "result_fn": lambda p, lang: _topsoil_result(p["largo_m"], p["ancho_m"], p["profundidad_cm"], lang),
        "wastage_default": 0,
    },

    # ── 103 Fence posts ── total length × post spacing
    "103": {
        "inputs": {
            "longitud_m": [10, 15, 20, 30, 40, 50, 60, 80, 100],
            "separacion_m": [1.5, 2.0, 2.5, 3.0],
        },
        "url_fn": lambda p: f"{int(p['longitud_m'])}m-{_fmt(p['separacion_m'])}sep",
        "title_template": {
            "es": "Valla de {l}m – Postes cada {s}m",
            "en": "{l}m Fence – Posts every {s}m",
            "fr": "Clôture {l}m – Poteaux tous les {s}m",
            "pt": "Cerca de {l}m – Postes a cada {s}m",
            "de": "{l}m Zaun – Pfosten alle {s}m",
            "it": "Recinzione {l}m – Pali ogni {s}m",
        },
        "title_fn": lambda p, tpl: tpl.format(l=int(p["longitud_m"]), s=p["separacion_m"]),
        "desc_template": {
            "es": "Calcula cuántos postes, paneles y hormigón necesitas para una valla de {l}m con postes cada {s}m.",
            "en": "Calculate posts, panels and concrete for a {l}m fence with posts spaced every {s}m.",
            "fr": "Calculez les poteaux, panneaux et béton pour une clôture de {l}m avec poteaux tous les {s}m.",
            "pt": "Calcule postes, painéis e concreto para uma cerca de {l}m com postes a cada {s}m.",
            "de": "Berechnen Sie Pfosten, Paneele und Beton für einen {l}m Zaun mit Pfostenabstand {s}m.",
            "it": "Calcola pali, pannelli e calcestruzzo per una recinzione di {l}m con pali ogni {s}m.",
        },
        "desc_fn": lambda p, tpl: tpl.format(l=int(p["longitud_m"]), s=p["separacion_m"]),
        "result_fn": lambda p, lang: _fence_result(p["longitud_m"], p["separacion_m"], lang),
        "wastage_default": 0,
    },
}

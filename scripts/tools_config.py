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
}

GROUP_ICONS = {
    "dims": "📐", "material": "🧱", "product": "🪣",
    "count": "🔢", "financial": "💶", "time": "🕐", "other": "⚙️",
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
]

# Quick lookup
TOOL_BY_ID = {t["id"]: t for t in TOOLS}

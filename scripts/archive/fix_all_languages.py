#!/usr/bin/env python3
"""
fix_all_languages.py - Batch-fix all 461 calculator JSON locale files.

Fixes applied:
  1. Missing seo_description: auto-generated from description field (max 160 chars)
  2. SEO length truncation: seo_title to 60 chars, seo_description to 160 chars
  3. Italian narrative markers: flag Spanish words in IT steps/mistakes/result_context/formula_display
  4. Input/output label translations: replace labels that match Spanish exactly
  5. Unit word translations: replace Spanish unit words in labels

Usage: py fix_all_languages.py
"""

import json
import os
import re
import sys
from pathlib import Path
from collections import OrderedDict

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CALC_DIR = Path(r"C:\Microsaas\obra\src\calculators")
LANG_CODES = ["es", "en", "fr", "pt", "de", "it"]
SEO_TITLE_MAX = 60
SEO_DESC_MAX = 160
TRUNC_SUFFIX = "..."

# Spanish words that signal untranslated Italian narrative content
# Word-boundary regex; case-insensitive
IT_SPANISH_TRIGGERS = re.compile(
    r"\b(para|como|calcular|introduce|el|la|los|las)\b",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Word-level label translation maps (Spanish word → target language)
# Used when a non-ES input/output label is character-for-character identical
# to the Spanish label.
# ---------------------------------------------------------------------------

LABEL_MAPS = {
    "de": {
        "Largo": "Länge", "Ancho": "Breite", "Alto": "Höhe", "Altura": "Höhe",
        "Longitud": "Länge", "Anchura": "Breite", "Profundidad": "Tiefe",
        "Diametro": "Durchmesser", "Radio": "Radius", "Perimetro": "Umfang",
        "Superficie": "Fläche", "Area": "Fläche", "Volumen": "Volumen",
        "Peso": "Gewicht", "Masa": "Masse", "Densidad": "Dichte",
        "Temperatura": "Temperatur", "Presion": "Druck", "Fuerza": "Kraft",
        "Potencia": "Leistung", "Energia": "Energie", "Velocidad": "Geschwindigkeit",
        "Aceleracion": "Beschleunigung", "Tiempo": "Zeit", "Distancia": "Entfernung",
        "Cantidad": "Menge", "Numero": "Anzahl", "Unidades": "Einheiten",
        "Porcentaje": "Prozentsatz", "Tasa": "Rate", "Interes": "Zinsen",
        "Coste": "Kosten", "Precio": "Preis", "Valor": "Wert", "Monto": "Betrag",
        "Saldo": "Saldo", "Rendimiento": "Rendite", "Margen": "Marge",
        "Beneficio": "Gewinn", "Ingreso": "Einnahmen", "Gasto": "Ausgaben",
        "Descuento": "Rabatt", "Impuesto": "Steuer", "Consumo": "Verbrauch",
        "Caudal": "Durchfluss", "Voltaje": "Spannung", "Corriente": "Strom",
        "Resistencia": "Widerstand", "Frecuencia": "Frequenz",
        "Capacidad": "Kapazität", "Inductancia": "Induktivität",
        "Impedancia": "Impedanz", "Horas": "Stunden", "Minutos": "Minuten",
        "Segundos": "Sekunden", "Dias": "Tage", "Semanas": "Wochen",
        "Meses": "Monate", "Anos": "Jahre", "Litros": "Liter",
        "Metros": "Meter", "Kilos": "Kilogramm", "Gramos": "Gramm",
    },
    "it": {
        "Largo": "Lunghezza", "Ancho": "Larghezza", "Alto": "Altezza",
        "Altura": "Altezza", "Longitud": "Lunghezza",
        "Profundidad": "Profondità", "Diametro": "Diametro", "Radio": "Raggio",
        "Perimetro": "Perimetro", "Volumen": "Volume", "Peso": "Peso",
        "Masa": "Massa", "Densidad": "Densità", "Temperatura": "Temperatura",
        "Presion": "Pressione", "Fuerza": "Forza", "Potencia": "Potenza",
        "Energia": "Energia", "Velocidad": "Velocità",
        "Aceleracion": "Accelerazione", "Tiempo": "Tempo",
        "Distancia": "Distanza", "Cantidad": "Quantità", "Numero": "Numero",
        "Unidades": "Unità", "Porcentaje": "Percentuale", "Tasa": "Tasso",
        "Interes": "Interesse", "Coste": "Costo", "Precio": "Prezzo",
        "Valor": "Valore", "Monto": "Importo", "Saldo": "Saldo",
        "Rendimiento": "Rendimento", "Margen": "Margine",
        "Beneficio": "Profitto", "Ingreso": "Entrate", "Gasto": "Spesa",
        "Descuento": "Sconto", "Impuesto": "Imposta", "Consumo": "Consumo",
        "Caudal": "Portata", "Voltaje": "Tensione", "Corriente": "Corrente",
        "Resistencia": "Resistenza", "Frecuencia": "Frequenza",
        "Capacidad": "Capacità", "Inductancia": "Induttanza",
        "Impedancia": "Impedenza", "Horas": "Ore", "Minutos": "Minuti",
        "Segundos": "Secondi", "Dias": "Giorni", "Semanas": "Settimane",
        "Meses": "Mesi", "Anos": "Anni", "Litros": "Litri",
        "Metros": "Metri", "Kilos": "Chilogrammi", "Gramos": "Grammi",
    },
    "fr": {
        "Largo": "Longueur", "Ancho": "Largeur", "Alto": "Hauteur",
        "Altura": "Hauteur", "Longitud": "Longueur",
        "Profundidad": "Profondeur", "Diametro": "Diamètre", "Radio": "Rayon",
        "Volumen": "Volume", "Peso": "Poids", "Masa": "Masse",
        "Densidad": "Densité", "Temperatura": "Température",
        "Presion": "Pression", "Fuerza": "Force", "Potencia": "Puissance",
        "Energia": "Énergie", "Velocidad": "Vitesse",
        "Aceleracion": "Accélération", "Tiempo": "Temps",
        "Distancia": "Distance", "Cantidad": "Quantité", "Numero": "Nombre",
        "Unidades": "Unités", "Porcentaje": "Pourcentage", "Tasa": "Taux",
        "Coste": "Coût", "Precio": "Prix", "Valor": "Valeur",
        "Consumo": "Consommation", "Horas": "Heures", "Minutos": "Minutes",
        "Dias": "Jours", "Meses": "Mois", "Litros": "Litres",
    },
    "pt": {
        "Largo": "Comprimento", "Ancho": "Largura", "Alto": "Altura",
        "Altura": "Altura", "Longitud": "Comprimento",
        "Profundidad": "Profundidade", "Diametro": "Diâmetro", "Radio": "Raio",
        "Volumen": "Volume", "Peso": "Peso", "Masa": "Massa",
        "Densidad": "Densidade", "Temperatura": "Temperatura",
        "Presion": "Pressão", "Fuerza": "Força", "Potencia": "Potência",
        "Energia": "Energia", "Velocidad": "Velocidade",
        "Aceleracion": "Aceleração", "Tiempo": "Tempo",
        "Distancia": "Distância", "Cantidad": "Quantidade",
        "Numero": "Número", "Porcentaje": "Percentagem", "Tasa": "Taxa",
        "Coste": "Custo", "Precio": "Preço", "Valor": "Valor",
        "Consumo": "Consumo", "Horas": "Horas", "Dias": "Dias",
        "Meses": "Meses", "Litros": "Litros",
    },
    "en": {
        "Largo": "Length", "Ancho": "Width", "Alto": "Height",
        "Altura": "Height", "Longitud": "Length", "Profundidad": "Depth",
        "Diametro": "Diameter", "Radio": "Radius", "Volumen": "Volume",
        "Peso": "Weight", "Masa": "Mass", "Densidad": "Density",
        "Temperatura": "Temperature", "Presion": "Pressure", "Fuerza": "Force",
        "Potencia": "Power", "Energia": "Energy", "Velocidad": "Speed",
        "Aceleracion": "Acceleration", "Tiempo": "Time",
        "Distancia": "Distance", "Cantidad": "Quantity", "Numero": "Number",
        "Porcentaje": "Percentage", "Tasa": "Rate", "Coste": "Cost",
        "Precio": "Price", "Valor": "Value", "Consumo": "Consumption",
        "Horas": "Hours", "Dias": "Days", "Meses": "Months",
        "Litros": "Liters", "Metros": "Meters", "Kilos": "Kilograms",
    },
}

# ---------------------------------------------------------------------------
# Unit-word translation maps (Spanish unit words → target language)
# Applied to ALL non-ES input/output labels regardless of whether they match ES.
# ---------------------------------------------------------------------------

UNIT_MAPS = {
    "de": {
        "metros": "Meter", "centimetros": "Zentimeter", "milimetros": "Millimeter",
        "kilometros": "Kilometer", "kilogramos": "Kilogramm", "gramos": "Gramm",
        "miligramos": "Milligramm", "litros": "Liter", "mililitros": "Milliliter",
        "horas": "Stunden", "minutos": "Minuten", "segundos": "Sekunden",
        "dias": "Tage", "semanas": "Wochen", "meses": "Monate", "anos": "Jahre",
        "grados": "Grad", "watts": "Watt", "voltios": "Volt",
        "amperios": "Ampere", "hercios": "Hertz", "pascales": "Pascal",
        "newtons": "Newton", "julios": "Joule", "calorias": "Kalorien",
        "euros": "Euro", "dolares": "Dollar",
        "pies": "Fuß", "pulgadas": "Zoll", "yardas": "Yards", "millas": "Meilen",
        "libras": "Pfund", "onzas": "Unzen", "toneladas": "Tonnen",
    },
    "it": {
        "metros": "metri", "centimetros": "centimetri", "milimetros": "millimetri",
        "kilometros": "chilometri", "kilogramos": "chilogrammi", "gramos": "grammi",
        "miligramos": "milligrammi", "litros": "litri", "mililitros": "millilitri",
        "horas": "ore", "minutos": "minuti", "segundos": "secondi",
        "dias": "giorni", "semanas": "settimane", "meses": "mesi", "anos": "anni",
        "grados": "gradi", "watts": "watt", "voltios": "volt",
        "amperios": "ampere", "hercios": "hertz", "pascales": "pascal",
        "newtons": "newton", "julios": "joule", "calorias": "calorie",
        "euros": "euro", "dolares": "dollari",
        "pies": "piedi", "pulgadas": "pollici", "yardas": "iarde",
        "millas": "miglia", "libras": "libbre", "onzas": "once",
        "toneladas": "tonnellate",
    },
    "fr": {
        "metros": "mètres", "centimetros": "centimètres",
        "milimetros": "millimètres", "kilometros": "kilomètres",
        "kilogramos": "kilogrammes", "gramos": "grammes",
        "miligramos": "milligrammes", "litros": "litres",
        "mililitros": "millilitres", "horas": "heures", "minutos": "minutes",
        "segundos": "secondes", "dias": "jours", "semanas": "semaines",
        "meses": "mois", "anos": "ans", "grados": "degrés", "watts": "watts",
        "voltios": "volts", "amperios": "ampères", "hercios": "hertz",
        "pascales": "pascals", "newtons": "newtons", "julios": "joules",
        "calorias": "calories", "euros": "euros", "dolares": "dollars",
        "pies": "pieds", "pulgadas": "pouces", "yardas": "yards",
        "millas": "miles", "libras": "livres", "onzas": "onces",
        "toneladas": "tonnes",
    },
    "pt": {
        "metros": "metros", "centimetros": "centímetros",
        "milimetros": "milímetros", "kilometros": "quilômetros",
        "kilogramos": "quilogramas", "gramos": "gramas",
        "miligramos": "miligramas", "litros": "litros",
        "mililitros": "mililitros", "horas": "horas", "minutos": "minutos",
        "segundos": "segundos", "dias": "dias", "semanas": "semanas",
        "meses": "meses", "anos": "anos", "grados": "graus", "watts": "watts",
        "voltios": "volts", "amperios": "amperes", "hercios": "hertz",
        "pascales": "pascals", "newtons": "newtons", "julios": "joules",
        "calorias": "calorias", "euros": "euros", "dolares": "dólares",
        "pies": "pés", "pulgadas": "polegadas", "yardas": "jardas",
        "millas": "milhas", "libras": "libras", "onzas": "onças",
        "toneladas": "toneladas",
    },
    "en": {
        "metros": "meters", "centimetros": "centimeters",
        "milimetros": "millimeters", "kilometros": "kilometers",
        "kilogramos": "kilograms", "gramos": "grams",
        "miligramos": "milligrams", "litros": "liters",
        "mililitros": "milliliters", "horas": "hours", "minutos": "minutes",
        "segundos": "seconds", "dias": "days", "semanas": "weeks",
        "meses": "months", "anos": "years", "grados": "degrees",
        "watts": "watts", "voltios": "volts", "amperios": "amperes",
        "hercios": "hertz", "pascales": "pascals", "newtons": "newtons",
        "julios": "joules", "calorias": "calories", "euros": "euros",
        "dolares": "dollars", "pies": "feet", "pulgadas": "inches",
        "yardas": "yards", "millas": "miles", "libras": "pounds",
        "onzas": "ounces", "toneladas": "tons",
    },
}

# ---------------------------------------------------------------------------
# Build a regex for all Spanish unit words (for efficient scanning)
# ---------------------------------------------------------------------------
_ALL_ES_UNIT_WORDS = sorted(
    set().union(*[UNIT_MAPS[lc].keys() for lc in LANG_CODES if lc != "es"]),
    key=len,
    reverse=True,
)
_UNIT_WORD_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(w) for w in _ALL_ES_UNIT_WORDS) + r")\b",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def truncate(text, max_len):
    """Truncate *text* to *max_len* chars; append TRUNC_SUFFIX if cut."""
    if len(text) <= max_len:
        return text
    return text[: max_len - len(TRUNC_SUFFIX)] + TRUNC_SUFFIX


def fix_seo_and_length(lang_entry):
    """
    Fix missing/empty seo_description and enforce SEO length limits.
    Returns (seo_desc_fixed, seo_title_truncated, seo_desc_truncated).
    """
    fixed_desc = False
    trunc_title = False
    trunc_desc = False

    description = lang_entry.get("description", "")
    if not isinstance(description, str):
        description = ""

    # 1) Generate missing seo_description from description field
    sd = lang_entry.get("seo_description")
    if not sd:
        lang_entry["seo_description"] = truncate(description, SEO_DESC_MAX)
        fixed_desc = True

    # 2) Truncate seo_title
    st = lang_entry.get("seo_title", "")
    if isinstance(st, str) and len(st) > SEO_TITLE_MAX:
        lang_entry["seo_title"] = truncate(st, SEO_TITLE_MAX)
        trunc_title = True

    # 3) Truncate seo_description (may have just been generated)
    sd = lang_entry.get("seo_description", "")
    if isinstance(sd, str) and len(sd) > SEO_DESC_MAX:
        lang_entry["seo_description"] = truncate(sd, SEO_DESC_MAX)
        trunc_desc = True

    return fixed_desc, trunc_title, trunc_desc


def _text_contains_spanish(text):
    """Return True if *text* contains any Spanish trigger word."""
    if not text:
        return False
    return bool(IT_SPANISH_TRIGGERS.search(str(text)))


def fix_italian_narrative(it_entry):
    """
    Prepend '[IT-NEEDS-FIX]' to Italian narrative fields that contain
    obvious Spanish words (steps, mistakes, result_context, formula_display).

    Returns number of items/fields marked.
    """
    marked = 0
    narrative_fields = ["steps", "mistakes", "result_context", "formula_display"]

    for field in narrative_fields:
        val = it_entry.get(field)
        if val is None:
            continue

        if isinstance(val, list):
            # steps / mistakes can be list of strings or list of dicts
            for idx, item in enumerate(val):
                if isinstance(item, dict):
                    desc = item.get("description", "")
                    if _text_contains_spanish(desc):
                        item["description"] = f"[IT-NEEDS-FIX] {desc}"
                        marked += 1
                elif isinstance(item, str):
                    if _text_contains_spanish(item):
                        val[idx] = f"[IT-NEEDS-FIX] {item}"
                        marked += 1
        elif isinstance(val, str):
            if _text_contains_spanish(val):
                it_entry[field] = f"[IT-NEEDS-FIX] {val}"
                marked += 1

    return marked


def _lookup_word(word, label_map, unit_map):
    """Try to translate a single word; preserve original case pattern."""
    # Exact match
    if word in label_map:
        return label_map[word]
    if word in unit_map:
        return unit_map[word]
    # Case-insensitive fallback
    word_lower = word.lower()
    for m in (label_map, unit_map):
        for k, v in m.items():
            if k.lower() == word_lower:
                # Preserve case: if original was ALL CAPS, uppercase result
                if word.isupper():
                    return v.upper()
                # If original was Title Case, title-case result
                if word[0].isupper() and word[1:].islower() if len(word) > 1 else word[0].isupper():
                    return v[0].upper() + v[1:] if len(v) > 1 else v.upper()
                return v
    return None


def _translate_spanish_words_in_label(label, label_map, unit_map):
    """
    Translate Spanish words inside a label using the provided maps.
    Handles parenthesised unit words like '(metros)' separately.
    """
    # Split on spaces but preserve parenthesised groups
    # Strategy: work on the full label, replace known Spanish words
    result = label

    # First, handle parenthesised words: replace "(spanish_word)" with "(translated)"
    def _replace_paren(match):
        inner = match.group(1)
        # Try label map first, then unit map
        replacement = _lookup_word(inner, label_map, unit_map)
        if replacement is not None:
            return f"({replacement})"
        return match.group(0)

    result = re.sub(r"\((\w+)\)", _replace_paren, result)

    # Then, handle standalone words (not inside parentheses)
    def _replace_standalone(match):
        word = match.group(0)
        # Skip if inside parentheses
        start = match.start()
        # Check if this word is inside parentheses by looking at context
        # Simple heuristic: if preceded by '(' with no ')' in between, it's inside parens
        before = result[:start]
        if before.rfind("(") > before.rfind(")"):
            return word  # inside parentheses, already handled
        replacement = _lookup_word(word, label_map, unit_map)
        if replacement is not None:
            return replacement
        return word

    # Replace standalone words
    result = re.sub(r"\b(\w+)\b", _replace_standalone, result)

    return result


def fix_label_translations(lang_code, lang_entry, es_entry):
    """
    Step 4: Replace input/output labels in *lang_entry* that are identical
    to the Spanish labels using the word-level translation maps.

    Returns (inputs_fixed, outputs_fixed).
    """
    if lang_code == "es":
        return 0, 0

    label_map = LABEL_MAPS.get(lang_code, {})
    unit_map = UNIT_MAPS.get(lang_code, {})

    es_inputs = es_entry.get("inputs", {})
    es_outputs = es_entry.get("outputs", {})

    inputs_fixed = 0
    outputs_fixed = 0

    for section_key, es_section, counter_key in [
        ("inputs", es_inputs, "inputs_fixed"),
        ("outputs", es_outputs, "outputs_fixed"),
    ]:
        lang_section = lang_entry.get(section_key, {})
        for key, es_label in es_section.items():
            if key not in lang_section:
                continue
            lang_label = lang_section[key]
            if not isinstance(lang_label, str) or not isinstance(es_label, str):
                continue
            # Exact match with Spanish → needs translation
            if lang_label == es_label:
                new_label = _translate_spanish_words_in_label(
                    lang_label, label_map, unit_map
                )
                if new_label != lang_label:
                    lang_section[key] = new_label
                    if section_key == "inputs":
                        inputs_fixed += 1
                    else:
                        outputs_fixed += 1

    return inputs_fixed, outputs_fixed


def fix_unit_words(lang_code, lang_entry):
    """
    Step 5: Replace Spanish unit words in input/output labels with the
    target-language equivalent.  Applied to ALL non-ES languages regardless
    of whether the label matches Spanish.

    Returns number of unit-word replacements made.
    """
    if lang_code == "es":
        return 0

    unit_map = UNIT_MAPS.get(lang_code, {})
    if not unit_map:
        return 0

    unit_count = 0

    for section_key in ("inputs", "outputs"):
        section = lang_entry.get(section_key, {})
        for key, label in list(section.items()):
            if not isinstance(label, str):
                continue

            # Check how many Spanish unit words appear in this label
            matches = _UNIT_WORD_PATTERN.findall(label)
            if not matches:
                continue

            new_label = label
            for match_word in matches:
                word_lower = match_word.lower()
                for uk, uv in unit_map.items():
                    if uk.lower() == word_lower:
                        # Case-preserving replacement
                        if match_word.isupper():
                            replacement = uv.upper()
                        elif (
                            match_word[0].isupper()
                            and (len(match_word) == 1 or match_word[1:].islower())
                        ):
                            replacement = uv[0].upper() + uv[1:]
                        else:
                            replacement = uv
                        # Replace only the specific occurrence (word boundary)
                        new_label = re.sub(
                            r"\b" + re.escape(match_word) + r"\b",
                            replacement,
                            new_label,
                            count=1,
                        )
                        unit_count += 1
                        break

            if new_label != label:
                section[key] = new_label

    return unit_count


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def process_file(filepath):
    """
    Process a single calculator JSON file.
    Returns a stats dict.
    """
    with open(filepath, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    i18n = data.get("i18n", {})
    es_entry = i18n.get("es", {})
    stats = {
        "file": os.path.basename(filepath),
        "seo_desc_fixed": 0,
        "seo_title_truncated": 0,
        "seo_desc_truncated": 0,
        "it_markers": 0,
        "input_labels_fixed": 0,
        "output_labels_fixed": 0,
        "unit_words_fixed": 0,
    }

    for lc in LANG_CODES:
        lang_entry = i18n.get(lc)
        if not lang_entry:
            continue

        # Steps 1 & 2: SEO fixes
        fixed_desc, trunc_title, trunc_desc = fix_seo_and_length(lang_entry)
        stats["seo_desc_fixed"] += 1 if fixed_desc else 0
        stats["seo_title_truncated"] += 1 if trunc_title else 0
        stats["seo_desc_truncated"] += 1 if trunc_desc else 0

        # Step 3: Italian narrative markers
        if lc == "it":
            stats["it_markers"] += fix_italian_narrative(lang_entry)

        # Step 4: Label translations (exact match with Spanish)
        in_fixed, out_fixed = fix_label_translations(lc, lang_entry, es_entry)
        stats["input_labels_fixed"] += in_fixed
        stats["output_labels_fixed"] += out_fixed

        # Step 5: Unit word translations
        stats["unit_words_fixed"] += fix_unit_words(lc, lang_entry)

    # Write back
    with open(filepath, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)

    return stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    files = sorted(CALC_DIR.glob("*.json"))
    total_files = len(files)
    print(f"Processing {total_files} calculator JSON files...\n")

    totals = {
        "seo_desc_fixed": 0,
        "seo_title_truncated": 0,
        "seo_desc_truncated": 0,
        "it_markers": 0,
        "input_labels_fixed": 0,
        "output_labels_fixed": 0,
        "unit_words_fixed": 0,
    }
    files_with_changes = 0

    for i, filepath in enumerate(files, 1):
        stats = process_file(filepath)
        changed = any(
            stats[k] > 0
            for k in [
                "seo_desc_fixed",
                "seo_title_truncated",
                "seo_desc_truncated",
                "it_markers",
                "input_labels_fixed",
                "output_labels_fixed",
                "unit_words_fixed",
            ]
        )
        if changed:
            files_with_changes += 1
        for k in totals:
            totals[k] += stats[k]

        if i % 50 == 0 or i == total_files:
            print(f"  [{i:>3}/{total_files}] files processed...", end="\r")

    print(f"\n{'='*60}")
    print(f"  FIX SUMMARY")
    print(f"{'='*60}")
    print(f"  Total files scanned:           {total_files:>5}")
    print(f"  Files modified:                {files_with_changes:>5}")
    print(f"{'='*60}")
    print(f"  1. seo_description generated:  {totals['seo_desc_fixed']:>5}")
    print(f"  2. seo_title truncated:        {totals['seo_title_truncated']:>5}")
    print(f"     seo_description truncated:  {totals['seo_desc_truncated']:>5}")
    print(f"  3. Italian [IT-NEEDS-FIX]:     {totals['it_markers']:>5}")
    print(f"  4. Input labels translated:    {totals['input_labels_fixed']:>5}")
    print(f"     Output labels translated:   {totals['output_labels_fixed']:>5}")
    print(f"  5. Unit words translated:      {totals['unit_words_fixed']:>5}")
    print(f"{'='*60}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

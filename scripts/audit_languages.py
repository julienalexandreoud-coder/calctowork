#!/usr/bin/env python3
"""Audit all 6 languages across 461 calculator files for quality issues."""

import json, os, glob, re
from collections import Counter, defaultdict

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

KNOWN_SPANISH_INPUTS = {
    "largo", "ancho", "alto", "altura", "espesor", "espesor_base", "espesor_corona",
    "longitud", "anchura", "profundidad", "diametro", "diametro_interior", "diametro_exterior",
    "radio", "perimetro", "superficie", "area", "volumen", "volumen_total",
    "cantidad", "unidades", "numero", "distancia", "angulo", "temperatura",
    "tiempo", "horas", "minutos", "segundos", "dias", "semanas", "meses", "anos",
    "masa", "peso", "densidad", "presion", "fuerza", "potencia", "energia",
    "caudal", "velocidad", "aceleracion", "frecuencia", "voltaje", "corriente",
    "resistencia", "capacidad", "inductancia", "impedancia", "consumo",
    "coste", "precio", "precio_unitario", "porcentaje", "tasa", "interes",
    "margen", "beneficio", "ingresos", "gastos", "presupuesto",
    "rendimiento", "altura_inicial", "altura_final", "gravedad",
    "tiempo_carga", "tiempo_descarga", "factor_seguridad", "factor_conversion",
    "longitud_onda", "indice_refraccion", "angulo_incidencia", "angulo_refraccion",
}

KNOWN_ENGLISH_INPUTS = {
    "length", "width", "height", "depth", "thickness", "radius", "diameter",
    "weight", "mass", "volume", "area", "perimeter", "angle", "temperature",
    "time", "hours", "minutes", "seconds", "days", "weeks", "months", "years",
    "speed", "velocity", "acceleration", "frequency", "voltage", "current",
    "resistance", "power", "energy", "force", "pressure", "density", "flow",
    "cost", "price", "percentage", "rate", "interest", "margin", "profit",
    "revenue", "expense", "budget", "efficiency", "distance", "amount",
    "quantity", "units", "number", "count", "consumption",
}

SPANISH_WORDS = {
    "calcular", "calcula", "calcule", "calculo", "calculadora",
    "introducir", "introduce", "introduzca", "introduciendo",
    "obtener", "obtiene", "obtenga", "obteniendo",
    "resultado", "resultados", "resultante",
    "valor", "valores", "unidad", "unidades",
    "multiplicar", "multiplica", "multiplicando",
    "dividir", "divide", "dividiendo",
    "sumar", "suma", "restando", "restar",
    "medir", "mide", "midiendo",
    "necesario", "necesaria", "necesarios",
    "basado", "basada", "utilizando", "usando",
    "gratis", "gratuita", "gratuito",
    "herramienta", "herramientas",
    "para", "por", "con", "sin", "del", "de", "la", "el", "los", "las",
    "puede", "pueden", "debe", "deben",
    "mas", "menos", "muy", "poco", "mucho",
    "este", "esta", "estos", "estas",
    "como", "cuando", "donde", "cual", "cuales",
    "que", "tiene", "tienen", "haber", "hacer", "ser", "estar",
    "cada", "todo", "todos", "toda", "todas",
    "primero", "segundo", "tercero",
    "calculo", "calcule", "calcula", "calcular",
    "utilice", "utiliza", "usar", "use",
    "ingrese", "ingresa", "ingresar",
    "seleccione", "selecciona", "seleccionar",
    "elija", "elige", "elegir",
    "presione", "presiona", "presionar",
    "haga", "hacer", "realice", "realizar",
    "verifique", "verifica", "verificar",
    "compruebe", "comprueba", "comprobar",
    "asegurese", "asegurarse",
    "considere", "considerar", "tenga", "tener",
    "recuerde", "recordar", "anote", "anotar",
    "datos", "datos", "entrada", "salida",
    "paso", "pasos", "paso a paso",
    "error", "errores", "advertencia",
    "formula", "formulas", "ecuacion", "ecuaciones",
}

GERMAN_WORDS = {
    "berechnen", "berechnet", "berechnung", "rechner",
    "eingeben", "eingabe", "geben sie",
    "ergebnis", "ergebnisse",
    "wert", "werte", "einheit", "einheiten",
    "multiplizieren", "dividieren", "addieren", "subtrahieren",
    "messen", "messung",
    "notwendig", "erforderlich", "benotigt",
    "kostenlos", "kostenlose", "kostenloses",
    "werkzeug", "werkzeuge",
    "fur", "mit", "ohne", "von", "zum", "zur",
    "konnen", "mussen", "sollten",
    "mehr", "weniger", "sehr",
    "dieser", "diese", "dieses",
    "wie", "wann", "wo", "welche", "welcher",
    "jeder", "jede", "alles", "alle",
    "erste", "zweite", "dritte",
    "verwenden", "benutzen", "nutzen",
    "auswahlen", "wahlen",
    "drucken", "drucken sie",
    "machen", "tun", "ausfuhren",
    "uberprufen", "prufen",
    "sicherstellen", "beachten", "berucksichtigen",
    "denken", "erinnern", "notieren",
    "daten", "eingabe", "ausgabe",
    "schritt", "schritte",
    "lange", "breite", "hohe", "dicke", "tiefe",
    "gewicht", "masse", "volumen", "flache",
    "geschwindigkeit", "druck", "kraft", 
    "strom", "spannung", "widerstand",
    "leistung", "energie",
}

def load_calc(fp):
    with open(fp, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def check_spanish_in_de(calc):
    """Check if German input labels are in Spanish."""
    issues = []
    de = calc.get("i18n", {}).get("de", {})
    de_inputs = de.get("inputs", {})
    es_inputs = calc.get("i18n", {}).get("es", {}).get("inputs", {})
    
    for inp_id, label in de_inputs.items():
        if not isinstance(label, str):
            continue
        # Check if German label matches Spanish label exactly
        es_label = es_inputs.get(inp_id, "")
        if label == es_label and label:
            # Only flag if the label looks like a real word (not just a number)
            if any(c.isalpha() for c in label):
                issues.append(f"DE input '{inp_id}'='{label}' == ES label")
    return issues

def check_spanish_words_in_de(calc):
    """Check for Spanish words in German text fields."""
    issues = []
    de = calc.get("i18n", {}).get("de", {})
    for field in ["name", "description", "seo_title", "seo_description",
                   "example_label", "result_context", "formula_display"]:
        text = de.get(field, "")
        if not isinstance(text, str) or not text:
            continue
        words = set(re.findall(r'\b[a-záéíóúñü]+\b', text.lower()))
        spanish_hits = words & SPANISH_WORDS
        german_hits = words & GERMAN_WORDS
        if len(spanish_hits) > 2 and len(german_hits) < len(spanish_hits):
            issues.append(f"DE {field} has {len(spanish_hits)} ES words vs {len(german_hits)} DE words: '{text[:80]}...'")
    return issues

def check_italian_pseudo(calc):
    """Check for pseudo-Italian (Spanish/English mixed in)."""
    issues = []
    it = calc.get("i18n", {}).get("it", {})
    for field in ["name", "description", "example_label", "result_context", "steps", "mistakes"]:
        text = it.get(field, "")
        if isinstance(text, list):
            text = " ".join(str(t) for t in text)
        if not isinstance(text, str) or not text:
            continue
        text_lower = text.lower()
        # Spanish-specific patterns that shouldn't be in Italian
        es_patterns = [
            r'\bel\s', r'\bla\s', r'\blos\s', r'\blas\s',  # Spanish articles
            r'\bcalcular\b', r'\bcalcula\b', r'\bintroduce\b',
            r'\bresultado\b', r'\bunidad\b',
            r'\bpara\b', r'\bcomo\b', r'\bcuando\b',
            r'ñ',  # ñ is Spanish, not Italian
            r'á', r'é', r'í', r'ó', r'ú',  # accented vowels not common in Italian
        ]
        hits = []
        for pat in es_patterns:
            if re.search(pat, text_lower):
                hits.append(pat)
        if len(hits) >= 3:
            issues.append(f"IT {field} has {len(hits)} ES patterns: '{str(text)[:100]}...'")
    
    # Check Italian input labels match Spanish
    it_inputs = it.get("inputs", {})
    es_inputs = calc.get("i18n", {}).get("es", {}).get("inputs", {})
    for inp_id, label in it_inputs.items():
        if not isinstance(label, str):
            continue
        es_label = es_inputs.get(inp_id, "")
        if label == es_label and label and any(c.isalpha() for c in label):
            issues.append(f"IT input '{inp_id}'='{label}' == ES label")
    
    return issues

def check_missing_fields(calc):
    """Check for missing critical fields in any language."""
    issues = []
    required = ["name", "description", "seo_title", "seo_description", "inputs", "outputs"]
    for lang in LANGS:
        entry = calc.get("i18n", {}).get(lang, {})
        if not entry:
            issues.append(f"{lang}: entire section missing")
            continue
        for field in required:
            if not entry.get(field):
                issues.append(f"{lang}: missing '{field}'")
    return issues

def check_seo_lengths(calc):
    """Check SEO title and description lengths."""
    issues = []
    for lang in LANGS:
        entry = calc.get("i18n", {}).get(lang, {})
        title = entry.get("seo_title", "")
        desc = entry.get("seo_description", "")
        if isinstance(title, str) and len(title) > 60:
            issues.append(f"{lang}: seo_title {len(title)} chars (max 60)")
        if isinstance(desc, str) and len(desc) > 160:
            issues.append(f"{lang}: seo_description {len(desc)} chars (max 160)")
    return issues

def check_duplicates(files):
    """Check for duplicate/overlapping calculator slugs."""
    slugs = defaultdict(list)
    for fp in files:
        try:
            calc = load_calc(fp)
            slug = calc.get("slug", "")
            slugs[slug].append(os.path.basename(fp))
        except:
            pass
    
    dups = {k: v for k, v in slugs.items() if len(v) > 1}
    return dups


def main():
    files = sorted(
        f for f in glob.glob(os.path.join(CALC_DIR, "*.json"))
        if os.path.basename(f) not in ("calculators.json",)
        and "bak" not in f and "monolithic" not in f
    )
    print(f"Auditing {len(files)} calculator files across 6 languages\n")
    
    de_spanish_inputs = 0
    de_spanish_inputs_total = 0
    de_spanish_words = 0
    it_issues = 0
    it_input_matches = 0
    missing = 0
    seo_issues = 0
    
    # Track issue details
    de_label_files = []
    de_word_files = []
    it_bad_files = []
    missing_files = []
    
    for fp in files:
        name = os.path.basename(fp)
        try:
            calc = load_calc(fp)
        except Exception as e:
            print(f"ERROR loading {name}: {e}")
            continue
        
        # German: Spanish input labels
        de_inp_issues = check_spanish_in_de(calc)
        if de_inp_issues:
            de_spanish_inputs += 1
            de_spanish_inputs_total += len(de_inp_issues)
            if len(de_label_files) < 10:
                de_label_files.append((name, de_inp_issues[:3]))
        
        # German: Spanish words in text
        de_word_issues = check_spanish_words_in_de(calc)
        if de_word_issues:
            de_spanish_words += 1
            if len(de_word_files) < 10:
                de_word_files.append((name, de_word_issues[:2]))
        
        # Italian: pseudo-Italian
        it_bad = check_italian_pseudo(calc)
        if it_bad:
            it_issues += 1
            it_input_matches += sum(1 for i in it_bad if "input" in i)
            if len(it_bad_files) < 10:
                it_bad_files.append((name, it_bad[:3]))
        
        # Missing fields
        mf = check_missing_fields(calc)
        if mf:
            missing += 1
            if len(missing_files) < 10:
                missing_files.append((name, mf))
        
        # SEO lengths
        sl = check_seo_lengths(calc)
        seo_issues += len(sl)
    
    # Duplicates
    dups = check_duplicates(files)
    
    print("=" * 60)
    print("AUDIT RESULTS")
    print("=" * 60)
    
    print(f"\n--- GERMAN (de) ---")
    print(f"Files with Spanish input labels: {de_spanish_inputs}/{len(files)} ({de_spanish_inputs_total} total labels)")
    print(f"Files with Spanish words in text: {de_spanish_words}/{len(files)}")
    if de_label_files:
        print("  Sample DE Spanish-label files:")
        for name, issues in de_label_files[:5]:
            for iss in issues:
                print(f"    {name}: {iss}")
    if de_word_files:
        print("  Sample DE word-mix files:")
        for name, issues in de_word_files[:3]:
            for iss in issues:
                print(f"    {name}: {iss}")
    
    print(f"\n--- ITALIAN (it) ---")
    print(f"Files with pseudo-Italian/issues: {it_issues}/{len(files)}")
    print(f"  (of which {it_input_matches} are input label matches to ES)")
    if it_bad_files:
        print("  Sample IT issue files:")
        for name, issues in it_bad_files[:5]:
            for iss in issues:
                print(f"    {name}: {iss}")
    
    print(f"\n--- FRENCH (fr) ---")
    # Check French input labels matching Spanish
    fr_match = 0
    fr_match_total = 0
    for fp in files:
        try:
            calc = load_calc(fp)
            fr_in = calc.get("i18n", {}).get("fr", {}).get("inputs", {})
            es_in = calc.get("i18n", {}).get("es", {}).get("inputs", {})
            for k, v in fr_in.items():
                if isinstance(v, str) and v == es_in.get(k, "") and v and any(c.isalpha() for c in v):
                    fr_match_total += 1
            if any(isinstance(v, str) and v == es_in.get(k, "") and v and any(c.isalpha() for c in v) 
                   for k, v in fr_in.items()):
                fr_match += 1
        except: pass
    print(f"Files with ES-matching input labels: {fr_match}/{len(files)} ({fr_match_total} labels)")
    
    print(f"\n--- PORTUGUESE (pt) ---")
    pt_match = 0
    pt_match_total = 0
    for fp in files:
        try:
            calc = load_calc(fp)
            pt_in = calc.get("i18n", {}).get("pt", {}).get("inputs", {})
            es_in = calc.get("i18n", {}).get("es", {}).get("inputs", {})
            for k, v in pt_in.items():
                if isinstance(v, str) and v == es_in.get(k, "") and v and any(c.isalpha() for c in v):
                    pt_match_total += 1
            if any(isinstance(v, str) and v == es_in.get(k, "") and v and any(c.isalpha() for c in v)
                   for k, v in pt_in.items()):
                pt_match += 1
        except: pass
    print(f"Files with ES-matching input labels: {pt_match}/{len(files)} ({pt_match_total} labels)")
    
    print(f"\n--- ENGLISH (en) ---")
    en_match = 0
    en_match_total = 0
    for fp in files:
        try:
            calc = load_calc(fp)
            en_in = calc.get("i18n", {}).get("en", {}).get("inputs", {})
            es_in = calc.get("i18n", {}).get("es", {}).get("inputs", {})
            for k, v in en_in.items():
                if isinstance(v, str) and v == es_in.get(k, "") and v and any(c.isalpha() for c in v):
                    en_match_total += 1
            if any(isinstance(v, str) and v == es_in.get(k, "") and v and any(c.isalpha() for c in v)
                   for k, v in en_in.items()):
                en_match += 1
        except: pass
    print(f"Files with ES-matching input labels: {en_match}/{len(files)} ({en_match_total} labels)")
    
    print(f"\n--- ALL LANGUAGES ---")
    print(f"Files missing critical fields: {missing}/{len(files)}")
    print(f"Total SEO length warnings: {seo_issues}")
    print(f"Duplicate slugs: {len(dups)}")
    for slug, files_ in list(dups.items())[:10]:
        print(f"  '{slug}': {files_}")
    
    print(f"\n--- SUMMARY ---")
    print(f"DE needs input label translation: ~{de_spanish_inputs_total} labels in {de_spanish_inputs} files")
    print(f"DE needs text translation cleanup: {de_spanish_words} files")
    print(f"IT needs translation cleanup: {it_issues} files")
    print(f"FR ES-matching labels: {fr_match_total} in {fr_match} files")
    print(f"PT ES-matching labels: {pt_match_total} in {pt_match} files")
    print(f"EN ES-matching labels: {en_match_total} in {en_match} files")

if __name__ == "__main__":
    main()

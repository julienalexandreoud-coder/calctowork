"""
Auto-fix SEO titles and descriptions for all calculators where they are
currently generic (just the calc name repeated). Generates specific,
keyword-rich descriptions from CALC_FACTS data where available.
"""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from calc_content import CALC_FACTS

ROOT = Path(__file__).parent.parent
I18N_DIR = ROOT / "src" / "i18n"

# ── SEO title templates per language ─────────────────────────────────────────
TITLE_TPL = {
    "es": "{name} – Fórmula, Cálculo y Ejemplos | CalcToWork",
    "en": "{name} – Formula, Calculation & Examples | CalcToWork",
    "fr": "{name} – Formule et Calcul en Ligne | CalcToWork",
    "pt": "{name} – Fórmula e Cálculo Online | CalcToWork",
    "de": "{name} – Formel und Rechner Online | CalcToWork",
    "it": "{name} – Formula e Calcolo Online | CalcToWork",
}

# ── SEO desc templates per language (used when CALC_FACTS available) ─────────
DESC_TPL_FACTS = {
    "es": "Calcula {formula}. Ejemplo: {ei} = {eo}. Calculadora gratuita y precisa, sin registro.",
    "en": "Calculate {formula}. Example: {ei} = {eo}. Free and accurate calculator, no signup needed.",
    "fr": "Calculez {formula}. Exemple: {ei} = {eo}. Calculateur gratuit et précis, sans inscription.",
    "pt": "Calcule {formula}. Exemplo: {ei} = {eo}. Calculadora gratuita e precisa, sem registo.",
    "de": "Berechne {formula}. Beispiel: {ei} = {eo}. Kostenloser und genauer Rechner.",
    "it": "Calcola {formula}. Esempio: {ei} = {eo}. Calcolatore gratuito e preciso, senza registrazione.",
}

DESC_TPL_BASIC = {
    "es": "{desc} Calculadora gratuita, precisa e instantánea.",
    "en": "{desc} Free, accurate and instant calculator.",
    "fr": "{desc} Calculateur gratuit, précis et instantané.",
    "pt": "{desc} Calculadora gratuita, precisa e instantânea.",
    "de": "{desc} Kostenloser, genauer und sofortiger Rechner.",
    "it": "{desc} Calcolatore gratuito, preciso e istantaneo.",
}

# ── Name fixes (bad display names → correct ones) ─────────────────────────────
NAME_FIXES = {
    "es": {
        "Calculadora Roi": "Calculadora ROI",
        "Calculadora Cagr": "Calculadora CAGR",
        "Calculadora Imc Bmi": "Calculadora IMC / BMI",
        "Calculadora Imc Deportista": "Calculadora IMC Deportista",
        "Calculadora Area Circulo": "Calculadora de Área del Círculo",
        "Calculadora Area Rectangulo": "Calculadora de Área del Rectángulo",
        "Calculadora Area Triangulo": "Calculadora de Área del Triángulo",
        "Calculadora Volumen Esfera": "Calculadora de Volumen de la Esfera",
        "Calculadora Volumen Cilindro": "Calculadora de Volumen del Cilindro",
        "Calculadora Mcm Mcd": "Calculadora MCM y MCD",
        "Calculadora Vo2 Max": "Calculadora VO2 Máx",
        "Calculadora Vo2Max": "Calculadora VO2 Máx",
        "Calculadora Metabolismo Basal": "Calculadora de Metabolismo Basal (TMB)",
        "Calculadora Potencias": "Calculadora de Potencias y Exponentes",
        "Calculadora Raiz": "Calculadora de Raíces (√)",
        "Calculadora Logaritmo": "Calculadora de Logaritmos",
        "Calculadora Factorial": "Calculadora de Factorial (n!)",
        "Calculadora Ecuacion Segundo Grado": "Calculadora de Ecuación de Segundo Grado",
        "Calculadora Interes Simple": "Calculadora de Interés Simple",
        "Calculadora Interes Compuesto": "Calculadora de Interés Compuesto",
        "Calculadora Regla 72": "Calculadora Regla del 72",
        "Calculadora Inflacion": "Calculadora de Inflación",
        "Calculadora Ratio Deuda": "Calculadora de Ratio de Endeudamiento",
        "Calculadora Desviacion Estandar": "Calculadora de Desviación Estándar",
        "Calculadora Puntuacion Z": "Calculadora de Puntuación Z (Z-score)",
        "Calculadora Coeficiente Variacion": "Calculadora de Coeficiente de Variación",
        "Calculadora Intervalo Confianza": "Calculadora de Intervalo de Confianza",
        "Calculadora Energia Cinetica": "Calculadora de Energía Cinética",
        "Calculadora Energia Potencial": "Calculadora de Energía Potencial",
        "Calculadora Trabajo Mecanico": "Calculadora de Trabajo Mecánico",
        "Calculadora Ley Ohm": "Calculadora de la Ley de Ohm",
        "Calculadora Potencia Electrica": "Calculadora de Potencia Eléctrica",
        "Calculadora Frecuencia Cardiaca Max": "Calculadora de Frecuencia Cardíaca Máxima",
        "Calculadora Frecuencia Cardiaca Max Salud": "Calculadora de Frecuencia Cardíaca Máxima",
        "Calculadora Zonas Cardiacas": "Calculadora de Zonas Cardíacas",
        "Calculadora Pasos Calorias": "Calculadora de Pasos a Calorías",
        "Calculadora Ritmo Natacion": "Calculadora de Ritmo de Natación",
        "Calculadora Ritmo Ciclismo": "Calculadora de Ritmo de Ciclismo",
        "Calculadora Ritmo Carrera": "Calculadora de Ritmo de Carrera (Pace)",
        "Calculadora Calorias Ejercicio": "Calculadora de Calorías Quemadas",
        "Calculadora Tiempo Pista": "Calculadora de Tiempos en Pista",
    },
    "en": {
        "Calculadora Roi": "ROI Calculator",
        "Calculadora Cagr": "CAGR Calculator",
    },
}


def is_generic_desc(desc: str, name: str) -> bool:
    """Return True if the description is basically just the name repeated."""
    if not desc or len(desc.strip()) < 40:
        return True
    # Check if desc is just the name (normalized comparison)
    d = desc.strip().lower()
    n = name.strip().lower()
    if d == n or d == n + "." or d.startswith(n + " ") and len(d) < len(n) + 20:
        return True
    return False


def generate_desc(cid: str, lang: str, name: str, existing_desc: str) -> str:
    facts = CALC_FACTS.get(cid, {})
    f = facts.get(lang) or facts.get("en", {})
    if f:
        formula = f.get("f", "")
        ei = f.get("ei", "")
        eo = f.get("eo", "")
        if formula and ei and eo:
            tpl = DESC_TPL_FACTS.get(lang, DESC_TPL_FACTS["en"])
            return tpl.format(formula=formula, ei=ei, eo=eo)[:250]
    # Fall back to enriched basic description
    if existing_desc and len(existing_desc.strip()) > 40:
        tpl = DESC_TPL_BASIC.get(lang, DESC_TPL_BASIC["en"])
        return tpl.format(desc=existing_desc.strip())[:250]
    return ""


def run():
    total_fixed = 0
    for lang in ["es", "en", "fr", "pt", "de", "it"]:
        path = I18N_DIR / f"{lang}.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        calcs = data.get("calculators", {})
        fixed = 0
        name_fixes = NAME_FIXES.get(lang, {})

        for cid, c in calcs.items():
            name = c.get("name", "")
            desc = c.get("desc", c.get("description", ""))
            seo_title = c.get("seo_title", "")
            seo_desc = c.get("seo_desc", c.get("seo_description", ""))

            changed = False

            # Fix bad display names
            if name in name_fixes:
                c["name"] = name_fixes[name]
                name = c["name"]
                changed = True

            # Fix seo_title if it's just "Calculadora X Online Gratis" pattern
            if (not seo_title or
                    seo_title.lower().rstrip('.') in (name.lower(), name.lower() + " online gratis",
                                                      name.lower() + " calculator",
                                                      name.lower() + " online free") or
                    len(seo_title) < 30):
                tpl = TITLE_TPL.get(lang, TITLE_TPL["en"])
                c["seo_title"] = tpl.format(name=name)
                changed = True

            # Fix seo_desc if generic
            if is_generic_desc(seo_desc, name):
                new_desc = generate_desc(cid, lang, name, desc)
                if new_desc:
                    c["seo_desc"] = new_desc
                    # also backfill seo_description key if used
                    if "seo_description" in c:
                        c["seo_description"] = new_desc
                    changed = True

            if changed:
                fixed += 1

        # Write back using WriteAllText-equivalent (UTF-8 no BOM)
        out = json.dumps(data, ensure_ascii=False, indent=2)
        import io
        p = Path(path)
        p.write_text(out, encoding="utf-8")
        print(f"[{lang}] {fixed}/{len(calcs)} calcs updated")
        total_fixed += fixed

    print(f"\nTotal: {total_fixed} calc entries improved across all languages.")


if __name__ == "__main__":
    run()

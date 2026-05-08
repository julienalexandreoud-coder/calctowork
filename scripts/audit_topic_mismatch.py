#!/usr/bin/env python3
"""
Phase 3: Detect content-topic mismatches across all calculator HTML files.
Compares the calculator's block_slug domain keywords against the actual HTML content.
Outputs: scripts/mismatch_report.csv (flagged calculators) and mismatch_ids.txt.
Run from project root: python scripts/audit_topic_mismatch.py
"""
import csv
import json
import re
import sys
from pathlib import Path

CALC_DIR = Path("src/calculators")
LANGS = ["en", "de", "es", "fr", "it", "pt"]
OUTPUT_CSV = Path("scripts/mismatch_report.csv")
OUTPUT_IDS = Path("scripts/mismatch_ids.txt")

# Keywords expected to appear in content for each block_slug domain
DOMAIN_KEYWORDS: dict[str, list[str]] = {
    "estructuras": [
        "concrete", "cement", "reinforcement", "slab", "footing",
        "hormigon", "concreto", "cemento", "armadura", "losa",
        "beton", "zement", "bewehrung",
        "betão", "cimento", "armadura",
        "calcestruzzo", "cemento", "armatura",
        "armature", "fondation",
    ],
    "mamposteria": [
        "brick", "block", "mortar", "wall", "masonry",
        "ladrillo", "bloque", "mortero", "muro",
        "ziegel", "mauer", "mauerwerk", "moertel",
        "brique", "bloc", "mortier", "mur",
        "mattone", "muratura", "malta",
        "tijolo", "alvenaria", "argamassa", "parede",
    ],
    "cubiertas": [
        "roof", "tile", "pitch", "slope", "cubierta",
        "teja", "tejado", "cubierta",
        "dach", "dachziegel", "dachneigung",
        "toiture", "tuile", "pente",
        "tetto", "tegola", "pendenza",
        "cobertura", "telha",
    ],
    "suelos": [
        "floor", "tile", "screed", "pavement",
        "suelo", "pavimento", "baldosa",
        "boden", "fliese", "estrich",
        "sol", "carrelage", "chape",
        "pavimento", "piastrella", "massetto",
        "chao", "piso", "azulejo",
    ],
    "electricidad": [
        "voltage", "current", "power", "kw", "kwh", "ampere", "cable",
        "voltaje", "corriente", "potencia", "electricidad",
        "spannung", "strom", "leistung", "kabel",
        "tension", "courant", "puissance", "electrique",
        "tensione", "corrente", "potenza", "cavo",
        "tensao", "corrente", "potencia", "cabo",
    ],
    "fontaneria": [
        "pipe", "flow", "pressure", "plumbing", "water", "diameter",
        "tuberia", "flujo", "presion", "agua", "fontaneria",
        "rohr", "durchfluss", "druck", "wasser",
        "tuyau", "debit", "pression", "eau", "plomberie",
        "tubo", "portata", "pressione", "acqua", "idraulica",
        "tubulacao", "vazao", "pressao",
    ],
    "climatizacion": [
        "thermal", "heating", "cooling", "hvac", "temperature", "insulation",
        "termica", "calefaccion", "refrigeracion", "temperatura", "aislamiento",
        "waerme", "heizung", "kuehlung", "temperatur", "daemmung",
        "thermique", "chauffage", "climatisation", "isolation",
        "termica", "riscaldamento", "raffreddamento", "isolamento",
        "termica", "aquecimento", "refrigeracao", "isolamento",
    ],
    "carpinteria": [
        "wood", "timber", "lumber", "board", "plank",
        "madera", "tablero", "viga", "carpinteria",
        "holz", "balken", "brett", "schreinerei",
        "bois", "plancher", "poutre", "menuiserie",
        "legno", "tavola", "trave", "falegnameria",
        "madeira", "tabua", "viga", "marcenaria",
    ],
    "pintura": [
        "paint", "coat", "surface", "primer", "coverage",
        "pintura", "capa", "superficie", "imprimacion",
        "farbe", "anstrich", "flaeche", "grundierung",
        "peinture", "couche", "surface", "fond",
        "vernice", "mano", "superficie", "primer",
        "tinta", "camada", "superficie", "primario",
    ],
    "finanzas": [
        "roi", "cost", "savings", "investment", "profit", "budget", "payback",
        "coste", "ahorro", "inversion", "beneficio", "presupuesto",
        "kosten", "ersparnis", "investition", "gewinn", "budget",
        "cout", "economie", "investissement", "benefice", "budget",
        "costo", "risparmio", "investimento", "profitto", "budget",
        "custo", "poupanca", "investimento", "lucro", "orcamento",
    ],
    "matematicas": [
        "formula", "equation", "calculation", "math", "theorem",
        "ecuacion", "calculo", "matematica", "formula",
        "formel", "gleichung", "berechnung", "mathematik",
        "equation", "calcul", "mathematique", "formule",
        "equazione", "calcolo", "matematica", "formula",
        "equacao", "calculo", "matematica", "formula",
    ],
    "salud": [
        "bmi", "calorie", "weight", "health", "body mass", "heart rate",
        "imc", "calorias", "peso", "salud", "frecuencia cardiaca",
        "bmi", "kalorien", "gewicht", "gesundheit", "herzfrequenz",
        "imc", "calories", "poids", "sante", "frequence cardiaque",
        "bmi", "calorie", "peso", "salute", "frequenza cardiaca",
        "imc", "calorias", "peso", "saude", "frequencia cardiaca",
    ],
    "ciencia": [
        "physics", "chemistry", "force", "wave", "frequency", "energy",
        "fisica", "quimica", "fuerza", "onda", "frecuencia", "energia",
        "physik", "chemie", "kraft", "welle", "frequenz", "energie",
        "physique", "chimie", "force", "onde", "frequence", "energie",
        "fisica", "chimica", "forza", "onda", "frequenza", "energia",
        "fisica", "quimica", "forca", "onda", "frequencia", "energia",
    ],
    "deportes": [
        "running", "pace", "training", "race", "marathon", "fitness",
        "carrera", "ritmo", "entrenamiento", "atletismo",
        "laufen", "tempo", "training", "marathon", "fitness",
        "course", "allure", "entrainement", "marathon",
        "corsa", "passo", "allenamento", "maratona",
        "corrida", "ritmo", "treino", "maratona",
    ],
    "transporte": [
        "distance", "fuel", "vehicle", "consumption", "trip",
        "distancia", "combustible", "vehiculo", "consumo", "viaje",
        "strecke", "kraftstoff", "fahrzeug", "verbrauch", "reise",
        "distance", "carburant", "vehicule", "consommation", "trajet",
        "distanza", "carburante", "veicolo", "consumo", "viaggio",
        "distancia", "combustivel", "veiculo", "consumo", "viagem",
    ],
    "ingenieria": [
        "stress", "load", "beam", "structural", "moment",
        "esfuerzo", "carga", "viga", "estructura", "momento",
        "spannung", "last", "traeger", "struktur", "moment",
        "contrainte", "charge", "poutre", "structure", "moment",
        "tensione", "carico", "trave", "struttura", "momento",
        "tensao", "carga", "viga", "estrutura", "momento",
    ],
    "quimica": [
        "mol", "molar", "concentration", "solution", "reaction", "element",
        "mol", "molar", "concentracion", "solucion", "reaccion", "elemento",
        "mol", "molar", "konzentration", "loesung", "reaktion", "element",
        "mol", "molaire", "concentration", "solution", "reaction", "element",
        "mol", "molare", "concentrazione", "soluzione", "reazione", "elemento",
        "mol", "molar", "concentracao", "solucao", "reacao", "elemento",
    ],
    "electronica": [
        "resistor", "capacitor", "ohm", "circuit", "transistor", "diode",
        "resistencia", "condensador", "circuito", "transistor", "diodo",
        "widerstand", "kondensator", "schaltkreis", "transistor", "diode",
        "resistance", "condensateur", "circuit", "transistor", "diode",
        "resistenza", "condensatore", "circuito", "transistor", "diodo",
        "resistencia", "condensador", "circuito", "transistor", "diodo",
    ],
    "clima": [
        "temperature", "humidity", "wind", "weather", "forecast",
        "temperatura", "humedad", "viento", "meteorologia", "tiempo",
        "temperatur", "luftfeuchtigkeit", "wind", "wetter",
        "temperature", "humidite", "vent", "meteo",
        "temperatura", "umidita", "vento", "meteo",
        "temperatura", "umidade", "vento", "meteorologia",
    ],
    "fotografia": [
        "aperture", "shutter", "iso", "focal", "exposure", "camera",
        "apertura", "obturador", "iso", "focal", "exposicion", "camara",
        "blende", "verschluss", "iso", "brennweite", "kamera",
        "ouverture", "obturateur", "iso", "focale", "exposition",
        "diaframma", "otturatore", "iso", "focale", "esposizione",
        "abertura", "obturador", "iso", "focal", "exposicao",
    ],
    "utilidades": [],
    "cotidiano": [],
    "conversion": ["convert", "unit", "meter", "kilogram", "celsius", "fahrenheit", "liter"],
    "estadistica": ["average", "mean", "median", "standard deviation", "probability"],
    "pavimentos": ["floor", "tile", "paving", "pavimento", "boden", "sol", "pavimento"],
    "gestion": ["project", "budget", "schedule", "cost", "management"],
    "transporte": ["distance", "fuel", "speed", "vehicle", "consumption"],
}

# Noise patterns - content that appears in wrong-topic files (from template contamination)
WRONG_TOPIC_SIGNALS: dict[str, list[str]] = {
    "sports_in_physics": ["training for", "5k", "marathon", "vo2 max", "heart rate zone", "athlete", "running pace"],
    "construction_in_other": ["brickwork", "masonry material", "mortar estimate", "ziegel", "muro", "mortero"],
}


def get_text_from_html(html: str) -> str:
    """Strip HTML tags and return plain text for keyword matching."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&[a-z]+;", " ", text)
    return text.lower()


def score_content(content_text: str, block_slug: str) -> tuple[float, list[str]]:
    """Score how well content matches expected block_slug domain. Returns (score 0-1, found keywords)."""
    keywords = DOMAIN_KEYWORDS.get(block_slug, [])
    if not keywords:
        return 1.0, []  # Skip check for domains with no keywords
    found = [kw for kw in keywords if kw in content_text]
    score = len(found) / len(keywords)
    return score, found


def check_wrong_signals(content_text: str, block_slug: str) -> list[str]:
    """Detect clearly wrong content patterns."""
    issues = []
    # Sports content in a physics/science calculator
    if block_slug in ("ciencia", "matematicas", "ingenieria", "quimica", "electronica"):
        sports = WRONG_TOPIC_SIGNALS["sports_in_physics"]
        found = [s for s in sports if s in content_text]
        if found:
            issues.append(f"sports keywords in {block_slug}: {found}")
    # Construction content in non-construction calculator
    if block_slug not in ("estructuras", "mamposteria", "cubiertas", "suelos", "carpinteria", "pintura", "climatizacion", "fontaneria"):
        const = WRONG_TOPIC_SIGNALS["construction_in_other"]
        found = [s for s in const if s in content_text]
        if found:
            issues.append(f"construction keywords in {block_slug}: {found}")
    return issues


def audit_calculator(calc_dir: Path) -> list[dict]:
    calc_json = calc_dir / "calc.json"
    if not calc_json.exists():
        return []

    with open(calc_json, encoding="utf-8") as f:
        calc_data = json.load(f)

    calc_id = calc_data.get("id", calc_dir.name)
    block_slug = calc_data.get("block_slug", "")
    slug = calc_data.get("slug", "")

    results = []
    for lang in LANGS:
        html_path = calc_dir / f"{lang}.html"
        if not html_path.exists():
            continue

        try:
            html = html_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        content_text = get_text_from_html(html)
        score, found_kw = score_content(content_text, block_slug)
        wrong_signals = check_wrong_signals(content_text, block_slug)

        is_mismatch = score < 0.25 or bool(wrong_signals)
        if is_mismatch:
            results.append({
                "calc_id": calc_id,
                "slug": slug,
                "block_slug": block_slug,
                "lang": lang,
                "match_score": round(score, 2),
                "found_keywords": "; ".join(found_kw),
                "wrong_signals": "; ".join(wrong_signals),
                "html_path": str(html_path),
            })

    return results


def main() -> None:
    if not CALC_DIR.exists():
        print(f"ERROR: {CALC_DIR} not found. Run from project root.")
        sys.exit(1)

    all_issues: list[dict] = []
    checked = 0

    for calc_dir in sorted(CALC_DIR.iterdir()):
        if not calc_dir.is_dir():
            continue
        checked += 1
        issues = audit_calculator(calc_dir)
        all_issues.extend(issues)

    print(f"Checked {checked} calculators. Found {len(all_issues)} mismatch files.")

    if not all_issues:
        print("No mismatches detected.")
        return

    # Write CSV report
    fieldnames = ["calc_id", "slug", "block_slug", "lang", "match_score", "found_keywords", "wrong_signals", "html_path"]
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_issues)

    # Write unique calc IDs for Phase 4
    unique_ids = sorted(set(row["calc_id"] for row in all_issues))
    with open(OUTPUT_IDS, "w", encoding="utf-8") as f:
        f.write("\n".join(unique_ids))

    print(f"Report: {OUTPUT_CSV}")
    print(f"IDs for regeneration: {OUTPUT_IDS}")
    print(f"Unique calculators with issues: {len(unique_ids)}")

    # Print summary by block_slug
    from collections import Counter
    by_block = Counter(row["block_slug"] for row in all_issues)
    print("\nMismatches by domain:")
    for block, count in by_block.most_common():
        print(f"  {block}: {count} files")

    # Print worst offenders
    print("\nTop 20 worst mismatches:")
    worst = sorted(all_issues, key=lambda r: r["match_score"])[:20]
    for row in worst:
        print(f"  [{row['calc_id']}] {row['slug']} ({row['lang']}) score={row['match_score']} block={row['block_slug']}")


if __name__ == "__main__":
    main()

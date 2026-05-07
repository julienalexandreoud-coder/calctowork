"""
Patch all 6 i18n JSON files:
1. Add missing outputs for calc 400 (IMC/BMI) — peso_saludable_min, peso_saludable_max
2. Add table column header translations for calc 300 (hipoteca) and 302 (interes-compuesto)
3. Fix any BMI output labels
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
I18N = ROOT / "src" / "i18n"

TRANSLATIONS = {
    "es": {
        "400_outputs": {
            "imc": "IMC",
            "categoria": "Categoría",
            "peso_saludable_min": "Peso mínimo saludable",
            "peso_saludable_max": "Peso máximo saludable",
        },
        "300_outputs": {
            "cuota_mensual": "Cuota mensual",
            "principal_eur": "Capital prestado",
            "total_intereses": "Total intereses",
            "total_pagado": "Total pagado",
        },
        "302_outputs": {
            "capital_final": "Capital final",
            "total_intereses": "Total intereses",
            "multiplicador": "Multiplicador",
        },
        "table_headers": {
            "year": "Año", "interest": "Intereses", "principal": "Capital",
            "balance": "Saldo restante",
        },
    },
    "en": {
        "400_outputs": {
            "imc": "BMI",
            "categoria": "Category",
            "peso_saludable_min": "Minimum healthy weight",
            "peso_saludable_max": "Maximum healthy weight",
        },
        "300_outputs": {
            "cuota_mensual": "Monthly payment",
            "principal_eur": "Loan principal",
            "total_intereses": "Total interest",
            "total_pagado": "Total paid",
        },
        "302_outputs": {
            "capital_final": "Final balance",
            "total_intereses": "Total interest earned",
            "multiplicador": "Multiplier",
        },
        "table_headers": {
            "year": "Year", "interest": "Interest", "principal": "Principal",
            "balance": "Remaining balance",
        },
    },
    "fr": {
        "400_outputs": {
            "imc": "IMC",
            "categoria": "Catégorie",
            "peso_saludable_min": "Poids sain minimum",
            "peso_saludable_max": "Poids sain maximum",
        },
        "300_outputs": {
            "cuota_mensual": "Mensualité",
            "principal_eur": "Capital emprunté",
            "total_intereses": "Total intérêts",
            "total_pagado": "Total payé",
        },
        "302_outputs": {
            "capital_final": "Capital final",
            "total_intereses": "Total intérêts",
            "multiplicador": "Multiplicateur",
        },
        "table_headers": {
            "year": "Année", "interest": "Intérêts", "principal": "Capital",
            "balance": "Solde restant",
        },
    },
    "pt": {
        "400_outputs": {
            "imc": "IMC",
            "categoria": "Categoria",
            "peso_saludable_min": "Peso saudável mínimo",
            "peso_saludable_max": "Peso saudável máximo",
        },
        "300_outputs": {
            "cuota_mensual": "Prestação mensal",
            "principal_eur": "Capital emprestado",
            "total_intereses": "Total juros",
            "total_pagado": "Total pago",
        },
        "302_outputs": {
            "capital_final": "Capital final",
            "total_intereses": "Total de juros",
            "multiplicador": "Multiplicador",
        },
        "table_headers": {
            "year": "Ano", "interest": "Juros", "principal": "Capital",
            "balance": "Saldo restante",
        },
    },
    "de": {
        "400_outputs": {
            "imc": "BMI",
            "categoria": "Kategorie",
            "peso_saludable_min": "Gesundes Mindestgewicht",
            "peso_saludable_max": "Gesundes Höchstgewicht",
        },
        "300_outputs": {
            "cuota_mensual": "Monatliche Rate",
            "principal_eur": "Kreditbetrag",
            "total_intereses": "Gesamtzinsen",
            "total_pagado": "Gesamtzahlung",
        },
        "302_outputs": {
            "capital_final": "Endkapital",
            "total_intereses": "Zinsen gesamt",
            "multiplicador": "Multiplikator",
        },
        "table_headers": {
            "year": "Jahr", "interest": "Zinsen", "principal": "Tilgung",
            "balance": "Restschuld",
        },
    },
    "it": {
        "400_outputs": {
            "imc": "IMC",
            "categoria": "Categoria",
            "peso_saludable_min": "Peso minimo sano",
            "peso_saludable_max": "Peso massimo sano",
        },
        "300_outputs": {
            "cuota_mensual": "Rata mensile",
            "principal_eur": "Capitale finanziato",
            "total_intereses": "Totale interessi",
            "total_pagado": "Totale pagato",
        },
        "302_outputs": {
            "capital_final": "Capitale finale",
            "total_intereses": "Totale interessi",
            "multiplicador": "Moltiplicatore",
        },
        "table_headers": {
            "year": "Anno", "interest": "Interessi", "principal": "Capitale",
            "balance": "Saldo residuo",
        },
    },
}

for lang, T in TRANSLATIONS.items():
    path = I18N / f"{lang}.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    calcs = data.setdefault("calculators", {})

    # Patch BMI outputs
    if "400" in calcs:
        calcs["400"]["outputs"] = T["400_outputs"]

    # Patch hipoteca outputs
    if "300" in calcs:
        calcs["300"]["outputs"] = T["300_outputs"]

    # Patch interes compuesto outputs
    if "302" in calcs:
        calcs["302"]["outputs"] = T["302_outputs"]

    # Add table_headers translation at top level
    data["table_headers"] = T["table_headers"]

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[OK] {lang}.json patched")

print("Done.")

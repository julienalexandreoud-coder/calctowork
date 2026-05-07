"""Add stat label translations to i18n files."""
import json, os

I18N_DIR = "src/i18n"

translations = {
    "en": {"stat_calculators": "Calculators", "stat_categories": "Categories", "stat_languages": "Languages"},
    "es": {"stat_calculators": "Calculadoras", "stat_categories": "Categorias", "stat_languages": "Idiomas"},
    "fr": {"stat_calculators": "Calculatrices", "stat_categories": "Catégories", "stat_languages": "Langues"},
    "pt": {"stat_calculators": "Calculadoras", "stat_categories": "Categorias", "stat_languages": "Idiomas"},
    "de": {"stat_calculators": "Rechner", "stat_categories": "Kategorien", "stat_languages": "Sprachen"},
    "it": {"stat_calculators": "Calcolatrici", "stat_categories": "Categorie", "stat_languages": "Lingue"},
}

for lang, stats in translations.items():
    fp = os.path.join(I18N_DIR, f"{lang}.json")
    if not os.path.exists(fp):
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    
    changed = False
    for k, v in stats.items():
        if k not in data:
            data[k] = v
            changed = True
    
    if changed:
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f"  Added stat labels to {lang}.json")

print("Done.")

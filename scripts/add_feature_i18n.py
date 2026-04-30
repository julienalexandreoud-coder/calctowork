"""Add i18n keys for new features: PDF export, price estimation, project tally."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent / "src" / "i18n"

KEYS = {
    "en": {
        "btn_pdf": "Download PDF",
        "btn_add_project": "Add to Project",
        "btn_export_pdf": "Export PDF",
        "btn_clear_all": "Clear All",
        "project_tally_title": "My Project",
        "price_section_label": "Add prices for cost estimate (optional)",
        "cost_estimate_label": "Estimated Cost",
        "buying_unit_prefix": "→",
    },
    "fr": {
        "btn_pdf": "Télécharger PDF",
        "btn_add_project": "Ajouter au projet",
        "btn_export_pdf": "Exporter PDF",
        "btn_clear_all": "Tout effacer",
        "project_tally_title": "Mon projet",
        "price_section_label": "Ajouter les prix pour estimer le coût (optionnel)",
        "cost_estimate_label": "Coût estimé",
        "buying_unit_prefix": "→",
    },
    "de": {
        "btn_pdf": "PDF herunterladen",
        "btn_add_project": "Zum Projekt hinzufügen",
        "btn_export_pdf": "PDF exportieren",
        "btn_clear_all": "Alles löschen",
        "project_tally_title": "Mein Projekt",
        "price_section_label": "Preise für Kostenschätzung hinzufügen (optional)",
        "cost_estimate_label": "Geschätzte Kosten",
        "buying_unit_prefix": "→",
    },
    "it": {
        "btn_pdf": "Scarica PDF",
        "btn_add_project": "Aggiungi al progetto",
        "btn_export_pdf": "Esporta PDF",
        "btn_clear_all": "Cancella tutto",
        "project_tally_title": "Il mio progetto",
        "price_section_label": "Aggiungi prezzi per stimare il costo (opzionale)",
        "cost_estimate_label": "Costo stimato",
        "buying_unit_prefix": "→",
    },
    "pt": {
        "btn_pdf": "Baixar PDF",
        "btn_add_project": "Adicionar ao projeto",
        "btn_export_pdf": "Exportar PDF",
        "btn_clear_all": "Limpar tudo",
        "project_tally_title": "Meu projeto",
        "price_section_label": "Adicionar preços para estimar custo (opcional)",
        "cost_estimate_label": "Custo estimado",
        "buying_unit_prefix": "→",
    },
    "es": {
        "btn_pdf": "Descargar PDF",
        "btn_add_project": "Añadir al proyecto",
        "btn_export_pdf": "Exportar PDF",
        "btn_clear_all": "Borrar todo",
        "project_tally_title": "Mi proyecto",
        "price_section_label": "Añadir precios para estimar el coste (opcional)",
        "cost_estimate_label": "Coste estimado",
        "buying_unit_prefix": "→",
    },
}

for lang, keys in KEYS.items():
    path = ROOT / f"{lang}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update(keys)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"  {lang}.json: {len(keys)} keys added")

print("Done.")

#!/usr/bin/env python3
"""Fix ALL German site-level strings — block slugs, UI, navigation, errors."""
import json, os

I18N_DIR = r"C:\Microsaas\obra\src\i18n"

with open(os.path.join(I18N_DIR, "de.json"), "r", encoding="utf-8") as f:
    de = json.load(f)

# === BLOCK SLUGS (currently in Spanish) ===
de["block_slugs"] = {
    "estructuras": "Fundamente & Rohbau",
    "mamposteria": "Mauerwerk & Wände",
    "pavimentos": "Böden & Fliesen",
    "fontaneria": "Sanitär & Wasser",
    "electricidad": "Elektroinstallation & Beleuchtung",
    "climatizacion": "Heizung, Lüftung & Klima",
    "carpinteria": "Tischler- & Metallbau",
    "pintura": "Maler & Beschichtungen",
    "gestion": "Baumanagement & Kosten",
    "matematicas": "Mathematik",
    "finanzas": "Finanzen",
    "salud": "Gesundheit",
    "cotidiano": "Alltag & Freizeit",
    "estadistica": "Statistik",
    "ciencia": "Wissenschaft & Physik",
    "conversion": "Einheiten umrechnen",
    "deportes": "Sport & Fitness",
}

# === BLOCK DESCRIPTIONS ===
de["block_descriptions"] = {
    "estructuras": "Kostenlose Fundament- und Betonrechner. Berechnen Sie Zement, Sand, Kies, Bewehrungsstahl und Schalung für Bodenplatten, Einzelfundamente und tragende Bauteile.",
    "mamposteria": "Kostenlose Mauerwerks-Rechner. Ermitteln Sie die exakten Mengen an Ziegeln, Steinen und Mörtel für Wände und Trennwände – inklusive Verschnitt.",
    "pavimentos": "Kostenlose Boden- und Fliesenrechner. Berechnen Sie Fliesen, Parkett, Kleber und Fugenmörtel für jede Fläche mit Verschnittzuschlag.",
    "fontaneria": "Kostenlose Sanitär-Rechner. Schätzen Sie Rohrdurchmesser, Wasserdruck, Durchfluss und Abwasserleitungen für Wohngebäude.",
    "electricidad": "Kostenlose Elektro- und Beleuchtungsrechner. Berechnen Sie Lumen, Kabelquerschnitte, Stromkreise und Leitungsdimensionierung für Ihr Zuhause.",
    "climatizacion": "Kostenlose Heizungs- und Klimarechner. Schätzen Sie Kühlleistung, Heizkörper, Dämmung und Wärmelast für Ihre Räume.",
    "carpinteria": "Kostenlose Tischler- und Metallbau-Rechner. Berechnen Sie Fenster, Türen, Treppen und Stahlprofile.",
    "pintura": "Kostenlose Maler- und Beschichtungsrechner. Berechnen Sie Farbmengen, Tapetenrollen, Putz und Versiegelungen.",
    "gestion": "Kostenlose Baumanagement-Rechner. Schätzen Sie Projektkosten, Arbeitsstunden und Materialbudgets für Ihre Baustelle.",
    "matematicas": "Kostenlose Mathematik-Rechner: Prozente, Geometrie, Algebra, Dreisatz und mehr. Sofortige Ergebnisse ohne Anmeldung.",
    "finanzas": "Kostenlose Finanzrechner: Hypotheken, Darlehen, Zinseszins, Mehrwertsteuer, Nettogehalt, Rabatte und Break-Even-Point.",
    "salud": "Kostenlose Gesundheitsrechner: BMI, täglicher Kalorienbedarf, Idealgewicht und Wasserbedarf. Ergebnisse basierend auf Ihrem Gewicht, Ihrer Größe und Ihrem Aktivitätslevel.",
    "cotidiano": "Alltagsrechner: Trinkgeld, Alter, Datumsdifferenz und mehr. Praktisch für jede Alltagssituation.",
    "estadistica": "Kostenlose Statistik-Rechner: Mittelwert, Median, Standardabweichung, Varianz, Wahrscheinlichkeit und mehr. Sofortige Ergebnisse.",
    "ciencia": "Wissenschafts- und Physik-Rechner: Geschwindigkeit, Kraft, Energie, Druck, Elektrizität und mehr.",
    "conversion": "Kostenlose Einheitenumrechner: Länge, Gewicht, Temperatur, Volumen, Fläche, Geschwindigkeit und mehr.",
    "deportes": "Sportrechner: Lauftempo, Kalorienverbrauch, Herzfrequenz, VO2max und mehr.",
}

# === SITE-LEVEL UI STRINGS ===
de["site_name"] = "CalcToWork"
de["site_tagline"] = "Kostenlose Online-Rechner für Mathematik, Finanzen, Gesundheit, Wissenschaft und mehr"
de["home_h1"] = "Kostenlose Online-Rechner – Mathematik, Finanzen, Gesundheit & mehr"
de["site_description"] = "Über 460 kostenlose Online-Rechner: Mathematik, Finanzen, Gesundheit, Statistik, Wissenschaft, Umrechnungen, Sport und Bauwesen. Sofortige Ergebnisse, keine Anmeldung."

# Navigation
de["nav_home"] = "Startseite"
de["nav_tools"] = "Rechner"
de["nav_about"] = "Über uns"
de["nav_privacy"] = "Datenschutz"
de["nav_terms"] = "Nutzungsbedingungen"
de["nav_contact"] = "Kontakt"
de["all_tools"] = "Alle Rechner"
de["related_tools"] = "Ähnliche Rechner"

# Buttons
de["calculate_btn"] = "Berechnen"
de["reset_btn"] = "Zurücksetzen"
de["result_title"] = "Ergebnis"
de["btn_copy"] = "Ergebnis kopieren"
de["btn_calculate"] = "Berechnen"
de["btn_reset"] = "Zurücksetzen"
de["copied_label"] = "Kopiert!"
de["link_copied_label"] = "Link kopiert!"
de["btn_pdf"] = "PDF herunterladen"
de["btn_add_project"] = "Zum Projekt hinzufügen"
de["btn_export_pdf"] = "PDF exportieren"
de["btn_clear_all"] = "Alles löschen"
de["btn_embed"] = "Einbetten"
de["btn_copy_embed"] = "Einbettungscode kopieren"

# Errors
de["error_invalid"] = "Bitte geben Sie gültige Werte ein."
de["error_invalid_math"] = "Berechnung nicht möglich – überprüfen Sie Ihre Eingaben (Division durch Null oder Wert außerhalb des Bereichs)."
de["error_input_range"] = "Der Wert muss zwischen {min} und {max} liegen."
de["error_no_output"] = "Keine Ergebniskonfiguration gefunden."

# Labels
de["label_inputs"] = "Eingaben"
de["label_results"] = "Ergebnisse"
de["result_placeholder"] = "Geben Sie die Werte ein und klicken Sie auf Berechnen"
de["table_headers"] = {}
de["unit_labels"] = {}

# Footer
de["footer_text"] = "Kostenlose Online-Rechner für alle"
de["footer_disclaimer"] = "Die Ergebnisse sind unverbindliche Schätzwerte. Konsultieren Sie stets einen Fachmann."
de["meta_suffix"] = "| CalcToWork"

# Cookies / Consent
de["email_consent"] = "Ich bin damit einverstanden, Produktaktualisierungen per E-Mail zu erhalten."
de["consent_required_lead"] = "Akzeptieren Sie Cookies, um E-Mail-Updates zu erhalten."
de["private_mode_warning"] = "Privater Modus – Ihre Daten werden zwischen Besuchen nicht gespeichert."

# Comparison
de["comparison_region_label"] = "Vergleichsvoreinstellungen"
de["sensitivity_no_var"] = "Fügen Sie einen zweiten Wert hinzu, um zu sehen, wie sich das Ergebnis ändert."

# Share
de["share_native"] = "Teilen"
de["last_updated"] = "Zuletzt aktualisiert"
de["reviewed_by"] = "Geprüft von"

# Price / Project
de["price_section_label"] = "Geschätzte Kosten"
de["cost_estimate_label"] = "Kostenschätzung"
de["buying_unit_prefix"] = "→"
de["project_tally_title"] = "Mein Projekt"
de["tally_empty"] = "Noch keine Einträge. Berechnen Sie etwas und klicken Sie auf „+ Projekt\"."

# Sensitivity
de["sensitivity_toggle"] = "Zeigen, wie sich {output} mit {input} ändert"

# Embed
de["embed_title"] = "Diesen Rechner einbetten"
de["embed_desc"] = "Kopieren Sie den folgenden Code, um diesen Rechner auf Ihrer Website einzubetten:"

# Email
de["email_title"] = "Bleiben Sie auf dem Laufenden"
de["email_desc"] = "Erhalten Sie die neuesten Rechner und Updates direkt in Ihren Posteingang."
de["email_placeholder"] = "Ihre E-Mail-Adresse"
de["email_btn"] = "Abonnieren"

# Feedback
de["feedback_thanks"] = "Vielen Dank!"

# Net/Total labels
de["net_label"] = "Netto (ohne Verschnitt)"
de["total_label"] = "Gesamt zu kaufen (+{pct}% Verschnitt)"

# Tags
de["tags"] = {}

# Cookie consent
de["cookie_consent_title"] = "Cookie-Einstellungen"
de["cookie_consent_text"] = "Diese Website verwendet Cookies, um Ihnen die bestmögliche Erfahrung zu bieten."
de["cookie_accept"] = "Akzeptieren"
de["cookie_reject"] = "Ablehnen"
de["cookie_customize"] = "Anpassen"

with open(os.path.join(I18N_DIR, "de.json"), "w", encoding="utf-8") as f:
    json.dump(de, f, ensure_ascii=False, indent=2)

print("All German UI strings fixed!")

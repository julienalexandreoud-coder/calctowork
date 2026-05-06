# -*- coding: utf-8 -*-
"""Comprehensive Spanish->German narrative translation for all 461 calculators."""
import json, os, glob

CALC = r"C:\Microsaas\obra\src\calculators"

REPLS = [
    # Articles
    (" El ", " Der "), (" el ", " der "), (" La ", " Die "), (" la ", " die "),
    (" Los ", " Die "), (" los ", " die "), (" Las ", " Die "), (" las ", " die "),
    (" del ", " des "), (" de la ", " der "), (" de los ", " der "),
    (" de las ", " der "), (" al ", " zum "), (" en el ", " im "),
    (" en la ", " in der "), (" en los ", " in den "), (" en las ", " in den "),
    (" un ", " ein "), (" una ", " eine "), (" unos ", " einige "),
    # Verbs
    ("Multiplicar ", "Multiplizieren "), ("Calcular ", "Berechnen "),
    ("Determinar ", "Bestimmen "), ("Introducir ", "Eingeben "),
    ("Obtener ", "Ermitteln "), ("Verificar ", "Uberprufen "),
    ("Usar ", "Verwenden "), ("Ingresar ", "Eingeben "),
    ("Medir ", "Messen "), ("Sumar ", "Addieren "),
    ("Dividir ", "Dividieren "), ("Restar ", "Subtrahieren "),
    ("Aplicar ", "Anwenden "), ("Seleccionar ", "Auswahlen "),
    ("Considerar ", "Berucksichtigen "), ("Convertir ", "Umwandeln "),
    ("Comparar ", "Vergleichen "), ("Comprobar ", "Uberprufen "),
    ("Identificar ", "Identifizieren "), ("Realizar ", "Durchfuhren "),
    ("Elegir ", "Auswahlen "), ("Revisar ", "Uberprufen "),
    ("Olvidar ", "Vergessen "), ("Confundir ", "Verwechseln "),
    ("Ignorar ", "Ignorieren "), ("Expresar ", "Ausdrucken "),
    ("Instalar ", "Installieren "), ("Asegurar ", "Sicherstellen "),
    ("Ajustar ", "Anpassen "), ("Guardar ", "Speichern "),
    ("Mostrar ", "Anzeigen "), ("Permitir ", "Ermoglichen "),
    ("Evitar ", "Vermeiden "), ("Incluir ", "Einschliessen "),
    ("Redondear ", "Runden "), ("Buscar ", "Suchen "),
    # Lowercase verbs
    ("multiplicar ", "multiplizieren "), ("calcular ", "berechnen "),
    ("determinar ", "bestimmen "), ("introducir ", "eingeben "),
    ("obtener ", "ermitteln "), ("verificar ", "uberprufen "),
    ("usar ", "verwenden "), ("ingresar ", "eingeben "),
    ("medir ", "messen "), ("sumar ", "addieren "),
    ("dividir ", "dividieren "), ("restar ", "subtrahieren "),
    ("aplicar ", "anwenden "), ("seleccionar ", "auswahlen "),
    ("considerar ", "berucksichtigen "), ("convertir ", "umwandeln "),
    ("comparar ", "vergleichen "), ("comprobar ", "uberprufen "),
    ("identificar ", "identifizieren "), ("realizar ", "durchfuhren "),
    ("elegir ", "auswahlen "), ("revisar ", "uberprufen "),
    ("olvidar ", "vergessen "), ("confundir ", "verwechseln "),
    ("ignorar ", "ignorieren "), ("esprimere ", "ausdrucken "),
    ("instalar ", "installieren "), ("asegurar ", "sicherstellen "),
    ("ajustar ", "anpassen "), ("mostrar ", "anzeigen "),
    ("permitir ", "ermoglichen "), ("evitar ", "vermeiden "),
    # English verbs in DE text
    ("Calculate ", "Berechnen "), ("calculate ", "berechnen "),
    ("Enter ", "Eingeben "), ("enter ", "eingeben "),
    ("Using ", "Verwenden von "), ("using ", "verwenden von "),
    ("Entering ", "Eingabe von "), ("entering ", "eingabe von "),
    ("Forgetting ", "Vergessen von "), ("forgetting ", "vergessen von "),
    ("Confusing ", "Verwechseln von "), ("confusing ", "verwechseln von "),
    # Nouns
    ("resultado ", "Ergebnis "), ("resultados ", "Ergebnisse "),
    ("Resultado ", "Ergebnis "), ("Resultados ", "Ergebnisse "),
    ("valor ", "Wert "), ("Valor ", "Wert "),
    ("valores ", "Werte "), ("Valores ", "Werte "),
    ("cantidad ", "Menge "), ("Cantidad ", "Menge "),
    ("unidad ", "Einheit "), ("Unidad ", "Einheit "),
    ("unidades ", "Einheiten "), ("Unidades ", "Einheiten "),
    ("peso ", "Gewicht "), ("Peso ", "Gewicht "),
    ("altura ", "Hohe "), ("Altura ", "Hohe "),
    ("longitud ", "Lange "), ("Longitud ", "Lange "),
    ("anchura ", "Breite "), ("Anchura ", "Breite "),
    ("profundidad ", "Tiefe "), ("Profundidad ", "Tiefe "),
    ("espesor ", "Dicke "), ("Espesor ", "Dicke "),
    ("tiempo ", "Zeit "), ("Tiempo ", "Zeit "),
    ("velocidad ", "Geschwindigkeit "), ("Velocidad ", "Geschwindigkeit "),
    ("temperatura ", "Temperatur "), ("Temperatura ", "Temperatur "),
    ("presion ", "Druck "), ("Presion ", "Druck "),
    ("presi\u00f3n ", "Druck "), ("Presi\u00f3n ", "Druck "),
    ("fuerza ", "Kraft "), ("Fuerza ", "Kraft "),
    ("energia ", "Energie "), ("Energia ", "Energie "),
    ("energ\u00eda ", "Energie "), ("Energ\u00eda ", "Energie "),
    ("potencia ", "Leistung "), ("Potencia ", "Leistung "),
    ("coste ", "Kosten "), ("Coste ", "Kosten "),
    ("precio ", "Preis "), ("Precio ", "Preis "),
    ("pago ", "Zahlung "), ("Pago ", "Zahlung "),
    ("interes ", "Zinsen "), ("Interes ", "Zinsen "),
    ("inter\u00e9s ", "Zinsen "), ("Inter\u00e9s ", "Zinsen "),
    ("tasa ", "Rate "), ("Tasa ", "Rate "),
    ("porcentaje ", "Prozentsatz "), ("Porcentaje ", "Prozentsatz "),
    ("descuento ", "Rabatt "), ("Descuento ", "Rabatt "),
    ("margen ", "Marge "), ("Margen ", "Marge "),
    ("beneficio ", "Gewinn "), ("Beneficio ", "Gewinn "),
    ("caloria ", "Kalorie "), ("Caloria ", "Kalorie "),
    ("calorias ", "Kalorien "), ("Calorias ", "Kalorien "),
    ("calor\u00eda ", "Kalorie "), ("Calor\u00eda ", "Kalorie "),
    ("calor\u00edas ", "Kalorien "), ("Calor\u00edas ", "Kalorien "),
    ("agua ", "Wasser "), ("Agua ", "Wasser "),
    ("paso ", "Schritt "), ("Paso ", "Schritt "),
    ("pasos ", "Schritte "), ("Pasos ", "Schritte "),
    ("calculo ", "Berechnung "), ("Calculo ", "Berechnung "),
    ("c\u00e1lculo ", "Berechnung "), ("C\u00e1lculo ", "Berechnung "),
    ("formula ", "Formel "), ("Formula ", "Formel "),
    ("f\u00f3rmula ", "Formel "), ("F\u00f3rmula ", "Formel "),
    ("ecuacion ", "Gleichung "), ("Ecuacion ", "Gleichung "),
    ("ecuaci\u00f3n ", "Gleichung "), ("Ecuaci\u00f3n ", "Gleichung "),
    ("ejemplo ", "Beispiel "), ("Ejemplo ", "Beispiel "),
    ("proyecto ", "Projekt "), ("Proyecto ", "Projekt "),
    ("datos ", "Daten "), ("Datos ", "Daten "),
    ("entrada ", "Eingabe "), ("Entrada ", "Eingabe "),
    ("salida ", "Ausgabe "), ("Salida ", "Ausgabe "),
    ("herramienta ", "Werkzeug "), ("Herramienta ", "Werkzeug "),
    ("herramientas ", "Werkzeuge "), ("Herramientas ", "Werkzeuge "),
    ("desperdicio ", "Verschwendung "), ("Desperdicio ", "Verschwendung "),
    ("merma ", "Schwund "), ("Merma ", "Schwund "),
    ("error ", "Fehler "), ("Error ", "Fehler "),
    ("errores ", "Fehler "), ("Errores ", "Fehler "),
    ("imprevisto ", "Unvorhergesehenes "), ("Imprevisto ", "Unvorhergesehenes "),
    ("imprevistos ", "Unvorhergesehenes "), ("Imprevistos ", "Unvorhergesehenes "),
    ("volumen ", "Volumen "), ("Volumen ", "Volumen "),
    ("area ", "Flache "), ("Area ", "Flache "),
    ("arena ", "Sand "), ("Arena ", "Sand "),
    ("grava ", "Kies "), ("Grava ", "Kies "),
    ("cemento ", "Zement "), ("Cemento ", "Zement "),
    ("hormigon ", "Beton "), ("Hormigon ", "Beton "),
    ("hormig\u00f3n ", "Beton "), ("Hormig\u00f3n ", "Beton "),
    ("resistencia ", "Festigkeit "), ("Resistencia ", "Festigkeit "),
    ("mezcla ", "Mischung "), ("Mezcla ", "Mischung "),
    # Common words
    (" para ", " fur "), (" como ", " wie "),
    (" cuando ", " wenn "), (" donde ", " wo "),
    (" necesario ", " notwendig "), (" necesaria ", " notwendig "),
    (" necesarios ", " notwendig "), (" necesarias ", " notwendig "),
    (" utilizando ", " unter Verwendung von "), (" usando ", " mit "),
    (" basado ", " basierend auf "), (" basada ", " basierend auf "),
    (" incluyendo ", " einschliesslich "), (" incluye ", " beinhaltet "),
    (" incluyen ", " beinhalten "),
    (" seg\u00fan ", " laut "), (" segun ", " laut "),
    # Quantities
    (" m\u00e1s ", " mehr "), (" mas ", " mehr "),
    (" menos ", " weniger "), (" cada ", " jede "),
    (" todo ", " alle "), (" toda ", " alle "),
    (" todos ", " alle "), (" todas ", " alle "),
    (" mismo ", " gleiche "), (" misma ", " gleiche "),
    (" otro ", " andere "), (" otra ", " andere "),
    (" otros ", " andere "), (" otras ", " andere "),
    (" m\u00ednimo ", " Minimum "), (" minimo ", " Minimum "),
    (" m\u00e1ximo ", " Maximum "), (" maximo ", " Maximum "),
    (" promedio ", " Durchschnitt "), (" total ", " Gesamt "),
    (" actual ", " aktuell "), (" inicial ", " Anfangs-"),
    (" final ", " End-"), (" siguiente ", " nachste "),
    # Time
    (" a\u00f1o ", " Jahr "), (" anos ", " Jahre "),
    (" a\u00f1os ", " Jahre "), (" mes ", " Monat "),
    (" meses ", " Monate "), (" d\u00eda ", " Tag "),
    (" dias ", " Tage "), (" d\u00edas ", " Tage "),
    (" hora ", " Stunde "), (" horas ", " Stunden "),
    (" minuto ", " Minute "), (" minutos ", " Minuten "),
    (" segundo ", " Sekunde "), (" segundos ", " Sekunden "),
    (" semana ", " Woche "), (" semanas ", " Wochen "),
    # Adjectives
    (" correcto ", " korrekt "), (" correcta ", " korrekt "),
    (" importante ", " wichtig "), (" principal ", " Haupt-"),
    (" grande ", " gross "), (" peque\u00f1o ", " klein "),
    (" pequeno ", " klein "), (" peque\u00f1a ", " klein "),
    (" pequena ", " klein "), (" nuevo ", " neu "),
    (" nueva ", " neu "), (" nuevos ", " neu "),
    (" r\u00e1pido ", " schnell "), (" rapido ", " schnell "),
    (" lento ", " langsam "), (" f\u00e1cil ", " einfach "),
    (" facil ", " einfach "), (" dif\u00edcil ", " schwierig "),
    (" dificil ", " schwierig "), (" mejor ", " besser "),
    (" peor ", " schlechter "), (" mayor ", " grosser "),
    (" menor ", " kleiner "), (" alto ", " hoch "),
    (" bajo ", " niedrig "), (" baja ", " niedrig "),
    (" gratis ", " kostenlos "), (" gratuita ", " kostenlos "),
    (" gratuito ", " kostenlos "),
    # Units
    (" metro ", " Meter "), (" metros ", " Meter "),
    (" centimetro ", " Zentimeter "), (" centimetros ", " Zentimeter "),
    (" milimetro ", " Millimeter "), (" milimetros ", " Millimeter "),
    (" kilogramo ", " Kilogramm "), (" kilos ", " Kilo "),
    (" gramo ", " Gramm "), (" gramos ", " Gramm "),
    (" litro ", " Liter "), (" litros ", " Liter "),
    (" euro ", " Euro "), (" euros ", " Euro "),
    (" dolar ", " Dollar "), (" dolares ", " Dollar "),
    # Common verbs
    (" puede ", " kann "), (" pueden ", " konnen "),
    (" debe ", " muss "), (" deben ", " mussen "),
    (" tiene ", " hat "), (" tienen ", " haben "),
    (" hay ", " es gibt "), (" hacer ", " machen "),
    (" este ", " dieser "), (" esta ", " diese "),
    (" estos ", " diese "), (" estas ", " diese "),
    (" es ", " ist "), (" son ", " sind "),
    (" est\u00e1 ", " ist "), (" est\u00e1n ", " sind "),
    (" estan ", " sind "), (" entre ", " zwischen "),
    (" sobre ", " uber "), (" despu\u00e9s ", " nach "),
    (" despues ", " nach "), (" antes ", " vor "),
    (" durante ", " wahrend "), (" siempre ", " immer "),
    (" nunca ", " nie "), (" mucho ", " viel "),
    (" poco ", " wenig "), (" muy ", " sehr "),
    (" tambi\u00e9n ", " auch "), (" tambien ", " auch "),
    (" solo ", " nur "), (" requiere ", " erfordert "),
    (" requieren ", " erfordern "),
    # Specific verbs
    ("Calcula ", "Berechne "), ("calcula ", "berechne "),
    ("Usa ", "Verwende "), ("usa ", "verwende "),
    ("Introduce ", "Gib ein "), ("introduce ", "gib ein "),
]

def apply(text):
    if not isinstance(text, str): return text
    for old, new in REPLS:
        text = text.replace(old, new)
    import re
    text = re.sub(r'\s+', ' ', text).strip()
    if text and text[0].islower():
        text = text[0].upper() + text[1:]
    return text

def main():
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json": continue
        with open(fp, "r", encoding="utf-8-sig") as fh: calc = json.load(fh)
        de = calc.setdefault("i18n", {}).setdefault("de", {})
        es = calc.get("i18n", {}).get("es", {})
        if not es: continue
        changed = False
        
        for field in ["steps", "mistakes"]:
            es_val = es.get(field, [])
            if not es_val: continue
            if isinstance(es_val, list):
                de_new = [apply(str(s)) for s in es_val]
                if de.get(field) != de_new:
                    de[field] = de_new
                    changed = True
        
        for field in ["result_context", "example_label", "formula_display"]:
            es_val = es.get(field, "")
            if es_val and isinstance(es_val, str):
                de_new = apply(es_val)
                if de.get(field) != de_new:
                    de[field] = de_new
                    changed = True
        
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated} German files")

if __name__ == "__main__":
    main()

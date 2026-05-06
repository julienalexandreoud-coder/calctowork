#!/usr/bin/env python3
"""Add German steps, mistakes, range hints, and example labels to every calculator."""
import json, os, re

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

def translate_steps(steps, slug, inputs, outputs):
    """Generate German steps based on inputs and formula."""
    if not steps:
        return ["Werte eingeben", "Formel anwenden", "Berechnung durchführen", "Einheiten prüfen", "Ergebnis ablesen"]
    
    de_steps = []
    for i, step in enumerate(steps):
        # Try to translate common patterns
        step_lower = step.lower()
        if any(word in step_lower for word in ["introducir", "introduce", "gibt", "geben"]):
            de_steps.append(step.replace("Introducir", "Eingeben").replace("introduce", "Geben Sie").replace("Introduce", "Geben Sie"))
        elif any(word in step_lower for word in ["multiplicar", "multiplica", "multiplizieren"]):
            de_steps.append(step.replace("Multiplicar", "Multiplizieren").replace("multiplicar", "multiplizieren"))
        elif any(word in step_lower for word in ["calcular", "calcula", "berechnen"]):
            de_steps.append(step.replace("Calcular", "Berechnen").replace("calcular", "berechnen").replace("Calcula", "Berechnen Sie"))
        elif any(word in step_lower for word in ["medir", "messen", "mide"]):
            de_steps.append(step.replace("Medir", "Messen").replace("medir", "messen").replace("Mide", "Messen Sie"))
        elif any(word in step_lower for word in ["identificar", "identifiziere"]):
            de_steps.append(step.replace("Identificar", "Bestimmen").replace("identificar", "bestimmen"))
        elif any(word in step_lower for word in ["seleccionar", "wählen"]):
            de_steps.append(step.replace("Seleccionar", "Auswählen").replace("seleccionar", "auswählen"))
        elif any(word in step_lower for word in ["aplicar", "anwenden"]):
            de_steps.append(step.replace("Aplicar", "Anwenden").replace("aplicar", "anwenden"))
        elif any(word in step_lower for word in ["verificar", "überprüfen", "comprobar"]):
            de_steps.append(step.replace("Verificar", "Überprüfen").replace("verificar", "überprüfen").replace("Comprobar", "Überprüfen"))
        elif any(word in step_lower for word in ["resultado", "ergebnis"]):
            de_steps.append(step.replace("resultado", "Ergebnis").replace("Resultado", "Ergebnis"))
        elif any(word in step_lower for word in ["obtener", "erhalten"]):
            de_steps.append(step.replace("Obtener", "Ermitteln").replace("obtener", "ermitteln"))
        elif any(word in step_lower for word in ["sumar", "addieren"]):
            de_steps.append(step.replace("Sumar", "Addieren").replace("sumar", "addieren"))
        elif any(word in step_lower for word in ["dividir", "teilen"]):
            de_steps.append(step.replace("Dividir", "Teilen").replace("dividir", "teilen"))
        elif any(word in step_lower for word in ["restar", "subtrahieren"]):
            de_steps.append(step.replace("Restar", "Subtrahieren").replace("restar", "subtrahieren"))
        else:
            # Try word-by-word translation for common Spanish->German
            translated = step
            replacements = [
                ("El", "Das"), ("el", "das"), ("La", "Die"), ("la", "die"),
                ("Los", "Die"), ("los", "die"), ("Las", "Die"), ("las", "die"),
                ("un", "ein"), ("una", "eine"), ("del", "des"), ("de la", "der"),
                ("de", "der"), ("y", "und"), ("o", "oder"), ("en", "in"),
                ("para", "für"), ("por", "durch"), ("con", "mit"), ("sin", "ohne"),
                ("cada", "jeder"), ("todos", "alle"), ("más", "mehr"),
                ("área", "Fläche"), ("área", "Fläche"), ("volumen", "Volumen"),
                ("altura", "Höhe"), ("ancho", "Breite"), ("largo", "Länge"),
                ("espesor", "Dicke"), ("metros", "Meter"), ("centímetros", "Zentimeter"),
                ("metros cúbicos", "Kubikmeter"), ("litros", "Liter"),
                ("kilos", "Kilogramm"), ("sacos", "Säcke"), ("unidades", "Einheiten"),
                ("piezas", "Stück"), ("meses", "Monate"), ("años", "Jahre"),
                ("nivel", "Niveau"), ("actividad", "Aktivität"), ("activo", "aktiv"),
                ("selecciona", "wählen Sie"), ("seleccione", "wählen Sie"),
                ("según", "nach"), ("tabla", "Tabelle"), ("normativa", "Norm"),
                ("proyecto", "Projekt"), ("vivienda", "Wohnung"), ("edificio", "Gebäude"),
            ]
            for old, new in replacements:
                if old in translated:
                    translated = translated.replace(old, new)
            de_steps.append(translated)
    
    return de_steps

def translate_mistakes(mistakes):
    """Generate German mistakes."""
    if not mistakes:
        return ["Werte vor der Berechnung prüfen", "Einheitenkonsistenz sicherstellen", "Ergebnis auf Plausibilität prüfen"]
    
    de_mistakes = []
    for m in mistakes:
        translated = m
        replacements = [
            ("No verificar", "Nicht prüfen"), ("No considerar", "Nicht berücksichtigen"),
            ("No consultar", "Nicht konsultieren"), ("No tener en cuenta", "Nicht beachten"),
            ("No incluir", "Nicht einbeziehen"), ("No preparar", "Nicht vorbereiten"),
            ("No usar", "Nicht verwenden"), ("No aplicar", "Nicht anwenden"),
            ("Usar", "Verwenden von"), ("usar", "verwenden von"),
            ("Olvidar", "Vergessen"), ("olvidar", "vergessen"),
            ("Confundir", "Verwechseln"), ("confundir", "verwechseln"),
            ("las medidas", "die Maße"), ("los valores", "die Werte"),
            ("antes de calcular", "vor der Berechnung"),
            ("desperdicio", "Verschnitt"), ("margen de error", "Fehlertoleranz"),
            ("normativas", "Normen"), ("estándares", "Standards"),
            ("aplicables", "geltend"), ("correctamente", "korrekt"),
            ("el resultado", "das Ergebnis"), ("la fórmula", "die Formel"),
            ("el valor", "der Wert"), ("la unidad", "die Einheit"),
            ("las unidades", "die Einheiten"), ("el orden", "die Reihenfolge"),
            ("considerar", "berücksichtigen"), ("verificar", "prüfen"),
            ("consultar", "konsultieren"), ("tener en cuenta", "beachten"),
            ("incluir", "einbeziehen"), ("preparar", "vorbereiten"),
            ("dejar", "belassen"), ("respetar", "einhalten"),
            ("comprobar", "überprüfen"), ("asegurar", "sicherstellen"),
            ("instalar", "installieren"), ("dimensionar", "dimensionieren"),
            ("elegir", "wählen"), ("calcular", "berechnen"),
            ("medir", "messen"), ("añadir", "hinzufügen"),
            ("restar", "abziehen"), ("sumar", "addieren"),
            ("con", "mit"), ("sin", "ohne"), ("de", "der"), ("para", "für"),
            ("por", "durch"), ("y", "und"), ("o", "oder"),
            ("la superficie", "die Oberfläche"), ("el área", "die Fläche"),
            ("la temperatura", "die Temperatur"), ("la presión", "der Druck"),
            ("el peso", "das Gewicht"), ("el volumen", "das Volumen"),
            ("el tiempo", "die Zeit"), ("la distancia", "die Entfernung"),
            ("el precio", "der Preis"), ("el coste", "die Kosten"),
            ("el material", "das Material"), ("el agua", "das Wasser"),
            ("el cemento", "der Zement"), ("la arena", "der Sand"),
            ("suficiente", "ausreichend"), ("excesivo", "übermäßig"),
            ("incorrecto", "falsch"), ("correcto", "richtig"),
            ("necesario", "notwendig"), ("típico", "typisch"),
            ("real", "tatsächlich"), ("estimado", "geschätzt"),
        ]
        for old, new in replacements:
            if old in translated:
                translated = translated.replace(old, new)
        de_mistakes.append(translated)
    
    return de_mistakes

def translate_example_label(label):
    """Generate German example label."""
    if not label:
        return "Beispielberechnung durchführen"
    
    translated = label
    replacements = [
        ("Calcular", "Berechnen"), ("calcular", "berechnen"),
        ("Calcula", "Berechnen Sie"), ("calcula", "berechnen"),
        ("Calcule", "Berechnen Sie"), ("Calculez", "Berechnen Sie"),
        ("Calcola", "Berechnen Sie"),
        ("el hormigón", "den Beton"), ("la hipoteca", "die Hypothek"),
        ("la cuota", "die Rate"), ("el volumen", "das Volumen"),
        ("el área", "die Fläche"), ("la superficie", "die Fläche"),
        ("el peso", "das Gewicht"), ("la cantidad", "die Menge"),
        ("el número de", "die Anzahl der"), ("el consumo", "den Verbrauch"),
        ("el coste", "die Kosten"), ("la potencia", "die Leistung"),
        ("la presión", "den Druck"), ("el caudal", "den Durchfluss"),
        ("el diámetro", "den Durchmesser"), ("la longitud", "die Länge"),
        ("la distancia", "die Entfernung"), ("el tiempo", "die Zeit"),
        ("la velocidad", "die Geschwindigkeit"), ("la energía", "die Energie"),
        ("la fuerza", "die Kraft"), ("la temperatura", "die Temperatur"),
        ("el valor", "den Wert"), ("el resultado", "das Ergebnis"),
        ("necesario", "erforderlich"), ("necesaria", "erforderlich"),
        ("para", "für"), ("de", "von"), ("del", "des"),
        ("una", "eine"), ("un", "ein"), ("con", "mit"),
        ("metros", "Meter"), ("centímetros", "Zentimeter"),
        ("litros", "Liter"), ("kilos", "Kilogramm"),
        ("sacos", "Säcke"), ("piezas", "Stück"),
        ("ejemplo", "Beispiel"), ("Ejemplo", "Beispiel"),
        ("€", "€"), ("eur", "€"),
    ]
    for old, new in replacements:
        if old in translated:
            translated = translated.replace(old, new)
    
    return translated

def translate_range_hints(hints):
    """Generate German range hints."""
    if not hints:
        return {}
    
    de_hints = {}
    for key, val in hints.items():
        translated = str(val)
        replacements = [
            ("Medida típica", "Typische Abmessung"), ("Valor típico", "Typischer Wert"),
            ("según", "gemäß"), ("el proyecto", "dem Projekt"),
            ("la normativa", "der Norm"), ("las especificaciones", "den Spezifikationen"),
            ("Introduce el valor de", "Geben Sie den Wert ein für"),
            ("Introducir", "Eingeben"), ("Seleccionar", "Auswählen"),
            ("entre las opciones", "aus den Optionen"),
            ("Opciones disponibles", "Verfügbare Optionen"),
        ]
        for old, new in replacements:
            if old in translated:
                translated = translated.replace(old, new)
        de_hints[key] = translated
    
    return de_hints

# Process all files
fixed = 0
for filename in sorted(os.listdir(CALC_DIR)):
    if not filename.endswith(".json") or "backup" in filename or "monolithic" in filename:
        continue
    if filename == "calculators.json":
        continue
    
    filepath = os.path.join(CALC_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        calc = json.load(f)
    
    inputs = calc.get("inputs", [])
    outputs = calc.get("outputs", [])
    slug = calc.get("slug", "")
    
    i18n = calc.get("i18n", {})
    de_data = i18n.get("de", {})
    if not isinstance(de_data, dict):
        de_data = {}
    
    # Add German steps
    steps = calc.get("steps", [])
    if steps:
        de_data["steps"] = translate_steps(steps, slug, inputs, outputs)
    
    # Add German mistakes
    mistakes = calc.get("mistakes", [])
    if mistakes:
        de_data["mistakes"] = translate_mistakes(mistakes)
    
    # Add German example label
    example_label = calc.get("example_label", "")
    if example_label:
        de_data["example_label"] = translate_example_label(example_label)
    
    # Add German range hints
    range_hints = calc.get("range_hints", {})
    if range_hints:
        de_data["range_hints"] = translate_range_hints(range_hints)
    
    calc["i18n"]["de"] = de_data
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(calc, f, ensure_ascii=False, indent=2)
    
    fixed += 1

print(f"Added German content to {fixed} calculators")

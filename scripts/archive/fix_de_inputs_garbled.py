"""
Fix German input labels and clean garbled extended text fields.
"""
import json, glob, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

# Input label translations (Spanish/English variable names -> German labels)
INPUT_TRANSLATIONS = {
    # Spanish -> German (common variable name keys)
    "tiempo": "Zeit",
    "Tiempo": "Zeit",
    "distancia": "Entfernung",
    "Distancia": "Entfernung",
    "velocidad": "Geschwindigkeit",
    "Velocidad": "Geschwindigkeit",
    "aceleracion": "Beschleunigung",
    "Aceleracion": "Beschleunigung",
    "fuerza": "Kraft",
    "Fuerza": "Kraft",
    "masa": "Masse",
    "Masa": "Masse",
    "volumen": "Volumen",
    "Volumen": "Volumen",
    "densidad": "Dichte",
    "Densidad": "Dichte",
    "presion": "Druck",
    "Presion": "Druck",
    "potencia": "Leistung",
    "Potencia": "Leistung",
    "energia": "Energie",
    "Energia": "Energie",
    "corriente": "Strom",
    "Corriente": "Strom",
    "voltaje": "Spannung",
    "Voltaje": "Spannung",
    "resistencia": "Widerstand",
    "Resistencia": "Widerstand",
    "frecuencia": "Frequenz",
    "Frecuencia": "Frequenz",
    "capacitancia": "Kapazität",
    "Capacitancia": "Kapazität",
    "inductancia": "Induktivität",
    "Inductancia": "Induktivität",
    "impedancia": "Impedanz",
    "Impedancia": "Impedanz",
    "longitud": "Länge",
    "Longitud": "Länge",
    "ancho": "Breite",
    "Ancho": "Breite",
    "anchura": "Breite",
    "Anchura": "Breite",
    "altura": "Höhe",
    "Altura": "Höhe",
    "profundidad": "Tiefe",
    "Profundidad": "Tiefe",
    "espesor": "Dicke",
    "Espesor": "Dicke",
    "radio": "Radius",
    "Radio": "Radius",
    "diametro": "Durchmesser",
    "Diametro": "Durchmesser",
    "perimetro": "Umfang",
    "Perimetro": "Umfang",
    "temperatura": "Temperatur",
    "Temperatura": "Temperatur",
    "angulo": "Winkel",
    "Angulo": "Winkel",
    "numero": "Zahl",
    "Numero": "Zahl",
    "fraccion": "Bruch",
    "Fraccion": "Bruch",
    "porcentaje": "Prozentsatz",
    "Porcentaje": "Prozentsatz",
    "decimales": "Dezimalstellen",
    "Decimales": "Dezimalstellen",
    "precio": "Preis",
    "Precio": "Preis",
    "costo": "Kosten",
    "Costo": "Kosten",
    "salario": "Gehalt",
    "Salario": "Gehalt",
    "tasa": "Zinssatz",
    "Tasa": "Zinssatz",
    "interes": "Zinsen",
    "Interes": "Zinsen",
    "capital": "Kapital",
    "Capital": "Kapital",
    "inversion": "Investition",
    "Inversion": "Investition",
    "ganancia": "Gewinn",
    "Ganancia": "Gewinn",
    "deuda": "Schulden",
    "Deuda": "Schulden",
    "hipoteca": "Hypothek",
    "Hipoteca": "Hypothek",
    "prestamo": "Kredit",
    "Prestamo": "Kredit",
    "ahorro": "Ersparnis",
    "Ahorro": "Ersparnis",
    "descuento": "Rabatt",
    "Descuento": "Rabatt",
    "impuesto": "Steuer",
    "Impuesto": "Steuer",
    "propina": "Trinkgeld",
    "Propina": "Trinkgeld",
    "calorias": "Kalorien",
    "Calorias": "Kalorien",
    "peso": "Gewicht",
    "Peso": "Gewicht",
    "altura_cm": "Größe (cm)",
    "edad": "Alter",
    "Edad": "Alter",
    "sexo": "Geschlecht",
    "Sexo": "Geschlecht",
    "grasa": "Körperfett",
    "Grasa": "Körperfett",
    "cintura": "Taillenumfang",
    "Cintura": "Taillenumfang",
    "cadera": "Hüftumfang",
    "Cadera": "Hüftumfang",
    "sistolica": "Systolisch",
    "Sistolica": "Systolisch",
    "diastolica": "Diastolisch",
    "Diastolica": "Diastolisch",
    "agua": "Wasser",
    "Agua": "Wasser",
    "litros": "Liter",
    "Litros": "Liter",
    "metros": "Meter",
    "Metros": "Meter",
    "kilogramos": "Kilogramm",
    "Kilogramos": "Kilogramm",
    "gramos": "Gramm",
    "Gramos": "Gramm",
    "centimetros": "Zentimeter",
    "Centimetros": "Zentimeter",
    "milimetros": "Millimeter",
    "Milimetros": "Millimeter",
    "horas": "Stunden",
    "Horas": "Stunden",
    "minutos": "Minuten",
    "Minutos": "Minuten",
    "segundos": "Sekunden",
    "Segundos": "Sekunden",
    "dias": "Tage",
    "Dias": "Tage",
    "semanas": "Wochen",
    "Semanas": "Wochen",
    "meses": "Monate",
    "Meses": "Monate",
    "anos": "Jahre",
    "Anos": "Jahre",
    "anio": "Jahr",
    "Anio": "Jahr",
    "mes": "Monat",
    "Mes": "Monat",
    "dia": "Tag",
    "Dia": "Tag",
    "area": "Fläche",
    "Area": "Fläche",
    "superficie": "Fläche",
    "Superficie": "Fläche",
    "habitaciones": "Zimmer",
    "Habitaciones": "Zimmer",
    "personas": "Personen",
    "Personas": "Personen",
    "duracion": "Dauer",
    "Duracion": "Dauer",
    "cantidad": "Menge",
    "Cantidad": "Menge",
    "objetivo": "Ziel",
    "Objetivo": "Ziel",
    "valor": "Wert",
    "Valor": "Wert",
    "unidad": "Einheit",
    "Unidad": "Einheit",
    "pendiente": "Steigung",
    "Pendiente": "Steigung",
    "constante": "Konstante",
    "Constante": "Konstante",
    "coeficiente": "Koeffizient",
    "Coeficiente": "Koeffizient",
    "exponente": "Exponent",
    "Exponente": "Exponent",
    "base": "Basis",
    "Base": "Basis",
    "lado": "Seite",
    "Lado": "Seite",
    "largo": "Länge",
    "Largo": "Länge",
    "carga": "Belastung",
    "Carga": "Belastung",
    "confianza": "Konfidenz",
    "Confianza": "Konfidenz",
    "significancia": "Signifikanz",
    "Significancia": "Signifikanz",
    "muestra": "Stichprobe",
    "Muestra": "Stichprobe",
    "fecha": "Datum",
    "Fecha": "Datum",
    "nacimiento": "Geburt",
    "Nacimiento": "Geburt",
    "inicio": "Start",
    "Inicio": "Start",
    "fin": "Ende",
    "Fin": "Ende",
    "cuenta": "Rechnung",
    "Cuenta": "Rechnung",
    "monto": "Betrag",
    "Monto": "Betrag",
    "pago": "Zahlung",
    "Pago": "Zahlung",
    "mensual": "Monatlich",
    "Mensual": "Monatlich",
    "anual": "Jährlich",
    "Anual": "Jährlich",
    "semanal": "Wöchentlich",
    "Semanal": "Wöchentlich",
    "diario": "Täglich",
    "Diario": "Täglich",
}

def fix_calculator_german(filepath):
    """Fix German i18n in calculator JSON: inputs and clean garbled fields."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    de = data.get('i18n', {}).get('de', {})
    if not de:
        return False
    
    modified = False
    
    # Fix input labels
    inputs = de.get('inputs', {})
    if inputs:
        new_inputs = {}
        for key, val in inputs.items():
            if val in INPUT_TRANSLATIONS:
                new_val = INPUT_TRANSLATIONS[val]
                if new_val != val:
                    modified = True
                new_inputs[key] = new_val
            else:
                new_inputs[key] = val
        de['inputs'] = new_inputs
    
    # Clean garbled extended fields - remove/clear obviously garbled content
    # These fields are NOT used by templates but are stored in the JSON
    garbled_markers = ['calcudiet', 'calcudie', 'furterminar', 'furcolocar',
                       'absonne', 'bund ', 'repristints', 'inergia',
                       'mofurrada', 'diist ', 'rechneih', 'uurrect',
                       'rderative', 'isttimation', 'bundated', 'paundmint',
                       'undear', 'percintage', 'mitsumo', 'adhistivo',
                       'incodiedo']
    
    for field in ['example_label', 'range_hints', 'steps', 'mistakes',
                  'input_type_review', 'formula_display', 'result_context']:
        val = de.get(field, '')
        if isinstance(val, str) and val:
            val_lower = val.lower()
            if any(m in val_lower for m in garbled_markers):
                # Clear the garbled field
                if isinstance(de.get(field), list):
                    de[field] = []
                elif isinstance(de.get(field), dict):
                    de[field] = {}
                else:
                    de[field] = ''
                modified = True
        elif isinstance(val, list):
            all_text = ' '.join(str(v).lower() for v in val)
            if any(m in all_text for m in garbled_markers):
                de[field] = []
                modified = True
        elif isinstance(val, dict):
            all_text = ' '.join(str(v).lower() for v in val.values())
            if any(m in all_text for m in garbled_markers):
                de[field] = {}
                modified = True
    
    if modified:
        data['i18n']['de'] = de
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    
    return False


def main():
    files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))
    fixed = 0
    skipped = 0
    
    for f in files:
        if fix_calculator_german(f):
            fixed += 1
        else:
            skipped += 1
    
    print(f"Total: {len(files)} | Fixed: {fixed} | Skipped: {skipped}")

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""Comprehensive Spanish->Italian narrative translation for all 461 calculators."""
import json, os, glob

CALC = r"C:\Microsaas\obra\src\calculators"

# Spanish -> Italian word replacement map
REPLS = [
    # Articles
    (" El ", " Il "), (" el ", " il "), (" La ", " La "), (" la ", " la "),
    (" Los ", " I "), (" los ", " i "), (" Las ", " Le "), (" las ", " le "),
    (" del ", " del "), (" de la ", " della "), (" de los ", " dei "),
    (" de las ", " delle "), (" al ", " al "), (" en el ", " nel "),
    (" en la ", " nella "), (" en los ", " nei "), (" en las ", " nelle "),
    (" un ", " un "), (" una ", " una "), (" unos ", " alcuni "),
    # Verbs
    ("Multiplicar ", "Moltiplicare "), ("Calcular ", "Calcolare "),
    ("Determinar ", "Determinare "), ("Introducir ", "Inserire "),
    ("Obtener ", "Ottenere "), ("Verificar ", "Verificare "),
    ("Usar ", "Usare "), ("Ingresar ", "Inserire "),
    ("Medir ", "Misurare "), ("Sumar ", "Sommare "),
    ("Dividir ", "Dividere "), ("Restar ", "Sottrarre "),
    ("Aplicar ", "Applicare "), ("Seleccionar ", "Selezionare "),
    ("Considerar ", "Considerare "), ("Convertir ", "Convertire "),
    ("Comparar ", "Confrontare "), ("Comprobar ", "Verificare "),
    ("Identificar ", "Identificare "), ("Realizar ", "Realizzare "),
    ("Elegir ", "Scegliere "), ("Revisar ", "Verificare "),
    ("Olvidar ", "Dimenticare "), ("Confundir ", "Confondere "),
    ("Ignorar ", "Ignorare "), ("Expresar ", "Esprimere "),
    ("Instalar ", "Installare "), ("Asegurar ", "Assicurare "),
    ("Ajustar ", "Regolare "), ("Guardar ", "Salvare "),
    ("Mostrar ", "Mostrare "), ("Permitir ", "Permettere "),
    ("Evitar ", "Evitare "), ("Incluir ", "Includere "),
    ("Redondear ", "Arrotondare "), ("Buscar ", "Cercare "),
    # Lowercase verbs
    ("multiplicar ", "moltiplicare "), ("calcular ", "calcolare "),
    ("determinar ", "determinare "), ("introducir ", "inserire "),
    ("obtener ", "ottenere "), ("verificar ", "verificare "),
    ("usar ", "usare "), ("ingresar ", "inserire "),
    ("medir ", "misurare "), ("sumar ", "sommare "),
    ("dividir ", "dividere "), ("restar ", "sottrarre "),
    ("aplicar ", "applicare "), ("seleccionar ", "selezionare "),
    ("considerar ", "considerare "), ("convertir ", "convertire "),
    ("comparar ", "confrontare "), ("comprobar ", "verificare "),
    ("identificar ", "identificare "), ("realizar ", "realizzare "),
    ("elegir ", "scegliere "), ("revisar ", "verificare "),
    ("olvidar ", "dimenticare "), ("confundir ", "confondere "),
    ("ignorar ", "ignorare "), ("esprimere ", "esprimere "),
    ("instalar ", "installare "), ("asegurar ", "assicurare "),
    ("ajustar ", "regolare "), ("mostrar ", "mostrare "),
    ("permitir ", "permettere "), ("evitar ", "evitare "),
    # Nouns
    ("resultado ", "risultato "), ("resultados ", "risultati "),
    ("Resultado ", "Risultato "), ("Resultados ", "Risultati "),
    ("valor ", "valore "), ("Valor ", "Valore "),
    ("valores ", "valori "), ("Valores ", "Valori "),
    ("cantidad ", "quantita "), ("Cantidad ", "Quantita "),
    ("unidad ", "unita "), ("Unidad ", "Unita "),
    ("unidades ", "unita "), ("Unidades ", "Unita "),
    ("peso ", "peso "), ("Peso ", "Peso "),
    ("altura ", "altezza "), ("Altura ", "Altezza "),
    ("longitud ", "lunghezza "), ("Longitud ", "Lunghezza "),
    ("anchura ", "larghezza "), ("Anchura ", "Larghezza "),
    ("profundidad ", "profondita "), ("Profundidad ", "Profondita "),
    ("espesor ", "spessore "), ("Espesor ", "Spessore "),
    ("tiempo ", "tempo "), ("Tiempo ", "Tempo "),
    ("velocidad ", "velocita "), ("Velocidad ", "Velocita "),
    ("temperatura ", "temperatura "), ("Temperatura ", "Temperatura "),
    ("presion ", "pressione "), ("Presion ", "Pressione "),
    ("presi\u00f3n ", "pressione "), ("Presi\u00f3n ", "Pressione "),
    ("fuerza ", "forza "), ("Fuerza ", "Forza "),
    ("energia ", "energia "), ("Energia ", "Energia "),
    ("energ\u00eda ", "energia "), ("Energ\u00eda ", "Energia "),
    ("potencia ", "potenza "), ("Potencia ", "Potenza "),
    ("coste ", "costo "), ("Coste ", "Costo "),
    ("precio ", "prezzo "), ("Precio ", "Prezzo "),
    ("pago ", "pagamento "), ("Pago ", "Pagamento "),
    ("interes ", "interesse "), ("Interes ", "Interesse "),
    ("inter\u00e9s ", "interesse "), ("Inter\u00e9s ", "Interesse "),
    ("tasa ", "tasso "), ("Tasa ", "Tasso "),
    ("porcentaje ", "percentuale "), ("Porcentaje ", "Percentuale "),
    ("descuento ", "sconto "), ("Descuento ", "Sconto "),
    ("margen ", "margine "), ("Margen ", "Margine "),
    ("beneficio ", "profitto "), ("Beneficio ", "Profitto "),
    ("caloria ", "caloria "), ("Caloria ", "Caloria "),
    ("calorias ", "calorie "), ("Calorias ", "Calorie "),
    ("calor\u00eda ", "caloria "), ("Calor\u00eda ", "Caloria "),
    ("calor\u00edas ", "calorie "), ("Calor\u00edas ", "Calorie "),
    ("agua ", "acqua "), ("Agua ", "Acqua "),
    ("paso ", "passo "), ("Paso ", "Passo "),
    ("pasos ", "passi "), ("Pasos ", "Passi "),
    ("calculo ", "calcolo "), ("Calculo ", "Calcolo "),
    ("c\u00e1lculo ", "calcolo "), ("C\u00e1lculo ", "Calcolo "),
    ("formula ", "formula "), ("Formula ", "Formula "),
    ("f\u00f3rmula ", "formula "), ("F\u00f3rmula ", "Formula "),
    ("ecuacion ", "equazione "), ("Ecuacion ", "Equazione "),
    ("ecuaci\u00f3n ", "equazione "), ("Ecuaci\u00f3n ", "Equazione "),
    ("ejemplo ", "esempio "), ("Ejemplo ", "Esempio "),
    ("proyecto ", "progetto "), ("Proyecto ", "Progetto "),
    ("datos ", "dati "), ("Datos ", "Dati "),
    ("entrada ", "input "), ("Entrada ", "Input "),
    ("salida ", "output "), ("Salida ", "Output "),
    ("herramienta ", "strumento "), ("Herramienta ", "Strumento "),
    ("herramientas ", "strumenti "), ("Herramientas ", "Strumenti "),
    ("desperdicio ", "spreco "), ("Desperdicio ", "Spreco "),
    ("merma ", "perdita "), ("Merma ", "Perdita "),
    ("error ", "errore "), ("Error ", "Errore "),
    ("errores ", "errori "), ("Errores ", "Errori "),
    ("imprevisto ", "imprevisto "), ("Imprevisto ", "Imprevisto "),
    ("imprevistos ", "imprevisti "), ("Imprevistos ", "Imprevisti "),
    ("volumen ", "volume "), ("Volumen ", "Volume "),
    ("area ", "area "), ("Area ", "Area "),
    ("arena ", "sabbia "), ("Arena ", "Sabbia "),
    ("grava ", "ghiaia "), ("Grava ", "Ghiaia "),
    ("cemento ", "cemento "), ("Cemento ", "Cemento "),
    ("hormigon ", "calcestruzzo "), ("Hormigon ", "Calcestruzzo "),
    ("hormig\u00f3n ", "calcestruzzo "), ("Hormig\u00f3n ", "Calcestruzzo "),
    ("resistencia ", "resistenza "), ("Resistencia ", "Resistenza "),
    ("mezcla ", "miscela "), ("Mezcla ", "Miscela "),
    # Common words
    (" para ", " per "), (" como ", " come "),
    (" cuando ", " quando "), (" donde ", " dove "),
    (" necesario ", " necessario "), (" necesaria ", " necessaria "),
    (" necesarios ", " necessari "), (" necesarias ", " necessarie "),
    (" utilizando ", " utilizzando "), (" usando ", " usando "),
    (" basado ", " basato "), (" basada ", " basata "),
    (" incluyendo ", " includendo "), (" incluye ", " include "),
    (" incluyen ", " includono "),
    (" seg\u00fan ", " secondo "), (" segun ", " secondo "),
    # Quantities
    (" m\u00e1s ", " pi\u00f9 "), (" mas ", " pi\u00f9 "),
    (" menos ", " meno "), (" cada ", " ogni "),
    (" todo ", " tutto "), (" toda ", " tutta "),
    (" todos ", " tutti "), (" todas ", " tutte "),
    (" mismo ", " stesso "), (" misma ", " stessa "),
    (" otro ", " altro "), (" otra ", " altra "),
    (" otros ", " altri "), (" otras ", " altre "),
    (" m\u00ednimo ", " minimo "), (" minimo ", " minimo "),
    (" m\u00e1ximo ", " massimo "), (" maximo ", " massimo "),
    (" promedio ", " media "), (" total ", " totale "),
    (" actual ", " attuale "), (" inicial ", " iniziale "),
    (" final ", " finale "), (" siguiente ", " successivo "),
    # Time
    (" a\u00f1o ", " anno "), (" anos ", " anni "),
    (" a\u00f1os ", " anni "), (" mes ", " mese "),
    (" meses ", " mesi "), (" d\u00eda ", " giorno "),
    (" dias ", " giorni "), (" d\u00edas ", " giorni "),
    (" hora ", " ora "), (" horas ", " ore "),
    (" minuto ", " minuto "), (" minutos ", " minuti "),
    (" segundo ", " secondo "), (" segundos ", " secondi "),
    (" semana ", " settimana "), (" semanas ", " settimane "),
    # Adjectives
    (" correcto ", " corretto "), (" correcta ", " corretta "),
    (" importante ", " importante "), (" principal ", " principale "),
    (" grande ", " grande "), (" peque\u00f1o ", " piccolo "),
    (" pequeno ", " piccolo "), (" peque\u00f1a ", " piccola "),
    (" pequena ", " piccola "), (" nuevo ", " nuovo "),
    (" nueva ", " nuova "), (" nuevos ", " nuovi "),
    (" r\u00e1pido ", " veloce "), (" rapido ", " veloce "),
    (" lento ", " lento "), (" f\u00e1cil ", " facile "),
    (" facil ", " facile "), (" dif\u00edcil ", " difficile "),
    (" dificil ", " difficile "), (" mejor ", " migliore "),
    (" peor ", " peggiore "), (" mayor ", " maggiore "),
    (" menor ", " minore "), (" alto ", " alto "),
    (" bajo ", " basso "), (" baja ", " bassa "),
    (" gratis ", " gratuito "), (" gratuita ", " gratuita "),
    (" gratuito ", " gratuito "),
    # Units
    (" metro ", " metro "), (" metros ", " metri "),
    (" centimetro ", " centimetro "), (" centimetros ", " centimetri "),
    (" milimetro ", " millimetro "), (" milimetros ", " millimetri "),
    (" kilogramo ", " chilogrammo "), (" kilos ", " chili "),
    (" gramo ", " grammo "), (" gramos ", " grammi "),
    (" litro ", " litro "), (" litros ", " litri "),
    (" euro ", " euro "), (" euros ", " euro "),
    (" dolar ", " dollaro "), (" dolares ", " dollari "),
    # Common verb forms
    (" puede ", " pu\u00f2 "), (" pueden ", " possono "),
    (" debe ", " deve "), (" deben ", " devono "),
    (" tiene ", " ha "), (" tienen ", " hanno "),
    (" hay ", " c'\u00e8 "), (" hacer ", " fare "),
    (" este ", " questo "), (" esta ", " questa "),
    (" estos ", " questi "), (" estas ", " queste "),
    (" es ", " \u00e8 "), (" son ", " sono "),
    (" est\u00e1 ", " \u00e8 "), (" est\u00e1n ", " sono "),
    (" estan ", " sono "), (" entre ", " tra "),
    (" sobre ", " sopra "), (" despu\u00e9s ", " dopo "),
    (" despues ", " dopo "), (" antes ", " prima "),
    (" durante ", " durante "), (" siempre ", " sempre "),
    (" nunca ", " mai "), (" mucho ", " molto "),
    (" poco ", " poco "), (" muy ", " molto "),
    (" tambi\u00e9n ", " anche "), (" tambien ", " anche "),
    (" solo ", " solo "), (" requiere ", " richiede "),
    (" requieren ", " richiedono "),
    # Clean up "calcula" at start of steps
    ("Calcula ", "Calcola "), ("calcula ", "calcola "),
    ("Calculado ", "Calcolato "), ("calculado ", "calcolato "),
    ("Calculada ", "Calcolata "), ("calculada ", "calcolata "),
    (" usa ", " utilizza "), (" Usa ", " Utilizza "),
    (" introduce ", " inserisci "), (" Introduce ", " Inserisci "),
]

def apply(text):
    if not isinstance(text, str): return text
    for old, new in REPLS:
        text = text.replace(old, new)
    # Clean up double spaces
    import re
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def main():
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json": continue
        with open(fp, "r", encoding="utf-8-sig") as fh: calc = json.load(fh)
        it = calc.setdefault("i18n", {}).setdefault("it", {})
        es = calc.get("i18n", {}).get("es", {})
        if not es: continue
        changed = False
        
        for field in ["steps", "mistakes"]:
            es_val = es.get(field, [])
            if not es_val: continue
            if isinstance(es_val, list):
                it_new = [apply(str(s)) for s in es_val]
                if it.get(field) != it_new:
                    it[field] = it_new
                    changed = True
        
        for field in ["result_context", "example_label", "formula_display"]:
            es_val = es.get(field, "")
            if es_val and isinstance(es_val, str):
                it_new = apply(es_val)
                if it.get(field) != it_new:
                    it[field] = it_new
                    changed = True
        
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated} Italian files")

if __name__ == "__main__":
    main()

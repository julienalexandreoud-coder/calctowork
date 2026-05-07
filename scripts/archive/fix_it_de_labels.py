#!/usr/bin/env python3
"""Fix Italian and remaining German input labels."""

import json, os, glob

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

# Labels that are still matching Spanish across all languages
# Map common ES input labels → IT, FR, PT, EN translations
TRANSLATIONS = {
    "it": {
        "anio": "Anno", "anio1": "Anno 1", "anio2": "Anno 2",
        "mes": "Mese", "mes1": "Mese 1", "mes2": "Mese 2",
        "dia": "Giorno", "dia1": "Giorno 1", "dia2": "Giorno 2",
        "glucosa_mgdl": "Glucosio (mg/dL)",
        "hdl": "HDL", "ldl": "LDL",
        "peso_actual": "Peso attuale",
        "cintura_cm": "Vita (cm)", "cadera_cm": "Fianchi (cm)",
        "cuello": "Collo", "Cuello": "Collo",
        "objetivo": "Obiettivo", "Objetivo": "Obiettivo",
        "valor": "Valore",
        "porcentaje": "Percentuale",
        "proporcion": "Proporzione",
        "confianza": "Confidenza",
        "decimales": "Decimali",
        "dias_totales": "Giorni totali", "Dias Totales": "Giorni totali",
        "festivos": "Festivi", "Festivos": "Festivi",
        "distancia": "Distanza", "Distancia": "Distanza",
        "duracion_min": "Durata (min)", "Duracion Min": "Durata (min)",
        "tiempo_ejercicio": "Durata esercizio", "Tiempo Ejercicio": "Durata esercizio",
        "tiempo_min": "Tempo (min)", "Tiempo Min": "Tempo (min)",
        "gravedad": "Gravità",
        "velocidad": "Velocità",
        "precio_original": "Prezzo originale",
        "ahorro_mensual": "Risparmio mensile",
        "ahorro_meses": "Mesi di risparmio",
        "flujo_anual": "Flusso annuale", "Flujo Anual": "Flusso annuale",
        "inversion": "Investimento",
        "inversion_inicial": "Investimento iniziale", "Inversion Inicial": "Investimento iniziale",
        "deuda_total": "Debito totale",
        "monto": "Importo", "Monto": "Importo",
        "saldo": "Saldo", "balance": "Saldo", "Saldo": "Saldo",
        "tasa_impuesto": "Aliquota fiscale", "Tasa Impuesto": "Aliquota fiscale",
        "comision": "Commissione", "Comision": "Commissione",
        "costes_fijos": "Costi fissi", "Costes Fijos": "Costi fissi",
        "coste_variable": "Costo variabile", "Coste Variable": "Costo variabile",
        "precio_accion": "Prezzo azione", "Precio Accion": "Prezzo azione",
        "precio_compra": "Prezzo acquisto", "Precio Compra": "Prezzo acquisto",
        "dividendo_anual": "Dividendo annuale", "Dividendo Anual": "Dividendo annuale",
        "tipo_cambio": "Tasso cambio", "Tipo Cambio": "Tasso cambio",
        "rating": "Valutazione", "Rating": "Valutazione",
        "score": "Punteggio", "Score": "Punteggio",
        "slope": "Pendenza", "Slope": "Pendenza",
        "bitrate": "Bitrate", "Bitrate": "Bitrate",
        "base": "Base",
        "km": "km", "Km": "km",
        "litros": "Litri", "Litros": "Litri",
        "densidad": "Densità", "Densidad": "Densità",
        "potencia": "Potenza", "potencia": "Potenza",
        "inductancia": "Induttanza", "Inductancia": "Induttanza",
        "capacitancia": "Capacità",
        "resistencia": "Resistenza",
        "voltaje_entrada": "Tensione ingresso", "Voltaje Entrada": "Tensione ingresso",
        "voltaje": "Tensione", "Voltaje": "Tensione",
        "corriente": "Corrente",
        "frecuencia": "Frequenza", "frecuente": "Frequente", "Frecuente": "Frequente",
        "velocidad_sonido": "Velocità suono", "Velocidad Sonido": "Velocità suono",
        "velocidad_angular": "Velocità angolare", "Velocidad Angular": "Velocità angolare",
        "velocidad_avion": "Velocità aereo", "Velocidad Avion": "Velocità aereo",
        "velocidad_fuente": "Velocità sorgente", "Velocidad Fuente": "Velocità sorgente",
        "velocidad_ms": "Velocità (m/s)", "Velocidad Ms": "Velocità (m/s)",
        "volumen": "Volume", "Volumen": "Volume",
        "volumen_gas": "Volume gas", "Volumen Gas": "Volume gas",
        "volumen_inicial": "Volume iniziale", "Volumen Inicial": "Volume iniziale",
        "volumen_final": "Volume finale", "Volumen Final": "Volume finale",
        "volumen (m³)": "Volume (m³)",
        "masa_solvente": "Massa solvente", "Masa Solvente": "Massa solvente",
        "concentracion_inicial": "Concentrazione iniziale", "Concentracion Inicial": "Concentrazione iniziale",
        "concentracion_final": "Concentrazione finale", "Concentracion Final": "Concentrazione finale",
        "concentracion_h": "Concentrazione H⁺", "Concentracion H": "Concentrazione H⁺",
        "punto_rocio": "Punto rugiada", "Punto Rocio": "Punto rugiada",
        "presion_base": "Pressione base", "Presion Base": "Pressione base",
        "modulo_elastico": "Modulo elastico", "Modulo Elastico": "Modulo elastico",
        "momento_inercia": "Momento inerzia", "Momento Inercia": "Momento inerzia",
        "carga_extra": "Carico extra", "Carga Extra": "Carico extra",
        "carga_precarga": "Precarico", "Carga Precarga": "Precarico",
        "diametro_cilindro": "Diametro cilindro", "Diametro Cilindro": "Diametro cilindro",
        "numero_cilindros": "Numero cilindri", "Numero Cilindros": "Numero cilindri",
        "temperatura_f": "Temperatura (°F)", "Temperatura F": "Temperatura (°F)",
        "ejercicio_hrs": "Esercizio (ore)",
        "fc_reposo": "FC riposo",
        "met": "MET", "mets": "METs", "Met": "MET",
        "iso": "ISO", "ias": "IAS",
        "pm25": "PM2,5",
        "ph": "pH", "Ph": "pH",
        "tamano_muestra": "Dimensione campione",
        "lado_b": "Lato B", "lado_c": "Lato C",
        "banda1": "Banda 1", "banda2": "Banda 2", "banda3": "Banda 3",
        "Banda1": "Banda 1", "Banda2": "Banda 2", "Banda3": "Banda 3",
        "segmentos": "Segmenti",
        "a": "a", "b": "b", "n": "n", "r": "r", "R": "R",
        "a1": "A₁", "c1": "C₁", "c2": "C₂",
        "r1": "R₁", "r2": "R₂", "r3": "R₃",
        "d": "D", "V": "V",
        "v_f": "V LED", "V LED": "V LED",
        "i_f": "I LED", "I LED": "I LED",
    },
    "de": {
        # Remaining edge cases
        "frecuente": "Frequente Frequenz", "Frecuente": "Frequente Frequenz",
        "voltaje_entrada": "Eingangsspannung", "Voltaje Entrada": "Eingangsspannung",
        "volumen": "Volumen", "Volumen": "Volumen",
        "volumen (m³)": "Volumen (m³)",
        "r": "r", "R": "R",
    },
}


def main():
    files = sorted(
        f for f in glob.glob(os.path.join(CALC_DIR, "*.json"))
        if os.path.basename(f) not in ("calculators.json",)
        and "bak" not in f and "monolithic" not in f
    )

    updated = 0
    fixed_counts = {"de": 0, "it": 0}

    for fp in files:
        with open(fp, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)

        es_inputs = calc.get("i18n", {}).get("es", {}).get("inputs", {})
        changed = False

        for lang in ["de", "it"]:
            entry = calc.get("i18n", {}).get(lang, {})
            lang_inputs = entry.get("inputs", {})
            trans = TRANSLATIONS.get(lang, {})

            for inp_id, label in list(lang_inputs.items()):
                if not isinstance(label, str) or not label:
                    continue
                es_label = es_inputs.get(inp_id, "")
                if label != es_label:
                    continue

                if label in trans:
                    lang_inputs[inp_id] = trans[label]
                    changed = True
                    fixed_counts[lang] += 1
                else:
                    # Try case-insensitive match
                    label_upper = label.upper()
                    for tk, tv in trans.items():
                        if tk.upper() == label_upper:
                            lang_inputs[inp_id] = tv
                            changed = True
                            fixed_counts[lang] += 1
                            break

        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            updated += 1

    print(f"Fixed in {updated}/{len(files)} files:")
    print(f"  DE: {fixed_counts['de']} labels")
    print(f"  IT: {fixed_counts['it']} labels")


if __name__ == "__main__":
    main()

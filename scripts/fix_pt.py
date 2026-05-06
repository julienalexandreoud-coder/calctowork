# -*- coding: utf-8 -*-
"""Fix Portuguese content — replace Spanish-only words with Portuguese equivalents."""
import json, os, glob

CALC = r"C:\Microsaas\obra\src\calculators"

REPLS = [
    # Verbs (Spanish → Portuguese)
    ("Obtener", "Obter"), ("obtener", "obter"),
    ("Introducir", "Introduzir"), ("introducir", "introduzir"),
    ("Introduce", "Introduz"), ("introduce", "introduz"),
    # Nouns
    ("herramienta", "ferramenta"), ("herramientas", "ferramentas"),
    ("Herramienta", "Ferramenta"), ("Herramientas", "Ferramentas"),
    ("merma", "quebra"), ("Merma", "Quebra"),
    ("desperdicio", "desperdicio"), ("Desperdicio", "Desperdicio"),  # PT = desperdicio
    ("hormig\u00f3n", "bet\u00e3o"), ("hormigon", "betao"),
    ("Hormig\u00f3n", "Bet\u00e3o"), ("Hormigon", "Betao"),
    ("resultado", "resultado"), ("Resultado", "Resultado"),  # Same in PT
    ("resultados", "resultados"), ("Resultados", "Resultados"),
    # Adjectives
    ("necesario", "necess\u00e1rio"), ("necesaria", "necess\u00e1ria"),
    ("necesarios", "necess\u00e1rios"), ("necesarias", "necess\u00e1rias"),
    ("Necesario", "Necess\u00e1rio"), ("Necesaria", "Necess\u00e1ria"),
    ("insuficiente", "insuficiente"), ("Insuficiente", "Insuficiente"),  # Same
    ("excesivo", "excessivo"), ("excesiva", "excessiva"),
    ("adecuado", "adequado"), ("adecuada", "adequada"),
    ("Adecuado", "Adequado"), ("Adecuada", "Adequada"),
    # Common words
    (" donde ", " onde "), (" Donde ", " Onde "),
    ("gratis", "gr\u00e1tis"), ("Gratis", "Gr\u00e1tis"),
    ("gratuita", "gratuita"), ("Gratuita", "Gratuita"),  # Same in PT
    ("gratuito", "gratuito"), ("Gratuito", "Gratuito"),
    ("seg\u00fan", "segundo"), ("segun", "segundo"),
    ("Seg\u00fan", "Segundo"), ("Segun", "Segundo"),
    ("mediante", "mediante"),  # Same in PT
    # Verbs
    ("tiene ", "tem "), ("Tiene ", "Tem "),
    ("tienen ", "t\u00eam "), ("Tienen ", "T\u00eam "),
    ("puede ", "pode "), ("Puede ", "Pode "),
    ("pueden ", "podem "), ("Pueden ", "Podem "),
    (" debe ", " deve "), (" Debe ", " Deve "),
    (" deben ", " devem "), (" Deben ", " Devem "),
    ("est\u00e1n ", "est\u00e3o "), ("estan ", "estao "),
    ("Est\u00e1n ", "Est\u00e3o "), ("Estan ", "Estao "),
    ("mezcla ", "mistura "), ("Mezcla ", "Mistura "),
    ("requiere ", "requer "), ("Requiere ", "Requer "),
    ("requieren ", "requerem "), ("Requieren ", "Requerem "),
    # Imperial/metric
    ("metros", "metros"), ("Metros", "Metros"),  # Same
    ("litros", "litros"), ("Litros", "Litros"),
    ("kilos", "quilos"), ("Kilos", "Quilos"),
    ("euros", "euros"), ("Euros", "Euros"),  # Same
    ("d\u00f3lares", "d\u00f3lares"), ("dolares", "dolares"),
    ("D\u00f3lares", "D\u00f3lares"), ("Dolares", "Dolares"),
    # Time
    ("a\u00f1o", "ano"), ("a\u00f1os", "anos"),
    ("A\u00f1o", "Ano"), ("A\u00f1os", "Anos"),
    ("d\u00eda ", "dia "), ("d\u00edas ", "dias "),
    ("D\u00eda ", "Dia "), ("D\u00edas ", "Dias "),
    # Misc
    ("calcula", "calcula"), ("Calcula", "Calcula"),  # Same in PT
    ("calcular", "calcular"), ("Calcular", "Calcular"),
    ("calculado", "calculado"), ("calculada", "calculada"),
    ("Calculado", "Calculado"), ("Calculada", "Calculada"),
    ("Multiplicar", "Multiplicar"),  # Same
    ("Determinar", "Determinar"),  # Same
    # Spanish-only items
    ("espesor ", "espessura "), ("Espesor ", "Espessura "),
    ("anchura ", "largura "), ("Anchura ", "Largura "),  
]

# Also input label translations
INPUT_TRANS = {
    # Common Spanish input labels → Portuguese
    "Largo": "Comprimento", "largo": "comprimento",
    "Ancho": "Largura", "ancho": "largura",
    "Alto": "Altura", "alto": "altura",  
    "Altura": "Altura", "altura": "altura",  # Same
    "Longitud": "Comprimento", "longitud": "comprimento",
    "Anchura": "Largura", "anchura": "largura",
    "Profundidad": "Profundidade", "profundidad": "profundidade",
    "Diametro": "Di\u00e2metro", "diametro": "di\u00e2metro",
    "Radio": "Raio", "radio": "raio",
    "Perimetro": "Per\u00edmetro", "perimetro": "per\u00edmetro",
    "Volumen": "Volume", "volumen": "volume",
    "Peso": "Peso", "peso": "peso",  # Same
    "Masa": "Massa", "masa": "massa",
    "Densidad": "Densidade", "densidad": "densidade",
    "Temperatura": "Temperatura", "temperatura": "temperatura",  # Same
    "Presion": "Press\u00e3o", "presion": "press\u00e3o",
    "Presi\u00f3n": "Press\u00e3o", "presi\u00f3n": "press\u00e3o",
    "Fuerza": "For\u00e7a", "fuerza": "for\u00e7a",
    "Potencia": "Pot\u00eancia", "potencia": "pot\u00eancia",
    "Energia": "Energia", "energia": "energia",  # Same
    "Energ\u00eda": "Energia", "energ\u00eda": "energia",
    "Velocidad": "Velocidade", "velocidad": "velocidade",
    "Aceleracion": "Acelera\u00e7\u00e3o", "aceleracion": "acelera\u00e7\u00e3o",
    "Aceleraci\u00f3n": "Acelera\u00e7\u00e3o", "aceleraci\u00f3n": "acelera\u00e7\u00e3o",
    "Tiempo": "Tempo", "tiempo": "tempo",
    "Distancia": "Dist\u00e2ncia", "distancia": "dist\u00e2ncia",
    "Cantidad": "Quantidade", "cantidad": "quantidade",
    "Numero": "N\u00famero", "numero": "n\u00famero",
    "N\u00famero": "N\u00famero", "n\u00famero": "n\u00famero",
    "Unidades": "Unidades", "unidades": "unidades",  # Same
    "Porcentaje": "Percentagem", "porcentaje": "percentagem",
    "Tasa": "Taxa", "tasa": "taxa",
    "Interes": "Juros", "interes": "juros",
    "Inter\u00e9s": "Juros", "inter\u00e9s": "juros",
    "Coste": "Custo", "coste": "custo",
    "Precio": "Pre\u00e7o", "precio": "pre\u00e7o",
    "Valor": "Valor", "valor": "valor",  # Same
    "Descuento": "Desconto", "descuento": "desconto",
    "Margen": "Margem", "margen": "margem",
    "Beneficio": "Lucro", "beneficio": "lucro",
    "Consumo": "Consumo", "consumo": "consumo",
    "Caudal": "Vaz\u00e3o", "caudal": "vaz\u00e3o",
    "Voltaje": "Tens\u00e3o", "voltaje": "tens\u00e3o",
    "Corriente": "Corrente", "corriente": "corrente",
    "Resistencia": "Resist\u00eancia", "resistencia": "resist\u00eancia",
    "Frecuencia": "Frequ\u00eancia", "frecuencia": "frequ\u00eancia",
    "Capacidad": "Capacidade", "capacidad": "capacidade",
    "Inductancia": "Indut\u00e2ncia", "inductancia": "indut\u00e2ncia",
    "Impedancia": "Imped\u00e2ncia", "impedancia": "imped\u00e2ncia",
    "Horas": "Horas", "horas": "horas",  # Same
    "Minutos": "Minutos", "minutos": "minutos",  # Same
    "Segundos": "Segundos", "segundos": "segundos",  # Same
    "Dias": "Dias", "dias": "dias",  # Same
    "Semanas": "Semanas", "semanas": "semanas",  # Same
    "Meses": "Meses", "meses": "meses",  # Same
    "A\u00f1os": "Anos", "a\u00f1os": "anos",
    "Anos": "Anos", "anos": "anos",
    "Litros": "Litros", "litros": "litros",  # Same
    "Metros": "Metros", "metros": "metros",  # Same
    "Kilos": "Quilos", "kilos": "quilos",
    "Gramos": "Gramas", "gramos": "gramas",
    # Output labels
    "Arena": "Areia", "arena": "areia",
    "Grava": "Brita", "grava": "brita",
    "Cemento": "Cimento", "cemento": "cimento",
    "Sacos": "Sacos", "sacos": "sacos",  # Same
    "arena_m3": "areia_m3",
    "grava_m3": "brita_m3",
    "cemento_sacos": "cimento_sacos",
    "acero_kg": "a\u00e7o_kg",
    "excavacion": "escava\u00e7\u00e3o",
    "volumen": "volume",
}

def apply_repls(text):
    if not isinstance(text, str): return text
    for old, new in REPLS:
        text = text.replace(old, new)
    return text

def main():
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json": continue
        with open(fp, "r", encoding="utf-8-sig") as fh: calc = json.load(fh)
        pt = calc.setdefault("i18n", {}).setdefault("pt", {})
        es = calc.get("i18n", {}).get("es", {})
        if not es: continue
        changed = False
        
        # Fix narrative fields
        for field in ["steps", "mistakes"]:
            val = pt.get(field, [])
            if isinstance(val, list):
                new = [apply_repls(str(s)) for s in val]
                if new != val: pt[field] = new; changed = True
        
        for field in ["result_context", "example_label", "formula_display"]:
            val = pt.get(field, "")
            if isinstance(val, str) and val:
                new = apply_repls(val)
                if new != val: pt[field] = new; changed = True
        
        # Fix input/output labels matching ES
        for io_field in ["inputs", "outputs"]:
            pt_io = pt.get(io_field, {})
            es_io = es.get(io_field, {})
            for k, v in list(pt_io.items()):
                if isinstance(v, str) and v == es_io.get(k, "") and v:
                    if v in INPUT_TRANS:
                        pt_io[k] = INPUT_TRANS[v]
                        changed = True
                    else:
                        new_v = apply_repls(v)
                        if new_v != v:
                            pt_io[k] = new_v
                            changed = True
        
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated} files")

if __name__ == "__main__":
    main()

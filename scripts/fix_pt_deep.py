# -*- coding: utf-8 -*-
"""Deep Portuguese fix — thorough Spanish→Portuguese narrative translation."""
import json, os, glob, re

CALC = r"C:\Microsaas\obra\src\calculators"

TRANS = [
    # Articles
    (r'\bEl\s+(\w+)', r'O \1'), (r'\bLa\s+(\w+)', r'A \1'),
    (r'\bLos\s+(\w+)', r'Os \1'), (r'\bLas\s+(\w+)', r'As \1'),
    (r'\bdel\s+(\w+)', r'do \1'), (r'\bde\s+la\s+(\w+)', r'da \1'),
    (r'\bde\s+los\s+(\w+)', r'dos \1'), (r'\bde\s+las\s+(\w+)', r'das \1'),
    (r'\bal\s+(\w+)', r'ao \1'), (r'\ben\s+el\s+(\w+)', r'no \1'),
    (r'\ben\s+la\s+(\w+)', r'na \1'),
    # Verbs
    (r'\bMultiplicar\b', r'Multiplicar'), (r'\bCalcular\b', r'Calcular'),
    (r'\bDeterminar\b', r'Determinar'), (r'\bIntroducir\b', r'Introduzir'),
    (r'\bObtener\b', r'Obter'), (r'\bVerificar\b', r'Verificar'),
    (r'\bUsar\b', r'Usar'), (r'\bIngresar\b', r'Inserir'),
    (r'\bMedir\b', r'Medir'), (r'\bSumar\b', r'Somar'),
    (r'\bDividir\b', r'Dividir'), (r'\bRestar\b', r'Subtrair'),
    (r'\bAplicar\b', r'Aplicar'), (r'\bSeleccionar\b', r'Selecionar'),
    (r'\bConsiderar\b', r'Considerar'), (r'\bConvertir\b', r'Converter'),
    (r'\bComparar\b', r'Comparar'), (r'\bComprobar\b', r'Verificar'),
    (r'\bIdentificar\b', r'Identificar'), (r'\bRealizar\b', r'Realizar'),
    (r'\bElegir\b', r'Escolher'), (r'\bRevisar\b', r'Verificar'),
    (r'\bOlvidar\b', r'Esquecer'), (r'\bConfundir\b', r'Confundir'),
    (r'\bAsumir\b', r'Assumir'), (r'\bIgnorar\b', r'Ignorar'),
    (r'\bExpresar\b', r'Expressar'), (r'\bNormalizar\b', r'Normalizar'),
    (r'\bInstalar\b', r'Instalar'), (r'\bAsegurar\b', r'Assegurar'),
    (r'\bAjustar\b', r'Ajustar'), (r'\bColocar\b', r'Colocar'),
    (r'\bGuardar\b', r'Guardar'), (r'\bMostrar\b', r'Mostrar'),
    (r'\bPermitir\b', r'Permitir'), (r'\bEvitar\b', r'Evitar'),
    (r'\bIncluir\b', r'Incluir'), (r'\bRedondear\b', r'Arredondar'),
    # Nouns
    (r'\bresultado\b', r'resultado'), (r'\bresultados\b', r'resultados'),
    (r'\bvalor\b', r'valor'), (r'\bvalores\b', r'valores'),
    (r'\bcantidad\b', r'quantidade'), (r'\bunidad\b', r'unidade'),
    (r'\bunidades\b', r'unidades'), (r'\bpeso\b', r'peso'),
    (r'\baltura\b', r'altura'), (r'\blongitud\b', r'comprimento'),
    (r'\banchura\b', r'largura'), (r'\bprofundidad\b', r'profundidade'),
    (r'\bespesor\b', r'espessura'), (r'\btiempo\b', r'tempo'),
    (r'\bvelocidad\b', r'velocidade'), (r'\btemperatura\b', r'temperatura'),
    (r'\bpresi\u00f3n\b', r'press\u00e3o'), (r'\bpresion\b', r'pressao'),
    (r'\bfuerza\b', r'for\u00e7a'), (r'\benerg\u00eda\b', r'energia'),
    (r'\benergia\b', r'energia'), (r'\bpotencia\b', r'pot\u00eancia'),
    (r'\bcoste\b', r'custo'), (r'\bprecio\b', r'pre\u00e7o'),
    (r'\bpago\b', r'pagamento'), (r'\binter\u00e9s\b', r'juros'),
    (r'\binteres\b', r'juros'), (r'\btasa\b', r'taxa'),
    (r'\bporcentaje\b', r'percentagem'), (r'\bdescuento\b', r'desconto'),
    (r'\bmargen\b', r'margem'), (r'\bbeneficio\b', r'lucro'),
    (r'\bcalor\u00eda\b', r'caloria'), (r'\bcaloria\b', r'caloria'),
    (r'\bcalor\u00edas\b', r'calorias'), (r'\bcalorias\b', r'calorias'),
    (r'\bagua\b', r'\u00e1gua'), (r'\bpaso\b', r'passo'),
    (r'\bpasos\b', r'passos'), (r'\bc\u00e1lculo\b', r'c\u00e1lculo'),
    (r'\bcalculo\b', r'calculo'), (r'\bf\u00f3rmula\b', r'f\u00f3rmula'),
    (r'\bformula\b', r'formula'), (r'\becuaci\u00f3n\b', r'equa\u00e7\u00e3o'),
    (r'\becuacion\b', r'equacao'), (r'\bejemplo\b', r'exemplo'),
    (r'\bproyecto\b', r'projeto'), (r'\bdatos\b', r'dados'),
    (r'\bentrada\b', r'entrada'), (r'\bsalida\b', r'sa\u00edda'),
    (r'\bherramienta\b', r'ferramenta'), (r'\bherramientas\b', r'ferramentas'),
    (r'\bdesperdicio\b', r'desperd\u00edcio'), (r'\bmerma\b', r'quebra'),
    (r'\berror\b', r'erro'), (r'\berrores\b', r'erros'),
    (r'\bimprevisto\b', r'imprevisto'), (r'\bimprevistos\b', r'imprevistos'),
    (r'\bvolumen\b', r'volume'), (r'\b\u00e1rea\b', r'\u00e1rea'),
    (r'\barea\b', r'\u00e1rea'), (r'\barena\b', r'areia'),
    (r'\bgrava\b', r'brita'), (r'\bcemento\b', r'cimento'),
    (r'\bhormig\u00f3n\b', r'bet\u00e3o'), (r'\bhormigon\b', r'betao'),
    (r'\bresistencia\b', r'resist\u00eancia'), (r'\bmezcla\b', r'mistura'),
    # Common words
    (r'\bpara\b', r'para'), (r'\bcomo\b', r'como'),
    (r'\bcuando\b', r'quando'), (r'\bdonde\b', r'onde'),
    (r'\bnecesario\b', r'necess\u00e1rio'), (r'\bnecesaria\b', r'necess\u00e1ria'),
    (r'\bnecesarios\b', r'necess\u00e1rios'), (r'\bnecesarias\b', r'necess\u00e1rias'),
    (r'\butilizando\b', r'utilizando'), (r'\busando\b', r'usando'),
    (r'\bbasado\b', r'baseado'), (r'\bbasada\b', r'baseada'),
    (r'\bincluyendo\b', r'incluindo'), (r'\bincluye\b', r'inclui'),
    (r'\bincluyen\b', r'incluem'),
    (r'\bseg\u00fan\b', r'segundo'), (r'\bsegun\b', r'segundo'),
    # Quantities
    (r'\bm\u00e1s\b', r'mais'), (r'\bmas\b', r'mais'),
    (r'\bmenos\b', r'menos'), (r'\bcada\b', r'cada'),
    (r'\btodo\b', r'todo'), (r'\btoda\b', r'toda'),
    (r'\btodos\b', r'todos'), (r'\btodas\b', r'todas'),
    (r'\bmismo\b', r'mesmo'), (r'\bmisma\b', r'mesma'),
    (r'\botro\b', r'outro'), (r'\botra\b', r'outra'),
    (r'\botros\b', r'outros'), (r'\botras\b', r'outras'),
    (r'\bm\u00ednimo\b', r'm\u00ednimo'), (r'\bminimo\b', r'minimo'),
    (r'\bm\u00e1ximo\b', r'm\u00e1ximo'), (r'\bmaximo\b', r'maximo'),
    (r'\bpromedio\b', r'm\u00e9dia'), (r'\btotal\b', r'total'),
    (r'\bactual\b', r'atual'), (r'\binicial\b', r'inicial'),
    (r'\bfinal\b', r'final'), (r'\bsiguiente\b', r'seguinte'),
    # Time
    (r'\ba\u00f1o\b', r'ano'), (r'\bano\b', r'ano'),
    (r'\ba\u00f1os\b', r'anos'), (r'\banos\b', r'anos'),
    (r'\bmes\b', r'm\u00eas'), (r'\bmeses\b', r'meses'),
    (r'\bd\u00eda\b', r'dia'), (r'\bdia\b', r'dia'),
    (r'\bd\u00edas\b', r'dias'), (r'\bdias\b', r'dias'),
    (r'\bhora\b', r'hora'), (r'\bhoras\b', r'horas'),
    (r'\bminuto\b', r'minuto'), (r'\bminutos\b', r'minutos'),
    (r'\bsegundo\b', r'segundo'), (r'\bsegundos\b', r'segundos'),
    (r'\bsemana\b', r'semana'), (r'\bsemanas\b', r'semanas'),
    # Adjectives
    (r'\bcorrecto\b', r'correto'), (r'\bcorrecta\b', r'correta'),
    (r'\bimportante\b', r'importante'), (r'\bprincipal\b', r'principal'),
    (r'\bgrande\b', r'grande'), (r'\bpeque\u00f1o\b', r'pequeno'),
    (r'\bpequeno\b', r'pequeno'), (r'\bpeque\u00f1a\b', r'pequena'),
    (r'\bpequena\b', r'pequena'), (r'\bnuevo\b', r'novo'),
    (r'\bnueva\b', r'nova'), (r'\bnuevos\b', r'novos'),
    (r'\br\u00e1pido\b', r'r\u00e1pido'), (r'\brapido\b', r'rapido'),
    (r'\blento\b', r'lento'), (r'\bf\u00e1cil\b', r'f\u00e1cil'),
    (r'\bfacil\b', r'facil'), (r'\bdif\u00edcil\b', r'dif\u00edcil'),
    (r'\bdificil\b', r'dificil'), (r'\bmejor\b', r'melhor'),
    (r'\bpeor\b', r'pior'), (r'\bmayor\b', r'maior'),
    (r'\bmenor\b', r'menor'), (r'\balto\b', r'alto'),
    (r'\bbajo\b', r'baixo'), (r'\bbaja\b', r'baixa'),
    (r'\bgratis\b', r'gr\u00e1tis'), (r'\bgratuita\b', r'gratuita'),
    (r'\bgratuito\b', r'gratuito'),
    # Units
    (r'\bmetro\b', r'metro'), (r'\bmetros\b', r'metros'),
    (r'\bcentimetro\b', r'cent\u00edmetro'), (r'\bcentimetros\b', r'cent\u00edmetros'),
    (r'\bmilimetro\b', r'mil\u00edmetro'), (r'\bmilimetros\b', r'mil\u00edmetros'),
    (r'\bkilogramo\b', r'quilograma'), (r'\bkilos\b', r'quilos'),
    (r'\bgramo\b', r'grama'), (r'\bgramos\b', r'gramas'),
    (r'\blitro\b', r'litro'), (r'\blitros\b', r'litros'),
    (r'\beuro\b', r'euro'), (r'\beuros\b', r'euros'),
    (r'\bdolar\b', r'd\u00f3lar'), (r'\bdolares\b', r'd\u00f3lares'),
    (r'\bd\u00f3lar\b', r'd\u00f3lar'), (r'\bd\u00f3lares\b', r'd\u00f3lares'),
    # Common verbs
    (r'\bpuede\b', r'pode'), (r'\bpueden\b', r'podem'),
    (r'\bdebe\b', r'deve'), (r'\bdeben\b', r'devem'),
    (r'\btiene\b', r'tem'), (r'\btienen\b', r't\u00eam'),
    (r'\bhay\b', r'h\u00e1'), (r'\bhacer\b', r'fazer'),
    (r'\beste\b', r'este'), (r'\besta\b', r'esta'),
    (r'\bestos\b', r'estes'), (r'\bestas\b', r'estas'),
    (r'\bes\b', r'\u00e9'), (r'\bson\b', r's\u00e3o'),
    (r'\best\u00e1\b', r'est\u00e1'), (r'\best\u00e1n\b', r'est\u00e3o'),
    (r'\bestan\b', r'estao'), (r'\bentre\b', r'entre'),
    (r'\bsobre\b', r'sobre'), (r'\bdespu\u00e9s\b', r'depois'),
    (r'\bdespues\b', r'depois'), (r'\bantes\b', r'antes'),
    (r'\bdurante\b', r'durante'), (r'\bsiempre\b', r'sempre'),
    (r'\bnunca\b', r'nunca'), (r'\bmucho\b', r'muito'),
    (r'\bpoco\b', r'pouco'), (r'\bmuy\b', r'muito'),
    (r'\btambi\u00e9n\b', r'tamb\u00e9m'), (r'\btambien\b', r'tambem'),
    (r'\bsolo\b', r'somente'), (r'\brequiere\b', r'requer'),
    (r'\brequieren\b', r'requerem'),
    # Clean up
    (r'\s+', r' '),
]

def translate(text):
    if not isinstance(text, str): return text
    result = text
    for pattern, replacement in TRANS:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    result = re.sub(r'\s+', ' ', result).strip()
    if result and result[0].islower():
        result = result[0].upper() + result[1:]
    return result

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
        
        for field in ["steps", "mistakes"]:
            es_val = es.get(field, [])
            if not es_val: continue
            if isinstance(es_val, list):
                pt_new = [translate(str(s)) for s in es_val]
                if pt.get(field) != pt_new:
                    pt[field] = pt_new
                    changed = True
        
        for field in ["result_context", "example_label", "formula_display"]:
            es_val = es.get(field, "")
            if es_val and isinstance(es_val, str):
                pt_new = translate(es_val)
                if pt.get(field) != pt_new:
                    pt[field] = pt_new
                    changed = True
        
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated} files")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate unique English narrative from Spanish source content for remaining calculators."""
import json, os, glob, re

CALC = r"C:\Microsaas\obra\src\calculators"
LANGS = ["es","en","fr","pt","de","it"]

# Spanish -> English patterns for common calculator phrases
TRANS = [
    # Article/noun patterns
    (r'\bEl\s+(\w+)', r'The \1'), (r'\bLa\s+(\w+)', r'The \1'),
    (r'\bLos\s+(\w+)', r'The \1'), (r'\bLas\s+(\w+)', r'The \1'),
    (r'\bdel\s+(\w+)', r'of the \1'), (r'\bde\s+la\s+(\w+)', r'of the \1'),
    (r'\bde\s+los\s+(\w+)', r'of the \1'), (r'\bde\s+las\s+(\w+)', r'of the \1'),
    (r'\bal\s+(\w+)', r'to the \1'), (r'\ben\s+el\s+(\w+)', r'in the \1'),
    # Verbs
    (r'\bMultiplicar\b', r'Multiply'), (r'\bmultiplicar\b', r'multiply'),
    (r'\bMultiplica\b', r'Multiply'), (r'\bmultiplica\b', r'multiply'),
    (r'\bCalcular\b', r'Calculate'), (r'\bcalcular\b', r'calculate'),
    (r'\bCalcula\b', r'Calculate'), (r'\bcalcula\b', r'calculate'),
    (r'\bDeterminar\b', r'Determine'), (r'\bdeterminar\b', r'determine'),
    (r'\bIntroducir\b', r'Enter'), (r'\bintroducir\b', r'enter'),
    (r'\bIntroduce\b', r'Enter'), (r'\bintroduce\b', r'enter'),
    (r'\bObtener\b', r'Obtain'), (r'\bobtener\b', r'obtain'),
    (r'\bObtiene\b', r'Obtain'), (r'\bobtiene\b', r'obtain'),
    (r'\bVerificar\b', r'Verify'), (r'\bverificar\b', r'verify'),
    (r'\bVerifica\b', r'Verify'), (r'\bverifica\b', r'verify'),
    (r'\bUsar\b', r'Use'), (r'\busar\b', r'use'),
    (r'\bUsa\b', r'Use'), (r'\busa\b', r'use'),
    (r'\bIngresar\b', r'Enter'), (r'\bingresar\b', r'enter'),
    (r'\bMedir\b', r'Measure'), (r'\bmedir\b', r'measure'),
    (r'\bSumar\b', r'Add'), (r'\bsumar\b', r'add'),
    (r'\bDividir\b', r'Divide'), (r'\bdividir\b', r'divide'),
    (r'\bRestar\b', r'Subtract'), (r'\brestar\b', r'subtract'),
    (r'\bAplicar\b', r'Apply'), (r'\baplicar\b', r'apply'),
    (r'\bSeleccionar\b', r'Select'), (r'\bseleccionar\b', r'select'),
    (r'\bSelecciona\b', r'Select'), (r'\bselecciona\b', r'select'),
    (r'\bAñadir\b', r'Add'), (r'\bConsiderar\b', r'Consider'),
    (r'\bConvertir\b', r'Convert'), (r'\bconvertir\b', r'convert'),
    (r'\bComparar\b', r'Compare'), (r'\bcomparar\b', r'compare'),
    (r'\bComprobar\b', r'Check'), (r'\bcomprobar\b', r'check'),
    (r'\bAsegurar\b', r'Ensure'), (r'\bIdentificar\b', r'Identify'),
    # Nouns
    (r'\bárea\b', r'area'), (r'\bÁrea\b', r'Area'),
    (r'\bvolumen\b', r'volume'), (r'\bVolumen\b', r'Volume'),
    (r'\bresultado\b', r'result'), (r'\bResultado\b', r'Result'),
    (r'\bresultados\b', r'results'), (r'\bResultados\b', r'Results'),
    (r'\bvalor\b', r'value'), (r'\bValor\b', r'Value'),
    (r'\bvalores\b', r'values'), (r'\bValores\b', r'Values'),
    (r'\bcantidad\b', r'quantity'), (r'\bCantidad\b', r'Quantity'),
    (r'\bunidad\b', r'unit'), (r'\bUnidad\b', r'Unit'),
    (r'\bunidades\b', r'units'), (r'\bUnidades\b', r'Units'),
    (r'\bpeso\b', r'weight'), (r'\bPeso\b', r'Weight'),
    (r'\baltura\b', r'height'), (r'\bAltura\b', r'Height'),
    (r'\blongitud\b', r'length'), (r'\bLongitud\b', r'Length'),
    (r'\banchura\b', r'width'), (r'\bAnchura\b', r'Width'),
    (r'\bprofundidad\b', r'depth'), (r'\bProfundidad\b', r'Depth'),
    (r'\bespesor\b', r'thickness'), (r'\bEspesor\b', r'Thickness'),
    (r'\btiempo\b', r'time'), (r'\bTiempo\b', r'Time'),
    (r'\bvelocidad\b', r'speed'), (r'\bVelocidad\b', r'Speed'),
    (r'\btemperatura\b', r'temperature'), (r'\bTemperatura\b', r'Temperature'),
    (r'\bpresión\b', r'pressure'), (r'\bPresión\b', r'Pressure'),
    (r'\bpresion\b', r'pressure'), (r'\bPresion\b', r'Pressure'),
    (r'\bfuerza\b', r'force'), (r'\bFuerza\b', r'Force'),
    (r'\benergía\b', r'energy'), (r'\bEnergía\b', r'Energy'),
    (r'\benergia\b', r'energy'), (r'\bEnergia\b', r'Energy'),
    (r'\bpotencia\b', r'power'), (r'\bPotencia\b', r'Power'),
    (r'\bcoste\b', r'cost'), (r'\bCoste\b', r'Cost'),
    (r'\bprecio\b', r'price'), (r'\bPrecio\b', r'Price'),
    (r'\bdinero\b', r'money'), (r'\bDinero\b', r'Money'),
    (r'\bpago\b', r'payment'), (r'\bPago\b', r'Payment'),
    (r'\binterés\b', r'interest'), (r'\bInterés\b', r'Interest'),
    (r'\binteres\b', r'interest'), (r'\bInteres\b', r'Interest'),
    (r'\btasa\b', r'rate'), (r'\bTasa\b', r'Rate'),
    (r'\bporcentaje\b', r'percentage'), (r'\bPorcentaje\b', r'Percentage'),
    (r'\bdescuento\b', r'discount'), (r'\bDescuento\b', r'Discount'),
    (r'\bmargen\b', r'margin'), (r'\bMargen\b', r'Margin'),
    (r'\bbeneficio\b', r'profit'), (r'\bBeneficio\b', r'Profit'),
    (r'\bcaloría\b', r'calorie'), (r'\bCaloría\b', r'Calorie'),
    (r'\bcaloria\b', r'calorie'), (r'\bCaloria\b', r'Calorie'),
    (r'\bcalorías\b', r'calories'), (r'\bCalorías\b', r'Calories'),
    (r'\bcalorias\b', r'calories'), (r'\bCalorias\b', r'Calories'),
    (r'\bagua\b', r'water'), (r'\bAgua\b', r'Water'),
    (r'\bpaso\b', r'step'), (r'\bPaso\b', r'Step'),
    (r'\bpasos\b', r'steps'), (r'\bPasos\b', r'Steps'),
    (r'\bcálculo\b', r'calculation'), (r'\bCálculo\b', r'Calculation'),
    (r'\bcalculo\b', r'calculation'), (r'\bCalculo\b', r'Calculation'),
    # Common words
    (r'\bpara\b', r'to'), (r'\bcomo\b', r'as'), (r'\bcuando\b', r'when'),
    (r'\bdonde\b', r'where'), (r'\bsegún\b', r'according to'),
    (r'\bnecesario\b', r'necessary'), (r'\bnecesaria\b', r'necessary'),
    (r'\butilizando\b', r'using'), (r'\busando\b', r'using'),
    (r'\bbasado\b', r'based'), (r'\bbasada\b', r'based'),
    (r'\bincluyendo\b', r'including'), (r'\bincluye\b', r'includes'),
    (r'\bsegún\s+(\w+)', r'according to \1'),
    # Quantities
    (r'\bmás\b', r'more'), (r'\bmenos\b', r'less'),
    (r'\bcada\b', r'each'), (r'\btodo\b', r'all'),
    (r'\bmismo\b', r'same'), (r'\botro\b', r'other'),
    (r'\bmínimo\b', r'minimum'), (r'\bmáximo\b', r'maximum'),
    (r'\bpromedio\b', r'average'), (r'\btotal\b', r'total'),
    (r'\bactual\b', r'current'), (r'\binicial\b', r'initial'),
    (r'\bfinal\b', r'final'), (r'\bsiguiente\b', r'following'),
    # Time
    (r'\baño\b', r'year'), (r'\baños\b', r'years'), (r'\banos\b', r'years'),
    (r'\bmes\b', r'month'), (r'\bmeses\b', r'months'),
    (r'\bdía\b', r'day'), (r'\bdías\b', r'days'), (r'\bdias\b', r'days'),
    (r'\bhora\b', r'hour'), (r'\bhoras\b', r'hours'),
    (r'\bminuto\b', r'minute'), (r'\bminutos\b', r'minutes'),
    (r'\bsegundo\b', r'second'), (r'\bsegundos\b', r'seconds'),
    (r'\bsemana\b', r'week'), (r'\bsemanas\b', r'weeks'),
    # Common adjectives
    (r'\bcorrecto\b', r'correct'), (r'\bcorrecta\b', r'correct'),
    (r'\bimportante\b', r'important'), (r'\bprincipal\b', r'main'),
    (r'\bgrande\b', r'large'), (r'\bpequeño\b', r'small'), (r'\bpequeno\b', r'small'),
    (r'\bnuevo\b', r'new'), (r'\bnueva\b', r'new'),
    (r'\brápido\b', r'fast'), (r'\blento\b', r'slow'),
    (r'\bfácil\b', r'easy'), (r'\bdifícil\b', r'difficult'),
    (r'\bmejor\b', r'best'), (r'\bpeor\b', r'worst'),
    (r'\bmayor\b', r'greater'), (r'\bmenor\b', r'lesser'),
    (r'\balto\b', r'high'), (r'\bbajo\b', r'low'),
    (r'\bgratis\b', r'free'), (r'\bgratuita\b', r'free'), (r'\bgratuito\b', r'free'),
    # Misc
    (r'\bherramienta\b', r'tool'), (r'\bherramientas\b', r'tools'),
    (r'\bproyecto\b', r'project'), (r'\bproyectos\b', r'projects'),
    (r'\bdatos\b', r'data'), (r'\bentrada\b', r'input'), (r'\bsalida\b', r'output'),
    (r'\bejemplo\b', r'example'), (r'\bfórmula\b', r'formula'), (r'\bformula\b', r'formula'),
    (r'\becuación\b', r'equation'), (r'\becuacion\b', r'equation'),
    (r'\bfunción\b', r'function'), (r'\bfuncion\b', r'function'),
    (r'\bmetro\b', r'meter'), (r'\bmetros\b', r'meters'),
    (r'\bcentímetro\b', r'centimeter'), (r'\bcentimetros\b', r'centimeters'),
    (r'\bmilímetro\b', r'millimeter'), (r'\bmilimetros\b', r'millimeters'),
    (r'\bkilogramo\b', r'kilogram'), (r'\bkilos\b', r'kilos'),
    (r'\bgramo\b', r'gram'), (r'\bgramos\b', r'grams'),
    (r'\blitro\b', r'liter'), (r'\blitros\b', r'liters'),
    (r'\beuro\b', r'eur'), (r'\beuros\b', r'eur'),
    (r'\bdólar\b', r'dollar'), (r'\bdólares\b', r'dollars'),
    (r'\bdolar\b', r'dollar'), (r'\bdolares\b', r'dollars'),
    (r'\bdesperdicio\b', r'waste'), (r'\bmerma\b', r'waste'),
    (r'\bimprevisto\b', r'unexpected'), (r'\bimprevistos\b', r'unexpected events'),
    (r'\berror\b', r'error'), (r'\berrores\b', r'errors'),
    # Cleaning up artifacts
    (r'\s+', r' '), (r'\s+\.', r'.'), (r'\.\s+\.', r'.'),
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
        en = calc.setdefault("i18n", {}).setdefault("en", {})
        es = calc.get("i18n", {}).get("es", {})
        if not es: continue
        changed = False
        
        for field in ["steps", "mistakes"]:
            es_val = es.get(field, [])
            en_val = en.get(field, [])
            if not es_val: continue
            if isinstance(es_val, list) and es_val:
                en_new = [translate(str(s)) for s in es_val]
                if en_new != en_val:
                    en[field] = en_new
                    changed = True
        
        for field in ["result_context", "example_label", "formula_display"]:
            es_val = es.get(field, "")
            en_val = en.get(field, "")
            if es_val and isinstance(es_val, str):
                en_new = translate(es_val)
                if en_new != en_val:
                    en[field] = en_new
                    changed = True
        
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated} files from Spanish source")

if __name__ == "__main__":
    main()

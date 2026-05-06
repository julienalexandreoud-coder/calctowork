#!/usr/bin/env python3
"""Fix all French narrative — translate Spanish source to proper French."""
import json, os, glob, re

CALC = r"C:\Microsaas\obra\src\calculators"

TRANS = [
    # Articles
    (r'\bEl\s+(\w+)', r'Le \1'), (r'\bLa\s+(\w+)', r'La \1'),
    (r'\bLos\s+(\w+)', r'Les \1'), (r'\bLas\s+(\w+)', r'Les \1'),
    (r'\bdel\s+(\w+)', r'du \1'), (r'\bde\s+la\s+(\w+)', r'de la \1'),
    (r'\bde\s+los\s+(\w+)', r'des \1'), (r'\bde\s+las\s+(\w+)', r'des \1'),
    (r'\bal\s+(\w+)', r'au \1'), (r'\ben\s+el\s+(\w+)', r'dans le \1'),
    (r'\bdel\b', r'du'),
    # Verbs
    (r'\bMultiplicar\b', r'Multiplier'), (r'\bmultiplicar\b', r'multiplier'),
    (r'\bMultiplica\b', r'Multiplier'), (r'\bmultiplica\b', r'multiplier'),
    (r'\bCalcular\b', r'Calculer'), (r'\bcalcular\b', r'calculer'),
    (r'\bCalcula\b', r'Calculer'), (r'\bcalcula\b', r'calculer'),
    (r'\bDeterminar\b', r'Déterminer'), (r'\bdéterminer\b', r'déterminer'),
    (r'\bIntroducir\b', r'Saisir'), (r'\bintroducir\b', r'saisir'),
    (r'\bIntroduce\b', r'Saisir'), (r'\bintroduce\b', r'saisir'),
    (r'\bObtener\b', r'Obtenir'), (r'\bobtener\b', r'obtenir'),
    (r'\bObtiene\b', r'Obtenir'), (r'\bobtiene\b', r'obtenir'),
    (r'\bVerificar\b', r'Vérifier'), (r'\bverificar\b', r'vérifier'),
    (r'\bVerifica\b', r'Vérifier'), (r'\bverifica\b', r'vérifier'),
    (r'\bUsar\b', r'Utiliser'), (r'\busar\b', r'utiliser'),
    (r'\bUsa\b', r'Utiliser'), (r'\busa\b', r'utiliser'),
    (r'\bIngresar\b', r'Saisir'), (r'\bingresar\b', r'saisir'),
    (r'\bMedir\b', r'Mesurer'), (r'\bmedir\b', r'mesurer'),
    (r'\bSumar\b', r'Additionner'), (r'\bsumar\b', r'additionner'),
    (r'\bDividir\b', r'Diviser'), (r'\bdividir\b', r'diviser'),
    (r'\bRestar\b', r'Soustraire'), (r'\brestar\b', r'soustraire'),
    (r'\bAplicar\b', r'Appliquer'), (r'\baplicar\b', r'appliquer'),
    (r'\bSeleccionar\b', r'Sélectionner'), (r'\bsélectionner\b', r'sélectionner'),
    (r'\bSelecciona\b', r'Sélectionner'), (r'\bsélectionne\b', r'sélectionner'),
    (r'\bAñadir\b', r'Ajouter'), (r'\bConsiderar\b', r'Considérer'),
    (r'\bConvertir\b', r'Convertir'), (r'\bconvertir\b', r'convertir'),
    (r'\bComparar\b', r'Comparer'), (r'\bcomparar\b', r'comparer'),
    (r'\bComprobar\b', r'Vérifier'), (r'\bcomprobar\b', r'vérifier'),
    (r'\bAsegurar\b', r'Assurer'), (r'\bIdentificar\b', r'Identifier'),
    (r'\bElegir\b', r'Choisir'), (r'\belegir\b', r'choisir'),
    (r'\bRevisar\b', r'Vérifier'), (r'\brevisar\b', r'vérifier'),
    (r'\bPresionar\b', r'Appuyer'), (r'\bRegistrar\b', r'Enregistrer'),
    # Nouns
    (r'\bárea\b', r'surface'), (r'\bÁrea\b', r'Surface'),
    (r'\bvolumen\b', r'volume'), (r'\bVolumen\b', r'Volume'),
    (r'\bresultado\b', r'résultat'), (r'\bResultado\b', r'Résultat'),
    (r'\bresultados\b', r'résultats'), (r'\bResultados\b', r'Résultats'),
    (r'\bvalor\b', r'valeur'), (r'\bValor\b', r'Valeur'),
    (r'\bvalores\b', r'valeurs'), (r'\bValores\b', r'Valeurs'),
    (r'\bcantidad\b', r'quantité'), (r'\bCantidad\b', r'Quantité'),
    (r'\bunidad\b', r'unité'), (r'\bUnidad\b', r'Unité'),
    (r'\bunidades\b', r'unités'), (r'\bUnidades\b', r'Unités'),
    (r'\bpeso\b', r'poids'), (r'\bPeso\b', r'Poids'),
    (r'\baltura\b', r'hauteur'), (r'\bAltura\b', r'Hauteur'),
    (r'\blongitud\b', r'longueur'), (r'\bLongitud\b', r'Longueur'),
    (r'\banchura\b', r'largeur'), (r'\bAnchura\b', r'Largeur'),
    (r'\bprofundidad\b', r'profondeur'), (r'\bProfundidad\b', r'Profondeur'),
    (r'\bespesor\b', r'épaisseur'), (r'\bEspesor\b', r'Épaisseur'),
    (r'\btiempo\b', r'temps'), (r'\bTiempo\b', r'Temps'),
    (r'\bvelocidad\b', r'vitesse'), (r'\bVelocidad\b', r'Vitesse'),
    (r'\btemperatura\b', r'température'), (r'\bTemperatura\b', r'Température'),
    (r'\bpresión\b', r'pression'), (r'\bPresión\b', r'Pression'),
    (r'\bpresion\b', r'pression'), (r'\bPresion\b', r'Pression'),
    (r'\bfuerza\b', r'force'), (r'\bFuerza\b', r'Force'),
    (r'\benergía\b', r'énergie'), (r'\bEnergía\b', r'Énergie'),
    (r'\benergia\b', r'énergie'), (r'\bEnergia\b', r'Énergie'),
    (r'\bpotencia\b', r'puissance'), (r'\bPotencia\b', r'Puissance'),
    (r'\bcoste\b', r'coût'), (r'\bCoste\b', r'Coût'),
    (r'\bprecio\b', r'prix'), (r'\bPrecio\b', r'Prix'),
    (r'\bdinero\b', r'argent'), (r'\bDinero\b', r'Argent'),
    (r'\bpago\b', r'paiement'), (r'\bPago\b', r'Paiement'),
    (r'\binterés\b', r'intérêt'), (r'\bInterés\b', r'Intérêt'),
    (r'\binteres\b', r'intérêt'), (r'\bInteres\b', r'Intérêt'),
    (r'\btasa\b', r'taux'), (r'\bTasa\b', r'Taux'),
    (r'\bporcentaje\b', r'pourcentage'), (r'\bPorcentaje\b', r'Pourcentage'),
    (r'\bdescuento\b', r'remise'), (r'\bDescuento\b', r'Remise'),
    (r'\bmargen\b', r'marge'), (r'\bMargen\b', r'Marge'),
    (r'\bbeneficio\b', r'bénéfice'), (r'\bBeneficio\b', r'Bénéfice'),
    (r'\bcaloría\b', r'calorie'), (r'\bCaloría\b', r'Calorie'),
    (r'\bcaloria\b', r'calorie'), (r'\bCaloria\b', r'Calorie'),
    (r'\bcalorías\b', r'calories'), (r'\bCalorías\b', r'Calories'),
    (r'\bcalorias\b', r'calories'), (r'\bCalorias\b', r'Calories'),
    (r'\bagua\b', r'eau'), (r'\bAgua\b', r'Eau'),
    (r'\bpaso\b', r'étape'), (r'\bPaso\b', r'Étape'),
    (r'\bpasos\b', r'étapes'), (r'\bPasos\b', r'Étapes'),
    (r'\bcálculo\b', r'calcul'), (r'\bCálculo\b', r'Calcul'),
    (r'\bcalculo\b', r'calcul'), (r'\bCalculo\b', r'Calcul'),
    # Common words
    (r'\bpara\b', r'pour'), (r'\bcomo\b', r'comme'), (r'\bcuando\b', r'quand'),
    (r'\bdonde\b', r'où'), (r'\bsegún\b', r'selon'),
    (r'\bnecesario\b', r'nécessaire'), (r'\bnecesaria\b', r'nécessaire'),
    (r'\butilizando\b', r'en utilisant'), (r'\busando\b', r'en utilisant'),
    (r'\bbasado\b', r'basé'), (r'\bbasada\b', r'basée'),
    (r'\bincluyendo\b', r'incluant'), (r'\bincluye\b', r'inclut'),
    (r'\bsegún\s+(\w+)', r'selon \1'),
    # Quantities
    (r'\bmás\b', r'plus'), (r'\bmás\s+de\b', r'plus de'),
    (r'\bmenos\b', r'moins'), (r'\bcada\b', r'chaque'),
    (r'\btodo\b', r'tout'), (r'\btoda\b', r'toute'),
    (r'\btodos\b', r'tous'), (r'\btodas\b', r'toutes'),
    (r'\bmismo\b', r'même'), (r'\botro\b', r'autre'),
    (r'\botra\b', r'autre'),
    (r'\bmínimo\b', r'minimum'), (r'\bmáximo\b', r'maximum'),
    (r'\bpromedio\b', r'moyenne'), (r'\btotal\b', r'total'),
    (r'\bactual\b', r'actuel'), (r'\binicial\b', r'initial'),
    (r'\bfinal\b', r'final'), (r'\bsiguiente\b', r'suivant'),
    # Time
    (r'\baño\b', r'an'), (r'\baños\b', r'ans'), (r'\banos\b', r'ans'),
    (r'\bmes\b', r'mois'), (r'\bmeses\b', r'mois'),
    (r'\bdía\b', r'jour'), (r'\bdías\b', r'jours'), (r'\bdias\b', r'jours'),
    (r'\bhora\b', r'heure'), (r'\bhoras\b', r'heures'),
    (r'\bminuto\b', r'minute'), (r'\bminutos\b', r'minutes'),
    (r'\bsegundo\b', r'seconde'), (r'\bsegundos\b', r'secondes'),
    (r'\bsemana\b', r'semaine'), (r'\bsemanas\b', r'semaines'),
    # Adjectives
    (r'\bcorrecto\b', r'correct'), (r'\bcorrecta\b', r'correcte'),
    (r'\bimportante\b', r'important'), (r'\bprincipal\b', r'principal'),
    (r'\bgrande\b', r'grand'), (r'\bpequeño\b', r'petit'), (r'\bpequeno\b', r'petit'),
    (r'\bpequeña\b', r'petite'), (r'\bpequena\b', r'petite'),
    (r'\bnuevo\b', r'nouveau'), (r'\bnueva\b', r'nouvelle'),
    (r'\bnuevos\b', r'nouveaux'), (r'\bnuevas\b', r'nouvelles'),
    (r'\brápido\b', r'rapide'), (r'\blento\b', r'lent'),
    (r'\bfácil\b', r'facile'), (r'\bdifícil\b', r'difficile'),
    (r'\bmejor\b', r'meilleur'), (r'\bpeor\b', r'pire'),
    (r'\bmayor\b', r'plus grand'), (r'\bmenor\b', r'plus petit'),
    (r'\balto\b', r'haut'), (r'\bbajo\b', r'bas'),
    (r'\bbaja\b', r'basse'),
    (r'\bgratis\b', r'gratuit'), (r'\bgratuita\b', r'gratuite'), (r'\bgratuito\b', r'gratuit'),
    # Misc
    (r'\bherramienta\b', r'outil'), (r'\bherramientas\b', r'outils'),
    (r'\bproyecto\b', r'projet'), (r'\bproyectos\b', r'projets'),
    (r'\bdatos\b', r'données'), (r'\bentrada\b', r'entrée'), (r'\bsalida\b', r'sortie'),
    (r'\bejemplo\b', r'exemple'), (r'\bfórmula\b', r'formule'), (r'\bformula\b', r'formule'),
    (r'\becuación\b', r'équation'), (r'\becuacion\b', r'équation'),
    (r'\bfunción\b', r'fonction'), (r'\bfuncion\b', r'fonction'),
    (r'\bmetro\b', r'mètre'), (r'\bmetros\b', r'mètres'),
    (r'\bcentímetro\b', r'centimètre'), (r'\bcentimetros\b', r'centimètres'),
    (r'\bmilímetro\b', r'millimètre'), (r'\bmilimetros\b', r'millimètres'),
    (r'\bkilogramo\b', r'kilogramme'), (r'\bkilos\b', r'kilos'),
    (r'\bgramo\b', r'gramme'), (r'\bgramos\b', r'grammes'),
    (r'\blitro\b', r'litre'), (r'\blitros\b', r'litres'),
    (r'\beuro\b', r'euro'), (r'\beuros\b', r'euros'),
    (r'\bdólar\b', r'dollar'), (r'\bdólares\b', r'dollars'),
    (r'\bdolar\b', r'dollar'), (r'\bdolares\b', r'dollars'),
    (r'\bdesperdicio\b', r'gaspillage'), (r'\bmerma\b', r'perte'),
    (r'\bimprevisto\b', r'imprévu'), (r'\bimprevistos\b', r'imprévus'),
    (r'\berror\b', r'erreur'), (r'\berrores\b', r'erreurs'),
    (r'\bpuede\b', r'peut'), (r'\bpueden\b', r'peuvent'),
    (r'\bdebe\b', r'doit'), (r'\bdeben\b', r'doivent'),
    (r'\btiene\b', r'a'), (r'\btienen\b', r'ont'),
    (r'\bhay\b', r'il y a'), (r'\bhacer\b', r'faire'),
    (r'\bestá\b', r'est'), (r'\bestán\b', r'sont'),
    (r'\bson\b', r'sont'), (r'\bentre\b', r'entre'),
    (r'\bsobre\b', r'sur'), (r'\bbajo\s+el\b', r'sous le'),
    (r'\bdurante\b', r'pendant'), (r'\bdespués\b', r'après'),
    (r'\bantes\b', r'avant'), (r'\bahora\b', r'maintenant'),
    # Clean up
    (r'\s+', r' '), (r'\s+\.', r'.'),
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
        fr = calc.setdefault("i18n", {}).setdefault("fr", {})
        es = calc.get("i18n", {}).get("es", {})
        if not es: continue
        changed = False
        
        for field in ["steps", "mistakes"]:
            es_val = es.get(field, [])
            fr_val = fr.get(field, [])
            if not es_val: continue
            if isinstance(es_val, list) and es_val:
                fr_new = [translate(str(s)) for s in es_val]
                if fr_new != fr_val:
                    fr[field] = fr_new
                    changed = True
        
        for field in ["result_context", "example_label", "formula_display"]:
            es_val = es.get(field, "")
            fr_val = fr.get(field, "")
            if es_val and isinstance(es_val, str):
                fr_new = translate(es_val)
                if fr_new != fr_val:
                    fr[field] = fr_new
                    changed = True
        
        # Also fix input labels matching ES
        fr_in = fr.get("inputs", {})
        es_in = es.get("inputs", {})
        fr_out = fr.get("outputs", {})
        es_out = es.get("outputs", {})
        for k, v in list(fr_in.items()):
            if isinstance(v, str) and v == es_in.get(k, "") and v:
                fr_in[k] = translate(v)
                changed = True
        for k, v in list(fr_out.items()):
            if isinstance(v, str) and v == es_out.get(k, "") and v:
                fr_out[k] = translate(v)
                changed = True
        
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated} files from Spanish source to French")

if __name__ == "__main__":
    main()

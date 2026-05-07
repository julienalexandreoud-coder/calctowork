# -*- coding: utf-8 -*-
"""Regenerate ALL French narrative from Spanish source — comprehensive translation."""
import json, os, glob, re

CALC = r"C:\Microsaas\obra\src\calculators"

TRANS = [
    # Articles
    (r'\bEl\s+(\w+)', r'Le \1'), (r'\bLa\s+(\w+)', r'La \1'),
    (r'\bLos\s+(\w+)', r'Les \1'), (r'\bLas\s+(\w+)', r'Les \1'),
    (r'\bdel\s+(\w+)', r'du \1'), (r'\bde la (\w+)', r'de la \1'),
    (r'\bde los (\w+)', r'des \1'), (r'\bde las (\w+)', r'des \1'),
    (r'\bal (\w+)', r'au \1'), (r'\ben el (\w+)', r'dans le \1'),
    (r'\bun (\w+)', r'un \1'), (r'\buna (\w+)', r'une \1'),
    (r'\bunos (\w+)', r'des \1'), (r'\bunas (\w+)', r'des \1'),
    # Verbs
    (r'\bMultiplicar\b', r'Multiplier'), (r'\bCalcular\b', r'Calculer'),
    (r'\bDeterminar\b', r'Determiner'), (r'\bIntroducir\b', r'Saisir'),
    (r'\bObtener\b', r'Obtenir'), (r'\bVerificar\b', r'Verifier'),
    (r'\bUsar\b', r'Utiliser'), (r'\bIngresar\b', r'Saisir'),
    (r'\bMedir\b', r'Mesurer'), (r'\bSumar\b', r'Additionner'),
    (r'\bDividir\b', r'Diviser'), (r'\bRestar\b', r'Soustraire'),
    (r'\bAplicar\b', r'Appliquer'), (r'\bSeleccionar\b', r'Selectionner'),
    (r'\bConsiderar\b', r'Considerer'), (r'\bConvertir\b', r'Convertir'),
    (r'\bComparar\b', r'Comparer'), (r'\bComprobar\b', r'Verifier'),
    (r'\bIdentificar\b', r'Identifier'), (r'\bRealizar\b', r'Realiser'),
    (r'\bElegir\b', r'Choisir'), (r'\bRevisar\b', r'Verifier'),
    (r'\bRegistrar\b', r'Enregistrer'), (r'\bPresionar\b', r'Appuyer'),
    (r'\bOlvidar\b', r'Oublier'), (r'\bConfundir\b', r'Confondre'),
    (r'\bAsumir\b', r'Supposer'), (r'\bIgnorar\b', r'Ignorer'),
    (r'\bExpresar\b', r'Exprimer'), (r'\bNormalizar\b', r'Normaliser'),
    (r'\bInstalar\b', r'Installer'), (r'\bAsegurar\b', r'Assurer'),
    (r'\bAjustar\b', r'Ajuster'), (r'\bColocar\b', r'Placer'),
    (r'\bGuardar\b', r'Enregistrer'), (r'\bBuscar\b', r'Chercher'),
    (r'\bMostrar\b', r'Afficher'), (r'\bPermitir\b', r'Permettre'),
    (r'\bEvitar\b', r'Eviter'), (r'\bIncluir\b', r'Inclure'),
    (r'\bRedondear\b', r'Arrondir'), (r'\bSustituir\b', r'Remplacer'),
    (r'\bcalcular\b', r'calculer'), (r'\bcalcula\b', r'calcule'),
    (r'\bintroduce\b', r'saisissez'), (r'\bintroducir\b', r'saisir'),
    (r'\bobtener\b', r'obtenir'), (r'\bobtiene\b', r'obtient'),
    (r'\busar\b', r'utiliser'), (r'\busa\b', r'utilise'),
    (r'\bmedir\b', r'mesurer'), (r'\baplicar\b', r'appliquer'),
    (r'\bverificar\b', r'verifier'), (r'\bcomparar\b', r'comparer'),
    (r'\bconvertir\b', r'convertir'), (r'\bidentificar\b', r'identifier'),
    (r'\brealizar\b', r'realiser'), (r'\bseleccionar\b', r'selectionner'),
    (r'\belegir\b', r'choisir'), (r'\bignorar\b', r'ignorer'),
    (r'\bconfundir\b', r'confondre'), (r'\bolvidar\b', r'oublier'),
    (r'\basumir\b', r'supposer'), (r'\binyectar\b', r'injecter'),
    # Nouns
    (r'\bresultado\b', r'resultat'), (r'\bresultados\b', r'resultats'),
    (r'\bResultado\b', r'Resultat'), (r'\bResultados\b', r'Resultats'),
    (r'\bvalor\b', r'valeur'), (r'\bValor\b', r'Valeur'),
    (r'\bvalores\b', r'valeurs'), (r'\bValores\b', r'Valeurs'),
    (r'\bcantidad\b', r'quantite'), (r'\bCantidad\b', r'Quantite'),
    (r'\bunidad\b', r'unite'), (r'\bUnidad\b', r'Unite'),
    (r'\bunidades\b', r'unites'), (r'\bUnidades\b', r'Unites'),
    (r'\bpeso\b', r'poids'), (r'\bPeso\b', r'Poids'),
    (r'\baltura\b', r'hauteur'), (r'\bAltura\b', r'Hauteur'),
    (r'\blongitud\b', r'longueur'), (r'\bLongitud\b', r'Longueur'),
    (r'\banchura\b', r'largeur'), (r'\bAnchura\b', r'Largeur'),
    (r'\bprofundidad\b', r'profondeur'), (r'\bProfundidad\b', r'Profondeur'),
    (r'\bespesor\b', r'epaisseur'), (r'\bEspesor\b', r'Epaisseur'),
    (r'\btiempo\b', r'temps'), (r'\bTiempo\b', r'Temps'),
    (r'\bvelocidad\b', r'vitesse'), (r'\bVelocidad\b', r'Vitesse'),
    (r'\btemperatura\b', r'temperature'), (r'\bTemperatura\b', r'Temperature'),
    (r'\bpresion\b', r'pression'), (r'\bPresion\b', r'Pression'),
    (r'\bpresi\u00f3n\b', r'pression'), (r'\bPresi\u00f3n\b', r'Pression'),
    (r'\bfuerza\b', r'force'), (r'\bFuerza\b', r'Force'),
    (r'\benergia\b', r'energie'), (r'\bEnergia\b', r'Energie'),
    (r'\benerg\u00eda\b', r'energie'), (r'\bEnerg\u00eda\b', r'Energie'),
    (r'\bpotencia\b', r'puissance'), (r'\bPotencia\b', r'Puissance'),
    (r'\bcoste\b', r'cout'), (r'\bCoste\b', r'Cout'),
    (r'\bprecio\b', r'prix'), (r'\bPrecio\b', r'Prix'),
    (r'\bpago\b', r'paiement'), (r'\bPago\b', r'Paiement'),
    (r'\binteres\b', r'interet'), (r'\bInteres\b', r'Interet'),
    (r'\binter\u00e9s\b', r'interet'), (r'\bInter\u00e9s\b', r'Interet'),
    (r'\btasa\b', r'taux'), (r'\bTasa\b', r'Taux'),
    (r'\bporcentaje\b', r'pourcentage'), (r'\bPorcentaje\b', r'Pourcentage'),
    (r'\bdescuento\b', r'remise'), (r'\bDescuento\b', r'Remise'),
    (r'\bmargen\b', r'marge'), (r'\bMargen\b', r'Marge'),
    (r'\bbeneficio\b', r'benefice'), (r'\bBeneficio\b', r'Benefice'),
    (r'\bcaloria\b', r'calorie'), (r'\bCaloria\b', r'Calorie'),
    (r'\bcalorias\b', r'calories'), (r'\bCalorias\b', r'Calories'),
    (r'\bcalor\u00eda\b', r'calorie'), (r'\bCalor\u00eda\b', r'Calorie'),
    (r'\bcalor\u00edas\b', r'calories'), (r'\bCalor\u00edas\b', r'Calories'),
    (r'\bagua\b', r'eau'), (r'\bAgua\b', r'Eau'),
    (r'\bpaso\b', r'etape'), (r'\bPaso\b', r'Etape'),
    (r'\bpasos\b', r'etapes'), (r'\bPasos\b', r'Etapes'),
    (r'\bcalculo\b', r'calcul'), (r'\bCalculo\b', r'Calcul'),
    (r'\bc\u00e1lculo\b', r'calcul'), (r'\bC\u00e1lculo\b', r'Calcul'),
    (r'\bformula\b', r'formule'), (r'\bFormula\b', r'Formule'),
    (r'\bf\u00f3rmula\b', r'formule'), (r'\bF\u00f3rmula\b', r'Formule'),
    (r'\becuacion\b', r'equation'), (r'\bEcuacion\b', r'Equation'),
    (r'\becuaci\u00f3n\b', r'equation'), (r'\bEcuaci\u00f3n\b', r'Equation'),
    (r'\bejemplo\b', r'exemple'), (r'\bEjemplo\b', r'Exemple'),
    (r'\bproyecto\b', r'projet'), (r'\bProyecto\b', r'Projet'),
    (r'\bdatos\b', r'donnees'), (r'\bDatos\b', r'Donnees'),
    (r'\bentrada\b', r'entree'), (r'\bEntrada\b', r'Entree'),
    (r'\bsalida\b', r'sortie'), (r'\bSalida\b', r'Sortie'),
    (r'\bherramienta\b', r'outil'), (r'\bHerramienta\b', r'Outil'),
    (r'\bherramientas\b', r'outils'), (r'\bHerramientas\b', r'Outils'),
    (r'\bdesperdicio\b', r'gaspillage'), (r'\bDesperdicio\b', r'Gaspillage'),
    (r'\bmerma\b', r'perte'), (r'\bMerma\b', r'Perte'),
    (r'\berror\b', r'erreur'), (r'\bError\b', r'Erreur'),
    (r'\berrores\b', r'erreurs'), (r'\bErrores\b', r'Erreurs'),
    (r'\bimprevisto\b', r'imprevu'), (r'\bImprevisto\b', r'Imprevu'),
    (r'\bimprevistos\b', r'imprevus'), (r'\bImprevistos\b', r'Imprevus'),
    (r'\bvolumen\b', r'volume'), (r'\bVolumen\b', r'Volume'),
    (r'\b\u00e1rea\b', r'surface'), (r'\b\u00c1rea\b', r'Surface'),
    (r'\barea\b', r'surface'), (r'\bArea\b', r'Surface'),
    # Common words
    (r'\bpara\b', r'pour'), (r'\bcomo\b', r'comme'),
    (r'\bcuando\b', r'quand'), (r'\bdonde\b', r'ou'),
    (r'\bnecesario\b', r'necessaire'), (r'\bnecesaria\b', r'necessaire'),
    (r'\bnecesarios\b', r'necessaires'), (r'\bnecesarias\b', r'necessaires'),
    (r'\butilizando\b', r'en utilisant'), (r'\busando\b', r'en utilisant'),
    (r'\bbasado\b', r'base'), (r'\bbasada\b', r'basee'),
    (r'\bincluyendo\b', r'incluant'), (r'\bincluye\b', r'inclut'),
    (r'\bincluyen\b', r'incluent'),
    (r'\bseg\u00fan\b', r'selon'), (r'\bsegun\b', r'selon'),
    # Quantities
    (r'\bm\u00e1s\b', r'plus'), (r'\bmas\b', r'plus'),
    (r'\bmenos\b', r'moins'), (r'\bcada\b', r'chaque'),
    (r'\btodo\b', r'tout'), (r'\btoda\b', r'toute'),
    (r'\btodos\b', r'tous'), (r'\btodas\b', r'toutes'),
    (r'\bmismo\b', r'meme'), (r'\bmisma\b', r'meme'),
    (r'\botro\b', r'autre'), (r'\botra\b', r'autre'),
    (r'\botros\b', r'autres'), (r'\botras\b', r'autres'),
    (r'\bm\u00ednimo\b', r'minimum'), (r'\bminimo\b', r'minimum'),
    (r'\bm\u00e1ximo\b', r'maximum'), (r'\bmaximo\b', r'maximum'),
    (r'\bpromedio\b', r'moyenne'), (r'\bPromedio\b', r'Moyenne'),
    (r'\btotal\b', r'total'), (r'\bTotal\b', r'Total'),
    (r'\bactual\b', r'actuel'), (r'\bActual\b', r'Actuel'),
    (r'\binicial\b', r'initial'), (r'\bInicial\b', r'Initial'),
    (r'\bfinal\b', r'final'), (r'\bFinal\b', r'Final'),
    (r'\bsiguiente\b', r'suivant'), (r'\bSiguiente\b', r'Suivant'),
    # Time
    (r'\ba\u00f1o\b', r'an'), (r'\bano\b', r'an'),
    (r'\ba\u00f1os\b', r'ans'), (r'\banos\b', r'ans'),
    (r'\bmes\b', r'mois'), (r'\bmeses\b', r'mois'),
    (r'\bd\u00eda\b', r'jour'), (r'\bdia\b', r'jour'),
    (r'\bd\u00edas\b', r'jours'), (r'\bdias\b', r'jours'),
    (r'\bhora\b', r'heure'), (r'\bhoras\b', r'heures'),
    (r'\bminuto\b', r'minute'), (r'\bminutos\b', r'minutes'),
    (r'\bsegundo\b', r'seconde'), (r'\bsegundos\b', r'secondes'),
    (r'\bsemana\b', r'semaine'), (r'\bsemanas\b', r'semaines'),
    # Adjectives
    (r'\bcorrecto\b', r'correct'), (r'\bcorrecta\b', r'correcte'),
    (r'\bimportante\b', r'important'), (r'\bprincipal\b', r'principal'),
    (r'\bgrande\b', r'grand'), (r'\bpeque\u00f1o\b', r'petit'),
    (r'\bpequeno\b', r'petit'), (r'\bpeque\u00f1a\b', r'petite'),
    (r'\bpequena\b', r'petite'), (r'\bnuevo\b', r'nouveau'),
    (r'\bnueva\b', r'nouvelle'), (r'\bnuevos\b', r'nouveaux'),
    (r'\br\u00e1pido\b', r'rapide'), (r'\brapido\b', r'rapide'),
    (r'\blento\b', r'lent'), (r'\bf\u00e1cil\b', r'facile'),
    (r'\bfacil\b', r'facile'), (r'\bdif\u00edcil\b', r'difficile'),
    (r'\bdificil\b', r'difficile'), (r'\bmejor\b', r'meilleur'),
    (r'\bpeor\b', r'pire'), (r'\bmayor\b', r'plus grand'),
    (r'\bmenor\b', r'plus petit'), (r'\balto\b', r'haut'),
    (r'\bbajo\b', r'bas'), (r'\bbaja\b', r'basse'),
    (r'\bgratis\b', r'gratuit'), (r'\bgratuita\b', r'gratuite'),
    (r'\bgratuito\b', r'gratuit'),
    # Units
    (r'\bmetro\b', r'metre'), (r'\bmetros\b', r'metres'),
    (r'\bcentimetro\b', r'centimetre'), (r'\bcentimetros\b', r'centimetres'),
    (r'\bmilimetro\b', r'millimetre'), (r'\bmilimetros\b', r'millimetres'),
    (r'\bkilogramo\b', r'kilogramme'), (r'\bkilos\b', r'kilos'),
    (r'\bgramo\b', r'gramme'), (r'\bgramos\b', r'grammes'),
    (r'\blitro\b', r'litre'), (r'\blitros\b', r'litres'),
    (r'\beuro\b', r'euro'), (r'\beuros\b', r'euros'),
    (r'\bdolar\b', r'dollar'), (r'\bdolares\b', r'dollars'),
    (r'\bd\u00f3lar\b', r'dollar'), (r'\bd\u00f3lares\b', r'dollars'),
    # Common verbs
    (r'\bpuede\b', r'peut'), (r'\bpueden\b', r'peuvent'),
    (r'\bdebe\b', r'doit'), (r'\bdeben\b', r'doivent'),
    (r'\btiene\b', r'a'), (r'\btienen\b', r'ont'),
    (r'\bhay\b', r'il y a'), (r'\bhacer\b', r'faire'),
    (r'\beste\b', r'ce'), (r'\besta\b', r'cette'),
    (r'\bestos\b', r'ces'), (r'\bestas\b', r'ces'),
    (r'\bes\b', r'est'), (r'\bson\b', r'sont'),
    (r'\best\u00e1\b', r'est'), (r'\besta\b', r'cette'),
    (r'\best\u00e1n\b', r'sont'), (r'\bestan\b', r'sont'),
    (r'\bentre\b', r'entre'), (r'\bsobre\b', r'sur'),
    (r'\bdespu\u00e9s\b', r'apres'), (r'\bdespues\b', r'apres'),
    (r'\bantes\b', r'avant'), (r'\bdurante\b', r'pendant'),
    (r'\bsiempre\b', r'toujours'), (r'\bnunca\b', r'jamais'),
    (r'\bmucho\b', r'beaucoup'), (r'\bpoco\b', r'peu'),
    (r'\bmuy\b', r'tres'), (r'\btambi\u00e9n\b', r'aussi'),
    (r'\btambien\b', r'aussi'), (r'\bsolo\b', r'seulement'),
    # Clean up
    (r'\s+', r' '),
]

def translate(text):
    if not isinstance(text, str): return text
    result = text
    for pattern, replacement in TRANS:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    result = re.sub(r'\s+', ' ', result).strip()
    # Remove stray numbers before words (artifact)
    result = re.sub(r'\b\d+ ([a-z\u00e0-\u00ff])', r'\1', result)
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
        
        # Regenerate ALL French narrative from Spanish
        for field in ["steps", "mistakes"]:
            es_val = es.get(field, [])
            if not es_val: continue
            if isinstance(es_val, list):
                fr_new = [translate(str(s)) for s in es_val]
                if fr.get(field) != fr_new:
                    fr[field] = fr_new
                    changed = True
        
        for field in ["result_context", "example_label", "formula_display"]:
            es_val = es.get(field, "")
            if es_val and isinstance(es_val, str):
                fr_new = translate(es_val)
                if fr.get(field) != fr_new:
                    fr[field] = fr_new
                    changed = True
        
        # Fix input/output labels matching ES
        fr_in = fr.get("inputs", {})
        es_in = es.get("inputs", {})
        for k, v in list(fr_in.items()):
            if isinstance(v, str) and v == es_in.get(k, "") and v:
                fr_in[k] = translate(v)
                changed = True
        fr_out = fr.get("outputs", {})
        es_out = es.get("outputs", {})
        for k, v in list(fr_out.items()):
            if isinstance(v, str) and v == es_out.get(k, "") and v:
                fr_out[k] = translate(v)
                changed = True
        
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated} files")

if __name__ == "__main__":
    main()

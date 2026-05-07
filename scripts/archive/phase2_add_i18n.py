#!/usr/bin/env python3
"""Phase 2 Step 3: Generate i18n entries for all 6 languages."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
I18N_DIR = os.path.join(BASE, "src", "i18n")
CALC_FILE = os.path.join(BASE, "src", "calculators", "calculators.json")
TOOLS_SRC = os.path.join(BASE, "scripts", "phase2_add_tools.py")
LANGS = ["es", "en", "fr", "pt", "de", "it"]

calcs_all = {c["id"]: c for c in json.load(open(CALC_FILE, encoding="utf-8"))["calculators"]}
new_ids = [str(i) for i in [600,601,602,603,604,605,606,607,608,609,700,701,702,703,704,705,706,707,708,709,800,801,802,803,804,805,806,807,808,809,900,901,902,903,904,905,906,907,908,909,210,211,212,213,214,215,216,217,218,219,310,311,312,313,314,315,316,317,318,319,410,411,412,413,414]]

TOOLS_DATA = []
for line in open(TOOLS_SRC, encoding="utf-8"):
    line = line.strip()
    if line.startswith('("') and ',"' in line:
        parts = line.strip(",").replace('"','').replace("(","").replace(")","").split(",")
        if len(parts) >= 8:
            TOOLS_DATA.append(parts)

slug_map = {}
for row in TOOLS_DATA:
    cid = row[0].strip()
    slug_map[cid] = {"es":row[2],"en":row[3],"fr":row[4],"pt":row[5],"de":row[6],"it":row[7]}

IN = json.load(open(os.path.join(BASE, "scripts", "phase2_input_names.json"), encoding="utf-8"))
OUT = json.load(open(os.path.join(BASE, "scripts", "phase2_output_names.json"), encoding="utf-8"))

NEW_BLOCK_SLUGS = {
    "estadistica": {"es":"Estad\u00edstica","en":"Statistics","fr":"Statistiques","pt":"Estat\u00edstica","de":"Statistik","it":"Statistica"},
    "ciencia": {"es":"Ciencia y F\u00edsica","en":"Science & Physics","fr":"Science et Physique","pt":"Ci\u00eancia e F\u00edsica","de":"Wissenschaft & Physik","it":"Scienza e Fisica"},
    "conversion": {"es":"Conversiones de Unidades","en":"Unit Conversions","fr":"Conversions d'Unit\u00e9s","pt":"Convers\u00f5es de Unidades","de":"Einheitenumrechnungen","it":"Conversioni di Unit\u00e0"},
    "deportes": {"es":"Deportes y Fitness","en":"Sports & Fitness","fr":"Sports et Fitness","pt":"Esportes e Fitness","de":"Sport & Fitness","it":"Sport e Fitness"},
}
NEW_BLOCK_DESCS = {
    "estadistica": {"es":"Calculadoras estad\u00edsticas gratuitas: media, mediana, desviaci\u00f3n est\u00e1ndar, varianza, probabilidad y m\u00e1s. Resultados instant\u00e1neos.","en":"Free statistics calculators: mean, median, standard deviation, variance, probability and more.","fr":"Calculatrices statistiques gratuites: moyenne, m\u00e9diane, \u00e9cart type, variance et plus.","pt":"Calculadoras estat\u00edsticas gratuitas: m\u00e9dia, mediana, desvio padr\u00e3o, vari\u00e2ncia e mais.","de":"Kostenlose Statistik-Rechner: Mittelwert, Median, Standardabweichung, Varianz und mehr.","it":"Calcolatori statistici gratuiti: media, mediana, deviazione standard, varianza e altro."},
    "ciencia": {"es":"Calculadoras de ciencia y f\u00edsica: velocidad, fuerza, energ\u00eda, presi\u00f3n, electricidad y m\u00e1s.","en":"Science and physics calculators: speed, force, energy, pressure, electricity and more.","fr":"Calculatrices de science et physique: vitesse, force, \u00e9nergie, pression et plus.","pt":"Calculadoras de ci\u00eancia e f\u00edsica: velocidade, for\u00e7a, energia, press\u00e3o e mais.","de":"Wissenschafts- und Physikrechner: Geschwindigkeit, Kraft, Energie, Druck und mehr.","it":"Calcolatori di scienza e fisica: velocit\u00e0, forza, energia, pressione e altro."},
    "conversion": {"es":"Convertidores de unidades gratuitos: longitud, peso, temperatura, volumen, \u00e1rea, velocidad y m\u00e1s.","en":"Free unit converters: length, weight, temperature, volume, area, speed and more.","fr":"Convertisseurs d'unit\u00e9s gratuits: longueur, poids, temp\u00e9rature, volume et plus.","pt":"Conversores de unidades gratuitos: comprimento, peso, temperatura, volume e mais.","de":"Kostenlose Einheitenumrechner: L\u00e4nge, Gewicht, Temperatur, Volumen und mehr.","it":"Convertitori di unit\u00e0 gratuiti: lunghezza, peso, temperatura, volume e altro."},
    "deportes": {"es":"Calculadoras deportivas: ritmo de carrera, calor\u00edas quemadas, frecuencia card\u00edaca, VO2 max y m\u00e1s.","en":"Sports calculators: running pace, calories burned, heart rate, VO2 max and more.","fr":"Calculatrices sportives: allure de course, calories br\u00fbl\u00e9es, FC max et plus.","pt":"Calculadoras esportivas: ritmo de corrida, calorias queimadas, frequ\u00eancia card\u00edaca e mais.","de":"Sportrechner: Laufpacing, verbrannte Kalorien, Herzfrequenz und mehr.","it":"Calcolatori sportivi: ritmo di corsa, calorie bruciate, frequenza cardiaca e altro."},
}

for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f"{lang}.json")
    data = json.load(open(fpath, encoding="utf-8"))
    calcs_i18n = data.setdefault("calculators", {})
    bs = data.setdefault("block_slugs", {})
    bd = data.setdefault("block_descriptions", {})
    for k, names in NEW_BLOCK_SLUGS.items():
        if k not in bs: bs[k] = names[lang]
    for k, descs in NEW_BLOCK_DESCS.items():
        if k not in bd: bd[k] = descs[lang]
    data["block_slugs"] = bs
    data["block_descriptions"] = bd
    count = 0
    for cid in new_ids:
        if cid not in calcs_all or cid in calcs_i18n:
            continue
        calc = calcs_all[cid]
        inp_labels = {}
        for i in calc["inputs"]:
            key = i["id"]
            inp_labels[key] = IN.get(key, {}).get(lang, key.replace("_"," ").title())
        out_labels = {}
        for o in calc["outputs"]:
            key = o["id"]
            out_labels[key] = OUT.get(key, {}).get(lang, key.replace("_"," ").title())
        slugs = slug_map.get(cid, {})
        s = slugs.get(lang, calc["slug"])
        name = s.replace("-"," ").title()
        entry = {"name":name,"desc":name,"description":name,"seo_title":f"{name} \u2013 Free Online Tool" if lang=="en" else f"{name} Online Gratis","seo_description":name,"inputs":inp_labels,"outputs":out_labels}
        calcs_i18n[cid] = entry
        count += 1
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  {lang}: +{count} entries")
print("Done step 3.")

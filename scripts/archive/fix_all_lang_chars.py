# -*- coding: utf-8 -*-
"""Audit all 5 non-Spanish languages for accent/special character issues."""
import json, os, glob

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

# Common mistakes per language
LANG_CHECKS = {
    "en": {},  # English has fewer accent issues
    "fr": {
        # Common French accent mistakes
        "a ": "\u00e0 ", "etre": "\u00eatre", "ete": "\u00e9t\u00e9",
        "deja": "d\u00e9j\u00e0", "tres": "tr\u00e8s", "apres": "apr\u00e8s",
        "francais": "fran\u00e7ais", "lecon": "le\u00e7on",
        "coefficient": "coefficient", "probleme": "probl\u00e8me",
        "methode": "m\u00e9thode", "systeme": "syst\u00e8me",
        "numero": "num\u00e9ro", "interet": "int\u00e9r\u00eat",
        "frequence": "fr\u00e9quence", "temperature": "temp\u00e9rature",
        "equivalence": "\u00e9quivalence", "economie": "\u00e9conomie",
        "electrique": "\u00e9lectrique", "energie": "\u00e9nergie",
        "epaisseur": "\u00e9paisseur", "etape": "\u00e9tape",
        "etre": "\u00eatre", "etudiant": "\u00e9tudiant",
        "exemple": "exemple", "meme": "m\u00eame",
    },
    "de": {
        # German umlaut issues
        "uber": "\u00fcber", "Uber": "\u00dcber",
        "fur": "f\u00fcr", "Fur": "F\u00fcr",
        "offnen": "\u00f6ffnen", "hohe": "h\u00f6he",
        "moglich": "m\u00f6glich", "konnen": "k\u00f6nnen",
        "mussen": "m\u00fcssen", "uberprufen": "\u00fcberpr\u00fcfen",
        "lang ": "l\u00e4ng ", "Lange": "L\u00e4nge",
        "flache": "Fl\u00e4che", "Flache": "Fl\u00e4che",
        "uberfluss": "\u00dcberfluss",
    },
    "it": {
        # Italian accent issues
        "perche": "perch\u00e9", "Perche": "Perch\u00e9",
        "piu": "pi\u00f9", "Piu": "Pi\u00f9",
        "cosi": "cos\u00ec", "Cosi": "Cos\u00ec",
        "citta": "citt\u00e0", "Citta": "Citt\u00e0",
        "unita": "unit\u00e0", "Unita": "Unit\u00e0",
        "quantita": "quantit\u00e0", "Quantita": "Quantit\u00e0",
        "velocita": "velocit\u00e0", "Velocita": "Velocit\u00e0",
        "facilita": "facilit\u00e0", "Facilita": "Facilit\u00e0",
        "e ": "\u00e8 ", "E ": "\u00c8 ",
        "necessario": "necessario", "Necessario": "Necessario",
    },
    "pt": {
        # Portuguese accent issues
        "calculo ": "c\u00e1lculo ", "Calculo ": "C\u00e1lculo ",
        "numero": "n\u00famero", "Numero": "N\u00famero",
        "formula ": "f\u00f3rmula ", "Formula ": "F\u00f3rmula ",
        "basico": "b\u00e1sico", "Basico": "B\u00e1sico",
        "maximo": "m\u00e1ximo", "Maximo": "M\u00e1ximo",
        "minimo": "m\u00ednimo", "Minimo": "M\u00ednimo",
        "optimo": "\u00f3timo", "Optimo": "\u00d3timo",
        "facil ": "f\u00e1cil ", "Facil ": "F\u00e1cil ",
        "dificil": "dif\u00edcil", "Dificil": "Dif\u00edcil",
        "util ": "\u00fatil ", "Util ": "\u00datil ",
        "area ": "\u00e1rea ", "Area ": "\u00c1rea ",
        "agua": "\u00e1gua", "Agua": "\u00c1gua",
    },
}

total_fixes = 0
files_fixed = 0

for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    name = os.path.basename(fp)
    if "bak" in fp or "monolithic" in fp or name == "calculators.json":
        continue

    with open(fp, "r", encoding="utf-8-sig") as f:
        calc = json.load(f)

    changed = False
    i18n = calc.get("i18n", {})

    for lang, fixes in LANG_CHECKS.items():
        if lang not in i18n:
            continue
        entry = i18n[lang]

        for field in ["name", "description", "seo_title", "seo_description",
                       "example_label", "result_context", "formula_display", "desc"]:
            val = entry.get(field, "")
            if isinstance(val, str) and val:
                fixed = val
                for wrong, correct in fixes.items():
                    if wrong in fixed:
                        fixed = fixed.replace(wrong, correct)
                        total_fixes += 1
                if fixed != val:
                    entry[field] = fixed
                    changed = True

        # Steps and mistakes
        for field in ["steps", "mistakes"]:
            val = entry.get(field, [])
            if isinstance(val, list):
                new_list = []
                for item in val:
                    if isinstance(item, str):
                        fixed_item = item
                        for wrong, correct in fixes.items():
                            if wrong in fixed_item:
                                fixed_item = fixed_item.replace(wrong, correct)
                                total_fixes += 1
                        new_list.append(fixed_item)
                    else:
                        new_list.append(item)
                if new_list != val:
                    entry[field] = new_list
                    changed = True

        # Input/output labels
        for io_field in ["inputs", "outputs"]:
            io_dict = entry.get(io_field, {})
            for k, v in list(io_dict.items()):
                if isinstance(v, str):
                    fixed_v = v
                    for wrong, correct in fixes.items():
                        if wrong in fixed_v:
                            fixed_v = fixed_v.replace(wrong, correct)
                            total_fixes += 1
                    if fixed_v != v:
                        io_dict[k] = fixed_v
                        changed = True

    if changed:
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(calc, f, ensure_ascii=False, indent=2)
        files_fixed += 1

print(f"Fixed {total_fixes} character issues across {files_fixed} files")
print(f"Languages checked: {list(LANG_CHECKS.keys())}")

# -*- coding: utf-8 -*-
"""Fix all missing Spanish accent marks across 461 calculator JSON files."""
import json, os, glob, re

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

# Spanish words that commonly miss accents → proper accented version
FIXES = [
    ("calculacion", "calculaci\u00f3n"), ("Calculacion", "Calculaci\u00f3n"),
    ("aceleracion", "aceleraci\u00f3n"), ("Aceleracion", "Aceleraci\u00f3n"),
    ("Calculo ", "C\u00e1lculo "), ("Calculo", "C\u00e1lculo"),
    ("calculo ", "c\u00e1lculo "),
    ("numero", "n\u00famero"), ("Numero", "N\u00famero"),
    ("diametro", "di\u00e1metro"), ("Diametro", "Di\u00e1metro"),
    ("simultaneo", "simult\u00e1neo"), ("Simultaneo", "Simult\u00e1neo"),
    ("optimo", "\u00f3ptimo"), ("Optimo", "\u00d3ptimo"),
    ("automaticamente", "autom\u00e1ticamente"), ("Automaticamente", "Autom\u00e1ticamente"),
    ("facil ", "f\u00e1cil "), ("Facil ", "F\u00e1cil "),
    ("rapido", "r\u00e1pido"), ("Rapido", "R\u00e1pido"),
    ("rapida", "r\u00e1pida"), ("Rapida", "R\u00e1pida"),
    ("maximo", "m\u00e1ximo"), ("Maximo", "M\u00e1ximo"),
    ("maxima", "m\u00e1xima"), ("Maxima", "M\u00e1xima"),
    ("minimo", "m\u00ednimo"), ("Minimo", "M\u00ednimo"),
    ("minima", "m\u00ednima"), ("Minima", "M\u00ednima"),
    ("formula ", "f\u00f3rmula "), ("Formula ", "F\u00f3rmula "),
    ("formulas", "f\u00f3rmulas"), ("Formulas", "F\u00f3rmulas"),
    (" se\\u0067un ", " seg\u00fan "), (" Se\\u0067un ", " Seg\u00fan "),
    ("area ", "\u00e1rea "), ("Area ", "\u00c1rea "),
    ("ultimo", "\u00faltimo"), ("Ultimo", "\u00daltimo"),
    ("unico", "\u00fanico"), ("Unico", "\u00danico"),
    ("matematicas", "matem\u00e1ticas"), ("Matematicas", "Matem\u00e1ticas"),
    ("fisica ", "f\u00edsica "), ("Fisica ", "F\u00edsica "),
    ("quimica", "qu\u00edmica"), ("Quimica", "Qu\u00edmica"),
    ("basico", "b\u00e1sico"), ("Basico", "B\u00e1sico"),
    ("basica", "b\u00e1sica"), ("Basica", "B\u00e1sica"),
    ("medico", "m\u00e9dico"), ("Medico", "M\u00e9dico"),
    ("medica", "m\u00e9dica"), ("Medica", "M\u00e9dica"),
    ("practico", "pr\u00e1ctico"), ("Practico", "Pr\u00e1ctico"),
    ("practica", "pr\u00e1ctica"), ("Practica", "Pr\u00e1ctica"),
    ("periodo", "per\u00edodo"), ("Periodo", "Per\u00edodo"),
    ("electronico", "electr\u00f3nico"), ("Electronico", "Electr\u00f3nico"),
    ("electronica", "electr\u00f3nica"), ("Electronica", "Electr\u00f3nica"),
    ("termico", "t\u00e9rmico"), ("Termico", "T\u00e9rmico"),
    ("termica", "t\u00e9rmica"), ("Termica", "T\u00e9rmica"),
    ("electrico", "el\u00e9ctrico"), ("Electrico", "El\u00e9ctrico"),
    ("electrica", "el\u00e9ctrica"), ("Electrica", "El\u00e9ctrica"),
    ("estandar", "est\u00e1ndar"), ("Estandar", "Est\u00e1ndar"),
    ("geometrico", "geom\u00e9trico"), ("Geometrico", "Geom\u00e9trico"),
    ("geometrica", "geom\u00e9trica"), ("Geometrica", "Geom\u00e9trica"),
    ("aritmetico", "aritm\u00e9tico"), ("Aritmetico", "Aritm\u00e9tico"),
    ("aritmetica", "aritm\u00e9tica"), ("Aritmetica", "Aritm\u00e9tica"),
    ("cientifico", "cient\u00edfico"), ("Cientifico", "Cient\u00edfico"),
    ("cientifica", "cient\u00edfica"), ("Cientifica", "Cient\u00edfica"),
    ("hidraulico", "hidr\u00e1ulico"), ("Hidraulico", "Hidr\u00e1ulico"),
    ("hidraulica", "hidr\u00e1ulica"), ("Hidraulica", "Hidr\u00e1ulica"),
    ("mecanico", "mec\u00e1nico"), ("Mecanico", "Mec\u00e1nico"),
    ("mecanica", "mec\u00e1nica"), ("Mecanica", "Mec\u00e1nica"),
    ("cilindro", "cilindro"), ("Cilindro", "Cilindro"),  # OK, no accent
    ("espesifico", "espec\u00edfico"), ("Espesifico", "Espec\u00edfico"),
]

def fix_spanish_text(text):
    if not isinstance(text, str):
        return text
    result = text
    for wrong, correct in FIXES:
        if wrong in result:
            result = result.replace(wrong, correct)
    return result


def main():
    updated = 0
    total_fixes = 0
    for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json":
            continue

        with open(fp, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)

        changed = False
        es = calc.get("i18n", {}).get("es", {})

        # Fix all Spanish string fields
        for field in ["name", "description", "seo_title", "seo_description",
                       "example_label", "result_context", "formula_display",
                       "desc"]:
            val = es.get(field, "")
            if isinstance(val, str) and val:
                fixed = fix_spanish_text(val)
                if fixed != val:
                    es[field] = fixed
                    changed = True
                    total_fixes += 1

        # Fix steps and mistakes (lists of strings)
        for field in ["steps", "mistakes"]:
            val = es.get(field, [])
            if isinstance(val, list):
                new = []
                for item in val:
                    if isinstance(item, str):
                        new.append(fix_spanish_text(item))
                    else:
                        new.append(item)
                if new != val:
                    es[field] = new
                    changed = True
                    total_fixes += 1

        # Fix input/output labels
        for io_field in ["inputs", "outputs"]:
            io_dict = es.get(io_field, {})
            for k, v in list(io_dict.items()):
                if isinstance(v, str):
                    fixed = fix_spanish_text(v)
                    if fixed != v:
                        io_dict[k] = fixed
                        changed = True
                        total_fixes += 1

        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            updated += 1

    print(f"Fixed {total_fixes} Spanish accent marks across {updated} files")


if __name__ == "__main__":
    main()

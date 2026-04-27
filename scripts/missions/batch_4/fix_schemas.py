import json
from pathlib import Path

p = Path("scripts/missions/batch_4/schemas.json")
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

for c in data["calculators"]:
    if c["id"] == 1064:
        c["formula"] = "factor = 1.2 if objetivo == 'mantener' else (1.6 if objetivo == 'ganar_musculo' else 2.0)\nreturn {'proteina_min': peso * 0.8, 'proteina_max': peso * 2.2, 'proteina_recomendada': peso * factor}"
    if c["id"] == 1072:
        for o in c["outputs"]:
            if o["id"] == "presion_out":
                o["id"] = "presion"
            if o["id"] == "moles_out":
                o["id"] = "moles"
        for lang in c["i18n"]:
            if "presion_out" in c["i18n"][lang]["outputs"]:
                c["i18n"][lang]["outputs"]["presion"] = c["i18n"][lang]["outputs"].pop("presion_out")
            if "moles_out" in c["i18n"][lang]["outputs"]:
                c["i18n"][lang]["outputs"]["moles"] = c["i18n"][lang]["outputs"].pop("moles_out")

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Fixed")

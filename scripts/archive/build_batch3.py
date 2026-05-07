# -*- coding: utf-8 -*-
"""
Batch 3 builder – directly appends 50 calculators to the project.
Run: python scripts/build_batch3.py
"""
import json, sys, math, random
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
CALCS_FILE = SRC / "calculators" / "calculators.json"
I18N_DIR = SRC / "i18n"
TOOLS_FILE = ROOT / "scripts" / "tools_config.py"
CONTENT_DIR = SRC / "content"

LANGS = ["es", "en", "fr", "pt", "de", "it"]
for lang in LANGS:
    (CONTENT_DIR / lang).mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "scripts"))
from run_batch1 import ContentEngine, verify_formula
engine = ContentEngine()

# ═══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def make_i18n(names, descs, inputs, outputs):
    """names/descs: list of 6 strings (es,en,fr,pt,de,it)
       inputs/outputs: dict {id: [6 strings]}"""
    return {
        lang: {
            "name": names[i],
            "description": descs[i],
            "inputs": {k: v[i] for k, v in inputs.items()},
            "outputs": {k: v[i] for k, v in outputs.items()},
        }
        for i, lang in enumerate(LANGS)
    }

CATALOG = []

def add(**kwargs):
    CATALOG.append(kwargs)

# ── CHEMISTRY (1000-1009) ──
add(
    id="1000", block="quimica", cat="E", domain="tech", concept="pH",
    slugs={"es":"calculadora-ph","en":"ph-calculator","fr":"calculateur-ph","pt":"calculadora-ph","de":"ph-rechner","it":"calcolatore-ph"},
    inputs=[{"id":"h","type":"number","step":"any","default":1e-7,"unit":"mol/L","unit_options":["mol/L","mmol/L"],"unit_category":"concentration"}],
    outputs=[{"id":"ph","unit":""}],
    formula="var h=parseFloat(inputs.h)||1e-7;var ph=-Math.log10(h);return{ph:ph.toFixed(2)};",
    related=["1001","1002"], latex_formula="\\text{pH} = -\\log_{10}[H^+]",
    i18n=make_i18n(
        ["Calculadora de pH","pH Calculator","Calculateur de pH","Calculadora de pH","pH-Rechner","Calcolatore pH"],
        ["Calcula el pH a partir de la concentración de iones hidrógeno.","Calculate pH from hydrogen ion concentration.","Calculez le pH à partir de la concentration en ions hydrogène.","Calcule o pH a partir da concentração de íons hidrogênio.","Berechnen Sie den pH-Wert aus der Wasserstoffionenkonzentration.","Calcola il pH dalla concentrazione di ioni idrogeno."],
        {"h":["Concentración H+","H+ concentration","Concentration H+","Concentração H+","H+-Konzentration","Concentrazione H+"]},
        {"ph":["pH","pH","pH","pH","pH","pH"]}
    ),
    use_cases=[{"en":"Laboratory Titration","en_body":"Chemists monitor pH during acid-base titrations to identify equivalence points."},{"en":"Swimming Pool Maintenance","en_body":"Pool operators keep pH between 7.2 and 7.8 to ensure chlorine effectiveness."},{"en":"Agriculture","en_body":"Farmers test soil pH to determine lime or sulfur amendments."}],
    steps=[{"en":"Enter the hydrogen ion concentration [H+] in mol/L."},{"en":"The calculator returns the pH value."}]
)

add(
    id="1001", block="quimica", cat="E", domain="tech", concept="pOH",
    slugs={"es":"calculadora-poh","en":"poh-calculator","fr":"calculateur-poh","pt":"calculadora-poh","de":"poh-rechner","it":"calcolatore-poh"},
    inputs=[{"id":"oh","type":"number","step":"any","default":1e-7,"unit":"mol/L","unit_options":["mol/L","mmol/L"],"unit_category":"concentration"}],
    outputs=[{"id":"poh","unit":""},{"id":"ph","unit":""}],
    formula="var oh=parseFloat(inputs.oh)||1e-7;var poh=-Math.log10(oh);var ph=14-poh;return{poh:poh.toFixed(2),ph:ph.toFixed(2)};",
    related=["1000","1002"], latex_formula="\\text{pOH} = -\\log_{10}[OH^-], \\quad \\text{pH} = 14 - \\text{pOH}",
    i18n=make_i18n(
        ["Calculadora de pOH","pOH Calculator","Calculateur de pOH","Calculadora de pOH","pOH-Rechner","Calcolatore pOH"],
        ["Calcula el pOH y pH a partir de la concentración de iones hidroxilo.","Calculate pOH and pH from hydroxide ion concentration.","Calculez le pOH et le pH à partir de la concentration en ions hydroxyle.","Calcule o pOH e pH a partir da concentração de íons hidróxido.","Berechnen Sie pOH und pH aus der Hydroxidionenkonzentration.","Calcola pOH e pH dalla concentrazione di ioni idrossido."],
        {"oh":["Concentración OH-","OH- concentration","Concentration OH-","Concentração OH-","OH--Konzentration","Concentrazione OH-"]},
        {"poh":["pOH","pOH","pOH","pOH","pOH","pOH"],"ph":["pH","pH","pH","pH","pH","pH"]}
    ),
    use_cases=[{"en":"Base Strength","en_body":"Industrial chemists characterize strong bases like NaOH by computing pOH."},{"en":"Water Quality","en_body":"Environmental labs measure hydroxide concentration in wastewater."},{"en":"Buffer Design","en_body":"Biochemists balance pH and pOH to maintain stable enzyme activity."}],
    steps=[{"en":"Enter the hydroxide ion concentration [OH-] in mol/L."},{"en":"The calculator returns pOH and derived pH at 25 °C."}]
)

add(
    id="1002", block="quimica", cat="E", domain="tech", concept="molarity",
    slugs={"es":"molaridad","en":"molarity-calculator","fr":"molarite","pt":"molaridade","de":"molaritaet","it":"molarita"},
    inputs=[
        {"id":"moles","type":"number","step":"any","default":1,"unit":"mol","unit_options":["mol","mmol"],"unit_category":"amount"},
        {"id":"volume","type":"number","step":"any","default":1,"unit":"L","unit_options":["L","mL"],"unit_category":"volume"}
    ],
    outputs=[{"id":"molarity","unit":"mol/L"}],
    formula="var moles=parseFloat(inputs.moles)||0;var vol=parseFloat(inputs.volume)||1;return{molarity:(moles/vol).toFixed(4)};",
    related=["1000","1003"], latex_formula="M = \\frac{n}{V}",
    i18n=make_i18n(
        ["Calculadora de Molaridad","Molarity Calculator","Calculateur de Molarité","Calculadora de Molaridade","Molaritätsrechner","Calcolatore Molarità"],
        ["Calcula la concentración molar de una solución.","Calculate the molar concentration of a solution.","Calculez la concentration molaire d'une solution.","Calcule a concentração molar de uma solução.","Berechnen Sie die Molarkonzentration einer Lösung.","Calcola la concentrazione molare di una soluzione."],
        {"moles":["Moles","Moles","Moles","Mols","Mol","Moli"],"volume":["Volumen","Volume","Volume","Volume","Volumen","Volume"]},
        {"molarity":["Molaridad","Molarity","Molarité","Molaridade","Molarität","Molarità"]}
    ),
    use_cases=[{"en":"Solution Preparation","en_body":"Teaching assistants prepare standard solutions by weighing solute and diluting to exact volumes."},{"en":"Titration","en_body":"Analytical chemists calculate unknown concentrations from titrant molarity."},{"en":"Drug Formulation","en_body":"Pharmacists ensure IV solutions have precise molarity."}],
    steps=[{"en":"Enter the amount of solute in moles."},{"en":"Enter the solution volume in liters."},{"en":"The calculator returns molarity in mol/L."}]
)

add(
    id="1003", block="quimica", cat="E", domain="tech", concept="dilution",
    slugs={"es":"dilucion","en":"dilution-calculator","fr":"dilution","pt":"diluicao","de":"verduennung","it":"diluizione"},
    inputs=[
        {"id":"c1","type":"number","step":"any","default":1,"unit":"mol/L","unit_options":["mol/L","M"],"unit_category":"concentration"},
        {"id":"v1","type":"number","step":"any","default":0.1,"unit":"L","unit_options":["L","mL"],"unit_category":"volume"},
        {"id":"c2","type":"number","step":"any","default":0.1,"unit":"mol/L","unit_options":["mol/L","M"],"unit_category":"concentration"}
    ],
    outputs=[{"id":"v2","unit":"L"}],
    formula="var c1=parseFloat(inputs.c1)||0;var v1=parseFloat(inputs.v1)||0;var c2=parseFloat(inputs.c2)||1;var v2=c1*v1/c2;return{v2:v2.toFixed(4)};",
    related=["1002","1004"], latex_formula="C_1 V_1 = C_2 V_2",
    i18n=make_i18n(
        ["Calculadora de Dilución","Dilution Calculator","Calculateur de Dilution","Calculadora de Diluição","Verdünnungsrechner","Calcolatore Diluizione"],
        ["Calcula el volumen final necesario para diluir una solución.","Calculate the final volume needed to dilute a solution.","Calculez le volume final nécessaire pour diluer une solution.","Calcule o volume final necessário para diluir uma solução.","Berechnen Sie das Endvolumen zum Verdünnen einer Lösung.","Calcola il volume finale necessario per diluire una soluzione."],
        {"c1":["Concentración inicial","Initial concentration","Concentration initiale","Concentração inicial","Ausgangskonzentration","Concentrazione iniziale"],"v1":["Volumen inicial","Initial volume","Volume initial","Volume inicial","Ausgangsvolumen","Volume iniziale"],"c2":["Concentración final","Final concentration","Concentration finale","Concentração final","Endkonzentration","Concentrazione finale"]},
        {"v2":["Volumen final","Final volume","Volume final","Volume final","Endvolumen","Volume finale"]}
    ),
    use_cases=[{"en":"Stock Solution","en_body":"Lab technicians dilute concentrated stock solutions to working concentrations."},{"en":"Microbiology","en_body":"Serial dilutions prepare bacterial cultures for colony counting."},{"en":"Beverage Industry","en_body":"Quality control verifies syrup-to-water dilution ratios."}],
    steps=[{"en":"Enter initial concentration and volume."},{"en":"Enter desired final concentration."},{"en":"The calculator returns the required final volume."}]
)

add(
    id="1004", block="quimica", cat="E", domain="tech", concept="ideal gas law",
    slugs={"es":"ley-gases-ideales","en":"ideal-gas-law","fr":"loi-gaz-parfaits","pt":"lei-gases-ideais","de":"ideale-gasgleichung","it":"legge-gas-ideali"},
    inputs=[
        {"id":"p","type":"number","step":"any","default":101325,"unit":"Pa","unit_options":["Pa","kPa","atm"],"unit_category":"pressure"},
        {"id":"v","type":"number","step":"any","default":0.0224,"unit":"m³","unit_options":["m³","L"],"unit_category":"volume"},
        {"id":"n","type":"number","step":"any","default":1,"unit":"mol","unit_options":["mol"],"unit_category":"amount"},
        {"id":"t","type":"number","step":"any","default":273.15,"unit":"K","unit_options":["K","°C"],"unit_category":"temperature"}
    ],
    outputs=[{"id":"result","unit":""}],
    formula="var p=parseFloat(inputs.p)||0;var v=parseFloat(inputs.v)||0;var n=parseFloat(inputs.n)||0;var t=parseFloat(inputs.t)||0;var r=8.314;var missing='';if(p===0)missing='P='+(n*r*t/v).toFixed(2)+' Pa';else if(v===0)missing='V='+(n*r*t/p).toFixed(6)+' m³';else if(n===0)missing='n='+(p*v/(r*t)).toFixed(4)+' mol';else if(t===0)missing='T='+(p*v/(n*r)).toFixed(2)+' K';else missing='All given';return{result:missing};",
    related=["1005","1006"], latex_formula="PV = nRT",
    i18n=make_i18n(
        ["Ley de Gases Ideales","Ideal Gas Law Calculator","Loi des Gaz Parfaits","Lei dos Gases Ideais","Ideale Gasgleichung","Legge dei Gas Ideali"],
        ["Calcula la variable desconocida de la ecuación PV=nRT.","Calculate the unknown variable from PV=nRT.","Calculez la variable inconnue de PV=nRT.","Calcule a variável desconhecida de PV=nRT.","Berechnen Sie die unbekannte Variable aus PV=nRT.","Calcola la variabile incognita da PV=nRT."],
        {"p":["Presión","Pressure","Pression","Pressão","Druck","Pressione"],"v":["Volumen","Volume","Volume","Volume","Volumen","Volume"],"n":["Moles","Moles","Moles","Mols","Mol","Moli"],"t":["Temperatura","Temperature","Température","Temperatura","Temperatur","Temperatura"]},
        {"result":["Resultado","Result","Résultat","Resultado","Ergebnis","Risultato"]}
    ),
    use_cases=[{"en":"Balloon Design","en_body":"Engineers predict gas volume changes with altitude pressure drops."},{"en":"SCUBA Tanks","en_body":"Divers calculate how many moles of compressed air fit in a tank."},{"en":"Chemical Reactors","en_body":"Process engineers size vessels by computing gas volume."}],
    steps=[{"en":"Enter three known values (P, V, n, T)."},{"en":"Leave the fourth as 0 to solve for it."},{"en":"The calculator returns the missing variable."}]
)

add(
    id="1005", block="quimica", cat="E", domain="tech", concept="Boyle's law",
    slugs={"es":"ley-boyle","en":"boyles-law","fr":"loi-de-boyle","pt":"lei-de-boyle","de":"boyle-mariotte-gesetz","it":"legge-di-boyle"},
    inputs=[
        {"id":"p1","type":"number","step":"any","default":1,"unit":"atm","unit_options":["atm","Pa","bar"],"unit_category":"pressure"},
        {"id":"v1","type":"number","step":"any","default":1,"unit":"L","unit_options":["L","mL"],"unit_category":"volume"},
        {"id":"p2","type":"number","step":"any","default":2,"unit":"atm","unit_options":["atm","Pa","bar"],"unit_category":"pressure"}
    ],
    outputs=[{"id":"v2","unit":"L"}],
    formula="var p1=parseFloat(inputs.p1)||0;var v1=parseFloat(inputs.v1)||0;var p2=parseFloat(inputs.p2)||1;var v2=p1*v1/p2;return{v2:v2.toFixed(4)};",
    related=["1004","1006"], latex_formula="P_1 V_1 = P_2 V_2",
    i18n=make_i18n(
        ["Ley de Boyle","Boyle's Law Calculator","Loi de Boyle","Lei de Boyle","Boyle-Mariotte-Gesetz","Legge di Boyle"],
        ["Calcula el volumen final a presión constante y temperatura fija.","Calculate final volume at fixed temperature.","Calculez le volume final à température fixe.","Calcule o volume final a temperatura fixa.","Berechnen Sie das Endvolumen bei fester Temperatur.","Calcola il volume finale a temperatura fissa."],
        {"p1":["Presión inicial","Initial pressure","Pression initiale","Pressão inicial","Anfangsdruck","Pressione iniziale"],"v1":["Volumen inicial","Initial volume","Volume initial","Volume inicial","Anfangsvolumen","Volume iniziale"],"p2":["Presión final","Final pressure","Pression finale","Pressão final","Enddruck","Pressione finale"]},
        {"v2":["Volumen final","Final volume","Volume final","Volume final","Endvolumen","Volume finale"]}
    ),
    use_cases=[{"en":"Syringes","en_body":"Medical devices compress gas volumes to increase pressure for fluid injection."},{"en":"Diving","en_body":"As divers descend, increasing pressure compresses air spaces."},{"en":"Pneumatics","en_body":"Compressed air systems use Boyle's law to size actuators."}],
    steps=[{"en":"Enter initial pressure and volume."},{"en":"Enter final pressure."},{"en":"The calculator returns the final volume."}]
)

add(
    id="1006", block="quimica", cat="E", domain="tech", concept="Charles's law",
    slugs={"es":"ley-charles","en":"charless-law","fr":"loi-de-charles","pt":"lei-de-charles","de":"charles-gesetz","it":"legge-di-charles"},
    inputs=[
        {"id":"v1","type":"number","step":"any","default":1,"unit":"L","unit_options":["L","mL"],"unit_category":"volume"},
        {"id":"t1","type":"number","step":"any","default":273.15,"unit":"K","unit_options":["K","°C"],"unit_category":"temperature"},
        {"id":"t2","type":"number","step":"any","default":373.15,"unit":"K","unit_options":["K","°C"],"unit_category":"temperature"}
    ],
    outputs=[{"id":"v2","unit":"L"}],
    formula="var v1=parseFloat(inputs.v1)||0;var t1=parseFloat(inputs.t1)||273.15;var t2=parseFloat(inputs.t2)||273.15;var v2=v1*t2/t1;return{v2:v2.toFixed(4)};",
    related=["1004","1005"], latex_formula="V_1/T_1 = V_2/T_2",
    i18n=make_i18n(
        ["Ley de Charles","Charles's Law Calculator","Loi de Charles","Lei de Charles","Charles-Gesetz","Legge di Charles"],
        ["Calcula el volumen final a presión constante.","Calculate final volume at constant pressure.","Calculez le volume final à pression constante.","Calcule o volume final a pressão constante.","Berechnen Sie das Endvolumen bei konstantem Druck.","Calcola il volume finale a pressione costante."],
        {"v1":["Volumen inicial","Initial volume","Volume initial","Volume inicial","Anfangsvolumen","Volume iniziale"],"t1":["Temperatura inicial","Initial temperature","Température initiale","Temperatura inicial","Anfangstemperatur","Temperatura iniziale"],"t2":["Temperatura final","Final temperature","Température finale","Temperatura final","Endtemperatur","Temperatura finale"]},
        {"v2":["Volumen final","Final volume","Volume final","Volume final","Endvolumen","Volume finale"]}
    ),
    use_cases=[{"en":"Hot Air Balloons","en_body":"Pilots heat air to expand its volume and decrease density."},{"en":"Thermometers","en_body":"Gas thermometers rely on volume changes proportional to temperature."},{"en":"Engine Cooling","en_body":"Coolant expands in overflow tanks as temperature rises."}],
    steps=[{"en":"Enter initial volume and temperature."},{"en":"Enter final temperature."},{"en":"The calculator returns the final volume."}]
)

add(
    id="1007", block="quimica", cat="E", domain="tech", concept="Gibbs free energy",
    slugs={"es":"energia-libre-gibbs","en":"gibbs-free-energy","fr":"energie-libre-gibbs","pt":"energia-livre-gibbs","de":"gibbs-energie","it":"energia-libera-gibbs"},
    inputs=[
        {"id":"h","type":"number","step":"any","default":-100,"unit":"kJ/mol","unit_options":["kJ/mol","J/mol"],"unit_category":"energy"},
        {"id":"s","type":"number","step":"any","default":0.2,"unit":"kJ/mol·K","unit_options":["kJ/mol·K","J/mol·K"],"unit_category":"entropy"},
        {"id":"t","type":"number","step":"any","default":298,"unit":"K","unit_options":["K","°C"],"unit_category":"temperature"}
    ],
    outputs=[{"id":"g","unit":"kJ/mol"}],
    formula="var h=parseFloat(inputs.h)||0;var s=parseFloat(inputs.s)||0;var t=parseFloat(inputs.t)||0;var g=h-s*t;return{g:g.toFixed(4)};",
    related=["1004","1008"], latex_formula="ΔG = ΔH - TΔS",
    i18n=make_i18n(
        ["Energía Libre de Gibbs","Gibbs Free Energy Calculator","Énergie Libre de Gibbs","Energia Livre de Gibbs","Gibbs-Energie","Energia Libera di Gibbs"],
        ["Determina la espontaneidad de una reacción química.","Determine the spontaneity of a chemical reaction.","Déterminez la spontanéité d'une réaction chimique.","Determine a espontaneidade de uma reação química.","Bestimmen Sie die Spontaneität einer chemischen Reaktion.","Determina la spontaneità di una reazione chimica."],
        {"h":["Entalpía ΔH","Enthalpy ΔH","Enthalpie ΔH","Entalpia ΔH","Enthalpie ΔH","Entalpia ΔH"],"s":["Entropía ΔS","Entropy ΔS","Entropie ΔS","Entropia ΔS","Entropie ΔS","Entropia ΔS"],"t":["Temperatura","Temperature","Température","Temperatura","Temperatur","Temperatura"]},
        {"g":["ΔG","ΔG","ΔG","ΔG","ΔG","ΔG"]}
    ),
    use_cases=[{"en":"Reaction Feasibility","en_body":"Chemists predict whether a reaction proceeds spontaneously."},{"en":"Battery Design","en_body":"Electrochemists maximize negative ΔG for high cell voltage."},{"en":"Protein Folding","en_body":"Biophysicists analyze Gibbs energy landscapes."}],
    steps=[{"en":"Enter enthalpy change ΔH."},{"en":"Enter entropy change ΔS."},{"en":"Enter temperature in Kelvin."}]
)

add(
    id="1008", block="quimica", cat="E", domain="tech", concept="molecular weight",
    slugs={"es":"peso-molecular","en":"molecular-weight","fr":"poids-moleculaire","pt":"peso-molecular","de":"molekulargewicht","it":"peso-molecolare"},
    inputs=[
        {"id":"c","type":"number","step":1,"default":6,"unit":"atoms","unit_options":["atoms"],"unit_category":"count"},
        {"id":"h","type":"number","step":1,"default":12,"unit":"atoms","unit_options":["atoms"],"unit_category":"count"},
        {"id":"o","type":"number","step":1,"default":6,"unit":"atoms","unit_options":["atoms"],"unit_category":"count"}
    ],
    outputs=[{"id":"mw","unit":"g/mol"}],
    formula="var c=parseFloat(inputs.c)||0;var h=parseFloat(inputs.h)||0;var o=parseFloat(inputs.o)||0;var mw=c*12.011+h*1.008+o*15.999;return{mw:mw.toFixed(3)};",
    related=["1002","1009"], latex_formula="MW = n_C × 12.011 + n_H × 1.008 + n_O × 15.999",
    i18n=make_i18n(
        ["Peso Molecular","Molecular Weight Calculator","Poids Moléculaire","Peso Molecular","Molekulargewicht","Peso Molecolare"],
        ["Estima el peso molecular de un compuesto orgánico simple.","Estimate the molecular weight of a simple organic compound.","Estimez le poids moléculaire d'un composé organique simple.","Estime o peso molecular de um composto orgânico simples.","Schätzen Sie das Molekulargewicht einer einfachen organischen Verbindung.","Stima il peso molecolare di un semplice composto organico."],
        {"c":["Átomos C","C atoms","Atomes C","Átomos C","C-Atome","Atomi C"],"h":["Átomos H","H atoms","Atomes H","Átomos H","H-Atome","Atomi H"],"o":["Átomos O","O atoms","Atomes O","Átomos O","O-Atome","Atomi O"]},
        {"mw":["Peso molecular","Molecular weight","Poids moléculaire","Peso molecular","Molekulargewicht","Peso molecolare"]}
    ),
    use_cases=[{"en":"Stoichiometry","en_body":"Students convert between grams and moles using molecular weight."},{"en":"Mass Spectrometry","en_body":"Analysts compare calculated molecular weights to observed peaks."},{"en":"Formulation","en_body":"Pharmaceutical scientists scale recipes based on molecular weight."}],
    steps=[{"en":"Enter the number of carbon, hydrogen, and oxygen atoms."},{"en":"The calculator returns approximate molecular weight in g/mol."}]
)

add(
    id="1009", block="quimica", cat="E", domain="tech", concept="titration",
    slugs={"es":"titulacion","en":"titration-calculator","fr":"titrage","pt":"titulacao","de":"titration","it":"titolazione"},
    inputs=[
        {"id":"c_acid","type":"number","step":"any","default":0.1,"unit":"mol/L","unit_options":["mol/L","M"],"unit_category":"concentration"},
        {"id":"v_acid","type":"number","step":"any","default":25,"unit":"mL","unit_options":["mL","L"],"unit_category":"volume"},
        {"id":"c_base","type":"number","step":"any","default":0.1,"unit":"mol/L","unit_options":["mol/L","M"],"unit_category":"concentration"}
    ],
    outputs=[{"id":"v_base","unit":"mL"}],
    formula="var ca=parseFloat(inputs.c_acid)||0;var va=parseFloat(inputs.v_acid)||0;var cb=parseFloat(inputs.c_base)||1;var vb=ca*va/cb;return{v_base:vb.toFixed(2)};",
    related=["1002","1003"], latex_formula="C_acid V_acid = C_base V_base",
    i18n=make_i18n(
        ["Calculadora de Titulación","Titration Calculator","Calculateur de Titrage","Calculadora de Titulação","Titrationsrechner","Calcolatore Titolazione"],
        ["Calcula el volumen de base necesario para neutralizar un ácido.","Calculate the volume of base needed to neutralize an acid.","Calculez le volume de base nécessaire pour neutraliser un acide.","Calcule o volume de base necessário para neutralizar um ácido.","Berechnen Sie das Basenvolumen zur Neutralisation einer Säure.","Calcola il volume di base necessario per neutralizzare un acido."],
        {"c_acid":["Concentración ácido","Acid concentration","Concentration acide","Concentração ácido","Säurekonzentration","Concentrazione acido"],"v_acid":["Volumen ácido","Acid volume","Volume acide","Volume ácido","Säurevolumen","Volume acido"],"c_base":["Concentración base","Base concentration","Concentration base","Concentração base","Basenkonzentration","Concentrazione base"]},
        {"v_base":["Volumen base","Base volume","Volume base","Volume base","Basenvolumen","Volume base"]}
    ),
    use_cases=[{"en":"Acid-Base Labs","en_body":"Students determine unknown concentrations by titrating against standardized solutions."},{"en":"Wine Making","en_body":"Enologists titrate total acidity to ensure wine pH stays within ranges."},{"en":"Wastewater","en_body":"Operators titrate alkalinity to verify buffering capacity."}],
    steps=[{"en":"Enter acid concentration and volume."},{"en":"Enter base concentration."},{"en":"The calculator returns the required base volume."}]
)

add(
    id="1010", block="electronica", cat="E", domain="tech", concept="voltage divider",
    slugs={"es":"divisor-tension","en":"voltage-divider","fr":"diviseur-tension","pt":"divisor-tensao","de":"spannungsteiler","it":"partitore-tensione"},
    inputs=[
        {"id":"vin","type":"number","step":"any","default":12,"unit":"V","unit_options":["V","mV"],"unit_category":"voltage"},
        {"id":"r1","type":"number","step":"any","default":1000,"unit":"Ω","unit_options":["Ω","kΩ","MΩ"],"unit_category":"resistance"},
        {"id":"r2","type":"number","step":"any","default":1000,"unit":"Ω","unit_options":["Ω","kΩ","MΩ"],"unit_category":"resistance"}
    ],
    outputs=[{"id":"vout","unit":"V"}],
    formula="var vin=parseFloat(inputs.vin)||0;var r1=parseFloat(inputs.r1)||1;var r2=parseFloat(inputs.r2)||1;var vout=vin*r2/(r1+r2);return{vout:vout.toFixed(4)};",
    related=["707","1011"], latex_formula="V_out = V_in * R_2 / (R_1 + R_2)",
    i18n=make_i18n(
        ["Divisor de Tensión","Voltage Divider Calculator","Diviseur de Tension","Divisor de Tensão","Spannungsteiler","Partitore di Tensione"],
        ["Calcula la tensión de salida de un divisor resistivo.","Calculate the output voltage of a resistive divider.","Calculez la tension de sortie d'un diviseur résistif.","Calcule a tensão de saída de um divisor resistivo.","Berechnen Sie die Ausgangsspannung eines Spannungsteilers.","Calcola la tensione di uscita di un partitore resistivo."],
        {"vin":["V entrada","V in","V entrée","V entrada","V Eingang","V ingresso"],"r1":["R1","R1","R1","R1","R1","R1"],"r2":["R2","R2","R2","R2","R2","R2"]},
        {"vout":["V salida","V out","V sortie","V saída","V Ausgang","V uscita"]}
    ),
    use_cases=[{"en":"Sensor Interfaces","en_body":"Microcontroller ADCs use voltage dividers to scale sensor outputs."},{"en":"Level Shifting","en_body":"Designers shift logic levels between 5 V and 3.3 V systems."},{"en":"Battery Monitors","en_body":"Low-cost battery gauges measure fractional voltage to estimate charge."}],
    steps=[{"en":"Enter input voltage."},{"en":"Enter R1 and R2 resistances."},{"en":"The calculator returns Vout."}]
)

add(
    id="1011", block="electronica", cat="E", domain="tech", concept="LED resistor",
    slugs={"es":"resistencia-led","en":"led-resistor","fr":"resistance-led","pt":"resistencia-led","de":"led-vorwiderstand","it":"resistenza-led"},
    inputs=[
        {"id":"v_supply","type":"number","step":"any","default":5,"unit":"V","unit_options":["V"],"unit_category":"voltage"},
        {"id":"v_f","type":"number","step":"any","default":2,"unit":"V","unit_options":["V"],"unit_category":"voltage"},
        {"id":"i_f","type":"number","step":"any","default":20,"unit":"mA","unit_options":["mA","A"],"unit_category":"current"}
    ],
    outputs=[{"id":"r","unit":"Ω"},{"id":"p","unit":"mW"}],
    formula="var vs=parseFloat(inputs.v_supply)||0;var vf=parseFloat(inputs.v_f)||0;var i=parseFloat(inputs.i_f)||1;var r=(vs-vf)/(i/1000);var p=(i/1000)*(i/1000)*r;return{r:Math.round(r),p:p.toFixed(2)};",
    related=["1010","707"], latex_formula="R = (V_supply - V_f) / I_f,  P = I_f^2 R",
    i18n=make_i18n(
        ["Resistencia para LED","LED Resistor Calculator","Résistance pour LED","Resistência para LED","LED-Vorwiderstand","Resistenza LED"],
        ["Calcula la resistencia en serie para un LED.","Calculate the series resistor for an LED.","Calculez la résistance en série pour une LED.","Calcule a resistência em série para um LED.","Berechnen Sie den Vorwiderstand für eine LED.","Calcola la resistenza in serie per un LED."],
        {"v_supply":["V fuente","Supply V","V alim","V fonte","V Versorgung","V alimentazione"],"v_f":["V LED","LED Vf","V LED","V LED","V LED","V LED"],"i_f":["I LED","LED If","I LED","I LED","I LED","I LED"]},
        {"r":["Resistencia","Resistor","Résistance","Resistência","Widerstand","Resistenza"],"p":["Potencia","Power","Puissance","Potência","Leistung","Potenza"]}
    ),
    use_cases=[{"en":"Circuit Design","en_body":"Hobbyists choose standard resistor values to limit LED current."},{"en":"PCB Layout","en_body":"Engineers verify power dissipation in LED series resistors."},{"en":"Automotive Lighting","en_body":"Technicians adapt LED strips to different voltage systems."}],
    steps=[{"en":"Enter supply voltage."},{"en":"Enter LED forward voltage and current."},{"en":"The calculator returns required resistor and power rating."}]
)

add(
    id="1012", block="electronica", cat="E", domain="tech", concept="parallel resistance",
    slugs={"es":"resistencia-paralelo","en":"parallel-resistance","fr":"resistance-parallele","pt":"resistencia-paralelo","de":"parallelwiderstand","it":"resistenza-parallelo"},
    inputs=[
        {"id":"r1","type":"number","step":"any","default":100,"unit":"Ω","unit_options":["Ω","kΩ","MΩ"],"unit_category":"resistance"},
        {"id":"r2","type":"number","step":"any","default":100,"unit":"Ω","unit_options":["Ω","kΩ","MΩ"],"unit_category":"resistance"}
    ],
    outputs=[{"id":"req","unit":"Ω"}],
    formula="var r1=parseFloat(inputs.r1)||1;var r2=parseFloat(inputs.r2)||1;var req=1/(1/r1+1/r2);return{req:req.toFixed(4)};",
    related=["1010","1013"], latex_formula="R_eq = 1 / (1/R_1 + 1/R_2)",
    i18n=make_i18n(
        ["Resistencia en Paralelo","Parallel Resistance Calculator","Résistance Parallèle","Resistência em Paralelo","Parallelwiderstand","Resistenza in Parallelo"],
        ["Calcula la resistencia equivalente de dos resistores en paralelo.","Calculate the equivalent resistance of two parallel resistors.","Calculez la résistance équivalente de deux résistances en parallèle.","Calcule a resistência equivalente de dois resistores em paralelo.","Berechnen Sie den Ersatzwiderstand zweier Parallelwiderstände.","Calcola la resistenza equivalente di due resistori in parallelo."],
        {"r1":["R1","R1","R1","R1","R1","R1"],"r2":["R2","R2","R2","R2","R2","R2"]},
        {"req":["R equivalente","R eq","R équivalente","R equivalente","R Ersatz","R equivalente"]}
    ),
    use_cases=[{"en":"Pull-Down Networks","en_body":"Digital designers place parallel resistors to establish reliable logic low levels."},{"en":"Current Sharing","en_body":"Power engineers parallel resistors to distribute load current."},{"en":"Sensor Bridges","en_body":"Wheatstone bridge arms use parallel combinations to balance ratios."}],
    steps=[{"en":"Enter R1 and R2."},{"en":"The calculator returns equivalent parallel resistance."}]
)

add(
    id="1013", block="electronica", cat="E", domain="tech", concept="capacitor energy",
    slugs={"es":"energia-condensador","en":"capacitor-energy","fr":"energie-condensateur","pt":"energia-capacitor","de":"kondensator-energie","it":"energia-condensatore"},
    inputs=[
        {"id":"c","type":"number","step":"any","default":100,"unit":"µF","unit_options":["µF","nF","F"],"unit_category":"capacitance"},
        {"id":"v","type":"number","step":"any","default":10,"unit":"V","unit_options":["V","kV"],"unit_category":"voltage"}
    ],
    outputs=[{"id":"e","unit":"J"},{"id":"e_mj","unit":"mJ"}],
    formula="var c=parseFloat(inputs.c)||0;var v=parseFloat(inputs.v)||0;var e=0.5*c*1e-6*v*v;return{e:e.toFixed(6),e_mj:(e*1000).toFixed(4)};",
    related=["1010","1014"], latex_formula="E = 1/2 C V^2",
    i18n=make_i18n(
        ["Energía en Condensador","Capacitor Energy Calculator","Énergie du Condensateur","Energia no Capacitor","Kondensatorenergie","Energia Condensatore"],
        ["Calcula la energía almacenada en un condensador.","Calculate the energy stored in a capacitor.","Calculez l'énergie stockée dans un condensateur.","Calcule a energia armazenada em um capacitor.","Berechnen Sie die im Kondensator gespeicherte Energie.","Calcola l'energia immagazzinata in un condensatore."],
        {"c":["Capacitancia","Capacitance","Capacité","Capacitância","Kapazität","Capacità"],"v":["Tensión","Voltage","Tension","Tensão","Spannung","Tensione"]},
        {"e":["Energía","Energy","Énergie","Energia","Energie","Energia"],"e_mj":["Energía mJ","Energy mJ","Énergie mJ","Energia mJ","Energie mJ","Energia mJ"]}
    ),
    use_cases=[{"en":"Camera Flashes","en_body":"Photographers rely on capacitor energy to produce brief bursts of light."},{"en":"Defibrillators","en_body":"Medical devices store hundreds of joules in capacitors."},{"en":"Supercapacitors","en_body":"Engineers size supercapacitor banks for burst power."}],
    steps=[{"en":"Enter capacitance and voltage."},{"en":"The calculator returns stored energy in joules and millijoules."}]
)

add(
    id="1014", block="electronica", cat="E", domain="tech", concept="inductor energy",
    slugs={"es":"energia-bobina","en":"inductor-energy","fr":"energie-bobine","pt":"energia-indutor","de":"spulen-energie","it":"energia-induttore"},
    inputs=[
        {"id":"l","type":"number","step":"any","default":10,"unit":"mH","unit_options":["mH","H","µH"],"unit_category":"inductance"},
        {"id":"i","type":"number","step":"any","default":1,"unit":"A","unit_options":["A","mA"],"unit_category":"current"}
    ],
    outputs=[{"id":"e","unit":"J"}],
    formula="var l=parseFloat(inputs.l)||0;var i=parseFloat(inputs.i)||0;var e=0.5*l*0.001*i*i;return{e:e.toFixed(6)};",
    related=["1013","1015"], latex_formula="E = 1/2 L I^2",
    i18n=make_i18n(
        ["Energía en Bobina","Inductor Energy Calculator","Énergie de la Bobine","Energia no Indutor","Spulenenergie","Energia Induttore"],
        ["Calcula la energía almacenada en una bobina.","Calculate the energy stored in an inductor.","Calculez l'énergie stockée dans une bobine.","Calcule a energia armazenada em um indutor.","Berechnen Sie die in einer Spule gespeicherte Energie.","Calcola l'energia immagazzinata in un induttore."],
        {"l":["Inductancia","Inductance","Inductance","Indutância","Induktivität","Induttanza"],"i":["Corriente","Current","Courant","Corrente","Strom","Corrente"]},
        {"e":["Energía","Energy","Énergie","Energia","Energie","Energia"]}
    ),
    use_cases=[{"en":"SMPS Design","en_body":"Switch-mode power supply designers select inductors based on peak energy storage."},{"en":"Solenoid Actuators","en_body":"Mechanical engineers calculate magnetic energy to predict force."},{"en":"Wireless Charging","en_body":"Coil designers optimize inductance and current for efficiency."}],
    steps=[{"en":"Enter inductance and current."},{"en":"The calculator returns stored energy in joules."}]
)

add(
    id="1015", block="electronica", cat="E", domain="tech", concept="transformer turns",
    slugs={"es":"relacion-transformador","en":"transformer-turns-ratio","fr":"rapport-transformateur","pt":"relacao-transformador","de":"uebersetzungsverhaeltnis","it":"rapporto-transformer"},
    inputs=[
        {"id":"vp","type":"number","step":"any","default":230,"unit":"V","unit_options":["V","kV"],"unit_category":"voltage"},
        {"id":"vs","type":"number","step":"any","default":12,"unit":"V","unit_options":["V","kV"],"unit_category":"voltage"}
    ],
    outputs=[{"id":"ratio","unit":""},{"id":"np_ns","unit":""}],
    formula="var vp=parseFloat(inputs.vp)||1;var vs=parseFloat(inputs.vs)||1;var r=vp/vs;return{ratio:r.toFixed(4),np_ns:r.toFixed(4)};",
    related=["1010","708"], latex_formula="N_p / N_s = V_p / V_s",
    i18n=make_i18n(
        ["Relación de Transformador","Transformer Turns Ratio","Rapport de Transformateur","Relação do Transformador","Übersetzungsverhältnis","Rapporto di Trasformazione"],
        ["Calcula la relación de espiras de un transformador.","Calculate the turns ratio of a transformer.","Calculez le rapport de transformation.","Calcule a relação de espiras de um transformador.","Berechnen Sie das Übersetzungsverhältnis eines Transformators.","Calcola il rapporto di trasformazione."],
        {"vp":["V primario","Primary V","V primaire","V primário","V Primär","V primario"],"vs":["V secundario","Secondary V","V secondaire","V secundário","V Sekundär","V secondario"]},
        {"ratio":["Relación","Ratio","Rapport","Relação","Verhältnis","Rapporto"],"np_ns":["Np/Ns","Np/Ns","Np/Ns","Np/Ns","Np/Ns","Np/Ns"]}
    ),
    use_cases=[{"en":"Power Supplies","en_body":"Designers select transformer ratios to step mains voltage down."},{"en":"Voltage Isolation","en_body":"Medical equipment uses transformers to isolate patient circuits."},{"en":"Impedance Matching","en_body":"Audio transformers match microphone impedance to preamp input."}],
    steps=[{"en":"Enter primary and secondary voltages."},{"en":"The calculator returns the turns ratio Np/Ns."}]
)

add(
    id="1016", block="electronica", cat="E", domain="tech", concept="RC time constant",
    slugs={"es":"constante-tiempo-rc","en":"rc-time-constant","fr":"constante-temps-rc","pt":"constante-tempo-rc","de":"rc-zeitkonstante","it":"costante-tempo-rc"},
    inputs=[
        {"id":"r","type":"number","step":"any","default":1000,"unit":"Ω","unit_options":["Ω","kΩ","MΩ"],"unit_category":"resistance"},
        {"id":"c","type":"number","step":"any","default":1,"unit":"µF","unit_options":["µF","nF","F"],"unit_category":"capacitance"}
    ],
    outputs=[{"id":"tau","unit":"s"},{"id":"cutoff","unit":"Hz"}],
    formula="var r=parseFloat(inputs.r)||0;var c=parseFloat(inputs.c)||0;var tau=r*c*1e-6;var cutoff=1/(2*Math.PI*tau);return{tau:tau.toFixed(6),cutoff:cutoff.toFixed(4)};",
    related=["1013","1017"], latex_formula="τ = RC,  f_c = 1 / (2πRC)",
    i18n=make_i18n(
        ["Constante de Tiempo RC","RC Time Constant Calculator","Constante de Temps RC","Constante de Tempo RC","RC-Zeitkonstante","Costante di Tempo RC"],
        ["Calcula la constante de tiempo y frecuencia de corte de un circuito RC.","Calculate the time constant and cutoff frequency of an RC circuit.","Calculez la constante de temps et la fréquence de coupure d'un circuit RC.","Calcule a constante de tempo e frequência de corte de um circuito RC.","Berechnen Sie die Zeitkonstante und Grenzfrequenz einer RC-Schaltung.","Calcola la costante di tempo e la frequenza di taglio di un circuito RC."],
        {"r":["Resistencia","Resistance","Résistance","Resistência","Widerstand","Resistenza"],"c":["Capacitancia","Capacitance","Capacité","Capacitância","Kapazität","Capacità"]},
        {"tau":["Tau","Tau","Tau","Tau","Tau","Tau"],"cutoff":["Frec corte","Cutoff freq","Fréq coupure","Freq corte","Grenzfrequenz","Freq taglio"]}
    ),
    use_cases=[{"en":"Audio Filters","en_body":"Engineers set cutoff frequencies for high-pass and low-pass filters."},{"en":"Signal Delay","en_body":"RC networks introduce controlled delays for timing circuits."},{"en":"Touch Sensors","en_body":"Capacitive touch screens measure RC time constant changes."}],
    steps=[{"en":"Enter resistance and capacitance."},{"en":"The calculator returns tau and cutoff frequency."}]
)

add(
    id="1017", block="electronica", cat="E", domain="tech", concept="Wheatstone bridge",
    slugs={"es":"puente-wheatstone","en":"wheatstone-bridge","fr":"pont-wheatstone","pt":"ponte-wheatstone","de":"wheatstone-bruecke","it":"ponte-wheatstone"},
    inputs=[
        {"id":"r1","type":"number","step":"any","default":100,"unit":"Ω","unit_options":["Ω","kΩ"],"unit_category":"resistance"},
        {"id":"r2","type":"number","step":"any","default":100,"unit":"Ω","unit_options":["Ω","kΩ"],"unit_category":"resistance"},
        {"id":"r3","type":"number","step":"any","default":100,"unit":"Ω","unit_options":["Ω","kΩ"],"unit_category":"resistance"}
    ],
    outputs=[{"id":"r4","unit":"Ω"}],
    formula="var r1=parseFloat(inputs.r1)||1;var r2=parseFloat(inputs.r2)||1;var r3=parseFloat(inputs.r3)||1;var r4=r2*r3/r1;return{r4:r4.toFixed(4)};",
    related=["1012","1016"], latex_formula="R_4 = R_2 R_3 / R_1",
    i18n=make_i18n(
        ["Puente de Wheatstone","Wheatstone Bridge Calculator","Pont de Wheatstone","Ponte de Wheatstone","Wheatstone-Brücke","Ponte di Wheatstone"],
        ["Calcula la resistencia desconocida en un puente de Wheatstone.","Calculate the unknown resistance in a Wheatstone bridge.","Calculez la résistance inconnue d'un pont de Wheatstone.","Calcule a resistência desconhecida em uma ponte de Wheatstone.","Berechnen Sie den unbekannten Widerstand einer Wheatstone-Brücke.","Calcola la resistenza sconosciuta di un ponte di Wheatstone."],
        {"r1":["R1","R1","R1","R1","R1","R1"],"r2":["R2","R2","R2","R2","R2","R2"],"r3":["R3","R3","R3","R3","R3","R3"]},
        {"r4":["R4 desconocida","R4 unknown","R4 inconnue","R4 desconhecida","R4 unbekannt","R4 sconosciuta"]}
    ),
    use_cases=[{"en":"Strain Gauges","en_body":"Load cells use Wheatstone bridges to convert resistance changes into voltage signals."},{"en":"Temperature Sensors","en_body":"RTD circuits balance bridge arms to detect temperature variations."},{"en":"Pressure Transducers","en_body":"Industrial pressure sensors employ Wheatstone bridges on deformable diaphragms."}],
    steps=[{"en":"Enter three known resistances."},{"en":"The calculator returns the fourth balanced resistance."}]
)

add(
    id="1018", block="electronica", cat="E", domain="tech", concept="series capacitance",
    slugs={"es":"capacitancia-serie","en":"series-capacitance","fr":"capacite-serie","pt":"capacitancia-serie","de":"reihenkapazitaet","it":"capacita-serie"},
    inputs=[
        {"id":"c1","type":"number","step":"any","default":10,"unit":"µF","unit_options":["µF","nF","F"],"unit_category":"capacitance"},
        {"id":"c2","type":"number","step":"any","default":10,"unit":"µF","unit_options":["µF","nF","F"],"unit_category":"capacitance"}
    ],
    outputs=[{"id":"ceq","unit":"µF"}],
    formula="var c1=parseFloat(inputs.c1)||1;var c2=parseFloat(inputs.c2)||1;var ceq=1/(1/c1+1/c2);return{ceq:ceq.toFixed(4)};",
    related=["1012","1013"], latex_formula="1/C_eq = 1/C_1 + 1/C_2",
    i18n=make_i18n(
        ["Capacitancia en Serie","Series Capacitance Calculator","Capacité en Série","Capacitância em Série","Reihenkapazität","Capacità in Serie"],
        ["Calcula la capacitancia equivalente en serie.","Calculate the equivalent series capacitance.","Calculez la capacité équivalente en série.","Calcule a capacitância equivalente em série.","Berechnen Sie die Ersatzkapazität in Reihe.","Calcola la capacità equivalente in serie."],
        {"c1":["C1","C1","C1","C1","C1","C1"],"c2":["C2","C2","C2","C2","C2","C2"]},
        {"ceq":["C equivalente","C eq","C équivalente","C equivalente","C Ersatz","C equivalente"]}
    ),
    use_cases=[{"en":"Tuning Circuits","en_body":"RF designers series capacitors to achieve precise values."},{"en":"Voltage Rating","en_body":"Engineers stack capacitors in series to increase voltage handling."},{"en":"Filter Design","en_body":"Audio crossover networks combine series and parallel capacitors."}],
    steps=[{"en":"Enter C1 and C2."},{"en":"The calculator returns equivalent series capacitance."}]
)

add(
    id="1019", block="electronica", cat="E", domain="tech", concept="resistor color code",
    slugs={"es":"codigo-colores-resistencia","en":"resistor-color-code","fr":"code-couleur-resistance","pt":"codigo-cores-resistor","de":"widerstands-farbcode","it":"codice-colori-resistenza"},
    inputs=[
        {"id":"band1","type":"number","step":1,"default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"band2","type":"number","step":1,"default":0,"unit":"","unit_options":[],"unit_category":""},
        {"id":"multiplier","type":"number","step":1,"default":2,"unit":"","unit_options":[],"unit_category":""}
    ],
    outputs=[{"id":"resistance","unit":"Ω"},{"id":"tolerance","unit":"%"}],
    formula="var b1=parseFloat(inputs.band1)||0;var b2=parseFloat(inputs.band2)||0;var m=parseFloat(inputs.multiplier)||0;var r=(b1*10+b2)*Math.pow(10,m);return{resistance:r,tolerance:5};",
    related=["1010","1012"], latex_formula="R = (10*b1 + b2) * 10^m",
    i18n=make_i18n(
        ["Código de Colores de Resistencia","Resistor Color Code Calculator","Code Couleur des Résistances","Código de Cores do Resistor","Widerstands-Farbcode","Codice Colori Resistenza"],
        ["Decodifica el valor de una resistencia de 4 bandas.","Decode the value of a 4-band resistor.","Décodez la valeur d'une résistance à 4 bandes.","Decodifique o valor de um resistor de 4 faixas.","Dekodieren Sie den Wert eines 4-Band-Widerstands.","Decodifica il valore di una resistenza a 4 fasce."],
        {"band1":["Banda 1","Band 1","Bande 1","Faixa 1","Ring 1","Fascia 1"],"band2":["Banda 2","Band 2","Bande 2","Faixa 2","Ring 2","Fascia 2"],"multiplier":["Multiplicador","Multiplier","Multiplicateur","Multiplicador","Multiplikator","Moltiplicatore"]},
        {"resistance":["Resistencia","Resistance","Résistance","Resistência","Widerstand","Resistenza"],"tolerance":["Tolerancia","Tolerance","Tolérance","Tolerância","Toleranz","Tolleranza"]}
    ),
    use_cases=[{"en":"Circuit Assembly","en_body":"Technicians verify resistor values before soldering."},{"en":"Inventory Management","en_body":"Hobbyists sort loose resistors by decoding color bands."},{"en":"Education","en_body":"Students practice color code memorization."}],
    steps=[{"en":"Enter the first color band digit (0-9)."},{"en":"Enter the second band digit."},{"en":"Enter the multiplier exponent."}]
)

add(
    id="1020", block="clima", cat="E", domain="tech", concept="dew point",
    slugs={"es":"punto-rocio","en":"dew-point-calculator","fr":"point-rosee","pt":"ponto-orvalho","de":"taupunkt","it":"punto-rugiada"},
    inputs=[
        {"id":"t","type":"number","step":"any","default":20,"unit":"°C","unit_options":["°C","°F","K"],"unit_category":"temperature"},
        {"id":"rh","type":"number","step":"any","default":50,"unit":"%","unit_options":["%"],"unit_category":"ratio"}
    ],
    outputs=[{"id":"dp","unit":"°C"}],
    formula="var t=parseFloat(inputs.t)||0;var rh=parseFloat(inputs.rh)||0;var a=17.27;var b=237.7;var gamma=((a*t)/(b+t))+Math.log(rh/100);var dp=(b*gamma)/(a-gamma);return{dp:dp.toFixed(2)};",
    related=["1021","1022"], latex_formula="γ = (17.27T)/(237.7+T) + ln(RH/100),  T_d = (237.7γ)/(17.27-γ)",
    i18n=make_i18n(
        ["Calculadora de Punto de Rocío","Dew Point Calculator","Calculateur de Point de Rosée","Calculadora de Ponto de Orvalho","Taupunktrechner","Calcolatore Punto di Rugiada"],
        ["Calcula el punto de rocío a partir de temperatura y humedad relativa.","Calculate dew point from temperature and relative humidity.","Calculez le point de rosée à partir de la température et de l'humidité relative.","Calcule o ponto de orvalho a partir da temperatura e umidade relativa.","Berechnen Sie den Taupunkt aus Temperatur und relativer Luftfeuchtigkeit.","Calcola il punto di rugiada da temperatura e umidità relativa."],
        {"t":["Temperatura","Temperature","Température","Temperatura","Temperatur","Temperatura"],"rh":["Humedad relativa","Relative humidity","Humidité relative","Umidade relativa","Relative Feuchtigkeit","Umidità relativa"]},
        {"dp":["Punto de rocío","Dew point","Point de rosée","Ponto de orvalho","Taupunkt","Punto di rugiada"]}
    ),
    use_cases=[{"en":"Aviation","en_body":"Pilots monitor dew point spread to predict fog and icing."},{"en":"HVAC","en_body":"Engineers size cooling coils to avoid condensation."},{"en":"Agriculture","en_body":"Farmers track dew point to schedule irrigation."}],
    steps=[{"en":"Enter air temperature."},{"en":"Enter relative humidity."},{"en":"The calculator returns the dew point temperature."}]
)

add(
    id="1021", block="clima", cat="E", domain="tech", concept="heat index",
    slugs={"es":"indice-calor","en":"heat-index-calculator","fr":"indice-chaleur","pt":"indice-calor","de":"hitzeindex","it":"indice-calore"},
    inputs=[
        {"id":"t","type":"number","step":"any","default":30,"unit":"°C","unit_options":["°C","°F"],"unit_category":"temperature"},
        {"id":"rh","type":"number","step":"any","default":70,"unit":"%","unit_options":["%"],"unit_category":"ratio"}
    ],
    outputs=[{"id":"hi","unit":"°C"}],
    formula="var t=parseFloat(inputs.t)||0;var rh=parseFloat(inputs.rh)||0;var hi=-8.784695+1.61139411*t+2.338549*rh-0.14611605*t*rh-0.012308094*t*t-0.016424828*rh*rh+0.002211732*t*t*rh+0.00072546*t*rh*rh-0.000003582*t*t*rh*rh;return{hi:hi.toFixed(2)};",
    related=["1020","1022"], latex_formula="HI = f(T, RH) (Rothfusz regression)",
    i18n=make_i18n(
        ["Índice de Calor","Heat Index Calculator","Indice de Chaleur","Índice de Calor","Hitzeindex","Indice di Calore"],
        ["Estima la sensación térmica combinando temperatura y humedad.","Estimate the apparent temperature combining heat and humidity.","Estimez la température ressentie en combinant chaleur et humidité.","Estime a temperatura aparente combinando calor e umidade.","Schätzen Sie die gefühlte Temperatur aus Hitze und Feuchtigkeit.","Stima la temperatura percepita combinando calore e umidità."],
        {"t":["Temperatura","Temperature","Température","Temperatura","Temperatur","Temperatura"],"rh":["Humedad relativa","Relative humidity","Humidité relative","Umidade relativa","Relative Feuchtigkeit","Umidità relativa"]},
        {"hi":["Índice de calor","Heat index","Indice de chaleur","Índice de calor","Hitzeindex","Indice di calore"]}
    ),
    use_cases=[{"en":"Public Health","en_body":"Emergency services issue heat warnings when heat index exceeds dangerous thresholds."},{"en":"Sports","en_body":"Coaches adjust practice intensity based on heat index."},{"en":"Workplace Safety","en_body":"OSHA guidelines reference heat index for rest cycles."}],
    steps=[{"en":"Enter air temperature."},{"en":"Enter relative humidity."},{"en":"The calculator returns the apparent temperature."}]
)

add(
    id="1022", block="clima", cat="E", domain="tech", concept="wind chill",
    slugs={"es":"sensacion-termica-viento","en":"wind-chill-calculator","fr":"refroidissement-eolien","pt":"sensacao-termica-vento","de":"windchill","it":"percepita-vento"},
    inputs=[
        {"id":"t","type":"number","step":"any","default":-5,"unit":"°C","unit_options":["°C","°F"],"unit_category":"temperature"},
        {"id":"v","type":"number","step":"any","default":20,"unit":"km/h","unit_options":["km/h","mph","m/s"],"unit_category":"speed"}
    ],
    outputs=[{"id":"wc","unit":"°C"}],
    formula="var t=parseFloat(inputs.t)||0;var v=parseFloat(inputs.v)||0;var wc=13.12+0.6215*t-11.37*Math.pow(v,0.16)+0.3965*t*Math.pow(v,0.16);return{wc:wc.toFixed(2)};",
    related=["1020","1021"], latex_formula="WCI = 13.12 + 0.6215 T - 11.37 V^0.16 + 0.3965 T V^0.16",
    i18n=make_i18n(
        ["Sensación Térmica por Viento","Wind Chill Calculator","Refroidissement Éolien","Sensação Térmica do Vento","Windchill","Percepita Vento"],
        ["Calcula la sensación térmica con viento.","Calculate the wind chill temperature.","Calculez la température de refroidissement éolien.","Calcule a sensação térmica do vento.","Berechnen Sie die Windchill-Temperatur.","Calcola la temperatura percepita con il vento."],
        {"t":["Temperatura","Temperature","Température","Temperatura","Temperatur","Temperatura"],"v":["Velocidad viento","Wind speed","Vitesse du vent","Velocidade do vento","Windgeschwindigkeit","Velocità vento"]},
        {"wc":["Sensación térmica","Wind chill","Refroidissement","Sensação térmica","Windchill","Percepita"]}
    ),
    use_cases=[{"en":"Winter Sports","en_body":"Ski resorts post wind chill values to warn about frostbite."},{"en":"Military Operations","en_body":"Commanders evaluate wind chill for arctic exposure times."},{"en":"Pet Safety","en_body":"Veterinarians advise limiting walks when wind chill drops."}],
    steps=[{"en":"Enter air temperature."},{"en":"Enter wind speed."},{"en":"The calculator returns the wind chill temperature."}]
)

add(
    id="1023", block="clima", cat="E", domain="tech", concept="relative humidity",
    slugs={"es":"humedad-relativa","en":"relative-humidity-calculator","fr":"humidite-relative","pt":"umidade-relativa","de":"relative-luftfeuchtigkeit","it":"umidita-relativa"},
    inputs=[
        {"id":"t","type":"number","step":"any","default":20,"unit":"°C","unit_options":["°C","°F"],"unit_category":"temperature"},
        {"id":"dp","type":"number","step":"any","default":10,"unit":"°C","unit_options":["°C","°F"],"unit_category":"temperature"}
    ],
    outputs=[{"id":"rh","unit":"%"}],
    formula="var t=parseFloat(inputs.t)||0;var dp=parseFloat(inputs.dp)||0;var a=17.27;var b=237.7;var num=Math.exp((a*dp)/(b+dp));var den=Math.exp((a*t)/(b+t));var rh=100*(num/den);return{rh:rh.toFixed(2)};",
    related=["1020","1021"], latex_formula="RH = 100 * e^(17.27 T_d / (237.7 + T_d)) / e^(17.27 T / (237.7 + T))",
    i18n=make_i18n(
        ["Calculadora de Humedad Relativa","Relative Humidity Calculator","Calculateur d'Humidité Relative","Calculadora de Umidade Relativa","Relative-Luftfeuchtigkeit","Calcolatore Umidità Relativa"],
        ["Calcula la humedad relativa desde el punto de rocío.","Calculate relative humidity from dew point.","Calculez l'humidité relative à partir du point de rosée.","Calcule a umidade relativa a partir do ponto de orvalho.","Berechnen Sie die relative Luftfeuchtigkeit aus dem Taupunkt.","Calcola l'umidità relativa dal punto di rugiada."],
        {"t":["Temperatura","Temperature","Température","Temperatura","Temperatur","Temperatura"],"dp":["Punto de rocío","Dew point","Point de rosée","Ponto de orvalho","Taupunkt","Punto di rugiada"]},
        {"rh":["Humedad relativa","Relative humidity","Humidité relative","Umidade relativa","Relative Feuchtigkeit","Umidità relativa"]}
    ),
    use_cases=[{"en":"Museums","en_body":"Conservators maintain relative humidity between 45-55% to preserve artifacts."},{"en":"Data Centers","en_body":"Operators keep RH low enough to prevent condensation but high enough to avoid static."},{"en":"Greenhouses","en_body":"Growers adjust ventilation to maintain optimal humidity."}],
    steps=[{"en":"Enter air temperature."},{"en":"Enter dew point."},{"en":"The calculator returns relative humidity."}]
)

add(
    id="1024", block="clima", cat="E", domain="tech", concept="air quality index",
    slugs={"es":"indice-calidad-aire","en":"air-quality-index","fr":"indice-qualite-air","pt":"indice-qualidade-ar","de":"luftqualitaetsindex","it":"indice-qualita-aria"},
    inputs=[{"id":"pm25","type":"number","step":"any","default":12,"unit":"µg/m³","unit_options":["µg/m³"],"unit_category":"concentration"}],
    outputs=[{"id":"aqi","unit":""},{"id":"category","unit":""}],
    formula="var pm=parseFloat(inputs.pm25)||0;var aqi=pm*4.17;var cat=aqi<=50?'Good':aqi<=100?'Moderate':aqi<=150?'Unhealthy for Sensitive':'Unhealthy';return{aqi:aqi.toFixed(0),category:cat};",
    related=["1020","1025"], latex_formula="AQI ≈ 4.17 × PM2.5 (simplified)",
    i18n=make_i18n(
        ["Índice de Calidad del Aire","Air Quality Index Calculator","Indice de Qualité de l'Air","Índice de Qualidade do Ar","Luftqualitätsindex","Indice di Qualità dell'Aria"],
        ["Estima el AQI a partir de la concentración de PM2.5.","Estimate AQI from PM2.5 concentration.","Estimez l'AQI à partir de la concentration de PM2.5.","Estime o AQI a partir da concentração de PM2.5.","Schätzen Sie den AQI aus der PM2.5-Konzentration.","Stima l'AQI dalla concentrazione di PM2.5."],
        {"pm25":["PM2.5","PM2.5","PM2.5","PM2.5","PM2.5","PM2.5"]},
        {"aqi":["AQI","AQI","AQI","AQI","AQI","AQI"],"category":["Categoría","Category","Catégorie","Categoria","Kategorie","Categoria"]}
    ),
    use_cases=[{"en":"Urban Planning","en_body":"City officials publish real-time AQI to inform residents."},{"en":"Exercise Timing","en_body":"Athletes check AQI before outdoor training."},{"en":"Travel Health","en_body":"Travelers with asthma consult AQI forecasts."}],
    steps=[{"en":"Enter PM2.5 concentration in µg/m³."},{"en":"The calculator returns a simplified AQI and category."}]
)

add(
    id="1025", block="clima", cat="E", domain="tech", concept="sunrise sunset",
    slugs={"es":"amanecer-atardecer","en":"sunrise-sunset-calculator","fr":"lever-coucher-soleil","pt":"nascer-por-sol","de":"sonnenauf-untergang","it":"alba-tramonto"},
    inputs=[
        {"id":"lat","type":"number","step":"any","default":40,"unit":"°","unit_options":["°"],"unit_category":"angle"},
        {"id":"day","type":"number","step":1,"default":172,"unit":"day","unit_options":["day"],"unit_category":"time"}
    ],
    outputs=[{"id":"daylight","unit":"h"}],
    formula="var lat=parseFloat(inputs.lat)||0;var day=parseFloat(inputs.day)||0;var decl=23.45*Math.sin((360/365)*(day-81)*Math.PI/180);var latr=lat*Math.PI/180;var decr=decl*Math.PI/180;var h=Math.acos(-Math.tan(latr)*Math.tan(decr));var daylight=h*2*12/Math.PI;return{daylight:daylight.toFixed(2)};",
    related=["1020","1026"], latex_formula="δ = 23.45° sin(360/365 (d-81)),  H = arccos(-tan φ tan δ)",
    i18n=make_i18n(
        ["Duración del Día","Daylight Hours Calculator","Durée du Jour","Duração do Dia","Tageslichtstunden","Ore di Luce Diurna"],
        ["Estima las horas de luz solar según latitud y día del año.","Estimate daylight hours based on latitude and day of year.","Estimez les heures de lumière selon la latitude et le jour.","Estime as horas de luz com base na latitude e dia do ano.","Schätzen Sie die Tageslichtstunden nach Breitengrad und Tag.","Stima le ore di luce in base a latitudine e giorno."],
        {"lat":["Latitud","Latitude","Latitude","Latitude","Breitengrad","Latitudine"],"day":["Día del año","Day of year","Jour de l'année","Dia do ano","Tag des Jahres","Giorno dell'anno"]},
        {"daylight":["Horas de luz","Daylight hours","Heures de lumière","Horas de luz","Tageslichtstunden","Ore di luce"]}
    ),
    use_cases=[{"en":"Solar Panel Sizing","en_body":"Installers use daylight hours to estimate annual energy production."},{"en":"Agriculture","en_body":"Farmers schedule planting around seasonal daylight changes."},{"en":"Mental Health","en_body":"Clinicians track daylight duration for seasonal affective disorder."}],
    steps=[{"en":"Enter latitude in degrees."},{"en":"Enter day of year (1-365)."},{"en":"The calculator returns approximate daylight hours."}]
)

add(
    id="1026", block="clima", cat="E", domain="tech", concept="UV exposure time",
    slugs={"es":"tiempo-exposicion-uv","en":"uv-exposure-time","fr":"temps-exposition-uv","pt":"tempo-exposicao-uv","de":"uv-expositionszeit","it":"tempo-esposizione-uv"},
    inputs=[
        {"id":"uvi","type":"number","step":"any","default":6,"unit":"","unit_options":[],"unit_category":""},
        {"id":"spf","type":"number","step":1,"default":30,"unit":"","unit_options":[],"unit_category":""}
    ],
    outputs=[{"id":"burn_time","unit":"min"}],
    formula="var uvi=parseFloat(inputs.uvi)||1;var spf=parseFloat(inputs.spf)||1;var burn=(200/3)/uvi*spf;return{burn_time:Math.round(burn)};",
    related=["1020","1025"], latex_formula="t_burn ≈ (200 / (3 × UVI)) × SPF",
    i18n=make_i18n(
        ["Tiempo de Exposición UV","UV Exposure Time Calculator","Temps d'Exposition UV","Tempo de Exposição UV","UV-Expositionszeit","Tempo di Esposizione UV"],
        ["Estima el tiempo seguro de exposición solar según UVI y SPF.","Estimate safe sun exposure time based on UV index and SPF.","Estimez le temps d'exposition solaire sécurisé selon l'UV et le SPF.","Estime o tempo seguro de exposição solar com base no UVI e SPF.","Schätzen Sie die sichere Sonnenexpositionszeit nach UV-Index und SPF.","Stima il tempo di esposizione solare sicuro in base a UVI e SPF."],
        {"uvi":["Índice UV","UV index","Indice UV","Índice UV","UV-Index","Indice UV"],"spf":["Factor SPF","SPF","SPF","SPF","SPF","SPF"]},
        {"burn_time":["Tiempo quemadura","Burn time","Temps brûlure","Tempo queimadura","Verbrennungszeit","Tempo scottatura"]}
    ),
    use_cases=[{"en":"Beach Safety","en_body":"Lifeguards post UV index forecasts and recommend SPF ratings."},{"en":"Outdoor Work","en_body":"Supervisors schedule shaded breaks based on UV exposure time."},{"en":"Skin Cancer Prevention","en_body":"Dermatologists educate on safe exposure limits."}],
    steps=[{"en":"Enter the UV index."},{"en":"Enter sunscreen SPF."},{"en":"The calculator returns estimated safe exposure minutes."}]
)

add(
    id="1027", block="clima", cat="E", domain="tech", concept="barometric pressure altitude",
    slugs={"es":"altitud-presion","en":"pressure-altitude","fr":"altitude-pression","pt":"altitude-pressao","de":"druckhoehe","it":"altitudine-pressione"},
    inputs=[{"id":"p","type":"number","step":"any","default":1013,"unit":"hPa","unit_options":["hPa","mbar","inHg"],"unit_category":"pressure"}],
    outputs=[{"id":"alt","unit":"m"}],
    formula="var p=parseFloat(inputs.p)||1013;var alt=44330*(1-Math.pow(p/1013.25,0.1903));return{alt:alt.toFixed(0)};",
    related=["1020","1025"], latex_formula="h = 44330 (1 - (P/1013.25)^0.1903)",
    i18n=make_i18n(
        ["Altitud por Presión","Pressure Altitude Calculator","Altitude par Pression","Altitude por Pressão","Druckhöhe","Altitudine per Pressione"],
        ["Calcula la altitud aproximada desde la presión barométrica.","Calculate approximate altitude from barometric pressure.","Calculez l'altitude approximative à partir de la pression barométrique.","Calcule a altitude aproximada a partir da pressão barométrica.","Berechnen Sie die ungefähre Höhe aus dem Luftdruck.","Calcola l'altitudine approssimativa dalla pressione barometrica."],
        {"p":["Presión","Pressure","Pression","Pressão","Druck","Pressione"]},
        {"alt":["Altitud","Altitude","Altitude","Altitude","Höhe","Altitudine"]}
    ),
    use_cases=[{"en":"Aviation","en_body":"Pilots set altimeters using barometric pressure."},{"en":"Hiking","en_body":"Outdoor enthusiasts use barometric watches to estimate elevation."},{"en":"Meteorology","en_body":"Weather stations correct surface pressure to sea level."}],
    steps=[{"en":"Enter barometric pressure."},{"en":"The calculator returns approximate altitude in meters."}]
)

add(
    id="1028", block="clima", cat="E", domain="tech", concept="rainfall volume",
    slugs={"es":"volumen-lluvia","en":"rainfall-volume","fr":"volume-pluie","pt":"volume-chuva","de":"regenmenge","it":"volume-pioggia"},
    inputs=[
        {"id":"area","type":"number","step":"any","default":100,"unit":"m²","unit_options":["m²","ft²"],"unit_category":"area"},
        {"id":"rain","type":"number","step":"any","default":10,"unit":"mm","unit_options":["mm","in"],"unit_category":"length"}
    ],
    outputs=[{"id":"volume","unit":"L"}],
    formula="var area=parseFloat(inputs.area)||0;var rain=parseFloat(inputs.rain)||0;var vol=area*rain/1000;return{volume:vol.toFixed(2)};",
    related=["1020","1029"], latex_formula="V = A × h",
    i18n=make_i18n(
        ["Volumen de Lluvia","Rainfall Volume Calculator","Volume de Pluie","Volume de Chuva","Regenmenge","Volume Pioggia"],
        ["Calcula el volumen de agua de lluvia recolectada.","Calculate collected rainwater volume.","Calculez le volume d'eau de pluie collectée.","Calcule o volume de água da chuva coletada.","Berechnen Sie das gesammelte Regenwasservolumen.","Calcola il volume di acqua piovana raccolta."],
        {"area":["Área","Area","Surface","Área","Fläche","Area"],"rain":["Lluvia","Rainfall","Précipitations","Precipitação","Niederschlag","Pioggia"]},
        {"volume":["Volumen","Volume","Volume","Volume","Volumen","Volume"]}
    ),
    use_cases=[{"en":"Rainwater Harvesting","en_body":"Homeowners size cisterns by multiplying roof area by rainfall."},{"en":"Agriculture","en_body":"Irrigation planners compare rainfall volume to crop water needs."},{"en":"Urban Drainage","en_body":"Civil engineers model runoff volumes for retention basins."}],
    steps=[{"en":"Enter collection area."},{"en":"Enter rainfall depth."},{"en":"The calculator returns collected volume in liters."}]
)

add(
    id="1029", block="clima", cat="E", domain="tech", concept="evapotranspiration",
    slugs={"es":"evapotranspiracion","en":"evapotranspiration","fr":"evapotranspiration","pt":"evapotranspiracao","de":"evapotranspiration","it":"evapotraspirazione"},
    inputs=[
        {"id":"temp","type":"number","step":"any","default":25,"unit":"°C","unit_options":["°C","°F"],"unit_category":"temperature"},
        {"id":"rh","type":"number","step":"any","default":50,"unit":"%","unit_options":["%"],"unit_category":"ratio"},
        {"id":"wind","type":"number","step":"any","default":2,"unit":"m/s","unit_options":["m/s","km/h"],"unit_category":"speed"}
    ],
    outputs=[{"id":"et","unit":"mm/d"}],
    formula="var t=parseFloat(inputs.temp)||0;var rh=parseFloat(inputs.rh)||0;var w=parseFloat(inputs.wind)||0;var et=0.0023*(t+17.8)*Math.pow(rh,0.5)*w;return{et:et.toFixed(2)};",
    related=["1020","1028"], latex_formula="ET₀ ≈ 0.0023 (T + 17.8) √RH · v",
    i18n=make_i18n(
        ["Evapotranspiración","Evapotranspiration Calculator","Évapotranspiration","Evapotranspiração","Evapotranspiration","Evapotraspirazione"],
        ["Estima la evapotranspiración de referencia.","Estimate reference evapotranspiration.","Estimez l'évapotranspiration de référence.","Estime a evapotranspiração de referência.","Schätzen Sie die Referenzevapotranspiration.","Stima l'evapotraspirazione di riferimento."],
        {"temp":["Temperatura","Temperature","Température","Temperatura","Temperatur","Temperatura"],"rh":["Humedad","Humidity","Humidité","Umidade","Feuchtigkeit","Umidità"],"wind":["Viento","Wind","Vent","Vento","Wind","Vento"]},
        {"et":["ET₀","ET₀","ET₀","ET₀","ET₀","ET₀"]}
    ),
    use_cases=[{"en":"Irrigation Scheduling","en_body":"Farmers replace ET₀ water loss through irrigation systems."},{"en":"Hydrology","en_body":"Watershed models use evapotranspiration to predict streamflow."},{"en":"Climate Studies","en_body":"Scientists track ET trends to assess ecosystem stress."}],
    steps=[{"en":"Enter temperature, humidity, and wind speed."},{"en":"The calculator returns reference evapotranspiration in mm/day."}]
)

add(
    id="1030", block="utilidades", cat="D", domain="tech", concept="day of year",
    slugs={"es":"dia-del-ano","en":"day-of-year","fr":"jour-de-lannee","pt":"dia-do-ano","de":"tag-des-jahres","it":"giorno-dellanno"},
    inputs=[
        {"id":"month","type":"number","step":1,"default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"day","type":"number","step":1,"default":1,"unit":"","unit_options":[],"unit_category":""}
    ],
    outputs=[{"id":"doy","unit":""}],
    formula="var m=parseFloat(inputs.month)||1;var d=parseFloat(inputs.day)||1;var days=[0,31,28,31,30,31,30,31,31,30,31,30,31];var doy=0;for(var i=1;i<m;i++)doy+=days[i];doy+=d;return{doy:doy};",
    related=["1031","1032"], latex_formula="DOY = Σ days_i + d",
    i18n=make_i18n(
        ["Día del Año","Day of Year Calculator","Jour de l'Année","Dia do Ano","Tag des Jahres","Giorno dell'Anno"],
        ["Convierte mes y día al día del año (1-365).","Convert month and day to day of year (1-365).","Convertissez mois et jour en jour de l'année.","Converta mês e dia em dia do ano.","Wandeln Sie Monat und Tag in den Tag des Jahres um.","Converti mese e giorno in giorno dell'anno."],
        {"month":["Mes","Month","Mois","Mês","Monat","Mese"],"day":["Día","Day","Jour","Dia","Tag","Giorno"]},
        {"doy":["Día del año","Day of year","Jour de l'année","Dia do ano","Tag des Jahres","Giorno dell'anno"]}
    ),
    use_cases=[{"en":"Astronomy","en_body":"Observers use day of year to compute solar declination."},{"en":"Project Management","en_body":"Managers track progress against annual day numbers."},{"en":"Agriculture","en_body":"Phenologists compare bloom dates using day of year."}],
    steps=[{"en":"Enter month (1-12)."},{"en":"Enter day (1-31)."},{"en":"The calculator returns day of year."}]
)

add(
    id="1031", block="utilidades", cat="D", domain="tech", concept="week number",
    slugs={"es":"numero-semana","en":"week-number","fr":"numero-semaine","pt":"numero-semana","de":"kalenderwoche","it":"numero-settimana"},
    inputs=[
        {"id":"month","type":"number","step":1,"default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"day","type":"number","step":1,"default":1,"unit":"","unit_options":[],"unit_category":""}
    ],
    outputs=[{"id":"week","unit":""}],
    formula="var m=parseFloat(inputs.month)||1;var d=parseFloat(inputs.day)||1;var doy=0;var days=[0,31,28,31,30,31,30,31,31,30,31,30,31];for(var i=1;i<m;i++)doy+=days[i];doy+=d;var week=Math.ceil(doy/7);return{week:week};",
    related=["1030","1032"], latex_formula="W = ceil(DOY / 7)",
    i18n=make_i18n(
        ["Número de Semana","Week Number Calculator","Numéro de Semaine","Número da Semana","Kalenderwoche","Numero Settimana"],
        ["Calcula el número de semana aproximado del año.","Calculate approximate week number of the year.","Calculez le numéro de semaine approximatif.","Calcule o número da semana aproximado do ano.","Berechnen Sie die ungefähre Kalenderwoche.","Calcola il numero approssimativo della settimana."],
        {"month":["Mes","Month","Mois","Mês","Monat","Mese"],"day":["Día","Day","Jour","Dia","Tag","Giorno"]},
        {"week":["Semana","Week","Semaine","Semana","Woche","Settimana"]}
    ),
    use_cases=[{"en":"Payroll","en_body":"HR departments align pay periods with ISO week numbers."},{"en":"Retail Planning","en_body":"Merchandisers analyze sales by week number."},{"en":"Academic Calendars","en_body":"Universities publish schedules using week numbers."}],
    steps=[{"en":"Enter month and day."},{"en":"The calculator returns approximate week number."}]
)

add(
    id="1032", block="utilidades", cat="D", domain="tech", concept="age in days",
    slugs={"es":"edad-en-dias","en":"age-in-days","fr":"age-en-jours","pt":"idade-em-dias","de":"alter-in-tagen","it":"eta-in-giorni"},
    inputs=[{"id":"birth","type":"date","default":"","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"days","unit":"days"}],
    formula="var b=inputs.birth||'';if(!b)return{days:0};var birth=new Date(b);var now=new Date();var diff=now-birth;return{days:Math.floor(diff/86400000)};",
    related=["942","1030"], latex_formula="days = (now - birth) / 86400000",
    i18n=make_i18n(
        ["Edad en Días","Age in Days Calculator","Âge en Jours","Idade em Dias","Alter in Tagen","Età in Giorni"],
        ["Calcula cuántos días has vivido.","Calculate how many days you have lived.","Calculez combien de jours vous avez vécu.","Calcule quantos dias você viveu.","Berechnen Sie, wie viele Tage Sie gelebt haben.","Calcola quanti giorni hai vissuto."],
        {"birth":["Fecha nacimiento","Birth date","Date naissance","Data nascimento","Geburtsdatum","Data di nascita"]},
        {"days":["Días vividos","Days lived","Jours vécus","Dias vividos","Gelebte Tage","Giorni vissuti"]}
    ),
    use_cases=[{"en":"Milestones","en_body":"People celebrate 10,000-day birthdays."},{"en":"Legal Age","en_body":"Courts verify minimum age by computing exact day counts."},{"en":"Medical Records","en_body":"Pediatricians use days of age for drug dosages."}],
    steps=[{"en":"Enter your birth date."},{"en":"The calculator returns your age in days."}]
)

add(
    id="1033", block="utilidades", cat="D", domain="tech", concept="reading time",
    slugs={"es":"tiempo-lectura","en":"reading-time","fr":"temps-de-lecture","pt":"tempo-leitura","de":"lesezeit","it":"tempo-lettura"},
    inputs=[
        {"id":"words","type":"number","step":1,"default":500,"unit":"words","unit_options":["words"],"unit_category":"count"},
        {"id":"wpm","type":"number","step":1,"default":200,"unit":"wpm","unit_options":["wpm"],"unit_category":"speed"}
    ],
    outputs=[{"id":"minutes","unit":"min"}],
    formula="var w=parseFloat(inputs.words)||0;var wpm=parseFloat(inputs.wpm)||200;return{minutes:Math.ceil(w/wpm)};",
    related=["1034","1035"], latex_formula="t = ceil(words / wpm)",
    i18n=make_i18n(
        ["Tiempo de Lectura","Reading Time Calculator","Temps de Lecture","Tempo de Leitura","Lesezeit","Tempo di Lettura"],
        ["Estima el tiempo de lectura de un texto.","Estimate reading time for a text.","Estimez le temps de lecture d'un texte.","Estime o tempo de leitura de um texto.","Schätzen Sie die Lesezeit für einen Text.","Stima il tempo di lettura di un testo."],
        {"words":["Palabras","Words","Mots","Palavras","Wörter","Parole"],"wpm":["Palabras/min","Words/min","Mots/min","Palavras/min","Wörter/min","Parole/min"]},
        {"minutes":["Minutos","Minutes","Minutes","Minutos","Minuten","Minuti"]}
    ),
    use_cases=[{"en":"Blogging","en_body":"Content management systems display reading time to set expectations."},{"en":"Education","en_body":"Teachers assign reading homework based on estimated times."},{"en":"Publishing","en_body":"Editors use reading time to pace chapters."}],
    steps=[{"en":"Enter word count."},{"en":"Enter reading speed in words per minute."},{"en":"The calculator returns estimated reading time."}]
)

add(
    id="1034", block="utilidades", cat="D", domain="tech", concept="password generator",
    slugs={"es":"generador-contrasenas","en":"password-generator","fr":"generateur-mot-passe","pt":"gerador-senhas","de":"passwort-generator","it":"generatore-password"},
    inputs=[{"id":"length","type":"number","step":1,"default":16,"unit":"chars","unit_options":["chars"],"unit_category":"count"}],
    outputs=[{"id":"password","unit":""}],
    formula="var len=parseFloat(inputs.length)||8;var chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*';var pwd='';for(var i=0;i<len;i++){pwd+=chars.charAt(Math.floor(Math.random()*chars.length));}return{password:pwd};",
    related=["509","1035"], latex_formula="password ~ Uniform(charset^length)",
    i18n=make_i18n(
        ["Generador de Contraseñas","Password Generator","Générateur de Mot de Passe","Gerador de Senhas","Passwort-Generator","Generatore di Password"],
        ["Genera una contraseña aleatoria segura.","Generate a secure random password.","Générez un mot de passe aléatoire sécurisé.","Gere uma senha aleatória segura.","Generieren Sie ein sicheres zufälliges Passwort.","Genera una password casuale sicura."],
        {"length":["Longitud","Length","Longueur","Comprimento","Länge","Lunghezza"]},
        {"password":["Contraseña","Password","Mot de passe","Senha","Passwort","Password"]}
    ),
    use_cases=[{"en":"Account Security","en_body":"Users create unique passwords for every service."},{"en":"IT Administration","en_body":"Admins generate temporary passwords for onboarding."},{"en":"Shared Accounts","en_body":"Teams rotate passwords using generated strings."}],
    steps=[{"en":"Enter desired password length."},{"en":"The calculator returns a random password."}]
)

add(
    id="1035", block="utilidades", cat="D", domain="tech", concept="random number",
    slugs={"es":"numero-aleatorio","en":"random-number","fr":"nombre-aleatoire","pt":"numero-aleatorio","de":"zufallszahl","it":"numero-casuale"},
    inputs=[
        {"id":"min","type":"number","step":1,"default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"max","type":"number","step":1,"default":100,"unit":"","unit_options":[],"unit_category":""}
    ],
    outputs=[{"id":"num","unit":""}],
    formula="var min=parseFloat(inputs.min)||0;var max=parseFloat(inputs.max)||100;var num=Math.floor(Math.random()*(max-min+1))+min;return{num:num};",
    related=["1034","1036"], latex_formula="X ~ Uniform(min, max)",
    i18n=make_i18n(
        ["Número Aleatorio","Random Number Generator","Nombre Aléatoire","Número Aleatório","Zufallszahl","Numero Casuale"],
        ["Genera un número entero aleatorio en un rango.","Generate a random integer within a range.","Générez un nombre entier aléatoire dans une plage.","Gere um número inteiro aleatório em um intervalo.","Generieren Sie eine zufällige Ganzzahl in einem Bereich.","Genera un numero intero casuale in un intervallo."],
        {"min":["Mínimo","Minimum","Minimum","Mínimo","Minimum","Minimo"],"max":["Máximo","Maximum","Maximum","Máximo","Maximum","Massimo"]},
        {"num":["Número","Number","Nombre","Número","Zahl","Numero"]}
    ),
    use_cases=[{"en":"Raffles","en_body":"Organizers draw winners using random numbers."},{"en":"Testing","en_body":"Developers generate random inputs for fuzz testing."},{"en":"Education","en_body":"Teachers create varied arithmetic worksheets."}],
    steps=[{"en":"Enter minimum and maximum values."},{"en":"The calculator returns a random integer."}]
)

add(
    id="1036", block="utilidades", cat="D", domain="tech", concept="dice roller",
    slugs={"es":"lanzador-dados","en":"dice-roller","fr":"lanceur-des","pt":"lancador-dados","de":"wuerfel","it":"lancio-dadi"},
    inputs=[
        {"id":"dice","type":"number","step":1,"default":2,"unit":"dice","unit_options":["dice"],"unit_category":"count"},
        {"id":"sides","type":"number","step":1,"default":6,"unit":"sides","unit_options":["sides"],"unit_category":"count"}
    ],
    outputs=[{"id":"total","unit":""},{"id":"rolls","unit":""}],
    formula="var d=parseFloat(inputs.dice)||1;var s=parseFloat(inputs.sides)||6;var total=0;var rolls=[];for(var i=0;i<d;i++){var r=Math.floor(Math.random()*s)+1;total+=r;rolls.push(r);}return{total:total,rolls:rolls.join(', ')};",
    related=["1035","1037"], latex_formula="roll_i ~ Uniform(1, sides)",
    i18n=make_i18n(
        ["Lanzador de Dados","Dice Roller","Lanceur de Dés","Lançador de Dados","Würfel","Lancio Dadi"],
        ["Lanza dados virtuales con cualquier número de caras.","Roll virtual dice with any number of sides.","Lancez des dés virtuels avec n'importe quel nombre de faces.","Role dados virtuais com qualquer número de faces.","Werfen Sie virtuelle Würfel mit beliebiger Seitenzahl.","Lancia dadi virtuali con qualsiasi numero di facce."],
        {"dice":["Número dados","Dice count","Nombre dés","Número dados","Anzahl Würfel","Numero dadi"],"sides":["Caras","Sides","Faces","Lados","Seiten","Facce"]},
        {"total":["Total","Total","Total","Total","Summe","Totale"],"rolls":["Tiradas","Rolls","Lancers","Lançamentos","Würfe","Lanci"]}
    ),
    use_cases=[{"en":"Board Games","en_body":"Players roll dice digitally when physical dice are unavailable."},{"en":"Role-Playing Games","en_body":"Dungeon masters generate damage by rolling polyhedral dice."},{"en":"Statistics","en_body":"Students simulate probability distributions with dice rolls."}],
    steps=[{"en":"Enter number of dice."},{"en":"Enter number of sides per die."},{"en":"The calculator returns total and individual rolls."}]
)

add(
    id="1037", block="utilidades", cat="D", domain="tech", concept="coin flip",
    slugs={"es":"cara-cruz","en":"coin-flip","fr":"pile-ou-face","pt":"cara-ou-coroa","de":"muenzwurf","it":"testa-o-croce"},
    inputs=[{"id":"flips","type":"number","step":1,"default":1,"unit":"flips","unit_options":["flips"],"unit_category":"count"}],
    outputs=[{"id":"heads","unit":""},{"id":"tails","unit":""},{"id":"result","unit":""}],
    formula="var n=parseFloat(inputs.flips)||1;var h=0;var r=[];for(var i=0;i<n;i++){if(Math.random()<0.5){h++;r.push('H');}else{r.push('T');}}return{heads:h,tails:n-h,result:r.join(' ')};",
    related=["1035","1036"], latex_formula="P(H) = P(T) = 0.5",
    i18n=make_i18n(
        ["Lanzar Moneda","Coin Flip","Pile ou Face","Cara ou Coroa","Münzwurf","Testa o Croce"],
        ["Lanza una moneda virtual múltiples veces.","Flip a virtual coin multiple times.","Lancez une pièce virtuelle plusieurs fois.","Jogue uma moeda virtual várias vezes.","Werfen Sie eine virtuelle Münze mehrmals.","Lancia una moneta virtuale più volte."],
        {"flips":["Lanzamientos","Flips","Lancers","Lançamentos","Würfe","Lanci"]},
        {"heads":["Caras","Heads","Piles","Caras","Kopf","Teste"],"tails":["Cruces","Tails","Faces","Coroas","Zahl","Croci"],"result":["Resultado","Result","Résultat","Resultado","Ergebnis","Risultato"]}
    ),
    use_cases=[{"en":"Decision Making","en_body":"Individuals use coin flips to break ties."},{"en":"Sports","en_body":"Referees decide kickoff possession with a coin toss."},{"en":"Probability Lessons","en_body":"Teachers demonstrate the law of large numbers."}],
    steps=[{"en":"Enter number of flips."},{"en":"The calculator returns heads, tails, and the sequence."}]
)

add(
    id="1038", block="utilidades", cat="D", domain="tech", concept="hex to RGB",
    slugs={"es":"hex-a-rgb","en":"hex-to-rgb","fr":"hex-a-rgb","pt":"hex-para-rgb","de":"hex-zu-rgb","it":"hex-a-rgb"},
    inputs=[{"id":"hex","type":"text","default":"#FF5733","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"r","unit":""},{"id":"g","unit":""},{"id":"b","unit":""}],
    formula="var hex=(inputs.hex||'#000000').replace('#','');if(hex.length===3)hex=hex.split('').map(function(c){return c+c;}).join('');var r=parseInt(hex.substring(0,2),16);var g=parseInt(hex.substring(2,4),16);var b=parseInt(hex.substring(4,6),16);return{r:r,g:g,b:b};",
    related=["1039","1040"], latex_formula="R = hex[1:2], G = hex[3:4], B = hex[5:6]",
    i18n=make_i18n(
        ["Hex a RGB","Hex to RGB Converter","Hex vers RGB","Hex para RGB","Hex zu RGB","Hex a RGB"],
        ["Convierte un color hexadecimal a valores RGB.","Convert a hex color to RGB values.","Convertissez une couleur hexadécimale en valeurs RGB.","Converta uma cor hexadecimal em valores RGB.","Wandeln Sie eine Hex-Farbe in RGB-Werte um.","Converti un colore esadecimale in valori RGB."],
        {"hex":["Color hex","Hex color","Couleur hex","Cor hex","Hex-Farbe","Colore hex"]},
        {"r":["R","R","R","R","R","R"],"g":["G","G","G","G","G","G"],"b":["B","B","B","B","B","B"]}
    ),
    use_cases=[{"en":"Web Design","en_body":"Developers extract RGB values from brand style guides."},{"en":"Image Editing","en_body":"Designers convert hex swatches to RGB for digital assets."},{"en":"Programming","en_body":"Developers parse hex color strings for sprite tints."}],
    steps=[{"en":"Enter a hex color code (e.g., #FF5733)."},{"en":"The calculator returns R, G, and B values (0-255)."}]
)

add(
    id="1039", block="fotografia", cat="D", domain="tech", concept="exposure value",
    slugs={"es":"valor-exposicion","en":"exposure-value","fr":"valeur-exposition","pt":"valor-exposicao","de":"belichtungswert","it":"valore-esposizione"},
    inputs=[
        {"id":"aperture","type":"number","step":"any","default":2.8,"unit":"f/","unit_options":["f/"],"unit_category":""},
        {"id":"shutter","type":"number","step":"any","default":125,"unit":"1/s","unit_options":["1/s"],"unit_category":""},
        {"id":"iso","type":"number","step":1,"default":100,"unit":"ISO","unit_options":["ISO"],"unit_category":""}
    ],
    outputs=[{"id":"ev","unit":"EV"}],
    formula="var a=parseFloat(inputs.aperture)||1;var s=parseFloat(inputs.shutter)||1;var iso=parseFloat(inputs.iso)||100;var ev=Math.log2((a*a)/(1/s))-Math.log2(iso/100);return{ev:ev.toFixed(2)};",
    related=["1040","1041"], latex_formula="EV = log2(N^2 / t) - log2(ISO / 100)",
    i18n=make_i18n(
        ["Valor de Exposición","Exposure Value Calculator","Valeur d'Exposition","Valor de Exposição","Belichtungswert","Valore di Esposizione"],
        ["Calcula el EV a partir de apertura, velocidad e ISO.","Calculate EV from aperture, shutter speed, and ISO.","Calculez la VE à partir de l'ouverture, vitesse et ISO.","Calcule o EV a partir da abertura, velocidade e ISO.","Berechnen Sie den BW aus Blende, Verschlusszeit und ISO.","Calcola il VE da diaframma, tempo e ISO."],
        {"aperture":["Apertura","Aperture","Ouverture","Abertura","Blende","Diaframma"],"shutter":["Velocidad","Shutter","Vitesse","Velocidade","Verschlusszeit","Tempo"],"iso":["ISO","ISO","ISO","ISO","ISO","ISO"]},
        {"ev":["EV","EV","EV","EV","BW","EV"]}
    ),
    use_cases=[{"en":"Manual Mode","en_body":"Photographers use EV to maintain consistent exposure."},{"en":"Flash Photography","en_body":"Studio shooters match ambient EV with flash output."},{"en":"HDR Bracketing","en_body":"Cameras vary exposure value to capture full dynamic range."}],
    steps=[{"en":"Enter aperture f-number."},{"en":"Enter shutter speed denominator (e.g., 125 for 1/125 s)."},{"en":"Enter ISO sensitivity."}]
)

add(
    id="1040", block="fotografia", cat="D", domain="tech", concept="depth of field",
    slugs={"es":"profundidad-campo","en":"depth-of-field","fr":"profondeur-champ","pt":"profundidade-campo","de":"schaerfentiefe","it":"profondita-campo"},
    inputs=[
        {"id":"focal","type":"number","step":"any","default":50,"unit":"mm","unit_options":["mm"],"unit_category":"length"},
        {"id":"aperture","type":"number","step":"any","default":2.8,"unit":"f/","unit_options":["f/"],"unit_category":""},
        {"id":"distance","type":"number","step":"any","default":3,"unit":"m","unit_options":["m","ft"],"unit_category":"length"},
        {"id":"coc","type":"number","step":"any","default":0.03,"unit":"mm","unit_options":["mm"],"unit_category":"length"}
    ],
    outputs=[{"id":"dof","unit":"m"}],
    formula="var f=parseFloat(inputs.focal)||1;var a=parseFloat(inputs.aperture)||1;var d=parseFloat(inputs.distance)||1;var c=parseFloat(inputs.coc)||0.03;var dof=2*d*d*(a*c)/(f*f);return{dof:dof.toFixed(3)};",
    related=["1039","1041"], latex_formula="DoF ≈ 2 u^2 N c / f^2",
    i18n=make_i18n(
        ["Profundidad de Campo","Depth of Field Calculator","Profondeur de Champ","Profundidade de Campo","Schärfentiefe","Profondità di Campo"],
        ["Calcula la profundidad de campo aproximada.","Calculate approximate depth of field.","Calculez la profondeur de champ approximative.","Calcule a profundidade de campo aproximada.","Berechnen Sie die ungefähre Schärfentiefe.","Calcola la profondità di campo approssimativa."],
        {"focal":["Distancia focal","Focal length","Distance focale","Distância focal","Brennweite","Distanza focale"],"aperture":["Apertura","Aperture","Ouverture","Abertura","Blende","Diaframma"],"distance":["Distancia","Distance","Distance","Distância","Entfernung","Distanza"],"coc":["Círculo confusión","Circle of confusion","Cercle de confusion","Círculo confusão","Zerstreuungskreis","Cerchio confusione"]},
        {"dof":["Profundidad campo","Depth of field","Profondeur champ","Profundidade campo","Schärfentiefe","Profondità campo"]}
    ),
    use_cases=[{"en":"Portrait Photography","en_body":"Photographers choose wide apertures for shallow depth of field."},{"en":"Landscape Photography","en_body":"Small apertures maximize depth of field."},{"en":"Macro Photography","en_body":"Extreme close-ups have razor-thin depth of field."}],
    steps=[{"en":"Enter focal length, aperture, subject distance, and circle of confusion."},{"en":"The calculator returns approximate depth of field."}]
)

add(
    id="1041", block="fotografia", cat="D", domain="tech", concept="hyperfocal distance",
    slugs={"es":"distancia-hiperfocal","en":"hyperfocal-distance","fr":"distance-hyperfocale","pt":"distancia-hiperfocal","de":"hyperfokale-distanz","it":"distanza-iperfocale"},
    inputs=[
        {"id":"focal","type":"number","step":"any","default":35,"unit":"mm","unit_options":["mm"],"unit_category":"length"},
        {"id":"aperture","type":"number","step":"any","default":8,"unit":"f/","unit_options":["f/"],"unit_category":""},
        {"id":"coc","type":"number","step":"any","default":0.03,"unit":"mm","unit_options":["mm"],"unit_category":"length"}
    ],
    outputs=[{"id":"hf","unit":"m"}],
    formula="var f=parseFloat(inputs.focal)||1;var a=parseFloat(inputs.aperture)||1;var c=parseFloat(inputs.coc)||0.03;var hf=(f*f)/(a*c)+f;var m=hf/1000;return{hf:m.toFixed(3)};",
    related=["1039","1040"], latex_formula="H = f^2 / (N c) + f",
    i18n=make_i18n(
        ["Distancia Hiperfocal","Hyperfocal Distance Calculator","Distance Hyperfocale","Distância Hiperfocal","Hyperfokale Distanz","Distanza Iperfocale"],
        ["Calcula la distancia hiperfocal para maximizar la profundidad de campo.","Calculate hyperfocal distance to maximize depth of field.","Calculez la distance hyperfocale pour maximiser la profondeur de champ.","Calcule a distância hiperfocal para maximizar a profundidade de campo.","Berechnen Sie die hyperfokale Distanz zur Maximierung der Schärfentiefe.","Calcola la distanza ierfocale per massimizzare la profondità di campo."],
        {"focal":["Distancia focal","Focal length","Distance focale","Distância focal","Brennweite","Distanza focale"],"aperture":["Apertura","Aperture","Ouverture","Abertura","Blende","Diaframma"],"coc":["Círculo confusión","Circle of confusion","Cercle de confusion","Círculo confusão","Zerstreuungskreis","Cerchio confusione"]},
        {"hf":["Hiperfocal","Hyperfocal","Hyperfocale","Hiperfocal","Hyperfokal","Ierfocale"]}
    ),
    use_cases=[{"en":"Landscape Photography","en_body":"Setting focus at hyperfocal distance keeps everything sharp."},{"en":"Astrophotography","en_body":"Star trackers capture foreground and Milky Way detail."},{"en":"Street Photography","en_body":"Pre-focusing allows quick candid shots."}],
    steps=[{"en":"Enter focal length, aperture, and circle of confusion."},{"en":"The calculator returns hyperfocal distance in meters."}]
)

add(
    id="1042", block="fotografia", cat="D", domain="tech", concept="decibel addition",
    slugs={"es":"suma-decibelios","en":"decibel-addition","fr":"addition-decibels","pt":"adicao-decibeis","de":"dezibel-addition","it":"addizione-decibel"},
    inputs=[
        {"id":"db1","type":"number","step":"any","default":60,"unit":"dB","unit_options":["dB"],"unit_category":""},
        {"id":"db2","type":"number","step":"any","default":60,"unit":"dB","unit_options":["dB"],"unit_category":""}
    ],
    outputs=[{"id":"total","unit":"dB"}],
    formula="var db1=parseFloat(inputs.db1)||0;var db2=parseFloat(inputs.db2)||0;var p1=Math.pow(10,db1/10);var p2=Math.pow(10,db2/10);var total=10*Math.log10(p1+p2);return{total:total.toFixed(2)};",
    related=["1043","1023"], latex_formula="L_total = 10 log10(10^(L1/10) + 10^(L2/10))",
    i18n=make_i18n(
        ["Suma de Decibelios","Decibel Addition Calculator","Addition de Décibels","Adição de Decibéis","Dezibel-Addition","Addizione Decibel"],
        ["Suma dos niveles de decibelios.","Add two decibel levels together.","Additionnez deux niveaux de décibels.","Some dois níveis de decibéis.","Addieren Sie zwei Dezibelpegel.","Somma due livelli di decibel."],
        {"db1":["Nivel 1","Level 1","Niveau 1","Nível 1","Pegel 1","Livello 1"],"db2":["Nivel 2","Level 2","Niveau 2","Nível 2","Pegel 2","Livello 2"]},
        {"total":["Total dB","Total dB","Total dB","Total dB","Gesamt dB","Totale dB"]}
    ),
    use_cases=[{"en":"Noise Control","en_body":"Acousticians sum decibel contributions from multiple machines."},{"en":"Audio Mixing","en_body":"Engineers estimate combined loudness when layering tracks."},{"en":"Environmental Assessments","en_body":"Regulators evaluate cumulative noise exposure."}],
    steps=[{"en":"Enter two decibel levels."},{"en":"The calculator returns the combined level."}]
)

add(
    id="1043", block="fotografia", cat="D", domain="tech", concept="SPL distance",
    slugs={"es":"nivel-sonoro-distancia","en":"spl-distance","fr":"niveau-sonore-distance","pt":"nivel-sonoro-distancia","de":"schalldruckabstand","it":"livello-sonoro-distanza"},
    inputs=[
        {"id":"spl1","type":"number","step":"any","default":80,"unit":"dB","unit_options":["dB"],"unit_category":""},
        {"id":"d1","type":"number","step":"any","default":1,"unit":"m","unit_options":["m","ft"],"unit_category":"length"},
        {"id":"d2","type":"number","step":"any","default":10,"unit":"m","unit_options":["m","ft"],"unit_category":"length"}
    ],
    outputs=[{"id":"spl2","unit":"dB"}],
    formula="var spl1=parseFloat(inputs.spl1)||0;var d1=parseFloat(inputs.d1)||1;var d2=parseFloat(inputs.d2)||1;var spl2=spl1-20*Math.log10(d2/d1);return{spl2:spl2.toFixed(2)};",
    related=["1042","1023"], latex_formula="SPL_2 = SPL_1 - 20 log10(d2/d1)",
    i18n=make_i18n(
        ["Nivel Sonoro a Distancia","SPL Distance Calculator","Niveau Sonore à Distance","Nível Sonoro à Distância","Schalldruckpegel-Distanz","Livello Sonoro Distanza"],
        ["Calcula el nivel de presión sonora a una nueva distancia.","Calculate sound pressure level at a new distance.","Calculez le niveau de pression sonore à une nouvelle distance.","Calcule o nível de pressão sonora em uma nova distância.","Berechnen Sie den Schalldruckpegel in einer neuen Entfernung.","Calcola il livello di pressione sonora a una nuova distanza."],
        {"spl1":["SPL inicial","Initial SPL","SPL initial","SPL inicial","SPL initial","SPL iniziale"],"d1":["Distancia 1","Distance 1","Distance 1","Distância 1","Distanz 1","Distanza 1"],"d2":["Distancia 2","Distance 2","Distance 2","Distância 2","Distanz 2","Distanza 2"]},
        {"spl2":["SPL final","Final SPL","SPL final","SPL final","End-SPL","SPL finale"]}
    ),
    use_cases=[{"en":"Concert Venues","en_body":"Audio designers predict SPL attenuation at boundaries."},{"en":"Industrial Noise","en_body":"Engineers determine barrier placement distances."},{"en":"Neighborhood Complaints","en_body":"Municipalities model sound propagation."}],
    steps=[{"en":"Enter initial SPL and distance."},{"en":"Enter new distance."},{"en":"The calculator returns SPL at the new distance."}]
)

add(
    id="1044", block="fotografia", cat="D", domain="tech", concept="contrast ratio",
    slugs={"es":"relacion-contraste","en":"contrast-ratio","fr":"rapport-contraste","pt":"proporcao-contraste","de":"kontrastverhaeltnis","it":"rapporto-contrasto"},
    inputs=[
        {"id":"l1","type":"number","step":"any","default":255,"unit":"","unit_options":[],"unit_category":""},
        {"id":"l2","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""}
    ],
    outputs=[{"id":"ratio","unit":""},{"id":"pass","unit":""}],
    formula="var l1=parseFloat(inputs.l1)||0;var l2=parseFloat(inputs.l2)||0;var r=(l1+0.05)/(l2+0.05);var pass=r>=4.5?'AA':r>=3?'A':'Fail';return{ratio:r.toFixed(2),pass:pass};",
    related=["1038","1042"], latex_formula="CR = (L1 + 0.05) / (L2 + 0.05)",
    i18n=make_i18n(
        ["Relación de Contraste","Contrast Ratio Calculator","Rapport de Contraste","Proporção de Contraste","Kontrastverhältnis","Rapporto di Contrasto"],
        ["Calcula la relación de contraste WCAG entre dos luminancias.","Calculate WCAG contrast ratio between two luminances.","Calculez le rapport de contraste WCAG entre deux luminances.","Calcule a proporção de contraste WCAG entre duas luminâncias.","Berechnen Sie das WCAG-Kontrastverhältnis zwischen zwei Leuchtdichten.","Calcola il rapporto di contrasto WCAG tra due luminanze."],
        {"l1":["Luminancia clara","Light luminance","Luminance claire","Luminância clara","Helle Leuchtdichte","Luminanza chiara"],"l2":["Luminancia oscura","Dark luminance","Luminance sombre","Luminância escura","Dunkle Leuchtdichte","Luminanza scura"]},
        {"ratio":["Relación","Ratio","Rapport","Proporção","Verhältnis","Rapporto"],"pass":["Pasa WCAG","WCAG pass","Passe WCAG","Passa WCAG","WCAG Bestanden","WCAG pass"]}
    ),
    use_cases=[{"en":"Web Accessibility","en_body":"Designers verify text contrast meets WCAG AA standards."},{"en":"Signage","en_body":"Graphic designers choose legible color combinations."},{"en":"UI Design","en_body":"Developers automate contrast checks in design systems."}],
    steps=[{"en":"Enter relative luminance of lighter color (0-1)."},{"en":"Enter relative luminance of darker color (0-1)."},{"en":"The calculator returns contrast ratio and WCAG pass/fail."}]
)

add(
    id="1045", block="transporte", cat="D", domain="tech", concept="crosswind component",
    slugs={"es":"viento-cruzado","en":"crosswind-component","fr":"vent-de-traverse","pt":"componente-vento","de":"seitenwindkomponente","it":"vento-trasversale"},
    inputs=[
        {"id":"wind_dir","type":"number","step":"any","default":270,"unit":"deg","unit_options":["deg"],"unit_category":"angle"},
        {"id":"runway","type":"number","step":"any","default":360,"unit":"deg","unit_options":["deg"],"unit_category":"angle"},
        {"id":"wind_speed","type":"number","step":"any","default":20,"unit":"kt","unit_options":["kt","km/h","mph"],"unit_category":"speed"}
    ],
    outputs=[{"id":"crosswind","unit":"kt"},{"id":"headwind","unit":"kt"}],
    formula="var wd=(parseFloat(inputs.wind_dir)||0)*Math.PI/180;var rw=(parseFloat(inputs.runway)||0)*Math.PI/180;var ws=parseFloat(inputs.wind_speed)||0;var angle=wd-rw;var cw=ws*Math.sin(angle);var hw=ws*Math.cos(angle);return{crosswind:Math.abs(cw).toFixed(1),headwind:hw.toFixed(1)};",
    related=["1046","1047"], latex_formula="CW = WS sin(θ),  HW = WS cos(θ)",
    i18n=make_i18n(
        ["Componente de Viento Cruzado","Crosswind Component Calculator","Composante de Vent de Travers","Componente de Vento","Seitenwindkomponente","Componente Vento Trasversale"],
        ["Calcula los componentes de viento cruzado y de cara.","Calculate crosswind and headwind components.","Calculez les composantes de vent de travers et de face.","Calcule os componentes de vento cruzado e de proa.","Berechnen Sie die Seiten- und Gegenwindkomponenten.","Calcola le componenti del vento trasversale e di prua."],
        {"wind_dir":["Dirección viento","Wind direction","Direction vent","Direção vento","Windrichtung","Direzione vento"],"runway":["Pista","Runway","Piste","Pista","Landebahn","Pista"],"wind_speed":["Velocidad viento","Wind speed","Vitesse vent","Velocidade vento","Windgeschwindigkeit","Velocità vento"]},
        {"crosswind":["Viento cruzado","Crosswind","Vent de travers","Vento cruzado","Seitenwind","Vento trasversale"],"headwind":["Viento de cara","Headwind","Vent de face","Vento de proa","Gegenwind","Vento di prua"]}
    ),
    use_cases=[{"en":"Flight Planning","en_body":"Pilots calculate crosswind to determine if it exceeds aircraft limits."},{"en":"Runway Selection","en_body":"Controllers choose active runways to minimize crosswind exposure."},{"en":"Sailing","en_body":"Skippers estimate leeway caused by crosswind components."}],
    steps=[{"en":"Enter wind direction, runway heading, and wind speed."},{"en":"The calculator returns crosswind and headwind components."}]
)

add(
    id="1046", block="transporte", cat="D", domain="tech", concept="fuel burn",
    slugs={"es":"consumo-combustible","en":"fuel-burn","fr":"consommation-carburant","pt":"consumo-combustivel","de":"kraftstoffverbrauch","it":"consumo-carburante"},
    inputs=[
        {"id":"flow","type":"number","step":"any","default":10,"unit":"gal/h","unit_options":["gal/h","L/h"],"unit_category":"flow"},
        {"id":"time","type":"number","step":"any","default":2,"unit":"h","unit_options":["h"],"unit_category":"time"}
    ],
    outputs=[{"id":"fuel","unit":"gal"}],
    formula="var flow=parseFloat(inputs.flow)||0;var time=parseFloat(inputs.time)||0;return{fuel:(flow*time).toFixed(2)};",
    related=["1045","1047"], latex_formula="Fuel = flow × time",
    i18n=make_i18n(
        ["Consumo de Combustible","Fuel Burn Calculator","Consommation de Carburant","Consumo de Combustível","Kraftstoffverbrauch","Consumo Carburante"],
        ["Calcula el combustible consumido en vuelo.","Calculate fuel burned in flight.","Calculez le carburant consommé en vol.","Calcule o combustível consumido em voo.","Berechnen Sie den Kraftstoffverbrauch im Flug.","Calcola il carburante consumato in volo."],
        {"flow":["Caudal","Flow","Débit","Fluxo","Durchfluss","Portata"],"time":["Tiempo","Time","Temps","Tempo","Zeit","Tempo"]},
        {"fuel":["Combustible","Fuel","Carburant","Combustível","Kraftstoff","Carburante"]}
    ),
    use_cases=[{"en":"Flight Planning","en_body":"Pilots compute total fuel needed for a route including reserves."},{"en":"Boating","en_body":"Captains estimate diesel consumption for long passages."},{"en":"Generator Sizing","en_body":"Facility managers size fuel tanks based on burn rate and runtime."}],
    steps=[{"en":"Enter fuel flow rate."},{"en":"Enter flight or operation time."},{"en":"The calculator returns total fuel consumed."}]
)

add(
    id="1047", block="transporte", cat="D", domain="tech", concept="true airspeed",
    slugs={"es":"velocidad-verdadera","en":"true-airspeed","fr":"vitesse-aire-vraie","pt":"velocidade-ar-verdadeira","de":"wahre-fluggeschwindigkeit","it":"velocita-aria-vera"},
    inputs=[
        {"id":"ias","type":"number","step":"any","default":120,"unit":"kt","unit_options":["kt","km/h","mph"],"unit_category":"speed"},
        {"id":"altitude","type":"number","step":"any","default":5000,"unit":"ft","unit_options":["ft","m"],"unit_category":"length"},
        {"id":"temp","type":"number","step":"any","default":5,"unit":"°C","unit_options":["°C","°F"],"unit_category":"temperature"}
    ],
    outputs=[{"id":"tas","unit":"kt"}],
    formula="var ias=parseFloat(inputs.ias)||0;var alt=parseFloat(inputs.altitude)||0;var t=parseFloat(inputs.temp)||0;var tas=ias*(1+alt/1000*0.02)*(1+(t-15)/273);return{tas:tas.toFixed(1)};",
    related=["1045","1046"], latex_formula="TAS ≈ IAS × (1 + alt/1000 × 0.02) × (1 + (T-15)/273)",
    i18n=make_i18n(
        ["Velocidad Verdadera","True Airspeed Calculator","Vitesse Aire Vraie","Velocidade Ar Verdadeira","Wahre Fluggeschwindigkeit","Velocità Aria Vera"],
        ["Calcula la velocidad verdadera desde la indicada.","Calculate true airspeed from indicated airspeed.","Calculez la vitesse aire vraie à partir de la vitesse indiquée.","Calcule a velocidade ar verdadeira a partir da indicada.","Berechnen Sie die wahre Fluggeschwindigkeit aus der angezeigten.","Calcola la velocità aria vera da quella indicata."],
        {"ias":["IAS","IAS","IAS","IAS","IAS","IAS"],"altitude":["Altitud","Altitude","Altitude","Altitude","Höhe","Altitudine"],"temp":["Temperatura","Temperature","Température","Temperatura","Temperatur","Temperatura"]},
        {"tas":["TAS","TAS","TAS","TAS","TAS","TAS"]}
    ),
    use_cases=[{"en":"Flight Planning","en_body":"Pilots convert IAS to TAS for accurate ETA calculations."},{"en":"Gliding","en_body":"Pilots optimize speed-to-fly using true airspeed at altitude."},{"en":"Aerodynamics","en_body":"Engineers validate performance charts with corrected TAS values."}],
    steps=[{"en":"Enter indicated airspeed."},{"en":"Enter altitude and temperature."},{"en":"The calculator returns approximate true airspeed."}]
)

add(
    id="1048", block="transporte", cat="D", domain="tech", concept="hull speed",
    slugs={"es":"velocidad-casco","en":"hull-speed","fr":"vitesse-coque","pt":"velocidade-casco","de":"rumpfgeschwindigkeit","it":"velocita-scafo"},
    inputs=[{"id":"loa","type":"number","step":"any","default":10,"unit":"m","unit_options":["m","ft"],"unit_category":"length"}],
    outputs=[{"id":"vh","unit":"kt"}],
    formula="var loa=parseFloat(inputs.loa)||0;var vh=1.34*Math.sqrt(loa)*1.94384;return{vh:vh.toFixed(2)};",
    related=["1046","1047"], latex_formula="V_h ≈ 1.34 √LWL (knots)",
    i18n=make_i18n(
        ["Velocidad de Casco","Hull Speed Calculator","Vitesse de Coque","Velocidade de Casco","Rumpfgeschwindigkeit","Velocità di Scafo"],
        ["Calcula la velocidad teórica máxima de un casco de desplazamiento.","Calculate theoretical maximum hull speed.","Calculez la vitesse maximale théorique d'une coque.","Calcule a velocidade máxima teórica de um casco.","Berechnen Sie die theoretische maximale Rumpfgeschwindigkeit.","Calcola la velocità massima teorica di uno scafo."],
        {"loa":["Eslora","Length","Longueur","Comprimento","Länge","Lunghezza"]},
        {"vh":["Velocidad casco","Hull speed","Vitesse coque","Velocidade casco","Rumpfgeschwindigkeit","Velocità scafo"]}
    ),
    use_cases=[{"en":"Yacht Design","en_body":"Naval architects use hull speed to set engine power requirements."},{"en":"Cruising","en_body":"Sailors understand why exceeding hull speed requires exponentially more power."},{"en":"Rowing","en_body":"Coaches explain why longer hulls glide faster with the same crew effort."}],
    steps=[{"en":"Enter waterline length."},{"en":"The calculator returns theoretical hull speed in knots."}]
)

add(
    id="1049", block="transporte", cat="D", domain="tech", concept="great circle distance",
    slugs={"es":"distancia-ortodromica","en":"great-circle-distance","fr":"distance-orthodromique","pt":"distancia-ortodromica","de":"orthodrome","it":"distanza-ortodromica"},
    inputs=[
        {"id":"lat1","type":"number","step":"any","default":40,"unit":"deg","unit_options":["deg"],"unit_category":"angle"},
        {"id":"lon1","type":"number","step":"any","default":-74,"unit":"deg","unit_options":["deg"],"unit_category":"angle"},
        {"id":"lat2","type":"number","step":"any","default":51,"unit":"deg","unit_options":["deg"],"unit_category":"angle"},
        {"id":"lon2","type":"number","step":"any","default":-0.1,"unit":"deg","unit_options":["deg"],"unit_category":"angle"}
    ],
    outputs=[{"id":"dist","unit":"km"}],
    formula="var lat1=parseFloat(inputs.lat1)||0;var lon1=parseFloat(inputs.lon1)||0;var lat2=parseFloat(inputs.lat2)||0;var lon2=parseFloat(inputs.lon2)||0;var R=6371;var dLat=(lat2-lat1)*Math.PI/180;var dLon=(lon2-lon1)*Math.PI/180;var a=Math.sin(dLat/2)*Math.sin(dLat/2)+Math.cos(lat1*Math.PI/180)*Math.cos(lat2*Math.PI/180)*Math.sin(dLon/2)*Math.sin(dLon/2);var c=2*Math.atan2(Math.sqrt(a),Math.sqrt(1-a));return{dist:(R*c).toFixed(2)};",
    related=["1045","1047"], latex_formula="d = 2R arcsin(√(sin²(Δφ/2) + cos φ1 cos φ2 sin²(Δλ/2)))",
    i18n=make_i18n(
        ["Distancia Ortodrómica","Great Circle Distance Calculator","Distance Orthodromique","Distância Ortodrómica","Orthodrome","Distanza Ortodromica"],
        ["Calcula la distancia más corta entre dos puntos en la Tierra.","Calculate the shortest distance between two points on Earth.","Calculez la distance la plus courte entre deux points sur Terre.","Calcule a distância mais curta entre dois pontos na Terra.","Berechnen Sie die kürzeste Entfernung zwischen zwei Punkten auf der Erde.","Calcola la distanza più breve tra due punti sulla Terra."],
        {"lat1":["Latitud 1","Latitude 1","Latitude 1","Latitude 1","Breite 1","Latitudine 1"],"lon1":["Longitud 1","Longitude 1","Longitude 1","Longitude 1","Länge 1","Longitudine 1"],"lat2":["Latitud 2","Latitude 2","Latitude 2","Latitude 2","Breite 2","Latitudine 2"],"lon2":["Longitud 2","Longitude 2","Longitude 2","Longitude 2","Länge 2","Longitudine 2"]},
        {"dist":["Distancia","Distance","Distance","Distância","Entfernung","Distanza"]}
    ),
    use_cases=[{"en":"Aviation","en_body":"Airlines compute great circle distances for fuel and time estimates."},{"en":"Shipping","en_body":"Vessel operators plan shortest ocean routes between ports."},{"en":"Geodesy","en_body":"Surveyors verify coordinate transformations using haversine distances."}],
    steps=[{"en":"Enter latitude and longitude of point 1."},{"en":"Enter latitude and longitude of point 2."},{"en":"The calculator returns distance in kilometers."}]
)


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN EXECUTION
# ═══════════════════════════════════════════════════════════════════════════════

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def append_calculators():
    data = load_json(CALCS_FILE)
    existing_ids = {c["id"] for c in data["calculators"]}
    added = 0
    for calc in CATALOG:
        if calc["id"] in existing_ids:
            print(f"  [SKIP] {calc['id']} already exists")
            continue
        calc_json = {
            "id": calc["id"],
            "slug": calc["slugs"]["es"],
            "block": hash(calc["id"]) % 17 + 1,
            "block_slug": calc["block"],
            "inputs": calc["inputs"],
            "formula": calc["formula"],
            "outputs": calc["outputs"],
            "related": calc.get("related", []),
        }
        data["calculators"].append(calc_json)
        added += 1
    save_json(CALCS_FILE, data)
    print(f"[OK] Added {added} calculators to {CALCS_FILE}")
    return added

def append_i18n():
    for lang in LANGS:
        path = I18N_DIR / f"{lang}.json"
        data = load_json(path)
        calcs = data.setdefault("calculators", {})
        added = 0
        for calc in CATALOG:
            cid = calc["id"]
            if cid in calcs:
                continue
            i18n_data = calc["i18n"][lang]
            calcs[cid] = {
                "name": i18n_data["name"],
                "description": i18n_data["description"],
                "inputs": i18n_data["inputs"],
                "outputs": i18n_data["outputs"],
            }
            added += 1
        save_json(path, data)
        print(f"[OK] Added {added} i18n entries to {lang}.json")

def append_tools():
    with open(TOOLS_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    marker = "\n]\n\n# Quick lookup\nTOOL_BY_ID"
    if marker not in content:
        print("[FAIL] Could not find TOOLS insertion marker")
        return
    entries = []
    for calc in CATALOG:
        slug_parts = [f'"{k}": "{v}"' for k, v in calc["slugs"].items()]
        entries.append(f'    {{"id": "{calc["id"]}", "cat": "{calc["cat"]}", "block": "{calc["block"]}", "slugs": {{{", ".join(slug_parts)}}}}}')
    new_block = "\n".join(entries) + ",\n"
    new_content = content.replace(marker, "\n" + new_block + marker)
    with open(TOOLS_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"[OK] Added {len(CATALOG)} TOOLS entries")

def generate_content():
    for calc in CATALOG:
        for lang in LANGS:
            html = engine.generate(calc, lang)
            out_path = CONTENT_DIR / lang / f"{calc['id']}.html"
            out_path.write_text(html, encoding="utf-8")
    print(f"[OK] Generated {len(CATALOG) * len(LANGS)} content files")

def main():
    print(f"CalcToWork Batch 3 Builder – {len(CATALOG)} calculators")
    print("=" * 60)
    print("[1] Verifying math...")
    ok = 0
    for calc in CATALOG:
        if verify_formula(calc):
            ok += 1
    print(f"[OK] {ok}/{len(CATALOG)} formulas passed verification")
    print("[2] Appending calculators...")
    append_calculators()
    print("[3] Appending i18n...")
    append_i18n()
    print("[4] Appending TOOLS...")
    append_tools()
    print("[5] Generating SEO content...")
    generate_content()
    print("=" * 60)
    print("Done. Run: python scripts/generate_calctowork.py")

if __name__ == "__main__":
    main()

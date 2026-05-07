# -*- coding: utf-8 -*-
"""CalcToWork Batch 2 – 50 calculators"""
import json, sys, random, hashlib
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
CALCS_FILE = SRC / "calculators" / "calculators.json"
I18N_DIR = SRC / "i18n"
TOOLS_FILE = ROOT / "scripts" / "tools_config.py"
CONTENT_DIR = SRC / "content"
LANGS = ["es", "en", "fr", "pt", "de", "it"]
for lang in LANGS: (CONTENT_DIR / lang).mkdir(parents=True, exist_ok=True)

# ── Load existing engine from Batch 1 ──
sys.path.insert(0, str(ROOT / "scripts"))
from run_batch1 import ContentEngine, verify_formula
engine = ContentEngine()

CATALOG = []
def add(**k): CATALOG.append(k)

# Helper for multilingual i18n
def i18n(name_es, name_en, name_fr, name_pt, name_de, name_it, desc_es, desc_en, desc_fr, desc_pt, desc_de, desc_it, inputs_es, inputs_en, inputs_fr, inputs_pt, inputs_de, inputs_it, outputs_es, outputs_en, outputs_fr, outputs_pt, outputs_de, outputs_it):
    return {
        "es":{"name":name_es,"description":desc_es,"inputs":inputs_es,"outputs":outputs_es},
        "en":{"name":name_en,"description":desc_en,"inputs":inputs_en,"outputs":outputs_en},
        "fr":{"name":name_fr,"description":desc_fr,"inputs":inputs_fr,"outputs":outputs_fr},
        "pt":{"name":name_pt,"description":desc_pt,"inputs":inputs_pt,"outputs":outputs_pt},
        "de":{"name":name_de,"description":desc_de,"inputs":inputs_de,"outputs":outputs_de},
        "it":{"name":name_it,"description":desc_it,"inputs":inputs_it,"outputs":outputs_it},
    }

# ═══════════════════════════════════════════════════════════════════════════════
#  BATCH 2 CATALOG
# ═══════════════════════════════════════════════════════════════════════════════

# ── MATH (130-139) ──
add(id="130",block="matematicas",cat="A",domain="math",concept="logarithm",
    slugs={"es":"logaritmo","en":"logarithm-calculator","fr":"logarithme","pt":"logaritmo","de":"logarithmus","it":"logaritmo"},
    inputs=[{"id":"x","type":"number","step":"any","default":100,"unit":"","unit_options":[],"unit_category":""},{"id":"base","type":"number","step":"any","default":10,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"log_val","unit":""}],formula="var x=parseFloat(inputs.x)||1;var b=parseFloat(inputs.base)||10;var v=Math.log(x)/Math.log(b);return{log_val:v.toFixed(6)};",
    related=["131","216"],latex_formula="\\log_b(x) = \\frac{\\ln(x)}{\\ln(b)}",
    i18n=i18n("Logaritmo","Logarithm Calculator","Logarithme","Logaritmo","Logarithmus","Logaritmo","Calcula el logaritmo de un número en cualquier base.","Calculate the logarithm of a number in any base.","Calculez le logarithme d'un nombre dans n'importe quelle base.","Calcule o logaritmo de um número em qualquer base.","Berechnen Sie den Logarithmus einer Zahl in beliebiger Basis.","Calcola il logaritmo di un numero in qualsiasi base.",
        {"x":"Número","base":"Base"},{"x":"Number","base":"Base"},{"x":"Nombre","base":"Base"},{"x":"Número","base":"Base"},{"x":"Zahl","base":"Basis"},{"x":"Numero","base":"Base"},
        {"log_val":"Logaritmo"},{"log_val":"Logarithm"},{"log_val":"Logarithme"},{"log_val":"Logaritmo"},{"log_val":"Logarithmus"},{"log_val":"Logaritmo"}),
    use_cases=[{"en":"Earthquake Magnitude","en_body":"The Richter scale uses base-10 logarithms to compare seismic wave amplitudes across vastly different scales."},{"en":"Information Theory","en_body":"Shannon entropy is computed using base-2 logarithms to measure information content in bits."},{"en":"Chemistry pH","en_body":"pH is the negative base-10 logarithm of hydrogen ion concentration, spanning 14 orders of magnitude."}],
    steps=[{"en":"Enter the number x."},{"en":"Enter the logarithmic base."},{"en":"The calculator returns log_base(x)."}])

add(id="131",block="matematicas",cat="A",domain="math",concept="natural logarithm",
    slugs={"es":"logaritmo-natural","en":"natural-logarithm","fr":"logarithme-neperien","pt":"logaritmo-natural","de":"natuerlicher-logarithmus","it":"logaritmo-naturale"},
    inputs=[{"id":"x","type":"number","step":"any","default":2.718,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"ln","unit":""}],formula="var x=parseFloat(inputs.x)||1;var v=Math.log(x);return{ln:v.toFixed(6)};",
    related=["130","302"],latex_formula="\\ln(x) = \\log_e(x)",
    i18n=i18n("Logaritmo Natural","Natural Logarithm","Logarithme Népérien","Logaritmo Natural","Natürlicher Logarithmus","Logaritmo Naturale","Calcula el logaritmo natural (base e).","Calculate the natural logarithm (base e).","Calculez le logarithme naturel (base e).","Calcule o logaritmo natural (base e).","Berechnen Sie den natürlichen Logarithmus (Basis e).","Calcola il logaritmo naturale (base e).",
        {"x":"Número"},{"x":"Number"},{"x":"Nombre"},{"x":"Número"},{"x":"Zahl"},{"x":"Numero"},
        {"ln":"ln(x)"},{"ln":"ln(x)"},{"ln":"ln(x)"},{"ln":"ln(x)"},{"ln":"ln(x)"},{"ln":"ln(x)"}),
    use_cases=[{"en":"Continuous Compounding","en_body":"The time to double an investment at continuous compounding uses natural log: t = ln(2)/r."},{"en":"Radioactive Decay","en_body":"The decay constant λ relates half-life to natural log: t½ = ln(2)/λ."},{"en":"Thermodynamics","en_body":"Entropy changes in ideal gases involve natural logarithms of volume and temperature ratios."}],
    steps=[{"en":"Enter a positive number x."},{"en":"The calculator returns ln(x)."}])

add(id="132",block="matematicas",cat="A",domain="math",concept="exponential growth",
    slugs={"es":"crecimiento-exponencial","en":"exponential-growth","fr":"croissance-exponentielle","pt":"crescimento-exponencial","de":"exponentielles-wachstum","it":"crescita-esponenziale"},
    inputs=[{"id":"p0","type":"number","step":"any","default":100,"unit":"","unit_options":[],"unit_category":""},{"id":"r","type":"number","step":"any","default":5,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"t","type":"number","step":"any","default":10,"unit":"yr","unit_options":["yr","mo"],"unit_category":"time"}],
    outputs=[{"id":"final","unit":""}],formula="var p0=parseFloat(inputs.p0)||0;var r=(parseFloat(inputs.r)||0)/100;var t=parseFloat(inputs.t)||0;var final=p0*Math.exp(r*t);return{final:final.toFixed(4)};",
    related=["112","302"],latex_formula="P(t) = P_0 e^{rt}",
    i18n=i18n("Crecimiento Exponencial","Exponential Growth Calculator","Croissance Exponentielle","Crescimento Exponencial","Exponentielles Wachstum","Crescita Esponenziale","Calcula el crecimiento exponencial continuo.","Calculate continuous exponential growth.","Calculez la croissance exponentielle continue.","Calcule o crescimento exponencial contínuo.","Berechnen Sie kontinuierliches exponentielles Wachstum.","Calcola la crescita esponenziale continua.",
        {"p0":"Valor inicial","r":"Tasa %","t":"Tiempo"},{"p0":"Initial value","r":"Rate %","t":"Time"},{"p0":"Valeur initiale","r":"Taux %","t":"Temps"},{"p0":"Valor inicial","r":"Taxa %","t":"Tempo"},{"p0":"Anfangswert","r":"Rate %","t":"Zeit"},{"p0":"Valore iniziale","r":"Tasso %","t":"Tempo"},
        {"final":"Valor final"},{"final":"Final value"},{"final":"Valeur finale"},{"final":"Valor final"},{"final":"Endwert"},{"final":"Valore finale"}),
    use_cases=[{"en":"Bacterial Cultures","en_body":"Microbiologists model bacterial doubling under ideal nutrient conditions using exponential growth equations."},{"en":"Viral Marketing","en_body":"Marketers estimate user acquisition when each customer refers multiple new users in a viral loop."},{"en":"Inflation Impact","en_body":"Economists project purchasing power erosion over decades using continuous compounding approximations."}],
    steps=[{"en":"Enter the initial amount P₀."},{"en":"Enter the continuous growth rate r."},{"en":"Enter the time period t."}])

add(id="133",block="matematicas",cat="A",domain="math",concept="factorial",
    slugs={"es":"factorial","en":"factorial-calculator","fr":"factorielle","pt":"fatorial","de":"fakultaet","it":"fattoriale"},
    inputs=[{"id":"n","type":"number","step":1,"default":5,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"fact","unit":""}],formula="var n=parseFloat(inputs.n)||0;var r=1;for(var i=2;i<=n;i++)r*=i;return{fact:r};",
    related=["604","217"],latex_formula="n! = \\prod_{k=1}^{n} k",
    i18n=i18n("Factorial","Factorial Calculator","Factorielle","Fatorial","Fakultät","Fattoriale","Calcula el factorial de un número entero.","Calculate the factorial of an integer.","Calculez la factorielle d'un entier.","Calcule o fatorial de um inteiro.","Berechnen Sie die Fakultät einer ganzen Zahl.","Calcola il fattoriale di un intero.",
        {"n":"n"},{"n":"n"},{"n":"n"},{"n":"n"},{"n":"n"},{"n":"n"},
        {"fact":"n!"},{"fact":"n!"},{"fact":"n!"},{"fact":"n!"},{"fact":"n!"},{"fact":"n!"}),
    use_cases=[{"en":"Combinatorics","en_body":"Factorials count the number of ways to arrange n distinct objects in a sequence."},{"en":"Probability Distributions","en_body":"The Poisson distribution uses factorials in its denominator to model rare event frequencies."},{"en":"Taylor Series","en_body":"Each term of a Taylor expansion includes a factorial in the denominator, controlling convergence."}],
    steps=[{"en":"Enter a non-negative integer n."},{"en":"The calculator returns n! = 1×2×...×n."}])

add(id="134",block="matematicas",cat="A",domain="math",concept="permutations",
    slugs={"es":"permutaciones","en":"permutations-calculator","fr":"permutations","pt":"permutacoes","de":"permutationen","it":"permutazioni"},
    inputs=[{"id":"n","type":"number","step":1,"default":5,"unit":"","unit_options":[],"unit_category":""},{"id":"r","type":"number","step":1,"default":3,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"perm","unit":""}],formula="var n=parseFloat(inputs.n)||0;var r=parseFloat(inputs.r)||0;var num=1;for(var i=0;i<r;i++)num*=n-i;var den=1;return{perm:num};",
    related=["133","604"],latex_formula="P(n,r) = \\frac{n!}{(n-r)!}",
    i18n=i18n("Permutaciones","Permutations Calculator","Permutations","Permutações","Permutationen","Permutazioni","Calcula las permutaciones de n elementos tomados de r en r.","Calculate permutations of n items taken r at a time.","Calculez les permutations de n éléments pris r à r.","Calcule as permutações de n itens tomados r de cada vez.","Berechnen Sie Permutationen von n Elementen, r auf einmal.","Calcola le permutazioni di n elementi presi r alla volta.",
        {"n":"n total","r":"r seleccionados"},{"n":"n total","r":"r chosen"},{"n":"n total","r":"r choisis"},{"n":"n total","r":"r escolhidos"},{"n":"n gesamt","r":"r ausgewählt"},{"n":"n totale","r":"r scelti"},
        {"perm":"Permutaciones"},{"perm":"Permutations"},{"perm":"Permutations"},{"perm":"Permutações"},{"perm":"Permutationen"},{"perm":"Permutazioni"}),
    use_cases=[{"en":"Password Combinatorics","en_body":"Security analysts count permutations to estimate brute-force cracking times for character-based passwords."},{"en":"Race Finishes","en_body":"Organizers calculate how many distinct podium finishes are possible with n runners and r medal positions."},{"en":"Scheduling","en_body":"Operations researchers enumerate task orderings to find optimal sequences that minimize setup times."}],
    steps=[{"en":"Enter the total number of items n."},{"en":"Enter how many items r to arrange."},{"en":"The calculator returns P(n,r)."}])

add(id="135",block="matematicas",cat="A",domain="math",concept="combinations",
    slugs={"es":"combinaciones","en":"combinations-calculator","fr":"combinaisons","pt":"combinacoes","de":"kombinationen","it":"combinazioni"},
    inputs=[{"id":"n","type":"number","step":1,"default":5,"unit":"","unit_options":[],"unit_category":""},{"id":"r","type":"number","step":1,"default":3,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"comb","unit":""}],formula="var n=parseFloat(inputs.n)||0;var r=parseFloat(inputs.r)||0;var num=1;var den=1;for(var i=0;i<r;i++){num*=n-i;den*=i+1;}return{comb:Math.round(num/den)};",
    related=["134","604"],latex_formula="C(n,r) = \\binom{n}{r} = \\frac{n!}{r!(n-r)!}",
    i18n=i18n("Combinaciones","Combinations Calculator","Combinaisons","Combinações","Kombinationen","Combinazioni","Calcula las combinaciones de n elementos tomados de r en r.","Calculate combinations of n items taken r at a time.","Calculez les combinaisons de n éléments pris r à r.","Calcule as combinações de n itens tomados r de cada vez.","Berechnen Sie Kombinationen von n Elementen, r auf einmal.","Calcola le combinazioni di n elementi presi r alla volta.",
        {"n":"n total","r":"r seleccionados"},{"n":"n total","r":"r chosen"},{"n":"n total","r":"r choisis"},{"n":"n total","r":"r escolhidos"},{"n":"n gesamt","r":"r ausgewählt"},{"n":"n totale","r":"r scelti"},
        {"comb":"Combinaciones"},{"comb":"Combinations"},{"comb":"Combinaisons"},{"comb":"Combinações"},{"comb":"Kombinationen"},{"comb":"Combinazioni"}),
    use_cases=[{"en":"Lottery Odds","en_body":"Players calculate C(n,r) to know the exact probability of matching r numbers from a pool of n."},{"en":"Poker Hands","en_body":"Probability textbooks derive royal flush odds by counting combinations of 5 cards from a 52-card deck."},{"en":"Clinical Trials","en_body":"Statisticians compute how many ways to choose control and treatment groups from a patient pool."}],
    steps=[{"en":"Enter the total number of items n."},{"en":"Enter how many items r to choose."},{"en":"The calculator returns C(n,r)."}])

add(id="136",block="matematicas",cat="A",domain="math",concept="standard deviation",
    slugs={"es":"desviacion-estandar","en":"standard-deviation","fr":"ecart-type","pt":"desvio-padrao","de":"standardabweichung","it":"deviazione-standard"},
    inputs=[{"id":"values","type":"text","default":"2,4,4,4,5,5,7,9","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"sd","unit":""},{"id":"mean","unit":""},{"id":"n","unit":""}],
    formula="var vals=(inputs.values||'').split(',').map(function(v){return parseFloat(v.trim());}).filter(function(v){return !isNaN(v);});var n=vals.length;if(n<2)return{sd:0,mean:0,n:0};var mean=vals.reduce(function(a,b){return a+b;},0)/n;var variance=vals.reduce(function(a,b){return a+Math.pow(b-mean,2);},0)/(n-1);return{sd:Math.sqrt(variance).toFixed(4),mean:mean.toFixed(4),n:n};",
    related=["137","608"],latex_formula="s = \\sqrt{\\frac{1}{n-1} \\sum_{i=1}^{n} (x_i - \\bar{x})^2}",
    i18n=i18n("Desviación Estándar","Standard Deviation Calculator","Écart-Type","Desvio Padrão","Standardabweichung","Deviazione Standard","Calcula la desviación estándar de un conjunto de datos.","Calculate the standard deviation of a dataset.","Calculez l'écart-type d'un ensemble de données.","Calcule o desvio padrão de um conjunto de dados.","Berechnen Sie die Standardabweichung eines Datensatzes.","Calcola la deviazione standard di un dataset.",
        {"values":"Valores separados por coma"},{"values":"Comma-separated values"},{"values":"Valeurs séparées par des virgules"},{"values":"Valores separados por vírgula"},{"values":"Durch Kommas getrennte Werte"},{"values":"Valori separati da virgole"},
        {"sd":"Desviación estándar","mean":"Media","n":"N"},{"sd":"Std dev","mean":"Mean","n":"N"},{"sd":"Écart-type","mean":"Moyenne","n":"N"},{"sd":"Desvio padrão","mean":"Média","n":"N"},{"sd":"Stdabw","mean":"Mittelwert","n":"N"},{"sd":"Dev std","mean":"Media","n":"N"}),
    use_cases=[{"en":"Quality Control","en_body":"Manufacturers monitor process standard deviation to detect when machine tolerances drift beyond acceptable limits."},{"en":"Finance Risk","en_body":"Portfolio managers use standard deviation of returns as the primary measure of investment volatility."},{"en":"Scientific Reproducibility","en_body":"Researchers report standard deviations to show the spread of replicate measurements around the mean."}],
    steps=[{"en":"Enter comma-separated numbers."},{"en":"The calculator returns sample standard deviation, mean, and count."}])

add(id="137",block="matematicas",cat="A",domain="math",concept="variance",
    slugs={"es":"varianza","en":"variance-calculator","fr":"variance","pt":"variancia","de":"varianz","it":"varianza"},
    inputs=[{"id":"values","type":"text","default":"2,4,4,4,5,5,7,9","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"variance","unit":""},{"id":"mean","unit":""}],formula="var vals=(inputs.values||'').split(',').map(function(v){return parseFloat(v.trim());}).filter(function(v){return !isNaN(v);});var n=vals.length;if(n<2)return{variance:0,mean:0};var mean=vals.reduce(function(a,b){return a+b;},0)/n;var varian=vals.reduce(function(a,b){return a+Math.pow(b-mean,2);},0)/(n-1);return{variance:varian.toFixed(4),mean:mean.toFixed(4)};",
    related=["136","608"],latex_formula="s^2 = \\frac{1}{n-1} \\sum_{i=1}^{n} (x_i - \\bar{x})^2",
    i18n=i18n("Varianza","Variance Calculator","Variance","Variância","Varianz","Varianza","Calcula la varianza muestral de un conjunto de datos.","Calculate the sample variance of a dataset.","Calculez la variance d'un ensemble de données.","Calcule a variância amostral de um conjunto de dados.","Berechnen Sie die Stichprobenvarianz eines Datensatzes.","Calcola la varianza campionaria di un dataset.",
        {"values":"Valores separados por coma"},{"values":"Comma-separated values"},{"values":"Valeurs séparées par des virgules"},{"values":"Valores separados por vírgula"},{"values":"Durch Kommas getrennte Werte"},{"values":"Valori separati da virgole"},
        {"variance":"Varianza","mean":"Media"},{"variance":"Variance","mean":"Mean"},{"variance":"Variance","mean":"Moyenne"},{"variance":"Variância","mean":"Média"},{"variance":"Varianz","mean":"Mittelwert"},{"variance":"Varianza","mean":"Media"}),
    use_cases=[{"en":"ANOVA","en_body":"Analysis of variance partitions total variance into between-group and within-group components to test hypotheses."},{"en":"Genetics","en_body":"Heritability estimates rely on variance components to determine how much trait variation is genetic versus environmental."},{"en":"Meteorology","en_body":"Climate scientists analyze temperature variance to detect increasing weather instability over decades."}],
    steps=[{"en":"Enter comma-separated numbers."},{"en":"The calculator returns sample variance and mean."}])

add(id="138",block="matematicas",cat="A",domain="math",concept="median",
    slugs={"es":"mediana","en":"median-calculator","fr":"mediane","pt":"mediana","de":"median","it":"mediana"},
    inputs=[{"id":"values","type":"text","default":"1,3,5,7,9","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"median","unit":""},{"id":"sorted","unit":""}],formula="var vals=(inputs.values||'').split(',').map(function(v){return parseFloat(v.trim());}).filter(function(v){return !isNaN(v);});vals.sort(function(a,b){return a-b;});var n=vals.length;var med=n%2===1?vals[Math.floor(n/2)]:(vals[n/2-1]+vals[n/2])/2;return{median:med.toFixed(4),sorted:vals.join(', ')};",
    related=["137","601"],latex_formula="\\text{Median} = \\begin{cases} x_{(n+1)/2} & n \\text{ odd} \\\\ \\frac{1}{2}(x_{n/2} + x_{n/2+1}) & n \\text{ even} \\end{cases}",
    i18n=i18n("Mediana","Median Calculator","Médiane","Mediana","Median","Mediana","Calcula la mediana de un conjunto de datos.","Calculate the median of a dataset.","Calculez la médiane d'un ensemble de données.","Calcule a mediana de um conjunto de dados.","Berechnen Sie den Median eines Datensatzes.","Calcola la mediana di un dataset.",
        {"values":"Valores separados por coma"},{"values":"Comma-separated values"},{"values":"Valeurs séparées par des virgules"},{"values":"Valores separados por vírgula"},{"values":"Durch Kommas getrennte Werte"},{"values":"Valori separati da virgole"},
        {"median":"Mediana","sorted":"Ordenados"},{"median":"Median","sorted":"Sorted"},{"median":"Médiane","sorted":"Triés"},{"median":"Mediana","sorted":"Ordenados"},{"median":"Median","sorted":"Sortiert"},{"median":"Mediana","sorted":"Ordinati"}),
    use_cases=[{"en":"Income Analysis","en_body":"Economists prefer median income over mean because it is robust against billionaire outliers."},{"en":"Real Estate","en_body":"Home price medians better represent typical affordability than averages skewed by luxury listings."},{"en":"Clinical Trials","en_body":"Survival analysis reports median time-to-event because distributions are often right-skewed."}],
    steps=[{"en":"Enter comma-separated numbers."},{"en":"The calculator sorts the data and returns the median value."}])

add(id="139",block="matematicas",cat="A",domain="math",concept="quartiles",
    slugs={"es":"cuartiles","en":"quartile-calculator","fr":"quartiles","pt":"quartis","de":"quartile","it":"quartili"},
    inputs=[{"id":"values","type":"text","default":"1,2,3,4,5,6,7,8,9,10","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"q1","unit":""},{"id":"q2","unit":""},{"id":"q3","unit":""},{"id":"iqr","unit":""}],formula="var vals=(inputs.values||'').split(',').map(function(v){return parseFloat(v.trim());}).filter(function(v){return !isNaN(v);});vals.sort(function(a,b){return a-b;});var n=vals.length;var getQ=function(p){var pos=(n-1)*p+1;var base=Math.floor(pos)-1;var rest=pos-base-1;if(base+1>=n)return vals[n-1];return vals[base]+rest*(vals[base+1]-vals[base]);};return{q1:getQ(0.25).toFixed(4),q2:getQ(0.5).toFixed(4),q3:getQ(0.75).toFixed(4),iqr:(getQ(0.75)-getQ(0.25)).toFixed(4)};",
    related=["138","136"],latex_formula="Q_1 = P_{25}, \\quad Q_2 = P_{50}, \\quad Q_3 = P_{75}, \\quad \\text{IQR} = Q_3 - Q_1",
    i18n=i18n("Cuartiles","Quartile Calculator","Quartiles","Quartis","Quartile","Quartili","Calcula los cuartiles e IQR de un conjunto de datos.","Calculate quartiles and IQR of a dataset.","Calculez les quartiles et l'écart interquartile.","Calcule os quartis e IQR de um conjunto de dados.","Berechnen Sie Quartile und IQR eines Datensatzes.","Calcola i quartili e l'IQR di un dataset.",
        {"values":"Valores separados por coma"},{"values":"Comma-separated values"},{"values":"Valeurs séparées par des virgules"},{"values":"Valores separados por vírgula"},{"values":"Durch Kommas getrennte Werte"},{"values":"Valori separati da virgole"},
        {"q1":"Q1","q2":"Q2 (Mediana)","q3":"Q3","iqr":"IQR"},{"q1":"Q1","q2":"Q2 (Median)","q3":"Q3","iqr":"IQR"},{"q1":"Q1","q2":"Q2 (Médiane)","q3":"Q3","iqr":"IQR"},{"q1":"Q1","q2":"Q2 (Mediana)","q3":"Q3","iqr":"IQR"},{"q1":"Q1","q2":"Q2 (Median)","q3":"Q3","iqr":"IQR"},{"q1":"Q1","q2":"Q2 (Mediana)","q3":"Q3","iqr":"IQR"}),
    use_cases=[{"en":"Box Plots","en_body":"Data scientists use quartiles to construct box plots that visualize spread and detect outliers."},{"en":"Salary Benchmarking","en_body":"HR departments report Q1, median, and Q3 to show pay ranges without revealing individual salaries."},{"en":"Outlier Detection","en_body":"Values beyond Q3 + 1.5×IQR or below Q1 - 1.5×IQR are flagged as statistical outliers."}],
    steps=[{"en":"Enter comma-separated numbers."},{"en":"The calculator returns Q1, Q2 (median), Q3, and IQR."}])

# ── PHYSICS (140-149) ──
add(id="140",block="ciencia",cat="E",domain="physics",concept="Bernoulli equation",
    slugs={"es":"ecuacion-bernoulli","en":"bernoulli-equation","fr":"equation-bernoulli","pt":"equacao-bernoulli","de":"bernoulli-gleichung","it":"equazione-bernoulli"},
    inputs=[{"id":"p1","type":"number","step":"any","default":100000,"unit":"Pa","unit_options":["Pa","kPa","bar","psi"],"unit_category":"pressure"},{"id":"v1","type":"number","step":"any","default":2,"unit":"m/s","unit_options":["m/s","km/h","mph"],"unit_category":"velocity"},{"id":"h1","type":"number","step":"any","default":0,"unit":"m","unit_options":["m","ft","cm"],"unit_category":"length"},{"id":"p2","type":"number","step":"any","default":80000,"unit":"Pa","unit_options":["Pa","kPa","bar","psi"],"unit_category":"pressure"},{"id":"h2","type":"number","step":"any","default":5,"unit":"m","unit_options":["m","ft","cm"],"unit_category":"length"}],
    outputs=[{"id":"v2","unit":"m/s"}],formula="var p1=parseFloat(inputs.p1)||0;var v1=parseFloat(inputs.v1)||0;var h1=parseFloat(inputs.h1)||0;var p2=parseFloat(inputs.p2)||0;var h2=parseFloat(inputs.h2)||0;var rho=1000;var g=9.80665;var term=p1+0.5*rho*v1*v1+rho*g*h1-p2-rho*g*h2;var v2=Math.sqrt(2*term/rho);return{v2:v2.toFixed(4)};",
    related=["141","129"],latex_formula="p_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = p_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
    i18n=i18n("Ecuación de Bernoulli","Bernoulli Equation Calculator","Équation de Bernoulli","Equação de Bernoulli","Bernoulli-Gleichung","Equazione di Bernoulli","Calcula la velocidad del fluido usando la ecuación de Bernoulli.","Calculate fluid velocity using Bernoulli's equation.","Calculez la vitesse du fluide avec l'équation de Bernoulli.","Calcule a velocidade do fluido usando a equação de Bernoulli.","Berechnen Sie die Fluidgeschwindigkeit mit der Bernoulli-Gleichung.","Calcola la velocità del fluido usando l'equazione di Bernoulli.",
        {"p1":"Presión 1","v1":"Velocidad 1","h1":"Altura 1","p2":"Presión 2","h2":"Altura 2"},{"p1":"Pressure 1","v1":"Velocity 1","h1":"Height 1","p2":"Pressure 2","h2":"Height 2"},{"p1":"Pression 1","v1":"Vitesse 1","h1":"Hauteur 1","p2":"Pression 2","h2":"Hauteur 2"},{"p1":"Pressão 1","v1":"Velocidade 1","h1":"Altura 1","p2":"Pressão 2","h2":"Altura 2"},{"p1":"Druck 1","v1":"Geschwindigkeit 1","h1":"Höhe 1","p2":"Druck 2","h2":"Höhe 2"},{"p1":"Pressione 1","v1":"Velocità 1","h1":"Altezza 1","p2":"Pressione 2","h2":"Altezza 2"},
        {"v2":"Velocidad 2"},{"v2":"Velocity 2"},{"v2":"Vitesse 2"},{"v2":"Velocidade 2"},{"v2":"Geschwindigkeit 2"},{"v2":"Velocità 2"}),
    use_cases=[{"en":"Aircraft Wings","en_body":"Aeronautical engineers use Bernoulli's principle to explain lift generation as air flows faster over the curved upper surface."},{"en":"Venturi Meters","en_body":"Fluid mechanics labs measure flow rates by constricting pipes and observing pressure drops via Bernoulli."},{"en":"Spray Bottles","en_body":"Trigger sprayers create low pressure over a tube by forcing air past an opening, drawing liquid upward."}],
    steps=[{"en":"Enter pressure, velocity, and height at point 1."},{"en":"Enter pressure and height at point 2."},{"en":"The calculator solves for velocity at point 2."}])

add(id="141",block="ciencia",cat="E",domain="physics",concept="Doppler effect",
    slugs={"es":"efecto-doppler","en":"doppler-effect","fr":"effet-doppler","pt":"efeito-doppler","de":"doppler-effekt","it":"effetto-doppler"},
    inputs=[{"id":"f0","type":"number","step":"any","default":440,"unit":"Hz","unit_options":["Hz","kHz"],"unit_category":"frequency"},{"id":"v_source","type":"number","step":"any","default":30,"unit":"m/s","unit_options":["m/s","km/h","mph"],"unit_category":"velocity"},{"id":"v_observer","type":"number","step":"any","default":0,"unit":"m/s","unit_options":["m/s","km/h","mph"],"unit_category":"velocity"},{"id":"v_sound","type":"number","step":"any","default":343,"unit":"m/s","unit_options":["m/s","km/h","mph"],"unit_category":"velocity"}],
    outputs=[{"id":"f_obs","unit":"Hz"}],formula="var f0=parseFloat(inputs.f0)||0;var vs=parseFloat(inputs.v_source)||0;var vo=parseFloat(inputs.v_observer)||0;var c=parseFloat(inputs.v_sound)||343;var f=f0*(c+vo)/(c-vs);return{f_obs:f.toFixed(2)};",
    related=["125","140"],latex_formula="f_{obs} = f_0 \\frac{v_{sound} + v_{observer}}{v_{sound} - v_{source}}",
    i18n=i18n("Efecto Doppler","Doppler Effect Calculator","Effet Doppler","Efeito Doppler","Doppler-Effekt","Effetto Doppler","Calcula la frecuencia observada debida al movimiento relativo.","Calculate observed frequency due to relative motion.","Calculez la fréquence observée due au mouvement relatif.","Calcule a frequência observada devido ao movimento relativo.","Berechnen Sie die beobachtete Frequenz aufgrund relativer Bewegung.","Calcola la frequenza osservata dovuta al moto relativo.",
        {"f0":"Frecuencia emisión","v_source":"Velocidad fuente","v_observer":"Velocidad observador","v_sound":"Velocidad sonido"},{"f0":"Source frequency","v_source":"Source velocity","v_observer":"Observer velocity","v_sound":"Speed of sound"},{"f0":"Fréquence émission","v_source":"Vitesse source","v_observer":"Vitesse observateur","v_sound":"Vitesse du son"},{"f0":"Frequência emissão","v_source":"Velocidade fonte","v_observer":"Velocidade observador","v_sound":"Velocidade do som"},{"f0":"Quellfrequenz","v_source":"Quellgeschwindigkeit","v_observer":"Beobachtergeschwindigkeit","v_sound":"Schallgeschwindigkeit"},{"f0":"Frequenza sorgente","v_source":"Velocità sorgente","v_observer":"Velocità osservatore","v_sound":"Velocità suono"},
        {"f_obs":"Frecuencia observada"},{"f_obs":"Observed frequency"},{"f_obs":"Fréquence observée"},{"f_obs":"Frequência observada"},{"f_obs":"Beobachtete Frequenz"},{"f_obs":"Frequenza osservata"}),
    use_cases=[{"en":"Radar Guns","en_body":"Police speed detectors bounce radio waves off moving vehicles and measure Doppler-shifted reflections."},{"en":"Medical Ultrasound","en_body":"Color Doppler imaging visualizes blood flow direction and velocity by detecting frequency shifts in echoes."},{"en":"Astronomy","en_body":"Redshift measurements of distant galaxies confirm cosmic expansion through the Doppler effect."}],
    steps=[{"en":"Enter the source frequency."},{"en":"Enter velocities of source, observer, and sound."},{"en":"The calculator returns the observed frequency."}])

add(id="142",block="ciencia",cat="E",domain="physics",concept="Snell's law",
    slugs={"es":"ley-snell","en":"snells-law","fr":"loi-de-snell","pt":"lei-de-snell","de":"snellius-gesetz","it":"legge-di-snell"},
    inputs=[{"id":"n1","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},{"id":"theta1","type":"number","step":"any","default":30,"unit":"deg","unit_options":["deg","rad"],"unit_category":"angle"},{"id":"n2","type":"number","step":"any","default":1.5,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"theta2","unit":"deg"}],formula="var n1=parseFloat(inputs.n1)||1;var t1=(parseFloat(inputs.theta1)||0)*Math.PI/180;var n2=parseFloat(inputs.n2)||1;var t2=Math.asin(n1*Math.sin(t1)/n2);return{theta2:(t2*180/Math.PI).toFixed(4)};",
    related=["126","141"],latex_formula="n_1 \\sin(\\theta_1) = n_2 \\sin(\\theta_2)",
    i18n=i18n("Ley de Snell","Snell's Law Calculator","Loi de Snell","Lei de Snell","Snellius-Gesetz","Legge di Snell","Calcula el ángulo de refracción entre dos medios.","Calculate the refraction angle between two media.","Calculez l'angle de réfraction entre deux milieux.","Calcule o ângulo de refração entre dois meios.","Berechnen Sie den Brechungswinkel zwischen zwei Medien.","Calcola l'angolo di rifrazione tra due mezzi.",
        {"n1":"Índice 1","theta1":"Ángulo incidencia","n2":"Índice 2"},{"n1":"Index 1","theta1":"Incident angle","n2":"Index 2"},{"n1":"Indice 1","theta1":"Angle incident","n2":"Indice 2"},{"n1":"Índice 1","theta1":"Ângulo incidência","n2":"Índice 2"},{"n1":"Index 1","theta1":"Einfallswinkel","n2":"Index 2"},{"n1":"Indice 1","theta1":"Angolo incidenza","n2":"Indice 2"},
        {"theta2":"Ángulo refracción"},{"theta2":"Refraction angle"},{"theta2":"Angle de réfraction"},{"theta2":"Ângulo refração"},{"theta2":"Brechungswinkel"},{"theta2":"Angolo rifrazione"}),
    use_cases=[{"en":"Fiber Optics","en_body":"Telecom engineers choose core and cladding refractive indices to ensure total internal reflection guides light."},{"en":"Eyeglasses","en_body":"Ophthalmologists specify lens materials with refractive indices that minimize thickness for a given prescription."},{"en":"Diamond Brilliance","en_body":"Gemologists exploit diamond's high refractive index (2.42) to maximize light return and fire."}],
    steps=[{"en":"Enter refractive index of first medium."},{"en":"Enter incident angle."},{"en":"Enter refractive index of second medium."}])

add(id="143",block="ciencia",cat="E",domain="physics",concept="Coulomb force",
    slugs={"es":"fuerza-coulomb","en":"coulomb-force","fr":"force-coulomb","pt":"forca-coulomb","de":"coulomb-kraft","it":"forza-coulomb"},
    inputs=[{"id":"q1","type":"number","step":"any","default":1e-6,"unit":"C","unit_options":["C","µC","nC"],"unit_category":"current"},{"id":"q2","type":"number","step":"any","default":1e-6,"unit":"C","unit_options":["C","µC","nC"],"unit_category":"current"},{"id":"r","type":"number","step":"any","default":0.1,"unit":"m","unit_options":["m","cm","mm"],"unit_category":"length"}],
    outputs=[{"id":"force","unit":"N"}],formula="var k=8.9875e9;var q1=parseFloat(inputs.q1)||0;var q2=parseFloat(inputs.q2)||0;var r=parseFloat(inputs.r)||1;var f=k*q1*q2/(r*r);return{force:f.toExponential(4)};",
    related=["122","144"],latex_formula="F = k_e \\frac{q_1 q_2}{r^2}, \\quad k_e = 8.9875 \\times 10^9 \\text{ N·m}^2/\\text{C}^2",
    i18n=i18n("Fuerza de Coulomb","Coulomb Force Calculator","Force de Coulomb","Força de Coulomb","Coulomb-Kraft","Forza di Coulomb","Calcula la fuerza electrostática entre dos cargas.","Calculate the electrostatic force between two charges.","Calculez la force électrostatique entre deux charges.","Calcule a força eletrostática entre duas cargas.","Berechnen Sie die elektrostatische Kraft zwischen zwei Ladungen.","Calcola la forza elettrostatica tra due cariche.",
        {"q1":"Carga 1","q2":"Carga 2","r":"Distancia"},{"q1":"Charge 1","q2":"Charge 2","r":"Distance"},{"q1":"Charge 1","q2":"Charge 2","r":"Distance"},{"q1":"Carga 1","q2":"Carga 2","r":"Distância"},{"q1":"Ladung 1","q2":"Ladung 2","r":"Abstand"},{"q1":"Carica 1","q2":"Carica 2","r":"Distanza"},
        {"force":"Fuerza"},{"force":"Force"},{"force":"Force"},{"force":"Força"},{"force":"Kraft"},{"force":"Forza"}),
    use_cases=[{"en":"Ion Traps","en_body":"Quantum physicists use Coulomb repulsion to suspend ions in electromagnetic traps for quantum computing."},{"en":"Electrostatic Precipitators","en_body":"Environmental engineers remove particulate pollution by charging particles and attracting them to oppositely charged plates."},{"en":"Capacitor Design","en_body":"Engineers calculate forces between capacitor plates to ensure mechanical stability under high voltage."}],
    steps=[{"en":"Enter the two charges in coulombs."},{"en":"Enter the distance between them."},{"en":"The calculator returns the Coulomb force."}])

add(id="144",block="ciencia",cat="E",domain="physics",concept="magnetic force on charge",
    slugs={"es":"fuerza-magnetica-carga","en":"magnetic-force-charge","fr":"force-magnetique-charge","pt":"forca-magnetica-carga","de":"magnetische-kraft-ladung","it":"forza-magnetica-carica"},
    inputs=[{"id":"q","type":"number","step":"any","default":1e-6,"unit":"C","unit_options":["C","µC"],"unit_category":"current"},{"id":"v","type":"number","step":"any","default":1000,"unit":"m/s","unit_options":["m/s","km/h"],"unit_category":"velocity"},{"id":"B","type":"number","step":"any","default":0.5,"unit":"T","unit_options":["T","mT"],"unit_category":""},{"id":"theta","type":"number","step":"any","default":90,"unit":"deg","unit_options":["deg","rad"],"unit_category":"angle"}],
    outputs=[{"id":"force","unit":"N"}],formula="var q=parseFloat(inputs.q)||0;var v=parseFloat(inputs.v)||0;var B=parseFloat(inputs.B)||0;var theta=(parseFloat(inputs.theta)||0)*Math.PI/180;var f=q*v*B*Math.sin(theta);return{force:f.toExponential(4)};",
    related=["143","707"],latex_formula="F = qvB \\sin(\\theta)",
    i18n=i18n("Fuerza Magnética sobre Carga","Magnetic Force on Charge Calculator","Force Magnétique sur Charge","Força Magnética sobre Carga","Magnetische Kraft auf Ladung","Forza Magnetica su Carica","Calcula la fuerza magnética sobre una carga en movimiento.","Calculate the magnetic force on a moving charge.","Calculez la force magnétique sur une charge en mouvement.","Calcule a força magnética sobre uma carga em movimento.","Berechnen Sie die magnetische Kraft auf eine bewegte Ladung.","Calcola la forza magnetica su una carica in movimento.",
        {"q":"Carga","v":"Velocidad","B":"Campo magnético","theta":"Ángulo"},{"q":"Charge","v":"Velocity","B":"Magnetic field","theta":"Angle"},{"q":"Charge","v":"Vitesse","B":"Champ magnétique","theta":"Angle"},{"q":"Carga","v":"Velocidade","B":"Campo magnético","theta":"Ângulo"},{"q":"Ladung","v":"Geschwindigkeit","B":"Magnetfeld","theta":"Winkel"},{"q":"Carica","v":"Velocità","B":"Campo magnetico","theta":"Angolo"},
        {"force":"Fuerza"},{"force":"Force"},{"force":"Force"},{"force":"Força"},{"force":"Kraft"},{"force":"Forza"}),
    use_cases=[{"en":"Mass Spectrometry","en_body":"Chemists separate ions by mass using magnetic fields that deflect charged particles along curved trajectories."},{"en":"Cyclotrons","en_body":"Particle physicists accelerate protons in circular paths by applying perpendicular magnetic fields."},{"en":"Hall Effect Sensors","en_body":"Automotive engineers measure current indirectly by detecting the magnetic force on charge carriers."}],
    steps=[{"en":"Enter charge, velocity, and magnetic field strength."},{"en":"Enter the angle between velocity and field."},{"en":"The calculator returns F = qvB sin(θ)."}])

add(id="145",block="ciencia",cat="E",domain="physics",concept="thermal expansion",
    slugs={"es":"dilatacion-termica","en":"thermal-expansion","fr":"dilatation-thermique","pt":"dilatacao-termica","de":"waermeausdehnung","it":"dilatazione-termica"},
    inputs=[{"id":"L0","type":"number","step":"any","default":10,"unit":"m","unit_options":["m","cm","mm","ft"],"unit_category":"length"},{"id":"alpha","type":"number","step":"any","default":12e-6,"unit":"/K","unit_options":["/K","/°C"],"unit_category":""},{"id":"dt","type":"number","step":"any","default":50,"unit":"K","unit_options":["K","°C"],"unit_category":"temperature"}],
    outputs=[{"id":"dL","unit":"m"},{"id":"L_final","unit":"m"}],formula="var L0=parseFloat(inputs.L0)||0;var alpha=parseFloat(inputs.alpha)||0;var dt=parseFloat(inputs.dt)||0;var dL=L0*alpha*dt;var Lf=L0+dL;return{dL:dL.toFixed(6),L_final:Lf.toFixed(6)};",
    related=["124","955"],latex_formula="\\Delta L = \\alpha L_0 \\Delta T",
    i18n=i18n("Dilatación Térmica","Thermal Expansion Calculator","Dilatation Thermique","Dilatação Térmica","Wärmeausdehnung","Dilatazione Termica","Calcula la expansión lineal de un sólido al calentarse.","Calculate linear expansion of a solid when heated.","Calculez la dilatation linéaire d'un solide chauffé.","Calcule a expansão linear de um sólido ao aquecer.","Berechnen Sie die lineare Ausdehnung eines festen Körpers beim Erwärmen.","Calcola la dilatazione lineare di un solido riscaldato.",
        {"L0":"Longitud inicial","alpha":"Coef. dilatación","dt":"Cambio temp"},{"L0":"Initial length","alpha":"Expansion coeff","dt":"Temp change"},{"L0":"Longueur initiale","alpha":"Coeff dilatation","dt":"Variation temp"},{"L0":"Comprimento inicial","alpha":"Coef expansão","dt":"Variação temp"},{"L0":"Anfangslänge","alpha":"Ausdehnungskoeff","dt":"Temperaturänderung"},{"L0":"Lunghezza iniziale","alpha":"Coeff dilatazione","dt":"Variazione temp"},
        {"dL":"Cambio longitud","L_final":"Longitud final"},{"dL":"Length change","L_final":"Final length"},{"dL":"Changement longueur","L_final":"Longueur finale"},{"dL":"Mudança comprimento","L_final":"Comprimento final"},{"dL":"Längenänderung","L_final":"Endlänge"},{"dL":"Variazione lunghezza","L_final":"Lunghezza finale"}),
    use_cases=[{"en":"Railway Tracks","en_body":"Civil engineers leave expansion gaps between rail segments to prevent buckling under summer heat."},{"en":"Bridge Design","en_body":"Suspension bridges incorporate roller bearings that accommodate thermal length changes across seasons."},{"en":"Precision Instruments","en_body":"Metrologists correct micrometer readings for thermal expansion when measuring at non-standard temperatures."}],
    steps=[{"en":"Enter the initial length."},{"en":"Enter the linear expansion coefficient."},{"en":"Enter the temperature change."}])

add(id="146",block="ciencia",cat="E",domain="physics",concept="Stefan-Boltzmann law",
    slugs={"es":"ley-stefan-boltzmann","en":"stefan-boltzmann-law","fr":"loi-stefan-boltzmann","pt":"lei-stefan-boltzmann","de":"stefan-boltzmann-gesetz","it":"legge-stefan-boltzmann"},
    inputs=[{"id":"T","type":"number","step":"any","default":300,"unit":"K","unit_options":["K","°C","°F"],"unit_category":"temperature"},{"id":"area","type":"number","step":"any","default":1,"unit":"m²","unit_options":["m²","cm²"],"unit_category":"area"},{"id":"emissivity","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"power","unit":"W"}],formula="var sigma=5.670374e-8;var T=parseFloat(inputs.T)||0;var A=parseFloat(inputs.area)||0;var eps=parseFloat(inputs.emissivity)||0;var P=sigma*eps*A*Math.pow(T,4);return{power:P.toFixed(4)};",
    related=["124","145"],latex_formula="P = \\varepsilon \\sigma A T^4, \\quad \\sigma = 5.670374 \\times 10^{-8} \\text{ W/m}^2\\text{K}^4",
    i18n=i18n("Ley de Stefan-Boltzmann","Stefan-Boltzmann Law Calculator","Loi de Stefan-Boltzmann","Lei de Stefan-Boltzmann","Stefan-Boltzmann-Gesetz","Legge di Stefan-Boltzmann","Calcula la potencia radiada por un cuerpo negro.","Calculate radiated power from a black body.","Calculez la puissance rayonnée par un corps noir.","Calcule a potência radiada por um corpo negro.","Berechnen Sie die Strahlungsleistung eines Schwarzen Körpers.","Calcola la potenza irradiata da un corpo nero.",
        {"T":"Temperatura","area":"Área","emissivity":"Emisividad"},{"T":"Temperature","area":"Area","emissivity":"Emissivity"},{"T":"Température","area":"Surface","emissivity":"Émissivité"},{"T":"Temperatura","area":"Área","emissivity":"Emissividade"},{"T":"Temperatur","area":"Fläche","emissivity":"Emissionsgrad"},{"T":"Temperatura","area":"Area","emissivity":"Emissività"},
        {"power":"Potencia radiada"},{"power":"Radiated power"},{"power":"Puissance rayonnée"},{"power":"Potência radiada"},{"power":"Strahlungsleistung"},{"power":"Potenza irradiata"}),
    use_cases=[{"en":"Star Luminosity","en_body":"Astrophysicists estimate stellar luminosities by applying Stefan-Boltzmann to measured surface temperatures and radii."},{"en":"Thermal Imaging","en_body":"Infrared cameras convert detected radiance to temperature using emissivity-corrected Stefan-Boltzmann equations."},{"en":"Radiator Sizing","en_body":"HVAC engineers calculate how much surface area a hot-water radiator needs to heat a room."}],
    steps=[{"en":"Enter surface temperature in Kelvin."},{"en":"Enter surface area."},{"en":"Enter emissivity (0-1, 1 for ideal blackbody)."}])

add(id="147",block="ciencia",cat="E",domain="physics",concept="RL circuit time constant",
    slugs={"es":"circuito-rl","en":"rl-circuit","fr":"circuit-rl","pt":"circuito-rl","de":"rl-schaltung","it":"circuito-rl"},
    inputs=[{"id":"L","type":"number","step":"any","default":1,"unit":"H","unit_options":["H","mH"],"unit_category":""},{"id":"R","type":"number","step":"any","default":10,"unit":"ohm","unit_options":["ohm","kohm"],"unit_category":"resistance"}],
    outputs=[{"id":"tau","unit":"s"},{"id":"current_final","unit":"A"}],formula="var L=parseFloat(inputs.L)||0;var R=parseFloat(inputs.R)||1;var tau=L/R;var V=10;var If=V/R;return{tau:tau.toFixed(6),current_final:If.toFixed(4)};",
    related=["148","707"],latex_formula="\\tau = \\frac{L}{R}, \\quad I_{final} = \\frac{V}{R}",
    i18n=i18n("Circuito RL","RL Circuit Calculator","Circuit RL","Circuito RL","RL-Schaltung","Circuito RL","Calcula la constante de tiempo de un circuito RL.","Calculate the time constant of an RL circuit.","Calculez la constante de temps d'un circuit RL.","Calcule a constante de tempo de um circuito RL.","Berechnen Sie die Zeitkonstante einer RL-Schaltung.","Calcola la costante di tempo di un circuito RL.",
        {"L":"Inductancia","R":"Resistencia"},{"L":"Inductance","R":"Resistance"},{"L":"Inductance","R":"Résistance"},{"L":"Indutância","R":"Resistência"},{"L":"Induktivität","R":"Widerstand"},{"L":"Induttanza","R":"Resistenza"},
        {"tau":"Constante tiempo","current_final":"Corriente final"},{"tau":"Time constant","current_final":"Final current"},{"tau":"Constante temps","current_final":"Courant final"},{"tau":"Constante tempo","current_final":"Corrente final"},{"tau":"Zeitkonstante","current_final":"Endstrom"},{"tau":"Costante tempo","current_final":"Corrente finale"}),
    use_cases=[{"en":"Relay Timing","en_body":"Electrical engineers select inductors to achieve desired relay pull-in and drop-out delays."},{"en":"DC-DC Converters","en_body":"Power supply designers ensure RL time constants are short enough for adequate switching frequency response."},{"en":"Spark Plug Coils","en_body":"Automotive ignition systems store energy in RL circuits and discharge it rapidly across spark gaps."}],
    steps=[{"en":"Enter inductance L."},{"en":"Enter resistance R."},{"en":"The calculator returns the time constant τ = L/R."}])

add(id="148",block="ciencia",cat="E",domain="physics",concept="RC circuit time constant",
    slugs={"es":"circuito-rc","en":"rc-circuit","fr":"circuit-rc","pt":"circuito-rc","de":"rc-schaltung","it":"circuito-rc"},
    inputs=[{"id":"R","type":"number","step":"any","default":1000,"unit":"ohm","unit_options":["ohm","kohm","Mohm"],"unit_category":"resistance"},{"id":"C","type":"number","step":"any","default":1e-6,"unit":"F","unit_options":["F","µF","nF","pF"],"unit_category":"capacitance"}],
    outputs=[{"id":"tau","unit":"s"},{"id":"freq","unit":"Hz"}],formula="var R=parseFloat(inputs.R)||0;var C=parseFloat(inputs.C)||0;var tau=R*C;var f=1/(2*Math.PI*tau);return{tau:tau.toFixed(6),freq:f.toFixed(4)};",
    related=["147","707"],latex_formula="\\tau = RC, \\quad f_{cutoff} = \\frac{1}{2\\pi RC}",
    i18n=i18n("Circuito RC","RC Circuit Calculator","Circuit RC","Circuito RC","RC-Schaltung","Circuito RC","Calcula la constante de tiempo y frecuencia de corte de un circuito RC.","Calculate the time constant and cutoff frequency of an RC circuit.","Calculez la constante de temps et fréquence de coupure d'un circuit RC.","Calcule a constante de tempo e frequência de corte de um circuito RC.","Berechnen Sie die Zeitkonstante und Grenzfrequenz einer RC-Schaltung.","Calcola la costante di tempo e frequenza di taglio di un circuito RC.",
        {"R":"Resistencia","C":"Capacitancia"},{"R":"Resistance","C":"Capacitance"},{"R":"Résistance","C":"Capacité"},{"R":"Resistência","C":"Capacitância"},{"R":"Widerstand","C":"Kapazität"},{"R":"Resistenza","C":"Capacità"},
        {"tau":"Constante tiempo","freq":"Frecuencia corte"},{"tau":"Time constant","freq":"Cutoff freq"},{"tau":"Constante temps","freq":"Fréq coupure"},{"tau":"Constante tempo","freq":"Freq corte"},{"tau":"Zeitkonstante","freq":"Grenzfrequenz"},{"tau":"Costante tempo","freq":"Frequenza taglio"}),
    use_cases=[{"en":"Audio Filters","en_body":"Audio engineers design high-pass and low-pass filters by choosing R and C for target cutoff frequencies."},{"en":"Camera Flashes","en_body":"Photographers control flash duration by selecting RC combinations that govern capacitor discharge rates."},{"en":"Neuron Modeling","en_body":"Neuroscientists model membrane potential decay using RC time constants to approximate passive cell properties."}],
    steps=[{"en":"Enter resistance R."},{"en":"Enter capacitance C."},{"en":"The calculator returns τ and cutoff frequency."}])

add(id="149",block="ciencia",cat="E",domain="physics",concept="ideal gas law",
    slugs={"es":"ley-gases-ideales","en":"ideal-gas-law","fr":"loi-gaz-parfaits","pt":"lei-gases-ideais","de":"ideale-gasgleichung","it":"legge-gas-ideali"},
    inputs=[{"id":"P","type":"number","step":"any","default":101325,"unit":"Pa","unit_options":["Pa","kPa","atm","bar"],"unit_category":"pressure"},{"id":"V","type":"number","step":"any","default":0.0224,"unit":"m³","unit_options":["m³","L","mL"],"unit_category":"volume"},{"id":"n","type":"number","step":"any","default":1,"unit":"mol","unit_options":["mol"],"unit_category":"count"},{"id":"T","type":"number","step":"any","default":273.15,"unit":"K","unit_options":["K","°C","°F"],"unit_category":"temperature"}],
    outputs=[{"id":"missing","unit":""}],formula="var R=8.314;var P=parseFloat(inputs.P)||0;var V=parseFloat(inputs.V)||0;var n=parseFloat(inputs.n)||0;var T=parseFloat(inputs.T)||0;var result={};if(P===0)result.missing=(n*R*T/V).toFixed(4)+' Pa';else if(V===0)result.missing=(n*R*T/P).toFixed(6)+' m³';else if(n===0)result.missing=(P*V/(R*T)).toFixed(6)+' mol';else if(T===0)result.missing=(P*V/(n*R)).toFixed(4)+' K';else result.missing='Enter 0 for one variable';return result;",
    related=["124","146"],latex_formula="PV = nRT, \\quad R = 8.314 \\text{ J/(mol·K)}",
    i18n=i18n("Ley de Gases Ideales","Ideal Gas Law Calculator","Loi des Gaz Parfaits","Lei dos Gases Ideais","Ideale Gasgleichung","Legge dei Gas Ideali","Calcula la variable desconocida de la ley de gases ideales.","Calculate the unknown variable in the ideal gas law.","Calculez la variable inconnue de la loi des gaz parfaits.","Calcule a variável desconhecida da lei dos gases ideais.","Berechnen Sie die unbekannte Variable der idealen Gasgleichung.","Calcola la variabile sconosciuta della legge dei gas ideali.",
        {"P":"Presión","V":"Volumen","n":"Moles","T":"Temperatura"},{"P":"Pressure","V":"Volume","n":"Moles","T":"Temperature"},{"P":"Pression","V":"Volume","n":"Moles","T":"Température"},{"P":"Pressão","V":"Volume","n":"Mols","T":"Temperatura"},{"P":"Druck","V":"Volumen","n":"Mol","T":"Temperatur"},{"P":"Pressione","V":"Volume","n":"Moli","T":"Temperatura"},
        {"missing":"Variable calculada"},{"missing":"Calculated variable"},{"missing":"Variable calculée"},{"missing":"Variável calculada"},{"missing":"Berechnete Variable"},{"missing":"Variabile calcolata"}),
    use_cases=[{"en":"Scuba Tanks","en_body":"Divers apply the ideal gas law to estimate how long a tank lasts at different depths and temperatures."},{"en":"Weather Balloons","en_body":"Meteorologists predict balloon ascent altitude by modeling gas expansion with decreasing pressure."},{"en":"Aerosol Cans","en_body":"Engineers ensure can pressures remain safe across temperature ranges using gas law predictions."}],
    steps=[{"en":"Enter three known variables (P, V, n, T)."},{"en":"Set the unknown variable to 0."},{"en":"The calculator solves for the missing quantity."}])

# ── FINANCE (330-339) ──
add(id="330",block="finanzas",cat="C",domain="finance",concept="payback period",
    slugs={"es":"periodo-recuperacion","en":"payback-period","fr":"delai-recuperation","pt":"periodo-retorno","de":"amortisationsdauer","it":"periodo-ritorno"},
    inputs=[{"id":"investment","type":"number","step":"any","default":10000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"annual_cash","type":"number","step":"any","default":2500,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"}],
    outputs=[{"id":"payback","unit":"yr"}],formula="var inv=parseFloat(inputs.investment)||0;var cash=parseFloat(inputs.annual_cash)||1;var pb=inv/cash;return{payback:pb.toFixed(2)};",
    related=["320","324"],latex_formula="\\text{Payback} = \\frac{\\text{Initial Investment}}{\\text{Annual Cash Flow}}",
    i18n=i18n("Periodo de Recuperación","Payback Period Calculator","Délai de Récupération","Período de Retorno","Amortisationsdauer","Periodo di Ritorno","Calcula el tiempo para recuperar una inversión.","Calculate the time to recover an investment.","Calculez le délai de récupération d'un investissement.","Calcule o período de retorno de um investimento.","Berechnen Sie die Amortisationsdauer einer Investition.","Calcola il periodo di ritorno di un investimento.",
        {"investment":"Inversión inicial","annual_cash":"Flujo anual"},{"investment":"Initial investment","annual_cash":"Annual cash flow"},{"investment":"Investissement initial","annual_cash":"Flux annuel"},{"investment":"Investimento inicial","annual_cash":"Fluxo anual"},{"investment":"Anfangsinvestition","annual_cash":"Jährlicher Cashflow"},{"investment":"Investimento iniziale","annual_cash":"Flusso annuo"},
        {"payback":"Años"},{"payback":"Years"},{"payback":"Années"},{"payback":"Anos"},{"payback":"Jahre"},{"payback":"Anni"}),
    use_cases=[{"en":"Equipment Purchase","en_body":"Factory managers compare payback periods of competing machines to justify capital expenditures."},{"en":"Solar Panels","en_body":"Homeowners divide installation cost by annual electricity savings to estimate payback time."},{"en":"Software Projects","en_body":"CTOs evaluate whether internal tool development costs will be recovered within two fiscal years."}],
    steps=[{"en":"Enter the total initial investment."},{"en":"Enter the annual net cash inflow."},{"en":"The quotient is the payback period in years."}])

add(id="331",block="finanzas",cat="C",domain="finance",concept="Sharpe ratio",
    slugs={"es":"ratio-sharpe","en":"sharpe-ratio","fr":"ratio-sharpe","pt":"indice-sharpe","de":"sharpe-ratio","it":"indice-sharpe"},
    inputs=[{"id":"return_p","type":"number","step":"any","default":12,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"rf","type":"number","step":"any","default":3,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"sd","type":"number","step":"any","default":15,"unit":"%","unit_options":["%"],"unit_category":"percentage"}],
    outputs=[{"id":"sharpe","unit":""}],formula="var rp=parseFloat(inputs.return_p)||0;var rf=parseFloat(inputs.rf)||0;var sd=parseFloat(inputs.sd)||1;var s=(rp-rf)/sd;return{sharpe:s.toFixed(4)};",
    related=["326","329"],latex_formula="S = \\frac{R_p - R_f}{\\sigma_p}",
    i18n=i18n("Ratio de Sharpe","Sharpe Ratio Calculator","Ratio de Sharpe","Índice de Sharpe","Sharpe-Ratio","Indice di Sharpe","Calcula el ratio de Sharpe de una inversión.","Calculate the Sharpe ratio of an investment.","Calculez le ratio de Sharpe d'un investissement.","Calcule o índice de Sharpe de um investimento.","Berechnen Sie das Sharpe-Ratio einer Investition.","Calcola l'indice di Sharpe di un investimento.",
        {"return_p":"Rendimiento %","rf":"Libre de riesgo %","sd":"Desviación %"},{"return_p":"Return %","rf":"Risk-free %","sd":"Std dev %"},{"return_p":"Rendement %","rf":"Sans risque %","sd":"Écart-type %"},{"return_p":"Retorno %","rf":"Livre de risco %","sd":"Desvio %"},{"return_p":"Rendite %","rf":"Risikofrei %","sd":"Stdabw %"},{"return_p":"Rendimento %","rf":"Risk-free %","sd":"Dev std %"},
        {"sharpe":"Sharpe ratio"},{"sharpe":"Sharpe ratio"},{"sharpe":"Ratio Sharpe"},{"sharpe":"Índice Sharpe"},{"sharpe":"Sharpe-Ratio"},{"sharpe":"Indice Sharpe"}),
    use_cases=[{"en":"Fund Comparison","en_body":"Investors rank mutual funds by Sharpe ratio to identify the best risk-adjusted returns."},{"en":"Portfolio Optimization","en_body":"Quantitative analysts maximize Sharpe ratio to construct efficient frontier portfolios."},{"en":"Hedge Fund Screening","en_body":"Institutional investors require Sharpe ratios above 1.0 as a minimum threshold for capital allocation."}],
    steps=[{"en":"Enter the portfolio return."},{"en":"Enter the risk-free rate."},{"en":"Enter the portfolio standard deviation."}])

add(id="332",block="finanzas",cat="C",domain="finance",concept="tax equivalent yield",
    slugs={"es":"rendimiento-equivalente-impuestos","en":"tax-equivalent-yield","fr":"rendement-equivalent-impo","pt":"rendimento-equivalente-imposto","de":"steueraequivalente-rendite","it":"rendimento-equivalente-tasse"},
    inputs=[{"id":"muni_yield","type":"number","step":"any","default":4,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"tax_rate","type":"number","step":"any","default":25,"unit":"%","unit_options":["%"],"unit_category":"percentage"}],
    outputs=[{"id":"tax_equiv","unit":"%"}],formula="var my=parseFloat(inputs.muni_yield)||0;var tr=parseFloat(inputs.tax_rate)||0;var te=my/(1-tr/100);return{tax_equiv:te.toFixed(4)};",
    related=["325","321"],latex_formula="\\text{TEY} = \\frac{\\text{Municipal Yield}}{1 - \\text{Tax Rate}}",
    i18n=i18n("Rendimiento Equivalente en Impuestos","Tax Equivalent Yield Calculator","Rendement Équivalent Impôt","Rendimento Equivalente Imposto","Steueräquivalente Rendite","Rendimento Equivalente Tasse","Compara bonos municipales exentos de impuestos con bonos gravables.","Compare tax-free municipal bonds to taxable bonds.","Comparez les obligations municipales exonérées aux obligations imposables.","Compare títulos municipais isentos de imposto com títulos tributáveis.","Vergleichen Sie steuerfreie Kommunalanleihen mit steuerpflichtigen Anleihen.","Confronta i titoli municipali esenti da imposta con i titoli tassabili.",
        {"muni_yield":"Rendimiento municipal %","tax_rate":"Impuesto %"},{"muni_yield":"Muni yield %","tax_rate":"Tax rate %"},{"muni_yield":"Rendement municipal %","tax_rate":"Taux d'imposition %"},{"muni_yield":"Rendimento municipal %","tax_rate":"Imposto %"},{"muni_yield":"Kommunalrendite %","tax_rate":"Steuersatz %"},{"muni_yield":"Rendimento municipale %","tax_rate":"Tasse %"},
        {"tax_equiv":"Rendimiento equivalente %"},{"tax_equiv":"Tax equiv yield %"},{"tax_equiv":"Rendement équivalent %"},{"tax_equiv":"Rendimento equivalente %"},{"tax_equiv":"Steueräquiv. Rendite %"},{"tax_equiv":"Rendimento equiv %"}),
    use_cases=[{"en":"Municipal Bond Investing","en_body":"High-income investors in high-tax states use TEY to see that muni yields often beat taxable Treasuries."},{"en":"Retirement Planning","en_body":"Retirees compare TEY across states to decide whether to hold local or out-of-state municipal bonds."},{"en":"Portfolio Rebalancing","en_body":"Advisors swap taxable corporates for municipals when TEY exceeds the after-tax corporate yield."}],
    steps=[{"en":"Enter the municipal bond yield."},{"en":"Enter your marginal tax rate."},{"en":"The calculator returns the taxable-equivalent yield."}])

add(id="333",block="finanzas",cat="C",domain="finance",concept="real rate of return",
    slugs={"es":"tasa-real-retorno","en":"real-rate-return","fr":"taux-reel-rendement","pt":"taxa-real-retorno","de":"reale-rendite","it":"tasso-reale-rendimento"},
    inputs=[{"id":"nominal","type":"number","step":"any","default":8,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"inflation","type":"number","step":"any","default":3,"unit":"%","unit_options":["%"],"unit_category":"percentage"}],
    outputs=[{"id":"real","unit":"%"}],formula="var nom=parseFloat(inputs.nominal)||0;var inf=parseFloat(inputs.inflation)||0;var real=((1+nom/100)/(1+inf/100)-1)*100;return{real:real.toFixed(4)};",
    related=["320","312"],latex_formula="r_{real} = \\frac{1 + r_{nom}}{1 + \\pi} - 1",
    i18n=i18n("Tasa Real de Retorno","Real Rate of Return Calculator","Taux Réel de Rendement","Taxa Real de Retorno","Reale Rendite","Tasso Reale di Rendimento","Calcula el rendimiento real después de la inflación.","Calculate the real return after inflation.","Calculez le rendement réel après inflation.","Calcule o retorno real após inflação.","Berechnen Sie die reale Rendite nach Inflation.","Calcola il rendimento reale dopo l'inflazione.",
        {"nominal":"Rendimiento nominal %","inflation":"Inflación %"},{"nominal":"Nominal return %","inflation":"Inflation %"},{"nominal":"Rendement nominal %","inflation":"Inflation %"},{"nominal":"Retorno nominal %","inflation":"Inflação %"},{"nominal":"Nominale Rendite %","inflation":"Inflation %"},{"nominal":"Rendimento nominale %","inflation":"Inflazione %"},
        {"real":"Retorno real %"},{"real":"Real return %"},{"real":"Rendement réel %"},{"real":"Retorno real %"},{"real":"Reale Rendite %"},{"real":"Rendimento reale %"}),
    use_cases=[{"en":"Retirement Planning","en_body":"Retirees subtract inflation from nominal portfolio returns to see if their purchasing power actually grows."},{"en":"International Investing","en_body":"Global investors adjust foreign equity returns for local inflation and currency depreciation."},{"en":"Wage Negotiations","en_body":"Workers calculate real wage growth by subtracting CPI inflation from nominal raise percentages."}],
    steps=[{"en":"Enter the nominal rate of return."},{"en":"Enter the inflation rate."},{"en":"The calculator returns the inflation-adjusted real return."}])

add(id="334",block="finanzas",cat="C",domain="finance",concept="loan affordability",
    slugs={"es":"prestamo-afordable","en":"loan-affordability","fr":"capacite-emprunt","pt":"capacidade-emprestimo","de":"kreditfaehigkeit","it":"capacita-prestito"},
    inputs=[{"id":"income","type":"number","step":"any","default":5000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"debt_ratio","type":"number","step":"any","default":36,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"rate","type":"number","step":"any","default":5,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"years","type":"number","step":1,"default":30,"unit":"yr","unit_options":["yr","mo"],"unit_category":"time"}],
    outputs=[{"id":"max_loan","unit":"USD"}],formula="var inc=parseFloat(inputs.income)||0;var dr=(parseFloat(inputs.debt_ratio)||0)/100;var r=(parseFloat(inputs.rate)||0)/1200;var n=(parseFloat(inputs.years)||0)*12;var max_payment=inc*dr;var max_loan=r>0?max_payment*(1-Math.pow(1+r,-n))/r:max_payment*n;return{max_loan:max_loan.toFixed(2)};",
    related=["322","300"],latex_formula="\\text{Max Loan} = PMT \\times \\frac{1 - (1+r)^{-n}}{r}, \\quad PMT = \\text{Income} \\times \\text{Debt Ratio}",
    i18n=i18n("Capacidad de Préstamo","Loan Affordability Calculator","Capacité d'Emprunt","Capacidade de Empréstimo","Kreditfähigkeit","Capacità di Prestito","Calcula el préstamo máximo que puedes asumir.","Calculate the maximum loan you can afford.","Calculez le prêt maximum que vous pouvez assumer.","Calcule o empréstimo máximo que pode assumir.","Berechnen Sie den maximalen Kredit, den Sie sich leisten können.","Calcola il prestito massimo che puoi permetterti.",
        {"income":"Ingreso mensual","debt_ratio":"Ratio deuda %","rate":"Tasa %","years":"Años"},{"income":"Monthly income","debt_ratio":"Debt ratio %","rate":"Rate %","years":"Years"},{"income":"Revenu mensuel","debt_ratio":"Ratio dette %","rate":"Taux %","years":"Années"},{"income":"Renda mensal","debt_ratio":"Ratio dívida %","rate":"Taxa %","years":"Anos"},{"income":"Monatliches Einkommen","debt_ratio":"Schuldenquote %","rate":"Zinssatz %","years":"Jahre"},{"income":"Reddito mensile","debt_ratio":"Ratio debito %","rate":"Tasso %","years":"Anni"},
        {"max_loan":"Préstamo máximo"},{"max_loan":"Max loan"},{"max_loan":"Prêt maximum"},{"max_loan":"Empréstimo máximo"},{"max_loan":"Maximaler Kredit"},{"max_loan":"Prestito massimo"}),
    use_cases=[{"en":"Home Shopping","en_body":"Buyers set realistic price ceilings before house hunting by computing their debt-to-income loan limits."},{"en":"Auto Financing","en_body":"Car shoppers determine the maximum vehicle price that keeps monthly payments within their budget."},{"en":"Debt Consolidation","en_body":"Borrowers verify that a consolidation loan won't exceed their affordability threshold."}],
    steps=[{"en":"Enter monthly gross income."},{"en":"Enter maximum debt-to-income ratio."},{"en":"Enter loan rate and term."}])

add(id="335",block="finanzas",cat="C",domain="finance",concept="mortgage payoff",
    slugs={"es":"liquidacion-hipoteca","en":"mortgage-payoff","fr":"remboursement-anticipe","pt":"quitacao-hipoteca","de":"hypothekentilgung","it":"estinzione-mutuo"},
    inputs=[{"id":"balance","type":"number","step":"any","default":200000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"rate","type":"number","step":"any","default":4,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"extra","type":"number","step":"any","default":200,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"}],
    outputs=[{"id":"months_saved","unit":"mo"},{"id":"interest_saved","unit":"USD"}],formula="var bal=parseFloat(inputs.balance)||0;var r=(parseFloat(inputs.rate)||0)/1200;var extra=parseFloat(inputs.extra)||0;var term=360;var pmt=bal*r/(1-Math.pow(1+r,-term));var months=0;var total_int_normal=pmt*term-bal;var total_int_extra=0;var b=bal;while(b>0&&months<1000){var interest=b*r;var principal=pmt+extra-interest;if(principal<=0)break;b-=principal;months++;total_int_extra+=interest;}return{months_saved:(term-months).toFixed(0),interest_saved:(total_int_normal-total_int_extra).toFixed(2)};",
    related=["300","334"],latex_formula="\\text{Interest Saved} = \\text{Total Interest}_{normal} - \\text{Total Interest}_{extra}",
    i18n=i18n("Liquidación Anticipada de Hipoteca","Mortgage Payoff Calculator","Remboursement Anticipé","Quitação de Hipoteca","Hypothekentilgung","Estinzione Anticipata Mutuo","Calcula cuánto ahorras pagando extra en tu hipoteca.","Calculate savings from extra mortgage payments.","Calculez les économies avec des remboursements anticipés.","Calcule a economia com pagamentos extras na hipoteca.","Berechnen Sie die Ersparnis durch zusätzliche Hypothekenzahlungen.","Calcola i risparmi con pagamenti extra sul mutuo.",
        {"balance":"Saldo","rate":"Tasa %","extra":"Pago extra mensual"},{"balance":"Balance","rate":"Rate %","extra":"Extra monthly"},{"balance":"Solde","rate":"Taux %","extra":"Mensualité suppl."},{"balance":"Saldo","rate":"Taxa %","extra":"Extra mensal"},{"balance":"Saldo","rate":"Zinssatz %","extra":"Zusätzlich monatlich"},{"balance":"Saldo","rate":"Tasso %","extra":"Extra mensile"},
        {"months_saved":"Meses ahorrados","interest_saved":"Interés ahorrado"},{"months_saved":"Months saved","interest_saved":"Interest saved"},{"months_saved":"Mois économisés","interest_saved":"Intérêts économisés"},{"months_saved":"Meses economizados","interest_saved":"Juros economizados"},{"months_saved":"Gesparte Monate","interest_saved":"Gesparte Zinsen"},{"months_saved":"Mesi risparmiati","interest_saved":"Interessi risparmiati"}),
    use_cases=[{"en":"Debt Freedom","en_body":"Homeowners accelerate payoff by adding $100-$500 monthly, often cutting 5-10 years off a 30-year mortgage."},{"en":"Interest Savings","en_body":"An extra $200/month on a $200K mortgage at 4% saves over $50,000 in lifetime interest."},{"en":"Refinance Evaluation","en_body":"Borrowers compare extra-payment savings versus refinancing costs to choose the cheaper strategy."}],
    steps=[{"en":"Enter current mortgage balance."},{"en":"Enter interest rate."},{"en":"Enter extra monthly principal payment."}])

add(id="336",block="finanzas",cat="C",domain="finance",concept="credit card payoff",
    slugs={"es":"liquidacion-tarjeta-credito","en":"credit-card-payoff","fr":"remboursement-carte","pt":"quitacao-cartao","de":"kreditkarten-tilgung","it":"estinzione-carta-credito"},
    inputs=[{"id":"balance","type":"number","step":"any","default":5000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"rate","type":"number","step":"any","default":18,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"payment","type":"number","step":"any","default":200,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"}],
    outputs=[{"id":"months","unit":"mo"},{"id":"total_interest","unit":"USD"}],formula="var bal=parseFloat(inputs.balance)||0;var r=(parseFloat(inputs.rate)||0)/1200;var pmt=parseFloat(inputs.payment)||0;var months=0;var total_int=0;var b=bal;while(b>0&&months<1000){var int_b=b*r;var prin=pmt-int_b;if(prin<=0){months=999;break;}b-=prin;months++;total_int+=int_b;}return{months:months.toFixed(0),total_interest:total_int.toFixed(2)};",
    related=["335","322"],latex_formula="\\text{Months} = \\min \\left\\{ n : \\sum_{k=1}^{n} PMT_k > B_0 \\right\\}",
    i18n=i18n("Liquidación de Tarjeta de Crédito","Credit Card Payoff Calculator","Remboursement Carte de Crédit","Quitação de Cartão de Crédito","Kreditkartentilgung","Estinzione Carta di Credito","Calcula cuánto tardas en pagar una tarjeta de crédito.","Calculate how long to pay off a credit card.","Calculez le délai pour rembourser une carte de crédit.","Calcule quanto tempo leva para quitar um cartão de crédito.","Berechnen Sie die Tilgungsdauer einer Kreditkarte.","Calcola quanto tempo ci vuole per estinguere una carta di credito.",
        {"balance":"Saldo","rate":"Tasa %","payment":"Pago mensual"},{"balance":"Balance","rate":"Rate %","payment":"Monthly payment"},{"balance":"Solde","rate":"Taux %","payment":"Mensualité"},{"balance":"Saldo","rate":"Taxa %","payment":"Pagamento mensal"},{"balance":"Saldo","rate":"Zinssatz %","payment":"Monatliche Rate"},{"balance":"Saldo","rate":"Tasso %","payment":"Rata mensile"},
        {"months":"Meses","total_interest":"Interés total"},{"months":"Months","total_interest":"Total interest"},{"months":"Mois","total_interest":"Intérêts totaux"},{"months":"Meses","total_interest":"Juros totais"},{"months":"Monate","total_interest":"Gesamtzinsen"},{"months":"Mesi","total_interest":"Interessi totali"}),
    use_cases=[{"en":"Debt Avalanche","en_body":"Consumers prioritize highest-rate cards first, using this calculator to see months and interest saved."},{"en":"Balance Transfer","en_body":"Cardholders compare 0% intro APR offers by modeling payoff before promotional rates expire."},{"en":"Minimum Payment Trap","en_body":"Paying only the minimum on $5K at 18% takes 30+ years; the calculator reveals this stark reality."}],
    steps=[{"en":"Enter credit card balance."},{"en":"Enter APR."},{"en":"Enter monthly payment amount."}])

add(id="337",block="finanzas",cat="C",domain="finance",concept="college savings",
    slugs={"es":"ahorro-universidad","en":"college-savings","fr":"epargne-etudes","pt":"poupanca-faculdade","de":"studien-sparen","it":"risparmio-universita"},
    inputs=[{"id":"cost","type":"number","step":"any","default":100000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"years","type":"number","step":1,"default":18,"unit":"yr","unit_options":["yr"],"unit_category":"time"},{"id":"rate","type":"number","step":"any","default":6,"unit":"%","unit_options":["%"],"unit_category":"percentage"}],
    outputs=[{"id":"monthly","unit":"USD"}],formula="var cost=parseFloat(inputs.cost)||0;var y=parseFloat(inputs.years)||1;var r=(parseFloat(inputs.rate)||0)/100;var n=y*12;var monthly=r>0?cost*r/12/(Math.pow(1+r/12,n)-1):cost/n;return{monthly:monthly.toFixed(2)};",
    related=["327","328"],latex_formula="PMT = \\frac{FV \\times \\frac{r}{12}}{(1 + \\frac{r}{12})^{n} - 1}",
    i18n=i18n("Ahorro para la Universidad","College Savings Calculator","Épargne Études","Poupança Faculdade","Studiensparen","Risparmio Università","Calcula cuánto ahorrar mensualmente para la universidad.","Calculate monthly savings needed for college.","Calculez l'épargne mensuelle nécessaire pour les études.","Calcule a poupança mensal necessária para a faculdade.","Berechnen Sie die monatliche Ersparnis für das Studium.","Calcola il risparmio mensile necessario per l'università.",
        {"cost":"Coste total","years":"Años","rate":"Rendimiento %"},{"cost":"Total cost","years":"Years","rate":"Return %"},{"cost":"Coût total","years":"Années","rate":"Rendement %"},{"cost":"Custo total","years":"Anos","rate":"Retorno %"},{"cost":"Gesamtkosten","years":"Jahre","rate":"Rendite %"},{"cost":"Costo totale","years":"Anni","rate":"Rendimento %"},
        {"monthly":"Ahorro mensual"},{"monthly":"Monthly savings"},{"monthly":"Épargne mensuelle"},{"monthly":"Poupança mensal"},{"monthly":"Monatliche Ersparnis"},{"monthly":"Risparmio mensile"}),
    use_cases=[{"en":"529 Plans","en_body":"Parents contribute to tax-advantaged 529 plans using calculated monthly targets to cover projected tuition inflation."},{"en":"Custodial Accounts","en_body":"Grandparents set up UTMA accounts with automatic monthly transfers sized to future education costs."},{"en":"Scholarship Gap","en_body":"Families compute savings shortfalls after expected scholarships to determine loan needs early."}],
    steps=[{"en":"Enter estimated total college cost."},{"en":"Enter years until enrollment."},{"en":"Enter expected investment return."}])

add(id="338",block="finanzas",cat="C",domain="finance",concept="life insurance needs",
    slugs={"es":"necesidades-seguro-vida","en":"life-insurance-needs","fr":"besoins-assurance-vie","pt":"necessidades-seguro-vida","de":"lebensversicherungsbedarf","it":"necessita-assicurazione-vita"},
    inputs=[{"id":"income","type":"number","step":"any","default":60000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"years","type":"number","step":1,"default":10,"unit":"yr","unit_options":["yr"],"unit_category":"time"},{"id":"debts","type":"number","step":"any","default":200000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"savings","type":"number","step":"any","default":50000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"}],
    outputs=[{"id":"needed","unit":"USD"}],formula="var inc=parseFloat(inputs.income)||0;var y=parseFloat(inputs.years)||0;var debts=parseFloat(inputs.debts)||0;var sav=parseFloat(inputs.savings)||0;var needed=inc*y+debts-sav;return{needed:needed.toFixed(2)};",
    related=["337","328"],latex_formula="\\text{Coverage} = (\\text{Income} \\times \\text{Years}) + \\text{Debts} - \\text{Savings}",
    i18n=i18n("Necesidades de Seguro de Vida","Life Insurance Needs Calculator","Besoins Assurance-Vie","Necessidades Seguro de Vida","Lebensversicherungsbedarf","Necessità Assicurazione Vita","Calcula la cobertura de seguro de vida recomendada.","Calculate recommended life insurance coverage.","Calculez la couverture d'assurance-vie recommandée.","Calcule a cobertura recomendada de seguro de vida.","Berechnen Sie den empfohlenen Lebensversicherungsbedarf.","Calcola la copertura assicurativa sulla vita raccomandata.",
        {"income":"Ingreso anual","years":"Años de sustento","debts":"Deudas","savings":"Ahorros"},{"income":"Annual income","years":"Years of support","debts":"Debts","savings":"Savings"},{"income":"Revenu annuel","years":"Années de soutien","debts":"Dettes","savings":"Épargne"},{"income":"Renda anual","years":"Anos de sustento","debts":"Dívidas","savings":"Poupança"},{"income":"Jahreseinkommen","years":"Unterhaltsjahre","debts":"Schulden","savings":"Ersparnisse"},{"income":"Reddito annuo","years":"Anni di sostentamento","debts":"Debiti","savings":"Risparmi"},
        {"needed":"Cobertura recomendada"},{"needed":"Coverage needed"},{"needed":"Couverture recommandée"},{"needed":"Cobertura necessária"},{"needed":"Empfohlene Deckung"},{"needed":"Copertura raccomandata"}),
    use_cases=[{"en":"Family Protection","en_body":"Parents buy term life insurance to replace income until children become financially independent."},{"en":"Mortgage Protection","en_body":"Homeowners match coverage to outstanding mortgage balances so surviving spouses keep the house."},{"en":"Business Continuity","en_body":"Partners fund buy-sell agreements with life insurance to ensure smooth ownership transitions."}],
    steps=[{"en":"Enter annual income to replace."},{"en":"Enter years of support needed."},{"en":"Enter debts to pay off and existing savings."}])

add(id="339",block="finanzas",cat="C",domain="finance",concept="compound annual growth rate monthly",
    slugs={"es":"cagr-mensual","en":"cagr-monthly","fr":"cagr-mensuel","pt":"cagr-mensal","de":"cagr-monatlich","it":"cagr-mensile"},
    inputs=[{"id":"begin","type":"number","step":"any","default":1000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"end","type":"number","step":"any","default":2000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"months","type":"number","step":1,"default":60,"unit":"mo","unit_options":["mo","yr"],"unit_category":"time"}],
    outputs=[{"id":"cagr","unit":"%"}],formula="var b=parseFloat(inputs.begin)||0;var e=parseFloat(inputs.end)||0;var m=parseFloat(inputs.months)||1;var cagr=(Math.pow(e/b,12/m)-1)*100;return{cagr:cagr.toFixed(4)};",
    related=["320","333"],latex_formula="\\text{CAGR}_{monthly} = \\left(\\frac{V_{final}}{V_{initial}}\\right)^{\\frac{12}{n}} - 1",
    i18n=i18n("CAGR Mensual","Monthly CAGR Calculator","CAGR Mensuel","CAGR Mensal","CAGR Monatlich","CAGR Mensile","Calcula el CAGR a partir de meses en lugar de años.","Calculate CAGR from months instead of years.","Calculez le CAGR à partir de mois au lieu d'années.","Calcule o CAGR a partir de meses em vez de anos.","Berechnen Sie den CAGR aus Monaten statt Jahren.","Calcola il CAGR da mesi invece di anni.",
        {"begin":"Valor inicial","end":"Valor final","months":"Meses"},{"begin":"Beginning value","end":"Ending value","months":"Months"},{"begin":"Valeur initiale","end":"Valeur finale","months":"Mois"},{"begin":"Valor inicial","end":"Valor final","months":"Meses"},{"begin":"Anfangswert","end":"Endwert","months":"Monate"},{"begin":"Valore iniziale","end":"Valore finale","months":"Mesi"},
        {"cagr":"CAGR % anualizado"},{"cagr":"Annualized CAGR %"},{"cagr":"CAGR % annualisé"},{"cagr":"CAGR % anualizado"},{"cagr":"Annualisierter CAGR %"},{"cagr":"CAGR % annualizzato"}),
    use_cases=[{"en":"Crypto Trading","en_body":"Short-term traders annualize monthly returns to compare performance against traditional investments."},{"en":"SaaS MRR","en_body":"Startup founders calculate monthly CAGR from MRR growth to report traction to investors."},{"en":"Subscription Growth","en_body":"Product managers track monthly user growth rates and annualize them for board presentations."}],
    steps=[{"en":"Enter initial value."},{"en":"Enter final value."},{"en":"Enter number of months."}])

# ── HEALTH (425-434) ──
add(id="425",block="salud",cat="B",domain="health",concept="body fat Navy",
    slugs={"es":"grasa-corporal-navy","en":"body-fat-navy","fr":"graisse-corporelle-navy","pt":"gordura-corporal-navy","de":"koerperfett-navy","it":"grasso-corpo-navy"},
    inputs=[{"id":"waist","type":"number","step":"any","default":80,"unit":"cm","unit_options":["cm","in"],"unit_category":"length"},{"id":"neck","type":"number","step":"any","default":40,"unit":"cm","unit_options":["cm","in"],"unit_category":"length"},{"id":"height","type":"number","step":"any","default":175,"unit":"cm","unit_options":["cm","ft"],"unit_category":"length"},{"id":"gender","type":"select","options":["male","female"],"default":"male","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"bfp","unit":"%"}],formula="var w=parseFloat(inputs.waist)||0;var n=parseFloat(inputs.neck)||0;var h=parseFloat(inputs.height)||0;var g=inputs.gender||'male';var bfp=g==='male'?495/(1.0324-0.19077*Math.log10(w-n)+0.15456*Math.log10(h))-450:495/(1.29579-0.35004*Math.log10(w-n)+0.22100*Math.log10(h))-450;return{bfp:bfp.toFixed(2)};",
    related=["416","400"],latex_formula="\\text{BFP} = \\frac{495}{1.0324 - 0.19077\\log_{10}(w-n) + 0.15456\\log_{10}(h)} - 450",
    i18n=i18n("Grasa Corporal Método Navy","Body Fat Navy Method","Grassee Corporelle Navy","Gordura Corporal Método Navy","Körperfett Navy-Methode","Grasso Corporeo Metodo Navy","Estima el % de grasa corporal con el método de la Marina.","Estimate body fat percentage using the Navy method.","Estimez le % de graisse corporelle avec la méthode Navy.","Estime a % de gordura corporal com o método Navy.","Schätzen Sie den Körperfettanteil mit der Navy-Methode.","Stima la % di grasso corporeo con il metodo Navy.",
        {"waist":"Cintura","neck":"Cuello","height":"Altura","gender":"Sexo"},{"waist":"Waist","neck":"Neck","height":"Height","gender":"Gender"},{"waist":"Taille","neck":"Cou","height":"Taille","gender":"Sexe"},{"waist":"Cintura","neck":"Pescoço","height":"Altura","gender":"Sexo"},{"waist":"Taille","neck":"Hals","height":"Größe","gender":"Geschlecht"},{"waist":"Vita","neck":"Collo","height":"Altezza","gender":"Sesso"},
        {"bfp":"% Grasa corporal"},{"bfp":"Body fat %"},{"bfp":"% Graisse"},{"bfp":"% Gordura"},{"bfp":"Körperfett %"},{"bfp":"% Grasso"}),
    use_cases=[{"en":"Military Fitness","en_body":"The US Navy uses circumference measurements to assess body composition without hydrostatic weighing."},{"en":"Home Fitness","en_body":"Home users track body fat trends with a tape measure when calipers or scales are unavailable."},{"en":"Clinical Screening","en_body":"Healthcare providers use Navy method as a quick, non-invasive alternative to DXA scans."}],
    steps=[{"en":"Measure waist at navel level."},{"en":"Measure neck at narrowest point."},{"en":"Enter height and gender."}])

add(id="426",block="salud",cat="B",domain="health",concept="TDEE",
    slugs={"es":"gasto-energetico-total","en":"tdee-calculator","fr":"depense-energetique-totale","pt":"gasto-energetico-total","de":"tdee","it":"tdee"},
    inputs=[{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"height","type":"number","step":"any","default":175,"unit":"cm","unit_options":["cm","ft"],"unit_category":"length"},{"id":"age","type":"number","step":1,"default":30,"unit":"yr","unit_options":["yr"],"unit_category":"time"},{"id":"gender","type":"select","options":["male","female"],"default":"male","unit":"","unit_options":[],"unit_category":""},{"id":"activity","type":"number","step":"any","default":1.55,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"tdee","unit":"kcal"},{"id":"bmr","unit":"kcal"}],formula="var w=parseFloat(inputs.weight)||0;var h=parseFloat(inputs.height)||0;var a=parseFloat(inputs.age)||0;var g=inputs.gender||'male';var act=parseFloat(inputs.activity)||1;var bmr=g==='male'?(10*w+6.25*h-5*a+5):(10*w+6.25*h-5*a-161);var tdee=bmr*act;return{tdee:tdee.toFixed(0),bmr:bmr.toFixed(0)};",
    related=["401","417"],latex_formula="\\text{BMR} = 10W + 6.25H - 5A + s, \\quad \\text{TDEE} = \\text{BMR} \\times \\text{AF}",
    i18n=i18n("Gasto Energético Total (TDEE)","TDEE Calculator","Dépense Énergétique Totale","Gasto Energético Total","TDEE-Rechner","TDEE","Calcula tus calorías diarias totales incluyendo actividad.","Calculate your total daily energy expenditure including activity.","Calculez votre dépense énergétique totale incluant l'activité.","Calcule seu gasto energético total diário incluindo atividade.","Berechnen Sie Ihren gesamten täglichen Energieverbrauch inklusive Aktivität.","Calcola la tua spesa energetica giornaliera totale inclusa l'attività.",
        {"weight":"Peso","height":"Altura","age":"Edad","gender":"Sexo","activity":"Factor actividad"},{"weight":"Weight","height":"Height","age":"Age","gender":"Gender","activity":"Activity factor"},{"weight":"Poids","height":"Taille","age":"Âge","gender":"Sexe","activity":"Facteur activité"},{"weight":"Peso","height":"Altura","age":"Idade","gender":"Sexo","activity":"Fator atividade"},{"weight":"Gewicht","height":"Größe","age":"Alter","gender":"Geschlecht","activity":"Aktivitätsfaktor"},{"weight":"Peso","height":"Altezza","age":"Età","gender":"Sesso","activity":"Fattore attività"},
        {"tdee":"TDEE kcal","bmr":"BMR kcal"},{"tdee":"TDEE kcal","bmr":"BMR kcal"},{"tdee":"TDEE kcal","bmr":"BMR kcal"},{"tdee":"TDEE kcal","bmr":"BMR kcal"},{"tdee":"TDEE kcal","bmr":"BMR kcal"},{"tdee":"TDEE kcal","bmr":"BMR kcal"}),
    use_cases=[{"en":"Weight Loss","en_body":"Dieters create caloric deficits by eating 300-500 kcal below their TDEE."},{"en":"Muscle Gain","en_body":"Bodybuilders eat 200-300 kcal above TDEE to support lean mass accretion."},{"en":"Maintenance","en_body":"Athletes in season adjust intake to match TDEE and maintain competition weight."}],
    steps=[{"en":"Enter weight, height, age, and gender."},{"en":"Select an activity factor (1.2-1.9)."},{"en":"The calculator returns BMR and TDEE."}])

add(id="427",block="salud",cat="B",domain="health",concept="BMR Mifflin-St Jeor",
    slugs={"es":"tasa-metabolica-basal-mifflin","en":"bmr-mifflin-st-jeor","fr":"tmb-mifflin-st-jeor","pt":"tmb-mifflin-st-jeor","de":"bmr-mifflin-st-jeor","it":"bmr-mifflin-st-jeor"},
    inputs=[{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"height","type":"number","step":"any","default":175,"unit":"cm","unit_options":["cm","ft"],"unit_category":"length"},{"id":"age","type":"number","step":1,"default":30,"unit":"yr","unit_options":["yr"],"unit_category":"time"},{"id":"gender","type":"select","options":["male","female"],"default":"male","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"bmr","unit":"kcal"}],formula="var w=parseFloat(inputs.weight)||0;var h=parseFloat(inputs.height)||0;var a=parseFloat(inputs.age)||0;var g=inputs.gender||'male';var bmr=g==='male'?(10*w+6.25*h-5*a+5):(10*w+6.25*h-5*a-161);return{bmr:bmr.toFixed(0)};",
    related=["426","400"],latex_formula="\\text{BMR}_{male} = 10W + 6.25H - 5A + 5, \\quad \\text{BMR}_{female} = 10W + 6.25H - 5A - 161",
    i18n=i18n("Tasa Metabólica Basal (Mifflin-St Jeor)","BMR Calculator (Mifflin-St Jeor)","Taux Métabolique de Base","Taxa Metabólica Basal","BMR Rechner (Mifflin-St Jeor)","BMR (Mifflin-St Jeor)","Calcula tu metabolismo basal con la fórmula de Mifflin-St Jeor.","Calculate basal metabolic rate using the Mifflin-St Jeor equation.","Calculez le taux métabolique de base avec Mifflin-St Jeor.","Calcule a taxa metabólica basal usando a equação de Mifflin-St Jeor.","Berechnen Sie den Grundumsatz mit der Mifflin-St-Jeor-Formel.","Calcola il metabolismo basale con l'equazione di Mifflin-St Jeor.",
        {"weight":"Peso","height":"Altura","age":"Edad","gender":"Sexo"},{"weight":"Weight","height":"Height","age":"Age","gender":"Gender"},{"weight":"Poids","height":"Taille","age":"Âge","gender":"Sexe"},{"weight":"Peso","height":"Altura","age":"Idade","gender":"Sexo"},{"weight":"Gewicht","height":"Größe","age":"Alter","gender":"Geschlecht"},{"weight":"Peso","height":"Altezza","age":"Età","gender":"Sesso"},
        {"bmr":"BMR kcal"},{"bmr":"BMR kcal"},{"bmr":"BMR kcal"},{"bmr":"BMR kcal"},{"bmr":"BMR kcal"},{"bmr":"BMR kcal"}),
    use_cases=[{"en":"Diet Planning","en_body":"Registered dietitians use BMR as the foundation for calculating personalized calorie prescriptions."},{"en":"ICU Nutrition","en_body":"Hospital nutrition teams estimate basal energy needs for mechanically ventilated patients."},{"en":"Wearable Calibration","en_body":"Fitness trackers use BMR equations to establish baseline calorie burn before adding activity data."}],
    steps=[{"en":"Enter weight, height, age, and gender."},{"en":"The calculator returns your basal metabolic rate in kcal/day."}])

add(id="428",block="salud",cat="B",domain="health",concept="RMR",
    slugs={"es":"metabolismo-en-reposo","en":"rmr-calculator","fr":"metabolisme-au-repos","pt":"taxa-metabolica-repouso","de":"ruheumsatz","it":"metabolismo-a-riposo"},
    inputs=[{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"height","type":"number","step":"any","default":175,"unit":"cm","unit_options":["cm","ft"],"unit_category":"length"},{"id":"age","type":"number","step":1,"default":30,"unit":"yr","unit_options":["yr"],"unit_category":"time"},{"id":"gender","type":"select","options":["male","female"],"default":"male","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"rmr","unit":"kcal"}],formula="var w=parseFloat(inputs.weight)||0;var h=parseFloat(inputs.height)||0;var a=parseFloat(inputs.age)||0;var g=inputs.gender||'male';var rmr=g==='male'?(9.99*w+6.25*h-4.92*a+5):(9.99*w+6.25*h-4.92*a-161);return{rmr:rmr.toFixed(0)};",
    related=["427","426"],latex_formula="\\text{RMR} = 9.99W + 6.25H - 4.92A + s",
    i18n=i18n("Metabolismo en Reposo (RMR)","RMR Calculator","Métabolisme au Repos","Taxa Metabólica de Repouso","Ruheumsatz","Metabolismo a Riposo","Calcula tu metabolismo en reposo.","Calculate your resting metabolic rate.","Calculez votre métabolisme au repos.","Calcule sua taxa metabólica de repouso.","Berechnen Sie Ihren Ruheumsatz.","Calcola il tuo metabolismo a riposo.",
        {"weight":"Peso","height":"Altura","age":"Edad","gender":"Sexo"},{"weight":"Weight","height":"Height","age":"Age","gender":"Gender"},{"weight":"Poids","height":"Taille","age":"Âge","gender":"Sexe"},{"weight":"Peso","height":"Altura","age":"Idade","gender":"Sexo"},{"weight":"Gewicht","height":"Größe","age":"Alter","gender":"Geschlecht"},{"weight":"Peso","height":"Altezza","age":"Età","gender":"Sesso"},
        {"rmr":"RMR kcal"},{"rmr":"RMR kcal"},{"rmr":"RMR kcal"},{"rmr":"RMR kcal"},{"rmr":"RMR kcal"},{"rmr":"RMR kcal"}),
    use_cases=[{"en":"Clinical Settings","en_body":"RMR is measured in metabolic carts and used to set precise feeding protocols for patients."},{"en":"Athlete Monitoring","en_body":"Sports scientists track RMR changes during training camps to detect overtraining or energy deficiency."},{"en":"Weight Management","en_body":"Apps use RMR plus activity multipliers to generate daily calorie budgets."}],
    steps=[{"en":"Enter weight, height, age, and gender."},{"en":"The calculator returns your RMR in kcal/day."}])

add(id="429",block="salud",cat="B",domain="health",concept="METs calculator",
    slugs={"es":"mets-actividad","en":"mets-calculator","fr":"mets-activite","pt":"mets-atividade","de":"mets-aktivitaet","it":"mets-attivita"},
    inputs=[{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"mets","type":"number","step":"any","default":5,"unit":"METs","unit_options":["METs"],"unit_category":""},{"id":"minutes","type":"number","step":"any","default":30,"unit":"min","unit_options":["min","h"],"unit_category":"time"}],
    outputs=[{"id":"calories","unit":"kcal"}],formula="var w=parseFloat(inputs.weight)||0;var mets=parseFloat(inputs.mets)||0;var min=parseFloat(inputs.minutes)||0;var cal=mets*3.5*w*min/200;return{calories:cal.toFixed(1)};",
    related=["428","905"],latex_formula="\\text{Calories} = \\frac{\\text{METs} \\times 3.5 \\times \\text{weight} \\times \\text{minutes}}{200}",
    i18n=i18n("Calculadora de METs","METs Calculator","Calculateur METs","Calculadora de METs","METs Rechner","Calcolatore METs","Calcula calorías quemadas usando el equivalente metabólico.","Calculate calories burned using metabolic equivalent.","Calculez les calories brûlées avec l'équivalent métabolique.","Calcule calorias queimadas usando equivalente metabólico.","Berechnen Sie verbrannte Kalorien mit dem metabolischen Äquivalent.","Calcola le calorie bruciate usando l'equivalente metabolico.",
        {"weight":"Peso","mets":"METs","minutes":"Minutos"},{"weight":"Weight","mets":"METs","minutes":"Minutes"},{"weight":"Poids","mets":"METs","minutes":"Minutes"},{"weight":"Peso","mets":"METs","minutes":"Minutos"},{"weight":"Gewicht","mets":"METs","minutes":"Minuten"},{"weight":"Peso","mets":"METs","minutes":"Minuti"},
        {"calories":"Calorías"},{"calories":"Calories"},{"calories":"Calories"},{"calories":"Calorias"},{"calories":"Kalorien"},{"calories":"Calorie"}),
    use_cases=[{"en":"Exercise Prescription","en_body":"Cardiologists recommend activities at specific MET levels for cardiac rehabilitation patients."},{"en":"Fitness Tracking","en_body":"Smartwatches estimate calorie burn by mapping heart rate to MET ranges during workouts."},{"en":"Epidemiology","en_body":"Population studies classify physical activity intensity using MET-minute thresholds."}],
    steps=[{"en":"Enter body weight."},{"en":"Enter activity MET level (1-16)."},{"en":"Enter duration in minutes."}])

add(id="430",block="salud",cat="B",domain="health",concept="target weight",
    slugs={"es":"peso-objetivo","en":"target-weight","fr":"poids-cible","pt":"peso-alvo","de":"zielgewicht","it":"peso-obiettivo"},
    inputs=[{"id":"current","type":"number","step":"any","default":80,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"goal_bmi","type":"number","step":"any","default":22,"unit":"","unit_options":[],"unit_category":""},{"id":"height","type":"number","step":"any","default":175,"unit":"cm","unit_options":["cm","ft"],"unit_category":"length"}],
    outputs=[{"id":"target","unit":"kg"},{"id":"to_lose","unit":"kg"}],formula="var h_m=(parseFloat(inputs.height)||0)/100;var goal=parseFloat(inputs.goal_bmi)||0;var target=goal*h_m*h_m;var current=parseFloat(inputs.current)||0;return{target:target.toFixed(2),to_lose:(current-target).toFixed(2)};",
    related=["400","422"],latex_formula="\\text{Target} = \\text{BMI}_{goal} \\times \\left(\\frac{H}{100}\\right)^2",
    i18n=i18n("Peso Objetivo","Target Weight Calculator","Poids Cible","Peso Alvo","Zielgewicht","Peso Obiettivo","Calcula tu peso ideal según un IMC deseado.","Calculate your ideal weight based on a target BMI.","Calculez votre poids idéal selon un IMC cible.","Calcule seu peso ideal com base em um IMC alvo.","Berechnen Sie Ihr Zielgewicht basierend auf einem Ziel-BMI.","Calcola il tuo peso ideale in base a un BMI target.",
        {"current":"Peso actual","goal_bmi":"IMC objetivo","height":"Altura"},{"current":"Current weight","goal_bmi":"Goal BMI","height":"Height"},{"current":"Poids actuel","goal_bmi":"IMC cible","height":"Taille"},{"current":"Peso atual","goal_bmi":"IMC alvo","height":"Altura"},{"current":"Aktuelles Gewicht","goal_bmi":"Ziel-BMI","height":"Größe"},{"current":"Peso attuale","goal_bmi":"BMI obiettivo","height":"Altezza"},
        {"target":"Peso objetivo","to_lose":"A perder"},{"target":"Target weight","to_lose":"To lose"},{"target":"Poids cible","to_lose":"À perdre"},{"target":"Peso alvo","to_lose":"A perder"},{"target":"Zielgewicht","to_lose":"Abzunehmen"},{"target":"Peso obiettivo","to_lose":"Da perdere"}),
    use_cases=[{"en":"Weight Loss Goals","en_body":"Dietitians set realistic weight targets by choosing healthy BMI endpoints rather than arbitrary numbers."},{"en":"Athletic Weight Classes","en_body":"Fighters and wrestlers determine safe weight cuts to make competition classes without dehydration."},{"en":"Post-Surgery","en_body":"Bariatric patients track progress toward goal weights calculated from their ideal BMI range."}],
    steps=[{"en":"Enter current weight."},{"en":"Enter target BMI (e.g., 22)."},{"en":"Enter height."}])

add(id="431",block="salud",cat="B",domain="health",concept="pregnancy weight gain",
    slugs={"es":"aumento-peso-embarazo","en":"pregnancy-weight-gain","fr":"prise-poids-grossesse","pt":"ganho-peso-gravidez","de":"schwangerschaftsgewicht","it":"aumento-peso-gravidanza"},
    inputs=[{"id":"pre_bmi","type":"number","step":"any","default":22,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"min_gain","unit":"kg"},{"id":"max_gain","unit":"kg"}],formula="var bmi=parseFloat(inputs.pre_bmi)||0;var min_g=bmi<18.5?12.5:(bmi<25?11.5:(bmi<30?7:5));var max_g=bmi<18.5?18:(bmi<25?16:(bmi<30?11.5:9));return{min_gain:min_g.toFixed(1),max_gain:max_g.toFixed(1)};",
    related=["423","430"],latex_formula="\\text{Gain}_{recommended} = f(\\text{Pre-pregnancy BMI})",
    i18n=i18n("Aumento de Peso en Embarazo","Pregnancy Weight Gain Calculator","Prise de Poids Grossesse","Ganho de Peso na Gravidez","Schwangerschaftsgewicht","Aumento di Peso Gravidanza","Calcula el aumento de peso recomendado durante el embarazo.","Calculate recommended weight gain during pregnancy.","Calculez la prise de poids recommandée pendant la grossesse.","Calcule o ganho de peso recomendado durante a gravidez.","Berechnen Sie die empfohlene Gewichtszunahme während der Schwangerschaft.","Calcola l'aumento di peso raccomandato durante la gravidanza.",
        {"pre_bmi":"IMC pre-embarazo"},{"pre_bmi":"Pre-pregnancy BMI"},{"pre_bmi":"IMC pré-grossesse"},{"pre_bmi":"IMC pré-gravidez"},{"pre_bmi":"BMI vor Schwangerschaft"},{"pre_bmi":"BMI pre-gravidanza"},
        {"min_gain":"Mínimo kg","max_gain":"Máximo kg"},{"min_gain":"Min kg","max_gain":"Max kg"},{"min_gain":"Min kg","max_gain":"Max kg"},{"min_gain":"Mín kg","max_gain":"Máx kg"},{"min_gain":"Min kg","max_gain":"Max kg"},{"min_gain":"Min kg","max_gain":"Max kg"}),
    use_cases=[{"en":"Prenatal Care","en_body":"OB-GYNs monitor weight gain at each visit to ensure fetal growth without maternal complications."},{"en":"Gestational Diabetes","en_body":"Controlled weight gain reduces the risk of gestational diabetes and preeclampsia."},{"en":"Postpartum Recovery","en_body":"Appropriate gain during pregnancy makes postpartum weight loss more achievable."}],
    steps=[{"en":"Enter pre-pregnancy BMI."},{"en":"The calculator returns IOM recommended weight gain range."}])

add(id="432",block="salud",cat="B",domain="health",concept="calories burned walking",
    slugs={"es":"calorias-caminar","en":"calories-burned-walking","fr":"calories-marche","pt":"calorias-caminhada","de":"kalorien-verbrauch-wandern","it":"calorie-bruciate-camminare"},
    inputs=[{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"distance","type":"number","step":"any","default":5,"unit":"km","unit_options":["km","mi"],"unit_category":"length"},{"id":"speed","type":"number","step":"any","default":5,"unit":"km/h","unit_options":["km/h","mph"],"unit_category":"velocity"}],
    outputs=[{"id":"calories","unit":"kcal"}],formula="var w=parseFloat(inputs.weight)||0;var d=parseFloat(inputs.distance)||0;var s=parseFloat(inputs.speed)||0;var met=s<3.2?2.8:(s<4.8?3.5:(s<6.4?5:6.5));var cal=met*3.5*w*d/s*60/200;return{calories:cal.toFixed(1)};",
    related=["429","905"],latex_formula="\\text{Calories} = \\frac{\\text{METs} \\times 3.5 \\times W \\times D}{S} \\times \\frac{60}{200}",
    i18n=i18n("Calorías Quemadas Caminando","Calories Burned Walking","Calories Brûlées Marche","Calorias Queimadas Caminhando","Kalorienverbrennung Gehen","Calorie Bruciate Camminando","Calcula las calorías quemadas caminando.","Calculate calories burned while walking.","Calculez les calories brûlées en marchant.","Calcule as calorias queimadas caminhando.","Berechnen Sie die verbrannten Kalorien beim Gehen.","Calcola le calorie bruciate camminando.",
        {"weight":"Peso","distance":"Distancia","speed":"Velocidad"},{"weight":"Weight","distance":"Distance","speed":"Speed"},{"weight":"Poids","distance":"Distance","speed":"Vitesse"},{"weight":"Peso","distance":"Distância","speed":"Velocidade"},{"weight":"Gewicht","distance":"Strecke","speed":"Geschwindigkeit"},{"weight":"Peso","distance":"Distanza","speed":"Velocità"},
        {"calories":"Calorías"},{"calories":"Calories"},{"calories":"Calories"},{"calories":"Calorias"},{"calories":"Kalorien"},{"calories":"Calorie"}),
    use_cases=[{"en":"Daily Activity","en_body":"Office workers track walking commutes to ensure they meet minimum daily activity guidelines."},{"en":"Weight Loss","en_body":"Dieters model calorie deficits by adding walking sessions of specific distances and speeds."},{"en":"Rehabilitation","en_body":"Physical therapists prescribe graded walking programs with target calorie expenditures."}],
    steps=[{"en":"Enter body weight."},{"en":"Enter walking distance."},{"en":"Enter average walking speed."}])

add(id="433",block="salud",cat="B",domain="health",concept="child growth percentile",
    slugs={"es":"percentil-crecimiento-infantil","en":"child-growth-percentile","fr":"percentile-croissance-enfant","pt":"percentil-crescimento-infantil","de":"kind-wachstumsperzentile","it":"percentile-crescita-bambino"},
    inputs=[{"id":"age_months","type":"number","step":1,"default":24,"unit":"mo","unit_options":["mo","yr"],"unit_category":"time"},{"id":"height","type":"number","step":"any","default":85,"unit":"cm","unit_options":["cm","ft"],"unit_category":"length"},{"id":"gender","type":"select","options":["male","female"],"default":"male","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"percentile","unit":"%"}],formula="var age=parseFloat(inputs.age_months)||0;var h=parseFloat(inputs.height)||0;var g=inputs.gender||'male';var median=g==='male'?(49.9+2.4*age):(49.1+2.3*age);var sd=3.5;var z=(h-median)/sd;var p=Math.round((1+erf(z/Math.sqrt(2)))/2*100);return{percentile:p};",
    related=["431","400"],latex_formula="\\text{Percentile} = \\Phi\\left(\\frac{H - \\mu_{age}}{\\sigma}\\right) \\times 100",
    i18n=i18n("Percentil de Crecimiento Infantil","Child Growth Percentile","Percentile Croissance Enfant","Percentil de Crescimento Infantil","Kind-Wachstumsperzentile","Percentile Crescita Bambino","Estima el percentil de talla de un niño.","Estimate a child's height percentile.","Estimez le percentile de taille d'un enfant.","Estime o percentil de altura de uma criança.","Schätzen Sie das Wachstumsperzentil eines Kindes.","Stima il percentile di altezza di un bambino.",
        {"age_months":"Edad meses","height":"Altura","gender":"Sexo"},{"age_months":"Age months","height":"Height","gender":"Gender"},{"age_months":"Âge mois","height":"Taille","gender":"Sexe"},{"age_months":"Idade meses","height":"Altura","gender":"Sexo"},{"age_months":"Alter Monate","height":"Größe","gender":"Geschlecht"},{"age_months":"Età mesi","height":"Altezza","gender":"Sesso"},
        {"percentile":"Percentil %"},{"percentile":"Percentile %"},{"percentile":"Percentile %"},{"percentile":"Percentil %"},{"percentile":"Perzentil %"},{"percentile":"Percentile %"}),
    use_cases=[{"en":"Pediatric Checkups","en_body":"Pediatricians plot height and weight on WHO growth charts to screen for failure to thrive."},{"en":"Parental Concern","en_body":"Parents verify whether their child's growth trajectory falls within normal statistical ranges."},{"en":"Endocrine Evaluation","en_body":"Endocrinologists investigate children below the 3rd or above the 97th percentile for hormonal disorders."}],
    steps=[{"en":"Enter child's age in months."},{"en":"Enter height."},{"en":"Select gender."}])

add(id="434",block="salud",cat="B",domain="health",concept="water intake by weight",
    slugs={"es":"agua-por-peso","en":"water-intake-by-weight","fr":"eau-par-poids","pt":"agua-por-peso","de":"wasserbedarf-nach-gewicht","it":"acqua-per-peso"},
    inputs=[{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"activity","type":"number","step":"any","default":30,"unit":"min","unit_options":["min","h"],"unit_category":"time"}],
    outputs=[{"id":"water","unit":"L"}],formula="var w=parseFloat(inputs.weight)||0;var act=parseFloat(inputs.activity)||0;var base=w*0.033;var extra=act*0.0004;var total=base+extra;return{water:total.toFixed(2)};",
    related=["403","432"],latex_formula="\\text{Water (L)} = 0.033 \\times \\text{weight} + 0.0004 \\times \\text{activity minutes}",
    i18n=i18n("Ingesta de Agua por Peso","Water Intake by Weight","Apport en Eau par Poids","Ingestão de Água por Peso","Wasserbedarf nach Gewicht","Assunzione Acqua per Peso","Calcula cuánta agua necesitas según tu peso y actividad.","Calculate water needs based on weight and activity.","Calculez vos besoins en eau selon poids et activité.","Calcule a necessidade de água com base no peso e atividade.","Berechnen Sie den Wasserbedarf basierend auf Gewicht und Aktivität.","Calcola il fabbisogno idrico in base a peso e attività.",
        {"weight":"Peso","activity":"Actividad min"},{"weight":"Weight","activity":"Activity min"},{"weight":"Poids","activity":"Activité min"},{"weight":"Peso","activity":"Atividade min"},{"weight":"Gewicht","activity":"Aktivität min"},{"weight":"Peso","activity":"Attività min"},
        {"water":"Agua L"},{"water":"Water L"},{"water":"Eau L"},{"water":"Água L"},{"water":"Wasser L"},{"water":"Acqua L"}),
    use_cases=[{"en":"Athlete Hydration","en_body":"Sports dietitians increase water recommendations for athletes training in hot climates."},{"en":"Kidney Health","en_body":"Nephrologists prescribe adequate fluid intake to prevent kidney stone formation."},{"en":"Elderly Care","en_body":"Caregivers monitor water consumption because thirst sensation diminishes with age."}],
    steps=[{"en":"Enter body weight."},{"en":"Enter daily active minutes."},{"en":"The calculator returns recommended water intake in liters."}])

# ── TECH / EVERYDAY (513-522) ──
add(id="513",block="cotidiano",cat="D",domain="tech",concept="screen resolution",
    slugs={"es":"resolucion-pantalla","en":"screen-resolution","fr":"resolution-ecran","pt":"resolucao-tela","de":"bildschirmaufloesung","it":"risoluzione-schermo"},
    inputs=[{"id":"width","type":"number","step":1,"default":1920,"unit":"px","unit_options":["px"],"unit_category":"count"},{"id":"height","type":"number","step":1,"default":1080,"unit":"px","unit_options":["px"],"unit_category":"count"}],
    outputs=[{"id":"total_pixels","unit":"MP"},{"id":"aspect_ratio","unit":""}],formula="var w=parseFloat(inputs.width)||0;var h=parseFloat(inputs.height)||0;var mp=w*h/1e6;var gcd=function(a,b){return b?gcd(b,a%b):a;};var g=gcd(w,h);return{total_pixels:mp.toFixed(2),aspect_ratio:(w/g).toFixed(0)+':'+(h/g).toFixed(0)};",
    related=["507","508"],latex_formula="\\text{MP} = \\frac{W \\times H}{10^6}, \\quad \\text{Aspect} = \\frac{W}{H}",
    i18n=i18n("Resolución de Pantalla","Screen Resolution","Résolution Écran","Resolução da Tela","Bildschirmauflösung","Risoluzione Schermo","Calcula megapíxeles y relación de aspecto de una resolución.","Calculate megapixels and aspect ratio of a resolution.","Calculez les mégapixels et le rapport d'aspect d'une résolution.","Calcule os megapixels e a proporção de uma resolução.","Berechnen Sie Megapixel und Seitenverhältnis einer Auflösung.","Calcola i megapixel e il rapporto d'aspetto di una risoluzione.",
        {"width":"Ancho px","height":"Alto px"},{"width":"Width px","height":"Height px"},{"width":"Largeur px","height":"Hauteur px"},{"width":"Largura px","height":"Altura px"},{"width":"Breite px","height":"Höhe px"},{"width":"Larghezza px","height":"Altezza px"},
        {"total_pixels":"Megapíxeles","aspect_ratio":"Relación aspecto"},{"total_pixels":"Megapixels","aspect_ratio":"Aspect ratio"},{"total_pixels":"Mégapixels","aspect_ratio":"Rapport aspect"},{"total_pixels":"Megapixels","aspect_ratio":"Proporção"},{"total_pixels":"Megapixel","aspect_ratio":"Seitenverhältnis"},{"total_pixels":"Megapixel","aspect_ratio":"Rapporto aspetto"}),
    use_cases=[{"en":"Monitor Shopping","en_body":"Buyers compare 1080p, 1440p, and 4K resolutions by total pixel count for clarity versus GPU load."},{"en":"Camera Sensors","en_body":"Photographers relate sensor resolution to print size capabilities and cropping flexibility."},{"en":"VR Headsets","en_body":"Engineers balance resolution against frame rate requirements to prevent motion sickness."}],
    steps=[{"en":"Enter width in pixels."},{"en":"Enter height in pixels."}])

add(id="514",block="cotidiano",cat="D",domain="tech",concept="video file size",
    slugs={"es":"tamano-archivo-video","en":"video-file-size","fr":"taille-fichier-video","pt":"tamanho-arquivo-video","de":"videodateigroesse","it":"dimensione-file-video"},
    inputs=[{"id":"duration","type":"number","step":"any","default":60,"unit":"s","unit_options":["s","min","h"],"unit_category":"time"},{"id":"bitrate","type":"number","step":"any","default":5000,"unit":"kbps","unit_options":["kbps","Mbps"],"unit_category":"data_rate"}],
    outputs=[{"id":"size_mb","unit":"MB"}],formula="var dur=parseFloat(inputs.duration)||0;var br=parseFloat(inputs.bitrate)||0;var size=(dur*br)/(8*1024);return{size_mb:size.toFixed(2)};",
    related=["511","504"],latex_formula="\\text{Size} = \\frac{\\text{Duration} \\times \\text{Bitrate}}{8 \\times 1024} \\text{ MB}",
    i18n=i18n("Tamaño de Archivo de Video","Video File Size Calculator","Taille Fichier Vidéo","Tamanho do Arquivo de Vídeo","Videodateigröße","Dimensione File Video","Calcula el tamaño de un archivo de video según bitrate y duración.","Calculate video file size from bitrate and duration.","Calculez la taille d'un fichier vidéo selon bitrate et durée.","Calcule o tamanho de um arquivo de vídeo a partir do bitrate e duração.","Berechnen Sie die Videodateigröße aus Bitrate und Dauer.","Calcola la dimensione di un file video da bitrate e durata.",
        {"duration":"Duración","bitrate":"Bitrate"},{"duration":"Duration","bitrate":"Bitrate"},{"duration":"Durée","bitrate":"Bitrate"},{"duration":"Duração","bitrate":"Bitrate"},{"duration":"Dauer","bitrate":"Bitrate"},{"duration":"Durata","bitrate":"Bitrate"},
        {"size_mb":"Tamaño MB"},{"size_mb":"Size MB"},{"size_mb":"Taille MB"},{"size_mb":"Tamanho MB"},{"size_mb":"Größe MB"},{"size_mb":"Dimensione MB"}),
    use_cases=[{"en":"Streaming Planning","en_body":"Content creators size export bitrates to keep video files under platform upload limits."},{"en":"Storage Budgeting","en_body":"Videographers estimate hard drive needs for multi-hour event recordings."},{"en":"CDN Costs","en_body":"Engineers model bandwidth costs by calculating file sizes across different quality tiers."}],
    steps=[{"en":"Enter video duration in seconds."},{"en":"Enter bitrate in kbps."}])

add(id="515",block="cotidiano",cat="D",domain="tech",concept="storage RAID",
    slugs={"es":"capacidad-raid","en":"raid-capacity","fr":"capacite-raid","pt":"capacidade-raid","de":"raid-kapazitaet","it":"capacita-raid"},
    inputs=[{"id":"drives","type":"number","step":1,"default":4,"unit":"","unit_options":[],"unit_category":""},{"id":"drive_size","type":"number","step":"any","default":2000,"unit":"GB","unit_options":["GB","TB"],"unit_category":"digital_storage"},{"id":"raid","type":"select","options":["0","1","5","6","10"],"default":"5","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"usable","unit":"GB"},{"id":"redundancy","unit":""}],formula="var d=parseFloat(inputs.drives)||0;var s=parseFloat(inputs.drive_size)||0;var r=inputs.raid||'5';var usable=r==='0'?d*s:r==='1'?s:r==='5'?(d-1)*s:r==='6'?(d-2)*s:r==='10'?(d/2)*s:0;var red=r==='0'?'None':r==='1'?'Mirror':r==='5'?'1 drive':r==='6'?'2 drives':r==='10'?'Mirror + Stripe':'Unknown';return{usable:usable.toFixed(0),redundancy:red};",
    related=["511","510"],latex_formula="\\text{Usable} = \\begin{cases} n \\times s & \\text{RAID 0} \\\\ s & \\text{RAID 1} \\\\ (n-1) \\times s & \\text{RAID 5} \\end{cases}",
    i18n=i18n("Capacidad RAID","RAID Capacity Calculator","Capacité RAID","Capacidade RAID","RAID-Kapazität","Capacità RAID","Calcula la capacidad útil de un arreglo RAID.","Calculate usable capacity of a RAID array.","Calculez la capacité utile d'un RAID.","Calcule a capacidade útil de um array RAID.","Berechnen Sie die nutzbare Kapazität eines RAID-Arrays.","Calcola la capacità utilizzabile di un array RAID.",
        {"drives":"Discos","drive_size":"Tamaño disco","raid":"Nivel RAID"},{"drives":"Drives","drive_size":"Drive size","raid":"RAID level"},{"drives":"Disques","drive_size":"Taille disque","raid":"Niveau RAID"},{"drives":"Drives","drive_size":"Tamanho disco","raid":"Nível RAID"},{"drives":"Laufwerke","drive_size":"Laufwerksgröße","raid":"RAID-Level"},{"drives":"Dischi","drive_size":"Dimensione disco","raid":"Livello RAID"},
        {"usable":"Capacidad útil","redundancy":"Redundancia"},{"usable":"Usable","redundancy":"Redundancy"},{"usable":"Capacité utile","redundancy":"Redondance"},{"usable":"Capacidade útil","redundancy":"Redundância"},{"usable":"Nutzbar","redundancy":"Redundanz"},{"usable":"Utilizzabile","redundancy":"Ridondanza"}),
    use_cases=[{"en":"NAS Building","en_body":"Home users choose RAID 5 for the best balance of capacity and single-drive fault tolerance."},{"en":"Enterprise Storage","en_body":"IT architects model RAID 6 for critical databases that cannot tolerate rebuild failures."},{"en":"Video Editing","en_body":"Post-production houses stripe multiple SSDs in RAID 0 for maximum sequential throughput."}],
    steps=[{"en":"Enter number of drives."},{"en":"Enter drive capacity."},{"en":"Select RAID level."}])

add(id="516",block="cotidiano",cat="D",domain="tech",concept="server uptime",
    slugs={"es":"tiempo-actividad","en":"server-uptime","fr":"disponibilite-serveur","pt":"uptime-servidor","de":"server-verfuegbarkeit","it":"uptime-server"},
    inputs=[{"id":"downtime_min","type":"number","step":"any","default":60,"unit":"min","unit_options":["min","h"],"unit_category":"time"},{"id":"period","type":"number","step":"any","default":30,"unit":"days","unit_options":["days","mo","yr"],"unit_category":"time"}],
    outputs=[{"id":"uptime_pct","unit":"%"},{"id":"sla","unit":""}],formula="var dt=parseFloat(inputs.downtime_min)||0;var p=parseFloat(inputs.period)||30;var total_min=p*24*60;var up=(1-dt/total_min)*100;var sla=up>=99.999?'Five nines':up>=99.99?'Four nines':up>=99.9?'Three nines':up>=99?'Two nines':'Below 99%';return{uptime_pct:up.toFixed(4),sla:sla};",
    related=["517","510"],latex_formula="\\text{Uptime} \\% = \\left(1 - \\frac{\\text{Downtime}}{\\text{Total Time}}\\right) \\times 100",
    i18n=i18n("Tiempo de Actividad","Server Uptime Calculator","Disponibilité Serveur","Uptime do Servidor","Server-Verfügbarkeit","Uptime Server","Calcula el porcentaje de disponibilidad de un servidor.","Calculate server availability percentage.","Calculez le pourcentage de disponibilité d'un serveur.","Calcule a porcentagem de disponibilidade de um servidor.","Berechnen Sie die Verfügbarkeit eines Servers in Prozent.","Calcola la percentuale di disponibilità di un server.",
        {"downtime_min":"Tiempo caída min","period":"Período días"},{"downtime_min":"Downtime min","period":"Period days"},{"downtime_min":"Indisponibilité min","period":"Période jours"},{"downtime_min":"Tempo inativo min","period":"Período dias"},{"downtime_min":"Ausfallzeit min","period":"Zeitraum Tage"},{"downtime_min":"Downtime min","period":"Periodo giorni"},
        {"uptime_pct":"Uptime %","sla":"Nivel SLA"},{"uptime_pct":"Uptime %","sla":"SLA level"},{"uptime_pct":"Disponibilité %","sla":"Niveau SLA"},{"uptime_pct":"Uptime %","sla":"Nível SLA"},{"uptime_pct":"Verfügbarkeit %","sla":"SLA-Level"},{"uptime_pct":"Uptime %","sla":"Livello SLA"}),
    use_cases=[{"en":"SLA Monitoring","en_body":"Cloud providers guarantee 99.99% uptime in contracts, equating to 4.32 minutes of allowed monthly downtime."},{"en":"Maintenance Windows","en_body":"Operations teams schedule patches within downtime budgets to avoid SLA penalties."},{"en":"Disaster Recovery","en_body":"Failover systems are designed to restore service within minutes to maintain five-nines availability."}],
    steps=[{"en":"Enter downtime in minutes."},{"en":"Enter monitoring period in days."}])

add(id="517",block="cotidiano",cat="D",domain="tech",concept="ping latency",
    slugs={"es":"latencia-ping","en":"ping-latency","fr":"latence-ping","pt":"latencia-ping","de":"ping-latenz","it":"latenza-ping"},
    inputs=[{"id":"distance","type":"number","step":"any","default":1000,"unit":"km","unit_options":["km","mi"],"unit_category":"length"},{"id":"medium","type":"select","options":["fiber","copper","wireless"],"default":"fiber","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"latency","unit":"ms"},{"id":"theoretical","unit":"ms"}],formula="var d=parseFloat(inputs.distance)||0;var m=inputs.medium||'fiber';var speed=m==='fiber'?2e8:m==='copper'?2.3e8:3e8;var lt=(d*1000/speed)*1000;var theo=lt*2;return{latency:lt.toFixed(2),theoretical:theo.toFixed(2)};",
    related=["516","504"],latex_formula="\\text{Latency} = \\frac{d}{v_{propagation}}, \\quad \\text{RTT} = 2 \\times \\text{Latency}",
    i18n=i18n("Latencia de Ping","Ping Latency Calculator","Latence Ping","Latência do Ping","Ping-Latenz","Latenza Ping","Calcula la latencia mínima teórica de red.","Calculate theoretical minimum network latency.","Calculez la latence réseau théorique minimale.","Calcule a latência de rede teórica mínima.","Berechnen Sie die theoretische minimale Netzwerklatenz.","Calcola la latenza di rete teorica minima.",
        {"distance":"Distancia","medium":"Medio"},{"distance":"Distance","medium":"Medium"},{"distance":"Distance","medium":"Médium"},{"distance":"Distância","medium":"Meio"},{"distance":"Entfernung","medium":"Medium"},{"distance":"Distanza","medium":"Medium"},
        {"latency":"Latencia ms","theoretical":"RTT teórico ms"},{"latency":"Latency ms","theoretical":"Theoretical RTT ms"},{"latency":"Latence ms","theoretical":"RTT théorique ms"},{"latency":"Latência ms","theoretical":"RTT teórico ms"},{"latency":"Latenz ms","theoretical":"Theoretischer RTT ms"},{"latency":"Latenza ms","theoretical":"RTT teorico ms"}),
    use_cases=[{"en":"Gaming Optimization","en_body":"Competitive gamers choose servers within 500 km to keep ping below 20 ms for responsive gameplay."},{"en":"High-Frequency Trading","en_body":"Trading firms colocate servers at exchanges to minimize propagation delay and gain microsecond advantages."},{"en":"Video Conferencing","en_body":"Global teams experience perceptible lag when latency exceeds 150 ms, degrading conversational flow."}],
    steps=[{"en":"Enter distance to server."},{"en":"Select transmission medium."}])

add(id="518",block="cotidiano",cat="D",domain="tech",concept="typing speed WPM",
    slugs={"es":"palabras-por-minuto","en":"typing-speed-wpm","fr":"mots-par-minute","pt":"palavras-por-minuto","de":"worte-pro-minute","it":"parole-al-minuto"},
    inputs=[{"id":"words","type":"number","step":1,"default":300,"unit":"words","unit_options":["words"],"unit_category":"count"},{"id":"minutes","type":"number","step":"any","default":5,"unit":"min","unit_options":["min"],"unit_category":"time"},{"id":"errors","type":"number","step":1,"default":5,"unit":"errors","unit_options":["errors"],"unit_category":"count"}],
    outputs=[{"id":"wpm","unit":"WPM"},{"id":"net_wpm","unit":"WPM"},{"id":"accuracy","unit":"%"}],formula="var w=parseFloat(inputs.words)||0;var m=parseFloat(inputs.minutes)||1;var e=parseFloat(inputs.errors)||0;var wpm=w/m;var net=(w-e)/m;var acc=((w-e)/w)*100;return{wpm:wpm.toFixed(1),net_wpm:net.toFixed(1),accuracy:acc.toFixed(1)};",
    related=["519","510"],latex_formula="\\text{WPM} = \\frac{\\text{Words}}{\\text{Minutes}}, \\quad \\text{Net WPM} = \\frac{\\text{Words} - \\text{Errors}}{\\text{Minutes}}",
    i18n=i18n("Palabras por Minuto (WPM)","Typing Speed (WPM)","Mots par Minute (MPM)","Palavras por Minuto (PPM)","Worte pro Minute (WPM)","Parole al Minuto (PAM)","Calcula tu velocidad de escritura en palabras por minuto.","Calculate your typing speed in words per minute.","Calculez votre vitesse de frappe en mots par minute.","Calcule sua velocidade de digitação em palavras por minuto.","Berechnen Sie Ihre Tippgeschwindigkeit in Worten pro Minute.","Calcola la tua velocità di battitura in parole al minuto.",
        {"words":"Palabras","minutes":"Minutos","errors":"Errores"},{"words":"Words","minutes":"Minutes","errors":"Errors"},{"words":"Mots","minutes":"Minutes","errors":"Erreurs"},{"words":"Palavras","minutes":"Minutos","errors":"Erros"},{"words":"Wörter","minutes":"Minuten","errors":"Fehler"},{"words":"Parole","minutes":"Minuti","errors":"Errori"},
        {"wpm":"WPM bruto","net_wpm":"WPM neto","accuracy":"Precisión %"},{"wpm":"Gross WPM","net_wpm":"Net WPM","accuracy":"Accuracy %"},{"wpm":"MPM brut","net_wpm":"MPM net","accuracy":"Précision %"},{"wpm":"PPM bruto","net_wpm":"PPM líquido","accuracy":"Precisão %"},{"wpm":"Brutto WPM","net_wpm":"Netto WPM","accuracy":"Genauigkeit %"},{"wpm":"PAM lordo","net_wpm":"PAM netto","accuracy":"Precisione %"}),
    use_cases=[{"en":"Job Screening","en_body":"Administrative positions often require 60+ WPM as a minimum qualification for data entry roles."},{"en":"Programming Productivity","en_body":"Developers with higher typing speeds spend less time on syntax and more time on problem solving."},{"en":"Captioning","en_body":"Real-time court reporters achieve 225+ WPM using stenography machines to record spoken testimony."}],
    steps=[{"en":"Enter total words typed."},{"en":"Enter time in minutes."},{"en":"Enter number of errors."}])

add(id="519",block="cotidiano",cat="D",domain="tech",concept="reading time",
    slugs={"es":"tiempo-lectura","en":"reading-time","fr":"temps-de-lecture","pt":"tempo-leitura","de":"lesezeit","it":"tempo-lettura"},
    inputs=[{"id":"word_count","type":"number","step":1,"default":1000,"unit":"words","unit_options":["words"],"unit_category":"count"},{"id":"wpm","type":"number","step":"any","default":200,"unit":"WPM","unit_options":["WPM"],"unit_category":"count"}],
    outputs=[{"id":"minutes","unit":"min"}],formula="var wc=parseFloat(inputs.word_count)||0;var wpm=parseFloat(inputs.wpm)||200;var min=wc/wpm;return{minutes:min.toFixed(1)};",
    related=["518","510"],latex_formula="\\text{Time} = \\frac{\\text{Word Count}}{\\text{WPM}}",
    i18n=i18n("Tiempo de Lectura","Reading Time Calculator","Temps de Lecture","Tempo de Leitura","Lesezeit","Tempo di Lettura","Calcula cuánto tarda leer un texto.","Calculate how long it takes to read a text.","Calculez le temps nécessaire pour lire un texte.","Calcule quanto tempo leva para ler um texto.","Berechnen Sie die Lesezeit eines Textes.","Calcola quanto tempo ci vuole per leggere un testo.",
        {"word_count":"Número de palabras","wpm":"Velocidad lectura"},{"word_count":"Word count","wpm":"Reading speed"},{"word_count":"Nombre de mots","wpm":"Vitesse lecture"},{"word_count":"Contagem palavras","wpm":"Velocidade leitura"},{"word_count":"Wortanzahl","wpm":"Lesegeschwindigkeit"},{"word_count":"Numero parole","wpm":"Velocità lettura"},
        {"minutes":"Minutos"},{"minutes":"Minutes"},{"minutes":"Minutes"},{"minutes":"Minutos"},{"minutes":"Minuten"},{"minutes":"Minuti"}),
    use_cases=[{"en":"Blog UX","en_body":"Content managers display estimated reading times to help readers decide whether to commit to long articles."},{"en":"Audiobook Planning","en_body":"Listeners estimate total listening time from word counts to fit books into commute schedules."},{"en":"Presentation Prep","en_body":"Speakers calculate reading time to ensure speeches fit within allocated time slots."}],
    steps=[{"en":"Enter word count."},{"en":"Enter reading speed in WPM."}])

add(id="520",block="cotidiano",cat="D",domain="tech",concept="text message cost",
    slugs={"es":"coste-sms","en":"sms-cost","fr":"cout-sms","pt":"custo-sms","de":"sms-kosten","it":"costo-sms"},
    inputs=[{"id":"messages","type":"number","step":1,"default":100,"unit":"SMS","unit_options":["SMS"],"unit_category":"count"},{"id":"cost_per","type":"number","step":"any","default":0.05,"unit":"$/SMS","unit_options":["$/SMS","€/SMS"],"unit_category":"currency"}],
    outputs=[{"id":"total_cost","unit":"USD"}],formula="var msg=parseFloat(inputs.messages)||0;var c=parseFloat(inputs.cost_per)||0;return{total_cost:(msg*c).toFixed(2)};",
    related=["512","510"],latex_formula="\\text{Total} = \\text{Messages} \\times \\text{Cost per SMS}",
    i18n=i18n("Coste de SMS","SMS Cost Calculator","Coût SMS","Custo de SMS","SMS-Kosten","Costo SMS","Calcula el coste total de enviar mensajes de texto.","Calculate the total cost of sending text messages.","Calculez le coût total d'envoi de SMS.","Calcule o custo total de envio de mensagens de texto.","Berechnen Sie die Gesamtkosten für den Versand von SMS.","Calcola il costo totale dell'invio di messaggi di testo.",
        {"messages":"Número de SMS","cost_per":"Coste/SMS"},{"messages":"Number of SMS","cost_per":"Cost per SMS"},{"messages":"Nombre de SMS","cost_per":"Coût/SMS"},{"messages":"Número de SMS","cost_per":"Custo/SMS"},{"messages":"Anzahl SMS","cost_per":"Kosten/SMS"},{"messages":"Numero di SMS","cost_per":"Costo/SMS"},
        {"total_cost":"Coste total"},{"total_cost":"Total cost"},{"total_cost":"Coût total"},{"total_cost":"Custo total"},{"total_cost":"Gesamtkosten"},{"total_cost":"Costo totale"}),
    use_cases=[{"en":"Business Messaging","en_body":"Retailers estimate SMS marketing campaign costs before sending promotional blasts to customer lists."},{"en":"International Roaming","en_body":"Travelers compute text message costs abroad to avoid bill shock from per-message roaming fees."},{"en":"Two-Factor Auth","en_body":"SaaS companies model OTP SMS delivery costs as user bases scale into millions."}],
    steps=[{"en":"Enter number of messages."},{"en":"Enter cost per SMS."}])

add(id="521",block="cotidiano",cat="D",domain="tech",concept="data usage estimator",
    slugs={"es":"estimador-datos","en":"data-usage-estimator","fr":"estimateur-donnees","pt":"estimador-dados","de":"datennutzung-schaetzer","it":"stimatore-dati"},
    inputs=[{"id":"hours_video","type":"number","step":"any","default":2,"unit":"h","unit_options":["h"],"unit_category":"time"},{"id":"hours_music","type":"number","step":"any","default":3,"unit":"h","unit_options":["h"],"unit_category":"time"},{"id":"hours_web","type":"number","step":"any","default":4,"unit":"h","unit_options":["h"],"unit_category":"time"}],
    outputs=[{"id":"total_gb","unit":"GB"}],formula="var vid=parseFloat(inputs.hours_video)||0;var mus=parseFloat(inputs.hours_music)||0;var web=parseFloat(inputs.hours_web)||0;var total=vid*3+mus*0.1+web*0.05;return{total_gb:total.toFixed(2)};",
    related=["504","520"],latex_formula="\\text{Total} = 3\\text{GB/h}_{video} + 0.1\\text{GB/h}_{music} + 0.05\\text{GB/h}_{web}",
    i18n=i18n("Estimador de Uso de Datos","Data Usage Estimator","Estimateur de Données","Estimador de Uso de Dados","Datennutzung-Schätzer","Stimatore Dati","Estima tu consumo mensual de datos móviles.","Estimate your monthly mobile data consumption.","Estimez votre consommation mensuelle de données mobiles.","Estime seu consumo mensal de dados móveis.","Schätzen Sie Ihren monatlichen Mobilfunkdatenverbrauch.","Stima il tuo consumo mensile di dati mobili.",
        {"hours_video":"Horas video","hours_music":"Horas música","hours_web":"Horas web"},{"hours_video":"Video hours","hours_music":"Music hours","hours_web":"Web hours"},{"hours_video":"Heures vidéo","hours_music":"Heures musique","hours_web":"Heures web"},{"hours_video":"Horas vídeo","hours_music":"Horas música","hours_web":"Horas web"},{"hours_video":"Videostunden","hours_music":"Musikstunden","hours_web":"Webstunden"},{"hours_video":"Ore video","hours_music":"Ore musica","hours_web":"Ore web"},
        {"total_gb":"Total GB"},{"total_gb":"Total GB"},{"total_gb":"Total GB"},{"total_gb":"Total GB"},{"total_gb":"Total GB"},{"total_gb":"Total GB"}),
    use_cases=[{"en":"Plan Selection","en_body":"Mobile subscribers choose between 5 GB, 10 GB, or unlimited plans based on estimated usage patterns."},{"en":"Travel eSIMs","en_body":"Travelers buy appropriately sized eSIM data packages for trips without overpaying for unused capacity."},{"en":"Remote Work","en_body":"Digital nomads calculate hotspot data needs for video calls when coworking Wi-Fi is unreliable."}],
    steps=[{"en":"Enter daily hours of video streaming."},{"en":"Enter daily hours of music streaming."},{"en":"Enter daily hours of web browsing."}])

add(id="522",block="cotidiano",cat="D",domain="tech",concept="screen brightness nits",
    slugs={"es":"brillo-pantalla-nits","en":"screen-brightness-nits","fr":"luminosite-ecran-nits","pt":"brilho-tela-nits","de":"bildschirmhelligkeit-nits","it":"luminosita-schermo-nits"},
    inputs=[{"id":"lumens","type":"number","step":"any","default":300,"unit":"lm","unit_options":["lm"],"unit_category":""},{"id":"area","type":"number","step":"any","default":0.1,"unit":"m²","unit_options":["m²","cm²"],"unit_category":"area"}],
    outputs=[{"id":"nits","unit":"cd/m²"}],formula="var lum=parseFloat(inputs.lumens)||0;var a=parseFloat(inputs.area)||1;var nits=lum/a;return{nits:nits.toFixed(2)};",
    related=["507","513"],latex_formula="\\text{Nits} = \\frac{\\text{Lumens}}{\\text{Area} \\times \\pi} \\times \\text{gain} \\approx \\frac{\\text{Lumens}}{\\text{Area}}",
    i18n=i18n("Brillo de Pantalla en Nits","Screen Brightness in Nits","Luminosité Écran en Nits","Brilho da Tela em Nits","Bildschirmhelligkeit in Nits","Luminosità Schermo in Nits","Calcula el brillo de una pantalla en nits.","Calculate screen brightness in nits.","Calculez la luminosité d'un écran en nits.","Calcule o brilho de uma tela em nits.","Berechnen Sie die Bildschirmhelligkeit in Nits.","Calcola la luminosità dello schermo in nits.",
        {"lumens":"Lúmenes","area":"Área"},{"lumens":"Lumens","area":"Area"},{"lumens":"Lumens","area":"Surface"},{"lumens":"Lúmens","area":"Área"},{"lumens":"Lumen","area":"Fläche"},{"lumens":"Lumen","area":"Area"},
        {"nits":"Nits (cd/m²)"},{"nits":"Nits (cd/m²)"},{"nits":"Nits (cd/m²)"},{"nits":"Nits (cd/m²)"},{"nits":"Nits (cd/m²)"},{"nits":"Nits (cd/m²)"}),
    use_cases=[{"en":"HDR Certification","en_body":"Display manufacturers target 1,000+ nits to meet DisplayHDR 1000 certification requirements."},{"en":"Outdoor Readability","en_body":"Smartphone screens need 700+ nits for comfortable viewing in direct sunlight."},{"en":"Cinema Projectors","en_body":"Theaters project at around 50 nits, far below consumer TVs, to preserve dark-scene detail."}],
    steps=[{"en":"Enter total light output in lumens."},{"en":"Enter screen area in square meters."}])


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
    print(f"[OK] Added {added} calculators")

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
    # Check existing IDs
    existing = set()
    for line in content.splitlines():
        if '"id"' in line:
            try:
                idx = line.find('"id": "') + 7
                end = line.find('"', idx)
                existing.add(line[idx:end])
            except:
                pass
    entries = []
    for calc in CATALOG:
        if calc["id"] in existing:
            continue
        slug_parts = [f'"{k}": "{v}"' for k, v in calc["slugs"].items()]
        entries.append(f'    {{"id": "{calc["id"]}", "cat": "{calc["cat"]}", "block": "{calc["block"]}", "slugs": {{{", ".join(slug_parts)}}}}},')
    if not entries:
        print("[OK] No new TOOLS entries needed")
        return
    new_block = "\n".join(entries)
    new_content = content.replace(marker, "\n" + new_block + "\n" + marker)
    with open(TOOLS_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"[OK] Added {len(entries)} TOOLS entries")

def generate_content():
    for calc in CATALOG:
        for lang in LANGS:
            html = engine.generate(calc, lang)
            out_path = CONTENT_DIR / lang / f"{calc['id']}.html"
            out_path.write_text(html, encoding="utf-8")
    print(f"[OK] Generated {len(CATALOG) * len(LANGS)} content files")

def main():
    print(f"CalcToWork Batch 2 Generator – {len(CATALOG)} calculators")
    print("=" * 60)
    print("[1] Verifying formulas...")
    ok = sum(1 for calc in CATALOG if verify_formula(calc))
    print(f"[OK] {ok}/{len(CATALOG)} formulas passed")
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

#!/usr/bin/env python3
"""Phase 2 Step 2: Add TOOLS entries to tools_config.py"""
import os, sys, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
TOOLS_FILE = os.path.join(BASE, "scripts", "tools_config.py")

TOOLS_DATA = [
    ("600","estadistica","calculadora-media","mean-calculator","calculateur-moyenne","calculadora-media","mittelwert-rechner","calcolatore-media"),
    ("601","estadistica","calculadora-mediana","median-calculator","calculateur-mediane","calculadora-mediana","median-rechner","calcolatore-mediana"),
    ("602","estadistica","calculadora-desviacion-estandar","standard-deviation-calculator","calculateur-ecart-type","calculadora-desvio-padrao","standardabweichung-rechner","calcolatore-deviazione-standard"),
    ("603","estadistica","calculadora-probabilidad","probability-calculator","calculateur-probabilite","calculadora-probabilidade","wahrscheinlichkeitsrechner","calcolatore-probabilita"),
    ("604","estadistica","calculadora-combinaciones","combinations-calculator","calculateur-combinaisons","calculadora-combinacoes","kombinationen-rechner","calcolatore-combinazioni"),
    ("605","estadistica","calculadora-permutaciones","permutations-calculator","calculateur-permutations","calculadora-permutacoes","permutationen-rechner","calcolatore-permutazioni"),
    ("606","estadistica","calculadora-intervalo-confianza","confidence-interval-calculator","calculateur-intervalle-confiance","calculadora-intervalo-confianca","konfidenzintervall-rechner","calcolatore-intervallo-confidenza"),
    ("607","estadistica","calculadora-coeficiente-variacion","coefficient-of-variation-calculator","calculateur-coefficient-variation","calculadora-coeficiente-variacao","variationskoeffizient-rechner","calcolatore-coefficiente-variazione"),
    ("608","estadistica","calculadora-varianza","variance-calculator","calculateur-variance","calculadora-variancia","varianz-rechner","calcolatore-varianza"),
    ("609","estadistica","calculadora-puntuacion-z","z-score-calculator","calculateur-score-z","calculadora-escore-z","z-wert-rechner","calcolatore-punteggio-z"),
    ("700","ciencia","calculadora-velocidad","speed-calculator","calculateur-vitesse","calculadora-velocidade","geschwindigkeitsrechner","calcolatore-velocita"),
    ("701","ciencia","calculadora-densidad","density-calculator","calculateur-densite","calculadora-densidade","dichte-rechner","calcolatore-densita"),
    ("702","ciencia","calculadora-fuerza","force-calculator","calculateur-force","calculadora-forca","kraft-rechner","calcolatore-forza"),
    ("703","ciencia","calculadora-energia-cinetica","kinetic-energy-calculator","calculateur-energie-cinetique","calculadora-energia-cinetica","kinetische-energie-rechner","calcolatore-energia-cinetica"),
    ("704","ciencia","calculadora-energia-potencial","potential-energy-calculator","calculateur-energie-potentielle","calculadora-energia-potencial","potentielle-energie-rechner","calcolatore-energia-potenziale"),
    ("705","ciencia","calculadora-presion","pressure-calculator","calculateur-pression","calculadora-pressao","druck-rechner","calcolatore-pressione"),
    ("706","ciencia","calculadora-trabajo-mecanico","work-calculator","calculateur-travail","calculadora-trabalho-mecanico","arbeit-rechner","calcolatore-lavoro-meccanico"),
    ("707","ciencia","calculadora-ley-ohm","ohms-law-calculator","calculateur-loi-ohm","calculadora-lei-de-ohm","ohmsches-gesetz-rechner","calcolatore-legge-di-ohm"),
    ("708","ciencia","calculadora-potencia-electrica","electrical-power-calculator","calculateur-puissance-electrique","calculadora-potencia-eletrica","elektrische-leistung-rechner","calcolatore-potenza-elettrica"),
    ("709","ciencia","calculadora-aceleracion","acceleration-calculator","calculateur-acceleration","calculadora-aceleracao","beschleunigungsrechner","calcolatore-accelerazione"),
    ("800","conversion","convertidor-longitud","length-converter","convertisseur-longueur","conversor-comprimento","laengenumrechner","convertitore-lunghezza"),
    ("801","conversion","convertidor-peso","weight-converter","convertisseur-poids","conversor-peso","gewichtsumrechner","convertitore-peso"),
    ("802","conversion","convertidor-temperatura","temperature-converter","convertisseur-temperature","conversor-temperatura","temperaturumrechner","convertitore-temperatura"),
    ("803","conversion","convertidor-volumen","volume-converter","convertisseur-volume","conversor-volume","volumenumrechner","convertitore-volume"),
    ("804","conversion","convertidor-area","area-converter","convertisseur-surface","conversor-area","flaechenumrechner","convertitore-area"),
    ("805","conversion","convertidor-velocidad","speed-converter","convertisseur-vitesse","conversor-velocidade","geschwindigkeitsumrechner","convertitore-velocita"),
    ("806","conversion","convertidor-datos-digitales","data-storage-converter","convertisseur-donnees","conversor-dados-digitais","datenumrechner","convertitore-dati-digitali"),
    ("807","conversion","convertidor-presion","pressure-converter","convertisseur-pression","conversor-pressao","druckumrechner","convertitore-pressione"),
    ("808","conversion","convertidor-tiempo","time-converter","convertisseur-temps","conversor-tempo","zeitumrechner","convertitore-tempo"),
    ("809","conversion","convertidor-energia","energy-converter","convertisseur-energie","conversor-energia","energieumrechner","convertitore-energia"),
    ("900","deportes","calculadora-ritmo-carrera","running-pace-calculator","calculateur-allure-course","calculadora-ritmo-corrida","laufpace-rechner","calcolatore-ritmo-corsa"),
    ("901","deportes","calculadora-calorias-ejercicio","exercise-calorie-calculator","calculateur-calories-exercice","calculadora-calorias-exercicio","trainingskalorien-rechner","calcolatore-calorie-esercizio"),
    ("902","deportes","calculadora-frecuencia-cardiaca-max","max-heart-rate-calculator","calculateur-fc-max","calculadora-frequencia-cardiaca-max","maximalpuls-rechner","calcolatore-frequenza-cardiaca-max"),
    ("903","deportes","calculadora-zonas-cardiacas","heart-rate-zones-calculator","calculateur-zones-cardiaques","calculadora-zonas-cardiacas","herzfrequenz-zonen-rechner","calcolatore-zone-cardiache"),
    ("904","deportes","calculadora-vo2-max","vo2-max-calculator","calculateur-vo2-max","calculadora-vo2-max","vo2max-rechner","calcolatore-vo2-max"),
    ("905","deportes","calculadora-pasos-calorias","steps-to-calories-calculator","calculateur-pas-calories","calculadora-passos-calorias","schritte-kalorien-rechner","calcolatore-passi-calorie"),
    ("906","deportes","calculadora-ritmo-natacion","swimming-pace-calculator","calculateur-allure-natation","calculadora-ritmo-natacao","schwimmpace-rechner","calcolatore-ritmo-nuoto"),
    ("907","deportes","calculadora-ritmo-ciclismo","cycling-pace-calculator","calculateur-allure-cyclisme","calculadora-ritmo-ciclismo","radpace-rechner","calcolatore-ritmo-ciclismo"),
    ("908","deportes","calculadora-imc-deportista","athletic-bmi-calculator","calculateur-imc-sportif","calculadora-imc-atleta","sport-bmi-rechner","calcolatore-imc-sportivo"),
    ("909","deportes","calculadora-tiempo-pista","race-time-predictor","calculateur-temps-course","calculadora-tempo-pista","laufzeit-rechner","calcolatore-tempo-pista"),
    ("210","matematicas","calculadora-area-circulo","circle-area-calculator","calculateur-aire-cercle","calculadora-area-circulo","kreisflaechenrechner","calcolatore-area-cerchio"),
    ("211","matematicas","calculadora-area-triangulo","triangle-area-calculator","calculateur-aire-triangle","calculadora-area-triangulo","dreiecksflaechenrechner","calcolatore-area-triangolo"),
    ("212","matematicas","calculadora-volumen-esfera","sphere-volume-calculator","calculateur-volume-sphere","calculadora-volume-esfera","kugelvolumenrechner","calcolatore-volume-sfera"),
    ("213","matematicas","calculadora-volumen-cilindro","cylinder-volume-calculator","calculateur-volume-cylindre","calculadora-volume-cilindro","zylindervolumenrechner","calcolatore-volume-cilindro"),
    ("214","matematicas","calculadora-potencias","exponent-calculator","calculateur-puissance","calculadora-potencias","potenzrechner","calcolatore-potenze"),
    ("215","matematicas","calculadora-raiz","root-calculator","calculateur-racine","calculadora-raiz","wurzelrechner","calcolatore-radice"),
    ("216","matematicas","calculadora-logaritmo","logarithm-calculator","calculateur-logarithme","calculadora-logaritmo","logarithmusrechner","calcolatore-logaritmo"),
    ("217","matematicas","calculadora-factorial","factorial-calculator","calculateur-factorielle","calculadora-fatorial","fakultaet-rechner","calcolatore-fattoriale"),
    ("218","matematicas","calculadora-ecuacion-segundo-grado","quadratic-equation-calculator","calculateur-equation-second-degre","calculadora-equacao-segundo-grau","quadratische-gleichung-rechner","calcolatore-equazione-secondo-grado"),
    ("219","matematicas","calculadora-mcm-mcd","lcm-gcd-calculator","calculateur-ppcm-pgcd","calculadora-mmc-mdc","kgv-ggt-rechner","calcolatore-mcm-mcd"),
    ("310","finanzas","calculadora-roi","roi-calculator","calculateur-roi","calculadora-roi","roi-rechner","calcolatore-roi"),
    ("311","finanzas","calculadora-ahorro-compuesto","compound-savings-calculator","calculateur-epargne-composee","calculadora-poupanca-composta","zinssparrechner","calcolatore-risparmio-composto"),
    ("312","finanzas","calculadora-inflacion","inflation-calculator","calculateur-inflation","calculadora-inflacao","inflationsrechner","calcolatore-inflazione"),
    ("313","finanzas","calculadora-subida-salarial","salary-increase-calculator","calculateur-augmentation-salaire","calculadora-aumento-salarial","gehaltserhoehung-rechner","calcolatore-aumento-stipendio"),
    ("314","finanzas","calculadora-plan-jubilacion","retirement-calculator","calculateur-retraite","calculadora-plano-aposentadoria","rentenrechner","calcolatore-piano-pensione"),
    ("315","finanzas","calculadora-regla-72","rule-of-72-calculator","calculateur-regle-72","calculadora-regra-72","regel-72-rechner","calcolatore-regola-72"),
    ("316","finanzas","calculadora-deposito-plazo","term-deposit-calculator","calculateur-depot-a-terme","calculadora-deposito-prazo","festgeldrechner","calcolatore-deposito-termine"),
    ("317","finanzas","calculadora-retorno-acciones","stock-return-calculator","calculateur-rendement-actions","calculadora-retorno-acoes","aktienrendite-rechner","calcolatore-rendimento-azioni"),
    ("318","finanzas","calculadora-ratio-deuda","debt-to-income-calculator","calculateur-ratio-dette","calculadora-ratio-divida","schuldenquote-rechner","calcolatore-rapporto-debito"),
    ("319","finanzas","calculadora-punto-equilibrio-unidades","break-even-units-calculator","calculateur-seuil-rentabilite","calculadora-ponto-equilibrio-unidades","break-even-rechner","calcolatore-punto-pareggio"),
    ("410","salud","calculadora-metabolismo-basal","bmr-calculator","calculateur-metabolisme-base","calculadora-metabolismo-basal","grundumsatz-rechner","calcolatore-metabolismo-basale"),
    ("411","salud","calculadora-frecuencia-cardiaca-max-salud","max-heart-rate-health-calculator","calculateur-fc-max-sante","calculadora-frequencia-cardiaca-max-saude","maximalpuls-gesundheit","calcolatore-frequenza-cardiaca-max-salute"),
    ("412","salud","calculadora-horas-sueno","sleep-calculator","calculateur-sommeil","calculadora-horas-sono","schlafrechner","calcolatore-ore-sonno"),
    ("413","salud","calculadora-porcentaje-grasa","body-fat-calculator","calculateur-graisse-corporelle","calculadora-porcentagem-gordura","koerperfett-rechner","calcolatore-percentuale-grasso"),
    ("414","salud","calculadora-rango-peso-saludable","healthy-weight-range-calculator","calculateur-poids-sante","calculadora-faixa-peso-saudavel","gesundheitsgewicht-rechner","calcolatore-peso-salutare"),
]

with open(TOOLS_FILE, "r", encoding="utf-8") as f:
    content = f.read()

existing_ids = set(re.findall(r'"id":\s*"(\d+)"', content))
added = 0
lines = []
for row in TOOLS_DATA:
    cid, block = row[0], row[1]
    if cid in existing_ids:
        continue
    slugs = f'"es": "{row[2]}", "en": "{row[3]}", "fr": "{row[4]}", "pt": "{row[5]}", "de": "{row[6]}", "it": "{row[7]}"'
    lines.append(f'    {{"id": "{cid}", "cat": "E", "block": "{block}", "slugs": {{{slugs}}}}},')
    added += 1

if lines:
    marker = "\nPARAMETRIC_VARIANTS"
    idx = content.find(marker)
    if idx == -1:
        idx = len(content)
    block_text = "\n    # ── Phase 2 calculators ──\n" + "\n".join(lines) + "\n\n"
    content = content[:idx] + block_text + content[idx:]
    with open(TOOLS_FILE, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Added {added} TOOLS entries. Run phase2_add_i18n.py next.")

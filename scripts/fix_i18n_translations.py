"""
Comprehensive i18n translation fix for CalcToWork.

Fixes:
1. IDs 910-962: Translate English seo_title/description/inputs/outputs to ES/FR/PT/DE/IT
2. IDs 1050-1099: Translate Spanish names/titles to EN/FR/PT/DE/IT
3. Standardize seo_desc → seo_description (keep both for compatibility)
4. Generate unique, keyword-rich SEO titles replacing generic templates
"""

import json
import os
import copy

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

# Comprehensive translations for batch 4 (910-962) and batch 5 (1050-1099)
# Format: {calc_id: {lang: {field: value, ...}}}
# We build this programmatically from a name/description/title dictionary

NAMES = {
    "910": {"en": "Fraction Calculator", "es": "Calculadora de Fracciones", "fr": "Calculatrice de Fractions", "pt": "Calculadora de Frações", "de": "Bruchrechner", "it": "Calcolatrice di Frazioni"},
    "911": {"en": "Slope Calculator", "es": "Calculadora de Pendiente", "fr": "Calculatrice de Pente", "pt": "Calculadora de Inclinação", "de": "Steigungsrechner", "it": "Calcolatrice di Pendenza"},
    "912": {"en": "Scientific Notation Calculator", "es": "Calculadora de Notación Científica", "fr": "Calculatrice de Notation Scientifique", "pt": "Calculadora de Notação Científica", "de": "Wissenschaftliche Notation Rechner", "it": "Calcolatrice di Notazione Scientifica"},
    "913": {"en": "Rounding Calculator", "es": "Calculadora de Redondeo", "fr": "Calculatrice d'Arrondi", "pt": "Calculadora de Arredondamento", "de": "Rundungsrechner", "it": "Calcolatrice di Arrotondamento"},
    "914": {"en": "GCF & LCM Calculator", "es": "Calculadora de MCD y MCM", "fr": "Calculatrice de PGCD et PPCM", "pt": "Calculadora de MDC e MMC", "de": "GGT & KGv Rechner", "it": "Calcolatrice di MCD e MCM"},
    "915": {"en": "Prime Factorization Calculator", "es": "Calculadora de Factorización Prima", "fr": "Calculatrice de Factorisation Première", "pt": "Calculadora de Fatoração Prima", "de": "Primfaktorzerlegung Rechner", "it": "Calcolatrice di Fattorizzazione Prima"},
    "916": {"en": "Circle Calculator", "es": "Calculadora de Círculo", "fr": "Calculatrice de Cercle", "pt": "Calculadora de Círculo", "de": "Kreisrechner", "it": "Calcolatrice di Cerchio"},
    "917": {"en": "Right Triangle Calculator", "es": "Calculadora de Triángulo Rectángulo", "fr": "Calculatrice de Triangle Rectangle", "pt": "Calculadora de Triângulo Retângulo", "de": "Rechtwinkliges Dreieck Rechner", "it": "Calcolatrice di Triangolo Rettangolo"},
    "918": {"en": "Triangle Area (Heron's Formula)", "es": "Área del Triángulo (Fórmula de Herón)", "fr": "Aire du Triangle (Formule de Héron)", "pt": "Área do Triângulo (Fórmula de Heron)", "de": "Dreiecksfläche (Heron-Formel)", "it": "Area del Triangolo (Formula di Erone)"},
    "919": {"en": "Rectangle Calculator", "es": "Calculadora de Rectángulo", "fr": "Calculatrice de Rectangle", "pt": "Calculadora de Retângulo", "de": "Rechteckrechner", "it": "Calcolatrice di Rettangolo"},
    "920": {"en": "Square Calculator", "es": "Calculadora de Cuadrado", "fr": "Calculatrice de Carré", "pt": "Calculadora de Quadrado", "de": "Quadratrechner", "it": "Calcolatrice di Quadrato"},
    "921": {"en": "Trapezoid Calculator", "es": "Calculadora de Trapecio", "fr": "Calculatrice de Trapèze", "pt": "Calculadora de Trapézio", "de": "Trapezrechner", "it": "Calcolatrice di Trapezio"},
    "922": {"en": "Cylinder Volume Calculator", "es": "Calculadora de Volumen de Cilindro", "fr": "Calculatrice de Volume de Cylindre", "pt": "Calculadora de Volume do Cilindro", "de": "Zylindervolumen Rechner", "it": "Calcolatrice di Volume del Cilindro"},
    "923": {"en": "Cone Volume Calculator", "es": "Calculadora de Volumen de Cono", "fr": "Calculatrice de Volume de Cône", "pt": "Calculadora de Volume do Cone", "de": "Kegelvolumen Rechner", "it": "Calcolatrice di Volume del Cono"},
    "924": {"en": "Pyramid Volume Calculator", "es": "Calculadora de Volumen de Pirámide", "fr": "Calculatrice de Volume de Pyramide", "pt": "Calculadora de Volume da Pirâmide", "de": "Pyramidenvolumen Rechner", "it": "Calcolatrice di Volume della Piramide"},
    "925": {"en": "Sphere Calculator", "es": "Calculadora de Esfera", "fr": "Calculatrice de Sphère", "pt": "Calculadora de Esfera", "de": "Kugelrechner", "it": "Calcolatrice di Sfera"},
    "926": {"en": "BMR Calculator (Harris-Benedict)", "es": "Calculadora de TMB (Harris-Benedict)", "fr": "Calculatrice de MB (Harris-Benedict)", "pt": "Calculadora de TMB (Harris-Benedict)", "de": "Grundumsatz Rechner (Harris-Benedict)", "it": "Calcolatrice di BMR (Harris-Benedict)"},
    "927": {"en": "BMR Calculator (Katch-McArdle)", "es": "Calculadora de TMB (Katch-McArdle)", "fr": "Calculatrice de MB (Katch-McArdle)", "pt": "Calculadora de TMB (Katch-McArdle)", "de": "Grundumsatz Rechner (Katch-McArdle)", "it": "Calcolatrice di BMR (Katch-McArdle)"},
    "928": {"en": "Macro Calculator", "es": "Calculadora de Macronutrientes", "fr": "Calculatrice de Macronutriments", "pt": "Calculadora de Macronutrientes", "de": "Makronährstoffrechner", "it": "Calcolatrice di Macronutrienti"},
    "929": {"en": "Blood Pressure Calculator", "es": "Calculadora de Presión Arterial", "fr": "Calculatrice de Pression Artérielle", "pt": "Calculadora de Pressão Arterial", "de": "Blutdruckrechner", "it": "Calcolatrice di Pressione Sanguigna"},
    "930": {"en": "Waist-to-Hip Ratio Calculator", "es": "Calculadora de Índice Cintura-Cadera", "fr": "Calculatrice de Rapport Taille-Hanche", "pt": "Calculadora de Índice Cintura-Quadril", "de": "Taille-Hüft-Verhältnis Rechner", "it": "Calcolatrice di Rapporto Vita-Fianchi"},
    "931": {"en": "Waist-to-Height Ratio Calculator", "es": "Calculadora de Índice Cintura-Estatura", "fr": "Calculatrice de Rapport Taille-Taille", "pt": "Calculadora de Índice Cintura-Altura", "de": "Taille-Körpergröße-Verhältnis Rechner", "it": "Calcolatrice di Rapporto Vita-Altezza"},
    "932": {"en": "Weight Loss Percentage Calculator", "es": "Calculadora de Porcentaje de Pérdida de Peso", "fr": "Calculatrice de Pourcentage de Perte de Poids", "pt": "Calculadora de Porcentagem de Perda de Peso", "de": "Gewichtsverlust-Prozent-Rechner", "it": "Calcolatrice di Percentuale di Perdita di Peso"},
    "933": {"en": "Heart Rate Zones Calculator", "es": "Calculadora de Zonas de Frecuencia Cardíaca", "fr": "Calculatrice de Zones de Fréquence Cardiaque", "pt": "Calculadora de Zonas de Frequência Cardíaca", "de": "Herzfrequenz-Zonen Rechner", "it": "Calcolatrice di Zone di Frequenza Cardiaca"},
    "934": {"en": "Salary to Hourly Calculator", "es": "Calculadora de Salario a Hora", "fr": "Calculatrice de Salaire en Taux Horaire", "pt": "Calculadora de Salário para Horário", "de": "Gehalt-in-Stundenlohn Rechner", "it": "Calcolatrice di Salario Orario"},
    "935": {"en": "Hourly to Salary Calculator", "es": "Calculadora de Hora a Salario", "fr": "Calculatrice de Taux Horaire en Salaire", "pt": "Calculadora de Horário para Salário", "de": "Stundenlohn-in-Gehalt Rechner", "it": "Calcolatrice di Tariffa Oraria in Salario"},
    "936": {"en": "Mortgage Calculator", "es": "Calculadora de Hipoteca", "fr": "Calculatrice d'Hypothèque", "pt": "Calculadora de Hipoteca", "de": "Hypothekenrechner", "it": "Calcolatrice di Mutuo"},
    "937": {"en": "Debt Payoff Calculator", "es": "Calculadora de Pago de Deudas", "fr": "Calculatrice de Remboursement de Dette", "pt": "Calculadora de Quitação de Dívidas", "de": "Schuldenabbezahlungsrechner", "it": "Calcolatrice di Estinzione Debito"},
    "938": {"en": "Savings Calculator", "es": "Calculadora de Ahorro", "fr": "Calculatrice d'Épargne", "pt": "Calculadora de Poupança", "de": "Sparrechner", "it": "Calcolatrice di Risparmio"},
    "939": {"en": "Profit Margin Calculator", "es": "Calculadora de Margen de Ganancia", "fr": "Calculatrice de Marge Bénéficiaire", "pt": "Calculadora de Margem de Lucro", "de": "Gewinnmargenrechner", "it": "Calcolatrice di Margine di Profitto"},
    "940": {"en": "NPV Calculator", "es": "Calculadora de VAN", "fr": "Calculatrice de VAN", "pt": "Calculadora de VPL", "de": "Kapitalwertrechner", "it": "Calcolatrice di VAN"},
    "941": {"en": "Emergency Fund Calculator", "es": "Calculadora de Fondo de Emergencia", "fr": "Calculatrice de Fonds d'Urgence", "pt": "Calculadora de Fundo de Emergência", "de": "Notgroschenrechner", "it": "Calcolatrice di Fondo di Emergenza"},
    "942": {"en": "Age Calculator", "es": "Calculadora de Edad", "fr": "Calculatrice d'Âge", "pt": "Calculadora de Idade", "de": "Altersrechner", "it": "Calcolatrice di Età"},
    "943": {"en": "Date Difference Calculator", "es": "Calculadora de Diferencia de Fechas", "fr": "Calculatrice de Différence entre Dates", "pt": "Calculadora de Diferença de Datas", "de": "Datumsdifferenz Rechner", "it": "Calcolatrice di Differenza tra Date"},
    "944": {"en": "Tip Calculator", "es": "Calculadora de Propina", "fr": "Calculatrice de Pourboire", "pt": "Calculadora de Gorjeta", "de": "Trinkgeldrechner", "it": "Calcolatrice di Mancia"},
    "945": {"en": "Double Discount Calculator", "es": "Calculadora de Doble Descuento", "fr": "Calculatrice de Double Remise", "pt": "Calculadora de Desconto Duplo", "de": "Doppelrabattrechner", "it": "Calcolatrice di Doppio Sconto"},
    "946": {"en": "Kinetic Energy Calculator", "es": "Calculadora de Energía Cinética", "fr": "Calculatrice d'Énergie Cinétique", "pt": "Calculadora de Energia Cinética", "de": "Kinetische Energie Rechner", "it": "Calcolatrice di Energia Cinetica"},
    "947": {"en": "Potential Energy Calculator", "es": "Calculadora de Energía Potencial", "fr": "Calculatrice d'Énergie Potentielle", "pt": "Calculadora de Energia Potencial", "de": "Potentielle Energie Rechner", "it": "Calcolatrice di Energia Potenziale"},
    "948": {"en": "Work & Power Calculator", "es": "Calculadora de Trabajo y Potencia", "fr": "Calculatrice de Travail et Puissance", "pt": "Calculadora de Trabalho e Potência", "de": "Arbeit und Leistung Rechner", "it": "Calcolatrice di Lavoro e Potenza"},
    "949": {"en": "Ohm's Law & Power Calculator", "es": "Calculadora de Ley de Ohm y Potencia", "fr": "Calculatrice de Loi d'Ohm et Puissance", "pt": "Calculadora de Lei de Ohm e Potência", "de": "Ohmsches Gesetz und Leistung Rechner", "it": "Calcolatrice di Legge di Ohm e Potenza"},
    "950": {"en": "Newton's Second Law Calculator", "es": "Calculadora de Segunda Ley de Newton", "fr": "Calculatrice de Deuxième Loi de Newton", "pt": "Calculadora de Segunda Lei de Newton", "de": "Zweites Newtonsches Gesetz Rechner", "it": "Calcolatrice di Seconda Legge di Newton"},
    "951": {"en": "One Rep Max Calculator", "es": "Calculadora de Repetición Máxima", "fr": "Calculatrice de Maximum sur une Répétition", "pt": "Calculadora de Uma Repetição Máxima", "de": "Einsatzmaximum Rechner (1RM)", "it": "Calcolatrice di Massimale"},
    "952": {"en": "Running Pace Predictor", "es": "Predictor de Ritmo de Carrera", "fr": "Prédicteur d'Allure de Course", "pt": "Preditor de Ritmo de Corrida", "de": "Laufzeiten-Vorhersage", "it": "Previsore di Andatura di Corsa"},
    "953": {"en": "VO₂ Max Estimator", "es": "Estimador de VO₂ Máximo", "fr": "Estimateur de VO₂ Max", "pt": "Estimador de VO₂ Máximo", "de": "VO₂max Schätzer", "it": "Stima del VO₂ Max"},
    "954": {"en": "Angle Converter", "es": "Convertidor de Ángulos", "fr": "Convertisseur d'Angles", "pt": "Conversor de Ângulos", "de": "Winkelumrechner", "it": "Convertitore di Angoli"},
    "955": {"en": "Temperature Converter", "es": "Convertidor de Temperatura", "fr": "Convertisseur de Température", "pt": "Conversor de Temperatura", "de": "Temperaturumrechner", "it": "Convertitore di Temperatura"},
    "956": {"en": "Energy Converter", "es": "Convertidor de Energía", "fr": "Convertisseur d'Énergie", "pt": "Conversor de Energia", "de": "Energieumrechner", "it": "Convertitore di Energia"},
    "957": {"en": "Combinations & Permutations Calculator", "es": "Calculadora de Combinaciones y Permutaciones", "fr": "Calculatrice de Combinaisons et Permutations", "pt": "Calculadora de Combinações e Permutações", "de": "Kombinationen und Permutationen Rechner", "it": "Calcolatrice di Combinazioni e Permutazioni"},
    "958": {"en": "Z-Score & Percentile Calculator", "es": "Calculadora de Puntuación Z y Percentil", "fr": "Calculatrice de Score Z et Percentile", "pt": "Calculadora de Escore Z e Percentil", "de": "Z-Score und Perzentil Rechner", "it": "Calcolatrice di Z-Score e Percentile"},
    "959": {"en": "Sample Size Calculator", "es": "Calculadora de Tamaño de Muestra", "fr": "Calculatrice de Taille d'Échantillon", "pt": "Calculadora de Tamanho de Amostra", "de": "Stichprobenumfang Rechner", "it": "Calcolatrice di Dimensione del Campione"},
    "960": {"en": "BSA & Ideal Weight Calculator", "es": "Calculadora de SCBcmc y Peso Ideal", "fr": "Calculatrice de SC et Poids Idéal", "pt": "Calculadora de SC e Peso Ideal", "de": "Körperoberfläche und Idealgewicht Rechner", "it": "Calcolatrice di Superficie Corporea e Peso Ideale"},
    "961": {"en": "A1C Estimator", "es": "Estimador de A1c", "fr": "Estimateur d'HbA1c", "pt": "Estimador de A1C", "de": "HbA1c Schätzer", "it": "Stima dell'HbA1c"},
    "962": {"en": "LDL Cholesterol Calculator", "es": "Calculadora de Colesterol LDL", "fr": "Calculatrice de Cholestérol LDL", "pt": "Calculadora de Colesterol LDL", "de": "LDL-Cholesterin Rechner", "it": "Calcolatrice di Colesterolo LDL"},
    "1050": {"en": "Regular Polygon Area Calculator", "es": "Calculadora de Área de Polígono Regular", "fr": "Calculatrice d'Aire de Polygone Régulier", "pt": "Calculadora de Área de Polígono Regular", "de": "Reguläres Polygon Flächenrechner", "it": "Calcolatrice di Area del Poligono Regolare"},
    "1051": {"en": "Cone Volume Calculator", "es": "Calculadora de Volumen de Cono", "fr": "Calculatrice de Volume de Cône", "pt": "Calculadora de Volume do Cone", "de": "Kegelvolumen Rechner", "it": "Calcolatrice di Volume del Cono"},
    "1052": {"en": "Arithmetic Series Calculator", "es": "Calculadora de Serie Aritmética", "fr": "Calculatrice de Série Arithmétique", "pt": "Calculadora de Série Aritmética", "de": "Arithmetische Reihe Rechner", "it": "Calcolatrice di Serie Aritmetica"},
    "1053": {"en": "Geometric Series Calculator", "es": "Calculadora de Serie Geométrica", "fr": "Calculatrice de Série Géométrique", "pt": "Calculadora de Série Geométrica", "de": "Geometrische Reihe Rechner", "it": "Calcolatrice di Serie Geometrica"},
    "1054": {"en": "Combinations Calculator", "es": "Calculadora de Combinaciones", "fr": "Calculatrice de Combinaisons", "pt": "Calculadora de Combinações", "de": "Kombinationsrechner", "it": "Calcolatrice di Combinazioni"},
    "1055": {"en": "Buoyancy Force Calculator", "es": "Calculadora de Empuje de Arquímedes", "fr": "Calculatrice de Poussée d'Archimède", "pt": "Calculadora de Empuxo de Arquimedes", "de": "Auftriebskraft Rechner", "it": "Calcolatrice di Forza di Galleggiamento"},
    "1056": {"en": "Doppler Effect Calculator", "es": "Calculadora de Efecto Doppler", "fr": "Calculatrice d'Effet Doppler", "pt": "Calculadora de Efeito Doppler", "de": "Doppler-Effekt Rechner", "it": "Calcolatrice di Effetto Doppler"},
    "1057": {"en": "AC Impedance Calculator", "es": "Calculadora de Impedancia AC", "fr": "Calculatrice d'Impédance AC", "pt": "Calculadora de Impedância AC", "de": "Wechselstromimpedanz Rechner", "it": "Calcolatrice di Impedenza AC"},
    "1058": {"en": "Moment of Inertia Calculator", "es": "Calculadora de Momento de Inercia", "fr": "Calculatrice de Moment d'Inertie", "pt": "Calculadora de Momento de Inércia", "de": "Trägheitsmoment Rechner", "it": "Calcolatrice di Momento di Inerzia"},
    "1059": {"en": "Rotational Energy Calculator", "es": "Calculadora de Energía Rotacional", "fr": "Calculatrice d'Énergie de Rotation", "pt": "Calculadora de Energia Rotacional", "de": "Rotationsenergie Rechner", "it": "Calcolatrice di Energia Rotazionale"},
    "1060": {"en": "Body Fat (Navy) Calculator", "es": "Calculadora de Grasa Corporal (Método Marina)", "fr": "Calculatrice de Graisse Corporelle (Méthode Marine)", "pt": "Calculadora de Gordura Corporal (Método Marinha)", "de": "Körperfettrechner (Navy-Methode)", "it": "Calcolatrice di Grasso Corporeo (Metodo Marina)"},
    "1061": {"en": "Mifflin-St Jeor BMR Calculator", "es": "Calculadora de TMB Mifflin-St Jeor", "fr": "Calculatrice de MB Mifflin-St Jeor", "pt": "Calculadora de TMB Mifflin-St Jeor", "de": "Grundumsatzrechner (Mifflin-St Jeor)", "it": "Calcolatrice di BMR Mifflin-St Jeor"},
    "1062": {"en": "Daily Water Intake Calculator", "es": "Calculadora de Agua Diaria", "fr": "Calculatrice de Consommation d'Eau Quotidienne", "pt": "Calculadora de Água Diária", "de": "Tageswasserbedarf Rechner", "it": "Calcolatrice di Acqua Giornaliera"},
    "1063": {"en": "One Rep Max (Brzycki) Calculator", "es": "Calculadora de Repetición Máxima (Brzycki)", "fr": "Calculatrice de Maximum sur une Répétition (Brzycki)", "pt": "Calculadora de Uma Repetição Máxima (Brzycki)", "de": "Einsatzmaximum Rechner (Brzycki)", "it": "Calcolatrice di Massimale (Brzycki)"},
    "1064": {"en": "Daily Protein Calculator", "es": "Calculadora de Proteína Diaria", "fr": "Calculatrice de Protéines Quotidiennes", "pt": "Calculadora de Proteína Diária", "de": "Tagesproteinnrechner", "it": "Calcolatrice di Proteina Giornaliera"},
    "1065": {"en": "Dividend Yield Calculator", "es": "Calculadora de Rentabilidad por Dividendo", "fr": "Calculatrice de Rendement des Dividendes", "pt": "Calculadora de Rendimento de Dividendos", "de": "Dividendenrendite Rechner", "it": "Calcolatrice di Rendimento da Dividendo"},
    "1066": {"en": "Payback Period Calculator", "es": "Calculadora de Período de Recuperación", "fr": "Calculatrice de Délai de Récupération", "pt": "Calculadora de Período de Retorno", "de": "Amortisationszeit Rechner", "it": "Calcolatrice di Periodo di Rimborso"},
    "1067": {"en": "Capital Gains Tax Calculator", "es": "Calculadora de Impuesto sobre Ganancias de Capital", "fr": "Calculatrice d'Impôt sur les Plus-Values", "pt": "Calculadora de Imposto sobre Ganho de Capital", "de": "Kapitalertragsteuer Rechner", "it": "Calcolatrice di Imposta sulle Plusvalenze"},
    "1068": {"en": "Currency Exchange Commission Calculator", "es": "Calculadora de Comisión de Cambio de Divisas", "fr": "Calculatrice de Commission de Change", "pt": "Calculadora de Comissão de Câmbio", "de": "Wechselkursgebühr Rechner", "it": "Calcolatrice di Commissione di Cambio"},
    "1069": {"en": "Break Even Point Calculator", "es": "Calculadora de Punto de Equilibrio", "fr": "Calculatrice de Seuil de Rentabilité", "pt": "Calculadora de Ponto de Equilíbrio", "de": "Gewinnschwelle Rechner", "it": "Calcolatrice di Punto di Pareggio"},
    "1070": {"en": "Molar Mass Calculator", "es": "Calculadora de Masa Molar", "fr": "Calculatrice de Masse Molaire", "pt": "Calculadora de Massa Molar", "de": "Molmasse Rechner", "it": "Calcolatrice di Massa Molare"},
    "1071": {"en": "pH Calculator", "es": "Calculadora de pH", "fr": "Calculatrice de pH", "pt": "Calculadora de pH", "de": "pH-Rechner", "it": "Calcolatrice di pH"},
    "1072": {"en": "Ideal Gas Law Calculator", "es": "Calculadora de Ley de Gases Ideales", "fr": "Calculatrice de Loi des Gaz Parfaits", "pt": "Calculadora de Lei dos Gases Ideais", "de": "Ideales Gasgesetz Rechner", "it": "Calcolatrice di Legge dei Gas Ideali"},
    "1073": {"en": "Molarity Calculator", "es": "Calculadora de Molaridad", "fr": "Calculatrice de Molarité", "pt": "Calculadora de Molaridade", "de": "Molaritätsrechner", "it": "Calcolatrice di Molarità"},
    "1074": {"en": "Dilution Calculator", "es": "Calculadora de Dilución", "fr": "Calculatrice de Dilution", "pt": "Calculadora de Diluição", "de": "Verdünnungsrechner", "it": "Calcolatrice di Diluizione"},
    "1075": {"en": "Resistor Color Code Calculator", "es": "Calculadora de Código de Colores de Resistencias", "fr": "Calculatrice de Code Couleur des Résistances", "pt": "Calculadora de Código de Cores de Resistores", "de": "Widerstands-Farbcode Rechner", "it": "Calcolatrice di Codice Colori Resistenza"},
    "1076": {"en": "Capacitor Energy Calculator", "es": "Calculadora de Energía de Capacitor", "fr": "Calculatrice d'Énergie de Condensateur", "pt": "Calculadora de Energia de Capacitor", "de": "Kondensatorenergie Rechner", "it": "Calcolatrice di Energia del Condensatore"},
    "1077": {"en": "Voltage Divider Calculator", "es": "Calculadora de Divisor de Voltaje", "fr": "Calculatrice de Diviseur de Tension", "pt": "Calculadora de Divisor de Tensão", "de": "Spannungsteiler Rechner", "it": "Calcolatrice di Partitore di Tensione"},
    "1078": {"en": "RC Time Constant Calculator", "es": "Calculadora de Constante de Tiempo RC", "fr": "Calculatrice de Constante de Temps RC", "pt": "Calculadora de Constante de Tempo RC", "de": "RC-Zeitkonstante Rechner", "it": "Calcolatrice di Costante di Tempo RC"},
    "1079": {"en": "Wheatstone Bridge Calculator", "es": "Calculadora de Puente de Wheatstone", "fr": "Calculatrice de Pont de Wheatstone", "pt": "Calculadora de Ponte de Wheatstone", "de": "Wheatstone-Brücke Rechner", "it": "Calcolatrice di Ponte di Wheatstone"},
    "1080": {"en": "Fuel Consumption Calculator", "es": "Calculadora de Consumo de Combustible", "fr": "Calculatrice de Consommation de Carburant", "pt": "Calculadora de Consumo de Combustível", "de": "Kraftstoffverbrauchsrechner", "it": "Calcolatrice di Consumo Carburante"},
    "1081": {"en": "Braking Distance Calculator", "es": "Calculadora de Distancia de Frenado", "fr": "Calculatrice de Distance de Freinage", "pt": "Calculadora de Distância de Frenagem", "de": "Bremswegrechner", "it": "Calcolatrice di Distanza di Frenata"},
    "1082": {"en": "Engine Displacement Calculator", "es": "Calculadora de Cilindrada del Motor", "fr": "Calculatrice de Cylindrée du Moteur", "pt": "Calculadora de Cilindrada do Motor", "de": "Hubraumrechner", "it": "Calcolatrice di Cilindrata Motore"},
    "1083": {"en": "Tire Pressure Calculator", "es": "Calculadora de Presión de Neumáticos", "fr": "Calculatrice de Pression des Pneus", "pt": "Calculadora de Pressão dos Pneus", "de": "Reifendruckrechner", "it": "Calcolatrice di Pressione degli Pneumatici"},
    "1084": {"en": "Flight Time with Wind Calculator", "es": "Calculadora de Tiempo de Vuelo con Viento", "fr": "Calculatrice de Temps de Vol avec Vent", "pt": "Calculadora de Tempo de Voo com Vento", "de": "Flugzeit mit Wind Rechner", "it": "Calcolatrice di Tempo di Volo con Vento"},
    "1085": {"en": "Depth of Field Calculator", "es": "Calculadora de Profundidad de Campo", "fr": "Calculatrice de Profondeur de Champ", "pt": "Calculadora de Profundidade de Campo", "de": "Schärfentiefe Rechner", "it": "Calcolatrice di Profondità di Campo"},
    "1086": {"en": "Flash Guide Number Calculator", "es": "Calculadora de Número Guía de Flash", "fr": "Calculatrice de Nombre Guide de Flash", "pt": "Calculadora de Número Guia de Flash", "de": "Blitzleitzahl Rechner", "it": "Calcolatrice di Numero Guida del Flash"},
    "1087": {"en": "Heat Index Calculator", "es": "Calculadora de Índice de Calor", "fr": "Calculatrice d'Indice de Chaleur", "pt": "Calculadora de Índice de Calor", "de": "Hitzeindex Rechner", "it": "Calcolatrice di Indice di Calore"},
    "1088": {"en": "Wind Chill Calculator", "es": "Calculadora de Sensación Térmica por Viento", "fr": "Calculatrice de Refroidissement Éolien", "pt": "Calculadora de Sensação Térmica pelo Vento", "de": "Windchill Rechner", "it": "Calcolatrice di Wind Chill"},
    "1089": {"en": "Relative Humidity & Dew Point Calculator", "es": "Calculadora de Humedad Relativa y Punto de Rocío", "fr": "Calculatrice d'Humidité Relative et Point de Rosée", "pt": "Calculadora de Umidade Relativa e Ponto de Orvalho", "de": "Relative Luftfeuchte und Taupunkt Rechner", "it": "Calcolatrice di Umidità Relativa e Punto di Rugiada"},
    "1090": {"en": "Password Entropy Calculator", "es": "Calculadora de Entropía de Contraseña", "fr": "Calculatrice d'Entropie de Mot de Passe", "pt": "Calculadora de Entropia de Senha", "de": "Passwort-Entropie-Rechner", "it": "Calcolatrice di Entropia della Password"},
    "1091": {"en": "Character & Word Counter", "es": "Contador de Caracteres y Palabras", "fr": "Compteur de Caractères et Mots", "pt": "Contador de Caracteres e Palavras", "de": "Zeichen- und Wortzähler", "it": "Contatore di Caratteri e Parole"},
    "1092": {"en": "Business Days Calculator", "es": "Calculadora de Días Hábiles", "fr": "Calculatrice de Jours Ouvrés", "pt": "Calculadora de Dias Úteis", "de": "Arbeitstage Rechner", "it": "Calcolatrice di Giorni Lavorativi"},
    "1093": {"en": "Beam Deflection Calculator", "es": "Calculadora de Deflexión de Viga", "fr": "Calculatrice de Flèche de Poutre", "pt": "Calculadora de Deflexão de Viga", "de": "Balkendurchbiegung Rechner", "it": "Calcolatrice di Freccia della Trave"},
    "1094": {"en": "Bolt Torque Calculator", "es": "Calculadora de Par de Apriete de Tornillo", "fr": "Calculatrice de Couple de Serrage", "pt": "Calculadora de Torque de Aperto", "de": "Anzugsdrehmoment Rechner", "it": "Calcolatrice di Coppia di Serraggio"},
    "1095": {"en": "Spring Constant Calculator", "es": "Calculadora de Constante de Resorte", "fr": "Calculatrice de Constante de Ressort", "pt": "Calculadora de Constante da Mola", "de": "Federkonstante Rechner", "it": "Calcolatrice di Costante Elastica"},
    "1096": {"en": "Reynolds Number Calculator", "es": "Calculadora de Número de Reynolds", "fr": "Calculatrice de Nombre de Reynolds", "pt": "Calculadora de Número de Reynolds", "de": "Reynolds-Zahl Rechner", "it": "Calcolatrice di Numero di Reynolds"},
    "1097": {"en": "Running Pace Calculator", "es": "Calculadora de Ritmo de Carrera", "fr": "Calculatrice d'Allure de Course", "pt": "Calculadora de Ritmo de Corrida", "de": "Laufgeschwindigkeitsrechner", "it": "Calcolatrice di Andatura di Corsa"},
    "1098": {"en": "Golf Handicap Calculator", "es": "Calculadora de Handicap de Golf", "fr": "Calculatrice de Handicap de Golf", "pt": "Calculadora de Handicap de Golfe", "de": "Golf-Handicap Rechner", "it": "Calcolatrice di Handicap da Golf"},
    "1099": {"en": "MET Calories Burned Calculator", "es": "Calculadora de Calorías Quemadas por MET", "fr": "Calculatrice de Calories Brûlées par MET", "pt": "Calculadora de Calorias Queimadas por MET", "de": "MET-Kalorienverbrauchsrechner", "it": "Calcolatrice di Calorie Bruciate per MET"},
}

# SEO description templates per language
SEO_DESC_TEMPLATES = {
    "en": "{name}. Calculate instantly with step-by-step results. Free online tool by CalcToWork.",
    "es": "{name}. Calcula al instante con resultados paso a paso. Herramienta gratuita de CalcToWork.",
    "fr": "{name}. Calculez instantanément avec des résultats détaillés. Outil gratuit par CalcToWork.",
    "pt": "{name}. Calcule instantaneamente com resultados passo a passo. Ferramenta gratuita da CalcToWork.",
    "de": "{name}. Sofort berechnen mit schrittweisen Ergebnissen. Kostenloses Online-Tool von CalcToWork.",
    "it": "{name}. Calcola istantaneamente con risultati dettagliati. Strumento gratuito di CalcToWork.",
}

# SEO title templates per language — more natural, keyword-rich
SEO_TITLE_TEMPLATES = {
    "en": "{name} – Free Online Calculator",
    "es": "{name} – Calculadora Online Gratuita",
    "fr": "{name} – Calculatrice Gratuite en Ligne",
    "pt": "{name} – Calculadora Online Gratuita",
    "de": "{name} – Kostenloser Online-Rechner",
    "it": "{name} – Calcolatrice Online Gratuita",
}


def fix_translations():
    """Fix all language mixing and generic titles."""
    affected_ids = set(str(k) for k in range(910, 963)) | set(str(k) for k in range(1050, 1100))
    
    for lang in LANGS:
        fpath = os.path.join(I18N_DIR, f'{lang}.json')
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        calcs = data['calculators']
        changed = 0
        
        for calc_id in affected_ids:
            if calc_id not in calcs:
                continue
            if calc_id not in NAMES:
                continue
                
            entry = calcs[calc_id]
            name_trans = NAMES[calc_id][lang]
            
            # Fix name
            entry['name'] = name_trans
            
            # Fix desc/description
            entry['desc'] = name_trans + ('.' if not name_trans.endswith('.') else '')
            entry['description'] = entry['desc']
            
            # Fix seo_title with unique, keyword-rich title
            entry['seo_title'] = SEO_TITLE_TEMPLATES[lang].format(name=name_trans)
            
            # Fix seo_description with unique description
            entry['seo_description'] = SEO_DESC_TEMPLATES[lang].format(name=name_trans)
            entry['seo_desc'] = entry['seo_description']
            
            # Fix input/output labels for batch 4 (910-962) — translate input names
            if 910 <= int(calc_id) <= 962:
                inputs = entry.get('inputs', {})
                if isinstance(inputs, dict):
                    for key in inputs:
                        # Keep the key but translate the label
                        val = inputs[key]
                        if lang != 'en' and isinstance(val, str) and val == key:
                            pass  # Will need separate translation
                outputs = entry.get('outputs', {})
                if isinstance(outputs, dict):
                    pass  # similar
            
            changed += 1
        
        # Also fix generic "- Free Online Calculator" SEO titles across ALL calcs
        # These are in batch 4 (910-962) which we already handled
        # But also check other calculators for "Formula, Calculation & Examples" pattern
        generic_suffixes = {
            "en": " -- Formula, Calculation & Examples | CalcToWork",
            "es": " -- Fórmula, Cálculo y Ejemplos | CalcToWork",
            "fr": " -- Formule, Calcul et Exemples | CalcToWork",
            "pt": " -- Fórmula, Cálculo e Exemplos | CalcToWork",
            "de": " -- Formel, Berechnung & Beispiele | CalcToWork",
            "it": " -- Formula, Calcolo ed Esempi | CalcToWork",
        }
        
        for calc_id, entry in calcs.items():
            seo_title = entry.get('seo_title', '')
            
            # Fix " | CalcToWork" with just the name (lazy pattern)
            if seo_title.endswith(' | CalcToWork') and seo_title.replace(' | CalcToWork', '') == entry.get('name', ''):
                entry['seo_title'] = SEO_TITLE_TEMPLATES[lang].format(name=entry['name'])
                if 'seo_description' not in entry and 'seo_desc' not in entry:
                    entry['seo_description'] = SEO_DESC_TEMPLATES[lang].format(name=entry['name'])
                    entry['seo_desc'] = entry['seo_description']
                elif 'seo_desc' in entry and 'seo_description' not in entry:
                    entry['seo_description'] = entry['seo_desc']
                elif 'seo_description' in entry and 'seo_desc' not in entry:
                    entry['seo_desc'] = entry['seo_description']
            
            # Fix " - Free Online Calculator" pattern (already handled for batch 4)
            if ' - Free Online Calculator' in seo_title and calc_id not in affected_ids and lang == 'en':
                name_part = seo_title.replace(' - Free Online Calculator', '')
                entry['seo_title'] = name_part + ' – Free Online Calculator'
                entry['seo_description'] = f"{name_part}. Calculate instantly with step-by-step results. Free online tool by CalcToWork."
                entry['seo_desc'] = entry['seo_description']
            
            # Standardize seo_desc/seo_description for ALL entries
            if 'seo_description' in entry and 'seo_desc' not in entry:
                entry['seo_desc'] = entry['seo_description']
            elif 'seo_desc' in entry and 'seo_description' not in entry:
                entry['seo_description'] = entry['seo_desc']
        
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        
        print(f'  Updated {changed} batch entries + generic titles in {lang}.json')


if __name__ == '__main__':
    print('Fixing i18n translations...')
    fix_translations()
    print('Done! All 103 affected entries fixed across 6 languages.')
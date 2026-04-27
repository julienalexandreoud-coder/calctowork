"""
Translate input/output labels for batch 4 (910-962) and batch 5 (1050-1099)
across all 6 languages (EN, ES, FR, PT, DE, IT).
"""

import json
import os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

# Translation dictionaries keyed by field_id, then by language
# For batch 4 (910-962)
INPUT_LABELS = {
    "numerador": {"en": "Numerator", "es": "Numerador", "fr": "Numérateur", "pt": "Numerador", "de": "Zähler", "it": "Numeratore"},
    "denominador": {"en": "Denominator", "es": "Denominador", "fr": "Dénominateur", "pt": "Denominador", "de": "Nenner", "it": "Denominatore"},
    "x1": {"en": "X₁", "es": "X₁", "fr": "X₁", "pt": "X₁", "de": "X₁", "it": "X₁"},
    "y1": {"en": "Y₁", "es": "Y₁", "fr": "Y₁", "pt": "Y₁", "de": "Y₁", "it": "Y₁"},
    "x2": {"en": "X₂", "es": "X₂", "fr": "X₂", "pt": "X₂", "de": "X₂", "it": "X₂"},
    "y2": {"en": "Y₂", "es": "Y₂", "fr": "Y₂", "pt": "Y₂", "de": "Y₂", "it": "Y₂"},
    "numero": {"en": "Number", "es": "Número", "fr": "Nombre", "pt": "Número", "de": "Zahl", "it": "Numero"},
    "coeficiente": {"en": "Coefficient", "es": "Coeficiente", "fr": "Coefficient", "pt": "Coeficiente", "de": "Koeffizient", "it": "Coefficiente"},
    "exponente": {"en": "Exponent", "es": "Exponente", "fr": "Exposant", "pt": "Expoente", "de": "Exponent", "it": "Esponente"},
    "decimal_places": {"en": "Decimal places", "es": "Decimales", "fr": "Décimales", "pt": "Casas decimais", "de": "Dezimalstellen", "it": "Decimali"},
    "numero_a": {"en": "Number A", "es": "Número A", "fr": "Nombre A", "pt": "Número A", "de": "Zahl A", "it": "Numero A"},
    "numero_b": {"en": "Number B", "es": "Número B", "fr": "Nombre B", "pt": "Número B", "de": "Zahl B", "it": "Numero B"},
    "radio": {"en": "Radius", "es": "Radio", "fr": "Rayon", "pt": "Raio", "de": "Radius", "it": "Raggio"},
    "altura": {"en": "Height", "es": "Altura", "fr": "Hauteur", "pt": "Altura", "de": "Höhe", "it": "Altezza"},
    "lado": {"en": "Side", "es": "Lado", "fr": "Côté", "pt": "Lado", "de": "Seite", "it": "Lato"},
    "largo": {"en": "Length", "es": "Largo", "fr": "Longueur", "pt": "Comprimento", "de": "Länge", "it": "Lunghezza"},
    "ancho": {"en": "Width", "es": "Ancho", "fr": "Largeur", "pt": "Largura", "de": "Breite", "it": "Larghezza"},
    "base_mayor": {"en": "Major base", "es": "Base mayor", "fr": "Grande base", "pt": "Base maior", "de": "Obere Basis", "it": "Base maggiore"},
    "base_menor": {"en": "Minor base", "es": "Base menor", "fr": "Petite base", "pt": "Base menor", "de": "Untere Basis", "it": "Base minore"},
    "generatriz": {"en": "Slant height", "es": "Generatriz", "fr": "Apothème", "pt": "Geratriz", "de": "Seitenlinie", "it": "Apotema"},
    "peso": {"en": "Weight", "es": "Peso", "fr": "Poids", "pt": "Peso", "de": "Gewicht", "it": "Peso"},
    "peso_kg": {"en": "Weight (kg)", "es": "Peso (kg)", "fr": "Poids (kg)", "pt": "Peso (kg)", "de": "Gewicht (kg)", "it": "Peso (kg)"},
    "altura_cm": {"en": "Height (cm)", "es": "Altura (cm)", "fr": "Taille (cm)", "pt": "Altura (cm)", "de": "Größe (cm)", "it": "Altezza (cm)"},
    "edad": {"en": "Age", "es": "Edad", "fr": "Âge", "pt": "Idade", "de": "Alter", "it": "Età"},
    "sexo": {"en": "Sex", "es": "Sexo", "fr": "Sexe", "pt": "Sexo", "de": "Geschlecht", "it": "Sesso"},
    "grasa_pct": {"en": "Body fat %", "es": "Grasa corporal %", "fr": "Graisse corporelle %", "pt": "Gordura corporal %", "de": "Körperfett %", "it": "Grasso corporeo %"},
    "calorias_objetivo": {"en": "Target calories", "es": "Calorías objetivo", "fr": "Calories cibles", "pt": "Calorias alvo", "de": "Zielkalorien", "it": "Calorie obiettivo"},
    "sistolica": {"en": "Systolic", "es": "Sistólica", "fr": "Systolique", "pt": "Sistólica", "de": "Systolisch", "it": "Sistolica"},
    "diastolica": {"en": "Diastolic", "es": "Diastólica", "fr": "Diastolique", "pt": "Diastólica", "de": "Diastolisch", "it": "Diastolica"},
    "cintura": {"en": "Waist", "es": "Cintura", "fr": "Taille", "pt": "Cintura", "de": "Taillenumfang", "it": "Vita"},
    "cadera": {"en": "Hip", "es": "Cadera", "fr": "Hanche", "pt": "Quadril", "de": "Hüftumfang", "it": "Fianchi"},
    "peso_inicial": {"en": "Initial weight", "es": "Peso inicial", "fr": "Poids initial", "pt": "Peso inicial", "de": "Anfangsgewicht", "it": "Peso iniziale"},
    "peso_final": {"en": "Final weight", "es": "Peso final", "fr": "Poids final", "pt": "Peso final", "de": "Endgewicht", "it": "Peso finale"},
    "fcm": {"en": "Max heart rate", "es": "FCM", "fr": "FCM", "pt": "FCM", "de": "Maximale Herzfrequenz", "it": "FCM"},
    "salario_anual": {"en": "Annual salary", "es": "Salario anual", "fr": "Salaire annuel", "pt": "Salário anual", "de": "Jahresgehalt", "it": "Salario annuale"},
    "horas_semana": {"en": "Hours per week", "es": "Horas por semana", "fr": "Heures par semaine", "pt": "Horas por semana", "de": "Stunden pro Woche", "it": "Ore a settimana"},
    "semanas_ano": {"en": "Weeks per year", "es": "Semanas al año", "fr": "Semaines par an", "pt": "Semanas por ano", "de": "Wochen pro Jahr", "it": "Settimane all'anno"},
    "salario_hora": {"en": "Hourly rate", "es": "Salario por hora", "fr": "Taux horaire", "pt": "Salário por hora", "de": "Stundenlohn", "it": "Tariffa oraria"},
    "precio_casa": {"en": "Home price", "es": "Precio de la casa", "fr": "Prix de la maison", "pt": "Preço da casa", "de": "Hauspreis", "it": "Prezzo della casa"},
    "entrada_pct": {"en": "Down payment %", "es": "Entrada %", "fr": "Apport %", "pt": "Entrada %", "de": "Anzahlung %", "it": "Acconto %"},
    "tasa_anual": {"en": "Annual rate %", "es": "Tasa anual %", "fr": "Taux annuel %", "pt": "Taxa anual %", "de": "Jahreszins %", "it": "Tasso annuale %"},
    "anos": {"en": "Years", "es": "Años", "fr": "Années", "pt": "Anos", "de": "Jahre", "it": "Anni"},
    "deuda": {"en": "Debt amount", "es": "Monto de deuda", "fr": "Montant de la dette", "pt": "Valor da dívida", "de": "Schuldenbetrag", "it": "Importo del debito"},
    "tasa_interes": {"en": "Interest rate %", "es": "Tasa de interés %", "fr": "Taux d'intérêt %", "pt": "Taxa de juros %", "de": "Zinssatz %", "it": "Tasso di interesse %"},
    "pago_mensual": {"en": "Monthly payment", "es": "Pago mensual", "fr": "Mensualité", "pt": "Pagamento mensal", "de": "Monatliche Zahlung", "it": "Pagamento mensile"},
    "capital_inicial": {"en": "Initial capital", "es": "Capital inicial", "fr": "Capital initial", "pt": "Capital inicial", "de": "Startkapital", "it": "Capitale iniziale"},
    "aporte_mensual": {"en": "Monthly contribution", "es": "Aporte mensual", "fr": "Contribution mensuelle", "pt": "Aporte mensal", "de": "Monatlicher Beitrag", "it": "Contributo mensile"},
    "costo": {"en": "Cost", "es": "Costo", "fr": "Coût", "pt": "Custo", "de": "Kosten", "it": "Costo"},
    "precio_venta": {"en": "Sale price", "es": "Precio de venta", "fr": "Prix de vente", "pt": "Preço de venda", "de": "Verkaufspreis", "it": "Prezzo di vendita"},
    "tasa_descuento": {"en": "Discount rate %", "es": "Tasa de descuento %", "fr": "Taux d'actualisation %", "pt": "Taxa de desconto %", "de": "Diskontierungszins %", "it": "Tasso di sconto %"},
    "flujo_caja": {"en": "Cash flows (comma-separated)", "es": "Flujos de caja (separados por coma)", "fr": "Flux de trésorerie (séparés par virgule)", "pt": "Fluxos de caixa (separados por vírgula)", "de": "Zahlungsströme (kommagetrennt)", "it": "Flussi di cassa (separati da virgola)"},
    "gastos_mensuales": {"en": "Monthly expenses", "es": "Gastos mensuales", "fr": "Dépenses mensuelles", "pt": "Despesas mensais", "de": "Monatliche Ausgaben", "it": "Spese mensili"},
    "meses_fondo": {"en": "Months of coverage", "es": "Meses de cobertura", "fr": "Mois de couverture", "pt": "Meses de cobertura", "de": "Monate Deckung", "it": "Mesi di copertura"},
    "fecha_nacimiento": {"en": "Date of birth", "es": "Fecha de nacimiento", "fr": "Date de naissance", "pt": "Data de nascimento", "de": "Geburtsdatum", "it": "Data di nascita"},
    "fecha_inicio": {"en": "Start date", "es": "Fecha inicio", "fr": "Date de début", "pt": "Data inicial", "de": "Startdatum", "it": "Data iniziale"},
    "fecha_fin": {"en": "End date", "es": "Fecha fin", "fr": "Date de fin", "pt": "Data final", "de": "Enddatum", "it": "Data finale"},
    "cuenta": {"en": "Bill amount", "es": "Monto de la cuenta", "fr": "Montant de l'addition", "pt": "Valor da conta", "de": "Rechnungsbetrag", "it": "Totale del conto"},
    "porcentaje_propina": {"en": "Tip percentage %", "es": "Porcentaje de propina %", "fr": "Pourcentage de pourboire %", "pt": "Porcentagem de gorjeta %", "de": "Trinkgeldprozent %", "it": "Percentuale mancia %"},
    "personas": {"en": "Split between", "es": "Dividir entre", "fr": "Partager entre", "pt": "Dividir entre", "de": "Aufteilen auf", "it": "Dividere tra"},
    "descuento1": {"en": "First discount %", "es": "Primer descuento %", "fr": "Première remise %", "pt": "Primeiro desconto %", "de": "Erster Rabatt %", "it": "Primo sconto %"},
    "descuento2": {"en": "Second discount %", "es": "Segundo descuento %", "fr": "Deuxième remise %", "pt": "Segundo desconto %", "de": "Zweiter Rabatt %", "it": "Secondo sconto %"},
    "masa": {"en": "Mass (kg)", "es": "Masa (kg)", "fr": "Masse (kg)", "pt": "Massa (kg)", "de": "Masse (kg)", "it": "Massa (kg)"},
    "velocidad": {"en": "Velocity (m/s)", "es": "Velocidad (m/s)", "fr": "Vitesse (m/s)", "pt": "Velocidade (m/s)", "de": "Geschwindigkeit (m/s)", "it": "Velocità (m/s)"},
    "aceleracion": {"en": "Acceleration (m/s²)", "es": "Aceleración (m/s²)", "fr": "Accélération (m/s²)", "pt": "Aceleração (m/s²)", "de": "Beschleunigung (m/s²)", "it": "Accelerazione (m/s²)"},
    "tiempo": {"en": "Time (s)", "es": "Tiempo (s)", "fr": "Temps (s)", "pt": "Tempo (s)", "de": "Zeit (s)", "it": "Tempo (s)"},
    "voltaje": {"en": "Voltage (V)", "es": "Voltaje (V)", "fr": "Tension (V)", "pt": "Voltagem (V)", "de": "Spannung (V)", "it": "Voltaggio (V)"},
    "corriente": {"en": "Current (A)", "es": "Corriente (A)", "fr": "Courant (A)", "pt": "Corrente (A)", "de": "Stromstärke (A)", "it": "Corrente (A)"},
    "resistencia": {"en": "Resistance (Ω)", "es": "Resistencia (Ω)", "fr": "Résistance (Ω)", "pt": "Resistência (Ω)", "de": "Widerstand (Ω)", "it": "Resistenza (Ω)"},
    "fuerza": {"en": "Force (N)", "es": "Fuerza (N)", "fr": "Force (N)", "pt": "Força (N)", "de": "Kraft (N)", "it": "Forza (N)"},
    "repeticiones": {"en": "Repetitions", "es": "Repeticiones", "fr": "Répétitions", "pt": "Repetições", "de": "Wiederholungen", "it": "Ripetizioni"},
    "peso_levantado": {"en": "Weight lifted", "es": "Peso levantado", "fr": "Poids soulevé", "pt": "Peso levantado", "de": "Gehobenes Gewicht", "it": "Peso sollevato"},
    "distancia_km": {"en": "Distance (km)", "es": "Distancia (km)", "fr": "Distance (km)", "pt": "Distância (km)", "de": "Distanz (km)", "it": "Distanza (km)"},
    "tiempo_minutos": {"en": "Time (min)", "es": "Tiempo (min)", "fr": "Temps (min)", "pt": "Tempo (min)", "de": "Zeit (min)", "it": "Tempo (min)"},
    "vo2ml": {"en": "VO₂ (ml/kg/min)", "es": "VO₂ (ml/kg/min)", "fr": "VO₂ (ml/kg/min)", "pt": "VO₂ (ml/kg/min)", "de": "VO₂ (ml/kg/min)", "it": "VO₂ (ml/kg/min)"},
    "grados": {"en": "Degrees", "es": "Grados", "fr": "Degrés", "pt": "Graus", "de": "Grad", "it": "Gradi"},
    "celsius": {"en": "Temperature (°C)", "es": "Temperatura (°C)", "fr": "Température (°C)", "pt": "Temperatura (°C)", "de": "Temperatur (°C)", "it": "Temperatura (°C)"},
    "julios": {"en": "Energy (J)", "es": "Energía (J)", "fr": "Énergie (J)", "pt": "Energia (J)", "de": "Energie (J)", "it": "Energia (J)"},
    "n_elementos": {"en": "Total elements (n)", "es": "Total de elementos (n)", "fr": "Total des éléments (n)", "pt": "Total de elementos (n)", "de": "Gesamtzahl der Elemente (n)", "it": "Elementi totali (n)"},
    "k_seleccion": {"en": "Selection (k)", "es": "Selección (k)", "fr": "Sélection (k)", "pt": "Seleção (k)", "de": "Auswahl (k)", "it": "Selezione (k)"},
    "puntuacion_z": {"en": "Z-score", "es": "Puntuación Z", "fr": "Score Z", "pt": "Escore Z", "de": "Z-Score", "it": "Z-Score"},
    "media": {"en": "Mean", "es": "Media", "fr": "Moyenne", "pt": "Média", "de": "Mittelwert", "it": "Media"},
    "desviacion": {"en": "Std deviation", "es": "Desviación estándar", "fr": "Écart type", "pt": "Desvio padrão", "de": "Standardabweichung", "it": "Deviazione standard"},
    "poblacion": {"en": "Population", "es": "Población", "fr": "Population", "pt": "População", "de": "Population", "it": "Popolazione"},
    "margen_error": {"en": "Margin of error %", "es": "Margen de error %", "fr": "Marge d'erreur %", "pt": "Margem de erro %", "de": "Fehlermarge %", "it": "Margine di errore %"},
    "nivel_confianza": {"en": "Confidence level %", "es": "Nivel de confianza %", "fr": "Niveau de confiance %", "pt": "Nível de confiança %", "de": "Konfidenzniveau %", "it": "Livello di confidenza %"},
    "glucosa_ayunas": {"en": "Fasting glucose (mg/dL)", "es": "Glucosa en ayunas (mg/dL)", "fr": "Glycémie à jeun (mg/dL)", "pt": "Glicose em jejum (mg/dL)", "de": "Nüchternglukose (mg/dL)", "it": "Glucosio a digiuno (mg/dL)"},
    "colesterol_total": {"en": "Total cholesterol (mg/dL)", "es": "Colesterol total (mg/dL)", "fr": "Cholestérol total (mg/dL)", "pt": "Colesterol total (mg/dL)", "de": "Gesamtcholesterin (mg/dL)", "it": "Colesterolo totale (mg/dL)"},
    "colesterol_hdl": {"en": "HDL cholesterol (mg/dL)", "es": "Colesterol HDL (mg/dL)", "fr": "Cholestérol HDL (mg/dL)", "pt": "Colesterol HDL (mg/dL)", "de": "HDL-Cholesterin (mg/dL)", "it": "Colesterolo HDL (mg/dL)"},
    "trigliceridos": {"en": "Triglycerides (mg/dL)", "es": "Triglicéridos (mg/dL)", "fr": "Triglycérides (mg/dL)", "pt": "Triglicerídeos (mg/dL)", "de": "Triglyceride (mg/dL)", "it": "Trigliceridi (mg/dL)"},
    "n": {"en": "Number of sides", "es": "Número de lados", "fr": "Nombre de côtés", "pt": "Número de lados", "de": "Seitenanzahl", "it": "Numero di lati"},
    "primer_termino": {"en": "First term", "es": "Primer término", "fr": "Premier terme", "pt": "Primeiro termo", "de": "Erstes Glied", "it": "Primo termine"},
    "razon": {"en": "Common ratio/difference", "es": "Razón común", "fr": "Raison commune", "pt": "Razão comum", "de": "Gemeinsame Ratio", "it": "Ragione comune"},
    "numero_terminos": {"en": "Number of terms", "es": "Número de términos", "fr": "Nombre de termes", "pt": "Número de termos", "de": "Anzahl der Glieder", "it": "Numero di termini"},
    "densidad_fluido": {"en": "Fluid density (kg/m³)", "es": "Densidad del fluido (kg/m³)", "fr": "Densité du fluide (kg/m³)", "pt": "Densidade do fluido (kg/m³)", "de": "Fluiddichte (kg/m³)", "it": "Densità del fluido (kg/m³)"},
    "volumen": {"en": "Volume (m³)", "es": "Volumen (m³)", "fr": "Volume (m³)", "pt": "Volume (m³)", "de": "Volumen (m³)", "it": "Volume (m³)"},
    "frecuencia": {"en": "Frequency (Hz)", "es": "Frecuencia (Hz)", "fr": "Fréquence (Hz)", "pt": "Frequência (Hz)", "de": "Frequenz (Hz)", "it": "Frequenza (Hz)"},
    "frecuencia_fuente": {"en": "Source frequency (Hz)", "es": "Frecuencia de la fuente (Hz)", "fr": "Fréquence source (Hz)", "pt": "Frequência da fonte (Hz)", "de": "Quellfrequenz (Hz)", "it": "Frequenza della sorgente (Hz)"},
    "velocidad_observador": {"en": "Observer velocity (m/s)", "es": "Velocidad del observador (m/s)", "fr": "Vitesse de l'observateur (m/s)", "pt": "Velocidade do observador (m/s)", "de": "Beobachtergeschwindigkeit (m/s)", "it": "Velocità dell'osservatore (m/s)"},
    "formula_quimica": {"en": "Chemical formula", "es": "Fórmula química", "fr": "Formule chimique", "pt": "Fórmula química", "de": "Chemische Formel", "it": "Formula chimica"},
    "presion": {"en": "Pressure (Pa)", "es": "Presión (Pa)", "fr": "Pression (Pa)", "pt": "Pressão (Pa)", "de": "Druck (Pa)", "it": "Pressione (Pa)"},
    "temperatura": {"en": "Temperature", "es": "Temperatura", "fr": "Température", "pt": "Temperatura", "de": "Temperatur", "it": "Temperatura"},
    "moles": {"en": "Moles (mol)", "es": "Moles (mol)", "fr": "Moles (mol)", "pt": "Moles (mol)", "de": "Mol (mol)", "it": "Moli (mol)"},
    "concentracion": {"en": "Concentration (mol/L)", "es": "Concentración (mol/L)", "fr": "Concentration (mol/L)", "pt": "Concentração (mol/L)", "de": "Konzentration (mol/L)", "it": "Concentrazione (mol/L)"},
    "volumen_solucion": {"en": "Solution volume (L)", "es": "Volumen de solución (L)", "fr": "Volume de solution (L)", "pt": "Volume da solução (L)", "de": "Lösungsvolumen (L)", "it": "Volume della soluzione (L)"},
    "resistencia1": {"en": "Resistance 1 (Ω)", "es": "Resistencia 1 (Ω)", "fr": "Résistance 1 (Ω)", "pt": "Resistência 1 (Ω)", "de": "Widerstand 1 (Ω)", "it": "Resistenza 1 (Ω)"},
    "resistencia2": {"en": "Resistance 2 (Ω)", "es": "Resistencia 2 (Ω)", "fr": "Résistance 2 (Ω)", "pt": "Resistência 2 (Ω)", "de": "Widerstand 2 (Ω)", "it": "Resistenza 2 (Ω)"},
    "resistencia3": {"en": "Resistance 3 (Ω)", "es": "Resistencia 3 (Ω)", "fr": "Résistance 3 (Ω)", "pt": "Resistência 3 (Ω)", "de": "Widerstand 3 (Ω)", "it": "Resistenza 3 (Ω)"},
    "capacitancia": {"en": "Capacitance (F)", "es": "Capacitancia (F)", "fr": "Capacité (F)", "pt": "Capacitância (F)", "de": "Kapazität (F)", "it": "Capacitanza (F)"},
    "voltaje1": {"en": "Voltage 1 (V)", "es": "Voltaje 1 (V)", "fr": "Tension 1 (V)", "pt": "Voltagem 1 (V)", "de": "Spannung 1 (V)", "it": "Voltaggio 1 (V)"},
    "voltaje2": {"en": "Voltage 2 (V)", "es": "Voltaje 2 (V)", "fr": "Tension 2 (V)", "pt": "Voltagem 2 (V)", "de": "Spannung 2 (V)", "it": "Voltaggio 2 (V)"},
    "litros_100km": {"en": "Fuel consumption (L/100km)", "es": "Consumo (L/100km)", "fr": "Consommation (L/100km)", "pt": "Consumo (L/100km)", "de": "Verbrauch (L/100km)", "it": "Consumo (L/100km)"},
    "velocidad_inicial": {"en": "Initial speed (km/h)", "es": "Velocidad inicial (km/h)", "fr": "Vitesse initiale (km/h)", "pt": "Velocidade inicial (km/h)", "de": "Anfangsgeschwindigkeit (km/h)", "it": "Velocità iniziale (km/h)"},
    "cilindros": {"en": "Cylinders", "es": "Cilindros", "fr": "Cylindres", "pt": "Cilindros", "de": "Zylinder", "it": "Cilindri"},
    "diametro": {"en": "Diameter", "es": "Diámetro", "fr": "Diamètre", "pt": "Diâmetro", "de": "Durchmesser", "it": "Diametro"},
    "carrera": {"en": "Stroke (mm)", "es": "Carrera (mm)", "fr": "Course (mm)", "pt": "Curso (mm)", "de": "Hub (mm)", "it": "Corsa (mm)"},
    "presion_recomendada": {"en": "Recommended pressure", "es": "Presión recomendada", "fr": "Pression recommandée", "pt": "Pressão recomendada", "de": "Empfohlener Druck", "it": "Pressione raccomandata"},
    "distancia_km_h": {"en": "Distance (km)", "es": "Distancia (km)", "fr": "Distance (km)", "pt": "Distância (km)", "de": "Distanz (km)", "it": "Distanza (km)"},
    "velocidad_viento": {"en": "Wind speed (km/h)", "es": "Velocidad del viento (km/h)", "fr": "Vitesse du vent (km/h)", "pt": "Velocidade do vento (km/h)", "de": "Windgeschwindigkeit (km/h)", "it": "Velocità del vento (km/h)"},
    "apertura": {"en": "Aperture (f/)", "es": "Apertura (f/)", "fr": "Ouverture (f/)", "pt": "Abertura (f/)", "de": "Blendenzahl (f/)", "it": "Apertura (f/)"},
    "distancia_enfoque": {"en": "Focus distance (m)", "es": "Distancia de enfoque (m)", "fr": "Distance de mise au point (m)", "pt": "Distância de foco (m)", "de": "Fokussierdistanz (m)", "it": "Distanza di messa a fuoco (m)"},
    "longitud_focal": {"en": "Focal length (mm)", "es": "Longitud focal (mm)", "fr": "Longueur focale (mm)", "pt": "Comprimento focal (mm)", "de": "Brennweite (mm)", "it": "Lunghezza focale (mm)"},
    "numero_guia": {"en": "Guide number", "es": "Número guía", "fr": "Nombre guide", "pt": "Número guia", "de": "Leitzahl", "it": "Numero guida"},
    "iso": {"en": "ISO", "es": "ISO", "fr": "ISO", "pt": "ISO", "de": "ISO", "it": "ISO"},
    "humedad": {"en": "Humidity %", "es": "Humedad %", "fr": "Humidité %", "pt": "Umidade %", "de": "Luftfeuchtigkeit %", "it": "Umidità %"},
    "longitud": {"en": "Length", "es": "Longitud", "fr": "Longueur", "pt": "Comprimento", "de": "Länge", "it": "Lunghezza"},
    "conjunto_caracteres": {"en": "Character set size", "es": "Tamaño del conjunto de caracteres", "fr": "Taille du jeu de caractères", "pt": "Tamanho do conjunto de caracteres", "de": "Zeichensatzgröße", "it": "Dimensione del set di caratteri"},
    "texto": {"en": "Text", "es": "Texto", "fr": "Texte", "pt": "Texto", "de": "Text", "it": "Testo"},
    "carga": {"en": "Load (N)", "es": "Carga (N)", "fr": "Charge (N)", "pt": "Carga (N)", "de": "Last (N)", "it": "Carico (N)"},
    "longitud_viga": {"en": "Beam length (m)", "es": "Longitud de viga (m)", "fr": "Longueur de poutre (m)", "pt": "Comprimento da viga (m)", "de": "Balkenlänge (m)", "it": "Lunghezza trave (m)"},
    "modulo_elasticidad": {"en": "Elastic modulus (GPa)", "es": "Módulo de elasticidad (GPa)", "fr": "Module d'élasticité (GPa)", "pt": "Módulo de elasticidade (GPa)", "de": "Elastizitätsmodul (GPa)", "it": "Modulo di elasticità (GPa)"},
    "momento_inercia_seccion": {"en": "Moment of inertia (cm⁴)", "es": "Momento de inercia (cm⁴)", "fr": "Moment d'inertie (cm⁴)", "pt": "Momento de inércia (cm⁴)", "de": "Flächenträgheitsmoment (cm⁴)", "it": "Momento d'inerzia (cm⁴)"},
    "diametro_tornillo": {"en": "Bolt diameter (mm)", "es": "Diámetro del tornillo (mm)", "fr": "Diamètre du boulon (mm)", "pt": "Diâmetro do parafuso (mm)", "de": "Bolzendurchmesser (mm)", "it": "Diametro del bullone (mm)"},
    "fuerza_apriete": {"en": "Clamping force (N)", "es": "Fuerza de apriete (N)", "fr": "Force de serrage (N)", "pt": "Força de aperto (N)", "de": "Klemmkraft (N)", "it": "Forza di serraggio (N)"},
    "constante_resorte": {"en": "Spring constant (N/m)", "es": "Constante del resorte (N/m)", "fr": "Constante du ressort (N/m)", "pt": "Constante da mola (N/m)", "de": "Federkonstante (N/m)", "it": "Costante elastica (N/m)"},
    "deformacion": {"en": "Deformation (m)", "es": "Deformación (m)", "fr": "Déformation (m)", "pt": "Deformação (m)", "de": "Verformung (m)", "it": "Deformazione (m)"},
    "velocidad_fluido": {"en": "Fluid velocity (m/s)", "es": "Velocidad del fluido (m/s)", "fr": "Vitesse du fluide (m/s)", "pt": "Velocidade do fluido (m/s)", "de": "Fluidgeschwindigkeit (m/s)", "it": "Velocità del fluido (m/s)"},
    "diametro_tubo": {"en": "Pipe diameter (m)", "es": "Diámetro del tubo (m)", "fr": "Diamètre du tuyau (m)", "pt": "Diâmetro do tubo (m)", "de": "Rohrdurchmesser (m)", "it": "Diametro del tubo (m)"},
    "viscosidad": {"en": "Viscosity (Pa·s)", "es": "Viscosidad (Pa·s)", "fr": "Viscosité (Pa·s)", "pt": "Viscosidade (Pa·s)", "de": "Viskosität (Pa·s)", "it": "Viscosità (Pa·s)"},
    "distancia_m": {"en": "Distance (m)", "es": "Distancia (m)", "fr": "Distance (m)", "pt": "Distância (m)", "de": "Distanz (m)", "it": "Distanza (m)"},
    "tiempo_segundos": {"en": "Time (seconds)", "es": "Tiempo (segundos)", "fr": "Temps (secondes)", "pt": "Tempo (segundos)", "de": "Zeit (Sekunden)", "it": "Tempo (secondi)"},
    "par": {"en": "Course par", "es": "Par del campo", "fr": "Par du parcours", "pt": "Par do campo", "de": "Platz-Par", "it": "Par del campo"},
    "peso_corporal": {"en": "Body weight (kg)", "es": "Peso corporal (kg)", "fr": "Poids corporel (kg)", "pt": "Peso corporal (kg)", "de": "Körpergewicht (kg)", "it": "Peso corporeo (kg)"},
    "met_valor": {"en": "MET value", "es": "Valor MET", "fr": "Valeur MET", "pt": "Valor MET", "de": "MET-Wert", "it": "Valore MET"},
    "perimetro": {"en": "Perimeter", "es": "Perímetro", "fr": "Périmètre", "pt": "Perímetro", "de": "Umfang", "it": "Perimetro"},
    "area_superficial": {"en": "Surface area", "es": "Área superficial", "fr": "Aire surfacique", "pt": "Área superficial", "de": "Oberfläche", "it": "Area superficiale"},
}

OUTPUT_LABELS = {
    "decimal": {"en": "Decimal", "es": "Decimal", "fr": "Décimal", "pt": "Decimal", "de": "Dezimal", "it": "Decimale"},
    "whole_number": {"en": "Whole number", "es": "Número entero", "fr": "Nombre entier", "pt": "Número inteiro", "de": "Ganze Zahl", "it": "Numero intero"},
    "remainder": {"en": "Remainder", "es": "Residuo", "fr": "Reste", "pt": "Resto", "de": "Rest", "it": "Resto"},
    "percentage": {"en": "Percentage", "es": "Porcentaje", "fr": "Pourcentage", "pt": "Porcentagem", "de": "Prozent", "it": "Percentuale"},
    "slope": {"en": "Slope", "es": "Pendiente", "fr": "Pente", "pt": "Inclinação", "de": "Steigung", "it": "Pendenza"},
    "angle_deg": {"en": "Angle (°)", "es": "Ángulo (°)", "fr": "Angle (°)", "pt": "Ângulo (°)", "de": "Winkel (°)", "it": "Angolo (°)"},
    "distance": {"en": "Distance", "es": "Distancia", "fr": "Distance", "pt": "Distância", "de": "Distanz", "it": "Distanza"},
    "hourly": {"en": "Hourly", "es": "Por hora", "fr": "Horaire", "pt": "Por hora", "de": "Stündlich", "it": "Orario"},
    "monthly": {"en": "Monthly", "es": "Mensual", "fr": "Mensuel", "pt": "Mensal", "de": "Monatlich", "it": "Mensile"},
    "weekly": {"en": "Weekly", "es": "Semanal", "fr": "Hebdomadaire", "pt": "Semanal", "de": "Wöchentlich", "it": "Settimanale"},
    "daily": {"en": "Daily", "es": "Diario", "fr": "Journalier", "pt": "Diário", "de": "Täglich", "it": "Giornaliero"},
    "annual": {"en": "Annual", "es": "Anual", "fr": "Annuel", "pt": "Anual", "de": "Jährlich", "it": "Annuale"},
    "monthly_payment": {"en": "Monthly payment", "es": "Pago mensual", "fr": "Mensualité", "pt": "Pagamento mensal", "de": "Monatliche Zahlung", "it": "Pagamento mensile"},
    "loan_amount": {"en": "Loan amount", "es": "Monto del préstamo", "fr": "Montant du prêt", "pt": "Valor do empréstimo", "de": "Darlehensbetrag", "it": "Importo del prestito"},
    "total_paid": {"en": "Total paid", "es": "Total pagado", "fr": "Total payé", "pt": "Total pago", "de": "Gesamtzahlung", "it": "Totale pagato"},
    "total_interest": {"en": "Total interest", "es": "Total de intereses", "fr": "Total des intérêts", "pt": "Total de juros", "de": "Gesamtzinsen", "it": "Interessi totali"},
    "interest_ratio": {"en": "Interest ratio", "es": "Proporción de intereses", "fr": "Ratio d'intérêt", "pt": "Proporção de juros", "de": "Zinsverhältnis", "it": "Rapporto interessi"},
    "kinetic_energy": {"en": "Kinetic energy", "es": "Energía cinética", "fr": "Énergie cinétique", "pt": "Energia cinética", "de": "Kinetische Energie", "it": "Energia cinetica"},
    "joules": {"en": "Joules", "es": "Julios", "fr": "Joules", "pt": "Joules", "de": "Joule", "it": "Joule"},
    "calories": {"en": "Calories", "es": "Calorías", "fr": "Calories", "pt": "Calorias", "de": "Kalorien", "it": "Calorie"},
    "force": {"en": "Force", "es": "Fuerza", "fr": "Force", "pt": "Força", "de": "Kraft", "it": "Forza"},
    "area": {"en": "Area", "es": "Área", "fr": "Aire", "pt": "Área", "de": "Fläche", "it": "Area"},
    "perimetro": {"en": "Perimeter", "es": "Perímetro", "fr": "Périmètre", "pt": "Perímetro", "de": "Umfang", "it": "Perimetro"},
    "volumen": {"en": "Volume", "es": "Volumen", "fr": "Volume", "pt": "Volume", "de": "Volumen", "it": "Volume"},
    "area_superficial": {"en": "Surface area", "es": "Área superficial", "fr": "Aire surfacique", "pt": "Área superficial", "de": "Oberfläche", "it": "Area superficiale"},
    "empuje": {"en": "Buoyancy force", "es": "Fuerza de empuje", "fr": "Poussée", "pt": "Empuxo", "de": "Auftriebskraft", "it": "Forza di galleggiamento"},
    "peso_aparente": {"en": "Apparent weight", "es": "Peso aparente", "fr": "Poids apparent", "pt": "Peso aparente", "de": "Scheinbares Gewicht", "it": "Peso apparente"},
    "masa_molar": {"en": "Molar mass", "es": "Masa molar", "fr": "Masse molaire", "pt": "Massa molar", "de": "Molmasse", "it": "Massa molare"},
    "ph": {"en": "pH", "es": "pH", "fr": "pH", "pt": "pH", "de": "pH", "it": "pH"},
    "indice_calor": {"en": "Heat index", "es": "Índice de calor", "fr": "Indice de chaleur", "pt": "Índice de calor", "de": "Hitzeindex", "it": "Indice di calore"},
    "entropia": {"en": "Entropy (bits)", "es": "Entropía (bits)", "fr": "Entropie (bits)", "pt": "Entropia (bits)", "de": "Entropie (Bits)", "it": "Entropia (bit)"},
    "fuerza_password": {"en": "Password strength", "es": "Fortaleza de la contraseña", "fr": "Force du mot de passe", "pt": "Força da senha", "de": "Passwortstärke", "it": "Forza della password"},
}


def translate_input_output_labels():
    """Translate input and output labels for batch 4 and 5 across all languages."""
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
            entry = calcs[calc_id]
            
            # Translate input labels
            inputs = entry.get('inputs', {})
            if isinstance(inputs, dict):
                for key in list(inputs.keys()):
                    if key in INPUT_LABELS and lang in INPUT_LABELS[key]:
                        inputs[key] = INPUT_LABELS[key][lang]
                        changed += 1
            
            # Translate output labels
            outputs = entry.get('outputs', {})
            if isinstance(outputs, dict):
                for key in list(outputs.keys()):
                    if key in OUTPUT_LABELS and lang in OUTPUT_LABELS[key]:
                        outputs[key] = OUTPUT_LABELS[key][lang]
                        changed += 1
        
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        
        print(f'  Translated {changed} labels in {lang}.json')


if __name__ == '__main__':
    print('Translating input/output labels...')
    translate_input_output_labels()
    print('Done!')
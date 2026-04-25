"""Patch calc_content.py: add CALC_FACTS dict + build_article_from_facts() + update generate_long_content()."""
import re, sys

TARGET = "scripts/calc_content.py"

APPEND = r'''

# ── CALC_FACTS: compact per-calc data for auto-generating unique SEO articles ──
# Keys: calc_id -> lang -> {f: formula, ei: example input, eo: example output, u: uses list}
# Only es + en needed; build_article_from_facts() falls back to "en" for other langs.
CALC_FACTS = {
    # ── Matemáticas ──────────────────────────────────────────────────────────
    "202": {  # area-rectangulo
        "es": {"f": "Área = largo × ancho", "ei": "largo 6 m, ancho 4,5 m", "eo": "Área = 27 m²",
               "u": ["calcular suelos y azulejos", "estimar pintura de techos", "diseño de jardines", "distribución de muebles"]},
        "en": {"f": "Area = length × width", "ei": "length 6 m, width 4.5 m", "eo": "Area = 27 m²",
               "u": ["flooring and tiling estimates", "ceiling paint coverage", "garden layout planning", "furniture arrangement"]},
    },
    "204": {  # regla-de-tres
        "es": {"f": "x = (B × C) / A  (si A→B, entonces C→x)", "ei": "3 kg cuestan 7,50 €; ¿cuánto cuestan 5 kg?", "eo": "x = 12,50 €",
               "u": ["conversión de recetas de cocina", "cálculo de precios proporcionales", "escalado de planos y mapas", "repartos proporcionales"]},
        "en": {"f": "x = (B × C) / A  (if A→B, then C→x)", "ei": "3 kg costs €7.50; how much do 5 kg cost?", "eo": "x = €12.50",
               "u": ["scaling recipes", "proportional price calculations", "map and blueprint scaling", "proportional distribution"]},
    },
    "211": {  # area-triangulo
        "es": {"f": "Área = (base × altura) / 2", "ei": "base 8 m, altura 5 m", "eo": "Área = 20 m²",
               "u": ["techados triangulares", "cálculo de terrenos irregulares", "proyectos de carpintería", "geometría escolar"]},
        "en": {"f": "Area = (base × height) / 2", "ei": "base 8 m, height 5 m", "eo": "Area = 20 m²",
               "u": ["triangular roof sections", "irregular land plots", "carpentry projects", "school geometry"]},
    },
    "212": {  # volumen-esfera
        "es": {"f": "Volumen = (4/3) × π × r³", "ei": "radio 3 m", "eo": "Volumen = 113,1 m³",
               "u": ["depósitos esféricos de agua o gas", "cálculo de bolas deportivas", "tanques industriales", "astronomía y planetas"]},
        "en": {"f": "Volume = (4/3) × π × r³", "ei": "radius 3 m", "eo": "Volume = 113.1 m³",
               "u": ["spherical water or gas tanks", "sports ball sizing", "industrial tanks", "astronomy and planet volumes"]},
    },
    "213": {  # volumen-cilindro
        "es": {"f": "Volumen = π × r² × h", "ei": "radio 2 m, altura 5 m", "eo": "Volumen = 62,83 m³",
               "u": ["depósitos cilíndricos", "tuberías y alcantarillado", "silos agrícolas", "envases industriales"]},
        "en": {"f": "Volume = π × r² × h", "ei": "radius 2 m, height 5 m", "eo": "Volume = 62.83 m³",
               "u": ["cylindrical tanks", "pipes and sewers", "agricultural silos", "industrial containers"]},
    },
    "214": {  # potencias
        "es": {"f": "aⁿ = a × a × … × a (n veces)", "ei": "2¹⁰", "eo": "1 024",
               "u": ["informática (bytes a potencias de 2)", "crecimiento exponencial", "física (potencias de 10)", "fórmulas de interés compuesto"]},
        "en": {"f": "aⁿ = a × a × … × a (n times)", "ei": "2¹⁰", "eo": "1,024",
               "u": ["computing (bytes as powers of 2)", "exponential growth modeling", "physics (powers of 10)", "compound interest formulas"]},
    },
    "215": {  # raiz
        "es": {"f": "ⁿ√x = x^(1/n)", "ei": "√144", "eo": "12",
               "u": ["cálculo de lados de un cuadrado", "estadística (desviación estándar)", "fórmula cuadrática", "normalización de datos"]},
        "en": {"f": "ⁿ√x = x^(1/n)", "ei": "√144", "eo": "12",
               "u": ["finding side length of a square", "statistics (standard deviation)", "quadratic formula", "data normalization"]},
    },
    "216": {  # logaritmo
        "es": {"f": "log_b(x) = y  ↔  b^y = x", "ei": "log₁₀(1000)", "eo": "3",
               "u": ["escala de Richter (terremotos)", "escala de decibelios (sonido)", "crecimiento exponencial inverso", "informática (complejidad algorítmica)"]},
        "en": {"f": "log_b(x) = y  ↔  b^y = x", "ei": "log₁₀(1000)", "eo": "3",
               "u": ["Richter scale (earthquakes)", "decibel scale (sound)", "inverse exponential growth", "computing (algorithm complexity)"]},
    },
    "217": {  # factorial
        "es": {"f": "n! = n × (n-1) × … × 2 × 1", "ei": "5!", "eo": "120",
               "u": ["combinaciones y permutaciones", "probabilidad", "series matemáticas (Taylor)", "juegos y apuestas"]},
        "en": {"f": "n! = n × (n-1) × … × 2 × 1", "ei": "5!", "eo": "120",
               "u": ["combinations and permutations", "probability calculations", "mathematical series (Taylor)", "games and betting odds"]},
    },
    "218": {  # ecuacion-segundo-grado
        "es": {"f": "x = (-b ± √(b²-4ac)) / 2a", "ei": "2x²+5x-3=0 (a=2, b=5, c=-3)", "eo": "x₁=0,5  x₂=-3",
               "u": ["trayectorias parabólicas", "optimización de áreas", "física (movimiento uniformemente acelerado)", "economía (punto de equilibrio cuadrático)"]},
        "en": {"f": "x = (-b ± √(b²-4ac)) / 2a", "ei": "2x²+5x-3=0 (a=2, b=5, c=-3)", "eo": "x₁=0.5  x₂=-3",
               "u": ["parabolic trajectories", "area optimization", "physics (uniformly accelerated motion)", "economics (quadratic break-even)"]},
    },
    "219": {  # mcm-mcd
        "es": {"f": "MCD por algoritmo de Euclides; MCM = (a×b)/MCD(a,b)", "ei": "MCD(48, 18)", "eo": "MCD = 6; MCM = 144",
               "u": ["simplificación de fracciones", "sincronización de ciclos repetitivos", "programación (alineación de buffers)", "problemas de distribución equitativa"]},
        "en": {"f": "GCD via Euclidean algorithm; LCM = (a×b)/GCD(a,b)", "ei": "GCD(48, 18)", "eo": "GCD = 6; LCM = 144",
               "u": ["simplifying fractions", "synchronizing repeating cycles", "programming (buffer alignment)", "equal distribution problems"]},
    },

    # ── Finanzas ─────────────────────────────────────────────────────────────
    "303": {  # interes-simple
        "es": {"f": "Interés = Principal × Tasa × Tiempo", "ei": "5.000 € al 4 % durante 3 años", "eo": "Interés = 600 €; Total = 5.600 €",
               "u": ["préstamos personales a corto plazo", "depósitos bancarios simples", "comparar ofertas de crédito", "cálculos de arrendamiento"]},
        "en": {"f": "Interest = Principal × Rate × Time", "ei": "€5,000 at 4% for 3 years", "eo": "Interest = €600; Total = €5,600",
               "u": ["short-term personal loans", "simple bank deposits", "comparing credit offers", "lease calculations"]},
    },
    "306": {  # descuento
        "es": {"f": "Precio final = Precio original × (1 - Descuento%/100)", "ei": "Precio 120 €, descuento 25 %", "eo": "Precio final = 90 €",
               "u": ["compras en rebajas", "negociación comercial", "márgenes de distribución", "comparar ofertas online"]},
        "en": {"f": "Final price = Original price × (1 - Discount%/100)", "ei": "Price €120, discount 25%", "eo": "Final price = €90",
               "u": ["sale shopping", "commercial negotiation", "distribution margins", "comparing online deals"]},
    },
    "307": {  # punto-de-equilibrio
        "es": {"f": "Unidades = Costes fijos / (Precio unitario - Coste variable unitario)", "ei": "Costes fijos 10.000 €, precio 50 €, coste variable 30 €", "eo": "Punto de equilibrio = 500 unidades",
               "u": ["valorar viabilidad de un negocio", "fijar precios mínimos", "análisis de nuevos productos", "decisiones de inversión"]},
        "en": {"f": "Units = Fixed costs / (Unit price - Variable unit cost)", "ei": "Fixed costs €10,000, price €50, variable cost €30", "eo": "Break-even = 500 units",
               "u": ["business feasibility analysis", "setting minimum prices", "new product analysis", "investment decisions"]},
    },
    "310": {  # roi
        "es": {"f": "ROI (%) = ((Beneficio neto - Coste) / Coste) × 100", "ei": "Inversión 2.000 €, retorno 2.600 €", "eo": "ROI = 30 %",
               "u": ["evaluar campañas de marketing", "comparar inversiones alternativas", "medir rentabilidad de proyectos", "análisis de acciones y fondos"]},
        "en": {"f": "ROI (%) = ((Net profit - Cost) / Cost) × 100", "ei": "Investment €2,000, return €2,600", "eo": "ROI = 30%",
               "u": ["evaluating marketing campaigns", "comparing alternative investments", "measuring project profitability", "stock and fund analysis"]},
    },
    "311": {  # ahorro-compuesto
        "es": {"f": "FV = PMT × ((1+r)ⁿ - 1) / r", "ei": "200 €/mes al 5 % anual durante 20 años", "eo": "Ahorro acumulado ≈ 82.549 €",
               "u": ["planificación del fondo de emergencia", "ahorro para la universidad", "jubilación anticipada", "comparar planes de pensiones"]},
        "en": {"f": "FV = PMT × ((1+r)ⁿ - 1) / r", "ei": "€200/month at 5% annual for 20 years", "eo": "Savings ≈ €82,549",
               "u": ["emergency fund planning", "college savings", "early retirement (FIRE)", "comparing pension plans"]},
    },
    "312": {  # inflacion
        "es": {"f": "Valor real = Valor nominal / (1 + Inflación%)ⁿ", "ei": "1.000 € con 3 % anual durante 10 años", "eo": "Poder adquisitivo real ≈ 744 €",
               "u": ["ajustar salarios a la inflación", "planificar el ahorro a largo plazo", "comparar precios históricos", "análisis económico"]},
        "en": {"f": "Real value = Nominal value / (1 + Inflation%)ⁿ", "ei": "€1,000 at 3% annual for 10 years", "eo": "Real purchasing power ≈ €744",
               "u": ["salary inflation adjustments", "long-term savings planning", "comparing historical prices", "economic analysis"]},
    },
    "313": {  # subida-salarial
        "es": {"f": "Nuevo salario = Salario actual × (1 + Subida%/100)", "ei": "Salario 28.000 €, subida 4,5 %", "eo": "Nuevo salario = 29.260 €",
               "u": ["negociar aumento de sueldo", "planificar presupuesto familiar", "evaluar ofertas laborales", "calcular coste salarial para empresas"]},
        "en": {"f": "New salary = Current salary × (1 + Raise%/100)", "ei": "Salary €28,000, raise 4.5%", "eo": "New salary = €29,260",
               "u": ["negotiating a pay raise", "family budget planning", "evaluating job offers", "employer payroll cost calculations"]},
    },
    "314": {  # plan-jubilacion
        "es": {"f": "Ahorro necesario = Gasto anual × Años jubilación / (1+r)ⁿ (simplificado)", "ei": "Retiro a 65, 2.000 €/mes, 25 años de retiro, 4 % rendimiento", "eo": "Capital necesario ≈ 378.000 €",
               "u": ["planificar la edad de jubilación", "estimar aportaciones mensuales al plan de pensiones", "estrategia FIRE (jubilación anticipada)", "comparar planes de pensiones"]},
        "en": {"f": "Required savings = Annual spending × Retirement years / (1+r)ⁿ (simplified)", "ei": "Retire at 65, €2,000/month, 25 years retirement, 4% return", "eo": "Capital needed ≈ €378,000",
               "u": ["planning retirement age", "estimating monthly pension contributions", "FIRE strategy (early retirement)", "comparing pension plans"]},
    },
    "315": {  # regla-72
        "es": {"f": "Años para doblar = 72 / Tasa de interés (%)", "ei": "Tasa de interés 6 % anual", "eo": "Inversión se dobla en ≈ 12 años",
               "u": ["estimar crecimiento de inversiones", "comparar fondos de inversión", "inflación: tiempo en que se reduce el poder adquisitivo a la mitad", "educación financiera básica"]},
        "en": {"f": "Years to double = 72 / Interest rate (%)", "ei": "Interest rate 6% annual", "eo": "Investment doubles in ≈ 12 years",
               "u": ["estimating investment growth", "comparing investment funds", "inflation: time for purchasing power to halve", "basic financial literacy"]},
    },
    "316": {  # deposito-plazo
        "es": {"f": "Interés = Capital × (1 + Tasa/n)^(n×t) - Capital", "ei": "10.000 € al 3,5 % anual, 1 año, capitalización mensual", "eo": "Interés = 355,77 €; Total = 10.355,77 €",
               "u": ["comparar depósitos bancarios", "planificar ahorro a corto plazo", "elegir entre depósito y fondo de inversión", "calcular rendimiento neto tras impuestos"]},
        "en": {"f": "Interest = Capital × (1 + Rate/n)^(n×t) - Capital", "ei": "€10,000 at 3.5% annual, 1 year, monthly compounding", "eo": "Interest = €355.77; Total = €10,355.77",
               "u": ["comparing bank deposits", "short-term savings planning", "choosing between deposit and fund", "net return after taxes"]},
    },
    "317": {  # retorno-acciones
        "es": {"f": "Retorno total (%) = ((Precio final + Dividendos - Precio inicial) / Precio inicial) × 100", "ei": "Compra a 50 €, venta a 62 €, dividendos 1,50 €", "eo": "Retorno = 27 %",
               "u": ["evaluar rentabilidad de acciones", "comparar inversiones en bolsa", "calcular retorno de ETF o fondos", "análisis histórico de cartera"]},
        "en": {"f": "Total return (%) = ((Final price + Dividends - Initial price) / Initial price) × 100", "ei": "Buy at €50, sell at €62, dividends €1.50", "eo": "Return = 27%",
               "u": ["evaluating stock performance", "comparing stock market investments", "ETF or fund return calculation", "historical portfolio analysis"]},
    },
    "318": {  # ratio-deuda
        "es": {"f": "Ratio de endeudamiento = Deuda total / Patrimonio neto", "ei": "Deuda 40.000 €, Patrimonio 160.000 €", "eo": "Ratio = 0,25 (25 %)",
               "u": ["análisis financiero de empresas", "solicitar préstamos hipotecarios", "evaluar solvencia de un autónomo", "análisis de riesgo crediticio"]},
        "en": {"f": "Debt ratio = Total debt / Net equity", "ei": "Debt €40,000, Equity €160,000", "eo": "Ratio = 0.25 (25%)",
               "u": ["company financial analysis", "mortgage loan applications", "freelancer solvency assessment", "credit risk analysis"]},
    },
    "319": {  # punto-equilibrio-unidades
        "es": {"f": "Precio mínimo = (Costes fijos / Unidades) + Coste variable unitario", "ei": "Costes fijos 5.000 €, 200 unidades, coste variable 15 €", "eo": "Precio mínimo = 40 €/ud",
               "u": ["fijar precio de venta mínimo", "evaluar nuevos productos", "licitaciones y presupuestos", "análisis coste-volumen-beneficio"]},
        "en": {"f": "Minimum price = (Fixed costs / Units) + Variable unit cost", "ei": "Fixed costs €5,000, 200 units, variable cost €15", "eo": "Minimum price = €40/unit",
               "u": ["setting minimum selling price", "new product evaluation", "bids and quotes", "cost-volume-profit analysis"]},
    },

    # ── Salud ────────────────────────────────────────────────────────────────
    "410": {  # metabolismo-basal
        "es": {"f": "TMB (Mifflin) = 10×peso + 6,25×altura - 5×edad + s (s=+5 H, -161 M)", "ei": "Hombre, 30 años, 75 kg, 178 cm", "eo": "TMB ≈ 1.804 kcal/día",
               "u": ["calcular calorías de mantenimiento", "planificar dietas de déficit o superávit", "nutrición deportiva", "planes de pérdida de peso"]},
        "en": {"f": "BMR (Mifflin) = 10×weight + 6.25×height - 5×age + s (s=+5 M, -161 F)", "ei": "Male, 30 years, 75 kg, 178 cm", "eo": "BMR ≈ 1,804 kcal/day",
               "u": ["calculating maintenance calories", "deficit or surplus diet planning", "sports nutrition", "weight loss plans"]},
    },
    "411": {  # frecuencia-cardiaca-max-salud
        "es": {"f": "FCmáx = 220 - edad (fórmula clásica)", "ei": "Persona de 35 años", "eo": "FCmáx = 185 ppm",
               "u": ["establecer zonas de entrenamiento cardíaco", "monitorizar esfuerzo en ejercicio", "prevenir sobrecarga cardiovascular", "programas de rehabilitación cardíaca"]},
        "en": {"f": "Max HR = 220 - age (classic formula)", "ei": "35-year-old person", "eo": "Max HR = 185 bpm",
               "u": ["setting heart rate training zones", "exercise effort monitoring", "preventing cardiovascular overload", "cardiac rehabilitation programs"]},
    },
    "412": {  # horas-sueno
        "es": {"f": "Sueño óptimo = Ciclos × 90 min (ciclos recomendados: 5–6)", "ei": "5 ciclos de sueño", "eo": "Sueño óptimo = 7,5 horas",
               "u": ["calcular hora óptima de despertar", "planificar siestas reparadoras", "gestión del jet lag", "higiene del sueño para deportistas"]},
        "en": {"f": "Optimal sleep = Cycles × 90 min (recommended cycles: 5–6)", "ei": "5 sleep cycles", "eo": "Optimal sleep = 7.5 hours",
               "u": ["calculating optimal wake-up time", "planning restorative naps", "jet lag management", "sleep hygiene for athletes"]},
    },
    "413": {  # porcentaje-grasa
        "es": {"f": "% Grasa (Marina US) = 86,010×log(abdomen-cuello) - 70,041×log(altura) + 36,76 (H)", "ei": "Hombre: abdomen 90 cm, cuello 38 cm, altura 178 cm", "eo": "% Grasa ≈ 19,4 %",
               "u": ["monitorizar composición corporal", "planificar ciclos de definición muscular", "evaluar riesgo de enfermedades metabólicas", "seguimiento de dietas cetogénicas"]},
        "en": {"f": "% Fat (US Navy) = 86.010×log(waist-neck) - 70.041×log(height) + 36.76 (M)", "ei": "Male: waist 90 cm, neck 38 cm, height 178 cm", "eo": "Body fat ≈ 19.4%",
               "u": ["monitoring body composition", "planning muscle definition cycles", "metabolic disease risk assessment", "keto diet tracking"]},
    },
    "414": {  # rango-peso-saludable
        "es": {"f": "Peso saludable: IMC entre 18,5 y 24,9 → Peso = IMC × altura²", "ei": "Altura 170 cm", "eo": "Rango saludable: 53,5 – 71,9 kg",
               "u": ["orientación nutricional básica", "objetivos de pérdida de peso", "evaluación pediátrica de crecimiento", "seguros de salud y medicina preventiva"]},
        "en": {"f": "Healthy weight: BMI between 18.5 and 24.9 → Weight = BMI × height²", "ei": "Height 170 cm", "eo": "Healthy range: 53.5 – 71.9 kg",
               "u": ["basic nutritional guidance", "weight loss goal setting", "pediatric growth assessment", "health insurance and preventive medicine"]},
    },

    # ── Cotidiano ────────────────────────────────────────────────────────────
    "502": {  # diferencia-fechas
        "es": {"f": "Diferencia = Fecha fin - Fecha inicio (en días, semanas, meses, años)", "ei": "Del 15/03/2020 al 22/04/2026", "eo": "2.229 días · 318 semanas · 73 meses · 6 años",
               "u": ["calcular antigüedad laboral", "plazos contractuales", "duración de embarazo", "cuenta atrás para eventos"]},
        "en": {"f": "Difference = End date - Start date (in days, weeks, months, years)", "ei": "From 15/03/2020 to 22/04/2026", "eo": "2,229 days · 318 weeks · 73 months · 6 years",
               "u": ["calculating work tenure", "contract deadlines", "pregnancy duration", "event countdowns"]},
    },

    # ── Estadística ──────────────────────────────────────────────────────────
    "601": {  # mediana
        "es": {"f": "Mediana = valor central del conjunto ordenado", "ei": "[3, 7, 2, 9, 5] → ordenado [2,3,5,7,9]", "eo": "Mediana = 5",
               "u": ["salarios (resistente a valores extremos)", "precios inmobiliarios", "tiempos de respuesta en sistemas", "encuestas de satisfacción"]},
        "en": {"f": "Median = middle value of sorted dataset", "ei": "[3, 7, 2, 9, 5] → sorted [2,3,5,7,9]", "eo": "Median = 5",
               "u": ["salary data (resistant to outliers)", "real estate prices", "system response times", "satisfaction surveys"]},
    },
    "602": {  # desviacion-estandar
        "es": {"f": "σ = √(Σ(xᵢ - μ)² / N)", "ei": "Datos: [2, 4, 4, 4, 5, 5, 7, 9]", "eo": "Media = 5; σ = 2",
               "u": ["control de calidad industrial", "análisis de riesgo financiero (volatilidad)", "evaluación de resultados académicos", "análisis de datos científicos"]},
        "en": {"f": "σ = √(Σ(xᵢ - μ)² / N)", "ei": "Data: [2, 4, 4, 4, 5, 5, 7, 9]", "eo": "Mean = 5; σ = 2",
               "u": ["industrial quality control", "financial risk analysis (volatility)", "academic results evaluation", "scientific data analysis"]},
    },
    "603": {  # probabilidad
        "es": {"f": "P(A) = Casos favorables / Casos totales", "ei": "Probabilidad de sacar un 6 al lanzar un dado", "eo": "P = 1/6 ≈ 16,7 %",
               "u": ["juegos de azar y apuestas", "control de calidad (defectos por lote)", "seguros y actuaría", "análisis de riesgos de proyectos"]},
        "en": {"f": "P(A) = Favorable outcomes / Total outcomes", "ei": "Probability of rolling a 6 on a die", "eo": "P = 1/6 ≈ 16.7%",
               "u": ["games of chance and betting", "quality control (defects per batch)", "insurance and actuarial science", "project risk analysis"]},
    },
    "604": {  # combinaciones
        "es": {"f": "C(n,k) = n! / (k! × (n-k)!)", "ei": "¿De cuántas formas elegir 3 personas de un grupo de 10?", "eo": "C(10,3) = 120",
               "u": ["lotería y quinielas", "formación de equipos", "combinaciones de menú o productos", "criptografía básica"]},
        "en": {"f": "C(n,k) = n! / (k! × (n-k)!)", "ei": "How many ways to choose 3 people from a group of 10?", "eo": "C(10,3) = 120",
               "u": ["lottery and pools", "team formation", "menu or product combinations", "basic cryptography"]},
    },
    "605": {  # permutaciones
        "es": {"f": "P(n,k) = n! / (n-k)!", "ei": "¿Cuántas formas de ordenar 3 libros de una estantería de 5?", "eo": "P(5,3) = 60",
               "u": ["ordenación de tareas o procesos", "contraseñas y PINs", "programación de competiciones deportivas", "criptografía y seguridad"]},
        "en": {"f": "P(n,k) = n! / (n-k)!", "ei": "How many ways to arrange 3 books from a shelf of 5?", "eo": "P(5,3) = 60",
               "u": ["task or process scheduling", "passwords and PINs", "sports competition scheduling", "cryptography and security"]},
    },
    "606": {  # intervalo-confianza
        "es": {"f": "IC = x̄ ± z × (σ/√n)", "ei": "x̄=50, σ=10, n=100, 95% confianza (z=1,96)", "eo": "IC: [48,04 ; 51,96]",
               "u": ["encuestas electorales", "investigación clínica y farmacéutica", "control de calidad estadístico", "estudios de mercado"]},
        "en": {"f": "CI = x̄ ± z × (σ/√n)", "ei": "x̄=50, σ=10, n=100, 95% confidence (z=1.96)", "eo": "CI: [48.04 ; 51.96]",
               "u": ["electoral polls", "clinical and pharmaceutical research", "statistical quality control", "market research studies"]},
    },
    "607": {  # coeficiente-variacion
        "es": {"f": "CV (%) = (Desviación estándar / Media) × 100", "ei": "Media 80, Desviación 12", "eo": "CV = 15 %",
               "u": ["comparar variabilidad de diferentes conjuntos", "análisis de fondos de inversión (riesgo/retorno)", "control de consistencia en producción", "comparación de resultados académicos entre grupos"]},
        "en": {"f": "CV (%) = (Standard deviation / Mean) × 100", "ei": "Mean 80, SD 12", "eo": "CV = 15%",
               "u": ["comparing variability across datasets", "investment fund risk/return analysis", "production consistency control", "comparing academic results between groups"]},
    },
    "608": {  # varianza
        "es": {"f": "σ² = Σ(xᵢ - μ)² / N", "ei": "Datos: [2, 4, 4, 4, 5, 5, 7, 9]", "eo": "Varianza = 4",
               "u": ["finanzas (varianza de retornos)", "física experimental (errores de medición)", "análisis estadístico previo a regresión", "psicometría y tests"]},
        "en": {"f": "σ² = Σ(xᵢ - μ)² / N", "ei": "Data: [2, 4, 4, 4, 5, 5, 7, 9]", "eo": "Variance = 4",
               "u": ["finance (return variance)", "experimental physics (measurement errors)", "statistical analysis before regression", "psychometrics and testing"]},
    },
    "609": {  # puntuacion-z
        "es": {"f": "z = (x - μ) / σ", "ei": "Nota 85, media de clase 70, desviación 10", "eo": "z = 1,5 (1,5 desviaciones sobre la media)",
               "u": ["comparar resultados en diferentes escalas", "detectar valores atípicos (outliers)", "estandarización de datos para machine learning", "percentiles en tests psicológicos"]},
        "en": {"f": "z = (x - μ) / σ", "ei": "Score 85, class mean 70, SD 10", "eo": "z = 1.5 (1.5 std deviations above mean)",
               "u": ["comparing results on different scales", "detecting outliers", "data standardization for machine learning", "percentiles in psychological tests"]},
    },

    # ── Ciencia / Física ─────────────────────────────────────────────────────
    "701": {  # densidad
        "es": {"f": "Densidad = Masa / Volumen", "ei": "Masa 540 g, Volumen 200 cm³", "eo": "Densidad = 2,7 g/cm³ (aluminio)",
               "u": ["identificar materiales desconocidos", "calcular flotabilidad", "ingeniería de materiales", "física del buque (desplazamiento)"]},
        "en": {"f": "Density = Mass / Volume", "ei": "Mass 540 g, Volume 200 cm³", "eo": "Density = 2.7 g/cm³ (aluminium)",
               "u": ["identifying unknown materials", "buoyancy calculations", "materials engineering", "naval engineering (displacement)"]},
    },
    "702": {  # fuerza
        "es": {"f": "F = m × a (Segunda ley de Newton)", "ei": "Masa 10 kg, aceleración 9,8 m/s²", "eo": "Fuerza = 98 N (peso en la Tierra)",
               "u": ["cálculo de fuerzas en estructuras", "diseño mecánico", "física del deporte (impacto)", "análisis de colisiones"]},
        "en": {"f": "F = m × a (Newton's second law)", "ei": "Mass 10 kg, acceleration 9.8 m/s²", "eo": "Force = 98 N (weight on Earth)",
               "u": ["structural force calculations", "mechanical design", "sports physics (impact)", "collision analysis"]},
    },
    "703": {  # energia-cinetica
        "es": {"f": "Ec = ½ × m × v²", "ei": "Masa 1.200 kg (coche), velocidad 30 m/s (108 km/h)", "eo": "Ec = 540.000 J = 540 kJ",
               "u": ["análisis de accidentes de tráfico", "diseño de sistemas de frenado", "física de proyectiles y deportes", "ingeniería de seguridad vial"]},
        "en": {"f": "KE = ½ × m × v²", "ei": "Mass 1,200 kg (car), velocity 30 m/s (108 km/h)", "eo": "KE = 540,000 J = 540 kJ",
               "u": ["traffic accident analysis", "braking system design", "projectile and sports physics", "road safety engineering"]},
    },
    "704": {  # energia-potencial
        "es": {"f": "Ep = m × g × h (g = 9,81 m/s²)", "ei": "Objeto 5 kg a 20 m de altura", "eo": "Ep = 981 J",
               "u": ["hidroeléctrica (energía del agua embalsada)", "diseño de montañas rusas", "física de caídas libres", "análisis de sistemas de contrapeso"]},
        "en": {"f": "PE = m × g × h (g = 9.81 m/s²)", "ei": "Object 5 kg at 20 m height", "eo": "PE = 981 J",
               "u": ["hydroelectric power (stored water energy)", "roller coaster design", "free-fall physics", "counterweight system analysis"]},
    },
    "705": {  # presion
        "es": {"f": "Presión = Fuerza / Área", "ei": "Fuerza 500 N, Área 0,25 m²", "eo": "Presión = 2.000 Pa = 2 kPa",
               "u": ["hidráulica e neumática", "meteorología (presión atmosférica)", "medicina (presión arterial)", "ingeniería de tuberías"]},
        "en": {"f": "Pressure = Force / Area", "ei": "Force 500 N, Area 0.25 m²", "eo": "Pressure = 2,000 Pa = 2 kPa",
               "u": ["hydraulics and pneumatics", "meteorology (atmospheric pressure)", "medicine (blood pressure)", "pipe engineering"]},
    },
    "706": {  # trabajo-mecanico
        "es": {"f": "W = F × d × cos(θ)", "ei": "Fuerza 200 N, distancia 15 m, ángulo 0°", "eo": "Trabajo = 3.000 J",
               "u": ["cálculo de potencia de motores", "ascensores y grúas", "biomecánica del ejercicio", "diseño de poleas y palancas"]},
        "en": {"f": "W = F × d × cos(θ)", "ei": "Force 200 N, distance 15 m, angle 0°", "eo": "Work = 3,000 J",
               "u": ["motor power calculations", "elevators and cranes", "exercise biomechanics", "pulley and lever design"]},
    },
    "707": {  # ley-ohm
        "es": {"f": "V = I × R  (también: I = V/R, R = V/I)", "ei": "Tensión 220 V, Resistencia 44 Ω", "eo": "Corriente = 5 A",
               "u": ["diseño de circuitos eléctricos", "selección de resistencias en electrónica", "diagnóstico de averías eléctricas", "instalaciones domésticas"]},
        "en": {"f": "V = I × R  (also: I = V/R, R = V/I)", "ei": "Voltage 220 V, Resistance 44 Ω", "eo": "Current = 5 A",
               "u": ["electrical circuit design", "resistor selection in electronics", "electrical fault diagnosis", "home electrical installations"]},
    },
    "708": {  # potencia-electrica
        "es": {"f": "P = V × I = I² × R = V²/R", "ei": "Tensión 230 V, Corriente 10 A", "eo": "Potencia = 2.300 W = 2,3 kW",
               "u": ["calcular consumo eléctrico", "dimensionar instalaciones fotovoltaicas", "selección de generadores y baterías", "coste de electrodomésticos en la factura"]},
        "en": {"f": "P = V × I = I² × R = V²/R", "ei": "Voltage 230 V, Current 10 A", "eo": "Power = 2,300 W = 2.3 kW",
               "u": ["calculating electricity consumption", "sizing solar PV installations", "generator and battery selection", "appliance cost on electricity bill"]},
    },
    "709": {  # aceleracion
        "es": {"f": "a = (v_f - v_i) / t", "ei": "v_i = 0 m/s, v_f = 30 m/s, t = 5 s", "eo": "a = 6 m/s²",
               "u": ["rendimiento de vehículos (0-100 km/h)", "análisis de colisiones", "física de cohetes y aeronaves", "diseño de sistemas de control"]},
        "en": {"f": "a = (v_f - v_i) / t", "ei": "v_i = 0 m/s, v_f = 30 m/s, t = 5 s", "eo": "a = 6 m/s²",
               "u": ["vehicle performance (0-100 km/h)", "collision analysis", "rocket and aircraft physics", "control system design"]},
    },

    # ── Conversión ───────────────────────────────────────────────────────────
    "801": {  # peso
        "es": {"f": "kg × 2,20462 = lb | kg × 1.000 = g | kg / 1.000 = t", "ei": "75 kg", "eo": "75 kg = 165,35 lb = 75.000 g = 0,075 t",
               "u": ["conversión de recetas de cocina", "límites de equipaje aéreo", "compra en tiendas internacionales", "medicina y farmacia"]},
        "en": {"f": "kg × 2.20462 = lb | kg × 1,000 = g | kg / 1,000 = t", "ei": "75 kg", "eo": "75 kg = 165.35 lb = 75,000 g = 0.075 t",
               "u": ["recipe conversions", "airline baggage limits", "international shopping", "medicine and pharmacy"]},
    },
    "803": {  # volumen
        "es": {"f": "1 L = 1.000 mL = 0,001 m³ = 0,2642 gal (US)", "ei": "5 litros", "eo": "5 L = 5.000 mL = 1,321 gal US = 1,099 gal UK",
               "u": ["conversión de recetas y coctelería", "cálculo de depósitos y estanques", "importación de combustibles", "compra en farmacia y laboratorio"]},
        "en": {"f": "1 L = 1,000 mL = 0.001 m³ = 0.2642 gal (US)", "ei": "5 liters", "eo": "5 L = 5,000 mL = 1.321 US gal = 1.099 UK gal",
               "u": ["recipe and cocktail conversions", "tank and reservoir calculations", "fuel import conversions", "pharmacy and lab purchases"]},
    },
    "804": {  # area
        "es": {"f": "1 m² = 10.000 cm² = 0,0001 ha = 10,764 ft²", "ei": "250 m²", "eo": "250 m² = 0,025 ha = 2.691 ft² = 0,062 acres",
               "u": ["comparar precios de inmuebles en distintos países", "compraventa de terrenos agrícolas", "proyectos de construcción internacionales", "planificación urbana"]},
        "en": {"f": "1 m² = 10,000 cm² = 0.0001 ha = 10.764 ft²", "ei": "250 m²", "eo": "250 m² = 0.025 ha = 2,691 ft² = 0.062 acres",
               "u": ["comparing real estate prices internationally", "agricultural land transactions", "international construction projects", "urban planning"]},
    },
    "805": {  # velocidad-unidades
        "es": {"f": "km/h × 0,27778 = m/s | km/h × 0,62137 = mph | km/h / 1,852 = nudos", "ei": "120 km/h", "eo": "120 km/h = 33,33 m/s = 74,56 mph = 64,8 nudos",
               "u": ["límites de velocidad internacionales", "navegación marítima y aérea", "física y cinemática", "competiciones deportivas cronometradas"]},
        "en": {"f": "km/h × 0.27778 = m/s | km/h × 0.62137 = mph | km/h / 1.852 = knots", "ei": "120 km/h", "eo": "120 km/h = 33.33 m/s = 74.56 mph = 64.8 knots",
               "u": ["international speed limits", "maritime and aviation navigation", "physics and kinematics", "timed sports competitions"]},
    },
    "806": {  # datos-digitales
        "es": {"f": "1 GB = 1.024 MB = 1.048.576 KB = 8.589.934.592 bits", "ei": "4,5 GB", "eo": "4,5 GB = 4.608 MB = 4.718.592 KB",
               "u": ["estimar espacio de almacenamiento", "calcular tiempo de descarga", "dimensionar planes de datos móviles", "presupuestar servidores y NAS"]},
        "en": {"f": "1 GB = 1,024 MB = 1,048,576 KB = 8,589,934,592 bits", "ei": "4.5 GB", "eo": "4.5 GB = 4,608 MB = 4,718,592 KB",
               "u": ["estimating storage space", "calculating download time", "sizing mobile data plans", "budgeting servers and NAS"]},
    },
    "807": {  # presion-unidades
        "es": {"f": "1 atm = 101.325 Pa = 1,01325 bar = 14,696 psi", "ei": "2,5 bar", "eo": "2,5 bar = 250.000 Pa = 36,26 psi = 2,47 atm",
               "u": ["mantenimiento de neumáticos (PSI/bar)", "buceo y equipos de respiración", "fontanería y sistemas hidráulicos", "meteorología (hPa/mbar)"]},
        "en": {"f": "1 atm = 101,325 Pa = 1.01325 bar = 14.696 psi", "ei": "2.5 bar", "eo": "2.5 bar = 250,000 Pa = 36.26 psi = 2.47 atm",
               "u": ["tyre pressure maintenance (PSI/bar)", "diving and breathing equipment", "plumbing and hydraulic systems", "meteorology (hPa/mbar)"]},
    },
    "808": {  # tiempo-unidades
        "es": {"f": "1 año = 365,25 días = 8.766 horas = 525.960 min = 31.557.600 s", "ei": "3,5 días", "eo": "3,5 días = 84 h = 5.040 min = 302.400 s",
               "u": ["conversión de plazos contractuales", "planificación de proyectos (días hábiles)", "física de partículas (nanosegundos)", "astronomía (años luz y parsecs)"]},
        "en": {"f": "1 year = 365.25 days = 8,766 hours = 525,960 min = 31,557,600 s", "ei": "3.5 days", "eo": "3.5 days = 84 h = 5,040 min = 302,400 s",
               "u": ["contract deadline conversions", "project planning (working days)", "particle physics (nanoseconds)", "astronomy (light-years and parsecs)"]},
    },
    "809": {  # energia-unidades
        "es": {"f": "1 kWh = 3.600.000 J = 3.600 kJ = 860,4 kcal", "ei": "5 kWh", "eo": "5 kWh = 18.000 kJ = 4.302 kcal = 17.065 BTU",
               "u": ["factura eléctrica (kWh a euros)", "paneles solares (producción diaria)", "nutrición (kcal a kJ)", "comparar fuentes de energía (BTU)"]},
        "en": {"f": "1 kWh = 3,600,000 J = 3,600 kJ = 860.4 kcal", "ei": "5 kWh", "eo": "5 kWh = 18,000 kJ = 4,302 kcal = 17,065 BTU",
               "u": ["electricity bill (kWh to €)", "solar panels (daily production)", "nutrition (kcal to kJ)", "comparing energy sources (BTU)"]},
    },

    # ── Deportes ─────────────────────────────────────────────────────────────
    "901": {  # calorias-ejercicio
        "es": {"f": "Calorías = MET × Peso (kg) × Tiempo (h)", "ei": "Correr (MET 9,8), 70 kg, 45 min", "eo": "Calorías quemadas ≈ 514 kcal",
               "u": ["déficit calórico para perder peso", "planificar recargas de carbohidratos", "comparar actividades deportivas", "seguimiento con pulsómetro"]},
        "en": {"f": "Calories = MET × Weight (kg) × Time (h)", "ei": "Running (MET 9.8), 70 kg, 45 min", "eo": "Calories burned ≈ 514 kcal",
               "u": ["caloric deficit for weight loss", "planning carbohydrate reloads", "comparing sports activities", "heart rate monitor tracking"]},
    },
    "902": {  # frecuencia-cardiaca-max
        "es": {"f": "FCmáx = 220 - edad | Fórmula Tanaka: 208 - 0,7 × edad", "ei": "Persona de 40 años", "eo": "FCmáx = 180 ppm (clásica) | 180 ppm (Tanaka)",
               "u": ["zonas de entrenamiento aeróbico y anaeróbico", "calibrar pulsómetros y relojes deportivos", "salud cardiovascular preventiva", "tests de esfuerzo clínicos"]},
        "en": {"f": "Max HR = 220 - age | Tanaka formula: 208 - 0.7 × age", "ei": "40-year-old person", "eo": "Max HR = 180 bpm (classic) | 180 bpm (Tanaka)",
               "u": ["aerobic and anaerobic training zones", "calibrating heart rate monitors", "preventive cardiovascular health", "clinical stress tests"]},
    },
    "903": {  # zonas-cardiacas
        "es": {"f": "Zona = % FCmáx | Zona 1: <60 %, Zona 2: 60-70 %, Zona 3: 70-80 %, Zona 4: 80-90 %, Zona 5: >90 %", "ei": "FCmáx 185 ppm", "eo": "Z2: 111-130 ppm | Z3: 130-148 ppm | Z4: 148-167 ppm",
               "u": ["estructurar semanas de entrenamiento", "mejorar resistencia aeróbica (zona 2)", "preparar carreras de competición", "recuperación activa (zona 1)"]},
        "en": {"f": "Zone = % Max HR | Zone 1: <60%, Zone 2: 60-70%, Zone 3: 70-80%, Zone 4: 80-90%, Zone 5: >90%", "ei": "Max HR 185 bpm", "eo": "Z2: 111-130 bpm | Z3: 130-148 bpm | Z4: 148-167 bpm",
               "u": ["structuring training weeks", "improving aerobic endurance (zone 2)", "preparing for races", "active recovery (zone 1)"]},
    },
    "904": {  # vo2-max
        "es": {"f": "VO2máx ≈ 15 × (FCmáx / FCreposo) (método simple)", "ei": "FCmáx 190 ppm, FCreposo 55 ppm", "eo": "VO2máx ≈ 51,8 ml/kg/min",
               "u": ["evaluar condición física aeróbica", "predecir tiempos en maratón y medios fondos", "monitorizar mejoras de entrenamiento", "valoración clínica de capacidad cardiorrespiratoria"]},
        "en": {"f": "VO2max ≈ 15 × (Max HR / Resting HR) (simple method)", "ei": "Max HR 190 bpm, Resting HR 55 bpm", "eo": "VO2max ≈ 51.8 ml/kg/min",
               "u": ["evaluating aerobic fitness", "predicting marathon and middle-distance times", "monitoring training improvements", "clinical cardiorespiratory assessment"]},
    },
    "905": {  # pasos-calorias
        "es": {"f": "Calorías ≈ Pasos × 0,04 kcal/paso (varía por peso y zancada)", "ei": "10.000 pasos, peso 70 kg", "eo": "Calorías quemadas ≈ 350-500 kcal",
               "u": ["seguimiento con podómetro o smartwatch", "reto de los 10.000 pasos", "pérdida de peso por actividad diaria", "sedentarismo y salud metabólica"]},
        "en": {"f": "Calories ≈ Steps × 0.04 kcal/step (varies by weight and stride)", "ei": "10,000 steps, weight 70 kg", "eo": "Calories burned ≈ 350-500 kcal",
               "u": ["pedometer or smartwatch tracking", "10,000 steps challenge", "weight loss through daily activity", "sedentarism and metabolic health"]},
    },
    "906": {  # ritmo-natacion
        "es": {"f": "Ritmo natación (min/100m) = Tiempo total (min) / Distancia (100m)", "ei": "800 m en 16 minutos", "eo": "Ritmo = 2:00 min/100m",
               "u": ["planificación de entrenamientos en piscina", "estimación de tiempos en triatlón", "comparar progresión de nadadores", "series de velocidad en natación"]},
        "en": {"f": "Swimming pace (min/100m) = Total time (min) / Distance (100m)", "ei": "800 m in 16 minutes", "eo": "Pace = 2:00 min/100m",
               "u": ["pool training session planning", "triathlon time estimation", "swimmer progression comparison", "swimming speed intervals"]},
    },
    "907": {  # ritmo-ciclismo
        "es": {"f": "Velocidad media (km/h) = Distancia (km) / Tiempo (h)", "ei": "60 km en 2 h 15 min", "eo": "Velocidad media = 26,7 km/h",
               "u": ["estimación de tiempos en cicloturismo", "planificar rutas por montaña", "comparar prestaciones de bicicletas", "entrenamiento por potencia (vatios)"]},
        "en": {"f": "Average speed (km/h) = Distance (km) / Time (h)", "ei": "60 km in 2 h 15 min", "eo": "Average speed = 26.7 km/h",
               "u": ["cycle touring time estimation", "mountain route planning", "bicycle performance comparison", "power-based training (watts)"]},
    },
    "908": {  # imc-deportista
        "es": {"f": "IMC = Peso (kg) / Altura² (m) — en deportistas, ajustar por composición corporal", "ei": "Jugador de rugby: 100 kg, 1,85 m", "eo": "IMC = 29,2 (sobrepeso por fórmula, pero ≈ 12 % grasa)",
               "u": ["evaluar composición corporal en atletas", "deportes de contacto (categorías por peso)", "nutrición deportiva de alta competición", "seguimiento de cambios en temporada"]},
        "en": {"f": "BMI = Weight (kg) / Height² (m) — in athletes, adjust for body composition", "ei": "Rugby player: 100 kg, 1.85 m", "eo": "BMI = 29.2 (overweight by formula, but ≈ 12% body fat)",
               "u": ["body composition assessment in athletes", "contact sports (weight categories)", "elite sports nutrition", "in-season body change tracking"]},
    },
    "909": {  # tiempo-pista
        "es": {"f": "Tiempo en pista = Distancia / Velocidad | Vuelta = Longitud circuito / Velocidad", "ei": "Circuito de 4.000 m, velocidad media 140 km/h", "eo": "Tiempo por vuelta = 1 min 42,9 s",
               "u": ["simulación de tiempos en karting", "planificación de estrategias de pit stop", "comparar rendimientos de vehículos en circuito", "análisis de telemetría deportiva"]},
        "en": {"f": "Track time = Distance / Speed | Lap time = Circuit length / Speed", "ei": "4,000 m circuit, average speed 140 km/h", "eo": "Lap time = 1 min 42.9 s",
               "u": ["karting lap time simulation", "pit stop strategy planning", "comparing vehicle performance on track", "sports telemetry analysis"]},
    },
}


def build_article_from_facts(facts: dict, lang: str) -> str:
    """Generate a unique 4-section SEO article from compact CALC_FACTS data."""
    d = facts.get(lang) or facts.get("en")
    if not d:
        return ""
    H = {
        "es": ("La fórmula", "Ejemplo paso a paso", "¿Para qué sirve?", "Consejos prácticos"),
        "en": ("The formula", "Step-by-step example", "What is it used for?", "Practical tips"),
        "fr": ("La formule", "Exemple pas à pas", "À quoi ça sert ?", "Conseils pratiques"),
        "pt": ("A fórmula", "Exemplo passo a passo", "Para que serve?", "Dicas práticas"),
        "de": ("Die Formel", "Schritt-für-Schritt-Beispiel", "Wofür wird es verwendet?", "Praktische Tipps"),
        "it": ("La formula", "Esempio passo dopo passo", "A cosa serve?", "Consigli pratici"),
    }
    tips = {
        "es": "Comprueba siempre las unidades antes de calcular. Un error de unidades puede dar resultados incorrectos.",
        "en": "Always check units before calculating. A unit mismatch can produce incorrect results.",
        "fr": "Vérifiez toujours les unités avant de calculer. Une erreur d'unité peut produire des résultats incorrects.",
        "pt": "Verifique sempre as unidades antes de calcular. Um erro de unidade pode produzir resultados incorretos.",
        "de": "Überprüfen Sie vor dem Rechnen immer die Einheiten. Ein Einheitenfehler kann zu falschen Ergebnissen führen.",
        "it": "Controlla sempre le unità prima di calcolare. Un errore di unità può produrre risultati errati.",
    }
    h = H.get(lang, H["en"])
    tip = tips.get(lang, tips["en"])
    uses_html = "".join(f"<li>{u}</li>" for u in d["u"])
    return f"""<section class="long-content">
<h2>{h[0]}</h2>
<p><strong>{d["f"]}</strong></p>
<h2>{h[1]}</h2>
<p><strong>Input:</strong> {d["ei"]}</p>
<p><strong>Result:</strong> {d["eo"]}</p>
<h2>{h[2]}</h2>
<ul>{uses_html}</ul>
<h2>{h[3]}</h2>
<p>{tip}</p>
</section>"""


def generate_long_content(calc_id: str, lang: str) -> str:
    """Return long-form SEO article for a calculator, or empty string if none."""
    entry = LONG_CONTENT.get(calc_id, {})
    result = entry.get(lang, entry.get("en", ""))
    if result:
        return result
    facts = CALC_FACTS.get(calc_id, {})
    if facts:
        return build_article_from_facts(facts, lang)
    return ""
'''

with open(TARGET, encoding="utf-8") as f:
    src = f.read()

# Remove the old generate_long_content function at the end
old_fn = '\ndef generate_long_content(calc_id: str, lang: str) -> str:\n    """Return long-form SEO article for a calculator, or empty string if none."""\n    entry = LONG_CONTENT.get(calc_id, {})\n    return entry.get(lang, entry.get("en", ""))'
if old_fn in src:
    src = src.replace(old_fn, "")
    print("Removed old generate_long_content")
else:
    print("WARNING: old generate_long_content not found exactly — appending anyway")

src = src.rstrip() + "\n" + APPEND

with open(TARGET, "w", encoding="utf-8", newline="\n") as f:
    f.write(src)

print(f"[OK] calc_content.py patched ({len(src)} chars)")

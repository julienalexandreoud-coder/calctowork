"""Patch calc_content.py: add block-aware intros + long-form content for top 20 calculators."""
from pathlib import Path

OBRA = Path(__file__).parent.parent

# ── 1. Update generate_intro in calc_content.py ────────────────────────────────
src = OBRA / "scripts" / "calc_content.py"
text = src.read_text(encoding="utf-8")

OLD_INTRO_FN = """def generate_intro(calc_id: str, lang: str, name: str, desc: str) -> str:
    tpl = INTRO_TEMPLATES.get(lang, INTRO_TEMPLATES["en"])
    return tpl.format(name=name, desc=desc)"""

NEW_INTRO_FN = """def generate_intro(calc_id: str, lang: str, name: str, desc: str, block_slug: str = "") -> str:
    block_tpls = BLOCK_INTRO_TEMPLATES.get(block_slug, {})
    tpl = block_tpls.get(lang) or INTRO_TEMPLATES.get(lang, INTRO_TEMPLATES["en"])
    return tpl.format(name=name, desc=desc)"""

text = text.replace(OLD_INTRO_FN, NEW_INTRO_FN)
assert NEW_INTRO_FN in text, "Replacement failed"

# ── 2. Append new dicts and functions ─────────────────────────────────────────
ADDITION = r'''

# ── Block-specific intro templates (non-construction categories) ──────────────

BLOCK_INTRO_TEMPLATES = {
    "matematicas": {
        "es": "La <strong>{name}</strong> es una calculadora matemática gratuita online. {desc} Obtén el resultado al instante con la fórmula detallada y ejemplos paso a paso.",
        "en": "The <strong>{name}</strong> is a free online math calculator. {desc} Get instant results with the detailed formula and step-by-step examples.",
        "fr": "Le <strong>{name}</strong> est une calculatrice mathématique gratuite. {desc} Résultat instantané avec formule et exemples détaillés.",
        "pt": "A <strong>{name}</strong> é uma calculadora matemática gratuita online. {desc} Resultado instantâneo com fórmula detalhada e exemplos passo a passo.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Online-Mathematikrechner. {desc} Sofortiges Ergebnis mit Formel und Beispielen.",
        "it": "Il <strong>{name}</strong> è una calcolatrice matematica gratuita. {desc} Risultato immediato con formula dettagliata ed esempi.",
    },
    "finanzas": {
        "es": "La <strong>{name}</strong> es una calculadora financiera gratuita. {desc} Planifica tus finanzas personales con precisión y toma mejores decisiones económicas.",
        "en": "The <strong>{name}</strong> is a free financial calculator. {desc} Plan your finances accurately and make better economic decisions.",
        "fr": "Le <strong>{name}</strong> est une calculatrice financière gratuite. {desc} Planifiez vos finances personnelles avec précision.",
        "pt": "A <strong>{name}</strong> é uma calculadora financeira gratuita. {desc} Planeje suas finanças com precisão e tome melhores decisões.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Finanzrechner. {desc} Planen Sie Ihre Finanzen genau.",
        "it": "Il <strong>{name}</strong> è una calcolatrice finanziaria gratuita. {desc} Pianifica le tue finanze con precisione.",
    },
    "salud": {
        "es": "La <strong>{name}</strong> es una calculadora de salud gratuita. {desc} Obtén una estimación basada en evidencia científica para mejorar tu bienestar.",
        "en": "The <strong>{name}</strong> is a free health calculator. {desc} Get evidence-based estimates to improve your wellbeing.",
        "fr": "Le <strong>{name}</strong> est une calculatrice santé gratuite. {desc} Estimations basées sur des preuves scientifiques.",
        "pt": "A <strong>{name}</strong> é uma calculadora de saúde gratuita. {desc} Estimativas baseadas em evidências científicas.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Gesundheitsrechner. {desc} Wissenschaftlich fundierte Schätzungen.",
        "it": "Il <strong>{name}</strong> è una calcolatrice per la salute gratuita. {desc} Stime basate su prove scientifiche.",
    },
    "cotidiano": {
        "es": "La <strong>{name}</strong> es una calculadora práctica gratuita para el día a día. {desc} Resultado instantáneo para facilitar tus cálculos cotidianos.",
        "en": "The <strong>{name}</strong> is a free everyday calculator. {desc} Instant results to simplify your daily calculations.",
        "fr": "Le <strong>{name}</strong> est une calculatrice quotidienne gratuite. {desc} Résultat instantané pour simplifier vos calculs.",
        "pt": "A <strong>{name}</strong> é uma calculadora prática gratuita. {desc} Resultado instantâneo para facilitar seus cálculos do dia a dia.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Alltagsrechner. {desc} Sofortige Ergebnisse für alltägliche Berechnungen.",
        "it": "Il <strong>{name}</strong> è una calcolatrice pratica gratuita. {desc} Risultato immediato per i calcoli quotidiani.",
    },
    "estadistica": {
        "es": "La <strong>{name}</strong> es una calculadora de estadística gratuita. {desc} Analiza tus datos al instante con fórmulas estadísticas precisas.",
        "en": "The <strong>{name}</strong> is a free statistics calculator. {desc} Analyze your data instantly with precise statistical formulas.",
        "fr": "Le <strong>{name}</strong> est une calculatrice statistique gratuite. {desc} Analysez vos données instantanément.",
        "pt": "A <strong>{name}</strong> é uma calculadora de estatística gratuita. {desc} Analise seus dados instantaneamente.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Statistikrechner. {desc} Analysieren Sie Ihre Daten sofort.",
        "it": "Il <strong>{name}</strong> è una calcolatrice statistica gratuita. {desc} Analizza i tuoi dati istantaneamente.",
    },
    "ciencia": {
        "es": "La <strong>{name}</strong> es una calculadora científica gratuita. {desc} Resuelve problemas de física y ciencias con fórmulas exactas.",
        "en": "The <strong>{name}</strong> is a free science calculator. {desc} Solve physics and science problems with exact formulas.",
        "fr": "Le <strong>{name}</strong> est une calculatrice scientifique gratuite. {desc} Résolvez des problèmes de physique avec des formules exactes.",
        "pt": "A <strong>{name}</strong> é uma calculadora científica gratuita. {desc} Resolva problemas de física com fórmulas exatas.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Wissenschaftsrechner. {desc} Lösen Sie Physikprobleme mit exakten Formeln.",
        "it": "Il <strong>{name}</strong> è una calcolatrice scientifica gratuita. {desc} Risolvi problemi di fisica con formule esatte.",
    },
    "conversion": {
        "es": "El <strong>{name}</strong> es un conversor de unidades gratuito. {desc} Convierte unidades al instante con resultados precisos en todas las escalas.",
        "en": "The <strong>{name}</strong> is a free unit converter. {desc} Convert units instantly with accurate results across all scales.",
        "fr": "Le <strong>{name}</strong> est un convertisseur d'unités gratuit. {desc} Convertissez des unités instantanément.",
        "pt": "O <strong>{name}</strong> é um conversor de unidades gratuito. {desc} Converta unidades instantaneamente.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Einheitenumrechner. {desc} Einheiten sofort und präzise umrechnen.",
        "it": "Il <strong>{name}</strong> è un convertitore di unità gratuito. {desc} Converti le unità istantaneamente.",
    },
    "deportes": {
        "es": "La <strong>{name}</strong> es una calculadora deportiva gratuita. {desc} Optimiza tu entrenamiento con datos precisos basados en ciencia del deporte.",
        "en": "The <strong>{name}</strong> is a free sports calculator. {desc} Optimize your training with accurate data based on sport science.",
        "fr": "Le <strong>{name}</strong> est une calculatrice sportive gratuite. {desc} Optimisez votre entraînement avec des données précises.",
        "pt": "A <strong>{name}</strong> é uma calculadora esportiva gratuita. {desc} Otimize seu treino com dados precisos baseados na ciência do esporte.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Sportrechner. {desc} Trainieren Sie mit präzisen sportwissenschaftlichen Daten.",
        "it": "Il <strong>{name}</strong> è una calcolatrice sportiva gratuita. {desc} Ottimizza il tuo allenamento con dati scientifici precisi.",
    },
}


# ── Per-calculator long-form SEO content ────────────────────────────────────────

LONG_CONTENT = {

    # ── MATEMATICAS ──────────────────────────────────────────────────────────────

    "200": {  # porcentaje
        "es": """<section class="long-content">
<h2>¿Qué es la calculadora de porcentaje?</h2>
<p>La <strong>calculadora de porcentaje</strong> resuelve al instante los tres problemas porcentuales más comunes: hallar qué porcentaje representa un número respecto a otro, calcular el valor de un porcentaje sobre una cantidad, o encontrar el total cuando conoces una parte y su porcentaje. Es la operación matemática más utilizada en la vida diaria: descuentos, impuestos, propinas, estadísticas, subidas salariales y análisis financieros.</p>

<h2>Fórmula del porcentaje</h2>
<p>Existen tres variantes según lo que quieras calcular:</p>
<ul>
  <li><strong>¿Qué % es A de B?</strong> → Porcentaje = (A ÷ B) × 100</li>
  <li><strong>¿Cuánto es el X% de B?</strong> → Valor = (X × B) ÷ 100</li>
  <li><strong>A es el X% de ¿qué total?</strong> → Total = A × 100 ÷ X</li>
</ul>

<h2>Ejemplo práctico paso a paso</h2>
<p><strong>Ejemplo 1 – Descuento en compra:</strong> Un televisor cuesta 650 € con un 30 % de descuento.</p>
<ol>
  <li>Importe del descuento: (30 × 650) ÷ 100 = <strong>195 €</strong></li>
  <li>Precio final: 650 − 195 = <strong>455 €</strong></li>
</ol>
<p><strong>Ejemplo 2 – Subida de precio:</strong> Tu factura eléctrica sube de 80 € a 96 €. ¿Qué % de aumento?</p>
<ol>
  <li>Diferencia: 96 − 80 = 16 €</li>
  <li>Porcentaje de aumento: (16 ÷ 80) × 100 = <strong>20 %</strong></li>
</ol>

<h2>Usos frecuentes de la calculadora de porcentaje</h2>
<ul>
  <li><strong>Compras con descuento:</strong> Black Friday, rebajas y cupones de oferta.</li>
  <li><strong>IVA e impuestos:</strong> Calcular el precio final con IVA o el precio sin impuestos.</li>
  <li><strong>Finanzas personales:</strong> Determinar qué % de tus ingresos destinas al ahorro o gastos.</li>
  <li><strong>Notas académicas:</strong> Convertir aciertos en puntuación porcentual.</li>
  <li><strong>Propinas:</strong> Calcular el 10 %, 15 % o 20 % de una cuenta de restaurante.</li>
  <li><strong>Intereses bancarios:</strong> Conocer cuánto crece una inversión con una tasa anual.</li>
</ul>

<h2>Errores comunes al calcular porcentajes</h2>
<ul>
  <li><strong>"El X% de" ≠ "el X%":</strong> Un 10 % más sobre 100 € son 110 €, no solo 10 €.</li>
  <li><strong>Orden del cociente:</strong> Para saber qué % es 20 de 80, divides 20 ÷ 80 (no al revés).</li>
  <li><strong>Descuentos acumulados:</strong> Un 20 % de descuento más un 10 % adicional no son el 30 %; son el 28 %.</li>
  <li><strong>Olvidar multiplicar por 100:</strong> A ÷ B da un decimal; multiplica por 100 para obtener el porcentaje.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is a percentage calculator?</h2>
<p>The <strong>percentage calculator</strong> instantly solves the three most common percentage problems: finding what percent one number is of another, calculating the value of a percentage of a number, or finding the whole when you know the part and its percentage. It's the most-used math operation in everyday life: discounts, taxes, tips, statistics, salary increases, and financial analysis.</p>

<h2>Percentage formulas</h2>
<ul>
  <li><strong>What % is A of B?</strong> → Percentage = (A ÷ B) × 100</li>
  <li><strong>What is X% of B?</strong> → Value = (X × B) ÷ 100</li>
  <li><strong>A is X% of what total?</strong> → Total = A × 100 ÷ X</li>
</ul>

<h2>Step-by-step examples</h2>
<p><strong>Example 1 – Shopping discount:</strong> A TV costs $650 with a 30% discount.</p>
<ol>
  <li>Discount amount: (30 × 650) ÷ 100 = <strong>$195</strong></li>
  <li>Final price: 650 − 195 = <strong>$455</strong></li>
</ol>
<p><strong>Example 2 – Price increase:</strong> Your electricity bill goes from $80 to $96. What % increase?</p>
<ol>
  <li>Difference: 96 − 80 = $16</li>
  <li>Percentage increase: (16 ÷ 80) × 100 = <strong>20%</strong></li>
</ol>

<h2>Common uses</h2>
<ul>
  <li><strong>Discounts:</strong> Black Friday, sales, and coupon codes.</li>
  <li><strong>Tax calculations:</strong> Find the price with or without VAT/sales tax.</li>
  <li><strong>Personal finance:</strong> What % of income goes to savings or expenses.</li>
  <li><strong>Grade conversions:</strong> Turn correct answers into a percentage score.</li>
  <li><strong>Tips:</strong> Calculate 10%, 15%, or 20% of a restaurant bill.</li>
</ul>

<h2>Common mistakes to avoid</h2>
<ul>
  <li><strong>"10% more" ≠ "10%":</strong> 10% more than $100 is $110, not just $10.</li>
  <li><strong>Wrong division order:</strong> To find what % 20 is of 80, divide 20 ÷ 80, not 80 ÷ 20.</li>
  <li><strong>Stacking discounts:</strong> 20% off then 10% off is a 28% total discount, not 30%.</li>
</ul>
</section>""",
    },

    "201": {  # cambio-porcentual
        "es": """<section class="long-content">
<h2>¿Qué es el cambio porcentual?</h2>
<p>El <strong>cambio porcentual</strong> (o variación porcentual) mide cuánto ha aumentado o disminuido una cantidad en relación a su valor original. Se expresa en porcentaje y se usa para comparar precios, estadísticas, resultados financieros y cualquier magnitud que cambia con el tiempo. Un valor positivo indica aumento; un valor negativo indica disminución.</p>

<h2>Fórmula del cambio porcentual</h2>
<p><strong>Cambio % = ((Valor nuevo − Valor original) ÷ Valor original) × 100</strong></p>
<p>Si el resultado es positivo, hubo un aumento. Si es negativo, hubo una reducción.</p>

<h2>Ejemplo práctico</h2>
<p><strong>Ejemplo 1 – Subida de precio:</strong> Un piso valía 180.000 € y ahora vale 220.000 €.</p>
<ol>
  <li>Diferencia: 220.000 − 180.000 = 40.000 €</li>
  <li>Cambio %: (40.000 ÷ 180.000) × 100 = <strong>+22,2 %</strong></li>
</ol>
<p><strong>Ejemplo 2 – Caída en bolsa:</strong> Una acción pasa de 50 € a 38 €.</p>
<ol>
  <li>Diferencia: 38 − 50 = −12 €</li>
  <li>Cambio %: (−12 ÷ 50) × 100 = <strong>−24 %</strong></li>
</ol>

<h2>Diferencia entre cambio porcentual y diferencia absoluta</h2>
<p>La diferencia absoluta solo dice cuánto cambió la cifra (ej. 40.000 €). El cambio porcentual dice <em>cuánto supone eso en relación al valor inicial</em>, permitiendo comparar magnitudes distintas de forma justa.</p>

<h2>Usos del cambio porcentual</h2>
<ul>
  <li><strong>Finanzas:</strong> Rentabilidad de inversiones, variación del precio de acciones.</li>
  <li><strong>Economía:</strong> Inflación mensual, variación del PIB, desempleo.</li>
  <li><strong>Ventas:</strong> Comparar resultados de un trimestre a otro.</li>
  <li><strong>Ciencias:</strong> Medir el crecimiento de una población o la variación de temperatura.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is percentage change?</h2>
<p><strong>Percentage change</strong> measures how much a quantity has increased or decreased relative to its original value. A positive result means an increase; a negative result means a decrease. It's used to compare prices, financial results, statistics, and any measurable quantity that changes over time.</p>

<h2>Percentage change formula</h2>
<p><strong>Change % = ((New Value − Original Value) ÷ Original Value) × 100</strong></p>

<h2>Step-by-step examples</h2>
<p><strong>Example 1 – Price increase:</strong> An apartment was worth $180,000 and is now $220,000.</p>
<ol>
  <li>Difference: 220,000 − 180,000 = $40,000</li>
  <li>Change: (40,000 ÷ 180,000) × 100 = <strong>+22.2%</strong></li>
</ol>
<p><strong>Example 2 – Stock drop:</strong> A stock falls from $50 to $38.</p>
<ol>
  <li>Difference: 38 − 50 = −$12</li>
  <li>Change: (−12 ÷ 50) × 100 = <strong>−24%</strong></li>
</ol>

<h2>Common uses</h2>
<ul>
  <li><strong>Finance:</strong> Investment returns, stock price movements.</li>
  <li><strong>Economics:</strong> Monthly inflation, GDP growth, unemployment rate changes.</li>
  <li><strong>Business:</strong> Quarter-over-quarter sales comparison.</li>
  <li><strong>Science:</strong> Population growth, temperature variation measurement.</li>
</ul>
</section>""",
    },

    "203": {  # pitagoras
        "es": """<section class="long-content">
<h2>¿Qué es el teorema de Pitágoras?</h2>
<p>El <strong>teorema de Pitágoras</strong> establece que en todo triángulo rectángulo, el cuadrado de la hipotenusa (el lado opuesto al ángulo recto) es igual a la suma de los cuadrados de los otros dos lados, llamados catetos. Es uno de los teoremas más fundamentales de la geometría y tiene aplicaciones directas en construcción, arquitectura, topografía, ingeniería y física.</p>

<h2>Fórmula de Pitágoras</h2>
<p><strong>a² + b² = c²</strong></p>
<p>Donde <em>a</em> y <em>b</em> son los catetos y <em>c</em> es la hipotenusa. Si buscas un cateto: <strong>a = √(c² − b²)</strong></p>

<h2>Ejemplo práctico paso a paso</h2>
<p><strong>Situación:</strong> Quieres saber si una esquina de obra está perfectamente a 90°. El cateto horizontal mide 3 m y el vertical 4 m. ¿Cuánto debería medir la diagonal?</p>
<ol>
  <li>c² = 3² + 4² = 9 + 16 = 25</li>
  <li>c = √25 = <strong>5 m</strong></li>
</ol>
<p>Esta es la famosa "terna pitagórica" 3-4-5, muy usada en construcción para verificar ángulos rectos.</p>

<h2>¿Para qué sirve la calculadora de Pitágoras?</h2>
<ul>
  <li><strong>Construcción:</strong> Verificar escuadras y ángulos rectos en obra.</li>
  <li><strong>Geometría:</strong> Calcular diagonales de rectángulos, alturas de triángulos.</li>
  <li><strong>Navegación:</strong> Distancias en mapas con coordenadas cartesianas.</li>
  <li><strong>Física:</strong> Composición de fuerzas y velocidades vectoriales.</li>
  <li><strong>Informática:</strong> Distancia entre dos puntos en pantalla (píxeles).</li>
</ul>

<h2>Ternas pitagóricas más comunes</h2>
<ul>
  <li>3 – 4 – 5 (y sus múltiplos: 6-8-10, 9-12-15...)</li>
  <li>5 – 12 – 13</li>
  <li>8 – 15 – 17</li>
  <li>7 – 24 – 25</li>
</ul>
<p>En la vida real el cateto y la hipotenusa raramente son números enteros, pero la calculadora devuelve el resultado exacto en cualquier caso.</p>
</section>""",
        "en": """<section class="long-content">
<h2>What is the Pythagorean theorem?</h2>
<p>The <strong>Pythagorean theorem</strong> states that in a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides (legs). It's one of the most fundamental theorems in geometry, with direct applications in construction, architecture, surveying, engineering, and physics.</p>

<h2>Pythagorean theorem formula</h2>
<p><strong>a² + b² = c²</strong></p>
<p>Where <em>a</em> and <em>b</em> are the legs and <em>c</em> is the hypotenuse. To find a missing leg: <strong>a = √(c² − b²)</strong></p>

<h2>Step-by-step example</h2>
<p><strong>Situation:</strong> You want to verify a 90° corner. The horizontal leg is 3 m, the vertical leg is 4 m. What should the diagonal measure?</p>
<ol>
  <li>c² = 3² + 4² = 9 + 16 = 25</li>
  <li>c = √25 = <strong>5 m</strong></li>
</ol>
<p>This is the famous 3-4-5 Pythagorean triple, widely used in construction to check right angles.</p>

<h2>Common uses</h2>
<ul>
  <li><strong>Construction:</strong> Checking right angles and squares on site.</li>
  <li><strong>Geometry:</strong> Finding diagonals of rectangles, triangle heights.</li>
  <li><strong>Navigation:</strong> Distances using Cartesian map coordinates.</li>
  <li><strong>Physics:</strong> Vector force and velocity composition.</li>
  <li><strong>Computer graphics:</strong> Distance between two points on screen.</li>
</ul>
</section>""",
    },

    "210": {  # area-circulo
        "es": """<section class="long-content">
<h2>¿Cómo calcular el área de un círculo?</h2>
<p>El <strong>área de un círculo</strong> es la superficie encerrada dentro de la circunferencia. Para calcularla necesitas el radio (distancia del centro al borde) o el diámetro (dos veces el radio). Esta calculadora te devuelve el área, el perímetro (circunferencia) y el diámetro al instante.</p>

<h2>Fórmula del área del círculo</h2>
<p><strong>Área = π × r²</strong></p>
<p>Donde <em>r</em> es el radio y π ≈ 3.14159265... Si solo tienes el diámetro: <strong>Área = π × (d ÷ 2)²</strong></p>
<p>La circunferencia (perímetro) se calcula como: <strong>C = 2 × π × r</strong></p>

<h2>Ejemplo práctico</h2>
<p><strong>Quieres instalar una piscina circular de 4 m de diámetro.</strong></p>
<ol>
  <li>Radio: 4 ÷ 2 = 2 m</li>
  <li>Área: π × 2² = 3.14159 × 4 ≈ <strong>12.57 m²</strong></li>
  <li>Circunferencia: 2 × π × 2 ≈ <strong>12.57 m</strong> (perímetro del borde)</li>
</ol>

<h2>Aplicaciones del área del círculo</h2>
<ul>
  <li><strong>Construcción:</strong> Calcular m² de una losa o base circular.</li>
  <li><strong>Jardinería:</strong> Superficie de un macizo o estanque circular.</li>
  <li><strong>Ingeniería:</strong> Sección transversal de tuberías y columnas.</li>
  <li><strong>Matemáticas:</strong> Problemas de geometría en secundaria y bachillerato.</li>
  <li><strong>Diseño gráfico:</strong> Calcular proporciones de elementos circulares.</li>
</ul>

<h2>¿Por qué π (pi)?</h2>
<p>Pi (π) es la relación constante entre la circunferencia de cualquier círculo y su diámetro. Su valor es aproximadamente 3.14159265, aunque es un número irracional con infinitos decimales sin patrón. Para cálculos prácticos basta con usar 3.1416.</p>
</section>""",
        "en": """<section class="long-content">
<h2>How to calculate the area of a circle</h2>
<p>The <strong>area of a circle</strong> is the surface enclosed within the circumference. You need the radius (center to edge) or the diameter (twice the radius). This calculator returns the area, circumference, and diameter instantly.</p>

<h2>Circle area formula</h2>
<p><strong>Area = π × r²</strong></p>
<p>Where <em>r</em> is the radius and π ≈ 3.14159. If you only have the diameter: <strong>Area = π × (d ÷ 2)²</strong></p>
<p>Circumference: <strong>C = 2 × π × r</strong></p>

<h2>Practical example</h2>
<p><strong>Installing a circular pool with a 4 m diameter:</strong></p>
<ol>
  <li>Radius: 4 ÷ 2 = 2 m</li>
  <li>Area: π × 2² ≈ <strong>12.57 m²</strong></li>
  <li>Circumference: 2 × π × 2 ≈ <strong>12.57 m</strong></li>
</ol>

<h2>Applications</h2>
<ul>
  <li><strong>Construction:</strong> Area of circular slabs or foundations.</li>
  <li><strong>Gardening:</strong> Surface of circular flowerbeds or ponds.</li>
  <li><strong>Engineering:</strong> Cross-section of pipes and columns.</li>
  <li><strong>Math:</strong> Geometry problems in school and university.</li>
</ul>
</section>""",
    },

    # ── FINANZAS ─────────────────────────────────────────────────────────────────

    "300": {  # hipoteca
        "es": """<section class="long-content">
<h2>¿Qué es la calculadora de hipoteca?</h2>
<p>La <strong>calculadora de hipoteca</strong> te permite conocer de antemano la cuota mensual que pagarás, el total de intereses acumulados durante toda la vida del préstamo y el importe total a devolver. Es indispensable antes de firmar cualquier hipoteca para comparar ofertas de diferentes bancos y entender el coste real del crédito hipotecario.</p>

<h2>Fórmula de la cuota hipotecaria</h2>
<p>Las hipotecas de tipo fijo usan la fórmula de amortización francesa:</p>
<p><strong>Cuota = P × [r(1+r)^n] ÷ [(1+r)^n − 1]</strong></p>
<ul>
  <li><strong>P</strong> = Capital prestado (precio de la vivienda menos la entrada)</li>
  <li><strong>r</strong> = Tipo de interés mensual (TAE anual ÷ 12)</li>
  <li><strong>n</strong> = Número total de cuotas (años × 12)</li>
</ul>

<h2>Ejemplo práctico paso a paso</h2>
<p><strong>Vivienda de 300.000 € con entrada del 20 %, interés del 3,5 % anual a 30 años.</strong></p>
<ol>
  <li>Capital prestado: 300.000 × 0,80 = <strong>240.000 €</strong></li>
  <li>Tipo mensual: 3,5 % ÷ 12 = 0,2917 % = 0,002917</li>
  <li>Número de cuotas: 30 × 12 = 360</li>
  <li>Cuota mensual: ≈ <strong>1.078 €/mes</strong></li>
  <li>Total pagado: 1.078 × 360 = <strong>388.080 €</strong></li>
  <li>Total intereses: 388.080 − 240.000 = <strong>148.080 €</strong></li>
</ol>

<h2>¿Qué factores afectan la cuota hipotecaria?</h2>
<ul>
  <li><strong>Capital prestado:</strong> Cuanto mayor sea el préstamo, mayor la cuota.</li>
  <li><strong>Tipo de interés:</strong> Un punto más de interés puede suponer cientos de euros más al mes.</li>
  <li><strong>Plazo:</strong> Ampliar el plazo reduce la cuota mensual pero dispara los intereses totales.</li>
  <li><strong>Entrada:</strong> Dar más entrada (20–30 %) reduce el capital y mejora las condiciones del banco.</li>
</ul>

<h2>Hipoteca fija vs variable</h2>
<ul>
  <li><strong>Tipo fijo:</strong> La cuota nunca cambia. Mayor seguridad, tipo inicial algo más alto.</li>
  <li><strong>Tipo variable (Euríbor + diferencial):</strong> Cuota puede subir o bajar. Suele empezar más bajo pero asumes el riesgo de subidas del Euríbor.</li>
  <li><strong>Tipo mixto:</strong> Fijo los primeros 5-10 años, variable después.</li>
</ul>

<h2>Consejos para reducir el coste de tu hipoteca</h2>
<ul>
  <li>Compara al menos 3-5 bancos antes de firmar.</li>
  <li>Negocia el diferencial sobre el Euríbor y las comisiones.</li>
  <li>Amortiza anticipadamente cuando puedas: reduce capital e intereses.</li>
  <li>Analiza si te conviene subrogarte a otra entidad si los tipos bajan.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is a mortgage calculator?</h2>
<p>The <strong>mortgage calculator</strong> lets you know in advance your monthly payment, total interest paid over the loan's life, and the total repayment amount. It's essential before signing any mortgage to compare bank offers and understand the real cost of your home loan.</p>

<h2>Mortgage payment formula</h2>
<p>Fixed-rate mortgages use the French amortization formula:</p>
<p><strong>Payment = P × [r(1+r)^n] ÷ [(1+r)^n − 1]</strong></p>
<ul>
  <li><strong>P</strong> = Loan principal (home price minus down payment)</li>
  <li><strong>r</strong> = Monthly interest rate (annual rate ÷ 12)</li>
  <li><strong>n</strong> = Total number of payments (years × 12)</li>
</ul>

<h2>Step-by-step example</h2>
<p><strong>$300,000 home, 20% down, 3.5% annual rate, 30 years.</strong></p>
<ol>
  <li>Principal: $300,000 × 0.80 = <strong>$240,000</strong></li>
  <li>Monthly rate: 3.5% ÷ 12 = 0.2917% = 0.002917</li>
  <li>Number of payments: 30 × 12 = 360</li>
  <li>Monthly payment: ≈ <strong>$1,078/month</strong></li>
  <li>Total paid: $1,078 × 360 = <strong>$388,080</strong></li>
  <li>Total interest: $388,080 − $240,000 = <strong>$148,080</strong></li>
</ol>

<h2>Factors affecting your mortgage payment</h2>
<ul>
  <li><strong>Loan amount:</strong> Higher principal means higher payments.</li>
  <li><strong>Interest rate:</strong> One percentage point more can add hundreds per month.</li>
  <li><strong>Term:</strong> Longer terms reduce monthly payments but increase total interest.</li>
  <li><strong>Down payment:</strong> More down (20–30%) reduces the loan and improves bank terms.</li>
</ul>

<h2>Tips to reduce your mortgage cost</h2>
<ul>
  <li>Compare at least 3–5 lenders before signing.</li>
  <li>Negotiate origination fees and the interest rate margin.</li>
  <li>Make extra payments when possible to reduce principal and interest.</li>
</ul>
</section>""",
    },

    "301": {  # prestamo
        "es": """<section class="long-content">
<h2>¿Qué calcula la calculadora de préstamo?</h2>
<p>La <strong>calculadora de préstamo personal</strong> te muestra la cuota mensual exacta que pagarás, el total de intereses y el coste total del crédito. Con esta información puedes comparar diferentes importes, plazos y tasas de interés para elegir el préstamo más conveniente y planificar tu presupuesto mensual con precisión.</p>

<h2>Fórmula de la cuota del préstamo</h2>
<p><strong>Cuota = C × [r(1+r)^n] ÷ [(1+r)^n − 1]</strong></p>
<ul>
  <li><strong>C</strong> = Capital del préstamo</li>
  <li><strong>r</strong> = Tipo de interés mensual (TIN anual ÷ 12)</li>
  <li><strong>n</strong> = Número de cuotas (meses)</li>
</ul>

<h2>Ejemplo práctico</h2>
<p><strong>Préstamo de 10.000 € al 6 % anual a 3 años (36 meses).</strong></p>
<ol>
  <li>Tipo mensual: 6 % ÷ 12 = 0,5 % = 0,005</li>
  <li>Cuota mensual: ≈ <strong>304 €/mes</strong></li>
  <li>Total pagado: 304 × 36 = <strong>10.944 €</strong></li>
  <li>Total intereses: 10.944 − 10.000 = <strong>944 €</strong></li>
</ol>

<h2>Tipos de préstamos personales</h2>
<ul>
  <li><strong>Préstamo personal:</strong> Para compras, reformas, viajes u otras necesidades.</li>
  <li><strong>Crédito al consumo:</strong> Para bienes de consumo como electrodomésticos o vehículos.</li>
  <li><strong>Préstamo automotriz:</strong> Específico para la compra de coche, con el propio vehículo como garantía.</li>
  <li><strong>Reunificación de deudas:</strong> Unifica varios préstamos en uno con menor cuota mensual.</li>
</ul>

<h2>¿Cómo reducir el coste de un préstamo?</h2>
<ul>
  <li>Negocia el tipo de interés: una pequeña diferencia en el TIN impacta mucho en el total.</li>
  <li>Reduce el plazo si puedes: menos tiempo = menos intereses totales.</li>
  <li>Amortiza anticipadamente: muchos préstamos permiten pagos extra sin comisión.</li>
  <li>Compara la TAE (no solo el TIN) para tener el coste real incluyendo comisiones.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What does a loan calculator tell you?</h2>
<p>The <strong>loan calculator</strong> shows your exact monthly payment, total interest paid, and total loan cost. With this information you can compare different amounts, terms, and interest rates to choose the best loan and accurately plan your monthly budget.</p>

<h2>Loan payment formula</h2>
<p><strong>Payment = P × [r(1+r)^n] ÷ [(1+r)^n − 1]</strong></p>
<ul>
  <li><strong>P</strong> = Loan principal</li>
  <li><strong>r</strong> = Monthly interest rate (annual rate ÷ 12)</li>
  <li><strong>n</strong> = Number of monthly payments</li>
</ul>

<h2>Practical example</h2>
<p><strong>$10,000 loan at 6% annual rate over 3 years (36 months).</strong></p>
<ol>
  <li>Monthly rate: 6% ÷ 12 = 0.5% = 0.005</li>
  <li>Monthly payment: ≈ <strong>$304/month</strong></li>
  <li>Total paid: $304 × 36 = <strong>$10,944</strong></li>
  <li>Total interest: $10,944 − $10,000 = <strong>$944</strong></li>
</ol>

<h2>Tips to reduce loan cost</h2>
<ul>
  <li>Compare APR (not just nominal rate) for the true cost including fees.</li>
  <li>Shorten the term if you can: less time = less total interest.</li>
  <li>Make extra payments to reduce principal and cut future interest.</li>
  <li>Check for prepayment penalties before paying ahead of schedule.</li>
</ul>
</section>""",
    },

    "302": {  # interes-compuesto
        "es": """<section class="long-content">
<h2>¿Qué es el interés compuesto?</h2>
<p>El <strong>interés compuesto</strong> es el mecanismo por el que los intereses generados se suman al capital inicial y, a su vez, generan nuevos intereses en el siguiente período. Es el principio financiero más poderoso del mundo: con el tiempo, hace que el dinero crezca de forma exponencial, no lineal. Albert Einstein lo llamó "la octava maravilla del mundo".</p>

<h2>Fórmula del interés compuesto</h2>
<p><strong>Monto final = P × (1 + r/n)^(n×t)</strong></p>
<ul>
  <li><strong>P</strong> = Capital inicial invertido</li>
  <li><strong>r</strong> = Tasa de interés anual (decimal: 5 % = 0,05)</li>
  <li><strong>n</strong> = Número de capitalizaciones por año (anual=1, semestral=2, mensual=12, diario=365)</li>
  <li><strong>t</strong> = Tiempo en años</li>
</ul>

<h2>Ejemplo práctico paso a paso</h2>
<p><strong>Inviertes 5.000 € al 6 % anual durante 10 años con capitalización mensual.</strong></p>
<ol>
  <li>r/n = 0,06/12 = 0,005</li>
  <li>n×t = 12×10 = 120</li>
  <li>Monto final: 5.000 × (1 + 0,005)^120 = 5.000 × 1,8194 = <strong>9.097 €</strong></li>
  <li>Intereses ganados: 9.097 − 5.000 = <strong>4.097 €</strong> (82 % de ganancia)</li>
</ol>

<h2>El poder del tiempo en el interés compuesto</h2>
<p>Si en el ejemplo anterior amplías el plazo a 30 años: el mismo capital de 5.000 € crece hasta <strong>30.243 €</strong> — ¡seis veces más! Esto ilustra por qué empezar a invertir pronto es la decisión financiera más importante que puedes tomar.</p>

<h2>Interés compuesto vs interés simple</h2>
<ul>
  <li><strong>Interés simple:</strong> Solo ganas interés sobre el capital inicial. Crecimiento lineal.</li>
  <li><strong>Interés compuesto:</strong> Ganas interés sobre el capital + los intereses acumulados. Crecimiento exponencial.</li>
</ul>

<h2>Aplicaciones del interés compuesto</h2>
<ul>
  <li>Cuentas de ahorro y depósitos bancarios</li>
  <li>Fondos de inversión y ETFs</li>
  <li>Planes de pensiones</li>
  <li>Amortización de préstamos e hipotecas</li>
  <li>Inflación (el interés compuesto del coste de vida)</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is compound interest?</h2>
<p><strong>Compound interest</strong> is the process by which interest earned is added to the principal, and then earns interest itself in the next period. It causes money to grow exponentially over time — not linearly. Albert Einstein reportedly called it "the eighth wonder of the world."</p>

<h2>Compound interest formula</h2>
<p><strong>Final Amount = P × (1 + r/n)^(n×t)</strong></p>
<ul>
  <li><strong>P</strong> = Initial principal</li>
  <li><strong>r</strong> = Annual interest rate (decimal: 5% = 0.05)</li>
  <li><strong>n</strong> = Compounding periods per year (annual=1, monthly=12, daily=365)</li>
  <li><strong>t</strong> = Time in years</li>
</ul>

<h2>Step-by-step example</h2>
<p><strong>Invest $5,000 at 6% annual rate for 10 years, compounded monthly.</strong></p>
<ol>
  <li>r/n = 0.06/12 = 0.005</li>
  <li>n×t = 12×10 = 120</li>
  <li>Final amount: 5,000 × (1.005)^120 = <strong>$9,097</strong></li>
  <li>Interest earned: $9,097 − $5,000 = <strong>$4,097</strong> (82% gain)</li>
</ol>

<h2>The power of time</h2>
<p>Extend the same example to 30 years: your $5,000 grows to <strong>$30,243</strong> — six times your investment. This illustrates why starting to invest early is the most important financial decision you can make.</p>

<h2>Compound vs simple interest</h2>
<ul>
  <li><strong>Simple interest:</strong> Earns interest only on principal. Linear growth.</li>
  <li><strong>Compound interest:</strong> Earns interest on principal plus accumulated interest. Exponential growth.</li>
</ul>
</section>""",
    },

    "304": {  # calculadora-iva
        "es": """<section class="long-content">
<h2>¿Qué es el IVA y cómo se calcula?</h2>
<p>El <strong>IVA (Impuesto sobre el Valor Añadido)</strong> es un impuesto indirecto que se aplica sobre el consumo de bienes y servicios. En España existen tres tipos de IVA: el tipo general del <strong>21 %</strong>, el tipo reducido del <strong>10 %</strong> y el tipo superreducido del <strong>4 %</strong>. Esta calculadora te permite convertir precios con IVA incluido a precios sin IVA, y viceversa.</p>

<h2>Fórmulas del IVA</h2>
<ul>
  <li><strong>Precio con IVA:</strong> Precio neto × (1 + tipo/100)</li>
  <li><strong>Precio sin IVA:</strong> Precio con IVA ÷ (1 + tipo/100)</li>
  <li><strong>Importe del IVA:</strong> Precio neto × (tipo/100)</li>
</ul>

<h2>Ejemplo práctico</h2>
<p><strong>Una factura indica 242 € con IVA del 21 %. ¿Cuál es la base imponible?</strong></p>
<ol>
  <li>Base imponible: 242 ÷ 1,21 = <strong>200 €</strong></li>
  <li>Importe del IVA: 242 − 200 = <strong>42 €</strong></li>
</ol>
<p><strong>Un servicio tiene una base de 500 €. ¿Cuánto pagas con IVA del 21 %?</strong></p>
<ol>
  <li>IVA: 500 × 0,21 = 105 €</li>
  <li>Total con IVA: 500 + 105 = <strong>605 €</strong></li>
</ol>

<h2>Tipos de IVA en España</h2>
<ul>
  <li><strong>21 % (tipo general):</strong> La mayoría de bienes y servicios: ropa, electrónica, hostelería, servicios profesionales.</li>
  <li><strong>10 % (tipo reducido):</strong> Alimentos en general, transporte, servicios de hostelería, viviendas nuevas.</li>
  <li><strong>4 % (tipo superreducido):</strong> Alimentos básicos (pan, leche, huevos, fruta), libros, periódicos, medicamentos.</li>
</ul>

<h2>Otros países hispanohablantes</h2>
<p>El IVA o equivalente varía según el país: México aplica el 16 % (IVA), Argentina el 21 %, Colombia el 19 %, Chile el 19 % (IVA). Ajusta el porcentaje según tu país al usar esta calculadora.</p>
</section>""",
        "en": """<section class="long-content">
<h2>What is VAT and how is it calculated?</h2>
<p><strong>VAT (Value Added Tax)</strong> is an indirect tax applied to the consumption of goods and services. Rates vary by country and product category. This calculator converts prices between VAT-inclusive and VAT-exclusive amounts instantly.</p>

<h2>VAT formulas</h2>
<ul>
  <li><strong>Price with VAT:</strong> Net price × (1 + rate/100)</li>
  <li><strong>Price without VAT:</strong> VAT-inclusive price ÷ (1 + rate/100)</li>
  <li><strong>VAT amount:</strong> Net price × (rate/100)</li>
</ul>

<h2>Practical example</h2>
<p><strong>An invoice shows £242 including 21% VAT. What is the net price?</strong></p>
<ol>
  <li>Net price: 242 ÷ 1.21 = <strong>£200</strong></li>
  <li>VAT amount: 242 − 200 = <strong>£42</strong></li>
</ol>

<h2>Common VAT rates by country</h2>
<ul>
  <li><strong>UK:</strong> 20% standard, 5% reduced, 0% zero-rated</li>
  <li><strong>EU average:</strong> 21% standard (varies by country)</li>
  <li><strong>Mexico:</strong> 16% IVA</li>
  <li><strong>Canada:</strong> 5% federal GST + provincial tax</li>
  <li><strong>Australia:</strong> 10% GST</li>
</ul>
</section>""",
    },

    "305": {  # salario-neto
        "es": """<section class="long-content">
<h2>¿Cómo calcular el salario neto en España?</h2>
<p>El <strong>salario neto</strong> es lo que realmente ingresas en tu cuenta después de que la empresa ha aplicado las retenciones del IRPF y las cotizaciones a la Seguridad Social. El salario bruto que figura en tu contrato y el neto que cobras pueden diferir considerablemente dependiendo de tu tramo de renta y situación familiar.</p>

<h2>Deducciones sobre el salario bruto</h2>
<ul>
  <li><strong>Cotización SS trabajador:</strong> ~6,35 % del salario bruto (contingencias comunes 4,7 % + desempleo 1,55 % + formación 0,1 %).</li>
  <li><strong>Retención IRPF:</strong> Variable según el tramo de renta, situación familiar y deducciones personales (entre el 2 % y el 45 % aproximadamente).</li>
</ul>

<h2>Tramos del IRPF 2024 (escala estatal)</h2>
<ul>
  <li>Hasta 12.450 €: <strong>19 %</strong></li>
  <li>12.450 – 20.200 €: <strong>24 %</strong></li>
  <li>20.200 – 35.200 €: <strong>30 %</strong></li>
  <li>35.200 – 60.000 €: <strong>37 %</strong></li>
  <li>60.000 – 300.000 €: <strong>45 %</strong></li>
  <li>Más de 300.000 €: <strong>47 %</strong></li>
</ul>
<p>Nota: Cada comunidad autónoma puede añadir su tramo autonómico.</p>

<h2>Ejemplo práctico</h2>
<p><strong>Salario bruto anual de 30.000 € (trabajador soltero sin hijos en Madrid, 2024):</strong></p>
<ol>
  <li>Cotización SS: 30.000 × 6,35 % = 1.905 €</li>
  <li>Base IRPF ≈ 30.000 − 1.905 − 2.000 (deducción gastos) = 26.095 €</li>
  <li>IRPF aproximado: ~3.800 € (varía según deducciones exactas)</li>
  <li>Salario neto anual: 30.000 − 1.905 − 3.800 ≈ <strong>24.295 €</strong></li>
  <li>Salario neto mensual (12 pagas): ≈ <strong>2.024 €/mes</strong></li>
</ol>

<h2>Cómo aumentar tu salario neto</h2>
<ul>
  <li>Solicitar retribución flexible (seguro médico, tiques restaurante): exentos de IRPF hasta ciertos límites.</li>
  <li>Deducción por maternidad/paternidad, ascendientes o personas con discapacidad a cargo.</li>
  <li>Plan de pensiones: reduce la base imponible del IRPF.</li>
  <li>Gastos deducibles como autónomo o trabajador por cuenta ajena con gastos justificados.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>How to calculate net salary</h2>
<p><strong>Net salary</strong> is what you actually receive after income tax and social security deductions are applied to your gross salary. The difference between gross and net can be significant depending on your tax bracket and personal situation.</p>

<h2>Typical deductions from gross salary</h2>
<ul>
  <li><strong>Social Security / National Insurance:</strong> Typically 6–12% depending on country.</li>
  <li><strong>Income Tax / PAYE:</strong> Progressive rate based on earnings bracket and personal allowances.</li>
  <li><strong>Pension contributions:</strong> May be deducted pre-tax, reducing taxable income.</li>
</ul>

<h2>How to increase your net salary</h2>
<ul>
  <li>Use pre-tax benefits: health insurance, commuter benefits, childcare vouchers.</li>
  <li>Maximize pension contributions (reduces taxable income).</li>
  <li>Claim all eligible deductions and tax credits.</li>
  <li>Consider salary sacrifice schemes where available.</li>
</ul>
</section>""",
    },

    # ── SALUD ────────────────────────────────────────────────────────────────────

    "400": {  # imc-bmi
        "es": """<section class="long-content">
<h2>¿Qué es el IMC (Índice de Masa Corporal)?</h2>
<p>El <strong>IMC (Índice de Masa Corporal)</strong>, también conocido como BMI por sus siglas en inglés (Body Mass Index), es un indicador numérico que relaciona el peso y la altura de una persona para estimar si su masa corporal es adecuada para su estatura. Es la herramienta de cribado más utilizada por la Organización Mundial de la Salud (OMS) para identificar el sobrepeso y la obesidad en adultos.</p>

<h2>Fórmula del IMC</h2>
<p><strong>IMC = Peso (kg) ÷ Altura² (m²)</strong></p>
<p>Ejemplo: Una persona que pesa 75 kg y mide 1,75 m tiene un IMC de 75 ÷ (1,75)² = 75 ÷ 3,0625 = <strong>24,5</strong></p>

<h2>Categorías del IMC según la OMS</h2>
<ul>
  <li><strong>Menos de 18,5:</strong> Bajo peso — puede implicar desnutrición o problemas de salud.</li>
  <li><strong>18,5 – 24,9:</strong> Peso normal — rango saludable para la mayoría de adultos.</li>
  <li><strong>25,0 – 29,9:</strong> Sobrepeso — mayor riesgo de enfermedades cardiovasculares.</li>
  <li><strong>30,0 – 34,9:</strong> Obesidad grado I — riesgo moderado.</li>
  <li><strong>35,0 – 39,9:</strong> Obesidad grado II — riesgo alto.</li>
  <li><strong>40 o más:</strong> Obesidad mórbida — riesgo muy alto de complicaciones.</li>
</ul>

<h2>Ejemplo práctico</h2>
<p>Persona de <strong>80 kg y 1,70 m</strong>:</p>
<ol>
  <li>IMC = 80 ÷ (1,70)² = 80 ÷ 2,89 = <strong>27,7</strong></li>
  <li>Categoría: <strong>Sobrepeso</strong></li>
</ol>

<h2>Limitaciones del IMC</h2>
<p>El IMC es una herramienta útil pero tiene limitaciones importantes que conviene conocer:</p>
<ul>
  <li><strong>No distingue grasa de músculo:</strong> Un atleta musculado puede tener un IMC de "sobrepeso" con muy poca grasa corporal.</li>
  <li><strong>No mide la distribución de grasa:</strong> La grasa abdominal (visceral) es más peligrosa que la subcutánea, pero el IMC no la diferencia.</li>
  <li><strong>Varía con la edad y el sexo:</strong> Los mismos valores pueden indicar diferentes riesgos en hombres y mujeres, o en personas mayores.</li>
  <li><strong>Diferentes grupos étnicos:</strong> Las personas de origen asiático suelen tener mayor riesgo cardiovascular con IMC más bajos.</li>
</ul>
<p>Para una evaluación completa de salud, consulta siempre con un médico y complementa el IMC con el perímetro de cintura y el porcentaje de grasa corporal.</p>
</section>""",
        "en": """<section class="long-content">
<h2>What is BMI (Body Mass Index)?</h2>
<p><strong>BMI (Body Mass Index)</strong> is a numerical indicator that relates weight and height to estimate whether a person's body mass is appropriate for their height. It's the most widely used screening tool by the World Health Organization (WHO) to identify overweight and obesity in adults.</p>

<h2>BMI formula</h2>
<p><strong>BMI = Weight (kg) ÷ Height² (m²)</strong></p>
<p>Example: A person weighing 75 kg and 1.75 m tall has a BMI of 75 ÷ (1.75)² = <strong>24.5</strong></p>

<h2>WHO BMI categories</h2>
<ul>
  <li><strong>Below 18.5:</strong> Underweight — possible malnutrition or health issues.</li>
  <li><strong>18.5 – 24.9:</strong> Normal weight — healthy range for most adults.</li>
  <li><strong>25.0 – 29.9:</strong> Overweight — increased risk of cardiovascular disease.</li>
  <li><strong>30.0 – 34.9:</strong> Obesity Class I — moderate risk.</li>
  <li><strong>35.0 – 39.9:</strong> Obesity Class II — high risk.</li>
  <li><strong>40+:</strong> Morbid obesity — very high risk of complications.</li>
</ul>

<h2>BMI limitations</h2>
<ul>
  <li><strong>Doesn't distinguish fat from muscle:</strong> A muscular athlete may show "overweight" BMI with very little body fat.</li>
  <li><strong>Doesn't measure fat distribution:</strong> Visceral (belly) fat is more dangerous than subcutaneous fat, but BMI doesn't differentiate.</li>
  <li><strong>Varies with age and sex:</strong> The same values carry different risks for men vs women, and for older people.</li>
</ul>
<p>For a complete health assessment, consult a doctor and complement BMI with waist circumference and body fat percentage measurements.</p>
</section>""",
    },

    "401": {  # calorias-diarias
        "es": """<section class="long-content">
<h2>¿Qué son las calorías diarias necesarias?</h2>
<p>Las <strong>calorías diarias necesarias</strong> (también llamadas TDEE, del inglés Total Daily Energy Expenditure) representan la energía total que tu cuerpo consume en un día, incluyendo el metabolismo basal y toda la actividad física. Conocer tu TDEE es fundamental para perder peso, ganar músculo o simplemente mantener tu peso actual de forma controlada.</p>

<h2>¿Cómo se calcula el gasto calórico diario?</h2>
<p>Se usa la <strong>fórmula de Mifflin-St Jeor</strong> (la más precisa según la ciencia actual) para calcular el Metabolismo Basal (MB), y luego se multiplica por el factor de actividad:</p>
<p><strong>Hombres: MB = 10 × peso(kg) + 6,25 × altura(cm) − 5 × edad + 5</strong></p>
<p><strong>Mujeres: MB = 10 × peso(kg) + 6,25 × altura(cm) − 5 × edad − 161</strong></p>

<h2>Factores de actividad (multiplicadores)</h2>
<ul>
  <li><strong>Sedentario (sin ejercicio):</strong> MB × 1,2</li>
  <li><strong>Ligero (1-3 días/semana):</strong> MB × 1,375</li>
  <li><strong>Moderado (3-5 días/semana):</strong> MB × 1,55</li>
  <li><strong>Activo (6-7 días/semana):</strong> MB × 1,725</li>
  <li><strong>Muy activo (ejercicio intenso diario):</strong> MB × 1,9</li>
</ul>

<h2>Ejemplo práctico</h2>
<p><strong>Hombre de 30 años, 75 kg, 175 cm, actividad moderada:</strong></p>
<ol>
  <li>MB = 10×75 + 6,25×175 − 5×30 + 5 = 750 + 1093,75 − 150 + 5 = <strong>1.698,75 kcal</strong></li>
  <li>TDEE = 1.698,75 × 1,55 = <strong>2.633 kcal/día</strong></li>
</ol>

<h2>¿Cómo usar el TDEE para tus objetivos?</h2>
<ul>
  <li><strong>Perder peso:</strong> Consume entre 300–500 kcal menos que tu TDEE al día. Deficit gradual = pérdida sostenible.</li>
  <li><strong>Ganar músculo:</strong> Consume 200–300 kcal más que tu TDEE. Superávit controlado para minimizar grasa.</li>
  <li><strong>Mantener peso:</strong> Consume exactamente tu TDEE.</li>
</ul>
<p><em>Nota: Este cálculo es una estimación. El metabolismo varía entre personas. Ajusta según resultados reales tras 2-3 semanas.</em></p>
</section>""",
        "en": """<section class="long-content">
<h2>What are daily calorie needs?</h2>
<p><strong>Daily calorie needs</strong> (TDEE — Total Daily Energy Expenditure) represent the total energy your body burns in a day, including basal metabolism and all physical activity. Knowing your TDEE is essential for losing weight, gaining muscle, or maintaining your current weight in a controlled way.</p>

<h2>Mifflin-St Jeor formula</h2>
<p>The most scientifically accurate formula for Basal Metabolic Rate (BMR):</p>
<p><strong>Men: BMR = 10 × weight(kg) + 6.25 × height(cm) − 5 × age + 5</strong></p>
<p><strong>Women: BMR = 10 × weight(kg) + 6.25 × height(cm) − 5 × age − 161</strong></p>

<h2>Activity multipliers</h2>
<ul>
  <li><strong>Sedentary (no exercise):</strong> BMR × 1.2</li>
  <li><strong>Light (1–3 days/week):</strong> BMR × 1.375</li>
  <li><strong>Moderate (3–5 days/week):</strong> BMR × 1.55</li>
  <li><strong>Active (6–7 days/week):</strong> BMR × 1.725</li>
  <li><strong>Very active (intense daily exercise):</strong> BMR × 1.9</li>
</ul>

<h2>Using TDEE for your goals</h2>
<ul>
  <li><strong>Lose weight:</strong> Eat 300–500 kcal below TDEE. Gradual deficit = sustainable loss.</li>
  <li><strong>Gain muscle:</strong> Eat 200–300 kcal above TDEE. Controlled surplus minimizes fat gain.</li>
  <li><strong>Maintain weight:</strong> Eat exactly your TDEE.</li>
</ul>
</section>""",
    },

    "402": {  # peso-ideal
        "es": """<section class="long-content">
<h2>¿Qué es el peso ideal?</h2>
<p>El <strong>peso ideal</strong> es un rango de peso que se considera saludable para una persona de determinada altura, edad y sexo. A diferencia del IMC, que puede sobreestimar la grasa en personas musculosas, las fórmulas de peso ideal ofrecen una referencia más personalizada. Existen varias fórmulas; las más utilizadas son Broca, Hamwi y la basada en el IMC saludable.</p>

<h2>Fórmulas del peso ideal</h2>
<ul>
  <li><strong>Fórmula de Broca:</strong> Hombres: Altura(cm) − 100; Mujeres: Altura(cm) − 105</li>
  <li><strong>Fórmula de Hamwi:</strong> Hombres: 48 kg + 2,7 kg por cada 2,5 cm por encima de 152 cm; Mujeres: 45,5 kg + 2,2 kg por cada 2,5 cm.</li>
  <li><strong>Rango IMC saludable:</strong> Peso entre IMC 18,5 y 24,9 para tu altura.</li>
</ul>

<h2>Ejemplo práctico</h2>
<p><strong>Mujer de 1,65 m de altura:</strong></p>
<ul>
  <li>Broca: 165 − 105 = <strong>60 kg</strong></li>
  <li>Rango IMC: 18,5 × 1,65² a 24,9 × 1,65² = <strong>50,3 kg a 67,8 kg</strong></li>
</ul>

<h2>Limitaciones del peso ideal</h2>
<ul>
  <li>No considera la composición corporal (músculo vs grasa).</li>
  <li>Las fórmulas se desarrollaron en poblaciones específicas y pueden no aplicarse universalmente.</li>
  <li>El peso "ideal" varía según la constitución ósea (pequeña, mediana, grande).</li>
</ul>
<p>Usa el peso ideal como una referencia orientativa, no como un objetivo rígido. Consulta con un profesional de salud para un plan personalizado.</p>
</section>""",
        "en": """<section class="long-content">
<h2>What is ideal body weight?</h2>
<p><strong>Ideal body weight</strong> is a weight range considered healthy for a person of a given height, age, and sex. Several formulas exist; the most widely used are Broca, Hamwi, and the healthy BMI range method.</p>

<h2>Ideal weight formulas</h2>
<ul>
  <li><strong>Broca formula:</strong> Men: Height(cm) − 100; Women: Height(cm) − 105</li>
  <li><strong>Hamwi formula:</strong> Men: 106 lb + 6 lb per inch over 5 ft; Women: 100 lb + 5 lb per inch over 5 ft</li>
  <li><strong>Healthy BMI range:</strong> Weight between BMI 18.5 and 24.9 for your height.</li>
</ul>

<h2>Practical example</h2>
<p><strong>Woman, 5'5" (165 cm) tall:</strong></p>
<ul>
  <li>Hamwi: 100 + 5×5 = <strong>125 lbs (56.7 kg)</strong></li>
  <li>BMI range: 50.3 kg to 67.8 kg (<strong>111 – 149 lbs</strong>)</li>
</ul>

<h2>Important limitations</h2>
<ul>
  <li>Doesn't account for body composition (muscle vs fat).</li>
  <li>Formulas were developed in specific populations and may not apply universally.</li>
  <li>"Ideal" weight varies with bone structure (small, medium, large frame).</li>
</ul>
</section>""",
    },

    "403": {  # agua-diaria
        "es": """<section class="long-content">
<h2>¿Cuánta agua necesitas beber al día?</h2>
<p>La cantidad de <strong>agua que debes beber al día</strong> depende de tu peso, nivel de actividad física, clima y estado de salud. La Organización Mundial de la Salud recomienda aproximadamente <strong>2-2,5 litros diarios</strong> para adultos, pero la cantidad óptima es personal. Esta calculadora usa la fórmula más aceptada científicamente: 35 ml por kilogramo de peso corporal, ajustado por actividad.</p>

<h2>Fórmula de hidratación diaria</h2>
<p><strong>Agua base = Peso (kg) × 35 ml</strong></p>
<p>Si practicas ejercicio, añade <strong>500-750 ml por hora de ejercicio moderado</strong> (más en climas calurosos).</p>

<h2>Ejemplo práctico</h2>
<p><strong>Persona de 70 kg con actividad moderada (30 min de ejercicio al día):</strong></p>
<ol>
  <li>Agua base: 70 × 35 = 2.450 ml</li>
  <li>Ajuste por ejercicio: +500 ml</li>
  <li>Total recomendado: <strong>2.950 ml ≈ 3 litros al día</strong></li>
</ol>

<h2>Señales de deshidratación</h2>
<ul>
  <li><strong>Orina oscura:</strong> La orina debe ser de color amarillo pálido.</li>
  <li><strong>Boca seca y sed:</strong> La sed ya indica deshidratación leve.</li>
  <li><strong>Fatiga y dolores de cabeza:</strong> Frecuentemente causados por falta de hidratación.</li>
  <li><strong>Piel sin elasticidad:</strong> Señal de deshidratación moderada a severa.</li>
</ul>

<h2>Consejos para hidratarte mejor</h2>
<ul>
  <li>Bebe un vaso de agua al levantarte en ayunas.</li>
  <li>Lleva siempre una botella de agua contigo.</li>
  <li>Come frutas y verduras con alto contenido en agua (sandía, pepino, naranja).</li>
  <li>Bebe agua antes de sentir sed, especialmente en verano o durante el ejercicio.</li>
  <li>El café, té y zumos también cuentan, aunque el agua pura es la mejor opción.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>How much water do you need per day?</h2>
<p>Your daily <strong>water intake needs</strong> depend on your weight, physical activity level, climate, and health status. The most widely accepted scientific formula is <strong>35 ml per kilogram of body weight</strong>, adjusted for activity level. This can range from about 2 liters to 3.5+ liters per day for active individuals.</p>

<h2>Daily hydration formula</h2>
<p><strong>Base water = Weight (kg) × 35 ml</strong></p>
<p>Add <strong>500–750 ml per hour of moderate exercise</strong> (more in hot climates).</p>

<h2>Practical example</h2>
<p><strong>Person of 70 kg with moderate activity (30 min exercise/day):</strong></p>
<ol>
  <li>Base water: 70 × 35 = 2,450 ml</li>
  <li>Exercise adjustment: +500 ml</li>
  <li>Total: <strong>2,950 ml ≈ 3 liters per day</strong></li>
</ol>

<h2>Signs of dehydration</h2>
<ul>
  <li><strong>Dark urine:</strong> Urine should be pale yellow.</li>
  <li><strong>Dry mouth and thirst:</strong> Thirst already indicates mild dehydration.</li>
  <li><strong>Fatigue and headaches:</strong> Often caused by insufficient hydration.</li>
</ul>
</section>""",
    },

    # ── COTIDIANO ────────────────────────────────────────────────────────────────

    "500": {  # propina
        "es": """<section class="long-content">
<h2>¿Cómo calcular la propina?</h2>
<p>La <strong>calculadora de propina</strong> te ayuda a calcular cuánto dejar de propina en un restaurante, café, peluquería o cualquier servicio donde se acostumbre a agradecer la atención con una gratificación. También divide el total automáticamente si váis en grupo, para que cada persona sepa exactamente cuánto pagar.</p>

<h2>Fórmula de la propina</h2>
<p><strong>Propina = Importe de la cuenta × (% de propina ÷ 100)</strong></p>
<p><strong>Total a pagar = Importe de la cuenta + Propina</strong></p>
<p><strong>Por persona = Total a pagar ÷ Número de personas</strong></p>

<h2>Porcentajes de propina recomendados</h2>
<ul>
  <li><strong>10 %:</strong> Servicio básico o simplemente por educación.</li>
  <li><strong>15 %:</strong> Servicio correcto, estándar habitual en muchos países.</li>
  <li><strong>20 %:</strong> Servicio excelente, estándar en EE. UU. y Canadá.</li>
  <li><strong>25 % o más:</strong> Servicio excepcional o para reconocer un esfuerzo especial.</li>
</ul>

<h2>Ejemplo práctico</h2>
<p><strong>Cuenta de 85 € entre 4 personas, propina del 15 %:</strong></p>
<ol>
  <li>Propina: 85 × 0,15 = <strong>12,75 €</strong></li>
  <li>Total: 85 + 12,75 = <strong>97,75 €</strong></li>
  <li>Por persona: 97,75 ÷ 4 = <strong>24,44 €/persona</strong></li>
</ol>

<h2>¿En qué países se deja propina?</h2>
<ul>
  <li><strong>EE. UU. y Canadá:</strong> Propina del 15-25 % es prácticamente obligatoria en restaurantes.</li>
  <li><strong>España:</strong> No es obligatoria; se deja de forma voluntaria, generalmente redondeo o 5-10 %.</li>
  <li><strong>México:</strong> 10-15 % en restaurantes es la norma.</li>
  <li><strong>Europa central:</strong> 5-10 % es habitual; en algunos países (Japón) no se practica.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>How to calculate a tip</h2>
<p>The <strong>tip calculator</strong> helps you figure out how much to leave as a gratuity at a restaurant, café, or any service where tipping is customary. It also splits the total automatically when dining in groups.</p>

<h2>Tip formula</h2>
<p><strong>Tip = Bill amount × (tip % ÷ 100)</strong></p>
<p><strong>Total = Bill + Tip</strong></p>
<p><strong>Per person = Total ÷ Number of people</strong></p>

<h2>Recommended tip percentages</h2>
<ul>
  <li><strong>10%:</strong> Basic or below-average service.</li>
  <li><strong>15%:</strong> Good service, standard in many countries.</li>
  <li><strong>20%:</strong> Excellent service, standard in the US and Canada.</li>
  <li><strong>25%+:</strong> Exceptional service or to recognize special effort.</li>
</ul>

<h2>Practical example</h2>
<p><strong>$85 bill for 4 people, 20% tip:</strong></p>
<ol>
  <li>Tip: $85 × 0.20 = <strong>$17</strong></li>
  <li>Total: $85 + $17 = <strong>$102</strong></li>
  <li>Per person: $102 ÷ 4 = <strong>$25.50/person</strong></li>
</ol>
</section>""",
    },

    "501": {  # calculadora-edad
        "es": """<section class="long-content">
<h2>¿Para qué sirve la calculadora de edad?</h2>
<p>La <strong>calculadora de edad</strong> calcula tu edad exacta en años, meses y días a partir de tu fecha de nacimiento. También puede calcular cuántos días faltan para tu próximo cumpleaños, el día de la semana en que naciste, y tu edad en otros formatos útiles. Es perfecta para trámites legales, cálculos de jubilación, o simplemente para saber exactamente cuántos días llevas en este mundo.</p>

<h2>¿Cómo se calcula la edad exacta?</h2>
<p>La edad no es simplemente el año actual menos el año de nacimiento. Debes tener en cuenta si ya ha pasado tu cumpleaños en el año actual:</p>
<ol>
  <li>Si la fecha actual es posterior a tu cumpleaños de este año: edad = año actual − año nacimiento</li>
  <li>Si aún no ha llegado tu cumpleaños: edad = año actual − año nacimiento − 1</li>
</ol>
<p>El cálculo exacto en días: diferencia total en días desde la fecha de nacimiento hasta hoy.</p>

<h2>Usos de la calculadora de edad</h2>
<ul>
  <li><strong>Trámites legales:</strong> Acreditar mayoría de edad, jubilación, herencias.</li>
  <li><strong>Medicina:</strong> Calcular la edad exacta de un paciente para dosis o diagnósticos.</li>
  <li><strong>Seguros:</strong> Las primas dependen de la edad exacta en la fecha de contratación.</li>
  <li><strong>Nutrición y deporte:</strong> Calcular el metabolismo basal y las necesidades calóricas.</li>
  <li><strong>Curiosidad personal:</strong> Saber en qué día de la semana naciste o cuántos días llevas vivo.</li>
</ul>

<h2>¿Cómo se cuenta la edad en distintos países?</h2>
<p>En la mayoría de países occidentales, la edad se cumple el día del aniversario de nacimiento. En Corea del Sur existe un sistema tradicional donde los bebés nacen con 1 año y cumplen años el 1 de enero (aunque esto está cambiando). En algunos contextos médicos se usa la edad gestacional o la edad corregida para bebés prematuros.</p>
</section>""",
        "en": """<section class="long-content">
<h2>What is an age calculator?</h2>
<p>The <strong>age calculator</strong> computes your exact age in years, months, and days from your birth date. It can also calculate how many days until your next birthday, what day of the week you were born, and your age in other useful formats.</p>

<h2>How exact age is calculated</h2>
<ol>
  <li>If today is after your birthday this year: age = current year − birth year</li>
  <li>If your birthday hasn't occurred yet this year: age = current year − birth year − 1</li>
</ol>
<p>For the exact count in days: total days elapsed from birth date to today.</p>

<h2>Common uses</h2>
<ul>
  <li><strong>Legal purposes:</strong> Proving legal age, retirement, inheritance eligibility.</li>
  <li><strong>Medicine:</strong> Calculating exact patient age for dosing or diagnosis.</li>
  <li><strong>Insurance:</strong> Premiums often depend on age at the contract date.</li>
  <li><strong>Nutrition and fitness:</strong> Calculating BMR and calorie needs.</li>
  <li><strong>Personal curiosity:</strong> What day were you born? How many days have you lived?</li>
</ul>
</section>""",
    },

    # ── ESTADISTICA ──────────────────────────────────────────────────────────────

    "600": {  # media
        "es": """<section class="long-content">
<h2>¿Qué es la media aritmética?</h2>
<p>La <strong>media aritmética</strong> (o promedio) es el valor que resulta de sumar todos los datos de un conjunto y dividir entre el número de datos. Es la medida de tendencia central más utilizada en estadística, ciencias, economía y vida cotidiana: promedios de notas, temperatura media mensual, salario medio, etc.</p>

<h2>Fórmula de la media aritmética</h2>
<p><strong>Media (x̄) = (x₁ + x₂ + ... + xₙ) ÷ n</strong></p>
<p>Donde <em>n</em> es el número de valores y x₁...xₙ son los valores del conjunto.</p>

<h2>Ejemplo práctico</h2>
<p><strong>Notas de un alumno en 5 exámenes: 7, 8, 6, 9, 5</strong></p>
<ol>
  <li>Suma: 7 + 8 + 6 + 9 + 5 = 35</li>
  <li>Media: 35 ÷ 5 = <strong>7,0</strong></li>
</ol>

<h2>Media, mediana y moda: ¿cuándo usar cada una?</h2>
<ul>
  <li><strong>Media:</strong> Ideal cuando los datos son simétricos sin valores extremos. Ej: temperatura media, nota promedio.</li>
  <li><strong>Mediana:</strong> Más robusta ante valores atípicos. Ej: salario mediano (el salario medio se distorsiona por los muy altos).</li>
  <li><strong>Moda:</strong> Para datos cualitativos o frecuencias. Ej: color más vendido, talla más popular.</li>
</ul>

<h2>Tipos de media</h2>
<ul>
  <li><strong>Media aritmética:</strong> Suma ÷ n (la más común).</li>
  <li><strong>Media ponderada:</strong> Cada valor tiene un peso diferente. Ej: nota final con distintos porcentajes por asignatura.</li>
  <li><strong>Media geométrica:</strong> Raíz n-ésima del producto de todos los valores. Usada en tasas de crecimiento.</li>
  <li><strong>Media armónica:</strong> Para velocidades o razones. Ej: velocidad media en recorridos de igual distancia.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is the arithmetic mean?</h2>
<p>The <strong>arithmetic mean</strong> (or average) is the value obtained by summing all data in a set and dividing by the count. It's the most widely used measure of central tendency in statistics, science, economics, and daily life.</p>

<h2>Arithmetic mean formula</h2>
<p><strong>Mean (x̄) = (x₁ + x₂ + ... + xₙ) ÷ n</strong></p>
<p>Where <em>n</em> is the number of values.</p>

<h2>Practical example</h2>
<p><strong>Student grades in 5 tests: 7, 8, 6, 9, 5</strong></p>
<ol>
  <li>Sum: 7 + 8 + 6 + 9 + 5 = 35</li>
  <li>Mean: 35 ÷ 5 = <strong>7.0</strong></li>
</ol>

<h2>Mean, median, and mode: when to use each</h2>
<ul>
  <li><strong>Mean:</strong> Best for symmetric data without outliers.</li>
  <li><strong>Median:</strong> More robust against outliers (e.g., median income vs mean income).</li>
  <li><strong>Mode:</strong> For categorical data or most frequent values.</li>
</ul>

<h2>Types of mean</h2>
<ul>
  <li><strong>Arithmetic mean:</strong> Sum ÷ n (most common).</li>
  <li><strong>Weighted mean:</strong> Each value has a different weight.</li>
  <li><strong>Geometric mean:</strong> nth root of the product — used for growth rates.</li>
  <li><strong>Harmonic mean:</strong> For rates and speeds.</li>
</ul>
</section>""",
    },

    # ── CIENCIA ──────────────────────────────────────────────────────────────────

    "700": {  # velocidad
        "es": """<section class="long-content">
<h2>La relación velocidad, distancia y tiempo</h2>
<p>La <strong>calculadora de velocidad, distancia y tiempo</strong> permite resolver cualquiera de las tres magnitudes cuando conoces las otras dos. Es una de las fórmulas más fundamentales de la física clásica y tiene aplicaciones directas en conducción, ciclismo, carreras, física y astronomía.</p>

<h2>Las tres fórmulas</h2>
<ul>
  <li><strong>Velocidad: v = d ÷ t</strong></li>
  <li><strong>Distancia: d = v × t</strong></li>
  <li><strong>Tiempo: t = d ÷ v</strong></li>
</ul>

<h2>Ejemplos prácticos</h2>
<p><strong>Ejemplo 1 – ¿A qué velocidad vas si recorres 240 km en 3 horas?</strong></p>
<ol>
  <li>v = 240 ÷ 3 = <strong>80 km/h</strong></li>
</ol>
<p><strong>Ejemplo 2 – ¿Cuánto tardas a 90 km/h en recorrer 270 km?</strong></p>
<ol>
  <li>t = 270 ÷ 90 = <strong>3 horas</strong></li>
</ol>
<p><strong>Ejemplo 3 – ¿Cuántos km recorres en 2,5 horas a 120 km/h?</strong></p>
<ol>
  <li>d = 120 × 2,5 = <strong>300 km</strong></li>
</ol>

<h2>Conversiones de unidades de velocidad</h2>
<ul>
  <li>1 km/h = 0,2778 m/s</li>
  <li>1 m/s = 3,6 km/h</li>
  <li>1 milla/h (mph) = 1,609 km/h</li>
  <li>1 nudo (knot) = 1,852 km/h (navegación y aviación)</li>
</ul>

<h2>Velocidades de referencia en la vida real</h2>
<ul>
  <li><strong>Persona caminando:</strong> ~5 km/h</li>
  <li><strong>Corredor a ritmo moderado:</strong> ~10-12 km/h</li>
  <li><strong>Bicicleta urbana:</strong> ~15-25 km/h</li>
  <li><strong>Autopista (límite España):</strong> 120 km/h</li>
  <li><strong>Velocidad del sonido:</strong> ~1.235 km/h</li>
  <li><strong>Avión comercial:</strong> ~900 km/h</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>Speed, distance, and time relationship</h2>
<p>The <strong>speed, distance, and time calculator</strong> solves any of the three quantities when you know the other two. It's one of the most fundamental formulas in classical physics, with direct applications in driving, cycling, running, physics, and astronomy.</p>

<h2>The three formulas</h2>
<ul>
  <li><strong>Speed: v = d ÷ t</strong></li>
  <li><strong>Distance: d = v × t</strong></li>
  <li><strong>Time: t = d ÷ v</strong></li>
</ul>

<h2>Practical examples</h2>
<p><strong>Example 1 – Speed: traveled 150 miles in 2.5 hours?</strong></p>
<ol><li>v = 150 ÷ 2.5 = <strong>60 mph</strong></li></ol>
<p><strong>Example 2 – Time: how long at 60 mph to cover 240 miles?</strong></p>
<ol><li>t = 240 ÷ 60 = <strong>4 hours</strong></li></ol>

<h2>Speed unit conversions</h2>
<ul>
  <li>1 mph = 1.609 km/h</li>
  <li>1 km/h = 0.6214 mph</li>
  <li>1 m/s = 3.6 km/h = 2.237 mph</li>
  <li>1 knot = 1.852 km/h (nautical and aviation)</li>
</ul>
</section>""",
    },

    # ── CONVERSION ───────────────────────────────────────────────────────────────

    "800": {  # longitud
        "es": """<section class="long-content">
<h2>Conversor de longitud: todas las unidades</h2>
<p>El <strong>conversor de longitud</strong> transforma al instante cualquier medida entre los sistemas métrico e imperial. Es imprescindible para bricolaje, cocina de recetas extranjeras, compras online en tiendas internacionales, viajes y cualquier actividad técnica que combine unidades de distintos sistemas.</p>

<h2>Unidades de longitud más comunes</h2>
<ul>
  <li><strong>Sistema métrico (SI):</strong> milímetro (mm), centímetro (cm), metro (m), kilómetro (km)</li>
  <li><strong>Sistema imperial (anglosajón):</strong> pulgada (in), pie (ft), yarda (yd), milla (mi)</li>
  <li><strong>Náutico:</strong> milla náutica (nm) = 1.852 m</li>
</ul>

<h2>Factores de conversión clave</h2>
<ul>
  <li>1 m = 100 cm = 1.000 mm</li>
  <li>1 km = 1.000 m</li>
  <li>1 pulgada = 2,54 cm</li>
  <li>1 pie = 30,48 cm = 12 pulgadas</li>
  <li>1 yarda = 91,44 cm = 3 pies</li>
  <li>1 milla = 1,609 km = 5.280 pies</li>
</ul>

<h2>Ejemplos prácticos</h2>
<ul>
  <li><strong>Tu altura en pies:</strong> 1,75 m = 1,75 ÷ 0,3048 = <strong>5 pies y 9 pulgadas</strong></li>
  <li><strong>Pantalla de 55 pulgadas:</strong> 55 × 2,54 = <strong>139,7 cm de diagonal</strong></li>
  <li><strong>Maratón en kilómetros:</strong> 26,2 millas × 1,609 = <strong>42,2 km</strong></li>
</ul>

<h2>¿Por qué existen dos sistemas?</h2>
<p>El sistema métrico fue adoptado por casi todos los países del mundo. Los EE. UU., Liberia y Myanmar son los únicos países que usan principalmente el sistema imperial. El Reino Unido usa un sistema mixto: kilómetros en señales de tráfico pero millas para distancias de conducción. En ciencia y tecnología, el SI (Sistema Internacional de Unidades) es el estándar universal.</p>
</section>""",
        "en": """<section class="long-content">
<h2>Length converter: all units</h2>
<p>The <strong>length converter</strong> instantly transforms any measurement between metric and imperial systems. It's essential for DIY projects, cooking with foreign recipes, international online shopping, travel, and any technical work combining units from different systems.</p>

<h2>Most common length units</h2>
<ul>
  <li><strong>Metric (SI):</strong> millimeter (mm), centimeter (cm), meter (m), kilometer (km)</li>
  <li><strong>Imperial:</strong> inch (in), foot (ft), yard (yd), mile (mi)</li>
  <li><strong>Nautical:</strong> nautical mile (nm) = 1,852 m</li>
</ul>

<h2>Key conversion factors</h2>
<ul>
  <li>1 m = 100 cm = 1,000 mm</li>
  <li>1 inch = 2.54 cm</li>
  <li>1 foot = 30.48 cm = 12 inches</li>
  <li>1 yard = 91.44 cm = 3 feet</li>
  <li>1 mile = 1.609 km = 5,280 feet</li>
</ul>

<h2>Practical examples</h2>
<ul>
  <li><strong>Your height in feet:</strong> 175 cm = 175 ÷ 30.48 = <strong>5'9"</strong></li>
  <li><strong>55-inch screen diagonal:</strong> 55 × 2.54 = <strong>139.7 cm</strong></li>
  <li><strong>Marathon in kilometers:</strong> 26.2 miles × 1.609 = <strong>42.2 km</strong></li>
</ul>
</section>""",
    },

    "802": {  # temperatura
        "es": """<section class="long-content">
<h2>Conversor de temperatura: Celsius, Fahrenheit y Kelvin</h2>
<p>El <strong>conversor de temperatura</strong> transforma entre las tres escalas de temperatura más utilizadas en el mundo: <strong>Celsius (°C)</strong>, usada en la mayor parte del mundo; <strong>Fahrenheit (°F)</strong>, usada principalmente en EE. UU.; y <strong>Kelvin (K)</strong>, la escala del Sistema Internacional de Unidades, usada en ciencia y física.</p>

<h2>Fórmulas de conversión de temperatura</h2>
<ul>
  <li><strong>°C a °F:</strong> °F = (°C × 9/5) + 32</li>
  <li><strong>°F a °C:</strong> °C = (°F − 32) × 5/9</li>
  <li><strong>°C a K:</strong> K = °C + 273,15</li>
  <li><strong>K a °C:</strong> °C = K − 273,15</li>
</ul>

<h2>Ejemplos prácticos</h2>
<ul>
  <li><strong>Temperatura corporal normal (37 °C):</strong> °F = (37 × 9/5) + 32 = <strong>98,6 °F</strong></li>
  <li><strong>Punto de ebullición del agua (100 °C):</strong> <strong>212 °F / 373,15 K</strong></li>
  <li><strong>Horno a 350 °F:</strong> °C = (350−32) × 5/9 = <strong>176,7 °C</strong></li>
  <li><strong>Cero absoluto:</strong> <strong>−273,15 °C = 0 K = −459,67 °F</strong></li>
</ul>

<h2>Temperaturas de referencia importantes</h2>
<ul>
  <li><strong>Cero absoluto:</strong> 0 K = −273,15 °C — temperatura más baja posible en el universo.</li>
  <li><strong>Congelación del agua:</strong> 0 °C = 32 °F = 273,15 K</li>
  <li><strong>Temperatura ambiente cómoda:</strong> ~22 °C = 71,6 °F</li>
  <li><strong>Temperatura corporal:</strong> 37 °C = 98,6 °F</li>
  <li><strong>Ebullición del agua:</strong> 100 °C = 212 °F</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>Temperature converter: Celsius, Fahrenheit, and Kelvin</h2>
<p>The <strong>temperature converter</strong> transforms between the three most used temperature scales: <strong>Celsius (°C)</strong>, used in most of the world; <strong>Fahrenheit (°F)</strong>, used mainly in the US; and <strong>Kelvin (K)</strong>, the SI base unit used in science and physics.</p>

<h2>Temperature conversion formulas</h2>
<ul>
  <li><strong>°C to °F:</strong> °F = (°C × 9/5) + 32</li>
  <li><strong>°F to °C:</strong> °C = (°F − 32) × 5/9</li>
  <li><strong>°C to K:</strong> K = °C + 273.15</li>
  <li><strong>K to °C:</strong> °C = K − 273.15</li>
</ul>

<h2>Key reference temperatures</h2>
<ul>
  <li><strong>Absolute zero:</strong> 0 K = −273.15 °C = −459.67 °F</li>
  <li><strong>Water freezing:</strong> 0 °C = 32 °F</li>
  <li><strong>Room temperature:</strong> ~22 °C = 71.6 °F</li>
  <li><strong>Body temperature:</strong> 37 °C = 98.6 °F</li>
  <li><strong>Water boiling:</strong> 100 °C = 212 °F</li>
  <li><strong>Oven at 350 °F:</strong> = 176.7 °C</li>
</ul>
</section>""",
    },

    # ── DEPORTES ─────────────────────────────────────────────────────────────────

    "900": {  # ritmo-carrera
        "es": """<section class="long-content">
<h2>¿Qué es el ritmo de carrera y cómo se calcula?</h2>
<p>El <strong>ritmo de carrera</strong> (también llamado pace) es el tiempo que tardas en recorrer un kilómetro o una milla corriendo. Se expresa en minutos por kilómetro (min/km) o minutos por milla (min/mi) y es la métrica principal que usan los corredores para controlar el esfuerzo y planificar carreras y entrenamientos.</p>

<h2>Fórmulas del ritmo de carrera</h2>
<ul>
  <li><strong>Ritmo (min/km) = Tiempo total (min) ÷ Distancia (km)</strong></li>
  <li><strong>Velocidad (km/h) = Distancia (km) ÷ Tiempo (h)</strong></li>
  <li><strong>Tiempo estimado = Distancia (km) × Ritmo (min/km)</strong></li>
</ul>

<h2>Ejemplo práctico</h2>
<p><strong>Corres 10 km en 55 minutos. ¿Cuál es tu ritmo?</strong></p>
<ol>
  <li>Ritmo: 55 ÷ 10 = <strong>5:30 min/km</strong></li>
  <li>Velocidad: 10 ÷ (55/60) = <strong>10,9 km/h</strong></li>
</ol>
<p><strong>¿A 5:30 min/km, en cuánto terminarías una maratón (42,195 km)?</strong></p>
<ol>
  <li>Tiempo: 42,195 × 5,5 = 232 min = <strong>3 horas y 52 minutos</strong></li>
</ol>

<h2>Ritmos de referencia según nivel</h2>
<ul>
  <li><strong>Principiante:</strong> 7:00 – 8:00 min/km</li>
  <li><strong>Intermedio:</strong> 5:30 – 7:00 min/km</li>
  <li><strong>Avanzado:</strong> 4:30 – 5:30 min/km</li>
  <li><strong>Competitivo popular:</strong> 4:00 – 4:30 min/km</li>
  <li><strong>Élite masculino:</strong> < 2:50 min/km (récord mundial maratón)</li>
</ul>

<h2>¿Cómo mejorar tu ritmo de carrera?</h2>
<ul>
  <li><strong>Entrenamiento en zonas cardíacas:</strong> La mayoría del volumen (70-80 %) debe ser en zona 2 (conversacional).</li>
  <li><strong>Intervalos:</strong> Series de 400 m, 1 km o 2 km a ritmo más rápido que el objetivo.</li>
  <li><strong>Tempo runs:</strong> Rodajes a ritmo de umbral anaeróbico (~1 hora de esfuerzo máximo sostenible).</li>
  <li><strong>Progresión:</strong> Aumenta el volumen un máximo del 10 % por semana para evitar lesiones.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is running pace and how is it calculated?</h2>
<p><strong>Running pace</strong> is the time it takes to cover one kilometer or mile while running. Expressed in minutes per kilometer (min/km) or minutes per mile (min/mi), it's the primary metric runners use to control effort and plan races and training sessions.</p>

<h2>Running pace formulas</h2>
<ul>
  <li><strong>Pace (min/km) = Total time (min) ÷ Distance (km)</strong></li>
  <li><strong>Speed (km/h) = Distance (km) ÷ Time (h)</strong></li>
  <li><strong>Estimated time = Distance (km) × Pace (min/km)</strong></li>
</ul>

<h2>Practical example</h2>
<p><strong>You run 10 km in 55 minutes. What's your pace?</strong></p>
<ol>
  <li>Pace: 55 ÷ 10 = <strong>5:30 min/km</strong></li>
  <li>Speed: 10 ÷ (55/60) = <strong>10.9 km/h</strong></li>
</ol>
<p><strong>At 5:30 min/km, what would your marathon time be (42.195 km)?</strong></p>
<ol>
  <li>Time: 42.195 × 5.5 = 232 min = <strong>3 hours 52 minutes</strong></li>
</ol>

<h2>Reference paces by level</h2>
<ul>
  <li><strong>Beginner:</strong> 7:00 – 8:00 min/km</li>
  <li><strong>Intermediate:</strong> 5:30 – 7:00 min/km</li>
  <li><strong>Advanced:</strong> 4:30 – 5:30 min/km</li>
  <li><strong>Competitive amateur:</strong> 4:00 – 4:30 min/km</li>
</ul>
</section>""",
    },

}


def generate_long_content(calc_id: str, lang: str) -> str:
    """Return long-form SEO article for a calculator, or empty string if none."""
    entry = LONG_CONTENT.get(calc_id, {})
    return entry.get(lang, entry.get("en", ""))
'''

text += ADDITION
src.write_bytes(text.encode("utf-8"))
print(f"[OK] calc_content.py patched ({len(text)} chars)")

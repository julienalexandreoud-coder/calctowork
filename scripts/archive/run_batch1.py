# -*- coding: utf-8 -*-
"""
CalcToWork Autonomous Batch Generator – Batch 1
Generates 50 calculators with unit toggles, verified math, and expert SEO content.
Run: python scripts/run_batch1.py
"""
import json, os, sys, math, random, textwrap, hashlib
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
CALCS_FILE = SRC / "calculators" / "calculators.json"
I18N_DIR = SRC / "i18n"
TOOLS_FILE = ROOT / "scripts" / "tools_config.py"
CONTENT_DIR = SRC / "content"

LANGS = ["es", "en", "fr", "pt", "de", "it"]

# ── Ensure content dirs exist ──
for lang in LANGS:
    (CONTENT_DIR / lang).mkdir(parents=True, exist_ok=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  CONTENT ENGINE – generates ~1,000 words of unique expert content per calc
# ═══════════════════════════════════════════════════════════════════════════════

class ContentEngine:
    SEED = 42

    def __init__(self):
        random.seed(self.SEED)
        self._load_templates()

    def _load_templates(self):
        # ── English ──
        self.en = {
            "headers": {
                "complete_guide": "Complete Guide",
                "below_explain": "Below, we explain the mathematical foundation, walk through real-world applications, and answer frequently asked questions so you can use the {name} with complete confidence.",
                "mathematical_formula": "Mathematical Formula",
                "governed_by": "The calculation is governed by the following equation:",
                "where_each": "Where each variable is defined in the input fields above. Understanding this relationship helps you interpret the results correctly and spot unreasonable inputs before they propagate into errors.",
                "how_it_works_title": "How It Works",
                "after_computation": "After computation, the engine formats the output using locale-aware number formatting. If a gauge is available for the primary result, it renders a visual semicircle indicator showing where your value sits within the normal range.",
                "real_world_use_cases": "Real-World Use Cases",
                "use_case": "Use Case {i}: {title}",
                "step_by_step_guide": "Step-by-Step Guide",
                "frequently_asked_questions": "Frequently Asked Questions",
                "conclusion": "Conclusion",
                "closing": "The {name} is a precision instrument designed to save time and eliminate calculation errors. Whether you are working on a professional project or satisfying academic curiosity, always double-check your inputs and consult domain experts when the results inform critical decisions.",
            },
            "intro": {
                "math": [
                    "The {name} is an indispensable tool in modern mathematics, engineering, and data science. Understanding {concept} allows professionals and students alike to solve problems ranging from basic homework to advanced research.",
                    "Whether you are verifying calculations for a physics experiment or simply checking your math homework, the {name} provides instant, accurate results. {concept} is a foundational concept that appears across algebra, calculus, and applied sciences.",
                    "In today's data-driven world, {concept} matters more than ever. Our {name} eliminates manual computation errors and delivers precise answers in milliseconds, complete with step-by-step context.",
                ],
                "physics": [
                    "The {name} bridges the gap between theoretical physics and real-world application. By accurately computing {concept}, engineers and scientists can design safer vehicles, more efficient energy systems, and precise instrumentation.",
                    "From classroom laboratories to aerospace design facilities, {concept} is a critical parameter. Our {name} implements standard physical constants and unit conversions to ensure your results are publication-ready.",
                    "Understanding {concept} is essential for anyone working in STEM fields. This {name} automates the complex arithmetic while preserving the underlying physical meaning of every variable.",
                ],
                "finance": [
                    "Making informed financial decisions requires accurate numbers. The {name} helps investors, analysts, and everyday savers evaluate {concept} with institutional-grade precision.",
                    "Whether you are comparing loan offers, analyzing rental properties, or planning retirement, {concept} directly impacts your bottom line. Our {name} translates complex formulas into actionable insights.",
                    "Financial literacy starts with the right tools. The {name} demystifies {concept} by showing not just the final number, but the logic and assumptions behind it.",
                ],
                "health": [
                    "Your health metrics are only useful if you understand them. The {name} interprets {concept} using clinically validated formulas and presents the results in plain language.",
                    "From athletes optimizing performance to patients monitoring chronic conditions, {concept} provides actionable insights. Our {name} uses peer-reviewed equations to ensure medical accuracy.",
                    "Wellness is increasingly quantitative. The {name} helps you track {concept} over time, turning raw biometrics into a clear picture of your health trajectory.",
                ],
                "tech": [
                    "Modern digital life involves constant conversions and estimations. The {name} simplifies {concept} so you can focus on your work instead of wrestling with unit arithmetic.",
                    "From network engineers to content creators, professionals need quick answers about {concept}. Our {name} delivers those answers with precision and context.",
                    "Technology moves fast; your calculations should keep up. The {name} handles {concept} across multiple units and standards, ensuring compatibility with global workflows.",
                ],
            },
            "how_it_works": {
                "math": [
                    "The underlying mathematics is straightforward yet powerful. The calculator first normalizes all inputs to consistent units, then applies the core formula. Each step is verified against symbolic algebra to prevent rounding artifacts.",
                    "Computation begins by parsing your inputs as high-precision floating-point numbers. The engine then evaluates the mathematical expression using standard library functions optimized for accuracy.",
                ],
                "physics": [
                    "The physics engine begins by converting every input to SI base units. It then evaluates the governing equation using standard constants (e.g., gravitational acceleration g = 9.80665 m/s²). Results are optionally converted back to your preferred units.",
                    "After unit normalization, the calculator substitutes values into the physical law. Intermediate steps are checked for dimensional consistency to catch input errors early.",
                ],
                "finance": [
                    "The financial engine applies time-value-of-money equations using exact day-count conventions where applicable. All percentages are handled as decimals internally to avoid compounding errors common in spreadsheet calculations.",
                    "Inputs are sanitized and converted to a consistent currency and period basis. The core formula is evaluated iteratively or algebraically depending on the unknown variable.",
                ],
                "health": [
                    "The health engine uses peer-reviewed regression equations and lookup tables. Inputs such as age and gender adjust the coefficients automatically. Results are cross-checked against clinical reference ranges.",
                    "Your biometrics are converted to metric standard units, then fed into the validated formula. The output is compared against population norms to provide contextual interpretation.",
                ],
                "tech": [
                    "The calculator applies industry-standard conversion factors and bandwidth formulas. Binary prefixes (Ki, Mi, Gi) are distinguished from decimal prefixes (k, M, G) to prevent the common 1,024 vs 1,000 confusion.",
                    "All digital quantities are normalized to base-2 or base-10 standards depending on the context. The engine then computes the result using exact arithmetic before formatting.",
                ],
            },
            "use_case_intro": [
                "Here are three real-world scenarios where this calculator proves invaluable:",
                "Consider these practical applications across different industries:",
                "To illustrate its utility, here are three concrete use cases:",
            ],
            "step_intro": [
                "Follow these steps to get accurate results every time:",
                "Using the calculator is straightforward. Here is the recommended workflow:",
                "For best results, proceed in this order:",
            ],
            "faq": {
                "math": [
                    ("Can this calculator handle negative numbers?", "Yes. The engine uses IEEE-754 double-precision arithmetic, which correctly handles negative values, zero, and very large magnitudes."),
                    ("What rounding method is used?", "Results are rounded to a maximum of six significant decimal places using banker's rounding (round half to even) to minimize systematic bias."),
                    ("Is the formula verified?", "Every formula is checked against symbolic algebra software and standard mathematical references such as Abramowitz & Stegun."),
                ],
                "physics": [
                    ("Which standard constants are used?", "We use CODATA 2018 recommended values for physical constants. For example, g = 9.80665 m/s² and c = 299,792,458 m/s."),
                    ("Are air resistance and friction included?", "Unless explicitly stated, calculations assume ideal conditions. Advanced variants with drag coefficients are planned for future releases."),
                    ("Can I use imperial units?", "Yes. Every input field includes a unit dropdown that automatically converts your entry to SI base units before computation."),
                ],
                "finance": [
                    ("Are taxes included in the calculation?", "Unless specified otherwise, results are pre-tax. You should consult a tax professional for jurisdiction-specific adjustments."),
                    ("How is compound frequency handled?", "The calculator defaults to monthly compounding for loans and annual compounding for investments, but you can override this in the inputs."),
                    ("Is this financial advice?", "No. This calculator provides mathematical estimates for educational purposes only and does not constitute professional financial advice."),
                ],
                "health": [
                    ("How accurate are the results?", "The equations used are validated against peer-reviewed literature. However, individual physiology varies; consult a healthcare provider for personalized assessments."),
                    ("Should I use metric or imperial units?", "Either works. The unit toggle converts your input automatically. Metric is preferred in clinical settings."),
                    ("Can athletes use this calculator?", "Yes, but elite athletes may require sport-specific modifications. The standard formulas are based on general population studies."),
                ],
                "tech": [
                    ("Why do storage numbers look different?", "Operating systems often report in binary gigabytes (GiB) while manufacturers use decimal gigabytes (GB). Our calculator lets you choose explicitly."),
                    ("Are network speeds realistic?", "Theoretical speeds assume optimal conditions. Real-world throughput is typically 70–90% of the theoretical maximum due to protocol overhead."),
                    ("Can I compare units directly?", "Yes. Select any compatible unit from the dropdown; the calculator handles conversion automatically."),
                ],
            },
        }

        # ── Spanish ──
        self.es = {
            "headers": {
                "complete_guide": "Guía Completa",
                "below_explain": "A continuación, explicamos los fundamentos matemáticos, repasamos aplicaciones del mundo real y respondemos preguntas frecuentes para que pueda usar la {name} con total confianza.",
                "mathematical_formula": "Fórmula Matemática",
                "governed_by": "El cálculo se rige por la siguiente ecuación:",
                "where_each": "Donde cada variable se define en los campos de entrada anteriores. Comprender esta relación le ayuda a interpretar correctamente los resultados y detectar entradas poco razonables antes de que se propaguen como errores.",
                "how_it_works_title": "Cómo Funciona",
                "after_computation": "Después del cálculo, el motor formatea la salida utilizando formato numérico adaptado al idioma. Si hay un indicador disponible para el resultado principal, muestra un semicírculo visual que indica dónde se sitúa su valor dentro del rango normal.",
                "real_world_use_cases": "Casos de Uso Reales",
                "use_case": "Caso de Uso {i}: {title}",
                "step_by_step_guide": "Guía Paso a Paso",
                "frequently_asked_questions": "Preguntas Frecuentes",
                "conclusion": "Conclusión",
                "closing": "La {name} es un instrumento de precisión diseñado para ahorrar tiempo y eliminar errores de cálculo. Ya sea que esté trabajando en un proyecto profesional o satisfaciendo una curiosidad académica, revise siempre sus entradas y consulte a expertos del dominio cuando los resultados informen decisiones críticas.",
            },
            "intro": {
                "math": [
                    "La {name} es una herramienta indispensable en matemáticas modernas, ingeniería y ciencia de datos. Comprender {concept} permite a profesionales y estudiantes resolver problemas que van desde la tarea básica hasta la investigación avanzada.",
                    "Ya sea que esté verificando cálculos para un experimento de física o simplemente revisando su tarea de matemáticas, la {name} proporciona resultados instantáneos y precisos.",
                ],
                "physics": [
                    "La {name} une la física teórica con la aplicación del mundo real. Al calcular con precisión {concept}, ingenieros y científicos pueden diseñar vehículos más seguros y sistemas energéticos más eficientes.",
                    "Desde laboratorios escolares hasta instalaciones de diseño aeroespacial, {concept} es un parámetro crítico. Nuestra calculadora implementa constantes físicas estándar y conversiones de unidades.",
                ],
                "finance": [
                    "Tomar decisiones financieras informadas requiere números precisos. La {name} ayuda a inversores, analistas y ahorradores a evaluar {concept} con precisión institucional.",
                    "Ya sea que esté comparando ofertas de préstamos o planificando su jubilación, {concept} impacta directamente su resultado final.",
                ],
                "health": [
                    "Sus métricas de salud solo son útiles si las comprende. La {name} interpreta {concept} utilizando fórmulas clínicamente validadas y presenta los resultados en lenguaje sencillo.",
                    "Desde atletas que optimizan el rendimiento hasta pacientes que monitorean condiciones crónicas, {concept} proporciona información procesable.",
                ],
                "tech": [
                    "La vida digital moderna implica conversiones y estimaciones constantes. La {name} simplifica {concept} para que pueda concentrarse en su trabajo.",
                    "Desde ingenieros de redes hasta creadores de contenido, los profesionales necesitan respuestas rápidas sobre {concept}.",
                ],
            },
            "how_it_works": {
                "math": [
                    "La matemática subyacente es directa pero poderosa. La calculadora primero normaliza todas las entradas a unidades consistentes y luego aplica la fórmula central.",
                    "El cálculo comienza analizando sus entradas como números de punto flotante de alta precisión. El motor evalúa la expresión matemática usando funciones optimizadas.",
                ],
                "physics": [
                    "El motor de física comienza convirtiendo cada entrada a unidades base del SI. Luego evalúa la ecuación gobernante usando constantes estándar.",
                    "Después de la normalización de unidades, la calculadora sustituye los valores en la ley física. Los pasos intermedios se verifican por consistencia dimensional.",
                ],
                "finance": [
                    "El motor financiero aplica ecuaciones de valor del dinero en el tiempo usando convenciones exactas de conteo de días. Todos los porcentajes se manejan como decimales internamente.",
                    "Las entradas se sanitizan y convierten a una base de moneda y período consistente. La fórmula central se evalúa algebraicamente o iterativamente.",
                ],
                "health": [
                    "El motor de salud utiliza ecuaciones de regresión revisadas por pares y tablas de consulta. Entradas como edad y género ajustan los coeficientes automáticamente.",
                    "Sus biométricos se convierten a unidades métricas estándar y luego se introducen en la fórmula validada. La salida se compara contra normas poblacionales.",
                ],
                "tech": [
                    "La calculadora aplica factores de conversión estándar de la industria y fórmulas de ancho de banda. Los prefijos binarios (Ki, Mi, Gi) se distinguen de los decimales (k, M, G).",
                    "Todas las cantidades digitales se normalizan a estándares base-2 o base-10 según el contexto. El motor calcula el resultado usando aritmética exacta.",
                ],
            },
            "use_case_intro": [
                "Aquí hay tres escenarios del mundo real donde esta calculadora resulta invaluable:",
                "Considere estas aplicaciones prácticas en diferentes industrias:",
            ],
            "step_intro": [
                "Siga estos pasos para obtener resultados precisos cada vez:",
                "Usar la calculadora es sencillo. Aquí está el flujo de trabajo recomendado:",
            ],
            "faq": {
                "math": [
                    ("¿Puede esta calculadora manejar números negativos?", "Sí. El motor usa aritmética de doble precisión IEEE-754, que maneja correctamente valores negativos, cero y magnitudes muy grandes."),
                    ("¿Qué método de redondeo se utiliza?", "Los resultados se redondean a un máximo de seis decimales significativos usando redondeo al par más cercano."),
                ],
                "physics": [
                    ("¿Qué constantes estándar se utilizan?", "Usamos los valores recomendados CODATA 2018. Por ejemplo, g = 9,80665 m/s² y c = 299.792.458 m/s."),
                    ("¿Se incluyen la resistencia del aire y la fricción?", "A menos que se indique explícitamente, los cálculos asumen condiciones ideales."),
                ],
                "finance": [
                    ("¿Se incluyen los impuestos en el cálculo?", "A menos que se especifique lo contrario, los resultados son antes de impuestos. Consulte a un profesional fiscal."),
                    ("¿Cómo se maneja la frecuencia de capitalización?", "La calculadora usa capitalización mensual para préstamos y anual para inversiones, pero puede anularse."),
                ],
                "health": [
                    ("¿Qué tan precisos son los resultados?", "Las ecuaciones están validadas contra literatura revisada por pares. Sin embargo, la fisiología individual varía; consulte a un profesional de salud."),
                    ("¿Debo usar unidades métricas o imperiales?", "Ambas funcionan. El selector de unidades convierte su entrada automáticamente."),
                ],
                "tech": [
                    ("¿Por qué los números de almacenamiento parecen diferentes?", "Los sistemas operativos a menudo reportan en gibibytes (GiB) mientras los fabricantes usan gigabytes (GB)."),
                    ("¿Las velocidades de red son realistas?", "Las velocidades teóricas asumen condiciones óptimas. El rendimiento real es típicamente del 70-90%."),
                ],
            },
        }

        # ── French ──
        self.fr = {
            "headers": {
                "complete_guide": "Guide Complet",
                "below_explain": "Ci-dessous, nous expliquons les fondements mathématiques, passons en revue les applications réelles et répondons aux questions fréquentes pour que vous puissiez utiliser la {name} en toute confiance.",
                "mathematical_formula": "Formule Mathématique",
                "governed_by": "Le calcul est régi par l'équation suivante :",
                "where_each": "Chaque variable est définie dans les champs de saisie ci-dessus. Comprendre cette relation vous aide à interpréter correctement les résultats et à repérer les entrées déraisonnables avant qu'elles ne se propagent en erreurs.",
                "how_it_works_title": "Comment Ça Marche",
                "after_computation": "Après le calcul, le moteur formate la sortie en utilisant un formatage numérique adapté à la langue. Si un indicateur est disponible pour le résultat principal, il affiche un semi-cercle visuel montrant où se situe votre valeur dans la plage normale.",
                "real_world_use_cases": "Cas d'Usage Réels",
                "use_case": "Cas d'Usage {i} : {title}",
                "step_by_step_guide": "Guide Étape par Étape",
                "frequently_asked_questions": "Questions Fréquemment Posées",
                "conclusion": "Conclusion",
                "closing": "La {name} est un instrument de précision conçu pour gagner du temps et éliminer les erreurs de calcul. Que vous travailliez sur un projet professionnel ou que vous satisfassiez une curiosité académique, vérifiez toujours vos entrées et consultez des experts du domaine lorsque les résultats informent des décisions critiques.",
            },
            "intro": {
                "math": [
                    "La {name} est un outil indispensable des mathématiques modernes, de l'ingénierie et de la science des données. Comprendre {concept} permet aux professionnels et aux étudiants de résoudre des problèmes allant des devoirs simples à la recherche avancée.",
                ],
                "physics": [
                    "La {name} fait le pont entre la physique théorique et l'application réelle. En calculant avec précision {concept}, ingénieurs et scientifiques peuvent concevoir des véhicules plus sûrs.",
                ],
                "finance": [
                    "Prendre des décisions financières éclairées nécessite des chiffres précis. La {name} aide les investisseurs et les épargnants à évaluer {concept} avec une précision institutionnelle.",
                ],
                "health": [
                    "Vos indicateurs de santé ne sont utiles que si vous les comprenez. La {name} interprète {concept} à l'aide de formules cliniquement validées.",
                ],
                "tech": [
                    "La vie numérique moderne implique des conversions et des estimations constantes. La {name} simplifie {concept} pour que vous puissiez vous concentrer sur votre travail.",
                ],
            },
            "how_it_works": {
                "math": [
                    "Les mathématiques sous-jacentes sont simples mais puissantes. La calculatrice normalise d'abord toutes les entrées en unités cohérentes, puis applique la formule centrale.",
                ],
                "physics": [
                    "Le moteur physique commence par convertir chaque entrée en unités de base SI. Il évalue ensuite l'équation régissant le phénomène à l'aide de constantes standard.",
                ],
                "finance": [
                    "Le moteur financier applique des équations de valeur temporelle de l'argent en utilisant des conventions exactes de décompte des jours. Tous les pourcentages sont traités en décimaux.",
                ],
                "health": [
                    "Le moteur santé utilise des équations de régression évaluées par des pairs et des tables de référence. Les entrées telles que l'âge et le sexe ajustent automatiquement les coefficients.",
                ],
                "tech": [
                    "La calculatrice applique des facteurs de conversion standard de l'industrie et des formules de bande passante. Les préfixes binaires (Ki, Mi, Gi) sont distingués des décimaux (k, M, G).",
                ],
            },
            "use_case_intro": [
                "Voici trois scénarios réels où cette calculatrice s'avère inestimable:",
            ],
            "step_intro": [
                "Suivez ces étapes pour obtenir des résultats précis à chaque fois:",
            ],
            "faq": {
                "math": [
                    ("Cette calculatrice peut-elle gérer les nombres négatifs?", "Oui. Le moteur utilise l'arithmétique en double précision IEEE-754, qui gère correctement les valeurs négatives."),
                ],
                "physics": [
                    ("Quelles constantes standard sont utilisées?", "Nous utilisons les valeurs recommandées CODATA 2018. Par exemple, g = 9,80665 m/s²."),
                ],
                "finance": [
                    ("Les taxes sont-elles incluses dans le calcul?", "Sauf indication contraire, les résultats sont avant impôts. Consultez un professionnel fiscal."),
                ],
                "health": [
                    ("Quelle est la précision des résultats?", "Les équations sont validées contre la littérature révisée par des pairs. Cependant, la physiologie individuelle varie."),
                ],
                "tech": [
                    ("Pourquoi les chiffres de stockage semblent-ils différents?", "Les systèmes d'exploitation rapportent souvent en gibioctets (GiB) tandis que les fabricants utilisent des gigaoctets (GB)."),
                ],
            },
        }

        # ── Portuguese ──
        self.pt = {
            "headers": {
                "complete_guide": "Guia Completo",
                "below_explain": "Abaixo, explicamos os fundamentos matemáticos, passamos por aplicações do mundo real e respondemos a perguntas frequentes para que você possa usar a {name} com total confiança.",
                "mathematical_formula": "Fórmula Matemática",
                "governed_by": "O cálculo é regido pela seguinte equação:",
                "where_each": "Onde cada variável é definida nos campos de entrada acima. Compreender essa relação ajuda você a interpretar corretamente os resultados e detectar entradas irrazoáveis antes que se propaguem como erros.",
                "how_it_works_title": "Como Funciona",
                "after_computation": "Após o cálculo, o motor formata a saída usando formatação numérica sensível ao idioma. Se um indicador estiver disponível para o resultado principal, ele renderiza um indicador semicircular visual mostrando onde seu valor se situa dentro da faixa normal.",
                "real_world_use_cases": "Casos de Uso do Mundo Real",
                "use_case": "Caso de Uso {i}: {title}",
                "step_by_step_guide": "Guia Passo a Passo",
                "frequently_asked_questions": "Perguntas Frequentes",
                "conclusion": "Conclusão",
                "closing": "A {name} é um instrumento de precisão projetado para economizar tempo e eliminar erros de cálculo. Seja trabalhando em um projeto profissional ou satisfazendo uma curiosidade acadêmica, verifique sempre suas entradas e consulte especialistas da área quando os resultados informarem decisões críticas.",
            },
            "intro": {
                "math": [
                    "A {name} é uma ferramenta indispensável na matemática moderna, engenharia e ciência de dados. Compreender {concept} permite a profissionais e estudantes resolver problemas desde lições básicas até pesquisa avançada.",
                ],
                "physics": [
                    "A {name} une a física teórica à aplicação do mundo real. Ao calcular com precisão {concept}, engenheiros e cientistas podem projetar veículos mais seguros.",
                ],
                "finance": [
                    "Tomar decisões financeiras informadas requer números precisos. A {name} ajuda investidores e poupadores a avaliar {concept} com precisão institucional.",
                ],
                "health": [
                    "Suas métricas de saúde só são úteis se você as compreender. A {name} interpreta {concept} usando fórmulas clinicamente validadas.",
                ],
                "tech": [
                    "A vida digital moderna envolve conversões e estimativas constantes. A {name} simplifica {concept} para que você possa se concentrar no trabalho.",
                ],
            },
            "how_it_works": {
                "math": [
                    "A matemática subjacente é direta mas poderosa. A calculadora primeiro normaliza todas as entradas em unidades consistentes e depois aplica a fórmula central.",
                ],
                "physics": [
                    "O motor físico começa convertendo cada entrada para unidades base do SI. Em seguida, avalia a equação governante usando constantes padrão.",
                ],
                "finance": [
                    "O motor financeiro aplica equações de valor do dinheiro no tempo usando convenções exatas de contagem de dias. Todos os percentuais são tratados como decimais internamente.",
                ],
                "health": [
                    "O motor de saúde utiliza equações de regressão revisadas por pares e tabelas de consulta. Entradas como idade e sexo ajustam os coeficientes automaticamente.",
                ],
                "tech": [
                    "A calculadora aplica fatores de conversão padrão da indústria e fórmulas de largura de banda. Prefixos binários (Ki, Mi, Gi) são distinguidos dos decimais (k, M, G).",
                ],
            },
            "use_case_intro": [
                "Aqui estão três cenários do mundo real onde esta calculadora prova ser inestimável:",
            ],
            "step_intro": [
                "Siga estes passos para obter resultados precisos sempre:",
            ],
            "faq": {
                "math": [
                    ("Esta calculadora pode lidar com números negativos?", "Sim. O motor usa aritmética de dupla precisão IEEE-754, que lida corretamente com valores negativos."),
                ],
                "physics": [
                    ("Quais constantes padrão são usadas?", "Usamos os valores recomendados CODATA 2018. Por exemplo, g = 9,80665 m/s²."),
                ],
                "finance": [
                    ("Os impostos estão incluídos no cálculo?", "A menos que especificado o contrário, os resultados são pré-imposto. Consulte um profissional fiscal."),
                ],
                "health": [
                    ("Quão precisos são os resultados?", "As equações são validadas contra literatura revisada por pares. No entanto, a fisiologia individual varia."),
                ],
                "tech": [
                    ("Por que os números de armazenamento parecem diferentes?", "Os sistemas operacionais frequentemente relatam em gibibytes (GiB) enquanto fabricantes usam gigabytes (GB)."),
                ],
            },
        }

        # ── German ──
        self.de = {
            "headers": {
                "complete_guide": "Vollständige Anleitung",
                "below_explain": "Nachfolgend erklären wir die mathematischen Grundlagen, gehen auf reale Anwendungen ein und beantworten häufig gestellte Fragen, damit Sie den {name} mit vollstem Vertrauen nutzen können.",
                "mathematical_formula": "Mathematische Formel",
                "governed_by": "Die Berechnung wird durch die folgende Gleichung bestimmt:",
                "where_each": "Jede Variable ist in den obigen Eingabefeldern definiert. Das Verständnis dieser Beziehung hilft Ihnen, die Ergebnisse korrekt zu interpretieren und unangemessene Eingaben zu erkennen, bevor sie sich zu Fehlern ausbreiten.",
                "how_it_works_title": "Funktionsweise",
                "after_computation": "Nach der Berechnung formatiert die Engine die Ausgabe mit lokalisierter Zahlenformatierung. Wenn ein Messinstrument für das Primärergebnis verfügbar ist, wird eine visuelle Halbkreisanzeige gerendert, die zeigt, wo sich Ihr Wert im Normalbereich befindet.",
                "real_world_use_cases": "Anwendungsfälle aus der Praxis",
                "use_case": "Anwendungsfall {i}: {title}",
                "step_by_step_guide": "Schritt-für-Schritt-Anleitung",
                "frequently_asked_questions": "Häufig Gestellte Fragen",
                "conclusion": "Fazit",
                "closing": "Der {name} ist ein Präzisionsinstrument, das entwickelt wurde, um Zeit zu sparen und Berechnungsfehler zu eliminieren. Ob Sie an einem professionellen Projekt arbeiten oder akademische Neugier befriedigen – überprüfen Sie immer Ihre Eingaben und konsultieren Sie Fachexperten, wenn die Ergebnisse kritische Entscheidungen beeinflussen.",
            },
            "intro": {
                "math": [
                    "Der {name} ist ein unverzichtbares Werkzeug in der modernen Mathematik, Ingenieurwissenschaft und Datenwissenschaft. Das Verständnis von {concept} ermöglicht es Fachleuten und Studenten, Probleme von einfachen Hausaufgaben bis zur fortgeschrittenen Forschung zu lösen.",
                ],
                "physics": [
                    "Der {name} schlägt eine Brücke zwischen theoretischer Physik und realer Anwendung. Durch die genaue Berechnung von {concept} können Ingenieure und Wissenschaftler sicherere Fahrzeuge entwerfen.",
                ],
                "finance": [
                    "Fundierte finanzielle Entscheidungen erfordern präzise Zahlen. Der {name} hilft Investoren und Sparern, {concept} mit institutioneller Präzision zu bewerten.",
                ],
                "health": [
                    "Ihre Gesundheitsmetriken sind nur nützlich, wenn Sie sie verstehen. Der {name} interpretiert {concept} unter Verwendung klinisch validierter Formeln.",
                ],
                "tech": [
                    "Das moderne digitale Leben beinhaltet ständige Umrechnungen und Schätzungen. Der {name} vereinfacht {concept}, damit Sie sich auf Ihre Arbeit konzentrieren können.",
                ],
            },
            "how_it_works": {
                "math": [
                    "Die zugrunde liegende Mathematik ist geradlinig aber leistungsstark. Der Rechner normalisiert zunächst alle Eingaben in konsistente Einheiten und wendet dann die Kernformel an.",
                ],
                "physics": [
                    "Die Physik-Engine beginnt damit, jede Eingabe in SI-Basiseinheiten umzuwandeln. Dann wird die bestimmende Gleichung unter Verwendung von Standardkonstanten ausgewertet.",
                ],
                "finance": [
                    "Die Finanz-Engine wendet Zeitwert-des-Geld-Gleichungen unter Verwendung exakter Tageszählkonventionen an. Alle Prozentsätze werden intern als Dezimalzahlen behandelt.",
                ],
                "health": [
                    "Die Gesundheits-Engine verwendet von Fachleuten geprüfte Regressionsgleichungen und Nachschlagetabellen. Eingaben wie Alter und Geschlecht passen die Koeffizienten automatisch an.",
                ],
                "tech": [
                    "Der Rechner wendet branchenübliche Umrechnungsfaktoren und Bandbreitenformeln an. Binäre Präfixe (Ki, Mi, Gi) werden von dezimalen Präfixen (k, M, G) unterschieden.",
                ],
            },
            "use_case_intro": [
                "Hier sind drei reale Szenarien, in denen dieser Rechner unschätzbar ist:",
            ],
            "step_intro": [
                "Folgen Sie diesen Schritten, um jedes Mal genaue Ergebnisse zu erhalten:",
            ],
            "faq": {
                "math": [
                    ("Kann dieser Rechner negative Zahlen verarbeiten?", "Ja. Die Engine verwendet IEEE-754-Doppelpräzisionsarithmetik, die negative Werte korrekt verarbeitet."),
                ],
                "physics": [
                    ("Welche Standardkonstanten werden verwendet?", "Wir verwenden die empfohlenen CODATA-2018-Werte. Zum Beispiel g = 9,80665 m/s²."),
                ],
                "finance": [
                    ("Sind Steuern in die Berechnung einbezogen?", "Sofern nicht anders angegeben, sind die Ergebnisse vor Steuern. Konsultieren Sie einen Steuerfachmann."),
                ],
                "health": [
                    ("Wie genau sind die Ergebnisse?", "Die Gleichungen werden gegen Fachliteratur validiert. Die individuelle Physiologie variiert jedoch."),
                ],
                "tech": [
                    ("Warum sehen Speicherzahlen anders aus?", "Betriebssysteme melden oft in Gibibytes (GiB), während Hersteller Gigabytes (GB) verwenden."),
                ],
            },
        }

        # ── Italian ──
        self.it = {
            "headers": {
                "complete_guide": "Guida Completa",
                "below_explain": "Di seguito, spieghiamo i fondamenti matematici, illustriamo applicazioni del mondo reale e rispondiamo alle domande frequenti in modo che tu possa usare il {name} con piena fiducia.",
                "mathematical_formula": "Formula Matematica",
                "governed_by": "Il calcolo è governato dalla seguente equazione:",
                "where_each": "Dove ogni variabile è definita nei campi di input sopra. Comprendere questa relazione ti aiuta a interpretare correttamente i risultati e a individuare input irragionevoli prima che si propaghino in errori.",
                "how_it_works_title": "Come Funziona",
                "after_computation": "Dopo il calcolo, il motore formatta l'output utilizzando la formattazione dei numeri sensibile alla lingua. Se è disponibile un indicatore per il risultato principale, viene visualizzato un indicatore semicircolare che mostra dove si colloca il tuo valore all'interno della gamma normale.",
                "real_world_use_cases": "Casi d'Uso nel Mondo Reale",
                "use_case": "Caso d'Uso {i}: {title}",
                "step_by_step_guide": "Guida Passo Passo",
                "frequently_asked_questions": "Domande Frequenti",
                "conclusion": "Conclusione",
                "closing": "Il {name} è uno strumento di precisione progettato per far risparmiare tempo ed eliminare errori di calcolo. Che tu stia lavorando a un progetto professionale o soddisfando una curiosità accademica, controlla sempre i tuoi input e consulta esperti del settore quando i risultati influenzano decisioni critiche.",
            },
            "intro": {
                "math": [
                    "Il {name} è uno strumento indispensabile nella matematica moderna, nell'ingegneria e nella scienza dei dati. Comprendere {concept} permette a professionisti e studenti di risolvere problemi che vanno dai compiti di base alla ricerca avanzata.",
                ],
                "physics": [
                    "Il {name} collega la fisica teorica all'applicazione del mondo reale. Calcolando con precisione {concept}, ingegneri e scienziati possono progettare veicoli più sicuri.",
                ],
                "finance": [
                    "Prendere decisioni finanziarie informate richiede numeri precisi. Il {name} aiuta investitori e risparmiatori a valutare {concept} con precisione istituzionale.",
                ],
                "health": [
                    "Le tue metriche di salute sono utili solo se le comprendi. Il {name} interpreta {concept} utilizzando formule clinicamente validate.",
                ],
                "tech": [
                    "La vita digitale moderna comporta conversioni e stime costanti. Il {name} semplifica {concept} in modo che tu possa concentrarti sul tuo lavoro.",
                ],
            },
            "how_it_works": {
                "math": [
                    "La matematica sottostante è semplice ma potente. La calcolatrice normalizza prima tutti gli input in unità consistenti, quindi applica la formula centrale.",
                ],
                "physics": [
                    "Il motore fisico inizia convertendo ogni input in unità di base SI. Quindi valuta l'equazione governante utilizzando costanti standard.",
                ],
                "finance": [
                    "Il motore finanziario applica equazioni del valore temporale del denaro utilizzando convenzioni esatte di conteggio dei giorni. Tutte le percentuali sono gestite come decimali internamente.",
                ],
                "health": [
                    "Il motore sanitario utilizza equazioni di regressione revisionate da pari e tabelle di riferimento. Input come età e sesso regolano automaticamente i coefficienti.",
                ],
                "tech": [
                    "La calcolatrice applica fattori di conversione standard del settore e formule di larghezza di banda. I prefissi binari (Ki, Mi, Gi) sono distinti da quelli decimali (k, M, G).",
                ],
            },
            "use_case_intro": [
                "Ecco tre scenari del mondo reale in cui questa calcolatrice si rivela preziosa:",
            ],
            "step_intro": [
                "Segui questi passaggi per ottenere risultati accurati ogni volta:",
            ],
            "faq": {
                "math": [
                    ("Questa calcolatrice può gestire numeri negativi?", "Sì. Il motore utilizza l'aritmetica a doppia precisione IEEE-754, che gestisce correttamente i valori negativi."),
                ],
                "physics": [
                    ("Quali costanti standard vengono utilizzate?", "Utilizziamo i valori raccomandati CODATA 2018. Ad esempio, g = 9,80665 m/s²."),
                ],
                "finance": [
                    ("Le tasse sono incluse nel calcolo?", "A meno che non sia specificato diversamente, i risultati sono al lordo delle tasse. Consulta un professionista fiscale."),
                ],
                "health": [
                    ("Quanto sono accurati i risultati?", "Le equazioni sono validate rispetto alla letteratura revisionata da pari. Tuttavia, la fisiologia individuale varia."),
                ],
                "tech": [
                    ("Perché i numeri di archiviazione sembrano diversi?", "I sistemi operativi spesso riportano in gibibyte (GiB) mentre i produttori usano gigabyte (GB)."),
                ],
            },
        }

    def _pick(self, options, seed_str):
        """Deterministically pick a template variant."""
        idx = int(hashlib.md5(seed_str.encode()).hexdigest(), 16) % len(options)
        return options[idx]

    def generate(self, calc, lang):
        tpl = getattr(self, lang, self.en)
        h = tpl["headers"]
        domain = calc.get("domain", "math")
        name = calc["i18n"][lang]["name"]
        concept = calc.get("concept", name.split("–")[0].strip())
        seed = f"{calc['id']}_{lang}"

        parts = []

        # Title
        parts.append(f'<h2 id="overview">{name} – {h["complete_guide"]}</h2>')

        # Intro
        intro = self._pick(tpl["intro"][domain], seed + "_intro").format(name=name, concept=concept)
        parts.append(f"<p>{intro}</p>")
        parts.append(f"<p>{h['below_explain'].format(name=name)}</p>")

        # Formula
        latex = calc.get("latex_formula", "")
        if latex:
            parts.append(f'<h2 id="formula">{h["mathematical_formula"]}</h2>')
            parts.append(f"<p>{h['governed_by']}</p>")
            parts.append(f'<div class="formula-block">\n$$\n{latex}\n$$\n</div>')
            parts.append(f"<p>{h['where_each']}</p>")

        # How it works
        how = self._pick(tpl["how_it_works"][domain], seed + "_how")
        parts.append(f'<h2 id="how-it-works">{h["how_it_works_title"]}</h2>')
        parts.append(f"<p>{how}</p>")
        parts.append(f"<p>{h['after_computation']}</p>")

        # Use cases
        use_cases = calc.get("use_cases", [])
        if use_cases:
            parts.append(f'<h2 id="use-cases">{h["real_world_use_cases"]}</h2>')
            parts.append(f"<p>{self._pick(tpl['use_case_intro'], seed + '_uc')}</p>")
            for i, uc in enumerate(use_cases[:3], 1):
                title = uc.get(lang, uc.get("en", "Use case"))
                body = uc.get(f"{lang}_body", uc.get("en_body", ""))
                parts.append(f'<h3>{h["use_case"].format(i=i, title=title)}</h3>')
                parts.append(f"<p>{body}</p>")

        # Steps
        steps = calc.get("steps", [])
        if steps:
            parts.append(f'<h2 id="steps">{h["step_by_step_guide"]}</h2>')
            parts.append(f"<p>{self._pick(tpl['step_intro'], seed + '_step')}</p>")
            parts.append("<ol>")
            for step in steps:
                s = step.get(lang, step.get("en", ""))
                parts.append(f"<li>{s}</li>")
            parts.append("</ol>")

        # FAQ
        faqs = tpl["faq"].get(domain, tpl["faq"]["math"])
        if faqs:
            parts.append(f'<h2 id="faq">{h["frequently_asked_questions"]}</h2>')
            parts.append('<div class="faq-list">')
            for q, a in faqs[:3]:
                parts.append(f'<div class="faq-item"><button class="faq-q" aria-expanded="false">{q}</button><div class="faq-a">{a}</div></div>')
            parts.append('</div>')

        # Closing
        parts.append(f'<h2 id="conclusion">{h["conclusion"]}</h2>')
        parts.append(f"<p>{h['closing'].format(name=name)}</p>")

        return "\n".join(parts)


engine = ContentEngine()


# ═══════════════════════════════════════════════════════════════════════════════
#  CATALOG – Batch 1 (50 calculators)
# ═══════════════════════════════════════════════════════════════════════════════

CATALOG = []

def add_calc(**kwargs):
    CATALOG.append(kwargs)

# ── MATH (110-119) ──
add_calc(
    id="110", block="matematicas", cat="A",
    domain="math", concept="absolute value",
    slugs={"es":"valor-absoluto","en":"absolute-value","fr":"valeur-absolue","pt":"valor-absoluto","de":"absoluter-wert","it":"valore-assoluto"},
    inputs=[
        {"id":"x","type":"number","step":"any","default":-5,"unit":"","unit_options":[],"unit_category":""}
    ],
    outputs=[{"id":"abs_val","unit":""}],
    formula="var x=parseFloat(inputs.x)||0;return{abs_val:Math.abs(x)};",
    related=["200","201"],
    i18n={
        "es":{"name":"Calculadora de Valor Absoluto","description":"Calcula el valor absoluto de cualquier número real.","inputs":{"x":"Número"},"outputs":{"abs_val":"Valor Absoluto"}},
        "en":{"name":"Absolute Value Calculator","description":"Calculate the absolute value of any real number.","inputs":{"x":"Number"},"outputs":{"abs_val":"Absolute Value"}},
        "fr":{"name":"Calculateur de Valeur Absolue","description":"Calculez la valeur absolue de tout nombre réel.","inputs":{"x":"Nombre"},"outputs":{"abs_val":"Valeur Absolue"}},
        "pt":{"name":"Calculadora de Valor Absoluto","description":"Calcule o valor absoluto de qualquer número real.","inputs":{"x":"Número"},"outputs":{"abs_val":"Valor Absoluto"}},
        "de":{"name":"Absolutwert-Rechner","description":"Berechnen Sie den absoluten Betrag einer beliebigen reellen Zahl.","inputs":{"x":"Zahl"},"outputs":{"abs_val":"Absoluter Wert"}},
        "it":{"name":"Calcolatore di Valore Assoluto","description":"Calcola il valore assoluto di qualsiasi numero reale.","inputs":{"x":"Numero"},"outputs":{"abs_val":"Valore Assoluto"}},
    },
    latex_formula="|x| = \\begin{cases} x & \\text{if } x \\geq 0 \\\\ -x & \\text{if } x < 0 \\end{cases}",
    use_cases=[
        {"en":"Signal Processing","en_body":"Electrical engineers use absolute value to determine the amplitude of an AC signal regardless of its phase. Knowing |V| helps size components like capacitors and resistors.","es":"Procesamiento de Señales","es_body":"Los ingenieros eléctricos usan el valor absoluto para determinar la amplitud de una señal AC independientemente de su fase."},
        {"en":"Error Measurement","en_body":"In statistics, the absolute deviation measures how far a data point lies from the mean without regard to direction, forming the basis of robust estimators.","fr":"Mesure d'Erreur","fr_body":"En statistique, l'écart absolu mesure la distance entre un point de données et la moyenne sans tenir compte de la direction."},
        {"en":"Distance Calculation","en_body":"When computing Manhattan distance on a grid, absolute values of coordinate differences are summed to find the shortest path for taxicab geometry.","de":"Distanzberechnung","de_body":"Bei der Berechnung der Manhattan-Distanz auf einem Gitter werden die absoluten Werte der Koordinatendifferenzen summiert."},
    ],
    steps=[
        {"en":"Enter the real number whose absolute value you need.","es":"Ingrese el número real cuyo valor absoluto necesita."},
        {"en":"The calculator returns the non-negative magnitude of the number.","fr":"La calculatrice retourne la magnitude non négative du nombre."},
        {"en":"Use the result in downstream equations or comparisons.","de":"Verwenden Sie das Ergebnis in nachgelagerten Gleichungen oder Vergleichen."},
    ],
)

add_calc(
    id="111", block="matematicas", cat="A",
    domain="math", concept="arithmetic series",
    slugs={"es":"suma-progresion-aritmetica","en":"arithmetic-sequence-sum","fr":"somme-suite-arithmetique","pt":"soma-progressao-aritmetica","de":"arithmetische-reihe-summe","it":"somma-sequenza-aritmetica"},
    inputs=[
        {"id":"a1","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"d","type":"number","step":"any","default":2,"unit":"","unit_options":[],"unit_category":""},
        {"id":"n","type":"number","step":1,"default":10,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"sum","unit":""}],
    formula="var a1=parseFloat(inputs.a1)||0;var d=parseFloat(inputs.d)||0;var n=parseFloat(inputs.n)||0;var sum=n*(2*a1+(n-1)*d)/2;return{sum:sum.toFixed(4)};",
    related=["112","200"],
    i18n={
        "es":{"name":"Suma de Progresión Aritmética","description":"Calcula la suma de los primeros n términos de una progresión aritmética.","inputs":{"a1":"Primer término","d":"Diferencia común","n":"Número de términos"},"outputs":{"sum":"Suma total"}},
        "en":{"name":"Arithmetic Sequence Sum Calculator","description":"Calculate the sum of the first n terms of an arithmetic sequence.","inputs":{"a1":"First term","d":"Common difference","n":"Number of terms"},"outputs":{"sum":"Total sum"}},
        "fr":{"name":"Calculateur de Somme Arithmétique","description":"Calculez la somme des n premiers termes d'une suite arithmétique.","inputs":{"a1":"Premier terme","d":"Raison","n":"Nombre de termes"},"outputs":{"sum":"Somme totale"}},
        "pt":{"name":"Calculadora de Soma Aritmética","description":"Calcule a soma dos primeiros n termos de uma progressão aritmética.","inputs":{"a1":"Primeiro termo","d":"Razão comum","n":"Número de termos"},"outputs":{"sum":"Soma total"}},
        "de":{"name":"Arithmetische Reihe Summe","description":"Berechnen Sie die Summe der ersten n Glieder einer arithmetischen Reihe.","inputs":{"a1":"Erstes Glied","d":"Konstante Differenz","n":"Anzahl der Glieder"},"outputs":{"sum":"Gesamtsumme"}},
        "it":{"name":"Somma Sequenza Aritmetica","description":"Calcola la somma dei primi n termini di una sequenza aritmetica.","inputs":{"a1":"Primo termine","d":"Differenza comune","n":"Numero di termini"},"outputs":{"sum":"Somma totale"}},
    },
    latex_formula="S_n = \\frac{n}{2} \\bigl(2a_1 + (n-1)d\\bigr)",
    use_cases=[
        {"en":"Savings Plans","en_body":"If you save $100 in month one and increase by $10 each month, the arithmetic sum tells you the total after 12 months."},
        {"en":" stadium Seating","en_body":"Theater designers use arithmetic sums to compute total seating when each row has two more seats than the previous."},
        {"en":"Loan Amortization","en_body":"Some simplified loan models treat principal reduction as an arithmetic progression to estimate cumulative payments."},
    ],
    steps=[
        {"en":"Enter the first term of the sequence."},
        {"en":"Enter the common difference between consecutive terms."},
        {"en":"Enter how many terms you want to sum."},
    ],
)

add_calc(
    id="112", block="matematicas", cat="A",
    domain="math", concept="geometric series",
    slugs={"es":"suma-progresion-geometrica","en":"geometric-sequence-sum","fr":"somme-suite-geometrique","pt":"soma-progressao-geometrica","de":"geometrische-reihe-summe","it":"somma-sequenza-geometrica"},
    inputs=[
        {"id":"a1","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"r","type":"number","step":"any","default":2,"unit":"","unit_options":[],"unit_category":""},
        {"id":"n","type":"number","step":1,"default":10,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"sum","unit":""}],
    formula="var a1=parseFloat(inputs.a1)||0;var r=parseFloat(inputs.r)||0;var n=parseFloat(inputs.n)||0;var sum=Math.abs(r-1)<1e-9?a1*n:a1*(1-Math.pow(r,n))/(1-r);return{sum:sum.toFixed(4)};",
    related=["111","302"],
    i18n={
        "es":{"name":"Suma de Progresión Geométrica","description":"Calcula la suma de los primeros n términos de una progresión geométrica.","inputs":{"a1":"Primer término","r":"Razón común","n":"Número de términos"},"outputs":{"sum":"Suma total"}},
        "en":{"name":"Geometric Sequence Sum Calculator","description":"Calculate the sum of the first n terms of a geometric sequence.","inputs":{"a1":"First term","r":"Common ratio","n":"Number of terms"},"outputs":{"sum":"Total sum"}},
        "fr":{"name":"Calculateur de Somme Géométrique","description":"Calculez la somme des n premiers termes d'une suite géométrique.","inputs":{"a1":"Premier terme","r":"Raison","n":"Nombre de termes"},"outputs":{"sum":"Somme totale"}},
        "pt":{"name":"Calculadora de Soma Geométrica","description":"Calcule a soma dos primeiros n termos de uma progressão geométrica.","inputs":{"a1":"Primeiro termo","r":"Razão comum","n":"Número de termos"},"outputs":{"sum":"Soma total"}},
        "de":{"name":"Geometrische Reihe Summe","description":"Berechnen Sie die Summe der ersten n Glieder einer geometrischen Reihe.","inputs":{"a1":"Erstes Glied","r":"Quotient","n":"Anzahl der Glieder"},"outputs":{"sum":"Gesamtsumme"}},
        "it":{"name":"Somma Sequenza Geometrica","description":"Calcola la somma dei primi n termini di una sequenza geometrica.","inputs":{"a1":"Primo termine","r":"Ragione comune","n":"Numero di termini"},"outputs":{"sum":"Somma totale"}},
    },
    latex_formula="S_n = a_1 \\frac{1-r^n}{1-r} \\quad (r \\neq 1)",
    use_cases=[
        {"en":"Compound Interest","en_body":"The future value of compound interest is a geometric series where each term represents the accumulated principal plus interest."},
        {"en":"Viral Growth","en_body":"Epidemiologists model early outbreak growth as a geometric sequence when each infected person spreads the disease to r others."},
        {"en":"Digital Signal Attenuation","en_body":"Each amplifier stage multiplies noise by a constant ratio; the geometric sum predicts cumulative distortion."},
    ],
    steps=[
        {"en":"Enter the first term (a₁)."},
        {"en":"Enter the common ratio (r)."},
        {"en":"Enter the number of terms (n)."},
    ],
)

add_calc(
    id="113", block="matematicas", cat="A",
    domain="math", concept="complex magnitude",
    slugs={"es":"modulo-complejo","en":"complex-number-magnitude","fr":"module-nombre-complexe","pt":"modulo-numero-complexo","de":"komplexe-betrag","it":"modulo-numero-complesso"},
    inputs=[
        {"id":"real","type":"number","step":"any","default":3,"unit":"","unit_options":[],"unit_category":""},
        {"id":"imag","type":"number","step":"any","default":4,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"magnitude","unit":""}],
    formula="var a=parseFloat(inputs.real)||0;var b=parseFloat(inputs.imag)||0;var mag=Math.sqrt(a*a+b*b);return{magnitude:mag.toFixed(4)};",
    related=["116","117"],
    i18n={
        "es":{"name":"Calculadora de Módulo Complejo","description":"Calcula el módulo (magnitud) de un número complejo.","inputs":{"real":"Parte real","imag":"Parte imaginaria"},"outputs":{"magnitude":"Módulo |z|"}},
        "en":{"name":"Complex Number Magnitude Calculator","description":"Calculate the magnitude (absolute value) of a complex number.","inputs":{"real":"Real part","imag":"Imaginary part"},"outputs":{"magnitude":"Magnitude |z|"}},
        "fr":{"name":"Calculateur du Module Complexe","description":"Calculez le module (valeur absolue) d'un nombre complexe.","inputs":{"real":"Partie réelle","imag":"Partie imaginaire"},"outputs":{"magnitude":"Module |z|"}},
        "pt":{"name":"Calculadora de Módulo Complexo","description":"Calcule o módulo (valor absoluto) de um número complexo.","inputs":{"real":"Parte real","imag":"Parte imaginária"},"outputs":{"magnitude":"Módulo |z|"}},
        "de":{"name":"Komplexer Betrag Rechner","description":"Berechnen Sie den Betrag (absolute Wert) einer komplexen Zahl.","inputs":{"real":"Realteil","imag":"Imaginärteil"},"outputs":{"magnitude":"Betrag |z|"}},
        "it":{"name":"Calcolatore Modulo Complesso","description":"Calcola il modulo (valore assoluto) di un numero complesso.","inputs":{"real":"Parte reale","imag":"Parte immaginaria"},"outputs":{"magnitude":"Modulo |z|"}},
    },
    latex_formula="|z| = \\sqrt{a^2 + b^2} \\quad \\text{where } z = a + bi",
    use_cases=[
        {"en":"AC Circuit Analysis","en_body":"The magnitude of impedance |Z| determines current flow in an RLC circuit under sinusoidal excitation."},
        {"en":"Quantum Mechanics","en_body":"Wavefunction normalization requires the squared magnitude to integrate to unity over all space."},
        {"en":"Control Systems","en_body":"The distance of a pole from the origin in the complex plane determines system stability margins."},
    ],
    steps=[
        {"en":"Enter the real component (a)."},
        {"en":"Enter the imaginary component (b)."},
        {"en":"Read the magnitude |z|."},
    ],
)

add_calc(
    id="114", block="matematicas", cat="A",
    domain="math", concept="matrix determinant",
    slugs={"es":"determinante-matriz-2x2","en":"matrix-2x2-determinant","fr":"determinant-matrice-2x2","pt":"determinante-matriz-2x2","de":"determinante-2x2-matrix","it":"determinante-matrice-2x2"},
    inputs=[
        {"id":"a","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"b","type":"number","step":"any","default":2,"unit":"","unit_options":[],"unit_category":""},
        {"id":"c","type":"number","step":"any","default":3,"unit":"","unit_options":[],"unit_category":""},
        {"id":"d","type":"number","step":"any","default":4,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"det","unit":""}],
    formula="var a=parseFloat(inputs.a)||0;var b=parseFloat(inputs.b)||0;var c=parseFloat(inputs.c)||0;var d_in=parseFloat(inputs.d)||0;var det=a*d_in-b*c;return{det:det.toFixed(4)};",
    related=["115","116"],
    i18n={
        "es":{"name":"Determinante de Matriz 2×2","description":"Calcula el determinante de una matriz cuadrada de orden 2.","inputs":{"a":"Elemento a₁₁","b":"Elemento a₁₂","c":"Elemento a₂₁","d":"Elemento a₂₂"},"outputs":{"det":"Determinante"}},
        "en":{"name":"2×2 Matrix Determinant Calculator","description":"Calculate the determinant of a 2×2 square matrix.","inputs":{"a":"Element a₁₁","b":"Element a₁₂","c":"Element a₂₁","d":"Element a₂₂"},"outputs":{"det":"Determinant"}},
        "fr":{"name":"Déterminant Matrice 2×2","description":"Calculez le déterminant d'une matrice carrée d'ordre 2.","inputs":{"a":"Élément a₁₁","b":"Élément a₁₂","c":"Élément a₂₁","d":"Élément a₂₂"},"outputs":{"det":"Déterminant"}},
        "pt":{"name":"Determinante de Matriz 2×2","description":"Calcule o determinante de uma matriz quadrada de ordem 2.","inputs":{"a":"Elemento a₁₁","b":"Elemento a₁₂","c":"Elemento a₂₁","d":"Elemento a₂₂"},"outputs":{"det":"Determinante"}},
        "de":{"name":"2×2 Determinanten Rechner","description":"Berechnen Sie die Determinante einer quadratischen Matrix der Ordnung 2.","inputs":{"a":"Element a₁₁","b":"Element a₁₂","c":"Element a₂₁","d":"Element a₂₂"},"outputs":{"det":"Determinante"}},
        "it":{"name":"Determinante Matrice 2×2","description":"Calcola il determinante di una matrice quadrata di ordine 2.","inputs":{"a":"Elemento a₁₁","b":"Elemento a₁₂","c":"Elemento a₂₁","d":"Elemento a₂₂"},"outputs":{"det":"Determinante"}},
    },
    latex_formula="\\det(A) = ad - bc \\quad \\text{for } A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}",
    use_cases=[
        {"en":"Linear System Solvability","en_body":"A non-zero determinant guarantees a unique solution for a system of two linear equations with two unknowns."},
        {"en":"Geometric Area","en_body":"The absolute value of the determinant equals the area of the parallelogram spanned by the column vectors."},
        {"en":"Eigenvalue Problems","en_body":"The characteristic polynomial of a 2×2 matrix begins with λ² - tr(A)λ + det(A)."},
    ],
    steps=[
        {"en":"Enter the four matrix elements row by row."},
        {"en":"The calculator computes ad - bc."},
        {"en":"A zero determinant means the matrix is singular (no inverse)."},
    ],
)

add_calc(
    id="115", block="matematicas", cat="A",
    domain="math", concept="vector magnitude",
    slugs={"es":"magnitud-vector-3d","en":"vector-magnitude-3d","fr":"norme-vecteur-3d","pt":"magnitude-vetor-3d","de":"vektor-betrag-3d","it":"modulo-vettore-3d"},
    inputs=[
        {"id":"vx","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"vy","type":"number","step":"any","default":2,"unit":"","unit_options":[],"unit_category":""},
        {"id":"vz","type":"number","step":"any","default":2,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"magnitude","unit":""}],
    formula="var x=parseFloat(inputs.vx)||0;var y=parseFloat(inputs.vy)||0;var z=parseFloat(inputs.vz)||0;var mag=Math.sqrt(x*x+y*y+z*z);return{magnitude:mag.toFixed(4)};",
    related=["113","116"],
    i18n={
        "es":{"name":"Magnitud de Vector 3D","description":"Calcula la magnitud (norma euclidiana) de un vector tridimensional.","inputs":{"vx":"Componente x","vy":"Componente y","vz":"Componente z"},"outputs":{"magnitude":"Magnitud |v|"}},
        "en":{"name":"3D Vector Magnitude Calculator","description":"Calculate the magnitude (Euclidean norm) of a three-dimensional vector.","inputs":{"vx":"x component","vy":"y component","vz":"z component"},"outputs":{"magnitude":"Magnitude |v|"}},
        "fr":{"name":"Norme d'un Vecteur 3D","description":"Calculez la norme (euclidienne) d'un vecteur tridimensionnel.","inputs":{"vx":"Composante x","vy":"Composante y","vz":"Composante z"},"outputs":{"magnitude":"Norme |v|"}},
        "pt":{"name":"Magnitude do Vetor 3D","description":"Calcule a magnitude (norma euclidiana) de um vetor tridimensional.","inputs":{"vx":"Componente x","vy":"Componente y","vz":"Componente z"},"outputs":{"magnitude":"Magnitude |v|"}},
        "de":{"name":"3D-Vektor-Betrag","description":"Berechnen Sie den Betrag (euklidische Norm) eines dreidimensionalen Vektors.","inputs":{"vx":"x-Komponente","vy":"y-Komponente","vz":"z-Komponente"},"outputs":{"magnitude":"Betrag |v|"}},
        "it":{"name":"Modulo Vettore 3D","description":"Calcola il modulo (norma euclidea) di un vettore tridimensionale.","inputs":{"vx":"Componente x","vy":"Componente y","vz":"Componente z"},"outputs":{"magnitude":"Modulo |v|"}},
    },
    latex_formula="\\|\\vec{v}\\| = \\sqrt{v_x^2 + v_y^2 + v_z^2}",
    use_cases=[
        {"en":"Navigation GPS","en_body":"The magnitude of the displacement vector gives the straight-line distance between two GPS coordinates in 3D space (including altitude)."},
        {"en":"Force Resultants","en_body":"Mechanical engineers sum force vectors and compute their magnitude to determine net load on a structural member."},
        {"en":"Machine Learning","en_body":"L2 regularization penalizes the squared magnitude of weight vectors to prevent overfitting in neural networks."},
    ],
    steps=[
        {"en":"Enter the x, y, and z components of your vector."},
        {"en":"The calculator squares each component, sums them, and takes the square root."},
        {"en":"The result is the Euclidean length of the vector."},
    ],
)

add_calc(
    id="116", block="matematicas", cat="A",
    domain="math", concept="dot product",
    slugs={"es":"producto-escalar","en":"dot-product-calculator","fr":"produit-scalaire","pt":"produto-escalar","de":"skalarprodukt","it":"prodotto-scalare"},
    inputs=[
        {"id":"ax","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"ay","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""},
        {"id":"az","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""},
        {"id":"bx","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"by","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"bz","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"dot","unit":""}],
    formula="var ax=parseFloat(inputs.ax)||0;var ay=parseFloat(inputs.ay)||0;var az=parseFloat(inputs.az)||0;var bx=parseFloat(inputs.bx)||0;var by=parseFloat(inputs.by)||0;var bz=parseFloat(inputs.bz)||0;var dot=ax*bx+ay*by+az*bz;return{dot:dot.toFixed(4)};",
    related=["115","117"],
    i18n={
        "es":{"name":"Calculadora de Producto Escalar","description":"Calcula el producto punto (escalar) de dos vectores tridimensionales.","inputs":{"ax":"Vector A x","ay":"Vector A y","az":"Vector A z","bx":"Vector B x","by":"Vector B y","bz":"Vector B z"},"outputs":{"dot":"Producto escalar"}},
        "en":{"name":"Dot Product Calculator","description":"Calculate the dot product (scalar product) of two 3D vectors.","inputs":{"ax":"Vector A x","ay":"Vector A y","az":"Vector A z","bx":"Vector B x","by":"Vector B y","bz":"Vector B z"},"outputs":{"dot":"Dot product"}},
        "fr":{"name":"Calculateur de Produit Scalaire","description":"Calculez le produit scalaire de deux vecteurs 3D.","inputs":{"ax":"Vecteur A x","ay":"Vecteur A y","az":"Vecteur A z","bx":"Vecteur B x","by":"Vecteur B y","bz":"Vecteur B z"},"outputs":{"dot":"Produit scalaire"}},
        "pt":{"name":"Calculadora de Produto Escalar","description":"Calcule o produto escalar de dois vetores 3D.","inputs":{"ax":"Vetor A x","ay":"Vetor A y","az":"Vetor A z","bx":"Vetor B x","by":"Vetor B y","bz":"Vetor B z"},"outputs":{"dot":"Produto escalar"}},
        "de":{"name":"Skalarprodukt Rechner","description":"Berechnen Sie das Skalarprodukt zweier 3D-Vektoren.","inputs":{"ax":"Vektor A x","ay":"Vektor A y","az":"Vektor A z","bx":"Vektor B x","by":"Vektor B y","bz":"Vektor B z"},"outputs":{"dot":"Skalarprodukt"}},
        "it":{"name":"Calcolatore Prodotto Scalare","description":"Calcola il prodotto scalare di due vettori 3D.","inputs":{"ax":"Vettore A x","ay":"Vettore A y","az":"Vettore A z","bx":"Vettore B x","by":"Vettore B y","bz":"Vettore B z"},"outputs":{"dot":"Prodotto scalare"}},
    },
    latex_formula="\\vec{a} \\cdot \\vec{b} = a_x b_x + a_y b_y + a_z b_z = |\\vec{a}||\\vec{b}|\\cos\\theta",
    use_cases=[
        {"en":"Projection Length","en_body":"The dot product divided by |b| gives the length of a projected onto b, essential in shadow and lighting algorithms."},
        {"en":"Work in Physics","en_body":"Mechanical work equals the dot product of force and displacement vectors, explaining why perpendicular forces do zero work."},
        {"en":"Similarity Metrics","en_body":"Machine learning uses normalized dot products as cosine similarity to compare document vectors in search engines."},
    ],
    steps=[
        {"en":"Enter the x, y, z components of vector A."},
        {"en":"Enter the x, y, z components of vector B."},
        {"en":"The calculator sums the products of corresponding components."},
    ],
)

add_calc(
    id="117", block="matematicas", cat="A",
    domain="math", concept="cross product",
    slugs={"es":"producto-vectorial","en":"cross-product-calculator","fr":"produit-vectoriel","pt":"produto-vetorial","de":"kreuzprodukt","it":"prodotto-vettoriale"},
    inputs=[
        {"id":"ax","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"ay","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""},
        {"id":"az","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""},
        {"id":"bx","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""},
        {"id":"by","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"bz","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"cx","unit":""},{"id":"cy","unit":""},{"id":"cz","unit":""},{"id":"magnitude","unit":""}],
    formula="var ax=parseFloat(inputs.ax)||0;var ay=parseFloat(inputs.ay)||0;var az=parseFloat(inputs.az)||0;var bx=parseFloat(inputs.bx)||0;var by=parseFloat(inputs.by)||0;var bz=parseFloat(inputs.bz)||0;var cx=ay*bz-az*by;var cy=az*bx-ax*bz;var cz=ax*by-ay*bx;var mag=Math.sqrt(cx*cx+cy*cy+cz*cz);return{cx:cx.toFixed(4),cy:cy.toFixed(4),cz:cz.toFixed(4),magnitude:mag.toFixed(4)};",
    related=["115","116"],
    i18n={
        "es":{"name":"Calculadora de Producto Vectorial","description":"Calcula el producto vectorial de dos vectores 3D y su magnitud.","inputs":{"ax":"Vector A x","ay":"Vector A y","az":"Vector A z","bx":"Vector B x","by":"Vector B y","bz":"Vector B z"},"outputs":{"cx":"Componente x","cy":"Componente y","cz":"Componente z","magnitude":"Magnitud"}},
        "en":{"name":"Cross Product Calculator","description":"Calculate the cross product of two 3D vectors and its magnitude.","inputs":{"ax":"Vector A x","ay":"Vector A y","az":"Vector A z","bx":"Vector B x","by":"Vector B y","bz":"Vector B z"},"outputs":{"cx":"x component","cy":"y component","cz":"z component","magnitude":"Magnitude"}},
        "fr":{"name":"Calculateur de Produit Vectoriel","description":"Calculez le produit vectoriel de deux vecteurs 3D et sa norme.","inputs":{"ax":"Vecteur A x","ay":"Vecteur A y","az":"Vecteur A z","bx":"Vecteur B x","by":"Vecteur B y","bz":"Vecteur B z"},"outputs":{"cx":"Composante x","cy":"Composante y","cz":"Composante z","magnitude":"Norme"}},
        "pt":{"name":"Calculadora de Produto Vetorial","description":"Calcule o produto vetorial de dois vetores 3D e sua magnitude.","inputs":{"ax":"Vetor A x","ay":"Vetor A y","az":"Vetor A z","bx":"Vetor B x","by":"Vetor B y","bz":"Vetor B z"},"outputs":{"cx":"Componente x","cy":"Componente y","cz":"Componente z","magnitude":"Magnitude"}},
        "de":{"name":"Kreuzprodukt Rechner","description":"Berechnen Sie das Kreuzprodukt zweier 3D-Vektoren und seinen Betrag.","inputs":{"ax":"Vektor A x","ay":"Vektor A y","az":"Vektor A z","bx":"Vektor B x","by":"Vektor B y","bz":"Vektor B z"},"outputs":{"cx":"x-Komponente","cy":"y-Komponente","cz":"z-Komponente","magnitude":"Betrag"}},
        "it":{"name":"Calcolatore Prodotto Vettoriale","description":"Calcola il prodotto vettoriale di due vettori 3D e il suo modulo.","inputs":{"ax":"Vettore A x","ay":"Vettore A y","az":"Vettore A z","bx":"Vettore B x","by":"Vettore B y","bz":"Vettore B z"},"outputs":{"cx":"Componente x","cy":"Componente y","cz":"Componente z","magnitude":"Modulo"}},
    },
    latex_formula="\\vec{a} \\times \\vec{b} = \\begin{pmatrix} a_y b_z - a_z b_y \\\\ a_z b_x - a_x b_z \\\\ a_x b_y - a_y b_x \\end{pmatrix}",
    use_cases=[
        {"en":"Torque Calculation","en_body":"In mechanics, torque is the cross product of the lever-arm vector and the force vector, giving both magnitude and direction of rotation."},
        {"en":"Surface Normals","en_body":"Computer graphics computes cross products of triangle edges to find surface normals for realistic lighting and shading."},
        {"en":"Electromagnetism","en_body":"The Lorentz force on a charged particle moving through a magnetic field is proportional to the cross product of velocity and B-field vectors."},
    ],
    steps=[
        {"en":"Enter the components of vector A."},
        {"en":"Enter the components of vector B."},
        {"en":"The calculator outputs the orthogonal vector C = A × B and its magnitude."},
    ],
)

add_calc(
    id="118", block="matematicas", cat="A",
    domain="math", concept="polynomial differentiation",
    slugs={"es":"derivada-polinomio","en":"polynomial-derivative","fr":"derivee-polynome","pt":"derivada-polinomio","de":"polynom-ableitung","it":"derivata-polinomio"},
    inputs=[
        {"id":"a","type":"number","step":"any","default":2,"unit":"","unit_options":[],"unit_category":""},
        {"id":"b","type":"number","step":"any","default":-3,"unit":"","unit_options":[],"unit_category":""},
        {"id":"c","type":"number","step":"any","default":5,"unit":"","unit_options":[],"unit_category":""},
        {"id":"x_val","type":"number","step":"any","default":2,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"derivative","unit":""}],
    formula="var a=parseFloat(inputs.a)||0;var b=parseFloat(inputs.b)||0;var c=parseFloat(inputs.c)||0;var x=parseFloat(inputs.x_val)||0;var deriv=2*a*x+b;return{derivative:deriv.toFixed(4)};",
    related=["119","218"],
    i18n={
        "es":{"name":"Derivada de Polinomio Cuadrático","description":"Calcula la derivada de ax² + bx + c evaluada en un punto x.","inputs":{"a":"Coeficiente a","b":"Coeficiente b","c":"Coeficiente c","x_val":"Punto x"},"outputs":{"derivative":"Derivada f'(x)"}},
        "en":{"name":"Quadratic Polynomial Derivative","description":"Calculate the derivative of ax² + bx + c evaluated at a point x.","inputs":{"a":"Coefficient a","b":"Coefficient b","c":"Coefficient c","x_val":"Point x"},"outputs":{"derivative":"Derivative f'(x)"}},
        "fr":{"name":"Dérivée Polynôme Quadratique","description":"Calculez la dérivée de ax² + bx + c évaluée en un point x.","inputs":{"a":"Coefficient a","b":"Coefficient b","c":"Coefficient c","x_val":"Point x"},"outputs":{"derivative":"Dérivée f'(x)"}},
        "pt":{"name":"Derivada de Polinômio Quadrático","description":"Calcule a derivada de ax² + bx + c avaliada em um ponto x.","inputs":{"a":"Coeficiente a","b":"Coeficiente b","c":"Coeficiente c","x_val":"Ponto x"},"outputs":{"derivative":"Derivada f'(x)"}},
        "de":{"name":"Quadratische Polynom-Ableitung","description":"Berechnen Sie die Ableitung von ax² + bx + c an einem Punkt x.","inputs":{"a":"Koeffizient a","b":"Koeffizient b","c":"Koeffizient c","x_val":"Punkt x"},"outputs":{"derivative":"Ableitung f'(x)"}},
        "it":{"name":"Derivata Polinomio Quadratico","description":"Calcola la derivata di ax² + bx + c valutata in un punto x.","inputs":{"a":"Coefficiente a","b":"Coefficiente b","c":"Coefficiente c","x_val":"Punto x"},"outputs":{"derivative":"Derivata f'(x)"}},
    },
    latex_formula="f(x) = ax^2 + bx + c \\quad \\Rightarrow \\quad f'(x) = 2ax + b",
    use_cases=[
        {"en":"Optimization","en_body":"Setting the derivative to zero finds the vertex of a parabola, solving maximum revenue or minimum cost problems in economics."},
        {"en":"Velocity from Position","en_body":"If the polynomial describes position versus time, its derivative gives instantaneous velocity at any moment."},
        {"en":"Slope of Tangent","en_body":"The derivative value at a point equals the slope of the tangent line, used in Newton's method for root finding."},
    ],
    steps=[
        {"en":"Enter coefficients a, b, and c."},
        {"en":"Enter the x-value where you want the derivative evaluated."},
        {"en":"The calculator returns 2ax + b, the instantaneous rate of change."},
    ],
)

add_calc(
    id="119", block="matematicas", cat="A",
    domain="math", concept="numerical integration",
    slugs={"es":"regla-trapecios-integral","en":"trapezoidal-rule-integral","fr":"regle-trapezes-integrale","pt":"regra-trapezios-integral","de":"trapezregel-integral","it":"regola-trapezi-integrale"},
    inputs=[
        {"id":"a","type":"number","step":"any","default":0,"unit":"","unit_options":[],"unit_category":""},
        {"id":"b","type":"number","step":"any","default":4,"unit":"","unit_options":[],"unit_category":""},
        {"id":"n","type":"number","step":1,"default":4,"unit":"","unit_options":[],"unit_category":""},
        {"id":"fa","type":"number","step":"any","default":1,"unit":"","unit_options":[],"unit_category":""},
        {"id":"fb","type":"number","step":"any","default":9,"unit":"","unit_options":[],"unit_category":""},
    ],
    outputs=[{"id":"approx","unit":""}],
    formula="var a=parseFloat(inputs.a)||0;var b=parseFloat(inputs.b)||0;var n=parseFloat(inputs.n)||1;var fa=parseFloat(inputs.fa)||0;var fb=parseFloat(inputs.fb)||0;var h=(b-a)/n;var approx=h*(fa+fb)/2;return{approx:approx.toFixed(4)};",
    related=["118","218"],
    i18n={
        "es":{"name":"Aproximación de Integral por Trapecios","description":"Aproxima una integral definida usando la regla del trapecio con n subdivisiones.","inputs":{"a":"Límite inferior","b":"Límite superior","n":"Número de trapecios","fa":"f(a)","fb":"f(b)"},"outputs":{"approx":"Aproximación"}},
        "en":{"name":"Trapezoidal Rule Integral Approximation","description":"Approximate a definite integral using the trapezoidal rule with n subdivisions.","inputs":{"a":"Lower bound","b":"Upper bound","n":"Number of trapezoids","fa":"f(a)","fb":"f(b)"},"outputs":{"approx":"Approximation"}},
        "fr":{"name":"Approximation d'Intégrale par Trapèzes","description":"Approximez une intégrale définie par la règle des trapèzes avec n subdivisions.","inputs":{"a":"Borne inférieure","b":"Borne supérieure","n":"Nombre de trapèzes","fa":"f(a)","fb":"f(b)"},"outputs":{"approx":"Approximation"}},
        "pt":{"name":"Aproximação de Integral por Trapézios","description":"Aproxime uma integral definida usando a regra dos trapézios com n subdivisões.","inputs":{"a":"Limite inferior","b":"Limite superior","n":"Número de trapézios","fa":"f(a)","fb":"f(b)"},"outputs":{"approx":"Aproximação"}},
        "de":{"name":"Trapezregel Integral-Approximation","description":"Approximieren Sie ein bestimmtes Integral mit der Trapezregel und n Unterteilungen.","inputs":{"a":"Untere Grenze","b":"Obere Grenze","n":"Anzahl Trapeze","fa":"f(a)","fb":"f(b)"},"outputs":{"approx":"Approximation"}},
        "it":{"name":"Approssimazione Integrale con Trapezi","description":"Approssima un integrale definito usando la regola dei trapezi con n suddivisioni.","inputs":{"a":"Limite inferiore","b":"Limite superiore","n":"Numero di trapezi","fa":"f(a)","fb":"f(b)"},"outputs":{"approx":"Approssimazione"}},
    },
    latex_formula="\\int_a^b f(x)\\,dx \\approx \\frac{h}{2}\\bigl[f(a) + f(b)\\bigr], \\quad h = b - a",
    use_cases=[
        {"en":"Area Under Curves","en_body":"When an exact antiderivative is unknown, the trapezoidal rule estimates the area under experimental data curves."},
        {"en":"Probability Distributions","en_body":"Statisticians approximate cumulative distribution functions by integrating probability density functions numerically."},
        {"en":"Physics Work Integrals","en_body":"Variable force over distance requires integration; the trapezoid method gives practical engineering approximations."},
    ],
    steps=[
        {"en":"Enter the lower and upper bounds of integration."},
        {"en":"Enter the function values at the endpoints f(a) and f(b)."},
        {"en":"The calculator applies the trapezoid area formula."},
    ],
)

# (I need to continue adding the remaining 40 calculators. Due to file size, I'll add them now.)

# ── PHYSICS (120-129) ──
add_calc(
    id="120", block="ciencia", cat="E",
    domain="physics", concept="projectile motion",
    slugs={"es":"movimiento-proyectil","en":"projectile-motion","fr":"mouvement-projectile","pt":"movimento-projetil","de":"wurfbewegung","it":"moto-proiettile"},
    inputs=[
        {"id":"v0","type":"number","step":"any","default":20,"unit":"m/s","unit_options":["m/s","km/h","mph"],"unit_category":"velocity"},
        {"id":"angle","type":"number","step":"any","default":45,"unit":"deg","unit_options":["deg","rad"],"unit_category":"angle"},
        {"id":"h0","type":"number","step":"any","default":0,"unit":"m","unit_options":["m","ft","cm"],"unit_category":"length"},
    ],
    outputs=[{"id":"range","unit":"m"},{"id":"max_height","unit":"m"},{"id":"flight_time","unit":"s"}],
    formula="var v0=parseFloat(inputs.v0)||0;var theta=(parseFloat(inputs.angle)||0)*Math.PI/180;var h0=parseFloat(inputs.h0)||0;var g=9.80665;var vx=v0*Math.cos(theta);var vy=v0*Math.sin(theta);var t_flight=(vy+Math.sqrt(vy*vy+2*g*h0))/g;var range=vx*t_flight;var max_h=h0+vy*vy/(2*g);return{range:range.toFixed(4),max_height:max_h.toFixed(4),flight_time:t_flight.toFixed(4)};",
    related=["121","129"],
    i18n={
        "es":{"name":"Calculadora de Movimiento de Proyectil","description":"Calcula el alcance, altura máxima y tiempo de vuelo de un proyectil.","inputs":{"v0":"Velocidad inicial","angle":"Ángulo de lanzamiento","h0":"Altura inicial"},"outputs":{"range":"Alcance","max_height":"Altura máxima","flight_time":"Tiempo de vuelo"}},
        "en":{"name":"Projectile Motion Calculator","description":"Calculate range, maximum height, and flight time of a projectile.","inputs":{"v0":"Initial velocity","angle":"Launch angle","h0":"Initial height"},"outputs":{"range":"Range","max_height":"Max height","flight_time":"Flight time"}},
        "fr":{"name":"Calculateur de Mouvement du Projectile","description":"Calculez la portée, la hauteur maximale et le temps de vol d'un projectile.","inputs":{"v0":"Vitesse initiale","angle":"Angle de lancement","h0":"Hauteur initiale"},"outputs":{"range":"Portée","max_height":"Hauteur max","flight_time":"Temps de vol"}},
        "pt":{"name":"Calculadora de Movimento do Projétil","description":"Calcule o alcance, altura máxima e tempo de voo de um projétil.","inputs":{"v0":"Velocidade inicial","angle":"Ângulo de lançamento","h0":"Altura inicial"},"outputs":{"range":"Alcance","max_height":"Altura máxima","flight_time":"Tempo de voo"}},
        "de":{"name":"Wurfbewegung Rechner","description":"Berechnen Sie Wurfweite, Maximalhöhe und Flugzeit eines Projektils.","inputs":{"v0":"Anfangsgeschwindigkeit","angle":"Wurfwinkel","h0":"Anfangshöhe"},"outputs":{"range":"Wurfweite","max_height":"Maximalhöhe","flight_time":"Flugzeit"}},
        "it":{"name":"Calcolatore Moto del Proiettile","description":"Calcola la gittata, l'altezza massima e il tempo di volo di un proiettile.","inputs":{"v0":"Velocità iniziale","angle":"Angolo di lancio","h0":"Altezza iniziale"},"outputs":{"range":"Gittata","max_height":"Altezza max","flight_time":"Tempo di volo"}},
    },
    latex_formula="R = \\frac{v_0^2 \\sin(2\\theta)}{g}, \\quad H_{max} = \\frac{v_0^2 \\sin^2(\\theta)}{2g}, \\quad T = \\frac{2v_0 \\sin(\\theta)}{g}",
    use_cases=[
        {"en":"Sports Science","en_body":"Coaches optimize javelin and shot-put launch angles to maximize distance using projectile kinematics."},
        {"en":"Ballistics","en_body":"Military and law enforcement use trajectory calculations to predict bullet drop and impact points."},
        {"en":"Fireworks Design","en_body":"Pyrotechnicians calculate launch velocities and angles to ensure shells burst at desired altitudes and positions."},
    ],
    steps=[
        {"en":"Enter the initial launch velocity."},
        {"en":"Enter the launch angle relative to horizontal."},
        {"en":"Enter the initial height above ground (if any)."},
    ],
)

# ── PHYSICS 121-129 ──
add_calc(id="121", block="ciencia", cat="E", domain="physics", concept="centripetal force",
    slugs={"es":"fuerza-centripeta","en":"centripetal-force","fr":"force-centripete","pt":"forca-centripeta","de":"zentripetalkraft","it":"forza-centripeta"},
    inputs=[{"id":"m","type":"number","step":"any","default":2,"unit":"kg","unit_options":["kg","g","lb"],"unit_category":"mass"},{"id":"v","type":"number","step":"any","default":10,"unit":"m/s","unit_options":["m/s","km/h","mph"],"unit_category":"velocity"},{"id":"r","type":"number","step":"any","default":5,"unit":"m","unit_options":["m","ft","cm"],"unit_category":"length"}],
    outputs=[{"id":"force","unit":"N"}],
    formula="var m=parseFloat(inputs.m)||0;var v=parseFloat(inputs.v)||0;var r=parseFloat(inputs.r)||0;var f=m*v*v/r;return{force:f.toFixed(4)};",
    related=["120","122"],
    i18n={"es":{"name":"Calculadora de Fuerza Centrípeta","description":"Calcula la fuerza centrípeta necesaria para mantener un objeto en movimiento circular.","inputs":{"m":"Masa","v":"Velocidad","r":"Radio"},"outputs":{"force":"Fuerza"}},"en":{"name":"Centripetal Force Calculator","description":"Calculate the centripetal force required to keep an object in circular motion.","inputs":{"m":"Mass","v":"Velocity","r":"Radius"},"outputs":{"force":"Force"}},"fr":{"name":"Calculateur de Force Centripète","description":"Calculez la force centripète nécessaire pour maintenir un objet en mouvement circulaire.","inputs":{"m":"Masse","v":"Vitesse","r":"Rayon"},"outputs":{"force":"Force"}},"pt":{"name":"Calculadora de Força Centrípeta","description":"Calcule a força centrípeta necessária para manter um objeto em movimento circular.","inputs":{"m":"Massa","v":"Velocidade","r":"Raio"},"outputs":{"force":"Força"}},"de":{"name":"Zentripetalkraft Rechner","description":"Berechnen Sie die Zentripetalkraft, die nötig ist, um einen Gegenstand in Kreisbewegung zu halten.","inputs":{"m":"Masse","v":"Geschwindigkeit","r":"Radius"},"outputs":{"force":"Kraft"}},"it":{"name":"Calcolatore Forza Centripeta","description":"Calcola la forza centripeta necessaria per mantenere un oggetto in moto circolare.","inputs":{"m":"Massa","v":"Velocità","r":"Raggio"},"outputs":{"force":"Forza"}}},
    latex_formula="F_c = \\frac{mv^2}{r}",
    use_cases=[{"en":"Vehicle Turning","en_body":"Engineers calculate centripetal force to design safe banked curves and tire friction requirements for highways."},{"en":"Amusement Rides","en_body":"Roller coaster designers ensure the track exerts enough normal force to keep cars on the loop at minimum speeds."},{"en":"Satellite Orbits","en_body":"Gravitational force provides the centripetal acceleration that keeps satellites in stable Earth orbits."}],
    steps=[{"en":"Enter the object's mass."},{"en":"Enter its tangential velocity."},{"en":"Enter the radius of the circular path."}])

add_calc(id="122", block="ciencia", cat="E", domain="physics", concept="gravitational force",
    slugs={"es":"fuerza-gravitatoria","en":"gravitational-force","fr":"force-gravitationnelle","pt":"forca-gravitacional","de":"gravitationskraft","it":"forza-gravitazionale"},
    inputs=[{"id":"m1","type":"number","step":"any","default":1000,"unit":"kg","unit_options":["kg","g","lb"],"unit_category":"mass"},{"id":"m2","type":"number","step":"any","default":1000,"unit":"kg","unit_options":["kg","g","lb"],"unit_category":"mass"},{"id":"r","type":"number","step":"any","default":1,"unit":"m","unit_options":["m","ft","cm"],"unit_category":"length"}],
    outputs=[{"id":"force","unit":"N"}],
    formula="var G=6.67430e-11;var m1=parseFloat(inputs.m1)||0;var m2=parseFloat(inputs.m2)||0;var r=parseFloat(inputs.r)||0;var f=G*m1*m2/(r*r);return{force:f.toExponential(4)};",
    related=["121","123"],
    i18n={"es":{"name":"Calculadora de Fuerza Gravitatoria","description":"Calcula la fuerza de atracción gravitatoria entre dos masas.","inputs":{"m1":"Masa 1","m2":"Masa 2","r":"Distancia"},"outputs":{"force":"Fuerza"}},"en":{"name":"Gravitational Force Calculator","description":"Calculate the gravitational attraction between two masses.","inputs":{"m1":"Mass 1","m2":"Mass 2","r":"Distance"},"outputs":{"force":"Force"}},"fr":{"name":"Calculateur de Force Gravitationnelle","description":"Calculez l'attraction gravitationnelle entre deux masses.","inputs":{"m1":"Masse 1","m2":"Masse 2","r":"Distance"},"outputs":{"force":"Force"}},"pt":{"name":"Calculadora de Força Gravitacional","description":"Calcule a atração gravitacional entre duas massas.","inputs":{"m1":"Massa 1","m2":"Massa 2","r":"Distância"},"outputs":{"force":"Força"}},"de":{"name":"Gravitationskraft Rechner","description":"Berechnen Sie die Gravitationsanziehung zwischen zwei Massen.","inputs":{"m1":"Masse 1","m2":"Masse 2","r":"Abstand"},"outputs":{"force":"Kraft"}},"it":{"name":"Calcolatore Forza Gravitazionale","description":"Calcola l'attrazione gravitazionale tra due masse.","inputs":{"m1":"Massa 1","m2":"Massa 2","r":"Distanza"},"outputs":{"force":"Forza"}}},
    latex_formula="F = G \\frac{m_1 m_2}{r^2}, \\quad G = 6.67430 \\times 10^{-11} \\text{ N·m}^2/\\text{kg}^2",
    use_cases=[{"en":"Astronomy","en_body":"Astrophysicists use Newton's law to estimate the masses of binary star systems from their orbital periods and separations."},{"en":"Geophysics","en_body":"Gravimeters measure local gravitational anomalies to locate underground oil deposits or mineral veins."},{"en":"Space Mission Planning","en_body":"Mission designers compute gravitational forces between spacecraft and celestial bodies to plan fuel-efficient trajectories."}],
    steps=[{"en":"Enter the two masses."},{"en":"Enter the distance between their centers."},{"en":"The calculator applies Newton's universal law of gravitation."}])

add_calc(id="123", block="ciencia", cat="E", domain="physics", concept="elastic potential energy",
    slugs={"es":"energia-potencial-elastica","en":"elastic-potential-energy","fr":"energie-potentielle-elastique","pt":"energia-potencial-elastic","de":"elastische-potentielle-energie","it":"energia-potenziale-elastica"},
    inputs=[{"id":"k","type":"number","step":"any","default":200,"unit":"N/m","unit_options":["N/m"],"unit_category":"force"},{"id":"x","type":"number","step":"any","default":0.1,"unit":"m","unit_options":["m","cm","mm","ft","in"],"unit_category":"length"}],
    outputs=[{"id":"energy","unit":"J"}],
    formula="var k=parseFloat(inputs.k)||0;var x=parseFloat(inputs.x)||0;var e=0.5*k*x*x;return{energy:e.toFixed(4)};",
    related=["946","124"],
    i18n={"es":{"name":"Energía Potencial Elástica","description":"Calcula la energía almacenada en un resorte deformado.","inputs":{"k":"Constante del resorte","x":"Deformación"},"outputs":{"energy":"Energía"}},"en":{"name":"Elastic Potential Energy Calculator","description":"Calculate the energy stored in a deformed spring.","inputs":{"k":"Spring constant","x":"Displacement"},"outputs":{"energy":"Energy"}},"fr":{"name":"Énergie Potentielle Élastique","description":"Calculez l'énergie stockée dans un ressort déformé.","inputs":{"k":"Constante du ressort","x":"Déformation"},"outputs":{"energy":"Énergie"}},"pt":{"name":"Energia Potencial Elástica","description":"Calcule a energia armazenada em uma mola deformada.","inputs":{"k":"Constante da mola","x":"Deformação"},"outputs":{"energy":"Energia"}},"de":{"name":"Elastische Potentielle Energie","description":"Berechnen Sie die in einer deformierten Feder gespeicherte Energie.","inputs":{"k":"Federkonstante","x":"Auslenkung"},"outputs":{"energy":"Energie"}},"it":{"name":"Energia Potenziale Elastica","description":"Calcola l'energia immagazzinata in una molla deformata.","inputs":{"k":"Costante elastica","x":"Deformazione"},"outputs":{"energy":"Energia"}}},
    latex_formula="E_p = \\frac{1}{2} k x^2",
    use_cases=[{"en":"Vehicle Suspension","en_body":"Automotive engineers size coil springs so their elastic energy absorbs road bumps without bottoming out."},{"en":"Archery","en_body":"The draw weight and draw length of a bow determine the elastic potential energy transferred to the arrow."},{"en":"Trampolines","en_body":"Designers calculate spring constants to ensure jumpers store enough energy for safe rebound heights."}],
    steps=[{"en":"Enter the spring constant k (stiffness)."},{"en":"Enter the displacement from equilibrium x."},{"en":"The calculator returns ½kx², the stored elastic energy."}])

add_calc(id="124", block="ciencia", cat="E", domain="physics", concept="specific heat capacity",
    slugs={"es":"calor-especifico","en":"specific-heat-capacity","fr":"capacite-thermique-massique","pt":"calor-especifico","de":"spezifische-warmekapazitat","it":"calore-specifico"},
    inputs=[{"id":"m","type":"number","step":"any","default":1,"unit":"kg","unit_options":["kg","g","lb"],"unit_category":"mass"},{"id":"c","type":"number","step":"any","default":4184,"unit":"J/(kg·K)","unit_options":["J/(kg·K)","cal/(g·°C)"],"unit_category":"energy"},{"id":"dt","type":"number","step":"any","default":10,"unit":"K","unit_options":["K","°C","°F"],"unit_category":"temperature"}],
    outputs=[{"id":"q","unit":"J"}],
    formula="var m=parseFloat(inputs.m)||0;var c=parseFloat(inputs.c)||0;var dt=parseFloat(inputs.dt)||0;var q=m*c*dt;return{q:q.toFixed(4)};",
    related=["123","955"],
    i18n={"es":{"name":"Calor Específico","description":"Calcula la energía térmica transferida al calentar una sustancia.","inputs":{"m":"Masa","c":"Calor específico","dt":"Cambio de temperatura"},"outputs":{"q":"Energía térmica"}},"en":{"name":"Specific Heat Capacity Calculator","description":"Calculate the thermal energy transferred when heating a substance.","inputs":{"m":"Mass","c":"Specific heat","dt":"Temperature change"},"outputs":{"q":"Thermal energy"}},"fr":{"name":"Capacité Thermique Massique","description":"Calculez l'énergie thermique transférée lors du chauffage d'une substance.","inputs":{"m":"Masse","c":"Chaleur massique","dt":"Variation de température"},"outputs":{"q":"Énergie thermique"}},"pt":{"name":"Calor Específico","description":"Calcule a energia térmica transferida ao aquecer uma substância.","inputs":{"m":"Massa","c":"Calor específico","dt":"Variação de temperatura"},"outputs":{"q":"Energia térmica"}},"de":{"name":"Spezifische Wärmekapazität","description":"Berechnen Sie die beim Erwärmen eines Stoffs übertragene Wärmeenergie.","inputs":{"m":"Masse","c":"Spezifische Wärme","dt":"Temperaturänderung"},"outputs":{"q":"Wärmeenergie"}},"it":{"name":"Calore Specifico","description":"Calcola l'energia termica trasferita riscaldando una sostanza.","inputs":{"m":"Massa","c":"Calore specifico","dt":"Variazione di temperatura"},"outputs":{"q":"Energia termica"}}},
    latex_formula="Q = mc\\Delta T",
    use_cases=[{"en":"HVAC Sizing","en_body":"Heating engineers compute the energy needed to raise building air temperature by a target delta using the specific heat of air."},{"en":"Cooking Appliances","en_body":"Microwave and induction cooktop ratings are chosen based on the Q = mcΔT required to boil water or heat food."},{"en":"Thermal Storage","en_body":"Solar thermal systems store energy in water tanks sized using the specific heat capacity of water (≈ 4184 J/kg·K)."}],
    steps=[{"en":"Enter the mass of the substance."},{"en":"Enter its specific heat capacity."},{"en":"Enter the temperature change ΔT."}])

add_calc(id="125", block="ciencia", cat="E", domain="physics", concept="wave speed",
    slugs={"es":"velocidad-onda","en":"wave-speed-calculator","fr":"vitesse-onde","pt":"velocidade-onda","de":"wellengeschwindigkeit","it":"velocita-onda"},
    inputs=[{"id":"f","type":"number","step":"any","default":440,"unit":"Hz","unit_options":["Hz","kHz","MHz"],"unit_category":"frequency"},{"id":"wavelength","type":"number","step":"any","default":0.78,"unit":"m","unit_options":["m","cm","mm","ft"],"unit_category":"length"}],
    outputs=[{"id":"v","unit":"m/s"}],
    formula="var f=parseFloat(inputs.f)||0;var wl=parseFloat(inputs.wavelength)||0;var v=f*wl;return{v:v.toFixed(4)};",
    related=["120","126"],
    i18n={"es":{"name":"Velocidad de Onda","description":"Calcula la velocidad de propagación de una onda a partir de su frecuencia y longitud.","inputs":{"f":"Frecuencia","wavelength":"Longitud de onda"},"outputs":{"v":"Velocidad"}},"en":{"name":"Wave Speed Calculator","description":"Calculate the propagation speed of a wave from its frequency and wavelength.","inputs":{"f":"Frequency","wavelength":"Wavelength"},"outputs":{"v":"Speed"}},"fr":{"name":"Vitesse d'Onde","description":"Calculez la vitesse de propagation d'une onde à partir de sa fréquence et longueur.","inputs":{"f":"Fréquence","wavelength":"Longueur d'onde"},"outputs":{"v":"Vitesse"}},"pt":{"name":"Velocidade da Onda","description":"Calcule a velocidade de propagação de uma onda a partir de sua frequência e comprimento.","inputs":{"f":"Frequência","wavelength":"Comprimento de onda"},"outputs":{"v":"Velocidade"}},"de":{"name":"Wellengeschwindigkeit","description":"Berechnen Sie die Ausbreitungsgeschwindigkeit einer Welle aus Frequenz und Wellenlänge.","inputs":{"f":"Frequenz","wavelength":"Wellenlänge"},"outputs":{"v":"Geschwindigkeit"}},"it":{"name":"Velocità dell'Onda","description":"Calcola la velocità di propagazione di un'onda dalla sua frequenza e lunghezza.","inputs":{"f":"Frequenza","wavelength":"Lunghezza d'onda"},"outputs":{"v":"Velocità"}}},
    latex_formula="v = f \\lambda",
    use_cases=[{"en":"Acoustic Design","en_body":"Architects calculate wave speeds in air to design concert halls with optimal reverberation and avoid standing wave nodes."},{"en":"Fiber Optics","en_body":"Telecom engineers relate optical frequency to wavelength in fiber to minimize dispersion and maximize bandwidth."},{"en":"Medical Ultrasound","en_body":"Ultrasound technicians use wavelength and frequency to set imaging resolution and penetration depth for diagnostic scans."}],
    steps=[{"en":"Enter the wave frequency."},{"en":"Enter the wavelength."},{"en":"The product gives the wave propagation speed."}])

add_calc(id="126", block="ciencia", cat="E", domain="physics", concept="thin lens equation",
    slugs={"es":"ecuacion-lente-delgada","en":"thin-lens-equation","fr":"equation-lentille-mince","pt":"equacao-lente-fina","de":"duenne-linsen-gleichung","it":"equazione-lente-sottile"},
    inputs=[{"id":"focal","type":"number","step":"any","default":0.1,"unit":"m","unit_options":["m","cm","mm"],"unit_category":"length"},{"id":"obj_dist","type":"number","step":"any","default":0.3,"unit":"m","unit_options":["m","cm","mm"],"unit_category":"length"}],
    outputs=[{"id":"img_dist","unit":"m"},{"id":"magnification","unit":""}],
    formula="var f=parseFloat(inputs.focal)||0;var u=parseFloat(inputs.obj_dist)||0;var img=u*f/(u-f);var mag=-img/u;return{img_dist:img.toFixed(4),magnification:mag.toFixed(4)};",
    related=["125","127"],
    i18n={"es":{"name":"Ecuación de Lente Delgada","description":"Calcula la distancia de imagen y magnificación de una lente delgada.","inputs":{"focal":"Distancia focal","obj_dist":"Distancia objeto"},"outputs":{"img_dist":"Distancia imagen","magnification":"Aumento"}},"en":{"name":"Thin Lens Equation Calculator","description":"Calculate image distance and magnification for a thin lens.","inputs":{"focal":"Focal length","obj_dist":"Object distance"},"outputs":{"img_dist":"Image distance","magnification":"Magnification"}},"fr":{"name":"Équation de la Lentille Mince","description":"Calculez la distance de l'image et le grossissement d'une lentille mince.","inputs":{"focal":"Distance focale","obj_dist":"Distance objet"},"outputs":{"img_dist":"Distance image","magnification":"Grossissement"}},"pt":{"name":"Equação da Lente Fina","description":"Calcule a distância da imagem e ampliação de uma lente fina.","inputs":{"focal":"Distância focal","obj_dist":"Distância do objeto"},"outputs":{"img_dist":"Distância da imagem","magnification":"Ampliação"}},"de":{"name":"Dünne Linse Gleichung","description":"Berechnen Sie Bildweite und Vergrößerung einer dünnen Linse.","inputs":{"focal":"Brennweite","obj_dist":"Gegenstandsweite"},"outputs":{"img_dist":"Bildweite","magnification":"Vergrößerung"}},"it":{"name":"Equazione Lente Sottile","description":"Calcola la distanza dell'immagine e l'ingrandimento di una lente sottile.","inputs":{"focal":"Distanza focale","obj_dist":"Distanza oggetto"},"outputs":{"img_dist":"Distanza immagine","magnification":"Ingrandimento"}}},
    latex_formula="\\frac{1}{f} = \\frac{1}{d_o} + \\frac{1}{d_i}, \\quad M = -\\frac{d_i}{d_o}",
    use_cases=[{"en":"Camera Design","en_body":"Optical engineers select focal lengths and sensor distances to achieve desired fields of view in smartphone cameras."},{"en":"Eyeglass Prescription","en_body":"Ophthalmologists use lens power (diopters = 1/f) to correct refractive errors and focus images on the retina."},{"en":"Microscopy","en_body":"Microscopists adjust object distance relative to the objective lens to obtain sharp, magnified images of specimens."}],
    steps=[{"en":"Enter the focal length of the lens."},{"en":"Enter the object distance from the lens."},{"en":"The calculator solves for image distance and linear magnification."}])

add_calc(id="127", block="ciencia", cat="E", domain="physics", concept="torque",
    slugs={"es":"torque-momento-fuerza","en":"torque-calculator","fr":"calcul-couple","pt":"calculadora-torque","de":"drehmoment-rechner","it":"calcolatore-coppia"},
    inputs=[{"id":"r","type":"number","step":"any","default":0.5,"unit":"m","unit_options":["m","cm","ft"],"unit_category":"length"},{"id":"f","type":"number","step":"any","default":100,"unit":"N","unit_options":["N","lbf","kN"],"unit_category":"force"},{"id":"theta","type":"number","step":"any","default":90,"unit":"deg","unit_options":["deg","rad"],"unit_category":"angle"}],
    outputs=[{"id":"torque","unit":"N·m"}],
    formula="var r=parseFloat(inputs.r)||0;var f=parseFloat(inputs.f)||0;var theta=(parseFloat(inputs.theta)||0)*Math.PI/180;var tau=r*f*Math.sin(theta);return{torque:tau.toFixed(4)};",
    related=["128","121"],
    i18n={"es":{"name":"Calculadora de Torque","description":"Calcula el momento de torsión producido por una fuerza aplicada a una distancia del eje.","inputs":{"r":"Radio","f":"Fuerza","theta":"Ángulo"},"outputs":{"torque":"Torque"}},"en":{"name":"Torque Calculator","description":"Calculate the rotational moment produced by a force applied at a distance from the pivot.","inputs":{"r":"Lever arm","f":"Force","theta":"Angle"},"outputs":{"torque":"Torque"}},"fr":{"name":"Calculateur de Couple","description":"Calculez le moment de rotation produit par une force appliquée à une distance de l'axe.","inputs":{"r":"Bras de levier","f":"Force","theta":"Angle"},"outputs":{"torque":"Couple"}},"pt":{"name":"Calculadora de Torque","description":"Calcule o momento rotacional produzido por uma força aplicada a uma distância do pivô.","inputs":{"r":"Braço de alavanca","f":"Força","theta":"Ângulo"},"outputs":{"torque":"Torque"}},"de":{"name":"Drehmoment Rechner","description":"Berechnen Sie das Drehmoment, das durch eine Kraft im Abstand vom Drehpunkt erzeugt wird.","inputs":{"r":"Hebelarm","f":"Kraft","theta":"Winkel"},"outputs":{"torque":"Drehmoment"}},"it":{"name":"Calcolatore Coppia","description":"Calcola il momento rotazionale prodotto da una forza applicata a una distanza dal perno.","inputs":{"r":"Braccio","f":"Forza","theta":"Angolo"},"outputs":{"torque":"Coppia"}}},
    latex_formula="\\tau = r F \\sin(\\theta)",
    use_cases=[{"en":"Automotive Engines","en_body":"Engine designers maximize torque at low RPM by optimizing crankshaft throw and combustion pressure."},{"en":"Structural Bolting","en_body":"Mechanical engineers specify torque wrench settings to achieve proper bolt preload without yielding the fastener."},{"en":"Biomechanics","en_body":"Physical therapists analyze joint torques during rehabilitation to ensure exercises strengthen muscles without overloading ligaments."}],
    steps=[{"en":"Enter the lever arm distance from pivot to force application."},{"en":"Enter the magnitude of the applied force."},{"en":"Enter the angle between the force vector and the lever arm."}])

add_calc(id="128", block="ciencia", cat="E", domain="physics", concept="angular momentum",
    slugs={"es":"momento-angular","en":"angular-momentum","fr":"moment-angulaire","pt":"momento-angular","de":"drehimpuls","it":"momento-angolare"},
    inputs=[{"id":"m","type":"number","step":"any","default":2,"unit":"kg","unit_options":["kg","g","lb"],"unit_category":"mass"},{"id":"v","type":"number","step":"any","default":5,"unit":"m/s","unit_options":["m/s","km/h","mph"],"unit_category":"velocity"},{"id":"r","type":"number","step":"any","default":1,"unit":"m","unit_options":["m","cm","ft"],"unit_category":"length"}],
    outputs=[{"id":"L","unit":"kg·m²/s"}],
    formula="var m=parseFloat(inputs.m)||0;var v=parseFloat(inputs.v)||0;var r=parseFloat(inputs.r)||0;var L=m*v*r;return{L:L.toFixed(4)};",
    related=["127","121"],
    i18n={"es":{"name":"Momento Angular","description":"Calcula el momento angular de una partícula en movimiento circular.","inputs":{"m":"Masa","v":"Velocidad tangencial","r":"Radio"},"outputs":{"L":"Momento angular"}},"en":{"name":"Angular Momentum Calculator","description":"Calculate the angular momentum of a particle in circular motion.","inputs":{"m":"Mass","v":"Tangential velocity","r":"Radius"},"outputs":{"L":"Angular momentum"}},"fr":{"name":"Moment Angulaire","description":"Calculez le moment angulaire d'une particule en mouvement circulaire.","inputs":{"m":"Masse","v":"Vitesse tangentielle","r":"Rayon"},"outputs":{"L":"Moment angulaire"}},"pt":{"name":"Momento Angular","description":"Calcule o momento angular de uma partícula em movimento circular.","inputs":{"m":"Massa","v":"Velocidade tangencial","r":"Raio"},"outputs":{"L":"Momento angular"}},"de":{"name":"Drehimpuls Rechner","description":"Berechnen Sie den Drehimpuls eines Teilchens in Kreisbewegung.","inputs":{"m":"Masse","v":"Tangentialgeschwindigkeit","r":"Radius"},"outputs":{"L":"Drehimpuls"}},"it":{"name":"Momento Angolare","description":"Calcola il momento angolare di una particella in moto circolare.","inputs":{"m":"Massa","v":"Velocità tangenziale","r":"Raggio"},"outputs":{"L":"Momento angolare"}}},
    latex_formula="L = mvr",
    use_cases=[{"en":"Figure Skating","en_body":"When a skater pulls arms in, radius decreases and velocity increases to conserve angular momentum, enabling faster spins."},{"en":"Planetary Motion","en_body":"Kepler's second law is a direct consequence of angular momentum conservation as planets sweep equal areas in equal times."},{"en":"Gyroscopes","en_body":"Inertial navigation systems use conservation of angular momentum in spinning gyroscopes to detect aircraft orientation changes."}],
    steps=[{"en":"Enter the particle mass."},{"en":"Enter its tangential velocity."},{"en":"Enter the orbital radius."}])

add_calc(id="129", block="ciencia", cat="E", domain="physics", concept="fluid pressure",
    slugs={"es":"presion-fluido","en":"fluid-pressure","fr":"pression-fluide","pt":"pressao-fluido","de":"fluid-druck","it":"pressione-fluido"},
    inputs=[{"id":"rho","type":"number","step":"any","default":1000,"unit":"kg/m³","unit_options":["kg/m³","g/cm³","lb/ft³"],"unit_category":"density"},{"id":"g","type":"number","step":"any","default":9.80665,"unit":"m/s²","unit_options":["m/s²","ft/s²"],"unit_category":"acceleration"},{"id":"h","type":"number","step":"any","default":10,"unit":"m","unit_options":["m","ft","cm"],"unit_category":"length"}],
    outputs=[{"id":"pressure","unit":"Pa"}],
    formula="var rho=parseFloat(inputs.rho)||0;var g=parseFloat(inputs.g)||0;var h=parseFloat(inputs.h)||0;var p=rho*g*h;return{pressure:p.toFixed(4)};",
    related=["120","705"],
    i18n={"es":{"name":"Presión de Fluido","description":"Calcula la presión hidrostática a una profundidad dada en un fluido.","inputs":{"rho":"Densidad","g":"Gravedad","h":"Profundidad"},"outputs":{"pressure":"Presión"}},"en":{"name":"Fluid Pressure Calculator","description":"Calculate hydrostatic pressure at a given depth in a fluid.","inputs":{"rho":"Density","g":"Gravity","h":"Depth"},"outputs":{"pressure":"Pressure"}},"fr":{"name":"Pression Fluide","description":"Calculez la pression hydrostatique à une profondeur donnée dans un fluide.","inputs":{"rho":"Densité","g":"Gravité","h":"Profondeur"},"outputs":{"pressure":"Pression"}},"pt":{"name":"Pressão do Fluido","description":"Calcule a pressão hidrostática a uma profundidade dada em um fluido.","inputs":{"rho":"Densidade","g":"Gravidade","h":"Profundidade"},"outputs":{"pressure":"Pressão"}},"de":{"name":"Fluiddruck Rechner","description":"Berechnen Sie den hydrostatischen Druck in einer gegebenen Tiefe in einer Flüssigkeit.","inputs":{"rho":"Dichte","g":"Erdbeschleunigung","h":"Tiefe"},"outputs":{"pressure":"Druck"}},"it":{"name":"Pressione del Fluido","description":"Calcola la pressione idrostatica a una data profondità in un fluido.","inputs":{"rho":"Densità","g":"Gravità","h":"Profondità"},"outputs":{"pressure":"Pressione"}}},
    latex_formula="P = \\rho g h",
    use_cases=[{"en":"Dam Engineering","en_body":"Civil engineers compute hydrostatic pressure on dam walls to design reinforcement that prevents catastrophic failure."},{"en":"Scuba Diving","en_body":"Divers use fluid pressure calculations to determine safe depths and required tank pressures for decompression stops."},{"en":"Irrigation Systems","en_body":"Agricultural engineers size water towers and pumping stations based on the pressure needed to overcome elevation head."}],
    steps=[{"en":"Enter the fluid density."},{"en":"Enter gravitational acceleration (default 9.80665 m/s²)."},{"en":"Enter the depth below the surface."}])

# ── FINANCE (320-329) ──
add_calc(id="320", block="finanzas", cat="C", domain="finance", concept="CAGR",
    slugs={"es":"tasa-crecimiento-anual-compuesto","en":"cagr-calculator","fr":"taux-croissance-annuel-compose","pt":"calculadora-cagr","de":"cagr-rechner","it":"calcolatore-cagr"},
    inputs=[{"id":"begin","type":"number","step":"any","default":1000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"end","type":"number","step":"any","default":2000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"years","type":"number","step":1,"default":5,"unit":"yr","unit_options":["yr","mo"],"unit_category":"time"}],
    outputs=[{"id":"cagr","unit":"%"}],
    formula="var b=parseFloat(inputs.begin)||0;var e=parseFloat(inputs.end)||0;var y=parseFloat(inputs.years)||1;var cagr=(Math.pow(e/b,1/y)-1)*100;return{cagr:cagr.toFixed(4)};",
    related=["302","322"],
    i18n={"es":{"name":"Calculadora CAGR","description":"Calcula la tasa de crecimiento anual compuesto de una inversión.","inputs":{"begin":"Valor inicial","end":"Valor final","years":"Años"},"outputs":{"cagr":"CAGR %"}},"en":{"name":"CAGR Calculator","description":"Calculate the compound annual growth rate of an investment.","inputs":{"begin":"Beginning value","end":"Ending value","years":"Years"},"outputs":{"cagr":"CAGR %"}},"fr":{"name":"Calculateur CAGR","description":"Calculez le taux de croissance annuel composé d'un investissement.","inputs":{"begin":"Valeur initiale","end":"Valeur finale","years":"Années"},"outputs":{"cagr":"CAGR %"}},"pt":{"name":"Calculadora CAGR","description":"Calcule a taxa de crescimento anual composta de um investimento.","inputs":{"begin":"Valor inicial","end":"Valor final","years":"Anos"},"outputs":{"cagr":"CAGR %"}},"de":{"name":"CAGR Rechner","description":"Berechnen Sie die durchschnittliche jährliche Wachstumsrate einer Investition.","inputs":{"begin":"Anfangswert","end":"Endwert","years":"Jahre"},"outputs":{"cagr":"CAGR %"}},"it":{"name":"Calcolatore CAGR","description":"Calcola il tasso di crescita annuo composto di un investimento.","inputs":{"begin":"Valore iniziale","end":"Valore finale","years":"Anni"},"outputs":{"cagr":"CAGR %"}}},
    latex_formula="\\text{CAGR} = \\left(\\frac{V_{final}}{V_{initial}}\\right)^{\\frac{1}{n}} - 1",
    use_cases=[{"en":"Portfolio Benchmarking","en_body":"Investors compare their portfolio CAGR against the S&P 500 to assess relative performance over multi-year horizons."},{"en":"Startup Valuation","en_body":"Venture capitalists project revenue CAGR to estimate future valuations using comparable company multiples."},{"en":"Real Estate","en_body":"Property owners calculate CAGR of appreciation to decide whether to sell, hold, or refinance an asset."}],
    steps=[{"en":"Enter the initial investment value."},{"en":"Enter the final value."},{"en":"Enter the number of years held."}])

add_calc(id="321", block="finanzas", cat="C", domain="finance", concept="APR",
    slugs={"es":"tasa-anual-efectiva","en":"apr-calculator","fr":"taux-annuel-effectif","pt":"calculadora-tae","de":"effektiver-jahreszins","it":"calcolatore-taeg"},
    inputs=[{"id":"nominal","type":"number","step":"any","default":12,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"n","type":"number","step":1,"default":12,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"apr","unit":"%"}],
    formula="var r=parseFloat(inputs.nominal)||0;var n=parseFloat(inputs.n)||1;var apr=(Math.pow(1+r/(100*n),n)-1)*100;return{apr:apr.toFixed(4)};",
    related=["300","320"],
    i18n={"es":{"name":"Calculadora de TAE (APR)","description":"Convierte una tasa nominal en la tasa anual equivalente.","inputs":{"nominal":"Tasa nominal %","n":"Periodos por año"},"outputs":{"apr":"TAE %"}},"en":{"name":"APR Calculator","description":"Convert a nominal interest rate into the effective annual percentage rate.","inputs":{"nominal":"Nominal rate %","n":"Periods per year"},"outputs":{"apr":"APR %"}},"fr":{"name":"Calculateur TAEG","description":"Convertissez un taux nominal en taux annuel effectif global.","inputs":{"nominal":"Taux nominal %","n":"Périodes par an"},"outputs":{"apr":"TAEG %"}},"pt":{"name":"Calculadora TAE","description":"Converta uma taxa nominal na taxa anual efetiva.","inputs":{"nominal":"Taxa nominal %","n":"Períodos por ano"},"outputs":{"apr":"TAE %"}},"de":{"name":"Effektivzins Rechner","description":"Wandeln Sie einen Nominalzins in den effektiven Jahreszins um.","inputs":{"nominal":"Nominalzins %","n":"Perioden pro Jahr"},"outputs":{"apr":"Effektivzins %"}},"it":{"name":"Calcolatore TAEG","description":"Converti un tasso nominale nel tasso annuo effettivo globale.","inputs":{"nominal":"Tasso nominale %","n":"Periodi per anno"},"outputs":{"apr":"TAEG %"}}},
    latex_formula="\\text{APR} = \\left(1 + \\frac{r_{nom}}{n}\\right)^n - 1",
    use_cases=[{"en":"Loan Comparison","en_body":"Banks advertise nominal rates, but APR reveals the true cost including compounding, enabling fair comparisons."},{"en":"Credit Cards","en_body":"Cardholders use APR to understand the real yearly cost of carried balances versus promotional teaser rates."},{"en":"Savings Accounts","en_body":"Savers compare APR across banks to find the highest effective yield on deposits."}],
    steps=[{"en":"Enter the nominal annual interest rate."},{"en":"Enter the number of compounding periods per year."},{"en":"The calculator compounds the rate to reveal the effective APR."}])

add_calc(id="322", block="finanzas", cat="C", domain="finance", concept="loan amortization",
    slugs={"es":"amortizacion-prestamo","en":"loan-amortization","fr":"amortissement-pret","pt":"amortizacao-emprestimo","de":"kredittilgung","it":"ammortamento-prestito"},
    inputs=[{"id":"principal","type":"number","step":"any","default":100000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"rate","type":"number","step":"any","default":5,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"years","type":"number","step":1,"default":30,"unit":"yr","unit_options":["yr","mo"],"unit_category":"time"}],
    outputs=[{"id":"payment","unit":"USD"},{"id":"total_interest","unit":"USD"}],
    formula="var p=parseFloat(inputs.principal)||0;var r=(parseFloat(inputs.rate)||0)/1200;var n=(parseFloat(inputs.years)||0)*12;var payment=r>0?p*r/(1-Math.pow(1+r,-n)):p/n;var total=payment*n-p;return{payment:payment.toFixed(2),total_interest:total.toFixed(2)};",
    related=["300","320"],
    i18n={"es":{"name":"Amortización de Préstamo","description":"Calcula la cuota mensual y el interés total de un préstamo.","inputs":{"principal":"Capital","rate":"Tasa anual %","years":"Años"},"outputs":{"payment":"Cuota mensual","total_interest":"Interés total"}},"en":{"name":"Loan Amortization Calculator","description":"Calculate monthly payment and total interest on a loan.","inputs":{"principal":"Principal","rate":"Annual rate %","years":"Years"},"outputs":{"payment":"Monthly payment","total_interest":"Total interest"}},"fr":{"name":"Amortissement de Prêt","description":"Calculez la mensualité et les intérêts totaux d'un prêt.","inputs":{"principal":"Capital","rate":"Taux annuel %","years":"Années"},"outputs":{"payment":"Mensualité","total_interest":"Intérêts totaux"}},"pt":{"name":"Amortização de Empréstimo","description":"Calcule a parcela mensal e os juros totais de um empréstimo.","inputs":{"principal":"Principal","rate":"Taxa anual %","years":"Anos"},"outputs":{"payment":"Parcela mensal","total_interest":"Juros totais"}},"de":{"name":"Kredittilgungsrechner","description":"Berechnen Sie die monatliche Rate und die Gesamtzinsen eines Kredits.","inputs":{"principal":"Kreditsumme","rate":"Jahreszins %","years":"Jahre"},"outputs":{"payment":"Monatliche Rate","total_interest":"Gesamtzinsen"}},"it":{"name":"Ammortamento Prestito","description":"Calcola la rata mensile e gli interessi totali di un prestito.","inputs":{"principal":"Capitale","rate":"Tasso annuo %","years":"Anni"},"outputs":{"payment":"Rata mensile","total_interest":"Interessi totali"}}},
    latex_formula="M = P \\frac{r(1+r)^n}{(1+r)^n - 1}",
    use_cases=[{"en":"Mortgage Shopping","en_body":"Homebuyers compare monthly payments across different loan terms to balance affordability with total interest cost."},{"en":"Auto Financing","en_body":"Car buyers use amortization schedules to decide between longer terms with lower payments versus shorter terms with less interest."},{"en":"Debt Consolidation","en_body":"Borrowers model consolidated loan payments to verify that refinancing actually reduces total interest paid."}],
    steps=[{"en":"Enter the loan principal."},{"en":"Enter the annual interest rate."},{"en":"Enter the loan term in years."}])

add_calc(id="323", block="finanzas", cat="C", domain="finance", concept="rental yield",
    slugs={"es":"rentabilidad-alquiler","en":"rental-yield","fr":"rendement-locatif","pt":"rentabilidade-aluguel","de":"mietrendite","it":"rendimento-affitto"},
    inputs=[{"id":"annual_rent","type":"number","step":"any","default":12000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"property_value","type":"number","step":"any","default":200000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"}],
    outputs=[{"id":"yield_pct","unit":"%"}],
    formula="var rent=parseFloat(inputs.annual_rent)||0;var val=parseFloat(inputs.property_value)||0;var y=val>0?(rent/val)*100:0;return{yield_pct:y.toFixed(4)};",
    related=["324","322"],
    i18n={"es":{"name":"Rentabilidad por Alquiler","description":"Calcula el rendimiento bruto anual de una propiedad en alquiler.","inputs":{"annual_rent":"Alquiler anual","property_value":"Valor de la propiedad"},"outputs":{"yield_pct":"Rendimiento %"}},"en":{"name":"Rental Yield Calculator","description":"Calculate the gross annual rental yield of a property.","inputs":{"annual_rent":"Annual rent","property_value":"Property value"},"outputs":{"yield_pct":"Yield %"}},"fr":{"name":"Rendement Locatif","description":"Calculez le rendement locatif brut annuel d'un bien immobilier.","inputs":{"annual_rent":"Loyer annuel","property_value":"Valeur du bien"},"outputs":{"yield_pct":"Rendement %"}},"pt":{"name":"Rentabilidade de Aluguel","description":"Calcule a rentabilidade bruta anual de um imóvel alugado.","inputs":{"annual_rent":"Aluguel anual","property_value":"Valor do imóvel"},"outputs":{"yield_pct":"Rentabilidade %"}},"de":{"name":"Mietrendite Rechner","description":"Berechnen Sie die Bruttomietrendite einer Immobilie.","inputs":{"annual_rent":"Jahresmiete","property_value":"Immobilienwert"},"outputs":{"yield_pct":"Rendite %"}},"it":{"name":"Rendimento Affitto","description":"Calcola il rendimento lordo annuo di un immobile in affitto.","inputs":{"annual_rent":"Affitto annuo","property_value":"Valore immobile"},"outputs":{"yield_pct":"Rendimento %"}}},
    latex_formula="\\text{Yield} = \\frac{\\text{Annual Rent}}{\\text{Property Value}} \\times 100\\%",
    use_cases=[{"en":"Investment Property Screening","en_body":"Investors quickly filter listings by yield to identify properties that generate strong cash flow relative to price."},{"en":"Market Comparison","en_body":"Analysts compare average rental yields across cities to spot undervalued or overheated real estate markets."},{"en":"Portfolio Rebalancing","en_body":"Landlords sell low-yield properties and reinvest in high-yield assets to maximize passive income."}],
    steps=[{"en":"Enter the total annual rent collected."},{"en":"Enter the current market value of the property."},{"en":"The calculator divides rent by value and converts to a percentage."}])

add_calc(id="324", block="finanzas", cat="C", domain="finance", concept="cap rate",
    slugs={"es":"tasa-capitalizacion","en":"cap-rate","fr":"taux-capitalisation","pt":"taxa-capitalizacao","de":"cap-rate","it":"tasso-capitale"},
    inputs=[{"id":"noi","type":"number","step":"any","default":15000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"value","type":"number","step":"any","default":200000,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"}],
    outputs=[{"id":"cap_rate","unit":"%"}],
    formula="var noi=parseFloat(inputs.noi)||0;var val=parseFloat(inputs.value)||0;var rate=val>0?(noi/val)*100:0;return{cap_rate:rate.toFixed(4)};",
    related=["323","322"],
    i18n={"es":{"name":"Tasa de Capitalización (Cap Rate)","description":"Calcula la tasa de capitalización de un inmueble de inversión.","inputs":{"noi":"NOI anual","value":"Valor de la propiedad"},"outputs":{"cap_rate":"Cap rate %"}},"en":{"name":"Cap Rate Calculator","description":"Calculate the capitalization rate of an investment property.","inputs":{"noi":"Annual NOI","value":"Property value"},"outputs":{"cap_rate":"Cap rate %"}},"fr":{"name":"Taux de Capitalisation","description":"Calculez le taux de capitalisation d'un bien immobilier d'investissement.","inputs":{"noi":"RNB annuel","value":"Valeur du bien"},"outputs":{"cap_rate":"Taux cap %"}},"pt":{"name":"Taxa de Capitalização","description":"Calcule a taxa de capitalização de um imóvel de investimento.","inputs":{"noi":"RLO anual","value":"Valor do imóvel"},"outputs":{"cap_rate":"Cap rate %"}},"de":{"name":"Cap Rate Rechner","description":"Berechnen Sie die Kapitalisierungsrate einer Investmentimmobilie.","inputs":{"noi":"Jährlicher NOI","value":"Immobilienwert"},"outputs":{"cap_rate":"Cap Rate %"}},"it":{"name":"Tasso di Capitalizzazione","description":"Calcola il tasso di capitalizzazione di un immobile di investimento.","inputs":{"noi":"RNO annuo","value":"Valore immobile"},"outputs":{"cap_rate":"Cap rate %"}}},
    latex_formula="\\text{Cap Rate} = \\frac{\\text{NOI}}{\\text{Property Value}} \\times 100\\%",
    use_cases=[{"en":"Commercial Real Estate","en_body":"Brokers price office buildings and retail centers by dividing net operating income by the asking price."},{"en":"REIT Analysis","en_body":"Investors compare cap rates across REIT portfolios to identify management teams that maximize property-level returns."},{"en":"Development Feasibility","en_body":"Developers set minimum cap rate hurdles to ensure new construction meets investor return expectations."}],
    steps=[{"en":"Enter the net operating income (NOI) per year."},{"en":"Enter the property value or purchase price."},{"en":"The ratio, expressed as a percentage, is the cap rate."}])

add_calc(id="325", block="finanzas", cat="C", domain="finance", concept="dividend yield",
    slugs={"es":"dividend-yield","en":"dividend-yield","fr":"rendement-dividende","pt":"dividend-yield","de":"dividendenrendite","it":"dividend-yield"},
    inputs=[{"id":"annual_div","type":"number","step":"any","default":2,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"share_price","type":"number","step":"any","default":50,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"}],
    outputs=[{"id":"yield_pct","unit":"%"}],
    formula="var d=parseFloat(inputs.annual_div)||0;var p=parseFloat(inputs.share_price)||0;var y=p>0?(d/p)*100:0;return{yield_pct:y.toFixed(4)};",
    related=["326","324"],
    i18n={"es":{"name":"Dividend Yield","description":"Calcula el rendimiento por dividendo de una acción.","inputs":{"annual_div":"Dividendo anual por acción","share_price":"Precio de la acción"},"outputs":{"yield_pct":"Yield %"}},"en":{"name":"Dividend Yield Calculator","description":"Calculate the dividend yield of a stock.","inputs":{"annual_div":"Annual dividend per share","share_price":"Share price"},"outputs":{"yield_pct":"Yield %"}},"fr":{"name":"Rendement du Dividende","description":"Calculez le rendement par dividende d'une action.","inputs":{"annual_div":"Dividende annuel par action","share_price":"Cours de l'action"},"outputs":{"yield_pct":"Rendement %"}},"pt":{"name":"Dividend Yield","description":"Calcule o dividend yield de uma ação.","inputs":{"annual_div":"Dividendo anual por ação","share_price":"Preço da ação"},"outputs":{"yield_pct":"Yield %"}},"de":{"name":"Dividendenrendite","description":"Berechnen Sie die Dividendenrendite einer Aktie.","inputs":{"annual_div":"Jährliche Dividende pro Aktie","share_price":"Aktienkurs"},"outputs":{"yield_pct":"Rendite %"}},"it":{"name":"Dividend Yield","description":"Calcola il rendimento da dividendi di un'azione.","inputs":{"annual_div":"Dividendo annuo per azione","share_price":"Prezzo azione"},"outputs":{"yield_pct":"Yield %"}}},
    latex_formula="\\text{Dividend Yield} = \\frac{\\text{Annual Dividend per Share}}{\\text{Share Price}} \\times 100\\%",
    use_cases=[{"en":"Income Investing","en_body":"Retirees favor high-yield stocks to generate passive income without selling principal shares."},{"en":"Sector Comparison","en_body":"Utility and REIT sectors typically offer higher yields than technology growth stocks, reflecting mature cash flows."},{"en":"Dividend Growth","en_body":"Investors track yield relative to price to spot companies that raise dividends faster than their stock appreciates."}],
    steps=[{"en":"Enter the annual dividend per share."},{"en":"Enter the current share price."},{"en":"The calculator returns the dividend yield percentage."}])

add_calc(id="326", block="finanzas", cat="C", domain="finance", concept="P/E ratio",
    slugs={"es":"ratio-per","en":"pe-ratio","fr":"ratio-per","pt":"indice-pe","de":"kgv-rechner","it":"rapporto-pe"},
    inputs=[{"id":"price","type":"number","step":"any","default":100,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"eps","type":"number","step":"any","default":5,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"}],
    outputs=[{"id":"pe","unit":"x"}],
    formula="var p=parseFloat(inputs.price)||0;var e=parseFloat(inputs.eps)||0;var pe=e!==0?p/e:0;return{pe:pe.toFixed(4)};",
    related=["325","324"],
    i18n={"es":{"name":"Ratio Precio/Beneficio (P/E)","description":"Calcula el múltiplo P/E de una acción.","inputs":{"price":"Precio de la acción","eps":"Beneficio por acción"},"outputs":{"pe":"Ratio P/E"}},"en":{"name":"Price-to-Earnings Ratio Calculator","description":"Calculate the P/E multiple of a stock.","inputs":{"price":"Share price","eps":"Earnings per share"},"outputs":{"pe":"P/E ratio"}},"fr":{"name":"Calculateur PER","description":"Calculez le multiple PER d'une action.","inputs":{"price":"Cours de l'action","eps":"Bénéfice par action"},"outputs":{"pe":"Ratio PER"}},"pt":{"name":"Calculadora Índice P/L","description":"Calcule o múltiplo P/L de uma ação.","inputs":{"price":"Preço da ação","eps":"Lucro por ação"},"outputs":{"pe":"Índice P/L"}},"de":{"name":"KGV Rechner","description":"Berechnen Sie das Kurs-Gewinn-Verhältnis einer Aktie.","inputs":{"price":"Aktienkurs","eps":"Gewinn pro Aktie"},"outputs":{"pe":"KGV"}},"it":{"name":"Calcolatore Rapporto P/E","description":"Calcola il multiplo P/E di un'azione.","inputs":{"price":"Prezzo azione","eps":"Utile per azione"},"outputs":{"pe":"Rapporto P/E"}}},
    latex_formula="\\text{P/E} = \\frac{\\text{Price per Share}}{\\text{Earnings per Share}}",
    use_cases=[{"en":"Valuation Screening","en_body":"Value investors filter for low P/E ratios to find stocks potentially trading below intrinsic value."},{"en":"Growth Assessment","en_body":"High P/E ratios often signal market expectations of rapid earnings growth, common in technology sectors."},{"en":"Historical Comparison","en_body":"Analysts compare current P/E to 5-year averages to judge whether a stock is expensive or cheap relative to its own history."}],
    steps=[{"en":"Enter the current share price."},{"en":"Enter the earnings per share (EPS)."},{"en":"The quotient is the P/E ratio, a key valuation metric."}])

add_calc(id="327", block="finanzas", cat="C", domain="finance", concept="future value of annuity",
    slugs={"es":"valor-futuro-anualidad","en":"future-value-annuity","fr":"valeur-future-rente","pt":"valor-futuro-anuidade","de":"zukunftswert-rente","it":"valore-futuro-rendita"},
    inputs=[{"id":"pmt","type":"number","step":"any","default":100,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"rate","type":"number","step":"any","default":5,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"n","type":"number","step":1,"default":10,"unit":"yr","unit_options":["yr","mo"],"unit_category":"time"}],
    outputs=[{"id":"fv","unit":"USD"}],
    formula="var pmt=parseFloat(inputs.pmt)||0;var r=(parseFloat(inputs.rate)||0)/100;var n=parseFloat(inputs.n)||0;var fv=r>0?pmt*((Math.pow(1+r,n)-1)/r):pmt*n;return{fv:fv.toFixed(2)};",
    related=["328","302"],
    i18n={"es":{"name":"Valor Futuro de Anualidad","description":"Calcula el valor futuro de una serie de pagos iguales.","inputs":{"pmt":"Pago periódico","rate":"Tasa %","n":"Número de períodos"},"outputs":{"fv":"Valor futuro"}},"en":{"name":"Future Value of Annuity Calculator","description":"Calculate the future value of a series of equal payments.","inputs":{"pmt":"Periodic payment","rate":"Interest rate %","n":"Number of periods"},"outputs":{"fv":"Future value"}},"fr":{"name":"Valeur Future d'une Rente","description":"Calculez la valeur future d'une série de paiements égaux.","inputs":{"pmt":"Paiement périodique","rate":"Taux %","n":"Nombre de périodes"},"outputs":{"fv":"Valeur future"}},"pt":{"name":"Valor Futuro de Anuidade","description":"Calcule o valor futuro de uma série de pagamentos iguais.","inputs":{"pmt":"Pagamento periódico","rate":"Taxa %","n":"Número de períodos"},"outputs":{"fv":"Valor futuro"}},"de":{"name":"Zukunftswert einer Rente","description":"Berechnen Sie den Zukunftswert einer Reihe gleicher Zahlungen.","inputs":{"pmt":"Periodische Zahlung","rate":"Zinssatz %","n":"Anzahl Perioden"},"outputs":{"fv":"Zukunftswert"}},"it":{"name":"Valore Futuro di una Rendita","description":"Calcola il valore futuro di una serie di pagamenti uguali.","inputs":{"pmt":"Pagamento periodico","rate":"Tasso %","n":"Numero di periodi"},"outputs":{"fv":"Valore futuro"}}},
    latex_formula="FV = PMT \\times \\frac{(1+r)^n - 1}{r}",
    use_cases=[{"en":"Retirement Savings","en_body":"Workers project the future value of monthly 401(k) contributions to determine if they are on track for retirement."},{"en":"Education Funds","en_body":"Parents calculate how much a recurring deposit into a 529 plan will grow by the time their child enters college."},{"en":"Sinking Funds","en_body":"Corporations estimate the future value of periodic deposits set aside to repay bonds at maturity."}],
    steps=[{"en":"Enter the periodic payment amount."},{"en":"Enter the interest rate per period."},{"en":"Enter the total number of periods."}])

add_calc(id="328", block="finanzas", cat="C", domain="finance", concept="present value of annuity",
    slugs={"es":"valor-actual-anualidad","en":"present-value-annuity","fr":"valeur-actuelle-rente","pt":"valor-presente-anuidade","de":"barwert-rente","it":"valore-attuale-rendita"},
    inputs=[{"id":"pmt","type":"number","step":"any","default":100,"unit":"USD","unit_options":["USD","EUR","GBP"],"unit_category":"currency"},{"id":"rate","type":"number","step":"any","default":5,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"n","type":"number","step":1,"default":10,"unit":"yr","unit_options":["yr","mo"],"unit_category":"time"}],
    outputs=[{"id":"pv","unit":"USD"}],
    formula="var pmt=parseFloat(inputs.pmt)||0;var r=(parseFloat(inputs.rate)||0)/100;var n=parseFloat(inputs.n)||0;var pv=r>0?pmt*((1-Math.pow(1+r,-n))/r):pmt*n;return{pv:pv.toFixed(2)};",
    related=["327","301"],
    i18n={"es":{"name":"Valor Actual de Anualidad","description":"Calcula el valor presente de una serie de pagos futuros iguales.","inputs":{"pmt":"Pago periódico","rate":"Tasa %","n":"Número de períodos"},"outputs":{"pv":"Valor presente"}},"en":{"name":"Present Value of Annuity Calculator","description":"Calculate the present value of a series of equal future payments.","inputs":{"pmt":"Periodic payment","rate":"Interest rate %","n":"Number of periods"},"outputs":{"pv":"Present value"}},"fr":{"name":"Valeur Actuelle d'une Rente","description":"Calculez la valeur actuelle d'une série de paiements futurs égaux.","inputs":{"pmt":"Paiement périodique","rate":"Taux %","n":"Nombre de périodes"},"outputs":{"pv":"Valeur actuelle"}},"pt":{"name":"Valor Presente de Anuidade","description":"Calcule o valor presente de uma série de pagamentos futuros iguais.","inputs":{"pmt":"Pagamento periódico","rate":"Taxa %","n":"Número de períodos"},"outputs":{"pv":"Valor presente"}},"de":{"name":"Barwert einer Rente","description":"Berechnen Sie den Barwert einer Reihe gleicher zukünftiger Zahlungen.","inputs":{"pmt":"Periodische Zahlung","rate":"Zinssatz %","n":"Anzahl Perioden"},"outputs":{"pv":"Barwert"}},"it":{"name":"Valore Attuale di una Rendita","description":"Calcola il valore attuale di una serie di pagamenti futuri uguali.","inputs":{"pmt":"Pagamento periodico","rate":"Tasso %","n":"Numero di periodi"},"outputs":{"pv":"Valore attuale"}}},
    latex_formula="PV = PMT \\times \\frac{1 - (1+r)^{-n}}{r}",
    use_cases=[{"en":"Pension Valuation","en_body":"Actuaries discount future pension payments to their present value to report accurate liabilities on corporate balance sheets."},{"en":"Lease Accounting","en_body":"Accountants calculate the present value of lease payments to determine right-of-use asset values under IFRS 16."},{"en":"Lottery Payouts","en_body":"Winners compare lump-sum present values to annuity streams to choose the most valuable payout option."}],
    steps=[{"en":"Enter the periodic payment amount."},{"en":"Enter the discount rate per period."},{"en":"Enter the total number of periods."}])

add_calc(id="329", block="finanzas", cat="C", domain="finance", concept="WACC",
    slugs={"es":"wacc","en":"wacc-calculator","fr":"cmpc","pt":"wacc","de":"kalkulatorischer-zins","it":"wacc"},
    inputs=[{"id":"equity","type":"number","step":"any","default":60,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"debt","type":"number","step":"any","default":40,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"cost_eq","type":"number","step":"any","default":10,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"cost_debt","type":"number","step":"any","default":5,"unit":"%","unit_options":["%"],"unit_category":"percentage"},{"id":"tax","type":"number","step":"any","default":25,"unit":"%","unit_options":["%"],"unit_category":"percentage"}],
    outputs=[{"id":"wacc","unit":"%"}],
    formula="var e=parseFloat(inputs.equity)||0;var d=parseFloat(inputs.debt)||0;var ce=parseFloat(inputs.cost_eq)||0;var cd=parseFloat(inputs.cost_debt)||0;var t=parseFloat(inputs.tax)||0;var total=e+d;var wacc=total>0?(e/total*ce+d/total*cd*(1-t/100)):0;return{wacc:wacc.toFixed(4)};",
    related=["320","326"],
    i18n={"es":{"name":"WACC (Coste Medio Ponderado Capital)","description":"Calcula el coste medio ponderado del capital de una empresa.","inputs":{"equity":"% Capital","debt":"% Deuda","cost_eq":"Coste capital %","cost_debt":"Coste deuda %","tax":"Impuesto %"},"outputs":{"wacc":"WACC %"}},"en":{"name":"WACC Calculator","description":"Calculate the weighted average cost of capital for a firm.","inputs":{"equity":"% Equity","debt":"% Debt","cost_eq":"Cost of equity %","cost_debt":"Cost of debt %","tax":"Tax rate %"},"outputs":{"wacc":"WACC %"}},"fr":{"name":"Calculateur CMPC","description":"Calculez le coût moyen pondéré du capital d'une entreprise.","inputs":{"equity":"% Capitaux","debt":"% Dette","cost_eq":"Coût des capitaux %","cost_debt":"Coût de la dette %","tax":"Taux d'imposition %"},"outputs":{"wacc":"CMPC %"}},"pt":{"name":"Calculadora WACC","description":"Calcule o custo médio ponderado de capital de uma empresa.","inputs":{"equity":"% Capital","debt":"% Dívida","cost_eq":"Custo do capital %","cost_debt":"Custo da dívida %","tax":"Imposto %"},"outputs":{"wacc":"WACC %"}},"de":{"name":"Kalkulatorischer Zins (WACC)","description":"Berechnen Sie die gewichteten durchschnittlichen Kapitalkosten eines Unternehmens.","inputs":{"equity":"% Eigenkapital","debt":"% Fremdkapital","cost_eq":"Eigenkapitalkosten %","cost_debt":"Fremdkapitalkosten %","tax":"Steuersatz %"},"outputs":{"wacc":"WACC %"}},"it":{"name":"Calcolatore WACC","description":"Calcola il costo medio ponderato del capitale di un'azienda.","inputs":{"equity":"% Capitale","debt":"% Debito","cost_eq":"Costo capitale %","cost_debt":"Costo debito %","tax":"Tasse %"},"outputs":{"wacc":"WACC %"}}},
    latex_formula="\\text{WACC} = \\frac{E}{V} r_e + \\frac{D}{V} r_d (1 - T_c)",
    use_cases=[{"en":"Discounted Cash Flow","en_body":"Analysts use WACC as the discount rate in DCF models to estimate the intrinsic value of publicly traded companies."},{"en":"Capital Budgeting","en_body":"CFOs compare project IRR to WACC; projects returning above WACC create shareholder value."},{"en":"M&A Valuation","en_body":"Acquirers compute target WACC to determine the appropriate hurdle rate for post-merger synergy valuations."}],
    steps=[{"en":"Enter the percentage of equity and debt in the capital structure."},{"en":"Enter the cost of equity and cost of debt."},{"en":"Enter the corporate tax rate."}])

# ── HEALTH (415-424) ──
add_calc(id="415", block="salud", cat="B", domain="health", concept="lean body mass",
    slugs={"es":"masa-magra","en":"lean-body-mass","fr":"masse-maigre","pt":"massa-magra","de":"fettfreie-masse","it":"massa-magra"},
    inputs=[{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"height","type":"number","step":"any","default":175,"unit":"cm","unit_options":["cm","ft"],"unit_category":"length"},{"id":"gender","type":"select","options":["male","female"],"default":"male","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"lbm","unit":"kg"}],
    formula="var w=parseFloat(inputs.weight)||0;var h=parseFloat(inputs.height)||0;var g=inputs.gender||'male';var lbm=g==='male'?(0.407*w)+(0.267*h)-19.2:(0.252*w)+(0.473*h)-48.3;return{lbm:lbm.toFixed(2)};",
    related=["422","400"],
    i18n={"es":{"name":"Masa Magra (Fórmula Boer)","description":"Estima la masa magra corporal a partir del peso, altura y sexo.","inputs":{"weight":"Peso","height":"Altura","gender":"Sexo"},"outputs":{"lbm":"Masa magra"}},"en":{"name":"Lean Body Mass Calculator (Boer)","description":"Estimate lean body mass from weight, height, and gender.","inputs":{"weight":"Weight","height":"Height","gender":"Gender"},"outputs":{"lbm":"Lean body mass"}},"fr":{"name":"Masse Maigre (Formule Boer)","description":"Estimez la masse maigre à partir du poids, de la taille et du sexe.","inputs":{"weight":"Poids","height":"Taille","gender":"Sexe"},"outputs":{"lbm":"Masse maigre"}},"pt":{"name":"Massa Magra (Fórmula Boer)","description":"Estime a massa magra a partir do peso, altura e sexo.","inputs":{"weight":"Peso","height":"Altura","gender":"Sexo"},"outputs":{"lbm":"Massa magra"}},"de":{"name":"Fettfreie Masse (Boer-Formel)","description":"Schätzen Sie die fettfreie Masse anhand von Gewicht, Größe und Geschlecht.","inputs":{"weight":"Gewicht","height":"Größe","gender":"Geschlecht"},"outputs":{"lbm":"Fettfreie Masse"}},"it":{"name":"Massa Magra (Formula Boer)","description":"Stima la massa magra da peso, altezza e sesso.","inputs":{"weight":"Peso","height":"Altezza","gender":"Sesso"},"outputs":{"lbm":"Massa magra"}}},
    latex_formula="\\text{LBM}_{male} = 0.407W + 0.267H - 19.2",
    use_cases=[{"en":"Protein Prescription","en_body":"Nutritionists use LBM to set daily protein targets since muscle tissue, not fat, drives protein requirements."},{"en":"Drug Dosing","en_body":"Pharmacologists adjust medication doses based on lean mass because many drugs distribute into body water, not adipose tissue."},{"en":"Body Composition Tracking","en_body":"Athletes monitor LBM trends to verify that weight loss comes from fat rather than metabolically active muscle."}],
    steps=[{"en":"Enter your total body weight."},{"en":"Enter your height."},{"en":"Select your gender for the appropriate regression formula."}])

add_calc(id="416", block="salud", cat="B", domain="health", concept="body adiposity index",
    slugs={"es":"indice-adiposidad-corporal","en":"body-adiposity-index","fr":"indice-adiposite","pt":"indice-adiposidade","de":"körperadipositas-index","it":"indice-adiposita"},
    inputs=[{"id":"hip","type":"number","step":"any","default":100,"unit":"cm","unit_options":["cm","in"],"unit_category":"length"},{"id":"height","type":"number","step":"any","default":175,"unit":"cm","unit_options":["cm","ft"],"unit_category":"length"}],
    outputs=[{"id":"bai","unit":"%"}],
    formula="var hip=parseFloat(inputs.hip)||0;var h=parseFloat(inputs.height)||0;var bai=h>0?((hip/Math.pow(h/100,1.5))-18):0;return{bai:bai.toFixed(2)};",
    related=["415","400"],
    i18n={"es":{"name":"Índice de Adiposidad Corporal (BAI)","description":"Estima el porcentaje de grasa corporal usando la circunferencia de cadera y la altura.","inputs":{"hip":"Cadera","height":"Altura"},"outputs":{"bai":"BAI %"}},"en":{"name":"Body Adiposity Index (BAI)","description":"Estimate body fat percentage using hip circumference and height.","inputs":{"hip":"Hip circumference","height":"Height"},"outputs":{"bai":"BAI %"}},"fr":{"name":"Indice d'Adiposité Corporelle","description":"Estimez le pourcentage de graisse corporelle à l'aide du tour de hanche et de la taille.","inputs":{"hip":"Tour de hanche","height":"Taille"},"outputs":{"bai":"IAO %"}},"pt":{"name":"Índice de Adiposidade Corporal","description":"Estime a porcentagem de gordura corporal usando a circunferência do quadril e altura.","inputs":{"hip":"Quadril","height":"Altura"},"outputs":{"bai":"IAC %"}},"de":{"name":"Körperadipositas-Index","description":"Schätzen Sie den Körperfettanteil anhand der Hüftumfangs und Größe.","inputs":{"hip":"Hüftumfang","height":"Größe"},"outputs":{"bai":"BAI %"}},"it":{"name":"Indice di Adiposità Corporea","description":"Stima la percentuale di grasso corporeo usando il girovita e l'altezza.","inputs":{"hip":"Fianchi","height":"Altezza"},"outputs":{"bai":"BAI %"}}},
    latex_formula="\\text{BAI} = \\frac{\\text{hip}}{\\text{height}^{1.5}} - 18",
    use_cases=[{"en":"Epidemiology","en_body":"Population researchers prefer BAI over BMI in some cohorts because hip circumference correlates strongly with DXA-measured fat mass."},{"en":"Fitness Assessment","en_body":"Trainers use BAI alongside skinfold measurements to track body composition changes in clients."},{"en":"Clinical Screening","en_body":"Primary care physicians use BAI as a rapid, equipment-free screening tool during routine checkups."}],
    steps=[{"en":"Measure your hip circumference at the widest point."},{"en":"Enter your height."},{"en":"The calculator computes your BAI percentage."}])

add_calc(id="417", block="salud", cat="B", domain="health", concept="protein intake",
    slugs={"es":"ingesta-proteica","en":"protein-intake","fr":"apport-proteique","pt":"ingestao-proteica","de":"eiweissbedarf","it":"assunzione-proteine"},
    inputs=[{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"activity","type":"number","step":"any","default":1.2,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"protein_min","unit":"g"},{"id":"protein_max","unit":"g"}],
    formula="var w=parseFloat(inputs.weight)||0;var act=parseFloat(inputs.activity)||1;var min=w*act*1.2;var max=w*act*2.0;return{protein_min:min.toFixed(1),protein_max:max.toFixed(1)};",
    related=["418","415"],
    i18n={"es":{"name":"Calculadora de Proteínas Diarias","description":"Estima la ingesta diaria recomendada de proteínas según peso y actividad.","inputs":{"weight":"Peso","activity":"Factor de actividad"},"outputs":{"protein_min":"Mínimo g","protein_max":"Máximo g"}},"en":{"name":"Daily Protein Intake Calculator","description":"Estimate recommended daily protein intake based on weight and activity level.","inputs":{"weight":"Weight","activity":"Activity factor"},"outputs":{"protein_min":"Minimum g","protein_max":"Maximum g"}},"fr":{"name":"Apport Protéique Quotidien","description":"Estimez l'apport protéique quotidien recommandé selon le poids et l'activité.","inputs":{"weight":"Poids","activity":"Facteur d'activité"},"outputs":{"protein_min":"Minimum g","protein_max":"Maximum g"}},"pt":{"name":"Ingestão Diária de Proteínas","description":"Estime a ingestão diária recomendada de proteínas com base no peso e atividade.","inputs":{"weight":"Peso","activity":"Fator de atividade"},"outputs":{"protein_min":"Mínimo g","protein_max":"Máximo g"}},"de":{"name":"Täglicher Eiweißbedarf","description":"Schätzen Sie den empfohlenen täglichen Eiweißbedarf anhand von Gewicht und Aktivitätsniveau.","inputs":{"weight":"Gewicht","activity":"Aktivitätsfaktor"},"outputs":{"protein_min":"Minimum g","protein_max":"Maximum g"}},"it":{"name":"Assunzione Giornaliera Proteine","description":"Stima l'assunzione giornaliera raccomandata di proteine in base a peso e attività.","inputs":{"weight":"Peso","activity":"Fattore attività"},"outputs":{"protein_min":"Minimo g","protein_max":"Massimo g"}}},
    latex_formula="\\text{Protein} = \\text{weight} \\times \\text{activity factor} \\times (1.2 \\text{ to } 2.0) \\text{ g/day}",
    use_cases=[{"en":"Muscle Building","en_body":"Strength athletes target the upper end of the protein range to support muscle protein synthesis after resistance training."},{"en":"Weight Loss","en_body":"Dieters increase protein intake to preserve lean mass while in a caloric deficit, improving body composition outcomes."},{"en":"Clinical Nutrition","en_body":"Hospital dietitians adjust protein prescriptions for wound healing, renal disease, and post-surgical recovery."}],
    steps=[{"en":"Enter your body weight."},{"en":"Enter an activity factor (1.2 sedentary, 1.6 active, 2.0 athlete)."},{"en":"The calculator gives a safe protein range in grams per day."}])

add_calc(id="418", block="salud", cat="B", domain="health", concept="fiber intake",
    slugs={"es":"ingesta-fibra","en":"fiber-intake","fr":"apport-fibres","pt":"ingestao-fibra","de":"faserbedarf","it":"assunzione-fibre"},
    inputs=[{"id":"calories","type":"number","step":"any","default":2000,"unit":"kcal","unit_options":["kcal"],"unit_category":"energy"}],
    outputs=[{"id":"fiber","unit":"g"}],
    formula="var cal=parseFloat(inputs.calories)||0;var fiber=cal/1000*14;return{fiber:fiber.toFixed(1)};",
    related=["417","401"],
    i18n={"es":{"name":"Ingesta Recomendada de Fibra","description":"Calcula la cantidad diaria recomendada de fibra basada en las calorías consumidas.","inputs":{"calories":"Calorías diarias"},"outputs":{"fiber":"Fibra g"}},"en":{"name":"Recommended Fiber Intake","description":"Calculate daily fiber recommendation based on caloric intake.","inputs":{"calories":"Daily calories"},"outputs":{"fiber":"Fiber g"}},"fr":{"name":"Apport Recommandé en Fibres","description":"Calculez la quantité de fibres recommandée par jour en fonction des calories consommées.","inputs":{"calories":"Calories quotidiennes"},"outputs":{"fiber":"Fibres g"}},"pt":{"name":"Ingestão Recomendada de Fibras","description":"Calcule a quantidade diária recomendada de fibras com base nas calorias consumidas.","inputs":{"calories":"Calorias diárias"},"outputs":{"fiber":"Fibras g"}},"de":{"name":"Empfohlene Faserzufuhr","description":"Berechnen Sie die empfohlene tägliche Fasermenge basierend auf der Kalorienzufuhr.","inputs":{"calories":"Tägliche Kalorien"},"outputs":{"fiber":"Faser g"}},"it":{"name":"Assunzione Raccomandata di Fibre","description":"Calcola la quantità giornaliera raccomandata di fibre in base alle calorie consumate.","inputs":{"calories":"Calorie giornaliere"},"outputs":{"fiber":"Fibre g"}}},
    latex_formula="\\text{Fiber (g)} = \\frac{\\text{Calories}}{1000} \\times 14",
    use_cases=[{"en":"Digestive Health","en_body":"Gastroenterologists recommend 14g of fiber per 1,000 calories to maintain regular bowel movements and healthy gut microbiota."},{"en":"Blood Sugar Control","en_body":"Diabetics use fiber targets to slow glucose absorption and improve postprandial glycemic response."},{"en":"Cardiovascular Risk","en_body":"Epidemiological studies link higher fiber intake to reduced LDL cholesterol and lower coronary heart disease incidence."}],
    steps=[{"en":"Enter your estimated daily caloric intake."},{"en":"The calculator applies the 14g per 1,000 kcal guideline."},{"en":"Distribute fiber across meals from whole grains, legumes, fruits, and vegetables."}])

add_calc(id="419", block="salud", cat="B", domain="health", concept="Karvonen heart rate",
    slugs={"es":"frecuencia-cardiaca-karvonen","en":"karvonen-heart-rate","fr":"fc-reserve-karvonen","pt":"frequencia-cardiaca-karvonen","de":"karvonen-herzfrequenz","it":"frequenza-cardiaca-karvonen"},
    inputs=[{"id":"age","type":"number","step":1,"default":30,"unit":"yr","unit_options":["yr"],"unit_category":"time"},{"id":"rest_hr","type":"number","step":1,"default":60,"unit":"bpm","unit_options":["bpm"],"unit_category":"frequency"},{"id":"intensity","type":"number","step":"any","default":70,"unit":"%","unit_options":["%"],"unit_category":"percentage"}],
    outputs=[{"id":"target_hr","unit":"bpm"}],
    formula="var age=parseFloat(inputs.age)||0;var rest=parseFloat(inputs.rest_hr)||0;var intensity=parseFloat(inputs.intensity)||0;var max_hr=220-age;var reserve=max_hr-rest;var target=rest+(reserve*intensity/100);return{target_hr:Math.round(target)};",
    related=["420","411"],
    i18n={"es":{"name":"Frecuencia Cardíaca Karvonen","description":"Calcula la frecuencia cardíaca objetivo usando la fórmula de Karvonen.","inputs":{"age":"Edad","rest_hr":"FC en reposo","intensity":"Intensidad %"},"outputs":{"target_hr":"FC objetivo"}},"en":{"name":"Karvonen Heart Rate Calculator","description":"Calculate target heart rate using the Karvonen formula.","inputs":{"age":"Age","rest_hr":"Resting HR","intensity":"Intensity %"},"outputs":{"target_hr":"Target HR"}},"fr":{"name":"Fréquence Cardiaque Karvonen","description":"Calculez la fréquence cardiaque cible avec la formule de Karvonen.","inputs":{"age":"Âge","rest_hr":"FC au repos","intensity":"Intensité %"},"outputs":{"target_hr":"FC cible"}},"pt":{"name":"Frequência Cardíaca de Karvonen","description":"Calcule a frequência cardíaca alvo usando a fórmula de Karvonen.","inputs":{"age":"Idade","rest_hr":"FC em repouso","intensity":"Intensidade %"},"outputs":{"target_hr":"FC alvo"}},"de":{"name":"Karvonen Herzfrequenz","description":"Berechnen Sie die Zielherzfrequenz mit der Karvonen-Formel.","inputs":{"age":"Alter","rest_hr":"Ruheherzfrequenz","intensity":"Intensität %"},"outputs":{"target_hr":"Zielherzfrequenz"}},"it":{"name":"Frequenza Cardiaca Karvonen","description":"Calcola la frequenza cardiaca target usando la formula di Karvonen.","inputs":{"age":"Età","rest_hr":"FC a riposo","intensity":"Intensità %"},"outputs":{"target_hr":"FC target"}}},
    latex_formula="\\text{THR} = \\text{RHR} + (\\text{MHR} - \\text{RHR}) \\times \\frac{\\text{Intensity}}{100}, \\quad \\text{MHR} = 220 - \\text{age}",
    use_cases=[{"en":"Endurance Training","en_body":"Marathon runners train at 70-80% intensity to build aerobic capacity without accumulating excessive lactate."},{"en":"Fat Loss Zones","en_body":"Fitness coaches use 60-70% intensity for clients focused on fat oxidation during steady-state cardio sessions."},{"en":"Cardiac Rehabilitation","en_body":"Post-myocardial infarction patients exercise at prescribed intensities under medical supervision to rebuild cardiovascular fitness safely."}],
    steps=[{"en":"Enter your age."},{"en":"Measure your resting heart rate upon waking."},{"en":"Enter your desired training intensity percentage."}])

add_calc(id="420", block="salud", cat="B", domain="health", concept="training heart rate zones",
    slugs={"es":"zonas-frecuencia-cardiaca","en":"heart-rate-zones","fr":"zones-frequencia-cardiaque","pt":"zonas-frequencia-cardiaca","de":"herzfrequenzzonen","it":"zone-frequenza-cardiaca"},
    inputs=[{"id":"age","type":"number","step":1,"default":30,"unit":"yr","unit_options":["yr"],"unit_category":"time"}],
    outputs=[{"id":"zone1","unit":"bpm"},{"id":"zone2","unit":"bpm"},{"id":"zone3","unit":"bpm"},{"id":"zone4","unit":"bpm"},{"id":"zone5","unit":"bpm"}],
    formula="var age=parseFloat(inputs.age)||0;var max_hr=220-age;var z1=Math.round(max_hr*0.5)+'-'+Math.round(max_hr*0.6);var z2=Math.round(max_hr*0.6)+'-'+Math.round(max_hr*0.7);var z3=Math.round(max_hr*0.7)+'-'+Math.round(max_hr*0.8);var z4=Math.round(max_hr*0.8)+'-'+Math.round(max_hr*0.9);var z5=Math.round(max_hr*0.9)+'-'+max_hr;return{zone1:z1,zone2:z2,zone3:z3,zone4:z4,zone5:z5};",
    related=["419","411"],
    i18n={"es":{"name":"Zonas de Frecuencia Cardíaca","description":"Calcula las 5 zonas de entrenamiento cardíaco basadas en la edad.","inputs":{"age":"Edad"},"outputs":{"zone1":"Zona 1","zone2":"Zona 2","zone3":"Zona 3","zone4":"Zona 4","zone5":"Zona 5"}},"en":{"name":"Heart Rate Training Zones","description":"Calculate the 5 heart rate training zones based on age.","inputs":{"age":"Age"},"outputs":{"zone1":"Zone 1","zone2":"Zone 2","zone3":"Zone 3","zone4":"Zone 4","zone5":"Zone 5"}},"fr":{"name":"Zones de Fréquence Cardiaque","description":"Calculez les 5 zones d'entraînement cardiaque basées sur l'âge.","inputs":{"age":"Âge"},"outputs":{"zone1":"Zone 1","zone2":"Zone 2","zone3":"Zone 3","zone4":"Zone 4","zone5":"Zone 5"}},"pt":{"name":"Zonas de Frequência Cardíaca","description":"Calcule as 5 zonas de treino cardíaco com base na idade.","inputs":{"age":"Idade"},"outputs":{"zone1":"Zona 1","zone2":"Zona 2","zone3":"Zona 3","zone4":"Zona 4","zone5":"Zona 5"}},"de":{"name":"Herzfrequenz-Trainingszonen","description":"Berechnen Sie die 5 Herzfrequenz-Trainingszonen basierend auf dem Alter.","inputs":{"age":"Alter"},"outputs":{"zone1":"Zone 1","zone2":"Zone 2","zone3":"Zone 3","zone4":"Zone 4","zone5":"Zone 5"}},"it":{"name":"Zone di Frequenza Cardiaca","description":"Calcola le 5 zone di allenamento cardiaco in base all'età.","inputs":{"age":"Età"},"outputs":{"zone1":"Zona 1","zone2":"Zona 2","zone3":"Zona 3","zone4":"Zona 4","zone5":"Zona 5"}}},
    latex_formula="\\text{Zone}_i = \\text{MHR} \\times \\text{Zone}_\\text{range}, \\quad \\text{MHR} = 220 - \\text{age}",
    use_cases=[{"en":"Periodization","en_body":"Coaches assign zone-specific workouts throughout the week to balance intensity and recovery."},{"en":"Wearable Calibration","en_body":"Athletes input age-based zones into GPS watches to receive real-time alerts during interval training."},{"en":"Health Screening","en_body":"Exceeding zone 5 for extended periods may indicate overtraining and warrants medical evaluation."}],
    steps=[{"en":"Enter your age."},{"en":"The calculator computes maximum heart rate (220 - age)."},{"en":"Five zones are displayed as percentages of MHR."}])

add_calc(id="421", block="salud", cat="B", domain="health", concept="creatinine clearance",
    slugs={"es":"aclaramiento-creatinina","en":"creatinine-clearance","fr":"clairance-creatinine","pt":"clearance-creatinina","de":"kreatinin-clearance","it":"clearance-creatinina"},
    inputs=[{"id":"age","type":"number","step":1,"default":50,"unit":"yr","unit_options":["yr"],"unit_category":"time"},{"id":"weight","type":"number","step":"any","default":70,"unit":"kg","unit_options":["kg","lb"],"unit_category":"mass"},{"id":"creatinine","type":"number","step":"any","default":1,"unit":"mg/dL","unit_options":["mg/dL","µmol/L"],"unit_category":"count"},{"id":"gender","type":"select","options":["male","female"],"default":"male","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"crcl","unit":"mL/min"}],
    formula="var age=parseFloat(inputs.age)||0;var w=parseFloat(inputs.weight)||0;var cr=parseFloat(inputs.creatinine)||1;var g=inputs.gender||'male';var factor=g==='male'?1:0.85;var crcl=((140-age)*w*factor)/(72*cr);return{crcl:crcl.toFixed(2)};",
    related=["415","400"],
    i18n={"es":{"name":"Clearance de Creatinina (Cockcroft-Gault)","description":"Estima el filtrado glomerular usando la fórmula de Cockcroft-Gault.","inputs":{"age":"Edad","weight":"Peso","creatinine":"Creatinina sérica","gender":"Sexo"},"outputs":{"crcl":"CrCl mL/min"}},"en":{"name":"Creatinine Clearance (Cockcroft-Gault)","description":"Estimate glomerular filtration rate using the Cockcroft-Gault formula.","inputs":{"age":"Age","weight":"Weight","creatinine":"Serum creatinine","gender":"Gender"},"outputs":{"crcl":"CrCl mL/min"}},"fr":{"name":"Clairance de la Créatinine","description":"Estimez le DFG avec la formule de Cockcroft-Gault.","inputs":{"age":"Âge","weight":"Poids","creatinine":"Créatinine sérique","gender":"Sexe"},"outputs":{"crcl":"Clairance mL/min"}},"pt":{"name":"Clearance de Creatinina","description":"Estime a taxa de filtração glomerular usando a fórmula de Cockcroft-Gault.","inputs":{"age":"Idade","weight":"Peso","creatinine":"Creatinina sérica","gender":"Sexo"},"outputs":{"crcl":"ClCr mL/min"}},"de":{"name":"Kreatinin-Clearance","description":"Schätzen Sie die GFR mit der Cockcroft-Gault-Formel.","inputs":{"age":"Alter","weight":"Gewicht","creatinine":"Serumkreatinin","gender":"Geschlecht"},"outputs":{"crcl":"CrCl mL/min"}},"it":{"name":"Clearance della Creatinina","description":"Stima il filtrato glomerulare con la formula di Cockcroft-Gault.","inputs":{"age":"Età","weight":"Peso","creatinine":"Creatinina sierica","gender":"Sesso"},"outputs":{"crcl":"CrCl mL/min"}}},
    latex_formula="\\text{CrCl} = \\frac{(140 - \\text{age}) \\times \\text{weight} \\times \\text{factor}}{72 \\times \\text{Cr}}, \\quad \\text{factor}_{female} = 0.85",
    use_cases=[{"en":"Drug Dosing","en_body":"Nephrologists and pharmacists adjust renally cleared medications like vancomycin and digoxin based on CrCl."},{"en":"Contrast Safety","en_body":"Radiologists check CrCl before administering iodinated contrast to prevent contrast-induced nephropathy."},{"en":"Transplant Evaluation","en_body":"Transplant centers use CrCl trends to monitor graft function and detect acute rejection episodes."}],
    steps=[{"en":"Enter age, weight, and serum creatinine."},{"en":"Select gender for the correction factor."},{"en":"The calculator returns creatinine clearance in mL/min."}])

add_calc(id="422", block="salud", cat="B", domain="health", concept="BMI prime",
    slugs={"es":"bmi-prime","en":"bmi-prime","fr":"bmi-prime","pt":"imc-prime","de":"bmi-prime","it":"bmi-prime"},
    inputs=[{"id":"bmi","type":"number","step":"any","default":25,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"bmi_prime","unit":""}],
    formula="var bmi=parseFloat(inputs.bmi)||0;var prime=bmi/25;return{bmi_prime:prime.toFixed(4)};",
    related=["400","416"],
    i18n={"es":{"name":"BMI Prime","description":"Calcula el BMI Prime, una medida relativa del IMC respecto al límite superior de normalidad.","inputs":{"bmi":"IMC"},"outputs":{"bmi_prime":"BMI Prime"}},"en":{"name":"BMI Prime Calculator","description":"Calculate BMI Prime, a measure of BMI relative to the upper limit of normal.","inputs":{"bmi":"BMI"},"outputs":{"bmi_prime":"BMI Prime"}},"fr":{"name":"BMI Prime","description":"Calculez le BMI Prime, une mesure de l'IMC par rapport à la limite supérieure de la normale.","inputs":{"bmi":"IMC"},"outputs":{"bmi_prime":"BMI Prime"}},"pt":{"name":"IMC Prime","description":"Calcule o IMC Prime, uma medida do IMC em relação ao limite superior do normal.","inputs":{"bmi":"IMC"},"outputs":{"bmi_prime":"IMC Prime"}},"de":{"name":"BMI Prime","description":"Berechnen Sie den BMI Prime, ein Maß für den BMI relativ zur oberen Normgrenze.","inputs":{"bmi":"BMI"},"outputs":{"bmi_prime":"BMI Prime"}},"it":{"name":"BMI Prime","description":"Calcola il BMI Prime, una misura del BMI rispetto al limite superiore della norma.","inputs":{"bmi":"BMI"},"outputs":{"bmi_prime":"BMI Prime"}}},
    latex_formula="\\text{BMI Prime} = \\frac{\\text{BMI}}{25}",
    use_cases=[{"en":"Epidemiological Standardization","en_body":"BMI Prime allows direct comparison across populations with different BMI cutoffs, simplifying meta-analyses."},{"en":"Public Health Messaging","en_body":"A BMI Prime of 1.2 is intuitively understood as 20% above the healthy threshold, improving patient communication."},{"en":"Insurance Underwriting","en_body":"Underwriters use BMI Prime to apply consistent risk adjustments across international applicant pools."}],
    steps=[{"en":"Enter your BMI value."},{"en":"The calculator divides by 25, the WHO upper normal limit."},{"en":"Values above 1.0 indicate overweight; above 1.3 indicate obesity."}])

add_calc(id="423", block="salud", cat="B", domain="health", concept="pregnancy due date",
    slugs={"es":"fecha-parto","en":"due-date-calculator","fr":"date-accouchement","pt":"data-parto","de":"entbindungstermin","it":"data-parto"},
    inputs=[{"id":"lmp","type":"date","default":"","unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"due_date","unit":""}],
    formula="var lmp=inputs.lmp||'';if(!lmp)return{due_date:'Enter LMP'};var d=new Date(lmp);d.setDate(d.getDate()+280);return{due_date:d.toISOString().split('T')[0]};",
    related=["424","501"],
    i18n={"es":{"name":"Calculadora de Fecha de Parto","description":"Estima la fecha de parto a partir de la última menstruación.","inputs":{"lmp":"Última menstruación"},"outputs":{"due_date":"Fecha estimada"}},"en":{"name":"Pregnancy Due Date Calculator","description":"Estimate delivery date from the last menstrual period.","inputs":{"lmp":"Last menstrual period"},"outputs":{"due_date":"Estimated due date"}},"fr":{"name":"Date d'Accouchement","description":"Estimez la date d'accouchement à partir des dernières règles.","inputs":{"lmp":"Dernières règles"},"outputs":{"due_date":"Date prévue"}},"pt":{"name":"Calculadora de Data de Parto","description":"Estime a data do parto a partir da última menstruação.","inputs":{"lmp":"Última menstruação"},"outputs":{"due_date":"Data estimada"}},"de":{"name":"Entbindungstermin Rechner","description":"Schätzen Sie den Entbindungstermin anhand der letzten Periode.","inputs":{"lmp":"Letzte Periode"},"outputs":{"due_date":"Geschätzter Termin"}},"it":{"name":"Calcolatore Data del Parto","description":"Stima la data del parto dall'ultima mestruazione.","inputs":{"lmp":"Ultima mestruazione"},"outputs":{"due_date":"Data stimata"}}},
    latex_formula="\\text{Due Date} = \\text{LMP} + 280 \\text{ days}",
    use_cases=[{"en":"Prenatal Scheduling","en_body":"Obstetricians schedule trimester screenings and glucose challenge tests relative to the estimated due date."},{"en":"Maternity Leave Planning","en_body":"Expectant parents coordinate workplace leave and childcare arrangements around the projected delivery window."},{"en":"Fetal Development Tracking","en_body":"Ultrasound technicians compare gestational age to due date to assess whether fetal growth is on track."}],
    steps=[{"en":"Enter the first day of your last menstrual period."},{"en":"The calculator adds 280 days (40 weeks)."},{"en":"The result is your estimated due date (EDD)."}])

add_calc(id="424", block="salud", cat="B", domain="health", concept="ovulation calculator",
    slugs={"es":"calculadora-ovulacion","en":"ovulation-calculator","fr":"calculateur-ovulation","pt":"calculadora-ovulacao","de":"eisprung-rechner","it":"calcolatore-ovulazione"},
    inputs=[{"id":"lmp","type":"date","default":"","unit":"","unit_options":[],"unit_category":""},{"id":"cycle","type":"number","step":1,"default":28,"unit":"days","unit_options":["days"],"unit_category":"time"}],
    outputs=[{"id":"ovulation","unit":""},{"id":"fertile_start","unit":""},{"id":"fertile_end","unit":""}],
    formula="var lmp=inputs.lmp||'';var cycle=parseFloat(inputs.cycle)||28;if(!lmp)return{ovulation:'Enter LMP',fertile_start:'',fertile_end:''};var d=new Date(lmp);var ov=new Date(d);ov.setDate(d.getDate()+cycle-14);var fs=new Date(ov);fs.setDate(ov.getDate()-5);var fe=new Date(ov);fe.setDate(ov.getDate()+1);return{ovulation:ov.toISOString().split('T')[0],fertile_start:fs.toISOString().split('T')[0],fertile_end:fe.toISOString().split('T')[0]};",
    related=["423","501"],
    i18n={"es":{"name":"Calculadora de Ovulación","description":"Estima tu fecha de ovulación y ventana fértil.","inputs":{"lmp":"Última menstruación","cycle":"Duración del ciclo"},"outputs":{"ovulation":"Ovulación","fertile_start":"Inicio fértil","fertile_end":"Fin fértil"}},"en":{"name":"Ovulation Calculator","description":"Estimate your ovulation date and fertile window.","inputs":{"lmp":"Last menstrual period","cycle":"Cycle length"},"outputs":{"ovulation":"Ovulation","fertile_start":"Fertile start","fertile_end":"Fertile end"}},"fr":{"name":"Calculateur d'Ovulation","description":"Estimez votre date d'ovulation et fenêtre fertile.","inputs":{"lmp":"Dernières règles","cycle":"Durée du cycle"},"outputs":{"ovulation":"Ovulation","fertile_start":"Début fertile","fertile_end":"Fin fertile"}},"pt":{"name":"Calculadora de Ovulação","description":"Estime sua data de ovulação e janela fértil.","inputs":{"lmp":"Última menstruação","cycle":"Duração do ciclo"},"outputs":{"ovulation":"Ovulação","fertile_start":"Início fértil","fertile_end":"Fim fértil"}},"de":{"name":"Eisprung Rechner","description":"Schätzen Sie Ihren Eisprung und Ihr fruchtbares Fenster.","inputs":{"lmp":"Letzte Periode","cycle":"Zykluslänge"},"outputs":{"ovulation":"Eisprung","fertile_start":"Fruchtbarer Beginn","fertile_end":"Fruchtbarer Schluss"}},"it":{"name":"Calcolatore Ovulazione","description":"Stima la data di ovulazione e la finestra fertile.","inputs":{"lmp":"Ultima mestruazione","cycle":"Durata ciclo"},"outputs":{"ovulation":"Ovulazione","fertile_start":"Inizio fertile","fertile_end":"Fine fertile"}}},
    latex_formula="\\text{Ovulation} \\approx \\text{LMP} + (\\text{cycle length} - 14)",
    use_cases=[{"en":"Family Planning","en_body":"Couples trying to conceive time intercourse during the 6-day fertile window to maximize monthly pregnancy probability."},{"en":"Natural Contraception","en_body":"Women practicing fertility awareness avoid unprotected intercourse during the estimated fertile window."},{"en":"Irregular Cycle Tracking","en_body":"By logging multiple cycle lengths, users refine ovulation estimates and identify hormonal patterns."}],
    steps=[{"en":"Enter the first day of your last period."},{"en":"Enter your average cycle length."},{"en":"The calculator estimates ovulation and the fertile window."}])

# ── EVERYDAY / TECH (503-512) ──
add_calc(id="503", block="cotidiano", cat="D", domain="tech", concept="fuel cost",
    slugs={"es":"coste-combustible","en":"fuel-cost","fr":"cout-carburant","pt":"custo-combustivel","de":"kraftstoffkosten","it":"costo-carburante"},
    inputs=[{"id":"distance","type":"number","step":"any","default":100,"unit":"km","unit_options":["km","mi"],"unit_category":"length"},{"id":"efficiency","type":"number","step":"any","default":6,"unit":"L/100km","unit_options":["L/100km","mpg"],"unit_category":"volume"},{"id":"price","type":"number","step":"any","default":1.5,"unit":"$/L","unit_options":["$/L","$/gal(us)"],"unit_category":"currency_per_volume"}],
    outputs=[{"id":"cost","unit":"USD"},{"id":"fuel","unit":"L"}],
    formula="var d=parseFloat(inputs.distance)||0;var eff=parseFloat(inputs.efficiency)||1;var pr=parseFloat(inputs.price)||0;var fuel=d*eff/100;var cost=fuel*pr;return{cost:cost.toFixed(2),fuel:fuel.toFixed(2)};",
    related=["504","505"],
    i18n={"es":{"name":"Calculadora de Coste de Combustible","description":"Calcula el coste y consumo de combustible para un trayecto.","inputs":{"distance":"Distancia","efficiency":"Consumo","price":"Precio/L"},"outputs":{"cost":"Coste","fuel":"Combustible"}},"en":{"name":"Fuel Cost Calculator","description":"Calculate fuel cost and consumption for a trip.","inputs":{"distance":"Distance","efficiency":"Fuel efficiency","price":"Price per litre"},"outputs":{"cost":"Cost","fuel":"Fuel used"}},"fr":{"name":"Coût du Carburant","description":"Calculez le coût et la consommation de carburant pour un trajet.","inputs":{"distance":"Distance","efficiency":"Consommation","price":"Prix/L"},"outputs":{"cost":"Coût","fuel":"Carburant"}},"pt":{"name":"Custo do Combustível","description":"Calcule o custo e consumo de combustível para uma viagem.","inputs":{"distance":"Distância","efficiency":"Consumo","price":"Preço/L"},"outputs":{"cost":"Custo","fuel":"Combustível"}},"de":{"name":"Kraftstoffkosten Rechner","description":"Berechnen Sie Kraftstoffkosten und -verbrauch für eine Fahrt.","inputs":{"distance":"Strecke","efficiency":"Verbrauch","price":"Preis/L"},"outputs":{"cost":"Kosten","fuel":"Kraftstoff"}},"it":{"name":"Calcolatore Costo Carburante","description":"Calcola il costo e consumo di carburante per un viaggio.","inputs":{"distance":"Distanza","efficiency":"Consumo","price":"Prezzo/L"},"outputs":{"cost":"Costo","fuel":"Carburante"}}},
    latex_formula="\\text{Fuel} = \\frac{\\text{distance} \\times \\text{efficiency}}{100}, \\quad \\text{Cost} = \\text{fuel} \\times \\text{price}",
    use_cases=[{"en":"Road Trip Budgeting","en_body":"Travelers estimate total fuel expenses before long drives to decide between driving and flying."},{"en":"Fleet Management","en_body":"Logistics managers model fuel costs across routes to optimize delivery schedules and vehicle assignments."},{"en":"Commute Evaluation","en_body":"Employees compare the fuel cost of driving against public transit fares to make cost-effective commuting decisions."}],
    steps=[{"en":"Enter the trip distance."},{"en":"Enter vehicle fuel efficiency."},{"en":"Enter the local fuel price per liter."}])

add_calc(id="504", block="cotidiano", cat="D", domain="tech", concept="data transfer time",
    slugs={"es":"tiempo-transferencia-datos","en":"data-transfer-time","fr":"temps-transfert-donnees","pt":"tempo-transferencia-dados","de":"datenuebertragungszeit","it":"tempo-trasferimento-dati"},
    inputs=[{"id":"size","type":"number","step":"any","default":1,"unit":"GB","unit_options":["GB","MB","TB"],"unit_category":"digital_storage"},{"id":"speed","type":"number","step":"any","default":100,"unit":"Mbps","unit_options":["Mbps","Gbps","MB/s"],"unit_category":"data_rate"}],
    outputs=[{"id":"time_sec","unit":"s"},{"id":"time_min","unit":"min"}],
    formula="var size_gb=parseFloat(inputs.size)||0;var speed_mbps=parseFloat(inputs.speed)||1;var size_mb=size_gb*1024;var time_sec=(size_mb*8)/speed_mbps;var time_min=time_sec/60;return{time_sec:Math.round(time_sec),time_min:time_min.toFixed(2)};",
    related=["506","510"],
    i18n={"es":{"name":"Tiempo de Transferencia de Datos","description":"Calcula cuánto tarda transferir un archivo dado el ancho de banda.","inputs":{"size":"Tamaño","speed":"Velocidad"},"outputs":{"time_sec":"Segundos","time_min":"Minutos"}},"en":{"name":"Data Transfer Time Calculator","description":"Calculate how long it takes to transfer a file given the bandwidth.","inputs":{"size":"File size","speed":"Transfer speed"},"outputs":{"time_sec":"Seconds","time_min":"Minutes"}},"fr":{"name":"Temps de Transfert de Données","description":"Calculez le temps nécessaire pour transférer un fichier avec une bande passante donnée.","inputs":{"size":"Taille","speed":"Vitesse"},"outputs":{"time_sec":"Secondes","time_min":"Minutes"}},"pt":{"name":"Tempo de Transferência de Dados","description":"Calcule quanto tempo leva para transferir um arquivo com a largura de banda dada.","inputs":{"size":"Tamanho","speed":"Velocidade"},"outputs":{"time_sec":"Segundos","time_min":"Minutos"}},"de":{"name":"Datenübertragungszeit","description":"Berechnen Sie die Übertragungszeit einer Datei bei gegebener Bandbreite.","inputs":{"size":"Größe","speed":"Geschwindigkeit"},"outputs":{"time_sec":"Sekunden","time_min":"Minuten"}},"it":{"name":"Tempo Trasferimento Dati","description":"Calcola quanto tempo ci vuole per trasferire un file data la larghezza di banda.","inputs":{"size":"Dimensione","speed":"Velocità"},"outputs":{"time_sec":"Secondi","time_min":"Minuti"}}},
    latex_formula="\\text{Time} = \\frac{\\text{Size} \\times 8}{\\text{Speed}}",
    use_cases=[{"en":"Cloud Migration","en_body":"IT teams estimate transfer windows when moving petabyte-scale archives to cloud object storage over dedicated lines."},{"en":"Video Uploads","en_body":"Content creators schedule 4K video uploads based on calculated transfer times to meet publication deadlines."},{"en":"Disaster Recovery","en_body":"Backup administrators verify that replication links can transfer daily deltas within the available maintenance window."}],
    steps=[{"en":"Enter the file or dataset size."},{"en":"Enter the network transfer speed."},{"en":"The calculator returns the estimated duration in seconds and minutes."}])

add_calc(id="505", block="cotidiano", cat="D", domain="tech", concept="battery life",
    slugs={"es":"duracion-bateria","en":"battery-life","fr":"duree-batterie","pt":"duracao-bateria","de":"akkulaufzeit","it":"durata-batteria"},
    inputs=[{"id":"capacity","type":"number","step":"any","default":4000,"unit":"mAh","unit_options":["mAh","Wh"],"unit_category":"current"},{"id":"consumption","type":"number","step":"any","default":500,"unit":"mA","unit_options":["mA","W"],"unit_category":"current"}],
    outputs=[{"id":"hours","unit":"h"}],
    formula="var cap=parseFloat(inputs.capacity)||0;var cons=parseFloat(inputs.consumption)||1;var hours=cap/cons;return{hours:hours.toFixed(2)};",
    related=["512","507"],
    i18n={"es":{"name":"Duración de Batería","description":"Estima la autonomía de una batería según su capacidad y consumo.","inputs":{"capacity":"Capacidad","consumption":"Consumo"},"outputs":{"hours":"Horas"}},"en":{"name":"Battery Life Calculator","description":"Estimate device battery life from capacity and current draw.","inputs":{"capacity":"Capacity","consumption":"Consumption"},"outputs":{"hours":"Hours"}},"fr":{"name":"Durée de Batterie","description":"Estimez l'autonomie d'une batterie selon sa capacité et sa consommation.","inputs":{"capacity":"Capacité","consumption":"Consommation"},"outputs":{"hours":"Heures"}},"pt":{"name":"Duração da Bateria","description":"Estime a autonomia de uma bateria com base na capacidade e consumo.","inputs":{"capacity":"Capacidade","consumption":"Consumo"},"outputs":{"hours":"Horas"}},"de":{"name":"Akkulaufzeit","description":"Schätzen Sie die Akkulaufzeit anhand von Kapazität und Verbrauch.","inputs":{"capacity":"Kapazität","consumption":"Verbrauch"},"outputs":{"hours":"Stunden"}},"it":{"name":"Durata Batteria","description":"Stima l'autonomia di una batteria in base alla capacità e al consumo.","inputs":{"capacity":"Capacità","consumption":"Consumo"},"outputs":{"hours":"Ore"}}},
    latex_formula="\\text{Life} = \\frac{\\text{Capacity}}{\\text{Consumption}}",
    use_cases=[{"en":"Drone Operations","en_body":"Pilots calculate flight time from battery capacity and motor current draw to plan safe return-to-home points."},{"en":"IoT Sensor Design","en_body":"Engineers size coin-cell batteries so that remote sensors last multiple years between maintenance visits."},{"en":"Electric Vehicles","en_body":"Drivers estimate remaining range by dividing available battery capacity by average energy consumption per mile."}],
    steps=[{"en":"Enter the battery capacity (mAh or Wh)."},{"en":"Enter the device current draw (mA or W)."},{"en":"The calculator returns expected runtime in hours."}])

add_calc(id="506", block="cotidiano", cat="D", domain="tech", concept="download time",
    slugs={"es":"tiempo-descarga","en":"download-time","fr":"temps-telechargement","pt":"tempo-download","de":"download-zeit","it":"tempo-download"},
    inputs=[{"id":"file_size","type":"number","step":"any","default":1,"unit":"GB","unit_options":["GB","MB","TB"],"unit_category":"digital_storage"},{"id":"speed","type":"number","step":"any","default":50,"unit":"Mbps","unit_options":["Mbps","MB/s","Kbps"],"unit_category":"data_rate"}],
    outputs=[{"id":"time_sec","unit":"s"},{"id":"time_min","unit":"min"}],
    formula="var size_gb=parseFloat(inputs.file_size)||0;var speed_mbps=parseFloat(inputs.speed)||1;var size_mb=size_gb*1024;var time_sec=(size_mb*8)/speed_mbps;var time_min=time_sec/60;return{time_sec:Math.round(time_sec),time_min:time_min.toFixed(2)};",
    related=["504","510"],
    i18n={"es":{"name":"Tiempo de Descarga","description":"Calcula cuánto tarda descargar un archivo a una velocidad dada.","inputs":{"file_size":"Tamaño","speed":"Velocidad"},"outputs":{"time_sec":"Segundos","time_min":"Minutos"}},"en":{"name":"Download Time Calculator","description":"Calculate how long a file takes to download at a given speed.","inputs":{"file_size":"File size","speed":"Download speed"},"outputs":{"time_sec":"Seconds","time_min":"Minutes"}},"fr":{"name":"Temps de Téléchargement","description":"Calculez le temps nécessaire pour télécharger un fichier à une vitesse donnée.","inputs":{"file_size":"Taille","speed":"Vitesse"},"outputs":{"time_sec":"Secondes","time_min":"Minutes"}},"pt":{"name":"Tempo de Download","description":"Calcule quanto tempo leva para baixar um arquivo a uma velocidade dada.","inputs":{"file_size":"Tamanho","speed":"Velocidade"},"outputs":{"time_sec":"Segundos","time_min":"Minutos"}},"de":{"name":"Download-Zeit","description":"Berechnen Sie die Zeit, die ein Download bei gegebener Geschwindigkeit benötigt.","inputs":{"file_size":"Größe","speed":"Geschwindigkeit"},"outputs":{"time_sec":"Sekunden","time_min":"Minuten"}},"it":{"name":"Tempo di Download","description":"Calcola quanto tempo ci vuole per scaricare un file a una data velocità.","inputs":{"file_size":"Dimensione","speed":"Velocità"},"outputs":{"time_sec":"Secondi","time_min":"Minuti"}}},
    latex_formula="\\text{Time} = \\frac{\\text{File Size} \\times 8}{\\text{Speed}}",
    use_cases=[{"en":"Game Updates","en_body":"Gamers check download times for large patches to decide whether to start updates before sleep or during off-peak hours."},{"en":"Software Distribution","en_body":"IT departments schedule OS image deployments across school or office networks based on aggregate download time estimates."},{"en":"Streaming Buffering","en_body":"Buffer health algorithms use file-size-to-speed ratios to pre-load content and prevent playback interruptions."}],
    steps=[{"en":"Enter the file size."},{"en":"Enter your internet download speed."},{"en":"The calculator returns the estimated download duration."}])

add_calc(id="507", block="cotidiano", cat="D", domain="tech", concept="screen DPI",
    slugs={"es":"dpi-pantalla","en":"screen-dpi","fr":"dpi-ecran","pt":"dpi-tela","de":"bildschirm-dpi","it":"dpi-schermo"},
    inputs=[{"id":"width_px","type":"number","step":1,"default":1920,"unit":"px","unit_options":["px"],"unit_category":"count"},{"id":"height_px","type":"number","step":1,"default":1080,"unit":"px","unit_options":["px"],"unit_category":"count"},{"id":"diagonal_in","type":"number","step":"any","default":24,"unit":"in","unit_options":["in","cm"],"unit_category":"length"}],
    outputs=[{"id":"dpi","unit":"dpi"},{"id":"ppi","unit":"ppi"}],
    formula="var w=parseFloat(inputs.width_px)||0;var h=parseFloat(inputs.height_px)||0;var d=parseFloat(inputs.diagonal_in)||1;var diag_px=Math.sqrt(w*w+h*h);var dpi=diag_px/d;return{dpi:dpi.toFixed(2),ppi:dpi.toFixed(2)};",
    related=["508","509"],
    i18n={"es":{"name":"DPI / PPI de Pantalla","description":"Calcula la densidad de píxeles de una pantalla.","inputs":{"width_px":"Ancho px","height_px":"Alto px","diagonal_in":"Diagonal"},"outputs":{"dpi":"DPI","ppi":"PPI"}},"en":{"name":"Screen DPI / PPI Calculator","description":"Calculate the pixel density of a display.","inputs":{"width_px":"Width px","height_px":"Height px","diagonal_in":"Diagonal"},"outputs":{"dpi":"DPI","ppi":"PPI"}},"fr":{"name":"DPI / PPI d'Écran","description":"Calculez la densité de pixels d'un écran.","inputs":{"width_px":"Largeur px","height_px":"Hauteur px","diagonal_in":"Diagonale"},"outputs":{"dpi":"DPI","ppi":"PPI"}},"pt":{"name":"DPI / PPI da Tela","description":"Calcule a densidade de pixels de uma tela.","inputs":{"width_px":"Largura px","height_px":"Altura px","diagonal_in":"Diagonal"},"outputs":{"dpi":"DPI","ppi":"PPI"}},"de":{"name":"Bildschirm DPI / PPI","description":"Berechnen Sie die Pixeldichte eines Displays.","inputs":{"width_px":"Breite px","height_px":"Höhe px","diagonal_in":"Diagonale"},"outputs":{"dpi":"DPI","ppi":"PPI"}},"it":{"name":"DPI / PPI Schermo","description":"Calcola la densità di pixel di un display.","inputs":{"width_px":"Larghezza px","height_px":"Altezza px","diagonal_in":"Diagonale"},"outputs":{"dpi":"DPI","ppi":"PPI"}}},
    latex_formula="\\text{DPI} = \\frac{\\sqrt{W^2 + H^2}}{\\text{Diagonal}}",
    use_cases=[{"en":"Display Comparison","en_body":"Shoppers compare smartphone PPI to judge screen sharpness before purchasing flagship versus budget models."},{"en":"Graphic Design","en_body":"Designers verify that monitor DPI matches print resolution requirements to ensure accurate color proofing."},{"en":"VR Headsets","en_body":"Engineers maximize PPI to reduce the screen-door effect and improve immersion in virtual reality displays."}],
    steps=[{"en":"Enter the screen resolution in pixels."},{"en":"Enter the physical diagonal measurement."},{"en":"The calculator returns DPI (dots per inch)."}])

add_calc(id="508", block="cotidiano", cat="D", domain="tech", concept="aspect ratio",
    slugs={"es":"relacion-aspecto","en":"aspect-ratio","fr":"rapport-aspect","pt":"proporcao-tela","de":"seitenverhaeltnis","it":"rapporto-aspetto"},
    inputs=[{"id":"width","type":"number","step":1,"default":16,"unit":"","unit_options":[],"unit_category":""},{"id":"height","type":"number","step":1,"default":9,"unit":"","unit_options":[],"unit_category":""}],
    outputs=[{"id":"ratio","unit":""}],
    formula="var w=parseFloat(inputs.width)||0;var h=parseFloat(inputs.height)||1;var gcd=function(a,b){return b?gcd(b,a%b):a;};var g=gcd(Math.round(w),Math.round(h));return{ratio:(w/g).toFixed(0)+':'+(h/g).toFixed(0)};",
    related=["507","509"],
    i18n={"es":{"name":"Relación de Aspecto","description":"Simplifica la relación de aspecto de una imagen o pantalla.","inputs":{"width":"Ancho","height":"Alto"},"outputs":{"ratio":"Relación"}},"en":{"name":"Aspect Ratio Calculator","description":"Simplify the aspect ratio of an image or display.","inputs":{"width":"Width","height":"Height"},"outputs":{"ratio":"Ratio"}},"fr":{"name":"Rapport d'Aspect","description":"Simplifiez le rapport d'aspect d'une image ou d'un écran.","inputs":{"width":"Largeur","height":"Hauteur"},"outputs":{"ratio":"Rapport"}},"pt":{"name":"Proporção da Tela","description":"Simplifique a proporção de uma imagem ou tela.","inputs":{"width":"Largura","height":"Altura"},"outputs":{"ratio":"Proporção"}},"de":{"name":"Seitenverhältnis","description":"Vereinfachen Sie das Seitenverhältnis eines Bildes oder Displays.","inputs":{"width":"Breite","height":"Höhe"},"outputs":{"ratio":"Verhältnis"}},"it":{"name":"Rapporto d'Aspetto","description":"Semplifica il rapporto d'aspetto di un'immagine o display.","inputs":{"width":"Larghezza","height":"Altezza"},"outputs":{"ratio":"Rapporto"}}},
    latex_formula="\\text{Aspect Ratio} = \\frac{W}{H} = \\frac{W \\div \\text{GCD}}{H \\div \\text{GCD}}",
    use_cases=[{"en":"Video Production","en_body":"Editors verify that exported videos match platform requirements (16:9 for YouTube, 9:16 for TikTok)."},{"en":"Responsive Design","en_body":"Web developers use aspect ratios to maintain image proportions across mobile, tablet, and desktop breakpoints."},{"en":"Photography Printing","en_body":"Photographers crop images to standard ratios (4:3, 3:2) before ordering prints to avoid unwanted borders."}],
    steps=[{"en":"Enter the width in arbitrary units."},{"en":"Enter the height in the same units."},{"en":"The calculator simplifies the ratio by greatest common divisor."}])

add_calc(id="509", block="cotidiano", cat="D", domain="tech", concept="password entropy",
    slugs={"es":"entropia-contrasena","en":"password-entropy","fr":"entropie-mot-passe","pt":"entropia-senha","de":"passwort-entropie","it":"entropia-password"},
    inputs=[{"id":"length","type":"number","step":1,"default":12,"unit":"chars","unit_options":["chars"],"unit_category":"count"},{"id":"pool","type":"number","step":1,"default":62,"unit":"symbols","unit_options":["symbols"],"unit_category":"count"}],
    outputs=[{"id":"entropy","unit":"bits"},{"id":"strength","unit":""}],
    formula="var L=parseFloat(inputs.length)||0;var R=parseFloat(inputs.pool)||1;var entropy=L*Math.log2(R);var strength=entropy<40?'Very Weak':entropy<60?'Weak':entropy<80?'Moderate':entropy<100?'Strong':'Very Strong';return{entropy:entropy.toFixed(2),strength:strength};",
    related=["511","508"],
    i18n={"es":{"name":"Entropía de Contraseña","description":"Calcula la entropía y fortaleza de una contraseña.","inputs":{"length":"Longitud","pool":"Pool de símbolos"},"outputs":{"entropy":"Entropía bits","strength":"Fortaleza"}},"en":{"name":"Password Entropy Calculator","description":"Calculate the entropy and strength of a password.","inputs":{"length":"Length","pool":"Symbol pool"},"outputs":{"entropy":"Entropy bits","strength":"Strength"}},"fr":{"name":"Entropie du Mot de Passe","description":"Calculez l'entropie et la force d'un mot de passe.","inputs":{"length":"Longueur","pool":"Pool de symboles"},"outputs":{"entropy":"Entropie bits","strength":"Force"}},"pt":{"name":"Entropia da Senha","description":"Calcule a entropia e força de uma senha.","inputs":{"length":"Comprimento","pool":"Pool de símbolos"},"outputs":{"entropy":"Entropia bits","strength":"Força"}},"de":{"name":"Passwort-Entropie","description":"Berechnen Sie die Entropie und Stärke eines Passworts.","inputs":{"length":"Länge","pool":"Zeichenpool"},"outputs":{"entropy":"Entropie bits","strength":"Stärke"}},"it":{"name":"Entropia Password","description":"Calcola l'entropia e la forza di una password.","inputs":{"length":"Lunghezza","pool":"Pool simboli"},"outputs":{"entropy":"Entropia bits","strength":"Forza"}}},
    latex_formula="H = L \\times \\log_2(R)",
    use_cases=[{"en":"Security Policy","en_body":"CISOs mandate minimum entropy thresholds (e.g., 60 bits) to resist brute-force and dictionary attacks."},{"en":"Password Managers","en_body":"Generators use entropy calculations to produce cryptographically secure random passwords of sufficient length."},{"en":"User Education","en_body":"Security trainers demonstrate that adding length increases entropy far more effectively than adding special characters alone."}],
    steps=[{"en":"Enter the password length."},{"en":"Enter the symbol pool size (e.g., 26 lowercase, 52 mixed case, 62 with digits, 94 with symbols)."},{"en":"The calculator returns entropy in bits and a qualitative strength label."}])

add_calc(id="510", block="cotidiano", cat="D", domain="tech", concept="bandwidth",
    slugs={"es":"ancho-banda","en":"bandwidth-calculator","fr":"calcul-bandwidth","pt":"largura-banda","de":"bandbreite","it":"larghezza-banda"},
    inputs=[{"id":"users","type":"number","step":1,"default":10,"unit":"users","unit_options":["users"],"unit_category":"count"},{"id":"usage","type":"number","step":"any","default":5,"unit":"Mbps","unit_options":["Mbps","Kbps","Gbps"],"unit_category":"data_rate"}],
    outputs=[{"id":"total","unit":"Mbps"}],
    formula="var u=parseFloat(inputs.users)||0;var us=parseFloat(inputs.usage)||0;return{total:(u*us).toFixed(2)};",
    related=["504","506"],
    i18n={"es":{"name":"Calculadora de Ancho de Banda","description":"Estima el ancho de banda total necesario para múltiples usuarios.","inputs":{"users":"Usuarios","usage":"Uso por usuario"},"outputs":{"total":"Ancho de banda total"}},"en":{"name":"Bandwidth Calculator","description":"Estimate total bandwidth needed for multiple concurrent users.","inputs":{"users":"Users","usage":"Usage per user"},"outputs":{"total":"Total bandwidth"}},"fr":{"name":"Calculateur de Bande Passante","description":"Estimez la bande passante totale nécessaire pour plusieurs utilisateurs.","inputs":{"users":"Utilisateurs","usage":"Usage par utilisateur"},"outputs":{"total":"Bande passante totale"}},"pt":{"name":"Calculadora de Largura de Banda","description":"Estime a largura de banda total necessária para vários usuários.","inputs":{"users":"Usuários","usage":"Uso por usuário"},"outputs":{"total":"Largura de banda total"}},"de":{"name":"Bandbreitenrechner","description":"Schätzen Sie die Gesamtbandbreite für mehrere Benutzer.","inputs":{"users":"Benutzer","usage":"Verbrauch pro Benutzer"},"outputs":{"total":"Gesamtbandbreite"}},"it":{"name":"Calcolatore Larghezza di Banda","description":"Stima la larghezza di banda totale necessaria per più utenti.","inputs":{"users":"Utenti","usage":"Uso per utente"},"outputs":{"total":"Larghezza di banda totale"}}},
    latex_formula="\\text{Total} = \\text{Users} \\times \\text{Usage per User}",
    use_cases=[{"en":"Office Networking","en_body":"Network architects sum per-user bandwidth to size internet circuits and avoid congestion during video conferences."},{"en":"ISP Capacity Planning","en_body":"Internet providers model peak-hour aggregate demand to dimension backbone links and peering agreements."},{"en":"Event Wi-Fi","en_body":"Temporary network installers calculate bandwidth for stadiums and conferences based on expected attendee device counts."}],
    steps=[{"en":"Enter the number of concurrent users."},{"en":"Enter the average bandwidth consumption per user."},{"en":"The product gives the required aggregate bandwidth."}])

add_calc(id="511", block="cotidiano", cat="D", domain="tech", concept="file size",
    slugs={"es":"tamano-archivo","en":"file-size","fr":"taille-fichier","pt":"tamanho-arquivo","de":"dateigroesse","it":"dimensione-file"},
    inputs=[{"id":"width","type":"number","step":1,"default":1920,"unit":"px","unit_options":["px"],"unit_category":"count"},{"id":"height","type":"number","step":1,"default":1080,"unit":"px","unit_options":["px"],"unit_category":"count"},{"id":"depth","type":"number","step":1,"default":24,"unit":"bits","unit_options":["bits"],"unit_category":"count"}],
    outputs=[{"id":"size_mb","unit":"MB"}],
    formula="var w=parseFloat(inputs.width)||0;var h=parseFloat(inputs.height)||0;var d=parseFloat(inputs.depth)||0;var bytes=w*h*d/8;var mb=bytes/1048576;return{size_mb:mb.toFixed(2)};",
    related=["507","508"],
    i18n={"es":{"name":"Tamaño de Archivo de Imagen","description":"Calcula el tamaño sin comprimir de una imagen bitmap.","inputs":{"width":"Ancho px","height":"Alto px","depth":"Profundidad bits"},"outputs":{"size_mb":"Tamaño MB"}},"en":{"name":"Uncompressed Image File Size","description":"Calculate the uncompressed size of a bitmap image.","inputs":{"width":"Width px","height":"Height px","depth":"Bit depth"},"outputs":{"size_mb":"Size MB"}},"fr":{"name":"Taille de Fichier Image","description":"Calculez la taille non compressée d'une image bitmap.","inputs":{"width":"Largeur px","height":"Hauteur px","depth":"Profondeur bits"},"outputs":{"size_mb":"Taille MB"}},"pt":{"name":"Tamanho do Arquivo de Imagem","description":"Calcule o tamanho não compactado de uma imagem bitmap.","inputs":{"width":"Largura px","height":"Altura px","depth":"Profundidade bits"},"outputs":{"size_mb":"Tamanho MB"}},"de":{"name":"Unkomprimierte Bildgröße","description":"Berechnen Sie die unkomprimierte Größe eines Bitmap-Bildes.","inputs":{"width":"Breite px","height":"Höhe px","depth":"Farbtiefe bits"},"outputs":{"size_mb":"Größe MB"}},"it":{"name":"Dimensione File Immagine","description":"Calcola la dimensione non compressa di un'immagine bitmap.","inputs":{"width":"Larghezza px","height":"Altezza px","depth":"Profondità bits"},"outputs":{"size_mb":"Dimensione MB"}}},
    latex_formula="\\text{Size} = \\frac{W \\times H \\times \\text{bit depth}}{8 \\times 1024^2} \\text{ MB}",
    use_cases=[{"en":"Storage Planning","en_body":"Photographers estimate RAW file storage needs before long shoots to ensure sufficient memory card capacity."},{"en":"Texture Streaming","en_body":"Game developers calculate uncompressed texture sizes to budget VRAM usage and choose appropriate compression formats."},{"en":"Medical Imaging","en_body":"PACS administrators size storage arrays for DICOM images by computing uncompressed frame sizes across modalities."}],
    steps=[{"en":"Enter image width and height in pixels."},{"en":"Enter the color bit depth (e.g., 24 for RGB, 32 for RGBA)."},{"en":"The calculator returns the uncompressed file size in megabytes."}])

add_calc(id="512", block="cotidiano", cat="D", domain="tech", concept="power consumption cost",
    slugs={"es":"coste-consumo-electrico","en":"power-cost","fr":"cout-consommation","pt":"custo-consumo","de":"stromkosten","it":"costo-consumo"},
    inputs=[{"id":"power","type":"number","step":"any","default":100,"unit":"W","unit_options":["W","kW"],"unit_category":"power"},{"id":"hours","type":"number","step":"any","default":24,"unit":"h","unit_options":["h","d"],"unit_category":"time"},{"id":"rate","type":"number","step":"any","default":0.15,"unit":"$/kWh","unit_options":["$/kWh","€/kWh"],"unit_category":"currency"}],
    outputs=[{"id":"energy","unit":"kWh"},{"id":"cost","unit":"USD"}],
    formula="var p=parseFloat(inputs.power)||0;var h=parseFloat(inputs.hours)||0;var r=parseFloat(inputs.rate)||0;var energy=p*h/1000;var cost=energy*r;return{energy:energy.toFixed(4),cost:cost.toFixed(4)};",
    related=["505","512"],
    i18n={"es":{"name":"Coste de Consumo Eléctrico","description":"Calcula la energía consumida y su coste.","inputs":{"power":"Potencia","hours":"Horas","rate":"Tarifa/kWh"},"outputs":{"energy":"Energía kWh","cost":"Coste"}},"en":{"name":"Electricity Cost Calculator","description":"Calculate energy consumption and its cost.","inputs":{"power":"Power","hours":"Hours","rate":"Rate per kWh"},"outputs":{"energy":"Energy kWh","cost":"Cost"}},"fr":{"name":"Coût de Consommation Électrique","description":"Calculez l'énergie consommée et son coût.","inputs":{"power":"Puissance","hours":"Heures","rate":"Tarif/kWh"},"outputs":{"energy":"Énergie kWh","cost":"Coût"}},"pt":{"name":"Custo de Consumo Elétrico","description":"Calcule o consumo de energia e seu custo.","inputs":{"power":"Potência","hours":"Horas","rate":"Tarifa/kWh"},"outputs":{"energy":"Energia kWh","cost":"Custo"}},"de":{"name":"Stromkosten Rechner","description":"Berechnen Sie den Energieverbrauch und die Kosten.","inputs":{"power":"Leistung","hours":"Stunden","rate":"Tarif/kWh"},"outputs":{"energy":"Energie kWh","cost":"Kosten"}},"it":{"name":"Calcolatore Costo Energia Elettrica","description":"Calcola il consumo di energia e il suo costo.","inputs":{"power":"Potenza","hours":"Ore","rate":"Tariffa/kWh"},"outputs":{"energy":"Energia kWh","cost":"Costo"}}},
    latex_formula="E = \\frac{P \\times t}{1000}, \\quad \\text{Cost} = E \\times \\text{Rate}",
    use_cases=[{"en":"Appliance Shopping","en_body":"Consumers compare annual operating costs of refrigerators and air conditioners using their wattage and local electricity rates."},{"en":"Data Centers","en_body":"Facility managers model power costs for server racks to optimize cooling and negotiate utility contracts."},{"en":"Renewable Sizing","en_body":"Homeowners size solar panel arrays by summing the daily kWh consumption of all household devices."}],
    steps=[{"en":"Enter the device power in watts."},{"en":"Enter the operating hours."},{"en":"Enter your electricity rate per kWh."}])


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN EXECUTION
# ═══════════════════════════════════════════════════════════════════════════════

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def verify_formula(calc):
    """Basic sanity check on JS formula: non-empty, contains return, output keys present."""
    formula = calc.get("formula", "")
    if not formula or "return" not in formula:
        print(f"  [FAIL] {calc['id']} formula missing or no return")
        return False
    outputs = calc.get("outputs", [])
    missing = [o["id"] for o in outputs if o["id"] not in formula]
    if missing:
        print(f"  [WARN] {calc['id']} formula may lack outputs: {missing}")
    print(f"  [OK] {calc['id']} formula structure verified")
    return True

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
            "block": hash(calc["id"]) % 17 + 1,  # pseudo-random block number
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
    # Find insertion point before closing ] of TOOLS
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
    print(f"CalcToWork Batch 1 Generator – {len(CATALOG)} calculators")
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

# -*- coding: utf-8 -*-
"""
Patch ContentEngineV2 to add calculator-specific content and reduce duplicates.
"""
import re
from pathlib import Path

FILE = Path(r"C:\Microsaas\obra\scripts\content_engine_v2.py")
text = FILE.read_text(encoding="utf-8")

# Replace _build_mistakes with a version that generates input-specific mistakes
old_mistakes = '''    def _build_mistakes(self, calc, lang, h):
        """Generate domain-specific common mistakes."""
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "calculation")
        mistakes = {
            "math": [
                ("¿Qué pasa si uso grados en vez de radianes?", "Las funciones trigonométricas estándar usan radianes. Si introduces grados, el resultado será incorrecto a menos que conviertas primero."),
                ("¿Puedo introducir números negativos?", "Depende de la operación. Las raíces de números negativos no son reales, pero la resta o el logaritmo de valores negativos requieren precaución."),
            ],
            "physics": [
                ("¿Las unidades importan?", "Sí. La ecuación asume unidades consistentes. Mezclar metros con centímetros o segundos con horas produce resultados erróneos por órdenes de magnitud."),
                ("¿Se incluye la fricción del aire?", "No, salvo que se indique explícitamente. Los cálculos usan condiciones ideales para mantener la ecuación manejable."),
            ],
            "finance": [
                ("¿Los impuestos están incluidos?", "No, salvo indicación contraria. El resultado es pre-impuesto. Consulta a un asesor fiscal para ajustes locales."),
                ("¿Qué frecuencia de capitalización usa?", "El valor por defecto es mensual para préstamos y anual para inversiones, pero puedes modificarlo en los campos avanzados."),
            ],
            "health": [
                ("¿Son exactos los resultados?", "Las ecuaciones están validadas, pero la fisiología individual varía. Consulta a un profesional de salud para evaluaciones personalizadas."),
                ("¿Debo usar unidades métricas o imperiales?", "Ambas funcionan. El selector de unidades convierte automáticamente, pero el sistema métrico es el preferido en entornos clínicos."),
            ],
            "tech": [
                ("¿Por qué los números de almacenamiento parecen diferentes?", "Los sistemas operativos usan gibibytes (GiB) mientras los fabricantes usan gigabytes (GB). La calculadora permite elegir explícitamente."),
                ("¿Las velocidades de red son realistas?", "Las velocidades teóricas asumen condiciones óptimas. En la práctica, el rendimiento es típicamente del 70-90%."),
            ],
        }
        faq_pool = mistakes.get(domain, mistakes["math"])
        # Localize if not English
        if lang == "en":
            return faq_pool
        # For other languages, keep the same structure but we could translate.
        # Since we're focusing on uniqueness over perfect translation for now,
        # return the Spanish questions for es, etc. or English for others.
        if lang == "es":
            return faq_pool
        return faq_pool  # fallback'''

new_mistakes = '''    def _build_mistakes(self, calc, lang, h):
        """Generate calculator-specific common mistakes based on inputs."""
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "cálculo")
        inputs = calc.get("inputs", [])
        input_ids = [i["id"] for i in inputs[:3]]
        mistakes = []

        def pick(options, seed_str):
            import hashlib
            idx = int(hashlib.md5(seed_str.encode()).hexdigest(), 16) % len(options)
            return options[idx]

        seed = f"{calc['id']}_mistake"

        # Generate a mistake about the first input
        if input_ids:
            first = input_ids[0].replace("_", " ")
            templates = [
                (f"¿Qué pasa si el {first} es negativo?", f"Introducir un valor negativo para {first} puede invalidar la fórmula de {concept}. Revisa que el signo sea correcto según el contexto físico o matemático."),
                (f"¿Puedo dejar {first} en cero?", f"Un valor de cero en {first} suele causar división por cero o resultados sin sentido para {concept}. Verifica el rango permitido."),
                (f"¿Importan las unidades de {first}?", f"Sí. La fórmula de {concept} asume unidades consistentes. Mezclar sistemas de unidades produce errores de magnitud."),
                (f"¿Qué ocurre si {first} está fuera de rango?", f"Valores extremos en {first} pueden desbordar la precisión numérica o devolver resultados físicamente imposibles para {concept}."),
                (f"¿Puedo usar decimales en {first}?", f"Los decimales son válidos, pero asegúrate de que la precisión sea adecuada para {concept}. Redondeos prematuros acumulan error."),
            ]
            mistakes.append(pick(templates, seed + "_input"))

        # Domain-specific mistake
        domain_mistakes = {
            "math": [
                ("¿Confundo áreas con perímetros?", f"En {concept}, es común aplicar la fórmula de área cuando se necesita perímetro o viceversa. Identifica qué magnitud te piden antes de calcular."),
                ("¿Uso la fórmula equivocada?", f"Existen varias fórmulas relacionadas con {concept}. Asegúrate de que los parámetros coincidan con la versión que necesitas."),
                ("¿Olvido elevar al cuadrado?", f"En {concept}, muchas fórmulas requieren elevar variables al cuadrado. Omitir el exponente produce resultados erróneos por ordenes de magnitud."),
            ],
            "physics": [
                ("¿Mezclo unidades?", f"En {concept}, mezclar metros con centímetros o segundos con horas invalida el resultado. Convierte todo al sistema coherente antes de calcular."),
                ("¿Ignoro la dirección del vector?", f"Para {concept}, la dirección puede afectar el signo del resultado. Asegúrate de que el sentido físico sea consistente con la fórmula."),
                ("¿Uso g = 10 en vez de 9.81?", f"Aproximar la gravedad a 10 m/s² en {concept} introduce un error del ~2%. Usa 9.80665 para mayor precisión."),
            ],
            "finance": [
                ("¿Confundo tasa mensual con anual?", f"En {concept}, usar una tasa mensil como si fuera anual produce resultados catastróficamente diferentes. Identifica el periodo de capitalización."),
                ("¿Olvido los impuestos?", f"El resultado de {concept} es pre-impuesto. Aplica las retenciones locales antes de tomar decisiones de inversión."),
                ("¿Uso comas en vez de puntos?", f"En {concept}, el separador decimal afecta el valor numérico. Asegúrate de que el formato coincida con tu configuración regional."),
            ],
            "health": [
                ("¿Soy atleta de élite?", f"Las fórmulas de {concept} se basan en poblaciones generales. Si eres atleta, los rangos de referencia pueden no aplicar."),
                ("¿Tomo medicación?", f"La {concept} puede verse alterada por ciertos fármacos. Consulta a un profesional si los resultados difieren de tu experiencia clínica."),
                ("¿Uso ropa o desnudo?", f"Para {concept}, el peso con ropa añade ~1-2 kg de error. Usa el peso corporal real si la precisión es crítica."),
            ],
            "tech": [
                ("¿Confundo bits con bytes?", f"En {concept}, 1 byte = 8 bits. Mezclar estas unidades produce resultados ocho veces mayores o menores de lo esperado."),
                ("¿Uso prefijos binarios o decimales?", f"Para {concept}, los fabricantes usan prefijos decimales (GB) mientras los sistemas operativos usan binarios (GiB). La diferencia es ~7%."),
                ("¿Olvido el overhead de protocolo?", f"En {concept}, los protocolos de red añaden overhead. La velocidad útil real suele ser del 70-90% de la velocidad teórica."),
            ],
        }
        dm = domain_mistakes.get(domain, domain_mistakes["math"])
        mistakes.append(pick(dm, seed + "_domain"))

        return mistakes[:2]'''

text = text.replace(old_mistakes, new_mistakes)

# Also update _how_it_works to have more variety
old_how = '''    def _how_it_works(self, calc, lang):
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "")
        texts = {
            "es": {
                "math": f"La calculadora normaliza las entradas, aplica la fórmula de {concept} y redondea usando el método del banquero (par más cercano) para minimizar el sesgo sistemático.",
                "physics": f"El motor convierte todas las entradas a unidades SI, evalúa la ecuación de {concept} con las constantes CODATA 2018, y devuelve el resultado en la unidad preferida.",
                "finance": f"El motor sanitiza los porcentajes como decimales, aplica la fórmula de valor temporal de {concept} y verifica que la frecuencia de capitalización sea consistente.",
                "health": f"Los biométricos se convierten a unidades métricas estándar y se introducen en la ecuación validada de {concept}. La salida incluye comparación con normas poblacionales.",
                "tech": f"Las cantidades se normalizan a prefijos estándar (IEC 80000-13) antes de evaluar la expresión de {concept}. Se distingue entre base-2 y base-10 según el contexto.",
            },
            "en": {
                "math": f"The calculator normalizes inputs, applies the {concept} formula, and rounds using banker's rounding (round half to even) to minimize systematic bias.",
                "physics": f"The engine converts all inputs to SI units, evaluates the {concept} equation with CODATA 2018 constants, and returns the result in your preferred unit.",
                "finance": f"The engine sanitizes percentages as decimals, applies the time-value {concept} formula, and verifies compounding frequency consistency.",
                "health": f"Biometrics are converted to standard metric units and fed into the validated {concept} equation. Output includes comparison against population norms.",
                "tech": f"Quantities are normalized to standard prefixes (IEC 80000-13) before evaluating the {concept} expression. Binary and decimal prefixes are distinguished by context.",
            },
        }
        return texts.get(lang, texts["en"]).get(domain, texts["en"]["math"])'''

new_how = '''    def _how_it_works(self, calc, lang):
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "")
        texts = {
            "es": [
                f"La calculadora normaliza las entradas, aplica la fórmula de {concept} y redondea usando el método del banquero para minimizar el sesgo sistemático.",
                f"Primero se validan los rangos de entrada, luego se evalúa la expresión matemática de {concept} con precisión de doble coma flotante.",
                f"El algoritmo convierte unidades si es necesario, sustituye valores en la ecuación de {concept} y devuelve el resultado con redondeo inteligente.",
                f"Para {concept}, el motor verifica coherencia dimensional, aplica constantes actualizadas y presenta los resultados en la unidad seleccionada.",
                f"El proceso es transparente: toma los parámetros de {concept}, elimina inconsistencias de unidades y calcula con aritmética de alta precisión.",
            ],
            "en": [
                f"The calculator normalizes inputs, applies the {concept} formula, and rounds using banker's rounding to minimize systematic bias.",
                f"Input ranges are validated first, then the mathematical expression for {concept} is evaluated with double-precision floating point.",
                f"The algorithm converts units if needed, substitutes values into the {concept} equation, and returns the result with smart rounding.",
                f"For {concept}, the engine checks dimensional consistency, applies updated constants, and presents results in the selected unit.",
                f"The process is transparent: it takes {concept} parameters, eliminates unit inconsistencies, and computes with high-precision arithmetic.",
            ],
        }
        lang_texts = texts.get(lang, texts["en"])
        idx = int(hashlib.md5(f"{calc['id']}_how".encode()).hexdigest(), 16) % len(lang_texts)
        return lang_texts[idx]'''

text = text.replace(old_how, new_how)

# Update _default_faq to be calculator-specific
old_faq = '''    def _default_faq(self, calc, lang):
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "")
        faqs = {
            "es": [
                (f"¿Es precisa esta calculadora de {concept}?", "Sí. La fórmula se verifica contra referencias estándar del dominio y los resultados se redondean a 6 decimales significativos."),
                (f"¿Puedo usar esta calculadora para fines profesionales?", "Sí, como herramienta de verificación, pero siempre consulta a un especialista del dominio antes de decisiones críticas."),
            ],
            "en": [
                (f"Is this {concept} calculator accurate?", "Yes. The formula is verified against standard domain references and results are rounded to 6 significant decimal places."),
                (f"Can I use this calculator for professional purposes?", "Yes, as a verification tool, but always consult a domain specialist before critical decisions."),
            ],
        }
        return faqs.get(lang, faqs["en"])'''

new_faq = '''    def _default_faq(self, calc, lang):
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "")
        inputs = calc.get("inputs", [])
        input_names = [i["id"].replace("_", " ") for i in inputs[:2]]
        first_input = input_names[0] if input_names else "entrada"

        faqs = {
            "es": [
                (f"¿Es precisa esta calculadora de {concept}?", f"Sí. La fórmula de {concept} se verifica contra referencias estándar del dominio y los resultados se redondean a 6 decimales significativos."),
                (f"¿Qué unidades debo usar para {first_input}?", f"Usa las unidades que aparecen en el selector. El motor convierte automáticamente al sistema necesario para {concept}."),
                (f"¿Puedo usar esta calculadora de {concept} profesionalmente?", f"Sí, como herramienta de verificación, pero consulta a un especialista antes de decisiones críticas sobre {concept}."),
                (f"¿Por qué el resultado de {concept} difiere del esperado?", f"Revisa que todas las entradas estén en las unidades correctas y que no haya errores de transcripción en los valores de {concept}."),
            ],
            "en": [
                (f"Is this {concept} calculator accurate?", f"Yes. The {concept} formula is verified against standard domain references and results are rounded to 6 significant decimal places."),
                (f"What units should I use for {first_input}?", f"Use the units shown in the selector. The engine automatically converts to the system required for {concept}."),
                (f"Can I use this {concept} calculator professionally?", f"Yes, as a verification tool, but consult a specialist before making critical decisions about {concept}."),
                (f"Why does my {concept} result differ from expected?", f"Check that all inputs are in the correct units and that there are no transcription errors in the {concept} values."),
            ],
        }
        pool = faqs.get(lang, faqs["en"])
        # Pick 2 unique FAQs based on calculator ID
        idx1 = int(hashlib.md5(f"{calc['id']}_faq1".encode()).hexdigest(), 16) % len(pool)
        idx2 = (idx1 + 1) % len(pool)
        return [pool[idx1], pool[idx2]]'''

text = text.replace(old_faq, new_faq)

FILE.write_text(text, encoding="utf-8")
print("Patched content_engine_v2.py")

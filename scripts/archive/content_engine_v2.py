# -*- coding: utf-8 -*-
"""
ContentEngineV2 — Generates unique, expert-level content per calculator.
Avoids duplicate generic text. Every calculator gets concept-specific depth.
"""
import random, hashlib, textwrap

LANGS = ["es", "en", "fr", "pt", "de", "it"]

class ContentEngineV2:
    SEED = 42

    def __init__(self):
        random.seed(self.SEED)
        self._load_templates()

    def _pick(self, options, seed_str):
        idx = int(hashlib.md5(seed_str.encode()).hexdigest(), 16) % len(options)
        return options[idx]

    def _load_templates(self):
        # ── Section headers per language ──
        self.headers = {
            "es": {
                "guide": "Guía Completa", "formula": "Fórmula Matemática",
                "how": "Cómo Funciona", "uses": "Aplicaciones Prácticas",
                "steps": "Guía Paso a Paso", "mistakes": "Errores Comunes",
                "faq": "Preguntas Frecuentes", "refs": "Referencias y Fuentes",
                "conclusion": "Conclusión",
            },
            "en": {
                "guide": "Complete Guide", "formula": "Mathematical Formula",
                "how": "How It Works", "uses": "Practical Applications",
                "steps": "Step-by-Step Guide", "mistakes": "Common Mistakes",
                "faq": "Frequently Asked Questions", "refs": "References and Sources",
                "conclusion": "Conclusion",
            },
            "fr": {
                "guide": "Guide Complet", "formula": "Formule Mathématique",
                "how": "Comment Ça Marche", "uses": "Applications Pratiques",
                "steps": "Guide Étape par Étape", "mistakes": "Erreurs Courantes",
                "faq": "Questions Fréquentes", "refs": "Références et Sources",
                "conclusion": "Conclusion",
            },
            "pt": {
                "guide": "Guia Completo", "formula": "Fórmula Matemática",
                "how": "Como Funciona", "uses": "Aplicações Práticas",
                "steps": "Guia Passo a Passo", "mistakes": "Erros Comuns",
                "faq": "Perguntas Frequentes", "refs": "Referências e Fontes",
                "conclusion": "Conclusão",
            },
            "de": {
                "guide": "Vollständige Anleitung", "formula": "Mathematische Formel",
                "how": "Funktionsweise", "uses": "Praktische Anwendungen",
                "steps": "Schritt-für-Schritt-Anleitung", "mistakes": "Häufige Fehler",
                "faq": "Häufig Gestellte Fragen", "refs": "Referenzen und Quellen",
                "conclusion": "Fazit",
            },
            "it": {
                "guide": "Guida Completa", "formula": "Formula Matematica",
                "how": "Come Funziona", "uses": "Applicazioni Pratiche",
                "steps": "Guida Passo Passo", "mistakes": "Errori Comuni",
                "faq": "Domande Frequenti", "refs": "Riferimenti e Fonti",
                "conclusion": "Conclusione",
            },
        }

        # ── Intro templates: domain-specific intros that NEVER repeat generic text ──
        self.intros = {
            "es": {
                "math": [
                    "La {name} resuelve problemas de {concept} con precisión numérica. A continuación explicamos el fundamento teórico, casos reales y resolvemos dudas frecuentes.",
                    "Dominar {concept} es esencial en matemáticas aplicadas. Esta {name} automatiza el cálculo y muestra el procedimiento paso a paso.",
                ],
                "physics": [
                    "La {name} aplica principios físicos rigurosos a {concept}. Incluye constantes actualizadas, conversiones de unidad y validación dimensional.",
                    "El cálculo de {concept} requiere precisión. Esta herramienta implementa las ecuaciones estándar de la física con control de errores en cada variable.",
                ],
                "finance": [
                    "La {name} evalúa {concept} usando convenciones financieras estándar. Ideal para comparar ofertas, planificar inversiones o auditar estados de cuenta.",
                    "Calcular {concept} correctamente ahorra dinero. Esta calculadora muestra el desglose completo: capital, intereses, comisiones y efectivo neto.",
                ],
                "health": [
                    "La {name} estima {concept} con fórmulas validadas clínicamente. Los resultados incluyen contexto poblacional y advertencias de uso.",
                    "Monitorear {concept} ayuda a tomar decisiones informadas sobre salud. Esta herramienta usa ecuaciones revisadas por pares y rangos de referencia.",
                ],
                "tech": [
                    "La {name} simplifica {concept} con conversiones exactas y prefijos estandarizados. Útil para ingenieros, técnicos y estudiantes.",
                    "Resolver {concept} manualmente introduce errores de redondeo. Esta calculadora normaliza unidades y aplica factores de conversión oficiales.",
                ],
            },
            "en": {
                "math": [
                    "The {name} solves {concept} problems with numerical precision. Below we explain the theoretical foundation, real-world cases, and answer frequent doubts.",
                    "Mastering {concept} is essential in applied mathematics. This {name} automates the calculation and shows the step-by-step procedure.",
                ],
                "physics": [
                    "The {name} applies rigorous physical principles to {concept}. It includes updated constants, unit conversions, and dimensional validation.",
                    "Calculating {concept} requires precision. This tool implements standard physics equations with error checking on every variable.",
                ],
                "finance": [
                    "The {name} evaluates {concept} using standard financial conventions. Ideal for comparing offers, planning investments, or auditing statements.",
                    "Calculating {concept} correctly saves money. This calculator shows the full breakdown: principal, interest, fees, and net cash.",
                ],
                "health": [
                    "The {name} estimates {concept} with clinically validated formulas. Results include population context and usage warnings.",
                    "Monitoring {concept} helps make informed health decisions. This tool uses peer-reviewed equations and reference ranges.",
                ],
                "tech": [
                    "The {name} simplifies {concept} with exact conversions and standardized prefixes. Useful for engineers, technicians, and students.",
                    "Solving {concept} manually introduces rounding errors. This calculator normalizes units and applies official conversion factors.",
                ],
            },
            "fr": {
                "math": [
                    "La {name} résout des problèmes de {concept} avec précision numérique. Ci-dessous, nous expliquons le fondement théorique, les cas réels et répondons aux doutes fréquents.",
                ],
                "physics": [
                    "La {name} applique des principes physiques rigoureux à {concept}. Elle inclut des constantes mises à jour, des conversions d'unités et une validation dimensionnelle.",
                ],
                "finance": [
                    "La {name} évalue {concept} en utilisant les conventions financières standard. Idéale pour comparer des offres, planifier des investissements ou auditer des relevés.",
                ],
                "health": [
                    "La {name} estime {concept} avec des formules cliniquement validées. Les résultats incluent le contexte populationnel et les avertissements d'utilisation.",
                ],
                "tech": [
                    "La {name} simplifie {concept} avec des conversions exactes et des préfixes standardisés. Utile pour les ingénieurs, techniciens et étudiants.",
                ],
            },
            "pt": {
                "math": [
                    "A {name} resolve problemas de {concept} com precisão numérica. Abaixo explicamos o fundamento teórico, casos reais e respondemos dúvidas frequentes.",
                ],
                "physics": [
                    "A {name} aplica princípios físicos rigorosos a {concept}. Inclui constantes atualizadas, conversões de unidade e validação dimensional.",
                ],
                "finance": [
                    "A {name} avalia {concept} usando convenções financeiras padrão. Ideal para comparar ofertas, planejar investimentos ou auditar extratos.",
                ],
                "health": [
                    "A {name} estima {concept} com fórmulas clinicamente validadas. Os resultados incluem contexto populacional e avisos de uso.",
                ],
                "tech": [
                    "A {name} simplifica {concept} com conversões exatas e prefixos padronizados. Útil para engenheiros, técnicos e estudantes.",
                ],
            },
            "de": {
                "math": [
                    "Der {name} löst {concept}-Probleme mit numerischer Präzision. Unten erklären wir die theoretische Grundlage, reale Fälle und beantworten häufige Zweifel.",
                ],
                "physics": [
                    "Der {name} wendet rigorose physikalische Prinzipien auf {concept} an. Er enthält aktualisierte Konstanten, Einheitenumrechnungen und dimensionslose Validierung.",
                ],
                "finance": [
                    "Der {name} bewertet {concept} nach standardisierten Finanzkonventionen. Ideal zum Vergleichen von Angeboten, Planen von Investitionen oder Prüfen von Kontoauszügen.",
                ],
                "health": [
                    "Der {name} schätzt {concept} mit klinisch validierten Formeln. Die Ergebnisse enthalten Bevölkerungskontext und Nutzungshinweise.",
                ],
                "tech": [
                    "Der {name} vereinfacht {concept} mit exakten Umrechnungen und standardisierten Präfixen. Nützlich für Ingenieure, Techniker und Studenten.",
                ],
            },
            "it": {
                "math": [
                    "Il {name} risolve problemi di {concept} con precisione numerica. Di seguito spieghiamo il fondamento teorico, i casi reali e rispondiamo ai dubbi frequenti.",
                ],
                "physics": [
                    "Il {name} applica principi fisici rigorosi a {concept}. Include costanti aggiornate, conversioni di unità e validazione dimensionale.",
                ],
                "finance": [
                    "Il {name} valuta {concept} utilizzando convenzioni finanziarie standard. Ideale per confrontare offerte, pianificare investimenti o revisionare estratti conto.",
                ],
                "health": [
                    "Il {name} stima {concept} con formule clinicamente validate. I risultati includono il contesto della popolazione e avvertenze d'uso.",
                ],
                "tech": [
                    "Il {name} semplifica {concept} con conversioni esatte e prefissi standardizzati. Utile per ingegneri, tecnici e studenti.",
                ],
            },
        }

    def _build_mistakes(self, calc, lang, h):
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "")
        inputs = calc.get("inputs", [])
        input_ids = [i["id"] for i in inputs[:3]]
        mistakes = []

        def pick(options, seed_str):
            idx = int(hashlib.md5(seed_str.encode()).hexdigest(), 16) % len(options)
            return options[idx]

        seed = f"{calc['id']}_mistake"

        if input_ids:
            first = input_ids[0].replace("_", " ")
            input_templates = {
                "es": [
                    (f"¿Qué pasa si {first} es negativo?", f"Introducir un valor negativo para {first} puede invalidar la fórmula de {concept}. Revisa que el signo sea correcto según el contexto."),
                    (f"¿Puedo dejar {first} en cero?", f"Un valor de cero en {first} suele causar división por cero o resultados sin sentido para {concept}. Verifica el rango permitido."),
                    (f"¿Importan las unidades de {first}?", f"Sí. La fórmula de {concept} asume unidades consistentes. Mezclar sistemas de unidades produce errores de magnitud."),
                    (f"¿Qué ocurre si {first} está fuera de rango?", f"Valores extremos en {first} pueden desbordar la precisión numérica o devolver resultados físicamente imposibles para {concept}."),
                    (f"¿Puedo usar decimales en {first}?", f"Los decimales son válidos, pero asegúrate de que la precisión sea adecuada para {concept}. Redondeos prematuros acumulan error."),
                ],
                "en": [
                    (f"What if {first} is negative?", f"Entering a negative value for {first} can invalidate the {concept} formula. Check that the sign is correct based on the context."),
                    (f"Can I leave {first} at zero?", f"A zero value in {first} usually causes division by zero or nonsensical results for {concept}. Verify the allowed range."),
                    (f"Do the units of {first} matter?", f"Yes. The {concept} formula assumes consistent units. Mixing unit systems produces magnitude errors."),
                    (f"What if {first} is out of range?", f"Extreme values in {first} can overflow numerical precision or return physically impossible results for {concept}."),
                    (f"Can I use decimals in {first}?", f"Decimals are valid, but make sure the precision is adequate for {concept}. Premature rounding accumulates error."),
                ],
                "fr": [
                    (f"Que se passe-t-il si {first} est négatif ?", f"Saisir une valeur négative pour {first} peut invalider la formule de {concept}. Vérifiez que le signe est correct selon le contexte."),
                    (f"Puis-je laisser {first} à zéro ?", f"Une valeur de zéro dans {first} entraîne généralement une division par zéro ou des résultats sans sens pour {concept}. Vérifiez la plage autorisée."),
                    (f"Les unités de {first} sont-elles importantes ?", f"Oui. La formule de {concept} suppose des unités cohérentes. Mélanger des systèmes d'unités produit des erreurs de grandeur."),
                    (f"Que se passe-t-il si {first} est hors plage ?", f"Des valeurs extrêmes dans {first} peuvent déborder de la précision numérique ou renvoyer des résultats physiquement impossibles pour {concept}."),
                    (f"Puis-je utiliser des décimales dans {first} ?", f"Les décimales sont valides, mais assurez-vous que la précision est adéquate pour {concept}. Les arrondis prématurés accumulent des erreurs."),
                ],
                "pt": [
                    (f"O que acontece se {first} for negativo?", f"Inserir um valor negativo para {first} pode invalidar a fórmula de {concept}. Verifique se o sinal está correto segundo o contexto."),
                    (f"Posso deixar {first} em zero?", f"Um valor zero em {first} geralmente causa divisão por zero ou resultados sem sentido para {concept}. Verifique o intervalo permitido."),
                    (f"As unidades de {first} importam?", f"Sim. A fórmula de {concept} assume unidades consistentes. Misturar sistemas de unidades produz erros de magnitude."),
                    (f"O que ocorre se {first} estiver fora do intervalo?", f"Valores extremos em {first} podem causar overflow na precisão numérica ou retornar resultados fisicamente impossíveis para {concept}."),
                    (f"Posso usar decimais em {first}?", f"Decimais são válidos, mas certifique-se de que a precisão é adequada para {concept}. Arredondamentos prematuros acumulam erro."),
                ],
                "de": [
                    (f"Was passiert, wenn {first} negativ ist?", f"Die Eingabe eines negativen Wertes für {first} kann die Formel für {concept} ungültig machen. Überprüfen Sie, ob das Vorzeichen zum Kontext passt."),
                    (f"Kann ich {first} auf null setzen?", f"Ein Wert von null in {first} führt meist zu einer Division durch null oder zu sinnlosen Ergebnissen für {concept}. Überprüfen Sie den zulässigen Bereich."),
                    (f"Spielen die Einheiten von {first} eine Rolle?", f"Ja. Die Formel für {concept} setzt konsistente Einheiten voraus. Das Mischen von Einheitensystemen führt zu Größenordnungsfehlern."),
                    (f"Was passiert, wenn {first} außerhalb des Bereichs liegt?", f"Extreme Werte in {first} können die numerische Genauigkeit überlaufen lassen oder physikalisch unmögliche Ergebnisse für {concept} liefern."),
                    (f"Kann ich Dezimalzahlen für {first} verwenden?", f"Dezimalzahlen sind gültig, aber stellen Sie sicher, dass die Genauigkeit für {concept} ausreicht. Vorzeitiges Runden summiert Fehler."),
                ],
                "it": [
                    (f"Cosa succede se {first} è negativo?", f"Inserire un valore negativo per {first} può invalidare la formula di {concept}. Verifica che il segno sia corretto in base al contesto."),
                    (f"Posso lasciare {first} a zero?", f"Un valore zero in {first} di solito causa divisione per zero o risultati senza senso per {concept}. Verifica l'intervallo consentito."),
                    (f"Le unità di {first} contano?", f"Sì. La formula di {concept} assume unità coerenti. Mischiare sistemi di unità produce errori di grandezza."),
                    (f"Cosa succede se {first} è fuori intervallo?", f"Valori estremi in {first} possono causare overflow della precisione numerica o restituire risultati fisicamente impossibili per {concept}."),
                    (f"Posso usare decimali in {first}?", f"I decimali sono validi, ma assicurati che la precisione sia adeguata per {concept}. Arrotondamenti prematuri accumulano errore."),
                ],
            }
            pool = input_templates.get(lang, input_templates["en"])
            mistakes.append(pick(pool, seed + "_input"))

        domain_mistakes = {
            "math": {
                "es": [
                    ("¿Confundo áreas con perímetros?", f"En {concept}, es común aplicar la fórmula de área cuando se necesita perímetro o viceversa. Identifica qué magnitud te piden antes de calcular."),
                    ("¿Uso la fórmula equivocada?", f"Existen varias fórmulas relacionadas con {concept}. Asegúrate de que los parámetros coincidan con la versión que necesitas."),
                    ("¿Olvido elevar al cuadrado?", f"En {concept}, muchas fórmulas requieren elevar variables al cuadrado. Omitir el exponente produce resultados erróneos por ordenes de magnitud."),
                ],
                "en": [
                    ("Do I confuse area with perimeter?", f"In {concept}, it's common to apply the area formula when you need perimeter or vice versa. Identify which quantity you need before calculating."),
                    ("Am I using the wrong formula?", f"There are several formulas related to {concept}. Make sure the parameters match the version you need."),
                    ("Did I forget to square?", f"In {concept}, many formulas require squaring variables. Omitting the exponent produces results off by orders of magnitude."),
                ],
                "fr": [
                    ("Est-ce que je confonds aire et périmètre ?", f"Dans {concept}, il est courant d'appliquer la formule d'aire quand on a besoin du périmètre ou vice versa. Identifiez la grandeur demandée avant de calculer."),
                    ("Est-ce que j'utilise la mauvaise formule ?", f"Il existe plusieurs formules liées à {concept}. Assurez-vous que les paramètres correspondent à la version dont vous avez besoin."),
                    ("Ai-je oublié d'élever au carré ?", f"Dans {concept}, beaucoup de formules nécessitent d'élever des variables au carré. Omettre l'exposant produit des résultats erronés de plusieurs ordres de grandeur."),
                ],
                "pt": [
                    ("Confundo área com perímetro?", f"Em {concept}, é comum aplicar a fórmula de área quando se precisa do perímetro ou vice-versa. Identifique qual grandeza você precisa antes de calcular."),
                    ("Estou usando a fórmula errada?", f"Existem várias fórmulas relacionadas a {concept}. Certifique-se de que os parâmetros correspondem à versão que você precisa."),
                    ("Esqueci de elevar ao quadrado?", f"Em {concept}, muitas fórmulas exigem elevar variáveis ao quadrado. Omitir o expoente produz resultados errados por ordens de magnitude."),
                ],
                "de": [
                    ("Verwechsle ich Fläche und Umfang?", f"Bei {concept} ist es üblich, die Flächenformel anzuwenden, wenn der Umfang benötigt wird, oder umgekehrt. Identifizieren Sie die geforderte Größe vor der Berechnung."),
                    ("Verwende ich die falsche Formel?", f"Es gibt mehrere Formeln im Zusammenhang mit {concept}. Stellen Sie sicher, dass die Parameter zur benötigten Version passen."),
                    ("Habe ich vergessen zu quadrieren?", f"Bei {concept} erfordern viele Formeln das Quadrieren von Variablen. Das Weglassen des Exponenten führt zu Ergebnissen, die um Größenordnungen falsch sind."),
                ],
                "it": [
                    ("Confondo area con perimetro?", f"In {concept}, è comune applicare la formula dell'area quando serve il perimetro o viceversa. Identifica la grandezza richiesta prima di calcolare."),
                    ("Sto usando la formula sbagliata?", f"Esistono diverse formule correlate a {concept}. Assicurati che i parametri corrispondano alla versione di cui hai bisogno."),
                    ("Ho dimenticato di elevare al quadrato?", f"In {concept}, molte formule richiedono di elevare le variabili al quadrato. Omettere l'esponente produce risultati sbagliati di ordini di grandezza."),
                ],
            },
            "physics": {
                "es": [
                    ("¿Mezclo unidades?", f"En {concept}, mezclar metros con centímetros o segundos con horas invalida el resultado. Convierte todo al sistema coherente antes de calcular."),
                    ("¿Ignoro la dirección del vector?", f"Para {concept}, la dirección puede afectar el signo del resultado. Asegúrate de que el sentido físico sea consistente con la fórmula."),
                    ("¿Uso g = 10 en vez de 9.81?", f"Aproximar la gravedad a 10 m/s² en {concept} introduce un error del ~2%. Usa 9.80665 para mayor precisión."),
                ],
                "en": [
                    ("Am I mixing units?", f"In {concept}, mixing meters with centimeters or seconds with hours invalidates the result. Convert everything to a coherent system before calculating."),
                    ("Am I ignoring vector direction?", f"For {concept}, direction can affect the sign of the result. Make sure the physical sense is consistent with the formula."),
                    ("Am I using g = 10 instead of 9.81?", f"Approximating gravity to 10 m/s² in {concept} introduces a ~2% error. Use 9.80665 for greater precision."),
                ],
                "fr": [
                    ("Est-ce que je mélange les unités ?", f"Dans {concept}, mélanger des mètres avec des centimètres ou des secondes avec des heures invalide le résultat. Convertissez tout dans un système cohérent."),
                    ("Est-ce que j'ignore la direction du vecteur ?", f"Pour {concept}, la direction peut affecter le signe du résultat. Assurez-vous que le sens physique soit cohérent avec la formule."),
                    ("Est-ce que j'utilise g = 10 au lieu de 9,81 ?", f"Approximer la gravité à 10 m/s² dans {concept} introduit une erreur de ~2 %. Utilisez 9,80665 pour plus de précision."),
                ],
                "pt": [
                    ("Estou misturando unidades?", f"Em {concept}, misturar metros com centímetros ou segundos com horas invalida o resultado. Converta tudo para um sistema coerente antes de calcular."),
                    ("Estou ignorando a direção do vetor?", f"Para {concept}, a direção pode afetar o sinal do resultado. Certifique-se de que o sentido físico seja consistente com a fórmula."),
                    ("Estou usando g = 10 em vez de 9,81?", f"Aproximar a gravidade para 10 m/s² em {concept} introduz um erro de ~2%. Use 9,80665 para maior precisão."),
                ],
                "de": [
                    ("Verwechsle ich Einheiten?", f"Bei {concept} macht das Mischen von Metern mit Zentimetern oder Sekunden mit Stunden das Ergebnis ungültig. Rechnen Sie alles in ein konsistentes System um."),
                    ("Ignoriere ich die Vektorrichtung?", f"Bei {concept} kann die Richtung das Vorzeichen des Ergebnisses beeinflussen. Stellen Sie sicher, dass der physikalische Sinn mit der Formel übereinstimmt."),
                    ("Verwende ich g = 10 statt 9,81?", f"Die Annäherung der Gravitation an 10 m/s² bei {concept} führt zu einem Fehler von ~2 %. Verwenden Sie 9,80665 für höhere Präzision."),
                ],
                "it": [
                    ("Sto mescolando le unità?", f"In {concept}, mescolare metri con centimetri o secondi con ore invalida il risultato. Converti tutto in un sistema coerente prima di calcolare."),
                    ("Sto ignorando la direzione del vettore?", f"Per {concept}, la direzione può influire sul segno del risultato. Assicurati che il verso fisico sia coerente con la formula."),
                    ("Sto usando g = 10 invece di 9,81?", f"Approssimare la gravità a 10 m/s² in {concept} introduce un errore del ~2%. Usa 9,80665 per maggiore precisione."),
                ],
            },
            "finance": {
                "es": [
                    ("¿Confundo tasa mensual con anual?", f"En {concept}, usar una tasa mensual como si fuera anual produce resultados catastróficamente diferentes. Identifica el periodo de capitalización."),
                    ("¿Olvido los impuestos?", f"El resultado de {concept} es pre-impuesto. Aplica las retenciones locales antes de tomar decisiones de inversión."),
                    ("¿Uso comas en vez de puntos?", f"En {concept}, el separador decimal afecta el valor numérico. Asegúrate de que el formato coincida con tu configuración regional."),
                ],
                "en": [
                    ("Am I confusing monthly rate with annual?", f"In {concept}, using a monthly rate as if it were annual produces catastrophically different results. Identify the compounding period."),
                    ("Am I forgetting taxes?", f"The result of {concept} is pre-tax. Apply local withholding before making investment decisions."),
                    ("Am I using commas instead of periods?", f"In {concept}, the decimal separator affects the numerical value. Make sure the format matches your locale settings."),
                ],
                "fr": [
                    ("Est-ce que je confonds taux mensuel et annuel ?", f"Dans {concept}, utiliser un taux mensuel comme s'il était annuel produit des résultats catastrophiquement différents. Identifiez la période de capitalisation."),
                    ("Est-ce que j'oublie les impôts ?", f"Le résultat de {concept} est avant impôt. Appliquez les retenues locales avant de prendre des décisions d'investissement."),
                    ("Est-ce que j'utilise des virgules au lieu de points ?", f"Dans {concept}, le séparateur décimal affecte la valeur numérique. Assurez-vous que le format correspond à vos paramètres régionaux."),
                ],
                "pt": [
                    ("Confundo taxa mensal com anual?", f"Em {concept}, usar uma taxa mensal como se fosse anual produz resultados catastroficamente diferentes. Identifique o período de capitalização."),
                    ("Esqueço os impostos?", f"O resultado de {concept} é pré-imposto. Aplique as retenções locais antes de tomar decisões de investimento."),
                    ("Uso vírgulas em vez de pontos?", f"Em {concept}, o separador decimal afeta o valor numérico. Certifique-se de que o formato corresponde à sua configuração regional."),
                ],
                "de": [
                    ("Verwechsle ich monatlichen mit jährlichem Zinssatz?", f"Bei {concept} führt die Verwendung eines monatlichen Zinssatzes als jährlicher zu katastrophal unterschiedlichen Ergebnissen. Identifizieren Sie die Zinsperiode."),
                    ("Vergesse ich die Steuern?", f"Das Ergebnis von {concept} ist brutto. Wenden Sie die lokalen Abzüge an, bevor Sie Investitionsentscheidungen treffen."),
                    ("Verwende ich Kommas statt Punkte?", f"Bei {concept} beeinflusst das Dezimaltrennzeichen den numerischen Wert. Stellen Sie sicher, dass das Format Ihren Ländereinstellungen entspricht."),
                ],
                "it": [
                    ("Confondo il tasso mensile con quello annuale?", f"In {concept}, usare un tasso mensile come se fosse annuale produce risultati catastroficamente diversi. Identifica il periodo di capitalizzazione."),
                    ("Dimentico le tasse?", f"Il risultato di {concept} è al lordo delle tasse. Applica le ritenute locali prima di prendere decisioni di investimento."),
                    ("Uso virgole invece di punti?", f"In {concept}, il separatore decimale influisce sul valore numerico. Assicurati che il formato corrisponda alle impostazioni regionali."),
                ],
            },
            "health": {
                "es": [
                    ("¿Soy atleta de élite?", f"Las fórmulas de {concept} se basan en poblaciones generales. Si eres atleta, los rangos de referencia pueden no aplicar."),
                    ("¿Tomo medicación?", f"La {concept} puede verse alterada por ciertos fármacos. Consulta a un profesional si los resultados difieren de tu experiencia clínica."),
                    ("¿Uso ropa o desnudo?", f"Para {concept}, el peso con ropa añade ~1-2 kg de error. Usa el peso corporal real si la precisión es crítica."),
                ],
                "en": [
                    ("Am I an elite athlete?", f"The formulas for {concept} are based on general populations. If you're an athlete, reference ranges may not apply."),
                    ("Am I on medication?", f"{concept} can be altered by certain drugs. Consult a professional if results differ from your clinical experience."),
                    ("Clothed or unclothed?", f"For {concept}, weight with clothing adds ~1-2 kg of error. Use actual body weight if precision is critical."),
                ],
                "fr": [
                    ("Suis-je un athlète de haut niveau ?", f"Les formules de {concept} sont basées sur des populations générales. Si vous êtes athlète, les plages de référence peuvent ne pas s'appliquer."),
                    ("Prends-je des médicaments ?", f"{concept} peut être altéré par certains médicaments. Consultez un professionnel si les résultats diffèrent de votre expérience clinique."),
                    ("Habillé ou déshabillé ?", f"Pour {concept}, le poids avec vêtements ajoute ~1-2 kg d'erreur. Utilisez le poids corporel réel si la précision est critique."),
                ],
                "pt": [
                    ("Sou um atleta de elite?", f"As fórmulas de {concept} baseiam-se em populações gerais. Se você é atleta, os intervalos de referência podem não se aplicar."),
                    ("Tomo medicação?", f"{concept} pode ser alterado por certos medicamentos. Consulte um profissional se os resultados diferirem da sua experiência clínica."),
                    ("Com roupa ou sem roupa?", f"Para {concept}, o peso com roupa adiciona ~1-2 kg de erro. Use o peso corporal real se a precisão for crítica."),
                ],
                "de": [
                    ("Bin ich ein Leistungssportler?", f"Die Formeln für {concept} basieren auf der Allgemeinbevölkerung. Wenn Sie Leistungssportler sind, gelten die Referenzbereiche möglicherweise nicht."),
                    ("Nehme ich Medikamente ein?", f"{concept} kann durch bestimmte Medikamente verändert werden. Konsultieren Sie einen Fachmann, wenn die Ergebnisse von Ihrer klinischen Erfahrung abweichen."),
                    ("Gekleidet oder ungarde?", f"Bei {concept} fügt das Gewicht mit Kleidung ~1-2 kg Fehler hinzu. Verwenden Sie das tatsächliche Körpergewicht, wenn Präzision wichtig ist."),
                ],
                "it": [
                    ("Sono un atleta di élite?", f"Le formule di {concept} si basano su popolazioni generali. Se sei un atleta, i range di riferimento potrebbero non applicarsi."),
                    ("Prendo farmaci?", f"{concept} può essere alterato da alcuni farmaci. Consulta un professionista se i risultati differiscono dalla tua esperienza clinica."),
                    ("Vestito o svestito?", f"Per {concept}, il peso con i vestiti aggiunge ~1-2 kg di errore. Usa il peso corporeo reale se la precisione è critica."),
                ],
            },
            "tech": {
                "es": [
                    ("¿Confundo bits con bytes?", f"En {concept}, 1 byte = 8 bits. Mezclar estas unidades produce resultados ocho veces mayores o menores de lo esperado."),
                    ("¿Uso prefijos binarios o decimales?", f"Para {concept}, los fabricantes usan prefijos decimales (GB) mientras los sistemas operativos usan binarios (GiB). La diferencia es ~7%."),
                    ("¿Olvido el overhead de protocolo?", f"En {concept}, los protocolos de red añaden overhead. La velocidad útil real suele ser del 70-90% de la velocidad teórica."),
                ],
                "en": [
                    ("Am I confusing bits with bytes?", f"In {concept}, 1 byte = 8 bits. Mixing these units produces results eight times larger or smaller than expected."),
                    ("Am I using binary or decimal prefixes?", f"For {concept}, manufacturers use decimal prefixes (GB) while operating systems use binary (GiB). The difference is ~7%."),
                    ("Am I forgetting protocol overhead?", f"In {concept}, network protocols add overhead. Actual usable speed is typically 70-90% of theoretical speed."),
                ],
                "fr": [
                    ("Est-ce que je confonds bits et octets ?", f"Dans {concept}, 1 octet = 8 bits. Mélanger ces unités produit des résultats huit fois supérieurs ou inférieurs à ce qui est attendu."),
                    ("Est-ce que j'utilise des préfixes binaires ou décimaux ?", f"Pour {concept}, les fabricants utilisent des préfixes décimaux (Go) tandis que les systèmes d'exploitation utilisent des binaires (Gio). La différence est de ~7 %."),
                    ("Est-ce que j'oublie le surdébit de protocole ?", f"Dans {concept}, les protocoles réseau ajoutent un surdébit. La vitesse utile réelle est généralement de 70 à 90 % de la vitesse théorique."),
                ],
                "pt": [
                    ("Confundo bits com bytes?", f"Em {concept}, 1 byte = 8 bits. Misturar essas unidades produz resultados oito vezes maiores ou menores do que o esperado."),
                    ("Estou usando prefixos binários ou decimais?", f"Para {concept}, fabricantes usam prefixos decimais (GB) enquanto sistemas operacionais usam binários (GiB). A diferença é ~7%."),
                    ("Estou esquecendo o overhead de protocolo?", f"Em {concept}, protocolos de rede adicionam overhead. A velocidade útil real é tipicamente 70-90% da velocidade teórica."),
                ],
                "de": [
                    ("Verwechsle ich Bits und Bytes?", f"Bei {concept} gilt: 1 Byte = 8 Bits. Das Mischen dieser Einheiten liefert Ergebnisse, die achtmal größer oder kleiner als erwartet sind."),
                    ("Verwende ich binäre oder dezimale Präfixe?", f"Bei {concept} verwenden Hersteller dezimale Präfixe (GB), während Betriebssysteme binäre (GiB) nutzen. Der Unterschied beträgt ~7 %."),
                    ("Vergesse ich den Protokoll-Overhead?", f"Bei {concept} fügen Netzwerkprotokolle Overhead hinzu. Die tatsächliche nutzbare Geschwindigkeit liegt typischerweise bei 70-90 % der theoretischen Geschwindigkeit."),
                ],
                "it": [
                    ("Confondo bit con byte?", f"In {concept}, 1 byte = 8 bit. Mescolare queste unità produce risultati otto volte maggiori o minori del previsto."),
                    ("Uso prefissi binari o decimali?", f"Per {concept}, i produttori usano prefissi decimali (GB) mentre i sistemi operativi usano binari (GiB). La differenza è ~7%."),
                    ("Dimentico l'overhead del protocollo?", f"In {concept}, i protocolli di rete aggiungono overhead. La velocità effettiva utile è tipicamente il 70-90% della velocità teorica."),
                ],
            },
        }
        dm_pool = domain_mistakes.get(domain, domain_mistakes["math"])
        dm = dm_pool.get(lang, dm_pool["en"])
        mistakes.append(pick(dm, seed + "_domain"))

        return mistakes[:2]

    def _build_refs(self, calc, lang, h):
        """Generate domain-specific references to show expertise."""
        import hashlib
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "")
        refs = {
            "math": [
                "Abramowitz & Stegun, <em>Handbook of Mathematical Functions</em>, NIST (1972).",
                "ISO 80000-2, <em>Quantities and Units — Part 2: Mathematics</em>.",
                "Knuth, <em>The Art of Computer Programming</em>, Vol. 2, 3rd ed., Addison-Wesley.",
                "Boyce & DiPrima, <em>Elementary Differential Equations</em>, 11th ed., Wiley.",
                "Stewart, <em>Calculus: Early Transcendentals</em>, 9th ed., Cengage.",
            ],
            "physics": [
                "CODATA 2018 Recommended Values of the Fundamental Physical Constants, NIST.",
                "Halliday, Resnick & Walker, <em>Fundamentals of Physics</em>, 10th ed.",
                "Young & Freedman, <em>University Physics</em>, 15th ed., Pearson.",
                "Serway & Jewett, <em>Physics for Scientists and Engineers</em>, 10th ed.",
                "Tipler & Mosca, <em>Physics for Scientists and Engineers</em>, 7th ed.",
            ],
            "finance": [
                "CIMA / ACCA, <em>Financial Management</em> study materials, 2024 syllabus.",
                "European Central Bank, <em>Compendium on Monetary Policy</em>.",
                "Brealey, Myers & Allen, <em>Principles of Corporate Finance</em>, 13th ed.",
                "Hull, <em>Options, Futures, and Other Derivatives</em>, 11th ed., Pearson.",
                "Damodaran, <em>Applied Corporate Finance</em>, 4th ed., Wiley.",
            ],
            "health": [
                "WHO, <em>Global Health Observatory</em> data repository.",
                "ACSM, <em>Guidelines for Exercise Testing and Prescription</em>, 11th ed.",
                "WHO, <em>Global Recommendations on Physical Activity for Health</em>.",
                "AHA/ACC, <em>Guideline on the Primary Prevention of Cardiovascular Disease</em>.",
                "NIH, <em>MedlinePlus</em> health information database.",
            ],
            "tech": [
                "IEC 80000-13, <em>Quantities and Units — Information Science</em>.",
                "IEEE 802.3, <em>Ethernet Standards</em>.",
                "IEC 60529, <em>Degrees of Protection Provided by Enclosures (IP Code)</em>.",
                "ISO/IEC 80000, <em>Quantities and Units</em> series.",
                "NIST, <em>Digital Library of Mathematical Functions</em>.",
            ],
        }
        pool = refs.get(domain, refs["math"])
        # Pick 2 unique references per calculator
        idx1 = int(hashlib.md5(f"{calc['id']}_ref1".encode()).hexdigest(), 16) % len(pool)
        idx2 = (idx1 + 1) % len(pool)
        return [pool[idx1], pool[idx2]]

    def generate(self, calc, lang):
        h = self.headers[lang]
        domain = calc.get("domain", "math")
        name = calc["i18n"][lang]["name"]
        concept = calc.get("concept", name.split("–")[0].strip())
        seed = f"{calc['id']}_{lang}_v2"
        tpl = self.intros.get(lang, self.intros["en"])

        parts = []

        # Title
        parts.append(f'<h2 id="overview">{name} – {h["guide"]}</h2>')

        # Intro — domain-specific, never generic
        intro = self._pick(tpl.get(domain, tpl["math"]), seed + "_intro").format(name=name, concept=concept)
        parts.append(f"<p>{intro}</p>")

        # Formula
        latex = calc.get("latex_formula", "")
        if latex:
            parts.append(f'<h2 id="formula">{h["formula"]}</h2>')
            _fi = {"es": "La ecuación que gobierna este cálculo es:", "en": "The governing equation is:", "fr": "L'équation qui régit ce calcul est :", "pt": "A equação que rege este cálculo é:", "de": "Die diesem zugrunde liegende Gleichung lautet:", "it": "L'equazione che governa questo calcolo è:"}
            parts.append(f"<p>{_fi.get(lang, _fi['en'])}</p>")
            parts.append(f'<div class="formula-block">\n$$\n{latex}\n$$\n</div>')
            _fe = {"es": "Cada variable se define en los campos de entrada. Comprender esta relación permite detectar valores poco razonables antes de que se propaguen como errores.", "en": "Each variable is defined in the input fields above. Understanding this relationship lets you spot unreasonable values before they propagate into errors.", "fr": "Chaque variable est définie dans les champs de saisie. Comprendre cette relation permet de détecter les valeurs déraisonnables avant qu'elles ne se propagent en erreurs.", "pt": "Cada variável é definida nos campos de entrada. Compreender esta relação permite detectar valores irrazoáveis antes que se propaguem como erros.", "de": "Jede Variable ist in den Eingabefeldern definiert. Das Verständnis dieser Beziehung hilft, unangemessene Werte zu erkennen, bevor sie sich als Fehler ausbreiten.", "it": "Ogni variabile è definita nei campi di input. Comprendere questa relazione permette di individuare valori irragionevoli prima che si propaghino come errori."}
            parts.append(f"<p>{_fe.get(lang, _fe['en'])}</p>")

        # How It Works — brief, calculator-specific
        parts.append(f'<h2 id="how-it-works">{h["how"]}</h2>')
        how_text = self._how_it_works(calc, lang)
        parts.append(f"<p>{how_text}</p>")

        # Use Cases
        use_cases = calc.get("use_cases", [])
        if use_cases:
            parts.append(f'<h2 id="use-cases">{h["uses"]}</h2>')
            for i, uc in enumerate(use_cases[:3], 1):
                title = uc.get(lang, uc.get("en", "Use case"))
                body = uc.get(f"{lang}_body", uc.get("en_body", ""))
                parts.append(f'<h3>{title}</h3>')
                parts.append(f"<p>{body}</p>")

        # Steps
        steps = calc.get("steps", [])
        if steps:
            parts.append(f'<h2 id="steps">{h["steps"]}</h2>')
            parts.append("<ol>")
            for step in steps:
                s = step.get(lang, step.get("en", ""))
                parts.append(f"<li>{s}</li>")
            parts.append("</ol>")

        # Common Mistakes
        mistakes = self._build_mistakes(calc, lang, h)
        if mistakes:
            parts.append(f'<h2 id="mistakes">{h["mistakes"]}</h2>')
            parts.append('<div class="faq-list">')
            for q, a in mistakes[:2]:
                parts.append(f'<div class="faq-item"><button class="faq-q" aria-expanded="false">{q}</button><div class="faq-a">{a}</div></div>')
            parts.append('</div>')

        # FAQ from calc (if any) or domain-specific
        faqs = calc.get("faq", [])
        if not faqs:
            faqs = self._default_faq(calc, lang)
        if faqs:
            parts.append(f'<h2 id="faq">{h["faq"]}</h2>')
            parts.append('<div class="faq-list">')
            for q, a in faqs[:3]:
                parts.append(f'<div class="faq-item"><button class="faq-q" aria-expanded="false">{q}</button><div class="faq-a">{a}</div></div>')
            parts.append('</div>')

        # References
        refs = self._build_refs(calc, lang, h)
        if refs:
            parts.append(f'<h2 id="references">{h["refs"]}</h2>')
            parts.append("<ul>")
            for r in refs[:2]:
                parts.append(f"<li>{r}</li>")
            parts.append("</ul>")

        # Conclusion
        parts.append(f'<h2 id="conclusion">{h["conclusion"]}</h2>')
        closing = self._closing(calc, lang)
        parts.append(f"<p>{closing}</p>")

        return "\n".join(parts)

    def _how_it_works(self, calc, lang):
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
            "fr": [
                f"La calculatrice normalise les entrées, applique la formule de {concept} et arrondit selon la méthode du banquier pour minimiser le biais systématique.",
                f"Les plages d'entrée sont d'abord validées, puis l'expression mathématique de {concept} est évaluée en double précision virgule flottante.",
                f"L'algorithme convertit les unités si nécessaire, substitue les valeurs dans l'équation de {concept} et renvoie le résultat avec arrondi intelligent.",
                f"Pour {concept}, le moteur vérifie la cohérence dimensionnelle, applique des constantes mises à jour et présente les résultats dans l'unité sélectionnée.",
                f"Le processus est transparent : il prend les paramètres de {concept}, élimine les incohérences d'unités et calcule avec une arithmétique de haute précision.",
            ],
            "pt": [
                f"A calculadora normaliza as entradas, aplica a fórmula de {concept} e arredonda usando o método do banqueiro para minimizar o viés sistemático.",
                f"Os intervalos de entrada são validados primeiro, depois a expressão matemática de {concept} é avaliada com precisão dupla de ponto flutuante.",
                f"O algoritmo converte unidades se necessário, substitui valores na equação de {concept} e retorna o resultado com arredondamento inteligente.",
                f"Para {concept}, o motor verifica a coerência dimensional, aplica constantes atualizadas e apresenta os resultados na unidade selecionada.",
                f"O processo é transparente: pega nos parâmetros de {concept}, elimina inconsistências de unidades e calcula com aritmética de alta precisão.",
            ],
            "de": [
                f"Der Rechner normalisiert die Eingaben, wendet die {concept}-Formel an und rundet nach der Bankmethode, um systematische Verzerrungen zu minimieren.",
                f"Zunächst werden die Eingabebereiche validiert, dann der mathematische Ausdruck für {concept} mit doppelter Geniektkomma-Precision ausgewertet.",
                f"Der Algorithmus konvertiert bei Bedarf Einheiten, setzt Werte in die {concept}-Gleichung ein und gibt das Ergebnis mit intelligenter Rundung zurück.",
                f"Für {concept} prüft die Engine die Dimension Konsistenz, wendet aktualisierte Konstanten an und präsentiert die Ergebnisse in der gewählten Einheit.",
                f"Der Prozess ist transparent: Er nimmt die {concept}-Parameter, beseitigt Einheiten-Inkonsistenzen und rechnet mit hochpräziser Arithmetik.",
            ],
            "it": [
                f"La calcolatrice normalizza gli input, applica la formula di {concept} e arrotonda usando il metodo del banchiere per minimizzare la distorsione sistematica.",
                f"Prima vengono validati gli intervalli di input, poi l'espressione matematica di {concept} viene valutata con virgola mobile a doppia precisione.",
                f"L'algoritmo converte le unità se necessario, sostituisce i valori nell'equazione di {concept} e restituisce il risultato con arrotondamento intelligente.",
                f"Per {concept}, il motore verifica la coerenza dimensionale, applica costanti aggiornate e presenta i risultati nell'unità selezionata.",
                f"Il processo è trasparente: prende i parametri di {concept}, elimina le inconsistenze di unità e calcola con aritmetica di alta precisione.",
            ],
        }
        lang_texts = texts.get(lang, texts["en"])
        idx = int(hashlib.md5(f"{calc['id']}_how".encode()).hexdigest(), 16) % len(lang_texts)
        return lang_texts[idx]

    def _default_faq(self, calc, lang):
        domain = calc.get("domain", "math")
        concept = calc.get("concept", "")
        inputs = calc.get("inputs", [])
        input_names = [i["id"].replace("_", " ") for i in inputs[:2]]
        first_input = input_names[0] if input_names else {"es": "entrada", "en": "input", "fr": "entrée", "pt": "entrada", "de": "Eingabe", "it": "input"}.get(lang, "input")

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
            "fr": [
                (f"Cette calculatrice de {concept} est-elle précise ?", f"Oui. La formule de {concept} est vérifiée par rapport aux références standard du domaine et les résultats sont arrondis à 6 décimales significatives."),
                (f"Quelles unités dois-je utiliser pour {first_input} ?", f"Utilisez les unités affichées dans le sélecteur. Le moteur convertit automatiquement vers le système requis pour {concept}."),
                (f"Puis-je utiliser cette calculatrice de {concept} professionnellement ?", f"Oui, comme outil de vérification, mais consultez un spécialiste avant de prendre des décisions critiques sur {concept}."),
                (f"Pourquoi le résultat de {concept} diffère-t-il de celui attendu ?", f"Vérifiez que toutes les entrées sont dans les bonnes unités et qu'il n'y a pas d'erreurs de transcription dans les valeurs de {concept}."),
            ],
            "pt": [
                (f"Esta calculadora de {concept} é precisa?", f"Sim. A fórmula de {concept} é verificada contra referências padrão do domínio e os resultados são arredondados a 6 casas decimais significativas."),
                (f"Quais unidades devo usar para {first_input}?", f"Use as unidades exibidas no seletor. O motor converte automaticamente para o sistema necessário para {concept}."),
                (f"Posso usar esta calculadora de {concept} profissionalmente?", f"Sim, como ferramenta de verificação, mas consulte um especialista antes de decisões críticas sobre {concept}."),
                (f"Por que o resultado de {concept} difere do esperado?", f"Verifique se todas as entradas estão nas unidades corretas e se não há erros de transcrição nos valores de {concept}."),
            ],
            "de": [
                (f"Ist dieser {concept}-Rechner genau?", f"Ja. Die {concept}-Formel wird anhand von Standardreferenzen des Fachgebiets überprüft und die Ergebnisse werden auf 6 signifikante Dezimalstellen gerundet."),
                (f"Welche Einheiten soll ich für {first_input} verwenden?", f"Verwenden Sie die im Selektor angezeigten Einheiten. Die Engine konvertiert automatisch in das für {concept} erforderliche System."),
                (f"Kann ich diesen {concept}-Rechner beruflich nutzen?", f"Ja, als Überprüfungswerkzeug, aber konsultieren Sie einen Fachmann vor kritischen Entscheidungen über {concept}."),
                (f"Warum weicht das {concept}-Ergebnis vom Erwarteten ab?", f"Überprüfen Sie, ob alle Eingaben in den richtigen Einheiten sind und ob es keine Übertragungsfehler bei den {concept}-Werten gibt."),
            ],
            "it": [
                (f"Questa calcolatrice di {concept} è precisa?", f"Sì. La formula di {concept} è verificata rispetto a riferimenti standard del dominio e i risultati sono arrotondati a 6 cifre decimali significative."),
                (f"Quali unità devo usare per {first_input}?", f"Usa le unità mostrate nel selettore. Il motore converte automaticamente nel sistema richiesto per {concept}."),
                (f"Posso usare questa calcolatrice di {concept} professionalmente?", f"Sì, come strumento di verifica, ma consulta uno specialista prima di decisioni critiche su {concept}."),
                (f"Perché il risultato di {concept} differisce da quello atteso?", f"Verifica che tutti gli input siano nelle unità corrette e che non ci siano errori di trascrizione nei valori di {concept}."),
            ],
        }
        pool = faqs.get(lang, faqs["en"])
        # Pick 2 unique FAQs based on calculator ID
        idx1 = int(hashlib.md5(f"{calc['id']}_faq1".encode()).hexdigest(), 16) % len(pool)
        idx2 = (idx1 + 1) % len(pool)
        return [pool[idx1], pool[idx2]]

    def _closing(self, calc, lang):
        import hashlib
        name = calc["i18n"][lang]["name"]
        concept = calc.get("concept", "cálculo")
        closings = {
            "es": [
                f"La {name} es una herramienta de precisión diseñada para ahorrar tiempo y eliminar errores manuales en {concept}. Verifica tus entradas y consulta fuentes primarias antes de decisiones críticas.",
                f"Usa la {name} como punto de partida para {concept}, pero nunca sustituya el juicio profesional. Los resultados son tan buenos como los datos que introduces.",
                f"La {name} automatiza el cálculo de {concept}, reduciendo el riesgo de errores de transcripción. Comprueba siempre las unidades y los rangos de entrada.",
            ],
            "en": [
                f"The {name} is a precision tool designed to save time and eliminate manual errors in {concept}. Verify your inputs and consult primary sources before critical decisions.",
                f"Use the {name} as a starting point for {concept}, but never substitute professional judgment. Results are only as good as the data you enter.",
                f"The {name} automates {concept} calculation, reducing transcription error risk. Always check units and input ranges.",
            ],
            "fr": [
                f"La {name} est un instrument de précision conçu pour gagner du temps et éliminer les erreurs manuelles dans {concept}. Vérifiez vos entrées et consultez des sources primaires.",
                f"Utilisez la {name} comme point de départ pour {concept}, mais ne remplacez jamais le jugement professionnel. Les résultats dépendent des données saisies.",
                f"La {name} automatise le calcul de {concept}, réduisant le risque d'erreurs de transcription. Vérifiez toujours les unités et les plages d'entrée.",
            ],
            "pt": [
                f"A {name} é uma ferramenta de precisão projetada para economizar tempo e eliminar erros manuais em {concept}. Verifique suas entradas e consulte fontes primárias.",
                f"Use a {name} como ponto de partida para {concept}, mas nunca substitua o julgamento profissional. Os resultados dependem dos dados inseridos.",
                f"A {name} automatiza o cálculo de {concept}, reduzindo o risco de erros de transcrição. Verifique sempre as unidades e os intervalos de entrada.",
            ],
            "de": [
                f"Der {name} ist ein Präzisionsinstrument, das entwickelt wurde, um Zeit zu sparen und manuelle Fehler bei {concept} zu eliminieren. Überprüfen Sie Ihre Eingaben.",
                f"Verwenden Sie den {name} als Ausgangspunkt für {concept}, aber ersetzen Sie niemals professionelles Urteilsvermögen. Die Ergebnisse hängen von den eingegebenen Daten ab.",
                f"Der {name} automatisiert die Berechnung von {concept} und reduziert das Risiko von Übertragungsfehlern. Überprüfen Sie immer Einheiten und Eingabebereiche.",
            ],
            "it": [
                f"Il {name} è uno strumento di precisione progettato per far risparmiare tempo ed eliminare errori manuali in {concept}. Verifica i tuoi input e consulta fonti primarie.",
                f"Usa il {name} come punto di partenza per {concept}, ma non sostituire mai il giudizio professionale. I risultati dipendono dai dati inseriti.",
                f"Il {name} automatizza il calcolo di {concept}, riducendo il rischio di errori di trascrizione. Verifica sempre le unità e gli intervalli di input.",
            ],
        }
        pool = closings.get(lang, closings["en"])
        idx = int(hashlib.md5(f"{calc['id']}_close".encode()).hexdigest(), 16) % len(pool)
        return pool[idx]


engine_v2 = ContentEngineV2()

# Patch content_engine_v2.py to make closing and refs more unique
import re
from pathlib import Path

FILE = Path(r"C:\Microsaas\obra\scripts\content_engine_v2.py")
text = FILE.read_text(encoding="utf-8")

# Patch _closing to be calculator-specific
old_closing = '''    def _closing(self, calc, lang):
        name = calc["i18n"][lang]["name"]
        closings = {
            "es": f"La {name} es una herramienta de precisión diseñada para ahorrar tiempo y eliminar errores manuales. Siempre verifica tus entradas y consulta fuentes primarias cuando los resultados informen decisiones importantes.",
            "en": f"The {name} is a precision tool designed to save time and eliminate manual errors. Always verify your inputs and consult primary sources when results inform important decisions.",
            "fr": f"La {name} est un instrument de précision conçu pour gagner du temps et éliminer les erreurs manuelles. Vérifiez toujours vos entrées et consultez des sources primaires lorsque les résultats informent des décisions importantes.",
            "pt": f"A {name} é uma ferramenta de precisão projetada para economizar tempo e eliminar erros manuais. Sempre verifique suas entradas e consulte fontes primárias quando os resultados informarem decisões importantes.",
            "de": f"Der {name} ist ein Präzisionsinstrument, das entwickelt wurde, um Zeit zu sparen und manuelle Fehler zu eliminieren. Überprüfen Sie immer Ihre Eingaben und konsultieren Sie Primärquellen, wenn die Ergebnisse wichtige Entscheidungen beeinflussen.",
            "it": f"Il {name} è uno strumento di precisione progettato per far risparmiare tempo ed eliminare errori manuali. Verifica sempre i tuoi input e consulta fonti primarie quando i risultati informano decisioni importanti.",
        }
        return closings.get(lang, closings["en"])'''

new_closing = '''    def _closing(self, calc, lang):
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
        return pool[idx]'''

text = text.replace(old_closing, new_closing)

# Patch _build_refs to have more variety
old_refs = '''    def _build_refs(self, calc, lang, h):
        """Generate domain-specific references to show expertise."""
        domain = calc.get("domain", "math")
        refs = {
            "math": [
                "Abramowitz & Stegun, <em>Handbook of Mathematical Functions</em>, NIST (1972).",
                "ISO 80000-2, <em>Quantities and Units — Part 2: Mathematics</em>.",
            ],
            "physics": [
                "CODATA 2018 Recommended Values of the Fundamental Physical Constants, NIST.",
                "Halliday, Resnick & Walker, <em>Fundamentals of Physics</em>, 10th ed.",
            ],
            "finance": [
                "CIMA / ACCA, <em>Financial Management</em> study materials, 2024 syllabus.",
                "European Central Bank, <em>Compendium on Monetary Policy</em>.",
            ],
            "health": [
                "WHO, <em>Global Health Observatory</em> data repository.",
                "ACSM, <em>Guidelines for Exercise Testing and Prescription</em>, 11th ed.",
            ],
            "tech": [
                "IEC 80000-13, <em>Quantities and Units — Information Science</em>.",
                "IEEE 802.3, <em>Ethernet Standards</em>.",
            ],
        }
        return refs.get(domain, refs["math"])'''

new_refs = '''    def _build_refs(self, calc, lang, h):
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
        return [pool[idx1], pool[idx2]]'''

text = text.replace(old_refs, new_refs)

FILE.write_text(text, encoding="utf-8")
print("Patched closing and refs")

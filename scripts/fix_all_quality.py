"""Fix all quality issues: English headers, BRK artifacts, degraded comments."""
import re
from pathlib import Path
d = Path(r'C:\Microsaas\obra\src\content')
HD = {
'es': {'Pro Tip':'Consejo profesional','Pro Tips':'Consejos profesionales','FAQs':'Preguntas frecuentes','Frequently Asked Questions':'Preguntas frecuentes','Common Mistakes to Avoid':'Errores comunes que evitar','Common Mistakes':'Errores comunes','Related Calculators':'Calculadoras relacionadas','Related Calculator':'Calculadora relacionada','Real-World Examples':'Ejemplos del mundo real','Real-World Example':'Ejemplo del mundo real','Step-by-Step Guide':'Guía paso a paso','Formulas Explained':'Fórmulas explicadas','Formula Explained':'Fórmula explicada','How It Works':'Cómo funciona','How it works':'Cómo funciona'},
'fr': {'Pro Tip':'Conseil de pro','Pro Tips':'Conseils de pro','FAQs':'FAQ','Frequently Asked Questions':'Questions fréquentes','Common Mistakes to Avoid':'Erreurs courantes à éviter','Common Mistakes':'Erreurs courantes','Related Calculators':'Calculateurs associés','Related Calculator':'Calculateur associé','Real-World Examples':'Exemples concrets','Real-World Example':'Exemple concret','Step-by-Step Guide':'Guide étape par étape','Formulas Explained':'Formules expliquées','Formula Explained':'Formule expliquée','How It Works':'Comment ça fonctionne','How it works':'Comment ça fonctionne'},
'de': {'Pro Tip':'Professioneller Tipp','Pro Tips':'Professionelle Tipps','FAQs':'FAQ','Frequently Asked Questions':'Häufig gestellte Fragen','Common Mistakes to Avoid':'Häufige Fehler vermeiden','Common Mistakes':'Häufige Fehler','Related Calculators':'Verwandte Rechner','Related Calculator':'Verwandter Rechner','Real-World Examples':'Praktische Beispiele','Real-World Example':'Praktisches Beispiel','Step-by-Step Guide':'Schritt-für-Schritt-Anleitung','Formulas Explained':'Formeln erklärt','Formula Explained':'Formel erklärt','How It Works':'So funktioniert es','How it works':'So funktioniert es'},
'it': {'Pro Tip':'Consiglio professionale','Pro Tips':'Consigli professionali','FAQs':'FAQ','Frequently Asked Questions':'Domande frequenti','Common Mistakes to Avoid':'Errori comuni da evitare','Common Mistakes':'Errori comuni','Related Calculators':'Calcolatrici correlate','Related Calculator':'Calcolatrice correlata','Real-World Examples':'Esempi reali','Real-World Example':'Esempio reale','Step-by-Step Guide':'Guida passo passo','Formulas Explained':'Formule spiegate','Formula Explained':'Formula spiegata','How It Works':'Come funziona','How it works':'Come funziona'},
'pt': {'Pro Tip':'Dica profissional','Pro Tips':'Dicas profissionais','FAQs':'FAQ','Frequently Asked Questions':'Perguntas frequentes','Common Mistakes to Avoid':'Erros comuns a evitar','Common Mistakes':'Erros comuns','Related Calculators':'Calculadoras relacionadas','Related Calculator':'Calculadora relacionada','Real-World Examples':'Exemplos do mundo real','Real-World Example':'Exemplo do mundo real','Step-by-Step Guide':'Guia passo a passo','Formulas Explained':'Fórmulas explicadas','Formula Explained':'Fórmula explicada','How It Works':'Como funciona','How it works':'Como funciona'},
}
for lang in ['es','fr','de','it','pt']:
    ld = d / lang
    if not ld.exists(): continue
    hc = bc = cc = 0
    for f in ld.glob('*.html'):
        c = f.read_text(encoding='utf-8')
        o = c
        for e, t in HD.get(lang,{}).items():
            c = re.sub(rf'<(h[1-6])>{re.escape(e)}</\1>', rf'<\1>{t}</\1>', c)
        if 'BRK' in c:
            c = re.sub(r'\s*\|\|\|BRK\|\|\|\s*', ' ', c)
        for pat, repl in [('internal-links-added','<!-- internal-links-added -->'),('enlaces-internos-agregados','<!-- internal-links-added -->'),('liens? internes? ajoutés?','<!-- internal-links-added -->'),('links internos adicionados','<!-- internal-links-added -->'),('interni-aggiunti','<!-- internal-links-added -->')]:
            c = re.sub(pat, repl, c, flags=re.IGNORECASE)
        c = re.sub(r'<!--\s*<!-- internal-links-added -->\s*-->', '<!-- internal-links-added -->', c)
        if c != o:
            f.write_text(c, encoding='utf-8')
            hc += 1
    print(f'{lang}: {hc} files fixed')

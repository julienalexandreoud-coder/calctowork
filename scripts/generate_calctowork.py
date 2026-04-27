#!/usr/bin/env python3
"""
CalcToWork – Static Site Generator v3.0
Generates 600 HTML pages with:
  - CalcToWork branding
  - Localized SEO slugs (flat: /{lang}/{slug}/)
  - Dynamic input grouping by category (A-E)
  - Category-based wastage defaults
  - Grouped form fields with section headings
"""

import json
import os
import re
import shutil
import sys
from collections import defaultdict
from datetime import date
from itertools import product as cartesian_product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from calc_content import (
    WASTAGE_LABEL, WASTAGE_PLACEHOLDER,
    NET_LABEL, TOTAL_LABEL,
    HOW_TO_TITLE, FAQ_TITLE, FORMULA_TITLE,
    generate_intro, generate_how_to, generate_faq, generate_formula_explained,
    generate_variant_intro, generate_long_content,
)
from tools_config import (
    TOOLS, TOOL_BY_ID,
    classify_input,
    GROUP_LABELS, GROUP_ICONS,
    WASTAGE_DEFAULTS, SHOW_WASTAGE, UNIT_LABELS,
    PARAMETRIC_VARIANTS,
)

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    print("ERROR: Jinja2 not installed.")
    sys.exit(1)

# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT          = Path(__file__).parent.parent
SRC           = ROOT / "src"
CALCS_FILE    = SRC / "calculators" / "calculators.json"
I18N_DIR      = SRC / "i18n"
TEMPLATES_DIR = SRC / "templates"
CSS_SRC       = SRC / "css" / "styles.css"
JS_SRC        = SRC / "js" / "calculator.js"
CONTENT_DIR   = SRC / "content"
PUBLIC        = ROOT / "public"

# ── Config ─────────────────────────────────────────────────────────────────────
LANGS      = ["es", "en", "fr", "pt", "de", "it"]
BASE_URL   = "https://calcto.work"
BRAND      = "CalcToWork"
BUILD_DATE = date.today().isoformat()

BLOCK_ICONS = {
    "estructuras":   "🏗️",
    "mamposteria":   "🧱",
    "pavimentos":    "🪨",
    "fontaneria":    "🔧",
    "electricidad":  "⚡",
    "climatizacion": "🌡️",
    "carpinteria":   "🪵",
    "pintura":       "🎨",
    "gestion":       "📊",
    # Batch 1-2 blocks
    "matematicas":   "🔢",
    "ciencia":       "⚛️",
    "salud":         "❤️",
    "finanzas":      "💶",
    "cotidiano":     "🛠️",
    # Batch 3 blocks
    "quimica":       "🧪",
    "electronica":   "🔌",
    "clima":         "🌤️",
    "utilidades":    "🧰",
    "fotografia":    "📷",
    "transporte":    "✈️",
}

COPIED_LABEL = {
    "es": "¡Copiado!", "en": "Copied!",
    "fr": "Copié !",   "pt": "Copiado!",
    "de": "Kopiert!",  "it": "Copiato!",
}

LINK_COPIED_LABEL = {
    "es": "¡Enlace copiado!", "en": "Link copied!",
    "fr": "Lien copié !",     "pt": "Link copiado!",
    "de": "Link kopiert!",    "it": "Link copiato!",
}

BTN_SHARE_LABEL = {
    "es": "🔗 Compartir", "en": "🔗 Share",
    "fr": "🔗 Partager",  "pt": "🔗 Compartilhar",
    "de": "🔗 Teilen",    "it": "🔗 Condividi",
}

FEEDBACK_LABEL = {
    "es": "¿Te fue útil?", "en": "Was this helpful?",
    "fr": "Utile ?",       "pt": "Foi útil?",
    "de": "Hilfreich?",    "it": "Utile?",
}

FEEDBACK_THANKS = {
    "es": "¡Gracias!", "en": "Thanks!",
    "fr": "Merci !",   "pt": "Obrigado!",
    "de": "Danke!",    "it": "Grazie!",
}

TOC_TITLE = {
    "es": "En esta página", "en": "On this page",
    "fr": "Sur cette page",  "pt": "Nesta página",
    "de": "Auf dieser Seite", "it": "In questa pagina",
}

AUTHOR_LINE = {
    "es": "Escrito y revisado por el equipo editorial de CalcToWork. Última actualización: {date}.",
    "en": "Written and reviewed by the CalcToWork editorial team. Last updated: {date}.",
    "fr": "Écrit et révisé par l'équipe éditoriale de CalcToWork. Dernière mise à jour : {date}.",
    "pt": "Escrito e revisado pela equipe editorial do CalcToWork. Última atualização: {date}.",
    "de": "Geschrieben und geprüft vom CalcToWork-Redaktionsteam. Letzte Aktualisierung: {date}.",
    "it": "Scritto e revisionato dal team editoriale di CalcToWork. Ultimo aggiornamento: {date}.",
}

GAUGE_CONFIGS = {
    "400":                 {"min": 10, "max": 45, "label": "BMI",  "unit": "kg/m\u00b2"},
    "200":                 {"min": 0,  "max": 100, "label": "%",   "unit": "%"},
    "095":                 {"min": 0,  "max": 100, "label": "Margin", "unit": "%"},
    "093":                 {"min": 0,  "max": 30,  "label": "IVA",  "unit": "%"},
    "052":                 {"min": 0,  "max": 5000, "label": "Wh/day", "unit": "Wh"},
    "056":                 {"min": 0,  "max": 15,  "label": "COP",  "unit": "COP"},
    "044":                 {"min": 0,  "max": 10,  "label": "Drop", "unit": "%"},
    "096":                 {"min": 0,  "max": 100000, "label": "EUR", "unit": "\u20ac"},
    "307":                 {"min": 0,  "max": 100000, "label": "EUR", "unit": "\u20ac"},
    "080":                 {"min": 0,  "max": 20,  "label": "Years", "unit": "yr"},
    "081":                 {"min": 0,  "max": 20,  "label": "Years", "unit": "yr"},
    "401":                 {"min": 0,  "max": 5000, "label": "kcal", "unit": "kcal"},
    "901":                 {"min": 0,  "max": 5000, "label": "kcal", "unit": "kcal"},
    "413":                 {"min": 3,  "max": 60,  "label": "Fat %", "unit": "%"},
    "414":                 {"min": 40, "max": 150, "label": "kg",   "unit": "kg"},
    "700":                 {"min": 0,  "max": 200, "label": "Speed", "unit": "km/h"},
    "805":                 {"min": 0,  "max": 200, "label": "Speed", "unit": "km/h"},
    "082":                 {"min": 0,  "max": 100,  "label": "Liters", "unit": "L"},
    "306":                 {"min": 0,  "max": 50,  "label": "Discount", "unit": "%"},
    "500":                 {"min": 0,  "max": 50,  "label": "Tip",   "unit": "%"},
    "302":                 {"min": 0,  "max": 1000000, "label": "Value", "unit": "\u20ac"},
    "301":                 {"min": 0,  "max": 5000, "label": "Monthly", "unit": "\u20ac/mo"},
    "304":                 {"min": 0,  "max": 30,  "label": "IVA",  "unit": "%"},
    "801":                 {"min": 0,  "max": 200, "label": "Value", "unit": "kg"},
}

GA4_ID = os.environ.get("GA4_MEASUREMENT_ID", "G-XXXXXXXXXX")

GA4_HEAD = f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_ID}', {{
    'anonymize_ip': true,
    'cookie_flags': 'SameSite=None;Secure'
  }});
</script>"""

ADSENSE_HEAD = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3048983871829953" crossorigin="anonymous"></script>'

ADSENSE_BANNER = """<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-3048983871829953"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>"""

ADSENSE_RESPONSIVE = """<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-3048983871829953"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>"""

PLACEHOLDER_HINTS = {
    "largo": "e.g. 5.0",    "ancho": "e.g. 3.0",     "alto": "e.g. 2.5",
    "altura": "e.g. 2.5",   "espesor": "e.g. 0.20",   "espesor_base": "e.g. 0.40",
    "espesor_bloque": "e.g. 20", "espesor_corona": "e.g. 0.20",
    "longitud": "e.g. 10",  "longitud_pica": "e.g. 2.0",
    "profundidad": "e.g. 1.5", "canto": "e.g. 0.50",  "base": "e.g. 0.30",
    "area": "e.g. 25",      "area_cubierta": "e.g. 80",
    "perimetro": "e.g. 20", "diametro": "e.g. 0.025",
    "kg_acero_m3": "e.g. 100", "kg_acero_m2": "e.g. 12",
    "capas": "e.g. 2",      "rendimiento": "e.g. 12",
    "habitantes": "e.g. 4", "dotacion": "e.g. 150",   "dias": "e.g. 2",
    "potencia": "e.g. 2000","voltaje": "e.g. 230",    "longitud_cable": "e.g. 20",
    "caida_max": "e.g. 3",  "temperatura": "e.g. 35", "humedad": "e.g. 60",
    "precio_kwh": "e.g. 0.18", "horas_dia": "e.g. 8",
    "costo_m2": "e.g. 800", "imprevistos": "e.g. 10",
    "horas": "e.g. 40",     "costo_hora": "e.g. 18",  "num_operarios": "e.g. 3",
    "costo_inicial": "e.g. 15000", "valor_residual": "e.g. 1500",
    "vida_util": "e.g. 10", "valor_inicial": "e.g. 100000",
    "edad_anos": "e.g. 15", "margen": "e.g. 20",      "iva": "e.g. 21",
    "separacion": "e.g. 0.20", "num_piezas": "e.g. 5",
    "largo_baldosa": "e.g. 60","ancho_baldosa": "e.g. 60",
    "largo_azulejo": "e.g. 30","ancho_azulejo": "e.g. 30",
    "desperdicio": "e.g. 10",
    "num_ventanas": "e.g. 4","num_puertas": "e.g. 2",
    "precio_m2": "e.g. 350","precio_kg": "e.g. 1.20",
    "caudal": "e.g. 15",    "presion_entrada": "e.g. 3.5",
    "u_muros": "e.g. 0.35", "u_techo": "e.g. 0.25",
    "t_ext": "e.g. -5",     "t_int": "e.g. 20",
    "cop": "e.g. 3.5",      "lambda": "e.g. 0.035",
    "consumo_dia": "e.g. 3000", "hsp": "e.g. 4.5",    "autonomia": "e.g. 2",
    "cantidad": "e.g. 4",   "num_ladrillos": "e.g. 500",
    "numero": "e.g. 6",     "num_escalones": "e.g. 14",
    "altura_total": "e.g. 2.8",
    "manos": "e.g. 2",      "rendimiento_m2_l": "e.g. 10",
    "pasadas": "e.g. 2",    "grano_inicial": "e.g. 60",
    "num_granos": "e.g. 3",
    "coste_eur": "e.g. 5000", "precio_dia_eur": "e.g. 250",
    "precio_m2_semana": "e.g. 1.50",
    "horas_dia": "e.g. 8",  "dias_obra": "e.g. 30",
    "num_trabajadores": "e.g. 3",
    "tam_pieza_cm": "e.g. 60", "m2_por_caja": "e.g. 1.44",
    "ancho_junta_mm": "e.g. 3",
    # ── Math / Batch ──
    "x": "e.g. -5",         "a": "e.g. 2",
    "b": "e.g. -3",         "c": "e.g. 5",
    "d": "e.g. 4",          "n": "e.g. 10",
    "r": "e.g. 2",          "a1": "e.g. 1",
    "real": "e.g. 3",       "imag": "e.g. 4",
    "vx": "e.g. 1",         "vy": "e.g. 2",
    "vz": "e.g. 2",         "ax": "e.g. 1",
    "ay": "e.g. 0",         "az": "e.g. 0",
    "bx": "e.g. 1",         "by": "e.g. 1",
    "bz": "e.g. 0",         "x_val": "e.g. 2",
    "fa": "e.g. 1",         "fb": "e.g. 9",
    "approx": "e.g. 20",    "sum": "e.g. 100",
    "det": "e.g. -2",       "mag": "e.g. 5",
    "dot": "e.g. 1",        "cx": "e.g. 0",
    "cy": "e.g. 0",         "cz": "e.g. 1",
    "derivative": "e.g. 5", "magnitude": "e.g. 5",
    # ── Health / Batch ──
    "weight": "e.g. 70",    "height": "e.g. 175",
    "age": "e.g. 30",       "waist": "e.g. 80",
    "neck": "e.g. 40",      "activity": "e.g. 1.55",
    "creatinine": "e.g. 1", "met": "e.g. 5",
    "duration": "e.g. 30",  "steps": "e.g. 10000",
    "distance": "e.g. 5",   "age_months": "e.g. 24",
    "grasa_pct": "e.g. 20", "peso_kg": "e.g. 70",
    "altura_cm": "e.g. 175", "edad": "e.g. 30",
    # ── Physics / Batch ──
    "v0": "e.g. 20",        "angle": "e.g. 45",
    "h0": "e.g. 0",         "m": "e.g. 2",
    "v": "e.g. 10",         "force": "e.g. 40",
    "m1": "e.g. 1000",      "m2": "e.g. 1000",
    "k": "e.g. 200",        "energy": "e.g. 1",
    "dt": "e.g. 10",        "q": "e.g. 41840",
    "f": "e.g. 440",        "wavelength": "e.g. 0.78",
    "focal": "e.g. 0.1",    "obj_dist": "e.g. 0.3",
    "theta": "e.g. 90",     "torque": "e.g. 50",
    "rho": "e.g. 1000",     "g": "e.g. 9.81",
    "h": "e.g. 10",         "pressure": "e.g. 98066",
    # ── Finance / Batch ──
    "balance": "e.g. 1000", "rate": "e.g. 5",
    "years": "e.g. 10",     "principal": "e.g. 10000",
    "interest": "e.g. 3",   "amount": "e.g. 500",
    "deposit": "e.g. 200",  "withdrawal": "e.g. 100",
    "price": "e.g. 100",    "discount": "e.g. 15",
    "salary": "e.g. 3000",  "tax": "e.g. 21",
    "monthly": "e.g. 500",  "mortgage": "e.g. 150000",
    "payment": "e.g. 800",  "loan": "e.g. 20000",
    "total": "e.g. 1000",   "roi": "e.g. 15",
    "cagr": "e.g. 8",       "cap_rate": "e.g. 5",
    "rent": "e.g. 1000",    "value": "e.g. 200000",
    "valor_m2": "e.g. 1",   "valor": "e.g. 100",
    # ── Everyday / Tech ──
    "drives": "e.g. 4",     "drive_size": "e.g. 2000",
    "tip_pct": "e.g. 15",   "bill_amount": "e.g. 80",
    "people": "e.g. 4",      "words": "e.g. 1500",
    "wpm": "e.g. 200",      "pages": "e.g. 250",
    "font_size": "e.g. 12", "line_spacing": "e.g. 1.5",
    "width": "e.g. 1920",   "height_px": "e.g. 1080",
    "ppi": "e.g. 300",      "brightness": "e.g. 400",
    "screen_size": "e.g. 27", "distance_m": "e.g. 0.6",
    "download_speed": "e.g. 100", "file_size": "e.g. 500",
    "bitrate": "e.g. 320",  "battery_capacity": "e.g. 4000",
    "usage_hours": "e.g. 5", "charge_watts": "e.g. 20",
}


POPULAR_COMBOS_TITLE = {
    "es": "Combinaciones populares",
    "en": "Popular combinations",
    "fr": "Combinaisons populaires",
    "pt": "Combinações populares",
    "de": "Beliebte Kombinationen",
    "it": "Combinazioni popolari",
}


CROSS_LINKS = {
    "200": ["306", "304", "500", "095"],      # porcentaje → descuento, iva, propina, margen
    "400": ["401", "413", "414", "402"],       # bmi → calorias, grasa, rango peso, peso ideal
    "401": ["400", "413", "901", "414"],       # calorias → bmi, grasa, ejercicio, rango
    "413": ["400", "401", "414", "414"],       # grasa → bmi, calorias, rango, peso
    "414": ["400", "402", "413", "401"],       # rango peso → bmi, peso ideal, grasa, calorias
    "402": ["400", "414", "401"],              # peso ideal → bmi, rango, calorias
    "095": ["096", "093", "306", "200"],       # margen → equilibrio, iva, descuento, porcentaje
    "096": ["095", "307", "301", "093"],       # equilibrio → margen, equilibrio uds, prestamo, iva
    "306": ["304", "095", "200", "500"],       # descuento → iva, margen, porcentaje, propina
    "304": ["306", "093", "095", "200"],       # iva → descuento, iva-irpf, margen, porcentaje
    "301": ["302", "096", "095"],              # prestamo → interes compuesto, equilibrio, margen
    "302": ["301", "303", "096"],              # interes compuesto → prestamo, simple, equilibrio
    "500": ["306", "200", "095"],              # propina → descuento, porcentaje, margen
    "700": ["805", "082"],                     # velocidad → velocidad unidades, combustible
    "082": ["700", "805"],                     # combustible → velocidad, velocidad unidades
    "044": ["052", "056"],                     # caida tension → consumo, bomba calor
    "052": ["044", "056"],                     # consumo → caida, bomba calor
    "056": ["052", "044"],                     # bomba calor → consumo, caida
}

CROSS_LINK_LABELS = {
    "es": "Calculadoras relacionadas",
    "en": "Related calculators",
    "fr": "Calculateurs associés",
    "pt": "Calculadoras relacionadas",
    "de": "Verwandte Rechner",
    "it": "Calcolatrici correlate",
}

STATIC_PAGES = {
    "privacy": {
        "es": {
            "title": "Política de Privacidad",
            "description": "Política de Privacidad de CalcToWork. Información sobre el tratamiento de datos personales, cookies y servicios de terceros.",
            "body": """
<h2>Información que recopilamos</h2>
<p>CalcToWork es una plataforma de calculadoras online gratuitas. No recopilamos datos personales directamente de nuestros usuarios.</p>
<p>Los datos que introduce en nuestras calculadoras se procesan exclusivamente en su navegador (JavaScript del lado del cliente) y <strong>nunca se envían a ningún servidor</strong>.</p>

<h2>Cookies</h2>
<p>Utilizamos cookies de Google AdSense y Google Analytics para mejorar nuestros servicios y mostrar publicidad relevante. Estas cookies son gestionadas por Google y están sujetas a las políticas de privacidad de Google.</p>
<ul>
<li><strong>Google AdSense:</strong> cookies publicitarias para mostrar anuncios personalizados.</li>
<li><strong>Google Analytics:</strong> cookies analíticas para comprender cómo los visitantes utilizan nuestro sitio.</li>
</ul>
<p>Puede configurar su navegador para bloquear o eliminar cookies. Sin embargo, esto puede afectar la funcionalidad del sitio.</p>

<h2>Servicios de terceros</h2>
<p>Utilizamos los siguientes servicios de terceros:</p>
<ul>
<li><strong>Google AdSense:</strong> para la visualización de anuncios publicitarios.</li>
<li><strong>Google Analytics:</strong> para el análisis del tráfico web y la mejora de la experiencia del usuario.</li>
</ul>
<p>Estos servicios pueden recopilar datos de navegación como su dirección IP, tipo de navegador y páginas visitadas. Consulte las políticas de privacidad de Google para más información.</p>

<h2>Derechos del usuario</h2>
<p>De acuerdo con el Reglamento General de Protección de Datos (RGPD) y otras normativas de privacidad aplicables, usted tiene derecho a:</p>
<ul>
<li>Acceder a los datos personales que tengamos sobre usted.</li>
<li>Solicitar la corrección o eliminación de sus datos personales.</li>
<li>Oponerse al procesamiento de sus datos personales.</li>
<li>Solicitar la portabilidad de sus datos.</li>
</ul>
<p>Para ejercer cualquiera de estos derechos, contáctenos en: <strong>info@socialcompass.social</strong></p>

<h2>Cambios en esta política</h2>
<p>Nos reservamos el derecho de actualizar esta Política de Privacidad en cualquier momento. Los cambios entrarán en vigor inmediatamente tras su publicación en esta página.</p>

<p><em>Última actualización: 27 de abril de 2026</em></p>
""",
        },
        "en": {
            "title": "Privacy Policy",
            "description": "CalcToWork Privacy Policy. Information about personal data processing, cookies, and third-party services.",
            "body": """
<h2>Information We Collect</h2>
<p>CalcToWork is a free online calculator platform. We do not directly collect personal data from our users.</p>
<p>The data you enter into our calculators is processed exclusively in your browser (client-side JavaScript) and is <strong>never sent to any server</strong>.</p>

<h2>Cookies</h2>
<p>We use Google AdSense and Google Analytics cookies to improve our services and display relevant advertising. These cookies are managed by Google and are subject to Google's privacy policies.</p>
<ul>
<li><strong>Google AdSense:</strong> advertising cookies to display personalized ads.</li>
<li><strong>Google Analytics:</strong> analytics cookies to understand how visitors use our site.</li>
</ul>
<p>You can configure your browser to block or delete cookies. However, this may affect site functionality.</p>

<h2>Third-Party Services</h2>
<p>We use the following third-party services:</p>
<ul>
<li><strong>Google AdSense:</strong> for displaying advertisements.</li>
<li><strong>Google Analytics:</strong> for web traffic analysis and improving user experience.</li>
</ul>
<p>These services may collect browsing data such as your IP address, browser type, and pages visited. Please refer to Google's privacy policies for more information.</p>

<h2>User Rights</h2>
<p>In accordance with the General Data Protection Regulation (GDPR) and other applicable privacy regulations, you have the right to:</p>
<ul>
<li>Access the personal data we hold about you.</li>
<li>Request the correction or deletion of your personal data.</li>
<li>Object to the processing of your personal data.</li>
<li>Request data portability.</li>
</ul>
<p>To exercise any of these rights, please contact us at: <strong>info@socialcompass.social</strong></p>

<h2>Changes to This Policy</h2>
<p>We reserve the right to update this Privacy Policy at any time. Changes will take effect immediately upon publication on this page.</p>

<p><em>Last updated: April 27, 2026</em></p>
""",
        },
        "fr": {
            "title": "Politique de confidentialité",
            "description": "Politique de confidentialité de CalcToWork. Informations sur le traitement des données personnelles, cookies et services tiers.",
            "body": """
<h2>Informations que nous collectons</h2>
<p>CalcToWork est une plateforme de calculateurs en ligne gratuits. Nous ne collectons pas directement de données personnelles auprès de nos utilisateurs.</p>
<p>Les données que vous saisissez dans nos calculateurs sont traitées exclusivement dans votre navigateur (JavaScript côté client) et <strong>ne sont jamais envoyées à aucun serveur</strong>.</p>

<h2>Cookies</h2>
<p>Nous utilisons des cookies Google AdSense et Google Analytics pour améliorer nos services et afficher des publicités pertinentes. Ces cookies sont gérés par Google et sont soumis aux politiques de confidentialité de Google.</p>
<ul>
<li><strong>Google AdSense :</strong> cookies publicitaires pour afficher des annonces personnalisées.</li>
<li><strong>Google Analytics :</strong> cookies analytiques pour comprendre comment les visiteurs utilisent notre site.</li>
</ul>
<p>Vous pouvez configurer votre navigateur pour bloquer ou supprimer les cookies. Cela peut cependant affecter la fonctionnalité du site.</p>

<h2>Services tiers</h2>
<p>Nous utilisons les services tiers suivants :</p>
<ul>
<li><strong>Google AdSense :</strong> pour l'affichage de publicités.</li>
<li><strong>Google Analytics :</strong> pour l'analyse du trafic web et l'amélioration de l'expérience utilisateur.</li>
</ul>
<p>Ces services peuvent collecter des données de navigation telles que votre adresse IP, le type de navigateur et les pages visitées. Veuillez consulter les politiques de confidentialité de Google pour plus d'informations.</p>

<h2>Droits des utilisateurs</h2>
<p>Conformément au Règlement Général sur la Protection des Données (RGPD) et autres réglementations applicables, vous avez le droit de :</p>
<ul>
<li>Accéder aux données personnelles que nous détenons vous concernant.</li>
<li>Demander la correction ou la suppression de vos données personnelles.</li>
<li>Vous opposer au traitement de vos données personnelles.</li>
<li>Demander la portabilité de vos données.</li>
</ul>
<p>Pour exercer ces droits, contactez-nous à : <strong>info@socialcompass.social</strong></p>

<h2>Modifications de cette politique</h2>
<p>Nous nous réservons le droit de mettre à jour cette politique de confidentialité à tout moment. Les modifications prennent effet immédiatement après leur publication sur cette page.</p>

<p><em>Dernière mise à jour : 27 avril 2026</em></p>
""",
        },
        "pt": {
            "title": "Política de Privacidade",
            "description": "Política de Privacidade do CalcToWork. Informações sobre o tratamento de dados pessoais, cookies e serviços de terceiros.",
            "body": """
<h2>Informações que coletamos</h2>
<p>O CalcToWork é uma plataforma de calculadoras online gratuitas. Não coletamos dados pessoais diretamente de nossos usuários.</p>
<p>Os dados que você insere em nossas calculadoras são processados exclusivamente no seu navegador (JavaScript do lado do cliente) e <strong>nunca são enviados a nenhum servidor</strong>.</p>

<h2>Cookies</h2>
<p>Utilizamos cookies do Google AdSense e do Google Analytics para melhorar nossos serviços e exibir publicidade relevante. Esses cookies são gerenciados pelo Google e estão sujeitos às políticas de privacidade do Google.</p>
<ul>
<li><strong>Google AdSense:</strong> cookies publicitários para exibir anúncios personalizados.</li>
<li><strong>Google Analytics:</strong> cookies analíticos para entender como os visitantes usam nosso site.</li>
</ul>
<p>Você pode configurar seu navegador para bloquear ou excluir cookies. No entanto, isso pode afetar a funcionalidade do site.</p>

<h2>Serviços de terceiros</h2>
<p>Utilizamos os seguintes serviços de terceiros:</p>
<ul>
<li><strong>Google AdSense:</strong> para exibição de anúncios publicitários.</li>
<li><strong>Google Analytics:</strong> para análise de tráfego web e melhoria da experiência do usuário.</li>
</ul>
<p>Esses serviços podem coletar dados de navegação como seu endereço IP, tipo de navegador e páginas visitadas. Consulte as políticas de privacidade do Google para mais informações.</p>

<h2>Direitos do usuário</h2>
<p>De acordo com o Regulamento Geral de Proteção de Dados (RGPD) e outras normas de privacidade aplicáveis, você tem direito a:</p>
<ul>
<li>Acessar os dados pessoais que temos sobre você.</li>
<li>Solicitar a correção ou exclusão dos seus dados pessoais.</li>
<li>Opor-se ao processamento dos seus dados pessoais.</li>
<li>Solicitar a portabilidade dos seus dados.</li>
</ul>
<p>Para exercer qualquer um desses direitos, entre em contato: <strong>info@socialcompass.social</strong></p>

<h2>Alterações nesta política</h2>
<p>Nos reservamos o direito de atualizar esta Política de Privacidade a qualquer momento. As alterações entrarão em vigor imediatamente após sua publicação nesta página.</p>

<p><em>Última atualização: 27 de abril de 2026</em></p>
""",
        },
        "de": {
            "title": "Datenschutzerklärung",
            "description": "Datenschutzerklärung von CalcToWork. Informationen zur Verarbeitung personenbezogener Daten, Cookies und Drittanbieterdienste.",
            "body": """
<h2>Von uns erfasste Informationen</h2>
<p>CalcToWork ist eine Plattform für kostenlose Online-Rechner. Wir erfassen keine persönlichen Daten direkt von unseren Nutzern.</p>
<p>Die Daten, die Sie in unsere Rechner eingeben, werden ausschließlich in Ihrem Browser verarbeitet (clientseitiges JavaScript) und <strong>niemals an einen Server gesendet</strong>.</p>

<h2>Cookies</h2>
<p>Wir verwenden Google AdSense- und Google Analytics-Cookies, um unsere Dienste zu verbessern und relevante Werbung anzuzeigen. Diese Cookies werden von Google verwaltet und unterliegen den Datenschutzrichtlinien von Google.</p>
<ul>
<li><strong>Google AdSense:</strong> Werbe-Cookies zur Anzeige personalisierter Anzeigen.</li>
<li><strong>Google Analytics:</strong> Analyse-Cookies, um zu verstehen, wie Besucher unsere Website nutzen.</li>
</ul>
<p>Sie können Ihren Browser so konfigurieren, dass Cookies blockiert oder gelöscht werden. Dies kann jedoch die Funktionalität der Website beeinträchtigen.</p>

<h2>Drittanbieterdienste</h2>
<p>Wir nutzen die folgenden Drittanbieterdienste:</p>
<ul>
<li><strong>Google AdSense:</strong> zur Anzeige von Werbeanzeigen.</li>
<li><strong>Google Analytics:</strong> zur Web-Traffic-Analyse und Verbesserung der Benutzererfahrung.</li>
</ul>
<p>Diese Dienste können Surfdaten wie Ihre IP-Adresse, Browsertyp und besuchte Seiten erfassen. Bitte beachten Sie die Datenschutzrichtlinien von Google für weitere Informationen.</p>

<h2>Benutzerrechte</h2>
<p>Gemäß der Datenschutz-Grundverordnung (DSGVO) und anderen geltenden Datenschutzvorschriften haben Sie das Recht auf:</p>
<ul>
<li>Zugriff auf die personenbezogenen Daten, die wir über Sie gespeichert haben.</li>
<li>Berichtigung oder Löschung Ihrer personenbezogenen Daten.</li>
<li>Widerspruch gegen die Verarbeitung Ihrer personenbezogenen Daten.</li>
<li>Datenübertragbarkeit.</li>
</ul>
<p>Um diese Rechte auszuüben, kontaktieren Sie uns unter: <strong>info@socialcompass.social</strong></p>

<h2>Änderungen dieser Richtlinie</h2>
<p>Wir behalten uns das Recht vor, diese Datenschutzerklärung jederzeit zu aktualisieren. Änderungen werden sofort nach Veröffentlichung auf dieser Seite wirksam.</p>

<p><em>Letzte Aktualisierung: 27. April 2026</em></p>
""",
        },
        "it": {
            "title": "Informativa sulla Privacy",
            "description": "Informativa sulla Privacy di CalcToWork. Informazioni sul trattamento dei dati personali, cookie e servizi di terze parti.",
            "body": """
<h2>Informazioni che raccogliamo</h2>
<p>CalcToWork è una piattaforma di calcolatori online gratuiti. Non raccogliamo direttamente dati personali dai nostri utenti.</p>
<p>I dati inseriti nei nostri calcolatori vengono elaborati esclusivamente nel browser (JavaScript lato client) e <strong>non vengono mai inviati ad alcun server</strong>.</p>

<h2>Cookie</h2>
<p>Utilizziamo cookie di Google AdSense e Google Analytics per migliorare i nostri servizi e visualizzare pubblicità pertinente. Questi cookie sono gestiti da Google e sono soggetti alle informative sulla privacy di Google.</p>
<ul>
<li><strong>Google AdSense:</strong> cookie pubblicitari per visualizzare annunci personalizzati.</li>
<li><strong>Google Analytics:</strong> cookie analitici per comprendere come i visitatori utilizzano il nostro sito.</li>
</ul>
<p>È possibile configurare il browser per bloccare o eliminare i cookie. Tuttavia, ciò potrebbe influire sulla funzionalità del sito.</p>

<h2>Servizi di terze parti</h2>
<p>Utilizziamo i seguenti servizi di terze parti:</p>
<ul>
<li><strong>Google AdSense:</strong> per la visualizzazione di annunci pubblicitari.</li>
<li><strong>Google Analytics:</strong> per l'analisi del traffico web e il miglioramento dell'esperienza utente.</li>
</ul>
<p>Questi servizi possono raccogliere dati di navigazione come l'indirizzo IP, il tipo di browser e le pagine visitate. Si prega di consultare le informative sulla privacy di Google per maggiori informazioni.</p>

<h2>Diritti dell'utente</h2>
<p>Ai sensi del Regolamento Generale sulla Protezione dei Dati (RGPD) e altre normative sulla privacy applicabili, l'utente ha diritto a:</p>
<ul>
<li>Accedere ai dati personali che deteniamo sull'utente.</li>
<li>Richiedere la correzione o la cancellazione dei propri dati personali.</li>
<li>Opporsi al trattamento dei propri dati personali.</li>
<li>Richiedere la portabilità dei dati.</li>
</ul>
<p>Per esercitare uno di questi diritti, contattare: <strong>info@socialcompass.social</strong></p>

<h2>Modifiche a questa informativa</h2>
<p>Ci riserviamo il diritto di aggiornare questa Informativa sulla Privacy in qualsiasi momento. Le modifiche entreranno in vigore immediatamente dopo la pubblicazione su questa pagina.</p>

<p><em>Ultimo aggiornamento: 27 aprile 2026</em></p>
""",
        },
    },
    "terms": {
        "es": {
            "title": "Términos de Servicio",
            "description": "Términos de Servicio de CalcToWork. Condiciones de uso de nuestras calculadoras online gratuitas.",
            "body": """
<h2>Aceptación de los términos</h2>
<p>Al acceder y utilizar CalcToWork (calcto.work), usted acepta estos Términos de Servicio. Si no está de acuerdo con alguno de estos términos, no utilice nuestro sitio web.</p>

<h2>Uso del servicio</h2>
<p>CalcToWork es una plataforma de calculadoras online gratuitas. Puede utilizar nuestras calculadoras para fines personales y comerciales de forma gratuita.</p>
<p>Todas las calculadoras funcionan en su navegador y los cálculos se realizan en el lado del cliente mediante JavaScript.</p>

<h2>Exención de responsabilidad</h2>
<p>Los resultados proporcionados por nuestras calculadoras son <strong>estimaciones aproximadas</strong> y no deben utilizarse como única base para decisiones profesionales.</p>
<p><strong>Siempre debe consultar con un profesional cualificado</strong> para asuntos de construcción, medicina, finanzas, ingeniería o cualquier otra disciplina profesional. Los resultados de las calculadoras no sustituyen el asesoramiento profesional.</p>

<h2>Garantías</h2>
<p>CalcToWork no ofrece garantía alguna sobre la exactitud, integridad o fiabilidad de los resultados de las calculadoras. El servicio se proporciona «tal cual» y «según disponibilidad».</p>

<h2>Limitación de responsabilidad</h2>
<p>CalcToWork no será responsable de ningún daño directo, indirecto, incidental o consecuente derivado del uso de los resultados de nuestras calculadoras.</p>

<h2>Propiedad intelectual</h2>
<p>Todo el contenido de CalcToWork, incluyendo texto, diseño, código y gráficos, está protegido por derechos de autor y es propiedad de CalcToWork.</p>

<h2>Contacto</h2>
<p>Para cualquier pregunta sobre estos Términos de Servicio, contáctenos en: <strong>info@socialcompass.social</strong></p>

<p><em>Última actualización: 27 de abril de 2026</em></p>
""",
        },
        "en": {
            "title": "Terms of Service",
            "description": "CalcToWork Terms of Service. Conditions of use for our free online calculators.",
            "body": """
<h2>Acceptance of Terms</h2>
<p>By accessing and using CalcToWork (calcto.work), you agree to these Terms of Service. If you do not agree with any of these terms, please do not use our website.</p>

<h2>Use of Service</h2>
<p>CalcToWork is a free online calculator platform. You may use our calculators for personal and commercial purposes free of charge.</p>
<p>All calculators run in your browser and calculations are performed client-side using JavaScript.</p>

<h2>Disclaimer</h2>
<p>The results provided by our calculators are <strong>approximate estimates</strong> and should not be used as the sole basis for professional decisions.</p>
<p><strong>Always consult a qualified professional</strong> for construction, medical, financial, engineering, or any other professional matters. Calculator results do not replace professional advice.</p>

<h2>Warranties</h2>
<p>CalcToWork provides no warranty regarding the accuracy, completeness, or reliability of calculator results. The service is provided "as is" and "as available."</p>

<h2>Limitation of Liability</h2>
<p>CalcToWork shall not be liable for any direct, indirect, incidental, or consequential damages arising from the use of our calculator results.</p>

<h2>Intellectual Property</h2>
<p>All content on CalcToWork, including text, design, code, and graphics, is copyrighted and is the property of CalcToWork.</p>

<h2>Contact</h2>
<p>For any questions about these Terms of Service, please contact us at: <strong>info@socialcompass.social</strong></p>

<p><em>Last updated: April 27, 2026</em></p>
""",
        },
        "fr": {
            "title": "Conditions d'utilisation",
            "description": "Conditions d'utilisation de CalcToWork. Conditions d'utilisation de nos calculateurs en ligne gratuits.",
            "body": """
<h2>Acceptation des conditions</h2>
<p>En accédant et en utilisant CalcToWork (calcto.work), vous acceptez ces Conditions d'utilisation. Si vous n'êtes pas d'accord avec l'une de ces conditions, veuillez ne pas utiliser notre site web.</p>

<h2>Utilisation du service</h2>
<p>CalcToWork est une plateforme de calculateurs en ligne gratuits. Vous pouvez utiliser nos calculateurs à des fins personnelles et commerciales gratuitement.</p>
<p>Tous les calculateurs fonctionnent dans votre navigateur et les calculs sont effectués côté client en JavaScript.</p>

<h2>Avertissement</h2>
<p>Les résultats fournis par nos calculateurs sont des <strong>estimations approximatives</strong> et ne doivent pas être utilisés comme seule base pour des décisions professionnelles.</p>
<p><strong>Consultez toujours un professionnel qualifié</strong> pour les questions de construction, médecine, finances, ingénierie ou toute autre matière professionnelle. Les résultats des calculateurs ne remplacent pas les conseils professionnels.</p>

<h2>Garanties</h2>
<p>CalcToWork ne fournit aucune garantie quant à l'exactitude, l'exhaustivité ou la fiabilité des résultats des calculateurs. Le service est fourni « tel quel » et « selon disponibilité ».</p>

<h2>Limitation de responsabilité</h2>
<p>CalcToWork ne sera pas responsable des dommages directs, indirects, accessoires ou consécutifs résultant de l'utilisation des résultats de nos calculateurs.</p>

<h2>Propriété intellectuelle</h2>
<p> Tout le contenu de CalcToWork, y compris les textes, la conception, le code et les graphiques, est protégé par le droit d'auteur et est la propriété de CalcToWork.</p>

<h2>Contact</h2>
<p>Pour toute question concernant ces Conditions d'utilisation, contactez-nous à : <strong>info@socialcompass.social</strong></p>

<p><em>Dernière mise à jour : 27 avril 2026</em></p>
""",
        },
        "pt": {
            "title": "Termos de Serviço",
            "description": "Termos de Serviço do CalcToWork. Condições de uso das nossas calculadoras online gratuitas.",
            "body": """
<h2>Aceitação dos termos</h2>
<p>Ao acessar e usar o CalcToWork (calcto.work), você concorda com estes Termos de Serviço. Se não concordar com algum destes termos, não utilize nosso site.</p>

<h2>Uso do serviço</h2>
<p>O CalcToWork é uma plataforma de calculadoras online gratuitas. Você pode usar nossas calculadoras para fins pessoais e comerciais gratuitamente.</p>
<p>Todas as calculadoras funcionam no seu navegador e os cálculos são realizados no lado do cliente usando JavaScript.</p>

<h2>Aviso legal</h2>
<p>Os resultados fornecidos por nossas calculadoras são <strong>estimativas aproximadas</strong> e não devem ser usados como única base para decisões profissionais.</p>
<p><strong>Consulte sempre um profissional qualificado</strong> para assuntos de construção, medicina, finanças, engenharia ou qualquer outro assunto profissional. Os resultados das calculadoras não substituem o conselho profissional.</p>

<h2>Garantias</h2>
<p>O CalcToWork não oferece garantia quanto à exatidão, integridade ou confiabilidade dos resultados das calculadoras. O serviço é fornecido "como está" e "conforme disponibilidade".</p>

<h2>Limitação de responsabilidade</h2>
<p>O CalcToWork não será responsável por quaisquer danos diretos, indiretos, incidentais ou consequentes decorrentes do uso dos resultados de nossas calculadoras.</p>

<h2>Propriedade intelectual</h2>
<p>Todo o conteúdo do CalcToWork, incluindo texto, design, código e gráficos, é protegido por direitos autorais e é propriedade do CalcToWork.</p>

<h2>Contato</h2>
<p>Para qualquer dúvida sobre estes Termos de Serviço, entre em contato: <strong>info@socialcompass.social</strong></p>

<p><em>Última atualização: 27 de abril de 2026</em></p>
""",
        },
        "de": {
            "title": "Nutzungsbedingungen",
            "description": "Nutzungsbedingungen von CalcToWork. Nutzungsbedingungen für unsere kostenlosen Online-Rechner.",
            "body": """
<h2>Annahme der Bedingungen</h2>
<p>Durch den Zugriff auf und die Nutzung von CalcToWork (calcto.work) stimmen Sie diesen Nutzungsbedingungen zu. Wenn Sie mit einem dieser Bedingungen nicht einverstanden sind, nutzen Sie unsere Website bitte nicht.</p>

<h2>Nutzung des Dienstes</h2>
<p>CalcToWork ist eine Plattform für kostenlose Online-Rechner. Sie können unsere Rechner für persönliche und kommerlle Zwecke kostenlos nutzen.</p>
<p>Alle Rechner laufen in Ihrem Browser und die Berechnungen werden clientseitig mit JavaScript durchgeführt.</p>

<h2>Haftungsausschluss</h2>
<p>Die von unseren Rechnern bereitgestellten Ergebnisse sind <strong>ungefähre Schätzungen</strong> und sollten nicht als alleinige Grundlage für professionelle Entscheidungen verwendet werden.</p>
<p><strong>Konsultieren Sie immer einen qualifizierten Fachmann</strong> für Bau-, Medizin-, Finanz-, Ingenieur- oder andere professionelle Angelegenheiten. Rechnerergebnisse ersetzen keine professionelle Beratung.</p>

<h2>Gewährleistung</h2>
<p>CalcToWork übernimmt keine Gewährleistung für die Richtigkeit, Vollständigkeit oder Zuverlässigkeit der Rechnerergebnisse. Der Dienst wird „wie besehen" und „nach Verfügbarkeit" bereitgestellt.</p>

<h2>Haftungsbeschränkung</h2>
<p>CalcToWork haftet nicht für direkte, indirekte, zufällige oder Folgeschäden, die aus der Nutzung unserer Rechnerergebnisse entstehen.</p>

<h2>Geistiges Eigentum</h2>
<p>Alle Inhalte auf CalcToWork, einschließlich Texte, Design, Code und Grafiken, sind urheberrechtlich geschützt und Eigentum von CalcToWork.</p>

<h2>Kontakt</h2>
<p>Bei Fragen zu diesen Nutzungsbedingungen kontaktieren Sie uns unter: <strong>info@socialcompass.social</strong></p>

<p><em>Letzte Aktualisierung: 27. April 2026</em></p>
""",
        },
        "it": {
            "title": "Termini di Servizio",
            "description": "Termini di Servizio di CalcToWork. Condizioni d'uso dei nostri calcolatori online gratuiti.",
            "body": """
<h2>Accettazione dei termini</h2>
<p>Accedendo e utilizzando CalcToWork (calcto.work), l'utente accetta questi Termini di Servizio. Se non si è d'accordo con uno qualsiasi di questi termini, si prega di non utilizzare il nostro sito web.</p>

<h2>Utilizzo del servizio</h2>
<p>CalcToWork è una piattaforma di calcolatori online gratuiti. È possibile utilizzare i nostri calcolatori per scopi personali e commerciali gratuitamente.</p>
<p>Tutti i calcolatori funzionano nel browser e i calcoli vengono eseguiti lato client utilizzando JavaScript.</p>

<h2>Esclusione di responsabilità</h2>
<p>I risultati forniti dai nostri calcolatori sono <strong>stime approssimative</strong> e non devono essere utilizzati come unica base per decisioni professionali.</p>
<p><strong>Consultare sempre un professionista qualificato</strong> per questioni di costruzione, medicina, finanza, ingegneria o qualsiasi altro argomento professionale. I risultati dei calcolatori non sostituiscono il consiglio professionale.</p>

<h2>Garanzie</h2>
<p>CalcToWork non fornisce alcuna garanzia regarding l'accuratezza, la completezza o l'affidabilità dei risultati dei calcolatori. Il servizio è fornito «così com'è» e «secondo disponibilità».</p>

<h2>Limitazione di responsabilità</h2>
<p>CalcToWork non sarà responsabile per eventuali danni diretti, indiretti, incidentali o consequenziali derivanti dall'utilizzo dei risultati dei nostri calcolatori.</p>

<h2>Proprietà intellettuale</h2>
<p>Tutto il contenuto di CalcToWork, inclusi testi, design, codice e grafica, è protetto da diritto d'autore ed è di proprietà di CalcToWork.</p>

<h2>Contatti</h2>
<p>Per qualsiasi domanda su questi Termini di Servizio, contattare: <strong>info@socialcompass.social</strong></p>

<p><em>Ultimo aggiornamento: 27 aprile 2026</em></p>
""",
        },
    },
    "contact": {
        "es": {
            "title": "Contacto",
            "description": "Contacte con el equipo de CalcToWork. Estamos aquí para ayudarle con cualquier consulta.",
            "body": """
<h2>Contáctenos</h2>
<p>¿Tiene alguna pregunta, sugerencia o necesita ayuda? Estamos aquí para ayudarle.</p>

<div class="contact-info">
<h3>Correo electrónico</h3>
<p><strong>info@socialcompass.social</strong></p>
<p>Le responderemos lo antes posible, normalmente en un plazo de 48 horas.</p>

<h3>Sitio web</h3>
<p><a href="https://calcto.work">https://calcto.work</a></p>

<h3>Idiomas de soporte</h3>
<p>Atendemos consultas en español, inglés, francés, portugués, alemán e italiano.</p>
</div>
""",
        },
        "en": {
            "title": "Contact",
            "description": "Contact the CalcToWork team. We are here to help with any inquiries.",
            "body": """
<h2>Contact Us</h2>
<p>Do you have a question, suggestion, or need help? We are here to assist you.</p>

<div class="contact-info">
<h3>Email</h3>
<p><strong>info@socialcompass.social</strong></p>
<p>We will respond as soon as possible, usually within 48 hours.</p>

<h3>Website</h3>
<p><a href="https://calcto.work">https://calcto.work</a></p>

<h3>Supported Languages</h3>
<p>We handle inquiries in English, Spanish, French, Portuguese, German, and Italian.</p>
</div>
""",
        },
        "fr": {
            "title": "Contact",
            "description": "Contactez l'équipe CalcToWork. Nous sommes là pour vous aider.",
            "body": """
<h2>Contactez-nous</h2>
<p>Vous avez une question, une suggestion ou besoin d'aide ? Nous sommes là pour vous aider.</p>

<div class="contact-info">
<h3>E-mail</h3>
<p><strong>info@socialcompass.social</strong></p>
<p>Nous vous répondrons dans les meilleurs délais, généralement sous 48 heures.</p>

<h3>Site web</h3>
<p><a href="https://calcto.work">https://calcto.work</a></p>

<h3>Langues supportées</h3>
<p>Nous traitons les demandes en français, anglais, espagnol, portugais, allemand et italien.</p>
</div>
""",
        },
        "pt": {
            "title": "Contato",
            "description": "Entre em contato com a equipe do CalcToWork. Estamos aqui para ajudar.",
            "body": """
<h2>Entre em contato</h2>
<p>Tem alguma dúvida, sugestão ou precisa de ajuda? Estamos aqui para ajudar.</p>

<div class="contact-info">
<h3>E-mail</h3>
<p><strong>info@socialcompass.social</strong></p>
<p>Responderemos o mais breve possível, geralmente em até 48 horas.</p>

<h3>Site</h3>
<p><a href="https://calcto.work">https://calcto.work</a></p>

<h3>Idiomas suportados</h3>
<p>Atendemos consultas em português, inglês, espanhol, francês, alemão e italiano.</p>
</div>
""",
        },
        "de": {
            "title": "Kontakt",
            "description": "Kontaktieren Sie das CalcToWork-Team. Wir sind hier, um Ihnen zu helfen.",
            "body": """
<h2>Kontaktieren Sie uns</h2>
<p>Haben Sie eine Frage, einen Vorschlag oder benötigen Sie Hilfe? Wir sind hier, um Ihnen zu helfen.</p>

<div class="contact-info">
<h3>E-Mail</h3>
<p><strong>info@socialcompass.social</strong></p>
<p>Wir antworten so schnell wie möglich, in der Regel innerhalb von 48 Stunden.</p>

<h3>Website</h3>
<p><a href="https://calcto.work">https://calcto.work</a></p>

<h3>Unterstützte Sprachen</h3>
<p>Wir bearbeiten Anfragen auf Deutsch, Englisch, Spanisch, Französisch, Portugiesisch und Italienisch.</p>
</div>
""",
        },
        "it": {
            "title": "Contatti",
            "description": "Contatta il team di CalcToWork. Siamo qui per aiutarti.",
            "body": """
<h2>Contattaci</h2>
<p>Hai domande, suggerimenti o bisogno di aiuto? Siamo qui per assisterti.</p>

<div class="contact-info">
<h3>Email</h3>
<p><strong>info@socialcompass.social</strong></p>
<p>Risponderemo il prima possibile, generalmente entro 48 ore.</p>

<h3>Sito web</h3>
<p><a href="https://calcto.work">https://calcto.work</a></p>

<h3>Lingue supportate</h3>
<p>Gestiamo richieste in italiano, inglese, spagnolo, francese, portoghese e tedesco.</p>
</div>
""",
        },
    },
    "about": {
        "es": {
            "title": "Sobre Nosotros",
            "description": "Conozca CalcToWork, la plataforma de calculadoras online gratuitas con más de 180 herramientas en 6 idiomas.",
            "body": """
<h2>¿Qué es CalcToWork?</h2>
<p>CalcToWork es una plataforma de calculadoras online gratuitas diseñada para hacer los cálculos accesibles a todos. Ofrecemos más de <strong>180 calculadoras</strong> que cubren una amplia gama de categorías:</p>
<ul>
<li><strong>Matemáticas:</strong> porcentajes, geometría, álgebra, estadísticas y más.</li>
<li><strong>Finanzas:</strong> hipotecas, préstamos, interés compuesto, IVA, salarios y más.</li>
<li><strong>Salud:</strong> IMC, calorías, peso ideal, consumo de agua y más.</li>
<li><strong>Ciencia:</strong> física, química, conversiones de unidades y más.</li>
<li><strong>Construcción:</strong> hormigón, mampostería, fontanería, electricidad y más.</li>
<li><strong>Vida cotidiana:</strong> propinas, edad, diferencia de fechas y más.</li>
</ul>

<h2>Nuestra misión</h2>
<p>Creemos que los cálculos precisos deben estar disponibles para todos, sin coste y sin barreras. Nuestro objetivo es proporcionar herramientas instantáneas, fiables y fáciles de usar que ayuden a estudiantes, profesionales y cualquier persona en su día a día.</p>

<h2>Disponibilidad multilingüe</h2>
<p>CalcToWork está disponible en <strong>6 idiomas</strong>: español, inglés, francés, portugués, alemán e italiano. Trabajamos para que nuestras calculadoras sean accesibles para personas de todo el mundo.</p>

<h2>Nuestro equipo</h2>
<p>CalcToWork fue fundado en 2025 por un pequeño equipo apasionado por hacer que los cálculos sean accesibles para todos. Cada calculadora es cuidadosamente diseñada y revisada para garantizar la mejor experiencia de usuario posible.</p>

<h2>Contacto</h2>
<p>¿Tiene alguna sugerencia o desea una nueva calculadora? Nos encantaría saber de usted: <strong>info@socialcompass.social</strong></p>
""",
        },
        "en": {
            "title": "About Us",
            "description": "Learn about CalcToWork, the free online calculator platform with over 180 tools in 6 languages.",
            "body": """
<h2>What is CalcToWork?</h2>
<p>CalcToWork is a free online calculator platform designed to make calculations accessible to everyone. We offer over <strong>180 calculators</strong> covering a wide range of categories:</p>
<ul>
<li><strong>Math:</strong> percentages, geometry, algebra, statistics, and more.</li>
<li><strong>Finance:</strong> mortgages, loans, compound interest, VAT, salaries, and more.</li>
<li><strong>Health:</strong> BMI, calories, ideal weight, water intake, and more.</li>
<li><strong>Science:</strong> physics, chemistry, unit conversions, and more.</li>
<li><strong>Construction:</strong> concrete, masonry, plumbing, electrical, and more.</li>
<li><strong>Everyday:</strong> tips, age, date differences, and more.</li>
</ul>

<h2>Our Mission</h2>
<p>We believe accurate calculations should be available to everyone, free of charge and without barriers. Our goal is to provide instant, reliable, and easy-to-use tools that help students, professionals, and anyone in their daily lives.</p>

<h2>Multilingual Availability</h2>
<p>CalcToWork is available in <strong>6 languages</strong>: English, Spanish, French, Portuguese, German, and Italian. We work to make our calculators accessible to people around the world.</p>

<h2>Our Team</h2>
<p>CalcToWork was founded in 2025 by a small team passionate about making calculations accessible to everyone. Each calculator is carefully designed and reviewed to ensure the best possible user experience.</p>

<h2>Contact</h2>
<p>Have a suggestion or want a new calculator? We'd love to hear from you: <strong>info@socialcompass.social</strong></p>
""",
        },
        "fr": {
            "title": "À propos",
            "description": "Découvrez CalcToWork, la plateforme de calculateurs en ligne gratuits avec plus de 180 outils en 6 langues.",
            "body": """
<h2>Qu'est-ce que CalcToWork ?</h2>
<p>CalcToWork est une plateforme de calculateurs en ligne gratuits conçue pour rendre les calculs accessibles à tous. Nous proposons plus de <strong>180 calculateurs</strong> couvrant un large éventail de catégories :</p>
<ul>
<li><strong>Mathématiques :</strong> pourcentages, géométrie, algèbre, statistiques et plus.</li>
<li><strong>Finances :</strong> hypothèques, prêts, intérêt composé, TVA, salaires et plus.</li>
<li><strong>Santé :</strong> IMC, calories, poids idéal, consommation d'eau et plus.</li>
<li><strong>Sciences :</strong> physique, chimie, conversions d'unités et plus.</li>
<li><strong>Construction :</strong> béton, maçonnerie, plomberie, électricité et plus.</li>
<li><strong>Quotidien :</strong> pourboires, âge, différence de dates et plus.</li>
</ul>

<h2>Notre mission</h2>
<p>Nous croyons que les calculs précis doivent être disponibles pour tous, gratuitement et sans barrières. Notre objectif est de fournir des outils instantanés, fiables et faciles à utiliser pour les étudiants, les professionnels et tout le monde.</p>

<h2>Disponibilité multilingue</h2>
<p>CalcToWork est disponible en <strong>6 langues</strong> : français, anglais, espagnol, portugais, allemand et italien. Nous travaillons pour rendre nos calculateurs accessibles aux personnes du monde entier.</p>

<h2>Notre équipe</h2>
<p>CalcToWork a été fondé en 2025 par une petite équipe passionnée par rendre les calculs accessibles à tous. Chaque calculateur est soigneusement conçu et révisé pour garantir la meilleure expérience utilisateur possible.</p>

<h2>Contact</h2>
<p>Vous avez une suggestion ou souhaitez un nouveau calculateur ? Nous serions ravis de vous entendre : <strong>info@socialcompass.social</strong></p>
""",
        },
        "pt": {
            "title": "Sobre Nós",
            "description": "Conheça o CalcToWork, a plataforma de calculadoras online gratuitas com mais de 180 ferramentas em 6 idiomas.",
            "body": """
<h2>O que é o CalcToWork?</h2>
<p>O CalcToWork é uma plataforma de calculadoras online gratuitas projetada para tornar os cálculos acessíveis a todos. Oferecemos mais de <strong>180 calculadoras</strong> abrangendo diversas categorias:</p>
<ul>
<li><strong>Matemática:</strong> porcentagens, geometria, álgebra, estatísticas e mais.</li>
<li><strong>Finanças:</strong> hipotecas, empréstimos, juros compostos, IVA, salários e mais.</li>
<li><strong>Saúde:</strong> IMC, calorias, peso ideal, consumo de água e mais.</li>
<li><strong>Ciência:</strong> física, química, conversões de unidades e mais.</li>
<li><strong>Construção:</strong> concreto, alvenaria, hidráulica, elétrica e mais.</li>
<li><strong>Cotidiano:</strong> gorjetas, idade, diferença de datas e mais.</li>
</ul>

<h2>Nossa missão</h2>
<p>Acreditamos que cálculos precisos devem estar disponíveis para todos, gratuitamente e sem barreiras. Nosso objetivo é fornecer ferramentas instantâneas, confiáveis e fáceis de usar que ajudem estudantes, profissionais e qualquer pessoa em seu dia a dia.</p>

<h2>Disponibilidade multilíngue</h2>
<p>O CalcToWork está disponível em <strong>6 idiomas</strong>: português, inglês, espanhol, francês, alemão e italiano. Trabalhamos para tornar nossas calculadoras acessíveis para pessoas do mundo todo.</p>

<h2>Nossa equipe</h2>
<p>O CalcToWork foi fundado em 2025 por uma pequena equipe apaixonada por tornar os cálculos acessíveis a todos. Cada calculadora é cuidadosamente projetada e revisada para garantir a melhor experiência possível.</p>

<h2>Contato</h2>
<p>Tem alguma sugestão ou deseja uma nova calculadora? Adoraríamos ouvir você: <strong>info@socialcompass.social</strong></p>
""",
        },
        "de": {
            "title": "Über uns",
            "description": "Erfahren Sie mehr über CalcToWork, die kostenlose Online-Rechner-Plattform mit über 180 Werkzeugen in 6 Sprachen.",
            "body": """
<h2>Was ist CalcToWork?</h2>
<p>CalcToWork ist eine Plattform für kostenlose Online-Rechner, die darauf ausgelegt ist, Berechnungen für jeden zugänglich zu machen. Wir bieten über <strong>180 Rechner</strong> in einer Vielzahl von Kategorien:</p>
<ul>
<li><strong>Mathematik:</strong> Prozent, Geometrie, Algebra, Statistik und mehr.</li>
<li><strong>Finanzen:</strong> Hypotheken, Kredite, Zinseszins, Mehrwertsteuer, Gehälter und mehr.</li>
<li><strong>Gesundheit:</strong> BMI, Kalorien, Idealgewicht, Wasserbedarf und mehr.</li>
<li><strong>Wissenschaft:</strong> Physik, Chemie, Einheitenumrechnungen und mehr.</li>
<li><strong>Bauwesen:</strong> Beton, Mauerwerk, Sanitär, Elektro und mehr.</li>
<li><strong>Alltag:</strong> Trinkgeld, Alter, Datumsdifferenzen und mehr.</li>
</ul>

<h2>Unsere Mission</h2>
<p>Wir glauben, dass genaue Berechnungen für alle verfügbar sein sollten, kostenlos und ohne Barrieren. Unser Ziel ist es, sofortige, zuverlässige und benutzerfreundliche Werkzeuge anzubieten, die Studenten, Fachleuten und jedem im Alltag helfen.</p>

<h2>Mehrsprachige Verfügbarkeit</h2>
<p>CalcToWork ist in <strong>6 Sprachen</strong> verfügbar: Deutsch, Englisch, Spanisch, Französisch, Portugiesisch und Italienisch. Wir arbeiten daran, unsere Rechner für Menschen auf der ganzen Welt zugänglich zu machen.</p>

<h2>Unser Team</h2>
<p>CalcToWork wurde 2025 von einem kleinen Team gegründet, das leidenschaftlich daran arbeitet, Berechnungen für alle zugänglich zu machen. Jeder Rechner wird sorgfältig entworfen und überprüft, um die bestmögliche Benutzererfahrung zu gewährleisten.</p>

<h2>Kontakt</h2>
<p>Haben Sie einen Vorschlag oder möchten einen neuen Rechner? Wir freuen uns auf Ihre Nachricht: <strong>info@socialcompass.social</strong></p>
""",
        },
        "it": {
            "title": "Chi siamo",
            "description": "Scopri CalcToWork, la piattaforma di calcolatori online gratuiti con oltre 180 strumenti in 6 lingue.",
            "body": """
<h2>Cos'è CalcToWork?</h2>
<p>CalcToWork è una piattaforma di calcolatori online gratuiti progettata per rendere i calcoli accessibili a tutti. Offriamo oltre <strong>180 calcolatori</strong> che coprono un'ampia gamma di categorie:</p>
<ul>
<li><strong>Matematica:</strong> percentuali, geometria, algebra, statistica e altro.</li>
<li><strong>Finanze:</strong> mutui, prestiti, interesse composto, IVA, stipendi e altro.</li>
<li><strong>Salute:</strong> IMC, calorie, peso ideale, consumo di acqua e altro.</li>
<li><strong>Scienze:</strong> fisica, chimica, conversioni di unità e altro.</li>
<li><strong>Costruzione:</strong> calcestruzzo, muratura, impianti idraulici, elettricità e altro.</li>
<li><strong>Vita quotidiana:</strong> mancia, età, differenza tra date e altro.</li>
</ul>

<h2>La nostra missione</h2>
<p>Crediamo che i calcoli accurati debbano essere disponibili per tutti, gratuitamente e senza barriere. Il nostro obiettivo è fornire strumenti istantanei, affidabili e facili da usare che aiutino studenti, professionisti e chiunque nella vita quotidiana.</p>

<h2>Disponibilità multilingue</h2>
<p>CalcToWork è disponibile in <strong>6 lingue</strong>: italiano, inglese, spagnolo, francese, portoghese e tedesco. Lavoriamo per rendere i nostri calcolatori accessibili alle persone di tutto il mondo.</p>

<h2>Il nostro team</h2>
<p>CalcToWork è stato fondato nel 2025 da un piccolo team appassionato di rendere i calcoli accessibili a tutti. Ogni calcolatore è accuratamente progettato e revisionato per garantire la migliore esperienza utente possibile.</p>

<h2>Contatti</h2>
<p>Hai un suggerimento o desideri un nuovo calcolatore? Ci piacerebbe sentirti: <strong>info@socialcompass.social</strong></p>
""",
        },
    },
}


def inject_cross_links(html: str, calc_id: str, lang: str, calc_url_by_id: dict, calcs_i18n: dict) -> str:
    links = CROSS_LINKS.get(calc_id, [])
    if not links or not html:
        return html
    items = []
    for rid in links:
        ci = calcs_i18n.get(rid, {})
        name = ci.get("name", "")
        slug = calc_url_by_id.get(rid, "")
        if name and slug:
            items.append(f'<a href="/{lang}/{slug}/">{name}</a>')
    if not items:
        return html
    label = CROSS_LINK_LABELS.get(lang, CROSS_LINK_LABELS["en"])
    link_html = " · ".join(items)
    close_tag = "</section>"
    cross_section = f'<p class="cross-links"><strong>{label}:</strong> {link_html}</p>'
    if close_tag in html:
        html = html.replace(close_tag, cross_section + close_tag, 1)
    else:
        html += cross_section
    return html


def build_popular_combos(cid: str, lang: str, loc_slug: str, max_combos: int = 8) -> list:
    """Return up to max_combos popular variant links for a base calculator page."""
    vcfg = PARAMETRIC_VARIANTS.get(cid)
    if not vcfg:
        return []
    vkeys = list(vcfg["inputs"].keys())
    vlists = [vcfg["inputs"][k] for k in vkeys]
    lang_tpl = vcfg["title_template"].get(lang, vcfg["title_template"]["en"])
    combos = []
    for combo in cartesian_product(*vlists):
        params = dict(zip(vkeys, combo))
        param_slug = vcfg["url_fn"](params)
        label = vcfg["title_fn"](params, lang_tpl)
        combos.append({"path": f"{loc_slug}/{param_slug}", "label": label})
    mid = len(combos) // 2
    quarter = len(combos) // 4
    indices = sorted(set([0, quarter, mid, mid + quarter, len(combos) - 1,
                          quarter // 2, mid + quarter // 2, len(combos) - quarter // 2 - 1]))
    return [combos[i] for i in indices if i < len(combos)][:max_combos]


# ── I/O helpers ────────────────────────────────────────────────────────────────

def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def normalize_trans(raw: dict) -> dict:
    """Map i18n file keys → template-expected keys."""
    raw_calcs = raw.get("calculators", {})
    calcs_i18n = {
        cid: {
            "name":            c.get("name", ""),
            "description":     c.get("desc", c.get("description", "")),
            "seo_title":       c.get("seo_title", c.get("name", "")),
            "seo_description": c.get("seo_desc", c.get("seo_description", c.get("description", ""))),
            "inputs":          c.get("inputs", {}),
            "outputs":         c.get("outputs", {}),
        }
        for cid, c in raw_calcs.items()
    }
    return {
        "lang":            raw.get("lang", ""),
        "lang_name":       raw.get("lang_name", ""),
        "site_name":       BRAND,
        "site_tagline":    raw.get("site_tagline", ""),
        "site_description":raw.get("site_description", ""),
        "nav_home":        raw.get("nav_home", "Home"),
        "nav_calculators": raw.get("nav_tools", raw.get("nav_calculators", "Calculators")),
        "nav_about":       raw.get("nav_about", ""),
        "nav_privacy":     raw.get("nav_privacy", ""),
        "nav_terms":       raw.get("nav_terms", ""),
        "nav_contact":     raw.get("nav_contact", ""),
        "footer_rights":   raw.get("footer_rights", raw.get("footer_text", "")),
        "footer_disclaimer": raw.get("footer_disclaimer", ""),
        "btn_calculate":   raw.get("calculate_btn", raw.get("btn_calculate", "Calculate")),
        "btn_reset":       raw.get("reset_btn", raw.get("btn_reset", "Reset")),
        "btn_copy":        raw.get("copy_btn", raw.get("btn_copy", "Copy results")),
        "label_results":   raw.get("result_title", raw.get("label_results", "Results")),
        "label_inputs":    raw.get("inputs_title", raw.get("label_inputs", "Inputs")),
        "label_related":   raw.get("related_tools", raw.get("label_related", "Related")),
        "error_invalid":   raw.get("error_invalid", "Invalid values."),
        "result_placeholder": raw.get("result_placeholder", "Enter values and press Calculate"),
        "meta_suffix":     f"| {BRAND}",
        "blocks":          raw.get("block_slugs", raw.get("blocks", {})),
        "calculators":     calcs_i18n,
    }


def load_translations() -> dict:
    result = {}
    for lang in LANGS:
        raw = load_json(I18N_DIR / f"{lang}.json")
        result[lang] = normalize_trans(raw)
    return result


def load_calculators() -> list:
    data = load_json(CALCS_FILE)
    return data.get("calculators", data) if isinstance(data, dict) else data


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_assets() -> None:
    assets = [
        (CSS_SRC,              PUBLIC / "css" / "styles.css"),
        (JS_SRC,               PUBLIC / "js"  / "calculator.js"),
        (SRC / "robots.txt",   PUBLIC / "robots.txt"),
        (SRC / "favicon.svg",  PUBLIC / "favicon.svg"),
    ]
    for src, dest in assets:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    print("  [assets] Copied CSS, JS, robots.txt and favicon")


def make_env() -> "Environment":
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def build_placeholders(input_keys: list, lang: str) -> dict:
    prefix_map = {
        "es": "ej.", "en": "e.g.", "fr": "ex.",
        "pt": "ex.", "de": "z.B.", "it": "es.",
    }
    prefix = prefix_map.get(lang, "e.g.")
    result = {}
    for key in input_keys:
        hint = PLACEHOLDER_HINTS.get(key, "")
        if hint:
            hint = hint.replace("e.g.", prefix)
        result[key] = hint
    return result


def extract_toc(html_content: str) -> list:
    if not html_content:
        return []
    headings = re.findall(r'<h2[^>]*>(.*?)</h2>', html_content)
    items = []
    seen = set()
    for h in headings:
        slug = re.sub(r'<[^>]+>', '', h).strip().lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
        if not slug or slug in seen:
            continue
        seen.add(slug)
        items.append({"id": slug, "text": re.sub(r'<[^>]+>', '', h).strip()})
    return items


def inject_heading_ids(html_content: str) -> str:
    if not html_content:
        return html_content
    def _add_id(match):
        attrs = match.group(1) or ''
        text = match.group(2)
        if 'id=' in attrs:
            return match.group(0)
        slug = re.sub(r'<[^>]+>', '', text).strip().lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
        return f'<h2 id="{slug}"{attrs}>{text}</h2>'
    return re.sub(r'<h2([^>]*)>(.*?)</h2>', _add_id, html_content)


def build_input_groups(input_items: list, lang: str, input_meta: dict = None) -> list:
    """
    Build grouped input structure for template rendering.
    input_items: list of (key, label) tuples.
    input_meta: optional dict mapping key -> input metadata dict.
    Returns: [{id, label, icon, fields: [{key, label, unit_options, unit_category}]}, ...]
    """
    groups_ordered = []
    groups_data: dict = {}
    input_meta = input_meta or {}

    for key, label in input_items:
        gid = classify_input(key)
        if gid not in groups_data:
            groups_ordered.append(gid)
            groups_data[gid] = []
        unit = UNIT_LABELS.get(key, "")
        full_label = f"{label} ({unit})" if unit else label
        meta = input_meta.get(key, {})
        field = {"key": key, "label": full_label, "type": meta.get("type", "number")}
        if meta.get("type") == "select":
            default_val = str(meta.get("default", ""))
            raw_opts = meta.get("options", [])
            field["options"] = [
                {
                    "value": str(o["value"]) if isinstance(o, dict) else str(o),
                    "label": str(o.get("label", o["value"])) if isinstance(o, dict) else str(o),
                    "selected": (str(o["value"]) if isinstance(o, dict) else str(o)) == default_val,
                }
                for o in raw_opts
            ]
        elif meta.get("unit_options"):
            field["unit_options"] = meta["unit_options"]
            field["unit_category"] = meta.get("unit_category", "")
            field["unit_default"] = meta.get("unit", "")
        groups_data[gid].append(field)

    return [
        {
            "id": gid,
            "label": GROUP_LABELS.get(gid, {}).get(lang, gid),
            "icon": GROUP_ICONS.get(gid, ""),
            "fields": groups_data[gid],
        }
        for gid in groups_ordered
    ]


# ── Redirect helpers ──────────────────────────────────────────────────────────

def make_redirect_html(target_url: str) -> str:
    return (
        '<!DOCTYPE html><html><head><meta charset="UTF-8">'
        f'<meta http-equiv="refresh" content="0;url={target_url}">'
        f'<link rel="canonical" href="{target_url}">'
        '</head><body>'
        f'<a href="{target_url}">Redirecting…</a>'
        '</body></html>'
    )


def generate_legacy_redirects(calculators: list, public: Path) -> int:
    """
    Generate redirect pages from old /lang/block_slug/slug/ → new /lang/loc_slug/
    so bookmarks and any existing links still work.
    """
    count = 0
    for lang in LANGS:
        for calc in calculators:
            cid = calc["id"]
            tool_cfg = TOOL_BY_ID.get(cid)
            if not tool_cfg:
                continue
            old_slug = calc.get("slug", "")
            block_slug = calc.get("block_slug", "")
            loc_slug = tool_cfg["slugs"].get(lang, old_slug)
            if not old_slug or not block_slug:
                continue
            # Only write redirect if old path differs from new path
            old_path = public / lang / block_slug / old_slug / "index.html"
            new_url = f"/{lang}/{loc_slug}/"
            if not old_path.exists():
                write_file(old_path, make_redirect_html(new_url))
                count += 1
    return count


# ── Main generation ────────────────────────────────────────────────────────────

def generate() -> None:
    print(f"{BRAND} v3.0 - Static Site Generator")
    print(f"  Build date : {BUILD_DATE}")
    print(f"  Languages  : {', '.join(LANGS)}")
    print(f"  Base URL   : {BASE_URL}")

    calculators  = load_calculators()
    translations = load_translations()
    env          = make_env()

    calc_by_id     = {c["id"]: c for c in calculators}
    blocks_by_slug: dict = {}
    for c in calculators:
        blocks_by_slug.setdefault(c["block_slug"], []).append(c)

    if PUBLIC.exists():
        shutil.rmtree(PUBLIC, ignore_errors=True)
    PUBLIC.mkdir(parents=True, exist_ok=True)
    print(f"  Output dir : {PUBLIC}")
    copy_assets()

    calc_tpl         = env.get_template("calculator.html.j2")
    index_tpl        = env.get_template("index.html.j2")
    block_tpl        = env.get_template("block.html.j2")
    static_tpl       = env.get_template("static_page.html.j2")
    sitemap_tpl      = env.get_template("sitemap.xml.j2")
    sitemap_idx_tpl  = env.get_template("sitemap_index.xml.j2")

    sitemap_entries: list = []
    page_count = 0
    warn_count = 0

    for lang in LANGS:
        t          = translations[lang]
        calcs_i18n = t["calculators"]

        # Localized slug lookup for this language: {calc_id: slug}
        calc_url_by_id = {
            calc["id"]: TOOL_BY_ID[calc["id"]]["slugs"].get(lang, calc["slug"])
            for calc in calculators
            if calc["id"] in TOOL_BY_ID
        }

        # Build search index for this language
        calc_index = [
            {
                "id": calc["id"],
                "name": calcs_i18n.get(calc["id"], {}).get("name", ""),
                "slug": calc_url_by_id.get(calc["id"], calc["slug"]),
                "block": t["blocks"].get(calc["block_slug"], calc["block_slug"]),
                "block_slug": calc["block_slug"],
            }
            for calc in calculators
            if calcs_i18n.get(calc["id"], {}).get("name")
        ]

        # ── Index page ────────────────────────────────────────────────────────
        index_html = index_tpl.render(
            lang=lang, t=t, all_langs=LANGS,
            blocks_by_slug=blocks_by_slug,
            calcs_i18n=calcs_i18n,
            block_icons=BLOCK_ICONS,
            brand_name=BRAND,
            site_base_url=BASE_URL,
            calc_url_by_id=calc_url_by_id,
            calc_index_json=json.dumps(calc_index, ensure_ascii=False),
            calc_count=len(calculators),
            ga4_head=GA4_HEAD,
            adsense_head=ADSENSE_HEAD,
            adsense_banner=ADSENSE_BANNER,
            adsense_responsive=ADSENSE_RESPONSIVE,
            author_line=AUTHOR_LINE.get(lang, AUTHOR_LINE["en"]).format(date=BUILD_DATE),
        )
        write_file(PUBLIC / lang / "index.html", index_html)
        page_count += 1
        sitemap_entries.append({
            "loc": f"{BASE_URL}/{lang}/",
            "priority": "1.0",
            "alternates": [{"lang": al, "href": f"{BASE_URL}/{al}/"} for al in LANGS],
            "lang": lang,
        })

        # ── Block pages ───────────────────────────────────────────────────────
        for block_slug, block_calcs in blocks_by_slug.items():
            block_name = t["blocks"].get(block_slug, block_slug)
            block_desc = t.get("block_descriptions", {}).get(block_slug, f"{block_name} – free construction calculators.")
            block_html = block_tpl.render(
                lang=lang, t=t, all_langs=LANGS,
                block_slug=block_slug, block_name=block_name,
                block_description=block_desc,
                block_calcs=block_calcs, calcs_i18n=calcs_i18n,
                brand_name=BRAND,
                site_base_url=BASE_URL,
                calc_url_by_id=calc_url_by_id,
                ga4_head=GA4_HEAD,
            adsense_head=ADSENSE_HEAD,
                adsense_banner=ADSENSE_BANNER,
                adsense_responsive=ADSENSE_RESPONSIVE,
            )
            write_file(PUBLIC / lang / block_slug / "index.html", block_html)
            page_count += 1
            sitemap_entries.append({
                "loc": f"{BASE_URL}/{lang}/{block_slug}/",
                "priority": "0.8",
                "alternates": [
                    {"lang": al, "href": f"{BASE_URL}/{al}/{block_slug}/"} for al in LANGS
                ],
                "lang": lang,
            })

        # ── Calculator pages ──────────────────────────────────────────────────
        for calc in calculators:
            cid = calc["id"]

            ci18n = calcs_i18n.get(cid)
            if not ci18n or not ci18n.get("name"):
                warn_count += 1
                continue

            tool_cfg = TOOL_BY_ID.get(cid)
            if not tool_cfg:
                print(f"  [WARN] No tool config for calc {cid} - skipping")
                warn_count += 1
                continue

            cat = tool_cfg["cat"]
            loc_slug = tool_cfg["slugs"].get(lang, tool_cfg["slugs"].get("es", calc["slug"]))
            alt_slugs = tool_cfg["slugs"]  # {lang: slug}

            block_name = t["blocks"].get(calc["block_slug"], calc["block_slug"])

            # ── Related calculators ──────────────────────────────────────────
            related_calcs = []
            for rel_id in calc.get("related", [])[:4]:
                rel = calc_by_id.get(rel_id)
                if rel:
                    rel_tool = TOOL_BY_ID.get(rel_id, {})
                    rel_ci18n = calcs_i18n.get(rel_id, {})
                    related_calcs.append({
                        "id": rel_id,
                        "name": rel_ci18n.get("name", rel["slug"]),
                        "url_path": rel_tool.get("slugs", {}).get(lang, rel["slug"]),
                        # keep for fallback
                        "slug": rel["slug"],
                        "block_slug": rel["block_slug"],
                    })

            # ── Long content + TOC ───────────────────────────────────────────
            # 1. Check for external content file first (batch-generated)
            content_file = CONTENT_DIR / lang / f"{cid}.html"
            has_long_content = content_file.exists()
            if has_long_content:
                long_content_raw = content_file.read_text(encoding="utf-8")
            else:
                long_content_raw = generate_long_content(cid, lang, calc_name=ci18n["name"])

            # ── Content ──────────────────────────────────────────────────────
            # Only generate generic block-level content when no calculator-specific
            # long content exists. This prevents wrong FAQ/formulas/how-to from
            # appearing on batch-generated calculators.
            intro_text        = generate_intro(cid, lang, ci18n["name"], ci18n["description"], block_slug=calc["block_slug"])
            if has_long_content:
                how_to_steps = []
                faq = []
                formula_explained = ""
            else:
                how_to_steps      = generate_how_to(calc["block_slug"], lang)
                faq               = generate_faq(calc["block_slug"], lang)
                formula_explained = generate_formula_explained(calc["block_slug"], lang)
            long_content_raw = inject_cross_links(long_content_raw, cid, lang, calc_url_by_id, calcs_i18n)
            long_content = inject_heading_ids(long_content_raw) if long_content_raw else ""
            toc_items = extract_toc(long_content_raw) if long_content_raw else []

            # ── Grouped inputs ───────────────────────────────────────────────
            input_items = list(ci18n["inputs"].items())
            input_keys  = [k for k, _ in input_items]
            input_meta = {inp["id"]: inp for inp in calc.get("inputs", []) if "id" in inp}
            input_groups = build_input_groups(input_items, lang, input_meta)
            input_placeholders = build_placeholders(input_keys, lang)

            # ── Wastage ──────────────────────────────────────────────────────
            # Only show wastage for construction-related blocks.
            construction_blocks = {
                "estructuras", "mamposteria", "pavimentos",
                "fontaneria", "electricidad", "climatizacion",
                "carpinteria", "pintura", "gestion",
            }
            is_construction = calc.get("block_slug", "") in construction_blocks
            show_wastage   = is_construction and SHOW_WASTAGE.get(cat, False)
            wastage_default = WASTAGE_DEFAULTS.get(cat, 0) if is_construction else 0

            calc_html = calc_tpl.render(
                lang=lang, t=t, all_langs=LANGS,
                calc=calc, calc_i18n=ci18n,
                block_name=block_name,
                related_calcs=related_calcs,
                brand_name=BRAND,
                site_base_url=BASE_URL,
                # URL
                calc_url_path=loc_slug,
                calc_alt_slugs=alt_slugs,
                # Content
                intro_text=intro_text,
                how_to_steps=how_to_steps,
                faq=faq,
                howto_title=HOW_TO_TITLE.get(lang, HOW_TO_TITLE["en"]),
                faq_title=FAQ_TITLE.get(lang, FAQ_TITLE["en"]),
                formula_explained=formula_explained,
                formula_title=FORMULA_TITLE.get(lang, FORMULA_TITLE["en"]),
                long_content=long_content,
                toc_items=toc_items,
                toc_title=TOC_TITLE.get(lang, TOC_TITLE["en"]),
                popular_combos=build_popular_combos(cid, lang, loc_slug),
                popular_combos_title=POPULAR_COMBOS_TITLE.get(lang, POPULAR_COMBOS_TITLE["en"]),
                # Inputs
                input_groups=input_groups,
                input_placeholders=input_placeholders,
                input_meta=input_meta,
                # Wastage
                show_wastage=show_wastage,
                wastage_default=wastage_default,
                wastage_label=WASTAGE_LABEL.get(lang, WASTAGE_LABEL["en"]),
                wastage_placeholder=WASTAGE_PLACEHOLDER.get(lang, "e.g. 10"),
                net_label=NET_LABEL.get(lang, NET_LABEL["en"]),
                total_label=TOTAL_LABEL.get(lang, TOTAL_LABEL["en"]),
                copied_label=COPIED_LABEL.get(lang, "Copied!"),
                link_copied_label=LINK_COPIED_LABEL.get(lang, "Link copied!"),
                btn_share_label=BTN_SHARE_LABEL.get(lang, "🔗 Share"),
                # Feedback
                feedback_label=FEEDBACK_LABEL.get(lang, FEEDBACK_LABEL["en"]),
                feedback_thanks=FEEDBACK_THANKS.get(lang, FEEDBACK_THANKS["en"]),
                # Gauge
                gauge_config=GAUGE_CONFIGS.get(cid),
                # Dates
                date_published="2025-01-01",
                date_modified=BUILD_DATE,
                BUILD_DATE=BUILD_DATE,
                author_line=AUTHOR_LINE.get(lang, AUTHOR_LINE["en"]).format(date=BUILD_DATE),
                # AdSense
                ga4_head=GA4_HEAD,
            adsense_head=ADSENSE_HEAD,
                adsense_banner=ADSENSE_BANNER,
                adsense_responsive=ADSENSE_RESPONSIVE,
            )

            out_path = PUBLIC / lang / loc_slug / "index.html"
            write_file(out_path, calc_html)
            page_count += 1

            sitemap_entries.append({
                "loc": f"{BASE_URL}/{lang}/{loc_slug}/",
                "priority": "0.7",
                "alternates": [
                    {"lang": al, "href": f"{BASE_URL}/{al}/{tool_cfg['slugs'].get(al, loc_slug)}/"}
                    for al in LANGS
                ],
                "lang": lang,
            })

    # ── Parametric pages ──────────────────────────────────────────────────────
    param_count = 0
    for lang in LANGS:
        t          = translations[lang]
        calcs_i18n = t["calculators"]
        calc_url_by_id = {
            calc["id"]: TOOL_BY_ID[calc["id"]]["slugs"].get(lang, calc["slug"])
            for calc in calculators
            if calc["id"] in TOOL_BY_ID
        }

        for calc in calculators:
            cid = calc["id"]
            if cid not in PARAMETRIC_VARIANTS:
                continue
            if cid not in TOOL_BY_ID:
                continue

            vcfg     = PARAMETRIC_VARIANTS[cid]
            loc_slug = calc_url_by_id.get(cid, calc["slug"])
            ci18n    = calcs_i18n.get(cid, {})
            if not ci18n:
                continue

            tool_cfg   = TOOL_BY_ID[cid]
            cat        = tool_cfg.get("cat", "C")
            block_slug = calc.get("block_slug", "")
            block_name = t.get("blocks", {}).get(block_slug, block_slug)
            construction_blocks = {
                "estructuras", "mamposteria", "pavimentos",
                "fontaneria", "electricidad", "climatizacion",
                "carpinteria", "pintura", "gestion",
            }
            is_construction = block_slug in construction_blocks
            show_wastage   = is_construction and SHOW_WASTAGE.get(cat, False)
            wastage_default = vcfg.get("wastage_default", WASTAGE_DEFAULTS.get(cat, 0)) if is_construction else 0

            input_items = list(ci18n["inputs"].items())
            input_keys  = [k for k, _ in input_items]
            input_groups = build_input_groups(input_items, lang)
            input_placeholders = build_placeholders(input_keys, lang)

            # Build alt slugs for hreflang
            alt_slugs = {al: TOOL_BY_ID[cid]["slugs"].get(al, calc["slug"]) for al in LANGS}

            # Cartesian product of all variant dimensions
            vkeys  = list(vcfg["inputs"].keys())
            vlists = [vcfg["inputs"][k] for k in vkeys]

            for combo in cartesian_product(*vlists):
                params     = dict(zip(vkeys, combo))
                param_slug = vcfg["url_fn"](params)
                lang_tpl   = vcfg["title_template"].get(lang, vcfg["title_template"]["en"])
                title      = vcfg["title_fn"](params, lang_tpl)
                desc_tpl   = vcfg["desc_template"].get(lang, vcfg["desc_template"]["en"])
                desc       = vcfg["desc_fn"](params, desc_tpl)
                result_fn  = vcfg.get("result_fn")
                quick_ans  = result_fn(params, lang) if result_fn else ""

                variant_url_path = f"{loc_slug}/{param_slug}"
                variant_alt_slugs = {
                    al: f"{TOOL_BY_ID[cid]['slugs'].get(al, loc_slug)}/{param_slug}"
                    for al in LANGS
                }

                html = calc_tpl.render(
                    lang=lang, t=t, all_langs=LANGS,
                    calc=calc, calc_i18n=ci18n,
                    block_name=block_name,
                    related_calcs=[],
                    brand_name=BRAND,
                    site_base_url=BASE_URL,
                    calc_url_path=variant_url_path,
                    calc_alt_slugs=variant_alt_slugs,
                    intro_text=generate_variant_intro(title, desc, lang, quick_ans),
                    how_to_steps=[],
                    faq=[],
                    howto_title=HOW_TO_TITLE.get(lang, HOW_TO_TITLE["en"]),
                    faq_title=FAQ_TITLE.get(lang, FAQ_TITLE["en"]),
                    formula_explained="",
                    formula_title=FORMULA_TITLE.get(lang, FORMULA_TITLE["en"]),
                    input_groups=input_groups,
                    input_placeholders=input_placeholders,
                    show_wastage=show_wastage,
                    wastage_default=wastage_default,
                    wastage_label=WASTAGE_LABEL.get(lang, WASTAGE_LABEL["en"]),
                    wastage_placeholder=WASTAGE_PLACEHOLDER.get(lang, "e.g. 10"),
                    net_label=NET_LABEL.get(lang, NET_LABEL["en"]),
                    total_label=TOTAL_LABEL.get(lang, TOTAL_LABEL["en"]),
                    copied_label=COPIED_LABEL.get(lang, "Copied!"),
                    link_copied_label=LINK_COPIED_LABEL.get(lang, "Link copied!"),
                    btn_share_label=BTN_SHARE_LABEL.get(lang, "🔗 Share"),
                    feedback_label=FEEDBACK_LABEL.get(lang, FEEDBACK_LABEL["en"]),
                    feedback_thanks=FEEDBACK_THANKS.get(lang, FEEDBACK_THANKS["en"]),
                    gauge_config=GAUGE_CONFIGS.get(cid),
                    date_published="2025-01-01",
                    date_modified=BUILD_DATE,
                    BUILD_DATE=BUILD_DATE,
                    author_line=AUTHOR_LINE.get(lang, AUTHOR_LINE["en"]).format(date=BUILD_DATE),
                    toc_items=[],
                    # Parametric overrides
                    seo_title_override=title,
                    seo_desc_override=desc,
                    prefill_json=json.dumps(params),
                    # AdSense
                    ga4_head=GA4_HEAD,
            adsense_head=ADSENSE_HEAD,
                    adsense_banner=ADSENSE_BANNER,
                    adsense_responsive=ADSENSE_RESPONSIVE,
                )

                out_path = PUBLIC / lang / loc_slug / param_slug / "index.html"
                write_file(out_path, html)
                param_count += 1

                sitemap_entries.append({
                    "loc": f"{BASE_URL}/{lang}/{loc_slug}/{param_slug}/",
                    "priority": "0.5",
                    "alternates": [],
                    "lang": lang,
                })

    # ── Static pages (privacy, terms, contact, about) ────────────────────────
    static_count = 0
    for page_slug, page_content in STATIC_PAGES.items():
        for lang in LANGS:
            t = translations[lang]
            pc = page_content.get(lang)
            if not pc:
                print(f"  [WARN] No static content for {page_slug}/{lang}")
                continue
            html = static_tpl.render(
                lang=lang, t=t, all_langs=LANGS,
                page_slug=page_slug,
                page_title=pc["title"],
                page_description=pc["description"],
                page_body=pc["body"],
                brand_name=BRAND,
                site_base_url=BASE_URL,
                ga4_head=GA4_HEAD,
            adsense_head=ADSENSE_HEAD,
                author_line=AUTHOR_LINE.get(lang, AUTHOR_LINE["en"]).format(date=BUILD_DATE),
            )
            out = PUBLIC / lang / page_slug / "index.html"
            write_file(out, html)
            static_count += 1
            sitemap_entries.append({
                "loc": f"{BASE_URL}/{lang}/{page_slug}/",
                "priority": "0.4",
                "alternates": [
                    {"lang": al, "href": f"{BASE_URL}/{al}/{page_slug}/"} for al in LANGS
                ],
                "lang": lang,
            })
    print(f"  [static] Generated {static_count} legal pages")

    # ── Sitemap: one file per language + sitemap index ────────────────────────
    by_lang = {lang: [] for lang in LANGS}
    for entry in sitemap_entries:
        entry_lang = entry.get("lang")
        if entry_lang and entry_lang in by_lang:
            by_lang[entry_lang].append(entry)
    for lang, entries in by_lang.items():
        xml = sitemap_tpl.render(sitemap_entries=entries, build_date=BUILD_DATE)
        write_file(PUBLIC / f"sitemap-{lang}.xml", xml)
    idx_xml = sitemap_idx_tpl.render(langs=LANGS, base_url=BASE_URL, build_date=BUILD_DATE)
    write_file(PUBLIC / "sitemap.xml", idx_xml)

    # ── Root redirect ─────────────────────────────────────────────────────────
    write_file(PUBLIC / "index.html", (
        '<!DOCTYPE html><html><head>'
        '<meta charset="UTF-8">'
        f'<meta http-equiv="refresh" content="0;url=/es/">'
        f'<link rel="canonical" href="{BASE_URL}/es/">'
        f'</head><body><a href="/es/">{BRAND}</a></body></html>'
    ))

    # ── Legacy redirects (/lang/block_slug/slug/ → /lang/loc_slug/) ──────────
    redirect_count = generate_legacy_redirects(calculators, PUBLIC)

    print(f"\n[OK] Generated {page_count} base pages")
    print(f"[OK] Parametric: {param_count} variant pages")
    print(f"[OK] Static: {static_count} legal pages")
    print(f"[OK] Redirects: {redirect_count} legacy URL redirects")
    if warn_count:
        print(f"[WARN] {warn_count} missing translations skipped")
    print(f"[OK] Sitemap : {len(sitemap_entries)} URLs ({len(LANGS)} language files)")
    print(f"[OK] Output  : {PUBLIC}")
    print(f"\nDeploy with:  firebase deploy --only hosting")


if __name__ == "__main__":
    generate()

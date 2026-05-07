#!/usr/bin/env python3
"""Fix ALL Italian (it) i18n issues in calculator JSONs. Spanish (es) is reference."""

import json
import glob
import os
import re
import sys

WORKDIR = r'C:\Microsaas\obra\src\calculators'

# ── Spanish → Italian term mappings ──────────────────────────────────────────

# Common words appearing in labels
ES_TO_IT_WORDS = {
    # Verbs
    'Ingresar': 'Inserire', 'ingresar': 'inserire',
    'Calcular': 'Calcolare', 'calcular': 'calcolare',
    'Convertir': 'Convertire', 'convertir': 'convertire',
    'Estimar': 'Stimare', 'estimar': 'stimare',
    'Introduce': 'Inserisci', 'introduce': 'inserisci',
    'Introducir': 'Inserire', 'introducir': 'inserire',
    'Pulsa': 'Premi', 'pulsa': 'premi',
    'Pulsar': 'Premere', 'pulsar': 'premere',
    'Revisa': 'Verifica', 'revisa': 'verifica',
    'Revisar': 'Verificare', 'revisar': 'verificare',
    'Leer': 'Leggi', 'leer': 'leggi',
    'Lee': 'Leggi', 'lee': 'leggi',
    'Interpreta': 'Interpreta', 'interpreta': 'interpreta',
    'Multiplica': 'Moltiplica', 'multiplica': 'moltiplica',
    'Divide': 'Dividi', 'divide': 'dividi',
    'Suma': 'Somma', 'suma': 'somma',
    'Resta': 'Sottrai', 'resta': 'sottrai',
    'Obtener': 'Ottenere', 'obtener': 'ottenere',
    'Obtén': 'Ottieni',
    'Elegir': 'Scegliere', 'elegir': 'scegliere',
    'Seleccionar': 'Selezionare', 'seleccionar': 'selezionare',
    'Usar': 'Usare', 'usar': 'usare',
    'Ajustar': 'Regolare', 'ajustar': 'regolare',
    'Ajusta': 'Regola', 'ajusta': 'regola',
    'Comparar': 'Confrontare', 'comparar': 'confrontare',
    'Evaluar': 'Valutare', 'evaluar': 'valutare',
    'Determinar': 'Determinare', 'determinar': 'determinare',
    'Analizar': 'Analizzare', 'analizar': 'analizzare',
    'Verificar': 'Verificare', 'verificar': 'verificare',
    'Aplicar': 'Applicare', 'aplicar': 'applicare',
    'Añadir': 'Aggiungere', 'añadir': 'aggiungere',
    'Comprobar': 'Verificare', 'comprobar': 'verificare',
    'Consultar': 'Consultare', 'consultar': 'consultare',
    'Considerar': 'Considerare', 'considerar': 'considerare',
    'Conocer': 'Conoscere', 'conocer': 'conoscere',
    'Convert': 'Convertire', 'convert': 'convertire',
    'Define': 'Definisci', 'define': 'definisci',
    'Utilizar': 'Utilizzare', 'utilizar': 'utilizzare',
    'Utiliza': 'Utilizza', 'utiliza': 'utilizza',

    # Nouns
    'Resultado': 'Risultato', 'resultado': 'risultato',
    'Resultados': 'Risultati', 'resultados': 'risultati',
    'Ejemplo': 'Esempio', 'ejemplo': 'esempio',
    'Ejemplos': 'Esempi', 'ejemplos': 'esempi',
    'Pasos': 'Passi', 'pasos': 'passi',
    'Paso': 'Passo', 'paso': 'passo',
    'Cálculo': 'Calcolo', 'cálculo': 'calcolo',
    'Cálculos': 'Calcoli', 'cálculos': 'calcoli',
    'Fórmula': 'Formula', 'fórmula': 'formula',
    'Error': 'Errore', 'error': 'errore',
    'Errores': 'Errori', 'errores': 'errori',
    'Valor': 'Valore', 'valor': 'valore',
    'Valores': 'Valori', 'valores': 'valori',
    'Unidad': 'Unità', 'unidad': 'unità',
    'Unidades': 'Unità', 'unidades': 'unità',
    'Medida': 'Misura', 'medida': 'misura',
    'Medidas': 'Misure', 'medidas': 'misure',
    'Dato': 'Dato', 'dato': 'dato',
    'Datos': 'Dati', 'datos': 'dati',
    'Tabla': 'Tabella', 'tabla': 'tabella',
    'Precio': 'Prezzo', 'precio': 'prezzo',
    'Coste': 'Costo', 'coste': 'costo',
    'Costes': 'Costi', 'costes': 'costi',
    'Gasto': 'Spesa', 'gasto': 'spesa',
    'Consumo': 'Consumo', 'consumo': 'consumo',
    'Ahorro': 'Risparmio', 'ahorro': 'risparmio',
    'Tiempo': 'Tempo', 'tiempo': 'tempo',
    'Fecha': 'Data', 'fecha': 'data',
    'Número': 'Numero', 'número': 'numero',
    'Cantidad': 'Quantità', 'cantidad': 'quantità',
    'Superficie': 'Superficie', 'superficie': 'superficie',
    'Área': 'Area', 'área': 'area',
    'Volumen': 'Volume', 'volumen': 'volume',
    'Longitud': 'Lunghezza', 'longitud': 'lunghezza',
    'Anchura': 'Larghezza', 'anchura': 'larghezza',
    'Ancho': 'Larghezza', 'ancho': 'larghezza',
    'Alto': 'Altezza', 'alto': 'altezza',
    'Altura': 'Altezza', 'altura': 'altezza',
    'Profundidad': 'Profondità', 'profundidad': 'profondità',
    'Diámetro': 'Diametro', 'diámetro': 'diametro',
    'Radio': 'Raggio', 'radio': 'raggio',
    'Perímetro': 'Perimetro', 'perímetro': 'perimetro',
    'Peso': 'Peso', 'peso': 'peso',
    'Masa': 'Massa', 'masa': 'massa',
    'Densidad': 'Densità', 'densidad': 'densità',
    'Temperatura': 'Temperatura', 'temperatura': 'temperatura',
    'Presión': 'Pressione', 'presión': 'pressione',
    'Potencia': 'Potenza', 'potencia': 'potenza',
    'Energía': 'Energia', 'energía': 'energia',
    'Tensión': 'Tensione', 'tensión': 'tensione',
    'Voltaje': 'Tensione', 'voltaje': 'tensione',
    'Corriente': 'Corrente', 'corriente': 'corrente',
    'Resistencia': 'Resistenza', 'resistencia': 'resistenza',
    'Capacidad': 'Capacità', 'capacidad': 'capacità',
    'Carga': 'Carico', 'carga': 'carico',
    'Descarga': 'Scarica', 'descarga': 'scarica',
    'Velocidad': 'Velocità', 'velocidad': 'velocità',
    'Aceleración': 'Accelerazione', 'aceleración': 'accelerazione',
    'Fuerza': 'Forza', 'fuerza': 'forza',
    'Trabajo': 'Lavoro', 'trabajo': 'lavoro',
    'Rendimiento': 'Rendimento', 'rendimiento': 'rendimento',
    'Eficiencia': 'Efficienza', 'eficiencia': 'efficienza',
    'Angulo': 'Angolo', 'angulo': 'angolo',
    'Ángulo': 'Angolo', 'ángulo': 'angolo',
    'Grados': 'Gradi', 'grados': 'gradi',
    'Radianes': 'Radianti', 'radianes': 'radianti',
    'Porcentaje': 'Percentuale', 'porcentaje': 'percentuale',
    'Tasa': 'Tasso', 'tasa': 'tasso',
    'Interés': 'Interesse', 'interés': 'interesse',
    'Plazo': 'Termine', 'plazo': 'termine',
    'Cuota': 'Rata', 'cuota': 'rata',
    'Préstamo': 'Prestito', 'préstamo': 'prestito',
    'Hipoteca': 'Mutuo', 'hipoteca': 'mutuo',
    'Salario': 'Stipendio', 'salario': 'stipendio',
    'Ingreso': 'Reddito', 'ingreso': 'reddito',
    'Beneficio': 'Profitto', 'beneficio': 'profitto',
    'Pérdida': 'Perdita', 'pérdida': 'perdita',
    'Ganancia': 'Guadagno', 'ganancia': 'guadagno',
    'Material': 'Materiale', 'material': 'materiale',
    'Materiales': 'Materiali', 'materiales': 'materiali',
    'Herramienta': 'Strumento', 'herramienta': 'strumento',
    'Máquina': 'Macchina', 'máquina': 'macchina',
    'Equipo': 'Apparecchiatura', 'equipo': 'apparecchiatura',
    'Instalación': 'Installazione', 'instalación': 'installazione',
    'Construcción': 'Costruzione', 'construcción': 'costruzione',
    'Edificación': 'Edificio', 'edificación': 'edificio',
    'Vivienda': 'Abitazione', 'vivienda': 'abitazione',
    'Habitación': 'Stanza', 'habitación': 'stanza',
    'Cocina': 'Cucina', 'cocina': 'cucina',
    'Baño': 'Bagno', 'baño': 'bagno',
    'Suelo': 'Pavimento', 'suelo': 'pavimento',
    'Pared': 'Parete', 'pared': 'parete',
    'Techo': 'Soffitto', 'techo': 'soffitto',
    'Ventana': 'Finestra', 'ventana': 'finestra',
    'Puerta': 'Porta', 'puerta': 'porta',
    'Escalera': 'Scala', 'escalera': 'scala',
    'Cimentación': 'Fondazione', 'cimentación': 'fondazione',
    'Estructura': 'Struttura', 'estructura': 'struttura',
    'Cubierta': 'Copertura', 'cubierta': 'copertura',
    'Fachada': 'Facciata', 'fachada': 'facciata',
    'Tabique': 'Tramezzo', 'tabique': 'tramezzo',
    'Ladrillo': 'Mattone', 'ladrillo': 'mattone',
    'Bloque': 'Blocco', 'bloque': 'blocco',
    'Hormigón': 'Calcestruzzo', 'hormigón': 'calcestruzzo',
    'Concreto': 'Calcestruzzo', 'concreto': 'calcestruzzo',
    'Mortero': 'Malta', 'mortero': 'malta',
    'Yeso': 'Gesso', 'yeso': 'gesso',
    'Cal': 'Calce', 'cal': 'calce',
    'Arena': 'Sabbia', 'arena': 'sabbia',
    'Grava': 'Ghiaia', 'grava': 'ghiaia',
    'Piedra': 'Pietra', 'piedra': 'pietra',
    'Madera': 'Legno', 'madera': 'legno',
    'Acero': 'Acciaio', 'acero': 'acciaio',
    'Hierro': 'Ferro', 'hierro': 'ferro',
    'Aluminio': 'Alluminio', 'aluminio': 'alluminio',
    'Cobre': 'Rame', 'cobre': 'rame',
    'Vidrio': 'Vetro', 'vidrio': 'vetro',
    'Cerámica': 'Ceramica', 'cerámica': 'ceramica',
    'Plástico': 'Plastica', 'plástico': 'plastica',
    'Pintura': 'Vernice', 'pintura': 'vernice',
    'Barniz': 'Vernice', 'barniz': 'vernice',
    'Adhesivo': 'Adesivo', 'adhesivo': 'adesivo',
    'Sellador': 'Sigillante', 'sellador': 'sigillante',
    'Aislante': 'Isolante', 'aislante': 'isolante',
    'Tubería': 'Tubazione', 'tubería': 'tubazione',
    'Cable': 'Cavo', 'cable': 'cavo',
    'Conductor': 'Conduttore', 'conductor': 'conduttore',
    'Circuito': 'Circuito', 'circuito': 'circuito',
    'Interruptor': 'Interruttore', 'interruptor': 'interruttore',
    'Enchufe': 'Presa', 'enchufe': 'presa',
    'Luminaria': 'Illuminazione', 'luminaria': 'illuminazione',
    'Calefacción': 'Riscaldamento', 'calefacción': 'riscaldamento',
    'Refrigeración': 'Raffreddamento', 'refrigeración': 'raffreddamento',
    'Ventilación': 'Ventilazione', 'ventilación': 'ventilazione',
    'Fontanería': 'Idraulica', 'fontanería': 'idraulica',
    'Electricidad': 'Elettricità', 'electricidad': 'elettricità',
    'Gas': 'Gas', 'gas': 'gas',
    'Agua': 'Acqua', 'agua': 'acqua',
    'Aire': 'Aria', 'aire': 'aria',
    'Combustible': 'Carburante', 'combustible': 'carburante',
    'Iluminación': 'Illuminazione', 'iluminación': 'illuminazione',
    'Sonido': 'Suono', 'sonido': 'suono',
    'Ruido': 'Rumore', 'ruido': 'rumore',

    # Prepositions / particles
    'por valor entre': 'Inserire un valore',
    'Por valor entre': 'Inserire un valore',
    'Medida típica': 'Misura tipica',
    'medida típica': 'misura tipica',

    # Adjectives
    'necesario': 'necessario', 'Necesario': 'Necessario',
    'necesaria': 'necessaria', 'Necesaria': 'Necessaria',
    'necesarios': 'necessari', 'Necesarios': 'Necessari',
    'necesarias': 'necessarie', 'Necesarias': 'Necessarie',
    'requerido': 'richiesto', 'Requerido': 'Richiesto',
    'requerida': 'richiesta', 'Requerida': 'Richiesta',
    'disponible': 'disponibile', 'Disponible': 'Disponibile',
    'máximo': 'massimo', 'Máximo': 'Massimo',
    'mínimo': 'minimo', 'Mínimo': 'Minimo',
    'total': 'totale', 'Total': 'Totale',
    'parcial': 'parziale', 'Parcial': 'Parziale',
    'aproximado': 'approssimativo', 'Aproximado': 'Approssimativo',
    'exacto': 'esatto', 'Exacto': 'Esatto',
    'recomendado': 'raccomandato', 'Recomendado': 'Raccomandato',
    'sugerido': 'suggerito', 'Sugerido': 'Suggerito',
    'estimado': 'stimato', 'Estimado': 'Stimato',
    'calculado': 'calcolato', 'Calculado': 'Calcolato',
    'gratuito': 'gratuito', 'Gratuito': 'Gratuito',
    'gratuita': 'gratuita', 'Gratuita': 'Gratuita',
    'gratis': 'gratis', 'Gratis': 'Gratis',
    'fácil': 'facile', 'Fácil': 'Facile',
    'rápido': 'veloce', 'Rápido': 'Veloce',
    'preciso': 'preciso', 'Preciso': 'Preciso',
    'precisa': 'precisa', 'Precisa': 'Precisa',
    'completo': 'completo', 'Completo': 'Completo',
    'detallado': 'dettagliato', 'Detallado': 'Dettagliato',
    'básico': 'di base', 'Básico': 'Di base',
    'avanzado': 'avanzato', 'Avanzado': 'Avanzato',
    'profesional': 'professionale', 'Profesional': 'Professionale',
    'técnico': 'tecnico', 'Técnico': 'Tecnico',
    'industrial': 'industriale', 'Industrial': 'Industriale',
    'doméstico': 'domestico', 'Doméstico': 'Domestico',
    'residencial': 'residenziale', 'Residencial': 'Residenziale',
    'comercial': 'commerciale', 'Comercial': 'Commerciale',
    'eléctrico': 'elettrico', 'Eléctrico': 'Elettrico',
    'eléctrica': 'elettrica', 'Eléctrica': 'Elettrica',
    'térmico': 'termico', 'Térmico': 'Termico',
    'térmica': 'termica', 'Térmica': 'Termica',
    'mecánico': 'meccanico', 'Mecánico': 'Meccanico',
    'hidráulico': 'idraulico', 'Hidráulico': 'Idraulico',
    'cuadrado': 'quadrato', 'Cuadrado': 'Quadrato',
    'cuadrada': 'quadrata', 'Cuadrada': 'Quadrata',
    'cuadrados': 'quadrati', 'Cuadrados': 'Quadrati',
    'cúbico': 'cubico', 'Cúbico': 'Cubico',
    'lineal': 'lineare', 'Lineal': 'Lineare',
    'unitario': 'unitario', 'Unitario': 'Unitario',
}

# Common suffix translations (order matters for longest-match)
PHRASE_FIXES = [
    # "unita de" → "unità di"
    (re.compile(r'\bunita de\b', re.IGNORECASE), 'unità di'),
    (re.compile(r'\bUnita De\b'), 'Unità Di'),
    (re.compile(r'\bUnita de\b'), 'Unità di'),
    (re.compile(r'\bunita di\b', re.IGNORECASE), 'unità di'),

    # "calcolato de" → "calcolato di"
    (re.compile(r'\bcalcolato de\b', re.IGNORECASE), 'calcolato di'),
    (re.compile(r'\bCalcolato de\b'), 'Calcolato di'),

    # "calcolare de" → "calcolare di"
    (re.compile(r'\bcalcolare de\b', re.IGNORECASE), 'calcolare di'),
    (re.compile(r'\bCalcolare de\b'), 'Calcolare di'),

    # "en m²" → "in m²" (Spanish preposition in Italian text)
    (re.compile(r'\ben m²\b'), 'in m²'),
    (re.compile(r'\ben m³\b'), 'in m³'),
    (re.compile(r'\ben m\b'), 'in m'),
    (re.compile(r'\ben kg\b'), 'in kg'),
    (re.compile(r'\ben tutte\b'), 'in tutte'),
    (re.compile(r'\ben cm\b'), 'in cm'),
    (re.compile(r'\ben mm\b'), 'in mm'),
    (re.compile(r'\ben litro'), 'in litro'),
    (re.compile(r'\ben MB\b'), 'in MB'),
    (re.compile(r'\ben GB\b'), 'in GB'),
    (re.compile(r'\ben W\b'), 'in W'),
    (re.compile(r'\ben kW\b'), 'in kW'),
    (re.compile(r'\ben kWh\b'), 'in kWh'),

    # "de m²" where should be "in m²" 
    # Actually "de" is often correct in Italian ("valore di m²"), but "en" is the Spanish problem

    # "resultado" → "risultato"
    (re.compile(r'\bresultado\b'), 'risultato'),
    (re.compile(r'\bResultado\b'), 'Risultato'),

    # "ejemplo" → "esempio"
    (re.compile(r'\bEjemplo\b'), 'Esempio'),
    (re.compile(r'\bejemplo\b'), 'esempio'),

    # "medida típica" → "misura tipica" 
    (re.compile(r'\bMedida típica\b'), 'Misura tipica'),
    (re.compile(r'\bmedida típica\b'), 'misura tipica'),

    # "por valor entre" → "Inserire un valore" (range_hints fix)
    (re.compile(r'\bpor valor entre\b', re.IGNORECASE), 'Inserire un valore'),

    # "el volume" → "il volume" 
    (re.compile(r'\bEl volume\b'), 'Il volume'),
    (re.compile(r'\bel volume\b'), 'il volume'),

    # "El area" → "L'area"
    (re.compile(r'\bEl area\b'), "L'area"),
    (re.compile(r'\bel area\b'), "l'area"),

    # "El resultado" → "Il risultato"
    (re.compile(r'\bEl risultato\b'), 'Il risultato'),
    (re.compile(r'\bel risultato\b'), 'il risultato'),

    # "El calcolo" → "Il calcolo"
    (re.compile(r'\bEl calcolo\b'), 'Il calcolo'),
    (re.compile(r'\bel calcolo\b'), 'il calcolo'),

    # "El consumo" → "Il consumo"
    (re.compile(r'\bEl consumo\b'), 'Il consumo'),
    (re.compile(r'\bel consumo\b'), 'il consumo'),

    # "El peso" → "Il peso"
    (re.compile(r'\bEl peso\b'), 'Il peso'),
    (re.compile(r'\bel peso\b'), 'il peso'),

    # "El valore" → "Il valore"
    (re.compile(r'\bEl valore\b'), 'Il valore'),
    (re.compile(r'\bel valore\b'), 'il valore'),

    # "La resultado" → "Il risultato"
    (re.compile(r'\bLa resultado\b'), 'Il risultato'),
    (re.compile(r'\bla resultado\b'), 'il risultato'),

    # "de la" in Italian should often be "della" 
    # (This is complex, don't blanket replace, handle specific patterns)

    # "en la" in Italian should be "nella"
    (re.compile(r'\ben la\b'), 'nella'),

    # "en el" → "nel"
    (re.compile(r'\ben el\b'), 'nel'),

    # "del la" → "della"
    (re.compile(r'\bdel la\b'), 'della'),

    # "de el" → "del"
    (re.compile(r'\bde el\b'), 'del'),

    # "No" (Spanish negation) → "Non" in Italian context
    # "No considerar" → "Non considerare"
    (re.compile(r'^No ([a-z])'), r'Non \1'),  # Sentence-start
    (re.compile(r'\. No ([a-z])'), r'. Non \1'),  # After period

    # "cálculo" → "calcolo"
    (re.compile(r'\bcálculo\b'), 'calcolo'),
    (re.compile(r'\bCálculo\b'), 'Calcolo'),

    # "cálculos" → "calcoli"
    (re.compile(r'\bcálculos\b'), 'calcoli'),
    (re.compile(r'\bCálculos\b'), 'Calcoli'),

    # "conversión" → "conversione"
    (re.compile(r'\bconversión\b'), 'conversione'),
    (re.compile(r'\bConversión\b'), 'Conversione'),

    # "selección" → "selezione"
    (re.compile(r'\bselección\b'), 'selezione'),
    (re.compile(r'\bSelección\b'), 'Selezione'),

    # accented chars that shouldn't be in Italian
    # Spanish á → Italian a (but only in non-Italian words)
    # Better to fix case by case
]

# ── Per-key fix functions ────────────────────────────────────────────────────

def fix_string(val, es_val=None):
    """Apply Spanish→Italian fixes to a string value."""
    if not isinstance(val, str):
        return val

    result = val

    # Apply regex phrase fixes
    for pattern, replacement in PHRASE_FIXES:
        result = pattern.sub(replacement, result)

    # Apply word-level fixes (longest first to avoid partial matches)
    # Sort by word length descending for proper ordering
    sorted_words = sorted(ES_TO_IT_WORDS.items(), key=lambda x: len(x[0]), reverse=True)
    
    fixed_parts = []
    # Use word boundary-aware replacement
    # Split by common boundaries but preserve structure
    for pattern_word, it_word in sorted_words:
        # Only replace if this specific Spanish word appears
        if pattern_word in result:
            # Create a regex that matches the exact word with boundaries
            # For Spanish accented words, match the accent exactly
            es_pattern = re.escape(pattern_word)
            regex = re.compile(r'(?<![a-zA-ZáéíóúüñÁÉÍÓÚÜÑ])' + es_pattern + r'(?![a-zA-ZáéíóúüñÁÉÍÓÚÜÑ])')
            if regex.search(result):
                result = regex.sub(it_word, result)

    return result


def translate_label(es_label, slug=''):
    """Translate a Spanish label to Italian using word mappings + context."""
    if not es_label or not isinstance(es_label, str):
        return es_label

    result = es_label

    # Special per-calculator translations that can't be done word-by-word
    # These are for common patterns across all calculators

    # "Calculadora de" → "Calcolatore di" (if masculine) or "Calcolatrice di" (fem)
    result = re.sub(r'^Calculadora de\b', 'Calcolatore di', result)
    result = re.sub(r'^Calculadora\b', 'Calcolatore', result)
    result = re.sub(r'^Convertidor\b', 'Convertitore', result)
    result = re.sub(r'^Conversor\b', 'Convertitore', result)
    result = re.sub(r'^Selector de\b', 'Selettore di', result)
    
    # Fix "Calcolatore di la" → "Calcolatore della"
    result = re.sub(r'Calcolatore di la\b', 'Calcolatore della', result)
    result = re.sub(r'Calcolatore di el\b', 'Calcolatore del', result)
    result = re.sub(r'Calcolatore di los\b', 'Calcolatore dei', result)
    result = re.sub(r'Calcolatore di las\b', 'Calcolatore delle', result)
    
    # Apply general word-level fixes
    result = fix_string(result)
    
    # Additional Italian-specific cleanups
    result = re.sub(r'\bGratuita\b', 'Gratuito', result)  # Italian calcolatore is masculine
    result = re.sub(r'\bgratuita\b', 'gratuito', result)
    
    # "Usato da" is fine for Italian, but "Utilizzato da" is more formal
    # "Usado por" → "Usato da"
    result = re.sub(r'\bUsado por\b', 'Usato da', result)
    result = re.sub(r'\busado por\b', 'usato da', result)

    return result


def fix_range_hints(rh, es_rh):
    """Fix range_hints: replace Spanish patterns with Italian."""
    if not isinstance(rh, dict):
        return rh
    
    result = {}
    for k, v in rh.items():
        if isinstance(v, str):
            # Replace Spanish patterns
            v = fix_string(v)
            # "Geben Sie einen Wert ein" (German leftovers) → "Inserire un valore"
            if 'Geben Sie' in v:
                v = 'Inserire un valore'
            # "por valor entre" pattern → "Inserire un valore" or keep original content
            v = re.sub(r'(?i)por valor entre\s*\d.*$', 'Inserire un valore', v)
            v = re.sub(r'(?i)Valore intre', 'Valore tra', v)
            result[k] = v
        else:
            result[k] = v
    return result


def fix_example_label(label, es_label=None):
    """Fix example_label to start with Calcolare... and use proper Italian."""
    if not isinstance(label, str):
        return label
    
    result = fix_string(label)
    
    # Fix Spanish-start labels
    # "Ejemplo di calcolo" → "Esempio di calcolo"
    result = re.sub(r'^Ejemplo di\b', 'Esempio di', result)
    result = re.sub(r'^Esempio de\b', 'Esempio di', result)
    result = re.sub(r'^Ejemplo de\b', 'Esempio di', result)
    
    # Fix "Estimar" → "Calcolare" or "Stimare"
    result = re.sub(r'^Estimar\b', 'Calcolare', result)
    
    # Fix "Calculate" (English leftover) → "Calcolare"
    result = re.sub(r'^Calculate\b', 'Calcolare', result)
    
    # Fix "Berechnen" (German leftover) → "Calcolare"  
    if result.startswith('Berechnen') or result.startswith('berechnen'):
        result = 'Calcolare' + result[9:] if len(result) > 9 else 'Calcolare'
    
    # Fix "Berechnet" → "Calcolare"
    result = re.sub(r'^Berechnet\b', 'Calcolare', result)
    result = re.sub(r'^berechnet\b', 'calcolare', result)
    
    # "de" → "di" in certain contexts
    result = re.sub(r'\bde (la|il|lo|l\'|i|gli|le)\b', r'di \1', result)
    
    return result


def fix_result_context(rc):
    """Fix result_context: remove Spanish/English mixed text."""
    if not isinstance(rc, str):
        return rc
    
    result = fix_string(rc)
    return result


def fix_steps(steps):
    """Fix steps: translate Spanish verb patterns to Italian."""
    if not isinstance(steps, list):
        return steps
    
    result = []
    for step in steps:
        if isinstance(step, str):
            s = fix_string(step)
            s = fix_step_verbs(s)
            result.append(s)
        else:
            result.append(step)
    return result


def fix_step_verbs(text):
    """Fix common step verb patterns from Spanish to Italian."""
    # "Ingresar" → "Inserire" (infinitive for impersonal)
    # "Ingresa" → "Inserisci" (imperative)
    # "Introduce" → "Inserisci"
    # "Introducir" → "Inserire"
    # Already handled by fix_string mostly, but catch edge cases
    
    # "Multiplicar" → "Moltiplicare" 
    text = re.sub(r'\bMultiplicar\b', 'Moltiplicare', text)
    text = re.sub(r'\bmultiplicar\b', 'moltiplicare', text)
    
    # "Sumar" → "Sommare"
    text = re.sub(r'\bSumar\b', 'Sommare', text)
    text = re.sub(r'\bsumar\b', 'sommare', text)
    
    # "Dividir" → "Dividere"  
    text = re.sub(r'\bDividir\b', 'Dividere', text)
    text = re.sub(r'\bdividir\b', 'dividere', text)
    
    # "Restar" → "Sottrarre"
    text = re.sub(r'\bRestar\b', 'Sottrarre', text)
    text = re.sub(r'\brestar\b', 'sottrarre', text)
    
    # Para → Per (Spanish "para" → Italian "per")
    text = re.sub(r'\bpara\b', 'per', text)
    text = re.sub(r'\bPara\b', 'Per', text)
    
    # "Convierte" → "Converti"
    text = re.sub(r'\bConvierte\b', 'Converti', text)
    text = re.sub(r'\bconvierte\b', 'converti', text)
    
    # "Convierte a" → "Converti in" 
    text = re.sub(r'\bConverti a\b', 'Converti in', text)
    
    # "y" → "e" (Spanish conjunction to Italian, but only standalone)
    # Actually "y" is rare in Italian text, but "e" is correct
    
    return text


def fix_mistakes(mistakes):
    """Fix mistake strings."""
    if not isinstance(mistakes, list):
        return mistakes
    
    result = []
    for m in mistakes:
        if isinstance(m, str):
            m = fix_string(m)
            # Fix "No" → "Non" for sentence-start negation
            m = re.sub(r'^No\b', 'Non', m)
            m = re.sub(r'\.\s*No\b', '. Non', m)
            result.append(m)
        else:
            result.append(m)
    return result


def fix_formula_display(fd):
    """Fix formula_display Spanish terms."""
    if not isinstance(fd, str):
        return fd
    return fix_string(fd)


def fix_seo_description(desc, max_len=160):
    """Fix seo_description and trim to ≤160 chars."""
    if not isinstance(desc, str):
        return desc
    
    result = fix_string(desc)
    if len(result) > max_len:
        result = result[:max_len-3].rstrip() + '...'
    return result


def load_json(filepath):
    """Load a JSON file with utf-8 encoding."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(filepath, data):
    """Save JSON with ensure_ascii=False, indent=2, and trailing newline."""
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def fix_calculator(filepath):
    """Fix Italian section in a single calculator JSON. Returns True if modified."""
    try:
        data = load_json(filepath)
    except Exception as e:
        print(f"  ERROR loading {filepath}: {e}")
        return False

    i18n = data.get('i18n')
    if not i18n:
        return False

    es = i18n.get('es', {})
    it = i18n.get('it', {})
    
    if not it:
        return False

    modified = False

    # ── Fix basic string fields ──────────────────────────────────────────
    string_keys = ['name', 'desc', 'description', 'seo_title', 'seo_description']
    for key in string_keys:
        if key in it and isinstance(it[key], str):
            old = it[key]
            if key == 'seo_description':
                new = fix_seo_description(old)
            else:
                new = translate_label(old)
            if new != old:
                it[key] = new
                modified = True

    # ── Fix example_label ────────────────────────────────────────────────
    if 'example_label' in it:
        old = it['example_label']
        es_label = es.get('example_label', '') if es else ''
        new = fix_example_label(old, es_label)
        if new != old:
            it['example_label'] = new
            modified = True
    elif es and 'example_label' in es:
        it['example_label'] = translate_label(es['example_label'])
        modified = True

    # ── Fix range_hints ──────────────────────────────────────────────────
    if 'range_hints' in it:
        old_rh = it['range_hints']
        es_rh = es.get('range_hints', {}) if es else {}
        if isinstance(old_rh, dict):
            new_rh = fix_range_hints(old_rh, es_rh)
            if new_rh != old_rh:
                it['range_hints'] = new_rh
                modified = True
    elif es and 'range_hints' in es:
        # Copy from Spanish and translate values
        new_rh = {}
        for k, v in es['range_hints'].items():
            if isinstance(v, str):
                new_rh[k] = translate_label(v)
            else:
                new_rh[k] = v
        it['range_hints'] = new_rh
        modified = True

    # ── Fix result_context ───────────────────────────────────────────────
    if 'result_context' in it:
        old = it['result_context']
        new = fix_result_context(old)
        if new != old:
            it['result_context'] = new
            modified = True
    elif es and 'result_context' in es:
        it['result_context'] = translate_label(es['result_context'])
        modified = True

    # ── Fix steps ────────────────────────────────────────────────────────
    if 'steps' in it:
        old = it['steps']
        new = fix_steps(old)
        if new != old:
            it['steps'] = new
            modified = True
    elif es and 'steps' in es:
        it['steps'] = fix_steps([translate_label(s) for s in es['steps']])
        modified = True

    # ── Fix mistakes ─────────────────────────────────────────────────────
    if 'mistakes' in it:
        old = it['mistakes']
        new = fix_mistakes(old)
        if new != old:
            it['mistakes'] = new
            modified = True
    elif es and 'mistakes' in es:
        it['mistakes'] = fix_mistakes([translate_label(m) for m in es['mistakes']])
        modified = True

    # ── Fix formula_display ──────────────────────────────────────────────
    if 'formula_display' in it:
        old = it['formula_display']
        new = fix_formula_display(old)
        if new != old:
            it['formula_display'] = new
            modified = True
    elif es and 'formula_display' in es:
        it['formula_display'] = translate_label(es['formula_display'])
        modified = True

    # ── Fix inputs ───────────────────────────────────────────────────────
    # If Italian inputs have wrong keys (mismatched with Spanish),
    # replace them with translations from Spanish
    es_inputs = es.get('inputs', {}) if es else {}
    it_inputs = it.get('inputs', {}) if 'inputs' in it else {}
    
    # Detect if Italian inputs are for a completely different calculator
    # by checking if the keys match the Spanish keys
    if es_inputs:
        es_input_keys = set(es_inputs.keys())
        it_input_keys = set(it_inputs.keys()) if it_inputs else set()
        
        # If Italian has different keys than Spanish, it's likely wrong
        if it_input_keys and not it_input_keys.intersection(es_input_keys):
            # Completely different calculator's inputs - replace
            new_inputs = {}
            for k, v in es_inputs.items():
                new_inputs[k] = translate_label(v)
            it['inputs'] = new_inputs
            modified = True
        elif it_input_keys and es_input_keys - it_input_keys:
            # Missing some keys - add them
            for k in es_input_keys - it_input_keys:
                it['inputs'][k] = translate_label(es_inputs[k])
            modified = True
        elif not it_inputs:
            # No inputs at all - copy from Spanish
            new_inputs = {}
            for k, v in es_inputs.items():
                new_inputs[k] = translate_label(v)
            it['inputs'] = new_inputs
            modified = True
    
    # Also fix values of existing inputs that match Spanish keys
    if 'inputs' in it and es_inputs:
        for k, v in it['inputs'].items():
            if isinstance(v, str):
                old = v
                new = fix_string(v)
                if new != old:
                    it['inputs'][k] = new
                    modified = True

    # ── Fix outputs ──────────────────────────────────────────────────────
    es_outputs = es.get('outputs', {}) if es else {}
    it_outputs = it.get('outputs', {}) if 'outputs' in it else {}
    
    if es_outputs:
        es_output_keys = set(es_outputs.keys())
        it_output_keys = set(it_outputs.keys()) if it_outputs else set()
        
        # If Italian has completely different keys, replace
        if it_output_keys and not it_output_keys.intersection(es_output_keys):
            new_outputs = {}
            for k, v in es_outputs.items():
                new_outputs[k] = translate_label(v)
            it['outputs'] = new_outputs
            modified = True
        elif it_output_keys and es_output_keys - it_output_keys:
            for k in es_output_keys - it_output_keys:
                it['outputs'][k] = translate_label(es_outputs[k])
            modified = True
        elif not it_outputs:
            new_outputs = {}
            for k, v in es_outputs.items():
                new_outputs[k] = translate_label(v)
            it['outputs'] = new_outputs
            modified = True
    
    # Fix values of existing outputs
    if 'outputs' in it and es_outputs:
        for k, v in it['outputs'].items():
            if isinstance(v, str):
                old = v
                new = fix_string(v)
                if new != old:
                    it['outputs'][k] = new
                    modified = True

    return modified


def main():
    files = sorted(glob.glob(os.path.join(WORKDIR, '*.json')))
    total = len(files)
    fixed_count = 0
    error_count = 0
    
    for i, filepath in enumerate(files):
        try:
            was_modified = fix_calculator(filepath)
            if was_modified:
                # Re-read to save
                data = load_json(filepath)
                # Check if Italian section was updated during fix
                save_json(filepath, data)
                fixed_count += 1
                name = os.path.basename(filepath)
                if fixed_count <= 20 or fixed_count % 50 == 0:
                    print(f"  [{i+1}/{total}] FIXED: {name}")
        except Exception as e:
            error_count += 1
            print(f"  [{i+1}/{total}] ERROR: {os.path.basename(filepath)}: {e}")

    print(f"\n=== RESULTS ===")
    print(f"Total files processed: {total}")
    print(f"Files fixed: {fixed_count}")
    print(f"Errors: {error_count}")
    return fixed_count


if __name__ == '__main__':
    count = main()
    print(f"\nFixed {count} calculator JSON files.")
    sys.exit(0 if count >= 0 else 1)

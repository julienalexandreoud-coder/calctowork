import json, glob, os, re

CALC_DIR = r'C:\Microsaas\obra\src\calculators'

def clean_spanish(text, lang):
    """Replace Spanish words in non-Spanish target language text with proper translations."""
    if not text:
        return text
    
    # These replacements are done carefully - only for clear Spanish words
    # that don't exist in the target language
    
    if lang == 'en':
        replacements = [
            ('cálculo', 'calculation'), ('Cálculo', 'Calculation'),
            ('calcular', 'calculate'), ('Calcular', 'Calculate'),
            ('calculadora', 'calculator'), ('Calculadora', 'Calculator'),
            ('resultado', 'result'), ('Resultado', 'Result'),
            ('valor', 'value'), ('valores', 'values'),
            ('dimensión', 'dimension'), ('dimensionar', 'size'),
            ('Dimensionar', 'Size'), ('potencia', 'power'),
            ('Potencia', 'Power'), ('consumo', 'consumption'),
            ('Consumo', 'Consumption'), ('rendimiento', 'performance'),
            ('espesor', 'thickness'), ('Espesor', 'Thickness'),
            ('superficie', 'surface'), ('Superficie', 'Surface'),
            ('volumen', 'volume'), ('Volumen', 'Volume'),
            ('altura', 'height'), ('Altura', 'Height'),
            ('longitud', 'length'), ('Longitud', 'Length'),
            ('ancho', 'width'), ('Ancho', 'Width'),
            ('hormigón', 'concrete'), ('Hormigón', 'Concrete'),
            ('mortero', 'mortar'), ('Mortero', 'Mortar'),
            ('ladrillo', 'brick'), ('ladrillos', 'bricks'),
            ('Ladrillos', 'Bricks'), ('acero', 'steel'),
            ('Acero', 'Steel'), ('encofrado', 'formwork'),
            ('Encofrado', 'Formwork'), ('pilares', 'pillars'),
            ('viga', 'beam'), ('vigas', 'beams'),
            ('zapata', 'footing'), ('losa', 'slab'),
            ('cimentación', 'foundation'), ('tubería', 'pipe'),
            ('tuberia', 'pipe'), ('Tubería', 'Pipe'),
            ('caudal', 'flow rate'), ('Caudal', 'Flow rate'),
            ('diámetro', 'diameter'), ('Diámetro', 'Diameter'),
            ('presión', 'pressure'), ('Presión', 'Pressure'),
            ('tensión', 'voltage'), ('Tensión', 'Voltage'),
            ('eficiencia', 'efficiency'), ('Eficiencia', 'Efficiency'),
            ('máxima', 'maximum'), ('máximo', 'maximum'),
            ('mínima', 'minimum'), ('mínimo', 'minimum'),
            ('catálogo', 'catalog'), ('ensayo', 'test'),
            ('carga', 'load'), ('Carga', 'Load'),
            ('estacional', 'seasonal'), ('nominal', 'nominal'),
            ('vivienda', 'home'), ('instalación', 'installation'),
            ('Instalación', 'Installation'),
            ('calefacción', 'heating'), ('refrigeración', 'cooling'),
            ('cerámico', 'ceramic'), ('cerámica', 'ceramic'),
            ('azulejo', 'tile'), ('mosaico', 'mosaic'),
            ('pared', 'wall'), ('suelo', 'floor'),
            ('techo', 'ceiling'), ('ventana', 'window'),
            ('puerta', 'door'), ('depósito', 'tank'),
            ('caldera', 'boiler'), ('radiador', 'radiator'),
            ('aislamiento', 'insulation'), ('Aislamiento', 'Insulation'),
            ('luminaria', 'light fixture'), ('luminarias', 'light fixtures'),
            ('Luminarias', 'Light fixtures'), ('lúmenes', 'lumens'),
            ('lumenes', 'lumens'), ('Lumenes', 'Lumens'),
            ('batería', 'battery'), ('baterías', 'batteries'),
            ('Baterías', 'Batteries'), ('autonomía', 'autonomy'),
            ('autonomia', 'autonomy'), ('cantidad', 'quantity'),
            ('Cantidad', 'Quantity'), ('masa', 'mass'),
            ('Masa', 'Mass'), ('peso', 'weight'),
            ('Peso', 'Weight'), ('trifásica', 'three-phase'),
            ('trifásico', 'three-phase'), ('Trifásica', 'Three-phase'),
            ('monofásica', 'single-phase'), ('monofásico', 'single-phase'),
            ('aparente', 'apparent'), ('activa', 'active'),
            ('reactiva', 'reactive'), ('Potencia', 'Power'),
            ('frecuencia', 'frequency'), ('fase', 'phase'),
            ('neutro', 'neutral'), ('tierra', 'ground'),
            ('protección', 'protection'), ('sección', 'cross-section'),
            ('cable', 'cable'), ('Cable', 'Cable'),
            ('puesta a tierra', 'grounding'), ('circuito', 'circuit'),
            ('Circuito', 'Circuit'), ('interruptor', 'breaker'),
            ('Interruptor', 'Breaker'), ('cuadro', 'panel'),
            ('eléctrico', 'electrical'), ('eléctrica', 'electrical'),
            ('térmica', 'thermal'), ('térmico', 'thermal'),
            ('consumo eléctrico', 'power consumption'),
            ('consumo electrico', 'power consumption'),
            ('potencia eléctrica', 'electrical power'),
            ('potencia electrica', 'electrical power'),
            ('energía', 'energy'), ('energia', 'energy'),
            ('solar', 'solar'), ('Solar', 'Solar'),
            ('placa', 'panel'), ('panel solar', 'solar panel'),
            ('temperatura', 'temperature'), ('Temperatura', 'Temperature'),
            ('agua', 'water'), ('Agua', 'Water'),
            ('caliente', 'hot'), ('fría', 'cold'),
            ('calor', 'heat'), ('frío', 'cooling'),
            ('calentador', 'water heater'), ('Calentador', 'Water heater'),
            ('piscina', 'pool'), ('depuradora', 'filter'),
            ('riego', 'irrigation'), ('goteo', 'drip'),
            ('sifón', 'trap'), ('sumidero', 'drain'),
            ('Sifón', 'Trap'), ('Sumidero', 'Drain'),
            ('desagüe', 'drainage'), ('ventilación', 'ventilation'),
            ('Ventilación', 'Ventilation'), ('mecánica', 'mechanical'),
            ('conducto', 'duct'), ('conductos', 'ducts'),
            ('aire acondicionado', 'air conditioning'),
            ('Aire acondicionado', 'Air conditioning'),
            ('bomba de calor', 'heat pump'), ('Bomba de calor', 'Heat pump'),
            ('aerotermia', 'aerothermal'), ('climatización', 'climate control'),
            ('gas refrigerante', 'refrigerant gas'), ('carga térmica', 'thermal load'),
            ('carga termica', 'thermal load'), ('rejilla', 'grille'),
            ('difusor', 'diffuser'), ('caudal de aire', 'airflow'),
            ('cambio porcentual', 'percentage change'),
            ('porcentaje', 'percentage'), ('Porcentaje', 'Percentage'),
            ('aumento', 'increase'), ('disminución', 'decrease'),
            ('Amortización', 'Amortization'), ('amortización', 'amortization'),
            ('préstamo', 'loan'), ('vehículo', 'vehicle'),
            ('maquinaria', 'machinery'), ('interés', 'interest'),
            ('cuota', 'payment'), ('mensual', 'monthly'),
            ('anual', 'annual'), ('total', 'total'),
            ('combinación', 'combination'), ('combinaciones', 'combinations'),
            ('permutación', 'permutation'), ('permutaciones', 'permutations'),
            ('variación', 'variation'), ('coeficiente', 'coefficient'),
            ('desviación', 'deviation'), ('media', 'mean'),
            ('estándar', 'standard'), ('código', 'code'),
            ('colores', 'colors'), ('resistencia', 'resistance'),
            ('condensador', 'capacitor'), ('constante', 'constant'),
            ('tiempo', 'time'), ('resorte', 'spring'),
            ('dilatación', 'expansion'), ('dilución', 'dilution'),
            ('concentración', 'concentration'), ('solución', 'solution'),
            ('Concentración', 'Concentration'),
            ('frenado', 'braking'), ('distancia', 'distance'),
            ('velocidad', 'speed'), ('reacción', 'reaction'),
            ('factor de potencia', 'power factor'),
            ('potencia activa', 'active power'),
            ('potencia reactiva', 'reactive power'),
            ('potencia aparente', 'apparent power'),
            ('iluminación', 'lighting'), ('Iluminación', 'Lighting'),
            ('punto', 'point'), ('puntos', 'points'),
            ('luz', 'light'), ('habitación', 'room'),
            ('Habitación', 'Room'), ('enchufe', 'outlet'),
            ('Enchufe', 'Outlet'), ('toma', 'socket'),
        ]
    elif lang == 'fr':
        replacements = [
            ('cálculo', 'calcul'), ('Cálculo', 'Calcul'),
            ('calcular', 'calculer'), ('Calcular', 'Calculer'),
            ('calculadora', 'calculatrice'), ('Calculadora', 'Calculatrice'),
            ('resultado', 'résultat'), ('Resultado', 'Résultat'),
            ('valor', 'valeur'), ('valores', 'valeurs'),
            ('dimensión', 'dimension'), ('dimensionar', 'dimensionner'),
            ('Dimensionar', 'Dimensionner'), ('potencia', 'puissance'),
            ('Potencia', 'Puissance'), ('consumo', 'consommation'),
            ('Consumo', 'Consommation'), ('rendimiento', 'rendement'),
            ('espesor', 'épaisseur'), ('superficie', 'surface'),
            ('Superficie', 'Superficie'), ('volumen', 'volume'),
            ('altura', 'hauteur'), ('Altura', 'Hauteur'),
            ('longitud', 'longueur'), ('ancho', 'largeur'),
            ('hormigón', 'béton'), ('Hormigón', 'Béton'),
            ('hormigon', 'béton'), ('Hormigon', 'Béton'),
            ('mortero', 'mortier'), ('Mortero', 'Mortier'),
            ('ladrillo', 'brique'), ('ladrillos', 'briques'),
            ('Ladrillos', 'Briques'), ('acero', 'acier'),
            ('Acero', 'Acier'), ('encofrado', 'coffrage'),
            ('pilares', 'piliers'), ('viga', 'poutre'),
            ('vigas', 'poutres'), ('zapata', 'semelle'),
            ('cimentación', 'fondation'), ('tubería', 'tuyau'),
            ('tuberia', 'tuyau'), ('Tubería', 'Tuyau'),
            ('caudal', 'débit'), ('Caudal', 'Débit'),
            ('diámetro', 'diamètre'), ('Diámetro', 'Diamètre'),
            ('presión', 'pression'), ('Presión', 'Pression'),
            ('tensión', 'tension'), ('Tensión', 'Tension'),
            ('eficiencia', 'efficacité'), ('Eficiencia', 'Efficacité'),
            ('máxima', 'maximale'), ('máximo', 'maximal'),
            ('mínima', 'minimale'), ('mínimo', 'minimal'),
            ('estacional', 'saisonnier'), ('carga', 'charge'),
            ('Carga', 'Charge'), ('vivienda', 'logement'),
            ('instalación', 'installation'), ('Instalación', 'Installation'),
            ('calefacción', 'chauffage'), ('refrigeración', 'refroidissement'),
            ('cerámico', 'céramique'), ('azulejo', 'carrelage'),
            ('mosaico', 'mosaïque'), ('aislamiento', 'isolation'),
            ('batería', 'batterie'), ('baterías', 'batteries'),
            ('Baterías', 'Batteries'), ('autonomía', 'autonomie'),
            ('cantidad', 'quantité'), ('Cantidad', 'Quantité'),
            ('masa', 'masse'), ('peso', 'poids'),
            ('trifásica', 'triphasé'), ('trifásico', 'triphasé'),
            ('monofásica', 'monophasé'), ('aparente', 'apparente'),
            ('activa', 'active'), ('reactiva', 'réactive'),
            ('sección', 'section'), ('cable', 'câble'),
            ('puesta a tierra', 'mise à la terre'),
            ('eléctrico', 'électrique'), ('eléctrica', 'électrique'),
            ('electrico', 'électrique'), ('electrica', 'électrique'),
            ('térmica', 'thermique'), ('térmico', 'thermique'),
            ('termica', 'thermique'), ('termico', 'thermique'),
            ('energía', 'énergie'), ('solar', 'solaire'),
            ('temperatura', 'température'), ('Temperatura', 'Température'),
            ('agua', 'eau'), ('Agua', 'Eau'),
            ('calentador', 'chauffe-eau'), ('Calentador', 'Chauffe-eau'),
            ('piscina', 'piscine'), ('depuradora', 'filtre'),
            ('riego', 'irrigation'), ('sifón', 'siphon'),
            ('sumidero', 'avaloir'), ('desagüe', 'drainage'),
            ('ventilación', 'ventilation'), ('Ventilación', 'Ventilation'),
            ('mecánica', 'mécanique'), ('conducto', 'conduit'),
            ('conductos', 'conduits'), ('aire acondicionado', 'climatisation'),
            ('Aire acondicionado', 'Climatisation'),
            ('bomba de calor', 'pompe à chaleur'),
            ('aerotermia', 'aérothermie'), ('climatización', 'climatisation'),
            ('gas refrigerante', 'fluide frigorigène'),
            ('carga térmica', 'charge thermique'),
            ('porcentaje', 'pourcentage'), ('Porcentaje', 'Pourcentage'),
            ('amortización', 'amortissement'), ('Amortización', 'Amortissement'),
            ('préstamo', 'prêt'), ('vehículo', 'véhicule'),
            ('maquinaria', 'machinerie'), ('interés', 'intérêt'),
            ('mensual', 'mensuel'), ('anual', 'annuel'),
            ('combinación', 'combinaison'), ('combinaciones', 'combinaisons'),
            ('permutación', 'permutation'), ('coeficiente', 'coefficient'),
            ('desviación', 'écart'), ('media', 'moyenne'),
            ('estándar', 'standard'), ('código', 'code'),
            ('colores', 'couleurs'), ('resistencia', 'résistance'),
            ('constante', 'constante'), ('tiempo', 'temps'),
            ('dilatación', 'dilatation'), ('dilución', 'dilution'),
            ('dilucion', 'dilution'), ('concentración', 'concentration'),
            ('solución', 'solution'), ('distancia', 'distance'),
            ('frenado', 'freinage'), ('velocidad', 'vitesse'),
            ('cuota', 'mensualité'), ('caldera', 'chaudière'),
            ('radiador', 'radiateur'), ('suelo', 'sol'),
            ('pared', 'mur'), ('techo', 'plafond'),
            ('ventana', 'fenêtre'), ('puerta', 'porte'),
            ('depósito', 'réservoir'), ('aluminio', 'aluminium'),
            ('luminaria', 'luminaire'), ('luminarias', 'luminaires'),
            ('lúmenes', 'lumens'), ('lumenes', 'lumens'),
        ]
    elif lang == 'de':
        replacements = [
            ('cálculo', 'Berechnung'), ('Cálculo', 'Berechnung'),
            ('calcular', 'berechnen'), ('Calcular', 'Berechnen'),
            ('calculadora', 'Rechner'), ('Calculadora', 'Rechner'),
            ('resultado', 'Ergebnis'), ('Resultado', 'Ergebnis'),
            ('valor', 'Wert'), ('valores', 'Werte'),
            ('dimensión', 'Abmessung'), ('dimensionar', 'dimensionieren'),
            ('Dimensionar', 'Dimensionieren'), ('potencia', 'Leistung'),
            ('Potencia', 'Leistung'), ('consumo', 'Verbrauch'),
            ('Consumo', 'Verbrauch'), ('rendimiento', 'Leistung'),
            ('espesor', 'Dicke'), ('superficie', 'Fläche'),
            ('Superficie', 'Fläche'), ('volumen', 'Volumen'),
            ('altura', 'Höhe'), ('Altura', 'Höhe'),
            ('longitud', 'Länge'), ('ancho', 'Breite'),
            ('hormigón', 'Beton'), ('Hormigón', 'Beton'),
            ('hormigon', 'Beton'), ('mortero', 'Mörtel'),
            ('ladrillo', 'Ziegel'), ('ladrillos', 'Ziegel'),
            ('Ladrillos', 'Ziegel'), ('acero', 'Stahl'),
            ('Acero', 'Stahl'), ('encofrado', 'Schalung'),
            ('pilares', 'Stützen'), ('viga', 'Balken'),
            ('vigas', 'Balken'), ('zapata', 'Fundament'),
            ('cimentación', 'Fundament'), ('tubería', 'Rohr'),
            ('tuberia', 'Rohr'), ('Tubería', 'Rohr'),
            ('caudal', 'Durchfluss'), ('Caudal', 'Durchfluss'),
            ('diámetro', 'Durchmesser'), ('Diámetro', 'Durchmesser'),
            ('presión', 'Druck'), ('Presión', 'Druck'),
            ('presion', 'Druck'), ('tensión', 'Spannung'),
            ('Tensión', 'Spannung'), ('tension', 'Spannung'),
            ('eficiencia', 'Effizienz'), ('Eficiencia', 'Effizienz'),
            ('máxima', 'maximale'), ('máximo', 'maximal'),
            ('mínima', 'minimale'), ('mínimo', 'minimal'),
            ('carga', 'Last'), ('Carga', 'Last'),
            ('vivienda', 'Wohnung'), ('instalación', 'Installation'),
            ('eléctrico', 'elektrisch'), ('eléctrica', 'elektrisch'),
            ('electrico', 'elektrisch'), ('electrica', 'elektrisch'),
            ('térmica', 'thermisch'), ('térmico', 'thermisch'),
            ('termica', 'thermisch'), ('termico', 'thermisch'),
            ('energía', 'Energie'), ('energia', 'Energie'),
            ('solar', 'Solar'), ('Solar', 'Solar'),
            ('temperatura', 'Temperatur'), ('Temperatura', 'Temperatur'),
            ('agua', 'Wasser'), ('Agua', 'Wasser'),
            ('calentador', 'Warmwasserbereiter'),
            ('piscina', 'Pool'), ('depuradora', 'Filter'),
            ('riego', 'Bewässerung'), ('goteo', 'Tropf-'),
            ('sifón', 'Siphon'), ('sumidero', 'Ablauf'),
            ('desagüe', 'Abfluss'), ('ventilación', 'Lüftung'),
            ('Ventilación', 'Lüftung'), ('mecánica', 'mechanisch'),
            ('conducto', 'Kanal'), ('conductos', 'Kanäle'),
            ('cerámico', 'Keramik'), ('azulejo', 'Fliese'),
            ('mosaico', 'Mosaik'), ('aislamiento', 'Dämmung'),
            ('batería', 'Batterie'), ('baterías', 'Batterien'),
            ('Baterías', 'Batterien'), ('autonomía', 'Autonomie'),
            ('cantidad', 'Menge'), ('Cantidad', 'Menge'),
            ('masa', 'Masse'), ('peso', 'Gewicht'),
            ('trifásica', 'Drehstrom'), ('trifásico', 'Drehstrom'),
            ('monofásica', 'Einphasen-'), ('monofásico', 'Einphasen-'),
            ('aparente', 'Schein-'), ('activa', 'Wirk-'),
            ('reactiva', 'Blind-'), ('sección', 'Querschnitt'),
            ('seccion', 'Querschnitt'), ('cable', 'Kabel'),
            ('puesta a tierra', 'Erdung'), ('cuadro', 'Verteiler'),
            ('calefacción', 'Heizung'), ('refrigeración', 'Kühlung'),
            ('porcentaje', 'Prozentsatz'), ('Porcentaje', 'Prozentsatz'),
            ('amortización', 'Abschreibung'), ('Amortización', 'Abschreibung'),
            ('préstamo', 'Darlehen'), ('maquinaria', 'Maschinen'),
            ('combinación', 'Kombination'), ('combinaciones', 'Kombinationen'),
            ('permutación', 'Permutation'), ('coeficiente', 'Koeffizient'),
            ('desviación', 'Abweichung'), ('media', 'Mittelwert'),
            ('código', 'Code'), ('colores', 'Farben'),
            ('resistencia', 'Widerstand'), ('resorte', 'Feder'),
            ('constante', 'Konstante'), ('tiempo', 'Zeit'),
            ('dilatación', 'Ausdehnung'), ('dilución', 'Verdünnung'),
            ('concentración', 'Konzentration'), ('solución', 'Lösung'),
            ('distancia', 'Abstand'), ('frenado', 'Bremsen'),
            ('velocidad', 'Geschwindigkeit'), ('caldera', 'Heizkessel'),
            ('radiador', 'Heizkörper'), ('suelo', 'Boden'),
            ('pared', 'Wand'), ('techo', 'Decke'),
            ('ventana', 'Fenster'), ('puerta', 'Tür'),
            ('depósito', 'Tank'), ('aluminio', 'Aluminium'),
            ('luminaria', 'Leuchte'), ('luminarias', 'Leuchten'),
            ('lúmenes', 'Lumen'), ('lumenes', 'Lumen'),
            ('iluminación', 'Beleuchtung'),
        ]
    elif lang == 'it':
        replacements = [
            ('cálculo', 'calcolo'), ('Cálculo', 'Calcolo'),
            ('calcular', 'calcolare'), ('Calcular', 'Calcolare'),
            ('calculadora', 'calcolatore'), ('resultado', 'risultato'),
            ('Resultado', 'Risultato'), ('valor', 'valore'),
            ('valores', 'valori'), ('dimensión', 'dimensione'),
            ('dimensionar', 'dimensionare'), ('Dimensionar', 'Dimensionare'),
            ('potencia', 'potenza'), ('Potencia', 'Potenza'),
            ('consumo', 'consumo'), ('Consumo', 'Consumo'),
            ('rendimiento', 'rendimento'), ('espesor', 'spessore'),
            ('superficie', 'superficie'), ('volumen', 'volume'),
            ('altura', 'altezza'), ('Altura', 'Altezza'),
            ('longitud', 'lunghezza'), ('ancho', 'larghezza'),
            ('hormigón', 'calcestruzzo'), ('Hormigón', 'Calcestruzzo'),
            ('hormigon', 'calcestruzzo'), ('mortero', 'malta'),
            ('ladrillo', 'mattone'), ('ladrillos', 'mattoni'),
            ('Ladrillos', 'Mattoni'), ('acero', 'acciaio'),
            ('Acero', 'Acciaio'), ('encofrado', 'cassaforma'),
            ('pilares', 'pilastri'), ('viga', 'trave'),
            ('vigas', 'travi'), ('zapata', 'plinto'),
            ('cimentación', 'fondazione'), ('tubería', 'tubo'),
            ('tuberia', 'tubo'), ('Tubería', 'Tubo'),
            ('caudal', 'portata'), ('Caudal', 'Portata'),
            ('diámetro', 'diametro'), ('Diámetro', 'Diametro'),
            ('presión', 'pressione'), ('Presión', 'Pressione'),
            ('presion', 'pressione'), ('tensión', 'tensione'),
            ('Tensión', 'Tensione'), ('tension', 'tensione'),
            ('eficiencia', 'efficienza'), ('Eficiencia', 'Efficienza'),
            ('máxima', 'massima'), ('máximo', 'massimo'),
            ('mínima', 'minima'), ('mínimo', 'minimo'),
            ('carga', 'carico'), ('Carga', 'Carico'),
            ('vivienda', 'abitazione'), ('instalación', 'installazione'),
            ('eléctrico', 'elettrico'), ('eléctrica', 'elettrica'),
            ('electrico', 'elettrico'), ('electrica', 'elettrica'),
            ('térmica', 'termica'), ('térmico', 'termico'),
            ('termica', 'termica'), ('termico', 'termico'),
            ('energía', 'energia'), ('energia', 'energia'),
            ('solar', 'solare'), ('temperatura', 'temperatura'),
            ('Temperatura', 'Temperatura'), ('agua', 'acqua'),
            ('Agua', 'Acqua'), ('calentador', 'scaldacqua'),
            ('piscina', 'piscina'), ('depuradora', 'filtro'),
            ('riego', 'irrigazione'), ('goteo', 'goccia'),
            ('sifón', 'sifone'), ('sumidero', 'scarico'),
            ('desagüe', 'scarico'), ('ventilación', 'ventilazione'),
            ('Ventilación', 'Ventilazione'), ('mecánica', 'meccanica'),
            ('conducto', 'condotto'), ('conductos', 'condotti'),
            ('cerámico', 'ceramico'), ('azulejo', 'piastrella'),
            ('mosaico', 'mosaico'), ('aislamiento', 'isolamento'),
            ('batería', 'batteria'), ('baterías', 'batterie'),
            ('Baterías', 'Batterie'), ('autonomía', 'autonomia'),
            ('cantidad', 'quantità'), ('Cantidad', 'Quantità'),
            ('masa', 'massa'), ('peso', 'peso'),
            ('trifásica', 'trifase'), ('trifásico', 'trifase'),
            ('monofásica', 'monofase'), ('aparente', 'apparente'),
            ('activa', 'attiva'), ('reactiva', 'reattiva'),
            ('sección', 'sezione'), ('seccion', 'sezione'),
            ('cable', 'cavo'), ('puesta a tierra', 'messa a terra'),
            ('calefacción', 'riscaldamento'), ('refrigeración', 'raffreddamento'),
            ('porcentaje', 'percentuale'), ('Porcentaje', 'Percentuale'),
            ('amortización', 'ammortamento'), ('Amortización', 'Ammortamento'),
            ('préstamo', 'prestito'), ('vehículo', 'veicolo'),
            ('maquinaria', 'macchinario'), ('interés', 'interesse'),
            ('mensual', 'mensile'), ('anual', 'annuale'),
            ('combinación', 'combinazione'), ('combinaciones', 'combinazioni'),
            ('permutación', 'permutazione'), ('coeficiente', 'coefficiente'),
            ('desviación', 'deviazione'), ('media', 'media'),
            ('estándar', 'standard'), ('código', 'codice'),
            ('colores', 'colori'), ('resistenza', 'resistenza'),
            ('costante', 'costante'), ('dilatación', 'dilatazione'),
            ('dilución', 'diluizione'), ('concentración', 'concentrazione'),
            ('solución', 'soluzione'), ('velocità', 'velocità'),
            ('caldera', 'caldaia'), ('radiador', 'radiatore'),
            ('suelo', 'pavimento'), ('pared', 'parete'),
            ('techo', 'soffitto'), ('ventana', 'finestra'),
            ('puerta', 'porta'), ('depósito', 'serbatoio'),
            ('luminaria', 'apparecchio'), ('luminarias', 'apparecchi'),
            ('lúmenes', 'lumen'), ('lumenes', 'lumen'),
            ('iluminación', 'illuminazione'),
        ]
    else:
        return text
    
    result = text
    for old, new in replacements:
        # Match whole word only
        try:
            result = re.sub(r'\b' + re.escape(old) + r'\b', new, result)
        except:
            pass
    
    # Also fix common Spanish phrases
    return result


def fix_calculator_text(filepath):
    """Fix Spanish text in non-Spanish translations for a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changed = False
    i18n = data.get('i18n', {})
    
    for lang in ['en', 'fr', 'de', 'it']:
        if lang not in i18n:
            continue
        
        ld = i18n[lang]
        
        # Process string fields
        for field in ['result_context', 'example_label', 'formula_display', 
                      'description', 'seo_description', 'name']:
            if field in ld and ld[field]:
                new_val = clean_spanish(ld[field], lang)
                if new_val != ld[field]:
                    ld[field] = new_val
                    changed = True
        
        # Process list fields
        if 'steps' in ld:
            for i, step in enumerate(ld['steps']):
                new_step = clean_spanish(step, lang)
                if new_step != step:
                    ld['steps'][i] = new_step
                    changed = True
        
        if 'mistakes' in ld:
            for i, mist in enumerate(ld['mistakes']):
                new_mist = clean_spanish(mist, lang)
                if new_mist != mist:
                    ld['mistakes'][i] = new_mist
                    changed = True
        
        # Process range_hints
        if 'range_hints' in ld:
            for k, v in ld['range_hints'].items():
                if isinstance(v, str):
                    new_v = clean_spanish(v, lang)
                    if new_v != v:
                        ld['range_hints'][k] = new_v
                        changed = True
        
        # Process input labels
        if 'inputs' in ld:
            for k, v in ld['inputs'].items():
                if isinstance(v, str) and lang == 'de':
                    # Clean input labels for de
                    new_v = clean_spanish(v, lang)
                    if new_v != v:
                        ld['inputs'][k] = new_v
                        changed = True
        
        # Process output labels
        if 'outputs' in ld:
            for k, v in ld['outputs'].items():
                if isinstance(v, str) and lang == 'de':
                    new_v = clean_spanish(v, lang)
                    if new_v != v:
                        ld['outputs'][k] = new_v
                        changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    return changed


if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(CALC_DIR, '*.json')))
    fixed = 0
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            cid = int(data.get('id', '999'))
            if cid > 50:
                continue
            if fix_calculator_text(f):
                fixed += 1
                print(f'Fixed: {cid:03d} {data["slug"]}')
        except Exception as e:
            print(f'Error {f}: {e}')
    
    print(f'\nTotal fixed: {fixed}')

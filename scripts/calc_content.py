"""
ObraCalc – Content module
Block-level How-to steps + FAQs per language.
generate_intro() and generate_faq() are called by the generator.
"""

# ── How-to steps per block per language ──────────────────────────────────────

HOWTO = {
    "estructuras": {
        "es": [
            "Mide las dimensiones del elemento (largo, ancho, altura) con cinta métrica y anótalas en metros.",
            "Introduce los valores en los campos del formulario.",
            "Si la pieza lleva armadura, introduce la cuantía en kg/m³ (valor habitual: 80–150 kg/m³).",
            "Ajusta el porcentaje de desperdicio (recomendado 5–10 %) para cubrir pérdidas en obra.",
            "Pulsa «Calcular» para obtener el volumen de hormigón, sacos de cemento, arena, grava y acero.",
        ],
        "en": [
            "Measure the element dimensions (length, width, height) with a tape and note them in meters.",
            "Enter the values in the form fields.",
            "If reinforcement is needed, enter the steel ratio in kg/m³ (typical: 80–150 kg/m³).",
            "Adjust the wastage allowance (recommended 5–10 %) to cover on-site losses.",
            "Click 'Calculate' to get concrete volume, cement bags, sand, gravel and steel.",
        ],
        "fr": [
            "Mesurez les dimensions de l'élément (longueur, largeur, hauteur) en mètres.",
            "Saisissez les valeurs dans le formulaire.",
            "Indiquez le taux d'armature en kg/m³ si nécessaire (valeur typique : 80–150 kg/m³).",
            "Ajustez le taux de perte (5–10 % recommandé) pour couvrir les pertes sur chantier.",
            "Cliquez sur «Calculer» pour obtenir le volume de béton, sacs de ciment, sable et gravier.",
        ],
        "pt": [
            "Meça as dimensões do elemento (comprimento, largura, altura) em metros.",
            "Insira os valores nos campos do formulário.",
            "Se precisar de armadura, informe a taxa em kg/m³ (típico: 80–150 kg/m³).",
            "Ajuste a porcentagem de perda (5–10 % recomendado) para cobrir perdas em obra.",
            "Clique em «Calcular» para obter volume de concreto, sacos de cimento, areia e brita.",
        ],
        "de": [
            "Messen Sie die Bauteilabmessungen (Länge, Breite, Höhe) in Metern.",
            "Geben Sie die Werte in die Formularfelder ein.",
            "Tragen Sie bei Bedarf den Bewehrungsgehalt in kg/m³ ein (üblich: 80–150 kg/m³).",
            "Passen Sie den Verschnittfaktor an (5–10 % empfohlen), um Baustellen-Verluste zu decken.",
            "Klicken Sie auf «Berechnen», um Betonvolumen, Zementsäcke, Sand und Kies zu erhalten.",
        ],
        "it": [
            "Misurare le dimensioni dell'elemento (lunghezza, larghezza, altezza) in metri.",
            "Inserire i valori nei campi del modulo.",
            "Indicare la percentuale di armatura in kg/m³ se necessario (tipico: 80–150 kg/m³).",
            "Regolare la percentuale di perdita (5–10 % consigliato) per coprire le perdite in cantiere.",
            "Cliccare «Calcola» per ottenere volume di calcestruzzo, sacchi di cemento, sabbia e ghiaia.",
        ],
    },

    "mamposteria": {
        "es": [
            "Mide la longitud y la altura del muro en metros.",
            "Introduce el espesor del muro según el tipo de ladrillo o bloque que vayas a usar.",
            "Indica las dimensiones del ladrillo/bloque si son diferentes al estándar.",
            "Añade el porcentaje de desperdicio (5–10 % para ladrillo visto, 3–5 % para bloque).",
            "Pulsa «Calcular» para ver unidades de material, mortero y sacos de cemento.",
        ],
        "en": [
            "Measure the wall length and height in meters.",
            "Enter the wall thickness based on the brick or block type you'll use.",
            "Indicate brick/block dimensions if different from standard.",
            "Add wastage allowance (5–10 % for face brickwork, 3–5 % for blockwork).",
            "Click 'Calculate' to see units of material, mortar and cement bags.",
        ],
        "fr": [
            "Mesurez la longueur et la hauteur du mur en mètres.",
            "Saisissez l'épaisseur du mur selon le type de brique ou de bloc utilisé.",
            "Indiquez les dimensions de la brique/du bloc si elles diffèrent du standard.",
            "Ajoutez le taux de perte (5–10 % pour maçonnerie apparente, 3–5 % pour bloc).",
            "Cliquez sur «Calculer» pour obtenir les unités de matériaux, mortier et ciment.",
        ],
        "pt": [
            "Meça o comprimento e a altura da parede em metros.",
            "Insira a espessura da parede conforme o tipo de tijolo ou bloco.",
            "Indique as dimensões do tijolo/bloco se diferentes do padrão.",
            "Adicione a porcentagem de perda (5–10 % para alvenaria aparente, 3–5 % para bloco).",
            "Clique em «Calcular» para ver unidades de material, argamassa e sacos de cimento.",
        ],
        "de": [
            "Messen Sie Wandlänge und -höhe in Metern.",
            "Geben Sie die Wandstärke entsprechend dem verwendeten Ziegel- oder Blocktyp ein.",
            "Geben Sie Ziegel-/Blockmaße an, wenn sie vom Standard abweichen.",
            "Fügen Sie den Verschnittfaktor hinzu (5–10 % für Sichtmauerwerk, 3–5 % für Blockmauerwerk).",
            "Klicken Sie auf «Berechnen», um Materialeinheiten, Mörtel und Zementsäcke zu erhalten.",
        ],
        "it": [
            "Misurare la lunghezza e l'altezza del muro in metri.",
            "Inserire lo spessore del muro in base al tipo di mattone o blocco da utilizzare.",
            "Indicare le dimensioni del mattone/blocco se diverse dallo standard.",
            "Aggiungere la percentuale di perdita (5–10 % per muratura a vista, 3–5 % per blocco).",
            "Cliccare «Calcola» per vedere le unità di materiale, la malta e i sacchi di cemento.",
        ],
    },

    "pavimentos": {
        "es": [
            "Mide la longitud y el ancho de la superficie a pavimentar en metros.",
            "Selecciona o introduce el tamaño de la baldosa/pieza.",
            "Indica la junta entre piezas (valor habitual: 2–5 mm para interiores, 5–10 mm para exteriores).",
            "Añade un porcentaje de desperdicio: 10 % para colocación en diagonal, 5 % para ortogonal.",
            "Pulsa «Calcular» para obtener el número de piezas, adhesivo y lechada necesarios.",
        ],
        "en": [
            "Measure the length and width of the surface to be tiled in meters.",
            "Select or enter the tile/piece size.",
            "Enter the grout joint width (typical: 2–5 mm indoors, 5–10 mm outdoors).",
            "Add wastage: 10 % for diagonal layout, 5 % for straight layout.",
            "Click 'Calculate' to get piece count, adhesive and grout needed.",
        ],
        "fr": [
            "Mesurez la longueur et la largeur de la surface à revêtir en mètres.",
            "Saisissez les dimensions du carrelage.",
            "Indiquez la largeur des joints (typique : 2–5 mm en intérieur, 5–10 mm en extérieur).",
            "Ajoutez le taux de perte : 10 % pour pose en diagonale, 5 % pour pose droite.",
            "Cliquez sur «Calculer» pour obtenir le nombre de pièces, la colle et le joint.",
        ],
        "pt": [
            "Meça o comprimento e a largura da superfície a ser revestida em metros.",
            "Informe o tamanho do piso/peça.",
            "Indique a largura da junta (típico: 2–5 mm interno, 5–10 mm externo).",
            "Adicione perda: 10 % para assentamento diagonal, 5 % para ortogonal.",
            "Clique em «Calcular» para obter quantidade de peças, cola e rejunte.",
        ],
        "de": [
            "Messen Sie Länge und Breite der zu verlegenden Fläche in Metern.",
            "Geben Sie die Fliesen-/Steinmaße ein.",
            "Geben Sie die Fugenbreite ein (typisch: 2–5 mm innen, 5–10 mm außen).",
            "Fügen Sie Verschnitt hinzu: 10 % bei Diagonalverlegung, 5 % bei Geradeausverlegung.",
            "Klicken Sie auf «Berechnen», um Stückzahl, Kleber und Fugenmasse zu erhalten.",
        ],
        "it": [
            "Misurare la lunghezza e la larghezza della superficie da pavimentare in metri.",
            "Inserire le dimensioni della piastrella/pezzo.",
            "Indicare la larghezza della fugatura (tipico: 2–5 mm interni, 5–10 mm esterni).",
            "Aggiungere la perdita: 10 % per posa in diagonale, 5 % per posa ortogonale.",
            "Cliccare «Calcola» per ottenere il numero di pezzi, colla e stucco.",
        ],
    },

    "fontaneria": {
        "es": [
            "Identifica el caudal necesario en litros por minuto (L/min) o litros por segundo (L/s).",
            "Mide la longitud de la tubería en metros, incluyendo los tramos verticales.",
            "Introduce el diámetro nominal o interior de la tubería.",
            "Añade las pérdidas localizadas estimadas (codos, válvulas) si las conoces.",
            "Pulsa «Calcular» para obtener velocidad del fluido, pérdidas de carga y diámetro recomendado.",
        ],
        "en": [
            "Identify the required flow rate in liters per minute (L/min) or liters per second (L/s).",
            "Measure the pipe length in meters, including vertical runs.",
            "Enter the nominal or internal pipe diameter.",
            "Add estimated minor losses (elbows, valves) if known.",
            "Click 'Calculate' to get fluid velocity, head loss and recommended diameter.",
        ],
        "fr": [
            "Identifiez le débit requis en litres par minute (L/min) ou litres par seconde (L/s).",
            "Mesurez la longueur de la tuyauterie en mètres, y compris les tronçons verticaux.",
            "Saisissez le diamètre nominal ou intérieur de la tuyauterie.",
            "Ajoutez les pertes de charge localisées estimées (coudes, vannes) si vous les connaissez.",
            "Cliquez sur «Calculer» pour obtenir la vitesse du fluide, les pertes de charge et le diamètre conseillé.",
        ],
        "pt": [
            "Identifique a vazão necessária em litros por minuto (L/min) ou litros por segundo (L/s).",
            "Meça o comprimento da tubulação em metros, incluindo os trechos verticais.",
            "Insira o diâmetro nominal ou interno da tubulação.",
            "Adicione as perdas localizadas estimadas (cotovelos, válvulas) se as conhecer.",
            "Clique em «Calcular» para obter velocidade do fluido, perda de carga e diâmetro recomendado.",
        ],
        "de": [
            "Ermitteln Sie den erforderlichen Durchfluss in Liter pro Minute (L/min) oder Liter pro Sekunde (L/s).",
            "Messen Sie die Rohrlänge in Metern, einschließlich vertikaler Abschnitte.",
            "Geben Sie den Nenn- oder Innendurchmesser des Rohres ein.",
            "Fügen Sie geschätzte Einzelwiderstände (Bögen, Ventile) hinzu, falls bekannt.",
            "Klicken Sie auf «Berechnen», um Strömungsgeschwindigkeit, Druckverlust und empfohlenen Durchmesser zu erhalten.",
        ],
        "it": [
            "Identificare la portata richiesta in litri al minuto (L/min) o litri al secondo (L/s).",
            "Misurare la lunghezza della tubazione in metri, inclusi i tratti verticali.",
            "Inserire il diametro nominale o interno della tubazione.",
            "Aggiungere le perdite di carico localizzate stimate (curve, valvole) se note.",
            "Cliccare «Calcola» per ottenere velocità del fluido, perdite di carico e diametro consigliato.",
        ],
    },

    "electricidad": {
        "es": [
            "Determina la potencia total del circuito en vatios (W) o kilovatios (kW).",
            "Mide la longitud total del cable en metros (ida + vuelta).",
            "Indica la tensión de la instalación (230 V monofásico o 400 V trifásico).",
            "Introduce la caída de tensión máxima admisible (máx. 3 % en vivienda, 5 % en industria).",
            "Pulsa «Calcular» para obtener la sección del cable, corriente y caída de tensión real.",
        ],
        "en": [
            "Determine the total circuit power in watts (W) or kilowatts (kW).",
            "Measure the total cable run in meters (outward + return).",
            "Enter the installation voltage (230 V single-phase or 400 V three-phase).",
            "Enter the maximum allowable voltage drop (max 3 % residential, 5 % industrial).",
            "Click 'Calculate' to get cable cross-section, current and actual voltage drop.",
        ],
        "fr": [
            "Déterminez la puissance totale du circuit en watts (W) ou kilowatts (kW).",
            "Mesurez la longueur totale du câble en mètres (aller + retour).",
            "Indiquez la tension d'installation (230 V monophasé ou 400 V triphasé).",
            "Saisissez la chute de tension maximale admissible (max. 3 % en résidentiel, 5 % en industrie).",
            "Cliquez sur «Calculer» pour obtenir la section du câble, le courant et la chute de tension réelle.",
        ],
        "pt": [
            "Determine a potência total do circuito em watts (W) ou quilowatts (kW).",
            "Meça o comprimento total do cabo em metros (ida + volta).",
            "Indique a tensão da instalação (220 V monofásico ou 380 V trifásico).",
            "Insira a queda de tensão máxima admissível (máx. 3 % residencial, 5 % industrial).",
            "Clique em «Calcular» para obter seção do cabo, corrente e queda de tensão real.",
        ],
        "de": [
            "Ermitteln Sie die Gesamtleistung des Stromkreises in Watt (W) oder Kilowatt (kW).",
            "Messen Sie die gesamte Kabellänge in Metern (Hin- und Rückleiter).",
            "Geben Sie die Installationsspannung ein (230 V einphasig oder 400 V dreiphasig).",
            "Tragen Sie den zulässigen Spannungsabfall ein (max. 3 % Wohngebäude, 5 % Industrie).",
            "Klicken Sie auf «Berechnen», um Kabelquerschnitt, Strom und tatsächlichen Spannungsabfall zu erhalten.",
        ],
        "it": [
            "Determinare la potenza totale del circuito in watt (W) o kilowatt (kW).",
            "Misurare la lunghezza totale del cavo in metri (andata + ritorno).",
            "Indicare la tensione dell'impianto (230 V monofase o 400 V trifase).",
            "Inserire la caduta di tensione massima ammissibile (max 3 % residenziale, 5 % industriale).",
            "Cliccare «Calcola» per ottenere la sezione del cavo, la corrente e la caduta di tensione reale.",
        ],
    },

    "climatizacion": {
        "es": [
            "Mide la superficie del local en m² y la altura libre en metros.",
            "Indica la orientación predominante del espacio (norte, sur, este, oeste).",
            "Introduce los valores de transmitancia térmica de muros y cubierta (U en W/m²K).",
            "Indica las temperaturas de diseño interior y exterior.",
            "Pulsa «Calcular» para obtener la carga térmica y la potencia del equipo recomendado.",
        ],
        "en": [
            "Measure the room area in m² and clear ceiling height in meters.",
            "Indicate the predominant orientation of the space.",
            "Enter the thermal transmittance values for walls and roof (U in W/m²K).",
            "Enter interior and exterior design temperatures.",
            "Click 'Calculate' to get thermal load and recommended equipment power.",
        ],
        "fr": [
            "Mesurez la surface du local en m² et la hauteur libre en mètres.",
            "Indiquez l'orientation prédominante de l'espace.",
            "Saisissez les valeurs de transmittance thermique des murs et de la toiture (U en W/m²K).",
            "Indiquez les températures de calcul intérieure et extérieure.",
            "Cliquez sur «Calculer» pour obtenir la charge thermique et la puissance d'équipement recommandée.",
        ],
        "pt": [
            "Meça a área do ambiente em m² e o pé-direito em metros.",
            "Indique a orientação predominante do espaço.",
            "Insira os valores de transmitância térmica de paredes e cobertura (U em W/m²K).",
            "Indique as temperaturas de projeto interior e exterior.",
            "Clique em «Calcular» para obter a carga térmica e a potência do equipamento recomendado.",
        ],
        "de": [
            "Messen Sie die Raumfläche in m² und die lichte Raumhöhe in Metern.",
            "Geben Sie die vorherrschende Ausrichtung des Raumes an.",
            "Tragen Sie die Wärmedurchgangskoeffizienten für Wände und Dach ein (U in W/m²K).",
            "Geben Sie Innen- und Außen-Auslegungstemperaturen ein.",
            "Klicken Sie auf «Berechnen», um Wärmelast und empfohlene Anlagenleistung zu erhalten.",
        ],
        "it": [
            "Misurare la superficie del locale in m² e l'altezza netta in metri.",
            "Indicare l'orientamento predominante dello spazio.",
            "Inserire i valori di trasmittanza termica di pareti e copertura (U in W/m²K).",
            "Indicare le temperature di progetto interne ed esterne.",
            "Cliccare «Calcola» per ottenere il carico termico e la potenza dell'impianto consigliato.",
        ],
    },

    "carpinteria": {
        "es": [
            "Anota las dimensiones de la pieza o elemento (largo × ancho × grueso) en metros o centímetros.",
            "Indica el número de piezas o unidades iguales que necesitas.",
            "Selecciona el tipo de madera o material y su densidad si es necesario para el cálculo del peso.",
            "Añade un porcentaje de desperdicio (10–15 % para madizos, 5–10 % para chapas y tableros).",
            "Pulsa «Calcular» para obtener m³ de madera, peso total y coste estimado.",
        ],
        "en": [
            "Note the dimensions of the piece (length × width × thickness) in meters or centimeters.",
            "Enter the number of equal pieces or units needed.",
            "Select the wood type and density if needed for weight calculation.",
            "Add wastage allowance (10–15 % for solid wood, 5–10 % for panels and veneers).",
            "Click 'Calculate' to get m³ of timber, total weight and estimated cost.",
        ],
        "fr": [
            "Notez les dimensions de la pièce (longueur × largeur × épaisseur) en mètres ou centimètres.",
            "Indiquez le nombre de pièces identiques nécessaires.",
            "Sélectionnez le type de bois et sa densité si nécessaire pour le calcul du poids.",
            "Ajoutez un taux de perte (10–15 % pour le massif, 5–10 % pour les panneaux et placages).",
            "Cliquez sur «Calculer» pour obtenir les m³ de bois, le poids total et le coût estimé.",
        ],
        "pt": [
            "Anote as dimensões da peça (comprimento × largura × espessura) em metros ou centímetros.",
            "Informe o número de peças iguais necessárias.",
            "Selecione o tipo de madeira e a densidade se necessário para o cálculo do peso.",
            "Adicione a porcentagem de perda (10–15 % para madeira maciça, 5–10 % para painéis).",
            "Clique em «Calcular» para obter m³ de madeira, peso total e custo estimado.",
        ],
        "de": [
            "Notieren Sie die Abmessungen des Bauteils (Länge × Breite × Dicke) in Metern oder Zentimetern.",
            "Geben Sie die Anzahl der benötigten gleichen Teile ein.",
            "Wählen Sie Holzart und Dichte aus, falls für die Gewichtsberechnung benötigt.",
            "Fügen Sie Verschnitt hinzu (10–15 % für Massivholz, 5–10 % für Platten und Furniere).",
            "Klicken Sie auf «Berechnen», um m³ Holz, Gesamtgewicht und geschätzte Kosten zu erhalten.",
        ],
        "it": [
            "Annotare le dimensioni del pezzo (lunghezza × larghezza × spessore) in metri o centimetri.",
            "Indicare il numero di pezzi uguali necessari.",
            "Selezionare il tipo di legno e la densità se necessario per il calcolo del peso.",
            "Aggiungere la percentuale di perdita (10–15 % per legno massello, 5–10 % per pannelli).",
            "Cliccare «Calcola» per ottenere m³ di legno, peso totale e costo stimato.",
        ],
    },

    "pintura": {
        "es": [
            "Mide la superficie a pintar en m² (largo × alto de cada pared/techo).",
            "Resta las superficies de puertas y ventanas (aproximadamente 1.8 m² por puerta, 1.2 m² por ventana).",
            "Indica el número de manos: 1 mano para renovación sobre mismo color, 2–3 manos para cambio de color.",
            "Comprueba el rendimiento de la pintura en la ficha técnica del producto (habitual: 10–14 m²/L).",
            "Pulsa «Calcular» para ver litros netos, litros totales con merma y envases a comprar.",
        ],
        "en": [
            "Measure the surface to paint in m² (length × height of each wall/ceiling).",
            "Subtract door and window areas (approx. 1.8 m² per door, 1.2 m² per window).",
            "Enter the number of coats: 1 coat for same-colour refresh, 2–3 for colour change.",
            "Check the paint spread rate on the product data sheet (typical: 10–14 m²/L).",
            "Click 'Calculate' to see net litres, total litres with wastage and cans to buy.",
        ],
        "fr": [
            "Mesurez la surface à peindre en m² (longueur × hauteur de chaque mur/plafond).",
            "Soustrayez les surfaces des portes et fenêtres (environ 1,8 m² par porte, 1,2 m² par fenêtre).",
            "Indiquez le nombre de couches : 1 couche pour une rénovation, 2–3 couches pour un changement de couleur.",
            "Vérifiez le rendement de la peinture sur la fiche technique (habituellement : 10–14 m²/L).",
            "Cliquez sur «Calculer» pour voir les litres nets, les litres totaux avec perte et les contenants à acheter.",
        ],
        "pt": [
            "Meça a superfície a pintar em m² (comprimento × altura de cada parede/teto).",
            "Subtraia as áreas de portas e janelas (aprox. 1,8 m² por porta, 1,2 m² por janela).",
            "Indique o número de demãos: 1 demão para renovação, 2–3 para troca de cor.",
            "Verifique o rendimento da tinta na ficha técnica (habitual: 10–14 m²/L).",
            "Clique em «Calcular» para ver litros líquidos, litros totais com perda e embalagens a comprar.",
        ],
        "de": [
            "Messen Sie die zu streichende Fläche in m² (Länge × Höhe jeder Wand/Decke).",
            "Ziehen Sie Tür- und Fensterflächen ab (ca. 1,8 m² pro Tür, 1,2 m² pro Fenster).",
            "Geben Sie die Anzahl der Anstriche ein: 1 Anstrich für Auffrischung, 2–3 für Farbwechsel.",
            "Prüfen Sie die Ergiebigkeit im Produktdatenblatt (üblich: 10–14 m²/L).",
            "Klicken Sie auf «Berechnen», um Nettoliter, Gesamtliter mit Verlust und zu kaufende Gebinde zu sehen.",
        ],
        "it": [
            "Misurare la superficie da verniciare in m² (lunghezza × altezza di ogni parete/soffitto).",
            "Sottrarre le superfici di porte e finestre (circa 1,8 m² per porta, 1,2 m² per finestra).",
            "Indicare il numero di mani: 1 mano per rinnovo dello stesso colore, 2–3 per cambio colore.",
            "Controllare la resa della pittura nella scheda tecnica (tipico: 10–14 m²/L).",
            "Cliccare «Calcola» per vedere litri netti, litri totali con perdita e confezioni da acquistare.",
        ],
    },

    "gestion": {
        "es": [
            "Reúne los datos de coste: materiales, mano de obra, maquinaria y gastos generales.",
            "Introduce los valores en los campos correspondientes.",
            "Indica el porcentaje de beneficio industrial y gastos generales si procede.",
            "Revisa los subtotales antes de aceptar el resultado final.",
            "Pulsa «Calcular» para obtener el desglose de costes, precio unitario y totales.",
        ],
        "en": [
            "Gather cost data: materials, labour, machinery and overheads.",
            "Enter the values in the corresponding fields.",
            "Enter the profit margin and overhead percentage if applicable.",
            "Review subtotals before accepting the final result.",
            "Click 'Calculate' to get cost breakdown, unit price and totals.",
        ],
        "fr": [
            "Rassemblez les données de coût : matériaux, main-d'œuvre, matériel et frais généraux.",
            "Saisissez les valeurs dans les champs correspondants.",
            "Indiquez le pourcentage de bénéfice industriel et de frais généraux le cas échéant.",
            "Vérifiez les sous-totaux avant d'accepter le résultat final.",
            "Cliquez sur «Calculer» pour obtenir la décomposition des coûts, le prix unitaire et les totaux.",
        ],
        "pt": [
            "Reúna os dados de custo: materiais, mão de obra, maquinário e despesas gerais.",
            "Insira os valores nos campos correspondentes.",
            "Indique a margem de lucro e o percentual de despesas gerais, se aplicável.",
            "Revise os subtotais antes de aceitar o resultado final.",
            "Clique em «Calcular» para obter o detalhamento de custos, preço unitário e totais.",
        ],
        "de": [
            "Sammeln Sie Kostendaten: Materialien, Arbeit, Maschinen und Gemeinkosten.",
            "Tragen Sie die Werte in die entsprechenden Felder ein.",
            "Geben Sie Gewinnmarge und Gemeinkostenzuschlag an, falls zutreffend.",
            "Überprüfen Sie die Zwischensummen, bevor Sie das Endergebnis akzeptieren.",
            "Klicken Sie auf «Berechnen», um Kostenaufstellung, Einheitspreis und Gesamtbeträge zu erhalten.",
        ],
        "it": [
            "Raccogliere i dati di costo: materiali, manodopera, macchinari e spese generali.",
            "Inserire i valori nei campi corrispondenti.",
            "Indicare la percentuale di utile e spese generali, se applicabile.",
            "Controllare i subtotali prima di accettare il risultato finale.",
            "Cliccare «Calcola» per ottenere il dettaglio dei costi, il prezzo unitario e i totali.",
        ],
    },

    "matematicas": {
        "es": ["Introduce los valores numéricos en los campos correspondientes.", "Pulsa «Calcular» para obtener el resultado al instante.", "Puedes usar decimales con punto o coma."],
        "en": ["Enter the numeric values in the corresponding fields.", "Click 'Calculate' to get the result instantly.", "You can use decimal points for non-integer values."],
        "fr": ["Saisissez les valeurs numériques dans les champs.", "Cliquez sur «Calculer» pour obtenir le résultat instantanément.", "Vous pouvez utiliser des décimales."],
        "pt": ["Insira os valores numéricos nos campos.", "Clique em «Calcular» para obter o resultado.", "Pode usar decimais com ponto ou vírgula."],
        "de": ["Geben Sie die Zahlenwerte in die entsprechenden Felder ein.", "Klicken Sie auf «Berechnen», um das Ergebnis sofort zu erhalten.", "Dezimalzahlen sind erlaubt."],
        "it": ["Inserire i valori numerici nei campi corrispondenti.", "Cliccare «Calcola» per ottenere il risultato immediatamente.", "Si possono usare i decimali."],
    },

    "finanzas": {
        "es": ["Introduce el importe principal o precio de partida.", "Ajusta el tipo de interés y el plazo según tu oferta bancaria.", "Revisa todos los resultados: cuota, intereses totales y coste total.", "Compara diferentes escenarios cambiando el plazo o el tipo de interés.", "Pulsa «Calcular» para ver el resultado al instante."],
        "en": ["Enter the principal amount or starting price.", "Adjust the interest rate and term to match your bank offer.", "Review all results: monthly payment, total interest and total cost.", "Compare scenarios by changing the term or interest rate.", "Click 'Calculate' to see the result instantly."],
        "fr": ["Saisissez le montant principal ou le prix de départ.", "Ajustez le taux d'intérêt et la durée selon votre offre bancaire.", "Consultez tous les résultats : mensualité, intérêts totaux et coût total.", "Comparez des scénarios en modifiant la durée ou le taux.", "Cliquez sur «Calculer» pour voir le résultat immédiatement."],
        "pt": ["Insira o montante principal ou preço de partida.", "Ajuste a taxa de juro e o prazo de acordo com a proposta do banco.", "Reveja todos os resultados: prestação, juros totais e custo total.", "Compare cenários alterando o prazo ou a taxa.", "Clique em «Calcular» para ver o resultado."],
        "de": ["Geben Sie den Hauptbetrag oder Ausgangspreis ein.", "Passen Sie Zinssatz und Laufzeit an Ihr Bankangebot an.", "Überprüfen Sie alle Ergebnisse: Rate, Gesamtzinsen und Gesamtkosten.", "Vergleichen Sie Szenarien durch Änderung von Laufzeit oder Zinssatz.", "Klicken Sie auf «Berechnen», um das Ergebnis sofort zu sehen."],
        "it": ["Inserire il capitale principale o il prezzo di partenza.", "Regolare il tasso di interesse e la durata in base all'offerta bancaria.", "Rivedere tutti i risultati: rata, interessi totali e costo totale.", "Confrontare scenari modificando la durata o il tasso.", "Cliccare «Calcola» per vedere il risultato immediatamente."],
    },

    "salud": {
        "es": ["Introduce tu peso en kilogramos y tu altura en centímetros.", "Indica tu sexo y nivel de actividad física para el cálculo de calorías.", "Pulsa «Calcular» para obtener tu resultado personalizado.", "Consulta siempre a un profesional de la salud antes de hacer cambios en tu dieta o ejercicio."],
        "en": ["Enter your weight in kilograms and height in centimetres.", "Indicate your sex and physical activity level for calorie calculations.", "Click 'Calculate' for your personalised result.", "Always consult a health professional before making changes to your diet or exercise routine."],
        "fr": ["Saisissez votre poids en kilogrammes et votre taille en centimètres.", "Indiquez votre sexe et votre niveau d'activité physique pour les calories.", "Cliquez sur «Calculer» pour votre résultat personnalisé.", "Consultez toujours un professionnel de santé avant de modifier votre alimentation."],
        "pt": ["Insira o seu peso em quilogramas e a altura em centímetros.", "Indique o seu sexo e nível de atividade física para o cálculo de calorias.", "Clique em «Calcular» para o resultado personalizado.", "Consulte sempre um profissional de saúde antes de alterar dieta ou exercício."],
        "de": ["Geben Sie Ihr Gewicht in Kilogramm und Ihre Körpergröße in Zentimetern ein.", "Geben Sie Ihr Geschlecht und Aktivitätsniveau für die Kalorienberechnung an.", "Klicken Sie auf «Berechnen» für Ihr persönliches Ergebnis.", "Konsultieren Sie immer einen Arzt, bevor Sie Ernährung oder Sport ändern."],
        "it": ["Inserire il peso in chilogrammi e l'altezza in centimetri.", "Indicare il sesso e il livello di attività fisica per il calcolo delle calorie.", "Cliccare «Calcola» per il risultato personalizzato.", "Consultare sempre un medico prima di modificare dieta o esercizio fisico."],
    },

    "cotidiano": {
        "es": ["Introduce los valores solicitados en el formulario.", "Para la propina, indica el total de la cuenta, el porcentaje y el número de comensales.", "Para la edad o fechas, usa año y mes numéricos.", "Pulsa «Calcular» para obtener el resultado."],
        "en": ["Enter the requested values in the form.", "For tips, enter the bill total, percentage and number of people.", "For age or dates, use numeric year and month.", "Click 'Calculate' to get the result."],
        "fr": ["Saisissez les valeurs demandées dans le formulaire.", "Pour le pourboire, entrez le total, le pourcentage et le nombre de convives.", "Pour l'âge ou les dates, utilisez des années et mois numériques.", "Cliquez sur «Calculer» pour obtenir le résultat."],
        "pt": ["Insira os valores pedidos no formulário.", "Para gorjetas, insira o total, a percentagem e o número de pessoas.", "Para idade ou datas, use ano e mês numéricos.", "Clique em «Calcular» para obter o resultado."],
        "de": ["Geben Sie die angeforderten Werte in das Formular ein.", "Für Trinkgeld: Rechnungsbetrag, Prozentsatz und Personenzahl eingeben.", "Für Alter oder Daten: numerisches Jahr und Monat verwenden.", "Klicken Sie auf «Berechnen», um das Ergebnis zu erhalten."],
        "it": ["Inserire i valori richiesti nel modulo.", "Per la mancia, inserire il totale, la percentuale e il numero di persone.", "Per età o date, usare anno e mese numerici.", "Cliccare «Calcola» per ottenere il risultato."],
    },
    "estadistica": {
        "es": ["Introduce hasta 10 valores numéricos en los campos (deja vacíos los que no uses).", "Para media, mediana, varianza y desviación estándar, introduce tus datos.", "Para probabilidad, introduce los casos favorables y totales.", "Pulsa «Calcular» para obtener el resultado."],
        "en": ["Enter up to 10 numerical values (leave unused fields blank).", "For mean, median, variance and standard deviation, enter your data.", "For probability, enter favorable and total outcomes.", "Click 'Calculate' to get the result."],
        "fr": ["Saisissez jusqu'à 10 valeurs numériques (laissez vides les champs inutilisés).", "Pour moyenne, médiane, variance et écart type, entrez vos données.", "Pour la probabilité, entrez les cas favorables et totaux.", "Cliquez sur «Calculer» pour obtenir le résultat."],
        "pt": ["Insira até 10 valores numéricos (deixe vazios os campos não usados).", "Para média, mediana, variância e desvio padrão, insira seus dados.", "Para probabilidade, insira casos favoráveis e totais.", "Clique em «Calcular» para obter o resultado."],
        "de": ["Geben Sie bis zu 10 Zahlenwerte ein (freie Felder leer lassen).", "Für Mittelwert, Median, Varianz und Standardabweichung: Daten eingeben.", "Für Wahrscheinlichkeit: günstige und Gesamtergebnisse eingeben.", "Klicken Sie auf «Berechnen» für das Ergebnis."],
        "it": ["Inserire fino a 10 valori numerici (lasciare vuoti i campi non usati).", "Per media, mediana, varianza e deviazione standard, inserire i dati.", "Per probabilità, inserire casi favorevoli e totali.", "Cliccare «Calcola» per ottenere il risultato."],
    },
    "ciencia": {
        "es": ["Introduce los valores conocidos en el formulario.", "Para velocidad: distancia y tiempo. Para fuerza: masa y aceleración.", "Para energía: masa, velocidad o altura según el tipo.", "Pulsa «Calcular» para obtener el resultado."],
        "en": ["Enter the known values in the form.", "For speed: distance and time. For force: mass and acceleration.", "For energy: mass, velocity or height depending on the type.", "Click 'Calculate' to get the result."],
        "fr": ["Saisissez les valeurs connues dans le formulaire.", "Vitesse : distance et temps. Force : masse et accélération.", "Énergie : masse, vitesse ou hauteur selon le type.", "Cliquez sur «Calculer» pour obtenir le résultat."],
        "pt": ["Insira os valores conhecidos no formulário.", "Velocidade: distância e tempo. Força: massa e aceleração.", "Energia: massa, velocidade ou altura conforme o tipo.", "Clique em «Calcular» para obter o resultado."],
        "de": ["Geben Sie die bekannten Werte in das Formular ein.", "Geschwindigkeit: Strecke und Zeit. Kraft: Masse und Beschleunigung.", "Energie: Masse, Geschwindigkeit oder Höhe je nach Typ.", "Klicken Sie auf «Berechnen» für das Ergebnis."],
        "it": ["Inserire i valori noti nel modulo.", "Velocità: distanza e tempo. Forza: massa e accelerazione.", "Energia: massa, velocità o altezza secondo il tipo.", "Cliccare «Calcola» per ottenere il risultato."],
    },
    "conversion": {
        "es": ["Introduce el valor en la unidad base indicada.", "El resultado muestra todas las conversiones automáticamente.", "No necesitas seleccionar la unidad de destino.", "Pulsa «Calcular» para obtener el resultado."],
        "en": ["Enter the value in the base unit shown.", "The result shows all conversions automatically.", "No need to select the target unit.", "Click 'Calculate' to get the result."],
        "fr": ["Saisissez la valeur dans l'unité de base indiquée.", "Le résultat affiche toutes les conversions automatiquement.", "Pas besoin de sélectionner l'unité cible.", "Cliquez sur «Calculer» pour obtenir le résultat."],
        "pt": ["Insira o valor na unidade base indicada.", "O resultado mostra todas as conversões automaticamente.", "Não precisa selecionar a unidade de destino.", "Clique em «Calcular» para obter o resultado."],
        "de": ["Geben Sie den Wert in der angegebenen Basiseinheit ein.", "Das Ergebnis zeigt alle Umrechnungen automatisch.", "Sie müssen die Zieleinheit nicht auswählen.", "Klicken Sie auf «Berechnen» für das Ergebnis."],
        "it": ["Inserire il valore nell'unità di base indicata.", "Il risultato mostra tutte le conversioni automaticamente.", "Non è necessario selezionare l'unità di destinazione.", "Cliccare «Calcola» per ottenere il risultato."],
    },
    "deportes": {
        "es": ["Introduce los datos de tu ejercicio o carrera.", "Para ritmo de carrera: distancia recorrida y tiempo empleado.", "Para calorías: peso, duración e intensidad (MET).", "Pulsa «Calcular» para obtener el resultado."],
        "en": ["Enter your exercise or race data.", "For running pace: distance covered and time elapsed.", "For calories: weight, duration and intensity (MET).", "Click 'Calculate' to get the result."],
        "fr": ["Saisissez les données de votre exercice ou course.", "Pour l'allure : distance parcourue et temps écoulé.", "Pour les calories : poids, durée et intensité (MET).", "Cliquez sur «Calculer» pour obtenir le résultat."],
        "pt": ["Insira os dados do seu exercício ou corrida.", "Para ritmo de corrida: distância percorrida e tempo gasto.", "Para calorias: peso, duração e intensidade (MET).", "Clique em «Calcular» para obter o resultado."],
        "de": ["Geben Sie Ihre Trainings- oder Laufdaten ein.", "Für Laufpacing: zurückgelegte Strecke und benötigte Zeit.", "Für Kalorien: Gewicht, Dauer und Intensität (MET).", "Klicken Sie auf «Berechnen» für das Ergebnis."],
        "it": ["Inserire i dati dell'esercizio o della corsa.", "Per il ritmo di corsa: distanza percorsa e tempo impiegato.", "Per le calorie: peso, durata e intensità (MET).", "Cliccare «Calcola» per ottenere il risultato."],
    },
}


# ── Block-level FAQs per language ─────────────────────────────────────────────

FAQS = {
    "estructuras": {
        "es": [
            {
                "q": "¿Cuántos sacos de cemento se necesitan por m³ de hormigón?",
                "a": "Para hormigón estándar (dosificación 250 kg/m³) se necesitan 5 sacos de 50 kg por m³. Para hormigón resistente (300 kg/m³), use 6 sacos. Esta calculadora usa la dosificación habitual para cada tipo de elemento.",
            },
            {
                "q": "¿Por qué debo añadir un porcentaje de desperdicio?",
                "a": "En obra siempre hay pérdidas por derrames, mezclas no aprovechables y correcciones de nivel. Se recomienda añadir entre el 5 % y el 10 % al pedido final para no quedarse corto.",
            },
            {
                "q": "¿Qué diferencia hay entre hormigón en masa y hormigón armado?",
                "a": "El hormigón en masa no lleva armadura de acero y se usa para cimientos de baja solicitación. El hormigón armado incluye barras de acero que le dan resistencia a tracción, siendo apto para losas, pilares y vigas.",
            },
        ],
        "en": [
            {
                "q": "How many cement bags are needed per m³ of concrete?",
                "a": "For standard concrete (250 kg/m³ mix), you need 5 bags of 50 kg per m³. For structural concrete (300 kg/m³), use 6 bags. This calculator uses the typical dosage for each element type.",
            },
            {
                "q": "Why should I add a wastage percentage?",
                "a": "On-site losses from spillage, unusable mixes and level corrections always occur. Adding 5–10 % to your final order ensures you don't run short of material.",
            },
            {
                "q": "What is the difference between mass concrete and reinforced concrete?",
                "a": "Mass concrete has no steel reinforcement and is used for low-load foundations. Reinforced concrete includes steel bars that provide tensile strength, making it suitable for slabs, columns and beams.",
            },
        ],
        "fr": [
            {
                "q": "Combien de sacs de ciment faut-il par m³ de béton ?",
                "a": "Pour un béton standard (dosage 250 kg/m³), il faut 5 sacs de 50 kg par m³. Pour un béton résistant (300 kg/m³), utilisez 6 sacs.",
            },
            {
                "q": "Pourquoi ajouter un pourcentage de perte ?",
                "a": "Sur chantier, il y a toujours des pertes dues aux déversements, aux mélanges inutilisables et aux corrections de niveau. Ajoutez 5 à 10 % à votre commande finale.",
            },
            {
                "q": "Quelle est la différence entre béton de masse et béton armé ?",
                "a": "Le béton de masse n'a pas d'armature en acier et est utilisé pour les fondations peu sollicitées. Le béton armé comprend des barres d'acier qui lui confèrent une résistance à la traction.",
            },
        ],
        "pt": [
            {
                "q": "Quantos sacos de cimento são necessários por m³ de concreto?",
                "a": "Para concreto padrão (250 kg/m³), são necessários 5 sacos de 50 kg por m³. Para concreto estrutural (300 kg/m³), use 6 sacos.",
            },
            {
                "q": "Por que adicionar uma porcentagem de perda?",
                "a": "Em obra sempre há perdas por derramamento, misturas inutilizáveis e correções de nível. Adicione 5 a 10 % ao pedido final para não faltar material.",
            },
            {
                "q": "Qual a diferença entre concreto simples e concreto armado?",
                "a": "O concreto simples não tem armadura de aço e é usado em fundações de baixa solicitação. O concreto armado inclui barras de aço que conferem resistência à tração.",
            },
        ],
        "de": [
            {
                "q": "Wie viele Zementsäcke werden pro m³ Beton benötigt?",
                "a": "Für Standardbeton (Dosierung 250 kg/m³) benötigen Sie 5 Säcke à 50 kg pro m³. Für tragenden Beton (300 kg/m³) verwenden Sie 6 Säcke.",
            },
            {
                "q": "Warum sollte ich einen Verschnittfaktor hinzufügen?",
                "a": "Auf Baustellen entstehen immer Verluste durch Verschütten, unbrauchbare Mischungen und Höhenkorrekturen. Fügen Sie 5–10 % zur Endbestellung hinzu.",
            },
            {
                "q": "Was ist der Unterschied zwischen unbewehrtem und bewehrtem Beton?",
                "a": "Unbewehrter Beton hat keine Stahlarmierung und wird für gering beanspruchte Fundamente verwendet. Stahlbeton enthält Bewehrungsstäbe, die Zugfestigkeit verleihen.",
            },
        ],
        "it": [
            {
                "q": "Quanti sacchi di cemento servono per m³ di calcestruzzo?",
                "a": "Per calcestruzzo standard (dosaggio 250 kg/m³) servono 5 sacchi da 50 kg per m³. Per calcestruzzo strutturale (300 kg/m³), usare 6 sacchi.",
            },
            {
                "q": "Perché aggiungere una percentuale di perdita?",
                "a": "In cantiere si verificano sempre perdite per versamenti, miscele inutilizzabili e correzioni di livello. Aggiungere il 5–10 % all'ordine finale per non rimanere a corto di materiale.",
            },
            {
                "q": "Qual è la differenza tra calcestruzzo in massa e calcestruzzo armato?",
                "a": "Il calcestruzzo in massa non ha armatura in acciaio e si usa per fondazioni a bassa sollecitazione. Il calcestruzzo armato include barre d'acciaio che gli conferiscono resistenza a trazione.",
            },
        ],
    },

    "mamposteria": {
        "es": [
            {
                "q": "¿Cuántos ladrillos hay por m²?",
                "a": "Con ladrillo estándar (24 × 11.5 cm) y junta de 1 cm se obtienen aproximadamente 38–40 ladrillos por m² para un muro de 1/2 pie. Para muro de 1 pie, multiplica por 2.",
            },
            {
                "q": "¿Cómo descuento las ventanas y puertas?",
                "a": "Resta el área de cada hueco (ancho × alto) de la superficie total antes de introducirla en la calculadora. Puertas estándar: 0.9 × 2.1 m = 1.89 m². Ventanas: según medida.",
            },
            {
                "q": "¿Qué proporción de mortero se usa en mampostería?",
                "a": "La proporción más habitual es 1:4 (cemento:arena) para muros exteriores y 1:5 para interiores. Con esta calculadora obtendrás directamente los kg de cemento y arena necesarios.",
            },
        ],
        "en": [
            {
                "q": "How many bricks per m²?",
                "a": "With a standard brick (24 × 11.5 cm) and a 1 cm joint, you get approx. 38–40 bricks per m² for a half-brick wall. For a full-brick wall, multiply by 2.",
            },
            {
                "q": "How do I deduct windows and doors?",
                "a": "Subtract the area of each opening (width × height) from the total before entering it in the calculator. Standard door: 0.9 × 2.1 m = 1.89 m². Windows: as measured.",
            },
            {
                "q": "What mortar mix is used in brickwork?",
                "a": "The most common ratio is 1:4 (cement:sand) for external walls and 1:5 for internal walls. This calculator gives you the cement and sand quantities directly.",
            },
        ],
        "fr": [
            {
                "q": "Combien de briques par m² ?",
                "a": "Avec une brique standard (24 × 11,5 cm) et un joint de 1 cm, on obtient environ 38–40 briques par m² pour un mur d'une demi-brique.",
            },
            {
                "q": "Comment déduire les fenêtres et portes ?",
                "a": "Soustrayez la surface de chaque ouverture (largeur × hauteur) de la surface totale avant de la saisir dans la calculatrice. Porte standard : 0,9 × 2,1 m = 1,89 m².",
            },
            {
                "q": "Quelle proportion de mortier utiliser en maçonnerie ?",
                "a": "La proportion la plus courante est 1:4 (ciment:sable) pour les murs extérieurs et 1:5 pour les murs intérieurs.",
            },
        ],
        "pt": [
            {
                "q": "Quantos tijolos por m²?",
                "a": "Com tijolo padrão (24 × 11,5 cm) e junta de 1 cm, obtêm-se aproximadamente 38–40 tijolos por m² para parede de meia espessura.",
            },
            {
                "q": "Como descontar janelas e portas?",
                "a": "Subtraia a área de cada vão (largura × altura) da superfície total antes de inserir na calculadora. Porta padrão: 0,9 × 2,1 m = 1,89 m².",
            },
            {
                "q": "Qual a proporção de argamassa usada na alvenaria?",
                "a": "A proporção mais comum é 1:4 (cimento:areia) para paredes externas e 1:5 para internas.",
            },
        ],
        "de": [
            {
                "q": "Wie viele Ziegel pro m²?",
                "a": "Mit einem Standardziegel (24 × 11,5 cm) und 1 cm Fuge erhält man ca. 38–40 Ziegel pro m² für ein Halbsteinmauerwerk.",
            },
            {
                "q": "Wie ziehe ich Fenster und Türen ab?",
                "a": "Ziehen Sie die Fläche jeder Öffnung (Breite × Höhe) von der Gesamtfläche ab, bevor Sie sie eingeben. Standardtür: 0,9 × 2,1 m = 1,89 m².",
            },
            {
                "q": "Welches Mörtelmischungsverhältnis wird im Mauerwerk verwendet?",
                "a": "Das häufigste Verhältnis ist 1:4 (Zement:Sand) für Außenwände und 1:5 für Innenwände.",
            },
        ],
        "it": [
            {
                "q": "Quanti mattoni per m²?",
                "a": "Con un mattone standard (24 × 11,5 cm) e una giunta di 1 cm si ottengono circa 38–40 mattoni per m² per una muratura a mezza pietra.",
            },
            {
                "q": "Come detrarre finestre e porte?",
                "a": "Sottrarre la superficie di ogni apertura (larghezza × altezza) dalla superficie totale prima di inserirla nel calcolatore. Porta standard: 0,9 × 2,1 m = 1,89 m².",
            },
            {
                "q": "Quale proporzione di malta si usa nella muratura?",
                "a": "La proporzione più comune è 1:4 (cemento:sabbia) per muri esterni e 1:5 per muri interni.",
            },
        ],
    },

    "pavimentos": {
        "es": [
            {
                "q": "¿Por qué debo añadir un 10 % de desperdicio en la colocación diagonal?",
                "a": "La colocación en diagonal genera más cortes y piezas sobrantes en los extremos. El 10 % es el mínimo recomendado; para patrones complejos considera hasta un 15 %.",
            },
            {
                "q": "¿Cuántos kg de adhesivo se necesitan por m²?",
                "a": "Depende del adhesivo y el tamaño de la baldosa. Para baldosas pequeñas (< 30 × 30 cm) se usan 2–4 kg/m², para grandes formatos (60 × 60 cm o más) se necesitan 5–8 kg/m².",
            },
            {
                "q": "¿Qué espesor de adhesivo se debe usar?",
                "a": "Para pavimentos interiores sin irregularidades, se aplica una capa de 3–5 mm. Para exteriores o superficies irregulares, se puede llegar a 10 mm con mortero-cola.",
            },
        ],
        "en": [
            {
                "q": "Why add 10 % wastage for diagonal laying?",
                "a": "Diagonal installation creates more cuts and offcuts at the edges. 10 % is the minimum recommended; for complex patterns consider up to 15 %.",
            },
            {
                "q": "How many kg of adhesive per m²?",
                "a": "It depends on the adhesive and tile size. For small tiles (< 30 × 30 cm) use 2–4 kg/m²; for large formats (60 × 60 cm or more) you need 5–8 kg/m².",
            },
            {
                "q": "What adhesive thickness should be used?",
                "a": "For smooth interior floors, apply a 3–5 mm layer. For exterior or uneven surfaces, up to 10 mm with tile adhesive mortar.",
            },
        ],
        "fr": [
            {
                "q": "Pourquoi ajouter 10 % de perte pour la pose en diagonale ?",
                "a": "La pose en diagonale génère plus de coupes et de chutes aux bords. 10 % est le minimum recommandé ; pour des motifs complexes, envisagez jusqu'à 15 %.",
            },
            {
                "q": "Combien de kg de colle par m² ?",
                "a": "Cela dépend de la colle et de la taille du carrelage. Pour les petits formats (< 30 × 30 cm), utilisez 2–4 kg/m² ; pour les grands formats (60 × 60 cm ou plus), il faut 5–8 kg/m².",
            },
            {
                "q": "Quelle épaisseur de colle doit être utilisée ?",
                "a": "Pour les sols intérieurs sans irrégularités, appliquez une couche de 3–5 mm. Pour les extérieurs ou les surfaces irrégulières, jusqu'à 10 mm avec mortier-colle.",
            },
        ],
        "pt": [
            {
                "q": "Por que adicionar 10 % de perda para assentamento diagonal?",
                "a": "O assentamento diagonal gera mais cortes e retalhos nas bordas. 10 % é o mínimo recomendado; para padrões complexos considere até 15 %.",
            },
            {
                "q": "Quantos kg de cola por m²?",
                "a": "Depende da cola e do tamanho da peça. Para peças pequenas (< 30 × 30 cm), use 2–4 kg/m²; para grandes formatos (60 × 60 cm ou mais), são necessários 5–8 kg/m².",
            },
            {
                "q": "Qual espessura de cola deve ser usada?",
                "a": "Para pisos internos sem irregularidades, aplique uma camada de 3–5 mm. Para externos ou superfícies irregulares, até 10 mm com argamassa colante.",
            },
        ],
        "de": [
            {
                "q": "Warum 10 % Verschnitt bei Diagonalverlegung hinzufügen?",
                "a": "Diagonalverlegung erzeugt mehr Schnitte und Abfälle an den Rändern. 10 % ist das empfohlene Minimum; bei komplexen Mustern bis zu 15 %.",
            },
            {
                "q": "Wie viele kg Kleber pro m²?",
                "a": "Je nach Kleber und Fliesengröße. Für kleine Fliesen (< 30 × 30 cm) 2–4 kg/m²; für Großformate (60 × 60 cm oder mehr) 5–8 kg/m².",
            },
            {
                "q": "Welche Klebstoffdicke sollte verwendet werden?",
                "a": "Für glatte Innenböden eine Schicht von 3–5 mm auftragen. Für Außenbereiche oder unebene Flächen bis zu 10 mm mit Fliesenkleber-Mörtel.",
            },
        ],
        "it": [
            {
                "q": "Perché aggiungere il 10 % di perdita per la posa in diagonale?",
                "a": "La posa in diagonale genera più tagli e scarti ai bordi. Il 10 % è il minimo raccomandato; per motivi complessi considerare fino al 15 %.",
            },
            {
                "q": "Quanti kg di adesivo per m²?",
                "a": "Dipende dall'adesivo e dalla dimensione della piastrella. Per piastrelle piccole (< 30 × 30 cm) usare 2–4 kg/m²; per grandi formati (60 × 60 cm o più) servono 5–8 kg/m².",
            },
            {
                "q": "Quale spessore di adesivo usare?",
                "a": "Per pavimenti interni senza irregolarità, applicare uno strato di 3–5 mm. Per esterni o superfici irregolari, fino a 10 mm con adesivo cementizio.",
            },
        ],
    },

    "fontaneria": {
        "es": [
            {
                "q": "¿Cuál es la velocidad máxima recomendada del agua en tuberías?",
                "a": "Para instalaciones domésticas se recomienda no superar 1.5 m/s en tuberías de distribución y 2 m/s en colectores. Velocidades mayores generan ruido y erosión.",
            },
            {
                "q": "¿Qué diámetro de tubería debo usar para mi vivienda?",
                "a": "Para una vivienda unifamiliar, la acometida suele ser de 25–32 mm, la distribución principal de 20 mm y los ramales de aparatos de 15–16 mm (Ø 1/2\").",
            },
            {
                "q": "¿Cómo calculo el volumen de una cisterna o depósito?",
                "a": "El volumen mínimo recomendado es de 150–200 litros por habitante para reserva de 1 día. Para reservas de emergencia, se amplía a 2–3 días.",
            },
        ],
        "en": [
            {
                "q": "What is the recommended maximum water velocity in pipes?",
                "a": "For domestic installations, do not exceed 1.5 m/s in distribution pipes and 2 m/s in collectors. Higher velocities cause noise and erosion.",
            },
            {
                "q": "What pipe diameter should I use for my house?",
                "a": "For a single-family home, the service pipe is usually 25–32 mm, main distribution 20 mm and appliance branches 15–16 mm (½\").",
            },
            {
                "q": "How do I calculate the volume of a cistern or tank?",
                "a": "Minimum recommended volume is 150–200 litres per occupant for 1-day reserve. For emergency reserves, extend to 2–3 days.",
            },
        ],
        "fr": [
            {
                "q": "Quelle est la vitesse maximale recommandée de l'eau dans les canalisations ?",
                "a": "Pour les installations domestiques, ne pas dépasser 1,5 m/s dans les canalisations de distribution et 2 m/s dans les collecteurs.",
            },
            {
                "q": "Quel diamètre de tuyau dois-je utiliser pour ma maison ?",
                "a": "Pour une maison individuelle, le branchement est généralement de 25–32 mm, la distribution principale de 20 mm et les branches d'appareils de 15–16 mm (½\").",
            },
            {
                "q": "Comment calculer le volume d'une citerne ou d'un réservoir ?",
                "a": "Le volume minimal recommandé est de 150–200 litres par occupant pour une réserve d'1 jour.",
            },
        ],
        "pt": [
            {
                "q": "Qual é a velocidade máxima recomendada da água em tubulações?",
                "a": "Para instalações domésticas, não exceder 1,5 m/s em tubulações de distribuição e 2 m/s em coletores.",
            },
            {
                "q": "Qual diâmetro de tubulação usar na minha casa?",
                "a": "Para residência unifamiliar, o ramal de entrada é geralmente de 25–32 mm, a distribuição principal de 20 mm e os ramais de aparelhos de 15–16 mm (½\").",
            },
            {
                "q": "Como calcular o volume de uma cisterna ou reservatório?",
                "a": "O volume mínimo recomendado é de 150–200 litros por morador para reserva de 1 dia.",
            },
        ],
        "de": [
            {
                "q": "Was ist die empfohlene maximale Wassergeschwindigkeit in Rohrleitungen?",
                "a": "Für häusliche Anlagen sollten 1,5 m/s in Verteilerleitungen und 2 m/s in Sammelrohren nicht überschritten werden.",
            },
            {
                "q": "Welchen Rohrdurchmesser soll ich für mein Haus verwenden?",
                "a": "Für ein Einfamilienhaus ist der Hausanschluss meist 25–32 mm, die Hauptverteilung 20 mm und die Geräteanschlüsse 15–16 mm (½\").",
            },
            {
                "q": "Wie berechne ich das Volumen einer Zisterne oder eines Tanks?",
                "a": "Das empfohlene Mindestvolumen beträgt 150–200 Liter pro Bewohner für eine Tagesreserve.",
            },
        ],
        "it": [
            {
                "q": "Qual è la velocità massima raccomandata dell'acqua nelle tubazioni?",
                "a": "Per impianti domestici non superare 1,5 m/s nelle tubazioni di distribuzione e 2 m/s nei collettori.",
            },
            {
                "q": "Quale diametro di tubazione usare per la mia casa?",
                "a": "Per un'abitazione unifamiliare, l'allacciamento è generalmente di 25–32 mm, la distribuzione principale di 20 mm e i rami degli apparecchi di 15–16 mm (½\").",
            },
            {
                "q": "Come calcolare il volume di una cisterna o serbatoio?",
                "a": "Il volume minimo raccomandato è di 150–200 litri per abitante per una riserva di 1 giorno.",
            },
        ],
    },

    "electricidad": {
        "es": [
            {
                "q": "¿Cuál es la caída de tensión máxima permitida en una instalación eléctrica?",
                "a": "Según el Reglamento Electrotécnico de Baja Tensión (REBT), la caída máxima es del 3 % para vivienda e industria (circuitos de alumbrado) y del 5 % para otros usos.",
            },
            {
                "q": "¿Qué sección mínima de cable se usa para tomas de corriente?",
                "a": "Para circuitos de tomas de uso general en vivienda se usa cable de 2.5 mm², y para circuitos de grandes electrodomésticos, de 4 mm². Los circuitos de alumbrado usan 1.5 mm².",
            },
            {
                "q": "¿Cómo sé si necesito instalar un diferencial adicional?",
                "a": "Si el circuito alimenta zonas húmedas (baño, cocina, exterior) o máquinas con mayor riesgo de contacto, es obligatorio instalar un diferencial de alta sensibilidad (30 mA).",
            },
        ],
        "en": [
            {
                "q": "What is the maximum allowable voltage drop in an electrical installation?",
                "a": "Per standard regulations, the maximum voltage drop is 3 % for residential and lighting circuits and 5 % for other uses.",
            },
            {
                "q": "What is the minimum cable cross-section for power outlets?",
                "a": "General-purpose outlet circuits use 2.5 mm² cable; large appliance circuits use 4 mm². Lighting circuits use 1.5 mm².",
            },
            {
                "q": "How do I know if I need an additional RCD?",
                "a": "If the circuit feeds wet areas (bathroom, kitchen, outdoor) or equipment with higher contact risk, a high-sensitivity RCD (30 mA) is mandatory.",
            },
        ],
        "fr": [
            {
                "q": "Quelle est la chute de tension maximale autorisée dans une installation électrique ?",
                "a": "Selon les normes, la chute de tension maximale est de 3 % pour les circuits résidentiels et d'éclairage, et de 5 % pour les autres usages.",
            },
            {
                "q": "Quelle section minimale de câble pour les prises de courant ?",
                "a": "Les circuits de prises standard utilisent du câble de 2,5 mm² ; les circuits de gros appareils, du 4 mm². Les circuits d'éclairage utilisent 1,5 mm².",
            },
            {
                "q": "Comment savoir si j'ai besoin d'un différentiel supplémentaire ?",
                "a": "Si le circuit alimente des zones humides ou des équipements à risque de contact, un différentiel haute sensibilité (30 mA) est obligatoire.",
            },
        ],
        "pt": [
            {
                "q": "Qual é a queda de tensão máxima permitida em uma instalação elétrica?",
                "a": "Conforme normas, a queda máxima é de 3 % para circuitos residenciais e de iluminação, e de 5 % para outros usos.",
            },
            {
                "q": "Qual é a seção mínima de cabo para tomadas de corrente?",
                "a": "Circuitos de tomadas de uso geral usam cabo de 2,5 mm²; circuitos de eletrodomésticos grandes, 4 mm². Circuitos de iluminação usam 1,5 mm².",
            },
            {
                "q": "Como saber se preciso instalar um DR adicional?",
                "a": "Se o circuito alimenta áreas úmidas ou equipamentos com maior risco de contato, é obrigatório instalar um DR de alta sensibilidade (30 mA).",
            },
        ],
        "de": [
            {
                "q": "Was ist der maximal zulässige Spannungsabfall in einer elektrischen Installation?",
                "a": "Nach den Vorschriften beträgt der maximale Spannungsabfall 3 % für Wohn- und Beleuchtungskreise und 5 % für andere Verwendungen.",
            },
            {
                "q": "Was ist der Mindestquerschnitt für Steckdosenstromkreise?",
                "a": "Allgemeine Steckdosenstromkreise verwenden 2,5 mm²-Kabel; Großgeräte-Stromkreise 4 mm². Beleuchtungsstromkreise verwenden 1,5 mm².",
            },
            {
                "q": "Woher weiß ich, ob ich einen zusätzlichen FI-Schutzschalter benötige?",
                "a": "Wenn der Stromkreis feuchte Bereiche oder Geräte mit erhöhtem Berührungsrisiko speist, ist ein hochempfindlicher FI-Schutzschalter (30 mA) vorgeschrieben.",
            },
        ],
        "it": [
            {
                "q": "Qual è la caduta di tensione massima ammessa in un impianto elettrico?",
                "a": "Secondo le norme, la caduta di tensione massima è del 3 % per circuiti residenziali e di illuminazione e del 5 % per altri usi.",
            },
            {
                "q": "Qual è la sezione minima di cavo per le prese di corrente?",
                "a": "I circuiti prese ad uso generale usano cavo da 2,5 mm²; i circuiti grandi elettrodomestici usano 4 mm². I circuiti di illuminazione usano 1,5 mm².",
            },
            {
                "q": "Come sapere se è necessario un differenziale aggiuntivo?",
                "a": "Se il circuito alimenta zone umide o apparecchiature con maggior rischio di contatto, è obbligatorio installare un differenziale ad alta sensibilità (30 mA).",
            },
        ],
    },

    "climatizacion": {
        "es": [
            {
                "q": "¿Cuántos BTU necesito por m²?",
                "a": "Como regla general, se estiman 100–150 W/m² (350–500 BTU/m²) en climas cálidos y 75–100 W/m² en climas templados. Esta calculadora tiene en cuenta la orientación y el aislamiento.",
            },
            {
                "q": "¿Cuál es la diferencia entre calefacción y refrigeración en el cálculo?",
                "a": "Para calefacción se calcula la pérdida de calor en invierno (ΔT entre interior y exterior). Para refrigeración se calcula la ganancia de calor en verano, que incluye radiación solar.",
            },
            {
                "q": "¿Cada cuánto tiempo se debe hacer el mantenimiento del equipo de climatización?",
                "a": "Los filtros deben limpiarse cada 3 meses y reemplazarse anualmente. La revisión general del equipo (gas refrigerante, intercambiador) debe hacerse cada 2–3 años por un técnico certificado.",
            },
        ],
        "en": [
            {
                "q": "How many BTU do I need per m²?",
                "a": "As a rule, estimate 100–150 W/m² (350–500 BTU/m²) for hot climates and 75–100 W/m² for temperate climates. This calculator accounts for orientation and insulation.",
            },
            {
                "q": "What is the difference between heating and cooling calculations?",
                "a": "For heating, heat loss in winter is calculated (ΔT between indoor and outdoor). For cooling, summer heat gain is calculated, which includes solar radiation.",
            },
            {
                "q": "How often should air conditioning equipment be serviced?",
                "a": "Filters should be cleaned every 3 months and replaced annually. A full service (refrigerant, heat exchanger) should be done every 2–3 years by a certified technician.",
            },
        ],
        "fr": [
            {
                "q": "De combien de BTU ai-je besoin par m² ?",
                "a": "En règle générale, estimez 100–150 W/m² (350–500 BTU/m²) pour les climats chauds et 75–100 W/m² pour les climats tempérés.",
            },
            {
                "q": "Quelle est la différence entre les calculs de chauffage et de climatisation ?",
                "a": "Pour le chauffage, on calcule la perte de chaleur en hiver (ΔT entre intérieur et extérieur). Pour la climatisation, on calcule le gain de chaleur en été, y compris le rayonnement solaire.",
            },
            {
                "q": "À quelle fréquence faut-il entretenir les équipements de climatisation ?",
                "a": "Les filtres doivent être nettoyés tous les 3 mois et remplacés annuellement. Une révision complète doit être effectuée tous les 2–3 ans par un technicien certifié.",
            },
        ],
        "pt": [
            {
                "q": "Quantos BTU preciso por m²?",
                "a": "Como regra geral, estime 100–150 W/m² (350–500 BTU/m²) para climas quentes e 75–100 W/m² para climas temperados.",
            },
            {
                "q": "Qual é a diferença entre os cálculos de aquecimento e refrigeração?",
                "a": "Para aquecimento, calcula-se a perda de calor no inverno (ΔT entre interior e exterior). Para refrigeração, calcula-se o ganho de calor no verão, incluindo radiação solar.",
            },
            {
                "q": "Com que frequência o equipamento de climatização deve ser manutenido?",
                "a": "Os filtros devem ser limpos a cada 3 meses e trocados anualmente. Uma revisão geral deve ser feita a cada 2–3 anos por um técnico certificado.",
            },
        ],
        "de": [
            {
                "q": "Wie viele BTU benötige ich pro m²?",
                "a": "Als Faustregel gilt: 100–150 W/m² (350–500 BTU/m²) für warme Klimazonen, 75–100 W/m² für gemäßigte Klimazonen.",
            },
            {
                "q": "Was ist der Unterschied zwischen Heiz- und Kühlberechnungen?",
                "a": "Beim Heizen wird der Wärmeverlust im Winter berechnet (ΔT zwischen Innen und Außen). Beim Kühlen wird der Sommerwärmegewinn einschließlich Sonnenstrahlung berechnet.",
            },
            {
                "q": "Wie oft sollten Klimaanlagen gewartet werden?",
                "a": "Filter sollten alle 3 Monate gereinigt und jährlich ersetzt werden. Eine Generalinspektion sollte alle 2–3 Jahre von einem zertifizierten Techniker durchgeführt werden.",
            },
        ],
        "it": [
            {
                "q": "Quanti BTU servono per m²?",
                "a": "Come regola generale, stimare 100–150 W/m² (350–500 BTU/m²) per climi caldi e 75–100 W/m² per climi temperati.",
            },
            {
                "q": "Qual è la differenza tra i calcoli di riscaldamento e raffrescamento?",
                "a": "Per il riscaldamento si calcola la dispersione di calore in inverno (ΔT tra interno ed esterno). Per il raffrescamento si calcola il guadagno di calore estivo, inclusa la radiazione solare.",
            },
            {
                "q": "Con quale frequenza vanno manutenuti gli impianti di climatizzazione?",
                "a": "I filtri devono essere puliti ogni 3 mesi e sostituiti annualmente. Una revisione generale deve essere effettuata ogni 2–3 anni da un tecnico certificato.",
            },
        ],
    },

    "carpinteria": {
        "es": [
            {
                "q": "¿Qué porcentaje de desperdicio debo añadir al cortar madera?",
                "a": "Para madera maciza en bruto, añade un 15–20 %. Para tableros de DM o contrachapado, con un 10 % suele ser suficiente. En trabajos de precisión con piezas muy ajustadas, puede reducirse al 5 %.",
            },
            {
                "q": "¿Cómo calculo la cantidad de tablas para un entarimado?",
                "a": "Divide la superficie total (m²) entre el ancho nominal de la tabla. Multiplica el resultado por la longitud de la estancia y añade el porcentaje de desperdicio según el tipo de colocación.",
            },
            {
                "q": "¿Qué densidad tiene la madera de pino?",
                "a": "La madera de pino tiene una densidad aproximada de 500–600 kg/m³ según la especie y el grado de secado. La madera de roble ronda los 700–750 kg/m³.",
            },
        ],
        "en": [
            {
                "q": "What wastage percentage should I add when cutting timber?",
                "a": "For rough solid timber, add 15–20 %. For MDF or plywood boards, 10 % is usually enough. For precision work with tightly fitted pieces, it can be reduced to 5 %.",
            },
            {
                "q": "How do I calculate the amount of boards for a wood floor?",
                "a": "Divide the total area (m²) by the board width and add the wastage percentage according to the laying pattern.",
            },
            {
                "q": "What is the density of pine wood?",
                "a": "Pine has an approximate density of 500–600 kg/m³ depending on species and drying grade. Oak is around 700–750 kg/m³.",
            },
        ],
        "fr": [
            {
                "q": "Quel pourcentage de perte dois-je ajouter lors de la coupe du bois ?",
                "a": "Pour le bois massif brut, ajoutez 15–20 %. Pour les panneaux MDF ou contreplaqué, 10 % est généralement suffisant.",
            },
            {
                "q": "Comment calculer la quantité de planches pour un parquet ?",
                "a": "Divisez la surface totale (m²) par la largeur nominale de la planche et ajoutez le pourcentage de perte selon le type de pose.",
            },
            {
                "q": "Quelle est la densité du bois de pin ?",
                "a": "Le pin a une densité d'environ 500–600 kg/m³ selon l'espèce et le degré de séchage. Le chêne est d'environ 700–750 kg/m³.",
            },
        ],
        "pt": [
            {
                "q": "Qual porcentagem de perda adicionar ao cortar madeira?",
                "a": "Para madeira maciça bruta, adicione 15–20 %. Para painéis de MDF ou compensado, 10 % geralmente é suficiente.",
            },
            {
                "q": "Como calcular a quantidade de tábuas para um piso de madeira?",
                "a": "Divida a área total (m²) pela largura nominal da tábua e adicione a porcentagem de perda conforme o tipo de assentamento.",
            },
            {
                "q": "Qual é a densidade da madeira de pinho?",
                "a": "O pinho tem densidade aproximada de 500–600 kg/m³ conforme a espécie e o grau de secagem. O carvalho gira em torno de 700–750 kg/m³.",
            },
        ],
        "de": [
            {
                "q": "Welchen Verschnittfaktor sollte ich beim Holzschneiden hinzufügen?",
                "a": "Für rohes Massivholz 15–20 % hinzufügen. Für MDF- oder Sperrholzplatten genügen in der Regel 10 %.",
            },
            {
                "q": "Wie berechne ich die Anzahl der Dielen für einen Holzboden?",
                "a": "Teilen Sie die Gesamtfläche (m²) durch die Nennbreite der Diele und fügen Sie den Verschnittfaktor je nach Verlegeart hinzu.",
            },
            {
                "q": "Wie hoch ist die Dichte von Kiefernholz?",
                "a": "Kiefer hat eine Dichte von ca. 500–600 kg/m³ je nach Art und Trocknungsgrad. Eiche liegt bei ca. 700–750 kg/m³.",
            },
        ],
        "it": [
            {
                "q": "Quale percentuale di perdita aggiungere quando si taglia il legno?",
                "a": "Per legno massello grezzo, aggiungere il 15–20 %. Per pannelli di MDF o compensato, il 10 % è solitamente sufficiente.",
            },
            {
                "q": "Come calcolare la quantità di tavole per un pavimento in legno?",
                "a": "Dividere la superficie totale (m²) per la larghezza nominale della tavola e aggiungere la percentuale di perdita in base al tipo di posa.",
            },
            {
                "q": "Qual è la densità del legno di pino?",
                "a": "Il pino ha una densità di circa 500–600 kg/m³ a seconda della specie e del grado di essiccazione. La quercia è intorno a 700–750 kg/m³.",
            },
        ],
    },

    "pintura": {
        "es": [
            {
                "q": "¿Cuántas manos de pintura necesito?",
                "a": "Para paredes en buen estado con mismo color: 1 mano. Para cambio de color o paredes muy absorbentes: 2 manos. Para colores oscuros sobre paredes claras o viceversa: 2–3 manos + imprimación.",
            },
            {
                "q": "¿Qué rendimiento tiene la pintura plástica para interior?",
                "a": "La pintura plástica de interior tiene un rendimiento habitual de 12–14 m²/L por mano. La pintura exterior o texturizada tiene un rendimiento menor, de 8–10 m²/L.",
            },
            {
                "q": "¿Cómo se calcula la pintura para techos?",
                "a": "Mide el largo × el ancho del techo en metros. Aplica el rendimiento de la pintura seleccionada (10–14 m²/L) y el número de manos. Para techos con gotelé, usa un 20 % más de pintura.",
            },
        ],
        "en": [
            {
                "q": "How many coats of paint do I need?",
                "a": "For walls in good condition with the same colour: 1 coat. For colour change or highly absorbent walls: 2 coats. For dark over light or vice versa: 2–3 coats + primer.",
            },
            {
                "q": "What is the coverage of interior emulsion paint?",
                "a": "Interior emulsion typically covers 12–14 m²/L per coat. Exterior or textured paint covers less, around 8–10 m²/L.",
            },
            {
                "q": "How is paint calculated for ceilings?",
                "a": "Measure length × width of the ceiling in metres. Apply the paint coverage (10–14 m²/L) and number of coats. For textured ceilings, use 20 % more paint.",
            },
        ],
        "fr": [
            {
                "q": "Combien de couches de peinture faut-il ?",
                "a": "Pour des murs en bon état avec la même couleur : 1 couche. Pour un changement de couleur ou des murs très absorbants : 2 couches. Pour les couleurs sombres sur les claires ou vice-versa : 2–3 couches + sous-couche.",
            },
            {
                "q": "Quel est le rendement de la peinture plastique intérieure ?",
                "a": "La peinture intérieure a un rendement habituel de 12–14 m²/L par couche. La peinture extérieure ou texturée a un rendement moindre, de 8–10 m²/L.",
            },
            {
                "q": "Comment calcule-t-on la peinture pour les plafonds ?",
                "a": "Mesurez la longueur × la largeur du plafond en mètres. Appliquez le rendement de la peinture et le nombre de couches. Pour les plafonds texturés, utilisez 20 % de peinture en plus.",
            },
        ],
        "pt": [
            {
                "q": "Quantas demãos de tinta preciso?",
                "a": "Para paredes em bom estado com a mesma cor: 1 demão. Para troca de cor ou paredes muito absorventes: 2 demãos. Para cores escuras sobre claras ou vice-versa: 2–3 demãos + selador.",
            },
            {
                "q": "Qual é o rendimento da tinta plástica para interior?",
                "a": "A tinta plástica de interior tem rendimento habitual de 12–14 m²/L por demão. A tinta exterior ou texturizada tem rendimento menor, de 8–10 m²/L.",
            },
            {
                "q": "Como calcular a tinta para tetos?",
                "a": "Meça o comprimento × a largura do teto em metros. Aplique o rendimento da tinta e o número de demãos. Para tetos com textura, use 20 % a mais de tinta.",
            },
        ],
        "de": [
            {
                "q": "Wie viele Anstriche benötige ich?",
                "a": "Für Wände in gutem Zustand mit gleicher Farbe: 1 Anstrich. Bei Farbwechsel oder stark saugenden Wänden: 2 Anstriche. Für Dunkel über Hell oder umgekehrt: 2–3 Anstriche + Grundierung.",
            },
            {
                "q": "Welche Ergiebigkeit hat Innenfarbe?",
                "a": "Innenfarbe hat üblicherweise eine Ergiebigkeit von 12–14 m²/L pro Anstrich. Außenfarbe oder strukturierte Farbe hat eine geringere Ergiebigkeit von 8–10 m²/L.",
            },
            {
                "q": "Wie berechnet man die Farbe für Decken?",
                "a": "Länge × Breite der Decke in Metern messen. Ergiebigkeit der Farbe und Anzahl der Anstriche anwenden. Für strukturierte Decken 20 % mehr Farbe einplanen.",
            },
        ],
        "it": [
            {
                "q": "Quante mani di pittura servono?",
                "a": "Per pareti in buono stato con lo stesso colore: 1 mano. Per cambio colore o pareti molto assorbenti: 2 mani. Per colori scuri su chiari o viceversa: 2–3 mani + fondo.",
            },
            {
                "q": "Qual è la resa della pittura plastica per interni?",
                "a": "La pittura da interni ha una resa abituale di 12–14 m²/L per mano. La pittura per esterni o texturizzata ha resa minore, di 8–10 m²/L.",
            },
            {
                "q": "Come si calcola la pittura per i soffitti?",
                "a": "Misurare lunghezza × larghezza del soffitto in metri. Applicare la resa della pittura e il numero di mani. Per soffitti texturizzati, usare il 20 % in più di pittura.",
            },
        ],
    },

    "gestion": {
        "es": [
            {
                "q": "¿Qué porcentaje de gastos generales se aplica en construcción?",
                "a": "En España, los gastos generales de empresa (GGE) se sitúan entre el 13 % y el 17 % del coste de ejecución material. A esto se añade el beneficio industrial, habitualmente del 6 %.",
            },
            {
                "q": "¿Cómo se calcula el precio de venta de una obra?",
                "a": "Precio de venta = Coste de ejecución material × (1 + GGE%) × (1 + BI%) × (1 + IVA%). Las calculadoras de gestión de esta suite te ayudan a desglosar cada partida.",
            },
            {
                "q": "¿Qué es el rendimiento de un operario?",
                "a": "El rendimiento es la cantidad de trabajo realizado por un operario en una jornada (p.ej. m² de enfoscado, ml de tubería instalada). Este dato es fundamental para calcular costes de mano de obra.",
            },
        ],
        "en": [
            {
                "q": "What overhead percentage is applied in construction?",
                "a": "Overheads typically range from 13–17 % of the direct cost. A profit margin of around 6 % is then added on top.",
            },
            {
                "q": "How is the selling price of a construction job calculated?",
                "a": "Selling price = Direct cost × (1 + Overhead%) × (1 + Profit%) × (1 + VAT%). The management calculators in this suite help you break down each item.",
            },
            {
                "q": "What is a worker's output rate?",
                "a": "Output rate is the amount of work completed by one worker per day (e.g. m² of plastering, ml of pipe installed). This is key for calculating labour costs.",
            },
        ],
        "fr": [
            {
                "q": "Quel pourcentage de frais généraux applique-t-on en construction ?",
                "a": "Les frais généraux sont généralement de 13–17 % du coût d'exécution direct. Un bénéfice industriel d'environ 6 % s'y ajoute.",
            },
            {
                "q": "Comment calcule-t-on le prix de vente d'un chantier ?",
                "a": "Prix de vente = Coût direct × (1 + Frais généraux%) × (1 + Bénéfice%) × (1 + TVA%). Les calculatrices de gestion de cette suite vous aident à décomposer chaque poste.",
            },
            {
                "q": "Qu'est-ce que le rendement d'un ouvrier ?",
                "a": "Le rendement est la quantité de travail réalisée par un ouvrier par jour (ex. m² d'enduit, ml de tuyau posé). C'est essentiel pour calculer les coûts de main-d'œuvre.",
            },
        ],
        "pt": [
            {
                "q": "Qual percentual de despesas gerais se aplica na construção?",
                "a": "As despesas gerais geralmente ficam entre 13–17 % do custo de execução direto. A isso se acrescenta a margem de lucro, habitualmente de 6 %.",
            },
            {
                "q": "Como se calcula o preço de venda de uma obra?",
                "a": "Preço de venda = Custo direto × (1 + Despesas gerais%) × (1 + Lucro%) × (1 + IVA%). As calculadoras de gestão desta suite ajudam a detalhar cada item.",
            },
            {
                "q": "O que é o rendimento de um operário?",
                "a": "O rendimento é a quantidade de trabalho realizada por um operário por dia (ex.: m² de reboco, ml de tubulação instalada). É fundamental para calcular custos de mão de obra.",
            },
        ],
        "de": [
            {
                "q": "Welcher Gemeinkostensatz wird im Bauwesen angewendet?",
                "a": "Gemeinkosten liegen üblicherweise bei 13–17 % der direkten Herstellungskosten. Dazu kommt ein Gewinnzuschlag von ca. 6 %.",
            },
            {
                "q": "Wie wird der Verkaufspreis eines Bauauftrags berechnet?",
                "a": "Verkaufspreis = Direktkosten × (1 + Gemeinkosten%) × (1 + Gewinn%) × (1 + MwSt%). Die Verwaltungskalkulatoren dieser Suite helfen Ihnen, jeden Posten aufzuschlüsseln.",
            },
            {
                "q": "Was ist die Leistung eines Arbeiters?",
                "a": "Die Leistung ist die pro Tag von einem Arbeiter erledigte Arbeitsmenge (z.B. m² Verputz, ml verlegtes Rohr). Dies ist für die Berechnung der Lohnkosten entscheidend.",
            },
        ],
        "it": [
            {
                "q": "Quale percentuale di spese generali si applica in edilizia?",
                "a": "Le spese generali sono tipicamente del 13–17 % del costo di esecuzione diretto. A questo si aggiunge un utile di circa il 6 %.",
            },
            {
                "q": "Come si calcola il prezzo di vendita di un lavoro edile?",
                "a": "Prezzo di vendita = Costo diretto × (1 + Spese generali%) × (1 + Utile%) × (1 + IVA%). Le calcolatrici di gestione di questa suite aiutano a dettagliare ogni voce.",
            },
            {
                "q": "Cos'è il rendimento di un operaio?",
                "a": "Il rendimento è la quantità di lavoro eseguita da un operaio al giorno (es. m² di intonaco, ml di tubo installato). È fondamentale per calcolare i costi di manodopera.",
            },
        ],
    },

    "matematicas": {
        "es": [
            {"q": "¿Cuánto es el 15% de 200?", "a": "El 15% de 200 es 30. Se calcula como 200 × 15 / 100 = 30."},
            {"q": "¿Cómo se calcula el cambio porcentual?", "a": "Cambio (%) = ((valor final − valor inicial) / |valor inicial|) × 100. Si sube de 80 a 100, el cambio es (20/80)×100 = 25%."},
            {"q": "¿Qué es el teorema de Pitágoras?", "a": "El teorema de Pitágoras establece que en un triángulo rectángulo, c² = a² + b², donde c es la hipotenusa y a, b los catetos."},
            {"q": "¿Cómo funciona la regla de tres?", "a": "Si A corresponde a B, y queremos saber qué corresponde a C, la regla de tres dice: X = (B × C) / A."},
        ],
        "en": [
            {"q": "What is 15% of 200?", "a": "15% of 200 is 30. Calculated as 200 × 15 / 100 = 30."},
            {"q": "How do you calculate percentage change?", "a": "Percentage change = ((final − initial) / |initial|) × 100. From 80 to 100 it is (20/80)×100 = 25%."},
            {"q": "What is the Pythagorean theorem?", "a": "The Pythagorean theorem states that in a right triangle, c² = a² + b², where c is the hypotenuse and a, b are the legs."},
            {"q": "How does the rule of three work?", "a": "If A corresponds to B, and we want what corresponds to C: X = (B × C) / A."},
        ],
        "fr": [
            {"q": "Combien est 15% de 200 ?", "a": "15% de 200 est 30. Calculé comme 200 × 15 / 100 = 30."},
            {"q": "Comment calculer une variation en pourcentage ?", "a": "Variation (%) = ((final − initial) / |initial|) × 100. De 80 à 100 : (20/80)×100 = 25%."},
            {"q": "Qu'est-ce que le théorème de Pythagore ?", "a": "Dans un triangle rectangle, c² = a² + b², où c est l'hypoténuse et a, b les côtés."},
            {"q": "Comment fonctionne la règle de trois ?", "a": "Si A correspond à B et on cherche ce qui correspond à C : X = (B × C) / A."},
        ],
        "pt": [
            {"q": "Quanto é 15% de 200?", "a": "15% de 200 é 30. Calculado como 200 × 15 / 100 = 30."},
            {"q": "Como se calcula a variação percentual?", "a": "Variação (%) = ((final − inicial) / |inicial|) × 100. De 80 a 100: (20/80)×100 = 25%."},
            {"q": "O que é o teorema de Pitágoras?", "a": "Num triângulo retângulo, c² = a² + b², onde c é a hipotenusa e a, b os catetos."},
            {"q": "Como funciona a regra de três?", "a": "Se A corresponde a B e queremos o que corresponde a C: X = (B × C) / A."},
        ],
        "de": [
            {"q": "Wie viel sind 15% von 200?", "a": "15% von 200 sind 30. Berechnung: 200 × 15 / 100 = 30."},
            {"q": "Wie berechnet man eine prozentuale Änderung?", "a": "Änderung (%) = ((End − Anfang) / |Anfang|) × 100. Von 80 auf 100: (20/80)×100 = 25%."},
            {"q": "Was ist der Satz des Pythagoras?", "a": "Im rechtwinkligen Dreieck gilt: c² = a² + b², wobei c die Hypotenuse und a, b die Katheten sind."},
            {"q": "Wie funktioniert der Dreisatz?", "a": "Wenn A zu B entspricht und man wissen will, was zu C entspricht: X = (B × C) / A."},
        ],
        "it": [
            {"q": "Quanto è il 15% di 200?", "a": "Il 15% di 200 è 30. Si calcola come 200 × 15 / 100 = 30."},
            {"q": "Come si calcola la variazione percentuale?", "a": "Variazione (%) = ((finale − iniziale) / |iniziale|) × 100. Da 80 a 100: (20/80)×100 = 25%."},
            {"q": "Cos'è il teorema di Pitagora?", "a": "In un triangolo rettangolo, c² = a² + b², dove c è l'ipotenusa e a, b i cateti."},
            {"q": "Come funziona la regola del tre?", "a": "Se A corrisponde a B e vogliamo sapere cosa corrisponde a C: X = (B × C) / A."},
        ],
    },

    "finanzas": {
        "es": [
            {"q": "¿Cómo se calcula la cuota mensual de una hipoteca?", "a": "Se usa la fórmula de amortización francesa: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1], donde P es el capital, r el tipo mensual y n el número de cuotas."},
            {"q": "¿Cuál es la diferencia entre interés simple y compuesto?", "a": "El interés simple se calcula solo sobre el capital inicial: I = P×r×t. El interés compuesto se calcula sobre el capital más los intereses acumulados: A = P(1+r/f)^(f×t)."},
            {"q": "¿Cómo calculo el IVA de un precio?", "a": "IVA = precio sin IVA × (porcentaje / 100). Precio con IVA = precio sin IVA × (1 + porcentaje/100)."},
            {"q": "¿Qué es el punto de equilibrio?", "a": "El punto de equilibrio (break-even) es el número de unidades que hay que vender para cubrir exactamente todos los costes. Se calcula como: PE = Costes fijos / (Precio venta − Coste variable unitario)."},
        ],
        "en": [
            {"q": "How is a monthly mortgage payment calculated?", "a": "Using the French amortisation formula: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1], where P is principal, r the monthly rate and n the number of payments."},
            {"q": "What is the difference between simple and compound interest?", "a": "Simple interest is calculated only on the principal: I = P×r×t. Compound interest is calculated on the principal plus accumulated interest: A = P(1+r/f)^(f×t)."},
            {"q": "How do I calculate VAT on a price?", "a": "VAT = price excl. tax × (percentage / 100). Price incl. VAT = price × (1 + percentage/100)."},
            {"q": "What is the break-even point?", "a": "The break-even point is the number of units that must be sold to cover all costs: BE = Fixed costs / (Selling price − Variable cost per unit)."},
        ],
        "fr": [
            {"q": "Comment calcule-t-on la mensualité d'un prêt ?", "a": "Avec la formule d'amortissement français : C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1], où P est le capital, r le taux mensuel et n le nombre d'échéances."},
            {"q": "Quelle est la différence entre intérêt simple et composé ?", "a": "L'intérêt simple est calculé sur le capital initial : I = P×r×t. L'intérêt composé tient compte des intérêts accumulés : A = P(1+r/f)^(f×t)."},
            {"q": "Comment calculer la TVA ?", "a": "TVA = prix HT × (taux / 100). Prix TTC = prix HT × (1 + taux/100)."},
            {"q": "Qu'est-ce que le seuil de rentabilité ?", "a": "Le seuil de rentabilité est le nombre d'unités à vendre pour couvrir tous les coûts : SR = Coûts fixes / (Prix − Coût variable unitaire)."},
        ],
        "pt": [
            {"q": "Como se calcula a prestação mensal de um empréstimo?", "a": "Com a fórmula de amortização francesa: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1], onde P é o capital, r a taxa mensal e n o número de prestações."},
            {"q": "Qual é a diferença entre juro simples e composto?", "a": "O juro simples calcula-se só sobre o capital inicial: I = P×r×t. O juro composto inclui os juros acumulados: A = P(1+r/f)^(f×t)."},
            {"q": "Como calculo o IVA de um preço?", "a": "IVA = preço sem IVA × (percentagem / 100). Preço com IVA = preço × (1 + percentagem/100)."},
            {"q": "O que é o ponto de equilíbrio?", "a": "O ponto de equilíbrio é o número de unidades a vender para cobrir todos os custos: PE = Custos fixos / (Preço venda − Custo variável unitário)."},
        ],
        "de": [
            {"q": "Wie wird eine monatliche Kreditrate berechnet?", "a": "Mit der Annuitätenformel: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1], wobei P das Kapital, r der Monatszins und n die Anzahl der Raten ist."},
            {"q": "Was ist der Unterschied zwischen einfachem und Zinseszins?", "a": "Einfacher Zins auf das Anfangskapital: I = P×r×t. Zinseszins auf Kapital plus aufgelaufene Zinsen: A = P(1+r/f)^(f×t)."},
            {"q": "Wie berechne ich die Mehrwertsteuer?", "a": "MwSt. = Nettobetrag × (Satz / 100). Bruttobetrag = Nettobetrag × (1 + Satz/100)."},
            {"q": "Was ist die Gewinnschwelle (Break-Even)?", "a": "Die Gewinnschwelle ist die Stückzahl, bei der alle Kosten gedeckt sind: BE = Fixkosten / (Preis − variable Stückkosten)."},
        ],
        "it": [
            {"q": "Come si calcola la rata mensile di un mutuo?", "a": "Con la formula di ammortamento francese: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1], dove P è il capitale, r il tasso mensile e n il numero di rate."},
            {"q": "Qual è la differenza tra interesse semplice e composto?", "a": "L'interesse semplice si calcola sul capitale iniziale: I = P×r×t. L'interesse composto include gli interessi maturati: A = P(1+r/f)^(f×t)."},
            {"q": "Come si calcola l'IVA su un prezzo?", "a": "IVA = prezzo IVA esclusa × (aliquota / 100). Prezzo IVA inclusa = prezzo × (1 + aliquota/100)."},
            {"q": "Cos'è il punto di pareggio?", "a": "Il punto di pareggio è il numero di unità da vendere per coprire tutti i costi: PE = Costi fissi / (Prezzo vendita − Costo variabile unitario)."},
        ],
    },

    "salud": {
        "es": [
            {"q": "¿Qué IMC se considera normal?", "a": "Un IMC entre 18.5 y 24.9 se considera peso normal según la OMS. Por debajo de 18.5 es bajo peso; entre 25 y 29.9, sobrepeso; 30 o más, obesidad."},
            {"q": "¿Cuántas calorías necesito para adelgazar?", "a": "Para perder aproximadamente 0.5 kg por semana necesitas un déficit de 500 kcal/día respecto a tu TDEE (calorías de mantenimiento)."},
            {"q": "¿Cuánta agua debo beber al día?", "a": "La recomendación general es 33 ml por kg de peso corporal. Para una persona de 70 kg, esto equivale a 2.3 litros al día, más el extra por el ejercicio realizado."},
            {"q": "¿Qué es el metabolismo basal (BMR)?", "a": "El BMR es la cantidad de calorías que tu cuerpo quema en reposo para mantener las funciones vitales. Se calcula con la ecuación de Mifflin-St Jeor."},
        ],
        "en": [
            {"q": "What BMI is considered normal?", "a": "A BMI between 18.5 and 24.9 is considered normal weight by the WHO. Below 18.5 is underweight; 25–29.9 is overweight; 30 or above is obese."},
            {"q": "How many calories do I need to lose weight?", "a": "To lose approximately 0.5 kg per week you need a deficit of 500 kcal/day compared to your TDEE (maintenance calories)."},
            {"q": "How much water should I drink per day?", "a": "The general recommendation is 33 ml per kg of body weight. For a 70 kg person, that is 2.3 litres per day, plus extra for exercise."},
            {"q": "What is basal metabolic rate (BMR)?", "a": "BMR is the number of calories your body burns at rest to maintain vital functions. It is calculated using the Mifflin-St Jeor equation."},
        ],
        "fr": [
            {"q": "Quel IMC est considéré normal ?", "a": "Un IMC entre 18.5 et 24.9 est considéré comme normal selon l'OMS. En dessous de 18.5, sous-poids ; 25–29.9, surpoids ; 30 ou plus, obésité."},
            {"q": "Combien de calories pour maigrir ?", "a": "Pour perdre environ 0.5 kg par semaine, il faut un déficit de 500 kcal/jour par rapport à votre TDEE."},
            {"q": "Combien d'eau boire par jour ?", "a": "La recommandation générale est 33 ml par kg de poids. Pour 70 kg, c'est 2.3 litres par jour, plus l'extra pour l'exercice."},
            {"q": "Qu'est-ce que le métabolisme de base (BMR) ?", "a": "Le BMR est le nombre de calories que votre corps brûle au repos. Il est calculé avec l'équation de Mifflin-St Jeor."},
        ],
        "pt": [
            {"q": "Que IMC é considerado normal?", "a": "Um IMC entre 18.5 e 24.9 é considerado peso normal pela OMS. Abaixo de 18.5 é baixo peso; 25–29.9 é excesso de peso; 30 ou mais, obesidade."},
            {"q": "Quantas calorias preciso para emagrecer?", "a": "Para perder cerca de 0.5 kg por semana precisa de um défice de 500 kcal/dia face ao seu TDEE."},
            {"q": "Quanta água devo beber por dia?", "a": "A recomendação geral é 33 ml por kg de peso. Para 70 kg, são 2.3 litros por dia, mais o extra pelo exercício."},
            {"q": "O que é o metabolismo basal (BMR)?", "a": "O BMR é a quantidade de calorias que o organismo queima em repouso. É calculado com a equação de Mifflin-St Jeor."},
        ],
        "de": [
            {"q": "Welcher BMI gilt als normal?", "a": "Ein BMI zwischen 18.5 und 24.9 gilt laut WHO als Normalgewicht. Unter 18.5 ist Untergewicht; 25–29.9 Übergewicht; 30 oder mehr Adipositas."},
            {"q": "Wie viele Kalorien brauche ich zum Abnehmen?", "a": "Um ca. 0.5 kg pro Woche abzunehmen, benötigen Sie ein Defizit von 500 kcal/Tag gegenüber Ihrem TDEE."},
            {"q": "Wie viel Wasser sollte ich täglich trinken?", "a": "Die allgemeine Empfehlung lautet 33 ml pro kg Körpergewicht. Bei 70 kg sind das 2.3 Liter täglich, zuzüglich Sport-Extra."},
            {"q": "Was ist der Grundumsatz (BMR)?", "a": "Der BMR ist die Kalorienmenge, die Ihr Körper im Ruhezustand verbrennt. Er wird mit der Mifflin-St-Jeor-Formel berechnet."},
        ],
        "it": [
            {"q": "Quale IMC è considerato normale?", "a": "Un IMC tra 18.5 e 24.9 è considerato normale dall'OMS. Sotto 18.5 è sottopeso; 25–29.9 sovrappeso; 30 o più obesità."},
            {"q": "Quante calorie mi servono per dimagrire?", "a": "Per perdere circa 0.5 kg a settimana serve un deficit di 500 kcal/giorno rispetto al proprio TDEE."},
            {"q": "Quanta acqua devo bere al giorno?", "a": "La raccomandazione generale è 33 ml per kg di peso corporeo. Per 70 kg, sono 2.3 litri al giorno, più l'extra per l'esercizio."},
            {"q": "Cos'è il metabolismo basale (BMR)?", "a": "Il BMR è la quantità di calorie che il corpo brucia a riposo. Si calcola con l'equazione di Mifflin-St Jeor."},
        ],
    },

    "cotidiano": {
        "es": [
            {"q": "¿Cuánto se deja de propina normalmente?", "a": "En España el porcentaje habitual es 5–10%. En EE. UU. el estándar es 15–20%. Puedes ajustar el porcentaje según el servicio recibido."},
            {"q": "¿Cómo se calcula la diferencia entre dos fechas?", "a": "La diferencia en días se obtiene restando las dos fechas en milisegundos y dividiendo entre 86.400.000 (milisegundos por día)."},
            {"q": "¿Cómo calculo mi edad exacta?", "a": "Resta el año de nacimiento al año actual. Si el mes de nacimiento todavía no ha llegado este año, réstale 1 al resultado."},
        ],
        "en": [
            {"q": "How much tip is normal?", "a": "In the UK and most of Europe, 5–10% is typical. In the US, 15–20% is standard. Adjust the percentage based on the service quality."},
            {"q": "How do you calculate the difference between two dates?", "a": "Subtract the two dates in milliseconds and divide by 86,400,000 (milliseconds per day) to get the number of days."},
            {"q": "How do I calculate my exact age?", "a": "Subtract your birth year from the current year. If your birth month hasn't occurred yet this year, subtract 1 from the result."},
        ],
        "fr": [
            {"q": "Quel est le pourboire habituel ?", "a": "En France, le pourboire n'est pas obligatoire mais 5–10% est courant dans les restaurants. Aux États-Unis, le standard est 15–20%."},
            {"q": "Comment calculer la différence entre deux dates ?", "a": "Soustrayez les deux dates en millisecondes et divisez par 86 400 000 (millisecondes par jour) pour obtenir le nombre de jours."},
            {"q": "Comment calculer mon âge exact ?", "a": "Soustrayez l'année de naissance à l'année actuelle. Si le mois de naissance n'est pas encore passé cette année, soustrayez 1 au résultat."},
        ],
        "pt": [
            {"q": "Quanto se deixa de gorjeta normalmente?", "a": "Em Portugal a gorjeta não é obrigatória, mas 5–10% é habitual. Nos EUA, o padrão é 15–20%."},
            {"q": "Como se calcula a diferença entre duas datas?", "a": "Subtraia as duas datas em milissegundos e divida por 86.400.000 (milissegundos por dia) para obter o número de dias."},
            {"q": "Como calculo a minha idade exata?", "a": "Subtraia o ano de nascimento ao ano atual. Se o mês de nascimento ainda não chegou este ano, subtraia 1 ao resultado."},
        ],
        "de": [
            {"q": "Wie viel Trinkgeld ist üblich?", "a": "In Deutschland sind 5–10% üblich. In den USA ist 15–20% Standard. Passen Sie den Betrag je nach Servicequalität an."},
            {"q": "Wie berechnet man die Differenz zwischen zwei Daten?", "a": "Die Differenz in Millisekunden dividiert durch 86.400.000 (Millisekunden pro Tag) ergibt die Anzahl der Tage."},
            {"q": "Wie berechne ich mein genaues Alter?", "a": "Geburtsjahr vom aktuellen Jahr subtrahieren. Wenn der Geburtsmonat noch nicht erreicht ist, 1 abziehen."},
        ],
        "it": [
            {"q": "Quanto si lascia di mancia di solito?", "a": "In Italia la mancia non è obbligatoria, ma il 5–10% è comune. Negli USA lo standard è 15–20%."},
            {"q": "Come si calcola la differenza tra due date?", "a": "Si sottraggono le due date in millisecondi e si divide per 86.400.000 (millisecondi al giorno) per ottenere i giorni."},
            {"q": "Come calcolo la mia età esatta?", "a": "Si sottrae l'anno di nascita dall'anno corrente. Se il mese di nascita non è ancora arrivato quest'anno, si sottrae 1 al risultato."},
        ],
    },
    "estadistica": {
        "es": [
            {"q": "¿Cuál es la diferencia entre media y mediana?", "a": "La media es la suma de todos los valores dividida por la cantidad. La mediana es el valor central cuando los datos están ordenados. La mediana es más resistente a valores atípicos."},
            {"q": "¿Qué es la desviación estándar?", "a": "Mide cuánto se alejan los datos de la media. Una desviación baja indica que los datos están agrupados cerca de la media; una alta indica mayor dispersión."},
            {"q": "¿Cómo se calcula la probabilidad?", "a": "Probabilidad = casos favorables / casos totales. El resultado es un número entre 0 (imposible) y 1 (seguro). Multiplicado por 100 da el porcentaje."},
        ],
        "en": [
            {"q": "What is the difference between mean and median?", "a": "The mean is the sum of all values divided by the count. The median is the middle value when data is sorted. The median is more resistant to outliers."},
            {"q": "What is standard deviation?", "a": "It measures how spread out data is from the mean. A low standard deviation means data clusters close to the mean; a high one means greater spread."},
            {"q": "How is probability calculated?", "a": "Probability = favorable outcomes / total outcomes. The result is between 0 (impossible) and 1 (certain). Multiplied by 100 gives the percentage."},
        ],
        "fr": [
            {"q": "Quelle est la différence entre moyenne et médiane ?", "a": "La moyenne est la somme divisée par le nombre. La médiane est la valeur centrale quand les données sont triées. La médiane résiste mieux aux valeurs aberrantes."},
            {"q": "Qu'est-ce que l'écart type ?", "a": "Il mesure la dispersion des données par rapport à la moyenne. Un écart type faible indique des données groupées ; un élevé indique une grande dispersion."},
            {"q": "Comment calcule-t-on la probabilité ?", "a": "Probabilité = cas favorables / cas totaux. Le résultat est entre 0 (impossible) et 1 (certain). Multiplié par 100, on obtient le pourcentage."},
        ],
        "pt": [
            {"q": "Qual a diferença entre média e mediana?", "a": "A média é a soma dividida pela quantidade. A mediana é o valor central dos dados ordenados. A mediana é mais resistente a valores atípicos."},
            {"q": "O que é desvio padrão?", "a": "Mede o quão dispersos os dados estão em relação à média. Um desvio baixo indica dados agrupados; um alto indica maior dispersão."},
            {"q": "Como se calcula a probabilidade?", "a": "Probabilidade = casos favoráveis / casos totais. O resultado vai de 0 (impossível) a 1 (certo). Multiplicado por 100 dá a percentagem."},
        ],
        "de": [
            {"q": "Was ist der Unterschied zwischen Mittelwert und Median?", "a": "Der Mittelwert ist die Summe geteilt durch die Anzahl. Der Median ist der Mittelwert bei sortierten Daten. Der Median ist robuster gegen Ausreißer."},
            {"q": "Was ist die Standardabweichung?", "a": "Sie misst die Streuung der Daten um den Mittelwert. Eine niedrige Standardabweichung bedeutet dicht beieinander liegende Daten."},
            {"q": "Wie wird Wahrscheinlichkeit berechnet?", "a": "Wahrscheinlichkeit = günstige / mögliche Ergebnisse. Das Ergebnis liegt zwischen 0 (unmöglich) und 1 (sicher)."},
        ],
        "it": [
            {"q": "Qual è la differenza tra media e mediana?", "a": "La media è la somma divisa per la quantità. La mediana è il valore centrale con dati ordinati. La mediana resiste meglio ai valori anomali."},
            {"q": "Cos'è la deviazione standard?", "a": "Misura quanto i dati si discostano dalla media. Una deviazione bassa indica dati raggruppati; una alta indica maggiore dispersione."},
            {"q": "Come si calcola la probabilità?", "a": "Probabilità = casi favorevoli / casi totali. Il risultato è tra 0 (impossibile) e 1 (certo). Moltiplicato per 100 dà la percentuale."},
        ],
    },
    "ciencia": {
        "es": [
            {"q": "¿Cuál es la fórmula de la velocidad?", "a": "Velocidad = distancia / tiempo (v = d/t). En unidades SI se mide en m/s. Para convertir a km/h, multiplica por 3.6."},
            {"q": "¿Qué es la fuerza según Newton?", "a": "Fuerza = masa × aceleración (F = m×a). Se mide en Newtons (N). 1 N es la fuerza necesaria para acelerar 1 kg a 1 m/s²."},
            {"q": "¿Cómo se calcula la energía cinética?", "a": "Energía cinética = ½ × masa × velocidad² (KE = ½mv²). Se mide en julios (J). Depende de la masa y del cuadrado de la velocidad."},
        ],
        "en": [
            {"q": "What is the speed formula?", "a": "Speed = distance / time (v = d/t). In SI units it's measured in m/s. To convert to km/h, multiply by 3.6."},
            {"q": "What is force according to Newton?", "a": "Force = mass × acceleration (F = m×a). Measured in Newtons (N). 1 N is the force to accelerate 1 kg at 1 m/s²."},
            {"q": "How is kinetic energy calculated?", "a": "Kinetic energy = ½ × mass × velocity² (KE = ½mv²). Measured in joules (J). It depends on mass and the square of velocity."},
        ],
        "fr": [
            {"q": "Quelle est la formule de la vitesse ?", "a": "Vitesse = distance / temps (v = d/t). En unités SI, elle se mesure en m/s. Pour convertir en km/h, multipliez par 3,6."},
            {"q": "Qu'est-ce que la force selon Newton ?", "a": "Force = masse × accélération (F = m×a). Mesurée en Newtons (N). 1 N accélère 1 kg à 1 m/s²."},
            {"q": "Comment calcule-t-on l'énergie cinétique ?", "a": "Énergie cinétique = ½ × masse × vitesse² (KE = ½mv²). Mesurée en joules (J)."},
        ],
        "pt": [
            {"q": "Qual é a fórmula da velocidade?", "a": "Velocidade = distância / tempo (v = d/t). Em unidades SI mede-se em m/s. Para converter em km/h, multiplique por 3,6."},
            {"q": "O que é força segundo Newton?", "a": "Força = massa × aceleração (F = m×a). Mede-se em Newtons (N). 1 N acelera 1 kg a 1 m/s²."},
            {"q": "Como se calcula a energia cinética?", "a": "Energia cinética = ½ × massa × velocidade² (KE = ½mv²). Mede-se em joules (J)."},
        ],
        "de": [
            {"q": "Wie lautet die Geschwindigkeitsformel?", "a": "Geschwindigkeit = Strecke / Zeit (v = s/t). In SI-Einheiten in m/s. Umrechnung in km/h: mit 3,6 multiplizieren."},
            {"q": "Was ist Kraft nach Newton?", "a": "Kraft = Masse × Beschleunigung (F = m×a). Gemessen in Newton (N). 1 N beschleunigt 1 kg auf 1 m/s²."},
            {"q": "Wie berechnet man kinetische Energie?", "a": "Kinetische Energie = ½ × Masse × Geschwindigkeit² (KE = ½mv²). Gemessen in Joule (J)."},
        ],
        "it": [
            {"q": "Qual è la formula della velocità?", "a": "Velocità = distanza / tempo (v = d/t). In unità SI si misura in m/s. Per convertire in km/h, moltiplica per 3,6."},
            {"q": "Cos'è la forza secondo Newton?", "a": "Forza = massa × accelerazione (F = m×a). Si misura in Newton (N). 1 N accelera 1 kg a 1 m/s²."},
            {"q": "Come si calcola l'energia cinetica?", "a": "Energia cinetica = ½ × massa × velocità² (KE = ½mv²). Si misura in joule (J)."},
        ],
    },
    "conversion": {
        "es": [
            {"q": "¿Cómo convierto metros a pies?", "a": "1 metro = 3.28084 pies. Multiplica los metros por 3.28084 para obtener el equivalente en pies."},
            {"q": "¿Cuántos kilogramos tiene una libra?", "a": "1 libra = 0.453592 kg. Para convertir libras a kg, multiplica por 0.453592. Para kg a libras, multiplica por 2.20462."},
            {"q": "¿Cómo paso de Celsius a Fahrenheit?", "a": "°F = °C × 9/5 + 32. Por ejemplo, 25°C = 25 × 9/5 + 32 = 77°F."},
        ],
        "en": [
            {"q": "How do I convert meters to feet?", "a": "1 meter = 3.28084 feet. Multiply meters by 3.28084 to get the equivalent in feet."},
            {"q": "How many kilograms in a pound?", "a": "1 pound = 0.453592 kg. To convert pounds to kg, multiply by 0.453592. For kg to pounds, multiply by 2.20462."},
            {"q": "How do I convert Celsius to Fahrenheit?", "a": "°F = °C × 9/5 + 32. For example, 25°C = 25 × 9/5 + 32 = 77°F."},
        ],
        "fr": [
            {"q": "Comment convertir des mètres en pieds ?", "a": "1 mètre = 3,28084 pieds. Multipliez les mètres par 3,28084."},
            {"q": "Combien de kilogrammes dans une livre ?", "a": "1 livre = 0,453592 kg. Multipliez par 0,453592 pour les livres en kg."},
            {"q": "Comment passer de Celsius à Fahrenheit ?", "a": "°F = °C × 9/5 + 32. Par exemple, 25°C = 77°F."},
        ],
        "pt": [
            {"q": "Como converter metros em pés?", "a": "1 metro = 3,28084 pés. Multiplique metros por 3,28084."},
            {"q": "Quantos quilogramas tem uma libra?", "a": "1 libra = 0,453592 kg. Multiplique por 0,453592 para converter libras em kg."},
            {"q": "Como converter Celsius para Fahrenheit?", "a": "°F = °C × 9/5 + 32. Por exemplo, 25°C = 77°F."},
        ],
        "de": [
            {"q": "Wie rechne ich Meter in Fuß um?", "a": "1 Meter = 3,28084 Fuß. Meter mit 3,28084 multiplizieren."},
            {"q": "Wie viele Kilogramm hat ein Pfund?", "a": "1 Pfund = 0,453592 kg. Mit 0,453592 multiplizieren für Pfund zu kg."},
            {"q": "Wie rechne ich Celsius in Fahrenheit um?", "a": "°F = °C × 9/5 + 32. Zum Beispiel: 25°C = 77°F."},
        ],
        "it": [
            {"q": "Come convertire metri in piedi?", "a": "1 metro = 3,28084 piedi. Moltiplica i metri per 3,28084."},
            {"q": "Quanti chilogrammi ha una libbra?", "a": "1 libbra = 0,453592 kg. Moltiplica per 0,453592 per convertire libbre in kg."},
            {"q": "Come convertire Celsius in Fahrenheit?", "a": "°F = °C × 9/5 + 32. Ad esempio, 25°C = 77°F."},
        ],
    },
    "deportes": {
        "es": [
            {"q": "¿Qué es el ritmo de carrera?", "a": "Es el tiempo que tardas en recorrer 1 km. Se calcula dividiendo el tiempo total entre la distancia. Se expresa en min/km."},
            {"q": "¿Qué son los MET?", "a": "MET (Equivalentes Metabólicos) mide la intensidad del ejercicio. Caminar = 3 MET, correr = 8-12 MET, nadar = 6-10 MET."},
            {"q": "¿Cómo se calcula la frecuencia cardíaca máxima?", "a": "La fórmula más común es FC máx = 220 − edad. La fórmula de Tanaka (208 − 0.7 × edad) es más precisa para personas mayores de 40 años."},
        ],
        "en": [
            {"q": "What is running pace?", "a": "It's the time it takes to cover 1 km. Calculated by dividing total time by distance. Expressed in min/km."},
            {"q": "What are METs?", "a": "MET (Metabolic Equivalents) measures exercise intensity. Walking = 3 MET, running = 8-12 MET, swimming = 6-10 MET."},
            {"q": "How is maximum heart rate calculated?", "a": "The most common formula is Max HR = 220 − age. Tanaka's formula (208 − 0.7 × age) is more accurate for people over 40."},
        ],
        "fr": [
            {"q": "Qu'est-ce que l'allure de course ?", "a": "C'est le temps pour parcourir 1 km. Calculé en divisant le temps total par la distance. Exprimé en min/km."},
            {"q": "Que sont les MET ?", "a": "MET (Équivalents Métaboliques) mesure l'intensité de l'exercice. Marche = 3 MET, course = 8-12 MET, natation = 6-10 MET."},
            {"q": "Comment calcule-t-on la FC max ?", "a": "FC max = 220 − âge. La formule de Tanaka (208 − 0,7 × âge) est plus précise pour les plus de 40 ans."},
        ],
        "pt": [
            {"q": "O que é o ritmo de corrida?", "a": "É o tempo para percorrer 1 km. Calcula-se dividindo o tempo total pela distância. Expresso em min/km."},
            {"q": "O que são METs?", "a": "MET (Equivalentes Metabólicos) mede a intensidade do exercício. Caminhada = 3 MET, corrida = 8-12 MET, natação = 6-10 MET."},
            {"q": "Como se calcula a frequência cardíaca máxima?", "a": "FC máx = 220 − idade. A fórmula de Tanaka (208 − 0,7 × idade) é mais precisa para maiores de 40 anos."},
        ],
        "de": [
            {"q": "Was ist Laufpacing?", "a": "Die Zeit für 1 km. Berechnet als Gesamtzeit geteilt durch Strecke. Angegeben in min/km."},
            {"q": "Was sind METs?", "a": "MET (Metabolische Äquivalente) misst die Übungsintensität. Gehen = 3 MET, Laufen = 8-12 MET, Schwimmen = 6-10 MET."},
            {"q": "Wie wird die maximale Herzfrequenz berechnet?", "a": "Max Puls = 220 − Alter. Tanaka-Formel (208 − 0,7 × Alter) ist genauer für über 40-Jährige."},
        ],
        "it": [
            {"q": "Cos'è il ritmo di corsa?", "a": "È il tempo per percorrere 1 km. Si calcola dividendo il tempo totale per la distanza. Espresso in min/km."},
            {"q": "Cosa sono i MET?", "a": "MET (Equivalente Metabolico) misura l'intensità dell'esercizio. Camminata = 3 MET, corsa = 8-12 MET, nuoto = 6-10 MET."},
            {"q": "Come si calcola la frequenza cardiaca massima?", "a": "FC max = 220 − età. La formula di Tanaka (208 − 0,7 × età) è più precisa per over 40."},
        ],
    },
}


# ── Wastage input labels per language ────────────────────────────────────────

WASTAGE_LABEL = {
    "es": "Merma / Desperdicio (%)",
    "en": "Wastage Allowance (%)",
    "fr": "Perte / Gâchis (%)",
    "pt": "Perda / Desperdício (%)",
    "de": "Verschnitt / Verlust (%)",
    "it": "Perdita / Scarto (%)",
}

WASTAGE_PLACEHOLDER = {
    "es": "ej. 10",
    "en": "e.g. 10",
    "fr": "ex. 10",
    "pt": "ex. 10",
    "de": "z.B. 10",
    "it": "es. 10",
}

NET_LABEL = {
    "es": "Neto (sin desperdicio)",
    "en": "Net (no wastage)",
    "fr": "Net (sans perte)",
    "pt": "Líquido (sem perda)",
    "de": "Netto (ohne Verlust)",
    "it": "Netto (senza perdita)",
}

TOTAL_LABEL = {
    "es": "Total a comprar (+{pct}% merma)",
    "en": "Total to buy (+{pct}% wastage)",
    "fr": "Total à acheter (+{pct}% perte)",
    "pt": "Total a comprar (+{pct}% perda)",
    "de": "Zu kaufen insgesamt (+{pct}% Verlust)",
    "it": "Totale da acquistare (+{pct}% perdita)",
}

HOW_TO_TITLE = {
    "es": "¿Cómo usar esta calculadora?",
    "en": "How to Use This Calculator",
    "fr": "Comment utiliser cette calculatrice ?",
    "pt": "Como usar esta calculadora?",
    "de": "Anleitung zur Verwendung",
    "it": "Come usare questo calcolatore?",
}

FAQ_TITLE = {
    "es": "Preguntas frecuentes",
    "en": "Frequently Asked Questions",
    "fr": "Questions fréquemment posées",
    "pt": "Perguntas frequentes",
    "de": "Häufig gestellte Fragen",
    "it": "Domande frequenti",
}

INTRO_TEMPLATES = {
    "es": (
        "La <strong>{name}</strong> es una calculadora gratuita y precisa. {desc} "
        "Introduce los valores, obtén el resultado al instante y consulta la fórmula con ejemplos detallados."
    ),
    "en": (
        "The <strong>{name}</strong> is a free and accurate calculator. {desc} "
        "Enter your values, get instant results, and explore the formula with detailed examples."
    ),
    "fr": (
        "Le <strong>{name}</strong> est une calculatrice gratuite et précise. {desc} "
        "Saisissez vos valeurs, obtenez un résultat instantané et consultez la formule avec des exemples."
    ),
    "pt": (
        "A <strong>{name}</strong> é uma calculadora gratuita e precisa. {desc} "
        "Insira os valores, obtenha o resultado instantaneamente e explore a fórmula com exemplos."
    ),
    "de": (
        "Der <strong>{name}</strong> ist ein kostenloser und genauer Rechner. {desc} "
        "Geben Sie die Werte ein, erhalten Sie sofortige Ergebnisse und erkunden Sie die Formel mit Beispielen."
    ),
    "it": (
        "Il <strong>{name}</strong> è una calcolatrice gratuita e precisa. {desc} "
        "Inserisci i valori, ottieni il risultato immediatamente e consulta la formula con esempi dettagliati."
    ),
}


def generate_intro(calc_id: str, lang: str, name: str, desc: str, block_slug: str = "") -> str:
    block_tpls = BLOCK_INTRO_TEMPLATES.get(block_slug, {})
    tpl = block_tpls.get(lang) or INTRO_TEMPLATES.get(lang, INTRO_TEMPLATES["en"])
    return tpl.format(name=name, desc=desc)


VARIANT_INTRO_TEMPLATES = {
    "es": (
        "<strong>{title}</strong>. {desc} "
        "Introduce los valores en el formulario y obtén el resultado al instante, "
        "incluyendo materiales desglosados y un margen de merma ajustable."
    ),
    "en": (
        "<strong>{title}</strong>. {desc} "
        "Enter your values in the form and get instant results, "
        "including a full materials breakdown and an adjustable wastage allowance."
    ),
    "fr": (
        "<strong>{title}</strong>. {desc} "
        "Saisissez vos valeurs dans le formulaire et obtenez un résultat instantané, "
        "avec une décomposition complète des matériaux et un taux de perte ajustable."
    ),
    "pt": (
        "<strong>{title}</strong>. {desc} "
        "Insira os valores no formulário e obtenha resultados instantâneos, "
        "incluindo detalhamento completo dos materiais e uma margem de perda ajustável."
    ),
    "de": (
        "<strong>{title}</strong>. {desc} "
        "Geben Sie Ihre Werte in das Formular ein und erhalten Sie sofort Ergebnisse, "
        "einschließlich einer vollständigen Materialaufstellung und eines anpassbaren Verschnittfaktors."
    ),
    "it": (
        "<strong>{title}</strong>. {desc} "
        "Inserisci i valori nel modulo e ottieni risultati istantanei, "
        "inclusa una ripartizione completa dei materiali e un margine di perdita regolabile."
    ),
}


QUICK_ANSWER_TEMPLATES = {
    "es": " <strong>Respuesta rápida:</strong> {answer}",
    "en": " <strong>Quick answer:</strong> {answer}",
    "fr": " <strong>Réponse rapide :</strong> {answer}",
    "pt": " <strong>Resposta rápida:</strong> {answer}",
    "de": " <strong>Schnelle Antwort:</strong> {answer}",
    "it": " <strong>Risposta rapida:</strong> {answer}",
}


def generate_variant_intro(title: str, desc: str, lang: str, quick_answer: str = "") -> str:
    tpl = VARIANT_INTRO_TEMPLATES.get(lang, VARIANT_INTRO_TEMPLATES["en"])
    base = tpl.format(title=title, desc=desc)
    if quick_answer:
        qa_tpl = QUICK_ANSWER_TEMPLATES.get(lang, QUICK_ANSWER_TEMPLATES["en"])
        base += qa_tpl.format(answer=quick_answer)
    return base


def generate_how_to(block_slug: str, lang: str) -> list:
    block_steps = HOWTO.get(block_slug, {})
    return block_steps.get(lang, block_steps.get("en", []))


# ── Formula explanation per block per language ────────────────────────────────

FORMULA_EXPLAINED = {
    "estructuras": {
        "es": "El volumen se obtiene multiplicando largo × ancho × altura. Los materiales se calculan con las dosificaciones estándar EN 206: ~350 kg de cemento, 0.65 m³ de arena y 0.90 m³ de grava por m³ de hormigón; el acero se estima con la cuantía introducida en kg/m³.",
        "en": "Volume = length × width × height. Materials are derived using EN 206 standard ratios: ~350 kg cement, 0.65 m³ sand and 0.90 m³ gravel per m³ of concrete; steel is estimated from the kg/m³ ratio you enter.",
        "fr": "Volume = longueur × largeur × hauteur. Les matériaux sont calculés selon les dosages EN 206 : ~350 kg de ciment, 0,65 m³ de sable et 0,90 m³ de gravier par m³ de béton ; l'acier est estimé à partir du taux saisi en kg/m³.",
        "pt": "Volume = comprimento × largura × altura. Os materiais são calculados com dosagens EN 206: ~350 kg de cimento, 0,65 m³ de areia e 0,90 m³ de brita por m³ de concreto; o aço é estimado pela taxa inserida em kg/m³.",
        "de": "Volumen = Länge × Breite × Höhe. Materialien werden nach EN 206 berechnet: ~350 kg Zement, 0,65 m³ Sand und 0,90 m³ Kies pro m³ Beton; Stahl wird aus dem eingegebenen kg/m³-Wert ermittelt.",
        "it": "Volume = lunghezza × larghezza × altezza. I materiali sono calcolati con i dosaggi EN 206: ~350 kg di cemento, 0,65 m³ di sabbia e 0,90 m³ di ghiaia per m³ di calcestruzzo; l'acciaio è stimato dalla percentuale inserita in kg/m³.",
    },
    "mamposteria": {
        "es": "El número de piezas se calcula dividiendo el área del muro entre el área de cada pieza (con juntas). El mortero se estima en 25–30 kg por m² de muro para juntas de 10 mm, ajustado por el coeficiente de dosificación cemento:arena.",
        "en": "The number of units is calculated by dividing the wall area by each unit's area (including joints). Mortar is estimated at 25–30 kg per m² of wall for 10 mm joints, adjusted by the cement:sand dosing ratio.",
        "fr": "Le nombre de pièces est obtenu en divisant la surface du mur par la surface de chaque pièce (joints compris). Le mortier est estimé à 25–30 kg par m² de mur pour des joints de 10 mm.",
        "pt": "O número de peças é calculado dividindo a área da parede pela área de cada peça (com juntas). A argamassa é estimada em 25–30 kg por m² de parede para juntas de 10 mm.",
        "de": "Die Stückzahl ergibt sich aus der Wandfläche geteilt durch die Fläche jedes Elements (inkl. Fugen). Mörtel wird mit 25–30 kg/m² Wandfläche für 10-mm-Fugen angesetzt.",
        "it": "Il numero di elementi si calcola dividendo la superficie del muro per la superficie di ogni elemento (giunti inclusi). La malta è stimata a 25–30 kg per m² di parete per giunti da 10 mm.",
    },
    "pavimentos": {
        "es": "Las piezas necesarias se calculan como: área ÷ área de cada pieza. La lechada se estima según el ancho de junta y el perímetro total de piezas; el adhesivo según el rendimiento del producto (kg/m²) especificado en ficha técnica.",
        "en": "Units needed = floor area ÷ tile area. Grout is estimated from joint width and total tile perimeter; adhesive from the product yield (kg/m²) stated on the technical datasheet.",
        "fr": "Pièces nécessaires = surface ÷ surface d'une pièce. Le coulis est estimé à partir de la largeur de joint et du périmètre total des pièces ; la colle selon le rendement produit (kg/m²).",
        "pt": "Peças necessárias = área ÷ área de cada peça. O rejunte é estimado pela largura da junta e o perímetro total das peças; a cola pelo rendimento do produto (kg/m²).",
        "de": "Benötigte Stücke = Fläche ÷ Fliesenfläche. Fugenmasse wird aus Fugenbreite und Gesamtumfang der Fliesen berechnet; Kleber nach Ergiebigkeit (kg/m²) laut Datenblatt.",
        "it": "Pezzi necessari = area ÷ area di ogni pezzo. Lo stucco è stimato dalla larghezza della fugatura e dal perimetro totale; l'adesivo dalla resa del prodotto (kg/m²).",
    },
    "fontaneria": {
        "es": "El caudal se calcula con la fórmula de Hazen-Williams o Darcy-Weisbach según el diámetro y la longitud de la tubería. La pérdida de presión se estima como: ΔP = f × (L/D) × (ρv²/2), donde f es el factor de fricción de Darcy.",
        "en": "Flow rate is calculated using Hazen-Williams or Darcy-Weisbach equations depending on pipe diameter and length. Pressure loss is estimated as: ΔP = f × (L/D) × (ρv²/2), where f is the Darcy friction factor.",
        "fr": "Le débit est calculé avec Hazen-Williams ou Darcy-Weisbach selon le diamètre et la longueur. La perte de pression est : ΔP = f × (L/D) × (ρv²/2), où f est le facteur de friction de Darcy.",
        "pt": "A vazão é calculada com Hazen-Williams ou Darcy-Weisbach conforme o diâmetro e o comprimento da tubulação. A perda de carga: ΔP = f × (L/D) × (ρv²/2).",
        "de": "Der Durchfluss wird nach Hazen-Williams oder Darcy-Weisbach berechnet. Druckverlust: ΔP = f × (L/D) × (ρv²/2), wobei f der Darcy-Reibungsbeiwert ist.",
        "it": "La portata è calcolata con Hazen-Williams o Darcy-Weisbach. La perdita di pressione: ΔP = f × (L/D) × (ρv²/2), dove f è il fattore di attrito di Darcy.",
    },
    "electricidad": {
        "es": "La sección del cable se calcula con la fórmula S = (2 × L × I) / (σ × ΔU), donde L es la longitud, I la intensidad, σ la conductividad del cobre (56 S·m/mm²) y ΔU la caída de tensión máxima permitida (normalmente 3–5 %).",
        "en": "Cable cross-section is calculated as S = (2 × L × I) / (σ × ΔU), where L is the length, I the current, σ the conductivity of copper (56 S·m/mm²) and ΔU the maximum permitted voltage drop (usually 3–5 %).",
        "fr": "La section du câble est calculée par S = (2 × L × I) / (σ × ΔU), où L est la longueur, I l'intensité, σ la conductivité du cuivre (56 S·m/mm²) et ΔU la chute de tension maximale autorisée (3–5 %).",
        "pt": "A seção do cabo é calculada por S = (2 × L × I) / (σ × ΔU), onde L é o comprimento, I a corrente, σ a condutividade do cobre (56 S·m/mm²) e ΔU a queda de tensão máxima (3–5 %).",
        "de": "Kabelquerschnitt: S = (2 × L × I) / (σ × ΔU), wobei L die Länge, I die Stromstärke, σ die Leitfähigkeit von Kupfer (56 S·m/mm²) und ΔU der max. Spannungsfall (3–5 %) ist.",
        "it": "Sezione cavo: S = (2 × L × I) / (σ × ΔU), dove L è la lunghezza, I la corrente, σ la conduttività del rame (56 S·m/mm²) e ΔU la caduta di tensione massima (3–5 %).",
    },
    "climatizacion": {
        "es": "La potencia necesaria se calcula como Q = U × A × ΔT, donde U es el coeficiente de transmisión térmica (W/m²K), A el área del cerramiento y ΔT la diferencia de temperatura interior-exterior. Se suman pérdidas por renovación de aire e infiltraciones.",
        "en": "Required power = Q = U × A × ΔT, where U is the thermal transmittance (W/m²K), A the envelope area and ΔT the indoor-outdoor temperature difference. Air renewal and infiltration losses are added.",
        "fr": "Puissance nécessaire : Q = U × A × ΔT, où U est la transmittance thermique (W/m²K), A la surface de l'enveloppe et ΔT la différence de température intérieur-extérieur. Les pertes par renouvellement d'air s'ajoutent.",
        "pt": "Potência necessária: Q = U × A × ΔT, onde U é a transmitância térmica (W/m²K), A a área da envolvente e ΔT a diferença de temperatura interior-exterior. Adicionam-se perdas por renovação de ar.",
        "de": "Erforderliche Leistung: Q = U × A × ΔT, wobei U der Wärmedurchgangskoeffizient (W/m²K), A die Gebäudehüllfläche und ΔT die Innen-Außen-Temperaturdifferenz ist. Lüftungsverluste werden addiert.",
        "it": "Potenza necessaria: Q = U × A × ΔT, dove U è la trasmittanza termica (W/m²K), A l'area dell'involucro e ΔT la differenza di temperatura interno-esterno. Si aggiungono le perdite per ricambio d'aria.",
    },
    "carpinteria": {
        "es": "El volumen de madera se calcula multiplicando largo × ancho × grosor de cada pieza, sumando todas las unidades. El peso se obtiene multiplicando el volumen total por la densidad de la especie (p. ej.: pino 500 kg/m³, roble 700 kg/m³).",
        "en": "Timber volume = length × width × thickness per piece, summed over all units. Weight = total volume × species density (e.g. pine 500 kg/m³, oak 700 kg/m³).",
        "fr": "Volume de bois = longueur × largeur × épaisseur de chaque pièce, additionné pour toutes les unités. Poids = volume total × densité de l'essence (ex. : pin 500 kg/m³, chêne 700 kg/m³).",
        "pt": "Volume de madeira = comprimento × largura × espessura de cada peça, somando todas as unidades. Peso = volume total × densidade da espécie (ex.: pinheiro 500 kg/m³, carvalho 700 kg/m³).",
        "de": "Holzvolumen = Länge × Breite × Dicke je Stück, summiert über alle Einheiten. Gewicht = Gesamtvolumen × Rohdichte der Holzart (z. B. Kiefer 500 kg/m³, Eiche 700 kg/m³).",
        "it": "Volume legno = lunghezza × larghezza × spessore per pezzo, sommato per tutte le unità. Peso = volume totale × densità della specie (es. pino 500 kg/m³, rovere 700 kg/m³).",
    },
    "pintura": {
        "es": "Los litros necesarios se calculan como: litros = área / rendimiento (m²/L) × número de manos. El rendimiento está indicado en la ficha técnica del producto (habitual: 10–14 m²/L). Se añade el porcentaje de merma para calcular la cantidad total a comprar.",
        "en": "Litres needed = area / coverage (m²/L) × number of coats. Coverage is stated on the product datasheet (typical: 10–14 m²/L). The wastage % is added to determine the total amount to purchase.",
        "fr": "Litres nécessaires = surface / rendement (m²/L) × nombre de couches. Le rendement est indiqué sur la fiche technique (habituel : 10–14 m²/L). Le taux de perte est ajouté pour calculer la quantité totale à acheter.",
        "pt": "Litros necessários = área / rendimento (m²/L) × número de demãos. O rendimento está na ficha técnica (habitual: 10–14 m²/L). A % de perda é adicionada para a quantidade total a comprar.",
        "de": "Benötigte Liter = Fläche / Ergiebigkeit (m²/L) × Anstrichanzahl. Die Ergiebigkeit steht im Produktdatenblatt (üblich: 10–14 m²/L). Der Verschnittfaktor wird zur Ermittlung der Gesamtmenge addiert.",
        "it": "Litri necessari = area / resa (m²/L) × numero di mani. La resa è indicata nella scheda tecnica (tipica: 10–14 m²/L). La % di perdita è aggiunta per calcolare la quantità totale da acquistare.",
    },
    "gestion": {
        "es": "El precio de venta se calcula como: PV = Coste directo × (1 + Gastos generales%) × (1 + Beneficio%) × (1 + IVA%). La tarifa horaria se obtiene dividiendo los costes fijos anuales entre las horas facturables y añadiendo el beneficio deseado.",
        "en": "Selling price = Direct cost × (1 + Overhead%) × (1 + Profit%) × (1 + VAT%). Hourly rate = annual fixed costs ÷ billable hours + desired profit margin.",
        "fr": "Prix de vente = Coût direct × (1 + Frais généraux%) × (1 + Bénéfice%) × (1 + TVA%). Taux horaire = coûts fixes annuels ÷ heures facturables + marge bénéficiaire souhaitée.",
        "pt": "Preço de venda = Custo direto × (1 + Despesas gerais%) × (1 + Lucro%) × (1 + IVA%). Tarifa horária = custos fixos anuais ÷ horas faturáveis + margem de lucro desejada.",
        "de": "Verkaufspreis = Direktkosten × (1 + Gemeinkosten%) × (1 + Gewinn%) × (1 + MwSt%). Stundensatz = jährliche Fixkosten ÷ abrechenbare Stunden + gewünschte Gewinnmarge.",
        "it": "Prezzo di vendita = Costo diretto × (1 + Spese generali%) × (1 + Utile%) × (1 + IVA%). Tariffa oraria = costi fissi annui ÷ ore fatturabili + margine di utile desiderato.",
    },
    "matematicas": {
        "es": "El porcentaje se calcula como: resultado = (valor × porcentaje) / 100. El cambio porcentual entre dos valores: cambio = ((final − inicial) / |inicial|) × 100. El teorema de Pitágoras: c² = a² + b², por lo que c = √(a² + b²). La regla de tres directa: si A → B, entonces C → X = (B × C) / A.",
        "en": "Percentage result = (value × percentage) / 100. Percentage change = ((final − initial) / |initial|) × 100. Pythagorean theorem: c² = a² + b², so c = √(a² + b²). Direct rule of three: if A → B then C → X = (B × C) / A.",
        "fr": "Résultat pourcentage = (valeur × pourcentage) / 100. Variation = ((final − initial) / |initial|) × 100. Théorème de Pythagore : c² = a² + b², donc c = √(a² + b²). Règle de trois : si A → B alors C → X = (B × C) / A.",
        "pt": "Resultado percentagem = (valor × percentagem) / 100. Variação = ((final − inicial) / |inicial|) × 100. Teorema de Pitágoras: c² = a² + b², logo c = √(a² + b²). Regra de três: se A → B então C → X = (B × C) / A.",
        "de": "Prozentwert = (Wert × Prozentsatz) / 100. Prozentuale Änderung = ((End − Anfang) / |Anfang|) × 100. Satz des Pythagoras: c² = a² + b², also c = √(a² + b²). Dreisatz: wenn A → B, dann C → X = (B × C) / A.",
        "it": "Risultato percentuale = (valore × percentuale) / 100. Variazione = ((finale − iniziale) / |iniziale|) × 100. Teorema di Pitagora: c² = a² + b², quindi c = √(a² + b²). Regola del tre: se A → B allora C → X = (B × C) / A.",
    },
    "finanzas": {
        "es": "La cuota mensual de un préstamo o hipoteca se calcula con la fórmula de amortización francesa: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1], donde P es el capital, r el tipo de interés mensual y n el número de cuotas. El interés compuesto: A = P(1 + r/f)^(f×t). El IVA: precio con IVA = precio × (1 + IVA/100).",
        "en": "Monthly loan/mortgage payment uses the French amortisation formula: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1], where P is principal, r the monthly interest rate and n the number of payments. Compound interest: A = P(1 + r/f)^(f×t). VAT: price with tax = price × (1 + VAT/100).",
        "fr": "La mensualité d'un prêt ou d'une hypothèque utilise la formule d'amortissement français : C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1]. L'intérêt composé : A = P(1 + r/f)^(f×t). TVA : prix TTC = prix × (1 + TVA/100).",
        "pt": "A prestação mensal usa a fórmula de amortização francesa: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1]. Juros compostos: A = P(1 + r/f)^(f×t). IVA: preço com IVA = preço × (1 + IVA/100).",
        "de": "Monatliche Kreditrate nach der Annuitätenformel: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1]. Zinseszins: A = P(1 + r/f)^(f×t). MwSt.: Bruttopreis = Nettopreis × (1 + MwSt./100).",
        "it": "La rata mensile usa la formula di ammortamento francese: C = P × [r(1+r)ⁿ] / [(1+r)ⁿ − 1]. Interesse composto: A = P(1 + r/f)^(f×t). IVA: prezzo IVA inclusa = prezzo × (1 + IVA/100).",
    },
    "salud": {
        "es": "El IMC se calcula como: IMC = peso(kg) / altura(m)². Las calorías de mantenimiento (TDEE) usan la ecuación de Mifflin-St Jeor: Hombres: BMR = 10P + 6.25H − 5E + 5; Mujeres: BMR = 10P + 6.25H − 5E − 161. El TDEE = BMR × factor de actividad (1.2–1.9). La ingesta de agua base se estima en 33 ml/kg de peso corporal.",
        "en": "BMI = weight(kg) / height(m)². Daily calorie maintenance (TDEE) uses the Mifflin-St Jeor equation: Men: BMR = 10W + 6.25H − 5A + 5; Women: BMR = 10W + 6.25H − 5A − 161. TDEE = BMR × activity factor (1.2–1.9). Base water intake is estimated at 33 ml/kg of body weight.",
        "fr": "IMC = poids(kg) / taille(m)². Les calories journalières (TDEE) utilisent Mifflin-St Jeor : Hommes : BMR = 10P + 6.25H − 5E + 5 ; Femmes : BMR = 10P + 6.25H − 5E − 161. TDEE = BMR × facteur d'activité (1.2–1.9). L'hydratation de base : 33 ml/kg.",
        "pt": "IMC = peso(kg) / altura(m)². Calorias diárias (TDEE) usa Mifflin-St Jeor: Homens: BMR = 10P + 6.25H − 5I + 5; Mulheres: BMR = 10P + 6.25H − 5I − 161. TDEE = BMR × fator atividade (1.2–1.9). Ingestão base de água: 33 ml/kg.",
        "de": "BMI = Gewicht(kg) / Körpergröße(m)². TDEE nach Mifflin-St Jeor: Männer: BMR = 10G + 6.25H − 5A + 5; Frauen: BMR = 10G + 6.25H − 5A − 161. TDEE = BMR × Aktivitätsfaktor (1,2–1,9). Basaler Wasserbedarf: 33 ml/kg Körpergewicht.",
        "it": "IMC = peso(kg) / altezza(m)². TDEE con Mifflin-St Jeor: Uomini: BMR = 10P + 6.25H − 5E + 5; Donne: BMR = 10P + 6.25H − 5E − 161. TDEE = BMR × fattore attività (1.2–1.9). Fabbisogno idrico base: 33 ml/kg di peso corporeo.",
    },
    "cotidiano": {
        "es": "La propina se calcula como: propina = total × (%) / 100; importe por persona = (total + propina) / n personas. La edad exacta se obtiene restando la fecha de nacimiento a la fecha actual. La diferencia entre fechas: días = (fecha2 − fecha1) en milisegundos / 86.400.000.",
        "en": "Tip = total × (%) / 100; per person = (total + tip) / n people. Exact age = current date − birth date. Date difference: days = (date2 − date1) in milliseconds / 86,400,000.",
        "fr": "Pourboire = total × (%) / 100 ; par personne = (total + pourboire) / n personnes. Âge exact = date actuelle − date de naissance. Différence de dates : jours = (date2 − date1) en millisecondes / 86 400 000.",
        "pt": "Gorjeta = total × (%) / 100; por pessoa = (total + gorjeta) / n pessoas. Idade exata = data atual − data de nascimento. Diferença de datas: dias = (data2 − data1) em milissegundos / 86.400.000.",
        "de": "Trinkgeld = Betrag × (%) / 100; pro Person = (Betrag + Trinkgeld) / n Personen. Genaues Alter = aktuelles Datum − Geburtsdatum. Datumsdifferenz: Tage = (Datum2 − Datum1) in Millisekunden / 86.400.000.",
        "it": "Mancia = totale × (%) / 100; per persona = (totale + mancia) / n persone. Età esatta = data attuale − data di nascita. Differenza tra date: giorni = (data2 − data1) in millisecondi / 86.400.000.",
    },
    "estadistica": {
        "es": "La media aritmética = suma de valores / número de valores. La mediana es el valor central de los datos ordenados. La varianza = Σ(xi − x̄)² / n. La desviación estándar = √varianza. La probabilidad = casos favorables / casos totales.",
        "en": "Arithmetic mean = sum of values / number of values. Median is the middle value of sorted data. Variance = Σ(xi − x̄)² / n. Standard deviation = √variance. Probability = favorable outcomes / total outcomes.",
        "fr": "Moyenne arithmétique = somme des valeurs / nombre de valeurs. Médiane = valeur centrale des données triées. Variance = Σ(xi − x̄)² / n. Écart type = √variance. Probabilité = cas favorables / cas totaux.",
        "pt": "Média aritmética = soma dos valores / número de valores. Mediana = valor central dos dados ordenados. Variância = Σ(xi − x̄)² / n. Desvio padrão = √variância. Probabilidade = casos favoráveis / casos totais.",
        "de": "Arithmetisches Mittel = Summe der Werte / Anzahl. Median = Mittelwert der sortierten Daten. Varianz = Σ(xi − x̄)² / n. Standardabweichung = √Varianz. Wahrscheinlichkeit = günstige / mögliche Ergebnisse.",
        "it": "Media aritmetica = somma dei valori / numero di valori. Mediana = valore centrale dei dati ordinati. Varianza = Σ(xi − x̄)² / n. Deviazione standard = √varianza. Probabilità = casi favorevoli / casi totali.",
    },
    "ciencia": {
        "es": "Velocidad v = distancia / tiempo. Densidad ρ = masa / volumen. Fuerza F = masa × aceleración. Energía cinética KE = ½mv². Energía potencial PE = mgh. Presión P = fuerza / área. Ley de Ohm: V = I × R. Potencia P = V × I.",
        "en": "Speed v = distance / time. Density ρ = mass / volume. Force F = mass × acceleration. Kinetic energy KE = ½mv². Potential energy PE = mgh. Pressure P = force / area. Ohm's law: V = I × R. Power P = V × I.",
        "fr": "Vitesse v = distance / temps. Densité ρ = masse / volume. Force F = masse × accélération. Énergie cinétique KE = ½mv². Énergie potentielle PE = mgh. Pression P = force / surface. Loi d'Ohm : V = I × R.",
        "pt": "Velocidade v = distância / tempo. Densidade ρ = massa / volume. Força F = massa × aceleração. Energia cinética KE = ½mv². Energia potencial PE = mgh. Pressão P = força / área. Lei de Ohm: V = I × R.",
        "de": "Geschwindigkeit v = Strecke / Zeit. Dichte ρ = Masse / Volumen. Kraft F = Masse × Beschleunigung. Kinetische Energie KE = ½mv². Potentielle Energie PE = mgh. Druck P = Kraft / Fläche. Ohmsches Gesetz: V = I × R.",
        "it": "Velocità v = distanza / tempo. Densità ρ = massa / volume. Forza F = massa × accelerazione. Energia cinetica KE = ½mv². Energia potenziale PE = mgh. Pressione P = forza / area. Legge di Ohm: V = I × R.",
    },
    "conversion": {
        "es": "1 metro = 3.28084 pies = 39.3701 pulgadas. 1 kg = 2.20462 libras. °F = °C × 9/5 + 32. 1 litro = 0.264172 galones (US). 1 m² = 10.7639 ft². 1 atm = 101325 Pa = 1.01325 bar = 14.696 psi.",
        "en": "1 meter = 3.28084 feet = 39.3701 inches. 1 kg = 2.20462 pounds. °F = °C × 9/5 + 32. 1 liter = 0.264172 US gallons. 1 m² = 10.7639 ft². 1 atm = 101325 Pa = 1.01325 bar = 14.696 psi.",
        "fr": "1 mètre = 3,28084 pieds. 1 kg = 2,20462 livres. °F = °C × 9/5 + 32. 1 litre = 0,264172 gallons US. 1 m² = 10,7639 pi². 1 atm = 101325 Pa.",
        "pt": "1 metro = 3,28084 pés. 1 kg = 2,20462 libras. °F = °C × 9/5 + 32. 1 litro = 0,264172 galões (US). 1 m² = 10,7639 ft². 1 atm = 101325 Pa.",
        "de": "1 Meter = 3,28084 Fuß. 1 kg = 2,20462 Pfund. °F = °C × 9/5 + 32. 1 Liter = 0,264172 US-Gallonen. 1 m² = 10,7639 ft². 1 atm = 101325 Pa.",
        "it": "1 metro = 3,28084 piedi. 1 kg = 2,20462 libbre. °F = °C × 9/5 + 32. 1 litro = 0,264172 galloni US. 1 m² = 10,7639 ft². 1 atm = 101325 Pa.",
    },
    "deportes": {
        "es": "Ritmo de carrera = tiempo (min) / distancia (km). Calorías quemadas = MET × peso (kg) × tiempo (h). FC máxima ≈ 220 − edad. Zonas de entrenamiento basadas en % de FC máxima o FC de reserva (Karvonen). VO2 max estimado ≈ 15.3 × (FC máx / FC reposo).",
        "en": "Running pace = time (min) / distance (km). Calories burned = MET × weight (kg) × time (h). Max HR ≈ 220 − age. Training zones based on % of max HR or HR reserve (Karvonen). Estimated VO2 max ≈ 15.3 × (max HR / resting HR).",
        "fr": "Allure de course = temps (min) / distance (km). Calories brûlées = MET × poids (kg) × temps (h). FC max ≈ 220 − âge. Zones d'entraînement basées sur le % de FC max. VO2 max estimé ≈ 15,3 × (FC max / FC repos).",
        "pt": "Ritmo de corrida = tempo (min) / distância (km). Calorias queimadas = MET × peso (kg) × tempo (h). FC máx ≈ 220 − idade. Zonas de treino baseadas em % da FC máx. VO2 máx estimado ≈ 15,3 × (FC máx / FC repouso).",
        "de": "Laufpace = Zeit (Min.) / Strecke (km). Verbrannte Kalorien = MET × Gewicht (kg) × Zeit (h). Max Puls ≈ 220 − Alter. Trainingszonen basieren auf % des Max Puls. Geschätztes VO2 max ≈ 15,3 × (Max Puls / Ruhepuls).",
        "it": "Ritmo di corsa = tempo (min) / distanza (km). Calorie bruciate = MET × peso (kg) × tempo (h). FC max ≈ 220 − età. Zone di allenamento basate su % della FC max. VO2 max stimato ≈ 15,3 × (FC max / FC riposo).",
    },
}

FORMULA_TITLE = {
    "es": "Cómo funciona la fórmula",
    "en": "How the formula works",
    "fr": "Comment fonctionne la formule",
    "pt": "Como funciona a fórmula",
    "de": "Wie die Formel funktioniert",
    "it": "Come funziona la formula",
}


def generate_formula_explained(block_slug: str, lang: str) -> str:
    block = FORMULA_EXPLAINED.get(block_slug, {})
    return block.get(lang, block.get("en", ""))


def generate_faq(block_slug: str, lang: str) -> list:
    block_faqs = FAQS.get(block_slug, {})
    return block_faqs.get(lang, block_faqs.get("en", []))


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
    "quimica": {
        "es": "La <strong>{name}</strong> es una calculadora de química gratuita. {desc} Resuelve cálculos químicos con precisión usando fórmulas validadas científicamente.",
        "en": "The <strong>{name}</strong> is a free chemistry calculator. {desc} Solve chemical calculations accurately using scientifically validated formulas.",
        "fr": "Le <strong>{name}</strong> est une calculatrice de chimie gratuite. {desc} Résolvez vos calculs chimiques avec précision.",
        "pt": "A <strong>{name}</strong> é uma calculadora de química gratuita. {desc} Resolva cálculos químicos com precisão usando fórmulas validadas.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Chemierechner. {desc} Lösen Sie chemische Berechnungen präzise mit wissenschaftlich validierten Formeln.",
        "it": "Il <strong>{name}</strong> è una calcolatrice di chimica gratuita. {desc} Risolvi calcoli chimici con precisione usando formule scientificamente validate.",
    },
    "electronica": {
        "es": "La <strong>{name}</strong> es una calculadora de electrónica gratuita. {desc} Diseña y analiza circuitos eléctricos con precisión usando las leyes fundamentales.",
        "en": "The <strong>{name}</strong> is a free electronics calculator. {desc} Design and analyze electrical circuits accurately using fundamental laws.",
        "fr": "Le <strong>{name}</strong> est une calculatrice d'électronique gratuite. {desc} Concevez et analysez des circuits électriques avec précision.",
        "pt": "A <strong>{name}</strong> é uma calculadora de eletrônica gratuita. {desc} Projete e analise circuitos elétricos com precisão usando leis fundamentais.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Elektronikrechner. {desc} Entwerfen und analysieren Sie elektrische Schaltkreise mit Präzision.",
        "it": "Il <strong>{name}</strong> è una calcolatrice di elettronica gratuita. {desc} Progetta e analizza circuiti elettrici con precisione usando le leggi fondamentali.",
    },
    "clima": {
        "es": "La <strong>{name}</strong> es una calculadora meteorológica gratuita. {desc} Obtén cálculos atmosféricos precisos para meteorología, agricultura y actividades al aire libre.",
        "en": "The <strong>{name}</strong> is a free weather calculator. {desc} Get accurate atmospheric calculations for meteorology, agriculture, and outdoor activities.",
        "fr": "Le <strong>{name}</strong> est une calculatrice météorologique gratuite. {desc} Calculs atmosphériques précis pour la météo, l'agriculture et les activités outdoor.",
        "pt": "A <strong>{name}</strong> é uma calculadora meteorológica gratuita. {desc} Obtenha cálculos atmosféricos precisos para meteorologia, agricultura e atividades ao ar livre.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Wetterrechner. {desc} Genaue atmosphärische Berechnungen für Meteorologie, Landwirtschaft und Outdoor-Aktivitäten.",
        "it": "Il <strong>{name}</strong> è una calcolatrice meteorologica gratuita. {desc} Calcoli atmosferici precisi per meteorologia, agricoltura e attività all'aperto.",
    },
    "utilidades": {
        "es": "La <strong>{name}</strong> es una calculadora de utilidades gratuita. {desc} Herramienta práctica para cálculos del día a día, educación y productividad.",
        "en": "The <strong>{name}</strong> is a free utility calculator. {desc} A practical tool for everyday calculations, education, and productivity.",
        "fr": "Le <strong>{name}</strong> est une calculatrice utilitaire gratuite. {desc} Un outil pratique pour les calculs du quotidien, l'éducation et la productivité.",
        "pt": "A <strong>{name}</strong> é uma calculadora utilitária gratuita. {desc} Uma ferramenta prática para cálculos do dia a dia, educação e produtividade.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Universalrechner. {desc} Ein praktisches Werkzeug für alltägliche Berechnungen, Bildung und Produktivität.",
        "it": "Il <strong>{name}</strong> è una calcolatrice utilitaria gratuita. {desc} Uno strumento pratico per i calcoli quotidiani, l'istruzione e la produttività.",
    },
    "fotografia": {
        "es": "La <strong>{name}</strong> es una calculadora de fotografía gratuita. {desc} Optimiza tus ajustes fotográficos con fórmulas ópticas precisas para mejores resultados.",
        "en": "The <strong>{name}</strong> is a free photography calculator. {desc} Optimize your photographic settings with precise optical formulas for better results.",
        "fr": "Le <strong>{name}</strong> est une calculatrice de photographie gratuite. {desc} Optimisez vos réglages photographiques avec des formules optiques précises.",
        "pt": "A <strong>{name}</strong> é uma calculadora de fotografia gratuita. {desc} Otimize seus ajustes fotográficos com fórmulas ópticas precisas para melhores resultados.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Fotografierechner. {desc} Optimieren Sie Ihre Fotoeinstellungen mit präzisen optischen Formeln.",
        "it": "Il <strong>{name}</strong> è una calcolatrice di fotografia gratuita. {desc} Ottimizza le tue impostazioni fotografiche con precise formule ottiche.",
    },
    "transporte": {
        "es": "La <strong>{name}</strong> es una calculadora de transporte y navegación gratuita. {desc} Cálculos precisos para aviación, náutica y planificación de rutas.",
        "en": "The <strong>{name}</strong> is a free transport and navigation calculator. {desc} Accurate calculations for aviation, marine navigation, and route planning.",
        "fr": "Le <strong>{name}</strong> est une calculatrice de transport et navigation gratuite. {desc} Calculs précis pour l'aviation, la navigation maritime et la planification d'itinéraires.",
        "pt": "A <strong>{name}</strong> é uma calculadora de transporte e navegação gratuita. {desc} Cálculos precisos para aviação, náutica e planejamento de rotas.",
        "de": "Der <strong>{name}</strong> ist ein kostenloser Transport- und Navigationsrechner. {desc} Genaue Berechnungen für Luftfahrt, Seefahrt und Routenplanung.",
        "it": "Il <strong>{name}</strong> è una calcolatrice di trasporto e navigazione gratuita. {desc} Calcoli precisi per aviazione, navigazione marittima e pianificazione di percorsi.",
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

    # ── PRIORITY ARTICLES ────────────────────────────────────────────────────

    "202": {  # area-rectangulo
        "es": """<section class="long-content">
<h2>¿Qué es el área de un rectángulo?</h2>
<p>El <strong>área de un rectángulo</strong> mide la superficie plana que ocupa la figura, expresada en unidades cuadradas (m², cm², ft²…). Es uno de los cálculos más utilizados en arquitectura, construcción, decoración de interiores y geometría escolar porque la mayoría de las habitaciones, suelos, paredes y terrenos tienen forma rectangular.</p>

<h2>Fórmula del área del rectángulo</h2>
<p><strong>Área = largo × ancho</strong></p>
<p>Si quieres el perímetro: <strong>Perímetro = 2 × (largo + ancho)</strong></p>
<p>Ambas medidas deben estar en la misma unidad. Si el largo está en metros y el ancho en centímetros, convierte primero a una unidad común antes de multiplicar.</p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Quieres alicatar el suelo de un salón de 6,5 m de largo por 4,2 m de ancho.</strong></p>
<ol>
  <li>Área = 6,5 × 4,2 = <strong>27,3 m²</strong></li>
  <li>Añade un 10 % de margen por cortes y desperdicios: 27,3 × 1,10 = <strong>30 m² de azulejos a comprar</strong></li>
  <li>Perímetro (para el rodapié): 2 × (6,5 + 4,2) = <strong>21,4 m lineales</strong></li>
</ol>

<h2>Usos prácticos frecuentes</h2>
<ul>
  <li><strong>Suelos y pavimentos:</strong> Calcula cuántos metros cuadrados de parquet, cerámica o moqueta necesitas.</li>
  <li><strong>Pintura de techos y paredes:</strong> Un litro de pintura cubre normalmente entre 8 y 12 m²; divide el área entre ese rendimiento para saber cuántos litros comprar.</li>
  <li><strong>Jardines y terrenos:</strong> Determina la cantidad de césped, piedra decorativa o tierra vegetal necesaria.</li>
  <li><strong>Instalación de paneles solares:</strong> Verifica si el área del tejado disponible es suficiente para los paneles que necesitas.</li>
  <li><strong>Distribución de muebles:</strong> Comprueba si un sofá, cama o mesa caben en el espacio disponible.</li>
</ul>

<h2>Errores comunes y cómo evitarlos</h2>
<ul>
  <li><strong>Unidades mixtas:</strong> Mezclar metros y centímetros sin convertir da resultados 100 veces mayores o menores de lo real.</li>
  <li><strong>Confundir largo con diagonal:</strong> La diagonal de un rectángulo (√(a²+b²)) es siempre mayor que sus lados. No la uses como medida de largo o ancho.</li>
  <li><strong>Olvidar el margen de desperdicio:</strong> En obras, siempre añade un 5–10 % al área calculada para cortes y roturas.</li>
  <li><strong>Superficies con huecos:</strong> Si la habitación tiene columnas o huecos, calcula el área del rectángulo completo y resta el área de los huecos.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is rectangle area?</h2>
<p><strong>Rectangle area</strong> measures the flat surface a rectangle occupies, expressed in square units (m², cm², ft²…). It's one of the most widely used calculations in architecture, construction, interior design, and school geometry — because most rooms, floors, walls, and plots of land are rectangular.</p>

<h2>Rectangle area formula</h2>
<p><strong>Area = length × width</strong></p>
<p>For perimeter: <strong>Perimeter = 2 × (length + width)</strong></p>
<p>Both dimensions must be in the same unit. If length is in meters and width in centimeters, convert to a common unit first.</p>

<h2>Step-by-step example</h2>
<p><strong>You want to tile a living room 6.5 m long and 4.2 m wide.</strong></p>
<ol>
  <li>Area = 6.5 × 4.2 = <strong>27.3 m²</strong></li>
  <li>Add 10% for cuts and waste: 27.3 × 1.10 = <strong>30 m² of tiles to buy</strong></li>
  <li>Perimeter (for baseboard trim): 2 × (6.5 + 4.2) = <strong>21.4 linear meters</strong></li>
</ol>

<h2>Common practical uses</h2>
<ul>
  <li><strong>Flooring and tiling:</strong> Calculate how many square meters of hardwood, ceramic, or carpet you need.</li>
  <li><strong>Ceiling and wall paint:</strong> One liter of paint covers roughly 8–12 m²; divide the area by that figure to find how many liters to buy.</li>
  <li><strong>Gardens and land:</strong> Determine the amount of sod, decorative gravel, or topsoil needed.</li>
  <li><strong>Solar panel installation:</strong> Check if available roof area can accommodate the required number of panels.</li>
  <li><strong>Furniture layout:</strong> Verify whether a sofa, bed, or table fits in the available floor space.</li>
</ul>

<h2>Common mistakes to avoid</h2>
<ul>
  <li><strong>Mixed units:</strong> Mixing meters and centimeters without converting gives results 100 times too large or small.</li>
  <li><strong>Diagonal vs. side:</strong> The rectangle's diagonal (√(a²+b²)) is always longer than its sides — don't use it as length or width.</li>
  <li><strong>Forgetting waste allowance:</strong> In construction, always add 5–10% to the calculated area for cuts and breakage.</li>
  <li><strong>Rooms with cutouts:</strong> Calculate the full rectangle area and subtract the area of any columns or recesses.</li>
</ul>
</section>""",
    },

    "204": {  # regla-de-tres
        "es": """<section class="long-content">
<h2>¿Qué es la regla de tres?</h2>
<p>La <strong>regla de tres</strong> es el método de cálculo proporcional más utilizado en matemáticas aplicadas. Permite encontrar un valor desconocido cuando conoces tres valores relacionados mediante una proporción directa (a más de uno, más del otro) o inversa (a más de uno, menos del otro). Es una herramienta imprescindible en cocina, comercio, ingeniería y la vida cotidiana.</p>

<h2>Fórmulas de la regla de tres</h2>
<p><strong>Regla de tres directa:</strong> Si A→B, ¿cuánto corresponde a C?<br>
<code>x = (B × C) / A</code></p>
<p><strong>Regla de tres inversa:</strong> Si A→B, y la relación es inversa, ¿cuánto corresponde a C?<br>
<code>x = (A × B) / C</code></p>
<p>La clave para distinguirlas: en la proporcionalidad directa, las dos magnitudes crecen juntas. En la inversa, cuando una crece, la otra disminuye.</p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Directa:</strong> Si 3 kg de manzanas cuestan 7,50 €, ¿cuánto cuestan 5 kg?</p>
<ol>
  <li>3 kg → 7,50 €</li>
  <li>5 kg → x = (7,50 × 5) / 3 = <strong>12,50 €</strong></li>
</ol>
<p><strong>Inversa:</strong> 4 obreros tardan 6 días en acabar una obra. ¿Cuántos días tardarán 8 obreros?</p>
<ol>
  <li>4 obreros → 6 días</li>
  <li>8 obreros → x = (4 × 6) / 8 = <strong>3 días</strong></li>
</ol>

<h2>Aplicaciones prácticas</h2>
<ul>
  <li><strong>Cocina y recetas:</strong> Adaptar ingredientes para 4 personas cuando la receta es para 6.</li>
  <li><strong>Precios y compras:</strong> Comparar el precio por unidad entre formatos de diferente tamaño.</li>
  <li><strong>Planos y mapas:</strong> Si 1 cm en el mapa equivale a 50 km, ¿qué distancia real representa 3,5 cm?</li>
  <li><strong>Velocidad y tiempo:</strong> Si un vehículo recorre 120 km en 1,5 h, ¿cuánto tardará en recorrer 450 km?</li>
  <li><strong>Finanzas:</strong> Calcular comisiones, intereses o repartos proporcionales.</li>
</ul>

<h2>Cómo no confundirse con la regla de tres</h2>
<ul>
  <li><strong>Identifica siempre las dos magnitudes:</strong> En "a más km, más tiempo" la magnitud 1 es distancia y la magnitud 2 es tiempo; la relación es directa.</li>
  <li><strong>Verifica la proporcionalidad:</strong> No todo par de valores es proporcional. El precio de un taxi puede tener tarifa fija + variable; ahí la regla de tres simple no aplica directamente.</li>
  <li><strong>Comprueba las unidades:</strong> Si una cantidad está en kg y otra en gramos, convierte antes de aplicar la fórmula.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is the rule of three?</h2>
<p>The <strong>rule of three</strong> is the most widely used method of proportional calculation in applied math. It lets you find an unknown value when you know three related values through a direct proportion (more of one, more of the other) or inverse proportion (more of one, less of the other). It's essential in cooking, commerce, engineering, and everyday life.</p>

<h2>Rule of three formulas</h2>
<p><strong>Direct rule of three:</strong> If A→B, what corresponds to C?<br>
<code>x = (B × C) / A</code></p>
<p><strong>Inverse rule of three:</strong> If A→B with an inverse relationship, what corresponds to C?<br>
<code>x = (A × B) / C</code></p>
<p>The key distinction: in direct proportionality, both quantities increase together. In inverse proportionality, when one increases the other decreases.</p>

<h2>Step-by-step examples</h2>
<p><strong>Direct:</strong> If 3 kg of apples cost $7.50, how much do 5 kg cost?</p>
<ol>
  <li>3 kg → $7.50</li>
  <li>5 kg → x = (7.50 × 5) / 3 = <strong>$12.50</strong></li>
</ol>
<p><strong>Inverse:</strong> 4 workers take 6 days to finish a job. How long do 8 workers take?</p>
<ol>
  <li>4 workers → 6 days</li>
  <li>8 workers → x = (4 × 6) / 8 = <strong>3 days</strong></li>
</ol>

<h2>Practical applications</h2>
<ul>
  <li><strong>Recipes:</strong> Scale ingredients for 4 people when a recipe serves 6.</li>
  <li><strong>Shopping:</strong> Compare unit prices between different package sizes.</li>
  <li><strong>Maps and blueprints:</strong> If 1 cm on the map equals 50 km, what real distance does 3.5 cm represent?</li>
  <li><strong>Speed and time:</strong> If a vehicle covers 120 km in 1.5 h, how long to cover 450 km?</li>
  <li><strong>Finance:</strong> Calculate commissions, interest, or proportional distributions.</li>
</ul>

<h2>Common mistakes to avoid</h2>
<ul>
  <li><strong>Always identify the two quantities:</strong> In "more km, more time" the two quantities are distance and time — a direct relationship.</li>
  <li><strong>Verify proportionality:</strong> Not all value pairs are proportional. A taxi fare with a fixed charge plus variable rate can't be solved with simple rule of three alone.</li>
  <li><strong>Check units:</strong> If one quantity is in kg and another in grams, convert before applying the formula.</li>
</ul>
</section>""",
    },

    "211": {  # area-triangulo
        "es": """<section class="long-content">
<h2>¿Qué es el área de un triángulo?</h2>
<p>El <strong>área de un triángulo</strong> mide la superficie plana encerrada por sus tres lados. Junto con el rectángulo, es la figura geométrica más utilizada en arquitectura, carpintería, ingeniería civil y diseño gráfico. Cualquier polígono puede descomponerse en triángulos, lo que hace de este cálculo la base de toda la geometría de superficies.</p>

<h2>Fórmulas del área del triángulo</h2>
<p><strong>Fórmula principal (base y altura):</strong><br>
<code>Área = (base × altura) / 2</code></p>
<p><strong>Si conoces los tres lados (fórmula de Herón):</strong><br>
Semiperímetro s = (a + b + c) / 2<br>
<code>Área = √(s × (s-a) × (s-b) × (s-c))</code></p>
<p><strong>Si conoces dos lados y el ángulo entre ellos:</strong><br>
<code>Área = (a × b × sen(θ)) / 2</code></p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Necesitas calcular el área de un tejado triangular de 9 m de base y 4 m de altura.</strong></p>
<ol>
  <li>Área = (9 × 4) / 2 = <strong>18 m²</strong></li>
  <li>Añade el 10 % de desperdicio para tejas: 18 × 1,10 = <strong>19,8 m² de material</strong></li>
</ol>
<p><strong>Fórmula de Herón:</strong> Triángulo de lados 7, 8 y 9 m.</p>
<ol>
  <li>s = (7+8+9)/2 = 12</li>
  <li>Área = √(12 × 5 × 4 × 3) = √720 ≈ <strong>26,83 m²</strong></li>
</ol>

<h2>Aplicaciones prácticas</h2>
<ul>
  <li><strong>Tejados a dos o cuatro aguas:</strong> Calcula la superficie exacta de cada paño triangular para presupuestar tejas, impermeabilizante o panel solar.</li>
  <li><strong>Terrenos irregulares:</strong> Divide el terreno en triángulos para sumar sus áreas y obtener la superficie total.</li>
  <li><strong>Carpintería y marquetería:</strong> Calcula el material necesario para piezas triangulares sin desperdicio.</li>
  <li><strong>Diseño gráfico y arquitectura:</strong> Los elementos triangulares son omnipresentes en logos, fachadas y estructuras.</li>
  <li><strong>Trigonometría aplicada:</strong> La base del cálculo de fuerzas, vectores y tensiones en estructuras.</li>
</ul>

<h2>La altura de un triángulo: cómo medirla</h2>
<p>La <strong>altura</strong> de un triángulo es la distancia perpendicular entre la base y el vértice opuesto. En un triángulo rectángulo, la altura respecto a la hipotenusa se puede calcular como <code>h = (cateto₁ × cateto₂) / hipotenusa</code>. En triángulos obtusángulos, la altura puede caer fuera del triángulo — en ese caso, prolonga la base para medirla correctamente.</p>
</section>""",
        "en": """<section class="long-content">
<h2>What is triangle area?</h2>
<p><strong>Triangle area</strong> measures the flat surface enclosed by three sides. Along with the rectangle, it's the most widely used shape in architecture, carpentry, civil engineering, and graphic design. Any polygon can be broken down into triangles, making this calculation the foundation of all surface geometry.</p>

<h2>Triangle area formulas</h2>
<p><strong>Main formula (base and height):</strong><br>
<code>Area = (base × height) / 2</code></p>
<p><strong>If you know all three sides (Heron's formula):</strong><br>
Semi-perimeter s = (a + b + c) / 2<br>
<code>Area = √(s × (s-a) × (s-b) × (s-c))</code></p>
<p><strong>If you know two sides and the angle between them:</strong><br>
<code>Area = (a × b × sin(θ)) / 2</code></p>

<h2>Step-by-step examples</h2>
<p><strong>Calculate the area of a triangular roof section 9 m wide and 4 m tall.</strong></p>
<ol>
  <li>Area = (9 × 4) / 2 = <strong>18 m²</strong></li>
  <li>Add 10% waste for roofing tiles: 18 × 1.10 = <strong>19.8 m² of material needed</strong></li>
</ol>
<p><strong>Heron's formula:</strong> Triangle with sides 7, 8, and 9 m.</p>
<ol>
  <li>s = (7+8+9)/2 = 12</li>
  <li>Area = √(12 × 5 × 4 × 3) = √720 ≈ <strong>26.83 m²</strong></li>
</ol>

<h2>Practical applications</h2>
<ul>
  <li><strong>Gabled roofs:</strong> Calculate exact area of each triangular roof panel for tiles, waterproofing, or solar panels.</li>
  <li><strong>Irregular plots:</strong> Divide the land into triangles, sum their areas to get total surface area.</li>
  <li><strong>Carpentry and woodworking:</strong> Calculate material needed for triangular pieces with minimal waste.</li>
  <li><strong>Graphic design and architecture:</strong> Triangular elements are everywhere in logos, facades, and structures.</li>
  <li><strong>Applied trigonometry:</strong> Foundation for calculating forces, vectors, and stresses in structures.</li>
</ul>

<h2>How to measure a triangle's height</h2>
<p>The <strong>height</strong> of a triangle is the perpendicular distance from the base to the opposite vertex. In a right triangle, the height relative to the hypotenuse is <code>h = (leg₁ × leg₂) / hypotenuse</code>. In obtuse triangles, the height falls outside the triangle — extend the base line to measure it correctly.</p>
</section>""",
    },

    "306": {  # descuento
        "es": """<section class="long-content">
<h2>¿Cómo calcular un descuento?</h2>
<p>Calcular un <strong>descuento</strong> consiste en determinar cuánto dinero ahorras (importe del descuento) y cuál es el precio final que pagarás. Es un cálculo cotidiano en rebajas, negociaciones comerciales, cupones y precios especiales. También te permite comparar de forma objetiva si un descuento del 30 % en un artículo de 100 € es mejor o peor que uno del 20 % en un artículo de 120 €.</p>

<h2>Fórmulas del descuento</h2>
<p><strong>Importe del descuento = Precio original × (Descuento% / 100)</strong></p>
<p><strong>Precio final = Precio original × (1 − Descuento% / 100)</strong></p>
<p><strong>Descuento% = ((Precio original − Precio final) / Precio original) × 100</strong></p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Un abrigo de 185 € tiene un 35 % de descuento. ¿Cuánto pagas?</strong></p>
<ol>
  <li>Importe del descuento: 185 × 0,35 = <strong>64,75 €</strong></li>
  <li>Precio final: 185 − 64,75 = <strong>120,25 €</strong> (o directamente: 185 × 0,65 = 120,25 €)</li>
</ol>
<p><strong>Descuentos encadenados: primero un 20 %, luego un 10 % adicional.</strong></p>
<ol>
  <li>Tras el primer descuento: 185 × 0,80 = 148 €</li>
  <li>Tras el segundo: 148 × 0,90 = <strong>133,20 €</strong></li>
  <li>Descuento real total: (185 − 133,20) / 185 × 100 = <strong>28 %</strong> (no 30 %)</li>
</ol>

<h2>Aplicaciones prácticas</h2>
<ul>
  <li><strong>Rebajas y ventas flash:</strong> Black Friday, ventas de temporada y outlets suelen combinar varios porcentajes de descuento — esta calculadora desenmascara el descuento real.</li>
  <li><strong>Negociación entre empresas:</strong> Calcular el margen que queda después de los rappels (descuentos por volumen) acordados con el proveedor.</li>
  <li><strong>Comparar ofertas online:</strong> Comprueba si el precio "tachado" del e-commerce es realmente más barato que la competencia.</li>
  <li><strong>Distribución y márgenes:</strong> Calcula el precio de venta al público manteniendo el margen deseado después de los descuentos al canal.</li>
</ul>

<h2>Trampas habituales en los descuentos</h2>
<ul>
  <li><strong>El precio de referencia inflado:</strong> Algunos comercios suben el precio antes de las rebajas para que el descuento parezca mayor.</li>
  <li><strong>Descuentos encadenados ≠ suma:</strong> Un 20 % + un 10 % no son un 30 %; son un 28 %. Siempre aplica los descuentos de forma secuencial.</li>
  <li><strong>Descuento en precio sin IVA:</strong> Verifica siempre si el descuento se aplica sobre el precio con o sin IVA incluido.</li>
  <li><strong>Coste final incluyendo envío:</strong> Un producto con 40 % de descuento pero con envío caro puede ser más caro que la competencia con envío gratis.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>How to calculate a discount</h2>
<p>Calculating a <strong>discount</strong> means finding how much money you save (the discount amount) and what final price you'll pay. It's an everyday calculation for sales, commercial negotiations, coupons, and special prices. It also lets you objectively compare whether a 30% discount on a $100 item is better or worse than a 20% discount on a $120 item.</p>

<h2>Discount formulas</h2>
<p><strong>Discount amount = Original price × (Discount% / 100)</strong></p>
<p><strong>Final price = Original price × (1 − Discount% / 100)</strong></p>
<p><strong>Discount% = ((Original price − Final price) / Original price) × 100</strong></p>

<h2>Step-by-step example</h2>
<p><strong>A $185 coat has a 35% discount. What do you pay?</strong></p>
<ol>
  <li>Discount amount: 185 × 0.35 = <strong>$64.75</strong></li>
  <li>Final price: 185 − 64.75 = <strong>$120.25</strong> (or directly: 185 × 0.65 = $120.25)</li>
</ol>
<p><strong>Stacked discounts: first 20% off, then an extra 10%.</strong></p>
<ol>
  <li>After first discount: 185 × 0.80 = $148</li>
  <li>After second: 148 × 0.90 = <strong>$133.20</strong></li>
  <li>Real total discount: (185 − 133.20) / 185 × 100 = <strong>28%</strong> (not 30%)</li>
</ol>

<h2>Practical applications</h2>
<ul>
  <li><strong>Sales and flash deals:</strong> Black Friday, seasonal sales, and outlet stores often combine multiple discount percentages — this calculator reveals the real total discount.</li>
  <li><strong>B2B negotiation:</strong> Calculate the margin remaining after volume discounts agreed with suppliers.</li>
  <li><strong>Comparing online offers:</strong> Check if the e-commerce "crossed out" price is truly cheaper than the competition.</li>
  <li><strong>Distribution and margins:</strong> Calculate the retail price while maintaining your desired margin after channel discounts.</li>
</ul>

<h2>Common discount traps</h2>
<ul>
  <li><strong>Inflated reference price:</strong> Some retailers raise the price before a sale to make the discount appear larger.</li>
  <li><strong>Stacked discounts ≠ sum:</strong> 20% + 10% is not 30%; it's 28%. Always apply discounts sequentially.</li>
  <li><strong>Pre-tax vs post-tax discount:</strong> Always check whether the discount applies to the price including or excluding VAT/sales tax.</li>
  <li><strong>Total cost including shipping:</strong> A 40% discount plus expensive shipping may cost more than a competitor with free shipping.</li>
</ul>
</section>""",
    },

    "310": {  # roi
        "es": """<section class="long-content">
<h2>¿Qué es el ROI (Retorno sobre la Inversión)?</h2>
<p>El <strong>ROI (Return on Investment)</strong> es el indicador financiero más universal para medir la rentabilidad de una inversión. Expresa, en forma de porcentaje, cuánto has ganado (o perdido) en relación con lo que invertiste. Un ROI del 25 % significa que por cada 100 € invertidos recuperas 125 €. Se usa en marketing, proyectos inmobiliarios, compra de maquinaria, bolsa y cualquier decisión de negocio donde hay un desembolso inicial.</p>

<h2>Fórmula del ROI</h2>
<p><strong>ROI (%) = ((Beneficio neto − Coste de inversión) / Coste de inversión) × 100</strong></p>
<p>O equivalentemente: <strong>ROI = (Ingresos totales − Coste) / Coste × 100</strong></p>
<p>Si el resultado es positivo, la inversión fue rentable. Si es negativo, hubo pérdidas.</p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Inviertes 2.000 € en una campaña de publicidad en redes sociales que genera 7.500 € en ventas, con un coste de producto de 4.000 €.</strong></p>
<ol>
  <li>Ingresos netos de la campaña: 7.500 − 4.000 = 3.500 €</li>
  <li>Beneficio neto (descontando inversión): 3.500 − 2.000 = 1.500 €</li>
  <li>ROI = (1.500 / 2.000) × 100 = <strong>75 %</strong></li>
</ol>
<p>Cada euro invertido en la campaña generó 0,75 € de beneficio neto.</p>

<h2>Aplicaciones del ROI por sector</h2>
<ul>
  <li><strong>Marketing digital:</strong> Compara el rendimiento de Google Ads, Meta Ads, email marketing y SEO en igualdad de condiciones.</li>
  <li><strong>Inversión inmobiliaria:</strong> Calcula si el alquiler anual justifica el precio de compra más los costes de reforma.</li>
  <li><strong>Inversión en bolsa:</strong> Mide la rentabilidad real de una cartera de acciones, incluyendo dividendos.</li>
  <li><strong>Maquinaria y equipamiento:</strong> Determina en cuántos meses se amortiza una inversión en una nueva máquina según el ahorro o ingreso adicional que genera.</li>
  <li><strong>Formación y desarrollo:</strong> Empresas que miden el ROI de la formación comprueban si el aumento de productividad justifica el coste del curso.</li>
</ul>

<h2>Limitaciones del ROI y alternativas</h2>
<ul>
  <li><strong>No tiene en cuenta el tiempo:</strong> Un ROI del 50 % en 10 años es muy diferente a un 50 % en 1 año. Para comparar inversiones a distintos plazos, usa el <strong>ROI anualizado</strong> o el <strong>CAGR</strong>.</li>
  <li><strong>Ignora el riesgo:</strong> Dos inversiones con el mismo ROI esperado pueden tener perfiles de riesgo muy diferentes.</li>
  <li><strong>Alternativas más completas:</strong> VAN (Valor Actual Neto), TIR (Tasa Interna de Retorno) y el Payback Period ofrecen una visión más completa para proyectos complejos o a largo plazo.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is ROI (Return on Investment)?</h2>
<p><strong>ROI (Return on Investment)</strong> is the most universal financial metric for measuring investment profitability. It expresses, as a percentage, how much you gained (or lost) relative to what you invested. An ROI of 25% means that for every $100 invested, you get back $125. It's used in marketing, real estate, equipment purchases, stock investing, and any business decision involving an upfront outlay.</p>

<h2>ROI formula</h2>
<p><strong>ROI (%) = ((Net profit − Investment cost) / Investment cost) × 100</strong></p>
<p>Equivalently: <strong>ROI = (Total returns − Cost) / Cost × 100</strong></p>
<p>A positive result means a profitable investment. A negative result means a loss.</p>

<h2>Step-by-step example</h2>
<p><strong>You invest $2,000 in a social media ad campaign that generates $7,500 in sales, with $4,000 in product costs.</strong></p>
<ol>
  <li>Campaign net revenue: 7,500 − 4,000 = $3,500</li>
  <li>Net profit (after subtracting investment): 3,500 − 2,000 = $1,500</li>
  <li>ROI = (1,500 / 2,000) × 100 = <strong>75%</strong></li>
</ol>
<p>Every dollar invested in the campaign generated $0.75 in net profit.</p>

<h2>ROI applications by sector</h2>
<ul>
  <li><strong>Digital marketing:</strong> Compare Google Ads, Meta Ads, email marketing, and SEO performance on equal terms.</li>
  <li><strong>Real estate investing:</strong> Calculate whether annual rental income justifies the purchase price plus renovation costs.</li>
  <li><strong>Stock market:</strong> Measure the true return of a stock portfolio, including dividends.</li>
  <li><strong>Equipment investment:</strong> Determine in how many months a new machine pays for itself based on additional savings or revenue.</li>
  <li><strong>Training and development:</strong> Companies measuring training ROI verify whether productivity gains justify the course cost.</li>
</ul>

<h2>ROI limitations and alternatives</h2>
<ul>
  <li><strong>Doesn't account for time:</strong> 50% ROI over 10 years is very different from 50% in 1 year. For comparing investments over different timeframes, use <strong>annualized ROI</strong> or <strong>CAGR</strong>.</li>
  <li><strong>Ignores risk:</strong> Two investments with the same expected ROI can have very different risk profiles.</li>
  <li><strong>More complete alternatives:</strong> NPV (Net Present Value), IRR (Internal Rate of Return), and Payback Period offer a fuller picture for complex or long-term projects.</li>
</ul>
</section>""",
    },

    "410": {  # metabolismo-basal
        "es": """<section class="long-content">
<h2>¿Qué es el metabolismo basal (TMB)?</h2>
<p>El <strong>metabolismo basal</strong> (también llamado Tasa Metabólica Basal o TMB) es la cantidad mínima de calorías que tu cuerpo necesita para mantener las funciones vitales en completo reposo: respiración, circulación sanguínea, temperatura corporal, función cerebral y renovación celular. Representa entre el 60 % y el 75 % del total de calorías que quemas al día. Conocer tu TMB es el primer paso para cualquier plan nutricional serio.</p>

<h2>Fórmulas del metabolismo basal</h2>
<p><strong>Ecuación de Mifflin-St Jeor</strong> (la más precisa según estudios recientes):</p>
<ul>
  <li>Hombres: <code>TMB = 10×peso(kg) + 6,25×altura(cm) − 5×edad + 5</code></li>
  <li>Mujeres: <code>TMB = 10×peso(kg) + 6,25×altura(cm) − 5×edad − 161</code></li>
</ul>
<p><strong>Ecuación de Harris-Benedict</strong> (clásica, ligeramente menos precisa):</p>
<ul>
  <li>Hombres: <code>TMB = 88,36 + 13,40×peso + 4,80×altura − 5,68×edad</code></li>
  <li>Mujeres: <code>TMB = 447,59 + 9,25×peso + 3,10×altura − 4,33×edad</code></li>
</ul>

<h2>Ejemplo paso a paso</h2>
<p><strong>Mujer de 32 años, 62 kg de peso, 165 cm de altura.</strong></p>
<ol>
  <li>TMB (Mifflin) = 10×62 + 6,25×165 − 5×32 − 161</li>
  <li>= 620 + 1031,25 − 160 − 161 = <strong>1.330 kcal/día</strong></li>
  <li>Con actividad moderada (3–5 días de ejercicio): 1.330 × 1,55 = <strong>2.062 kcal/día de mantenimiento</strong></li>
</ol>

<h2>TMB y el gasto calórico total (TDEE)</h2>
<p>Para calcular las calorías totales diarias, multiplica tu TMB por el <strong>factor de actividad</strong>:</p>
<ul>
  <li>Sedentario (sin ejercicio): TMB × 1,2</li>
  <li>Actividad ligera (1–3 días/semana): TMB × 1,375</li>
  <li>Actividad moderada (3–5 días/semana): TMB × 1,55</li>
  <li>Actividad intensa (6–7 días/semana): TMB × 1,725</li>
  <li>Atleta o trabajo físico muy intenso: TMB × 1,9</li>
</ul>

<h2>Aplicaciones del TMB en nutrición</h2>
<ul>
  <li><strong>Pérdida de peso:</strong> Come 300–500 kcal por debajo de tu TDEE para perder 0,3–0,5 kg/semana de forma sostenible.</li>
  <li><strong>Ganancia de masa muscular:</strong> Superávit de 200–300 kcal sobre el TDEE con suficiente proteína (1,6–2,2 g/kg).</li>
  <li><strong>Mantenimiento:</strong> Come igual a tu TDEE calculado y ajusta cada 2–4 semanas según el peso real.</li>
  <li><strong>Atletas:</strong> En deportes de alta carga, el TDEE puede superar las 4.000–5.000 kcal/día.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is Basal Metabolic Rate (BMR)?</h2>
<p>Your <strong>Basal Metabolic Rate (BMR)</strong> is the minimum number of calories your body needs to maintain vital functions at complete rest: breathing, blood circulation, body temperature, brain function, and cell renewal. It accounts for 60–75% of the total calories you burn each day. Knowing your BMR is the first step in any serious nutrition plan.</p>

<h2>BMR formulas</h2>
<p><strong>Mifflin-St Jeor equation</strong> (most accurate according to recent studies):</p>
<ul>
  <li>Men: <code>BMR = 10×weight(kg) + 6.25×height(cm) − 5×age + 5</code></li>
  <li>Women: <code>BMR = 10×weight(kg) + 6.25×height(cm) − 5×age − 161</code></li>
</ul>
<p><strong>Harris-Benedict equation</strong> (classic, slightly less precise):</p>
<ul>
  <li>Men: <code>BMR = 88.36 + 13.40×weight + 4.80×height − 5.68×age</code></li>
  <li>Women: <code>BMR = 447.59 + 9.25×weight + 3.10×height − 4.33×age</code></li>
</ul>

<h2>Step-by-step example</h2>
<p><strong>Woman, 32 years old, 62 kg, 165 cm tall.</strong></p>
<ol>
  <li>BMR (Mifflin) = 10×62 + 6.25×165 − 5×32 − 161</li>
  <li>= 620 + 1,031.25 − 160 − 161 = <strong>1,330 kcal/day</strong></li>
  <li>With moderate activity (3–5 days of exercise): 1,330 × 1.55 = <strong>2,062 kcal/day maintenance</strong></li>
</ol>

<h2>BMR and total daily energy expenditure (TDEE)</h2>
<p>To calculate total daily calories, multiply your BMR by an <strong>activity factor</strong>:</p>
<ul>
  <li>Sedentary (no exercise): BMR × 1.2</li>
  <li>Light activity (1–3 days/week): BMR × 1.375</li>
  <li>Moderate activity (3–5 days/week): BMR × 1.55</li>
  <li>Intense activity (6–7 days/week): BMR × 1.725</li>
  <li>Athlete or very intense physical work: BMR × 1.9</li>
</ul>

<h2>BMR applications in nutrition</h2>
<ul>
  <li><strong>Weight loss:</strong> Eat 300–500 kcal below your TDEE to lose 0.3–0.5 kg/week sustainably.</li>
  <li><strong>Muscle gain:</strong> Caloric surplus of 200–300 kcal above TDEE with sufficient protein (1.6–2.2 g/kg).</li>
  <li><strong>Maintenance:</strong> Eat at your calculated TDEE and adjust every 2–4 weeks based on actual weight changes.</li>
  <li><strong>Athletes:</strong> In high-volume sports, TDEE can exceed 4,000–5,000 kcal/day.</li>
</ul>
</section>""",
    },

    "502": {  # diferencia-fechas
        "es": """<section class="long-content">
<h2>¿Para qué sirve la calculadora de diferencia entre fechas?</h2>
<p>La <strong>calculadora de diferencia entre fechas</strong> calcula con precisión el tiempo transcurrido entre dos fechas: en días exactos, semanas completas, meses aproximados y años. Es una herramienta imprescindible en derecho laboral (para calcular la antigüedad o el finiquito), medicina (semanas de embarazo, tiempo de tratamiento), logística (plazos de entrega) y planificación personal (cuentas atrás).</p>

<h2>¿Cómo funciona el cálculo?</h2>
<p>La calculadora cuenta los <strong>días naturales</strong> entre ambas fechas y los convierte:</p>
<ul>
  <li><strong>Días exactos:</strong> suma directa incluyendo años bisiestos.</li>
  <li><strong>Semanas:</strong> días ÷ 7 (enteras y días restantes).</li>
  <li><strong>Meses:</strong> cuenta los meses completos + días sobrantes.</li>
  <li><strong>Años:</strong> suma de años completos + meses y días restantes.</li>
</ul>

<h2>Ejemplo paso a paso</h2>
<p><strong>¿Cuántos días llevas en tu empresa si empezaste el 1 de septiembre de 2020?</strong></p>
<ol>
  <li>Fecha inicio: 01/09/2020</li>
  <li>Fecha fin: hoy, 25/04/2026</li>
  <li>Diferencia: <strong>2.062 días</strong> (teniendo en cuenta el año bisiesto 2024)</li>
  <li>Equivale a: <strong>294 semanas y 4 días</strong>, o <strong>67 meses y 24 días</strong>, o <strong>5 años y 7 meses</strong></li>
</ol>

<h2>Usos más frecuentes</h2>
<ul>
  <li><strong>Derecho laboral:</strong> Calcular la antigüedad exacta para indemnizaciones, finiquitos y bonificaciones por años de servicio.</li>
  <li><strong>Embarazo:</strong> Determinar las semanas de gestación desde la fecha de la última regla (FUR) y la fecha estimada de parto.</li>
  <li><strong>Plazos legales y contractuales:</strong> Verificar si han transcurrido los días de garantía, prescripción o caducidad de un contrato.</li>
  <li><strong>Planificación de eventos:</strong> Cuenta atrás exacta para bodas, viajes, exámenes o fechas límite de proyectos.</li>
  <li><strong>Seguimiento de tratamientos:</strong> Controlar cuántos días llevas siguiendo un régimen de medicación, dieta o entrenamiento.</li>
</ul>

<h2>Años bisiestos y diferencias de fechas</h2>
<p>Un <strong>año bisiesto</strong> tiene 366 días en lugar de 365. Es bisiesto si es divisible por 4, excepto los centenarios (divisibles por 100), salvo que también sean divisibles por 400. Esto afecta los cálculos cuando el rango incluye febrero de un año bisiesto. Nuestra calculadora tiene en cuenta automáticamente todos los años bisiestos del rango seleccionado.</p>
</section>""",
        "en": """<section class="long-content">
<h2>What is a date difference calculator for?</h2>
<p>A <strong>date difference calculator</strong> precisely calculates the time elapsed between two dates: in exact days, full weeks, approximate months, and years. It's an essential tool in labor law (calculating seniority or severance), medicine (weeks of pregnancy, treatment duration), logistics (delivery deadlines), and personal planning (countdowns).</p>

<h2>How the calculation works</h2>
<p>The calculator counts the <strong>calendar days</strong> between both dates and converts them:</p>
<ul>
  <li><strong>Exact days:</strong> direct count including leap years.</li>
  <li><strong>Weeks:</strong> days ÷ 7 (full weeks plus remaining days).</li>
  <li><strong>Months:</strong> full calendar months plus remaining days.</li>
  <li><strong>Years:</strong> full years plus remaining months and days.</li>
</ul>

<h2>Step-by-step example</h2>
<p><strong>How many days have you worked at your company if you started September 1, 2020?</strong></p>
<ol>
  <li>Start date: 09/01/2020</li>
  <li>End date: today, 04/25/2026</li>
  <li>Difference: <strong>2,062 days</strong> (accounting for leap year 2024)</li>
  <li>Equivalent to: <strong>294 weeks and 4 days</strong>, or <strong>67 months and 24 days</strong>, or <strong>5 years and 7 months</strong></li>
</ol>

<h2>Most common uses</h2>
<ul>
  <li><strong>Labor law:</strong> Calculate exact seniority for severance pay, settlement, and service bonuses.</li>
  <li><strong>Pregnancy:</strong> Determine weeks of gestation from the last menstrual period (LMP) and estimated due date.</li>
  <li><strong>Legal and contractual deadlines:</strong> Verify if warranty periods, statutes of limitation, or contract expiration dates have elapsed.</li>
  <li><strong>Event planning:</strong> Exact countdown for weddings, trips, exams, or project deadlines.</li>
  <li><strong>Treatment tracking:</strong> Monitor how many days you've been following a medication, diet, or training regimen.</li>
</ul>

<h2>Leap years and date differences</h2>
<p>A <strong>leap year</strong> has 366 days instead of 365. A year is a leap year if it's divisible by 4, except century years (divisible by 100), unless they're also divisible by 400. This affects calculations when the date range includes February of a leap year. Our calculator automatically accounts for all leap years in the selected range.</p>
</section>""",
    },

    "601": {  # mediana
        "es": """<section class="long-content">
<h2>¿Qué es la mediana y para qué se usa?</h2>
<p>La <strong>mediana</strong> es el valor central de un conjunto de datos ordenados de menor a mayor. A diferencia de la media aritmética, la mediana es <strong>resistente a los valores extremos (outliers)</strong>, lo que la convierte en la medida de tendencia central más representativa en distribuciones asimétricas. En datos de salarios, precios inmobiliarios o tiempo de respuesta de sistemas, la mediana suele ser más informativa que la media.</p>

<h2>Cómo calcular la mediana</h2>
<p><strong>Paso 1:</strong> Ordena los datos de menor a mayor.</p>
<p><strong>Si hay un número impar de datos:</strong> la mediana es el valor del medio.<br>
Posición = (n + 1) / 2</p>
<p><strong>Si hay un número par de datos:</strong> la mediana es la media de los dos valores centrales.<br>
Mediana = (valor en posición n/2 + valor en posición n/2+1) / 2</p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Los salarios de 7 empleados son: 28.000, 35.000, 31.000, 95.000, 29.000, 33.000, 30.000 €</strong></p>
<ol>
  <li>Ordenados: 28.000, 29.000, 30.000, <strong>31.000</strong>, 33.000, 35.000, 95.000</li>
  <li>n = 7 (impar) → posición central = (7+1)/2 = 4ª</li>
  <li>Mediana = <strong>31.000 €</strong></li>
  <li>Media aritmética: 281.000 / 7 = 40.143 € (distorsionada por el salario de 95.000 €)</li>
</ol>
<p>La mediana refleja mejor la realidad del grupo que la media.</p>

<h2>Mediana vs Media: ¿cuándo usar cada una?</h2>
<ul>
  <li><strong>Usa la media</strong> cuando los datos tienen distribución simétrica y sin outliers (alturas de adultos, temperaturas, tiempos de producción estandarizados).</li>
  <li><strong>Usa la mediana</strong> cuando hay outliers o distribución asimétrica: salarios, precios de vivienda, ingresos familiares, tiempos de espera en servicios de urgencia.</li>
</ul>

<h2>Aplicaciones de la mediana en distintos sectores</h2>
<ul>
  <li><strong>Economía y salarios:</strong> El INE y Eurostat publican salarios medianos (no medios) para describir mejor la distribución real de ingresos.</li>
  <li><strong>Inmobiliario:</strong> El precio mediano de la vivienda separa el mercado en dos mitades iguales por número de transacciones.</li>
  <li><strong>Sistemas informáticos:</strong> La latencia P50 (percentil 50) en sistemas web es la mediana del tiempo de respuesta.</li>
  <li><strong>Medicina:</strong> La supervivencia mediana en oncología indica el tiempo tras el cual el 50 % de los pacientes sigue vivo.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is the median and what is it used for?</h2>
<p>The <strong>median</strong> is the middle value of a dataset ordered from smallest to largest. Unlike the arithmetic mean, the median is <strong>resistant to extreme values (outliers)</strong>, making it the most representative measure of central tendency in skewed distributions. For salary data, real estate prices, or system response times, the median is usually more informative than the mean.</p>

<h2>How to calculate the median</h2>
<p><strong>Step 1:</strong> Sort the data from smallest to largest.</p>
<p><strong>If there's an odd number of values:</strong> the median is the middle value.<br>
Position = (n + 1) / 2</p>
<p><strong>If there's an even number of values:</strong> the median is the average of the two middle values.<br>
Median = (value at position n/2 + value at position n/2+1) / 2</p>

<h2>Step-by-step example</h2>
<p><strong>7 employees earn: $28,000, $35,000, $31,000, $95,000, $29,000, $33,000, $30,000</strong></p>
<ol>
  <li>Sorted: 28,000, 29,000, 30,000, <strong>31,000</strong>, 33,000, 35,000, 95,000</li>
  <li>n = 7 (odd) → middle position = (7+1)/2 = 4th</li>
  <li>Median = <strong>$31,000</strong></li>
  <li>Arithmetic mean: 281,000 / 7 = $40,143 (distorted by the $95,000 salary)</li>
</ol>
<p>The median better reflects the group's reality than the mean.</p>

<h2>Median vs Mean: when to use each</h2>
<ul>
  <li><strong>Use the mean</strong> when data has a symmetric distribution with no outliers (adult heights, temperatures, standardized production times).</li>
  <li><strong>Use the median</strong> when there are outliers or asymmetric distribution: salaries, house prices, household income, emergency room wait times.</li>
</ul>

<h2>Applications of the median across sectors</h2>
<ul>
  <li><strong>Economics and salaries:</strong> Statistical agencies publish median salaries (not mean) to better describe the true distribution of income.</li>
  <li><strong>Real estate:</strong> The median house price splits the market into two equal halves by number of transactions.</li>
  <li><strong>IT systems:</strong> P50 latency (50th percentile) in web systems is the median response time.</li>
  <li><strong>Medicine:</strong> Median survival in oncology indicates the time at which 50% of patients are still alive.</li>
</ul>
</section>""",
    },

    "602": {  # desviacion-estandar
        "es": """<section class="long-content">
<h2>¿Qué es la desviación estándar?</h2>
<p>La <strong>desviación estándar (σ)</strong> mide cuánto se dispersan los datos alrededor de la media. Un valor bajo indica que los datos están muy agrupados (consistentes); un valor alto indica alta variabilidad. Es la medida de dispersión más utilizada en estadística, control de calidad, finanzas y ciencia, porque se expresa en las mismas unidades que los datos originales.</p>

<h2>Fórmula de la desviación estándar</h2>
<p><strong>Población completa (σ):</strong><br>
<code>σ = √( Σ(xᵢ − μ)² / N )</code></p>
<p><strong>Muestra (s) — más común en la práctica:</strong><br>
<code>s = √( Σ(xᵢ − x̄)² / (n−1) )</code></p>
<p>La diferencia: al analizar una muestra en lugar de toda la población, se divide entre (n−1) en vez de n (corrección de Bessel) para obtener una estimación insesgada.</p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Las temperaturas máximas de 5 días en mayo fueron: 22, 25, 21, 28, 24 °C.</strong></p>
<ol>
  <li>Media (μ) = (22+25+21+28+24) / 5 = <strong>24 °C</strong></li>
  <li>Diferencias al cuadrado: (22−24)²=4, (25−24)²=1, (21−24)²=9, (28−24)²=16, (24−24)²=0</li>
  <li>Suma = 30; dividida entre 5 = 6 (varianza)</li>
  <li>σ = √6 ≈ <strong>2,45 °C</strong></li>
</ol>

<h2>La regla 68-95-99,7</h2>
<p>En una distribución normal, aproximadamente:</p>
<ul>
  <li><strong>68 %</strong> de los datos cae dentro de ±1 desviación estándar de la media.</li>
  <li><strong>95 %</strong> dentro de ±2 desviaciones estándar.</li>
  <li><strong>99,7 %</strong> dentro de ±3 desviaciones estándar.</li>
</ul>
<p>En el ejemplo anterior, el 68 % de las temperaturas cae entre 24 − 2,45 = 21,55 °C y 24 + 2,45 = 26,45 °C.</p>

<h2>Aplicaciones prácticas</h2>
<ul>
  <li><strong>Control de calidad:</strong> En producción industrial, detecta piezas fuera de tolerancia; el objetivo es σ < límite de especificación / 3.</li>
  <li><strong>Finanzas (volatilidad):</strong> La desviación estándar de los retornos diarios de una acción mide su riesgo. Mayor σ = mayor incertidumbre.</li>
  <li><strong>Educación:</strong> Normalizar notas de examen para comparar entre distintas pruebas (puntuación Z = (x − μ) / σ).</li>
  <li><strong>Meteorología:</strong> Cuantificar la variabilidad climática entre regiones o décadas.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is standard deviation?</h2>
<p><strong>Standard deviation (σ)</strong> measures how spread out data is around the mean. A low value means data points are tightly clustered (consistent); a high value indicates high variability. It's the most widely used measure of dispersion in statistics, quality control, finance, and science, because it's expressed in the same units as the original data.</p>

<h2>Standard deviation formula</h2>
<p><strong>Full population (σ):</strong><br>
<code>σ = √( Σ(xᵢ − μ)² / N )</code></p>
<p><strong>Sample (s) — more common in practice:</strong><br>
<code>s = √( Σ(xᵢ − x̄)² / (n−1) )</code></p>
<p>The difference: when analyzing a sample rather than the full population, divide by (n−1) instead of n (Bessel's correction) for an unbiased estimate.</p>

<h2>Step-by-step example</h2>
<p><strong>The maximum temperatures over 5 days in May were: 22, 25, 21, 28, 24 °C.</strong></p>
<ol>
  <li>Mean (μ) = (22+25+21+28+24) / 5 = <strong>24°C</strong></li>
  <li>Squared differences: (22−24)²=4, (25−24)²=1, (21−24)²=9, (28−24)²=16, (24−24)²=0</li>
  <li>Sum = 30; divided by 5 = 6 (variance)</li>
  <li>σ = √6 ≈ <strong>2.45°C</strong></li>
</ol>

<h2>The 68-95-99.7 rule</h2>
<p>In a normal distribution, approximately:</p>
<ul>
  <li><strong>68%</strong> of data falls within ±1 standard deviation of the mean.</li>
  <li><strong>95%</strong> within ±2 standard deviations.</li>
  <li><strong>99.7%</strong> within ±3 standard deviations.</li>
</ul>
<p>In the example above, 68% of temperatures fall between 24 − 2.45 = 21.55°C and 24 + 2.45 = 26.45°C.</p>

<h2>Practical applications</h2>
<ul>
  <li><strong>Quality control:</strong> In manufacturing, detects out-of-tolerance parts; the goal is σ &lt; specification limit / 3.</li>
  <li><strong>Finance (volatility):</strong> Standard deviation of daily stock returns measures risk. Higher σ = greater uncertainty.</li>
  <li><strong>Education:</strong> Normalize exam scores for comparison across different tests (Z-score = (x − μ) / σ).</li>
  <li><strong>Meteorology:</strong> Quantify climate variability between regions or decades.</li>
</ul>
</section>""",
    },

    "701": {  # densidad
        "es": """<section class="long-content">
<h2>¿Qué es la densidad?</h2>
<p>La <strong>densidad</strong> es la cantidad de masa contenida en un volumen determinado. Se trata de una propiedad intensiva de la materia: no depende de la cantidad del material, sino de su naturaleza. El agua tiene una densidad de 1.000 kg/m³ a 4 °C; el hierro, 7.874 kg/m³; el aire, apenas 1,225 kg/m³ a nivel del mar. La densidad explica por qué flota el hielo en el agua, por qué el aceite y el agua no se mezclan, y cómo funciona el principio de Arquímedes.</p>

<h2>Fórmula de la densidad</h2>
<p><strong>ρ = m / V</strong></p>
<p>Donde:</p>
<ul>
  <li><strong>ρ</strong> (rho) = densidad (kg/m³, g/cm³, kg/L…)</li>
  <li><strong>m</strong> = masa (kg, g)</li>
  <li><strong>V</strong> = volumen (m³, cm³, L)</li>
</ul>
<p>Las tres formas despejadas: <code>m = ρ × V</code> y <code>V = m / ρ</code></p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Una barra de aluminio pesa 540 g y tiene un volumen de 200 cm³. ¿Es realmente aluminio?</strong></p>
<ol>
  <li>ρ = m / V = 540 / 200 = <strong>2,7 g/cm³</strong></li>
  <li>Densidad del aluminio puro: 2,70 g/cm³ ✓</li>
  <li>Si la densidad fuera mayor (≈ 2,9), podría indicar una aleación con zinc u otros metales.</li>
</ol>

<h2>Densidades de materiales comunes</h2>
<ul>
  <li>Aire (20 °C): 1,204 kg/m³</li>
  <li>Agua (4 °C): 1.000 kg/m³ = 1 g/cm³</li>
  <li>Madera (pino seco): 500–600 kg/m³</li>
  <li>Hormigón: 2.200–2.400 kg/m³</li>
  <li>Aluminio: 2.700 kg/m³</li>
  <li>Hierro/acero: 7.850–7.900 kg/m³</li>
  <li>Plomo: 11.340 kg/m³</li>
  <li>Oro: 19.300 kg/m³</li>
</ul>

<h2>Aplicaciones de la densidad</h2>
<ul>
  <li><strong>Identificación de materiales:</strong> Verificar si una pieza metálica es la aleación correcta o detectar adulteraciones.</li>
  <li><strong>Flotabilidad (Arquímedes):</strong> Un objeto flota si su densidad media es menor que la del fluido que lo rodea.</li>
  <li><strong>Ingeniería y construcción:</strong> Calcular el peso de una estructura conociendo su volumen y el material.</li>
  <li><strong>Geología:</strong> La densidad de las rocas y minerales ayuda a identificarlos y a modelar el interior de la Tierra.</li>
  <li><strong>Alimentación:</strong> La densidad del mosto (1,04–1,10 g/cm³) indica el contenido de azúcar en la elaboración de vino y cerveza.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is density?</h2>
<p><strong>Density</strong> is the amount of mass contained in a given volume. It's an intensive property of matter — it doesn't depend on how much of the material you have, only its nature. Water has a density of 1,000 kg/m³ at 4°C; iron, 7,874 kg/m³; air, just 1.225 kg/m³ at sea level. Density explains why ice floats on water, why oil and water don't mix, and how Archimedes' principle works.</p>

<h2>Density formula</h2>
<p><strong>ρ = m / V</strong></p>
<p>Where:</p>
<ul>
  <li><strong>ρ</strong> (rho) = density (kg/m³, g/cm³, kg/L…)</li>
  <li><strong>m</strong> = mass (kg, g)</li>
  <li><strong>V</strong> = volume (m³, cm³, L)</li>
</ul>
<p>The three rearranged forms: <code>m = ρ × V</code> and <code>V = m / ρ</code></p>

<h2>Step-by-step example</h2>
<p><strong>An aluminum bar weighs 540 g and has a volume of 200 cm³. Is it really aluminum?</strong></p>
<ol>
  <li>ρ = m / V = 540 / 200 = <strong>2.7 g/cm³</strong></li>
  <li>Pure aluminum density: 2.70 g/cm³ ✓</li>
  <li>If density were higher (≈2.9), it could indicate an alloy with zinc or other metals.</li>
</ol>

<h2>Densities of common materials</h2>
<ul>
  <li>Air (20°C): 1.204 kg/m³</li>
  <li>Water (4°C): 1,000 kg/m³ = 1 g/cm³</li>
  <li>Pine wood (dry): 500–600 kg/m³</li>
  <li>Concrete: 2,200–2,400 kg/m³</li>
  <li>Aluminum: 2,700 kg/m³</li>
  <li>Iron/steel: 7,850–7,900 kg/m³</li>
  <li>Lead: 11,340 kg/m³</li>
  <li>Gold: 19,300 kg/m³</li>
</ul>

<h2>Applications of density</h2>
<ul>
  <li><strong>Material identification:</strong> Verify whether a metal part is the correct alloy or detect adulteration.</li>
  <li><strong>Buoyancy (Archimedes):</strong> An object floats if its average density is less than the surrounding fluid's density.</li>
  <li><strong>Engineering and construction:</strong> Calculate the weight of a structure knowing its volume and material.</li>
  <li><strong>Geology:</strong> Rock and mineral density helps identify them and model Earth's interior.</li>
  <li><strong>Food and beverage:</strong> Must density (1.04–1.10 g/cm³) indicates sugar content in wine and beer production.</li>
</ul>
</section>""",
    },

    "707": {  # ley-ohm
        "es": """<section class="long-content">
<h2>¿Qué es la Ley de Ohm?</h2>
<p>La <strong>Ley de Ohm</strong> establece la relación fundamental entre las tres magnitudes eléctricas básicas: tensión (voltios), corriente (amperios) y resistencia (ohmios). Formulada por Georg Simon Ohm en 1827, es la base de todo el cálculo eléctrico y electrónico. Con ella puedes dimensionar cables, calcular consumos, diseñar circuitos y diagnosticar averías eléctricas.</p>

<h2>Fórmulas de la Ley de Ohm</h2>
<p>La relación es: <strong>V = I × R</strong></p>
<p>Las tres formas despejadas:</p>
<ul>
  <li><strong>Tensión:</strong> V = I × R (voltios = amperios × ohmios)</li>
  <li><strong>Corriente:</strong> I = V / R (amperios = voltios / ohmios)</li>
  <li><strong>Resistencia:</strong> R = V / I (ohmios = voltios / amperios)</li>
</ul>
<p>Y la relación de <strong>potencia eléctrica:</strong> P = V × I = I² × R = V² / R</p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Tienes una bombilla de 60 W conectada a 230 V. ¿Qué corriente consume y cuál es su resistencia?</strong></p>
<ol>
  <li>Corriente: I = P / V = 60 / 230 = <strong>0,261 A</strong></li>
  <li>Resistencia: R = V / I = 230 / 0,261 = <strong>881 Ω</strong></li>
  <li>Verificación: P = I² × R = 0,261² × 881 ≈ 60 W ✓</li>
</ol>

<h2>Aplicaciones prácticas de la Ley de Ohm</h2>
<ul>
  <li><strong>Dimensionado de cables:</strong> Calcula la sección mínima del cable para que no se sobrecaliente con la corriente máxima esperada.</li>
  <li><strong>Diseño de circuitos:</strong> Elige resistencias correctas para controlar la corriente a través de LEDs y otros componentes.</li>
  <li><strong>Protecciones eléctricas:</strong> Verifica que el fusible o magnetotérmico está correctamente calibrado para el circuito.</li>
  <li><strong>Diagnóstico de averías:</strong> Mide tensión y corriente con un polímetro y calcula si la resistencia es la esperada.</li>
  <li><strong>Instalaciones fotovoltaicas:</strong> Calcula las pérdidas en el cableado entre paneles y baterías.</li>
</ul>

<h2>Límites de la Ley de Ohm</h2>
<p>La Ley de Ohm es válida para <strong>componentes óhmicos</strong>: resistencias, cables, calefactores. No aplica directamente a:</p>
<ul>
  <li><strong>Diodos y LEDs:</strong> Su resistencia varía con la tensión.</li>
  <li><strong>Transistores:</strong> Controlan la corriente de forma no lineal.</li>
  <li><strong>Condensadores e inductores:</strong> Su comportamiento depende de la frecuencia (impedancia).</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is Ohm's Law?</h2>
<p><strong>Ohm's Law</strong> establishes the fundamental relationship between the three basic electrical quantities: voltage (volts), current (amps), and resistance (ohms). Formulated by Georg Simon Ohm in 1827, it's the foundation of all electrical and electronic calculations. With it you can size cables, calculate power consumption, design circuits, and diagnose electrical faults.</p>

<h2>Ohm's Law formulas</h2>
<p>The relationship is: <strong>V = I × R</strong></p>
<p>The three rearranged forms:</p>
<ul>
  <li><strong>Voltage:</strong> V = I × R (volts = amps × ohms)</li>
  <li><strong>Current:</strong> I = V / R (amps = volts / ohms)</li>
  <li><strong>Resistance:</strong> R = V / I (ohms = volts / amps)</li>
</ul>
<p>And the related <strong>electrical power formula:</strong> P = V × I = I² × R = V² / R</p>

<h2>Step-by-step example</h2>
<p><strong>A 60 W bulb is connected to 230 V. What current does it draw and what is its resistance?</strong></p>
<ol>
  <li>Current: I = P / V = 60 / 230 = <strong>0.261 A</strong></li>
  <li>Resistance: R = V / I = 230 / 0.261 = <strong>881 Ω</strong></li>
  <li>Verification: P = I² × R = 0.261² × 881 ≈ 60 W ✓</li>
</ol>

<h2>Practical applications of Ohm's Law</h2>
<ul>
  <li><strong>Cable sizing:</strong> Calculate the minimum cable cross-section so it doesn't overheat at maximum expected current.</li>
  <li><strong>Circuit design:</strong> Choose correct resistors to control current through LEDs and other components.</li>
  <li><strong>Electrical protection:</strong> Verify that fuses or circuit breakers are correctly rated for the circuit.</li>
  <li><strong>Fault diagnosis:</strong> Measure voltage and current with a multimeter and calculate whether resistance is as expected.</li>
  <li><strong>Solar PV installations:</strong> Calculate wiring losses between panels and batteries.</li>
</ul>

<h2>Limits of Ohm's Law</h2>
<p>Ohm's Law is valid for <strong>ohmic components</strong>: resistors, cables, heaters. It doesn't apply directly to:</p>
<ul>
  <li><strong>Diodes and LEDs:</strong> Their resistance varies with voltage.</li>
  <li><strong>Transistors:</strong> They control current in a non-linear way.</li>
  <li><strong>Capacitors and inductors:</strong> Their behavior depends on frequency (impedance).</li>
</ul>
</section>""",
    },

    "801": {  # peso (weight converter)
        "es": """<section class="long-content">
<h2>Conversor de unidades de peso y masa</h2>
<p>El <strong>conversor de peso</strong> transforma de forma instantánea entre kilogramos, libras, gramos, onzas, toneladas métricas y más. Es indispensable para compras internacionales, recetas de cocina en sistemas anglosajones, control de peso corporal con dispositivos en libras, envíos postales y cualquier contexto donde coexistan el Sistema Internacional (SI) y el sistema imperial.</p>

<h2>Factores de conversión de peso</h2>
<ul>
  <li>1 kilogramo (kg) = 1.000 g = 2,2046 lb = 35,274 oz</li>
  <li>1 libra (lb) = 453,592 g = 0,4536 kg = 16 oz</li>
  <li>1 onza (oz) = 28,3495 g = 0,0625 lb</li>
  <li>1 tonelada métrica (t) = 1.000 kg = 2.204,6 lb</li>
  <li>1 tonelada corta (US ton) = 907,185 kg = 2.000 lb</li>
</ul>

<h2>Ejemplos de conversión</h2>
<p><strong>75 kg a libras (peso corporal):</strong><br>
75 × 2,2046 = <strong>165,3 lb</strong></p>
<p><strong>12 oz a gramos (receta de cocina):</strong><br>
12 × 28,3495 = <strong>340,2 g</strong></p>
<p><strong>3 libras y 5 oz a kilogramos:</strong><br>
(3 × 453,592 + 5 × 28,3495) / 1000 = <strong>1,502 kg</strong></p>

<h2>Cuándo necesitas convertir unidades de peso</h2>
<ul>
  <li><strong>Cocina anglosajona:</strong> Las recetas americanas y británicas usan oz, lb y tazas. Esta calculadora convierte directamente a gramos sin memorizar tablas.</li>
  <li><strong>Compras online internacionales:</strong> El peso máximo de envío expresado en libras en sitios de EE. UU. convertido a kg para comparar con tu báscula.</li>
  <li><strong>Fitness y nutrición:</strong> Balanzas de cocina y aplicaciones como MyFitnessPal pueden mostrar tanto gramos como oz — convierte al instante.</li>
  <li><strong>Transporte y logística:</strong> Aduanas, mensajería y carga aérea mezclan kg y lb en sus tarifas.</li>
  <li><strong>Medicina veterinaria:</strong> Dosis de medicamentos expresadas en mg/lb convertidas a mg/kg para calcular la dosis en peso métrico del animal.</li>
</ul>

<h2>Masa vs Peso: la diferencia técnica</h2>
<p>Técnicamente, la <strong>masa</strong> (kg) es la cantidad de materia, mientras que el <strong>peso</strong> es la fuerza gravitacional sobre esa masa (newtons). En la Tierra, 1 kg de masa tiene un peso de 9,81 N. Sin embargo, en el lenguaje cotidiano se usa "peso" para referirse a la masa, y esta calculadora opera con esa convención usual.</p>
</section>""",
        "en": """<section class="long-content">
<h2>Weight and mass unit converter</h2>
<p>The <strong>weight converter</strong> instantly transforms between kilograms, pounds, grams, ounces, metric tons, and more. It's essential for international shopping, cooking recipes in imperial units, body weight tracking with devices in pounds, postal shipping, and any context where the International System (SI) and imperial system coexist.</p>

<h2>Weight conversion factors</h2>
<ul>
  <li>1 kilogram (kg) = 1,000 g = 2.2046 lb = 35.274 oz</li>
  <li>1 pound (lb) = 453.592 g = 0.4536 kg = 16 oz</li>
  <li>1 ounce (oz) = 28.3495 g = 0.0625 lb</li>
  <li>1 metric ton (t) = 1,000 kg = 2,204.6 lb</li>
  <li>1 US short ton = 907.185 kg = 2,000 lb</li>
</ul>

<h2>Conversion examples</h2>
<p><strong>75 kg to pounds (body weight):</strong><br>
75 × 2.2046 = <strong>165.3 lb</strong></p>
<p><strong>12 oz to grams (cooking recipe):</strong><br>
12 × 28.3495 = <strong>340.2 g</strong></p>
<p><strong>3 lb 5 oz to kilograms:</strong><br>
(3 × 453.592 + 5 × 28.3495) / 1000 = <strong>1.502 kg</strong></p>

<h2>When you need to convert weight units</h2>
<ul>
  <li><strong>Anglo-American cooking:</strong> US and UK recipes use oz, lb, and cups. This calculator converts directly to grams without memorizing tables.</li>
  <li><strong>International online shopping:</strong> Maximum shipping weight expressed in pounds on US sites, converted to kg to compare with your scale.</li>
  <li><strong>Fitness and nutrition:</strong> Kitchen scales and apps like MyFitnessPal can show both grams and oz — convert instantly.</li>
  <li><strong>Transport and logistics:</strong> Customs, courier services, and air freight mix kg and lb in their tariffs.</li>
  <li><strong>Veterinary medicine:</strong> Drug doses expressed in mg/lb converted to mg/kg to calculate dosage from the animal's metric weight.</li>
</ul>

<h2>Mass vs Weight: the technical difference</h2>
<p>Technically, <strong>mass</strong> (kg) is the amount of matter, while <strong>weight</strong> is the gravitational force on that mass (newtons). On Earth, 1 kg of mass has a weight of 9.81 N. In everyday language, however, "weight" refers to mass — and this calculator operates on that common convention.</p>
</section>""",
    },

    "901": {  # calorias-ejercicio
        "es": """<section class="long-content">
<h2>¿Cómo se calculan las calorías quemadas haciendo ejercicio?</h2>
<p>Las <strong>calorías quemadas durante el ejercicio</strong> dependen del tipo de actividad, la duración, tu peso corporal y la intensidad del esfuerzo. La fórmula más precisa utiliza el <strong>MET (Equivalente Metabólico de Tarea)</strong>, un sistema que clasifica cada actividad según cuántas veces multiplica tu metabolismo basal en reposo. Conocer este dato te permite planificar déficits calóricos reales para perder peso, o superávits para ganar músculo.</p>

<h2>Fórmula de las calorías quemadas</h2>
<p><strong>Calorías quemadas = MET × peso(kg) × tiempo(h)</strong></p>
<p>O en kcal/min: <strong>kcal/min = (MET × 3,5 × peso_kg) / 200</strong></p>
<p>El MET del reposo absoluto es 1. Caminar a paso ligero tiene un MET de 3,5; correr a 10 km/h, un MET de 10; nadar a ritmo moderado, un MET de 5,8.</p>

<h2>Ejemplo paso a paso</h2>
<p><strong>Persona de 70 kg que corre 45 minutos a 10 km/h (MET = 10).</strong></p>
<ol>
  <li>Tiempo: 45 min = 0,75 h</li>
  <li>Calorías = 10 × 70 × 0,75 = <strong>525 kcal</strong></li>
  <li>Equivale a: 3 plátanos grandes, una pizza pequeña o ≈ 75 g de chocolate negro.</li>
</ol>

<h2>MET de actividades comunes</h2>
<ul>
  <li>Caminar lento (4 km/h): MET 2,8</li>
  <li>Caminar rápido (6 km/h): MET 4,3</li>
  <li>Ciclismo suave (15 km/h): MET 5,8</li>
  <li>Natación moderada: MET 5,8</li>
  <li>Fútbol en partido: MET 10</li>
  <li>Correr a 10 km/h: MET 10</li>
  <li>Correr a 14 km/h: MET 13,5</li>
  <li>Saltar a la comba: MET 12,3</li>
  <li>HIIT (alta intensidad): MET 8–14</li>
</ul>

<h2>Factores que afectan al gasto calórico real</h2>
<ul>
  <li><strong>Peso corporal:</strong> Pesar más significa quemar más calorías en el mismo ejercicio (más masa que mover).</li>
  <li><strong>Nivel de forma física:</strong> Las personas más entrenadas son más eficientes y queman ligeramente menos calorías en el mismo esfuerzo.</li>
  <li><strong>Temperatura ambiental:</strong> El frío extremo incrementa el gasto calórico por termorregulación.</li>
  <li><strong>EPOC (Efecto Afterburn):</strong> Tras ejercicios intensos, el metabolismo permanece elevado 12–24 h adicionales, sumando un 5–15 % más de calorías quemadas.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>How are exercise calories calculated?</h2>
<p><strong>Calories burned during exercise</strong> depend on activity type, duration, your body weight, and exercise intensity. The most accurate formula uses the <strong>MET (Metabolic Equivalent of Task)</strong>, a system that classifies each activity by how many times it multiplies your resting metabolic rate. Knowing this lets you plan real caloric deficits for weight loss or surpluses for muscle gain.</p>

<h2>Calories burned formula</h2>
<p><strong>Calories burned = MET × weight(kg) × time(h)</strong></p>
<p>Or in kcal/min: <strong>kcal/min = (MET × 3.5 × body_weight_kg) / 200</strong></p>
<p>Absolute rest has a MET of 1. Brisk walking has MET 3.5; running at 10 km/h, MET 10; moderate swimming, MET 5.8.</p>

<h2>Step-by-step example</h2>
<p><strong>A 70 kg person runs 45 minutes at 10 km/h (MET = 10).</strong></p>
<ol>
  <li>Time: 45 min = 0.75 h</li>
  <li>Calories = 10 × 70 × 0.75 = <strong>525 kcal</strong></li>
  <li>Equivalent to: 3 large bananas, a small pizza, or ≈75 g of dark chocolate.</li>
</ol>

<h2>MET values for common activities</h2>
<ul>
  <li>Slow walking (4 km/h): MET 2.8</li>
  <li>Brisk walking (6 km/h): MET 4.3</li>
  <li>Easy cycling (15 km/h): MET 5.8</li>
  <li>Moderate swimming: MET 5.8</li>
  <li>Soccer match: MET 10</li>
  <li>Running at 10 km/h: MET 10</li>
  <li>Running at 14 km/h: MET 13.5</li>
  <li>Jump rope: MET 12.3</li>
  <li>HIIT (high intensity): MET 8–14</li>
</ul>

<h2>Factors that affect real caloric expenditure</h2>
<ul>
  <li><strong>Body weight:</strong> Weighing more means burning more calories for the same exercise (more mass to move).</li>
  <li><strong>Fitness level:</strong> Fitter people are more efficient and burn slightly fewer calories at the same effort.</li>
  <li><strong>Ambient temperature:</strong> Extreme cold increases caloric expenditure through thermoregulation.</li>
  <li><strong>EPOC (Afterburn Effect):</strong> After intense exercise, metabolism stays elevated for 12–24 additional hours, burning an extra 5–15% of calories.</li>
</ul>
</section>""",
    },

    "902": {  # frecuencia-cardiaca-max
        "es": """<section class="long-content">
<h2>¿Qué es la frecuencia cardíaca máxima (FCmáx)?</h2>
<p>La <strong>frecuencia cardíaca máxima (FCmáx)</strong> es el número máximo de latidos por minuto que tu corazón puede alcanzar durante un esfuerzo físico exhaustivo. Es el punto de referencia fundamental para diseñar zonas de entrenamiento cardíaco, optimizar el rendimiento deportivo y garantizar que el ejercicio es seguro y eficaz. No es posible mantenerla más de unos segundos sin que el organismo entre en fatiga extrema.</p>

<h2>Fórmulas para calcular la FCmáx</h2>
<p>Existen varias fórmulas. Las más utilizadas son:</p>
<ul>
  <li><strong>Fórmula clásica (Fox, 1971):</strong> FCmáx = 220 − edad (la más popular pero la menos precisa)</li>
  <li><strong>Fórmula de Tanaka (2001):</strong> FCmáx = 208 − (0,7 × edad) (más precisa para adultos mayores)</li>
  <li><strong>Fórmula de Gelish (2007):</strong> FCmáx = 207 − (0,7 × edad) (buena para deportistas)</li>
  <li><strong>Prueba de esfuerzo:</strong> La medición real con electrocardiograma es siempre más precisa que cualquier fórmula.</li>
</ul>

<h2>Ejemplo de cálculo para un adulto de 35 años</h2>
<ol>
  <li>Fox: 220 − 35 = <strong>185 ppm</strong></li>
  <li>Tanaka: 208 − (0,7 × 35) = 208 − 24,5 = <strong>183,5 ppm</strong></li>
  <li>Gelish: 207 − (0,7 × 35) = 207 − 24,5 = <strong>182,5 ppm</strong></li>
</ol>

<h2>Las 5 zonas de entrenamiento cardíaco</h2>
<p>Basadas en un porcentaje de la FCmáx:</p>
<ul>
  <li><strong>Zona 1 (50–60 % FCmáx):</strong> Recuperación activa. Caminar suave, calentamiento.</li>
  <li><strong>Zona 2 (60–70 % FCmáx):</strong> Resistencia aeróbica base. El 70–80 % del volumen de entrenamiento debe hacerse aquí.</li>
  <li><strong>Zona 3 (70–80 % FCmáx):</strong> Desarrollo aeróbico. Conversación difícil pero posible.</li>
  <li><strong>Zona 4 (80–90 % FCmáx):</strong> Umbral anaeróbico. Esfuerzo intenso, mejora del rendimiento.</li>
  <li><strong>Zona 5 (90–100 % FCmáx):</strong> Máximo anaeróbico. Sprints cortos, solo sostenible segundos o pocos minutos.</li>
</ul>

<h2>FCmáx en la práctica deportiva</h2>
<ul>
  <li><strong>Pérdida de grasa:</strong> La zona 2 (60–70 %) quema un mayor porcentaje de grasa como combustible, aunque la zona 3–4 quema más calorías en total.</li>
  <li><strong>Mejora cardiovascular:</strong> El entrenamiento en zona 4 con intervalos (HIIT) es el más eficiente para mejorar el VO2 máx.</li>
  <li><strong>Prevención de sobreentrenamiento:</strong> Monitorizar la FC evita entrenar en exceso, especialmente en semanas de carga alta.</li>
  <li><strong>Rehabilitación cardíaca:</strong> Los programas de rehabilitación limitan el esfuerzo a zonas 1–2 para pacientes con enfermedades cardiovasculares.</li>
</ul>
</section>""",
        "en": """<section class="long-content">
<h2>What is maximum heart rate (MHR)?</h2>
<p>Your <strong>maximum heart rate (MHR)</strong> is the highest number of beats per minute your heart can achieve during exhaustive physical effort. It's the fundamental reference point for designing heart rate training zones, optimizing athletic performance, and ensuring exercise is safe and effective. It cannot be sustained for more than a few seconds before the body enters extreme fatigue.</p>

<h2>Formulas for calculating MHR</h2>
<p>Several formulas exist. The most widely used are:</p>
<ul>
  <li><strong>Classic formula (Fox, 1971):</strong> MHR = 220 − age (most popular but least precise)</li>
  <li><strong>Tanaka formula (2001):</strong> MHR = 208 − (0.7 × age) (more accurate for older adults)</li>
  <li><strong>Gelish formula (2007):</strong> MHR = 207 − (0.7 × age) (good for athletes)</li>
  <li><strong>Stress test:</strong> Actual ECG measurement is always more precise than any formula.</li>
</ul>

<h2>Example calculation for a 35-year-old adult</h2>
<ol>
  <li>Fox: 220 − 35 = <strong>185 bpm</strong></li>
  <li>Tanaka: 208 − (0.7 × 35) = 208 − 24.5 = <strong>183.5 bpm</strong></li>
  <li>Gelish: 207 − (0.7 × 35) = 207 − 24.5 = <strong>182.5 bpm</strong></li>
</ol>

<h2>The 5 heart rate training zones</h2>
<p>Based on a percentage of MHR:</p>
<ul>
  <li><strong>Zone 1 (50–60% MHR):</strong> Active recovery. Easy walking, warm-up.</li>
  <li><strong>Zone 2 (60–70% MHR):</strong> Aerobic base endurance. 70–80% of training volume should be here.</li>
  <li><strong>Zone 3 (70–80% MHR):</strong> Aerobic development. Conversation is difficult but possible.</li>
  <li><strong>Zone 4 (80–90% MHR):</strong> Anaerobic threshold. Intense effort, performance improvement.</li>
  <li><strong>Zone 5 (90–100% MHR):</strong> Max anaerobic. Short sprints, sustainable only for seconds or a few minutes.</li>
</ul>

<h2>MHR in sports practice</h2>
<ul>
  <li><strong>Fat loss:</strong> Zone 2 (60–70%) burns a higher percentage of fat as fuel, though zones 3–4 burn more total calories.</li>
  <li><strong>Cardiovascular improvement:</strong> Zone 4 interval training (HIIT) is most efficient for improving VO2 max.</li>
  <li><strong>Overtraining prevention:</strong> Monitoring HR prevents overtraining, especially during high-load weeks.</li>
  <li><strong>Cardiac rehabilitation:</strong> Rehabilitation programs limit effort to zones 1–2 for patients with cardiovascular disease.</li>
</ul>
</section>""",
    },

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

    "001": {"en": {"f": "Hormigon Masa = f(largo, ancho, espesor)", "ei": "5 m; 3 m; 0.2 m", "eo": "Results calculated from 3 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Hormigon Masa = f(largo, ancho, espesor)", "ei": "5 m; 3 m; 0.2 m", "eo": "Results calculated from 3 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Hormigon Masa = f(largo, ancho, espesor)", "ei": "5 m; 3 m; 0.2 m", "eo": "Results calculated from 3 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Hormigon Masa = f(largo, ancho, espesor)", "ei": "5 m; 3 m; 0.2 m", "eo": "Results calculated from 3 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Hormigon Masa = f(largo, ancho, espesor)", "ei": "5 m; 3 m; 0.2 m", "eo": "Results calculated from 3 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Hormigon Masa = f(largo, ancho, espesor)", "ei": "5 m; 3 m; 0.2 m", "eo": "Results calculated from 3 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "002": {"en": {"f": "Hormigon Armado = f(largo, ancho, espesor, kg_acero_m3)", "ei": "5 m; 3 m; 0.25 m; 100 kg/m³", "eo": "Results calculated from 4 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Hormigon Armado = f(largo, ancho, espesor, kg_acero_m3)", "ei": "5 m; 3 m; 0.25 m; 100 kg/m³", "eo": "Results calculated from 4 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Hormigon Armado = f(largo, ancho, espesor, kg_acero_m3)", "ei": "5 m; 3 m; 0.25 m; 100 kg/m³", "eo": "Results calculated from 4 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Hormigon Armado = f(largo, ancho, espesor, kg_acero_m3)", "ei": "5 m; 3 m; 0.25 m; 100 kg/m³", "eo": "Results calculated from 4 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Hormigon Armado = f(largo, ancho, espesor, kg_acero_m3)", "ei": "5 m; 3 m; 0.25 m; 100 kg/m³", "eo": "Results calculated from 4 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Hormigon Armado = f(largo, ancho, espesor, kg_acero_m3)", "ei": "5 m; 3 m; 0.25 m; 100 kg/m³", "eo": "Results calculated from 4 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "003": {"en": {"f": "Zapata Aislada = f(largo, ancho, canto, cantidad)", "ei": "1.5 m; 1.5 m; 0.5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Zapata Aislada = f(largo, ancho, canto, cantidad)", "ei": "1.5 m; 1.5 m; 0.5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Zapata Aislada = f(largo, ancho, canto, cantidad)", "ei": "1.5 m; 1.5 m; 0.5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Zapata Aislada = f(largo, ancho, canto, cantidad)", "ei": "1.5 m; 1.5 m; 0.5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Zapata Aislada = f(largo, ancho, canto, cantidad)", "ei": "1.5 m; 1.5 m; 0.5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Zapata Aislada = f(largo, ancho, canto, cantidad)", "ei": "1.5 m; 1.5 m; 0.5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "004": {"en": {"f": "Muro Contencion = f(largo, altura, espesor_base, espesor_corona)", "ei": "10 m; 2 m; 0.4 m; 0.3 m", "eo": "Results calculated from 4 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Muro Contencion = f(largo, altura, espesor_base, espesor_corona)", "ei": "10 m; 2 m; 0.4 m; 0.3 m", "eo": "Results calculated from 4 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Muro Contencion = f(largo, altura, espesor_base, espesor_corona)", "ei": "10 m; 2 m; 0.4 m; 0.3 m", "eo": "Results calculated from 4 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Muro Contencion = f(largo, altura, espesor_base, espesor_corona)", "ei": "10 m; 2 m; 0.4 m; 0.3 m", "eo": "Results calculated from 4 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Muro Contencion = f(largo, altura, espesor_base, espesor_corona)", "ei": "10 m; 2 m; 0.4 m; 0.3 m", "eo": "Results calculated from 4 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Muro Contencion = f(largo, altura, espesor_base, espesor_corona)", "ei": "10 m; 2 m; 0.4 m; 0.3 m", "eo": "Results calculated from 4 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "005": {"en": {"f": "Pilares Hormigon = f(ancho, profundidad, altura, cantidad)", "ei": "0.3 m; 0.3 m; 3 m; 6 ud", "eo": "Results calculated from 4 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Pilares Hormigon = f(ancho, profundidad, altura, cantidad)", "ei": "0.3 m; 0.3 m; 3 m; 6 ud", "eo": "Results calculated from 4 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Pilares Hormigon = f(ancho, profundidad, altura, cantidad)", "ei": "0.3 m; 0.3 m; 3 m; 6 ud", "eo": "Results calculated from 4 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Pilares Hormigon = f(ancho, profundidad, altura, cantidad)", "ei": "0.3 m; 0.3 m; 3 m; 6 ud", "eo": "Results calculated from 4 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Pilares Hormigon = f(ancho, profundidad, altura, cantidad)", "ei": "0.3 m; 0.3 m; 3 m; 6 ud", "eo": "Results calculated from 4 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Pilares Hormigon = f(ancho, profundidad, altura, cantidad)", "ei": "0.3 m; 0.3 m; 3 m; 6 ud", "eo": "Results calculated from 4 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "006": {"en": {"f": "Vigas Hormigon = f(ancho, canto, longitud, cantidad)", "ei": "0.25 m; 0.5 m; 5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Vigas Hormigon = f(ancho, canto, longitud, cantidad)", "ei": "0.25 m; 0.5 m; 5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Vigas Hormigon = f(ancho, canto, longitud, cantidad)", "ei": "0.25 m; 0.5 m; 5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Vigas Hormigon = f(ancho, canto, longitud, cantidad)", "ei": "0.25 m; 0.5 m; 5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Vigas Hormigon = f(ancho, canto, longitud, cantidad)", "ei": "0.25 m; 0.5 m; 5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Vigas Hormigon = f(ancho, canto, longitud, cantidad)", "ei": "0.25 m; 0.5 m; 5 m; 4 ud", "eo": "Results calculated from 4 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "007": {"en": {"f": "Forjado Vigueta = f(largo, ancho, intereje, canto_forjado)", "ei": "8 m; 6 m; 0.7 m; 0.25 m", "eo": "Results calculated from 4 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Forjado Vigueta = f(largo, ancho, intereje, canto_forjado)", "ei": "8 m; 6 m; 0.7 m; 0.25 m", "eo": "Results calculated from 4 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Forjado Vigueta = f(largo, ancho, intereje, canto_forjado)", "ei": "8 m; 6 m; 0.7 m; 0.25 m", "eo": "Results calculated from 4 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Forjado Vigueta = f(largo, ancho, intereje, canto_forjado)", "ei": "8 m; 6 m; 0.7 m; 0.25 m", "eo": "Results calculated from 4 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Forjado Vigueta = f(largo, ancho, intereje, canto_forjado)", "ei": "8 m; 6 m; 0.7 m; 0.25 m", "eo": "Results calculated from 4 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Forjado Vigueta = f(largo, ancho, intereje, canto_forjado)", "ei": "8 m; 6 m; 0.7 m; 0.25 m", "eo": "Results calculated from 4 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "008": {"en": {"f": "Losa Hormigon = f(largo, ancho, espesor, kg_acero_m2)", "ei": "6 m; 4 m; 0.2 m; 12 kg/m²", "eo": "Results calculated from 4 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Losa Hormigon = f(largo, ancho, espesor, kg_acero_m2)", "ei": "6 m; 4 m; 0.2 m; 12 kg/m²", "eo": "Results calculated from 4 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Losa Hormigon = f(largo, ancho, espesor, kg_acero_m2)", "ei": "6 m; 4 m; 0.2 m; 12 kg/m²", "eo": "Results calculated from 4 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Losa Hormigon = f(largo, ancho, espesor, kg_acero_m2)", "ei": "6 m; 4 m; 0.2 m; 12 kg/m²", "eo": "Results calculated from 4 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Losa Hormigon = f(largo, ancho, espesor, kg_acero_m2)", "ei": "6 m; 4 m; 0.2 m; 12 kg/m²", "eo": "Results calculated from 4 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Losa Hormigon = f(largo, ancho, espesor, kg_acero_m2)", "ei": "6 m; 4 m; 0.2 m; 12 kg/m²", "eo": "Results calculated from 4 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "009": {"en": {"f": "Cimiento Corrido = f(longitud, ancho, profundidad)", "ei": "20 m; 0.6 m; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Cimiento Corrido = f(longitud, ancho, profundidad)", "ei": "20 m; 0.6 m; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Cimiento Corrido = f(longitud, ancho, profundidad)", "ei": "20 m; 0.6 m; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Cimiento Corrido = f(longitud, ancho, profundidad)", "ei": "20 m; 0.6 m; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Cimiento Corrido = f(longitud, ancho, profundidad)", "ei": "20 m; 0.6 m; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Cimiento Corrido = f(longitud, ancho, profundidad)", "ei": "20 m; 0.6 m; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "010": {"en": {"f": "Excavacion Tierra = f(largo, ancho, profundidad, esponjamiento)", "ei": "10 m; 6 m; 1.5 m; 1.25 factor", "eo": "Results calculated from 4 inputs", "u": ["residential foundation calculations", "concrete ordering for construction projects", "structural material estimation", "DIY home improvement planning"]}, "es": {"f": "Excavacion Tierra = f(largo, ancho, profundidad, esponjamiento)", "ei": "10 m; 6 m; 1.5 m; 1.25 factor", "eo": "Results calculated from 4 inputs", "u": ["cálculos de cimentación residencial", "pedidos de concreto para proyectos de construcción", "estimación de materiales estructurales", "planificación de mejoras del hogar"]}, "fr": {"f": "Excavacion Tierra = f(largo, ancho, profundidad, esponjamiento)", "ei": "10 m; 6 m; 1.5 m; 1.25 factor", "eo": "Results calculated from 4 inputs", "u": ["calculs de fondations résidentielles", "commandes de béton pour projets de construction", "estimation de matériaux structurels", "planification de rénovations"]}, "pt": {"f": "Excavacion Tierra = f(largo, ancho, profundidad, esponjamiento)", "ei": "10 m; 6 m; 1.5 m; 1.25 factor", "eo": "Results calculated from 4 inputs", "u": ["cálculos de fundação residencial", "pedidos de concreto para projetos de construção", "estimativa de materiais estruturais", "planejamento de melhorias domésticas"]}, "de": {"f": "Excavacion Tierra = f(largo, ancho, profundidad, esponjamiento)", "ei": "10 m; 6 m; 1.5 m; 1.25 factor", "eo": "Results calculated from 4 inputs", "u": ["Berechnungen für Wohnungsfundamente", "Betonbestellungen für Bauprojekte", "Schätzungen von Baumaterialien", "Heimwerker-Planung"]}, "it": {"f": "Excavacion Tierra = f(largo, ancho, profundidad, esponjamiento)", "ei": "10 m; 6 m; 1.5 m; 1.25 factor", "eo": "Results calculated from 4 inputs", "u": ["calcoli di fondazioni residenziali", "ordini di calcestruzzo per progetti edilizi", "stima di materiali strutturali", "pianificazione di miglioramenti domestici"]}},
    "011": {"en": {"f": "Ladrillo Hueco = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 2.5 m²", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Ladrillo Hueco = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 2.5 m²", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Ladrillo Hueco = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 2.5 m²", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Ladrillo Hueco = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 2.5 m²", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Ladrillo Hueco = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 2.5 m²", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Ladrillo Hueco = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 2.5 m²", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "012": {"en": {"f": "Ladrillo Cara Vista = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 4 m²", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Ladrillo Cara Vista = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 4 m²", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Ladrillo Cara Vista = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 4 m²", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Ladrillo Cara Vista = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 4 m²", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Ladrillo Cara Vista = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 4 m²", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Ladrillo Cara Vista = f(largo, alto, descontar_huecos)", "ei": "8 m; 2.8 m; 4 m²", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "013": {"en": {"f": "Bloque Hormigon = f(largo, alto, descontar_huecos)", "ei": "10 m; 3 m; 3 m²", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Bloque Hormigon = f(largo, alto, descontar_huecos)", "ei": "10 m; 3 m; 3 m²", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Bloque Hormigon = f(largo, alto, descontar_huecos)", "ei": "10 m; 3 m; 3 m²", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Bloque Hormigon = f(largo, alto, descontar_huecos)", "ei": "10 m; 3 m; 3 m²", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Bloque Hormigon = f(largo, alto, descontar_huecos)", "ei": "10 m; 3 m; 3 m²", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Bloque Hormigon = f(largo, alto, descontar_huecos)", "ei": "10 m; 3 m; 3 m²", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "014": {"en": {"f": "Tabique Pladur = f(largo, alto, tipo_placa, aislamiento)", "ei": "10 m; 2.6 m; single; si", "eo": "Results calculated from 4 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Tabique Pladur = f(largo, alto, tipo_placa, aislamiento)", "ei": "10 m; 2.6 m; single; si", "eo": "Results calculated from 4 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Tabique Pladur = f(largo, alto, tipo_placa, aislamiento)", "ei": "10 m; 2.6 m; single; si", "eo": "Results calculated from 4 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Tabique Pladur = f(largo, alto, tipo_placa, aislamiento)", "ei": "10 m; 2.6 m; single; si", "eo": "Results calculated from 4 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Tabique Pladur = f(largo, alto, tipo_placa, aislamiento)", "ei": "10 m; 2.6 m; single; si", "eo": "Results calculated from 4 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Tabique Pladur = f(largo, alto, tipo_placa, aislamiento)", "ei": "10 m; 2.6 m; single; si", "eo": "Results calculated from 4 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "015": {"en": {"f": "Aislamiento Termico = f(largo, alto, espesor_cm)", "ei": "10 m; 3 m; 6 cm", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Aislamiento Termico = f(largo, alto, espesor_cm)", "ei": "10 m; 3 m; 6 cm", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Aislamiento Termico = f(largo, alto, espesor_cm)", "ei": "10 m; 3 m; 6 cm", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Aislamiento Termico = f(largo, alto, espesor_cm)", "ei": "10 m; 3 m; 6 cm", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Aislamiento Termico = f(largo, alto, espesor_cm)", "ei": "10 m; 3 m; 6 cm", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Aislamiento Termico = f(largo, alto, espesor_cm)", "ei": "10 m; 3 m; 6 cm", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "016": {"en": {"f": "Revoco Proyectado = f(area, espesor_mm)", "ei": "50 m²; 15 mm", "eo": "Results calculated from 2 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Revoco Proyectado = f(area, espesor_mm)", "ei": "50 m²; 15 mm", "eo": "Results calculated from 2 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Revoco Proyectado = f(area, espesor_mm)", "ei": "50 m²; 15 mm", "eo": "Results calculated from 2 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Revoco Proyectado = f(area, espesor_mm)", "ei": "50 m²; 15 mm", "eo": "Results calculated from 2 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Revoco Proyectado = f(area, espesor_mm)", "ei": "50 m²; 15 mm", "eo": "Results calculated from 2 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Revoco Proyectado = f(area, espesor_mm)", "ei": "50 m²; 15 mm", "eo": "Results calculated from 2 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "017": {"en": {"f": "Mortero Cemento = f(area, espesor_cm, dosificacion)", "ei": "30 m²; 2 cm; 300 kg/m³", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Mortero Cemento = f(area, espesor_cm, dosificacion)", "ei": "30 m²; 2 cm; 300 kg/m³", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Mortero Cemento = f(area, espesor_cm, dosificacion)", "ei": "30 m²; 2 cm; 300 kg/m³", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Mortero Cemento = f(area, espesor_cm, dosificacion)", "ei": "30 m²; 2 cm; 300 kg/m³", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Mortero Cemento = f(area, espesor_cm, dosificacion)", "ei": "30 m²; 2 cm; 300 kg/m³", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Mortero Cemento = f(area, espesor_cm, dosificacion)", "ei": "30 m²; 2 cm; 300 kg/m³", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "018": {"en": {"f": "Enfoscado Guarnecido = f(area, espesor_mm, tipo)", "ei": "80 m²; 15 mm; cemento", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Enfoscado Guarnecido = f(area, espesor_mm, tipo)", "ei": "80 m²; 15 mm; cemento", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Enfoscado Guarnecido = f(area, espesor_mm, tipo)", "ei": "80 m²; 15 mm; cemento", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Enfoscado Guarnecido = f(area, espesor_mm, tipo)", "ei": "80 m²; 15 mm; cemento", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Enfoscado Guarnecido = f(area, espesor_mm, tipo)", "ei": "80 m²; 15 mm; cemento", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Enfoscado Guarnecido = f(area, espesor_mm, tipo)", "ei": "80 m²; 15 mm; cemento", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "019": {"en": {"f": "Mamposteria Piedra = f(largo, alto, espesor)", "ei": "6 m; 2 m; 0.4 m", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Mamposteria Piedra = f(largo, alto, espesor)", "ei": "6 m; 2 m; 0.4 m", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Mamposteria Piedra = f(largo, alto, espesor)", "ei": "6 m; 2 m; 0.4 m", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Mamposteria Piedra = f(largo, alto, espesor)", "ei": "6 m; 2 m; 0.4 m", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Mamposteria Piedra = f(largo, alto, espesor)", "ei": "6 m; 2 m; 0.4 m", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Mamposteria Piedra = f(largo, alto, espesor)", "ei": "6 m; 2 m; 0.4 m", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "020": {"en": {"f": "Cubierta Teja = f(area_planta, pendiente_pct, tipo_teja)", "ei": "60 m²; 30 %; arabe", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Cubierta Teja = f(area_planta, pendiente_pct, tipo_teja)", "ei": "60 m²; 30 %; arabe", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Cubierta Teja = f(area_planta, pendiente_pct, tipo_teja)", "ei": "60 m²; 30 %; arabe", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Cubierta Teja = f(area_planta, pendiente_pct, tipo_teja)", "ei": "60 m²; 30 %; arabe", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Cubierta Teja = f(area_planta, pendiente_pct, tipo_teja)", "ei": "60 m²; 30 %; arabe", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Cubierta Teja = f(area_planta, pendiente_pct, tipo_teja)", "ei": "60 m²; 30 %; arabe", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "021": {"en": {"f": "Solado Ceramico = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "25 m²; 60 cm; 4 ud", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Solado Ceramico = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "25 m²; 60 cm; 4 ud", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Solado Ceramico = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "25 m²; 60 cm; 4 ud", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Solado Ceramico = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "25 m²; 60 cm; 4 ud", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Solado Ceramico = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "25 m²; 60 cm; 4 ud", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Solado Ceramico = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "25 m²; 60 cm; 4 ud", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "022": {"en": {"f": "Porcelanico = f(area, m2_por_caja)", "ei": "30 m²; 1.44 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Porcelanico = f(area, m2_por_caja)", "ei": "30 m²; 1.44 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Porcelanico = f(area, m2_por_caja)", "ei": "30 m²; 1.44 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Porcelanico = f(area, m2_por_caja)", "ei": "30 m²; 1.44 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Porcelanico = f(area, m2_por_caja)", "ei": "30 m²; 1.44 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Porcelanico = f(area, m2_por_caja)", "ei": "30 m²; 1.44 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "023": {"en": {"f": "Laminado Flotante = f(area, m2_por_caja)", "ei": "20 m²; 2.5 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Laminado Flotante = f(area, m2_por_caja)", "ei": "20 m²; 2.5 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Laminado Flotante = f(area, m2_por_caja)", "ei": "20 m²; 2.5 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Laminado Flotante = f(area, m2_por_caja)", "ei": "20 m²; 2.5 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Laminado Flotante = f(area, m2_por_caja)", "ei": "20 m²; 2.5 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Laminado Flotante = f(area, m2_por_caja)", "ei": "20 m²; 2.5 m²/caja", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "024": {"en": {"f": "Parquet Madera = f(area, m2_por_caja, colocacion)", "ei": "25 m²; 2.2 m²/caja; recto", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Parquet Madera = f(area, m2_por_caja, colocacion)", "ei": "25 m²; 2.2 m²/caja; recto", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Parquet Madera = f(area, m2_por_caja, colocacion)", "ei": "25 m²; 2.2 m²/caja; recto", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Parquet Madera = f(area, m2_por_caja, colocacion)", "ei": "25 m²; 2.2 m²/caja; recto", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Parquet Madera = f(area, m2_por_caja, colocacion)", "ei": "25 m²; 2.2 m²/caja; recto", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Parquet Madera = f(area, m2_por_caja, colocacion)", "ei": "25 m²; 2.2 m²/caja; recto", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "025": {"en": {"f": "Marmol Granito = f(area, espesor_cm, tipo)", "ei": "15 m²; 2 cm; marmol", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Marmol Granito = f(area, espesor_cm, tipo)", "ei": "15 m²; 2 cm; marmol", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Marmol Granito = f(area, espesor_cm, tipo)", "ei": "15 m²; 2 cm; marmol", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Marmol Granito = f(area, espesor_cm, tipo)", "ei": "15 m²; 2 cm; marmol", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Marmol Granito = f(area, espesor_cm, tipo)", "ei": "15 m²; 2 cm; marmol", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Marmol Granito = f(area, espesor_cm, tipo)", "ei": "15 m²; 2 cm; marmol", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "026": {"en": {"f": "Terrazo = f(area, tam_pieza_cm, incluye_mortero)", "ei": "30 m²; 40 cm; si", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Terrazo = f(area, tam_pieza_cm, incluye_mortero)", "ei": "30 m²; 40 cm; si", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Terrazo = f(area, tam_pieza_cm, incluye_mortero)", "ei": "30 m²; 40 cm; si", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Terrazo = f(area, tam_pieza_cm, incluye_mortero)", "ei": "30 m²; 40 cm; si", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Terrazo = f(area, tam_pieza_cm, incluye_mortero)", "ei": "30 m²; 40 cm; si", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Terrazo = f(area, tam_pieza_cm, incluye_mortero)", "ei": "30 m²; 40 cm; si", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "027": {"en": {"f": "Azulejo Pared = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "20 m²; 30 cm; 10 ud", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Azulejo Pared = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "20 m²; 30 cm; 10 ud", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Azulejo Pared = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "20 m²; 30 cm; 10 ud", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Azulejo Pared = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "20 m²; 30 cm; 10 ud", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Azulejo Pared = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "20 m²; 30 cm; 10 ud", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Azulejo Pared = f(area, tam_pieza_cm, piezas_por_caja)", "ei": "20 m²; 30 cm; 10 ud", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "028": {"en": {"f": "Mosaico = f(area, tam_malla_cm)", "ei": "8 m²; 30 cm", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Mosaico = f(area, tam_malla_cm)", "ei": "8 m²; 30 cm", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Mosaico = f(area, tam_malla_cm)", "ei": "8 m²; 30 cm", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Mosaico = f(area, tam_malla_cm)", "ei": "8 m²; 30 cm", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Mosaico = f(area, tam_malla_cm)", "ei": "8 m²; 30 cm", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Mosaico = f(area, tam_malla_cm)", "ei": "8 m²; 30 cm", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "029": {"en": {"f": "Adhesivo Ceramico = f(area, tipo_colocacion)", "ei": "25 m²; suelo", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Adhesivo Ceramico = f(area, tipo_colocacion)", "ei": "25 m²; suelo", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Adhesivo Ceramico = f(area, tipo_colocacion)", "ei": "25 m²; suelo", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Adhesivo Ceramico = f(area, tipo_colocacion)", "ei": "25 m²; suelo", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Adhesivo Ceramico = f(area, tipo_colocacion)", "ei": "25 m²; suelo", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Adhesivo Ceramico = f(area, tipo_colocacion)", "ei": "25 m²; suelo", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "030": {"en": {"f": "Lechada Junta = f(area, tam_pieza_cm, ancho_junta_mm, grosor_pieza_mm)", "ei": "25 m²; 60 cm; 3 mm; 10 mm", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Lechada Junta = f(area, tam_pieza_cm, ancho_junta_mm, grosor_pieza_mm)", "ei": "25 m²; 60 cm; 3 mm; 10 mm", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Lechada Junta = f(area, tam_pieza_cm, ancho_junta_mm, grosor_pieza_mm)", "ei": "25 m²; 60 cm; 3 mm; 10 mm", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Lechada Junta = f(area, tam_pieza_cm, ancho_junta_mm, grosor_pieza_mm)", "ei": "25 m²; 60 cm; 3 mm; 10 mm", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Lechada Junta = f(area, tam_pieza_cm, ancho_junta_mm, grosor_pieza_mm)", "ei": "25 m²; 60 cm; 3 mm; 10 mm", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Lechada Junta = f(area, tam_pieza_cm, ancho_junta_mm, grosor_pieza_mm)", "ei": "25 m²; 60 cm; 3 mm; 10 mm", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "031": {"en": {"f": "Tuberia Pvc Saneamiento = f(longitud, tramos)", "ei": "20 m; 4 tramos", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tuberia Pvc Saneamiento = f(longitud, tramos)", "ei": "20 m; 4 tramos", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tuberia Pvc Saneamiento = f(longitud, tramos)", "ei": "20 m; 4 tramos", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tuberia Pvc Saneamiento = f(longitud, tramos)", "ei": "20 m; 4 tramos", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tuberia Pvc Saneamiento = f(longitud, tramos)", "ei": "20 m; 4 tramos", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tuberia Pvc Saneamiento = f(longitud, tramos)", "ei": "20 m; 4 tramos", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "032": {"en": {"f": "Tuberia Cobre Pex = f(longitud, puntos_suministro)", "ei": "25 m; 6 ud", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tuberia Cobre Pex = f(longitud, puntos_suministro)", "ei": "25 m; 6 ud", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tuberia Cobre Pex = f(longitud, puntos_suministro)", "ei": "25 m; 6 ud", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tuberia Cobre Pex = f(longitud, puntos_suministro)", "ei": "25 m; 6 ud", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tuberia Cobre Pex = f(longitud, puntos_suministro)", "ei": "25 m; 6 ud", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tuberia Cobre Pex = f(longitud, puntos_suministro)", "ei": "25 m; 6 ud", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "033": {"en": {"f": "Presion Agua = f(altura_m, perdidas_carga_pct)", "ei": "10 m; 15 %", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Presion Agua = f(altura_m, perdidas_carga_pct)", "ei": "10 m; 15 %", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Presion Agua = f(altura_m, perdidas_carga_pct)", "ei": "10 m; 15 %", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Presion Agua = f(altura_m, perdidas_carga_pct)", "ei": "10 m; 15 %", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Presion Agua = f(altura_m, perdidas_carga_pct)", "ei": "10 m; 15 %", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Presion Agua = f(altura_m, perdidas_carga_pct)", "ei": "10 m; 15 %", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "034": {"en": {"f": "Deposito Agua = f(personas, litros_persona_dia, dias_autonomia)", "ei": "4 personas; 150 L/p/día; 1 días", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Deposito Agua = f(personas, litros_persona_dia, dias_autonomia)", "ei": "4 personas; 150 L/p/día; 1 días", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Deposito Agua = f(personas, litros_persona_dia, dias_autonomia)", "ei": "4 personas; 150 L/p/día; 1 días", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Deposito Agua = f(personas, litros_persona_dia, dias_autonomia)", "ei": "4 personas; 150 L/p/día; 1 días", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Deposito Agua = f(personas, litros_persona_dia, dias_autonomia)", "ei": "4 personas; 150 L/p/día; 1 días", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Deposito Agua = f(personas, litros_persona_dia, dias_autonomia)", "ei": "4 personas; 150 L/p/día; 1 días", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "035": {"en": {"f": "Calentador Agua = f(litros_deposito, temp_entrada_c, temp_salida_c, horas_calentamiento)", "ei": "80 L; 12 °C; 55 °C; 2 h", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Calentador Agua = f(litros_deposito, temp_entrada_c, temp_salida_c, horas_calentamiento)", "ei": "80 L; 12 °C; 55 °C; 2 h", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Calentador Agua = f(litros_deposito, temp_entrada_c, temp_salida_c, horas_calentamiento)", "ei": "80 L; 12 °C; 55 °C; 2 h", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Calentador Agua = f(litros_deposito, temp_entrada_c, temp_salida_c, horas_calentamiento)", "ei": "80 L; 12 °C; 55 °C; 2 h", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Calentador Agua = f(litros_deposito, temp_entrada_c, temp_salida_c, horas_calentamiento)", "ei": "80 L; 12 °C; 55 °C; 2 h", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Calentador Agua = f(litros_deposito, temp_entrada_c, temp_salida_c, horas_calentamiento)", "ei": "80 L; 12 °C; 55 °C; 2 h", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "036": {"en": {"f": "Caldera Gas = f(area_m2, altura_m, aislamiento)", "ei": "100 m²; 2.7 m; medio", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Caldera Gas = f(area_m2, altura_m, aislamiento)", "ei": "100 m²; 2.7 m; medio", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Caldera Gas = f(area_m2, altura_m, aislamiento)", "ei": "100 m²; 2.7 m; medio", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Caldera Gas = f(area_m2, altura_m, aislamiento)", "ei": "100 m²; 2.7 m; medio", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Caldera Gas = f(area_m2, altura_m, aislamiento)", "ei": "100 m²; 2.7 m; medio", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Caldera Gas = f(area_m2, altura_m, aislamiento)", "ei": "100 m²; 2.7 m; medio", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "037": {"en": {"f": "Radiador Aluminio = f(area_m2, altura_m, orientacion)", "ei": "15 m²; 2.7 m; interior", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Radiador Aluminio = f(area_m2, altura_m, orientacion)", "ei": "15 m²; 2.7 m; interior", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Radiador Aluminio = f(area_m2, altura_m, orientacion)", "ei": "15 m²; 2.7 m; interior", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Radiador Aluminio = f(area_m2, altura_m, orientacion)", "ei": "15 m²; 2.7 m; interior", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Radiador Aluminio = f(area_m2, altura_m, orientacion)", "ei": "15 m²; 2.7 m; interior", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Radiador Aluminio = f(area_m2, altura_m, orientacion)", "ei": "15 m²; 2.7 m; interior", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "038": {"en": {"f": "Suelo Radiante = f(area_m2, separacion_cm, circuitos_max_m)", "ei": "80 m²; 20 cm; 80 m/circuito", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Suelo Radiante = f(area_m2, separacion_cm, circuitos_max_m)", "ei": "80 m²; 20 cm; 80 m/circuito", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Suelo Radiante = f(area_m2, separacion_cm, circuitos_max_m)", "ei": "80 m²; 20 cm; 80 m/circuito", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Suelo Radiante = f(area_m2, separacion_cm, circuitos_max_m)", "ei": "80 m²; 20 cm; 80 m/circuito", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Suelo Radiante = f(area_m2, separacion_cm, circuitos_max_m)", "ei": "80 m²; 20 cm; 80 m/circuito", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Suelo Radiante = f(area_m2, separacion_cm, circuitos_max_m)", "ei": "80 m²; 20 cm; 80 m/circuito", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "039": {"en": {"f": "Riego Goteo = f(area_m2, separacion_goteros_cm, separacion_lineas_m)", "ei": "200 m²; 30 cm; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Riego Goteo = f(area_m2, separacion_goteros_cm, separacion_lineas_m)", "ei": "200 m²; 30 cm; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Riego Goteo = f(area_m2, separacion_goteros_cm, separacion_lineas_m)", "ei": "200 m²; 30 cm; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Riego Goteo = f(area_m2, separacion_goteros_cm, separacion_lineas_m)", "ei": "200 m²; 30 cm; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Riego Goteo = f(area_m2, separacion_goteros_cm, separacion_lineas_m)", "ei": "200 m²; 30 cm; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Riego Goteo = f(area_m2, separacion_goteros_cm, separacion_lineas_m)", "ei": "200 m²; 30 cm; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "040": {"en": {"f": "Acometida Agua = f(caudal_lps, longitud_m)", "ei": "0.5 L/s; 15 m", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Acometida Agua = f(caudal_lps, longitud_m)", "ei": "0.5 L/s; 15 m", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Acometida Agua = f(caudal_lps, longitud_m)", "ei": "0.5 L/s; 15 m", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Acometida Agua = f(caudal_lps, longitud_m)", "ei": "0.5 L/s; 15 m", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Acometida Agua = f(caudal_lps, longitud_m)", "ei": "0.5 L/s; 15 m", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Acometida Agua = f(caudal_lps, longitud_m)", "ei": "0.5 L/s; 15 m", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "041": {"en": {"f": "Depuradora Piscina = f(largo_m, ancho_m, profundidad_media_m, turnos_dia)", "ei": "8 m; 4 m; 1.5 m; 2 turnos/día", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Depuradora Piscina = f(largo_m, ancho_m, profundidad_media_m, turnos_dia)", "ei": "8 m; 4 m; 1.5 m; 2 turnos/día", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Depuradora Piscina = f(largo_m, ancho_m, profundidad_media_m, turnos_dia)", "ei": "8 m; 4 m; 1.5 m; 2 turnos/día", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Depuradora Piscina = f(largo_m, ancho_m, profundidad_media_m, turnos_dia)", "ei": "8 m; 4 m; 1.5 m; 2 turnos/día", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Depuradora Piscina = f(largo_m, ancho_m, profundidad_media_m, turnos_dia)", "ei": "8 m; 4 m; 1.5 m; 2 turnos/día", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Depuradora Piscina = f(largo_m, ancho_m, profundidad_media_m, turnos_dia)", "ei": "8 m; 4 m; 1.5 m; 2 turnos/día", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "042": {"en": {"f": "Sifon Sumidero = f(num_aparatos, longitud_bajante_m, pendiente_pct)", "ei": "5 aparatos; 8 m; 2 %", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Sifon Sumidero = f(num_aparatos, longitud_bajante_m, pendiente_pct)", "ei": "5 aparatos; 8 m; 2 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Sifon Sumidero = f(num_aparatos, longitud_bajante_m, pendiente_pct)", "ei": "5 aparatos; 8 m; 2 %", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Sifon Sumidero = f(num_aparatos, longitud_bajante_m, pendiente_pct)", "ei": "5 aparatos; 8 m; 2 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Sifon Sumidero = f(num_aparatos, longitud_bajante_m, pendiente_pct)", "ei": "5 aparatos; 8 m; 2 %", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Sifon Sumidero = f(num_aparatos, longitud_bajante_m, pendiente_pct)", "ei": "5 aparatos; 8 m; 2 %", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "043": {"en": {"f": "Cable Electrico Seccion = f(corriente_a, longitud_m, tension_v, caida_max_pct)", "ei": "16 A; 20 m; 230; 3 %", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Cable Electrico Seccion = f(corriente_a, longitud_m, tension_v, caida_max_pct)", "ei": "16 A; 20 m; 230; 3 %", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Cable Electrico Seccion = f(corriente_a, longitud_m, tension_v, caida_max_pct)", "ei": "16 A; 20 m; 230; 3 %", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Cable Electrico Seccion = f(corriente_a, longitud_m, tension_v, caida_max_pct)", "ei": "16 A; 20 m; 230; 3 %", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Cable Electrico Seccion = f(corriente_a, longitud_m, tension_v, caida_max_pct)", "ei": "16 A; 20 m; 230; 3 %", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Cable Electrico Seccion = f(corriente_a, longitud_m, tension_v, caida_max_pct)", "ei": "16 A; 20 m; 230; 3 %", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "044": {"en": {"f": "Caida Tension = f(seccion_mm2, longitud_m, corriente_a, tension_v)", "ei": "2.5 mm²; 30 m; 16 A; 230", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Caida Tension = f(seccion_mm2, longitud_m, corriente_a, tension_v)", "ei": "2.5 mm²; 30 m; 16 A; 230", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Caida Tension = f(seccion_mm2, longitud_m, corriente_a, tension_v)", "ei": "2.5 mm²; 30 m; 16 A; 230", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Caida Tension = f(seccion_mm2, longitud_m, corriente_a, tension_v)", "ei": "2.5 mm²; 30 m; 16 A; 230", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Caida Tension = f(seccion_mm2, longitud_m, corriente_a, tension_v)", "ei": "2.5 mm²; 30 m; 16 A; 230", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Caida Tension = f(seccion_mm2, longitud_m, corriente_a, tension_v)", "ei": "2.5 mm²; 30 m; 16 A; 230", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "045": {"en": {"f": "Luminarias Lumenes = f(area_m2, lux_requeridos, eficiencia_luminaria)", "ei": "20 m²; 300 lux; 90 lm/W", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Luminarias Lumenes = f(area_m2, lux_requeridos, eficiencia_luminaria)", "ei": "20 m²; 300 lux; 90 lm/W", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Luminarias Lumenes = f(area_m2, lux_requeridos, eficiencia_luminaria)", "ei": "20 m²; 300 lux; 90 lm/W", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Luminarias Lumenes = f(area_m2, lux_requeridos, eficiencia_luminaria)", "ei": "20 m²; 300 lux; 90 lm/W", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Luminarias Lumenes = f(area_m2, lux_requeridos, eficiencia_luminaria)", "ei": "20 m²; 300 lux; 90 lm/W", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Luminarias Lumenes = f(area_m2, lux_requeridos, eficiencia_luminaria)", "ei": "20 m²; 300 lux; 90 lm/W", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "046": {"en": {"f": "Puntos Luz Habitacion = f(area_m2, uso)", "ei": "15 m²; dormitorio", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Puntos Luz Habitacion = f(area_m2, uso)", "ei": "15 m²; dormitorio", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Puntos Luz Habitacion = f(area_m2, uso)", "ei": "15 m²; dormitorio", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Puntos Luz Habitacion = f(area_m2, uso)", "ei": "15 m²; dormitorio", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Puntos Luz Habitacion = f(area_m2, uso)", "ei": "15 m²; dormitorio", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Puntos Luz Habitacion = f(area_m2, uso)", "ei": "15 m²; dormitorio", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "047": {"en": {"f": "Cuadro Electrico = f(potencia_kw, tension_v, factor_simultaneidad)", "ei": "9.2 kW; 230; 0.7", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Cuadro Electrico = f(potencia_kw, tension_v, factor_simultaneidad)", "ei": "9.2 kW; 230; 0.7", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Cuadro Electrico = f(potencia_kw, tension_v, factor_simultaneidad)", "ei": "9.2 kW; 230; 0.7", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Cuadro Electrico = f(potencia_kw, tension_v, factor_simultaneidad)", "ei": "9.2 kW; 230; 0.7", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Cuadro Electrico = f(potencia_kw, tension_v, factor_simultaneidad)", "ei": "9.2 kW; 230; 0.7", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Cuadro Electrico = f(potencia_kw, tension_v, factor_simultaneidad)", "ei": "9.2 kW; 230; 0.7", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "048": {"en": {"f": "Instalacion Solar = f(consumo_diario_kwh, hsp_dia, potencia_panel_w)", "ei": "15 kWh/día; 4.5 HSP/día; 400 W/panel", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Instalacion Solar = f(consumo_diario_kwh, hsp_dia, potencia_panel_w)", "ei": "15 kWh/día; 4.5 HSP/día; 400 W/panel", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Instalacion Solar = f(consumo_diario_kwh, hsp_dia, potencia_panel_w)", "ei": "15 kWh/día; 4.5 HSP/día; 400 W/panel", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Instalacion Solar = f(consumo_diario_kwh, hsp_dia, potencia_panel_w)", "ei": "15 kWh/día; 4.5 HSP/día; 400 W/panel", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Instalacion Solar = f(consumo_diario_kwh, hsp_dia, potencia_panel_w)", "ei": "15 kWh/día; 4.5 HSP/día; 400 W/panel", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Instalacion Solar = f(consumo_diario_kwh, hsp_dia, potencia_panel_w)", "ei": "15 kWh/día; 4.5 HSP/día; 400 W/panel", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "049": {"en": {"f": "Baterias Autonomia = f(consumo_diario_kwh, dias_autonomia, capacidad_bateria_kwh)", "ei": "10 kWh/día; 1 días; 5 kWh/bat", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Baterias Autonomia = f(consumo_diario_kwh, dias_autonomia, capacidad_bateria_kwh)", "ei": "10 kWh/día; 1 días; 5 kWh/bat", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Baterias Autonomia = f(consumo_diario_kwh, dias_autonomia, capacidad_bateria_kwh)", "ei": "10 kWh/día; 1 días; 5 kWh/bat", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Baterias Autonomia = f(consumo_diario_kwh, dias_autonomia, capacidad_bateria_kwh)", "ei": "10 kWh/día; 1 días; 5 kWh/bat", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Baterias Autonomia = f(consumo_diario_kwh, dias_autonomia, capacidad_bateria_kwh)", "ei": "10 kWh/día; 1 días; 5 kWh/bat", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Baterias Autonomia = f(consumo_diario_kwh, dias_autonomia, capacidad_bateria_kwh)", "ei": "10 kWh/día; 1 días; 5 kWh/bat", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "050": {"en": {"f": "Trifasica Potencia = f(corriente_a, tension_v, fp)", "ei": "63 A; 400 V; 0.9 cos φ", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Trifasica Potencia = f(corriente_a, tension_v, fp)", "ei": "63 A; 400 V; 0.9 cos φ", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Trifasica Potencia = f(corriente_a, tension_v, fp)", "ei": "63 A; 400 V; 0.9 cos φ", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Trifasica Potencia = f(corriente_a, tension_v, fp)", "ei": "63 A; 400 V; 0.9 cos φ", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Trifasica Potencia = f(corriente_a, tension_v, fp)", "ei": "63 A; 400 V; 0.9 cos φ", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Trifasica Potencia = f(corriente_a, tension_v, fp)", "ei": "63 A; 400 V; 0.9 cos φ", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "051": {"en": {"f": "Puesta Tierra = f(resistividad_ohm_m, resistencia_max_ohm, tipo_pica)", "ei": "100 Ω·m; 10 Ω; cobre", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Puesta Tierra = f(resistividad_ohm_m, resistencia_max_ohm, tipo_pica)", "ei": "100 Ω·m; 10 Ω; cobre", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Puesta Tierra = f(resistividad_ohm_m, resistencia_max_ohm, tipo_pica)", "ei": "100 Ω·m; 10 Ω; cobre", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Puesta Tierra = f(resistividad_ohm_m, resistencia_max_ohm, tipo_pica)", "ei": "100 Ω·m; 10 Ω; cobre", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Puesta Tierra = f(resistividad_ohm_m, resistencia_max_ohm, tipo_pica)", "ei": "100 Ω·m; 10 Ω; cobre", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Puesta Tierra = f(resistividad_ohm_m, resistencia_max_ohm, tipo_pica)", "ei": "100 Ω·m; 10 Ω; cobre", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "052": {"en": {"f": "Consumo Electrico Mensual = f(potencia_w, horas_dia, precio_kwh)", "ei": "2000 W; 4 h/día; 0.18 €/kWh", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Consumo Electrico Mensual = f(potencia_w, horas_dia, precio_kwh)", "ei": "2000 W; 4 h/día; 0.18 €/kWh", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Consumo Electrico Mensual = f(potencia_w, horas_dia, precio_kwh)", "ei": "2000 W; 4 h/día; 0.18 €/kWh", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Consumo Electrico Mensual = f(potencia_w, horas_dia, precio_kwh)", "ei": "2000 W; 4 h/día; 0.18 €/kWh", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Consumo Electrico Mensual = f(potencia_w, horas_dia, precio_kwh)", "ei": "2000 W; 4 h/día; 0.18 €/kWh", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Consumo Electrico Mensual = f(potencia_w, horas_dia, precio_kwh)", "ei": "2000 W; 4 h/día; 0.18 €/kWh", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "053": {"en": {"f": "Aire Acondicionado Btu = f(area_m2, altura_m, orientacion, aislamiento)", "ei": "20 m²; 2.7 m; norte; medio", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Aire Acondicionado Btu = f(area_m2, altura_m, orientacion, aislamiento)", "ei": "20 m²; 2.7 m; norte; medio", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Aire Acondicionado Btu = f(area_m2, altura_m, orientacion, aislamiento)", "ei": "20 m²; 2.7 m; norte; medio", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Aire Acondicionado Btu = f(area_m2, altura_m, orientacion, aislamiento)", "ei": "20 m²; 2.7 m; norte; medio", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Aire Acondicionado Btu = f(area_m2, altura_m, orientacion, aislamiento)", "ei": "20 m²; 2.7 m; norte; medio", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Aire Acondicionado Btu = f(area_m2, altura_m, orientacion, aislamiento)", "ei": "20 m²; 2.7 m; norte; medio", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "054": {"en": {"f": "Conductos Aire = f(caudal_m3h, velocidad_ms)", "ei": "500 m³/h; 4 m/s", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Conductos Aire = f(caudal_m3h, velocidad_ms)", "ei": "500 m³/h; 4 m/s", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Conductos Aire = f(caudal_m3h, velocidad_ms)", "ei": "500 m³/h; 4 m/s", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Conductos Aire = f(caudal_m3h, velocidad_ms)", "ei": "500 m³/h; 4 m/s", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Conductos Aire = f(caudal_m3h, velocidad_ms)", "ei": "500 m³/h; 4 m/s", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Conductos Aire = f(caudal_m3h, velocidad_ms)", "ei": "500 m³/h; 4 m/s", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "055": {"en": {"f": "Ventilacion Mecanica = f(area_m2, altura_m, renovaciones_hora)", "ei": "100 m²; 2.7 m; 0.8 ren/h", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Ventilacion Mecanica = f(area_m2, altura_m, renovaciones_hora)", "ei": "100 m²; 2.7 m; 0.8 ren/h", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Ventilacion Mecanica = f(area_m2, altura_m, renovaciones_hora)", "ei": "100 m²; 2.7 m; 0.8 ren/h", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Ventilacion Mecanica = f(area_m2, altura_m, renovaciones_hora)", "ei": "100 m²; 2.7 m; 0.8 ren/h", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Ventilacion Mecanica = f(area_m2, altura_m, renovaciones_hora)", "ei": "100 m²; 2.7 m; 0.8 ren/h", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Ventilacion Mecanica = f(area_m2, altura_m, renovaciones_hora)", "ei": "100 m²; 2.7 m; 0.8 ren/h", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "056": {"en": {"f": "Bomba Calor Aerotermia = f(area_m2, aislamiento, acs_personas)", "ei": "120 m²; medio; 4 personas", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Bomba Calor Aerotermia = f(area_m2, aislamiento, acs_personas)", "ei": "120 m²; medio; 4 personas", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Bomba Calor Aerotermia = f(area_m2, aislamiento, acs_personas)", "ei": "120 m²; medio; 4 personas", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Bomba Calor Aerotermia = f(area_m2, aislamiento, acs_personas)", "ei": "120 m²; medio; 4 personas", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Bomba Calor Aerotermia = f(area_m2, aislamiento, acs_personas)", "ei": "120 m²; medio; 4 personas", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Bomba Calor Aerotermia = f(area_m2, aislamiento, acs_personas)", "ei": "120 m²; medio; 4 personas", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "057": {"en": {"f": "Calculo Cop Eer = f(potencia_util_kw, potencia_elec_kw)", "ei": "3.5 kW útil; 1 kW eléctrico", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Calculo Cop Eer = f(potencia_util_kw, potencia_elec_kw)", "ei": "3.5 kW útil; 1 kW eléctrico", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Calculo Cop Eer = f(potencia_util_kw, potencia_elec_kw)", "ei": "3.5 kW útil; 1 kW eléctrico", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Calculo Cop Eer = f(potencia_util_kw, potencia_elec_kw)", "ei": "3.5 kW útil; 1 kW eléctrico", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Calculo Cop Eer = f(potencia_util_kw, potencia_elec_kw)", "ei": "3.5 kW útil; 1 kW eléctrico", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Calculo Cop Eer = f(potencia_util_kw, potencia_elec_kw)", "ei": "3.5 kW útil; 1 kW eléctrico", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "058": {"en": {"f": "Dimensionado Conducto = f(caudal_m3h, perdida_carga_pa_m)", "ei": "1000 m³/h; 1.5 Pa/m", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Dimensionado Conducto = f(caudal_m3h, perdida_carga_pa_m)", "ei": "1000 m³/h; 1.5 Pa/m", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Dimensionado Conducto = f(caudal_m3h, perdida_carga_pa_m)", "ei": "1000 m³/h; 1.5 Pa/m", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Dimensionado Conducto = f(caudal_m3h, perdida_carga_pa_m)", "ei": "1000 m³/h; 1.5 Pa/m", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Dimensionado Conducto = f(caudal_m3h, perdida_carga_pa_m)", "ei": "1000 m³/h; 1.5 Pa/m", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Dimensionado Conducto = f(caudal_m3h, perdida_carga_pa_m)", "ei": "1000 m³/h; 1.5 Pa/m", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "059": {"en": {"f": "Rejillas Difusores = f(caudal_m3h, velocidad_cara_ms)", "ei": "200 m³/h; 2 m/s", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Rejillas Difusores = f(caudal_m3h, velocidad_cara_ms)", "ei": "200 m³/h; 2 m/s", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Rejillas Difusores = f(caudal_m3h, velocidad_cara_ms)", "ei": "200 m³/h; 2 m/s", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Rejillas Difusores = f(caudal_m3h, velocidad_cara_ms)", "ei": "200 m³/h; 2 m/s", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Rejillas Difusores = f(caudal_m3h, velocidad_cara_ms)", "ei": "200 m³/h; 2 m/s", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Rejillas Difusores = f(caudal_m3h, velocidad_cara_ms)", "ei": "200 m³/h; 2 m/s", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "060": {"en": {"f": "Carga Gas Refrigerante = f(longitud_linea_m, potencia_eq_kw, tipo_gas)", "ei": "5 m; 3.5 kW; R32", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Carga Gas Refrigerante = f(longitud_linea_m, potencia_eq_kw, tipo_gas)", "ei": "5 m; 3.5 kW; R32", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Carga Gas Refrigerante = f(longitud_linea_m, potencia_eq_kw, tipo_gas)", "ei": "5 m; 3.5 kW; R32", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Carga Gas Refrigerante = f(longitud_linea_m, potencia_eq_kw, tipo_gas)", "ei": "5 m; 3.5 kW; R32", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Carga Gas Refrigerante = f(longitud_linea_m, potencia_eq_kw, tipo_gas)", "ei": "5 m; 3.5 kW; R32", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Carga Gas Refrigerante = f(longitud_linea_m, potencia_eq_kw, tipo_gas)", "ei": "5 m; 3.5 kW; R32", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "061": {"en": {"f": "Ventanas Aluminio Pvc = f(num_ventanas, ancho_m, alto_m)", "ei": "6 ud; 1.2 m; 1.2 m", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Ventanas Aluminio Pvc = f(num_ventanas, ancho_m, alto_m)", "ei": "6 ud; 1.2 m; 1.2 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Ventanas Aluminio Pvc = f(num_ventanas, ancho_m, alto_m)", "ei": "6 ud; 1.2 m; 1.2 m", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Ventanas Aluminio Pvc = f(num_ventanas, ancho_m, alto_m)", "ei": "6 ud; 1.2 m; 1.2 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Ventanas Aluminio Pvc = f(num_ventanas, ancho_m, alto_m)", "ei": "6 ud; 1.2 m; 1.2 m", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Ventanas Aluminio Pvc = f(num_ventanas, ancho_m, alto_m)", "ei": "6 ud; 1.2 m; 1.2 m", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "062": {"en": {"f": "Puertas Paso = f(num_puertas, ancho_m, alto_m)", "ei": "8 ud; 0.82 m; 2.03 m", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Puertas Paso = f(num_puertas, ancho_m, alto_m)", "ei": "8 ud; 0.82 m; 2.03 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Puertas Paso = f(num_puertas, ancho_m, alto_m)", "ei": "8 ud; 0.82 m; 2.03 m", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Puertas Paso = f(num_puertas, ancho_m, alto_m)", "ei": "8 ud; 0.82 m; 2.03 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Puertas Paso = f(num_puertas, ancho_m, alto_m)", "ei": "8 ud; 0.82 m; 2.03 m", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Puertas Paso = f(num_puertas, ancho_m, alto_m)", "ei": "8 ud; 0.82 m; 2.03 m", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "063": {"en": {"f": "Puertas Correderas = f(num_puertas, ancho_hoja_m, alto_m)", "ei": "3 ud; 0.9 m; 2.1 m", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Puertas Correderas = f(num_puertas, ancho_hoja_m, alto_m)", "ei": "3 ud; 0.9 m; 2.1 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Puertas Correderas = f(num_puertas, ancho_hoja_m, alto_m)", "ei": "3 ud; 0.9 m; 2.1 m", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Puertas Correderas = f(num_puertas, ancho_hoja_m, alto_m)", "ei": "3 ud; 0.9 m; 2.1 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Puertas Correderas = f(num_puertas, ancho_hoja_m, alto_m)", "ei": "3 ud; 0.9 m; 2.1 m", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Puertas Correderas = f(num_puertas, ancho_hoja_m, alto_m)", "ei": "3 ud; 0.9 m; 2.1 m", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "064": {"en": {"f": "Escalera Madera = f(altura_total_m, ancho_m, contrahuella_cm)", "ei": "2.8 m; 0.9 m; 18 cm", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Escalera Madera = f(altura_total_m, ancho_m, contrahuella_cm)", "ei": "2.8 m; 0.9 m; 18 cm", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Escalera Madera = f(altura_total_m, ancho_m, contrahuella_cm)", "ei": "2.8 m; 0.9 m; 18 cm", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Escalera Madera = f(altura_total_m, ancho_m, contrahuella_cm)", "ei": "2.8 m; 0.9 m; 18 cm", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Escalera Madera = f(altura_total_m, ancho_m, contrahuella_cm)", "ei": "2.8 m; 0.9 m; 18 cm", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Escalera Madera = f(altura_total_m, ancho_m, contrahuella_cm)", "ei": "2.8 m; 0.9 m; 18 cm", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "065": {"en": {"f": "Barandilla Metalica = f(longitud_m, altura_m, separacion_montantes_m)", "ei": "15 m; 1 m; 1 m", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Barandilla Metalica = f(longitud_m, altura_m, separacion_montantes_m)", "ei": "15 m; 1 m; 1 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Barandilla Metalica = f(longitud_m, altura_m, separacion_montantes_m)", "ei": "15 m; 1 m; 1 m", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Barandilla Metalica = f(longitud_m, altura_m, separacion_montantes_m)", "ei": "15 m; 1 m; 1 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Barandilla Metalica = f(longitud_m, altura_m, separacion_montantes_m)", "ei": "15 m; 1 m; 1 m", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Barandilla Metalica = f(longitud_m, altura_m, separacion_montantes_m)", "ei": "15 m; 1 m; 1 m", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "066": {"en": {"f": "Estructuras Metalicas = f(luz_m, carga_kn_m2, longitud_nave_m)", "ei": "6 m; 5 kN/m²; 20 m", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Estructuras Metalicas = f(luz_m, carga_kn_m2, longitud_nave_m)", "ei": "6 m; 5 kN/m²; 20 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Estructuras Metalicas = f(luz_m, carga_kn_m2, longitud_nave_m)", "ei": "6 m; 5 kN/m²; 20 m", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Estructuras Metalicas = f(luz_m, carga_kn_m2, longitud_nave_m)", "ei": "6 m; 5 kN/m²; 20 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Estructuras Metalicas = f(luz_m, carga_kn_m2, longitud_nave_m)", "ei": "6 m; 5 kN/m²; 20 m", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Estructuras Metalicas = f(luz_m, carga_kn_m2, longitud_nave_m)", "ei": "6 m; 5 kN/m²; 20 m", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "067": {"en": {"f": "Cerrajeria Puerta = f(ancho_m, alto_m)", "ei": "1.5 m; 2 m", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Cerrajeria Puerta = f(ancho_m, alto_m)", "ei": "1.5 m; 2 m", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Cerrajeria Puerta = f(ancho_m, alto_m)", "ei": "1.5 m; 2 m", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Cerrajeria Puerta = f(ancho_m, alto_m)", "ei": "1.5 m; 2 m", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Cerrajeria Puerta = f(ancho_m, alto_m)", "ei": "1.5 m; 2 m", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Cerrajeria Puerta = f(ancho_m, alto_m)", "ei": "1.5 m; 2 m", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "068": {"en": {"f": "Vidrio Cristal = f(m2_total, tipo_vidrio, merma_pct)", "ei": "10 m²; doble_4_16_4; 10 %", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Vidrio Cristal = f(m2_total, tipo_vidrio, merma_pct)", "ei": "10 m²; doble_4_16_4; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Vidrio Cristal = f(m2_total, tipo_vidrio, merma_pct)", "ei": "10 m²; doble_4_16_4; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Vidrio Cristal = f(m2_total, tipo_vidrio, merma_pct)", "ei": "10 m²; doble_4_16_4; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Vidrio Cristal = f(m2_total, tipo_vidrio, merma_pct)", "ei": "10 m²; doble_4_16_4; 10 %", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Vidrio Cristal = f(m2_total, tipo_vidrio, merma_pct)", "ei": "10 m²; doble_4_16_4; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "069": {"en": {"f": "Pintura Plastica Paredes = f(area_m2, manos, rendimiento_m2_l)", "ei": "60 m²; 2 manos; 10 m²/L", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Pintura Plastica Paredes = f(area_m2, manos, rendimiento_m2_l)", "ei": "60 m²; 2 manos; 10 m²/L", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Pintura Plastica Paredes = f(area_m2, manos, rendimiento_m2_l)", "ei": "60 m²; 2 manos; 10 m²/L", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Pintura Plastica Paredes = f(area_m2, manos, rendimiento_m2_l)", "ei": "60 m²; 2 manos; 10 m²/L", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Pintura Plastica Paredes = f(area_m2, manos, rendimiento_m2_l)", "ei": "60 m²; 2 manos; 10 m²/L", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Pintura Plastica Paredes = f(area_m2, manos, rendimiento_m2_l)", "ei": "60 m²; 2 manos; 10 m²/L", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "070": {"en": {"f": "Pintura Techo = f(area_m2, manos, color)", "ei": "40 m²; 2 manos; blanco", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Pintura Techo = f(area_m2, manos, color)", "ei": "40 m²; 2 manos; blanco", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Pintura Techo = f(area_m2, manos, color)", "ei": "40 m²; 2 manos; blanco", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Pintura Techo = f(area_m2, manos, color)", "ei": "40 m²; 2 manos; blanco", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Pintura Techo = f(area_m2, manos, color)", "ei": "40 m²; 2 manos; blanco", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Pintura Techo = f(area_m2, manos, color)", "ei": "40 m²; 2 manos; blanco", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "071": {"en": {"f": "Esmalte Sintetico = f(area_m2, manos, rendimiento_m2_l)", "ei": "20 m²; 2 manos; 12 m²/L", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Esmalte Sintetico = f(area_m2, manos, rendimiento_m2_l)", "ei": "20 m²; 2 manos; 12 m²/L", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Esmalte Sintetico = f(area_m2, manos, rendimiento_m2_l)", "ei": "20 m²; 2 manos; 12 m²/L", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Esmalte Sintetico = f(area_m2, manos, rendimiento_m2_l)", "ei": "20 m²; 2 manos; 12 m²/L", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Esmalte Sintetico = f(area_m2, manos, rendimiento_m2_l)", "ei": "20 m²; 2 manos; 12 m²/L", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Esmalte Sintetico = f(area_m2, manos, rendimiento_m2_l)", "ei": "20 m²; 2 manos; 12 m²/L", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "072": {"en": {"f": "Barniz Exterior = f(area_m2, manos)", "ei": "15 m²; 3 manos", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Barniz Exterior = f(area_m2, manos)", "ei": "15 m²; 3 manos", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Barniz Exterior = f(area_m2, manos)", "ei": "15 m²; 3 manos", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Barniz Exterior = f(area_m2, manos)", "ei": "15 m²; 3 manos", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Barniz Exterior = f(area_m2, manos)", "ei": "15 m²; 3 manos", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Barniz Exterior = f(area_m2, manos)", "ei": "15 m²; 3 manos", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "073": {"en": {"f": "Papel Pintado = f(longitud_pared_m, altura_m, ancho_rollo_m, longitud_rollo_m)", "ei": "12 m; 2.6 m; 0.53 m; 10 m", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Papel Pintado = f(longitud_pared_m, altura_m, ancho_rollo_m, longitud_rollo_m)", "ei": "12 m; 2.6 m; 0.53 m; 10 m", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Papel Pintado = f(longitud_pared_m, altura_m, ancho_rollo_m, longitud_rollo_m)", "ei": "12 m; 2.6 m; 0.53 m; 10 m", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Papel Pintado = f(longitud_pared_m, altura_m, ancho_rollo_m, longitud_rollo_m)", "ei": "12 m; 2.6 m; 0.53 m; 10 m", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Papel Pintado = f(longitud_pared_m, altura_m, ancho_rollo_m, longitud_rollo_m)", "ei": "12 m; 2.6 m; 0.53 m; 10 m", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Papel Pintado = f(longitud_pared_m, altura_m, ancho_rollo_m, longitud_rollo_m)", "ei": "12 m; 2.6 m; 0.53 m; 10 m", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "074": {"en": {"f": "Acabado Texturado = f(area_m2, tipo_textura)", "ei": "80 m²; proyectado", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Acabado Texturado = f(area_m2, tipo_textura)", "ei": "80 m²; proyectado", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Acabado Texturado = f(area_m2, tipo_textura)", "ei": "80 m²; proyectado", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Acabado Texturado = f(area_m2, tipo_textura)", "ei": "80 m²; proyectado", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Acabado Texturado = f(area_m2, tipo_textura)", "ei": "80 m²; proyectado", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Acabado Texturado = f(area_m2, tipo_textura)", "ei": "80 m²; proyectado", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "075": {"en": {"f": "Imprimacion Sellador = f(area_m2, tipo_soporte)", "ei": "80 m²; normal", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Imprimacion Sellador = f(area_m2, tipo_soporte)", "ei": "80 m²; normal", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Imprimacion Sellador = f(area_m2, tipo_soporte)", "ei": "80 m²; normal", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Imprimacion Sellador = f(area_m2, tipo_soporte)", "ei": "80 m²; normal", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Imprimacion Sellador = f(area_m2, tipo_soporte)", "ei": "80 m²; normal", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Imprimacion Sellador = f(area_m2, tipo_soporte)", "ei": "80 m²; normal", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "076": {"en": {"f": "Masilla Filler = f(area_m2, pasadas, espesor_mm)", "ei": "50 m²; 2 pasadas; 1 mm", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Masilla Filler = f(area_m2, pasadas, espesor_mm)", "ei": "50 m²; 2 pasadas; 1 mm", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Masilla Filler = f(area_m2, pasadas, espesor_mm)", "ei": "50 m²; 2 pasadas; 1 mm", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Masilla Filler = f(area_m2, pasadas, espesor_mm)", "ei": "50 m²; 2 pasadas; 1 mm", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Masilla Filler = f(area_m2, pasadas, espesor_mm)", "ei": "50 m²; 2 pasadas; 1 mm", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Masilla Filler = f(area_m2, pasadas, espesor_mm)", "ei": "50 m²; 2 pasadas; 1 mm", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "077": {"en": {"f": "Lija Abrasivo = f(area_m2, num_granos)", "ei": "20 m²; 2 granos", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Lija Abrasivo = f(area_m2, num_granos)", "ei": "20 m²; 2 granos", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Lija Abrasivo = f(area_m2, num_granos)", "ei": "20 m²; 2 granos", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Lija Abrasivo = f(area_m2, num_granos)", "ei": "20 m²; 2 granos", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Lija Abrasivo = f(area_m2, num_granos)", "ei": "20 m²; 2 granos", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Lija Abrasivo = f(area_m2, num_granos)", "ei": "20 m²; 2 granos", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "078": {"en": {"f": "Presupuesto Reforma = f(area_m2, tipo_reforma, zona_geografica)", "ei": "100 m²; media; media", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Presupuesto Reforma = f(area_m2, tipo_reforma, zona_geografica)", "ei": "100 m²; media; media", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Presupuesto Reforma = f(area_m2, tipo_reforma, zona_geografica)", "ei": "100 m²; media; media", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Presupuesto Reforma = f(area_m2, tipo_reforma, zona_geografica)", "ei": "100 m²; media; media", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Presupuesto Reforma = f(area_m2, tipo_reforma, zona_geografica)", "ei": "100 m²; media; media", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Presupuesto Reforma = f(area_m2, tipo_reforma, zona_geografica)", "ei": "100 m²; media; media", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "079": {"en": {"f": "Precio Hora Trabajo = f(costes_fijos_mes, costes_variables_mes, horas_facturables_mes, beneficio_deseado_pct)", "ei": "2000 €/mes; 800 €/mes; 150 h/mes; 20 %", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Precio Hora Trabajo = f(costes_fijos_mes, costes_variables_mes, horas_facturables_mes, beneficio_deseado_pct)", "ei": "2000 €/mes; 800 €/mes; 150 h/mes; 20 %", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Precio Hora Trabajo = f(costes_fijos_mes, costes_variables_mes, horas_facturables_mes, beneficio_deseado_pct)", "ei": "2000 €/mes; 800 €/mes; 150 h/mes; 20 %", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Precio Hora Trabajo = f(costes_fijos_mes, costes_variables_mes, horas_facturables_mes, beneficio_deseado_pct)", "ei": "2000 €/mes; 800 €/mes; 150 h/mes; 20 %", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Precio Hora Trabajo = f(costes_fijos_mes, costes_variables_mes, horas_facturables_mes, beneficio_deseado_pct)", "ei": "2000 €/mes; 800 €/mes; 150 h/mes; 20 %", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Precio Hora Trabajo = f(costes_fijos_mes, costes_variables_mes, horas_facturables_mes, beneficio_deseado_pct)", "ei": "2000 €/mes; 800 €/mes; 150 h/mes; 20 %", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "080": {"en": {"f": "Amortizacion Maquinaria = f(coste_eur, anos_vida_util, valor_residual_pct)", "ei": "15000 €; 5 años; 10 %", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Amortizacion Maquinaria = f(coste_eur, anos_vida_util, valor_residual_pct)", "ei": "15000 €; 5 años; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Amortizacion Maquinaria = f(coste_eur, anos_vida_util, valor_residual_pct)", "ei": "15000 €; 5 años; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Amortizacion Maquinaria = f(coste_eur, anos_vida_util, valor_residual_pct)", "ei": "15000 €; 5 años; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Amortizacion Maquinaria = f(coste_eur, anos_vida_util, valor_residual_pct)", "ei": "15000 €; 5 años; 10 %", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Amortizacion Maquinaria = f(coste_eur, anos_vida_util, valor_residual_pct)", "ei": "15000 €; 5 años; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "081": {"en": {"f": "Amortizacion Vehiculo = f(coste_eur, anos_vida_util, km_anuales)", "ei": "25000 €; 7 años; 30000 km/año", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Amortizacion Vehiculo = f(coste_eur, anos_vida_util, km_anuales)", "ei": "25000 €; 7 años; 30000 km/año", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Amortizacion Vehiculo = f(coste_eur, anos_vida_util, km_anuales)", "ei": "25000 €; 7 años; 30000 km/año", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Amortizacion Vehiculo = f(coste_eur, anos_vida_util, km_anuales)", "ei": "25000 €; 7 años; 30000 km/año", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Amortizacion Vehiculo = f(coste_eur, anos_vida_util, km_anuales)", "ei": "25000 €; 7 años; 30000 km/año", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Amortizacion Vehiculo = f(coste_eur, anos_vida_util, km_anuales)", "ei": "25000 €; 7 años; 30000 km/año", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "082": {"en": {"f": "Coste Combustible = f(km_viaje, consumo_l100km, precio_l)", "ei": "150 km; 8 L/100km; 1.55 €/L", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Coste Combustible = f(km_viaje, consumo_l100km, precio_l)", "ei": "150 km; 8 L/100km; 1.55 €/L", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Coste Combustible = f(km_viaje, consumo_l100km, precio_l)", "ei": "150 km; 8 L/100km; 1.55 €/L", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Coste Combustible = f(km_viaje, consumo_l100km, precio_l)", "ei": "150 km; 8 L/100km; 1.55 €/L", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Coste Combustible = f(km_viaje, consumo_l100km, precio_l)", "ei": "150 km; 8 L/100km; 1.55 €/L", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Coste Combustible = f(km_viaje, consumo_l100km, precio_l)", "ei": "150 km; 8 L/100km; 1.55 €/L", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "083": {"en": {"f": "Dietas Desplazamiento = f(dias_obra, tipo_dieta, km_diarios)", "ei": "20 días; media_dieta; 80 km/día", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Dietas Desplazamiento = f(dias_obra, tipo_dieta, km_diarios)", "ei": "20 días; media_dieta; 80 km/día", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Dietas Desplazamiento = f(dias_obra, tipo_dieta, km_diarios)", "ei": "20 días; media_dieta; 80 km/día", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Dietas Desplazamiento = f(dias_obra, tipo_dieta, km_diarios)", "ei": "20 días; media_dieta; 80 km/día", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Dietas Desplazamiento = f(dias_obra, tipo_dieta, km_diarios)", "ei": "20 días; media_dieta; 80 km/día", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Dietas Desplazamiento = f(dias_obra, tipo_dieta, km_diarios)", "ei": "20 días; media_dieta; 80 km/día", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "084": {"en": {"f": "Alquiler Contenedor = f(m3_escombros, dias_alquiler, precio_dia_eur)", "ei": "8 m³; 7 días; 6 €/día", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Alquiler Contenedor = f(m3_escombros, dias_alquiler, precio_dia_eur)", "ei": "8 m³; 7 días; 6 €/día", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Alquiler Contenedor = f(m3_escombros, dias_alquiler, precio_dia_eur)", "ei": "8 m³; 7 días; 6 €/día", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Alquiler Contenedor = f(m3_escombros, dias_alquiler, precio_dia_eur)", "ei": "8 m³; 7 días; 6 €/día", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Alquiler Contenedor = f(m3_escombros, dias_alquiler, precio_dia_eur)", "ei": "8 m³; 7 días; 6 €/día", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Alquiler Contenedor = f(m3_escombros, dias_alquiler, precio_dia_eur)", "ei": "8 m³; 7 días; 6 €/día", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "085": {"en": {"f": "Alquiler Andamio = f(longitud_m, altura_m, semanas, precio_m2_semana)", "ei": "12 m; 6 m; 4 semanas; 1.5 €/m²·sem", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Alquiler Andamio = f(longitud_m, altura_m, semanas, precio_m2_semana)", "ei": "12 m; 6 m; 4 semanas; 1.5 €/m²·sem", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Alquiler Andamio = f(longitud_m, altura_m, semanas, precio_m2_semana)", "ei": "12 m; 6 m; 4 semanas; 1.5 €/m²·sem", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Alquiler Andamio = f(longitud_m, altura_m, semanas, precio_m2_semana)", "ei": "12 m; 6 m; 4 semanas; 1.5 €/m²·sem", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Alquiler Andamio = f(longitud_m, altura_m, semanas, precio_m2_semana)", "ei": "12 m; 6 m; 4 semanas; 1.5 €/m²·sem", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Alquiler Andamio = f(longitud_m, altura_m, semanas, precio_m2_semana)", "ei": "12 m; 6 m; 4 semanas; 1.5 €/m²·sem", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "086": {"en": {"f": "Limpieza Obra = f(area_m2, tipo_limpieza, precio_m2)", "ei": "100 m²; final_obra; 6 €/m²", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Limpieza Obra = f(area_m2, tipo_limpieza, precio_m2)", "ei": "100 m²; final_obra; 6 €/m²", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Limpieza Obra = f(area_m2, tipo_limpieza, precio_m2)", "ei": "100 m²; final_obra; 6 €/m²", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Limpieza Obra = f(area_m2, tipo_limpieza, precio_m2)", "ei": "100 m²; final_obra; 6 €/m²", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Limpieza Obra = f(area_m2, tipo_limpieza, precio_m2)", "ei": "100 m²; final_obra; 6 €/m²", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Limpieza Obra = f(area_m2, tipo_limpieza, precio_m2)", "ei": "100 m²; final_obra; 6 €/m²", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "087": {"en": {"f": "Seguro Responsabilidad = f(facturacion_anual_eur, tipo_actividad, capital_asegurado_eur)", "ei": "150000 €/año; reforma; 300000 €", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Seguro Responsabilidad = f(facturacion_anual_eur, tipo_actividad, capital_asegurado_eur)", "ei": "150000 €/año; reforma; 300000 €", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Seguro Responsabilidad = f(facturacion_anual_eur, tipo_actividad, capital_asegurado_eur)", "ei": "150000 €/año; reforma; 300000 €", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Seguro Responsabilidad = f(facturacion_anual_eur, tipo_actividad, capital_asegurado_eur)", "ei": "150000 €/año; reforma; 300000 €", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Seguro Responsabilidad = f(facturacion_anual_eur, tipo_actividad, capital_asegurado_eur)", "ei": "150000 €/año; reforma; 300000 €", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Seguro Responsabilidad = f(facturacion_anual_eur, tipo_actividad, capital_asegurado_eur)", "ei": "150000 €/año; reforma; 300000 €", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "088": {"en": {"f": "Epi Equipos Proteccion = f(num_trabajadores, meses_obra, tipo_obra)", "ei": "5 trabajadores; 6 meses; reforma", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Epi Equipos Proteccion = f(num_trabajadores, meses_obra, tipo_obra)", "ei": "5 trabajadores; 6 meses; reforma", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Epi Equipos Proteccion = f(num_trabajadores, meses_obra, tipo_obra)", "ei": "5 trabajadores; 6 meses; reforma", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Epi Equipos Proteccion = f(num_trabajadores, meses_obra, tipo_obra)", "ei": "5 trabajadores; 6 meses; reforma", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Epi Equipos Proteccion = f(num_trabajadores, meses_obra, tipo_obra)", "ei": "5 trabajadores; 6 meses; reforma", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Epi Equipos Proteccion = f(num_trabajadores, meses_obra, tipo_obra)", "ei": "5 trabajadores; 6 meses; reforma", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "089": {"en": {"f": "Senalizacion Obra = f(perimetro_m, altura_riesgo)", "ei": "60 m; medio", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Senalizacion Obra = f(perimetro_m, altura_riesgo)", "ei": "60 m; medio", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Senalizacion Obra = f(perimetro_m, altura_riesgo)", "ei": "60 m; medio", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Senalizacion Obra = f(perimetro_m, altura_riesgo)", "ei": "60 m; medio", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Senalizacion Obra = f(perimetro_m, altura_riesgo)", "ei": "60 m; medio", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Senalizacion Obra = f(perimetro_m, altura_riesgo)", "ei": "60 m; medio", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "090": {"en": {"f": "Rendimiento Diario = f(operarios, horas_dia, rendimiento_m2_h)", "ei": "2 operarios; 8 h/día; 5 m²/h/op", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Rendimiento Diario = f(operarios, horas_dia, rendimiento_m2_h)", "ei": "2 operarios; 8 h/día; 5 m²/h/op", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Rendimiento Diario = f(operarios, horas_dia, rendimiento_m2_h)", "ei": "2 operarios; 8 h/día; 5 m²/h/op", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Rendimiento Diario = f(operarios, horas_dia, rendimiento_m2_h)", "ei": "2 operarios; 8 h/día; 5 m²/h/op", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Rendimiento Diario = f(operarios, horas_dia, rendimiento_m2_h)", "ei": "2 operarios; 8 h/día; 5 m²/h/op", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Rendimiento Diario = f(operarios, horas_dia, rendimiento_m2_h)", "ei": "2 operarios; 8 h/día; 5 m²/h/op", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "091": {"en": {"f": "Planificacion Gantt = f(num_tareas, duracion_media_dias, paralelismo_pct)", "ei": "8 tareas; 5 días/tarea; 30 %", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Planificacion Gantt = f(num_tareas, duracion_media_dias, paralelismo_pct)", "ei": "8 tareas; 5 días/tarea; 30 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Planificacion Gantt = f(num_tareas, duracion_media_dias, paralelismo_pct)", "ei": "8 tareas; 5 días/tarea; 30 %", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Planificacion Gantt = f(num_tareas, duracion_media_dias, paralelismo_pct)", "ei": "8 tareas; 5 días/tarea; 30 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Planificacion Gantt = f(num_tareas, duracion_media_dias, paralelismo_pct)", "ei": "8 tareas; 5 días/tarea; 30 %", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Planificacion Gantt = f(num_tareas, duracion_media_dias, paralelismo_pct)", "ei": "8 tareas; 5 días/tarea; 30 %", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "092": {"en": {"f": "Licencias Municipales = f(presupuesto_obra_eur, tipo_licencia, tasa_municipal_pct)", "ei": "50000 €; obra_menor; 2 %", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Licencias Municipales = f(presupuesto_obra_eur, tipo_licencia, tasa_municipal_pct)", "ei": "50000 €; obra_menor; 2 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Licencias Municipales = f(presupuesto_obra_eur, tipo_licencia, tasa_municipal_pct)", "ei": "50000 €; obra_menor; 2 %", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Licencias Municipales = f(presupuesto_obra_eur, tipo_licencia, tasa_municipal_pct)", "ei": "50000 €; obra_menor; 2 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Licencias Municipales = f(presupuesto_obra_eur, tipo_licencia, tasa_municipal_pct)", "ei": "50000 €; obra_menor; 2 %", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Licencias Municipales = f(presupuesto_obra_eur, tipo_licencia, tasa_municipal_pct)", "ei": "50000 €; obra_menor; 2 %", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "093": {"en": {"f": "Iva Irpf = f(base_imponible_eur, tipo_iva_pct, tipo_irpf_pct)", "ei": "5000 €; 21 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Iva Irpf = f(base_imponible_eur, tipo_iva_pct, tipo_irpf_pct)", "ei": "5000 €; 21 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Iva Irpf = f(base_imponible_eur, tipo_iva_pct, tipo_irpf_pct)", "ei": "5000 €; 21 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Iva Irpf = f(base_imponible_eur, tipo_iva_pct, tipo_irpf_pct)", "ei": "5000 €; 21 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Iva Irpf = f(base_imponible_eur, tipo_iva_pct, tipo_irpf_pct)", "ei": "5000 €; 21 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Iva Irpf = f(base_imponible_eur, tipo_iva_pct, tipo_irpf_pct)", "ei": "5000 €; 21 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "094": {"en": {"f": "Prestamo Equipo = f(importe_eur, tae_pct, plazo_meses)", "ei": "20000 €; 6.5 % TAE; 48 meses", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Prestamo Equipo = f(importe_eur, tae_pct, plazo_meses)", "ei": "20000 €; 6.5 % TAE; 48 meses", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Prestamo Equipo = f(importe_eur, tae_pct, plazo_meses)", "ei": "20000 €; 6.5 % TAE; 48 meses", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Prestamo Equipo = f(importe_eur, tae_pct, plazo_meses)", "ei": "20000 €; 6.5 % TAE; 48 meses", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Prestamo Equipo = f(importe_eur, tae_pct, plazo_meses)", "ei": "20000 €; 6.5 % TAE; 48 meses", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Prestamo Equipo = f(importe_eur, tae_pct, plazo_meses)", "ei": "20000 €; 6.5 % TAE; 48 meses", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "095": {"en": {"f": "Margen Beneficio = f(coste_total_eur, precio_venta_eur)", "ei": "8000 €; 10000 €", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Margen Beneficio = f(coste_total_eur, precio_venta_eur)", "ei": "8000 €; 10000 €", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Margen Beneficio = f(coste_total_eur, precio_venta_eur)", "ei": "8000 €; 10000 €", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Margen Beneficio = f(coste_total_eur, precio_venta_eur)", "ei": "8000 €; 10000 €", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Margen Beneficio = f(coste_total_eur, precio_venta_eur)", "ei": "8000 €; 10000 €", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Margen Beneficio = f(coste_total_eur, precio_venta_eur)", "ei": "8000 €; 10000 €", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "096": {"en": {"f": "Punto Equilibrio = f(costes_fijos_eur, precio_venta_ud, coste_variable_ud)", "ei": "5000 €/mes; 800 €/ud; 500 €/ud", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Punto Equilibrio = f(costes_fijos_eur, precio_venta_ud, coste_variable_ud)", "ei": "5000 €/mes; 800 €/ud; 500 €/ud", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Punto Equilibrio = f(costes_fijos_eur, precio_venta_ud, coste_variable_ud)", "ei": "5000 €/mes; 800 €/ud; 500 €/ud", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Punto Equilibrio = f(costes_fijos_eur, precio_venta_ud, coste_variable_ud)", "ei": "5000 €/mes; 800 €/ud; 500 €/ud", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Punto Equilibrio = f(costes_fijos_eur, precio_venta_ud, coste_variable_ud)", "ei": "5000 €/mes; 800 €/ud; 500 €/ud", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Punto Equilibrio = f(costes_fijos_eur, precio_venta_ud, coste_variable_ud)", "ei": "5000 €/mes; 800 €/ud; 500 €/ud", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "097": {"en": {"f": "Consumo Agua Obra = f(operarios, dias_obra, tipo_obra)", "ei": "8 operarios; 60 días; reforma", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Consumo Agua Obra = f(operarios, dias_obra, tipo_obra)", "ei": "8 operarios; 60 días; reforma", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Consumo Agua Obra = f(operarios, dias_obra, tipo_obra)", "ei": "8 operarios; 60 días; reforma", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Consumo Agua Obra = f(operarios, dias_obra, tipo_obra)", "ei": "8 operarios; 60 días; reforma", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Consumo Agua Obra = f(operarios, dias_obra, tipo_obra)", "ei": "8 operarios; 60 días; reforma", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Consumo Agua Obra = f(operarios, dias_obra, tipo_obra)", "ei": "8 operarios; 60 días; reforma", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "098": {"en": {"f": "Factor Merma Material = f(cantidad_neta, factor_merma_pct, precio_ud)", "ei": "100 (unidades); 10 %; 25 €/ud", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Factor Merma Material = f(cantidad_neta, factor_merma_pct, precio_ud)", "ei": "100 (unidades); 10 %; 25 €/ud", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Factor Merma Material = f(cantidad_neta, factor_merma_pct, precio_ud)", "ei": "100 (unidades); 10 %; 25 €/ud", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Factor Merma Material = f(cantidad_neta, factor_merma_pct, precio_ud)", "ei": "100 (unidades); 10 %; 25 €/ud", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Factor Merma Material = f(cantidad_neta, factor_merma_pct, precio_ud)", "ei": "100 (unidades); 10 %; 25 €/ud", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Factor Merma Material = f(cantidad_neta, factor_merma_pct, precio_ud)", "ei": "100 (unidades); 10 %; 25 €/ud", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "099": {"en": {"f": "Coste Mano Obra = f(operarios, horas_jornada, dias_obra, coste_hora_eur)", "ei": "3 operarios; 8 h/día; 15 días; 25 €/h", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Coste Mano Obra = f(operarios, horas_jornada, dias_obra, coste_hora_eur)", "ei": "3 operarios; 8 h/día; 15 días; 25 €/h", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Coste Mano Obra = f(operarios, horas_jornada, dias_obra, coste_hora_eur)", "ei": "3 operarios; 8 h/día; 15 días; 25 €/h", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Coste Mano Obra = f(operarios, horas_jornada, dias_obra, coste_hora_eur)", "ei": "3 operarios; 8 h/día; 15 días; 25 €/h", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Coste Mano Obra = f(operarios, horas_jornada, dias_obra, coste_hora_eur)", "ei": "3 operarios; 8 h/día; 15 días; 25 €/h", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Coste Mano Obra = f(operarios, horas_jornada, dias_obra, coste_hora_eur)", "ei": "3 operarios; 8 h/día; 15 días; 25 €/h", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "100": {"en": {"f": "Roi Herramienta = f(coste_herramienta_eur, ahorro_horas_mes, coste_hora_eur, vida_util_anos)", "ei": "1200 €; 8 h/mes; 30 €/h; 5 años", "eo": "Results calculated from 4 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Roi Herramienta = f(coste_herramienta_eur, ahorro_horas_mes, coste_hora_eur, vida_util_anos)", "ei": "1200 €; 8 h/mes; 30 €/h; 5 años", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Roi Herramienta = f(coste_herramienta_eur, ahorro_horas_mes, coste_hora_eur, vida_util_anos)", "ei": "1200 €; 8 h/mes; 30 €/h; 5 años", "eo": "Results calculated from 4 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Roi Herramienta = f(coste_herramienta_eur, ahorro_horas_mes, coste_hora_eur, vida_util_anos)", "ei": "1200 €; 8 h/mes; 30 €/h; 5 años", "eo": "Results calculated from 4 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Roi Herramienta = f(coste_herramienta_eur, ahorro_horas_mes, coste_hora_eur, vida_util_anos)", "ei": "1200 €; 8 h/mes; 30 €/h; 5 años", "eo": "Results calculated from 4 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Roi Herramienta = f(coste_herramienta_eur, ahorro_horas_mes, coste_hora_eur, vida_util_anos)", "ei": "1200 €; 8 h/mes; 30 €/h; 5 años", "eo": "Results calculated from 4 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "101": {"en": {"f": "Volumen Piscina = f(largo_m, ancho_m, profundidad_m)", "ei": "8 m; 4 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Volumen Piscina = f(largo_m, ancho_m, profundidad_m)", "ei": "8 m; 4 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Volumen Piscina = f(largo_m, ancho_m, profundidad_m)", "ei": "8 m; 4 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Volumen Piscina = f(largo_m, ancho_m, profundidad_m)", "ei": "8 m; 4 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Volumen Piscina = f(largo_m, ancho_m, profundidad_m)", "ei": "8 m; 4 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Volumen Piscina = f(largo_m, ancho_m, profundidad_m)", "ei": "8 m; 4 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "102": {"en": {"f": "Tierra Jardin = f(largo_m, ancho_m, profundidad_cm)", "ei": "4 m; 2 m; 20 cm", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tierra Jardin = f(largo_m, ancho_m, profundidad_cm)", "ei": "4 m; 2 m; 20 cm", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tierra Jardin = f(largo_m, ancho_m, profundidad_cm)", "ei": "4 m; 2 m; 20 cm", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tierra Jardin = f(largo_m, ancho_m, profundidad_cm)", "ei": "4 m; 2 m; 20 cm", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tierra Jardin = f(largo_m, ancho_m, profundidad_cm)", "ei": "4 m; 2 m; 20 cm", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tierra Jardin = f(largo_m, ancho_m, profundidad_cm)", "ei": "4 m; 2 m; 20 cm", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "103": {"en": {"f": "Postes Valla = f(longitud_m, separacion_m, altura_m)", "ei": "20 m; 2 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["brick and block wall construction", "masonry material estimation", "wall area and mortar calculations", "construction budgeting"]}, "es": {"f": "Postes Valla = f(longitud_m, separacion_m, altura_m)", "ei": "20 m; 2 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["construcción de muros de ladrillo y bloque", "estimación de materiales de mampostería", "cálculos de área de muro y mortero", "presupuestos de construcción"]}, "fr": {"f": "Postes Valla = f(longitud_m, separacion_m, altura_m)", "ei": "20 m; 2 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["construction de murs en briques et parpaings", "estimation de matériaux de maçonnerie", "calculs de surface de mur et mortier", "budgets de construction"]}, "pt": {"f": "Postes Valla = f(longitud_m, separacion_m, altura_m)", "ei": "20 m; 2 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["construção de paredes de tijolo e bloco", "estimativa de materiais de alvenaria", "cálculos de área de parede e argamassa", "orçamentos de construção"]}, "de": {"f": "Postes Valla = f(longitud_m, separacion_m, altura_m)", "ei": "20 m; 2 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["Ziegel- und Blockmauerwerk", "Maurerarbeiten-Materialschätzung", "Wandfläche- und Mörtelberechnungen", "Baubudgetplanung"]}, "it": {"f": "Postes Valla = f(longitud_m, separacion_m, altura_m)", "ei": "20 m; 2 m; 1.5 m", "eo": "Results calculated from 3 inputs", "u": ["costruzione di muri in mattoni e blocchi", "stima di materiali da muratura", "calcoli di area murale e malta", "budget di costruzione"]}},
    "110": {"en": {"f": "Valor Absoluto = f(x)", "ei": "-5", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Valor Absoluto = f(x)", "ei": "-5", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Valor Absoluto = f(x)", "ei": "-5", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Valor Absoluto = f(x)", "ei": "-5", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Valor Absoluto = f(x)", "ei": "-5", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Valor Absoluto = f(x)", "ei": "-5", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "111": {"en": {"f": "Suma Progresion Aritmetica = f(a1, d, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Suma Progresion Aritmetica = f(a1, d, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Suma Progresion Aritmetica = f(a1, d, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Suma Progresion Aritmetica = f(a1, d, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Suma Progresion Aritmetica = f(a1, d, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Suma Progresion Aritmetica = f(a1, d, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "112": {"en": {"f": "Suma Progresion Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Suma Progresion Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Suma Progresion Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Suma Progresion Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Suma Progresion Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Suma Progresion Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "113": {"en": {"f": "Modulo Complejo = f(real, imag)", "ei": "3; 4", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Modulo Complejo = f(real, imag)", "ei": "3; 4", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Modulo Complejo = f(real, imag)", "ei": "3; 4", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Modulo Complejo = f(real, imag)", "ei": "3; 4", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Modulo Complejo = f(real, imag)", "ei": "3; 4", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Modulo Complejo = f(real, imag)", "ei": "3; 4", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "114": {"en": {"f": "Determinante Matriz 2X2 = f(a, b, c, d)", "ei": "1; 2; 3; 4", "eo": "Results calculated from 4 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Determinante Matriz 2X2 = f(a, b, c, d)", "ei": "1; 2; 3; 4", "eo": "Results calculated from 4 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Determinante Matriz 2X2 = f(a, b, c, d)", "ei": "1; 2; 3; 4", "eo": "Results calculated from 4 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Determinante Matriz 2X2 = f(a, b, c, d)", "ei": "1; 2; 3; 4", "eo": "Results calculated from 4 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Determinante Matriz 2X2 = f(a, b, c, d)", "ei": "1; 2; 3; 4", "eo": "Results calculated from 4 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Determinante Matriz 2X2 = f(a, b, c, d)", "ei": "1; 2; 3; 4", "eo": "Results calculated from 4 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "115": {"en": {"f": "Magnitud Vector 3D = f(vx, vy, vz)", "ei": "1; 2; 2", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Magnitud Vector 3D = f(vx, vy, vz)", "ei": "1; 2; 2", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Magnitud Vector 3D = f(vx, vy, vz)", "ei": "1; 2; 2", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Magnitud Vector 3D = f(vx, vy, vz)", "ei": "1; 2; 2", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Magnitud Vector 3D = f(vx, vy, vz)", "ei": "1; 2; 2", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Magnitud Vector 3D = f(vx, vy, vz)", "ei": "1; 2; 2", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "116": {"en": {"f": "Producto Escalar = f(ax, ay, az, bx)", "ei": "1; 0; 0; 1", "eo": "Results calculated from 6 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Producto Escalar = f(ax, ay, az, bx)", "ei": "1; 0; 0; 1", "eo": "Results calculated from 6 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Producto Escalar = f(ax, ay, az, bx)", "ei": "1; 0; 0; 1", "eo": "Results calculated from 6 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Producto Escalar = f(ax, ay, az, bx)", "ei": "1; 0; 0; 1", "eo": "Results calculated from 6 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Producto Escalar = f(ax, ay, az, bx)", "ei": "1; 0; 0; 1", "eo": "Results calculated from 6 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Producto Escalar = f(ax, ay, az, bx)", "ei": "1; 0; 0; 1", "eo": "Results calculated from 6 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "117": {"en": {"f": "Producto Vectorial = f(ax, ay, az, bx)", "ei": "1; 0; 0; 0", "eo": "Results calculated from 6 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Producto Vectorial = f(ax, ay, az, bx)", "ei": "1; 0; 0; 0", "eo": "Results calculated from 6 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Producto Vectorial = f(ax, ay, az, bx)", "ei": "1; 0; 0; 0", "eo": "Results calculated from 6 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Producto Vectorial = f(ax, ay, az, bx)", "ei": "1; 0; 0; 0", "eo": "Results calculated from 6 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Producto Vectorial = f(ax, ay, az, bx)", "ei": "1; 0; 0; 0", "eo": "Results calculated from 6 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Producto Vectorial = f(ax, ay, az, bx)", "ei": "1; 0; 0; 0", "eo": "Results calculated from 6 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "118": {"en": {"f": "Derivada Polinomio = f(a, b, c, x_val)", "ei": "2; -3; 5; 2", "eo": "Results calculated from 4 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Derivada Polinomio = f(a, b, c, x_val)", "ei": "2; -3; 5; 2", "eo": "Results calculated from 4 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Derivada Polinomio = f(a, b, c, x_val)", "ei": "2; -3; 5; 2", "eo": "Results calculated from 4 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Derivada Polinomio = f(a, b, c, x_val)", "ei": "2; -3; 5; 2", "eo": "Results calculated from 4 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Derivada Polinomio = f(a, b, c, x_val)", "ei": "2; -3; 5; 2", "eo": "Results calculated from 4 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Derivada Polinomio = f(a, b, c, x_val)", "ei": "2; -3; 5; 2", "eo": "Results calculated from 4 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "119": {"en": {"f": "Regla Trapecios Integral = f(a, b, n, fa)", "ei": "0; 4; 4; 1", "eo": "Results calculated from 5 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Regla Trapecios Integral = f(a, b, n, fa)", "ei": "0; 4; 4; 1", "eo": "Results calculated from 5 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Regla Trapecios Integral = f(a, b, n, fa)", "ei": "0; 4; 4; 1", "eo": "Results calculated from 5 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Regla Trapecios Integral = f(a, b, n, fa)", "ei": "0; 4; 4; 1", "eo": "Results calculated from 5 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Regla Trapecios Integral = f(a, b, n, fa)", "ei": "0; 4; 4; 1", "eo": "Results calculated from 5 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Regla Trapecios Integral = f(a, b, n, fa)", "ei": "0; 4; 4; 1", "eo": "Results calculated from 5 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "120": {"en": {"f": "Movimiento Proyectil = f(v0, angle, h0)", "ei": "20 m/s; 45 deg; 0 m", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Movimiento Proyectil = f(v0, angle, h0)", "ei": "20 m/s; 45 deg; 0 m", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Movimiento Proyectil = f(v0, angle, h0)", "ei": "20 m/s; 45 deg; 0 m", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Movimiento Proyectil = f(v0, angle, h0)", "ei": "20 m/s; 45 deg; 0 m", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Movimiento Proyectil = f(v0, angle, h0)", "ei": "20 m/s; 45 deg; 0 m", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Movimiento Proyectil = f(v0, angle, h0)", "ei": "20 m/s; 45 deg; 0 m", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "121": {"en": {"f": "Fuerza Centripeta = f(m, v, r)", "ei": "2 kg; 10 m/s; 5 m", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Fuerza Centripeta = f(m, v, r)", "ei": "2 kg; 10 m/s; 5 m", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Fuerza Centripeta = f(m, v, r)", "ei": "2 kg; 10 m/s; 5 m", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Fuerza Centripeta = f(m, v, r)", "ei": "2 kg; 10 m/s; 5 m", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Fuerza Centripeta = f(m, v, r)", "ei": "2 kg; 10 m/s; 5 m", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Fuerza Centripeta = f(m, v, r)", "ei": "2 kg; 10 m/s; 5 m", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "122": {"en": {"f": "Fuerza Gravitatoria = f(m1, m2, r)", "ei": "1000 kg; 1000 kg; 1 m", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Fuerza Gravitatoria = f(m1, m2, r)", "ei": "1000 kg; 1000 kg; 1 m", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Fuerza Gravitatoria = f(m1, m2, r)", "ei": "1000 kg; 1000 kg; 1 m", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Fuerza Gravitatoria = f(m1, m2, r)", "ei": "1000 kg; 1000 kg; 1 m", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Fuerza Gravitatoria = f(m1, m2, r)", "ei": "1000 kg; 1000 kg; 1 m", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Fuerza Gravitatoria = f(m1, m2, r)", "ei": "1000 kg; 1000 kg; 1 m", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "123": {"en": {"f": "Energia Potencial Elastica = f(k, x)", "ei": "200 N/m; 0.1 m", "eo": "Results calculated from 2 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Energia Potencial Elastica = f(k, x)", "ei": "200 N/m; 0.1 m", "eo": "Results calculated from 2 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Energia Potencial Elastica = f(k, x)", "ei": "200 N/m; 0.1 m", "eo": "Results calculated from 2 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Energia Potencial Elastica = f(k, x)", "ei": "200 N/m; 0.1 m", "eo": "Results calculated from 2 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Energia Potencial Elastica = f(k, x)", "ei": "200 N/m; 0.1 m", "eo": "Results calculated from 2 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Energia Potencial Elastica = f(k, x)", "ei": "200 N/m; 0.1 m", "eo": "Results calculated from 2 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "124": {"en": {"f": "Calor Especifico = f(m, c, dt)", "ei": "1 kg; 4184 J/(kg·K); 10 K", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Calor Especifico = f(m, c, dt)", "ei": "1 kg; 4184 J/(kg·K); 10 K", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Calor Especifico = f(m, c, dt)", "ei": "1 kg; 4184 J/(kg·K); 10 K", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Calor Especifico = f(m, c, dt)", "ei": "1 kg; 4184 J/(kg·K); 10 K", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Calor Especifico = f(m, c, dt)", "ei": "1 kg; 4184 J/(kg·K); 10 K", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Calor Especifico = f(m, c, dt)", "ei": "1 kg; 4184 J/(kg·K); 10 K", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "125": {"en": {"f": "Velocidad Onda = f(f, wavelength)", "ei": "440 Hz; 0.78 m", "eo": "Results calculated from 2 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Velocidad Onda = f(f, wavelength)", "ei": "440 Hz; 0.78 m", "eo": "Results calculated from 2 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Velocidad Onda = f(f, wavelength)", "ei": "440 Hz; 0.78 m", "eo": "Results calculated from 2 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Velocidad Onda = f(f, wavelength)", "ei": "440 Hz; 0.78 m", "eo": "Results calculated from 2 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Velocidad Onda = f(f, wavelength)", "ei": "440 Hz; 0.78 m", "eo": "Results calculated from 2 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Velocidad Onda = f(f, wavelength)", "ei": "440 Hz; 0.78 m", "eo": "Results calculated from 2 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "126": {"en": {"f": "Ecuacion Lente Delgada = f(focal, obj_dist)", "ei": "0.1 m; 0.3 m", "eo": "Results calculated from 2 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Ecuacion Lente Delgada = f(focal, obj_dist)", "ei": "0.1 m; 0.3 m", "eo": "Results calculated from 2 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Ecuacion Lente Delgada = f(focal, obj_dist)", "ei": "0.1 m; 0.3 m", "eo": "Results calculated from 2 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Ecuacion Lente Delgada = f(focal, obj_dist)", "ei": "0.1 m; 0.3 m", "eo": "Results calculated from 2 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Ecuacion Lente Delgada = f(focal, obj_dist)", "ei": "0.1 m; 0.3 m", "eo": "Results calculated from 2 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Ecuacion Lente Delgada = f(focal, obj_dist)", "ei": "0.1 m; 0.3 m", "eo": "Results calculated from 2 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "127": {"en": {"f": "Torque Momento Fuerza = f(r, f, theta)", "ei": "0.5 m; 100 N; 90 deg", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Torque Momento Fuerza = f(r, f, theta)", "ei": "0.5 m; 100 N; 90 deg", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Torque Momento Fuerza = f(r, f, theta)", "ei": "0.5 m; 100 N; 90 deg", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Torque Momento Fuerza = f(r, f, theta)", "ei": "0.5 m; 100 N; 90 deg", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Torque Momento Fuerza = f(r, f, theta)", "ei": "0.5 m; 100 N; 90 deg", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Torque Momento Fuerza = f(r, f, theta)", "ei": "0.5 m; 100 N; 90 deg", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "128": {"en": {"f": "Momento Angular = f(m, v, r)", "ei": "2 kg; 5 m/s; 1 m", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Momento Angular = f(m, v, r)", "ei": "2 kg; 5 m/s; 1 m", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Momento Angular = f(m, v, r)", "ei": "2 kg; 5 m/s; 1 m", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Momento Angular = f(m, v, r)", "ei": "2 kg; 5 m/s; 1 m", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Momento Angular = f(m, v, r)", "ei": "2 kg; 5 m/s; 1 m", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Momento Angular = f(m, v, r)", "ei": "2 kg; 5 m/s; 1 m", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "129": {"en": {"f": "Presion Fluido = f(rho, g, h)", "ei": "1000 kg/m³; 9.80665 m/s²; 10 m", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Presion Fluido = f(rho, g, h)", "ei": "1000 kg/m³; 9.80665 m/s²; 10 m", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Presion Fluido = f(rho, g, h)", "ei": "1000 kg/m³; 9.80665 m/s²; 10 m", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Presion Fluido = f(rho, g, h)", "ei": "1000 kg/m³; 9.80665 m/s²; 10 m", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Presion Fluido = f(rho, g, h)", "ei": "1000 kg/m³; 9.80665 m/s²; 10 m", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Presion Fluido = f(rho, g, h)", "ei": "1000 kg/m³; 9.80665 m/s²; 10 m", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "130": {"en": {"f": "Logaritmo = f(x, base)", "ei": "100; 10", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Logaritmo = f(x, base)", "ei": "100; 10", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Logaritmo = f(x, base)", "ei": "100; 10", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Logaritmo = f(x, base)", "ei": "100; 10", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Logaritmo = f(x, base)", "ei": "100; 10", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Logaritmo = f(x, base)", "ei": "100; 10", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "131": {"en": {"f": "Logaritmo Natural = f(x)", "ei": "2.718", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Logaritmo Natural = f(x)", "ei": "2.718", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Logaritmo Natural = f(x)", "ei": "2.718", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Logaritmo Natural = f(x)", "ei": "2.718", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Logaritmo Natural = f(x)", "ei": "2.718", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Logaritmo Natural = f(x)", "ei": "2.718", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "132": {"en": {"f": "Crecimiento Exponencial = f(p0, r, t)", "ei": "100; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Crecimiento Exponencial = f(p0, r, t)", "ei": "100; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Crecimiento Exponencial = f(p0, r, t)", "ei": "100; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Crecimiento Exponencial = f(p0, r, t)", "ei": "100; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Crecimiento Exponencial = f(p0, r, t)", "ei": "100; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Crecimiento Exponencial = f(p0, r, t)", "ei": "100; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "133": {"en": {"f": "Factorial = f(n)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Factorial = f(n)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Factorial = f(n)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Factorial = f(n)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Factorial = f(n)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Factorial = f(n)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "134": {"en": {"f": "Permutaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Permutaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Permutaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Permutaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Permutaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Permutaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "135": {"en": {"f": "Combinaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Combinaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Combinaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Combinaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Combinaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Combinaciones = f(n, r)", "ei": "5; 3", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "136": {"en": {"f": "Desviacion Estandar = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Desviacion Estandar = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Desviacion Estandar = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Desviacion Estandar = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Desviacion Estandar = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Desviacion Estandar = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "137": {"en": {"f": "Varianza = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Varianza = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Varianza = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Varianza = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Varianza = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Varianza = f(values)", "ei": "2,4,4,4,5,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "138": {"en": {"f": "Mediana = f(values)", "ei": "1,3,5,7,9", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Mediana = f(values)", "ei": "1,3,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Mediana = f(values)", "ei": "1,3,5,7,9", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Mediana = f(values)", "ei": "1,3,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Mediana = f(values)", "ei": "1,3,5,7,9", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Mediana = f(values)", "ei": "1,3,5,7,9", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "139": {"en": {"f": "Cuartiles = f(values)", "ei": "1,2,3,4,5,6,7,8,9,10", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Cuartiles = f(values)", "ei": "1,2,3,4,5,6,7,8,9,10", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Cuartiles = f(values)", "ei": "1,2,3,4,5,6,7,8,9,10", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Cuartiles = f(values)", "ei": "1,2,3,4,5,6,7,8,9,10", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Cuartiles = f(values)", "ei": "1,2,3,4,5,6,7,8,9,10", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Cuartiles = f(values)", "ei": "1,2,3,4,5,6,7,8,9,10", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "140": {"en": {"f": "Ecuacion Bernoulli = f(p1, v1, h1, p2)", "ei": "100000 Pa; 2 m/s; 0 m; 80000 Pa", "eo": "Results calculated from 5 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Ecuacion Bernoulli = f(p1, v1, h1, p2)", "ei": "100000 Pa; 2 m/s; 0 m; 80000 Pa", "eo": "Results calculated from 5 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Ecuacion Bernoulli = f(p1, v1, h1, p2)", "ei": "100000 Pa; 2 m/s; 0 m; 80000 Pa", "eo": "Results calculated from 5 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Ecuacion Bernoulli = f(p1, v1, h1, p2)", "ei": "100000 Pa; 2 m/s; 0 m; 80000 Pa", "eo": "Results calculated from 5 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Ecuacion Bernoulli = f(p1, v1, h1, p2)", "ei": "100000 Pa; 2 m/s; 0 m; 80000 Pa", "eo": "Results calculated from 5 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Ecuacion Bernoulli = f(p1, v1, h1, p2)", "ei": "100000 Pa; 2 m/s; 0 m; 80000 Pa", "eo": "Results calculated from 5 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "141": {"en": {"f": "Efecto Doppler = f(f0, v_source, v_observer, v_sound)", "ei": "440 Hz; 30 m/s; 0 m/s; 343 m/s", "eo": "Results calculated from 4 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Efecto Doppler = f(f0, v_source, v_observer, v_sound)", "ei": "440 Hz; 30 m/s; 0 m/s; 343 m/s", "eo": "Results calculated from 4 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Efecto Doppler = f(f0, v_source, v_observer, v_sound)", "ei": "440 Hz; 30 m/s; 0 m/s; 343 m/s", "eo": "Results calculated from 4 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Efecto Doppler = f(f0, v_source, v_observer, v_sound)", "ei": "440 Hz; 30 m/s; 0 m/s; 343 m/s", "eo": "Results calculated from 4 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Efecto Doppler = f(f0, v_source, v_observer, v_sound)", "ei": "440 Hz; 30 m/s; 0 m/s; 343 m/s", "eo": "Results calculated from 4 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Efecto Doppler = f(f0, v_source, v_observer, v_sound)", "ei": "440 Hz; 30 m/s; 0 m/s; 343 m/s", "eo": "Results calculated from 4 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "142": {"en": {"f": "Ley Snell = f(n1, theta1, n2)", "ei": "1; 30 deg; 1.5", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Ley Snell = f(n1, theta1, n2)", "ei": "1; 30 deg; 1.5", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Ley Snell = f(n1, theta1, n2)", "ei": "1; 30 deg; 1.5", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Ley Snell = f(n1, theta1, n2)", "ei": "1; 30 deg; 1.5", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Ley Snell = f(n1, theta1, n2)", "ei": "1; 30 deg; 1.5", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Ley Snell = f(n1, theta1, n2)", "ei": "1; 30 deg; 1.5", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "143": {"en": {"f": "Fuerza Coulomb = f(q1, q2, r)", "ei": "1e-06 C; 1e-06 C; 0.1 m", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Fuerza Coulomb = f(q1, q2, r)", "ei": "1e-06 C; 1e-06 C; 0.1 m", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Fuerza Coulomb = f(q1, q2, r)", "ei": "1e-06 C; 1e-06 C; 0.1 m", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Fuerza Coulomb = f(q1, q2, r)", "ei": "1e-06 C; 1e-06 C; 0.1 m", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Fuerza Coulomb = f(q1, q2, r)", "ei": "1e-06 C; 1e-06 C; 0.1 m", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Fuerza Coulomb = f(q1, q2, r)", "ei": "1e-06 C; 1e-06 C; 0.1 m", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "144": {"en": {"f": "Fuerza Magnetica Carga = f(q, v, B, theta)", "ei": "1e-06 C; 1000 m/s; 0.5 T; 90 deg", "eo": "Results calculated from 4 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Fuerza Magnetica Carga = f(q, v, B, theta)", "ei": "1e-06 C; 1000 m/s; 0.5 T; 90 deg", "eo": "Results calculated from 4 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Fuerza Magnetica Carga = f(q, v, B, theta)", "ei": "1e-06 C; 1000 m/s; 0.5 T; 90 deg", "eo": "Results calculated from 4 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Fuerza Magnetica Carga = f(q, v, B, theta)", "ei": "1e-06 C; 1000 m/s; 0.5 T; 90 deg", "eo": "Results calculated from 4 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Fuerza Magnetica Carga = f(q, v, B, theta)", "ei": "1e-06 C; 1000 m/s; 0.5 T; 90 deg", "eo": "Results calculated from 4 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Fuerza Magnetica Carga = f(q, v, B, theta)", "ei": "1e-06 C; 1000 m/s; 0.5 T; 90 deg", "eo": "Results calculated from 4 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "145": {"en": {"f": "Dilatacion Termica = f(L0, alpha, dt)", "ei": "10 m; 1.2e-05 /K; 50 K", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Dilatacion Termica = f(L0, alpha, dt)", "ei": "10 m; 1.2e-05 /K; 50 K", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Dilatacion Termica = f(L0, alpha, dt)", "ei": "10 m; 1.2e-05 /K; 50 K", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Dilatacion Termica = f(L0, alpha, dt)", "ei": "10 m; 1.2e-05 /K; 50 K", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Dilatacion Termica = f(L0, alpha, dt)", "ei": "10 m; 1.2e-05 /K; 50 K", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Dilatacion Termica = f(L0, alpha, dt)", "ei": "10 m; 1.2e-05 /K; 50 K", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "146": {"en": {"f": "Ley Stefan Boltzmann = f(T, area, emissivity)", "ei": "300 K; 1 m²; 1", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Ley Stefan Boltzmann = f(T, area, emissivity)", "ei": "300 K; 1 m²; 1", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Ley Stefan Boltzmann = f(T, area, emissivity)", "ei": "300 K; 1 m²; 1", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Ley Stefan Boltzmann = f(T, area, emissivity)", "ei": "300 K; 1 m²; 1", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Ley Stefan Boltzmann = f(T, area, emissivity)", "ei": "300 K; 1 m²; 1", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Ley Stefan Boltzmann = f(T, area, emissivity)", "ei": "300 K; 1 m²; 1", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "147": {"en": {"f": "Circuito Rl = f(L, R)", "ei": "1 H; 10 ohm", "eo": "Results calculated from 2 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Circuito Rl = f(L, R)", "ei": "1 H; 10 ohm", "eo": "Results calculated from 2 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Circuito Rl = f(L, R)", "ei": "1 H; 10 ohm", "eo": "Results calculated from 2 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Circuito Rl = f(L, R)", "ei": "1 H; 10 ohm", "eo": "Results calculated from 2 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Circuito Rl = f(L, R)", "ei": "1 H; 10 ohm", "eo": "Results calculated from 2 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Circuito Rl = f(L, R)", "ei": "1 H; 10 ohm", "eo": "Results calculated from 2 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "148": {"en": {"f": "Circuito Rc = f(R, C)", "ei": "1000 ohm; 1e-06 F", "eo": "Results calculated from 2 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Circuito Rc = f(R, C)", "ei": "1000 ohm; 1e-06 F", "eo": "Results calculated from 2 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Circuito Rc = f(R, C)", "ei": "1000 ohm; 1e-06 F", "eo": "Results calculated from 2 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Circuito Rc = f(R, C)", "ei": "1000 ohm; 1e-06 F", "eo": "Results calculated from 2 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Circuito Rc = f(R, C)", "ei": "1000 ohm; 1e-06 F", "eo": "Results calculated from 2 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Circuito Rc = f(R, C)", "ei": "1000 ohm; 1e-06 F", "eo": "Results calculated from 2 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "149": {"en": {"f": "Ley Gases Ideales = f(P, V, n, T)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Ley Gases Ideales = f(P, V, n, T)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Ley Gases Ideales = f(P, V, n, T)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Ley Gases Ideales = f(P, V, n, T)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Ley Gases Ideales = f(P, V, n, T)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Ley Gases Ideales = f(P, V, n, T)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "320": {"en": {"f": "Tasa Crecimiento Anual Compuesto = f(begin, end, years)", "ei": "1000 USD; 2000 USD; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Tasa Crecimiento Anual Compuesto = f(begin, end, years)", "ei": "1000 USD; 2000 USD; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Tasa Crecimiento Anual Compuesto = f(begin, end, years)", "ei": "1000 USD; 2000 USD; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Tasa Crecimiento Anual Compuesto = f(begin, end, years)", "ei": "1000 USD; 2000 USD; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Tasa Crecimiento Anual Compuesto = f(begin, end, years)", "ei": "1000 USD; 2000 USD; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Tasa Crecimiento Anual Compuesto = f(begin, end, years)", "ei": "1000 USD; 2000 USD; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "321": {"en": {"f": "Tasa Anual Efectiva = f(nominal, n)", "ei": "12 %; 12", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Tasa Anual Efectiva = f(nominal, n)", "ei": "12 %; 12", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Tasa Anual Efectiva = f(nominal, n)", "ei": "12 %; 12", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Tasa Anual Efectiva = f(nominal, n)", "ei": "12 %; 12", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Tasa Anual Efectiva = f(nominal, n)", "ei": "12 %; 12", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Tasa Anual Efectiva = f(nominal, n)", "ei": "12 %; 12", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "322": {"en": {"f": "Amortizacion Prestamo = f(principal, rate, years)", "ei": "100000 USD; 5 %; 30 yr", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Amortizacion Prestamo = f(principal, rate, years)", "ei": "100000 USD; 5 %; 30 yr", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Amortizacion Prestamo = f(principal, rate, years)", "ei": "100000 USD; 5 %; 30 yr", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Amortizacion Prestamo = f(principal, rate, years)", "ei": "100000 USD; 5 %; 30 yr", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Amortizacion Prestamo = f(principal, rate, years)", "ei": "100000 USD; 5 %; 30 yr", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Amortizacion Prestamo = f(principal, rate, years)", "ei": "100000 USD; 5 %; 30 yr", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "323": {"en": {"f": "Rentabilidad Alquiler = f(annual_rent, property_value)", "ei": "12000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Rentabilidad Alquiler = f(annual_rent, property_value)", "ei": "12000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Rentabilidad Alquiler = f(annual_rent, property_value)", "ei": "12000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Rentabilidad Alquiler = f(annual_rent, property_value)", "ei": "12000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Rentabilidad Alquiler = f(annual_rent, property_value)", "ei": "12000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Rentabilidad Alquiler = f(annual_rent, property_value)", "ei": "12000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "324": {"en": {"f": "Tasa Capitalizacion = f(noi, value)", "ei": "15000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Tasa Capitalizacion = f(noi, value)", "ei": "15000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Tasa Capitalizacion = f(noi, value)", "ei": "15000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Tasa Capitalizacion = f(noi, value)", "ei": "15000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Tasa Capitalizacion = f(noi, value)", "ei": "15000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Tasa Capitalizacion = f(noi, value)", "ei": "15000 USD; 200000 USD", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "325": {"en": {"f": "Dividend Yield = f(annual_div, share_price)", "ei": "2 USD; 50 USD", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Dividend Yield = f(annual_div, share_price)", "ei": "2 USD; 50 USD", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Dividend Yield = f(annual_div, share_price)", "ei": "2 USD; 50 USD", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Dividend Yield = f(annual_div, share_price)", "ei": "2 USD; 50 USD", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Dividend Yield = f(annual_div, share_price)", "ei": "2 USD; 50 USD", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Dividend Yield = f(annual_div, share_price)", "ei": "2 USD; 50 USD", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "326": {"en": {"f": "Ratio Per = f(price, eps)", "ei": "100 USD; 5 USD", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Ratio Per = f(price, eps)", "ei": "100 USD; 5 USD", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Ratio Per = f(price, eps)", "ei": "100 USD; 5 USD", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Ratio Per = f(price, eps)", "ei": "100 USD; 5 USD", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Ratio Per = f(price, eps)", "ei": "100 USD; 5 USD", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Ratio Per = f(price, eps)", "ei": "100 USD; 5 USD", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "327": {"en": {"f": "Valor Futuro Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Valor Futuro Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Valor Futuro Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Valor Futuro Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Valor Futuro Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Valor Futuro Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "328": {"en": {"f": "Valor Actual Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Valor Actual Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Valor Actual Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Valor Actual Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Valor Actual Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Valor Actual Anualidad = f(pmt, rate, n)", "ei": "100 USD; 5 %; 10 yr", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "329": {"en": {"f": "Wacc = f(equity, debt, cost_eq, cost_debt)", "ei": "60 %; 40 %; 10 %; 5 %", "eo": "Results calculated from 5 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Wacc = f(equity, debt, cost_eq, cost_debt)", "ei": "60 %; 40 %; 10 %; 5 %", "eo": "Results calculated from 5 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Wacc = f(equity, debt, cost_eq, cost_debt)", "ei": "60 %; 40 %; 10 %; 5 %", "eo": "Results calculated from 5 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Wacc = f(equity, debt, cost_eq, cost_debt)", "ei": "60 %; 40 %; 10 %; 5 %", "eo": "Results calculated from 5 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Wacc = f(equity, debt, cost_eq, cost_debt)", "ei": "60 %; 40 %; 10 %; 5 %", "eo": "Results calculated from 5 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Wacc = f(equity, debt, cost_eq, cost_debt)", "ei": "60 %; 40 %; 10 %; 5 %", "eo": "Results calculated from 5 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "330": {"en": {"f": "Periodo Recuperacion = f(investment, annual_cash)", "ei": "10000 USD; 2500 USD", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Periodo Recuperacion = f(investment, annual_cash)", "ei": "10000 USD; 2500 USD", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Periodo Recuperacion = f(investment, annual_cash)", "ei": "10000 USD; 2500 USD", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Periodo Recuperacion = f(investment, annual_cash)", "ei": "10000 USD; 2500 USD", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Periodo Recuperacion = f(investment, annual_cash)", "ei": "10000 USD; 2500 USD", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Periodo Recuperacion = f(investment, annual_cash)", "ei": "10000 USD; 2500 USD", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "331": {"en": {"f": "Ratio Sharpe = f(return_p, rf, sd)", "ei": "12 %; 3 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Ratio Sharpe = f(return_p, rf, sd)", "ei": "12 %; 3 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Ratio Sharpe = f(return_p, rf, sd)", "ei": "12 %; 3 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Ratio Sharpe = f(return_p, rf, sd)", "ei": "12 %; 3 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Ratio Sharpe = f(return_p, rf, sd)", "ei": "12 %; 3 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Ratio Sharpe = f(return_p, rf, sd)", "ei": "12 %; 3 %; 15 %", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "332": {"en": {"f": "Rendimiento Equivalente Impuestos = f(muni_yield, tax_rate)", "ei": "4 %; 25 %", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Rendimiento Equivalente Impuestos = f(muni_yield, tax_rate)", "ei": "4 %; 25 %", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Rendimiento Equivalente Impuestos = f(muni_yield, tax_rate)", "ei": "4 %; 25 %", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Rendimiento Equivalente Impuestos = f(muni_yield, tax_rate)", "ei": "4 %; 25 %", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Rendimiento Equivalente Impuestos = f(muni_yield, tax_rate)", "ei": "4 %; 25 %", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Rendimiento Equivalente Impuestos = f(muni_yield, tax_rate)", "ei": "4 %; 25 %", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "333": {"en": {"f": "Tasa Real Retorno = f(nominal, inflation)", "ei": "8 %; 3 %", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Tasa Real Retorno = f(nominal, inflation)", "ei": "8 %; 3 %", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Tasa Real Retorno = f(nominal, inflation)", "ei": "8 %; 3 %", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Tasa Real Retorno = f(nominal, inflation)", "ei": "8 %; 3 %", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Tasa Real Retorno = f(nominal, inflation)", "ei": "8 %; 3 %", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Tasa Real Retorno = f(nominal, inflation)", "ei": "8 %; 3 %", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "334": {"en": {"f": "Prestamo Afordable = f(income, debt_ratio, rate, years)", "ei": "5000 USD; 36 %; 5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Prestamo Afordable = f(income, debt_ratio, rate, years)", "ei": "5000 USD; 36 %; 5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Prestamo Afordable = f(income, debt_ratio, rate, years)", "ei": "5000 USD; 36 %; 5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Prestamo Afordable = f(income, debt_ratio, rate, years)", "ei": "5000 USD; 36 %; 5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Prestamo Afordable = f(income, debt_ratio, rate, years)", "ei": "5000 USD; 36 %; 5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Prestamo Afordable = f(income, debt_ratio, rate, years)", "ei": "5000 USD; 36 %; 5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "335": {"en": {"f": "Liquidacion Hipoteca = f(balance, rate, extra)", "ei": "200000 USD; 4 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Liquidacion Hipoteca = f(balance, rate, extra)", "ei": "200000 USD; 4 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Liquidacion Hipoteca = f(balance, rate, extra)", "ei": "200000 USD; 4 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Liquidacion Hipoteca = f(balance, rate, extra)", "ei": "200000 USD; 4 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Liquidacion Hipoteca = f(balance, rate, extra)", "ei": "200000 USD; 4 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Liquidacion Hipoteca = f(balance, rate, extra)", "ei": "200000 USD; 4 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "336": {"en": {"f": "Liquidacion Tarjeta Credito = f(balance, rate, payment)", "ei": "5000 USD; 18 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Liquidacion Tarjeta Credito = f(balance, rate, payment)", "ei": "5000 USD; 18 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Liquidacion Tarjeta Credito = f(balance, rate, payment)", "ei": "5000 USD; 18 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Liquidacion Tarjeta Credito = f(balance, rate, payment)", "ei": "5000 USD; 18 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Liquidacion Tarjeta Credito = f(balance, rate, payment)", "ei": "5000 USD; 18 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Liquidacion Tarjeta Credito = f(balance, rate, payment)", "ei": "5000 USD; 18 %; 200 USD", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "337": {"en": {"f": "Ahorro Universidad = f(cost, years, rate)", "ei": "100000 USD; 18 yr; 6 %", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Ahorro Universidad = f(cost, years, rate)", "ei": "100000 USD; 18 yr; 6 %", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Ahorro Universidad = f(cost, years, rate)", "ei": "100000 USD; 18 yr; 6 %", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Ahorro Universidad = f(cost, years, rate)", "ei": "100000 USD; 18 yr; 6 %", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Ahorro Universidad = f(cost, years, rate)", "ei": "100000 USD; 18 yr; 6 %", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Ahorro Universidad = f(cost, years, rate)", "ei": "100000 USD; 18 yr; 6 %", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "338": {"en": {"f": "Necesidades Seguro Vida = f(income, years, debts, savings)", "ei": "60000 USD; 10 yr; 200000 USD; 50000 USD", "eo": "Results calculated from 4 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Necesidades Seguro Vida = f(income, years, debts, savings)", "ei": "60000 USD; 10 yr; 200000 USD; 50000 USD", "eo": "Results calculated from 4 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Necesidades Seguro Vida = f(income, years, debts, savings)", "ei": "60000 USD; 10 yr; 200000 USD; 50000 USD", "eo": "Results calculated from 4 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Necesidades Seguro Vida = f(income, years, debts, savings)", "ei": "60000 USD; 10 yr; 200000 USD; 50000 USD", "eo": "Results calculated from 4 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Necesidades Seguro Vida = f(income, years, debts, savings)", "ei": "60000 USD; 10 yr; 200000 USD; 50000 USD", "eo": "Results calculated from 4 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Necesidades Seguro Vida = f(income, years, debts, savings)", "ei": "60000 USD; 10 yr; 200000 USD; 50000 USD", "eo": "Results calculated from 4 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "339": {"en": {"f": "Cagr Mensual = f(begin, end, months)", "ei": "1000 USD; 2000 USD; 60 mo", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Cagr Mensual = f(begin, end, months)", "ei": "1000 USD; 2000 USD; 60 mo", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Cagr Mensual = f(begin, end, months)", "ei": "1000 USD; 2000 USD; 60 mo", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Cagr Mensual = f(begin, end, months)", "ei": "1000 USD; 2000 USD; 60 mo", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Cagr Mensual = f(begin, end, months)", "ei": "1000 USD; 2000 USD; 60 mo", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Cagr Mensual = f(begin, end, months)", "ei": "1000 USD; 2000 USD; 60 mo", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "415": {"en": {"f": "Masa Magra = f(weight, height, gender)", "ei": "70 kg; 175 cm; male", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Masa Magra = f(weight, height, gender)", "ei": "70 kg; 175 cm; male", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Masa Magra = f(weight, height, gender)", "ei": "70 kg; 175 cm; male", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Masa Magra = f(weight, height, gender)", "ei": "70 kg; 175 cm; male", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Masa Magra = f(weight, height, gender)", "ei": "70 kg; 175 cm; male", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Masa Magra = f(weight, height, gender)", "ei": "70 kg; 175 cm; male", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "416": {"en": {"f": "Indice Adiposidad Corporal = f(hip, height)", "ei": "100 cm; 175 cm", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Indice Adiposidad Corporal = f(hip, height)", "ei": "100 cm; 175 cm", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Indice Adiposidad Corporal = f(hip, height)", "ei": "100 cm; 175 cm", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Indice Adiposidad Corporal = f(hip, height)", "ei": "100 cm; 175 cm", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Indice Adiposidad Corporal = f(hip, height)", "ei": "100 cm; 175 cm", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Indice Adiposidad Corporal = f(hip, height)", "ei": "100 cm; 175 cm", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "417": {"en": {"f": "Ingesta Proteica = f(weight, activity)", "ei": "70 kg; 1.2", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Ingesta Proteica = f(weight, activity)", "ei": "70 kg; 1.2", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Ingesta Proteica = f(weight, activity)", "ei": "70 kg; 1.2", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Ingesta Proteica = f(weight, activity)", "ei": "70 kg; 1.2", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Ingesta Proteica = f(weight, activity)", "ei": "70 kg; 1.2", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Ingesta Proteica = f(weight, activity)", "ei": "70 kg; 1.2", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "418": {"en": {"f": "Ingesta Fibra = f(calories)", "ei": "2000 kcal", "eo": "Results calculated from 1 input", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Ingesta Fibra = f(calories)", "ei": "2000 kcal", "eo": "Results calculated from 1 input", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Ingesta Fibra = f(calories)", "ei": "2000 kcal", "eo": "Results calculated from 1 input", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Ingesta Fibra = f(calories)", "ei": "2000 kcal", "eo": "Results calculated from 1 input", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Ingesta Fibra = f(calories)", "ei": "2000 kcal", "eo": "Results calculated from 1 input", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Ingesta Fibra = f(calories)", "ei": "2000 kcal", "eo": "Results calculated from 1 input", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "419": {"en": {"f": "Frecuencia Cardiaca Karvonen = f(age, rest_hr, intensity)", "ei": "30 yr; 60 bpm; 70 %", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Frecuencia Cardiaca Karvonen = f(age, rest_hr, intensity)", "ei": "30 yr; 60 bpm; 70 %", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Frecuencia Cardiaca Karvonen = f(age, rest_hr, intensity)", "ei": "30 yr; 60 bpm; 70 %", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Frecuencia Cardiaca Karvonen = f(age, rest_hr, intensity)", "ei": "30 yr; 60 bpm; 70 %", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Frecuencia Cardiaca Karvonen = f(age, rest_hr, intensity)", "ei": "30 yr; 60 bpm; 70 %", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Frecuencia Cardiaca Karvonen = f(age, rest_hr, intensity)", "ei": "30 yr; 60 bpm; 70 %", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "420": {"en": {"f": "Zonas Frecuencia Cardiaca = f(age)", "ei": "30 yr", "eo": "Results calculated from 1 input", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Zonas Frecuencia Cardiaca = f(age)", "ei": "30 yr", "eo": "Results calculated from 1 input", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Zonas Frecuencia Cardiaca = f(age)", "ei": "30 yr", "eo": "Results calculated from 1 input", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Zonas Frecuencia Cardiaca = f(age)", "ei": "30 yr", "eo": "Results calculated from 1 input", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Zonas Frecuencia Cardiaca = f(age)", "ei": "30 yr", "eo": "Results calculated from 1 input", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Zonas Frecuencia Cardiaca = f(age)", "ei": "30 yr", "eo": "Results calculated from 1 input", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "421": {"en": {"f": "Aclaramiento Creatinina = f(age, weight, creatinine, gender)", "ei": "50 yr; 70 kg; 1 mg/dL; male", "eo": "Results calculated from 4 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Aclaramiento Creatinina = f(age, weight, creatinine, gender)", "ei": "50 yr; 70 kg; 1 mg/dL; male", "eo": "Results calculated from 4 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Aclaramiento Creatinina = f(age, weight, creatinine, gender)", "ei": "50 yr; 70 kg; 1 mg/dL; male", "eo": "Results calculated from 4 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Aclaramiento Creatinina = f(age, weight, creatinine, gender)", "ei": "50 yr; 70 kg; 1 mg/dL; male", "eo": "Results calculated from 4 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Aclaramiento Creatinina = f(age, weight, creatinine, gender)", "ei": "50 yr; 70 kg; 1 mg/dL; male", "eo": "Results calculated from 4 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Aclaramiento Creatinina = f(age, weight, creatinine, gender)", "ei": "50 yr; 70 kg; 1 mg/dL; male", "eo": "Results calculated from 4 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "422": {"en": {"f": "Bmi Prime = f(bmi)", "ei": "25", "eo": "Results calculated from 1 input", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Bmi Prime = f(bmi)", "ei": "25", "eo": "Results calculated from 1 input", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Bmi Prime = f(bmi)", "ei": "25", "eo": "Results calculated from 1 input", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Bmi Prime = f(bmi)", "ei": "25", "eo": "Results calculated from 1 input", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Bmi Prime = f(bmi)", "ei": "25", "eo": "Results calculated from 1 input", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Bmi Prime = f(bmi)", "ei": "25", "eo": "Results calculated from 1 input", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "423": {"en": {"f": "Fecha Parto = f(lmp)", "ei": "", "eo": "Results calculated from 1 input", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Fecha Parto = f(lmp)", "ei": "", "eo": "Results calculated from 1 input", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Fecha Parto = f(lmp)", "ei": "", "eo": "Results calculated from 1 input", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Fecha Parto = f(lmp)", "ei": "", "eo": "Results calculated from 1 input", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Fecha Parto = f(lmp)", "ei": "", "eo": "Results calculated from 1 input", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Fecha Parto = f(lmp)", "ei": "", "eo": "Results calculated from 1 input", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "424": {"en": {"f": "Calculadora Ovulacion = f(lmp, cycle)", "ei": "; 28 days", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Calculadora Ovulacion = f(lmp, cycle)", "ei": "; 28 days", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Calculadora Ovulacion = f(lmp, cycle)", "ei": "; 28 days", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Calculadora Ovulacion = f(lmp, cycle)", "ei": "; 28 days", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Calculadora Ovulacion = f(lmp, cycle)", "ei": "; 28 days", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Calculadora Ovulacion = f(lmp, cycle)", "ei": "; 28 days", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "425": {"en": {"f": "Grasa Corporal Navy = f(waist, neck, height, gender)", "ei": "80 cm; 40 cm; 175 cm; male", "eo": "Results calculated from 4 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Grasa Corporal Navy = f(waist, neck, height, gender)", "ei": "80 cm; 40 cm; 175 cm; male", "eo": "Results calculated from 4 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Grasa Corporal Navy = f(waist, neck, height, gender)", "ei": "80 cm; 40 cm; 175 cm; male", "eo": "Results calculated from 4 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Grasa Corporal Navy = f(waist, neck, height, gender)", "ei": "80 cm; 40 cm; 175 cm; male", "eo": "Results calculated from 4 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Grasa Corporal Navy = f(waist, neck, height, gender)", "ei": "80 cm; 40 cm; 175 cm; male", "eo": "Results calculated from 4 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Grasa Corporal Navy = f(waist, neck, height, gender)", "ei": "80 cm; 40 cm; 175 cm; male", "eo": "Results calculated from 4 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "426": {"en": {"f": "Gasto Energetico Total = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 5 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Gasto Energetico Total = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 5 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Gasto Energetico Total = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 5 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Gasto Energetico Total = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 5 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Gasto Energetico Total = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 5 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Gasto Energetico Total = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 5 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "427": {"en": {"f": "Tasa Metabolica Basal Mifflin = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Tasa Metabolica Basal Mifflin = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Tasa Metabolica Basal Mifflin = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Tasa Metabolica Basal Mifflin = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Tasa Metabolica Basal Mifflin = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Tasa Metabolica Basal Mifflin = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "428": {"en": {"f": "Metabolismo En Reposo = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Metabolismo En Reposo = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Metabolismo En Reposo = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Metabolismo En Reposo = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Metabolismo En Reposo = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Metabolismo En Reposo = f(weight, height, age, gender)", "ei": "70 kg; 175 cm; 30 yr; male", "eo": "Results calculated from 4 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "429": {"en": {"f": "Mets Actividad = f(weight, mets, minutes)", "ei": "70 kg; 5 METs; 30 min", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Mets Actividad = f(weight, mets, minutes)", "ei": "70 kg; 5 METs; 30 min", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Mets Actividad = f(weight, mets, minutes)", "ei": "70 kg; 5 METs; 30 min", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Mets Actividad = f(weight, mets, minutes)", "ei": "70 kg; 5 METs; 30 min", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Mets Actividad = f(weight, mets, minutes)", "ei": "70 kg; 5 METs; 30 min", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Mets Actividad = f(weight, mets, minutes)", "ei": "70 kg; 5 METs; 30 min", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "430": {"en": {"f": "Peso Objetivo = f(current, goal_bmi, height)", "ei": "80 kg; 22; 175 cm", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Peso Objetivo = f(current, goal_bmi, height)", "ei": "80 kg; 22; 175 cm", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Peso Objetivo = f(current, goal_bmi, height)", "ei": "80 kg; 22; 175 cm", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Peso Objetivo = f(current, goal_bmi, height)", "ei": "80 kg; 22; 175 cm", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Peso Objetivo = f(current, goal_bmi, height)", "ei": "80 kg; 22; 175 cm", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Peso Objetivo = f(current, goal_bmi, height)", "ei": "80 kg; 22; 175 cm", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "431": {"en": {"f": "Aumento Peso Embarazo = f(pre_bmi)", "ei": "22", "eo": "Results calculated from 1 input", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Aumento Peso Embarazo = f(pre_bmi)", "ei": "22", "eo": "Results calculated from 1 input", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Aumento Peso Embarazo = f(pre_bmi)", "ei": "22", "eo": "Results calculated from 1 input", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Aumento Peso Embarazo = f(pre_bmi)", "ei": "22", "eo": "Results calculated from 1 input", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Aumento Peso Embarazo = f(pre_bmi)", "ei": "22", "eo": "Results calculated from 1 input", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Aumento Peso Embarazo = f(pre_bmi)", "ei": "22", "eo": "Results calculated from 1 input", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "432": {"en": {"f": "Calorias Caminar = f(weight, distance, speed)", "ei": "70 kg; 5 km; 5 km/h", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Calorias Caminar = f(weight, distance, speed)", "ei": "70 kg; 5 km; 5 km/h", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Calorias Caminar = f(weight, distance, speed)", "ei": "70 kg; 5 km; 5 km/h", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Calorias Caminar = f(weight, distance, speed)", "ei": "70 kg; 5 km; 5 km/h", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Calorias Caminar = f(weight, distance, speed)", "ei": "70 kg; 5 km; 5 km/h", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Calorias Caminar = f(weight, distance, speed)", "ei": "70 kg; 5 km; 5 km/h", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "433": {"en": {"f": "Percentil Crecimiento Infantil = f(age_months, height, gender)", "ei": "24 mo; 85 cm; male", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Percentil Crecimiento Infantil = f(age_months, height, gender)", "ei": "24 mo; 85 cm; male", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Percentil Crecimiento Infantil = f(age_months, height, gender)", "ei": "24 mo; 85 cm; male", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Percentil Crecimiento Infantil = f(age_months, height, gender)", "ei": "24 mo; 85 cm; male", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Percentil Crecimiento Infantil = f(age_months, height, gender)", "ei": "24 mo; 85 cm; male", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Percentil Crecimiento Infantil = f(age_months, height, gender)", "ei": "24 mo; 85 cm; male", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "434": {"en": {"f": "Agua Por Peso = f(weight, activity)", "ei": "70 kg; 30 min", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Agua Por Peso = f(weight, activity)", "ei": "70 kg; 30 min", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Agua Por Peso = f(weight, activity)", "ei": "70 kg; 30 min", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Agua Por Peso = f(weight, activity)", "ei": "70 kg; 30 min", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Agua Por Peso = f(weight, activity)", "ei": "70 kg; 30 min", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Agua Por Peso = f(weight, activity)", "ei": "70 kg; 30 min", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "503": {"en": {"f": "Coste Combustible = f(distance, efficiency, price)", "ei": "100 km; 6 L/100km; 1.5 $/L", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Coste Combustible = f(distance, efficiency, price)", "ei": "100 km; 6 L/100km; 1.5 $/L", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Coste Combustible = f(distance, efficiency, price)", "ei": "100 km; 6 L/100km; 1.5 $/L", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Coste Combustible = f(distance, efficiency, price)", "ei": "100 km; 6 L/100km; 1.5 $/L", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Coste Combustible = f(distance, efficiency, price)", "ei": "100 km; 6 L/100km; 1.5 $/L", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Coste Combustible = f(distance, efficiency, price)", "ei": "100 km; 6 L/100km; 1.5 $/L", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "504": {"en": {"f": "Tiempo Transferencia Datos = f(size, speed)", "ei": "1 GB; 100 Mbps", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tiempo Transferencia Datos = f(size, speed)", "ei": "1 GB; 100 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tiempo Transferencia Datos = f(size, speed)", "ei": "1 GB; 100 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tiempo Transferencia Datos = f(size, speed)", "ei": "1 GB; 100 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tiempo Transferencia Datos = f(size, speed)", "ei": "1 GB; 100 Mbps", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tiempo Transferencia Datos = f(size, speed)", "ei": "1 GB; 100 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "505": {"en": {"f": "Duracion Bateria = f(capacity, consumption)", "ei": "4000 mAh; 500 mA", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Duracion Bateria = f(capacity, consumption)", "ei": "4000 mAh; 500 mA", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Duracion Bateria = f(capacity, consumption)", "ei": "4000 mAh; 500 mA", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Duracion Bateria = f(capacity, consumption)", "ei": "4000 mAh; 500 mA", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Duracion Bateria = f(capacity, consumption)", "ei": "4000 mAh; 500 mA", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Duracion Bateria = f(capacity, consumption)", "ei": "4000 mAh; 500 mA", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "506": {"en": {"f": "Tiempo Descarga = f(file_size, speed)", "ei": "1 GB; 50 Mbps", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tiempo Descarga = f(file_size, speed)", "ei": "1 GB; 50 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tiempo Descarga = f(file_size, speed)", "ei": "1 GB; 50 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tiempo Descarga = f(file_size, speed)", "ei": "1 GB; 50 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tiempo Descarga = f(file_size, speed)", "ei": "1 GB; 50 Mbps", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tiempo Descarga = f(file_size, speed)", "ei": "1 GB; 50 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "507": {"en": {"f": "Dpi Pantalla = f(width_px, height_px, diagonal_in)", "ei": "1920 px; 1080 px; 24 in", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Dpi Pantalla = f(width_px, height_px, diagonal_in)", "ei": "1920 px; 1080 px; 24 in", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Dpi Pantalla = f(width_px, height_px, diagonal_in)", "ei": "1920 px; 1080 px; 24 in", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Dpi Pantalla = f(width_px, height_px, diagonal_in)", "ei": "1920 px; 1080 px; 24 in", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Dpi Pantalla = f(width_px, height_px, diagonal_in)", "ei": "1920 px; 1080 px; 24 in", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Dpi Pantalla = f(width_px, height_px, diagonal_in)", "ei": "1920 px; 1080 px; 24 in", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "508": {"en": {"f": "Relacion Aspecto = f(width, height)", "ei": "16; 9", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Relacion Aspecto = f(width, height)", "ei": "16; 9", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Relacion Aspecto = f(width, height)", "ei": "16; 9", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Relacion Aspecto = f(width, height)", "ei": "16; 9", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Relacion Aspecto = f(width, height)", "ei": "16; 9", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Relacion Aspecto = f(width, height)", "ei": "16; 9", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "509": {"en": {"f": "Entropia Contrasena = f(length, pool)", "ei": "12 chars; 62 symbols", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Entropia Contrasena = f(length, pool)", "ei": "12 chars; 62 symbols", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Entropia Contrasena = f(length, pool)", "ei": "12 chars; 62 symbols", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Entropia Contrasena = f(length, pool)", "ei": "12 chars; 62 symbols", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Entropia Contrasena = f(length, pool)", "ei": "12 chars; 62 symbols", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Entropia Contrasena = f(length, pool)", "ei": "12 chars; 62 symbols", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "510": {"en": {"f": "Ancho Banda = f(users, usage)", "ei": "10 users; 5 Mbps", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Ancho Banda = f(users, usage)", "ei": "10 users; 5 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Ancho Banda = f(users, usage)", "ei": "10 users; 5 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Ancho Banda = f(users, usage)", "ei": "10 users; 5 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Ancho Banda = f(users, usage)", "ei": "10 users; 5 Mbps", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Ancho Banda = f(users, usage)", "ei": "10 users; 5 Mbps", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "511": {"en": {"f": "Tamano Archivo = f(width, height, depth)", "ei": "1920 px; 1080 px; 24 bits", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tamano Archivo = f(width, height, depth)", "ei": "1920 px; 1080 px; 24 bits", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tamano Archivo = f(width, height, depth)", "ei": "1920 px; 1080 px; 24 bits", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tamano Archivo = f(width, height, depth)", "ei": "1920 px; 1080 px; 24 bits", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tamano Archivo = f(width, height, depth)", "ei": "1920 px; 1080 px; 24 bits", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tamano Archivo = f(width, height, depth)", "ei": "1920 px; 1080 px; 24 bits", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "512": {"en": {"f": "Coste Consumo Electrico = f(power, hours, rate)", "ei": "100 W; 24 h; 0.15 $/kWh", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Coste Consumo Electrico = f(power, hours, rate)", "ei": "100 W; 24 h; 0.15 $/kWh", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Coste Consumo Electrico = f(power, hours, rate)", "ei": "100 W; 24 h; 0.15 $/kWh", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Coste Consumo Electrico = f(power, hours, rate)", "ei": "100 W; 24 h; 0.15 $/kWh", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Coste Consumo Electrico = f(power, hours, rate)", "ei": "100 W; 24 h; 0.15 $/kWh", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Coste Consumo Electrico = f(power, hours, rate)", "ei": "100 W; 24 h; 0.15 $/kWh", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "513": {"en": {"f": "Resolucion Pantalla = f(width, height)", "ei": "1920 px; 1080 px", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Resolucion Pantalla = f(width, height)", "ei": "1920 px; 1080 px", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Resolucion Pantalla = f(width, height)", "ei": "1920 px; 1080 px", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Resolucion Pantalla = f(width, height)", "ei": "1920 px; 1080 px", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Resolucion Pantalla = f(width, height)", "ei": "1920 px; 1080 px", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Resolucion Pantalla = f(width, height)", "ei": "1920 px; 1080 px", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "514": {"en": {"f": "Tamano Archivo Video = f(duration, bitrate)", "ei": "60 s; 5000 kbps", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tamano Archivo Video = f(duration, bitrate)", "ei": "60 s; 5000 kbps", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tamano Archivo Video = f(duration, bitrate)", "ei": "60 s; 5000 kbps", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tamano Archivo Video = f(duration, bitrate)", "ei": "60 s; 5000 kbps", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tamano Archivo Video = f(duration, bitrate)", "ei": "60 s; 5000 kbps", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tamano Archivo Video = f(duration, bitrate)", "ei": "60 s; 5000 kbps", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "515": {"en": {"f": "Capacidad Raid = f(drives, drive_size, raid)", "ei": "4; 2000 GB; 5", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Capacidad Raid = f(drives, drive_size, raid)", "ei": "4; 2000 GB; 5", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Capacidad Raid = f(drives, drive_size, raid)", "ei": "4; 2000 GB; 5", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Capacidad Raid = f(drives, drive_size, raid)", "ei": "4; 2000 GB; 5", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Capacidad Raid = f(drives, drive_size, raid)", "ei": "4; 2000 GB; 5", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Capacidad Raid = f(drives, drive_size, raid)", "ei": "4; 2000 GB; 5", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "516": {"en": {"f": "Tiempo Actividad = f(downtime_min, period)", "ei": "60 min; 30 days", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tiempo Actividad = f(downtime_min, period)", "ei": "60 min; 30 days", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tiempo Actividad = f(downtime_min, period)", "ei": "60 min; 30 days", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tiempo Actividad = f(downtime_min, period)", "ei": "60 min; 30 days", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tiempo Actividad = f(downtime_min, period)", "ei": "60 min; 30 days", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tiempo Actividad = f(downtime_min, period)", "ei": "60 min; 30 days", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "517": {"en": {"f": "Latencia Ping = f(distance, medium)", "ei": "1000 km; fiber", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Latencia Ping = f(distance, medium)", "ei": "1000 km; fiber", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Latencia Ping = f(distance, medium)", "ei": "1000 km; fiber", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Latencia Ping = f(distance, medium)", "ei": "1000 km; fiber", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Latencia Ping = f(distance, medium)", "ei": "1000 km; fiber", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Latencia Ping = f(distance, medium)", "ei": "1000 km; fiber", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "518": {"en": {"f": "Palabras Por Minuto = f(words, minutes, errors)", "ei": "300 words; 5 min; 5 errors", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Palabras Por Minuto = f(words, minutes, errors)", "ei": "300 words; 5 min; 5 errors", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Palabras Por Minuto = f(words, minutes, errors)", "ei": "300 words; 5 min; 5 errors", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Palabras Por Minuto = f(words, minutes, errors)", "ei": "300 words; 5 min; 5 errors", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Palabras Por Minuto = f(words, minutes, errors)", "ei": "300 words; 5 min; 5 errors", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Palabras Por Minuto = f(words, minutes, errors)", "ei": "300 words; 5 min; 5 errors", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "519": {"en": {"f": "Tiempo Lectura = f(word_count, wpm)", "ei": "1000 words; 200 WPM", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tiempo Lectura = f(word_count, wpm)", "ei": "1000 words; 200 WPM", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tiempo Lectura = f(word_count, wpm)", "ei": "1000 words; 200 WPM", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tiempo Lectura = f(word_count, wpm)", "ei": "1000 words; 200 WPM", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tiempo Lectura = f(word_count, wpm)", "ei": "1000 words; 200 WPM", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tiempo Lectura = f(word_count, wpm)", "ei": "1000 words; 200 WPM", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "520": {"en": {"f": "Coste Sms = f(messages, cost_per)", "ei": "100 SMS; 0.05 $/SMS", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Coste Sms = f(messages, cost_per)", "ei": "100 SMS; 0.05 $/SMS", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Coste Sms = f(messages, cost_per)", "ei": "100 SMS; 0.05 $/SMS", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Coste Sms = f(messages, cost_per)", "ei": "100 SMS; 0.05 $/SMS", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Coste Sms = f(messages, cost_per)", "ei": "100 SMS; 0.05 $/SMS", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Coste Sms = f(messages, cost_per)", "ei": "100 SMS; 0.05 $/SMS", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "521": {"en": {"f": "Estimador Datos = f(hours_video, hours_music, hours_web)", "ei": "2 h; 3 h; 4 h", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Estimador Datos = f(hours_video, hours_music, hours_web)", "ei": "2 h; 3 h; 4 h", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Estimador Datos = f(hours_video, hours_music, hours_web)", "ei": "2 h; 3 h; 4 h", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Estimador Datos = f(hours_video, hours_music, hours_web)", "ei": "2 h; 3 h; 4 h", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Estimador Datos = f(hours_video, hours_music, hours_web)", "ei": "2 h; 3 h; 4 h", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Estimador Datos = f(hours_video, hours_music, hours_web)", "ei": "2 h; 3 h; 4 h", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "522": {"en": {"f": "Brillo Pantalla Nits = f(lumens, area)", "ei": "300 lm; 0.1 m²", "eo": "Results calculated from 2 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Brillo Pantalla Nits = f(lumens, area)", "ei": "300 lm; 0.1 m²", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Brillo Pantalla Nits = f(lumens, area)", "ei": "300 lm; 0.1 m²", "eo": "Results calculated from 2 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Brillo Pantalla Nits = f(lumens, area)", "ei": "300 lm; 0.1 m²", "eo": "Results calculated from 2 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Brillo Pantalla Nits = f(lumens, area)", "ei": "300 lm; 0.1 m²", "eo": "Results calculated from 2 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Brillo Pantalla Nits = f(lumens, area)", "ei": "300 lm; 0.1 m²", "eo": "Results calculated from 2 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "910": {"en": {"f": "Fraction Calculator = f(numerador, denominador)", "ei": "1; 2", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Fraction Calculator = f(numerador, denominador)", "ei": "1; 2", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Fraction Calculator = f(numerador, denominador)", "ei": "1; 2", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Fraction Calculator = f(numerador, denominador)", "ei": "1; 2", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Fraction Calculator = f(numerador, denominador)", "ei": "1; 2", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Fraction Calculator = f(numerador, denominador)", "ei": "1; 2", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "911": {"en": {"f": "Slope Calculator = f(x1, y1, x2, y2)", "ei": "0; 0; 1; 1", "eo": "Results calculated from 4 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Slope Calculator = f(x1, y1, x2, y2)", "ei": "0; 0; 1; 1", "eo": "Results calculated from 4 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Slope Calculator = f(x1, y1, x2, y2)", "ei": "0; 0; 1; 1", "eo": "Results calculated from 4 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Slope Calculator = f(x1, y1, x2, y2)", "ei": "0; 0; 1; 1", "eo": "Results calculated from 4 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Slope Calculator = f(x1, y1, x2, y2)", "ei": "0; 0; 1; 1", "eo": "Results calculated from 4 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Slope Calculator = f(x1, y1, x2, y2)", "ei": "0; 0; 1; 1", "eo": "Results calculated from 4 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "912": {"en": {"f": "Scientific Notation = f(numero)", "ei": "1234.5", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Scientific Notation = f(numero)", "ei": "1234.5", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Scientific Notation = f(numero)", "ei": "1234.5", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Scientific Notation = f(numero)", "ei": "1234.5", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Scientific Notation = f(numero)", "ei": "1234.5", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Scientific Notation = f(numero)", "ei": "1234.5", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "913": {"en": {"f": "Rounding Calculator = f(numero, decimales)", "ei": "3.14159; 2", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Rounding Calculator = f(numero, decimales)", "ei": "3.14159; 2", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Rounding Calculator = f(numero, decimales)", "ei": "3.14159; 2", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Rounding Calculator = f(numero, decimales)", "ei": "3.14159; 2", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Rounding Calculator = f(numero, decimales)", "ei": "3.14159; 2", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Rounding Calculator = f(numero, decimales)", "ei": "3.14159; 2", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "914": {"en": {"f": "Gcf Lcm Calculator = f(a, b)", "ei": "12; 18", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Gcf Lcm Calculator = f(a, b)", "ei": "12; 18", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Gcf Lcm Calculator = f(a, b)", "ei": "12; 18", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Gcf Lcm Calculator = f(a, b)", "ei": "12; 18", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Gcf Lcm Calculator = f(a, b)", "ei": "12; 18", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Gcf Lcm Calculator = f(a, b)", "ei": "12; 18", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "915": {"en": {"f": "Prime Factorization = f(numero)", "ei": "60", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Prime Factorization = f(numero)", "ei": "60", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Prime Factorization = f(numero)", "ei": "60", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Prime Factorization = f(numero)", "ei": "60", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Prime Factorization = f(numero)", "ei": "60", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Prime Factorization = f(numero)", "ei": "60", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "916": {"en": {"f": "Circle Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Circle Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Circle Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Circle Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Circle Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Circle Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "917": {"en": {"f": "Right Triangle Calculator = f(cateto_a, cateto_b, hipotenusa)", "ei": "3; 4; 0", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Right Triangle Calculator = f(cateto_a, cateto_b, hipotenusa)", "ei": "3; 4; 0", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Right Triangle Calculator = f(cateto_a, cateto_b, hipotenusa)", "ei": "3; 4; 0", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Right Triangle Calculator = f(cateto_a, cateto_b, hipotenusa)", "ei": "3; 4; 0", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Right Triangle Calculator = f(cateto_a, cateto_b, hipotenusa)", "ei": "3; 4; 0", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Right Triangle Calculator = f(cateto_a, cateto_b, hipotenusa)", "ei": "3; 4; 0", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "918": {"en": {"f": "Heron Triangle Area = f(base, altura, lado_c)", "ei": "5; 6; 7", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Heron Triangle Area = f(base, altura, lado_c)", "ei": "5; 6; 7", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Heron Triangle Area = f(base, altura, lado_c)", "ei": "5; 6; 7", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Heron Triangle Area = f(base, altura, lado_c)", "ei": "5; 6; 7", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Heron Triangle Area = f(base, altura, lado_c)", "ei": "5; 6; 7", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Heron Triangle Area = f(base, altura, lado_c)", "ei": "5; 6; 7", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "919": {"en": {"f": "Rectangle Calculator = f(base, altura)", "ei": "10; 5", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Rectangle Calculator = f(base, altura)", "ei": "10; 5", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Rectangle Calculator = f(base, altura)", "ei": "10; 5", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Rectangle Calculator = f(base, altura)", "ei": "10; 5", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Rectangle Calculator = f(base, altura)", "ei": "10; 5", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Rectangle Calculator = f(base, altura)", "ei": "10; 5", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "920": {"en": {"f": "Square Calculator = f(lado)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Square Calculator = f(lado)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Square Calculator = f(lado)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Square Calculator = f(lado)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Square Calculator = f(lado)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Square Calculator = f(lado)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "921": {"en": {"f": "Trapezoid Calculator = f(base_mayor, base_menor, altura)", "ei": "10; 6; 4", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Trapezoid Calculator = f(base_mayor, base_menor, altura)", "ei": "10; 6; 4", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Trapezoid Calculator = f(base_mayor, base_menor, altura)", "ei": "10; 6; 4", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Trapezoid Calculator = f(base_mayor, base_menor, altura)", "ei": "10; 6; 4", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Trapezoid Calculator = f(base_mayor, base_menor, altura)", "ei": "10; 6; 4", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Trapezoid Calculator = f(base_mayor, base_menor, altura)", "ei": "10; 6; 4", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "922": {"en": {"f": "Cylinder Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Cylinder Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Cylinder Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Cylinder Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Cylinder Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Cylinder Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "923": {"en": {"f": "Cone Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Cone Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Cone Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Cone Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Cone Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Cone Volume = f(radio, altura)", "ei": "3; 10", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "924": {"en": {"f": "Pyramid Volume = f(base, lado_b, lado_c, altura)", "ei": "6; 5; 5; 8", "eo": "Results calculated from 4 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Pyramid Volume = f(base, lado_b, lado_c, altura)", "ei": "6; 5; 5; 8", "eo": "Results calculated from 4 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Pyramid Volume = f(base, lado_b, lado_c, altura)", "ei": "6; 5; 5; 8", "eo": "Results calculated from 4 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Pyramid Volume = f(base, lado_b, lado_c, altura)", "ei": "6; 5; 5; 8", "eo": "Results calculated from 4 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Pyramid Volume = f(base, lado_b, lado_c, altura)", "ei": "6; 5; 5; 8", "eo": "Results calculated from 4 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Pyramid Volume = f(base, lado_b, lado_c, altura)", "ei": "6; 5; 5; 8", "eo": "Results calculated from 4 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "925": {"en": {"f": "Sphere Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Sphere Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Sphere Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Sphere Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Sphere Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Sphere Calculator = f(radio)", "ei": "5", "eo": "Results calculated from 1 input", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "926": {"en": {"f": "Bmr Harris Benedict = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 4 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Bmr Harris Benedict = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 4 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Bmr Harris Benedict = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 4 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Bmr Harris Benedict = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 4 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Bmr Harris Benedict = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 4 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Bmr Harris Benedict = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 4 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "927": {"en": {"f": "Bmr Katch Mcardle = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 5 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Bmr Katch Mcardle = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 5 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Bmr Katch Mcardle = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 5 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Bmr Katch Mcardle = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 5 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Bmr Katch Mcardle = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 5 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Bmr Katch Mcardle = f(peso_kg, altura_cm, edad, sexo)", "ei": "70 kg; 175 cm; 30 years; mujer", "eo": "Results calculated from 5 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "928": {"en": {"f": "Macro Calculator = f(peso_kg, ejercicio_hrs, objetivo)", "ei": "70 kg; 3 h; mantener", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Macro Calculator = f(peso_kg, ejercicio_hrs, objetivo)", "ei": "70 kg; 3 h; mantener", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Macro Calculator = f(peso_kg, ejercicio_hrs, objetivo)", "ei": "70 kg; 3 h; mantener", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Macro Calculator = f(peso_kg, ejercicio_hrs, objetivo)", "ei": "70 kg; 3 h; mantener", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Macro Calculator = f(peso_kg, ejercicio_hrs, objetivo)", "ei": "70 kg; 3 h; mantener", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Macro Calculator = f(peso_kg, ejercicio_hrs, objetivo)", "ei": "70 kg; 3 h; mantener", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "929": {"en": {"f": "Blood Pressure = f(sistolica, diastolica)", "ei": "120 mmHg; 80 mmHg", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Blood Pressure = f(sistolica, diastolica)", "ei": "120 mmHg; 80 mmHg", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Blood Pressure = f(sistolica, diastolica)", "ei": "120 mmHg; 80 mmHg", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Blood Pressure = f(sistolica, diastolica)", "ei": "120 mmHg; 80 mmHg", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Blood Pressure = f(sistolica, diastolica)", "ei": "120 mmHg; 80 mmHg", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Blood Pressure = f(sistolica, diastolica)", "ei": "120 mmHg; 80 mmHg", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "930": {"en": {"f": "Waist Hip Ratio = f(cintura_cm, cadera_cm, sexo)", "ei": "80 cm; 95 cm; mujer", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Waist Hip Ratio = f(cintura_cm, cadera_cm, sexo)", "ei": "80 cm; 95 cm; mujer", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Waist Hip Ratio = f(cintura_cm, cadera_cm, sexo)", "ei": "80 cm; 95 cm; mujer", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Waist Hip Ratio = f(cintura_cm, cadera_cm, sexo)", "ei": "80 cm; 95 cm; mujer", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Waist Hip Ratio = f(cintura_cm, cadera_cm, sexo)", "ei": "80 cm; 95 cm; mujer", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Waist Hip Ratio = f(cintura_cm, cadera_cm, sexo)", "ei": "80 cm; 95 cm; mujer", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "931": {"en": {"f": "Waist Height Ratio = f(altura_cm, cintura_cm)", "ei": "175 cm; 80 cm", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Waist Height Ratio = f(altura_cm, cintura_cm)", "ei": "175 cm; 80 cm", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Waist Height Ratio = f(altura_cm, cintura_cm)", "ei": "175 cm; 80 cm", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Waist Height Ratio = f(altura_cm, cintura_cm)", "ei": "175 cm; 80 cm", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Waist Height Ratio = f(altura_cm, cintura_cm)", "ei": "175 cm; 80 cm", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Waist Height Ratio = f(altura_cm, cintura_cm)", "ei": "175 cm; 80 cm", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "932": {"en": {"f": "Weight Loss Percentage = f(peso_inicial, peso_actual)", "ei": "80 kg; 75 kg", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Weight Loss Percentage = f(peso_inicial, peso_actual)", "ei": "80 kg; 75 kg", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Weight Loss Percentage = f(peso_inicial, peso_actual)", "ei": "80 kg; 75 kg", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Weight Loss Percentage = f(peso_inicial, peso_actual)", "ei": "80 kg; 75 kg", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Weight Loss Percentage = f(peso_inicial, peso_actual)", "ei": "80 kg; 75 kg", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Weight Loss Percentage = f(peso_inicial, peso_actual)", "ei": "80 kg; 75 kg", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "933": {"en": {"f": "Heart Rate Zones = f(edad, fc_reposo)", "ei": "30 years; 60 bpm", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Heart Rate Zones = f(edad, fc_reposo)", "ei": "30 years; 60 bpm", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Heart Rate Zones = f(edad, fc_reposo)", "ei": "30 years; 60 bpm", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Heart Rate Zones = f(edad, fc_reposo)", "ei": "30 years; 60 bpm", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Heart Rate Zones = f(edad, fc_reposo)", "ei": "30 years; 60 bpm", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Heart Rate Zones = f(edad, fc_reposo)", "ei": "30 years; 60 bpm", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "934": {"en": {"f": "Salary To Hourly = f(salario_anual, horas_semana, semanas_ano)", "ei": "50000 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Salary To Hourly = f(salario_anual, horas_semana, semanas_ano)", "ei": "50000 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Salary To Hourly = f(salario_anual, horas_semana, semanas_ano)", "ei": "50000 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Salary To Hourly = f(salario_anual, horas_semana, semanas_ano)", "ei": "50000 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Salary To Hourly = f(salario_anual, horas_semana, semanas_ano)", "ei": "50000 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Salary To Hourly = f(salario_anual, horas_semana, semanas_ano)", "ei": "50000 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "935": {"en": {"f": "Hourly To Salary = f(salario_hora, horas_semana, semanas_ano)", "ei": "25 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Hourly To Salary = f(salario_hora, horas_semana, semanas_ano)", "ei": "25 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Hourly To Salary = f(salario_hora, horas_semana, semanas_ano)", "ei": "25 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Hourly To Salary = f(salario_hora, horas_semana, semanas_ano)", "ei": "25 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Hourly To Salary = f(salario_hora, horas_semana, semanas_ano)", "ei": "25 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Hourly To Salary = f(salario_hora, horas_semana, semanas_ano)", "ei": "25 EUR; 40 h; 52 wk", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "936": {"en": {"f": "Mortgage Calculator = f(precio_casa, entrada_pct, tasa_anual, anos)", "ei": "300000 EUR; 20 %; 3.5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Mortgage Calculator = f(precio_casa, entrada_pct, tasa_anual, anos)", "ei": "300000 EUR; 20 %; 3.5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Mortgage Calculator = f(precio_casa, entrada_pct, tasa_anual, anos)", "ei": "300000 EUR; 20 %; 3.5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Mortgage Calculator = f(precio_casa, entrada_pct, tasa_anual, anos)", "ei": "300000 EUR; 20 %; 3.5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Mortgage Calculator = f(precio_casa, entrada_pct, tasa_anual, anos)", "ei": "300000 EUR; 20 %; 3.5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Mortgage Calculator = f(precio_casa, entrada_pct, tasa_anual, anos)", "ei": "300000 EUR; 20 %; 3.5 %; 30 yr", "eo": "Results calculated from 4 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "937": {"en": {"f": "Debt Payoff = f(deuda_total, tasa_anual, pago_mensual)", "ei": "10000 EUR; 18 %; 300 EUR", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Debt Payoff = f(deuda_total, tasa_anual, pago_mensual)", "ei": "10000 EUR; 18 %; 300 EUR", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Debt Payoff = f(deuda_total, tasa_anual, pago_mensual)", "ei": "10000 EUR; 18 %; 300 EUR", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Debt Payoff = f(deuda_total, tasa_anual, pago_mensual)", "ei": "10000 EUR; 18 %; 300 EUR", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Debt Payoff = f(deuda_total, tasa_anual, pago_mensual)", "ei": "10000 EUR; 18 %; 300 EUR", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Debt Payoff = f(deuda_total, tasa_anual, pago_mensual)", "ei": "10000 EUR; 18 %; 300 EUR", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "938": {"en": {"f": "Savings Calculator = f(ahorro_mensual, tasa_anual, anos)", "ei": "500 EUR; 7 %; 20 yr", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Savings Calculator = f(ahorro_mensual, tasa_anual, anos)", "ei": "500 EUR; 7 %; 20 yr", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Savings Calculator = f(ahorro_mensual, tasa_anual, anos)", "ei": "500 EUR; 7 %; 20 yr", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Savings Calculator = f(ahorro_mensual, tasa_anual, anos)", "ei": "500 EUR; 7 %; 20 yr", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Savings Calculator = f(ahorro_mensual, tasa_anual, anos)", "ei": "500 EUR; 7 %; 20 yr", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Savings Calculator = f(ahorro_mensual, tasa_anual, anos)", "ei": "500 EUR; 7 %; 20 yr", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "939": {"en": {"f": "Profit Margin = f(costo, precio_venta)", "ei": "50 EUR; 100 EUR", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Profit Margin = f(costo, precio_venta)", "ei": "50 EUR; 100 EUR", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Profit Margin = f(costo, precio_venta)", "ei": "50 EUR; 100 EUR", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Profit Margin = f(costo, precio_venta)", "ei": "50 EUR; 100 EUR", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Profit Margin = f(costo, precio_venta)", "ei": "50 EUR; 100 EUR", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Profit Margin = f(costo, precio_venta)", "ei": "50 EUR; 100 EUR", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "940": {"en": {"f": "Npv Calculator = f(inversion, flujo_anual, anos)", "ei": "10000 EUR; 2500 EUR; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Npv Calculator = f(inversion, flujo_anual, anos)", "ei": "10000 EUR; 2500 EUR; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Npv Calculator = f(inversion, flujo_anual, anos)", "ei": "10000 EUR; 2500 EUR; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Npv Calculator = f(inversion, flujo_anual, anos)", "ei": "10000 EUR; 2500 EUR; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Npv Calculator = f(inversion, flujo_anual, anos)", "ei": "10000 EUR; 2500 EUR; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Npv Calculator = f(inversion, flujo_anual, anos)", "ei": "10000 EUR; 2500 EUR; 5 yr", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "941": {"en": {"f": "Emergency Fund = f(gastos_mensuales, ahorro_meses)", "ei": "2000 EUR; 6 mo", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Emergency Fund = f(gastos_mensuales, ahorro_meses)", "ei": "2000 EUR; 6 mo", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Emergency Fund = f(gastos_mensuales, ahorro_meses)", "ei": "2000 EUR; 6 mo", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Emergency Fund = f(gastos_mensuales, ahorro_meses)", "ei": "2000 EUR; 6 mo", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Emergency Fund = f(gastos_mensuales, ahorro_meses)", "ei": "2000 EUR; 6 mo", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Emergency Fund = f(gastos_mensuales, ahorro_meses)", "ei": "2000 EUR; 6 mo", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "942": {"en": {"f": "Age Calculator Advanced = f(anio, mes, dia)", "ei": "1995; 6; 15", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Age Calculator Advanced = f(anio, mes, dia)", "ei": "1995; 6; 15", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Age Calculator Advanced = f(anio, mes, dia)", "ei": "1995; 6; 15", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Age Calculator Advanced = f(anio, mes, dia)", "ei": "1995; 6; 15", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Age Calculator Advanced = f(anio, mes, dia)", "ei": "1995; 6; 15", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Age Calculator Advanced = f(anio, mes, dia)", "ei": "1995; 6; 15", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "943": {"en": {"f": "Date Difference = f(anio1, mes1, dia1, anio2)", "ei": "2020; 1; 1; 2025", "eo": "Results calculated from 6 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Date Difference = f(anio1, mes1, dia1, anio2)", "ei": "2020; 1; 1; 2025", "eo": "Results calculated from 6 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Date Difference = f(anio1, mes1, dia1, anio2)", "ei": "2020; 1; 1; 2025", "eo": "Results calculated from 6 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Date Difference = f(anio1, mes1, dia1, anio2)", "ei": "2020; 1; 1; 2025", "eo": "Results calculated from 6 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Date Difference = f(anio1, mes1, dia1, anio2)", "ei": "2020; 1; 1; 2025", "eo": "Results calculated from 6 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Date Difference = f(anio1, mes1, dia1, anio2)", "ei": "2020; 1; 1; 2025", "eo": "Results calculated from 6 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "944": {"en": {"f": "Tip Calculator Advanced = f(cuenta, porcentaje, personas)", "ei": "100 EUR; 15 %; 2", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Tip Calculator Advanced = f(cuenta, porcentaje, personas)", "ei": "100 EUR; 15 %; 2", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Tip Calculator Advanced = f(cuenta, porcentaje, personas)", "ei": "100 EUR; 15 %; 2", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Tip Calculator Advanced = f(cuenta, porcentaje, personas)", "ei": "100 EUR; 15 %; 2", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Tip Calculator Advanced = f(cuenta, porcentaje, personas)", "ei": "100 EUR; 15 %; 2", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Tip Calculator Advanced = f(cuenta, porcentaje, personas)", "ei": "100 EUR; 15 %; 2", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "945": {"en": {"f": "Double Discount = f(precio_original, descuento1, descuento2)", "ei": "100 EUR; 20 %; 10 %", "eo": "Results calculated from 3 inputs", "u": ["everyday math problems", "budgeting and planning", "cooking and home measurements", "travel and time calculations"]}, "es": {"f": "Double Discount = f(precio_original, descuento1, descuento2)", "ei": "100 EUR; 20 %; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos cotidianos", "presupuesto y planificación", "cocina y mediciones del hogar", "cálculos de viaje y tiempo"]}, "fr": {"f": "Double Discount = f(precio_original, descuento1, descuento2)", "ei": "100 EUR; 20 %; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problèmes mathématiques quotidiens", "budget et planification", "cuisine et mesures domestiques", "calculs de voyage et de temps"]}, "pt": {"f": "Double Discount = f(precio_original, descuento1, descuento2)", "ei": "100 EUR; 20 %; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemas matemáticos do dia a dia", "orçamento e planejamento", "culinária e medições domésticas", "cálculos de viagem e tempo"]}, "de": {"f": "Double Discount = f(precio_original, descuento1, descuento2)", "ei": "100 EUR; 20 %; 10 %", "eo": "Results calculated from 3 inputs", "u": ["alltägliche Mathematikprobleme", "Budgetierung und Planung", "Kochen und Heimessungen", "Reise- und Zeitberechnungen"]}, "it": {"f": "Double Discount = f(precio_original, descuento1, descuento2)", "ei": "100 EUR; 20 %; 10 %", "eo": "Results calculated from 3 inputs", "u": ["problemi matematici quotidiani", "budget e pianificazione", "cucina e misurazioni domestiche", "calcoli di viaggio e tempo"]}},
    "946": {"en": {"f": "Kinetic Energy = f(masa, velocidad)", "ei": "10 kg; 5 m/s", "eo": "Results calculated from 2 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Kinetic Energy = f(masa, velocidad)", "ei": "10 kg; 5 m/s", "eo": "Results calculated from 2 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Kinetic Energy = f(masa, velocidad)", "ei": "10 kg; 5 m/s", "eo": "Results calculated from 2 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Kinetic Energy = f(masa, velocidad)", "ei": "10 kg; 5 m/s", "eo": "Results calculated from 2 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Kinetic Energy = f(masa, velocidad)", "ei": "10 kg; 5 m/s", "eo": "Results calculated from 2 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Kinetic Energy = f(masa, velocidad)", "ei": "10 kg; 5 m/s", "eo": "Results calculated from 2 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "947": {"en": {"f": "Potential Energy = f(masa, altura, gravedad)", "ei": "10 kg; 10 m; 9.81 m/s2", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Potential Energy = f(masa, altura, gravedad)", "ei": "10 kg; 10 m; 9.81 m/s2", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Potential Energy = f(masa, altura, gravedad)", "ei": "10 kg; 10 m; 9.81 m/s2", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Potential Energy = f(masa, altura, gravedad)", "ei": "10 kg; 10 m; 9.81 m/s2", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Potential Energy = f(masa, altura, gravedad)", "ei": "10 kg; 10 m; 9.81 m/s2", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Potential Energy = f(masa, altura, gravedad)", "ei": "10 kg; 10 m; 9.81 m/s2", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "948": {"en": {"f": "Work Power = f(fuerza, distancia, tiempo)", "ei": "100 N; 10 m; 5 s", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Work Power = f(fuerza, distancia, tiempo)", "ei": "100 N; 10 m; 5 s", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Work Power = f(fuerza, distancia, tiempo)", "ei": "100 N; 10 m; 5 s", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Work Power = f(fuerza, distancia, tiempo)", "ei": "100 N; 10 m; 5 s", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Work Power = f(fuerza, distancia, tiempo)", "ei": "100 N; 10 m; 5 s", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Work Power = f(fuerza, distancia, tiempo)", "ei": "100 N; 10 m; 5 s", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "949": {"en": {"f": "Ohms Law Power = f(voltaje, corriente, resistencia, potencia)", "ei": "0 V; 0 A; 0 Ohm; 0 W", "eo": "Results calculated from 4 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Ohms Law Power = f(voltaje, corriente, resistencia, potencia)", "ei": "0 V; 0 A; 0 Ohm; 0 W", "eo": "Results calculated from 4 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Ohms Law Power = f(voltaje, corriente, resistencia, potencia)", "ei": "0 V; 0 A; 0 Ohm; 0 W", "eo": "Results calculated from 4 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Ohms Law Power = f(voltaje, corriente, resistencia, potencia)", "ei": "0 V; 0 A; 0 Ohm; 0 W", "eo": "Results calculated from 4 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Ohms Law Power = f(voltaje, corriente, resistencia, potencia)", "ei": "0 V; 0 A; 0 Ohm; 0 W", "eo": "Results calculated from 4 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Ohms Law Power = f(voltaje, corriente, resistencia, potencia)", "ei": "0 V; 0 A; 0 Ohm; 0 W", "eo": "Results calculated from 4 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "950": {"en": {"f": "Newtons Second Law = f(masa, aceleracion, tiempo)", "ei": "10 kg; 2 m/s2; 5 s", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Newtons Second Law = f(masa, aceleracion, tiempo)", "ei": "10 kg; 2 m/s2; 5 s", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Newtons Second Law = f(masa, aceleracion, tiempo)", "ei": "10 kg; 2 m/s2; 5 s", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Newtons Second Law = f(masa, aceleracion, tiempo)", "ei": "10 kg; 2 m/s2; 5 s", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Newtons Second Law = f(masa, aceleracion, tiempo)", "ei": "10 kg; 2 m/s2; 5 s", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Newtons Second Law = f(masa, aceleracion, tiempo)", "ei": "10 kg; 2 m/s2; 5 s", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "951": {"en": {"f": "One Rep Max = f(peso_kg, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["training pace and performance tracking", "fitness goal planning", "sports science calculations", "competition preparation"]}, "es": {"f": "One Rep Max = f(peso_kg, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de ritmo y rendimiento de entrenamiento", "planificación de objetivos de fitness", "cálculos de ciencia del deporte", "preparación para competiciones"]}, "fr": {"f": "One Rep Max = f(peso_kg, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["suivi d'allure et de performance d'entraînement", "planification d'objectifs de fitness", "calculs de science du sport", "préparation aux compétitions"]}, "pt": {"f": "One Rep Max = f(peso_kg, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de ritmo e desempenho de treino", "planejamento de objetivos de fitness", "cálculos de ciência do esporte", "preparação para competições"]}, "de": {"f": "One Rep Max = f(peso_kg, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["Trainingspace- und Leistungs-Tracking", "Fitness-Zielplanung", "Sportwissenschaft-Berechnungen", "Wettkampfvorbereitung"]}, "it": {"f": "One Rep Max = f(peso_kg, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio dell'andatura e delle prestazioni", "pianificazione degli obiettivi di fitness", "calcoli di scienza dello sport", "preparazione alle competizioni"]}},
    "952": {"en": {"f": "Running Pace Predictor = f(distancia_km, tiempo_min)", "ei": "5 km; 25 min", "eo": "Results calculated from 2 inputs", "u": ["training pace and performance tracking", "fitness goal planning", "sports science calculations", "competition preparation"]}, "es": {"f": "Running Pace Predictor = f(distancia_km, tiempo_min)", "ei": "5 km; 25 min", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de ritmo y rendimiento de entrenamiento", "planificación de objetivos de fitness", "cálculos de ciencia del deporte", "preparación para competiciones"]}, "fr": {"f": "Running Pace Predictor = f(distancia_km, tiempo_min)", "ei": "5 km; 25 min", "eo": "Results calculated from 2 inputs", "u": ["suivi d'allure et de performance d'entraînement", "planification d'objectifs de fitness", "calculs de science du sport", "préparation aux compétitions"]}, "pt": {"f": "Running Pace Predictor = f(distancia_km, tiempo_min)", "ei": "5 km; 25 min", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de ritmo e desempenho de treino", "planejamento de objetivos de fitness", "cálculos de ciência do esporte", "preparação para competições"]}, "de": {"f": "Running Pace Predictor = f(distancia_km, tiempo_min)", "ei": "5 km; 25 min", "eo": "Results calculated from 2 inputs", "u": ["Trainingspace- und Leistungs-Tracking", "Fitness-Zielplanung", "Sportwissenschaft-Berechnungen", "Wettkampfvorbereitung"]}, "it": {"f": "Running Pace Predictor = f(distancia_km, tiempo_min)", "ei": "5 km; 25 min", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio dell'andatura e delle prestazioni", "pianificazione degli obiettivi di fitness", "calcoli di scienza dello sport", "preparazione alle competizioni"]}},
    "953": {"en": {"f": "Vo2 Max Estimator = f(edad, peso_kg, fc_reposo, duracion_min)", "ei": "30 years; 70 kg; 60 bpm; 30 min", "eo": "Results calculated from 4 inputs", "u": ["training pace and performance tracking", "fitness goal planning", "sports science calculations", "competition preparation"]}, "es": {"f": "Vo2 Max Estimator = f(edad, peso_kg, fc_reposo, duracion_min)", "ei": "30 years; 70 kg; 60 bpm; 30 min", "eo": "Results calculated from 4 inputs", "u": ["seguimiento de ritmo y rendimiento de entrenamiento", "planificación de objetivos de fitness", "cálculos de ciencia del deporte", "preparación para competiciones"]}, "fr": {"f": "Vo2 Max Estimator = f(edad, peso_kg, fc_reposo, duracion_min)", "ei": "30 years; 70 kg; 60 bpm; 30 min", "eo": "Results calculated from 4 inputs", "u": ["suivi d'allure et de performance d'entraînement", "planification d'objectifs de fitness", "calculs de science du sport", "préparation aux compétitions"]}, "pt": {"f": "Vo2 Max Estimator = f(edad, peso_kg, fc_reposo, duracion_min)", "ei": "30 years; 70 kg; 60 bpm; 30 min", "eo": "Results calculated from 4 inputs", "u": ["acompanhamento de ritmo e desempenho de treino", "planejamento de objetivos de fitness", "cálculos de ciência do esporte", "preparação para competições"]}, "de": {"f": "Vo2 Max Estimator = f(edad, peso_kg, fc_reposo, duracion_min)", "ei": "30 years; 70 kg; 60 bpm; 30 min", "eo": "Results calculated from 4 inputs", "u": ["Trainingspace- und Leistungs-Tracking", "Fitness-Zielplanung", "Sportwissenschaft-Berechnungen", "Wettkampfvorbereitung"]}, "it": {"f": "Vo2 Max Estimator = f(edad, peso_kg, fc_reposo, duracion_min)", "ei": "30 years; 70 kg; 60 bpm; 30 min", "eo": "Results calculated from 4 inputs", "u": ["monitoraggio dell'andatura e delle prestazioni", "pianificazione degli obiettivi di fitness", "calcoli di scienza dello sport", "preparazione alle competizioni"]}},
    "954": {"en": {"f": "Angle Converter = f(grados)", "ei": "45 deg", "eo": "Results calculated from 1 input", "u": ["unit conversion for travel", "recipe and cooking conversions", "engineering and science calculations", "international measurement comparisons"]}, "es": {"f": "Angle Converter = f(grados)", "ei": "45 deg", "eo": "Results calculated from 1 input", "u": ["conversión de unidades para viajes", "conversiones de recetas y cocina", "cálculos de ingeniería y ciencia", "comparaciones de medidas internacionales"]}, "fr": {"f": "Angle Converter = f(grados)", "ei": "45 deg", "eo": "Results calculated from 1 input", "u": ["conversion d'unités pour les voyages", "conversions de recettes et cuisine", "calculs d'ingénierie et de science", "comparaisons de mesures internationales"]}, "pt": {"f": "Angle Converter = f(grados)", "ei": "45 deg", "eo": "Results calculated from 1 input", "u": ["conversão de unidades para viagens", "conversões de receitas e culinária", "cálculos de engenharia e ciência", "comparações de medidas internacionais"]}, "de": {"f": "Angle Converter = f(grados)", "ei": "45 deg", "eo": "Results calculated from 1 input", "u": ["Einheitenumrechnung für Reisen", "Rezept- und Kochumrechnungen", "Ingenieur- und Wissenschaftsberechnungen", "internationale Maßvergleiche"]}, "it": {"f": "Angle Converter = f(grados)", "ei": "45 deg", "eo": "Results calculated from 1 input", "u": ["conversione di unità per viaggi", "conversioni di ricette e cucina", "calcoli ingegneristici e scientifici", "confronti di misurazioni internazionali"]}},
    "955": {"en": {"f": "Temperature Full = f(celsius)", "ei": "25 C", "eo": "Results calculated from 1 input", "u": ["unit conversion for travel", "recipe and cooking conversions", "engineering and science calculations", "international measurement comparisons"]}, "es": {"f": "Temperature Full = f(celsius)", "ei": "25 C", "eo": "Results calculated from 1 input", "u": ["conversión de unidades para viajes", "conversiones de recetas y cocina", "cálculos de ingeniería y ciencia", "comparaciones de medidas internacionales"]}, "fr": {"f": "Temperature Full = f(celsius)", "ei": "25 C", "eo": "Results calculated from 1 input", "u": ["conversion d'unités pour les voyages", "conversions de recettes et cuisine", "calculs d'ingénierie et de science", "comparaisons de mesures internationales"]}, "pt": {"f": "Temperature Full = f(celsius)", "ei": "25 C", "eo": "Results calculated from 1 input", "u": ["conversão de unidades para viagens", "conversões de receitas e culinária", "cálculos de engenharia e ciência", "comparações de medidas internacionais"]}, "de": {"f": "Temperature Full = f(celsius)", "ei": "25 C", "eo": "Results calculated from 1 input", "u": ["Einheitenumrechnung für Reisen", "Rezept- und Kochumrechnungen", "Ingenieur- und Wissenschaftsberechnungen", "internationale Maßvergleiche"]}, "it": {"f": "Temperature Full = f(celsius)", "ei": "25 C", "eo": "Results calculated from 1 input", "u": ["conversione di unità per viaggi", "conversioni di ricette e cucina", "calcoli ingegneristici e scientifici", "confronti di misurazioni internazionali"]}},
    "956": {"en": {"f": "Energy Converter = f(joules)", "ei": "100 J", "eo": "Results calculated from 1 input", "u": ["unit conversion for travel", "recipe and cooking conversions", "engineering and science calculations", "international measurement comparisons"]}, "es": {"f": "Energy Converter = f(joules)", "ei": "100 J", "eo": "Results calculated from 1 input", "u": ["conversión de unidades para viajes", "conversiones de recetas y cocina", "cálculos de ingeniería y ciencia", "comparaciones de medidas internacionales"]}, "fr": {"f": "Energy Converter = f(joules)", "ei": "100 J", "eo": "Results calculated from 1 input", "u": ["conversion d'unités pour les voyages", "conversions de recettes et cuisine", "calculs d'ingénierie et de science", "comparaisons de mesures internationales"]}, "pt": {"f": "Energy Converter = f(joules)", "ei": "100 J", "eo": "Results calculated from 1 input", "u": ["conversão de unidades para viagens", "conversões de receitas e culinária", "cálculos de engenharia e ciência", "comparações de medidas internacionais"]}, "de": {"f": "Energy Converter = f(joules)", "ei": "100 J", "eo": "Results calculated from 1 input", "u": ["Einheitenumrechnung für Reisen", "Rezept- und Kochumrechnungen", "Ingenieur- und Wissenschaftsberechnungen", "internationale Maßvergleiche"]}, "it": {"f": "Energy Converter = f(joules)", "ei": "100 J", "eo": "Results calculated from 1 input", "u": ["conversione di unità per viaggi", "conversioni di ricette e cucina", "calcoli ingegneristici e scientifici", "confronti di misurazioni internazionali"]}},
    "957": {"en": {"f": "Combinations Permutations = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["data analysis and research", "survey sample planning", "quality control and testing", "academic statistics problems"]}, "es": {"f": "Combinations Permutations = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["análisis de datos e investigación", "planificación de muestras de encuestas", "control de calidad y pruebas", "problemas de estadística académica"]}, "fr": {"f": "Combinations Permutations = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["analyse de données et recherche", "planification d'échantillons d'enquêtes", "contrôle qualité et tests", "problèmes de statistiques académiques"]}, "pt": {"f": "Combinations Permutations = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["análise de dados e pesquisa", "planejamento de amostras de pesquisas", "controle de qualidade e testes", "problemas de estatística acadêmica"]}, "de": {"f": "Combinations Permutations = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["Datenanalyse und Forschung", "Umfrage-Stichprobenplanung", "Qualitätskontrolle und Tests", "akademische Statistikprobleme"]}, "it": {"f": "Combinations Permutations = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["analisi dei dati e ricerca", "pianificazione di campioni di sondaggi", "controllo qualità e test", "problemi di statistica accademica"]}},
    "958": {"en": {"f": "Z Score Percentile = f(valor, media, desviacion)", "ei": "85; 75; 10", "eo": "Results calculated from 3 inputs", "u": ["data analysis and research", "survey sample planning", "quality control and testing", "academic statistics problems"]}, "es": {"f": "Z Score Percentile = f(valor, media, desviacion)", "ei": "85; 75; 10", "eo": "Results calculated from 3 inputs", "u": ["análisis de datos e investigación", "planificación de muestras de encuestas", "control de calidad y pruebas", "problemas de estadística académica"]}, "fr": {"f": "Z Score Percentile = f(valor, media, desviacion)", "ei": "85; 75; 10", "eo": "Results calculated from 3 inputs", "u": ["analyse de données et recherche", "planification d'échantillons d'enquêtes", "contrôle qualité et tests", "problèmes de statistiques académiques"]}, "pt": {"f": "Z Score Percentile = f(valor, media, desviacion)", "ei": "85; 75; 10", "eo": "Results calculated from 3 inputs", "u": ["análise de dados e pesquisa", "planejamento de amostras de pesquisas", "controle de qualidade e testes", "problemas de estatística acadêmica"]}, "de": {"f": "Z Score Percentile = f(valor, media, desviacion)", "ei": "85; 75; 10", "eo": "Results calculated from 3 inputs", "u": ["Datenanalyse und Forschung", "Umfrage-Stichprobenplanung", "Qualitätskontrolle und Tests", "akademische Statistikprobleme"]}, "it": {"f": "Z Score Percentile = f(valor, media, desviacion)", "ei": "85; 75; 10", "eo": "Results calculated from 3 inputs", "u": ["analisi dei dati e ricerca", "pianificazione di campioni di sondaggi", "controllo qualità e test", "problemi di statistica accademica"]}},
    "959": {"en": {"f": "Sample Size Confidence = f(tamano_muestra, proporcion, margen_error, confianza)", "ei": "100; 0.5; 0.05; 0.95", "eo": "Results calculated from 4 inputs", "u": ["data analysis and research", "survey sample planning", "quality control and testing", "academic statistics problems"]}, "es": {"f": "Sample Size Confidence = f(tamano_muestra, proporcion, margen_error, confianza)", "ei": "100; 0.5; 0.05; 0.95", "eo": "Results calculated from 4 inputs", "u": ["análisis de datos e investigación", "planificación de muestras de encuestas", "control de calidad y pruebas", "problemas de estadística académica"]}, "fr": {"f": "Sample Size Confidence = f(tamano_muestra, proporcion, margen_error, confianza)", "ei": "100; 0.5; 0.05; 0.95", "eo": "Results calculated from 4 inputs", "u": ["analyse de données et recherche", "planification d'échantillons d'enquêtes", "contrôle qualité et tests", "problèmes de statistiques académiques"]}, "pt": {"f": "Sample Size Confidence = f(tamano_muestra, proporcion, margen_error, confianza)", "ei": "100; 0.5; 0.05; 0.95", "eo": "Results calculated from 4 inputs", "u": ["análise de dados e pesquisa", "planejamento de amostras de pesquisas", "controle de qualidade e testes", "problemas de estatística acadêmica"]}, "de": {"f": "Sample Size Confidence = f(tamano_muestra, proporcion, margen_error, confianza)", "ei": "100; 0.5; 0.05; 0.95", "eo": "Results calculated from 4 inputs", "u": ["Datenanalyse und Forschung", "Umfrage-Stichprobenplanung", "Qualitätskontrolle und Tests", "akademische Statistikprobleme"]}, "it": {"f": "Sample Size Confidence = f(tamano_muestra, proporcion, margen_error, confianza)", "ei": "100; 0.5; 0.05; 0.95", "eo": "Results calculated from 4 inputs", "u": ["analisi dei dati e ricerca", "pianificazione di campioni di sondaggi", "controllo qualità e test", "problemi di statistica accademica"]}},
    "960": {"en": {"f": "Bsa Ideal Weight = f(edad, peso_kg, altura_cm, sexo)", "ei": "30 years; 70 kg; 175 cm; mujer", "eo": "Results calculated from 4 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Bsa Ideal Weight = f(edad, peso_kg, altura_cm, sexo)", "ei": "30 years; 70 kg; 175 cm; mujer", "eo": "Results calculated from 4 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Bsa Ideal Weight = f(edad, peso_kg, altura_cm, sexo)", "ei": "30 years; 70 kg; 175 cm; mujer", "eo": "Results calculated from 4 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Bsa Ideal Weight = f(edad, peso_kg, altura_cm, sexo)", "ei": "30 years; 70 kg; 175 cm; mujer", "eo": "Results calculated from 4 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Bsa Ideal Weight = f(edad, peso_kg, altura_cm, sexo)", "ei": "30 years; 70 kg; 175 cm; mujer", "eo": "Results calculated from 4 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Bsa Ideal Weight = f(edad, peso_kg, altura_cm, sexo)", "ei": "30 years; 70 kg; 175 cm; mujer", "eo": "Results calculated from 4 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "961": {"en": {"f": "A1C Estimator = f(glucosa_mgdl)", "ei": "100 mg/dL", "eo": "Results calculated from 1 input", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "A1C Estimator = f(glucosa_mgdl)", "ei": "100 mg/dL", "eo": "Results calculated from 1 input", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "A1C Estimator = f(glucosa_mgdl)", "ei": "100 mg/dL", "eo": "Results calculated from 1 input", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "A1C Estimator = f(glucosa_mgdl)", "ei": "100 mg/dL", "eo": "Results calculated from 1 input", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "A1C Estimator = f(glucosa_mgdl)", "ei": "100 mg/dL", "eo": "Results calculated from 1 input", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "A1C Estimator = f(glucosa_mgdl)", "ei": "100 mg/dL", "eo": "Results calculated from 1 input", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "962": {"en": {"f": "Cholesterol Ldl = f(colesterol_total, hdl, trigliceridos)", "ei": "200 mg/dL; 50 mg/dL; 150 mg/dL", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Cholesterol Ldl = f(colesterol_total, hdl, trigliceridos)", "ei": "200 mg/dL; 50 mg/dL; 150 mg/dL", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Cholesterol Ldl = f(colesterol_total, hdl, trigliceridos)", "ei": "200 mg/dL; 50 mg/dL; 150 mg/dL", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Cholesterol Ldl = f(colesterol_total, hdl, trigliceridos)", "ei": "200 mg/dL; 50 mg/dL; 150 mg/dL", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Cholesterol Ldl = f(colesterol_total, hdl, trigliceridos)", "ei": "200 mg/dL; 50 mg/dL; 150 mg/dL", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Cholesterol Ldl = f(colesterol_total, hdl, trigliceridos)", "ei": "200 mg/dL; 50 mg/dL; 150 mg/dL", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "1000": {"en": {"f": "Calculadora Ph = f(h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Calculadora Ph = f(h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Calculadora Ph = f(h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Calculadora Ph = f(h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Calculadora Ph = f(h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Calculadora Ph = f(h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1001": {"en": {"f": "Calculadora Poh = f(oh)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Calculadora Poh = f(oh)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Calculadora Poh = f(oh)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Calculadora Poh = f(oh)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Calculadora Poh = f(oh)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Calculadora Poh = f(oh)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1002": {"en": {"f": "Molaridad = f(moles, volume)", "ei": "1 mol; 1 L", "eo": "Results calculated from 2 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Molaridad = f(moles, volume)", "ei": "1 mol; 1 L", "eo": "Results calculated from 2 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Molaridad = f(moles, volume)", "ei": "1 mol; 1 L", "eo": "Results calculated from 2 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Molaridad = f(moles, volume)", "ei": "1 mol; 1 L", "eo": "Results calculated from 2 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Molaridad = f(moles, volume)", "ei": "1 mol; 1 L", "eo": "Results calculated from 2 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Molaridad = f(moles, volume)", "ei": "1 mol; 1 L", "eo": "Results calculated from 2 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1003": {"en": {"f": "Dilucion = f(c1, v1, c2)", "ei": "1 mol/L; 0.1 L; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Dilucion = f(c1, v1, c2)", "ei": "1 mol/L; 0.1 L; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Dilucion = f(c1, v1, c2)", "ei": "1 mol/L; 0.1 L; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Dilucion = f(c1, v1, c2)", "ei": "1 mol/L; 0.1 L; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Dilucion = f(c1, v1, c2)", "ei": "1 mol/L; 0.1 L; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Dilucion = f(c1, v1, c2)", "ei": "1 mol/L; 0.1 L; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1004": {"en": {"f": "Ley Gases Ideales = f(p, v, n, t)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Ley Gases Ideales = f(p, v, n, t)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Ley Gases Ideales = f(p, v, n, t)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Ley Gases Ideales = f(p, v, n, t)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Ley Gases Ideales = f(p, v, n, t)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Ley Gases Ideales = f(p, v, n, t)", "ei": "101325 Pa; 0.0224 m³; 1 mol; 273.15 K", "eo": "Results calculated from 4 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1005": {"en": {"f": "Ley Boyle = f(p1, v1, p2)", "ei": "1 atm; 1 L; 2 atm", "eo": "Results calculated from 3 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Ley Boyle = f(p1, v1, p2)", "ei": "1 atm; 1 L; 2 atm", "eo": "Results calculated from 3 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Ley Boyle = f(p1, v1, p2)", "ei": "1 atm; 1 L; 2 atm", "eo": "Results calculated from 3 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Ley Boyle = f(p1, v1, p2)", "ei": "1 atm; 1 L; 2 atm", "eo": "Results calculated from 3 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Ley Boyle = f(p1, v1, p2)", "ei": "1 atm; 1 L; 2 atm", "eo": "Results calculated from 3 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Ley Boyle = f(p1, v1, p2)", "ei": "1 atm; 1 L; 2 atm", "eo": "Results calculated from 3 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1006": {"en": {"f": "Ley Charles = f(v1, t1, t2)", "ei": "1 L; 273.15 K; 373.15 K", "eo": "Results calculated from 3 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Ley Charles = f(v1, t1, t2)", "ei": "1 L; 273.15 K; 373.15 K", "eo": "Results calculated from 3 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Ley Charles = f(v1, t1, t2)", "ei": "1 L; 273.15 K; 373.15 K", "eo": "Results calculated from 3 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Ley Charles = f(v1, t1, t2)", "ei": "1 L; 273.15 K; 373.15 K", "eo": "Results calculated from 3 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Ley Charles = f(v1, t1, t2)", "ei": "1 L; 273.15 K; 373.15 K", "eo": "Results calculated from 3 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Ley Charles = f(v1, t1, t2)", "ei": "1 L; 273.15 K; 373.15 K", "eo": "Results calculated from 3 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1007": {"en": {"f": "Energia Libre Gibbs = f(h, s, t)", "ei": "-100 kJ/mol; 0.2 kJ/mol·K; 298 K", "eo": "Results calculated from 3 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Energia Libre Gibbs = f(h, s, t)", "ei": "-100 kJ/mol; 0.2 kJ/mol·K; 298 K", "eo": "Results calculated from 3 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Energia Libre Gibbs = f(h, s, t)", "ei": "-100 kJ/mol; 0.2 kJ/mol·K; 298 K", "eo": "Results calculated from 3 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Energia Libre Gibbs = f(h, s, t)", "ei": "-100 kJ/mol; 0.2 kJ/mol·K; 298 K", "eo": "Results calculated from 3 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Energia Libre Gibbs = f(h, s, t)", "ei": "-100 kJ/mol; 0.2 kJ/mol·K; 298 K", "eo": "Results calculated from 3 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Energia Libre Gibbs = f(h, s, t)", "ei": "-100 kJ/mol; 0.2 kJ/mol·K; 298 K", "eo": "Results calculated from 3 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1008": {"en": {"f": "Peso Molecular = f(c, h, o)", "ei": "6 atoms; 12 atoms; 6 atoms", "eo": "Results calculated from 3 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Peso Molecular = f(c, h, o)", "ei": "6 atoms; 12 atoms; 6 atoms", "eo": "Results calculated from 3 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Peso Molecular = f(c, h, o)", "ei": "6 atoms; 12 atoms; 6 atoms", "eo": "Results calculated from 3 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Peso Molecular = f(c, h, o)", "ei": "6 atoms; 12 atoms; 6 atoms", "eo": "Results calculated from 3 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Peso Molecular = f(c, h, o)", "ei": "6 atoms; 12 atoms; 6 atoms", "eo": "Results calculated from 3 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Peso Molecular = f(c, h, o)", "ei": "6 atoms; 12 atoms; 6 atoms", "eo": "Results calculated from 3 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1009": {"en": {"f": "Titulacion = f(c_acid, v_acid, c_base)", "ei": "0.1 mol/L; 25 mL; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Titulacion = f(c_acid, v_acid, c_base)", "ei": "0.1 mol/L; 25 mL; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Titulacion = f(c_acid, v_acid, c_base)", "ei": "0.1 mol/L; 25 mL; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Titulacion = f(c_acid, v_acid, c_base)", "ei": "0.1 mol/L; 25 mL; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Titulacion = f(c_acid, v_acid, c_base)", "ei": "0.1 mol/L; 25 mL; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Titulacion = f(c_acid, v_acid, c_base)", "ei": "0.1 mol/L; 25 mL; 0.1 mol/L", "eo": "Results calculated from 3 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1010": {"en": {"f": "Divisor Tension = f(vin, r1, r2)", "ei": "12 V; 1000 Ω; 1000 Ω", "eo": "Results calculated from 3 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Divisor Tension = f(vin, r1, r2)", "ei": "12 V; 1000 Ω; 1000 Ω", "eo": "Results calculated from 3 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Divisor Tension = f(vin, r1, r2)", "ei": "12 V; 1000 Ω; 1000 Ω", "eo": "Results calculated from 3 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Divisor Tension = f(vin, r1, r2)", "ei": "12 V; 1000 Ω; 1000 Ω", "eo": "Results calculated from 3 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Divisor Tension = f(vin, r1, r2)", "ei": "12 V; 1000 Ω; 1000 Ω", "eo": "Results calculated from 3 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Divisor Tension = f(vin, r1, r2)", "ei": "12 V; 1000 Ω; 1000 Ω", "eo": "Results calculated from 3 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1011": {"en": {"f": "Resistencia Led = f(v_supply, v_f, i_f)", "ei": "5 V; 2 V; 20 mA", "eo": "Results calculated from 3 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Resistencia Led = f(v_supply, v_f, i_f)", "ei": "5 V; 2 V; 20 mA", "eo": "Results calculated from 3 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Resistencia Led = f(v_supply, v_f, i_f)", "ei": "5 V; 2 V; 20 mA", "eo": "Results calculated from 3 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Resistencia Led = f(v_supply, v_f, i_f)", "ei": "5 V; 2 V; 20 mA", "eo": "Results calculated from 3 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Resistencia Led = f(v_supply, v_f, i_f)", "ei": "5 V; 2 V; 20 mA", "eo": "Results calculated from 3 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Resistencia Led = f(v_supply, v_f, i_f)", "ei": "5 V; 2 V; 20 mA", "eo": "Results calculated from 3 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1012": {"en": {"f": "Resistencia Paralelo = f(r1, r2)", "ei": "100 Ω; 100 Ω", "eo": "Results calculated from 2 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Resistencia Paralelo = f(r1, r2)", "ei": "100 Ω; 100 Ω", "eo": "Results calculated from 2 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Resistencia Paralelo = f(r1, r2)", "ei": "100 Ω; 100 Ω", "eo": "Results calculated from 2 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Resistencia Paralelo = f(r1, r2)", "ei": "100 Ω; 100 Ω", "eo": "Results calculated from 2 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Resistencia Paralelo = f(r1, r2)", "ei": "100 Ω; 100 Ω", "eo": "Results calculated from 2 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Resistencia Paralelo = f(r1, r2)", "ei": "100 Ω; 100 Ω", "eo": "Results calculated from 2 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1013": {"en": {"f": "Energia Condensador = f(c, v)", "ei": "100 µF; 10 V", "eo": "Results calculated from 2 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Energia Condensador = f(c, v)", "ei": "100 µF; 10 V", "eo": "Results calculated from 2 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Energia Condensador = f(c, v)", "ei": "100 µF; 10 V", "eo": "Results calculated from 2 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Energia Condensador = f(c, v)", "ei": "100 µF; 10 V", "eo": "Results calculated from 2 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Energia Condensador = f(c, v)", "ei": "100 µF; 10 V", "eo": "Results calculated from 2 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Energia Condensador = f(c, v)", "ei": "100 µF; 10 V", "eo": "Results calculated from 2 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1014": {"en": {"f": "Energia Bobina = f(l, i)", "ei": "10 mH; 1 A", "eo": "Results calculated from 2 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Energia Bobina = f(l, i)", "ei": "10 mH; 1 A", "eo": "Results calculated from 2 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Energia Bobina = f(l, i)", "ei": "10 mH; 1 A", "eo": "Results calculated from 2 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Energia Bobina = f(l, i)", "ei": "10 mH; 1 A", "eo": "Results calculated from 2 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Energia Bobina = f(l, i)", "ei": "10 mH; 1 A", "eo": "Results calculated from 2 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Energia Bobina = f(l, i)", "ei": "10 mH; 1 A", "eo": "Results calculated from 2 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1015": {"en": {"f": "Relacion Transformador = f(vp, vs)", "ei": "230 V; 12 V", "eo": "Results calculated from 2 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Relacion Transformador = f(vp, vs)", "ei": "230 V; 12 V", "eo": "Results calculated from 2 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Relacion Transformador = f(vp, vs)", "ei": "230 V; 12 V", "eo": "Results calculated from 2 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Relacion Transformador = f(vp, vs)", "ei": "230 V; 12 V", "eo": "Results calculated from 2 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Relacion Transformador = f(vp, vs)", "ei": "230 V; 12 V", "eo": "Results calculated from 2 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Relacion Transformador = f(vp, vs)", "ei": "230 V; 12 V", "eo": "Results calculated from 2 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1016": {"en": {"f": "Constante Tiempo Rc = f(r, c)", "ei": "1000 Ω; 1 µF", "eo": "Results calculated from 2 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Constante Tiempo Rc = f(r, c)", "ei": "1000 Ω; 1 µF", "eo": "Results calculated from 2 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Constante Tiempo Rc = f(r, c)", "ei": "1000 Ω; 1 µF", "eo": "Results calculated from 2 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Constante Tiempo Rc = f(r, c)", "ei": "1000 Ω; 1 µF", "eo": "Results calculated from 2 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Constante Tiempo Rc = f(r, c)", "ei": "1000 Ω; 1 µF", "eo": "Results calculated from 2 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Constante Tiempo Rc = f(r, c)", "ei": "1000 Ω; 1 µF", "eo": "Results calculated from 2 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1017": {"en": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1018": {"en": {"f": "Capacitancia Serie = f(c1, c2)", "ei": "10 µF; 10 µF", "eo": "Results calculated from 2 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Capacitancia Serie = f(c1, c2)", "ei": "10 µF; 10 µF", "eo": "Results calculated from 2 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Capacitancia Serie = f(c1, c2)", "ei": "10 µF; 10 µF", "eo": "Results calculated from 2 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Capacitancia Serie = f(c1, c2)", "ei": "10 µF; 10 µF", "eo": "Results calculated from 2 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Capacitancia Serie = f(c1, c2)", "ei": "10 µF; 10 µF", "eo": "Results calculated from 2 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Capacitancia Serie = f(c1, c2)", "ei": "10 µF; 10 µF", "eo": "Results calculated from 2 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1019": {"en": {"f": "Codigo Colores Resistencia = f(band1, band2, multiplier)", "ei": "1; 0; 2", "eo": "Results calculated from 3 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Codigo Colores Resistencia = f(band1, band2, multiplier)", "ei": "1; 0; 2", "eo": "Results calculated from 3 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Codigo Colores Resistencia = f(band1, band2, multiplier)", "ei": "1; 0; 2", "eo": "Results calculated from 3 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Codigo Colores Resistencia = f(band1, band2, multiplier)", "ei": "1; 0; 2", "eo": "Results calculated from 3 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Codigo Colores Resistencia = f(band1, band2, multiplier)", "ei": "1; 0; 2", "eo": "Results calculated from 3 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Codigo Colores Resistencia = f(band1, band2, multiplier)", "ei": "1; 0; 2", "eo": "Results calculated from 3 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1020": {"en": {"f": "Punto Rocio = f(t, rh)", "ei": "20 °C; 50 %", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Punto Rocio = f(t, rh)", "ei": "20 °C; 50 %", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Punto Rocio = f(t, rh)", "ei": "20 °C; 50 %", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Punto Rocio = f(t, rh)", "ei": "20 °C; 50 %", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Punto Rocio = f(t, rh)", "ei": "20 °C; 50 %", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Punto Rocio = f(t, rh)", "ei": "20 °C; 50 %", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1021": {"en": {"f": "Indice Calor = f(t, rh)", "ei": "30 °C; 70 %", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Indice Calor = f(t, rh)", "ei": "30 °C; 70 %", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Indice Calor = f(t, rh)", "ei": "30 °C; 70 %", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Indice Calor = f(t, rh)", "ei": "30 °C; 70 %", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Indice Calor = f(t, rh)", "ei": "30 °C; 70 %", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Indice Calor = f(t, rh)", "ei": "30 °C; 70 %", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1022": {"en": {"f": "Sensacion Termica Viento = f(t, v)", "ei": "-5 °C; 20 km/h", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Sensacion Termica Viento = f(t, v)", "ei": "-5 °C; 20 km/h", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Sensacion Termica Viento = f(t, v)", "ei": "-5 °C; 20 km/h", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Sensacion Termica Viento = f(t, v)", "ei": "-5 °C; 20 km/h", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Sensacion Termica Viento = f(t, v)", "ei": "-5 °C; 20 km/h", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Sensacion Termica Viento = f(t, v)", "ei": "-5 °C; 20 km/h", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1023": {"en": {"f": "Humedad Relativa = f(t, dp)", "ei": "20 °C; 10 °C", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Humedad Relativa = f(t, dp)", "ei": "20 °C; 10 °C", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Humedad Relativa = f(t, dp)", "ei": "20 °C; 10 °C", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Humedad Relativa = f(t, dp)", "ei": "20 °C; 10 °C", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Humedad Relativa = f(t, dp)", "ei": "20 °C; 10 °C", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Humedad Relativa = f(t, dp)", "ei": "20 °C; 10 °C", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1024": {"en": {"f": "Indice Calidad Aire = f(pm25)", "ei": "12 µg/m³", "eo": "Results calculated from 1 input", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Indice Calidad Aire = f(pm25)", "ei": "12 µg/m³", "eo": "Results calculated from 1 input", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Indice Calidad Aire = f(pm25)", "ei": "12 µg/m³", "eo": "Results calculated from 1 input", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Indice Calidad Aire = f(pm25)", "ei": "12 µg/m³", "eo": "Results calculated from 1 input", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Indice Calidad Aire = f(pm25)", "ei": "12 µg/m³", "eo": "Results calculated from 1 input", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Indice Calidad Aire = f(pm25)", "ei": "12 µg/m³", "eo": "Results calculated from 1 input", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1025": {"en": {"f": "Amanecer Atardecer = f(lat, day)", "ei": "40 °; 172 day", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Amanecer Atardecer = f(lat, day)", "ei": "40 °; 172 day", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Amanecer Atardecer = f(lat, day)", "ei": "40 °; 172 day", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Amanecer Atardecer = f(lat, day)", "ei": "40 °; 172 day", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Amanecer Atardecer = f(lat, day)", "ei": "40 °; 172 day", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Amanecer Atardecer = f(lat, day)", "ei": "40 °; 172 day", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1026": {"en": {"f": "Tiempo Exposicion Uv = f(uvi, spf)", "ei": "6; 30", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Tiempo Exposicion Uv = f(uvi, spf)", "ei": "6; 30", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Tiempo Exposicion Uv = f(uvi, spf)", "ei": "6; 30", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Tiempo Exposicion Uv = f(uvi, spf)", "ei": "6; 30", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Tiempo Exposicion Uv = f(uvi, spf)", "ei": "6; 30", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Tiempo Exposicion Uv = f(uvi, spf)", "ei": "6; 30", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1027": {"en": {"f": "Altitud Presion = f(p)", "ei": "1013 hPa", "eo": "Results calculated from 1 input", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Altitud Presion = f(p)", "ei": "1013 hPa", "eo": "Results calculated from 1 input", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Altitud Presion = f(p)", "ei": "1013 hPa", "eo": "Results calculated from 1 input", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Altitud Presion = f(p)", "ei": "1013 hPa", "eo": "Results calculated from 1 input", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Altitud Presion = f(p)", "ei": "1013 hPa", "eo": "Results calculated from 1 input", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Altitud Presion = f(p)", "ei": "1013 hPa", "eo": "Results calculated from 1 input", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1028": {"en": {"f": "Volumen Lluvia = f(area, rain)", "ei": "100 m²; 10 mm", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Volumen Lluvia = f(area, rain)", "ei": "100 m²; 10 mm", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Volumen Lluvia = f(area, rain)", "ei": "100 m²; 10 mm", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Volumen Lluvia = f(area, rain)", "ei": "100 m²; 10 mm", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Volumen Lluvia = f(area, rain)", "ei": "100 m²; 10 mm", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Volumen Lluvia = f(area, rain)", "ei": "100 m²; 10 mm", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1029": {"en": {"f": "Evapotranspiracion = f(temp, rh, wind)", "ei": "25 °C; 50 %; 2 m/s", "eo": "Results calculated from 3 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Evapotranspiracion = f(temp, rh, wind)", "ei": "25 °C; 50 %; 2 m/s", "eo": "Results calculated from 3 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Evapotranspiracion = f(temp, rh, wind)", "ei": "25 °C; 50 %; 2 m/s", "eo": "Results calculated from 3 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Evapotranspiracion = f(temp, rh, wind)", "ei": "25 °C; 50 %; 2 m/s", "eo": "Results calculated from 3 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Evapotranspiracion = f(temp, rh, wind)", "ei": "25 °C; 50 %; 2 m/s", "eo": "Results calculated from 3 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Evapotranspiracion = f(temp, rh, wind)", "ei": "25 °C; 50 %; 2 m/s", "eo": "Results calculated from 3 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1030": {"en": {"f": "Dia Del Ano = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Dia Del Ano = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Dia Del Ano = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Dia Del Ano = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Dia Del Ano = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Dia Del Ano = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1031": {"en": {"f": "Numero Semana = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Numero Semana = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Numero Semana = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Numero Semana = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Numero Semana = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Numero Semana = f(month, day)", "ei": "1; 1", "eo": "Results calculated from 2 inputs", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1032": {"en": {"f": "Edad En Dias = f(birth)", "ei": "", "eo": "Results calculated from 1 input", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Edad En Dias = f(birth)", "ei": "", "eo": "Results calculated from 1 input", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Edad En Dias = f(birth)", "ei": "", "eo": "Results calculated from 1 input", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Edad En Dias = f(birth)", "ei": "", "eo": "Results calculated from 1 input", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Edad En Dias = f(birth)", "ei": "", "eo": "Results calculated from 1 input", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Edad En Dias = f(birth)", "ei": "", "eo": "Results calculated from 1 input", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1033": {"en": {"f": "Tiempo Lectura = f(words, wpm)", "ei": "500 words; 200 wpm", "eo": "Results calculated from 2 inputs", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Tiempo Lectura = f(words, wpm)", "ei": "500 words; 200 wpm", "eo": "Results calculated from 2 inputs", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Tiempo Lectura = f(words, wpm)", "ei": "500 words; 200 wpm", "eo": "Results calculated from 2 inputs", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Tiempo Lectura = f(words, wpm)", "ei": "500 words; 200 wpm", "eo": "Results calculated from 2 inputs", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Tiempo Lectura = f(words, wpm)", "ei": "500 words; 200 wpm", "eo": "Results calculated from 2 inputs", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Tiempo Lectura = f(words, wpm)", "ei": "500 words; 200 wpm", "eo": "Results calculated from 2 inputs", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1034": {"en": {"f": "Generador Contrasenas = f(length)", "ei": "16 chars", "eo": "Results calculated from 1 input", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Generador Contrasenas = f(length)", "ei": "16 chars", "eo": "Results calculated from 1 input", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Generador Contrasenas = f(length)", "ei": "16 chars", "eo": "Results calculated from 1 input", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Generador Contrasenas = f(length)", "ei": "16 chars", "eo": "Results calculated from 1 input", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Generador Contrasenas = f(length)", "ei": "16 chars", "eo": "Results calculated from 1 input", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Generador Contrasenas = f(length)", "ei": "16 chars", "eo": "Results calculated from 1 input", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1035": {"en": {"f": "Numero Aleatorio = f(min, max)", "ei": "1; 100", "eo": "Results calculated from 2 inputs", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Numero Aleatorio = f(min, max)", "ei": "1; 100", "eo": "Results calculated from 2 inputs", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Numero Aleatorio = f(min, max)", "ei": "1; 100", "eo": "Results calculated from 2 inputs", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Numero Aleatorio = f(min, max)", "ei": "1; 100", "eo": "Results calculated from 2 inputs", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Numero Aleatorio = f(min, max)", "ei": "1; 100", "eo": "Results calculated from 2 inputs", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Numero Aleatorio = f(min, max)", "ei": "1; 100", "eo": "Results calculated from 2 inputs", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1036": {"en": {"f": "Lanzador Dados = f(dice, sides)", "ei": "2 dice; 6 sides", "eo": "Results calculated from 2 inputs", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Lanzador Dados = f(dice, sides)", "ei": "2 dice; 6 sides", "eo": "Results calculated from 2 inputs", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Lanzador Dados = f(dice, sides)", "ei": "2 dice; 6 sides", "eo": "Results calculated from 2 inputs", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Lanzador Dados = f(dice, sides)", "ei": "2 dice; 6 sides", "eo": "Results calculated from 2 inputs", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Lanzador Dados = f(dice, sides)", "ei": "2 dice; 6 sides", "eo": "Results calculated from 2 inputs", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Lanzador Dados = f(dice, sides)", "ei": "2 dice; 6 sides", "eo": "Results calculated from 2 inputs", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1037": {"en": {"f": "Cara Cruz = f(flips)", "ei": "1 flips", "eo": "Results calculated from 1 input", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Cara Cruz = f(flips)", "ei": "1 flips", "eo": "Results calculated from 1 input", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Cara Cruz = f(flips)", "ei": "1 flips", "eo": "Results calculated from 1 input", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Cara Cruz = f(flips)", "ei": "1 flips", "eo": "Results calculated from 1 input", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Cara Cruz = f(flips)", "ei": "1 flips", "eo": "Results calculated from 1 input", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Cara Cruz = f(flips)", "ei": "1 flips", "eo": "Results calculated from 1 input", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1038": {"en": {"f": "Hex A Rgb = f(hex)", "ei": "#FF5733", "eo": "Results calculated from 1 input", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Hex A Rgb = f(hex)", "ei": "#FF5733", "eo": "Results calculated from 1 input", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Hex A Rgb = f(hex)", "ei": "#FF5733", "eo": "Results calculated from 1 input", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Hex A Rgb = f(hex)", "ei": "#FF5733", "eo": "Results calculated from 1 input", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Hex A Rgb = f(hex)", "ei": "#FF5733", "eo": "Results calculated from 1 input", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Hex A Rgb = f(hex)", "ei": "#FF5733", "eo": "Results calculated from 1 input", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1039": {"en": {"f": "Valor Exposicion = f(aperture, shutter, iso)", "ei": "2.8 f/; 125 1/s; 100 ISO", "eo": "Results calculated from 3 inputs", "u": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"]}, "es": {"f": "Valor Exposicion = f(aperture, shutter, iso)", "ei": "2.8 f/; 125 1/s; 100 ISO", "eo": "Results calculated from 3 inputs", "u": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"]}, "fr": {"f": "Valor Exposicion = f(aperture, shutter, iso)", "ei": "2.8 f/; 125 1/s; 100 ISO", "eo": "Results calculated from 3 inputs", "u": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"]}, "pt": {"f": "Valor Exposicion = f(aperture, shutter, iso)", "ei": "2.8 f/; 125 1/s; 100 ISO", "eo": "Results calculated from 3 inputs", "u": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"]}, "de": {"f": "Valor Exposicion = f(aperture, shutter, iso)", "ei": "2.8 f/; 125 1/s; 100 ISO", "eo": "Results calculated from 3 inputs", "u": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"]}, "it": {"f": "Valor Exposicion = f(aperture, shutter, iso)", "ei": "2.8 f/; 125 1/s; 100 ISO", "eo": "Results calculated from 3 inputs", "u": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"]}},
    "1040": {"en": {"f": "Profundidad Campo = f(focal, aperture, distance, coc)", "ei": "50 mm; 2.8 f/; 3 m; 0.03 mm", "eo": "Results calculated from 4 inputs", "u": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"]}, "es": {"f": "Profundidad Campo = f(focal, aperture, distance, coc)", "ei": "50 mm; 2.8 f/; 3 m; 0.03 mm", "eo": "Results calculated from 4 inputs", "u": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"]}, "fr": {"f": "Profundidad Campo = f(focal, aperture, distance, coc)", "ei": "50 mm; 2.8 f/; 3 m; 0.03 mm", "eo": "Results calculated from 4 inputs", "u": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"]}, "pt": {"f": "Profundidad Campo = f(focal, aperture, distance, coc)", "ei": "50 mm; 2.8 f/; 3 m; 0.03 mm", "eo": "Results calculated from 4 inputs", "u": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"]}, "de": {"f": "Profundidad Campo = f(focal, aperture, distance, coc)", "ei": "50 mm; 2.8 f/; 3 m; 0.03 mm", "eo": "Results calculated from 4 inputs", "u": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"]}, "it": {"f": "Profundidad Campo = f(focal, aperture, distance, coc)", "ei": "50 mm; 2.8 f/; 3 m; 0.03 mm", "eo": "Results calculated from 4 inputs", "u": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"]}},
    "1041": {"en": {"f": "Distancia Hiperfocal = f(focal, aperture, coc)", "ei": "35 mm; 8 f/; 0.03 mm", "eo": "Results calculated from 3 inputs", "u": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"]}, "es": {"f": "Distancia Hiperfocal = f(focal, aperture, coc)", "ei": "35 mm; 8 f/; 0.03 mm", "eo": "Results calculated from 3 inputs", "u": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"]}, "fr": {"f": "Distancia Hiperfocal = f(focal, aperture, coc)", "ei": "35 mm; 8 f/; 0.03 mm", "eo": "Results calculated from 3 inputs", "u": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"]}, "pt": {"f": "Distancia Hiperfocal = f(focal, aperture, coc)", "ei": "35 mm; 8 f/; 0.03 mm", "eo": "Results calculated from 3 inputs", "u": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"]}, "de": {"f": "Distancia Hiperfocal = f(focal, aperture, coc)", "ei": "35 mm; 8 f/; 0.03 mm", "eo": "Results calculated from 3 inputs", "u": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"]}, "it": {"f": "Distancia Hiperfocal = f(focal, aperture, coc)", "ei": "35 mm; 8 f/; 0.03 mm", "eo": "Results calculated from 3 inputs", "u": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"]}},
    "1042": {"en": {"f": "Suma Decibelios = f(db1, db2)", "ei": "60 dB; 60 dB", "eo": "Results calculated from 2 inputs", "u": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"]}, "es": {"f": "Suma Decibelios = f(db1, db2)", "ei": "60 dB; 60 dB", "eo": "Results calculated from 2 inputs", "u": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"]}, "fr": {"f": "Suma Decibelios = f(db1, db2)", "ei": "60 dB; 60 dB", "eo": "Results calculated from 2 inputs", "u": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"]}, "pt": {"f": "Suma Decibelios = f(db1, db2)", "ei": "60 dB; 60 dB", "eo": "Results calculated from 2 inputs", "u": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"]}, "de": {"f": "Suma Decibelios = f(db1, db2)", "ei": "60 dB; 60 dB", "eo": "Results calculated from 2 inputs", "u": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"]}, "it": {"f": "Suma Decibelios = f(db1, db2)", "ei": "60 dB; 60 dB", "eo": "Results calculated from 2 inputs", "u": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"]}},
    "1043": {"en": {"f": "Nivel Sonoro Distancia = f(spl1, d1, d2)", "ei": "80 dB; 1 m; 10 m", "eo": "Results calculated from 3 inputs", "u": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"]}, "es": {"f": "Nivel Sonoro Distancia = f(spl1, d1, d2)", "ei": "80 dB; 1 m; 10 m", "eo": "Results calculated from 3 inputs", "u": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"]}, "fr": {"f": "Nivel Sonoro Distancia = f(spl1, d1, d2)", "ei": "80 dB; 1 m; 10 m", "eo": "Results calculated from 3 inputs", "u": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"]}, "pt": {"f": "Nivel Sonoro Distancia = f(spl1, d1, d2)", "ei": "80 dB; 1 m; 10 m", "eo": "Results calculated from 3 inputs", "u": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"]}, "de": {"f": "Nivel Sonoro Distancia = f(spl1, d1, d2)", "ei": "80 dB; 1 m; 10 m", "eo": "Results calculated from 3 inputs", "u": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"]}, "it": {"f": "Nivel Sonoro Distancia = f(spl1, d1, d2)", "ei": "80 dB; 1 m; 10 m", "eo": "Results calculated from 3 inputs", "u": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"]}},
    "1044": {"en": {"f": "Relacion Contraste = f(l1, l2)", "ei": "255; 0", "eo": "Results calculated from 2 inputs", "u": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"]}, "es": {"f": "Relacion Contraste = f(l1, l2)", "ei": "255; 0", "eo": "Results calculated from 2 inputs", "u": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"]}, "fr": {"f": "Relacion Contraste = f(l1, l2)", "ei": "255; 0", "eo": "Results calculated from 2 inputs", "u": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"]}, "pt": {"f": "Relacion Contraste = f(l1, l2)", "ei": "255; 0", "eo": "Results calculated from 2 inputs", "u": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"]}, "de": {"f": "Relacion Contraste = f(l1, l2)", "ei": "255; 0", "eo": "Results calculated from 2 inputs", "u": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"]}, "it": {"f": "Relacion Contraste = f(l1, l2)", "ei": "255; 0", "eo": "Results calculated from 2 inputs", "u": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"]}},
    "1045": {"en": {"f": "Viento Cruzado = f(wind_dir, runway, wind_speed)", "ei": "270 deg; 360 deg; 20 kt", "eo": "Results calculated from 3 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Viento Cruzado = f(wind_dir, runway, wind_speed)", "ei": "270 deg; 360 deg; 20 kt", "eo": "Results calculated from 3 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Viento Cruzado = f(wind_dir, runway, wind_speed)", "ei": "270 deg; 360 deg; 20 kt", "eo": "Results calculated from 3 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Viento Cruzado = f(wind_dir, runway, wind_speed)", "ei": "270 deg; 360 deg; 20 kt", "eo": "Results calculated from 3 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Viento Cruzado = f(wind_dir, runway, wind_speed)", "ei": "270 deg; 360 deg; 20 kt", "eo": "Results calculated from 3 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Viento Cruzado = f(wind_dir, runway, wind_speed)", "ei": "270 deg; 360 deg; 20 kt", "eo": "Results calculated from 3 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1046": {"en": {"f": "Consumo Combustible = f(flow, time)", "ei": "10 gal/h; 2 h", "eo": "Results calculated from 2 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Consumo Combustible = f(flow, time)", "ei": "10 gal/h; 2 h", "eo": "Results calculated from 2 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Consumo Combustible = f(flow, time)", "ei": "10 gal/h; 2 h", "eo": "Results calculated from 2 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Consumo Combustible = f(flow, time)", "ei": "10 gal/h; 2 h", "eo": "Results calculated from 2 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Consumo Combustible = f(flow, time)", "ei": "10 gal/h; 2 h", "eo": "Results calculated from 2 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Consumo Combustible = f(flow, time)", "ei": "10 gal/h; 2 h", "eo": "Results calculated from 2 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1047": {"en": {"f": "Velocidad Verdadera = f(ias, altitude, temp)", "ei": "120 kt; 5000 ft; 5 °C", "eo": "Results calculated from 3 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Velocidad Verdadera = f(ias, altitude, temp)", "ei": "120 kt; 5000 ft; 5 °C", "eo": "Results calculated from 3 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Velocidad Verdadera = f(ias, altitude, temp)", "ei": "120 kt; 5000 ft; 5 °C", "eo": "Results calculated from 3 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Velocidad Verdadera = f(ias, altitude, temp)", "ei": "120 kt; 5000 ft; 5 °C", "eo": "Results calculated from 3 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Velocidad Verdadera = f(ias, altitude, temp)", "ei": "120 kt; 5000 ft; 5 °C", "eo": "Results calculated from 3 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Velocidad Verdadera = f(ias, altitude, temp)", "ei": "120 kt; 5000 ft; 5 °C", "eo": "Results calculated from 3 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1048": {"en": {"f": "Velocidad Casco = f(loa)", "ei": "10 m", "eo": "Results calculated from 1 input", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Velocidad Casco = f(loa)", "ei": "10 m", "eo": "Results calculated from 1 input", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Velocidad Casco = f(loa)", "ei": "10 m", "eo": "Results calculated from 1 input", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Velocidad Casco = f(loa)", "ei": "10 m", "eo": "Results calculated from 1 input", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Velocidad Casco = f(loa)", "ei": "10 m", "eo": "Results calculated from 1 input", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Velocidad Casco = f(loa)", "ei": "10 m", "eo": "Results calculated from 1 input", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1049": {"en": {"f": "Distancia Ortodromica = f(lat1, lon1, lat2, lon2)", "ei": "40 deg; -74 deg; 51 deg; -0.1 deg", "eo": "Results calculated from 4 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Distancia Ortodromica = f(lat1, lon1, lat2, lon2)", "ei": "40 deg; -74 deg; 51 deg; -0.1 deg", "eo": "Results calculated from 4 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Distancia Ortodromica = f(lat1, lon1, lat2, lon2)", "ei": "40 deg; -74 deg; 51 deg; -0.1 deg", "eo": "Results calculated from 4 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Distancia Ortodromica = f(lat1, lon1, lat2, lon2)", "ei": "40 deg; -74 deg; 51 deg; -0.1 deg", "eo": "Results calculated from 4 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Distancia Ortodromica = f(lat1, lon1, lat2, lon2)", "ei": "40 deg; -74 deg; 51 deg; -0.1 deg", "eo": "Results calculated from 4 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Distancia Ortodromica = f(lat1, lon1, lat2, lon2)", "ei": "40 deg; -74 deg; 51 deg; -0.1 deg", "eo": "Results calculated from 4 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1050": {"en": {"f": "Poligono Regular Area = f(n, lado)", "ei": "6; 10 m", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Poligono Regular Area = f(n, lado)", "ei": "6; 10 m", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Poligono Regular Area = f(n, lado)", "ei": "6; 10 m", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Poligono Regular Area = f(n, lado)", "ei": "6; 10 m", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Poligono Regular Area = f(n, lado)", "ei": "6; 10 m", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Poligono Regular Area = f(n, lado)", "ei": "6; 10 m", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "1051": {"en": {"f": "Cono Volumen = f(radio, altura)", "ei": "5 m; 10 m", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Cono Volumen = f(radio, altura)", "ei": "5 m; 10 m", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Cono Volumen = f(radio, altura)", "ei": "5 m; 10 m", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Cono Volumen = f(radio, altura)", "ei": "5 m; 10 m", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Cono Volumen = f(radio, altura)", "ei": "5 m; 10 m", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Cono Volumen = f(radio, altura)", "ei": "5 m; 10 m", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "1052": {"en": {"f": "Suma Aritmetica = f(a1, d, n)", "ei": "1; 1; 10", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Suma Aritmetica = f(a1, d, n)", "ei": "1; 1; 10", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Suma Aritmetica = f(a1, d, n)", "ei": "1; 1; 10", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Suma Aritmetica = f(a1, d, n)", "ei": "1; 1; 10", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Suma Aritmetica = f(a1, d, n)", "ei": "1; 1; 10", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Suma Aritmetica = f(a1, d, n)", "ei": "1; 1; 10", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "1053": {"en": {"f": "Suma Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Suma Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Suma Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Suma Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Suma Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Suma Geometrica = f(a1, r, n)", "ei": "1; 2; 10", "eo": "Results calculated from 3 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "1054": {"en": {"f": "Combinaciones = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["homework and exam preparation", "engineering and scientific calculations", "financial modeling and analysis", "everyday math problems"]}, "es": {"f": "Combinaciones = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["preparación de tareas y exámenes", "cálculos de ingeniería y ciencia", "modelado y análisis financiero", "problemas matemáticos cotidianos"]}, "fr": {"f": "Combinaciones = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["préparation aux devoirs et examens", "calculs d'ingénierie et scientifiques", "modélisation et analyse financière", "problèmes mathématiques quotidiens"]}, "pt": {"f": "Combinaciones = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["preparação para tarefas e exames", "cálculos de engenharia e ciência", "modelagem e análise financeira", "problemas matemáticos diários"]}, "de": {"f": "Combinaciones = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["Hausaufgaben- und Prüfungsvorbereitung", "Ingenieur- und Wissenschaftsberechnungen", "finanzielle Modellierung und Analyse", "alltägliche Mathematikprobleme"]}, "it": {"f": "Combinaciones = f(n, r)", "ei": "10; 3", "eo": "Results calculated from 2 inputs", "u": ["preparazione per compiti ed esami", "calcoli ingegneristici e scientifici", "modellazione e analisi finanziaria", "problemi matematici quotidiani"]}},
    "1055": {"en": {"f": "Empuje Arquimedes = f(densidad_fluido, volumen, masa)", "ei": "1000 kg/m³; 0.1 m³; 50 kg", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Empuje Arquimedes = f(densidad_fluido, volumen, masa)", "ei": "1000 kg/m³; 0.1 m³; 50 kg", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Empuje Arquimedes = f(densidad_fluido, volumen, masa)", "ei": "1000 kg/m³; 0.1 m³; 50 kg", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Empuje Arquimedes = f(densidad_fluido, volumen, masa)", "ei": "1000 kg/m³; 0.1 m³; 50 kg", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Empuje Arquimedes = f(densidad_fluido, volumen, masa)", "ei": "1000 kg/m³; 0.1 m³; 50 kg", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Empuje Arquimedes = f(densidad_fluido, volumen, masa)", "ei": "1000 kg/m³; 0.1 m³; 50 kg", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "1056": {"en": {"f": "Efecto Doppler = f(frecuente, velocidad_sonido, velocidad_fuente, velocidad_observador)", "ei": "440 Hz; 343 m/s; 30 m/s; 0 m/s", "eo": "Results calculated from 4 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Efecto Doppler = f(frecuente, velocidad_sonido, velocidad_fuente, velocidad_observador)", "ei": "440 Hz; 343 m/s; 30 m/s; 0 m/s", "eo": "Results calculated from 4 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Efecto Doppler = f(frecuente, velocidad_sonido, velocidad_fuente, velocidad_observador)", "ei": "440 Hz; 343 m/s; 30 m/s; 0 m/s", "eo": "Results calculated from 4 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Efecto Doppler = f(frecuente, velocidad_sonido, velocidad_fuente, velocidad_observador)", "ei": "440 Hz; 343 m/s; 30 m/s; 0 m/s", "eo": "Results calculated from 4 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Efecto Doppler = f(frecuente, velocidad_sonido, velocidad_fuente, velocidad_observador)", "ei": "440 Hz; 343 m/s; 30 m/s; 0 m/s", "eo": "Results calculated from 4 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Efecto Doppler = f(frecuente, velocidad_sonido, velocidad_fuente, velocidad_observador)", "ei": "440 Hz; 343 m/s; 30 m/s; 0 m/s", "eo": "Results calculated from 4 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "1057": {"en": {"f": "Impedancia Ac = f(resistencia, inductancia, capacitancia, frecuencia)", "ei": "10 Ω; 0.1 H; 100 μF; 60 Hz", "eo": "Results calculated from 4 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Impedancia Ac = f(resistencia, inductancia, capacitancia, frecuencia)", "ei": "10 Ω; 0.1 H; 100 μF; 60 Hz", "eo": "Results calculated from 4 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Impedancia Ac = f(resistencia, inductancia, capacitancia, frecuencia)", "ei": "10 Ω; 0.1 H; 100 μF; 60 Hz", "eo": "Results calculated from 4 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Impedancia Ac = f(resistencia, inductancia, capacitancia, frecuencia)", "ei": "10 Ω; 0.1 H; 100 μF; 60 Hz", "eo": "Results calculated from 4 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Impedancia Ac = f(resistencia, inductancia, capacitancia, frecuencia)", "ei": "10 Ω; 0.1 H; 100 μF; 60 Hz", "eo": "Results calculated from 4 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Impedancia Ac = f(resistencia, inductancia, capacitancia, frecuencia)", "ei": "10 Ω; 0.1 H; 100 μF; 60 Hz", "eo": "Results calculated from 4 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "1058": {"en": {"f": "Momento Inercia = f(masa, radio)", "ei": "10 kg; 0.5 m", "eo": "Results calculated from 2 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Momento Inercia = f(masa, radio)", "ei": "10 kg; 0.5 m", "eo": "Results calculated from 2 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Momento Inercia = f(masa, radio)", "ei": "10 kg; 0.5 m", "eo": "Results calculated from 2 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Momento Inercia = f(masa, radio)", "ei": "10 kg; 0.5 m", "eo": "Results calculated from 2 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Momento Inercia = f(masa, radio)", "ei": "10 kg; 0.5 m", "eo": "Results calculated from 2 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Momento Inercia = f(masa, radio)", "ei": "10 kg; 0.5 m", "eo": "Results calculated from 2 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "1059": {"en": {"f": "Energia Rotacional = f(momento_inercia, velocidad_angular, radio)", "ei": "2.5 kg·m²; 10 rad/s; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["physics and chemistry homework", "engineering problem-solving", "scientific research calculations", "lab experiment verification"]}, "es": {"f": "Energia Rotacional = f(momento_inercia, velocidad_angular, radio)", "ei": "2.5 kg·m²; 10 rad/s; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["tareas de física y química", "resolución de problemas de ingeniería", "cálculos de investigación científica", "verificación de experimentos de laboratorio"]}, "fr": {"f": "Energia Rotacional = f(momento_inercia, velocidad_angular, radio)", "ei": "2.5 kg·m²; 10 rad/s; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["devoirs de physique et chimie", "résolution de problèmes d'ingénierie", "calculs de recherche scientifique", "vérification d'expériences de laboratoire"]}, "pt": {"f": "Energia Rotacional = f(momento_inercia, velocidad_angular, radio)", "ei": "2.5 kg·m²; 10 rad/s; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["tarefas de física e química", "resolução de problemas de engenharia", "cálculos de pesquisa científica", "verificação de experimentos de laboratório"]}, "de": {"f": "Energia Rotacional = f(momento_inercia, velocidad_angular, radio)", "ei": "2.5 kg·m²; 10 rad/s; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["Physik- und Chemiehausaufgaben", "Ingenieur-Problemlösung", "wissenschaftliche Forschungsberechnungen", "Laborexperiment-Verifizierung"]}, "it": {"f": "Energia Rotacional = f(momento_inercia, velocidad_angular, radio)", "ei": "2.5 kg·m²; 10 rad/s; 0.5 m", "eo": "Results calculated from 3 inputs", "u": ["compiti di fisica e chimica", "risoluzione di problemi ingegneristici", "calcoli di ricerca scientifica", "verifica di esperimenti di laboratorio"]}},
    "1060": {"en": {"f": "Grasa Corporal Marina = f(cintura, cuello, altura_cm, sexo)", "ei": "80 cm; 35 cm; 170 cm; 10", "eo": "Results calculated from 5 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Grasa Corporal Marina = f(cintura, cuello, altura_cm, sexo)", "ei": "80 cm; 35 cm; 170 cm; 10", "eo": "Results calculated from 5 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Grasa Corporal Marina = f(cintura, cuello, altura_cm, sexo)", "ei": "80 cm; 35 cm; 170 cm; 10", "eo": "Results calculated from 5 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Grasa Corporal Marina = f(cintura, cuello, altura_cm, sexo)", "ei": "80 cm; 35 cm; 170 cm; 10", "eo": "Results calculated from 5 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Grasa Corporal Marina = f(cintura, cuello, altura_cm, sexo)", "ei": "80 cm; 35 cm; 170 cm; 10", "eo": "Results calculated from 5 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Grasa Corporal Marina = f(cintura, cuello, altura_cm, sexo)", "ei": "80 cm; 35 cm; 170 cm; 10", "eo": "Results calculated from 5 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "1061": {"en": {"f": "Tasa Metabolica Mifflin = f(peso, altura_cm, edad, sexo)", "ei": "70 kg; 170 cm; 30 años; 10", "eo": "Results calculated from 4 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Tasa Metabolica Mifflin = f(peso, altura_cm, edad, sexo)", "ei": "70 kg; 170 cm; 30 años; 10", "eo": "Results calculated from 4 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Tasa Metabolica Mifflin = f(peso, altura_cm, edad, sexo)", "ei": "70 kg; 170 cm; 30 años; 10", "eo": "Results calculated from 4 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Tasa Metabolica Mifflin = f(peso, altura_cm, edad, sexo)", "ei": "70 kg; 170 cm; 30 años; 10", "eo": "Results calculated from 4 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Tasa Metabolica Mifflin = f(peso, altura_cm, edad, sexo)", "ei": "70 kg; 170 cm; 30 años; 10", "eo": "Results calculated from 4 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Tasa Metabolica Mifflin = f(peso, altura_cm, edad, sexo)", "ei": "70 kg; 170 cm; 30 años; 10", "eo": "Results calculated from 4 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "1062": {"en": {"f": "Agua Diaria = f(peso, tiempo_ejercicio, temperatura)", "ei": "70 kg; 30 min; 20 °C", "eo": "Results calculated from 3 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Agua Diaria = f(peso, tiempo_ejercicio, temperatura)", "ei": "70 kg; 30 min; 20 °C", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Agua Diaria = f(peso, tiempo_ejercicio, temperatura)", "ei": "70 kg; 30 min; 20 °C", "eo": "Results calculated from 3 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Agua Diaria = f(peso, tiempo_ejercicio, temperatura)", "ei": "70 kg; 30 min; 20 °C", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Agua Diaria = f(peso, tiempo_ejercicio, temperatura)", "ei": "70 kg; 30 min; 20 °C", "eo": "Results calculated from 3 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Agua Diaria = f(peso, tiempo_ejercicio, temperatura)", "ei": "70 kg; 30 min; 20 °C", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "1063": {"en": {"f": "Repeticion Maxima Brzycki = f(peso_levantado, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Repeticion Maxima Brzycki = f(peso_levantado, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Repeticion Maxima Brzycki = f(peso_levantado, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Repeticion Maxima Brzycki = f(peso_levantado, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Repeticion Maxima Brzycki = f(peso_levantado, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Repeticion Maxima Brzycki = f(peso_levantado, repeticiones)", "ei": "80 kg; 5", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "1064": {"en": {"f": "Proteina Diaria = f(peso, objetivo)", "ei": "70 kg; 10", "eo": "Results calculated from 2 inputs", "u": ["health and fitness tracking", "nutrition and diet planning", "medical parameter estimation", "wellness goal setting"]}, "es": {"f": "Proteina Diaria = f(peso, objetivo)", "ei": "70 kg; 10", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de salud y fitness", "planificación de nutrición y dieta", "estimación de parámetros médicos", "establecimiento de metas de bienestar"]}, "fr": {"f": "Proteina Diaria = f(peso, objetivo)", "ei": "70 kg; 10", "eo": "Results calculated from 2 inputs", "u": ["suivi de santé et de fitness", "planification nutritionnelle et diététique", "estimation de paramètres médicaux", "fixation d'objectifs de bien-être"]}, "pt": {"f": "Proteina Diaria = f(peso, objetivo)", "ei": "70 kg; 10", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de saúde e fitness", "planejamento de nutrição e dieta", "estimativa de parâmetros médicos", "definição de metas de bem-estar"]}, "de": {"f": "Proteina Diaria = f(peso, objetivo)", "ei": "70 kg; 10", "eo": "Results calculated from 2 inputs", "u": ["Gesundheits- und Fitness-Tracking", "Ernährungs- und Diätplanung", "medizinische Parameterschätzung", "Wellness-Zielsetzung"]}, "it": {"f": "Proteina Diaria = f(peso, objetivo)", "ei": "70 kg; 10", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio di salute e fitness", "pianificazione nutrizionale e dietetica", "stima di parametri medici", "definizione di obiettivi di benessere"]}},
    "1065": {"en": {"f": "Rentabilidad Dividendo = f(dividendo_anual, precio_accion)", "ei": "2 €; 50 €", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Rentabilidad Dividendo = f(dividendo_anual, precio_accion)", "ei": "2 €; 50 €", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Rentabilidad Dividendo = f(dividendo_anual, precio_accion)", "ei": "2 €; 50 €", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Rentabilidad Dividendo = f(dividendo_anual, precio_accion)", "ei": "2 €; 50 €", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Rentabilidad Dividendo = f(dividendo_anual, precio_accion)", "ei": "2 €; 50 €", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Rentabilidad Dividendo = f(dividendo_anual, precio_accion)", "ei": "2 €; 50 €", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "1066": {"en": {"f": "Periodo Recuperacion = f(inversion_inicial, flujo_anual)", "ei": "10000 €; 2000 €", "eo": "Results calculated from 2 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Periodo Recuperacion = f(inversion_inicial, flujo_anual)", "ei": "10000 €; 2000 €", "eo": "Results calculated from 2 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Periodo Recuperacion = f(inversion_inicial, flujo_anual)", "ei": "10000 €; 2000 €", "eo": "Results calculated from 2 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Periodo Recuperacion = f(inversion_inicial, flujo_anual)", "ei": "10000 €; 2000 €", "eo": "Results calculated from 2 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Periodo Recuperacion = f(inversion_inicial, flujo_anual)", "ei": "10000 €; 2000 €", "eo": "Results calculated from 2 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Periodo Recuperacion = f(inversion_inicial, flujo_anual)", "ei": "10000 €; 2000 €", "eo": "Results calculated from 2 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "1067": {"en": {"f": "Impuesto Ganancias Capital = f(precio_compra, precio_venta, tasa_impuesto)", "ei": "100 €; 150 €; 19 %", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Impuesto Ganancias Capital = f(precio_compra, precio_venta, tasa_impuesto)", "ei": "100 €; 150 €; 19 %", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Impuesto Ganancias Capital = f(precio_compra, precio_venta, tasa_impuesto)", "ei": "100 €; 150 €; 19 %", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Impuesto Ganancias Capital = f(precio_compra, precio_venta, tasa_impuesto)", "ei": "100 €; 150 €; 19 %", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Impuesto Ganancias Capital = f(precio_compra, precio_venta, tasa_impuesto)", "ei": "100 €; 150 €; 19 %", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Impuesto Ganancias Capital = f(precio_compra, precio_venta, tasa_impuesto)", "ei": "100 €; 150 €; 19 %", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "1068": {"en": {"f": "Tipo Cambio Comision = f(monto, tipo_cambio, comision)", "ei": "1000 €; 1.08; 1.5 %", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Tipo Cambio Comision = f(monto, tipo_cambio, comision)", "ei": "1000 €; 1.08; 1.5 %", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Tipo Cambio Comision = f(monto, tipo_cambio, comision)", "ei": "1000 €; 1.08; 1.5 %", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Tipo Cambio Comision = f(monto, tipo_cambio, comision)", "ei": "1000 €; 1.08; 1.5 %", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Tipo Cambio Comision = f(monto, tipo_cambio, comision)", "ei": "1000 €; 1.08; 1.5 %", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Tipo Cambio Comision = f(monto, tipo_cambio, comision)", "ei": "1000 €; 1.08; 1.5 %", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "1069": {"en": {"f": "Punto Equilibrio = f(costes_fijos, precio_venta, coste_variable)", "ei": "5000 €; 50 €; 30 €", "eo": "Results calculated from 3 inputs", "u": ["personal financial planning", "loan and mortgage comparisons", "investment return analysis", "budget and savings goals"]}, "es": {"f": "Punto Equilibrio = f(costes_fijos, precio_venta, coste_variable)", "ei": "5000 €; 50 €; 30 €", "eo": "Results calculated from 3 inputs", "u": ["planificación financiera personal", "comparación de préstamos e hipotecas", "análisis de rendimiento de inversiones", "presupuesto y metas de ahorro"]}, "fr": {"f": "Punto Equilibrio = f(costes_fijos, precio_venta, coste_variable)", "ei": "5000 €; 50 €; 30 €", "eo": "Results calculated from 3 inputs", "u": ["planification financière personnelle", "comparaison de prêts et hypothèques", "analyse de rendement des investissements", "budget et objectifs d'épargne"]}, "pt": {"f": "Punto Equilibrio = f(costes_fijos, precio_venta, coste_variable)", "ei": "5000 €; 50 €; 30 €", "eo": "Results calculated from 3 inputs", "u": ["planejamento financeiro pessoal", "comparação de empréstimos e hipotecas", "análise de retorno de investimentos", "orçamento e metas de poupança"]}, "de": {"f": "Punto Equilibrio = f(costes_fijos, precio_venta, coste_variable)", "ei": "5000 €; 50 €; 30 €", "eo": "Results calculated from 3 inputs", "u": ["persönliche Finanzplanung", "Kredit- und Hypothekenvergleiche", "Investitionsrendite-Analyse", "Budget- und Sparziele"]}, "it": {"f": "Punto Equilibrio = f(costes_fijos, precio_venta, coste_variable)", "ei": "5000 €; 50 €; 30 €", "eo": "Results calculated from 3 inputs", "u": ["pianificazione finanziaria personale", "confronto di prestiti e mutui", "analisi del rendimento degli investimenti", "budget e obiettivi di risparmio"]}},
    "1070": {"en": {"f": "Masa Molar = f(formula_quimica)", "ei": "18 g/mol", "eo": "Results calculated from 1 input", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Masa Molar = f(formula_quimica)", "ei": "18 g/mol", "eo": "Results calculated from 1 input", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Masa Molar = f(formula_quimica)", "ei": "18 g/mol", "eo": "Results calculated from 1 input", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Masa Molar = f(formula_quimica)", "ei": "18 g/mol", "eo": "Results calculated from 1 input", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Masa Molar = f(formula_quimica)", "ei": "18 g/mol", "eo": "Results calculated from 1 input", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Masa Molar = f(formula_quimica)", "ei": "18 g/mol", "eo": "Results calculated from 1 input", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1071": {"en": {"f": "Ph Hidrogeno = f(concentracion_h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Ph Hidrogeno = f(concentracion_h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Ph Hidrogeno = f(concentracion_h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Ph Hidrogeno = f(concentracion_h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Ph Hidrogeno = f(concentracion_h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Ph Hidrogeno = f(concentracion_h)", "ei": "1e-07 mol/L", "eo": "Results calculated from 1 input", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1072": {"en": {"f": "Gas Ideal = f(presion, volumen_gas, moles, temperatura)", "ei": "1 atm; 22.4 L; 1 mol; 273 K", "eo": "Results calculated from 4 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Gas Ideal = f(presion, volumen_gas, moles, temperatura)", "ei": "1 atm; 22.4 L; 1 mol; 273 K", "eo": "Results calculated from 4 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Gas Ideal = f(presion, volumen_gas, moles, temperatura)", "ei": "1 atm; 22.4 L; 1 mol; 273 K", "eo": "Results calculated from 4 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Gas Ideal = f(presion, volumen_gas, moles, temperatura)", "ei": "1 atm; 22.4 L; 1 mol; 273 K", "eo": "Results calculated from 4 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Gas Ideal = f(presion, volumen_gas, moles, temperatura)", "ei": "1 atm; 22.4 L; 1 mol; 273 K", "eo": "Results calculated from 4 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Gas Ideal = f(presion, volumen_gas, moles, temperatura)", "ei": "1 atm; 22.4 L; 1 mol; 273 K", "eo": "Results calculated from 4 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1073": {"en": {"f": "Molaridad = f(moles, volumen, masa_solvente)", "ei": "1 mol; 1 L; 1000 g", "eo": "Results calculated from 3 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Molaridad = f(moles, volumen, masa_solvente)", "ei": "1 mol; 1 L; 1000 g", "eo": "Results calculated from 3 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Molaridad = f(moles, volumen, masa_solvente)", "ei": "1 mol; 1 L; 1000 g", "eo": "Results calculated from 3 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Molaridad = f(moles, volumen, masa_solvente)", "ei": "1 mol; 1 L; 1000 g", "eo": "Results calculated from 3 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Molaridad = f(moles, volumen, masa_solvente)", "ei": "1 mol; 1 L; 1000 g", "eo": "Results calculated from 3 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Molaridad = f(moles, volumen, masa_solvente)", "ei": "1 mol; 1 L; 1000 g", "eo": "Results calculated from 3 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1074": {"en": {"f": "Dilucion = f(concentracion_inicial, volumen_inicial, concentracion_final, volumen_final)", "ei": "1 M; 100 mL; 0.1 M; 1000 mL", "eo": "Results calculated from 4 inputs", "u": ["chemistry homework and lab work", "pharmaceutical and medical calculations", "industrial chemistry analysis", "environmental science and safety"]}, "es": {"f": "Dilucion = f(concentracion_inicial, volumen_inicial, concentracion_final, volumen_final)", "ei": "1 M; 100 mL; 0.1 M; 1000 mL", "eo": "Results calculated from 4 inputs", "u": ["tareas de química y trabajo de laboratorio", "cálculos farmacéuticos y médicos", "análisis de química industrial", "ciencia ambiental y seguridad"]}, "fr": {"f": "Dilucion = f(concentracion_inicial, volumen_inicial, concentracion_final, volumen_final)", "ei": "1 M; 100 mL; 0.1 M; 1000 mL", "eo": "Results calculated from 4 inputs", "u": ["devoirs de chimie et travail de laboratoire", "calculs pharmaceutiques et médicaux", "analyse de chimie industrielle", "science environnementale et sécurité"]}, "pt": {"f": "Dilucion = f(concentracion_inicial, volumen_inicial, concentracion_final, volumen_final)", "ei": "1 M; 100 mL; 0.1 M; 1000 mL", "eo": "Results calculated from 4 inputs", "u": ["tarefas de química e trabalho de laboratório", "cálculos farmacêuticos e médicos", "análise de química industrial", "ciência ambiental e segurança"]}, "de": {"f": "Dilucion = f(concentracion_inicial, volumen_inicial, concentracion_final, volumen_final)", "ei": "1 M; 100 mL; 0.1 M; 1000 mL", "eo": "Results calculated from 4 inputs", "u": ["Chemiehausaufgaben und Laborarbeit", "pharmazeutische und medizinische Berechnungen", "industrielle Chemieanalyse", "Umweltwissenschaft und Sicherheit"]}, "it": {"f": "Dilucion = f(concentracion_inicial, volumen_inicial, concentracion_final, volumen_final)", "ei": "1 M; 100 mL; 0.1 M; 1000 mL", "eo": "Results calculated from 4 inputs", "u": ["compiti di chimica e lavoro di laboratorio", "calcoli farmaceutici e medici", "analisi di chimica industriale", "scienza ambientale e sicurezza"]}},
    "1075": {"en": {"f": "Codigo Colores Resistencia = f(banda1, banda2, banda3)", "ei": "10; 10; 10", "eo": "Results calculated from 3 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Codigo Colores Resistencia = f(banda1, banda2, banda3)", "ei": "10; 10; 10", "eo": "Results calculated from 3 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Codigo Colores Resistencia = f(banda1, banda2, banda3)", "ei": "10; 10; 10", "eo": "Results calculated from 3 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Codigo Colores Resistencia = f(banda1, banda2, banda3)", "ei": "10; 10; 10", "eo": "Results calculated from 3 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Codigo Colores Resistencia = f(banda1, banda2, banda3)", "ei": "10; 10; 10", "eo": "Results calculated from 3 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Codigo Colores Resistencia = f(banda1, banda2, banda3)", "ei": "10; 10; 10", "eo": "Results calculated from 3 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1076": {"en": {"f": "Energia Capacitor = f(capacitancia, voltaje)", "ei": "100 μF; 12 V", "eo": "Results calculated from 2 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Energia Capacitor = f(capacitancia, voltaje)", "ei": "100 μF; 12 V", "eo": "Results calculated from 2 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Energia Capacitor = f(capacitancia, voltaje)", "ei": "100 μF; 12 V", "eo": "Results calculated from 2 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Energia Capacitor = f(capacitancia, voltaje)", "ei": "100 μF; 12 V", "eo": "Results calculated from 2 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Energia Capacitor = f(capacitancia, voltaje)", "ei": "100 μF; 12 V", "eo": "Results calculated from 2 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Energia Capacitor = f(capacitancia, voltaje)", "ei": "100 μF; 12 V", "eo": "Results calculated from 2 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1077": {"en": {"f": "Divisor Voltaje = f(voltaje_entrada, r1, r2)", "ei": "12 V; 1000 Ω; 2000 Ω", "eo": "Results calculated from 3 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Divisor Voltaje = f(voltaje_entrada, r1, r2)", "ei": "12 V; 1000 Ω; 2000 Ω", "eo": "Results calculated from 3 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Divisor Voltaje = f(voltaje_entrada, r1, r2)", "ei": "12 V; 1000 Ω; 2000 Ω", "eo": "Results calculated from 3 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Divisor Voltaje = f(voltaje_entrada, r1, r2)", "ei": "12 V; 1000 Ω; 2000 Ω", "eo": "Results calculated from 3 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Divisor Voltaje = f(voltaje_entrada, r1, r2)", "ei": "12 V; 1000 Ω; 2000 Ω", "eo": "Results calculated from 3 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Divisor Voltaje = f(voltaje_entrada, r1, r2)", "ei": "12 V; 1000 Ω; 2000 Ω", "eo": "Results calculated from 3 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1078": {"en": {"f": "Constante Tiempo Rc = f(resistencia, capacitancia)", "ei": "1000 Ω; 100 μF", "eo": "Results calculated from 2 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Constante Tiempo Rc = f(resistencia, capacitancia)", "ei": "1000 Ω; 100 μF", "eo": "Results calculated from 2 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Constante Tiempo Rc = f(resistencia, capacitancia)", "ei": "1000 Ω; 100 μF", "eo": "Results calculated from 2 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Constante Tiempo Rc = f(resistencia, capacitancia)", "ei": "1000 Ω; 100 μF", "eo": "Results calculated from 2 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Constante Tiempo Rc = f(resistencia, capacitancia)", "ei": "1000 Ω; 100 μF", "eo": "Results calculated from 2 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Constante Tiempo Rc = f(resistencia, capacitancia)", "ei": "1000 Ω; 100 μF", "eo": "Results calculated from 2 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1079": {"en": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["circuit design and analysis", "electronics homework and projects", "component selection and verification", "troubleshooting electrical circuits"]}, "es": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["diseño y análisis de circuitos", "tareas y proyectos de electrónica", "selección y verificación de componentes", "resolución de circuitos eléctricos"]}, "fr": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["conception et analyse de circuits", "devoirs et projets d'électronique", "sélection et vérification de composants", "dépannage de circuits électriques"]}, "pt": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["projeto e análise de circuitos", "tarefas e projetos de eletrônica", "seleção e verificação de componentes", "solução de problemas de circuitos elétricos"]}, "de": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["Schaltungsdesign und Analyse", "Elektronik-Hausaufgaben und Projekte", "Bauteilauswahl und Verifizierung", "Fehlersuche in elektrischen Schaltungen"]}, "it": {"f": "Puente Wheatstone = f(r1, r2, r3)", "ei": "100 Ω; 100 Ω; 100 Ω", "eo": "Results calculated from 3 inputs", "u": ["progettazione e analisi di circuiti", "compiti e progetti di elettronica", "selezione e verifica di componenti", "risoluzione di circuiti elettrici"]}},
    "1080": {"en": {"f": "Consumo Combustible = f(litros, km)", "ei": "50 L; 500 km", "eo": "Results calculated from 2 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Consumo Combustible = f(litros, km)", "ei": "50 L; 500 km", "eo": "Results calculated from 2 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Consumo Combustible = f(litros, km)", "ei": "50 L; 500 km", "eo": "Results calculated from 2 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Consumo Combustible = f(litros, km)", "ei": "50 L; 500 km", "eo": "Results calculated from 2 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Consumo Combustible = f(litros, km)", "ei": "50 L; 500 km", "eo": "Results calculated from 2 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Consumo Combustible = f(litros, km)", "ei": "50 L; 500 km", "eo": "Results calculated from 2 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1081": {"en": {"f": "Distancia Frenado = f(velocidad_ms, coeficiente)", "ei": "20 m/s; 0.7", "eo": "Results calculated from 2 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Distancia Frenado = f(velocidad_ms, coeficiente)", "ei": "20 m/s; 0.7", "eo": "Results calculated from 2 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Distancia Frenado = f(velocidad_ms, coeficiente)", "ei": "20 m/s; 0.7", "eo": "Results calculated from 2 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Distancia Frenado = f(velocidad_ms, coeficiente)", "ei": "20 m/s; 0.7", "eo": "Results calculated from 2 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Distancia Frenado = f(velocidad_ms, coeficiente)", "ei": "20 m/s; 0.7", "eo": "Results calculated from 2 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Distancia Frenado = f(velocidad_ms, coeficiente)", "ei": "20 m/s; 0.7", "eo": "Results calculated from 2 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1082": {"en": {"f": "Cilindrada Motor = f(diametro_cilindro, carrera, numero_cilindros)", "ei": "80 mm; 90 mm; 4", "eo": "Results calculated from 3 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Cilindrada Motor = f(diametro_cilindro, carrera, numero_cilindros)", "ei": "80 mm; 90 mm; 4", "eo": "Results calculated from 3 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Cilindrada Motor = f(diametro_cilindro, carrera, numero_cilindros)", "ei": "80 mm; 90 mm; 4", "eo": "Results calculated from 3 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Cilindrada Motor = f(diametro_cilindro, carrera, numero_cilindros)", "ei": "80 mm; 90 mm; 4", "eo": "Results calculated from 3 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Cilindrada Motor = f(diametro_cilindro, carrera, numero_cilindros)", "ei": "80 mm; 90 mm; 4", "eo": "Results calculated from 3 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Cilindrada Motor = f(diametro_cilindro, carrera, numero_cilindros)", "ei": "80 mm; 90 mm; 4", "eo": "Results calculated from 3 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1083": {"en": {"f": "Presion Neumaticos = f(presion_base, carga_extra)", "ei": "2.2 bar; 200 kg", "eo": "Results calculated from 2 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Presion Neumaticos = f(presion_base, carga_extra)", "ei": "2.2 bar; 200 kg", "eo": "Results calculated from 2 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Presion Neumaticos = f(presion_base, carga_extra)", "ei": "2.2 bar; 200 kg", "eo": "Results calculated from 2 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Presion Neumaticos = f(presion_base, carga_extra)", "ei": "2.2 bar; 200 kg", "eo": "Results calculated from 2 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Presion Neumaticos = f(presion_base, carga_extra)", "ei": "2.2 bar; 200 kg", "eo": "Results calculated from 2 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Presion Neumaticos = f(presion_base, carga_extra)", "ei": "2.2 bar; 200 kg", "eo": "Results calculated from 2 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1084": {"en": {"f": "Tiempo Vuelo Viento = f(distancia, velocidad_avion, velocidad_viento)", "ei": "1000 km; 900 km/h; 50 km/h", "eo": "Results calculated from 3 inputs", "u": ["road trip cost planning", "vehicle fuel efficiency analysis", "driving distance and time estimation", "transportation budgeting"]}, "es": {"f": "Tiempo Vuelo Viento = f(distancia, velocidad_avion, velocidad_viento)", "ei": "1000 km; 900 km/h; 50 km/h", "eo": "Results calculated from 3 inputs", "u": ["planificación de costos de viaje por carretera", "análisis de eficiencia de combustible del vehículo", "estimación de distancia y tiempo de conducción", "presupuesto de transporte"]}, "fr": {"f": "Tiempo Vuelo Viento = f(distancia, velocidad_avion, velocidad_viento)", "ei": "1000 km; 900 km/h; 50 km/h", "eo": "Results calculated from 3 inputs", "u": ["planification des coûts de voyage", "analyse de l'efficacité énergétique du véhicule", "estimation de distance et de temps de conduite", "budget de transport"]}, "pt": {"f": "Tiempo Vuelo Viento = f(distancia, velocidad_avion, velocidad_viento)", "ei": "1000 km; 900 km/h; 50 km/h", "eo": "Results calculated from 3 inputs", "u": ["planejamento de custos de viagem", "análise de eficiência de combustível do veículo", "estimativa de distância e tempo de direção", "orçamento de transporte"]}, "de": {"f": "Tiempo Vuelo Viento = f(distancia, velocidad_avion, velocidad_viento)", "ei": "1000 km; 900 km/h; 50 km/h", "eo": "Results calculated from 3 inputs", "u": ["Kostenplanung für Straßenreisen", "Analyse der Kraftstoffeffizienz", "Schätzung von Fahrstrecke und -zeit", "Transportbudgetplanung"]}, "it": {"f": "Tiempo Vuelo Viento = f(distancia, velocidad_avion, velocidad_viento)", "ei": "1000 km; 900 km/h; 50 km/h", "eo": "Results calculated from 3 inputs", "u": ["pianificazione dei costi di viaggio", "analisi dell'efficienza del carburante", "stima di distanza e tempo di guida", "budget dei trasporti"]}},
    "1085": {"en": {"f": "Profundidad Campo = f(longitud_focal, apertura, distancia)", "ei": "50 mm; 2.8 f/; 3 m", "eo": "Results calculated from 3 inputs", "u": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"]}, "es": {"f": "Profundidad Campo = f(longitud_focal, apertura, distancia)", "ei": "50 mm; 2.8 f/; 3 m", "eo": "Results calculated from 3 inputs", "u": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"]}, "fr": {"f": "Profundidad Campo = f(longitud_focal, apertura, distancia)", "ei": "50 mm; 2.8 f/; 3 m", "eo": "Results calculated from 3 inputs", "u": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"]}, "pt": {"f": "Profundidad Campo = f(longitud_focal, apertura, distancia)", "ei": "50 mm; 2.8 f/; 3 m", "eo": "Results calculated from 3 inputs", "u": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"]}, "de": {"f": "Profundidad Campo = f(longitud_focal, apertura, distancia)", "ei": "50 mm; 2.8 f/; 3 m", "eo": "Results calculated from 3 inputs", "u": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"]}, "it": {"f": "Profundidad Campo = f(longitud_focal, apertura, distancia)", "ei": "50 mm; 2.8 f/; 3 m", "eo": "Results calculated from 3 inputs", "u": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"]}},
    "1086": {"en": {"f": "Numero Guia Flash = f(numero_guia, apertura)", "ei": "36; 4 f/", "eo": "Results calculated from 2 inputs", "u": ["photography technique optimization", "lens and camera settings", "studio and lighting calculations", "landscape and portrait planning"]}, "es": {"f": "Numero Guia Flash = f(numero_guia, apertura)", "ei": "36; 4 f/", "eo": "Results calculated from 2 inputs", "u": ["optimización de técnicas fotográficas", "ajustes de lente y cámara", "cálculos de estudio e iluminación", "planificación de paisaje y retrato"]}, "fr": {"f": "Numero Guia Flash = f(numero_guia, apertura)", "ei": "36; 4 f/", "eo": "Results calculated from 2 inputs", "u": ["optimisation des techniques photographiques", "réglages d'objectif et d'appareil", "calculs de studio et d'éclairage", "planification de paysage et portrait"]}, "pt": {"f": "Numero Guia Flash = f(numero_guia, apertura)", "ei": "36; 4 f/", "eo": "Results calculated from 2 inputs", "u": ["otimização de técnicas fotográficas", "configurações de lente e câmera", "cálculos de estúdio e iluminação", "planejamento de paisagem e retrato"]}, "de": {"f": "Numero Guia Flash = f(numero_guia, apertura)", "ei": "36; 4 f/", "eo": "Results calculated from 2 inputs", "u": ["Optimierung der Fototechnik", "Objektiv- und Kameraeinstellungen", "Studio- und Lichtberechnungen", "Landschafts- und Porträtplanung"]}, "it": {"f": "Numero Guia Flash = f(numero_guia, apertura)", "ei": "36; 4 f/", "eo": "Results calculated from 2 inputs", "u": ["ottimizzazione delle tecniche fotografiche", "impostazioni di lente e fotocamera", "calcoli di studio e illuminazione", "pianificazione di paesaggio e ritratto"]}},
    "1087": {"en": {"f": "Indice Calor = f(temperatura, humedad)", "ei": "30 °F; 60 %", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Indice Calor = f(temperatura, humedad)", "ei": "30 °F; 60 %", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Indice Calor = f(temperatura, humedad)", "ei": "30 °F; 60 %", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Indice Calor = f(temperatura, humedad)", "ei": "30 °F; 60 %", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Indice Calor = f(temperatura, humedad)", "ei": "30 °F; 60 %", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Indice Calor = f(temperatura, humedad)", "ei": "30 °F; 60 %", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1088": {"en": {"f": "Sensacion Frio Viento = f(temperatura_f, velocidad_viento)", "ei": "20 °F; 10 mph", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Sensacion Frio Viento = f(temperatura_f, velocidad_viento)", "ei": "20 °F; 10 mph", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Sensacion Frio Viento = f(temperatura_f, velocidad_viento)", "ei": "20 °F; 10 mph", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Sensacion Frio Viento = f(temperatura_f, velocidad_viento)", "ei": "20 °F; 10 mph", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Sensacion Frio Viento = f(temperatura_f, velocidad_viento)", "ei": "20 °F; 10 mph", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Sensacion Frio Viento = f(temperatura_f, velocidad_viento)", "ei": "20 °F; 10 mph", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1089": {"en": {"f": "Humedad Relativa Rocio = f(temperatura, punto_rocio)", "ei": "20 °C; 15 °C", "eo": "Results calculated from 2 inputs", "u": ["weather safety and heat index", "outdoor activity planning", "HVAC and comfort calculations", "agricultural and environmental monitoring"]}, "es": {"f": "Humedad Relativa Rocio = f(temperatura, punto_rocio)", "ei": "20 °C; 15 °C", "eo": "Results calculated from 2 inputs", "u": ["seguridad meteorológica e índice de calor", "planificación de actividades al aire libre", "cálculos de HVAC y confort", "monitoreo agrícola y ambiental"]}, "fr": {"f": "Humedad Relativa Rocio = f(temperatura, punto_rocio)", "ei": "20 °C; 15 °C", "eo": "Results calculated from 2 inputs", "u": ["sécurité météorologique et indice de chaleur", "planification d'activités en plein air", "calculs CVC et de confort", "surveillance agricole et environnementale"]}, "pt": {"f": "Humedad Relativa Rocio = f(temperatura, punto_rocio)", "ei": "20 °C; 15 °C", "eo": "Results calculated from 2 inputs", "u": ["segurança meteorológica e índice de calor", "planejamento de atividades ao ar livre", "cálculos de HVAC e conforto", "monitoramento agrícola e ambiental"]}, "de": {"f": "Humedad Relativa Rocio = f(temperatura, punto_rocio)", "ei": "20 °C; 15 °C", "eo": "Results calculated from 2 inputs", "u": ["Wettersicherheit und Hitzeindex", "Planung von Outdoor-Aktivitäten", "HKL- und Komfortberechnungen", "landwirtschaftliche und Umweltüberwachung"]}, "it": {"f": "Humedad Relativa Rocio = f(temperatura, punto_rocio)", "ei": "20 °C; 15 °C", "eo": "Results calculated from 2 inputs", "u": ["sicurezza meteorologica e indice di calore", "pianificazione di attività all'aperto", "calcoli HVAC e comfort", "monitoraggio agricolo e ambientale"]}},
    "1090": {"en": {"f": "Entropia Contrasena = f(longitud, conjunto_caracteres)", "ei": "12 caracteres; 62", "eo": "Results calculated from 2 inputs", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Entropia Contrasena = f(longitud, conjunto_caracteres)", "ei": "12 caracteres; 62", "eo": "Results calculated from 2 inputs", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Entropia Contrasena = f(longitud, conjunto_caracteres)", "ei": "12 caracteres; 62", "eo": "Results calculated from 2 inputs", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Entropia Contrasena = f(longitud, conjunto_caracteres)", "ei": "12 caracteres; 62", "eo": "Results calculated from 2 inputs", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Entropia Contrasena = f(longitud, conjunto_caracteres)", "ei": "12 caracteres; 62", "eo": "Results calculated from 2 inputs", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Entropia Contrasena = f(longitud, conjunto_caracteres)", "ei": "12 caracteres; 62", "eo": "Results calculated from 2 inputs", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1091": {"en": {"f": "Contador Caracteres Texto = f(texto)", "ei": "Hola mundo", "eo": "Results calculated from 1 input", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Contador Caracteres Texto = f(texto)", "ei": "Hola mundo", "eo": "Results calculated from 1 input", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Contador Caracteres Texto = f(texto)", "ei": "Hola mundo", "eo": "Results calculated from 1 input", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Contador Caracteres Texto = f(texto)", "ei": "Hola mundo", "eo": "Results calculated from 1 input", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Contador Caracteres Texto = f(texto)", "ei": "Hola mundo", "eo": "Results calculated from 1 input", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Contador Caracteres Texto = f(texto)", "ei": "Hola mundo", "eo": "Results calculated from 1 input", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1092": {"en": {"f": "Dias Habiles = f(dias_totales, festivos)", "ei": "30 días; 2 días", "eo": "Results calculated from 2 inputs", "u": ["password security assessment", "text analysis and character counting", "date and time calculations", "everyday utility tasks"]}, "es": {"f": "Dias Habiles = f(dias_totales, festivos)", "ei": "30 días; 2 días", "eo": "Results calculated from 2 inputs", "u": ["evaluación de seguridad de contraseñas", "análisis de texto y conteo de caracteres", "cálculos de fecha y hora", "tareas utilitarias cotidianas"]}, "fr": {"f": "Dias Habiles = f(dias_totales, festivos)", "ei": "30 días; 2 días", "eo": "Results calculated from 2 inputs", "u": ["évaluation de la sécurité des mots de passe", "analyse de texte et comptage de caractères", "calculs de date et d'heure", "tâches utilitaires quotidiennes"]}, "pt": {"f": "Dias Habiles = f(dias_totales, festivos)", "ei": "30 días; 2 días", "eo": "Results calculated from 2 inputs", "u": ["avaliação de segurança de senhas", "análise de texto e contagem de caracteres", "cálculos de data e hora", "tarefas utilitárias diárias"]}, "de": {"f": "Dias Habiles = f(dias_totales, festivos)", "ei": "30 días; 2 días", "eo": "Results calculated from 2 inputs", "u": ["Passwortsicherheitsbewertung", "Textanalyse und Zeichenzählung", "Datums- und Zeitberechnungen", "alltägliche Hilfsaufgaben"]}, "it": {"f": "Dias Habiles = f(dias_totales, festivos)", "ei": "30 días; 2 días", "eo": "Results calculated from 2 inputs", "u": ["valutazione della sicurezza delle password", "analisi del testo e conteggio dei caratteri", "calcoli di data e ora", "task utilitari quotidiani"]}},
    "1093": {"en": {"f": "Deflexion Viga = f(carga, longitud, modulo_elastico, momento_inercia)", "ei": "1000 N; 2 m; 200000000000.0 Pa; 1e-06 m⁴", "eo": "Results calculated from 4 inputs", "u": ["structural engineering analysis", "mechanical design calculations", "construction planning and verification", "academic engineering problems"]}, "es": {"f": "Deflexion Viga = f(carga, longitud, modulo_elastico, momento_inercia)", "ei": "1000 N; 2 m; 200000000000.0 Pa; 1e-06 m⁴", "eo": "Results calculated from 4 inputs", "u": ["análisis de ingeniería estructural", "cálculos de diseño mecánico", "planificación y verificación de construcción", "problemas de ingeniería académica"]}, "fr": {"f": "Deflexion Viga = f(carga, longitud, modulo_elastico, momento_inercia)", "ei": "1000 N; 2 m; 200000000000.0 Pa; 1e-06 m⁴", "eo": "Results calculated from 4 inputs", "u": ["analyse d'ingénierie structurelle", "calculs de conception mécanique", "planification et vérification de construction", "problèmes d'ingénierie académique"]}, "pt": {"f": "Deflexion Viga = f(carga, longitud, modulo_elastico, momento_inercia)", "ei": "1000 N; 2 m; 200000000000.0 Pa; 1e-06 m⁴", "eo": "Results calculated from 4 inputs", "u": ["análise de engenharia estrutural", "cálculos de projeto mecânico", "planejamento e verificação de construção", "problemas de engenharia acadêmica"]}, "de": {"f": "Deflexion Viga = f(carga, longitud, modulo_elastico, momento_inercia)", "ei": "1000 N; 2 m; 200000000000.0 Pa; 1e-06 m⁴", "eo": "Results calculated from 4 inputs", "u": ["Struktur-Ingenieuranalyse", "mechanische Auslegungsberechnungen", "Bauplanung und Verifizierung", "akademische Ingenieurprobleme"]}, "it": {"f": "Deflexion Viga = f(carga, longitud, modulo_elastico, momento_inercia)", "ei": "1000 N; 2 m; 200000000000.0 Pa; 1e-06 m⁴", "eo": "Results calculated from 4 inputs", "u": ["analisi di ingegneria strutturale", "calcoli di progettazione meccanica", "pianificazione e verifica della costruzione", "problemi di ingegneria accademica"]}},
    "1094": {"en": {"f": "Par Apriete Tornillo = f(diametro, carga_precarga, coeficiente)", "ei": "10 mm; 50000 N; 0.2", "eo": "Results calculated from 3 inputs", "u": ["structural engineering analysis", "mechanical design calculations", "construction planning and verification", "academic engineering problems"]}, "es": {"f": "Par Apriete Tornillo = f(diametro, carga_precarga, coeficiente)", "ei": "10 mm; 50000 N; 0.2", "eo": "Results calculated from 3 inputs", "u": ["análisis de ingeniería estructural", "cálculos de diseño mecánico", "planificación y verificación de construcción", "problemas de ingeniería académica"]}, "fr": {"f": "Par Apriete Tornillo = f(diametro, carga_precarga, coeficiente)", "ei": "10 mm; 50000 N; 0.2", "eo": "Results calculated from 3 inputs", "u": ["analyse d'ingénierie structurelle", "calculs de conception mécanique", "planification et vérification de construction", "problèmes d'ingénierie académique"]}, "pt": {"f": "Par Apriete Tornillo = f(diametro, carga_precarga, coeficiente)", "ei": "10 mm; 50000 N; 0.2", "eo": "Results calculated from 3 inputs", "u": ["análise de engenharia estrutural", "cálculos de projeto mecânico", "planejamento e verificação de construção", "problemas de engenharia acadêmica"]}, "de": {"f": "Par Apriete Tornillo = f(diametro, carga_precarga, coeficiente)", "ei": "10 mm; 50000 N; 0.2", "eo": "Results calculated from 3 inputs", "u": ["Struktur-Ingenieuranalyse", "mechanische Auslegungsberechnungen", "Bauplanung und Verifizierung", "akademische Ingenieurprobleme"]}, "it": {"f": "Par Apriete Tornillo = f(diametro, carga_precarga, coeficiente)", "ei": "10 mm; 50000 N; 0.2", "eo": "Results calculated from 3 inputs", "u": ["analisi di ingegneria strutturale", "calcoli di progettazione meccanica", "pianificazione e verifica della costruzione", "problemi di ingegneria accademica"]}},
    "1095": {"en": {"f": "Constante Resorte = f(fuerza, deformacion)", "ei": "100 N; 0.01 m", "eo": "Results calculated from 2 inputs", "u": ["structural engineering analysis", "mechanical design calculations", "construction planning and verification", "academic engineering problems"]}, "es": {"f": "Constante Resorte = f(fuerza, deformacion)", "ei": "100 N; 0.01 m", "eo": "Results calculated from 2 inputs", "u": ["análisis de ingeniería estructural", "cálculos de diseño mecánico", "planificación y verificación de construcción", "problemas de ingeniería académica"]}, "fr": {"f": "Constante Resorte = f(fuerza, deformacion)", "ei": "100 N; 0.01 m", "eo": "Results calculated from 2 inputs", "u": ["analyse d'ingénierie structurelle", "calculs de conception mécanique", "planification et vérification de construction", "problèmes d'ingénierie académique"]}, "pt": {"f": "Constante Resorte = f(fuerza, deformacion)", "ei": "100 N; 0.01 m", "eo": "Results calculated from 2 inputs", "u": ["análise de engenharia estrutural", "cálculos de projeto mecânico", "planejamento e verificação de construção", "problemas de engenharia acadêmica"]}, "de": {"f": "Constante Resorte = f(fuerza, deformacion)", "ei": "100 N; 0.01 m", "eo": "Results calculated from 2 inputs", "u": ["Struktur-Ingenieuranalyse", "mechanische Auslegungsberechnungen", "Bauplanung und Verifizierung", "akademische Ingenieurprobleme"]}, "it": {"f": "Constante Resorte = f(fuerza, deformacion)", "ei": "100 N; 0.01 m", "eo": "Results calculated from 2 inputs", "u": ["analisi di ingegneria strutturale", "calcoli di progettazione meccanica", "pianificazione e verifica della costruzione", "problemi di ingegneria accademica"]}},
    "1096": {"en": {"f": "Numero Reynolds = f(densidad, velocidad, diametro, viscosidad)", "ei": "1000 kg/m³; 1 m/s; 0.1 m; 0.001 Pa·s", "eo": "Results calculated from 4 inputs", "u": ["structural engineering analysis", "mechanical design calculations", "construction planning and verification", "academic engineering problems"]}, "es": {"f": "Numero Reynolds = f(densidad, velocidad, diametro, viscosidad)", "ei": "1000 kg/m³; 1 m/s; 0.1 m; 0.001 Pa·s", "eo": "Results calculated from 4 inputs", "u": ["análisis de ingeniería estructural", "cálculos de diseño mecánico", "planificación y verificación de construcción", "problemas de ingeniería académica"]}, "fr": {"f": "Numero Reynolds = f(densidad, velocidad, diametro, viscosidad)", "ei": "1000 kg/m³; 1 m/s; 0.1 m; 0.001 Pa·s", "eo": "Results calculated from 4 inputs", "u": ["analyse d'ingénierie structurelle", "calculs de conception mécanique", "planification et vérification de construction", "problèmes d'ingénierie académique"]}, "pt": {"f": "Numero Reynolds = f(densidad, velocidad, diametro, viscosidad)", "ei": "1000 kg/m³; 1 m/s; 0.1 m; 0.001 Pa·s", "eo": "Results calculated from 4 inputs", "u": ["análise de engenharia estrutural", "cálculos de projeto mecânico", "planejamento e verificação de construção", "problemas de engenharia acadêmica"]}, "de": {"f": "Numero Reynolds = f(densidad, velocidad, diametro, viscosidad)", "ei": "1000 kg/m³; 1 m/s; 0.1 m; 0.001 Pa·s", "eo": "Results calculated from 4 inputs", "u": ["Struktur-Ingenieuranalyse", "mechanische Auslegungsberechnungen", "Bauplanung und Verifizierung", "akademische Ingenieurprobleme"]}, "it": {"f": "Numero Reynolds = f(densidad, velocidad, diametro, viscosidad)", "ei": "1000 kg/m³; 1 m/s; 0.1 m; 0.001 Pa·s", "eo": "Results calculated from 4 inputs", "u": ["analisi di ingegneria strutturale", "calcoli di progettazione meccanica", "pianificazione e verifica della costruzione", "problemi di ingegneria accademica"]}},
    "1097": {"en": {"f": "Ritmo Carrera = f(distancia, tiempo_min)", "ei": "10 km; 50 min", "eo": "Results calculated from 2 inputs", "u": ["training pace and performance tracking", "fitness goal planning", "sports science calculations", "competition preparation"]}, "es": {"f": "Ritmo Carrera = f(distancia, tiempo_min)", "ei": "10 km; 50 min", "eo": "Results calculated from 2 inputs", "u": ["seguimiento de ritmo y rendimiento de entrenamiento", "planificación de objetivos de fitness", "cálculos de ciencia del deporte", "preparación para competiciones"]}, "fr": {"f": "Ritmo Carrera = f(distancia, tiempo_min)", "ei": "10 km; 50 min", "eo": "Results calculated from 2 inputs", "u": ["suivi d'allure et de performance d'entraînement", "planification d'objectifs de fitness", "calculs de science du sport", "préparation aux compétitions"]}, "pt": {"f": "Ritmo Carrera = f(distancia, tiempo_min)", "ei": "10 km; 50 min", "eo": "Results calculated from 2 inputs", "u": ["acompanhamento de ritmo e desempenho de treino", "planejamento de objetivos de fitness", "cálculos de ciência do esporte", "preparação para competições"]}, "de": {"f": "Ritmo Carrera = f(distancia, tiempo_min)", "ei": "10 km; 50 min", "eo": "Results calculated from 2 inputs", "u": ["Trainingspace- und Leistungs-Tracking", "Fitness-Zielplanung", "Sportwissenschaft-Berechnungen", "Wettkampfvorbereitung"]}, "it": {"f": "Ritmo Carrera = f(distancia, tiempo_min)", "ei": "10 km; 50 min", "eo": "Results calculated from 2 inputs", "u": ["monitoraggio dell'andatura e delle prestazioni", "pianificazione degli obiettivi di fitness", "calcoli di scienza dello sport", "preparazione alle competizioni"]}},
    "1098": {"en": {"f": "Handicap Golf = f(score, rating, slope)", "ei": "90; 72; 113", "eo": "Results calculated from 3 inputs", "u": ["training pace and performance tracking", "fitness goal planning", "sports science calculations", "competition preparation"]}, "es": {"f": "Handicap Golf = f(score, rating, slope)", "ei": "90; 72; 113", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de ritmo y rendimiento de entrenamiento", "planificación de objetivos de fitness", "cálculos de ciencia del deporte", "preparación para competiciones"]}, "fr": {"f": "Handicap Golf = f(score, rating, slope)", "ei": "90; 72; 113", "eo": "Results calculated from 3 inputs", "u": ["suivi d'allure et de performance d'entraînement", "planification d'objectifs de fitness", "calculs de science du sport", "préparation aux compétitions"]}, "pt": {"f": "Handicap Golf = f(score, rating, slope)", "ei": "90; 72; 113", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de ritmo e desempenho de treino", "planejamento de objetivos de fitness", "cálculos de ciência do esporte", "preparação para competições"]}, "de": {"f": "Handicap Golf = f(score, rating, slope)", "ei": "90; 72; 113", "eo": "Results calculated from 3 inputs", "u": ["Trainingspace- und Leistungs-Tracking", "Fitness-Zielplanung", "Sportwissenschaft-Berechnungen", "Wettkampfvorbereitung"]}, "it": {"f": "Handicap Golf = f(score, rating, slope)", "ei": "90; 72; 113", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio dell'andatura e delle prestazioni", "pianificazione degli obiettivi di fitness", "calcoli di scienza dello sport", "preparazione alle competizioni"]}},
    "1099": {"en": {"f": "Quemar Calorias Met = f(met, peso, duracion_min)", "ei": "8; 70 kg; 60 min", "eo": "Results calculated from 3 inputs", "u": ["training pace and performance tracking", "fitness goal planning", "sports science calculations", "competition preparation"]}, "es": {"f": "Quemar Calorias Met = f(met, peso, duracion_min)", "ei": "8; 70 kg; 60 min", "eo": "Results calculated from 3 inputs", "u": ["seguimiento de ritmo y rendimiento de entrenamiento", "planificación de objetivos de fitness", "cálculos de ciencia del deporte", "preparación para competiciones"]}, "fr": {"f": "Quemar Calorias Met = f(met, peso, duracion_min)", "ei": "8; 70 kg; 60 min", "eo": "Results calculated from 3 inputs", "u": ["suivi d'allure et de performance d'entraînement", "planification d'objectifs de fitness", "calculs de science du sport", "préparation aux compétitions"]}, "pt": {"f": "Quemar Calorias Met = f(met, peso, duracion_min)", "ei": "8; 70 kg; 60 min", "eo": "Results calculated from 3 inputs", "u": ["acompanhamento de ritmo e desempenho de treino", "planejamento de objetivos de fitness", "cálculos de ciência do esporte", "preparação para competições"]}, "de": {"f": "Quemar Calorias Met = f(met, peso, duracion_min)", "ei": "8; 70 kg; 60 min", "eo": "Results calculated from 3 inputs", "u": ["Trainingspace- und Leistungs-Tracking", "Fitness-Zielplanung", "Sportwissenschaft-Berechnungen", "Wettkampfvorbereitung"]}, "it": {"f": "Quemar Calorias Met = f(met, peso, duracion_min)", "ei": "8; 70 kg; 60 min", "eo": "Results calculated from 3 inputs", "u": ["monitoraggio dell'andatura e delle prestazioni", "pianificazione degli obiettivi di fitness", "calcoli di scienza dello sport", "preparazione alle competizioni"]}},
}


def build_article_from_facts(facts: dict, lang: str, calc_name: str = "") -> str:
    """Generate a unique 5-section SEO article (~400 words) from CALC_FACTS data."""
    d = facts.get(lang) or facts.get("en")
    if not d:
        return ""

    H = {
        "es": (
            "{name}: fórmula y definición",
            "Cómo usar la calculadora: ejemplo paso a paso",
            "¿Para qué sirve la {name}?",
            "Cómo interpretar los resultados",
            "Preguntas frecuentes sobre la {name}",
        ),
        "en": (
            "{name}: formula and definition",
            "How to use the calculator: step-by-step example",
            "What is the {name} used for?",
            "How to interpret the results",
            "Frequently asked questions about the {name}",
        ),
        "fr": (
            "{name} : formule et définition",
            "Comment utiliser la calculatrice : exemple pas à pas",
            "À quoi sert le {name} ?",
            "Comment interpréter les résultats",
            "Questions fréquentes sur le {name}",
        ),
        "pt": (
            "{name}: fórmula e definição",
            "Como usar a calculadora: exemplo passo a passo",
            "Para que serve a {name}?",
            "Como interpretar os resultados",
            "Perguntas frequentes sobre a {name}",
        ),
        "de": (
            "{name}: Formel und Definition",
            "Anleitung: Schritt-für-Schritt-Beispiel",
            "Wofür wird der {name} verwendet?",
            "So interpretieren Sie die Ergebnisse",
            "Häufig gestellte Fragen zum {name}",
        ),
        "it": (
            "{name}: formula e definizione",
            "Come usare la calcolatrice: esempio passo dopo passo",
            "A cosa serve il {name}?",
            "Come interpretare i risultati",
            "Domande frequenti sul {name}",
        ),
    }

    intro_p = {
        "es": (
            "La <strong>{f}</strong>. Este cálculo es fundamental en ciencia, ingeniería, "
            "medicina y educación. Comprender la fórmula te permite verificar los resultados "
            "y detectar valores atípicos antes de tomar decisiones importantes."
        ),
        "en": (
            "The formula: <strong>{f}</strong>. This calculation is fundamental in science, "
            "engineering, medicine, and education. Understanding the formula lets you verify "
            "results and spot outliers before making important decisions."
        ),
        "fr": (
            "La formule : <strong>{f}</strong>. Ce calcul est fondamental en science, "
            "ingénierie, médecine et éducation. Comprendre la formule vous permet de "
            "vérifier les résultats et détecter les valeurs aberrantes."
        ),
        "pt": (
            "A fórmula: <strong>{f}</strong>. Este cálculo é fundamental em ciência, "
            "engenharia, medicina e educação. Compreender a fórmula permite verificar "
            "os resultados e identificar valores atípicos."
        ),
        "de": (
            "Die Formel: <strong>{f}</strong>. Diese Berechnung ist grundlegend in Wissenschaft, "
            "Ingenieurwesen, Medizin und Bildung. Das Verständnis der Formel ermöglicht es "
            "Ihnen, Ergebnisse zu überprüfen."
        ),
        "it": (
            "La formula: <strong>{f}</strong>. Questo calcolo è fondamentale in scienza, "
            "ingegneria, medicina e istruzione. Capire la formula ti permette di verificare "
            "i risultati e individuare valori anomali."
        ),
    }

    step_p = {
        "es": (
            "<p>Sigue estos pasos para obtener el resultado correcto:</p>"
            "<ol>"
            "<li><strong>Introduce los datos de entrada:</strong> {ei}</li>"
            "<li><strong>La calculadora aplica la fórmula</strong> y muestra el resultado inmediatamente.</li>"
            "<li><strong>Resultado obtenido:</strong> {eo}</li>"
            "<li><strong>Verifica el resultado</strong> comprobando que las unidades son coherentes y el valor es razonable para tu caso.</li>"
            "</ol>"
            "<p>Si el resultado parece incorrecto, revisa que has introducido las unidades correctas y que los valores están dentro del rango esperado.</p>"
        ),
        "en": (
            "<p>Follow these steps to get the correct result:</p>"
            "<ol>"
            "<li><strong>Enter the input data:</strong> {ei}</li>"
            "<li><strong>The calculator applies the formula</strong> and shows the result instantly.</li>"
            "<li><strong>Result obtained:</strong> {eo}</li>"
            "<li><strong>Verify the result</strong> by checking that units are consistent and the value is reasonable for your case.</li>"
            "</ol>"
            "<p>If the result seems incorrect, check that you have entered the correct units and that values are within the expected range.</p>"
        ),
        "fr": (
            "<p>Suivez ces étapes pour obtenir le résultat correct :</p>"
            "<ol>"
            "<li><strong>Saisissez les données d'entrée :</strong> {ei}</li>"
            "<li><strong>La calculatrice applique la formule</strong> et affiche immédiatement le résultat.</li>"
            "<li><strong>Résultat obtenu :</strong> {eo}</li>"
            "<li><strong>Vérifiez le résultat</strong> en contrôlant la cohérence des unités.</li>"
            "</ol>"
        ),
        "pt": (
            "<p>Siga estes passos para obter o resultado correto:</p>"
            "<ol>"
            "<li><strong>Introduza os dados de entrada:</strong> {ei}</li>"
            "<li><strong>A calculadora aplica a fórmula</strong> e mostra o resultado imediatamente.</li>"
            "<li><strong>Resultado obtido:</strong> {eo}</li>"
            "<li><strong>Verifique o resultado</strong> conferindo que as unidades são coerentes.</li>"
            "</ol>"
        ),
        "de": (
            "<p>Befolgen Sie diese Schritte für das richtige Ergebnis:</p>"
            "<ol>"
            "<li><strong>Geben Sie die Eingabedaten ein:</strong> {ei}</li>"
            "<li><strong>Der Rechner wendet die Formel an</strong> und zeigt sofort das Ergebnis.</li>"
            "<li><strong>Erhaltenes Ergebnis:</strong> {eo}</li>"
            "<li><strong>Überprüfen Sie das Ergebnis</strong> auf Einheitenkonsistenz.</li>"
            "</ol>"
        ),
        "it": (
            "<p>Segui questi passaggi per ottenere il risultato corretto:</p>"
            "<ol>"
            "<li><strong>Inserisci i dati di input:</strong> {ei}</li>"
            "<li><strong>La calcolatrice applica la formula</strong> e mostra immediatamente il risultato.</li>"
            "<li><strong>Risultato ottenuto:</strong> {eo}</li>"
            "<li><strong>Verifica il risultato</strong> controllando la coerenza delle unità.</li>"
            "</ol>"
        ),
    }

    interpret_p = {
        "es": (
            "Una vez obtenido el resultado, considera lo siguiente para una interpretación correcta: "
            "compara el valor con rangos de referencia estándar de tu campo, ten en cuenta que "
            "pequeñas variaciones en los datos de entrada pueden producir cambios significativos "
            "en el resultado (sensibilidad a los parámetros), y documenta siempre las condiciones "
            "en las que realizaste la medición para poder reproducir el cálculo en el futuro."
        ),
        "en": (
            "Once you have the result, consider the following for correct interpretation: "
            "compare the value with standard reference ranges in your field, note that "
            "small variations in input data can produce significant changes in the result "
            "(parameter sensitivity), and always document the conditions under which you "
            "made the measurement so you can reproduce the calculation in the future."
        ),
        "fr": (
            "Une fois le résultat obtenu, considérez ceci pour une interprétation correcte : "
            "comparez la valeur avec les plages de référence standard de votre domaine, "
            "notez que de petites variations dans les données d'entrée peuvent produire "
            "des changements significatifs dans le résultat."
        ),
        "pt": (
            "Após obter o resultado, considere o seguinte para uma interpretação correta: "
            "compare o valor com intervalos de referência padrão da sua área, note que "
            "pequenas variações nos dados de entrada podem produzir mudanças significativas "
            "no resultado."
        ),
        "de": (
            "Sobald Sie das Ergebnis haben, beachten Sie für eine korrekte Interpretation: "
            "Vergleichen Sie den Wert mit Standardreferenzbereichen in Ihrem Bereich, "
            "beachten Sie, dass kleine Variationen in den Eingabedaten zu erheblichen "
            "Änderungen im Ergebnis führen können."
        ),
        "it": (
            "Una volta ottenuto il risultato, considera quanto segue per un'interpretazione corretta: "
            "confronta il valore con gli intervalli di riferimento standard del tuo campo, "
            "nota che piccole variazioni nei dati di input possono produrre cambiamenti "
            "significativi nel risultato."
        ),
    }

    faq_q1 = {
        "es": "¿Es precisa esta calculadora?",
        "en": "Is this calculator accurate?",
        "fr": "Cette calculatrice est-elle précise ?",
        "pt": "Esta calculadora é precisa?",
        "de": "Ist dieser Rechner genau?",
        "it": "Questa calcolatrice è precisa?",
    }
    faq_a1 = {
        "es": f"Sí. La calculadora utiliza la fórmula estándar: {d['f']}. Los resultados son matemáticamente exactos; la precisión final depende de la exactitud de los datos que introduces.",
        "en": f"Yes. The calculator uses the standard formula: {d['f']}. Results are mathematically exact; final accuracy depends on the precision of the data you enter.",
        "fr": f"Oui. La calculatrice utilise la formule standard : {d['f']}. Les résultats sont mathématiquement exacts.",
        "pt": f"Sim. A calculadora usa a fórmula padrão: {d['f']}. Os resultados são matematicamente exatos.",
        "de": f"Ja. Der Rechner verwendet die Standardformel: {d['f']}. Die Ergebnisse sind mathematisch exakt.",
        "it": f"Sì. La calcolatrice usa la formula standard: {d['f']}. I risultati sono matematicamente esatti.",
    }
    faq_q2 = {
        "es": "¿Puedo usar esta calculadora en el móvil?",
        "en": "Can I use this calculator on my phone?",
        "fr": "Puis-je utiliser cette calculatrice sur mobile ?",
        "pt": "Posso usar esta calculadora no celular?",
        "de": "Kann ich diesen Rechner auf dem Handy nutzen?",
        "it": "Posso usare questa calcolatrice sul telefono?",
    }
    faq_a2 = {
        "es": "Sí, la calculadora es totalmente responsiva y funciona en cualquier dispositivo: ordenador, tablet y móvil. No requiere instalación ni registro.",
        "en": "Yes, the calculator is fully responsive and works on any device: computer, tablet, and mobile. No installation or registration required.",
        "fr": "Oui, la calculatrice est entièrement responsive et fonctionne sur tout appareil. Aucune installation ni inscription requise.",
        "pt": "Sim, a calculadora é totalmente responsiva e funciona em qualquer dispositivo. Não requer instalação nem cadastro.",
        "de": "Ja, der Rechner ist vollständig responsiv und funktioniert auf jedem Gerät. Keine Installation oder Anmeldung erforderlich.",
        "it": "Sì, la calcolatrice è completamente responsive e funziona su qualsiasi dispositivo. Non richiede installazione né registrazione.",
    }

    h = H.get(lang, H["en"])
    ip = intro_p.get(lang, intro_p["en"])
    sp = step_p.get(lang, step_p["en"])
    itp = interpret_p.get(lang, interpret_p["en"])
    q1, a1, q2, a2 = faq_q1.get(lang, faq_q1["en"]), faq_a1.get(lang, faq_a1["en"]), faq_q2.get(lang, faq_q2["en"]), faq_a2.get(lang, faq_a2["en"])

    h0 = h[0].format(name=calc_name) if calc_name else h[0]
    h2 = h[2].format(name=calc_name) if calc_name else h[2]
    h3 = h[3]
    h4 = h[4].format(name=calc_name) if calc_name else h[4]
    uses_html = "".join(f"<li>{u}</li>" for u in d["u"])

    return f"""<section class="long-content">
<h2>{h0}</h2>
<p>{ip.format(f=d["f"])}</p>
<h2>{h[1]}</h2>
{sp.format(ei=d["ei"], eo=d["eo"])}
<h2>{h2}</h2>
<ul>{uses_html}</ul>
<h2>{h3}</h2>
<p>{itp}</p>
<h2>{h4}</h2>
<div class="faq-list">
<div class="faq-item"><button class="faq-q" aria-expanded="false">{q1}</button><div class="faq-a"><p>{a1}</p></div></div>
<div class="faq-item"><button class="faq-q" aria-expanded="false">{q2}</button><div class="faq-a"><p>{a2}</p></div></div>
</div>
</section>"""


def generate_long_content(calc_id: str, lang: str, calc_name: str = "") -> str:
    """Return long-form SEO article for a calculator, or empty string if none."""
    entry = LONG_CONTENT.get(calc_id, {})
    result = entry.get(lang, entry.get("en", ""))
    if result:
        return result
    facts = CALC_FACTS.get(calc_id, {})
    if facts:
        return build_article_from_facts(facts, lang, calc_name=calc_name)
    return ""

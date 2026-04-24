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
        "La <strong>{name}</strong> es una herramienta gratuita diseñada para profesionales "
        "y aficionados de la construcción. {desc} "
        "Obtén al instante los materiales necesarios desglosados por unidades de compra, "
        "con opción de añadir un porcentaje de merma para no quedarte corto en obra."
    ),
    "en": (
        "The <strong>{name}</strong> is a free tool designed for construction professionals "
        "and enthusiasts. {desc} "
        "Instantly get the required materials broken down by purchase units, "
        "with an option to add a wastage allowance so you never run short on site."
    ),
    "fr": (
        "Le <strong>{name}</strong> est un outil gratuit conçu pour les professionnels "
        "et les passionnés de la construction. {desc} "
        "Obtenez instantanément les matériaux nécessaires décomposés par unités d'achat, "
        "avec la possibilité d'ajouter un taux de perte pour ne jamais manquer de matériaux sur chantier."
    ),
    "pt": (
        "A <strong>{name}</strong> é uma ferramenta gratuita projetada para profissionais "
        "e entusiastas da construção. {desc} "
        "Obtenha instantaneamente os materiais necessários detalhados por unidades de compra, "
        "com opção de adicionar uma porcentagem de perda para nunca faltar material em obra."
    ),
    "de": (
        "Der <strong>{name}</strong> ist ein kostenloses Werkzeug für Baufachleute und Heimwerker. "
        "{desc} "
        "Erhalten Sie sofort die benötigten Materialien aufgeschlüsselt nach Kaufeinheiten, "
        "mit der Möglichkeit, einen Verschnittfaktor hinzuzufügen, damit Sie auf der Baustelle nie zu kurz kommen."
    ),
    "it": (
        "Il <strong>{name}</strong> è uno strumento gratuito progettato per professionisti "
        "e appassionati dell'edilizia. {desc} "
        "Ottieni immediatamente i materiali necessari suddivisi per unità di acquisto, "
        "con la possibilità di aggiungere una percentuale di perdita per non rimanere mai a corto in cantiere."
    ),
}


def generate_intro(calc_id: str, lang: str, name: str, desc: str) -> str:
    tpl = INTRO_TEMPLATES.get(lang, INTRO_TEMPLATES["en"])
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

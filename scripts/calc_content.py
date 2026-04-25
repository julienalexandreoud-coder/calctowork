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


def generate_long_content(calc_id: str, lang: str) -> str:
    """Return long-form SEO article for a calculator, or empty string if none."""
    entry = LONG_CONTENT.get(calc_id, {})
    return entry.get(lang, entry.get("en", ""))

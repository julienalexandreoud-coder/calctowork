#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multilingual domain-specific content templates for all 6 languages.
Provides intro, how_it_works, tips, and FAQs for each calculator domain.
"""

MULTILINGUAL_DOMAIN_CONTENT = {
    "pavimentos": {
        "en": {
            "intro": "This calculator helps you determine the exact quantity of floor tiles, adhesive, and grout needed for your project.",
            "how_it_works": "The calculator divides your total floor area by the area of a single tile to determine the base number needed. It automatically adds a waste margin (typically 10%) to account for cutting losses at edges and corners, and calculates material quantities for adhesive and grout based on industry standards.",
            "tips": [
                "Always order 10-15% extra material for cutting waste and future repairs",
                "Verify all tiles come from the same manufacturing batch to ensure color consistency",
                "Plan your starting position to minimize edge cuts and create a balanced layout",
                "Use thin-set mortar for interior floors and flexible adhesive for moisture-prone areas",
                "Allow 24-48 hours for adhesive to cure completely before applying grout"
            ],
            "faq": [
                {"q": "Why do you add extra material for waste?", "a": "During installation, tiles are cut at edges and corners, creating waste. We add 10% by default for straight layouts and recommend 15% for diagonal patterns. Additional waste accounts for breakage and defective pieces that need replacement."},
                {"q": "How much adhesive do I need per square meter?", "a": "Typical coverage is 2-4 kg/m² for small tiles (<30×30cm), 4-6 kg/m² for medium tiles, and 5-8 kg/m² for large format tiles (60×60cm+). Check the manufacturer's specifications for exact coverage rates."},
                {"q": "What's the difference between grout and adhesive?", "a": "Adhesive (mortar) bonds tiles to the substrate. Grout fills the joints between tiles. Both are essential—adhesive must cure before grouting begins."},
                {"q": "Can I use different tile sizes in the same project?", "a": "Yes, but mixing sizes requires careful planning. Larger tiles appear more spacious but show imperfections; smaller tiles hide irregularities. Plan your layout carefully to create a balanced, professional result."}
            ]
        },
        "es": {
            "intro": "Esta calculadora te ayuda a determinar la cantidad exacta de baldosas, adhesivo y lechada necesarios para tu proyecto de pavimentación.",
            "how_it_works": "La calculadora divide el área total del piso entre el área de una baldosa individual para obtener la cantidad base necesaria. Automáticamente añade un margen de desperdicio (típicamente 10%) para contabilizar los cortes en bordes y esquinas, y calcula las cantidades de adhesivo y lechada según los estándares de la industria.",
            "tips": [
                "Siempre pide un 10-15% extra de material para cubrir desperdicios de corte y reparaciones futuras",
                "Verifica que todas las baldosas provengan del mismo lote de fabricación para garantizar uniformidad de color",
                "Planifica tu posición inicial para minimizar cortes en los bordes y crear un diseño balanceado",
                "Utiliza mortero de capa fina para pisos interiores y adhesivo flexible para áreas con humedad",
                "Deja que el adhesivo cure 24-48 horas completamente antes de aplicar la lechada"
            ],
            "faq": [
                {"q": "¿Por qué se añade material extra para desperdicio?", "a": "Durante la instalación, las baldosas se cortan en bordes y esquinas, creando desperdicio. Añadimos 10% por defecto para disposiciones rectas y recomendamos 15% para patrones diagonales. El desperdicio adicional contabiliza roturas y piezas defectuosas que necesitan reemplazo."},
                {"q": "¿Cuánto adhesivo necesito por metro cuadrado?", "a": "La cobertura típica es 2-4 kg/m² para baldosas pequeñas (<30×30cm), 4-6 kg/m² para medianas, y 5-8 kg/m² para grandes formatos (60×60cm+). Consulta las especificaciones del fabricante para tasas de cobertura exactas."},
                {"q": "¿Cuál es la diferencia entre lechada y adhesivo?", "a": "El adhesivo (mortero) une las baldosas al sustrato. La lechada rellena las juntas entre baldosas. Ambos son esenciales—el adhesivo debe curarse antes de aplicar la lechada."},
                {"q": "¿Puedo usar diferentes tamaños de baldosas en el mismo proyecto?", "a": "Sí, pero mezclar tamaños requiere planificación cuidadosa. Las baldosas más grandes se ven más espaciosas pero muestran imperfecciones; las más pequeñas ocultan irregularidades. Planifica tu distribución cuidadosamente para un resultado profesional y balanceado."}
            ]
        },
        "de": {
            "intro": "Dieser Rechner hilft Ihnen, die genaue Menge an Bodenfliesen, Kleber und Fugenmasse zu bestimmen, die für Ihr Projekt erforderlich ist.",
            "how_it_works": "Der Rechner teilt Ihre Gesamtbodenfläche durch die Fläche einer einzelnen Fliese, um die benötigte Basismenge zu ermitteln. Er addiert automatisch einen Verschnittzuschlag (typischerweise 10%), um Schnittverluste an Kanten und Ecken zu berücksichtigen, und berechnet die Mengen für Kleber und Fugenmasse nach Branchenstandards.",
            "tips": [
                "Bestellen Sie immer 10-15% zusätzliches Material für Verschnitt und zukünftige Reparaturen",
                "Vergewissern Sie sich, dass alle Fliesen aus der gleichen Fertigungscharge stammen, um Farbkonsistenz zu gewährleisten",
                "Planen Sie Ihre Startposition, um Randschnitte zu minimieren und ein ausgewogenes Layout zu schaffen",
                "Verwenden Sie Dünnbettmörtel für Innenböden und flexiblen Kleber für feuchtigkeitsempfindliche Bereiche",
                "Lassen Sie den Kleber vor dem Verfugen 24-48 Stunden vollständig aushärten"
            ],
            "faq": [
                {"q": "Warum wird zusätzliches Material für Verschnitt addiert?", "a": "Beim Verlegen werden Fliesen an Kanten und Ecken geschnitten, was zu Verschnitt führt. Wir addieren standardmäßig 10% für gerade Verlegung und empfehlen 15% für Diagonalverlegung. Zusätzlicher Verschnitt berücksichtigt Bruchware und fehlerhafte Teile, die ersetzt werden müssen."},
                {"q": "Wie viel Kleber benötige ich pro Quadratmeter?", "a": "Der typische Verbrauch liegt bei 2-4 kg/m² für kleine Fliesen (<30×30cm), 4-6 kg/m² für mittlere Fliesen und 5-8 kg/m² für großformatige Fliesen (60×60cm+). Konsultieren Sie die Herstellerangaben für genaue Verbrauchswerte."},
                {"q": "Was ist der Unterschied zwischen Fugenmasse und Fliesenkleber?", "a": "Fliesenkleber verbindet Fliesen mit dem Untergrund. Fugenmasse füllt die Fugen zwischen Fliesen. Beide sind unverzichtbar – der Kleber muss aushärten, bevor die Fugenmasse aufgetragen wird."},
                {"q": "Kann ich verschiedene Fliesengrößen im gleichen Projekt verwenden?", "a": "Ja, aber das Mischen von Größen erfordert sorgfältige Planung. Größere Fliesen wirken großzügiger, zeigen aber Unebenheiten deutlicher; kleinere Fliesen kaschieren Unebenheiten. Planen Sie Ihr Layout sorgfältig für ein professionelles, ausgewogenes Ergebnis."}
            ]
        },
        "fr": {
            "intro": "Cette calculatrice vous aide à déterminer la quantité exacte de carreaux de sol, de colle et de joint nécessaires pour votre projet.",
            "how_it_works": "La calculatrice divise votre surface totale de sol par la surface d'un seul carreau pour obtenir la quantité de base nécessaire. Elle ajoute automatiquement une marge de perte (généralement 10%) pour tenir compte des découpes aux bords et aux coins, et calcule les quantités de colle et de joint selon les normes industrielles.",
            "tips": [
                "Commandez toujours 10-15% de matériau supplémentaire pour les pertes de découpe et les réparations futures",
                "Vérifiez que tous les carreaux proviennent du même lot de fabrication pour assurer la cohérence des couleurs",
                "Planifiez votre position de départ pour minimiser les découpes en bordure et créer un agencement équilibré",
                "Utilisez un mortier-colle fin pour les sols intérieurs et une colle flexible pour les zones sensibles à l'humidité",
                "Laissez la colle durcir complètement 24 à 48 heures avant d'appliquer le joint"
            ],
            "faq": [
                {"q": "Pourquoi ajouter du matériau supplémentaire pour la perte?", "a": "Lors de la pose, les carreaux sont coupés aux bords et aux coins, créant une perte. Nous ajoutons 10% par défaut pour les poses droites et recommandons 15% pour les motifs en diagonale. La perte supplémentaire tient compte des cassures et des pièces défectueuses qui doivent être remplacées."},
                {"q": "Combien de colle ai-je besoin par mètre carré?", "a": "Le rendement typique est de 2-4 kg/m² pour les petits carreaux (<30×30cm), 4-6 kg/m² pour les carreaux moyens et 5-8 kg/m² pour les grands formats (60×60cm+). Consultez les spécifications du fabricant pour les rendements exacts."},
                {"q": "Quelle est la différence entre le joint et la colle à carrelage?", "a": "La colle à carrelage lie les carreaux au support. Le joint remplit les espaces entre les carreaux. Les deux sont essentiels – la colle doit durcir avant l'application du joint."},
                {"q": "Puis-je utiliser différentes tailles de carreaux dans le même projet?", "a": "Oui, mais mélanger les tailles nécessite une planification minutieuse. Les carreaux plus grands semblent plus spacieux mais montrent les imperfections; les plus petits cachent les irrégularités. Planifiez soigneusement votre agencement pour un résultat professionnel et équilibré."}
            ]
        },
        "it": {
            "intro": "Questo calcolatore ti aiuta a determinare la quantità esatta di piastrelle da pavimento, adesivo e stucco necessari per il tuo progetto.",
            "how_it_works": "Il calcolatore divide l'area totale del pavimento per l'area di una singola piastrella per ottenere la quantità base necessaria. Aggiunge automaticamente un margine di scarto (tipicamente 10%) per tenere conto dei tagli ai bordi e agli angoli, e calcola le quantità di adesivo e stucco secondo gli standard del settore.",
            "tips": [
                "Ordina sempre il 10-15% di materiale extra per coprire gli scarti di taglio e le riparazioni future",
                "Verifica che tutte le piastrelle provengono dallo stesso lotto di produzione per garantire coerenza dei colori",
                "Pianifica la tua posizione iniziale per minimizzare i tagli ai bordi e creare un layout equilibrato",
                "Usa malta collante fine per pavimenti interni e adesivo flessibile per aree sensibili all'umidità",
                "Lascia indurire completamente l'adesivo 24-48 ore prima di applicare lo stucco"
            ],
            "faq": [
                {"q": "Perché aggiungere materiale extra per lo scarto?", "a": "Durante la posa, le piastrelle vengono tagliate ai bordi e agli angoli, creando scarti. Aggiungiamo il 10% di default per la posa diritta e raccomandiamo il 15% per i motivi diagonali. Lo scarto aggiuntivo tiene conto delle rotture e dei pezzi difettosi che devono essere sostituiti."},
                {"q": "Quanto adesivo mi serve per metro quadrato?", "a": "La copertura tipica è 2-4 kg/m² per piastrelle piccole (<30×30cm), 4-6 kg/m² per medie e 5-8 kg/m² per grandi formati (60×60cm+). Consulta le specifiche del produttore per i tassi di copertura esatti."},
                {"q": "Qual è la differenza tra stucco e adesivo?", "a": "L'adesivo lega le piastrelle al supporto. Lo stucco riempie gli spazi tra le piastrelle. Entrambi sono essenziali – l'adesivo deve indurire prima di applicare lo stucco."},
                {"q": "Posso usare diverse dimensioni di piastrelle nello stesso progetto?", "a": "Sì, ma mescolare le dimensioni richiede una pianificazione attenta. Le piastrelle più grandi sembrano più spaziose ma mostrano le imperfezioni; le più piccole nascondono le irregolarità. Pianifica attentamente il tuo layout per un risultato professionale ed equilibrato."}
            ]
        },
        "pt": {
            "intro": "Esta calculadora ajuda você a determinar a quantidade exata de cerâmicas, adesivo e rejunte necessários para seu projeto.",
            "how_it_works": "A calculadora divide sua área total de piso pela área de uma única cerâmica para obter a quantidade base necessária. Ela adiciona automaticamente uma margem de desperdício (tipicamente 10%) para contabilizar os cortes nas bordas e cantos, e calcula as quantidades de adesivo e rejunte conforme os padrões da indústria.",
            "tips": [
                "Sempre solicite 10-15% de material adicional para cobrir desperdícios de corte e reparos futuros",
                "Verifique que todas as cerâmicas vêm do mesmo lote de fabricação para garantir consistência de cor",
                "Planeje sua posição inicial para minimizar cortes nas bordas e criar um layout equilibrado",
                "Use argamassa colante fina para pisos interiores e adesivo flexível para áreas sensíveis à umidade",
                "Deixe o adesivo curar completamente por 24-48 horas antes de aplicar o rejunte"
            ],
            "faq": [
                {"q": "Por que adicionar material extra para desperdício?", "a": "Durante a instalação, as cerâmicas são cortadas nas bordas e cantos, criando desperdício. Adicionamos 10% por padrão para assentamento reto e recomendamos 15% para padrões diagonais. O desperdício adicional contabiliza quebras e peças defeituosas que precisam ser substituídas."},
                {"q": "Quanto adesivo preciso por metro quadrado?", "a": "A cobertura típica é 2-4 kg/m² para cerâmicas pequenas (<30×30cm), 4-6 kg/m² para médias e 5-8 kg/m² para grandes formatos (60×60cm+). Consulte as especificações do fabricante para as taxas de cobertura exatas."},
                {"q": "Qual é a diferença entre rejunte e adesivo?", "a": "O adesivo une as cerâmicas ao substrato. O rejunte preenche os espaços entre as cerâmicas. Ambos são essenciais – o adesivo deve curar antes de aplicar o rejunte."},
                {"q": "Posso usar diferentes tamanhos de cerâmica no mesmo projeto?", "a": "Sim, mas misturar tamanhos requer planejamento cuidadoso. Cerâmicas maiores parecem mais espaçosas mas mostram imperfeições; as menores ocultam irregularidades. Planeje seu layout cuidadosamente para um resultado profissional e equilibrado."}
            ]
        }
    },
    "electricidad": {
        "en": {
            "intro": "This calculator determines the correct electrical cable size, voltage drop, and capacity for your installation based on current, distance, and system voltage.",
            "how_it_works": "The calculator applies standard electrical formulas to compute the minimum cable cross-section needed to safely carry the specified current while keeping voltage drop within acceptable limits. It accounts for copper or aluminum conductors and recommends standard commercial cable sizes.",
            "tips": [
                "Always size cables based on the maximum continuous load, not just average usage",
                "Voltage drop should not exceed 3% for branch circuits and 5% for main feeders",
                "Use copper conductors for better conductivity and longevity compared to aluminum",
                "Install cable in conduit to protect against damage and improve cooling",
                "Follow local electrical codes and regulations for your region"
            ],
            "faq": [
                {"q": "What does voltage drop mean?", "a": "Voltage drop is the reduction in voltage from the source to the load due to wire resistance. Excessive drop causes equipment to operate below rated voltage, reducing efficiency and performance. Standard practice limits it to 3-5%."},
                {"q": "Why is cable size important?", "a": "Undersized cable cannot safely handle the current, causing overheating, insulation damage, and fire risk. Oversized cable wastes material and cost. Proper sizing ensures safety, efficiency, and longevity."},
                {"q": "Is copper better than aluminum?", "a": "Yes, copper has higher conductivity (lower resistance) and better durability. Aluminum is lighter and cheaper but requires larger cross-section for the same ampacity. Most applications prefer copper."},
                {"q": "How do I calculate voltage drop?", "a": "Voltage drop = (2 × length × current × resistance) / 1000. Most tables provide resistance values per 1000m. For example, copper at 2.5mm² has ~7.41 ohms per 1000m."}
            ]
        },
        "es": {
            "intro": "Esta calculadora determina el tamaño correcto de cable eléctrico, caída de tensión y capacidad para tu instalación basándose en la corriente, distancia y voltaje del sistema.",
            "how_it_works": "La calculadora aplica fórmulas eléctricas estándar para calcular la sección mínima de cable necesaria para conducir de forma segura la corriente especificada mientras mantiene la caída de tensión dentro de los límites aceptables. Contabiliza conductores de cobre o aluminio y recomienda tamaños de cable comerciales estándar.",
            "tips": [
                "Siempre dimensiona los cables basándote en la carga continua máxima, no solo en el uso promedio",
                "La caída de tensión no debe exceder 3% para circuitos derivados y 5% para alimentadores principales",
                "Utiliza conductores de cobre para mejor conductividad y durabilidad en comparación con aluminio",
                "Instala el cable en conducto para protegerlo contra daños y mejorar el enfriamiento",
                "Sigue los códigos y regulaciones eléctricas locales de tu región"
            ],
            "faq": [
                {"q": "¿Qué significa caída de tensión?", "a": "La caída de tensión es la reducción en voltaje desde la fuente hasta la carga debido a la resistencia del cable. La caída excesiva causa que los equipos operen por debajo del voltaje nominal, reduciendo eficiencia y rendimiento. La práctica estándar la limita al 3-5%."},
                {"q": "¿Por qué es importante el tamaño del cable?", "a": "Un cable subdimensionado no puede conducir de forma segura la corriente, causando sobrecalentamiento, daño del aislamiento y riesgo de fuego. Un cable sobredimensionado desperdicia material y costo. El dimensionamiento correcto asegura seguridad, eficiencia y durabilidad."},
                {"q": "¿Es mejor el cobre que el aluminio?", "a": "Sí, el cobre tiene mayor conductividad (menor resistencia) y mejor durabilidad. El aluminio es más ligero y económico pero requiere una sección más grande para la misma capacidad. La mayoría de aplicaciones prefieren cobre."},
                {"q": "¿Cómo calculo la caída de tensión?", "a": "Caída de tensión = (2 × longitud × corriente × resistencia) / 1000. La mayoría de tablas proporcionan valores de resistencia por 1000m. Por ejemplo, cobre de 2,5mm² tiene ~7,41 ohmios por 1000m."}
            ]
        },
        "de": {
            "intro": "Dieser Rechner bestimmt die richtige Kabelgröße, Spannungsfall und Kapazität für Ihre Installation basierend auf Strom, Entfernung und Systemspannung.",
            "how_it_works": "Der Rechner wendet Standard-Elektroformeln an, um den minimalen Kabelquerschnitt zu berechnen, der erforderlich ist, um den angegebenen Strom sicher zu führen und gleichzeitig den Spannungsfall innerhalb akzeptabler Grenzen zu halten. Er berücksichtigt Kupfer- oder Aluminium-Leiter und empfiehlt Standard-Handelskabelgrößen.",
            "tips": [
                "Dimensionieren Sie Kabel immer basierend auf der maximalen Dauerlast, nicht nur auf die durchschnittliche Nutzung",
                "Der Spannungsfall sollte 3% für Nebenschaltkreise und 5% für Hauptleitungen nicht überschreiten",
                "Verwenden Sie Kupferleiter für bessere Leitfähigkeit und Haltbarkeit im Vergleich zu Aluminium",
                "Installieren Sie Kabel in Leerrohren, um sie vor Beschädigungen zu schützen und die Kühlung zu verbessern",
                "Befolgen Sie lokale elektrische Vorschriften und Bestimmungen für Ihre Region"
            ],
            "faq": [
                {"q": "Was bedeutet Spannungsfall?", "a": "Der Spannungsfall ist die Spannungsabnahme von der Quelle bis zur Last aufgrund des Leitungswiderstands. Ein übermäßiger Fall verursacht, dass Geräte unterhalb der Nominalspannung arbeiten, was die Effizienz und Leistung vermindert. Die Standardpraxis begrenzt ihn auf 3-5%."},
                {"q": "Warum ist die Kabelgröße wichtig?", "a": "Ein untergroßes Kabel kann den Strom nicht sicher führen, was zu Überhitzung, Isolationsschaden und Brandrisiko führt. Ein übergroßes Kabel verschwendet Material und Kosten. Richtige Dimensionierung gewährleistet Sicherheit, Effizienz und Haltbarkeit."},
                {"q": "Ist Kupfer besser als Aluminium?", "a": "Ja, Kupfer hat höhere Leitfähigkeit (niedrigerer Widerstand) und bessere Haltbarkeit. Aluminium ist leichter und billiger, erfordert aber größere Querschnitte für die gleiche Stromtragfähigkeit. Die meisten Anwendungen bevorzugen Kupfer."},
                {"q": "Wie berechne ich den Spannungsfall?", "a": "Spannungsfall = (2 × Länge × Strom × Widerstand) / 1000. Die meisten Tabellen geben Widerstandswerte pro 1000m an. Zum Beispiel hat Kupfer 2,5mm² etwa 7,41 Ohm pro 1000m."}
            ]
        },
        "fr": {
            "intro": "Cette calculatrice détermine la taille correcte du câble électrique, la chute de tension et la capacité pour votre installation en fonction du courant, de la distance et de la tension du système.",
            "how_it_works": "La calculatrice applique des formules électriques standard pour calculer la section minimale de câble nécessaire pour transporter en toute sécurité le courant spécifié tout en gardant la chute de tension dans les limites acceptables. Elle tient compte des conducteurs en cuivre ou en aluminium et recommande des tailles de câble commercial standard.",
            "tips": [
                "Dimensionnez toujours les câbles en fonction de la charge continue maximale, pas seulement de l'utilisation moyenne",
                "La chute de tension ne doit pas dépasser 3% pour les circuits dérivés et 5% pour les alimentations principales",
                "Utilisez des conducteurs en cuivre pour une meilleure conductivité et durabilité par rapport à l'aluminium",
                "Installez le câble dans une gaine de protection pour le protéger contre les dommages et améliorer le refroidissement",
                "Respectez les codes et réglementations électriques locaux de votre région"
            ],
            "faq": [
                {"q": "Qu'est-ce que la chute de tension?", "a": "La chute de tension est la réduction de tension de la source à la charge due à la résistance du câble. Une chute excessive fait fonctionner l'équipement en dessous de la tension nominale, réduisant l'efficacité et les performances. La pratique standard la limite à 3-5%."},
                {"q": "Pourquoi la taille du câble est-elle importante?", "a": "Un câble sous-dimensionné ne peut pas transporter le courant en toute sécurité, causant une surchauffe, une détérioration de l'isolation et un risque d'incendie. Un câble sur-dimensionné gaspille du matériau et de l'argent. Un dimensionnement correct assure la sécurité, l'efficacité et la durabilité."},
                {"q": "Le cuivre est-il meilleur que l'aluminium?", "a": "Oui, le cuivre a une conductivité plus élevée (résistance plus faible) et une meilleure durabilité. L'aluminium est plus léger et moins cher mais nécessite une section plus grande pour la même capacité. La plupart des applications préfèrent le cuivre."},
                {"q": "Comment calculer la chute de tension?", "a": "Chute de tension = (2 × longueur × courant × résistance) / 1000. La plupart des tables fournissent des valeurs de résistance pour 1000m. Par exemple, le cuivre de 2,5mm² a environ 7,41 ohms par 1000m."}
            ]
        },
        "it": {
            "intro": "Questo calcolatore determina la corretta sezione del cavo elettrico, la caduta di tensione e la capacità per la tua installazione in base a corrente, distanza e tensione del sistema.",
            "how_it_works": "Il calcolatore applica formule elettriche standard per calcolare la sezione minima di cavo necessaria per trasportare in sicurezza la corrente specificata mantenendo la caduta di tensione entro i limiti accettabili. Tiene conto dei conduttori in rame o alluminio e consiglia sezioni di cavo commerciali standard.",
            "tips": [
                "Dimensiona sempre i cavi in base al carico continuo massimo, non solo all'uso medio",
                "La caduta di tensione non deve superare il 3% per i circuiti derivati e il 5% per gli alimentatori principali",
                "Usa conduttori in rame per migliore conduttività e durabilità rispetto all'alluminio",
                "Installa il cavo in condotti per proteggerlo dai danni e migliorare il raffreddamento",
                "Segui i codici e le normative elettriche locali della tua regione"
            ],
            "faq": [
                {"q": "Cosa significa caduta di tensione?", "a": "La caduta di tensione è la riduzione di tensione dalla fonte al carico a causa della resistenza del cavo. Una caduta eccessiva fa funzionare l'apparecchiatura al di sotto della tensione nominale, riducendo l'efficienza e le prestazioni. La pratica standard la limita al 3-5%."},
                {"q": "Perché la sezione del cavo è importante?", "a": "Un cavo sottodimensionato non può trasportare la corrente in sicurezza, causando surriscaldamento, danni all'isolamento e rischio di incendio. Un cavo sovradimensionato spreca materiale e denaro. Il corretto dimensionamento assicura sicurezza, efficienza e durabilità."},
                {"q": "Il rame è migliore dell'alluminio?", "a": "Sì, il rame ha conduttività più elevata (resistenza inferiore) e migliore durabilità. L'alluminio è più leggero ed economico ma richiede sezioni più grandi per la stessa portata di corrente. La maggior parte delle applicazioni preferisce il rame."},
                {"q": "Come calcolo la caduta di tensione?", "a": "Caduta di tensione = (2 × lunghezza × corrente × resistenza) / 1000. La maggior parte delle tabelle fornisce valori di resistenza per 1000m. Ad esempio, il rame 2,5mm² ha circa 7,41 ohm per 1000m."}
            ]
        },
        "pt": {
            "intro": "Esta calculadora determina o tamanho correto do cabo elétrico, queda de tensão e capacidade para sua instalação com base na corrente, distância e tensão do sistema.",
            "how_it_works": "A calculadora aplica fórmulas elétricas padrão para calcular a seção mínima de cabo necessária para transportar com segurança a corrente especificada, mantendo a queda de tensão dentro dos limites aceitáveis. Ela contabiliza condutores de cobre ou alumínio e recomenda tamanhos de cabo comerciais padrão.",
            "tips": [
                "Sempre dimensione cabos com base na carga contínua máxima, não apenas no uso médio",
                "A queda de tensão não deve exceder 3% para circuitos derivados e 5% para alimentadores principais",
                "Use condutores de cobre para melhor condutividade e durabilidade em comparação com alumínio",
                "Instale o cabo em conduítes para protegê-lo contra danos e melhorar o resfriamento",
                "Siga os códigos e regulamentos elétricos locais de sua região"
            ],
            "faq": [
                {"q": "O que é queda de tensão?", "a": "Queda de tensão é a redução de tensão da fonte para a carga devido à resistência do cabo. A queda excessiva causa que o equipamento funcione abaixo da tensão nominal, reduzindo eficiência e desempenho. A prática padrão a limita a 3-5%."},
                {"q": "Por que o tamanho do cabo é importante?", "a": "Um cabo subdimensionado não pode transportar a corrente com segurança, causando superaquecimento, dano de isolamento e risco de incêndio. Um cabo superdimensionado desperdiça material e custo. O dimensionamento correto garante segurança, eficiência e durabilidade."},
                {"q": "O cobre é melhor que o alumínio?", "a": "Sim, o cobre tem condutividade mais alta (resistência mais baixa) e melhor durabilidade. O alumínio é mais leve e econômico, mas requer seções maiores para a mesma capacidade. A maioria das aplicações prefere cobre."},
                {"q": "Como calculo a queda de tensão?", "a": "Queda de tensão = (2 × comprimento × corrente × resistência) / 1000. A maioria das tabelas fornece valores de resistência por 1000m. Por exemplo, cobre de 2,5mm² tem aproximadamente 7,41 ohms por 1000m."}
            ]
        }
    }
}

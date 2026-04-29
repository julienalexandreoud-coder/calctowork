const fs = require('fs');

// Read source file
const data = JSON.parse(fs.readFileSync('src/calculators/calculators.json', 'utf8'));

// Translation dictionary for common construction terms
const dict = {
  // Common words
  'Calcular': 'Berechnen',
  'calcular': 'berechnen',
  'materiales': 'Materialien',
  'para': 'für',
  'una': 'eine',
  'un': 'einen',
  'losa': 'Bodenplatte',
  'hormigón': 'Beton',
  'hormigón armado': 'Stahlbeton',
  'de': 'aus',
  'y': 'und',
  'Medida': 'Maß',
  'típica': 'typisch',
  'según': 'nach',
  'el': 'dem',
  'proyecto': 'Projekt',
  'Espesor': 'Dicke',
  'requerida': 'erforderlich',
  'Resistencia': 'Festigkeit',
  'Resultados': 'Ergebnisse',
  'sacos': 'Säcke',
  'cemento': 'Zement',
  'arena': 'Sand',
  'grava': 'Kies',
  'acero': 'Stahl',
  'Volumen': 'Volumen',
  'largo': 'Länge',
  'ancho': 'Breite',
  'espesor': 'Dicke',
  'área': 'Fläche',
  'Multiplicar': 'Multiplizieren',
  'Calcular': 'Berechnen',
  'Usar': 'Verwenden',
  'espesor insuficiente': 'unzureichende Dicke',
  'puede causar': 'kann verursachen',
  'grietas': 'Risse',
  'No considerar': 'Nicht berücksichtigen',
  'desperdicio': 'Verschnitt',
  'Confundir': 'Verwechseln',
  'metros cúbicos': 'Kubikmeter',
  'con': 'mit',
  'metros cuadrados': 'Quadratmeter',
  'No verificar': 'Nicht überprüfen',
  'las medidas': 'die Maße',
  'antes': 'vor',
  'margen': 'Marge',
  'error': 'Fehler',
  'No consultar': 'Nicht konsultieren',
  'normativas': 'Vorschriften',
  'o': 'oder',
  'estándares': 'Standards',
  'aplicables': 'anwendbar',
  'según plano': 'gemäß Plan',
  'Número': 'Anzahl',
  'unidades': 'Einheiten',
  'necesarias': 'erforderlich',
  'por': 'pro',
  'unidad': 'Einheit',
  'encofrado': 'Schalung',
  'No aumentar': 'Nicht vergrößern',
  'tamaño': 'Größe',
  'suelo': 'Boden',
  'baja': 'niedriger',
  'capacidad': 'Kapazität',
  'Omitir': 'Auslassen',
  'espera': 'Warte',
  'pilar': 'Pfeiler',
  'No considerar': 'Nicht berücksichtigen',
  'solado': 'Sohle',
  'limpieza': 'Reinigung',
  'Altura': 'Höhe',
  'requerimientos': 'Anforderungen',
  'Medida lineal': 'Linearmaß',
  'longitud': 'Länge',
  'total': 'gesamt',
  'requerida': 'erforderlich',
  'Profundidad': 'Tiefe',
  'necesidad': 'Bedarf',
  'sección': 'Querschnitt',
  'Viga': 'Träger',
  'vigas': 'Träger',
  'canto': 'Höhe',
  'Intereje': 'Achsabstand',
  'Forjado': 'Decke',
  'vigas': 'Balken',
  'bovedillas': 'Hohlkörper',
  'capa': 'Schicht',
  'compresión': 'Druck',
  'Identificar': 'Identifizieren',
  'valores': 'Werte',
  'entrada': 'Eingabe',
  'Aplicar': 'Anwenden',
  'fórmula': 'Formel',
  'correspondiente': 'entsprechend',
  'Realizar': 'Durchführen',
  'cálculos': 'Berechnungen',
  'paso': 'Schritt',
  'Verificar': 'Überprüfen',
  'unidades': 'Einheiten',
  'medida': 'Maß',
  'Obtener': 'Erhalten',
  'resultado': 'Ergebnis',
  'final': 'endgültig',
  'cimientos': 'Fundamente',
  'corrida': 'Streifen',
  'excavación': 'Aushub',
  'tierra': 'Erde',
  'pilar': 'Säule',
  'zapatas': 'Einzelfundamente',
  'aislada': 'isoliert',
  'muro': 'Wand',
  'contención': 'Stütz',
  'forjado': 'Decke',
  'vigas': 'Balken',
  'losa': 'Platte',
  'cimiento': 'Fundament',
  'corrido': 'Streifenfundament',
  'excavacion': 'Aushub',
  'terra': 'Erde',
  'placa': 'Platte',
  'base': 'Basis',
  'cimentación': 'Fundament',
  'losa de cimentación': 'Fundamentplatte',
  'radier': 'Fundamentplatte',
  'escalera': 'Treppe',
  'hormigón': 'Beton',
  'escalones': 'Stufen',
  'peldaños': 'Stufen',
  'techo': 'Decke',
  'aligerado': 'leicht',
  'vigueta': 'Balken',
  'bovedilla': 'Hohlkörper',
  'muro hormigón': 'Betonwand',
  'muros': 'Wände',
  'pavimento': 'Bodenbelag',
  'impreso': 'bedruckt',
  'hormigon': 'Beton',
  'masa': 'Masse',
  'armado': 'bewehrt',
  'zapata': 'Fundament',
  'contencion': 'Stützwand',
  'pilares': 'Säulen',
  'forjado vigueta': 'Balkendecke',
  'acero': 'Stahl',
  'kg': 'kg',
  'm³': 'm³',
  'm²': 'm²',
  'ud': 'Stk',
  'sacos 50kg': '50kg-Säcke',
  'valor': 'Wert',
  'especificaciones': 'Spezifikationen',
  'del': 'des',
  'según': 'gemäß',
  'Resultados:': 'Ergebnisse:',
  'por unidad': 'pro Einheit',
  'de': 'von',
  'la': 'der',
  'los': 'die',
  'las': 'die',
  'necesario': 'erforderlich',
  'necesaria': 'erforderliche',
  'necesarias': 'erforderliche',
  'necesarios': 'erforderliche',
  'según necesidad': 'nach Bedarf',
  'según requerimientos': 'nach Anforderungen',
  'según resistencia': 'nach Festigkeit',
  'según especificaciones': 'nach Spezifikationen'
};

// Function to translate text
function translate(text) {
  if (!text) return text;
  
  let result = text;
  
  // Sort dictionary by length (longest first) to avoid partial replacements
  const sortedKeys = Object.keys(dict).sort((a, b) => b.length - a.length);
  
  for (const key of sortedKeys) {
    const regex = new RegExp(key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
    result = result.replace(regex, dict[key]);
  }
  
  // Fix common patterns
  result = result.replace(/\d+m\s*×\s*\d+m/g, match => {
    return match.replace(/×/g, '×');
  });
  
  // Fix "m × m × m" patterns - keep numbers, translate units context
  result = result.replace(/(\d+\.?\d*)\s*m\s*×\s*(\d+\.?\d*)\s*m\s*×\s*(\d+\.?\d*)\s*m/g, '$1 m × $2 m × $3 m');
  
  // Fix "m³ de" patterns
  result = result.replace(/m³\s*de\s+/g, 'm³ ');
  
  // Clean up double spaces
  result = result.replace(/\s+/g, ' ');
  
  return result.trim();
}

// Process calculators
const output = {
  calculators: []
};

for (const calc of data.calculators) {
  const translated = {
    id: calc.id,
    slug: calc.slug,
    example_label: translate(calc.example_label),
    range_hints: {},
    result_context: translate(calc.result_context),
    formula_display: translate(calc.formula_display),
    steps: calc.steps.map(s => translate(s)),
    mistakes: calc.mistakes.map(m => translate(m)),
    input_type_review: calc.input_type_review.map(itr => ({
      field_id: itr.field_id,
      current_type: itr.current_type,
      recommended_type: itr.recommended_type,
      reason: translate(itr.reason)
    }))
  };
  
  // Translate range_hints
  for (const [key, value] of Object.entries(calc.range_hints)) {
    translated.range_hints[key] = translate(value);
  }
  
  output.calculators.push(translated);
}

// Write output with UTF-8 encoding (no BOM)
fs.writeFileSync('i18n_de.json', JSON.stringify(output, null, 2), 'utf8');

console.log(`Translated ${output.calculators.length} calculators to German`);
console.log('Output saved to i18n_de.json');

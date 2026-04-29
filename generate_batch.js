const fs = require('fs');

const calculatorsData = require('./src/calculators/calculators.json');

function generateCalculatorData(calc) {
  const id = calc.id;
  const slug = calc.slug;
  const inputs = calc.inputs;
  
  // Get input field names and defaults
  const inputFields = {};
  inputs.forEach(inp => {
    if (inp.type === 'number') {
      inputFields[inp.id] = inp.default || inp.min || 1;
    } else if (inp.type === 'select') {
      inputFields[inp.id] = inp.default || inp.options[0];
    }
  });

  // Domain-specific data based on calculator slug
  const domainData = getDomainData(slug, inputs, inputFields);
  
  return {
    id: calc.id,
    slug: calc.slug,
    example_inputs: domainData.example_inputs,
    example_label: domainData.example_label,
    range_hints: domainData.range_hints,
    result_context: domainData.result_context,
    formula_display: domainData.formula_display,
    steps: domainData.steps,
    mistakes: domainData.mistakes,
    input_type_review: domainData.input_type_review
  };
}

function getDomainData(slug, inputs, inputFields) {
  const data = {
    example_inputs: {},
    example_label: '',
    range_hints: {},
    result_context: '',
    formula_display: '',
    steps: [],
    mistakes: [],
    input_type_review: []
  };

  // Build example_inputs from defaults
  inputs.forEach(inp => {
    if (inp.type === 'number') {
      data.example_inputs[inp.id] = inp.default || inp.min || 1;
    } else if (inp.type === 'select') {
      data.example_inputs[inp.id] = inp.default || inp.options[0];
    }
  });

  // Domain-specific content by slug
  const domainConfig = DOMAIN_CONFIG[slug] || DOMAIN_CONFIG.default;
  
  data.example_label = domainConfig.example_label(inputs, data.example_inputs);
  
  // Build range_hints for number inputs
  inputs.forEach(inp => {
    if (inp.type === 'number') {
      data.range_hints[inp.id] = domainConfig.range_hints[inp.id] || `Rango válido: ${inp.min}-${inp.max} ${inp.unit || ''}`;
    }
  });
  
  data.result_context = domainConfig.result_context;
  data.formula_display = domainConfig.formula_display;
  data.steps = domainConfig.steps;
  data.mistakes = domainConfig.mistakes;
  
  // Build input_type_review
  data.input_type_review = inputs.map(inp => ({
    field_id: inp.id,
    current_type: inp.type,
    recommended_type: inp.type === 'select' ? 'select' : (inp.step === 1 && inp.max <= 100 ? 'number' : 'number'),
    reason: inp.type === 'select' ? 'Correcto: opción discreta' : 'Correcto: valor continuo con decimales'
  }));

  return data;
}

const DOMAIN_CONFIG = {
  'hormigon-masa': {
    example_label: () => 'Calcular el hormigón necesario para una losa de cimentación de 5m de largo por 3m de ancho con 20cm de espesor.',
    range_hints: {
      largo: 'Medida típica: 3-10m para losas residenciales',
      ancho: 'Medida típica: 2-5m para losas residenciales',
      espesor: 'Mínimo 0.15m para cargas ligeras, 0.20-0.30m para cargas normales'
    },
    result_context: 'El volumen calculado de {volumen} m³ requiere {cemento_sacos} sacos de cemento, {arena_m3} m³ de arena y {grava_m3} m³ de grava para una mezcla de resistencia estándar.',
    formula_display: 'Volumen = largo × ancho × espesor',
    steps: [
      'Multiplicar 5m × 3m = 15m² de área superficial',
      'Multiplicar 15m² × 0.20m = 3m³ de volumen de hormigón',
      'Calcular materiales: 3m³ × 7 sacos/m³ = 21 sacos de cemento',
      'Calcular arena: 3m³ × 0.65 = 1.95m³ de arena',
      'Calcular grava: 3m³ × 0.90 = 2.70m³ de grava'
    ],
    mistakes: [
      'Usar espesor insuficiente (menos de 15cm) que puede causar grietas bajo carga',
      'No considerar el 5-10% de desperdicio por derrames y nivelación',
      'Confundir metros cúbicos con metros cuadrados al pedir el hormigón'
    ]
  },
  'hormigon-armado': {
    example_label: () => 'Calcular materiales para una losa de hormigón armado de 6m × 4m con 25cm de espesor y densidad de acero de 120 kg/m³.',
    range_hints: {
      largo: 'Para losas estructurales: 4-12m típicamente',
      ancho: 'Para losas estructurales: 3-8m típicamente',
      espesor: 'Losas armadas: 0.20-0.40m según cargas y luces',
      kg_acero_m3: 'Vigas: 100-150 kg/m³, Losas: 80-120 kg/m³, Cimentaciones: 60-100 kg/m³'
    },
    result_context: 'Para {volumen} m³ de hormigón armado se necesitan {cemento_sacos} sacos de cemento, {arena_m3} m³ de arena, {grava_m3} m³ de grava y {acero_kg} kg de acero de refuerzo.',
    formula_display: 'Volumen = largo × ancho × espesor; Acero = volumen × kg_acero_m³',
    steps: [
      'Calcular área: 6m × 4m = 24m²',
      'Calcular volumen: 24m² × 0.25m = 6m³ de hormigón',
      'Calcular cemento: 6m³ × 7 sacos/m³ = 42 sacos',
      'Calcular acero: 6m³ × 120 kg/m³ = 720 kg de acero',
      'Calcular agregados: 6m³ × 0.55 = 3.30m³ arena, 6m³ × 0.80 = 4.80m³ grava'
    ],
    mistakes: [
      'Subestimar la densidad de acero para elementos estructurales críticos',
      'No verificar que el recubrimiento mínimo del acero sea 3-4cm',
      'Olvidar que el hormigón armado requiere vibrado adecuado para compactar'
    ]
  },
  'zapata-aislada': {
    example_label: () => 'Calcular hormigón y encofrado para 4 zapatas aisladas de 1.5m × 1.5m con 50cm de canto (altura).',
    range_hints: {
      largo: 'Zapatas típicas: 1.0-2.5m según carga del pilar',
      ancho: 'Zapatas cuadradas o rectangulares: 1.0-2.5m',
      canto: 'Altura típica: 0.40-0.80m según capacidad portante del suelo',
      cantidad: 'Número de pilares a cimentar en la estructura'
    },
    result_context: 'Cada zapata requiere {vol_unitario} m³ de hormigón. Para {cantidad} zapatas: {vol_total} m³ total, {cemento_sacos} sacos de cemento, {acero_kg} kg de acero y {encofrado_m2} m² de encofrado.',
    formula_display: 'Vol_unitario = largo × ancho × canto; Vol_total = vol_unitario × cantidad',
    steps: [
      'Calcular volumen unitario: 1.5m × 1.5m × 0.5m = 1.125 m³ por zapata',
      'Calcular volumen total: 1.125m³ × 4 = 4.5m³ de hormigón',
      'Calcular cemento: 4.5m³ × 7 = 31.5 → 32 sacos',
      'Calcular acero de refuerzo: 4.5m³ × 120 kg/m³ = 540 kg',
      'Calcular encofrado: perímetro × altura × cantidad = 2(1.5+0.5)×0.5×4 = 8m²'
    ],
    mistakes: [
      'No aumentar el tamaño de la zapata cuando el suelo tiene baja capacidad portante',
      'Omitir el acero de espera para conectar con el pilar',
      'No considerar el solado de limpieza de 10cm debajo de la zapata'
    ]
  },
  'muro-contencion': {
    example_label: () => 'Calcular materiales para un muro de contención de gravedad de 10m de longitud, 2m de altura, 40cm en la base y 30cm en la corona.',
    range_hints: {
      largo: 'Longitud total del muro a construir',
      altura: 'Muros residenciales: 1-3m, Muros estructurales: hasta 6m',
      espesor_base: 'Generalmente 0.4-0.6 × altura para muros de gravedad',
      espesor_corona: 'Mínimo 0.25-0.30m para resistencia estructural'
    },
    result_context: 'El muro de {vol_muro} m³ requiere {cemento_sacos} sacos de cemento, {acero_kg} kg de acero, {encofrado_m2} m² de encofrado. Volumen estimado de losa de cimentación: {vol_losa_cim} m³.',
    formula_display: 'Volumen = largo × altura × (espesor_base + espesor_corona) ÷ 2',
    steps: [
      'Calcular espesor promedio: (0.4m + 0.3m) ÷ 2 = 0.35m',
      'Calcular volumen del muro: 10m × 2m × 0.35m = 7m³',
      'Calcular cemento: 7m³ × 7 = 49 sacos',
      'Calcular acero: 7m³ × 90 kg/m³ = 630 kg',
      'Calcular encofrado (doble cara): 10m × 2m × 2 = 40m²'
    ],
    mistakes: [
      'No inclinar el muro hacia el terreno (debería tener ligera inclinación)',
      'Omitir drenajes y filtros detrás del muro para evitar presión hidrostática',
      'Usar espesor de corona insuficiente que reduce la estabilidad'
    ]
  },
  'pilares-hormigon': {
    example_label: () => 'Calcular materiales para 6 pilares de hormigón armado de sección 30×30cm y 3m de altura.',
    range_hints: {
      ancho: 'Pilares típicos: 0.25-0.50m según cargas',
      profundidad: 'Pilares cuadrados o rectangulares: 0.25-0.50m',
      altura: 'Altura de planta típica: 2.5-3.5m',
      cantidad: 'Número total de pilares en la estructura'
    },
    result_context: 'Cada pilar requiere {vol_unitario} m³. Total para {cantidad} pilares: {vol_total} m³ de hormigón, {cemento_sacos} sacos de cemento, {acero_kg} kg de acero y {encofrado_m2} m² de encofrado.',
    formula_display: 'Vol_unitario = ancho × profundidad × altura; Vol_total = vol_unitario × cantidad',
    steps: [
      'Calcular volumen unitario: 0.30m × 0.30m × 3m = 0.27m³ por pilar',
      'Calcular volumen total: 0.27m³ × 6 = 1.62m³',
      'Calcular cemento: 1.62m³ × 7 = 11.34 → 12 sacos',
      'Calcular acero: 1.62m³ × 160 kg/m³ = 259 kg',
      'Calcular encofrado: 4 caras × 0.30m × 3m × 6 = 21.6m²'
    ],
    mistakes: [
      'No considerar la longitud de solape de las barras verticales en empalmes',
      'Usar estribos con separación excesiva (deberían ir más juntos en extremos)',
      'Omitir recubrimiento mínimo de 3cm para proteger el acero'
    ]
  },
  'vigas-hormigon': {
    example_label: () => 'Calcular materiales para 4 vigas de hormigón armado de 25cm de ancho, 50cm de canto y 5m de longitud.',
    range_hints: {
      ancho: 'Vigas típicas: 0.20-0.40m según luz y cargas',
      canto: 'Relación luz/canto ≈ 12-15: para 5m de luz, canto ≈ 0.35-0.45m',
      longitud: 'Longitud de la viga entre apoyos',
      cantidad: 'Número de vigas del mismo tipo'
    },
    result_context: 'Cada viga requiere {vol_unitario} m³. Total: {vol_total} m³ de hormigón, {cemento_sacos} sacos de cemento, {acero_kg} kg de acero y {encofrado_m2} m² de encofrado.',
    formula_display: 'Vol_unitario = ancho × canto × longitud; Vol_total = vol_unitario × cantidad',
    steps: [
      'Calcular volumen unitario: 0.25m × 0.50m × 5m = 0.625m³ por viga',
      'Calcular volumen total: 0.625m³ × 4 = 2.5m³',
      'Calcular cemento: 2.5m³ × 7 = 17.5 → 18 sacos',
      'Calcular acero: 2.5m³ × 140 kg/m³ = 350 kg',
      'Calcular encofrado: 2(0.25+0.50)×5×4 = 30m² (sin contar base si apoya sobre muro)'
    ],
    mistakes: [
      'No calcular correctamente el canto según la luz (vigas muy esbeltas se deforman)',
      'Colocar mal el acero de tracción (debe ir en la zona inferior en vigas simplemente apoyadas)',
      'No prever anclajes adecuados en los apoyos de la viga'
    ]
  },
  'forjado-vigueta': {
    example_label: () => 'Calcular viguetas y bovedillas para un forjado de 8m × 6m con intereje de 70cm y canto de 25cm.',
    range_hints: {
      largo: 'Luz del forjado en dirección de viguetas',
      ancho: 'Ancho del forjado perpendicular a viguetas',
      intereje: 'Estándar: 0.60-0.80m entre ejes de viguetas',
      canto_forjado: 'Forjados unidireccionales: 0.20-0.30m según luz'
    },
    result_context: 'Para {area_m2} m² de forjado se necesitan {viguetas} viguetas, {bovedillas_ud} bovedillas, {vol_capa_comp} m³ de capa de compresión y {cemento_sacos} sacos de cemento.',
    formula_display: 'Viguetas = ancho ÷ intereje + 1; Área = largo × ancho',
    steps: [
      'Calcular área del forjado: 8m × 6m = 48m²',
      'Calcular número de viguetas: 6m ÷ 0.70m + 1 = 9.57 → 10 viguetas',
      'Calcular bovedillas: 48m² ÷ (0.70m × 0.25m) ≈ 274 unidades',
      'Calcular volumen capa de compresión: 48m² × 0.04m = 1.92m³ (aprox)',
      'Calcular cemento para capa: 1.92m³ × 7 ≈ 14 sacos'
    ],
    mistakes: [
      'No considerar vigueta adicional en extremos y bordes',
      'Colocar mal la malla de reparto sobre la capa de compresión',
      'No prever apuntalamiento adecuado durante el fraguado'
    ]
  },
  'losa-hormigon': {
    example_label: () => 'Calcular materiales para una losa de hormigón armado de 6m × 4m con 20cm de espesor y 12 kg/m² de acero.',
    range_hints: {
      largo: 'Losas de entrepiso: 4-10m típicamente',
      ancho: 'Losas de entrepiso: 3-8m típicamente',
      espesor: 'Losas macizas: 0.15-0.25m según luz y cargas',
      kg_acero_m2: 'Losas livianas: 8-12 kg/m², Losas pesadas: 15-25 kg/m²'
    },
    result_context: 'Para {area_m2} m² de losa se necesitan {vol_m3} m³ de hormigón, {cemento_sacos} sacos de cemento y {acero_kg} kg de acero de refuerzo.',
    formula_display: 'Área = largo × ancho; Volumen = área × espesor; Acero = área × kg_acero_m²',
    steps: [
      'Calcular área: 6m × 4m = 24m²',
      'Calcular volumen: 24m² × 0.20m = 4.8m³ de hormigón',
      'Calcular cemento: 4.8m³ × 7 = 33.6 → 34 sacos',
      'Calcular acero: 24m² × 12 kg/m² = 288 kg',
      'Calcular encofrado lateral según perímetro'
    ],
    mistakes: [
      'Usar espesor insuficiente que causa flechas excesivas',
      'No colocar acero de reparto en dirección perpendicular al principal',
      'Omitir separadores para mantener el recubrimiento del acero'
    ]
  },
  'cimiento-corrido': {
    example_label: () => 'Calcular excavación y hormigón para un cimiento corrido de 20m de longitud, 60cm de ancho y 50cm de profundidad.',
    range_hints: {
      longitud: 'Suma de longitudes de todos los muros cimentados',
      ancho: 'Cimientos típicos: 0.50-1.00m según carga y suelo',
      profundidad: 'Por debajo de línea de helada: 0.50-1.50m mínimo'
    },
    result_context: 'Se requieren {vol_m3} m³ de hormigón, {cemento_sacos} sacos de cemento, {arena_m3} m³ de arena, {grava_m3} m³ de grava y {acero_kg} kg de acero.',
    formula_display: 'Volumen = longitud × ancho × profundidad',
    steps: [
      'Calcular volumen de excavación: 20m × 0.60m × 0.50m = 6m³',
      'Calcular volumen de hormigón: 6m³ (asumiendo excavación exacta)',
      'Calcular cemento: 6m³ × 7 = 42 sacos',
      'Calcular arena: 6m³ × 0.65 = 3.9m³',
      'Calcular grava: 6m³ × 0.90 = 5.4m³'
    ],
    mistakes: [
      'No excavar hasta profundidad suficiente (por debajo de zona de heladas)',
      'No compactar el fondo de la excavación antes de hormigonar',
      'Usar ancho insuficiente para la capacidad portante del suelo'
    ]
  },
  'excavacion-tierra': {
    example_label: () => 'Calcular volumen de excavación para un sótano de 10m × 6m × 1.5m considerando factor de esponjamiento de 1.25.',
    range_hints: {
      largo: 'Dimensión mayor de la excavación',
      ancho: 'Dimensión menor de la excavación',
      profundidad: 'Profundidad desde nivel del terreno',
      esponjamiento: 'Tierra: 1.20-1.40, Arena: 1.10-1.20, Arcilla: 1.30-1.50'
    },
    result_context: 'Volumen neto excavado: {vol_neto_m3} m³. Volumen esponjado (para transporte): {vol_esponjado_m3} m³. Se necesitan {camiones_8m3} camiones de 8m³.',
    formula_display: 'Vol_neto = largo × ancho × profundidad; Vol_esponjado = vol_neto × factor_esponjamiento',
    steps: [
      'Calcular volumen neto: 10m × 6m × 1.5m = 90m³',
      'Aplicar factor de esponjamiento: 90m³ × 1.25 = 112.5m³',
      'Calcular camiones necesarios: 112.5m³ ÷ 8m³ = 14.06 → 15 camiones',
      'Calcular perímetro de taludes: 2(10+6)×1.5 = 48m² (para estimar entibación)'
    ],
    mistakes: [
      'No considerar el factor de esponjamiento al calcular transporte de tierra',
      'No prever taludes adecuados o entibación en excavaciones profundas',
      'Olvidar espacio adicional para encofrado de muros perimetrales'
    ]
  },
  'ladrillo-hueco': {
    example_label: () => 'Calcular ladrillos huecos para un muro de 8m × 2.8m descontando 2.5m² de huecos (puertas/ventanas).',
    range_hints: {
      largo: 'Longitud total del muro',
      alto: 'Altura libre del muro (techo o losa)',
      descontar_huecos: 'Sumar área de todas las aberturas a descontar'
    },
    result_context: 'Para un muro de {area_bruta} m² brutos ({area_neta} m² netos) se necesitan {ladrillos_ud} ladrillos huecos y {mortero_kg} kg de mortero de agarre.',
    formula_display: 'Área_bruta = largo × alto; Área_neta = área_bruta - huecos; Ladrillos = área_neta × 32 ud/m²',
    steps: [
      'Calcular área bruta del muro: 8m × 2.8m = 22.4m²',
      'Descontar huecos: 22.4m² - 2.5m² = 19.9m² de área neta',
      'Calcular ladrillos: 19.9m² × 32 ud/m² × 1.05 (merma) = 669 ladrillos',
      'Calcular mortero: 19.9m² × 8 kg/m² = 159 kg de mortero'
    ],
    mistakes: [
      'No descontar huecos de puertas y ventanas del cálculo',
      'No considerar merma del 5-10% por cortes y roturas',
      'Usar rendimiento incorrecto según tamaño del ladrillo (12×24×5cm ≈ 32 ud/m²)'
    ]
  },
  'ladrillo-cara-vista': {
    example_label: () => 'Calcular ladrillos cara vista para una fachada de 8m × 2.8m descontando 4m² de huecos.',
    range_hints: {
      largo: 'Longitud de la fachada o muro visto',
      alto: 'Altura del muro cara vista',
      descontar_huecos: 'Área total de ventanas y puertas a descontar'
    },
    result_context: 'Fachada de {area_bruta} m² brutos ({area_neta} m² netos) requiere {ladrillos_ud} ladrillos cara vista, {mortero_kg} kg de mortero y {lechada_kg} kg de lechada para juntas.',
    formula_display: 'Área_neta = (largo × alto) - huecos; Ladrillos = área_neta × 55 ud/m²',
    steps: [
      'Calcular área bruta: 8m × 2.8m = 22.4m²',
      'Restar huecos: 22.4m² - 4m² = 18.4m² netos',
      'Calcular ladrillos: 18.4m² × 55 ud/m² × 1.07 (merma 7%) = 1083 ladrillos',
      'Calcular mortero: 18.4m² × 20 kg/m² = 368 kg',
      'Calcular lechada para juntas: 18.4m² × 0.5 kg/m² = 9.2 kg'
    ],
    mistakes: [
      'No considerar merma mayor (7%) por la delicadeza del material cara vista',
      'No calcular lechada especial para juntas vistas',
      'No prever ladrillos adicionales para replanteo y cortes especiales'
    ]
  },
  'bloque-hormigon': {
    example_label: () => 'Calcular bloques de hormigón para un muro de 10m × 3m descontando 3m² de huecos.',
    range_hints: {
      largo: 'Longitud total del muro de bloques',
      alto: 'Altura del muro',
      descontar_huecos: 'Suma de áreas de aberturas'
    },
    result_context: 'Muro de {area_neta} m² requiere {bloques_ud} bloques de hormigón (40×20×20cm) y {mortero_kg} kg de mortero de agarre.',
    formula_display: 'Área_neta = (largo × alto) - huecos; Bloques = área_neta × 12.5 ud/m²',
    steps: [
      'Calcular área bruta: 10m × 3m = 30m²',
      'Descontar huecos: 30m² - 3m² = 27m² netos',
      'Calcular bloques: 27m² × 12.5 ud/m² × 1.05 (merma) = 354 bloques',
      'Calcular mortero: 27m² × 12 kg/m² = 324 kg de mortero'
    ],
    mistakes: [
      'No considerar merma por cortes en esquinas y encuentros',
      'Usar rendimiento incorrecto (bloque 40×20cm ≈ 12.5 ud/m²)',
      'No prever bloques especiales para esquinas y dinteles'
    ]
  },
  'tabique-pladur': {
    example_label: () => 'Calcular materiales para un tabique de pladur de 10m × 2.6m con doble placa y aislamiento de lana mineral.',
    range_hints: {
      largo: 'Longitud total del tabique',
      alto: 'Altura libre de suelo a techo',
      tipo_placa: 'Single: 1 capa por cara, Double: 2 capas por cara (mejor aislamiento acústico)',
      aislamiento: 'Incluir lana mineral en el interior para aislamiento térmico/acústico'
    },
    result_context: 'Tabique de {area_m2} m² requiere {placas_ud} placas de yeso, {perfiles_canal} perfiles de canal, {perfiles_montante} montantes, {tornillos_ud} tornillos, {pasta_juntas_kg} kg de pasta y {lana_mineral_m2} m² de aislamiento.',
    formula_display: 'Área = largo × alto; Placas = (área × capas) ÷ 2.88 m²/placa',
    steps: [
      'Calcular área: 10m × 2.6m = 26m²',
      'Calcular placas (doble): 26m² × 2 caras ÷ 2.88m² × 1.1 (merma) = 20 placas',
      'Calcular perfiles canal (suelo/techo): 10m × 2 × 1.1 = 22 unidades',
      'Calcular montantes (cada 0.60m): (10m ÷ 0.60m + 1) × 2 = 34 montantes',
      'Calcular tornillos: 26m² × 20 ud/m² = 520 tornillos'
    ],
    mistakes: [
      'No usar doble placa cuando se requiere aislamiento acústico',
      'Separar demasiado los montantes (máximo 0.60m)',
      'No colocar lana mineral cuando el tabique separa ambientes ruidosos'
    ]
  },
  'aislamiento-termico': {
    example_label: () => 'Calcular planchas de aislamiento térmico para una fachada de 10m × 3m con espesor de 6cm.',
    range_hints: {
      largo: 'Longitud del paramento a aislar',
      alto: 'Altura del paramento',
      espesor_cm: 'Aislamiento típico: 4-8cm fachadas, 10-20cm cubiertas'
    },
    result_context: 'Para {area_m2} m² de superficie se necesitan {plancha_m2} m² de planchas de aislamiento (con 5% de merma), equivalentes a {vol_m3} m³ de material.',
    formula_display: 'Área = largo × alto; Planchas = área × 1.05; Volumen = área × espesor_m',
    steps: [
      'Calcular área: 10m × 3m = 30m²',
      'Aplicar merma: 30m² × 1.05 = 31.5m² de planchas',
      'Convertir espesor: 6cm = 0.06m',
      'Calcular volumen: 30m² × 0.06m = 1.8m³ de aislamiento'
    ],
    mistakes: [
      'No considerar puentes térmicos en encuentros con forjados y pilares',
      'Usar espesor insuficiente para la zona climática',
      'No prever barrera de vapor cuando el aislamiento va en cara interior'
    ]
  },
  'revoco-proyectado': {
    example_label: () => 'Calcular mortero proyectado para revocar 50m² de muro con espesor de 15mm.',
    range_hints: {
      area: 'Superficie total a revocar (descontar huecos si se desea)',
      espesor_mm: 'Revoco fino: 10-15mm, Revoco grueso: 15-25mm'
    },
    result_context: 'Para {area} m² con {espesor_mm}mm de espesor se necesitan {kg_total} kg de mortero proyectado ({sacos_25kg} sacos de 25kg). Consumo: {kg_m2} kg/m².',
    formula_display: 'Consumo = espesor_mm × 1.5 kg/m² por mm; Total = área × consumo',
    steps: [
      'Calcular consumo por m²: 15mm × 1.5 kg/m²/mm = 22.5 kg/m²',
      'Calcular total sin merma: 50m² × 22.5 kg/m² = 1125 kg',
      'Aplicar merma 10%: 1125 kg × 1.10 = 1237.5 kg',
      'Calcular sacos: 1237.5 kg ÷ 25 kg/saco = 49.5 → 50 sacos'
    ],
    mistakes: [
      'No preparar adecuadamente el soporte (limpieza, humidificación)',
      'Aplicar espesor excesivo en una sola capa (puede desprenderse)',
      'No considerar merma por rebote en proyección mecánica'
    ]
  },
  'mortero-cemento': {
    example_label: () => 'Calcular mortero para solado de 40m² con 3cm de espesor y dosificación de 350 kg/m³ de cemento.',
    range_hints: {
      area: 'Superficie a cubrir con mortero',
      espesor_cm: 'Solados: 3-5cm, Enlucidos: 1-2cm, Nivelación: 2-4cm',
      dosificacion: 'Mortero pobre: 250 kg/m³, Estándar: 350 kg/m³, Rico: 450 kg/m³'
    },
    result_context: 'Para {area} m² con {espesor_cm}cm de espesor se necesitan {vol_m3} m³ de mortero, {cemento_kg} kg de cemento ({cemento_sacos} sacos) y {arena_m3} m³ de arena.',
    formula_display: 'Volumen = área × espesor_m; Cemento = volumen × dosificación; Arena = volumen × 1.1',
    steps: [
      'Convertir espesor: 3cm = 0.03m',
      'Calcular volumen de mortero: 40m² × 0.03m = 1.2m³',
      'Calcular cemento: 1.2m³ × 350 kg/m³ = 420 kg (8.4 sacos)',
      'Calcular arena: 1.2m³ × 1.1 = 1.32m³ de arena',
      'Aplicar merma del 5% si es necesario'
    ],
    mistakes: [
      'Usar dosificación incorrecta para el tipo de trabajo',
      'No considerar la merma por compactación del mortero',
      'Mezclar arena con demasiada agua (reduce resistencia)'
    ]
  },
  'enfoscado-guarnecido': {
    example_label: () => 'Calcular mortero de enfoscado para 60m² de paramento con espesor de 15mm tipo monocapa.',
    range_hints: {
      area: 'Superficie total de muros y techos a enfoscar',
      espesor_mm: 'Monocapa: 12-18mm, Tradicional: 15-25mm en varias capas',
      tipo: 'Monocapa: aplicación directa, Tradicional: guarnecido + afinado'
    },
    result_context: 'Superficie de {area} m² con {espesor_mm}mm requiere {sacos} sacos de mortero {tipo}. Consumo estimado: {kg_m2} kg/m².',
    formula_display: 'Consumo = espesor_mm × 1.6 kg/m² por mm; Sacos = (área × consumo) ÷ 25kg',
    steps: [
      'Calcular consumo por m²: 15mm × 1.6 kg/m²/mm = 24 kg/m²',
      'Calcular total: 60m² × 24 kg/m² = 1440 kg',
      'Calcular sacos: 1440 kg ÷ 25 kg/saco = 57.6 → 58 sacos',
      'Para tradicional: considerar capas separadas (guarnecido 10mm + afinado 5mm)'
    ],
    mistakes: [
      'No humedecer el soporte antes de aplicar mortero tradicional',
      'Aplicar monocapa sobre soportes muy absorbentes sin imprimación',
      'No usar malla de refuerzo en encuentros entre materiales diferentes'
    ]
  },
  'mamposteria-piedra': {
    example_label: () => 'Calcular materiales para un muro de mampostería de piedra de 5m × 2m con 40cm de espesor.',
    range_hints: {
      largo: 'Longitud total del muro de piedra',
      alto: 'Altura del muro',
      espesor: 'Muros de piedra: 0.30-0.60m según altura y función'
    },
    result_context: 'Muro de {volumen} m³ requiere {piedra_m3} m³ de piedra, {mortero_kg} kg de mortero de agarre y {juntas_kg} kg de mortero para juntas.',
    formula_display: 'Volumen = largo × alto × espesor; Piedra = volumen × 0.75; Mortero = volumen × 0.35',
    steps: [
      'Calcular volumen del muro: 5m × 2m × 0.40m = 4m³',
      'Calcular piedra: 4m³ × 0.75 = 3m³ de piedra aproximadamente',
      'Calcular mortero: 4m³ × 350 kg/m³ = 1400 kg de mortero',
      'Considerar 15-20% de mortero para relleno de juntas'
    ],
    mistakes: [
      'No seleccionar piedras de tamaño adecuado (deben trabar entre sí)',
      'Usar exceso de mortero (la piedra debe apoyarse sobre piedra)',
      'No colocar piedras de mayor tamaño en esquinas y bases'
    ]
  },
  'cubierta-teja': {
    example_label: () => 'Calcular tejas para una cubierta de 80m² en planta con 30% de pendiente usando teja curva.',
    range_hints: {
      area_planta: 'Superficie en planta (proyección horizontal) de la cubierta',
      pendiente_pct: 'Teja curva: 25-50%, Teja plana: 15-30%, Pizarra: 30-60%',
      tipo_teja: 'Curva (árabe): tradicional, Plana: moderna, Mixta: combinación'
    },
    result_context: 'Cubierta de {area_real} m² reales ({area_planta} m² en planta) requiere {tejas_ud} tejas {tipo_teja} ({tejas_m2} ud/m²), {cumbreras_ud} piezas de cumbrera y {caballetes_ud} caballetes.',
    formula_display: 'Área_real = área_planta × factor_pendiente; Tejas = área_real × ud/m² según tipo',
    steps: [
      'Calcular factor de pendiente: 30% ≈ 1.044 (coeficiente multiplicador)',
      'Calcular área real: 80m² × 1.044 = 83.5m² de cubierta',
      'Teja curva: 83.5m² × 15 ud/m² = 1253 tejas (aprox)',
      'Aplicar merma 5%: 1253 × 1.05 = 1316 tejas',
      'Calcular cumbreras: longitud de cumbrera ÷ 0.30m por pieza'
    ],
    mistakes: [
      'No aplicar coeficiente de pendiente (área real > área en planta)',
      'Usar pendiente insuficiente para el tipo de teja (puede filtrar)',
      'No calcular piezas especiales de cumbrera, limas y caballetes'
    ]
  },
  'solado-ceramico': {
    example_label: () => 'Calcular cajas de cerámico de 30×30cm para solado de 25m² (8 piezas por caja).',
    range_hints: {
      area: 'Superficie a cubrir con cerámico',
      tam_pieza_cm: 'Formatos comunes: 20×20, 30×30, 40×40, 60×60 cm',
      piezas_por_caja: 'Varía según tamaño: 30×30 ≈ 8-11 ud/caja, 40×40 ≈ 6-8 ud/caja'
    },
    result_context: 'Para {area} m² se necesitan {piezas_ud} piezas de {tam_pieza_cm}×{tam_pieza_cm}cm, equivalentes a {cajas_ud} cajas. Se recomienda {area_merma} m² con merma del 10%.',
    formula_display: 'Piezas = área ÷ (lado_m × lado_m); Cajas = piezas ÷ piezas_por_caja',
    steps: [
      'Calcular área por pieza: 0.30m × 0.30m = 0.09m² por pieza',
      'Calcular piezas sin merma: 25m² ÷ 0.09m² = 278 piezas',
      'Aplicar merma 10%: 278 × 1.10 = 306 piezas',
      'Calcular cajas: 306 ÷ 8 = 38.25 → 39 cajas'
    ],
    mistakes: [
      'No considerar merma por cortes (10% colocación recta, 15% diagonal)',
      'No verificar que todas las cajas sean del mismo lote (puede haber variación de tono)',
      'No calcular pieza de inicio para optimizar cortes en bordes'
    ]
  },
  'porcelanico': {
    example_label: () => 'Calcular cajas de porcelánico para 30m² (cajas de 1.44m², formato 60×60cm).',
    range_hints: {
      area: 'Superficie a cubrir con porcelánico',
      m2_por_caja: '60×60cm: 1.08-1.44m²/caja, 80×80cm: 1.28-1.92m²/caja'
    },
    result_context: 'Para {area} m² de porcelánico se necesitan {cajas_ud} cajas ({m2_total} m² totales). Se recomienda comprar {cajas_extra} caja(s) adicional(es) como repuesto.',
    formula_display: 'Cajas = área ÷ m2_por_caja (redondear hacia arriba)',
    steps: [
      'Calcular cajas sin merma: 30m² ÷ 1.44m²/caja = 20.83 → 21 cajas',
      'Aplicar merma 5-8% (porcelánico tiene menos desperdicio): 21 × 1.08 = 22.68 → 23 cajas',
      'Verificar m² totales: 23 cajas × 1.44m² = 33.12m²',
      'Recomendar 1-2 cajas extra para futuras reparaciones'
    ],
    mistakes: [
      'No considerar que el porcelánico requiere adhesivo especial (no mortero común)',
      'Cortar porcelánico sin herramienta adecuada (se fractura fácilmente)',
      'No dejar juntas de dilatación en superficies grandes'
    ]
  },
  'laminado-flotante': {
    example_label: () => 'Calcular cajas de piso laminado flotante para 35m² (cajas de 2.1m²).',
    range_hints: {
      area: 'Superficie del piso a cubrir',
      m2_por_caja: 'Laminado estándar: 1.5-2.5m²/caja según dimensiones de tabla'
    },
    result_context: 'Para {area} m² se necesitan {cajas_ud} cajas de piso laminado ({m2_total} m²). Incluye {subpisaje_m2} m² de subpisaje y {zocalos_ud} metros lineales de zócalos.',
    formula_display: 'Cajas = área ÷ m2_por_caja; Zócalos = perímetro - ancho_puerta',
    steps: [
      'Calcular cajas: 35m² ÷ 2.1m²/caja = 16.67 → 17 cajas',
      'Aplicar merma 5%: 17 × 1.05 = 17.85 → 18 cajas',
      'Calcular subpisaje: 35m² × 1.05 = 36.75m² de subpisaje',
      'Estimar zócalos: perímetro de habitación menos 1m de puerta'
    ],
    mistakes: [
      'No dejar junta de dilatación perimetral (10-15mm)',
      'No instalar barrera de vapor sobre contrapisos húmedos',
      'No aclimatar el material 48h en el ambiente antes de instalar'
    ]
  },
  'parquet-madera': {
    example_label: () => 'Calcular parquet de madera para 40m² con colocación pegada (cajas de 1.8m²).',
    range_hints: {
      area: 'Superficie a cubrir con parquet',
      m2_por_caja: 'Parquet multilamina: 1.5-2.5m²/caja, Madera maciza: 0.8-1.5m²/caja',
      colocacion: 'Pegado: sobre contrapiso nivelado, Flotante: sobre subpisaje, Clavado: sobre listones'
    },
    result_context: 'Para {area} m² con colocación {colocacion} se necesitan {cajas_ud} cajas de parquet ({m2_total} m²), {adhesivo_kg} kg de adhesivo y {zocalos_ml} ml de zócalos.',
    formula_display: 'Cajas = área ÷ m2_por_caja; Adhesivo = área × 1.2 kg/m² (pegado)',
    steps: [
      'Calcular cajas: 40m² ÷ 1.8m²/caja = 22.22 → 23 cajas',
      'Aplicar merma 8% (parquet requiere más cortes): 23 × 1.08 = 24.84 → 25 cajas',
      'Calcular adhesivo (pegado): 40m² × 1.2 kg/m² = 48 kg',
      'Calcular zócalos: perímetro de la habitación'
    ],
    mistakes: [
      'No nivelar perfectamente el contrapiso antes de pegar',
      'No respetar tiempo de curado del adhesivo antes de transitar',
      'No considerar la dirección de colocación (luz natural vs. veta)'
    ]
  },
  'marmol-granito': {
    example_label: () => 'Calcular losas de granito de 2cm de espesor para 20m² de superficie.',
    range_hints: {
      area: 'Superficie a revestir con piedra natural',
      espesor_cm: 'Pisos: 2-3cm, Revestimientos: 1.5-2cm, Encimeras: 3cm',
      tipo: 'Mármol: más elegante pero poroso, Granito: más duro y resistente'
    },
    result_context: 'Para {area} m² de {tipo} de {espesor_cm}cm se necesitan {m2_total} m² de losas (con merma), {adhesivo_kg} kg de adhesivo y {juntas_ml} ml de junta.',
    formula_display: 'M2_total = área × 1.10 (merma); Adhesivo = área × 4 kg/m²',
    steps: [
      'Calcular merma 10%: 20m² × 1.10 = 22m² de losas',
      'Calcular volumen de piedra: 20m² × 0.02m = 0.4m³',
      'Calcular peso aproximado: 0.4m³ × 2700 kg/m³ = 1080 kg (granito)',
      'Calcular adhesivo: 20m² × 4 kg/m² = 80 kg de adhesivo flexible'
    ],
    mistakes: [
      'No sellar el mármol (es poroso y mancha fácilmente)',
      'Usar adhesivo común en lugar de adhesivo flexible para piedra',
      'No verificar que la estructura soporte el peso (piedra es muy pesada)'
    ]
  },
  'terrazo': {
    example_label: () => 'Calcular baldosas de terrazo de 40×40cm para 45m² incluyendo mortero de colocación.',
    range_hints: {
      area: 'Superficie a cubrir con terrazo',
      tam_pieza_cm: 'Formatos comunes: 30×30, 40×40, 50×50 cm',
      incluye_mortero: 'Sí: calcular mortero, No: solo baldosas'
    },
    result_context: 'Para {area} m² con baldosas de {tam_pieza_cm}×{tam_pieza_cm}cm se necesitan {baldosas_ud} baldosas ({baldosas_cajas} cajas), {mortero_kg} kg de mortero y {juntas_kg} kg de fragüe.',
    formula_display: 'Baldosas = área ÷ (lado_m × lado_m); Mortero = área × 15 kg/m²',
    steps: [
      'Calcular área por baldosa: 0.40m × 0.40m = 0.16m²',
      'Calcular baldosas: 45m² ÷ 0.16m² = 281.25 → 282 baldosas',
      'Aplicar merma 5%: 282 × 1.05 = 296 baldosas',
      'Calcular mortero: 45m² × 15 kg/m² = 675 kg'
    ],
    mistakes: [
      'No remojar las baldosas de terrazo antes de colocar (absorben agua)',
      'No dejar juntas uniformes (usar separadores/cruces)',
      'No pulir y sellar después de colocado si es terrazo continuo'
    ]
  },
  'azulejo-pared': {
    example_label: () => 'Calcular azulejos de 20×20cm para revestir 35m² de pared (20 piezas por caja).',
    range_hints: {
      area: 'Superficie de paredes a revestir (baños, cocinas)',
      tam_pieza_cm: 'Formatos comunes: 15×15, 20×20, 20×30, 30×60 cm',
      piezas_por_caja: 'Varía según tamaño: 20×20 ≈ 15-25 ud/caja'
    },
    result_context: 'Para {area} m² de pared se necesitan {piezas_ud} azulejos de {tam_pieza_cm}×{tam_pieza_cm}cm, equivalentes a {cajas_ud} cajas. Adhesivo necesario: {adhesivo_kg} kg.',
    formula_display: 'Piezas = área ÷ (lado_m × lado_m); Cajas = piezas ÷ piezas_por_caja',
    steps: [
      'Calcular área por pieza: 0.20m × 0.20m = 0.04m²',
      'Calcular piezas: 35m² ÷ 0.04m² = 875 piezas',
      'Aplicar merma 10% (más cortes en paredes): 875 × 1.10 = 963 piezas',
      'Calcular cajas: 963 ÷ 20 = 48.15 → 49 cajas',
      'Calcular adhesivo: 35m² × 5 kg/m² = 175 kg'
    ],
    mistakes: [
      'No comenzar desde el centro o punto visible (cortes asimétricos)',
      'No usar nivelador de juntas para azulejos grandes',
      'No impermeabilizar paredes de ducha antes de azulejar'
    ]
  },
  'mosaico': {
    example_label: () => 'Calcular mosaico sobre malla de 30×30cm para cubrir 8m² (típico para piscinas o baños).',
    range_hints: {
      area: 'Superficie a cubrir con mosaico',
      tam_malla_cm: 'Mallas comunes: 30×30cm, algunas de 32×32cm'
    },
    result_context: 'Para {area} m² se necesitan {mallas_ud} mallas de mosaico de {tam_malla_cm}×{tam_malla_cm}cm ({m2_total} m²). Adhesivo: {adhesivo_kg} kg, Fragüe: {fragüe_kg} kg.',
    formula_display: 'Mallas = área ÷ (lado_m × lado_m); Adhesivo = área × 4 kg/m²',
    steps: [
      'Calcular área por malla: 0.30m × 0.30m = 0.09m²',
      'Calcular mallas: 8m² ÷ 0.09m² = 88.89 → 89 mallas',
      'Aplicar merma 5%: 89 × 1.05 = 93.45 → 94 mallas',
      'Calcular adhesivo: 8m² × 4 kg/m² = 32 kg (adhesivo blanco para mosaico)',
      'Calcular fragüe: 8m² × 0.5 kg/m² = 4 kg'
    ],
    mistakes: [
      'No usar adhesivo blanco (puede transparentarse en mosaicos vítreos)',
      'No limpiar el exceso de fragüe inmediatamente (se endurece)',
      'No respetar tiempo de curado antes de llenar piscina'
    ]
  },
  'adhesivo-ceramico': {
    example_label: () => 'Calcular adhesivo para colocar 50m² de cerámica con doble encolado.',
    range_hints: {
      area: 'Superficie a cubrir con cerámica/porcelánico',
      tipo_colocacion: 'Simple: piezas pequeñas, Doble encolado: piezas grandes o exteriores'
    },
    result_context: 'Para {area} m² con {tipo_colocacion} se necesitan {adhesivo_kg} kg de adhesivo ({sacos_ud} sacos de 25kg). Consumo: {kg_m2} kg/m².',
    formula_display: 'Consumo_simple = 4 kg/m²; Consumo_doble = 8 kg/m²; Total = área × consumo',
    steps: [
      'Determinar consumo según tipo: doble encolado = 8 kg/m²',
      'Calcular total: 50m² × 8 kg/m² = 400 kg',
      'Calcular sacos: 400 kg ÷ 25 kg/saco = 16 sacos',
      'Para doble encolado: aplicar adhesivo en soporte Y en dorso de pieza'
    ],
    mistakes: [
      'No hacer doble encolado en piezas mayores a 30×30cm',
      'Usar el mismo adhesivo para interior y exterior (debe ser flexible en exteriores)',
      'No respetar tiempo abierto del adhesivo (se seca antes de colocar)'
    ]
  },
  'lechada-junta': {
    example_label: () => 'Calcular fragüe/lechada para 40m² de cerámica de 30×30cm con junta de 3mm y espesor de pieza 10mm.',
    range_hints: {
      area: 'Superficie total colocada',
      tam_pieza_cm: 'Tamaño de la pieza cerámica',
      ancho_junta_mm: 'Juntas estándar: 2-5mm según tipo de piso',
      grosor_pieza_mm: 'Espesor de la baldosa (afecta volumen de junta)'
    },
    result_context: 'Para {area} m² de {tam_pieza_cm}×{tam_pieza_cm}cm con junta de {ancho_junta_mm}mm se necesitan {fragüe_kg} kg de fragüe ({sacos_ud} sacos). Longitud total de juntas: {long_juntas_ml} ml.',
    formula_display: 'Long_juntas = área ÷ lado_m × 2; Vol_junta = long × ancho × grosor; Peso = vol × 1.6 kg/m³',
    steps: [
      'Calcular longitud de juntas: 40m² ÷ 0.30m × 2 = 266.67 ml',
      'Calcular volumen de junta: 266.67m × 0.003m × 0.01m = 0.008 m³',
      'Calcular peso: 0.008m³ × 1600 kg/m³ = 12.8 kg',
      'Aplicar factor desperdicio: 12.8 kg × 1.15 = 14.72 kg de fragüe'
    ],
    mistakes: [
      'Usar fragüe incorrecto para el tipo de junta (epóxico para zonas húmedas)',
      'No limpiar el exceso de fragüe antes de que seque',
      'Aplicar fragüe en juntas muy anchas sin usar fragüe especial'
    ]
  },
  'tuberia-pvc-saneamiento': {
    example_label: () => 'Calcular tubería PVC de saneamiento para 25m lineales en 5 tramos.',
    range_hints: {
      longitud: 'Longitud total de tubería necesaria',
      tramos: 'Número de tramos rectos (tuberías vienen en barras de 3-6m)'
    },
    result_context: 'Para {longitud}m en {tramos} tramos se necesitan {barras_ud} barras de PVC, {accesorios_ud} accesorios (codos, tes, reducciones) y {pegamento_ud} unidades de pegamento.',
    formula_display: 'Barras = longitud ÷ 4m (longitud estándar barra); Accesorios = tramos × 2',
    steps: [
      'Calcular barras de 4m: 25m ÷ 4m = 6.25 → 7 barras',
      'Estimar accesorios: 5 tramos × 2 = 10 accesorios (codos/tes)',
      'Calcular pegamento: 7 barras × 1 unidad por barra = 7 unidades',
      'Considerar pendiente mínima: 2% para desagües'
    ],
    mistakes: [
      'No respetar pendiente mínima de 2% (puede haber estancamientos)',
      'Usar tubería de pared delgada para enterrado (debe ser pared gruesa)',
      'No dejar registros/registros para limpieza en cambios de dirección'
    ]
  },
  'tuberia-cobre-pex': {
    example_label: () => 'Calcular tubería de cobre/PEX para instalación de agua con 40m de longitud y 6 puntos de suministro.',
    range_hints: {
      longitud: 'Longitud total de tubería para agua fría/caliente',
      puntos_suministro: 'Grifos, duchas, inodoros, lavadoras, etc.'
    },
    result_context: 'Para {longitud}m de tubería con {puntos_suministro} puntos se necesitan {tuberia_m}m de tubo, {accesorios_ud} accesorios y {aislamiento_m}m de aislamiento térmico.',
    formula_display: 'Tubería = longitud × 1.10 (merma); Accesorios = puntos × 3',
    steps: [
      'Calcular tubería con merma: 40m × 1.10 = 44m',
      'Estimar accesorios: 6 puntos × 3 = 18 accesorios (válvulas, codos, tes)',
      'Calcular aislamiento: 40m × 0.80 = 32m (solo agua caliente)',
      'Diferenciar diámetros: 1/2" para grifos, 3/4" para duchas, 1" para principales'
    ],
    mistakes: [
      'No aislar tuberías de agua caliente (pérdida de energía)',
      'Usar diámetro insuficiente (baja presión en puntos alejados)',
      'No prever llaves de corte por sector para mantenimiento'
    ]
  },
  'presion-agua': {
    example_label: () => 'Calcular presión de agua necesaria para una altura de 15m considerando 15% de pérdidas por fricción.',
    range_hints: {
      altura_m: 'Altura geométrica desde bomba/tanque hasta punto más alto',
      perdidas_carga_pct: 'Pérdidas típicas: 10-25% según longitud y diámetro de tubería'
    },
    result_context: 'Para altura de {altura_m}m con {perdidas_carga_pct}% de pérdidas se necesita presión de {presion_bar} bar ({presion_mca} mca). Potencia de bomba estimada: {potencia_cv} CV.',
    formula_display: 'Presión_mca = altura + (altura × pérdidas%); Presión_bar = presión_mca ÷ 10',
    steps: [
      'Convertir altura a presión: 15m = 1.5 bar (10m = 1 bar)',
      'Calcular pérdidas: 15m × 0.15 = 2.25m adicionales',
      'Presión total: 15m + 2.25m = 17.25m = 1.725 bar',
      'Estimar potencia de bomba según caudal requerido'
    ],
    mistakes: [
      'No considerar pérdidas por fricción en tuberías largas',
      'Dimensionar bomba solo por altura (ignorar caudal necesario)',
      'No prever vaso de expansión para evitar arranques frecuentes'
    ]
  },
  'deposito-agua': {
    example_label: () => 'Calcular capacidad de depósito de agua para 4 personas con consumo de 150 L/persona/día y 2 días de autonomía.',
    range_hints: {
      personas: 'Número de habitantes de la vivienda',
      litros_persona_dia: 'Consumo típico: 100-200 L/persona/día según hábitos',
      dias_autonomia: 'Recomendado: 1-3 días según frecuencia de suministro'
    },
    result_context: 'Para {personas} personas con {litros_persona_dia} L/día se necesitan {consumo_diario} L/día. Con {dias_autonomia} días de autonomía: {capacidad_total} L de depósito ({capacidad_m3} m³).',
    formula_display: 'Consumo_diario = personas × litros_persona_día; Capacidad = consumo × días_autonomía',
    steps: [
      'Calcular consumo diario: 4 personas × 150 L = 600 L/día',
      'Calcular capacidad: 600 L/día × 2 días = 1200 L',
      'Convertir a m³: 1200 L ÷ 1000 = 1.2 m³',
      'Considerar volumen muerto: agregar 10% = 1320 L (depósito comercial: 1500 L)'
    ],
    mistakes: [
      'No considerar volumen muerto del depósito (fondo no utilizable)',
      'Dimensionar sin margen para visitas o consumo excepcional',
      'No prever sistema de rebose y limpieza del depósito'
    ]
  },
  'calentador-agua': {
    example_label: () => 'Calcular potencia de calentador para 100L de agua, de 15°C a 60°C en 2 horas.',
    range_hints: {
      litros_deposito: 'Capacidad del termo/acumulador',
      temp_entrada_c: 'Temperatura del agua de red (varía por estación)',
      temp_salida_c: 'Temperatura de uso: 45-50°C ducha, 60°C para legionela',
      horas_calentamiento: 'Tiempo deseado para calentar el depósito completo'
    },
    result_context: 'Para calentar {litros_deposito}L de {temp_entrada_c}°C a {temp_salida_c}°C en {horas_calentamiento}h se necesita potencia de {potencia_kw} kW ({potencia_w} W). Energía requerida: {energia_kwh} kWh.',
    formula_display: 'ΔT = T_salida - T_entrada; Energía = litros × ΔT × 0.00116; Potencia = energía ÷ horas',
    steps: [
      'Calcular diferencia de temperatura: 60°C - 15°C = 45°C',
      'Calcular energía: 100L × 45°C × 0.00116 = 5.22 kWh',
      'Calcular potencia: 5.22 kWh ÷ 2h = 2.61 kW',
      'Considerar pérdidas: 2.61 kW × 1.15 = 3.0 kW (potencia comercial)'
    ],
    mistakes: [
      'No programar temperatura mínima de 60°C para evitar legionela',
      'Dimensionar potencia insuficiente (tiempo de recuperación muy largo)',
      'No considerar tarifa eléctrica para programar calentamiento en horas valle'
    ]
  },
  'caldera-gas': {
    example_label: () => 'Calcular potencia de caldera de gas para vivienda de 100m² con 2.5m de altura y aislamiento medio.',
    range_hints: {
      area_m2: 'Superficie útil de la vivienda a calefaccionar',
      altura_m: 'Altura libre de techos (afecta volumen a calentar)',
      aislamiento: 'Bajo: sin aislamiento, Medio: aislamiento básico, Alto: aislamiento completo'
    },
    result_context: 'Vivienda de {area_m2}m² con {altura_m}m de altura y aislamiento {aislamiento} requiere caldera de {potencia_kw} kW ({potencia_kcal} kcal/h). Volumen a calentar: {volumen_m3} m³.',
    formula_display: 'Volumen = área × altura; Potencia = volumen × factor_aislamiento (30-50 W/m³)',
    steps: [
      'Calcular volumen: 100m² × 2.5m = 250m³',
      'Factor aislamiento medio: 40 W/m³',
      'Calcular potencia: 250m³ × 40 W/m³ = 10000 W = 10 kW',
      'Aplicar margen seguridad 20%: 10 kW × 1.20 = 12 kW'
    ],
    mistakes: [
      'Dimensionar solo por m² sin considerar altura y aislamiento',
      'No prever potencia adicional para agua caliente sanitaria',
      'Instalar caldera sobredimensionada (ciclos cortos, menor eficiencia)'
    ]
  },
  'radiador-aluminio': {
    example_label: () => 'Calcular radiador de aluminio para habitación de 20m² con 2.5m de altura y orientación norte.',
    range_hints: {
      area_m2: 'Superficie de la habitación',
      altura_m: 'Altura del techo',
      orientacion: 'Norte: más frío, Sur: más soleado, Este/Oeste: intermedio'
    },
    result_context: 'Habitación de {area_m2}m² con orientación {orientacion} requiere radiador de {potencia_w} W ({elementos_ud} elementos de aluminio). Volumen: {volumen_m3} m³.',
    formula_display: 'Volumen = área × altura; Potencia = volumen × factor_orientación (35-50 W/m³)',
    steps: [
      'Calcular volumen: 20m² × 2.5m = 50m³',
      'Factor orientación norte: 50 W/m³ (más potencia por menor sol)',
      'Calcular potencia: 50m³ × 50 W/m³ = 2500 W',
      'Elementos de aluminio: 2500W ÷ 180W/elemento = 13.89 → 14 elementos'
    ],
    mistakes: [
      'No considerar orientación (norte requiere 15-20% más potencia)',
      'No prever válvulas termostáticas para control individual',
      'Ubicar radiador en lugar incorrecto (debe ir bajo ventana)'
    ]
  },
  'suelo-radiante': {
    example_label: () => 'Calcular tubería para suelo radiante de 80m² con separación de 15cm entre tubos.',
    range_hints: {
      area_m2: 'Superficie a calefaccionar con suelo radiante',
      separacion_cm: 'Típico: 10-20cm (15cm estándar para viviendas)',
      circuitos_max_m: 'Longitud máxima por circuito: 80-120m según diámetro'
    },
    result_context: 'Para {area_m2}m² con tubería cada {separacion_cm}cm se necesitan {tuberia_m}m de tubo PEX en {circuitos_ud} circuitos. Colector de {vias_ud} vías requerido.',
    formula_display: 'Tubería = área × (100 ÷ separación_cm); Circuitos = tubería ÷ circuitos_max_m',
    steps: [
      'Calcular metros de tubería: 80m² × (100 ÷ 15) = 80 × 6.67 = 533.33m',
      'Aplicar factor 1.10 por bordes: 533m × 1.10 = 586m de tubo',
      'Calcular circuitos: 586m ÷ 100m/circuito = 5.86 → 6 circuitos',
      'Colector necesario: 6 salidas (vías)'
    ],
    mistakes: [
      'Exceder longitud máxima por circuito (pérdida de carga excesiva)',
      'No aislar térmicamente bajo los tubos (pérdida hacia abajo)',
      'No dejar juntas de dilatación en superficies > 40m²'
    ]
  },
  'riego-goteo': {
    example_label: () => 'Calcular sistema de riego por goteo para 100m² de jardín con goteros cada 40cm y líneas separadas 1.5m.',
    range_hints: {
      area_m2: 'Superficie a irrigar',
      separacion_goteros_cm: 'Goteros: 30-50cm según tipo de cultivo',
      separacion_lineas_m: 'Líneas: 1-2m según alcance del gotero'
    },
    result_context: 'Para {area_m2}m² se necesitan {lineas_ud} líneas de riego, {goteros_ud} goteros, {tuberia_m}m de tubería principal y {filtro_ud} filtro de {caudal_lph} L/h.',
    formula_display: 'Líneas = área ÷ (largo × separación); Goteros = (largo ÷ sep_goteros) × líneas',
    steps: [
      'Asumir área 10m × 10m = 100m²',
      'Calcular líneas: 10m ÷ 1.5m = 6.67 → 7 líneas',
      'Calcular goteros por línea: 10m ÷ 0.40m = 25 goteros',
      'Total goteros: 25 × 7 = 175 goteros',
      'Caudal total: 175 × 4 L/h = 700 L/h (necesita filtro y programador)'
    ],
    mistakes: [
      'No instalar filtro (los goteros se tapan fácilmente)',
      'No considerar presión de red (puede necesitar reductor)',
      'Espaciar demasiado las líneas (zonas sin riego)'
    ]
  },
  'acometida-agua': {
    example_label: () => 'Calcular diámetro de tubería para acometida de agua con caudal de 2.5 L/s y 30m de longitud.',
    range_hints: {
      caudal_lps: 'Caudal máximo simultáneo esperado',
      longitud_m: 'Longitud desde red pública hasta contador/vivienda'
    },
    result_context: 'Para {caudal_lps} L/s en {longitud_m}m se recomienda tubería de {diametro_mm}mm ({diametro_pulgadas}"). Velocidad del agua: {velocidad_ms} m/s. Pérdida de carga: {perdida_bar} bar.',
    formula_display: 'Diámetro = √(4 × caudal ÷ (π × velocidad)); Velocidad recomendada: 1-2 m/s',
    steps: [
      'Asumir velocidad óptima: 1.5 m/s',
      'Convertir caudal: 2.5 L/s = 0.0025 m³/s',
      'Calcular diámetro: √(4 × 0.0025 ÷ (π × 1.5)) = 0.046m = 46mm',
      'Diámetro comercial: 50mm (2 pulgadas)'
    ],
    mistakes: [
      'Usar diámetro muy pequeño (pérdida de presión excesiva)',
      'No considerar caudal simultáneo máximo (varios grifos abiertos)',
      'No prever llave de corte y contador en acometida'
    ]
  },
  'depuradora-piscina': {
    example_label: () => 'Calcular depuradora para piscina de 8×4m con profundidad media 1.5m y 2 turnos de filtrado por día.',
    range_hints: {
      largo_m: 'Longitud de la piscina',
      ancho_m: 'Ancho de la piscina',
      profundidad_media_m: 'Promedio entre profundidad mínima y máxima',
      turnos_dia: 'Veces que se filtra el volumen total por día (2-4 turnos)'
    },
    result_context: 'Piscina de {volumen_m3} m³ ({volumen_litros} L) requiere depuradora de {caudal_m3h} m³/h para {turnos_dia} turnos/día. Tiempo de filtrado: {tiempo_horas} horas.',
    formula_display: 'Volumen = largo × ancho × profundidad; Caudal = volumen × turnos ÷ 24h',
    steps: [
      'Calcular volumen: 8m × 4m × 1.5m = 48m³ = 48000 L',
      'Filtrar 2 veces por día: 48m³ × 2 = 96m³/día',
      'Calcular caudal: 96m³ ÷ 24h = 4m³/h',
      'Seleccionar bomba: 4-5 m³/h (margen de seguridad)'
    ],
    mistakes: [
      'Dimensionar depuradora insuficiente (agua turbia)',
      'No calcular tiempo de filtrado según temporada (más en verano)',
      'No prever limpieza de filtros cuando manómetro indica saturación'
    ]
  },
  'sifon-sumidero': {
    example_label: () => 'Calcular sifones y sumideros para 5 aparatos sanitarios con bajante de 8m y 2% de pendiente.',
    range_hints: {
      num_aparatos: 'Lavabos, inodoros, duchas, bidets, lavadoras',
      longitud_bajante_m: 'Longitud desde aparato más alejado hasta bajante principal',
      pendiente_pct: 'Saneamiento: 2-3% mínimo para evitar obstrucciones'
    },
    result_context: 'Para {num_aparatos} aparatos con bajante de {longitud_bajante_m}m se necesitan {sifones_ud} sifones, {sumideros_ud} sumideros y {tuberia_m}m de tubería con {pendiente_pct}% de pendiente.',
    formula_display: 'Sifones = num_aparatos; Tubería = longitud × 1.05 (por pendiente)',
    steps: [
      'Calcular sifones: 5 aparatos = 5 sifones (1 por aparato)',
      'Calcular tubería con pendiente: 8m × 1.02 = 8.16m (ligeramente más por inclinación)',
      'Verificar pendiente: 2% = 2cm por metro = 16cm en 8m',
      'Diámetros: lavabo 40mm, ducha 50mm, inodoro 110mm'
    ],
    mistakes: [
      'No instalar sifón en cada aparato (entran olores)',
      'Pendiente insuficiente (menos de 2% causa obstrucciones)',
      'No prever ventilación de bajante (puede hacer sifonaje)'
    ]
  },
  'cable-electrico-seccion': {
    example_label: () => 'Calcular sección de cable para 25A a 30m de distancia en 230V con caída máxima de 3%.',
    range_hints: {
      corriente_a: 'Corriente máxima del circuito',
      longitud_m: 'Distancia desde cuadro hasta carga',
      tension_v: '230V monofásica o 400V trifásica',
      caida_max_pct: 'Iluminación: 3%, Fuerza: 5% máximo'
    },
    result_context: 'Para {corriente_a}A a {longitud_m}m en {tension_v}V se recomienda cable de {seccion_mm2}mm². Caída de tensión calculada: {caida_pct}%. Corriente máxima admisible: {imax_a}A.',
    formula_display: 'Sección = (2 × longitud × corriente) ÷ (caida% × tensión × conductividad)',
    steps: [
      'Caída máxima: 230V × 0.03 = 6.9V',
      'Calcular sección (cobre, σ=56): (2 × 30 × 25) ÷ (6.9 × 56) = 1500 ÷ 386.4 = 3.88mm²',
      'Sección comercial: 4mm² (pero verificar por corriente)',
      'Verificar por corriente: 4mm² soporta ~30A > 25A ✓'
    ],
    mistakes: [
      'Dimensionar solo por corriente sin considerar caída de tensión',
      'No usar sección mínima reglamentaria (2.5mm² para enchufes)',
      'No considerar agrupamiento de cables (reduce capacidad)'
    ]
  },
  'caida-tension': {
    example_label: () => 'Calcular caída de tensión en cable de 6mm² para 32A a 40m en 230V.',
    range_hints: {
      seccion_mm2: 'Sección del cable: 1.5, 2.5, 4, 6, 10, 16mm²...',
      longitud_m: 'Longitud del circuito',
      corriente_a: 'Corriente que circulará',
      tension_v: 'Tensión de la instalación'
    },
    result_context: 'Cable de {seccion_mm2}mm² a {longitud_m}m con {corriente_a}A tiene caída de {caida_v}V ({caida_pct}%). ¿Cumple? {cumple}. Caída máxima permitida: {caida_max_v}V.',
    formula_display: 'Caída_V = (2 × longitud × corriente) ÷ (sección × conductividad); Caída_% = (caída_V ÷ tensión) × 100',
    steps: [
      'Conductividad cobre: 56 m/(Ω·mm²)',
      'Calcular caída: (2 × 40 × 32) ÷ (6 × 56) = 2560 ÷ 336 = 7.62V',
      'Calcular porcentaje: (7.62V ÷ 230V) × 100 = 3.31%',
      'Verificar: 3.31% > 3% (iluminación) ✗, pero < 5% (fuerza) ✓'
    ],
    mistakes: [
      'Aceptar caída > 3% en circuitos de iluminación',
      'No considerar que cables agrupados disipan menos calor',
      'Confundir conductividad del cobre (56) con aluminio (35)'
    ]
  },
  'luminarias-lumenes': {
    example_label: () => 'Calcular luminarias necesarias para 25m² de oficina requiriendo 300 lux con lámparas de 100 lm/W.',
    range_hints: {
      area_m2: 'Superficie del local a iluminar',
      lux_requeridos: 'Oficina: 300-500 lux, Hogar: 100-300 lux, Taller: 500-1000 lux',
      eficiencia_luminaria: 'LED: 80-150 lm/W, Fluorescente: 60-100 lm/W'
    },
    result_context: 'Para {area_m2}m² con {lux_requeridos} lux se necesitan {lumenes_totales} lúmenes. Con lámparas de {eficiencia_luminaria} lm/W: {potencia_total_w}W en {luminarias_ud} luminarias de {w_por_luminaria}W.',
    formula_display: 'Lúmenes = área × lux; Potencia = lúmenes ÷ eficiencia; Luminarias = potencia ÷ W_por_lámpara',
    steps: [
      'Calcular lúmenes totales: 25m² × 300 lux = 7500 lúmenes',
      'Considerar factor de mantenimiento 0.8: 7500 ÷ 0.8 = 9375 lúmenes',
      'Calcular potencia: 9375 lm ÷ 100 lm/W = 93.75W',
      'Si luminarias LED de 20W: 93.75W ÷ 20W = 4.69 → 5 luminarias'
    ],
    mistakes: [
      'No considerar factor de mantenimiento (polvo, envejecimiento)',
      'No distribuir uniformemente las luminarias',
      'Confundir lúmenes (cantidad de luz) con lux (luz por m²)'
    ]
  },
  'puntos-luz-habitacion': {
    example_label: () => 'Calcular puntos de luz recomendados para un dormitorio de 18m².',
    range_hints: {
      area_m2: 'Superficie de la habitación',
      uso: 'Tipo de habitación: determina nivel de iluminación y tipo de puntos'
    },
    result_context: 'Habitación de {area_m2}m² para {uso} requiere {puntos_luz_ud} puntos de luz: {techo_ud} en techo, {pared_ud} en pared. Potencia total: {potencia_w}W. Interruptores: {interruptores_ud} conmutados.',
    formula_display: 'Puntos_techo = área ÷ 6m²; Puntos_pared = según uso; Total = suma',
    steps: [
      'Puntos de techo: 18m² ÷ 6m² = 3 puntos',
      'Dormitorio: agregar 1-2 puntos de pared (lectura)',
      'Total: 3 techo + 2 pared = 5 puntos de luz',
      'Prever conmutación en entrada y cabecera de cama'
    ],
    mistakes: [
      'No prever conmutación (incómodo apagar luz desde la cama)',
      'No considerar luz de lectura junto a la cama',
      'Ubicar interruptor detrás de la puerta (debe quedar accesible)'
    ]
  },
  'cuadro-electrico': {
    example_label: () => 'Calcular intensidad y protecciones para cuadro eléctrico de 9.2kW en 230V con factor 0.6.',
    range_hints: {
      potencia_kw: 'Potencia contratada o instalada',
      tension_v: '230V monofásica o 400V trifásica',
      factor_simultaneidad: 'Vivienda: 0.4-0.6, Industria: 0.7-0.9'
    },
    result_context: 'Instalación de {potencia_kw}kW en {tension_v}V requiere IGA de {iga_a}A. Potencia simultánea: {potencia_simultanea}kW. Sección entrada: {seccion_mm2}mm².',
    formula_display: 'Intensidad = potencia ÷ tensión; I_simultánea = I_total × factor',
    steps: [
      'Calcular intensidad total: 9200W ÷ 230V = 40A',
      'Aplicar factor simultaneidad: 40A × 0.6 = 24A',
      'Seleccionar IGA: 40A (por potencia contratada)',
      'Sección cable entrada: 10mm² (soporta 50A)'
    ],
    mistakes: [
      'No considerar factor de simultaneidad (sobredimensiona)',
      'Usar sección insuficiente para la distancia al contador',
      'No prever diferencial de 30mA y 40A mínimo'
    ]
  },
  'instalacion-solar': {
    example_label: () => 'Calcular instalación solar para consumo de 15 kWh/día con 4.5 HSP y paneles de 450W.',
    range_hints: {
      consumo_diario_kwh: 'Consumo promedio diario de la vivienda',
      hsp_dia: 'Horas Sol Pico según ubicación: 3-6 HSP/día',
      potencia_panel_w: 'Paneles comerciales: 350-550W'
    },
    result_context: 'Para {consumo_diario_kwh} kWh/día con {hsp_dia} HSP se necesitan {potencia_total_w}W de paneles ({paneles_ud} paneles de {potencia_panel_w}W). Baterías: {capacidad_kwh} kWh para 1 día.',
    formula_display: 'Potencia = consumo ÷ HSP; Paneles = potencia ÷ W_panel; Baterías = consumo × días',
    steps: [
      'Calcular potencia necesaria: 15 kWh ÷ 4.5 HSP = 3.33 kW = 3333W',
      'Considerar pérdidas 20%: 3333W × 1.20 = 4000W',
      'Calcular paneles: 4000W ÷ 450W = 8.89 → 9 paneles',
      'Baterías 1 día: 15 kWh × 1.20 = 18 kWh (considerar profundidad descarga 50%: 36 kWh)'
    ],
    mistakes: [
      'No considerar pérdidas del sistema (inversor, cables, temperatura)',
      'Dimensionar baterías sin considerar profundidad de descarga',
      'No orientar paneles correctamente (sur en hemisferio norte)'
    ]
  },
  'baterias-autonomia': {
    example_label: () => 'Calcular baterías para 10 kWh/día de consumo, 2 días de autonomía con baterías de 5 kWh.',
    range_hints: {
      consumo_diario_kwh: 'Consumo diario de la instalación',
      dias_autonomia: 'Días sin sol: 1-5 días según ubicación',
      capacidad_bateria_kwh: 'Baterías litio: 2.5-15 kWh por unidad'
    },
    result_context: 'Para {consumo_diario_kwh} kWh/día con {dias_autonomia} días de autonomía se necesitan {energia_total_kwh} kWh. Con baterías de {capacidad_bateria_kwh} kWh: {baterias_ud} baterías ({configuracion}).',
    formula_display: 'Energía = consumo × días ÷ profundidad_descarga; Baterías = energía ÷ capacidad_unitaria',
    steps: [
      'Energía necesaria: 10 kWh × 2 días = 20 kWh',
      'Considerar profundidad descarga 80% (litio): 20 kWh ÷ 0.80 = 25 kWh',
      'Calcular baterías: 25 kWh ÷ 5 kWh = 5 baterías',
      'Configuración: 5 baterías en paralelo (o serie-paralelo según voltaje)'
    ],
    mistakes: [
      'No considerar profundidad de descarga (acorta vida útil)',
      'Mezclar baterías de diferente capacidad o antigüedad',
      'No prever BMS (Battery Management System) para litio'
    ]
  },
  'trifasica-potencia': {
    example_label: () => 'Calcular potencia trifásica para 32A a 400V con factor de potencia 0.85.',
    range_hints: {
      corriente_a: 'Corriente por fase',
      tension_v: 'Tensión entre fases (400V estándar Europa)',
      fp: 'Factor de potencia: 0.8-1.0 (1.0 resistivo puro)'
    },
    result_context: 'Sistema trifásico de {corriente_a}A a {tension_v}V con FP={fp} tiene potencia activa de {potencia_kw} kW ({potencia_hp} HP). Potencia aparente: {potencia_kva} kVA.',
    formula_display: 'P = √3 × V × I × FP; S = √3 × V × I',
    steps: [
      'Calcular potencia activa: √3 × 400V × 32A × 0.85 = 1.732 × 400 × 32 × 0.85',
      'P = 18881W = 18.88 kW',
      'Calcular potencia aparente: √3 × 400V × 32A = 22170 VA = 22.17 kVA',
      'Convertir a HP: 18.88 kW ÷ 0.746 = 25.3 HP'
    ],
    mistakes: [
      'Olvidar factor √3 en fórmula trifásica (usa fórmula monofásica)',
      'No considerar factor de potencia en cálculos de potencia activa',
      'Confundir tensión fase-neutro (230V) con fase-fase (400V)'
    ]
  },
  'puesta-tierra': {
    example_label: () => 'Calcular puesta a tierra con resistividad de 100 Ω·m y resistencia máxima de 10 Ω usando pica de cobre de 2m.',
    range_hints: {
      resistividad_ohm_m: 'Suelo húmedo: 50-200 Ω·m, Seco: 200-500 Ω·m, Rocoso: >500 Ω·m',
      resistencia_max_ohm: 'Vivienda: <10 Ω, Industrial: <5 Ω, Hospitalaria: <1 Ω',
      tipo_pica: 'Longitud y material de la pica de tierra'
    },
    result_context: 'Con resistividad {resistividad_ohm_m} Ω·m y pica {tipo_pica} se estima resistencia de {resistencia_ohm} Ω. ¿Cumple? {cumple}. Número de picas necesarias: {picas_ud}.',
    formula_display: 'R_pica = (resistividad × 0.366) ÷ longitud; R_total = R_pica ÷ num_picas',
    steps: [
      'Calcular resistencia de una pica: (100 × 0.366) ÷ 2 = 18.3 Ω',
      'Verificar: 18.3 Ω > 10 Ω (no cumple con una pica)',
      'Calcular picas necesarias: 18.3 Ω ÷ 10 Ω = 1.83 → 2 picas',
      'Con 2 picas en paralelo: 18.3 Ω ÷ 2 = 9.15 Ω ✓ (cumple)'
    ],
    mistakes: [
      'No medir resistividad real del suelo antes de diseñar',
      'Enterrar picas en suelo seco (mejor en zona húmeda)',
      'No conectar todas las masas al mismo sistema de tierra'
    ]
  },
  'consumo-electrico-mensual': {
    example_label: () => 'Calcular consumo mensual de un aparato de 1000W usado 5 horas/día con precio de 0.15 €/kWh.',
    range_hints: {
      potencia_w: 'Potencia del aparato en watts',
      horas_dia: 'Horas de uso diario',
      precio_kwh: 'Precio de la electricidad (varía por contrato y país)'
    },
    result_context: 'Aparato de {potencia_w}W usado {horas_dia}h/día consume {consumo_diario_kwh} kWh/día, {consumo_mensual_kwh} kWh/mes. Costo mensual: {costo_mensual}€.',
    formula_display: 'Consumo_diario = potencia_W × horas ÷ 1000; Costo = consumo × precio × 30',
    steps: [
      'Calcular consumo diario: 1000W × 5h ÷ 1000 = 5 kWh/día',
      'Calcular consumo mensual: 5 kWh × 30 días = 150 kWh/mes',
      'Calcular costo: 150 kWh × 0.15 €/kWh = 22.50€/mes',
      'Comparar con otros aparatos para identificar mayores consumidores'
    ],
    mistakes: [
      'No considerar consumo en standby (puede ser 5-10% del total)',
      'Usar potencia nominal en lugar de consumo real medido',
      'No considerar variación de precio por horas punta/valle'
    ]
  },
  'aire-acondicionado-btu': {
    example_label: () => 'Calcular capacidad de aire acondicionado para habitación de 25m² con 2.6m de altura, orientación sur y aislamiento bueno.',
    range_hints: {
      area_m2: 'Superficie de la habitación a climatizar',
      altura_m: 'Altura del techo (afecta volumen)',
      orientacion: 'Norte: menos calor, Sur: más calor solar',
      aislamiento: 'Bajo/Medio/Alto afecta ganancia/pérdida térmica'
    },
    result_context: 'Habitación de {area_m2}m² con {altura_m}m de altura requiere equipo de {btu} BTU/h ({toneladas} toneladas). Potencia eléctrica: {potencia_kw} kW.',
    formula_display: 'BTU = área × altura × factor (40-60 según orientación/aislamiento)',
    steps: [
      'Calcular volumen: 25m² × 2.6m = 65m³',
      'Factor orientación sur + aislamiento bueno: 50 BTU/m³',
      'Calcular BTU: 65m³ × 50 = 3250 BTU/h',
      'Para m² método rápido: 25m² × 600 BTU/m² = 15000 BTU/h',
      'Convertir a toneladas: 15000 ÷ 12000 = 1.25 toneladas'
    ],
    mistakes: [
      'Dimensionar solo por m² sin considerar altura y orientación',
      'No prever capacidad adicional para techos con mucho sol',
      'Instalar equipo sobredimensionado (cicla mucho, no deshumidifica bien)'
    ]
  },
  'conductos-aire': {
    example_label: () => 'Calcular diámetro de conducto de aire para caudal de 500 m³/h con velocidad de 4 m/s.',
    range_hints: {
      caudal_m3h: 'Caudal de aire a circular',
      velocidad_ms: 'Conductos principales: 4-6 m/s, Ramales: 3-4 m/s, Difusores: 2-3 m/s'
    },
    result_context: 'Para {caudal_m3h} m³/h a {velocidad_ms} m/s se necesita conducto de {diametro_mm}mm de diámetro ({area_cm2} cm² de sección).',
    formula_display: 'Sección_m2 = caudal_m3/s ÷ velocidad; Diámetro = 2 × √(sección ÷ π)',
    steps: [
      'Convertir caudal a m³/s: 500 m³/h ÷ 3600 = 0.139 m³/s',
      'Calcular sección: 0.139 m³/s ÷ 4 m/s = 0.0347 m²',
      'Calcular diámetro: 2 × √(0.0347 ÷ π) = 0.210m = 210mm',
      'Diámetro comercial: 200mm o 250mm según disponibilidad'
    ],
    mistakes: [
      'Usar velocidad muy alta (ruido excesivo)',
      'Usar velocidad muy baja (conductos muy grandes, costo mayor)',
      'No considerar pérdidas por codos y derivaciones'
    ]
  },
  'ventilacion-mecanica': {
    example_label: () => 'Calcular ventilación mecánica para vivienda de 90m² con 2.5m de altura y 0.5 renovaciones/hora.',
    range_hints: {
      area_m2: 'Superficie útil de la vivienda',
      altura_m: 'Altura libre de techos',
      renovaciones_hora: 'Vivienda: 0.5-1 ren/h, Oficinas: 2-4 ren/h, Gimnasios: 6-8 ren/h'
    },
    result_context: 'Vivienda de {area_m2}m² con {altura_m}m de altura requiere ventilador de {caudal_m3h} m³/h ({caudal_ls} L/s) para {renovaciones_hora} renovaciones/hora.',
    formula_display: 'Volumen = área × altura; Caudal = volumen × renovaciones_hora',
    steps: [
      'Calcular volumen: 90m² × 2.5m = 225m³',
      'Calcular caudal: 225m³ × 0.5 ren/h = 112.5 m³/h',
      'Convertir a L/s: 112.5 ÷ 3.6 = 31.25 L/s',
      'Seleccionar ventilador: 120-150 m³/h (con margen)'
    ],
    mistakes: [
      'No considerar renovación mínima según normativa (CTE DB-HS3)',
      'Instalar ventilador sin recuperación de calor (pérdida energética)',
      'No prever entrada de aire desde exteriores (ventanas, rejillas)'
    ]
  },
  'default': {
    example_label: (inputs, example_inputs) => `Calcular ${inputs.map(i => i.id).join(', ')} para este cálculo.`,
    range_hints: {},
    result_context: 'Resultado del cálculo con los valores ingresados.',
    formula_display: 'Ver fórmula en calculadora',
    steps: [
      'Ingresar valores en los campos',
      'Presionar calcular',
      'Revisar resultados'
    ],
    mistakes: [
      'No verificar unidades de medida',
      'Usar valores fuera de rango',
      'No considerar márgenes de seguridad'
    ]
  }
};

// Generate all 55 calculators
const calculators = calculatorsData.calculators.slice(0, 55).map(calc => generateCalculatorData(calc));

const output = { calculators };

fs.writeFileSync('batch_001-055_fixed.json', JSON.stringify(output, null, 2), 'utf8');
console.log('Generated batch_001-055_fixed.json with', calculators.length, 'calculators');

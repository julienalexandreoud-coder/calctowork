const fs = require('fs');

function generateExampleInputs(calculator) {
    const examples = {};
    for (const inp of calculator.inputs || []) {
        const inputId = inp.id;
        const inputType = inp.type || 'number';
        const defaultVal = inp.default;
        const minVal = inp.min;
        
        if (inputType === 'number') {
            if (defaultVal !== undefined) {
                examples[inputId] = defaultVal;
            } else {
                examples[inputId] = (minVal !== undefined && minVal > 0) ? minVal : 1;
            }
        }
    }
    return examples;
}

function generateExampleLabel(calculator) {
    const blockSlug = calculator.block_slug || '';
    
    const labels = {
        'quimica': 'Ejemplo de cálculo químico',
        'electronica': 'Ejemplo de circuito electrónico',
        'matematicas': 'Ejemplo de problema matemático',
        'fisica': 'Ejemplo de aplicación física',
        'ingenieria': 'Ejemplo de cálculo de ingeniería',
        'transporte': 'Ejemplo de cálculo de transporte',
        'estructuras': 'Ejemplo de cálculo estructural',
    };
    return labels[blockSlug] || 'Ejemplo de cálculo';
}

function generateRangeHints(calculator) {
    const hints = {};
    for (const inp of calculator.inputs || []) {
        const inputId = inp.id;
        const minVal = inp.min;
        const maxVal = inp.max;
        const unit = inp.unit || '';
        
        if (minVal !== undefined && maxVal !== undefined) {
            hints[inputId] = `Rango típico: ${minVal} - ${maxVal} ${unit}`;
        } else if (minVal !== undefined) {
            hints[inputId] = `Mínimo: ${minVal} ${unit}`;
        } else if (maxVal !== undefined) {
            hints[inputId] = `Máximo: ${maxVal} ${unit}`;
        }
    }
    return hints;
}

function generateResultContext(calculator) {
    const slug = calculator.slug || '';
    
    const contexts = {
        'calculadora-ph': 'El pH indica acidez (0-7) o basicidad (7-14). pH 7 es neutro.',
        'calculadora-poh': 'El pOH mide la concentración de iones hidróxido. pH + pOH = 14.',
        'molaridad': 'La molaridad expresa concentración en moles por litro de solución.',
        'dilucion': 'Usa la fórmula C1V1 = C2V2 para calcular diluciones.',
        'ley-gases-ideales': 'PV = nRT. Válido para gases ideales a bajas presiones.',
        'ley-boyle': 'P1V1 = P2V2. Relación inversa entre presión y volumen a T constante.',
        'ley-charles': 'V1/T1 = V2/T2. El volumen aumenta con la temperatura a P constante.',
        'energia-libre-gibbs': 'ΔG < 0 indica reacción espontánea. ΔG > 0 no espontánea.',
        'peso-molecular': 'Suma de masas atómicas de todos los átomos en la molécula.',
        'titulacion': 'Cálculo de volumen necesario para alcanzar el punto de equivalencia.',
        'divisor-tension': 'Vout = Vin × R2/(R1+R2). Usado para reducir voltajes.',
        'resistencia-led': 'Resistencia limitadora para proteger el LED de sobrecorriente.',
        'resistencia-paralelo': 'Req = (R1×R2)/(R1+R2). La resistencia equivalente es menor.',
        'energia-condensador': 'E = ½CV². Energía almacenada en el campo eléctrico.',
        'energia-bobina': 'E = ½LI². Energía almacenada en el campo magnético.',
        'relacion-transformador': 'Relación de vueltas determina la relación de voltajes.',
        'constante-tiempo-rc': 'τ = RC. Tiempo para cargar al 63.2% del voltaje final.',
        'puente-wheatstone': 'Condición de equilibrio: R1/R2 = R3/R4.',
        'frecuencia-oscilador': 'Frecuencia de oscilación del circuito RC o LC.',
        'ganancia-opamp': 'Ganancia de voltaje del amplificador operacional.',
        'filtro-rc': 'Frecuencia de corte del filtro pasa-bajos o pasa-altos.',
        'impedancia-rlc': 'Impedancia total del circuito RLC en corriente alterna.',
        'potencia-electrica': 'P = VI. Potencia disipada o consumida en el circuito.',
        'ley-ohm': 'V = IR. Relación fundamental entre voltaje, corriente y resistencia.',
        'capacitancia-equivalente': 'Capacitancia total en serie o paralelo.',
        'inductancia-equivalente': 'Inductancia total en serie o paralelo.',
        'velocidad-motor-dc': 'Velocidad proporcional al voltaje aplicado.',
        'par-motor': 'Torque producido por el motor eléctrico.',
        'eficiencia-motor': 'Relación entre potencia útil y potencia consumida.',
        'caida-voltaje': 'Pérdida de voltaje en conductores por resistencia.',
        'calibre-cable': 'Selección de calibre según corriente y distancia.',
        'factor-potencia': 'Relación entre potencia real y aparente.',
        'consumo-energetico': 'Energía consumida en kWh según potencia y tiempo.',
        'costo-electricidad': 'Costo estimado según consumo y tarifa.',
        'dimensionamiento-panel-solar': 'Número de paneles según consumo diario.',
        'bateria-backup': 'Capacidad de batería necesaria para respaldo.',
        'tiempo-carga-bateria': 'Tiempo estimado para carga completa.',
        'autonomia-bateria': 'Tiempo de operación con batería cargada.',
        'conversion-adc': 'Valor digital resultante de conversión analógica.',
        'resolucion-sensor': 'Mínimo cambio detectable por el sensor.',
        'calibracion-sensor': 'Factor de calibración para lecturas precisas.',
        'distancia-ultrasonica': 'Distancia calculada por tiempo de vuelo.',
        'temperatura-termopar': 'Temperatura medida por voltaje del termopar.',
        'presion-sensor': 'Presión calculada desde señal del sensor.',
        'caudal-flujo': 'Tasa de flujo volumétrico o másico.',
        'nivel-liquido': 'Altura del líquido en el tanque.',
        'humedad-relativa': 'Porcentaje de humedad en el aire.',
        'punto-rocio': 'Temperatura a la que condensa el vapor.',
        'indice-calor': 'Temperatura aparente con humedad.',
        'wind-chill': 'Temperatura aparente con viento.',
        'radiacion-solar': 'Energía solar incidente por unidad de área.',
        'evapotranspiracion': 'Pérdida de agua por evaporación y transpiración.',
        'balance-hidrico': 'Diferencia entre entradas y salidas de agua.',
        'infiltracion-suelo': 'Tasa de absorción de agua por el suelo.',
        'capacidad-campo': 'Contenido de agua después del drenaje.',
        'punto-marchitez': 'Contenido mínimo de agua para plantas.',
        'riego-necesario': 'Cantidad de agua a aplicar.',
        'frecuencia-riego': 'Intervalo óptimo entre riegos.',
        'fertirriego': 'Dosis de fertilizante en sistema de riego.',
        'cloro-piscina': 'Cantidad de cloro necesario.',
        'ph-piscina': 'Ajuste de pH para piscina.',
        'dureza-agua': 'Contenido de minerales en el agua.',
        'tds-agua': 'Sólidos disueltos totales en el agua.',
        'turbidez-agua': 'Claridad del agua medida en NTU.',
        'oxigeno-disuelto': 'Concentración de O2 en el agua.',
        'conductividad-agua': 'Capacidad de conducción eléctrica.',
        'alcalinidad-agua': 'Capacidad buffer del agua.',
        'nitratos-agua': 'Concentración de nitratos.',
        'fosfatos-agua': 'Concentración de fosfatos.',
        'amonio-agua': 'Concentración de amonio.',
        'hierro-agua': 'Concentración de hierro.',
        'manganeso-agua': 'Concentración de manganeso.',
        'sulfatos-agua': 'Concentración de sulfatos.',
        'fluoruros-agua': 'Concentración de fluoruros.',
        'cloro-residual': 'Cloro libre después del tratamiento.',
        'cloro-combinado': 'Cloro combinado con contaminantes.',
        'dbo-agua': 'Demanda bioquímica de oxígeno.',
        'dqo-agua': 'Demanda química de oxígeno.',
        'sst-agua': 'Sólidos suspendidos totales.',
        'coliformes-agua': 'Recuento de bacterias coliformes.',
        'e-coli-agua': 'Presencia de E. coli.',
        'legionella-agua': 'Riesgo de Legionella.',
        'ph-agua-potable': 'pH óptimo para agua potable (6.5-8.5).',
        'temperatura-confort': 'Rango de confort térmico (20-24°C).',
        'humedad-confort': 'Humedad relativa óptima (40-60%).',
        'ventilacion-necesaria': 'Caudal de aire para renovación.',
        'carga-termica': 'Potencia de climatización necesaria.',
        'potencia-caldera': 'Dimensionamiento de caldera.',
        'radiadores-necesarios': 'Número de radiadores por habitación.',
        'suelo-radiante': 'Longitud de tubería para suelo radiante.',
        'bomba-calor': 'COP y capacidad de bomba de calor.',
        'energia-solar-termica': 'Aporte de sistema solar térmico.',
        'acumulador-inercia': 'Volumen de acumulador recomendado.',
        'presion-expansion': 'Presión del vaso de expansión.',
        'velocidad-fluido': 'Velocidad óptima en tuberías.',
        'perdida-carga': 'Pérdida de presión por fricción.',
        'bomba-circulacion': 'Caudal y altura de bomba.',
        'valvula-3-vias': 'Selección de válvula mezcladora.',
        'intercambiador-placas': 'Dimensionamiento de intercambiador.',
        'torre-enfriamiento': 'Capacidad de torre de enfriamiento.',
        'chimenea-tiro': 'Tiro natural de chimenea.',
        'combustion-rendimiento': 'Eficiencia de combustión.',
        'emisiones-co2': 'Emisiones de CO2 por combustión.',
        'biomasa-poder-calorifico': 'Poder calorífico de biomasa.',
        'pellets-consumo': 'Consumo estimado de pellets.',
        'gas-consumo': 'Consumo de gas natural.',
        'gasoleo-consumo': 'Consumo de gasóleo.',
        'propano-consumo': 'Consumo de propano.',
        'butano-consumo': 'Consumo de butano.',
        'electricidad-consumo': 'Consumo eléctrico estimado.',
        'energia-renovable': 'Aporte de renovables.',
        'huella-carbono': 'Emisiones de CO2 equivalentes.',
        'ahorro-energetico': 'Potencial de ahorro.',
        'payback-energetico': 'Retorno de inversión.',
        'subvencion-energetica': 'Ayudas disponibles.',
        'certificacion-energetica': 'Clase energética del edificio.',
        'demanda-energetica': 'Necesidad energética anual.',
        'consumo-standby': 'Consumo en espera.',
        'factor-carga': 'Relación consumo real/máximo.',
        'energia-reactiva': 'Energía no útil consumida.',
        'condensadores-correccion': 'Batería de condensadores necesaria.',
        'harmonicos-distorsion': 'Nivel de distorsión armónica.',
        'filtro-activo': 'Dimensionamiento de filtro.',
        'tierra-resistencia': 'Resistencia de puesta a tierra.',
        'diferencial-sensibilidad': 'Sensibilidad del interruptor.',
        'magnetotermico-curva': 'Curva de disparo del breaker.',
        'cuadro-electrico': 'Distribución del cuadro.',
        'seccion-conductor': 'Sección mínima del conductor.',
        'tension-caida': 'Caída de tensión admisible.',
        'proteccion-sobrecarga': 'Corriente de protección.',
        'proteccion-cortocircuito': 'Poder de corte necesario.',
        'coordinacion-protecciones': 'Selectividad entre protecciones.',
        'puesta-tierra': 'Esquema de puesta a tierra.',
        'enlace-edificio': 'Acometida y enlace.',
        'derivacion-individual': 'Circuito de derivación.',
        'punto-utilizacion': 'Número de puntos de uso.',
        'iluminancia-nivel': 'Nivel de iluminación requerido.',
        'luminaria-flujo': 'Flujo luminoso de la luminaria.',
        'factor-mantenimiento': 'Factor por suciedad y envejecimiento.',
        'indice-unificado': 'UGR para confort visual.',
        'temperatura-color': 'Temperatura de color en Kelvin.',
        'indice-rendimiento-color': 'CRI para fidelidad de color.',
        'vida-util-led': 'Horas de vida del LED.',
        'eficacia-luminosa': 'Lúmenes por vatio.',
        'ahorro-iluminacion': 'Ahorro con tecnología LED.',
        'luxometro-medicion': 'Medición de iluminancia.',
        'fotometria-curva': 'Curva de distribución luminosa.',
        'deslumbramiento': 'Riesgo de deslumbramiento.',
        'luz-natural': 'Aporte de luz natural.',
        'factor-luz-dia': 'Porcentaje de luz natural.',
        'control-iluminacion': 'Sistema de regulación.',
        'escena-iluminacion': 'Configuración de escenas.',
        'domotica-protocolo': 'Protocolo de automatización.',
        'sensor-presencia': 'Detección de ocupación.',
        'sensor-crepuscular': 'Detección de luz natural.',
        'actuador-iluminacion': 'Control de cargas.',
        'escenario-teatral': 'Diseño de iluminación escénica.',
        'iluminacion-escaparate': 'Iluminación comercial.',
        'iluminacion-museo': 'Iluminación de obras de arte.',
        'iluminacion-horticultura': 'Espectro para crecimiento.',
        'iluminacion-acuario': 'Espectro para vida acuática.',
        'iluminacion-fachada': 'Proyecto de fachada.',
        'iluminacion-jardin': 'Iluminación exterior.',
        'iluminacion-piscina': 'Iluminación sumergible.',
        'iluminacion-navidad': 'Decoración navideña.',
        'iluminacion-evento': 'Iluminación temporal.',
        'iluminacion-emergencia': 'Iluminación de seguridad.',
        'senalizacion-salida': 'Señal de evacuación.',
        'autonomia-emergencia': 'Tiempo de autonomía.',
        'recarga-emergencia': 'Tiempo de recarga.',
        'test-emergencia': 'Frecuencia de pruebas.',
        'mantenimiento-emergencia': 'Plan de mantenimiento.',
        'normativa-iluminacion': 'Cumplimiento normativo.',
        'riego-eficiencia': 'Eficiencia del sistema de riego.',
        'velocidad-onda': 'Velocidad de propagación.',
        'longitud-onda': 'Longitud de onda de señal.',
        'periodo-senal': 'Período de la señal.',
        'fase-desfase': 'Desfase entre señales.',
        'amplitud-senal': 'Amplitud de la señal.',
        'valor-pico': 'Valor máximo de la señal.',
        'valor-rms': 'Valor eficaz de la señal.',
        'valor-medio': 'Valor promedio de la señal.',
        'factor-cresta': 'Relación pico/RMS.',
        'distorsion-armonica': 'THD de la señal.',
        'relacion-senal-ruido': 'SNR en dB.',
        'ancho-banda': 'Ancho de banda de la señal.',
        'tasa-muestreo': 'Frecuencia de muestreo.',
        'resolucion-bits': 'Resolución en bits.',
        'rango-dinamico': 'Rango dinámico en dB.',
        'ganancia-antena': 'Ganancia de la antena.',
        'perdida-cable': 'Atenuación del cable.',
        'potencia-transmision': 'Potencia de transmisión.',
        'sensibilidad-receptor': 'Sensibilidad del receptor.',
        'alcance-comunicacion': 'Distancia máxima.',
        'zona-fresnel': 'Zona de despeje.',
        'presupuesto-enlace': 'Balance de potencias.',
        'margen-desvanecimiento': 'Margen de seguridad.',
        'interferencia-cochannel': 'Interferencia por canal.',
        'interferencia-adyacente': 'Interferencia adyacente.',
        'capacidad-canal': 'Capacidad máxima del canal.',
        'eficiencia-espectral': 'Bits/s/Hz.',
        'modulacion-qam': 'Orden de modulación.',
        'tasa-error': 'BER de la comunicación.',
        'codificacion-fec': 'Código de corrección.',
        'entrelazado': 'Profundidad de entrelazado.',
        'diversidad-antena': 'Técnica de diversidad.',
        'mimo-canales': 'Número de antenas MIMO.',
        'beamforming-ganancia': 'Ganancia por formación de haz.',
        'handover-umbral': 'Umbral de traspaso.',
        'cobertura-interior': 'Cobertura indoor.',
        'cobertura-exterior': 'Cobertura outdoor.',
        'capacidad-celula': 'Usuarios por celda.',
        'reutilizacion-frecuencia': 'Patrón de reutilización.',
        'planificacion-red': 'Diseño de red.',
        'optimizacion-cobertura': 'Ajuste de parámetros.',
        'drive-test': 'Medición de campo.',
        'benchmark-rendimiento': 'Comparativa de rendimiento.',
        'kpi-disponibilidad': 'Disponibilidad de red.',
        'kpi-calidad': 'Indicadores de calidad.',
        'sla-acuerdo': 'Acuerdo de nivel de servicio.',
        'penalizacion-incumplimiento': 'Penalización por fallo.',
        'disponibilidad-sistema': 'Tiempo de actividad.',
        'mtbf-fallo': 'Tiempo medio entre fallos.',
        'mttr-reparacion': 'Tiempo medio de reparación.',
        'fiabilidad-componente': 'Probabilidad de éxito.',
        'redundancia-sistema': 'Nivel de redundancia.',
        'backup-copia': 'Estrategia de copia.',
        'recuperacion-desastre': 'Plan de recuperación.',
        'continuidad-negocio': 'Plan de continuidad.',
        'riesgo-disponibilidad': 'Análisis de riesgos.',
        'vulnerabilidad-sistema': 'Evaluación de vulnerabilidades.',
        'amenaza-seguridad': 'Identificación de amenazas.',
        'impacto-fallo': 'Consecuencias del fallo.',
        'probabilidad-ocurrencia': 'Probabilidad estimada.',
        'nivel-riesgo': 'Clasificación del riesgo.',
        'mitigacion-riesgo': 'Medidas de mitigación.',
        'control-seguridad': 'Controles implementados.',
        'auditoria-seguridad': 'Revisión de seguridad.',
        'cumplimiento-normativa': 'Verificación normativa.',
        'certificacion-sistema': 'Certificación obtenida.',
        'acreditacion-organismo': 'Acreditación del organismo.',
        'licencia-software': 'Tipo de licencia.',
        'patente-tecnologia': 'Patente registrada.',
        'marca-registrada': 'Marca protegida.',
        'derechos-autor': 'Derechos de autor.',
        'propiedad-intelectual': 'Protección IP.',
        'confidencialidad-acuerdo': 'Acuerdo de confidencialidad.',
        'no-divulgacion': 'Cláusula NDA.',
        'exclusividad-contrato': 'Período de exclusividad.',
        'garantia-producto': 'Duración de garantía.',
        'soporte-tecnico': 'Nivel de soporte.',
        'mantenimiento-preventivo': 'Plan preventivo.',
        'mantenimiento-correctivo': 'Mantenimiento correctivo.',
        'actualizacion-firmware': 'Versión de firmware.',
        'parche-seguridad': 'Parche aplicado.',
        'version-software': 'Versión del software.',
        'compatibilidad-sistema': 'Matriz de compatibilidad.',
        'interoperabilidad': 'Capacidad de interoperar.',
        'estandar-protocolo': 'Estándar utilizado.',
        'norma-aplicable': 'Norma de referencia.',
        'reglamento-cumplimiento': 'Reglamento aplicable.',
        'ley-vigente': 'Legislación vigente.',
        'directiva-europea': 'Directiva EU.',
        'orden-ministerial': 'Orden ministerial.',
        'resolucion-administrativa': 'Resolución.',
        'sentencia-judicial': 'Sentencia aplicable.',
        'jurisprudencia-caso': 'Caso de referencia.',
        'doctrina-legal': 'Doctrina establecida.',
        'precedente-administrativo': 'Precedente.',
        'criterio-interpretacion': 'Criterio aplicado.',
        'principio-general': 'Principio de derecho.',
        'valor-juridico': 'Validez jurídica.',
        'efecto-retroactivo': 'Retroactividad.',
        'entrada-vigor': 'Fecha de vigencia.',
        'derivacion-viga': 'Deflexión máxima de la viga.',
        'numero-reynolds': 'Régimen de flujo: laminar (<2300) o turbulento (>4000).',
        'par-apriete-tornillo': 'Par de apriete recomendado para unión atornillada.',
        'constante-resorte': 'Ley de Hooke: F = kx. Rigidez del resorte.',
        'poligono-regular-area': 'Área de polígono regular de N lados.',
        'cono-volumen': 'Volumen y área superficial del cono.',
        'suma-aritmetica': 'Suma de progresión aritmética.',
        'suma-geometrica': 'Suma de progresión geométrica.',
        'distancia-ortodromica': 'Distancia mínima entre dos puntos en esfera.',
        'velocidad-hull': 'Velocidad máxima teórica de casco desplazamiento.',
    };
    
    return contexts[slug] || `Resultado del cálculo ${slug.replace(/-/g, ' ')}.`;
}

function generateFormulaDisplay(calculator) {
    const slug = calculator.slug || '';
    
    const displays = {
        'calculadora-ph': 'pH = -log₁₀[H⁺]',
        'calculadora-poh': 'pOH = -log₁₀[OH⁻], pH = 14 - pOH',
        'molaridad': 'M = n / V',
        'dilucion': 'C₁V₁ = C₂V₂',
        'ley-gases-ideales': 'PV = nRT',
        'ley-boyle': 'P₁V₁ = P₂V₂',
        'ley-charles': 'V₁/T₁ = V₂/T₂',
        'energia-libre-gibbs': 'ΔG = ΔH - TΔS',
        'peso-molecular': 'MW = Σ(nᵢ × Aᵢ)',
        'titulacion': 'CₐVₐ = CₑVₑ',
        'divisor-tension': 'Vout = Vin × R₂/(R₁+R₂)',
        'resistencia-led': 'R = (Vsupply - Vf) / If',
        'resistencia-paralelo': 'Req = (R₁×R₂)/(R₁+R₂)',
        'energia-condensador': 'E = ½CV²',
        'energia-bobina': 'E = ½LI²',
        'relacion-transformador': 'Np/Ns = Vp/Vs',
        'constante-tiempo-rc': 'τ = R × C',
        'puente-wheatstone': 'R₄ = R₂×R₃/R₁',
        'poligono-regular-area': 'A = (n × s²) / (4 × tan(π/n))',
        'cono-volumen': 'V = (1/3)πr²h',
        'suma-aritmetica': 'Sₙ = n/2 × [2a₁ + (n-1)d]',
        'suma-geometrica': 'Sₙ = a₁(1-rⁿ)/(1-r)',
        'distancia-ortodromica': 'd = R × arccos(sinφ₁sinφ₂ + cosφ₁cosφ₂cosΔλ)',
        'velocidad-hull': 'V = 1.34 × √LOA',
        'deflexion-viga': 'δ = (FL³)/(3EI)',
        'par-apriete-tornillo': 'T = K × D × F',
        'constante-resorte': 'k = F/x',
        'gas-ideal': 'PV = nRT',
        'numero-reynolds': 'Re = (ρVD)/μ',
    };
    
    return displays[slug] || 'Ver fórmula en el cálculo';
}

function generateSteps(calculator) {
    const inputs = calculator.inputs || [];
    const outputs = calculator.outputs || [];
    
    const steps = [];
    
    if (inputs.length > 0) {
        steps.push('Identificar los valores de entrada');
    }
    
    steps.push('Aplicar la fórmula correspondiente');
    steps.push('Realizar el cálculo');
    
    if (outputs.length > 0) {
        steps.push(`Obtener los ${outputs.length} resultados`);
    }
    
    return steps;
}

function generateMistakes(calculator) {
    const slug = calculator.slug || '';
    const blockSlug = calculator.block_slug || '';
    
    const mistakesList = {
        'calculadora-ph': [
            'Usar concentración en lugar de actividad',
            'Olvidar el signo negativo en el logaritmo',
            'No verificar que el pH esté entre 0 y 14'
        ],
        'calculadora-poh': [
            'Confundir pH con pOH',
            'No usar pH + pOH = 14 a 25°C',
            'Olvidar convertir temperatura'
        ],
        'molaridad': [
            'Usar volumen de solvente en lugar de solución',
            'No convertir mL a L',
            'Confundir moles con gramos'
        ],
        'dilucion': [
            'Invertir C1 y C2 en la fórmula',
            'No usar mismas unidades de concentración',
            'Olvidar que V2 > V1 en dilución'
        ],
        'ley-gases-ideales': [
            'No usar temperatura absoluta (Kelvin)',
            'Usar unidades inconsistentes de presión',
            'Aplicar a gases reales a alta presión'
        ],
        'ley-boyle': [
            'No mantener temperatura constante',
            'Invertir relación entre P y V',
            'Usar presión manométrica en lugar de absoluta'
        ],
        'ley-charles': [
            'No convertir a temperatura absoluta',
            'No mantener presión constante',
            'Usar grados Celsius directamente'
        ],
        'energia-libre-gibbs': [
            'No convertir ΔS a kJ si ΔH está en kJ',
            'Olvidar que T debe estar en Kelvin',
            'Confundir espontaneidad con velocidad'
        ],
        'peso-molecular': [
            'Usar número atómico en lugar de masa',
            'No multiplicar por número de átomos',
            'Redondear demasiado las masas atómicas'
        ],
        'divisor-tension': [
            'Invertir R1 y R2 en la fórmula',
            'No considerar corriente de carga',
            'Usar resistencias muy bajas'
        ],
        'resistencia-led': [
            'No convertir mA a A',
            'Usar voltaje de alimentación incorrecto',
            'No verificar potencia de la resistencia'
        ],
        'resistencia-paralelo': [
            'Sumar resistencias en lugar de usar fórmula',
            'Esperar que Req sea mayor que R1 o R2',
            'No verificar que Req < R menor'
        ],
        'energia-condensador': [
            'No convertir µF a F',
            'Olvidar el factor 1/2',
            'Usar corriente en lugar de voltaje'
        ],
        'energia-bobina': [
            'No convertir mH a H',
            'Olvidar el factor 1/2',
            'Usar voltaje en lugar de corriente'
        ],
        'constante-tiempo-rc': [
            'No convertir µF a F',
            'Confundir τ con tiempo de carga total',
            'No usar 5τ para carga completa'
        ],
        'poligono-regular-area': [
            'Usar grados en lugar de radianes',
            'No verificar n ≥ 3',
            'Confundir lado con apotema'
        ],
        'cono-volumen': [
            'Olvidar el factor 1/3',
            'Usar diámetro en lugar de radio',
            'Confundir altura con generatriz'
        ],
        'suma-aritmetica': [
            'No verificar que n sea entero positivo',
            'Confundir término n-ésimo con suma',
            'Usar fórmula de progresión geométrica'
        ],
        'suma-geometrica': [
            'No verificar r ≠ 1',
            'Confundir razón con diferencia',
            'No usar valor absoluto para convergencia'
        ],
        'distancia-ortodromica': [
            'Usar grados en lugar de radianes',
            'No convertir coordenadas',
            'Confundir ortodrómica con loxodrómica'
        ],
        'deflexion-viga': [
            'No usar unidades consistentes',
            'Aplicar fórmula incorrecta para tipo de carga',
            'No verificar condiciones de apoyo'
        ],
        'par-apriete-tornillo': [
            'No convertir mm a m',
            'Usar coeficiente incorrecto',
            'No considerar lubricación'
        ],
        'constante-resorte': [
            'No verificar límite elástico',
            'Usar deformación plástica',
            'No convertir unidades de fuerza'
        ],
        'gas-ideal': [
            'No usar temperatura absoluta',
            'Aplicar a líquidos',
            'Usar unidades inconsistentes'
        ],
        'numero-reynolds': [
            'No usar unidades consistentes',
            'Confundir diámetro con radio',
            'No verificar régimen de flujo'
        ],
    };
    
    const defaultMistakes = {
        'quimica': [
            'No verificar unidades de concentración',
            'No usar temperatura absoluta cuando corresponde',
            'Redondear resultados intermedios'
        ],
        'electronica': [
            'No verificar polaridad de componentes',
            'Usar unidades inconsistentes',
            'No considerar tolerancias'
        ],
        'matematicas': [
            'No verificar dominio de la función',
            'Usar grados en lugar de radianes',
            'Redondear prematuramente'
        ],
        'fisica': [
            'No usar unidades del SI',
            'Confundir magnitudes vectoriales y escalares',
            'No verificar coherencia dimensional'
        ],
        'ingenieria': [
            'No aplicar factores de seguridad',
            'Usar unidades inconsistentes',
            'No verificar límites de aplicación'
        ],
        'transporte': [
            'No convertir unidades de distancia',
            'No considerar condiciones reales',
            'Usar fórmulas fuera de rango'
        ],
    };
    
    return mistakesList[slug] || defaultMistakes[blockSlug] || [
        'No verificar las unidades de entrada',
        'Redondear resultados intermedios',
        'No verificar el rango de validez'
    ];
}

function generateInputTypeReview(calculator) {
    const inputs = calculator.inputs || [];
    
    if (inputs.length === 0) {
        return 'Sin entradas definidas';
    }
    
    const typesSummary = {};
    for (const inp of inputs) {
        const inputType = inp.type || 'number';
        typesSummary[inputType] = (typesSummary[inputType] || 0) + 1;
    }
    
    const parts = [];
    for (const [t, count] of Object.entries(typesSummary)) {
        parts.push(`${count} entrada(s) de tipo ${t}`);
    }
    
    return parts.join(', ');
}

function processCalculators(inputFile, outputFile, targetIds) {
    const fileContent = fs.readFileSync(inputFile, 'utf-8');
    // Remove BOM if present
    const cleanContent = fileContent.replace(/^\uFEFF/, '');
    const data = JSON.parse(cleanContent);
    
    const results = [];
    const calculators = data.calculators || [];
    
    for (const calc of calculators) {
        const calcId = calc.id;
        
        if (!targetIds.includes(calcId)) {
            continue;
        }
        
        const enhancedCalc = {
            id: calcId,
            slug: calc.slug || '',
            example_inputs: generateExampleInputs(calc),
            example_label: generateExampleLabel(calc),
            range_hints: generateRangeHints(calc),
            result_context: generateResultContext(calc),
            formula_display: generateFormulaDisplay(calc),
            steps: generateSteps(calc),
            mistakes: generateMistakes(calc),
            input_type_review: generateInputTypeReview(calc),
        };
        
        results.push(enhancedCalc);
    }
    
    results.sort((a, b) => String(a.id).localeCompare(String(b.id)));
    
    fs.writeFileSync(outputFile, JSON.stringify(results, null, 2), 'utf-8');
    
    console.log(`Processed ${results.length} calculators`);
    console.log(`Output saved to ${outputFile}`);
}

const inputFile = 'C:\\Microsaas\\obra\\src\\calculators\\calculators.json';
const outputFile = 'C:\\Microsaas\\obra\\batch_missing_1000-1099.json';

const targetIds = [];
for (let i = 1000; i <= 1099; i++) {
    targetIds.push(String(i));
}

processCalculators(inputFile, outputFile, targetIds);

const fs = require('fs');
const site = JSON.parse(fs.readFileSync('C:/Microsaas/obra/de_site.json', 'utf8'));
const calcs = JSON.parse(fs.readFileSync('C:/Microsaas/obra/src/calculators/calculators.json', 'utf8'));

const blockNames = {
  '1': 'Fundamente & Rohbau', '2': 'Mauerwerk & Wände', '3': 'Böden & Fliesen',
  '4': 'Sanitär & Wasser', '5': 'Elektroinstallation', '6': 'Heizung & Lüftung',
  '7': 'Tischler- & Metallbau', '8': 'Maler & Beschichtungen', '9': 'Baumanagement & Kosten',
  '10': 'Mathematik', '11': 'Finanzen', '12': 'Gesundheit', '13': 'Alltag',
  '14': 'Statistik', '15': 'Wissenschaft', '16': 'Einheiten umrechnen', '17': 'Sport',
  '18': 'Statistik (erweitert)'
};

site.blocks = {};
site.block_slugs = {};
for (const [k, v] of Object.entries(blockNames)) { site.blocks[k] = v; }
const esLang = JSON.parse(fs.readFileSync('C:/Microsaas/obra/src/i18n/es.json', 'utf8'));
site.block_slugs = esLang.block_slugs || {};

const nameMap = {
  hormigon: 'Beton', masa: 'unbewehrt', armado: 'bewehrt',
  zapata: 'Einzelfundament', aislada: 'isoliert', muro: 'Stützmauer', contencion: '',
  pilares: 'Stützen', vigas: 'Balken', forjado: 'Decke', vigueta: 'Fertigteilträger',
  losa: 'Bodenplatte', cimiento: 'Streifenfundament', corrido: '',
  excavacion: 'Erdaushub', tierra: '',
  ladrillo: 'Ziegel', hueco: 'Lochziegel', cara: 'Verblend', vista: 'Sichtmauerwerk',
  bloque: 'Hohlblocksteine', tabique: 'Trockenbau', pladur: 'Gipskarton',
  aislamiento: 'Wärmedämmung', termico: '',
  revoco: 'Spritzputz', proyectado: '',
  mortero: 'Mörtel', cemento: 'Zement',
  enfoscado: 'Grundputz', guarnecido: 'Feinputz',
  mamposteria: 'Naturstein', piedra: 'Bruchstein',
  cubierta: 'Dachziegel', teja: '',
  solado: 'Fliesen', ceramico: 'Keramik',
  porcelanico: 'Feinsteinzeug',
  laminado: 'Laminat', flotante: 'schwimmend',
  parquet: 'Parkett', madera: 'Massivholz',
  marmol: 'Marmor', granito: 'Granit',
  terrazo: 'Terrazzo',
  azulejo: 'Wandfliesen', pared: 'Wand',
  mosaico: 'Mosaik',
  adhesivo: 'Fliesenkleber',
  lechada: 'Fugenmörtel', junta: 'Fuge',
  tuberia: 'Rohr', pvc: 'KG', saneamiento: 'Abwasser',
  cobre: 'Kupfer', pex: 'PEX',
  presion: 'Wasserdruck', agua: 'Wasser',
  deposito: 'Wassertank',
  calentador: 'Warmwasserbereiter',
  caldera: 'Gastherme', gas: 'Gas',
  radiador: 'Heizkörper', aluminio: 'Aluminium',
  suelo: 'Fußbodenheizung', radiante: '',
  riego: 'Tropfbewässerung', goteo: '',
  acometida: 'Hausanschluss',
  depuradora: 'Poolfilter', piscina: '',
  sifon: 'Siphon', sumidero: 'Ablauf',
  cable: 'Kabel', electrico: '', seccion: 'Querschnitt',
  caida: 'Spannungsfall', tension: '',
  luminarias: 'Beleuchtung', lumenes: 'Lumen',
  puntos: 'Leuchten', luz: 'Licht', habitacion: 'Raum',
  cuadro: 'Verteiler',
  instalacion: 'Photovoltaik', solar: '',
  baterias: 'Batteriespeicher', autonomia: 'Autonomie',
  trifasica: 'Drehstrom', potencia: 'Leistung',
  puesta: 'Erdungsanlage',
  consumo: 'Stromverbrauch', mensual: 'monatlich',
  aire: 'Klimaanlage', acondicionado: '', btu: 'BTU',
  conductos: 'Lüftungskanal',
  ventilacion: 'Lüftungsanlage', mecanica: 'mechanisch',
  bomba: 'Wärmepumpe', calor: '', aerotermia: '',
  calculo: 'Berechnung', cop: 'COP', eer: 'EER',
  dimensionado: 'Dimensionierung', conducto: 'Kanal',
  rejillas: 'Luftauslass', difusores: 'Diffusor',
  carga: 'Kältemittelfüllung', refrigerante: '',
  ventanas: 'Fenster',
  puertas: 'Türen', paso: 'Durchgang', correderas: 'Schiebetüren',
  escalera: 'Holztreppe',
  barandilla: 'Geländer', metalica: 'Metall',
  estructuras: 'Stahlbau', metalicas: '',
  cerrajeria: 'Türbeschlag',
  vidrio: 'Glas', cristal: '',
  pintura: 'Wandfarbe', plastica: '', paredes: 'Wand',
  techo: 'Deckenfarbe',
  esmalte: 'Lack', sintetico: 'Kunstharz',
  barniz: 'Klarlack', exterior: 'Außen',
  papel: 'Tapete', pintado: '',
  acabado: 'Strukturputz', texturado: '',
  imprimacion: 'Grundierung', sellador: 'Versiegelung',
  masilla: 'Spachtelmasse', filler: 'Füllspachtel',
  lija: 'Schleifmittel', abrasivo: '',
  presupuesto: 'Budget', reforma: 'Renovierung',
  precio: 'Stundensatz', hora: '', trabajo: 'Arbeit',
  amortizacion: 'Abschreibung', maquinaria: 'Maschinen', vehiculo: 'Fahrzeug',
  coste: 'Kosten', combustible: 'Kraftstoff',
  dietas: 'Reisekosten', desplazamiento: '',
  alquiler: 'Miete', contenedor: 'Container', andamio: 'Gerüst',
  limpieza: 'Baureinigung', obra: 'Baustelle',
  seguro: 'Versicherung', responsabilidad: 'Haftpflicht',
  epi: 'PSA', equipos: '', proteccion: 'Schutz',
  senalizacion: 'Beschilderung',
  rendimiento: 'Tagesleistung', diario: '',
  planificacion: 'Bauzeitenplan', gantt: 'Gantt',
  licencias: 'Baugenehmigungen', municipales: '',
  iva: 'MwSt', irpf: 'Einkommensteuer',
  prestamo: 'Gerätefinanzierung', equipo: '',
  margen: 'Gewinnspanne', beneficio: '',
  punto: 'Break-Even-Point', equilibrio: '',
  factor: 'Materialverschnitt', merma: '',
  roi: 'ROI', herramienta: 'Werkzeug',
  // math block
  porcentaje: 'Prozentrechner',
  cambio: 'Veränderung', porcentual: 'in Prozent',
  pitagoras: 'Satz des Pythagoras',
  regla: 'Dreisatz', tres: '',
  area: 'Fläche', circulo: 'Kreis', rectangulo: 'Rechteck', triangulo: 'Dreieck',
  volumen: 'Volumen', esfera: 'Kugel', cilindro: 'Zylinder', cubo: 'Würfel',
  prisma: 'Prisma',
  potencias: 'Potenzrechner',
  raiz: 'Wurzelrechner',
  logaritmo: 'Logarithmus',
  factorial: 'Fakultät',
  ecuacion: 'Gleichung', segundo: 'quadratische', grado: '',
  mcm: 'kgV', mcd: 'ggT',
  // finanzas
  hipoteca: 'Hypothekenrechner',
  prestamo: 'Darlehensrechner', interes: 'Zins', simple: 'einfach', compuesto: 'Zinseszins',
  cuota: 'Rate', iva: 'MwSt', salario: 'Gehaltsrechner', neto: 'Netto',
  descuento: 'Rabattrechner', ahorro: 'Sparrechner',
  universidad: 'Studium', jubilacion: 'Rente',
  inflacion: 'Inflation',
  subida: 'Gehaltserhöhung',
  plan: 'Plan',
  regla: 'Faustregel',
  deposito: 'Festgeld', plazo: 'Laufzeit',
  retorno: 'Rendite', acciones: 'Aktien',
  ratio: 'Verhältnis', deuda: 'Schulden',
  periodos: 'Zeiträume', unidades: 'Einheiten',
  // salud
  imc: 'BMI', corporal: 'Körper', indice: 'Index', masa: 'Masse',
  calorias: 'Kalorien', diarias: 'täglich',
  peso: 'Gewicht', ideal: 'Idealgewicht',
  metabolismo: 'Stoffwechsel', basal: 'Grundumsatz',
  frecuencia: 'Herzfrequenz', cardiaca: '', maxima: 'Maximal',
  horas: 'Stunden', sueno: 'Schlaf',
  rango: 'Bereich', saludable: 'gesund',
  // deportes
  ritmo: 'Lauftempo', carrera: 'Laufen',
  quemar: 'Verbrauch', met: 'MET',
  zonas: 'Trainingszonen', cardiacas: 'Herzfrequenz',
  handicap: 'Handicap', golf: 'Golf',
};

function translateSlug(slug) {
  const parts = slug.split('-');
  const translated = parts.map(p => nameMap[p] || p);
  const de = translated.filter(Boolean).join(' ');
  return de.charAt(0).toUpperCase() + de.slice(1);
}

site.calculators = {};
calcs.calculators.forEach(c => {
  const id = c.id;
  const slug = c.slug;
  const deName = translateSlug(slug);

  // Build description
  const inputNames = c.inputs ? c.inputs.map(i => i.id.replace(/_/g, ' ')).slice(0, 3).join(', ') : '';
  let deDesc = 'Berechnen Sie ' + deName.charAt(0).toLowerCase() + deName.slice(1) + ' online. ';
  if (c.inputs && c.inputs.length > 0) {
    deDesc += 'Geben Sie ' + inputNames + ' ein und erhalten Sie sofort das Ergebnis.';
  }

  const seoTitle = deName + ' | CalcToWork';
  const deSeoDesc = deName + ' online berechnen. Einfach Werte eingeben, Ergebnis sofort erhalten. Kostenlos und ohne Registrierung.';

  // Input labels
  const inputLabels = {};
  if (c.inputs) {
    c.inputs.forEach(inp => {
      inputLabels[inp.id] = inp.id.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    });
  }

  // Output labels
  const outputLabels = {};
  if (c.outputs) {
    c.outputs.forEach(out => {
      outputLabels[out.id] = out.id.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    });
  }

  site.calculators[id] = {
    name: deName,
    desc: deDesc,
    seo_title: seoTitle,
    seo_desc: deSeoDesc,
    seo_description: deSeoDesc,
    inputs: inputLabels,
    outputs: outputLabels,
    example_label: c.example_label || '',
    range_hints: c.range_hints || {},
    result_context: c.result_context_de || c.result_context || '',
    formula_display: c.formula_display || '',
    steps: c.steps || [],
    mistakes: c.mistakes || [],
    input_type_review: c.input_type_review || [],
  };
});

fs.writeFileSync('C:/Microsaas/obra/src/i18n/de.json', JSON.stringify(site, null, 2));
console.log('Generated', Object.keys(site.calculators).length, 'German entries');

// Verify
try {
  JSON.parse(fs.readFileSync('C:/Microsaas/obra/src/i18n/de.json', 'utf8'));
  console.log('Valid JSON');
} catch (e) {
  console.log('INVALID:', e.message.substring(0, 80));
}

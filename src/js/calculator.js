/* CalcToWork – Calculator Engine v8.0 (Unit Toggle + Rich Outputs) */
(function () {
  'use strict';

  var cfg    = window.CALC_CONFIG || {};
  var i18n   = cfg.i18n || {};
  var form   = document.getElementById('calc-form');
  var resultsBox = document.getElementById('calc-results');
  var resetBtn   = document.getElementById('btn-reset');
  var copyBtn    = document.getElementById('btn-copy');
  var shareBtn   = document.getElementById('btn-share');
  var pdfBtn     = document.getElementById('btn-pdf');
  var addProjectBtn = document.getElementById('btn-add-project');
  var gaugeEl    = document.getElementById('result-gauge');
  var tocLinks   = document.querySelectorAll('.toc-link');
  var feedbackBtns = document.querySelectorAll('.feedback-btn');

  if (!form || !resultsBox) return;

  var calcFn;
  try {
    calcFn = new Function('inputs', cfg.formula || 'return{error:true};');
  } catch (e) {
    console.error('[CalcToWork] Formula compile error:', e);
    calcFn = function () { return { error: true }; };
  }

  /* ── Unit Conversion System ── */
  var UNIT_FACTORS = {
    length: { m: 1, km: 1000, cm: 0.01, mm: 0.001, ft: 0.3048, in: 0.0254, yd: 0.9144, mi: 1609.34 },
    mass: { kg: 1, g: 0.001, mg: 0.000001, lb: 0.453592, oz: 0.0283495, t: 1000, st: 6.35029 },
    time: { s: 1, min: 60, h: 3600, d: 86400, wk: 604800, mo: 2592000, yr: 31536000 },
    velocity: { 'm/s': 1, 'km/h': 0.277778, mph: 0.44704, knot: 0.514444, 'ft/s': 0.3048 },
    speed: { 'm/s': 1, 'km/h': 0.277778, mph: 0.44704, knot: 0.514444, 'ft/s': 0.3048, mach: 340.3 },
    acceleration: { 'm/s²': 1, g: 9.80665, 'ft/s²': 0.3048 },
    force: { N: 1, kN: 1000, lbf: 4.44822, dyn: 0.00001 },
    energy: { J: 1, kJ: 1000, cal: 4.184, kcal: 4184, Wh: 3600, kWh: 3600000, eV: 1.602e-19, BTU: 1055.06 },
    power: { W: 1, kW: 1000, MW: 1000000, hp: 745.7, 'BTU/h': 0.293071 },
    pressure: { Pa: 1, kPa: 1000, MPa: 1000000, bar: 100000, atm: 101325, psi: 6894.76, torr: 133.322, mmHg: 133.322 },
    area: { 'm²': 1, 'km²': 1e6, 'cm²': 0.0001, 'mm²': 1e-6, 'ft²': 0.092903, 'in²': 0.00064516, ac: 4046.86, ha: 10000 },
    volume: { 'm³': 1, L: 0.001, mL: 0.000001, 'cm³': 0.000001, 'ft³': 0.0283168, 'gal(us)': 0.00378541, 'gal(uk)': 0.00454609, qt: 0.000946353 },
    angle: { deg: 1, rad: 57.2958, grad: 0.9 },
    frequency: { Hz: 1, kHz: 1000, MHz: 1000000, GHz: 1e9, rpm: 0.0166667 },
    digital_storage: { B: 1, KB: 1024, MB: 1048576, GB: 1073741824, TB: 1099511627776 },
    data_rate: { bps: 1, Kbps: 1000, Mbps: 1000000, Gbps: 1e9 },
    percentage: { '%': 1 },
    count: { unit: 1, dozen: 12, hundred: 100, thousand: 1000, million: 1e6 },
    density: { 'kg/m³': 1, 'g/cm³': 1000, 'lb/ft³': 16.0185 },
    temperature: { C: 'special', F: 'special', K: 'special' },
    currency_per_volume: { '$/L': 1, '$/gal(us)': 0.264172, '€/L': 1, '€/gal(us)': 0.264172 },
    currency: { USD: 1, EUR: 1, GBP: 1 },
    current: { A: 1, mA: 0.001, kA: 1000 },
    voltage: { V: 1, mV: 0.001, kV: 1000 },
    resistance: { ohm: 1, kohm: 1000, Mohm: 1000000 },
    capacitance: { F: 1, mF: 0.001, uF: 0.000001, nF: 1e-9, pF: 1e-12 },
    /* ── Derived categories: base = the unit the formula expects ── */
    length_cm:    { cm: 1, m: 100, mm: 0.1, km: 100000, ft: 30.48, in: 2.54, yd: 91.44, mi: 160934 },
    length_km:    { km: 1, m: 0.001, cm: 0.00001, mm: 0.000001, mi: 1.60934, ft: 0.0003048, in: 0.0000254 },
    length_mm:    { mm: 1, cm: 10, m: 1000, km: 1000000, ft: 304.8, in: 25.4 },
    volume_L:     { L: 1, mL: 0.001, 'm³': 1000, 'cm³': 0.001, 'ft³': 28.3168, 'gal(us)': 3.78541, 'gal(uk)': 4.54609, qt: 0.946353 },
    speed_kmh:    { 'km/h': 1, 'm/s': 3.6, mph: 1.60934, knot: 1.852, 'ft/s': 1.09728 },
    digital_MB:   { MB: 1, KB: 0.0009766, GB: 1024, TB: 1048576, B: 9.5367e-7 },
    pressure_atm: { atm: 1, Pa: 9.869e-6, kPa: 0.009869, bar: 0.986923, psi: 0.068046, mmHg: 0.001316, torr: 0.001316 },
    time_h:       { h: 1, min: 0.016667, s: 2.7778e-4, d: 24, wk: 168 },
    temp_c:       { '°C': 'special_c', '°F': 'special_c', K: 'special_c', C: 'special_c', F: 'special_c' }
  };

  function toKelvin(val, unit) {
    if (unit === 'C') return val + 273.15;
    if (unit === 'F') return (val - 32) * 5 / 9 + 273.15;
    if (unit === 'K') return val;
    return val;
  }
  function fromKelvin(val, unit) {
    if (unit === 'C') return val - 273.15;
    if (unit === 'F') return (val - 273.15) * 9 / 5 + 32;
    if (unit === 'K') return val;
    return val;
  }

  function toBaseTempC(val, unit) {
    var u = unit.replace('°', '');
    if (u === 'F') return (val - 32) * 5 / 9;
    if (u === 'K') return val - 273.15;
    return val;
  }

  function toBaseUnit(value, unit, category) {
    if (category === 'temperature') return toKelvin(value, unit);
    if (category === 'temp_c') return toBaseTempC(value, unit);
    var factors = UNIT_FACTORS[category];
    if (!factors) return value;
    var factor = factors[unit];
    if (factor === undefined) return value;
    return value * factor;
  }

  function fromBaseUnit(value, unit, category) {
    if (category === 'temperature') return fromKelvin(value, unit);
    var factors = UNIT_FACTORS[category];
    if (!factors) return value;
    var factor = factors[unit];
    if (factor === undefined) return value;
    return value / factor;
  }

  function collectInputs() {
    var inputs = {};
    var fields = form.querySelectorAll('input[name]');
    for (var i = 0; i < fields.length; i++) {
      var name = fields[i].name;
      var rawVal = fields[i].value;
      var numVal = parseFloat(rawVal);
      var unitSel = form.querySelector('.unit-select[data-input="' + name + '"]');
      if (unitSel && !isNaN(numVal)) {
        var category = unitSel.getAttribute('data-category');
        var unit = unitSel.value;
        inputs[name] = toBaseUnit(numVal, unit, category);
      } else {
        inputs[name] = rawVal;
      }
    }
    return inputs;
  }

  function allFilled() {
    var fields = form.querySelectorAll('input[name]:not([name="desperdicio_merma"])');
    for (var i = 0; i < fields.length; i++) {
      var v = fields[i].value.trim();
      if (v === '' || isNaN(parseFloat(v))) return false;
    }
    return fields.length > 0;
  }

  function hasAnyInput() {
    var fields = form.querySelectorAll('input[name]:not([name="desperdicio_merma"])');
    for (var i = 0; i < fields.length; i++) {
      var v = fields[i].value.trim();
      if (v !== '' && !isNaN(parseFloat(v))) return true;
    }
    return false;
  }

  function fmt(val) {
    if (val === null || val === undefined || val === '') return '\u2014';
    var n = parseFloat(val);
    if (isNaN(n)) return String(val);
    return n.toLocaleString(undefined, { maximumFractionDigits: 3 });
  }

  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function makeRow(label, value, extraClass) {
    return (
      '<div class="result-item' + (extraClass ? ' ' + extraClass : '') + '">' +
        '<span class="result-label">' + esc(label) + '</span>' +
        '<span class="result-value">' + esc(String(fmt(value))) + '</span>' +
      '</div>'
    );
  }

  var CATEGORY_CLASSES = {
    /* BMI */
    'bajo peso': 'badge-warning', 'underweight': 'badge-warning',
    'normal': 'badge-ok', 'healthy': 'badge-ok',
    'sobrepeso': 'badge-warn', 'overweight': 'badge-warn',
    'obesidad': 'badge-danger', 'obese': 'badge-danger', 'obesity': 'badge-danger',
    /* generic */
    'bajo': 'badge-warning', 'low': 'badge-warning',
    'alto': 'badge-warn', 'high': 'badge-warn',
    'muy alto': 'badge-danger', 'very high': 'badge-danger',
    'óptimo': 'badge-ok', 'optimal': 'badge-ok', 'optimo': 'badge-ok',
  };

  function badgeClass(val) {
    var v = String(val).toLowerCase();
    for (var k in CATEGORY_CLASSES) {
      if (v.indexOf(k) !== -1) return CATEGORY_CLASSES[k];
    }
    return 'badge-neutral';
  }

  function makeCategoryRow(label, value) {
    var cls = badgeClass(value);
    return (
      '<div class="result-item result-category">' +
        '<span class="result-label">' + esc(label) + '</span>' +
        '<span class="result-badge ' + cls + '">' + esc(String(value)) + '</span>' +
      '</div>'
    );
  }

  function makeZoneBar(label, value) {
    var zoneNum = parseInt(label.replace(/\D/g, ''), 10) || 0;
    var colors = ['', '#6ee7b7', '#34d399', '#fbbf24', '#f97316', '#ef4444'];
    var color = colors[zoneNum] || '#94a3b8';
    return (
      '<div class="result-zone">' +
        '<span class="zone-label">' + esc(label) + '</span>' +
        '<div class="zone-bar-wrap">' +
          '<div class="zone-bar" style="background:' + color + ';width:' + (zoneNum * 18 + 10) + '%"></div>' +
        '</div>' +
        '<span class="zone-value">' + esc(String(value)) + '</span>' +
      '</div>'
    );
  }

  function makeTable(data, headers) {
    if (!Array.isArray(data) || !data.length) return '';
    var cols = headers || Object.keys(data[0]);
    var html = '<div class="result-table-wrap"><table class="result-table"><thead><tr>';
    cols.forEach(function (c) { html += '<th>' + esc(String(c)) + '</th>'; });
    html += '</tr></thead><tbody>';
    data.slice(0, 30).forEach(function (row) {
      html += '<tr>';
      cols.forEach(function (c) { html += '<td>' + esc(String(fmt(row[c]))) + '</td>'; });
      html += '</tr>';
    });
    html += '</tbody></table></div>';
    return html;
  }

  /* ── SVG Gauge Renderer ── */
  function renderGauge(value, min, max, label, unit) {
    if (!gaugeEl) return;
    if (value === null || value === undefined || isNaN(parseFloat(value))) {
      gaugeEl.innerHTML = '';
      gaugeEl.style.display = 'none';
      return;
    }
    var v = parseFloat(value);
    var pct = Math.max(0, Math.min(1, (v - min) / (max - min)));
    var angle = pct * 180;
    var rad = (angle - 90) * Math.PI / 180;
    var cx = 120, cy = 100, r = 80;
    var nx = cx + r * Math.cos(rad);
    var ny = cy + r * Math.sin(rad);

    var greenStart = 0.25, greenEnd = 0.55;
    function arcPath(startPct, endPct, color) {
      var a1 = (startPct * 180 - 180) * Math.PI / 180;
      var a2 = (endPct * 180 - 180) * Math.PI / 180;
      var x1 = cx + r * Math.cos(a1), y1 = cy + r * Math.sin(a1);
      var x2 = cx + r * Math.cos(a2), y2 = cy + r * Math.sin(a2);
      var large = (endPct - startPct) > 0.5 ? 1 : 0;
      return '<path d="M' + x1 + ',' + y1 + ' A' + r + ',' + r + ' 0 ' + large + ' 1 ' + x2 + ',' + y2 + '" fill="none" stroke="' + color + '" stroke-width="14" stroke-linecap="round"/>';
    }

    gaugeEl.style.display = '';
    gaugeEl.innerHTML =
      '<svg viewBox="0 0 240 130" class="gauge-svg">' +
        '<path d="M' + (cx - r) + ',' + cy + ' A' + r + ',' + r + ' 0 0 1 ' + (cx + r) + ',' + cy + '" fill="none" stroke="#e2e8f0" stroke-width="14" stroke-linecap="round"/>' +
        arcPath(0, greenStart, '#ef4444') +
        arcPath(greenStart, greenEnd, '#22c55e') +
        arcPath(greenEnd, 1, '#ef4444') +
        '<line x1="' + cx + '" y1="' + cy + '" x2="' + nx + '" y2="' + ny + '" stroke="' + 'var(--secondary)' + '" stroke-width="3" stroke-linecap="round" style="transition:all .5s ease"/>' +
        '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="' + 'var(--secondary)' + '"/>' +
        '<text x="' + cx + '" y="' + (cy + 30) + '" text-anchor="middle" font-size="22" font-weight="800" fill="' + 'var(--primary-dark)' + '">' + esc(fmt(value)) + '</text>' +
        (unit ? '<text x="' + cx + '" y="' + (cy + 46) + '" text-anchor="middle" font-size="11" fill="' + 'var(--text-muted)' + '">' + esc(unit) + '</text>' : '') +
        (label ? '<text x="' + cx + '" y="' + (cy - 20) + '" text-anchor="middle" font-size="11" font-weight="600" fill="' + 'var(--text-muted)' + '">' + esc(label) + '</text>' : '') +
        '<text x="' + (cx - r - 5) + '" y="' + (cy + 15) + '" text-anchor="middle" font-size="9" fill="#94a3b8">' + fmt(min) + '</text>' +
        '<text x="' + (cx + r + 5) + '" y="' + (cy + 15) + '" text-anchor="middle" font-size="9" fill="#94a3b8">' + fmt(max) + '</text>' +
      '</svg>';
  }

  function renderResults(results, wastePct) {
    if (!results || results.error) {
      resultsBox.innerHTML =
        '<div class="result-error">' + (i18n.error_invalid || 'Please enter valid values.') + '</div>';
      if (copyBtn) copyBtn.style.display = 'none';
      if (shareBtn) shareBtn.style.display = 'none';
      if (gaugeEl) gaugeEl.innerHTML = '';
      return;
    }

    var outputKeys = cfg.outputs || {};
    var keys = Object.keys(outputKeys);
    if (!keys.length) {
      resultsBox.innerHTML = '<div class="result-error">No output configuration found.</div>';
      return;
    }

    var firstVal = results[keys[0]];
    var gaugeConfig = cfg.gauge;
    if (gaugeConfig && firstVal !== undefined) {
      renderGauge(firstVal, gaugeConfig.min, gaugeConfig.max, gaugeConfig.label || '', gaugeConfig.unit || '');
    }

    var hasWaste = wastePct > 0;
    var html = '<div class="results-animate">';

    if (hasWaste) {
      html += '<div class="result-section-title">' + esc(i18n.net_label || 'Net') + '</div>';
    }

    for (var i = 0; i < keys.length; i++) {
      var key = keys[i];
      if (!(key in results)) continue;
      var label = outputKeys[key] || key;
      var val = results[key];
      if (key === 'table' && Array.isArray(val)) {
        html += makeTable(val, cfg.tableHeaders || null);
      } else if (key === 'categoria' || key === 'category' || key === 'categoria_imc' || key === 'categorie') {
        html += makeCategoryRow(label, val);
      } else if (/^zona\d?$/.test(key) || /^zone\d?$/.test(key) || /^z\d$/.test(key)) {
        html += makeZoneBar(label, val);
      } else {
        html += makeRow(label, val, hasWaste ? 'result-item--net' : '');
      }
    }

    if (hasWaste) {
      html += '<div class="result-section-title" style="margin-top:.75rem;">' +
        esc((i18n.total_label || 'Total to buy (+{pct}%)').replace('{pct}', wastePct)) +
      '</div>';
      for (var j = 0; j < keys.length; j++) {
        var k = keys[j];
        if (!(k in results)) continue;
        if (k === 'table' || k === 'categoria' || k === 'category') continue;
        var num = parseFloat(results[k]);
        var totalVal = !isNaN(num) ? +(num * (1 + wastePct / 100)).toFixed(3) : results[k];
        html += makeRow(outputKeys[k] || k, totalVal, 'result-item--total');
      }
    }

    /* Buying units sub-rows */
    if (cfg.buying_units) {
      html += renderBuyingUnits(results, cfg.buying_units, i18n.buying_unit_prefix);
    }

    /* Cost estimation row */
    var prices = collectPriceInputs();
    if (Object.keys(prices).length) {
      html += renderCostRow(results, prices, i18n.cost_estimate_label);
    }

    html += '</div>';
    resultsBox.innerHTML = html;
    if (copyBtn) copyBtn.style.display = '';
    if (shareBtn) shareBtn.style.display = '';
    if (socialShare) showSocialShare();

    resultsBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function encodeToHash(inputs) {
    try {
      var filtered = {};
      Object.keys(inputs).forEach(function (k) {
        if (inputs[k] !== '' && k !== 'desperdicio_merma') filtered[k] = inputs[k];
      });
      history.replaceState(null, '', '#' + btoa(JSON.stringify(filtered)));
    } catch (e) {}
  }

  function decodeFromHash() {
    try {
      var hash = window.location.hash;
      if (!hash || hash.length < 4) return false;
      var decoded = JSON.parse(atob(hash.slice(1)));
      Object.keys(decoded).forEach(function (k) {
        var el = form.querySelector('[name="' + k + '"]');
        if (el) el.value = decoded[k];
      });
      return true;
    } catch (e) { return false; }
  }

  function trackEvent(action, category, label, value) {
    try {
      if (typeof gtag === 'function') {
        gtag('event', action, { event_category: category, event_label: label, value: value || undefined });
      }
    } catch (e) {}
  }

  function trackAdView(slotName) {
    try {
      if (typeof gtag === 'function') {
        gtag('event', 'ad_viewed', { event_category: 'ads', event_label: slotName });
      }
    } catch (e) {}
  }

  function trackAffiliateClick(program) {
    try {
      if (typeof gtag === 'function') {
        gtag('event', 'aff_click', { event_category: 'affiliate', event_label: program });
      }
    } catch (e) {}
  }

  /* ── Scroll depth tracking (25%, 50%, 75%, 100%) ── */
  (function initScrollTracking() {
    var depths = [25, 50, 75, 100];
    var tracked = {};
    var ticking = false;

    function getScrollDepth() {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      if (docHeight <= 0) return 0;
      return Math.round((scrollTop / docHeight) * 100);
    }

    function check() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var d = getScrollDepth();
        depths.forEach(function (threshold) {
          if (d >= threshold && !tracked[threshold]) {
            tracked[threshold] = true;
            try {
              if (typeof gtag === 'function') gtag('event', 'scroll_depth', { event_category: 'engagement', event_label: threshold + '%' });
            } catch (e) {}
          }
        });
        ticking = false;
      });
    }

    window.addEventListener('scroll', check, { passive: true });
    check();
  })();

  /* ── Ad viewability tracking (IntersectionObserver on ad slots) ── */
  (function initAdTracking() {
    var adSlots = document.querySelectorAll('.ad-slot');
    if (!adSlots.length) return;
    var observed = {};
    if ('IntersectionObserver' in window) {
      var adObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
            var el = entry.target;
            var slotName = el.classList.contains('ad-slot-banner') ? 'banner' :
                           el.classList.contains('ad-slot-inarticle') ? 'inarticle' :
                           el.classList.contains('ad-slot-responsive') ? 'responsive' : 'unknown';
            var key = el.className + (el.getAttribute('data-ad-slot') || '');
            if (!observed[key]) {
              observed[key] = true;
              trackAdView(slotName);
            }
          }
        });
      }, { threshold: 0.5 });

      adSlots.forEach(function (slot) { adObserver.observe(slot); });
    }
  })();

  /* ── Affiliate click tracking ── */
  (function initAffiliateTracking() {
    document.addEventListener('click', function (e) {
      var target = e.target.closest('[data-affiliate]');
      if (target) {
        trackAffiliateClick(target.getAttribute('data-affiliate'));
      }
    });
  })();

  /* ── Ad refresh on calculation (with 30s cooldown) ── */
  var lastAdRefresh = 0;
  function refreshAds() {
    var now = Date.now();
    if (now - lastAdRefresh < 30000) return;
    lastAdRefresh = now;
    try {
      if (window.adsbygoogle && window.__adsense_allowed !== false) {
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      }
    } catch (e) {}
  }

  /* ── Price estimation (cost rows) ── */
  function collectPriceInputs() {
    var prices = {};
    var fields = document.querySelectorAll('[data-price-for]');
    fields.forEach(function (el) {
      var key = el.getAttribute('data-price-for');
      var v = parseFloat(el.value);
      if (!isNaN(v) && v > 0) prices[key] = v;
    });
    return prices;
  }

  function renderCostRow(results, prices, label) {
    var total = 0;
    var hasAny = false;
    Object.keys(prices).forEach(function (key) {
      var qty = parseFloat(results[key]);
      if (!isNaN(qty)) {
        total += qty * prices[key];
        hasAny = true;
      }
    });
    if (!hasAny) return '';
    return '<div class="result-item result-cost">' +
      '<span class="result-label">' + esc(label || 'Estimated Cost') + '</span>' +
      '<span class="result-value result-cost-value">' + total.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + '</span>' +
    '</div>';
  }

  /* ── Buying units sub-rows ── */
  function renderBuyingUnits(results, buyingUnits, prefix) {
    if (!buyingUnits || !Object.keys(buyingUnits).length) return '';
    var html = '';
    Object.keys(buyingUnits).forEach(function (outputKey) {
      var val = parseFloat(results[outputKey]);
      if (isNaN(val)) return;
      var units = buyingUnits[outputKey];
      units.forEach(function (bu) {
        var qty = bu.round === 'ceil' ? Math.ceil(val * bu.factor) : +(val * bu.factor).toFixed(1);
        html += '<div class="result-item result-buying-unit">' +
          '<span class="result-label">' + esc((prefix || '→') + ' ' + bu.label) + '</span>' +
          '<span class="result-value">~' + qty + ' ' + esc(bu.unit_suffix || '') + '</span>' +
        '</div>';
      });
    });
    return html;
  }

  function calculate() {
    var inputs  = collectInputs();
    var wastePct = parseFloat(inputs.desperdicio_merma) || 0;
    var results;
    try {
      results = calcFn(inputs);
    } catch (e) {
      console.error('[CalcToWork] Runtime error:', e);
      results = { error: true };
    }
    window._lastResults = results;
    renderResults(results, wastePct);
    encodeToHash(inputs);
    trackEvent('calculate', 'calculator', cfg.slug || window.location.pathname);
    refreshAds();
    if (pdfBtn) pdfBtn.style.display = '';
    if (addProjectBtn) addProjectBtn.style.display = '';
  }

  var debounceTimer = null;
  function onInputChange() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      if (allFilled()) calculate();
    }, 300);
  }

  form.addEventListener('submit', function (e) { e.preventDefault(); calculate(); });
  form.addEventListener('input', onInputChange);

  /* ── Unit select changes trigger recalculation ── */
  form.querySelectorAll('.unit-select').forEach(function (sel) {
    sel.addEventListener('change', function () {
      if (allFilled()) calculate();
    });
  });

  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      form.reset();
      resultsBox.innerHTML =
        '<div class="result-placeholder">' + (i18n.result_placeholder || i18n.label_results || 'Results') + '</div>';
      if (copyBtn)  copyBtn.style.display  = 'none';
      if (shareBtn) shareBtn.style.display = 'none';
      if (gaugeEl) gaugeEl.innerHTML = '';
      if (socialShare) hideSocialShare();
      history.replaceState(null, '', window.location.pathname);
    });
  }

  if (copyBtn) {
    copyBtn.style.display = 'none';
    copyBtn.addEventListener('click', function () {
      var items = resultsBox.querySelectorAll('.result-item');
      var lines = [];
      for (var i = 0; i < items.length; i++) {
        var lEl = items[i].querySelector('.result-label');
        var vEl = items[i].querySelector('.result-value');
        if (lEl && vEl) lines.push(lEl.textContent.trim() + ': ' + vEl.textContent.trim());
      }
      if (!lines.length) return;
      var text = lines.join('\n');
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function() { flashCopied(); trackEvent('copy_results', 'calculator', cfg.slug || window.location.pathname); });
      } else {
        var ta = document.createElement('textarea');
        ta.value = text; ta.style.cssText = 'position:fixed;opacity:0';
        document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); } catch (ex) {}
        document.body.removeChild(ta);
        flashCopied();
      }
    });
  }

  if (shareBtn) {
    shareBtn.style.display = 'none';
    shareBtn.addEventListener('click', function () {
      var inputs = collectInputs();
      encodeToHash(inputs);
      var url = window.location.href;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function() { flashShared(); trackEvent('share_link', 'calculator', cfg.slug || window.location.pathname); });
      } else {
        var ta = document.createElement('textarea');
        ta.value = url; ta.style.cssText = 'position:fixed;opacity:0';
        document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); } catch (ex) {}
        document.body.removeChild(ta);
        flashShared();
      }
    });
  }

  /* Social share buttons */
  var socialShare = document.getElementById('social-share');
  var btnWhatsapp = document.getElementById('btn-whatsapp');
  var btnTwitter = document.getElementById('btn-twitter');
  var btnFacebook = document.getElementById('btn-facebook');

  function showSocialShare() {
    if (socialShare) socialShare.style.display = '';
  }
  function hideSocialShare() {
    if (socialShare) socialShare.style.display = 'none';
  }

  function getShareUrl() {
    var inputs = collectInputs();
    encodeToHash(inputs);
    return window.location.href;
  }

  function getShareText() {
    var title = i18n.seo_title || document.title;
    return title + ' – CalcToWork';
  }

  if (btnWhatsapp) {
    btnWhatsapp.addEventListener('click', function (e) {
      e.preventDefault();
      var url = encodeURIComponent(getShareUrl());
      var text = encodeURIComponent(getShareText());
      window.open('https://wa.me/?text=' + text + '%20' + url, '_blank');
      trackEvent('share_whatsapp', 'calculator', cfg.slug || window.location.pathname);
    });
  }
  if (btnTwitter) {
    btnTwitter.addEventListener('click', function (e) {
      e.preventDefault();
      var url = encodeURIComponent(getShareUrl());
      var text = encodeURIComponent(getShareText());
      window.open('https://twitter.com/intent/tweet?text=' + text + '&url=' + url, '_blank');
      trackEvent('share_twitter', 'calculator', cfg.slug || window.location.pathname);
    });
  }
  if (btnFacebook) {
    btnFacebook.addEventListener('click', function (e) {
      e.preventDefault();
      var url = encodeURIComponent(getShareUrl());
      window.open('https://www.facebook.com/sharer/sharer.php?u=' + url, '_blank');
      trackEvent('share_facebook', 'calculator', cfg.slug || window.location.pathname);
    });
  }

  function flashCopied() {
    if (!copyBtn) return;
    var orig = copyBtn.textContent;
    copyBtn.textContent = '\u2713 ' + (i18n.copied || 'Copied!');
    copyBtn.classList.add('copied');
    setTimeout(function () { copyBtn.textContent = orig; copyBtn.classList.remove('copied'); }, 1800);
  }

  function flashShared() {
    if (!shareBtn) return;
    var orig = shareBtn.textContent;
    shareBtn.textContent = '\u2713 ' + (i18n.link_copied || 'Link copied!');
    shareBtn.classList.add('copied');
    setTimeout(function () { shareBtn.textContent = orig; shareBtn.classList.remove('copied'); }, 2000);
  }

  /* ── Sticky calculator (desktop) ── */
  var stickyCard = document.querySelector('.results-panel');
  var stickySentinel = document.querySelector('.sticky-sentinel');
  if (stickyCard && stickySentinel && window.matchMedia('(min-width: 1024px)').matches) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) {
          stickyCard.classList.add('is-sticky');
        } else {
          stickyCard.classList.remove('is-sticky');
        }
      });
    }, { rootMargin: '-70px 0px 0px 0px' });
    observer.observe(stickySentinel);
  }

  /* ── Table of Contents (smooth scroll + active state) ── */
  if (tocLinks.length) {
    tocLinks.forEach(function (link) {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        var target = document.getElementById(this.getAttribute('href').slice(1));
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        tocLinks.forEach(function (l) { l.classList.remove('active'); });
        this.classList.add('active');
      });
    });
  }

  /* ── Feedback widget ── */
  if (feedbackBtns.length) {
    feedbackBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var wrap = this.closest('.feedback-wrap');
        if (wrap) wrap.innerHTML = '<span class="feedback-thanks">' + (i18n.feedback_thanks || 'Thanks!') + '</span>';
        try {
          var key = 'ctw_fb_' + window.location.pathname;
          localStorage.setItem(key, this.dataset.val);
        } catch (e) {}
      });
    });
  }

  /* ── Init ── */
  (function init() {
    if (window.CALC_PREFILL) {
      Object.keys(window.CALC_PREFILL).forEach(function (k) {
        var el = form.querySelector('[name="' + k + '"]');
        if (el) el.value = window.CALC_PREFILL[k];
      });
      calculate();
      return;
    }
    var restored = decodeFromHash();
    if (restored || allFilled()) calculate();
  })();

}());

/* ── Comparison Table: click row to prefill calculator ── */
(function initComparisonTable() {
  var table = document.getElementById('comparison-table');
  if (!table) return;
  var form2 = document.getElementById('calc-form');
  if (!form2) return;
  table.querySelectorAll('tbody tr[data-prefill]').forEach(function (row) {
    row.style.cursor = 'pointer';
    row.addEventListener('click', function () {
      try {
        var vals = JSON.parse(this.getAttribute('data-prefill'));
        Object.keys(vals).forEach(function (k) {
          var el = form2.querySelector('[name="' + k + '"]');
          if (el) el.value = vals[k];
        });
        table.querySelectorAll('tbody tr').forEach(function (r) { r.classList.remove('comparison-active'); });
        row.classList.add('comparison-active');
        window.scrollTo({ top: form2.getBoundingClientRect().top + window.scrollY - 80, behavior: 'smooth' });
        form2.dispatchEvent(new Event('input', { bubbles: true }));
      } catch (e) {}
    });
  });
}());

/* ── PDF Export ── */
(function initPDF() {
  var btn = document.getElementById('btn-pdf');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var cfg2 = window.CALC_CONFIG || {};
    var i18n2 = cfg2.i18n || {};
    function buildAndSave(jsPDF) {
      var doc = new jsPDF({ unit: 'mm', format: 'a4' });
      var pageW = doc.internal.pageSize.getWidth();
      var margin = 15;
      var y = 20;

      /* Header */
      doc.setFontSize(18);
      doc.setFont(undefined, 'bold');
      doc.text(i18n2.calc_name || i18n2.seo_title || 'CalcToWork', margin, y);
      y += 8;
      doc.setFontSize(10);
      doc.setFont(undefined, 'normal');
      doc.setTextColor(120);
      doc.text('calcto.work  –  ' + new Date().toLocaleDateString(), margin, y);
      y += 8;
      doc.setDrawColor(200);
      doc.line(margin, y, pageW - margin, y);
      y += 8;

      /* Inputs */
      doc.setTextColor(0);
      doc.setFontSize(13);
      doc.setFont(undefined, 'bold');
      doc.text('Inputs', margin, y);
      y += 6;
      doc.setFontSize(10);
      doc.setFont(undefined, 'normal');
      var form2 = document.getElementById('calc-form');
      if (form2) {
        var fields = form2.querySelectorAll('input[name]');
        fields.forEach(function (f) {
          if (!f.value) return;
          var label = form2.querySelector('label[for="input-' + f.name + '"]');
          var labelText = label ? label.textContent.trim() : f.name;
          var unitSel = form2.querySelector('.unit-select[data-input="' + f.name + '"]');
          var unitText = unitSel ? ' ' + unitSel.options[unitSel.selectedIndex].value : '';
          doc.text(labelText + ': ' + f.value + unitText, margin + 4, y);
          y += 6;
          if (y > 270) { doc.addPage(); y = 20; }
        });
      }
      y += 4;
      doc.line(margin, y, pageW - margin, y);
      y += 8;

      /* Results */
      doc.setFontSize(13);
      doc.setFont(undefined, 'bold');
      doc.text('Results', margin, y);
      y += 6;
      doc.setFontSize(10);
      doc.setFont(undefined, 'normal');
      var resultsBox2 = document.getElementById('calc-results');
      if (resultsBox2) {
        var items = resultsBox2.querySelectorAll('.result-item');
        items.forEach(function (item) {
          var lEl = item.querySelector('.result-label');
          var vEl = item.querySelector('.result-value');
          if (lEl && vEl) {
            var line = lEl.textContent.trim() + ': ' + vEl.textContent.trim();
            doc.text(line, margin + 4, y);
            y += 6;
            if (y > 270) { doc.addPage(); y = 20; }
          }
        });
      }

      /* Footer */
      y += 6;
      doc.setFontSize(8);
      doc.setTextColor(150);
      doc.text('Generated by CalcToWork (calcto.work) – results are estimates only.', margin, y);

      var slug = cfg2.slug || 'result';
      doc.save(slug.replace(/\//g, '-') + '.pdf');
    }

    if (window.jspdf && window.jspdf.jsPDF) {
      buildAndSave(window.jspdf.jsPDF);
    } else {
      var s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js';
      s.onload = function () { buildAndSave(window.jspdf.jsPDF); };
      document.head.appendChild(s);
    }
  });
}());

/* ── Project Tally ── */
(function initProjectTally() {
  var STORAGE_KEY = 'ctw_project_v1';
  var fab = document.getElementById('btn-project-fab');
  var panel = document.getElementById('project-tally');
  var itemsEl = document.getElementById('project-tally-items');
  var addBtn = document.getElementById('btn-add-project');
  var closeBtn = document.getElementById('btn-tally-close');
  var exportBtn = document.getElementById('btn-tally-pdf');
  var clearBtn = document.getElementById('btn-tally-clear');
  var fabCount = document.getElementById('project-fab-count');
  if (!fab || !panel) return;

  var cfg2 = window.CALC_CONFIG || {};
  var i18n2 = cfg2.i18n || {};

  function loadItems() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'); } catch (e) { return []; }
  }
  function saveItems(items) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(items)); } catch (e) {}
  }

  function updateFab() {
    var items = loadItems();
    var count = items.length;
    if (fabCount) fabCount.textContent = count;
    if (count > 0) {
      fab.style.display = '';
    }
  }

  function renderItems() {
    var items = loadItems();
    if (!itemsEl) return;
    if (!items.length) {
      itemsEl.innerHTML = '<div class="tally-empty">No items yet. Calculate something and click "+ Project".</div>';
      return;
    }
    var html = '';
    items.forEach(function (item, idx) {
      html += '<div class="tally-item">';
      html += '<div class="tally-item-name">' + item.name + '</div>';
      html += '<div class="tally-item-results">' + item.resultsText + '</div>';
      html += '<button class="tally-remove" data-idx="' + idx + '" aria-label="Remove">&#10005;</button>';
      html += '</div>';
    });
    itemsEl.innerHTML = html;
    itemsEl.querySelectorAll('.tally-remove').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var items2 = loadItems();
        items2.splice(parseInt(this.getAttribute('data-idx'), 10), 1);
        saveItems(items2);
        renderItems();
        updateFab();
      });
    });
  }

  if (addBtn) {
    addBtn.addEventListener('click', function () {
      var resultsBox2 = document.getElementById('calc-results');
      if (!resultsBox2) return;
      var items2 = resultsBox2.querySelectorAll('.result-item');
      var lines = [];
      items2.forEach(function (item) {
        var lEl = item.querySelector('.result-label');
        var vEl = item.querySelector('.result-value');
        if (lEl && vEl) lines.push(lEl.textContent.trim() + ': ' + vEl.textContent.trim());
      });
      if (!lines.length) return;
      var entry = {
        name: i18n2.calc_name || document.title,
        resultsText: lines.join(' | '),
        url: window.location.pathname,
        ts: Date.now()
      };
      var items3 = loadItems();
      items3.push(entry);
      saveItems(items3);
      updateFab();
      addBtn.textContent = '✓';
      setTimeout(function () { addBtn.textContent = '+ ' + (i18n2.btn_add_project || 'Project'); }, 1500);
    });
  }

  if (fab) {
    fab.addEventListener('click', function () {
      panel.style.display = '';
      renderItems();
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', function () {
      panel.style.display = 'none';
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      saveItems([]);
      renderItems();
      updateFab();
      fab.style.display = 'none';
    });
  }

  if (exportBtn) {
    exportBtn.addEventListener('click', function () {
      function buildTallyPDF(jsPDF) {
        var doc = new jsPDF({ unit: 'mm', format: 'a4' });
        var margin = 15;
        var y = 20;
        doc.setFontSize(16);
        doc.setFont(undefined, 'bold');
        doc.text(i18n2.project_tally_title || 'My Project', margin, y);
        y += 8;
        doc.setFontSize(9);
        doc.setFont(undefined, 'normal');
        doc.setTextColor(120);
        doc.text('calcto.work  –  ' + new Date().toLocaleDateString(), margin, y);
        y += 8;
        doc.setDrawColor(200);
        doc.line(margin, y, doc.internal.pageSize.getWidth() - margin, y);
        y += 8;
        doc.setTextColor(0);
        var items = loadItems();
        items.forEach(function (item) {
          doc.setFontSize(11);
          doc.setFont(undefined, 'bold');
          doc.text(item.name, margin, y);
          y += 6;
          doc.setFontSize(9);
          doc.setFont(undefined, 'normal');
          item.resultsText.split(' | ').forEach(function (line) {
            doc.text(line, margin + 4, y);
            y += 5;
            if (y > 270) { doc.addPage(); y = 20; }
          });
          y += 4;
        });
        doc.save('my-project.pdf');
      }
      if (window.jspdf && window.jspdf.jsPDF) {
        buildTallyPDF(window.jspdf.jsPDF);
      } else {
        var s = document.createElement('script');
        s.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js';
        s.onload = function () { buildTallyPDF(window.jspdf.jsPDF); };
        document.head.appendChild(s);
      }
    });
  }

  /* Price inputs trigger recalculation */
  document.querySelectorAll('[data-price-for]').forEach(function (el) {
    el.addEventListener('input', function () {
      if (window._lastResults) {
        var cfg3 = window.CALC_CONFIG || {};
        var wastePct = parseFloat((document.getElementById('input-desperdicio_merma') || {}).value) || 0;
        /* Re-trigger renderResults via the main IIFE's calculate wrapper */
        var form3 = document.getElementById('calc-form');
        if (form3) form3.dispatchEvent(new Event('submit'));
      }
    });
  });

  updateFab();
}());

/* ── FAQ accordion (accessible) ── */
document.querySelectorAll('.faq-q').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var item = btn.closest('.faq-item');
    var answer = item.querySelector('.faq-a');
    var isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(function (el) {
      el.classList.remove('open');
      el.querySelector('.faq-a').style.maxHeight = null;
      el.querySelector('.faq-a').style.opacity = null;
    });
    if (!isOpen) {
      item.classList.add('open');
      answer.style.maxHeight = answer.scrollHeight + 'px';
      answer.style.opacity = '1';
    }
    btn.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
  });
});

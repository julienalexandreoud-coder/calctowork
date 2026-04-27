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

    html += '</div>';
    resultsBox.innerHTML = html;
    if (copyBtn) copyBtn.style.display = '';
    if (shareBtn) shareBtn.style.display = '';

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
    renderResults(results, wastePct);
    encodeToHash(inputs);
    trackEvent('calculate', 'calculator', cfg.slug || window.location.pathname);
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

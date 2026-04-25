/* CalcToWork – Calculator Engine v5.0 */
(function () {
  'use strict';

  var cfg    = window.CALC_CONFIG || {};
  var i18n   = cfg.i18n || {};
  var form   = document.getElementById('calc-form');
  var resultsBox = document.getElementById('calc-results');
  var resetBtn   = document.getElementById('btn-reset');
  var copyBtn    = document.getElementById('btn-copy');
  var shareBtn   = document.getElementById('btn-share');

  if (!form || !resultsBox) return;

  /* ── Compile formula ── */
  var calcFn;
  try {
    calcFn = new Function('inputs', cfg.formula || 'return{error:true};');
  } catch (e) {
    console.error('[CalcToWork] Formula compile error:', e);
    calcFn = function () { return { error: true }; };
  }

  /* ── Collect input values ── */
  function collectInputs() {
    var inputs = {};
    var fields = form.querySelectorAll('input[name]');
    for (var i = 0; i < fields.length; i++) {
      inputs[fields[i].name] = fields[i].value;
    }
    return inputs;
  }

  /* ── Check all required inputs are filled ── */
  function allFilled() {
    var fields = form.querySelectorAll('input[name]:not([name="desperdicio_merma"])');
    for (var i = 0; i < fields.length; i++) {
      var v = fields[i].value.trim();
      if (v === '' || isNaN(parseFloat(v))) return false;
    }
    return fields.length > 0;
  }

  /* ── Format number ── */
  function fmt(val) {
    if (val === null || val === undefined || val === '') return '—';
    var n = parseFloat(val);
    if (isNaN(n)) return String(val);
    return n.toLocaleString(undefined, { maximumFractionDigits: 3 });
  }

  /* ── HTML escape ── */
  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  /* ── Build a single result row ── */
  function makeRow(label, value, extraClass) {
    return (
      '<div class="result-item' + (extraClass ? ' ' + extraClass : '') + '">' +
        '<span class="result-label">' + esc(label) + '</span>' +
        '<span class="result-value">' + esc(String(fmt(value))) + '</span>' +
      '</div>'
    );
  }

  /* ── Render results ── */
  function renderResults(results, wastePct) {
    if (!results || results.error) {
      resultsBox.innerHTML =
        '<div class="result-error">' + (i18n.error_invalid || 'Please enter valid values.') + '</div>';
      if (copyBtn) copyBtn.style.display = 'none';
      if (shareBtn) shareBtn.style.display = 'none';
      return;
    }

    var outputKeys = cfg.outputs || {};
    var keys = Object.keys(outputKeys);
    if (!keys.length) {
      resultsBox.innerHTML = '<div class="result-error">No output configuration found.</div>';
      return;
    }

    var hasWaste = wastePct > 0;
    var html = '<div class="results-animate">';

    if (hasWaste) {
      html += '<div class="result-section-title">' + esc(i18n.net_label || 'Net') + '</div>';
    }

    for (var i = 0; i < keys.length; i++) {
      var key = keys[i];
      if (!(key in results)) continue;
      html += makeRow(outputKeys[key] || key, results[key], hasWaste ? 'result-item--net' : '');
    }

    if (hasWaste) {
      html += '<div class="result-section-title" style="margin-top:.75rem;">' +
        esc((i18n.total_label || 'Total to buy (+{pct}%)').replace('{pct}', wastePct)) +
      '</div>';
      for (var j = 0; j < keys.length; j++) {
        var k = keys[j];
        if (!(k in results)) continue;
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

  /* ── URL hash encode / decode ── */
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

  /* ── Calculate ── */
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
  }

  /* ── Debounced auto-calculate ── */
  var debounceTimer = null;
  function onInputChange() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      if (allFilled()) calculate();
    }, 400);
  }

  /* ── Events ── */
  form.addEventListener('submit', function (e) { e.preventDefault(); calculate(); });
  form.addEventListener('input', onInputChange);

  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      form.reset();
      resultsBox.innerHTML =
        '<div class="result-placeholder">' + (i18n.result_placeholder || i18n.label_results || 'Results') + '</div>';
      if (copyBtn)  copyBtn.style.display  = 'none';
      if (shareBtn) shareBtn.style.display = 'none';
      history.replaceState(null, '', window.location.pathname);
    });
  }

  /* ── Copy results ── */
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
        navigator.clipboard.writeText(text).then(flashCopied);
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

  /* ── Share calculation (copy URL with pre-filled values) ── */
  if (shareBtn) {
    shareBtn.style.display = 'none';
    shareBtn.addEventListener('click', function () {
      var inputs = collectInputs();
      encodeToHash(inputs);
      var url = window.location.href;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(flashShared);
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

  /* ── On load: parametric prefill -> hash restore -> auto-calc ── */
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

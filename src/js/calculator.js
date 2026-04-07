/* ObraCalc – Calculator Engine v2.0 */
(function () {
  'use strict';

  var cfg = window.CALC_CONFIG || {};
  var i18n = cfg.i18n || {};

  var form = document.getElementById('calc-form');
  var resultsBox = document.getElementById('calc-results');
  var resetBtn = document.getElementById('btn-reset');
  var copyBtn = document.getElementById('btn-copy');

  if (!form || !resultsBox) return;

  /* ── Compile formula ── */
  var calcFn;
  try {
    calcFn = new Function('inputs', cfg.formula || 'return{error:true};');
  } catch (e) {
    console.error('[ObraCalc] Formula compile error:', e);
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
      return;
    }

    var outputKeys = cfg.outputs || {};
    var keys = Object.keys(outputKeys);
    if (!keys.length) {
      resultsBox.innerHTML = '<div class="result-error">No output configuration found.</div>';
      return;
    }

    var hasWaste = wastePct > 0;
    var html = '';

    if (hasWaste) {
      html += '<div class="result-section-title">' + esc(i18n.net_label || 'Net') + '</div>';
    }

    for (var i = 0; i < keys.length; i++) {
      var key = keys[i];
      if (!(key in results)) continue;
      var label = outputKeys[key] || key;
      var value = results[key];
      html += makeRow(label, value, hasWaste ? 'result-item--net' : '');
    }

    if (hasWaste) {
      html += '<div class="result-section-title" style="margin-top:.75rem;">' +
        esc((i18n.total_label || 'Total to buy (+{pct}%)').replace('{pct}', wastePct)) +
      '</div>';

      for (var j = 0; j < keys.length; j++) {
        var k = keys[j];
        if (!(k in results)) continue;
        var rawVal = results[k];
        var num = parseFloat(rawVal);
        var totalVal = !isNaN(num) ? +(num * (1 + wastePct / 100)).toFixed(3) : rawVal;
        html += makeRow(outputKeys[k] || k, totalVal, 'result-item--total');
      }
    }

    resultsBox.innerHTML = html;
    if (copyBtn) copyBtn.style.display = '';
  }

  /* ── Calculate ── */
  function calculate() {
    var inputs = collectInputs();
    var wastePct = parseFloat(inputs.desperdicio_merma) || 0;

    // Pass all inputs to formula (formula ignores unknown keys)
    var results;
    try {
      results = calcFn(inputs);
    } catch (e) {
      console.error('[ObraCalc] Runtime error:', e);
      results = { error: true };
    }
    renderResults(results, wastePct);

    if (window.innerWidth < 768) {
      resultsBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  /* ── Events ── */
  form.addEventListener('submit', function (e) { e.preventDefault(); calculate(); });
  form.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); calculate(); } });

  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      form.reset();
      resultsBox.innerHTML =
        '<div class="result-placeholder">' + (i18n.label_results || 'Results') + '</div>';
      if (copyBtn) copyBtn.style.display = 'none';
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

  function flashCopied() {
    if (!copyBtn) return;
    var orig = copyBtn.textContent;
    copyBtn.textContent = '✓ ' + (i18n.copied || 'Copied!');
    copyBtn.classList.add('copied');
    setTimeout(function () { copyBtn.textContent = orig; copyBtn.classList.remove('copied'); }, 1800);
  }

  /* ── Auto-calculate on page load if inputs pre-filled ── */
  (function autoCalc() {
    var fields = form.querySelectorAll('input[name]:not([name="desperdicio_merma"])');
    var allFilled = fields.length > 0;
    for (var i = 0; i < fields.length; i++) {
      if (!fields[i].value) { allFilled = false; break; }
    }
    if (allFilled) calculate();
  })();

}());

/* ── FAQ accordion (outside calculator IIFE so it always runs) ── */
document.querySelectorAll('.faq-q').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var item = btn.closest('.faq-item');
    var isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(function (el) { el.classList.remove('open'); });
    if (!isOpen) item.classList.add('open');
    btn.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
  });
});

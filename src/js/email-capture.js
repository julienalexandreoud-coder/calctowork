/* CalcToWork - Email capture + real PDF generation */
(function () {
  'use strict';

  var form = document.getElementById('email-capture-form');
  var box = document.getElementById('email-capture-box');
  if (!form || !box) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var email = form.querySelector('input[name="email"]').value.trim();
    if (!email || email.indexOf('@') < 1) return;

    var btn = form.querySelector('button');
    var origText = btn.textContent;
    btn.disabled = true;
    btn.textContent = 'Generating PDF…';

    function onReady() {
      generateAndDownloadPDF(email);
      btn.textContent = origText;
      btn.disabled = false;
      box.innerHTML = '<div class="email-capture-thanks">&#128196; Your PDF has been downloaded. Thanks!</div>';
      trackLead(email);
    }

    if (window.jspdf && window.jspdf.jsPDF) {
      onReady();
    } else {
      var s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js';
      s.onload = onReady;
      s.onerror = function () {
        btn.textContent = origText;
        btn.disabled = false;
        alert('PDF generator could not be loaded. Please try again.');
      };
      document.head.appendChild(s);
    }
  });

  function generateAndDownloadPDF(email) {
    var cfg = window.CALC_CONFIG || {};
    var i18n = cfg.i18n || {};
    var calcName = i18n.calc_name || document.title;
    var resultsBox = document.getElementById('calc-results');
    var lines = [];

    if (resultsBox) {
      resultsBox.querySelectorAll('.result-item').forEach(function (item) {
        var lEl = item.querySelector('.result-label');
        var vEl = item.querySelector('.result-value');
        if (lEl && vEl) lines.push(lEl.textContent.trim() + ': ' + vEl.textContent.trim());
      });
    }

    var doc = new window.jspdf.jsPDF({ unit: 'mm', format: 'a4' });
    var margin = 15;
    var y = 20;

    doc.setFontSize(18);
    doc.setFont(undefined, 'bold');
    doc.setTextColor(249, 115, 22);
    doc.text('CalcToWork', margin, y);
    y += 10;

    doc.setFontSize(14);
    doc.setTextColor(30, 41, 59);
    doc.text(calcName, margin, y);
    y += 8;

    doc.setFontSize(9);
    doc.setFont(undefined, 'normal');
    doc.setTextColor(120);
    doc.text('Generated: ' + new Date().toLocaleString() + '  |  calcto.work', margin, y);
    y += 6;
    doc.text('Email: ' + email, margin, y);
    y += 8;

    doc.setDrawColor(200);
    doc.line(margin, y, doc.internal.pageSize.getWidth() - margin, y);
    y += 8;

    doc.setTextColor(30, 41, 59);
    if (lines.length) {
      lines.forEach(function (line) {
        doc.setFontSize(11);
        doc.text(line, margin, y);
        y += 7;
        if (y > 270) { doc.addPage(); y = 20; }
      });
    } else {
      doc.setFontSize(11);
      doc.text('No calculation results available.', margin, y);
    }

    y += 10;
    doc.setFontSize(8);
    doc.setTextColor(150);
    doc.text('Results are approximate estimates. Always consult a professional.', margin, y);

    var safeName = calcName.replace(/[^a-z0-9]/gi, '_').toLowerCase().substring(0, 30);
    doc.save('calctowork_' + safeName + '.pdf');
  }

  function trackLead(email) {
    try {
      if (typeof gtag === 'function') {
        gtag('event', 'email_capture', {
          event_category: 'lead',
          event_label: window.CALC_CONFIG ? (window.CALC_CONFIG.slug || '') : window.location.pathname
        });
      }
      if (window.CTWAnalytics && typeof window.CTWAnalytics.track === 'function') {
        window.CTWAnalytics.track('lead_captured', {
          calc_slug: window.CALC_CONFIG ? (window.CALC_CONFIG.slug || '') : window.location.pathname,
          email_domain: email.split('@')[1]
        });
      }
    } catch (e) {}

    // Send to webhook if configured
    var webhookUrl = box.getAttribute('data-webhook');
    if (webhookUrl) {
      fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: email,
          page: window.location.href,
          calc_name: (window.CALC_CONFIG && window.CALC_CONFIG.i18n) ? window.CALC_CONFIG.i18n.calc_name : document.title,
          timestamp: new Date().toISOString()
        })
      }).catch(function () {});
    }
  }
})();

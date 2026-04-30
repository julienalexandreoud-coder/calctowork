/* CalcToWork - Email capture for PDF report download */
(function () {
  'use strict';

  var form = document.getElementById('email-capture-form');
  if (!form) return;

  var box = document.getElementById('email-capture-box');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var email = form.querySelector('input[name="email"]').value.trim();
    if (!email || email.indexOf('@') < 1) return;

    var btn = form.querySelector('button');
    var origText = btn.textContent;
    btn.disabled = true;
    btn.textContent = 'Sending\u2026';

    var webhookUrl = document.getElementById('email-capture-box').getAttribute('data-webhook');

    if (webhookUrl) {
      fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email, page: window.location.href, timestamp: new Date().toISOString() })
      })
        .then(function () { showThanks(origText, btn); })
        .catch(function () { showThanks(origText, btn); });
    } else {
      setTimeout(function () { showThanks(origText, btn); }, 600);
    }

    try {
      if (typeof gtag === 'function') gtag('event', 'email_capture', { event_category: 'lead', event_label: window.CALC_CONFIG ? (window.CALC_CONFIG.slug || '') : window.location.pathname });
    } catch (e) {}
  });

  function showThanks(origText, btn) {
    box.innerHTML = '<div class="email-capture-thanks">\u2709 Check your inbox! We\u2019ve sent your PDF report.</div>';
    try {
      if (typeof gtag === 'function') gtag('event', 'email_confirmed', { event_category: 'lead', event_label: window.CALC_CONFIG ? (window.CALC_CONFIG.slug || '') : window.location.pathname });
    } catch (e) {}
  }
})();

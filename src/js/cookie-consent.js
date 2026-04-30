/* CalcToWork - Cookie Consent for AdSense GDPR/CCPA compliance */
(function () {
  'use strict';

  var CONSENT_KEY = 'ctw_cookie_consent';
  var HIDDEN_KEY = 'ctw_consent_hidden';

  if (localStorage.getItem(CONSENT_KEY) === '1') { window.__adsense_allowed = true; return; }

  var banner = document.createElement('div');
  banner.id = 'cookie-consent';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', 'Cookie consent');
  banner.innerHTML =
    '<div class="cc-inner">' +
      '<p class="cc-text">We use cookies to personalise ads and analyse traffic. By clicking "Accept" you consent to our use of cookies. <a href="/en/privacy/">Learn more</a></p>' +
      '<div class="cc-actions">' +
        '<button id="cc-reject" class="cc-btn cc-btn-secondary">Reject</button>' +
        '<button id="cc-accept" class="cc-btn cc-btn-primary">Accept</button>' +
      '</div>' +
    '</div>';

  document.body.prepend(banner);

  function hideBanner() {
    banner.classList.add('cc-hidden');
    localStorage.setItem(HIDDEN_KEY, '1');
    setTimeout(function () { if (banner.parentNode) banner.parentNode.removeChild(banner); }, 400);
  }

  function accept() {
    localStorage.setItem(CONSENT_KEY, '1');
    window.__adsense_allowed = true;
    hideBanner();
    if (typeof loadDeferredAds === 'function') loadDeferredAds();
    try {
      if (typeof gtag === 'function') gtag('consent', 'update', { ad_storage: 'granted', analytics_storage: 'granted' });
    } catch (e) {}
  }

  function reject() {
    localStorage.setItem(CONSENT_KEY, '0');
    window.__adsense_allowed = false;
    hideBanner();
    try {
      if (typeof gtag === 'function') gtag('consent', 'update', { ad_storage: 'denied', analytics_storage: 'denied' });
    } catch (e) {}
  }

  document.getElementById('cc-accept').addEventListener('click', accept);
  document.getElementById('cc-reject').addEventListener('click', reject);

  window.__adsense_allowed = false;
})();

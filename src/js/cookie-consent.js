/* CalcToWork - Cookie Consent for AdSense GDPR/CCPA compliance */
(function () {
  'use strict';

  var CONSENT_KEY = 'ctw_cookie_consent';
  var HIDDEN_KEY = 'ctw_consent_hidden';

  if (localStorage.getItem(CONSENT_KEY) === '1') { window.__adsense_allowed = true; return; }

  var i18n = (window.COOKIE_CONSENT_I18N || {});
  var text = i18n.text || 'We use cookies to personalise ads and analyse traffic. By clicking "Accept" you consent to our use of cookies.';
  var learnMore = i18n.learn_more || 'Learn more';
  var acceptLabel = i18n.accept || 'Accept';
  var rejectLabel = i18n.reject || 'Reject';
  var privacyPath = i18n.privacy_path || '/en/privacy/';

  var banner = document.createElement('div');
  banner.id = 'cookie-consent';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', 'Cookie consent');
  banner.innerHTML =
    '<div class="cc-inner">' +
      '<p class="cc-text">' + text + ' <a href="' + privacyPath + '">' + learnMore + '</a></p>' +
      '<div class="cc-actions">' +
        '<button id="cc-reject" class="cc-btn cc-btn-secondary">' + rejectLabel + '</button>' +
        '<button id="cc-accept" class="cc-btn cc-btn-primary">' + acceptLabel + '</button>' +
      '</div>' +
    '</div>';

  document.body.prepend(banner);

  var DECIDED_UNTIL_KEY = 'ctw_consent_decided_until';
  var nowTs = Date.now();
  var decidedUntil = localStorage.getItem(DECIDED_UNTIL_KEY);
  if (decidedUntil && parseInt(decidedUntil, 10) > nowTs) {
    if (banner.parentNode) banner.parentNode.removeChild(banner);
    return;
  }

  function hideBanner() {
    banner.classList.add('cc-hidden');
    localStorage.setItem(HIDDEN_KEY, '1');
    localStorage.setItem(DECIDED_UNTIL_KEY, String(nowTs + 30 * 24 * 60 * 60 * 1000));
    setTimeout(function () { if (banner.parentNode) banner.parentNode.removeChild(banner); }, 400);
  }

  function accept() {
    localStorage.setItem(CONSENT_KEY, '1');
    window.__adsense_allowed = true;
    hideBanner();
    if (typeof window.__loadAdsense === 'function') window.__loadAdsense();
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

  var ccAccept = document.getElementById('cc-accept');
  var ccReject = document.getElementById('cc-reject');
  if (ccAccept) ccAccept.addEventListener('click', accept);
  if (ccReject) ccReject.addEventListener('click', reject);

  window.__adsense_allowed = false;
})();

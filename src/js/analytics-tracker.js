/**
 * CalcToWork Analytics Event Tracker
 * Writes user interaction events directly to Firestore
 */

(function() {
  // Configuration
  const CONFIG = {
    collection: 'analytics_events',
    batchSize: 5,
    flushInterval: 30000,
    sampleRate: 1.0,
  };

  // State
  let eventQueue = [];
  let sessionId = getSessionId();
  let pageLoadTime = Date.now();
  let calculationCount = 0;
  let flushTimer = null;
  let db = null;

  // Initialize
  function init() {
    // Only run on allowed domains (prevents abuse on staging/localhost/forks)
    var host = window.location.hostname;
    if (!/^(www\.)?calcto\.work$/.test(host)) {
      console.log('[CTWAnalytics] Skipped: unsupported domain', host);
      return;
    }

    if (Math.random() > CONFIG.sampleRate) return;

    // Wait for Firebase to be ready
    if (typeof firebase === 'undefined' || !firebase.apps || firebase.apps.length === 0) {
      setTimeout(init, 500);
      return;
    }
    try {
      db = firebase.firestore();
    } catch (e) {
      console.error('Analytics: Firestore init failed', e);
      return;
    }

    trackPageView();
    window.addEventListener('beforeunload', flushEvents);
    window.addEventListener('visibilitychange', handleVisibilityChange);
    setupInteractionTracking();
    startFlushTimer();
  }

  /* Opt out of analytics on this device: visit any page with ?ctw_notrack=1
     (and ?ctw_notrack=0 to opt back in). Own-browser testing was landing in the
     same numbers as real visitors, which quietly inflates every daily figure. */
  function isOptedOut() {
    try {
      var q = String(location.search || "");
      if (q.indexOf("ctw_notrack=1") !== -1) localStorage.setItem("ctw_notrack", "1");
      if (q.indexOf("ctw_notrack=0") !== -1) localStorage.removeItem("ctw_notrack");
      return localStorage.getItem("ctw_notrack") === "1";
    } catch (e) { return false; }
  }

  function getSessionId() {
    let id = sessionStorage.getItem('ctw_session_id');
    if (!id) {
      id = 'sess_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
      sessionStorage.setItem('ctw_session_id', id);
    }
    return id;
  }

  function getUserId() {
    let id = localStorage.getItem('ctw_user_id');
    if (!id) {
      id = 'user_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
      localStorage.setItem('ctw_user_id', id);
    }
    return id;
  }

  function trackPageView() {
    track('page_view', {
      calc_id: getCalcId(),
      calc_slug: getCalcSlug(),
      referrer: document.referrer || 'direct',
      landing_page: window.location.href,
      screen_width: window.screen.width,
      screen_height: window.screen.height,
      viewport_width: window.innerWidth,
      viewport_height: window.innerHeight,
      device_memory: navigator.deviceMemory || 'unknown',
      connection: navigator.connection ? navigator.connection.effectiveType : 'unknown',
    });
  }

  function getCalcId() {
    const favBtn = document.getElementById('fav-btn');
    if (favBtn) return favBtn.getAttribute('data-calc-id');
    const meta = document.querySelector('meta[name="calculator-id"]');
    if (meta) return meta.getAttribute('content');
    return null;
  }

  function getCalcSlug() {
    return (window.CALC_CONFIG && window.CALC_CONFIG.slug) || null;
  }

  function setupInteractionTracking() {
    const calcBtn = document.getElementById('calc-btn');
    if (calcBtn) calcBtn.addEventListener('click', handleCalculate);

    const resetBtn = document.getElementById('btn-reset');
    if (resetBtn) resetBtn.addEventListener('click', () => track('reset_clicked', getCalcContext()));

    const copyBtn = document.getElementById('btn-copy');
    if (copyBtn) copyBtn.addEventListener('click', () => track('copy_results', getCalcContext()));

    const shareBtn = document.getElementById('btn-share');
    if (shareBtn) shareBtn.addEventListener('click', () => track('share_clicked', getCalcContext()));

    const pdfBtn = document.getElementById('btn-pdf');
    if (pdfBtn) pdfBtn.addEventListener('click', () => track('pdf_export', getCalcContext()));

    // One event per session, not one per field interaction. Per-field events were
    // ~70% of all analytics writes and told us nothing we act on.
    const inputs = document.querySelectorAll('#calc-form input, #calc-form select');
    let formEngaged = false;
    inputs.forEach(input => {
      input.addEventListener('change', () => {
        if (formEngaged) return;
        formEngaged = true;
        track('form_engaged', { ...getCalcContext(), fields_total: inputs.length });
      });
    });

    let maxScroll = 0;
    window.addEventListener('scroll', () => {
      const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
      if (scrollPercent > maxScroll) {
        maxScroll = scrollPercent;
        if (scrollPercent >= 50) trackScrollDepth(50);
        if (scrollPercent >= 100) trackScrollDepth(100);
      }
    });

    // Engagement heartbeat — fire only at a few milestones, then stop, and never
    // while the tab is hidden. Previously this fired every 10s forever, flooding
    // Firestore with hundreds of time_on_page writes per session (huge cost at scale).
    const PING_MILESTONES = [30, 120, 600];
    let nextPing = 0;
    const pingTimer = setInterval(() => {
      if (nextPing >= PING_MILESTONES.length) { clearInterval(pingTimer); return; }
      if (document.visibilityState === 'hidden') return; // don't count time in a background tab
      const t = Math.round((Date.now() - pageLoadTime) / 1000);
      if (t >= PING_MILESTONES[nextPing]) {
        track('time_on_page', { ...getCalcContext(), seconds: t });
        nextPing++;
      }
    }, 5000);

    document.addEventListener('mouseleave', (e) => {
      if (e.clientY <= 0) {
        track('exit_intent', { ...getCalcContext(), time_on_page: Math.round((Date.now() - pageLoadTime) / 1000), calculations_done: calculationCount });
      }
    });
  }

  function handleCalculate(e) {
    const inputs = {};
    const formInputs = document.querySelectorAll('#calc-form input, #calc-form select');
    formInputs.forEach(input => { inputs[input.id || input.name] = !!input.value; });
    const results = document.querySelectorAll('#calc-results .result-value, #calc-results .result');
    calculationCount++;
    track('calculation_completed', {
      calc_id: getCalcId(),
      calc_slug: getCalcSlug(),
      inputs_filled: Object.keys(inputs).filter(k => inputs[k]).length,
      inputs_total: Object.keys(inputs).length,
      results_count: results.length,
      calculation_number: calculationCount,
      time_to_calculate: Math.round((Date.now() - pageLoadTime) / 1000),
    });
  }

  const scrollTracked = {};
  function trackScrollDepth(percent) {
    if (!scrollTracked[percent]) {
      scrollTracked[percent] = true;
      track('scroll_depth', { ...getCalcContext(), percent: percent });
    }
  }

  function getCalcContext() {
    return {
      calc_id: getCalcId(),
      calc_slug: getCalcSlug(),
      time_on_page: Math.round((Date.now() - pageLoadTime) / 1000),
    };
  }

  function getPageLanguage() {
    if (window.CALC_LANG) return window.CALC_LANG;
    const path = window.location.pathname;
    const parts = path.split('/').filter(p => p);
    return (parts.length > 0) ? parts[0] : null;
  }

  function isBot() {
    const ua = (navigator.userAgent || '').toLowerCase();
    return /(bot|crawler|spider|scraper|curl|wget|headless|phantom|selenium|puppeteer|playwright|googlebot|bingbot|yandex|baidu|duckduckbot|slurp|facebookexternalhit|twitterbot|whatsapp|linkedinbot|semrush|ahrefs|majestic|moz\.com|lighthouse|pagespeed|gtmetrix|pingdom|prerender)/.test(ua);
  }


  /* Which search engine or site sent this visit. Bing matters here specifically:
     IndexNow pings Bing, so this is how we see whether that pays off. */
  function detectSource() {
    var r = document.referrer || '';
    if (!r) return 'direct';
    var host;
    try { host = new URL(r).hostname.toLowerCase(); } catch (e) { return 'other'; }
    if (host.indexOf(window.location.hostname) !== -1) return 'internal';
    if (/(^|\.)bing\./.test(host) || host.indexOf('msn.') !== -1) return 'bing';
    if (/(^|\.)google\./.test(host)) return 'google';
    if (host.indexOf('duckduckgo') !== -1) return 'duckduckgo';
    if (/(^|\.)yandex\./.test(host)) return 'yandex';
    if (host.indexOf('yahoo') !== -1) return 'yahoo';
    if (host.indexOf('ecosia') !== -1) return 'ecosia';
    if (host.indexOf('brave') !== -1) return 'brave';
    if (host.indexOf('baidu') !== -1) return 'baidu';
    if (host.indexOf('chatgpt') !== -1 || host.indexOf('openai') !== -1) return 'chatgpt';
    if (host.indexOf('perplexity') !== -1) return 'perplexity';
    if (host.indexOf('claude.ai') !== -1) return 'claude';
    if (host.indexOf('gemini.google') !== -1) return 'gemini';
    if (/facebook|instagram|twitter|x\.com|linkedin|reddit|pinterest|tiktok|youtube|whatsapp|t\.co/.test(host)) return 'social';
    return 'referral';
  }

  /* Browser family. Order matters: Edge and Opera both contain "Chrome" in their
     user-agent, so they must be tested before Chrome or everything looks like Chrome. */
  function detectBrowser() {
    var u = navigator.userAgent || '';
    if (/Edg\//.test(u)) return 'edge';
    if (/OPR\/|Opera/.test(u)) return 'opera';
    if (/SamsungBrowser/.test(u)) return 'samsung';
    if (/Firefox\//.test(u)) return 'firefox';
    if (/Chrome\//.test(u)) return 'chrome';
    if (/Safari\//.test(u) && /Version\//.test(u)) return 'safari';
    return 'other';
  }

  function detectDevice() {
    var u = navigator.userAgent || '';
    if (/iPad|Tablet/.test(u)) return 'tablet';
    if (/Mobi|Android|iPhone/.test(u)) return 'mobile';
    return 'desktop';
  }

  function track(eventName, eventData) {
    if (isOptedOut()) return;
    const event = {
      event_name: eventName,
      event_time: new Date().toISOString(),
      session_id: sessionId,
      user_id: getUserId(),
      page_url: window.location.href,
      page_title: document.title,
      referrer: document.referrer,
      user_agent: navigator.userAgent,
      language: getPageLanguage(),
      is_bot: isBot(),
      traffic_source: detectSource(),
      browser: detectBrowser(),
      device_type: detectDevice(),
      ...eventData,
    };
    eventQueue.push(event);
    if (eventQueue.length >= CONFIG.batchSize) flushEvents();
  }

  function flushEvents() {
    if (!db || eventQueue.length === 0) return;
    const eventsToSend = [...eventQueue];
    eventQueue = [];

    // Write each event as a separate Firestore document
    eventsToSend.forEach(evt => {
      try {
        const docData = {
          event_name: evt.event_name,
          event_time: firebase.firestore.Timestamp.fromDate(new Date(evt.event_time)),
          session_id: evt.session_id,
          user_id: evt.user_id,
          page_url: evt.page_url || null,
          page_title: evt.page_title || null,
          calc_id: evt.calc_id || null,
          calc_slug: evt.calc_slug || null,
          calc_name: evt.calc_name || null,
          referrer: evt.referrer || null,
          user_agent: evt.user_agent || null,
          traffic_source: evt.traffic_source || null,
          browser: evt.browser || null,
          device_type: evt.device_type || null,
          language: evt.language || null,
          is_bot: evt.is_bot || false,
          screen_width: evt.screen_width || null,
          screen_height: evt.screen_height || null,
          viewport_width: evt.viewport_width || null,
          viewport_height: evt.viewport_height || null,
          device_memory: evt.device_memory || null,
          connection: evt.connection || null,
          inputs_filled: evt.inputs_filled || null,
          inputs_total: evt.inputs_total || null,
          results_count: evt.results_count || null,
          calculation_number: evt.calculation_number || null,
          time_to_calculate: evt.time_to_calculate || null,
          time_on_page: evt.time_on_page || null,
          calculations_done: evt.calculations_done || null,
          field_id: evt.field_id || null,
          field_name: evt.field_name || null,
          has_value: evt.has_value || null,
          percent: evt.percent || null,
          seconds: evt.seconds || null,
          vote: evt.vote || null,
          share_platform: evt.share_platform || null,
          created_at: firebase.firestore.FieldValue.serverTimestamp(),
        };
        db.collection(CONFIG.collection).add(docData).catch(err => {
          // Silently fail to avoid breaking user experience
        });
      } catch (e) {
        // Silently fail
      }
    });
  }

  let hiddenEventCount = 0, lastHidden = 0;
  function handleVisibilityChange() {
    // page_visible was pure noise (re-fired on every tab return) — dropped.
    if (document.visibilityState !== 'hidden') return;
    const now = Date.now();
    flushEvents(); // always send queued events before the tab is backgrounded
    // Emit at most a few page_hidden events per session, debounced, so rapid
    // tab-switching can't flood the log.
    if (hiddenEventCount < 5 && now - lastHidden > 3000) {
      lastHidden = now; hiddenEventCount++;
      track('page_hidden', { ...getCalcContext(), time_on_page: Math.round((now - pageLoadTime) / 1000), calculations_done: calculationCount });
    }
  }

  function startFlushTimer() {
    if (flushTimer) clearInterval(flushTimer);
    flushTimer = setInterval(flushEvents, CONFIG.flushInterval);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.CTWAnalytics = { track, flush: flushEvents };
})();

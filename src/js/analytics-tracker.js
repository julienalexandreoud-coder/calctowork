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
    const path = window.location.pathname;
    const parts = path.split('/').filter(p => p);
    if (parts.length >= 2) return parts[parts.length - 2];
    return null;
  }

  function setupInteractionTracking() {
    const calcBtn = document.getElementById('calc-btn');
    if (calcBtn) calcBtn.addEventListener('click', handleCalculate);

    const resetBtn = document.getElementById('reset-btn');
    if (resetBtn) resetBtn.addEventListener('click', () => track('reset_clicked', getCalcContext()));

    const copyBtn = document.getElementById('btn-copy');
    if (copyBtn) copyBtn.addEventListener('click', () => track('copy_results', getCalcContext()));

    const shareBtn = document.getElementById('btn-share');
    if (shareBtn) shareBtn.addEventListener('click', () => track('share_clicked', getCalcContext()));

    const pdfBtn = document.getElementById('btn-pdf');
    if (pdfBtn) pdfBtn.addEventListener('click', () => track('pdf_export', getCalcContext()));

    const inputs = document.querySelectorAll('#calc-form input, #calc-form select');
    inputs.forEach(input => {
      input.addEventListener('focus', () => {
        track('input_focus', { ...getCalcContext(), field_id: input.id, field_name: input.name });
      });
      input.addEventListener('change', () => {
        track('input_changed', { ...getCalcContext(), field_id: input.id, field_name: input.name, has_value: !!input.value });
      });
    });

    let maxScroll = 0;
    window.addEventListener('scroll', () => {
      const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
      if (scrollPercent > maxScroll) {
        maxScroll = scrollPercent;
        if (scrollPercent >= 25) trackScrollDepth(25);
        if (scrollPercent >= 50) trackScrollDepth(50);
        if (scrollPercent >= 75) trackScrollDepth(75);
        if (scrollPercent >= 100) trackScrollDepth(100);
      }
    });

    setInterval(() => {
      const timeOnPage = Math.round((Date.now() - pageLoadTime) / 1000);
      if (timeOnPage % 10 === 0) {
        track('time_on_page', { ...getCalcContext(), seconds: timeOnPage });
      }
    }, 10000);

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

  function track(eventName, eventData) {
    const event = {
      event_name: eventName,
      event_time: new Date().toISOString(),
      session_id: sessionId,
      user_id: getUserId(),
      page_url: window.location.href,
      page_title: document.title,
      referrer: document.referrer,
      user_agent: navigator.userAgent,
      language: navigator.language,
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
          referrer: evt.referrer || null,
          user_agent: evt.user_agent || null,
          language: evt.language || null,
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

  function handleVisibilityChange() {
    if (document.visibilityState === 'hidden') {
      track('page_hidden', { ...getCalcContext(), time_on_page: Math.round((Date.now() - pageLoadTime) / 1000), calculations_done: calculationCount });
      flushEvents();
    } else {
      track('page_visible', { ...getCalcContext() });
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

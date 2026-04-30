/**
 * CalcToWork Analytics Event Tracker
 * Tracks user interactions with calculators for behavioral analytics
 */

(function() {
  // Configuration
  const CONFIG = {
    endpoint: 'https://us-central1-calctowork.cloudfunctions.net/analytics',  // Firebase Function URL
    sendBeacon: true,            // Use sendBeacon for reliability
    batchEvents: true,           // Batch events before sending
    batchSize: 5,                // Send after N events
    flushInterval: 30000,        // Or every 30 seconds
    sampleRate: 1.0,             // Track 100% of users (adjust for scale)
  };

  // State
  let eventQueue = [];
  let sessionId = getSessionId();
  let pageLoadTime = Date.now();
  let lastInteractionTime = Date.now();
  let calculationCount = 0;
  let flushTimer = null;

  // Initialize
  function init() {
    if (Math.random() > CONFIG.sampleRate) return;
    
    // Track page view
    trackPageView();
    
    // Track before unload
    window.addEventListener('beforeunload', flushEvents);
    window.addEventListener('visibilitychange', handleVisibilityChange);
    
    // Track interactions
    setupInteractionTracking();
    
    // Start flush timer
    startFlushTimer();
  }

  // Generate/get session ID
  function getSessionId() {
    let id = sessionStorage.getItem('ctw_session_id');
    if (!id) {
      id = 'sess_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
      sessionStorage.setItem('ctw_session_id', id);
    }
    return id;
  }

  // Get user ID (anonymous, localStorage based)
  function getUserId() {
    let id = localStorage.getItem('ctw_user_id');
    if (!id) {
      id = 'user_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
      localStorage.setItem('ctw_user_id', id);
    }
    return id;
  }

  // Track page view
  function trackPageView() {
    const calcId = getCalcId();
    const calcSlug = getCalcSlug();
    
    track('page_view', {
      calc_id: calcId,
      calc_slug: calcSlug,
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

  // Get calculator ID from page
  function getCalcId() {
    const favBtn = document.getElementById('fav-btn');
    if (favBtn) return favBtn.getAttribute('data-calc-id');
    
    // Try from meta
    const meta = document.querySelector('meta[name="calculator-id"]');
    if (meta) return meta.getAttribute('content');
    
    return null;
  }

  // Get calculator slug from URL
  function getCalcSlug() {
    const path = window.location.pathname;
    const parts = path.split('/').filter(p => p);
    // URL structure: /{lang}/{slug}/ or /{lang}/{block}/{slug}/
    if (parts.length >= 2) {
      return parts[parts.length - 2]; // Second to last
    }
    return null;
  }

  // Setup interaction tracking
  function setupInteractionTracking() {
    // Track calculate button clicks
    const calcBtn = document.getElementById('calc-btn');
    if (calcBtn) {
      calcBtn.addEventListener('click', handleCalculate);
    }

    // Track reset button clicks
    const resetBtn = document.getElementById('reset-btn');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        track('reset_clicked', getCalcContext());
      });
    }

    // Track copy result clicks
    const copyBtn = document.getElementById('btn-copy');
    if (copyBtn) {
      copyBtn.addEventListener('click', () => {
        track('copy_results', getCalcContext());
      });
    }

    // Track share clicks
    const shareBtn = document.getElementById('btn-share');
    if (shareBtn) {
      shareBtn.addEventListener('click', () => {
        track('share_clicked', getCalcContext());
      });
    }

    // Track PDF export
    const pdfBtn = document.getElementById('btn-pdf');
    if (pdfBtn) {
      pdfBtn.addEventListener('click', () => {
        track('pdf_export', getCalcContext());
      });
    }

    // Track input interactions
    const inputs = document.querySelectorAll('#calc-form input, #calc-form select');
    inputs.forEach(input => {
      input.addEventListener('focus', () => {
        track('input_focus', {
          ...getCalcContext(),
          field_id: input.id,
          field_name: input.name,
        });
      });
      
      input.addEventListener('change', () => {
        track('input_changed', {
          ...getCalcContext(),
          field_id: input.id,
          field_name: input.name,
          has_value: !!input.value,
        });
      });
    });

    // Track scroll depth
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

    // Track time on page (every 10 seconds)
    setInterval(() => {
      const timeOnPage = Math.round((Date.now() - pageLoadTime) / 1000);
      if (timeOnPage % 10 === 0) {
        track('time_on_page', {
          ...getCalcContext(),
          seconds: timeOnPage,
        });
      }
    }, 10000);

    // Track exit intent
    document.addEventListener('mouseleave', (e) => {
      if (e.clientY <= 0) {
        track('exit_intent', {
          ...getCalcContext(),
          time_on_page: Math.round((Date.now() - pageLoadTime) / 1000),
          calculations_done: calculationCount,
        });
      }
    });
  }

  // Handle calculate button
  function handleCalculate(e) {
    const calcId = getCalcId();
    const calcSlug = getCalcSlug();
    
    // Get input values (anonymized - just check if filled)
    const inputs = {};
    const formInputs = document.querySelectorAll('#calc-form input, #calc-form select');
    formInputs.forEach(input => {
      inputs[input.id || input.name] = !!input.value;
    });

    // Get results (count how many results shown)
    const results = document.querySelectorAll('#calc-results .result-value, #calc-results .result');
    
    calculationCount++;
    lastInteractionTime = Date.now();

    track('calculation_completed', {
      calc_id: calcId,
      calc_slug: calcSlug,
      inputs_filled: Object.keys(inputs).filter(k => inputs[k]).length,
      inputs_total: Object.keys(inputs).length,
      results_count: results.length,
      calculation_number: calculationCount,
      time_to_calculate: Math.round((Date.now() - pageLoadTime) / 1000),
    });
  }

  // Track scroll depth (only once per threshold)
  const scrollTracked = {};
  function trackScrollDepth(percent) {
    if (!scrollTracked[percent]) {
      scrollTracked[percent] = true;
      track('scroll_depth', {
        ...getCalcContext(),
        percent: percent,
      });
    }
  }

  // Get calculator context
  function getCalcContext() {
    return {
      calc_id: getCalcId(),
      calc_slug: getCalcSlug(),
      time_on_page: Math.round((Date.now() - pageLoadTime) / 1000),
    };
  }

  // Track event
  function track(eventName, eventData = {}) {
    const event = {
      event_id: 'evt_' + Math.random().toString(36).substr(2, 9),
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

    // Flush if batch is full
    if (CONFIG.batchEvents && eventQueue.length >= CONFIG.batchSize) {
      flushEvents();
    }
  }

  // Flush events to server
  function flushEvents() {
    if (eventQueue.length === 0) return;

    const eventsToSend = [...eventQueue];
    eventQueue = [];

    if (CONFIG.sendBeacon && navigator.sendBeacon) {
      // Use sendBeacon for reliability (works even when page closes)
      const blob = new Blob([JSON.stringify(eventsToSend)], { type: 'application/json' });
      navigator.sendBeacon(CONFIG.endpoint, blob);
    } else {
      // Fallback to fetch
      fetch(CONFIG.endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(eventsToSend),
        keepalive: true,
      }).catch(err => console.error('Analytics send failed:', err));
    }
  }

  // Handle visibility change (tab switch)
  function handleVisibilityChange() {
    if (document.visibilityState === 'hidden') {
      track('page_hidden', {
        ...getCalcContext(),
        time_on_page: Math.round((Date.now() - pageLoadTime) / 1000),
        calculations_done: calculationCount,
      });
      flushEvents();
    } else {
      track('page_visible', {
        ...getCalcContext(),
      });
    }
  }

  // Start flush timer
  function startFlushTimer() {
    if (flushTimer) clearInterval(flushTimer);
    flushTimer = setInterval(flushEvents, CONFIG.flushInterval);
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose track function globally for custom tracking
  window.CTWAnalytics = { track, flush: flushEvents };
})();

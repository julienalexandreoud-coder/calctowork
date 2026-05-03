// Favorites/bookmarks system for CalcToWork
// Uses localStorage to persist user's favorite calculators

(function() {
  'use strict';

  var STORAGE_KEY = 'calctowork_favorites';
  var MAX_FAVORITES = 50;

  function getFavorites() {
    try {
      var data = localStorage.getItem(STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch(e) {
      return [];
    }
  }

  function saveFavorites(favs) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(favs));
    } catch(e) {}
  }

  function isFavorite(calcId) {
    var favs = getFavorites();
    return favs.some(function(f) { return f.id === calcId; });
  }

  function trackFavorite(eventName, calcId, calcName) {
    try {
      if (window.CTWAnalytics && typeof window.CTWAnalytics.track === 'function') {
        window.CTWAnalytics.track(eventName, { calc_id: calcId, calc_name: calcName || '' });
      }
    } catch(e) {}
  }

  function addFavorite(calcId, calcName, calcUrl) {
    var favs = getFavorites();
    if (favs.some(function(f) { return f.id === calcId; })) return;
    favs.unshift({ id: calcId, name: calcName, url: calcUrl, addedAt: Date.now() });
    if (favs.length > MAX_FAVORITES) favs = favs.slice(0, MAX_FAVORITES);
    saveFavorites(favs);
    updateHeartIcon(calcId);
    renderFavoritesSection();
    trackFavorite('favorite_added', calcId, calcName);
  }

  function removeFavorite(calcId) {
    var favs = getFavorites();
    var removed = favs.filter(function(f) { return f.id === calcId; });
    var calcName = removed.length ? removed[0].name : '';
    favs = favs.filter(function(f) { return f.id !== calcId; });
    saveFavorites(favs);
    updateHeartIcon(calcId);
    renderFavoritesSection();
    trackFavorite('favorite_removed', calcId, calcName);
  }

  function toggleFavorite(calcId, calcName, calcUrl) {
    if (isFavorite(calcId)) {
      removeFavorite(calcId);
    } else {
      addFavorite(calcId, calcName, calcUrl);
    }
  }

  function updateHeartIcon(calcId) {
    var btn = document.getElementById('fav-btn');
    if (!btn) return;
    var filled = isFavorite(calcId);
    btn.innerHTML = filled
      ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>'
      : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
    btn.classList.toggle('is-favorite', filled);
    btn.title = filled ? 'Remove from favorites' : 'Save to favorites';
  }

  function renderFavoritesSection() {
    var container = document.getElementById('favorites-list');
    if (!container) return;
    var favs = getFavorites();
    var section = container.closest('.favorites-section');
    if (!section) return;

    if (favs.length === 0) {
      section.style.display = 'none';
      return;
    }
    section.style.display = '';
    
    var html = '';
    favs.forEach(function(f) {
      html += '<a href="' + f.url + '" class="fav-item">'
        + '<span class="fav-name">' + f.name + '</span>'
        + '<button class="fav-remove" data-id="' + f.id + '" title="Remove">&times;</button>'
        + '</a>';
    });
    container.innerHTML = html;

    container.querySelectorAll('.fav-remove').forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        removeFavorite(btn.getAttribute('data-id'));
      });
    });
  }

  // Initialize on calculator pages
  function initCalculatorPage() {
    var btn = document.getElementById('fav-btn');
    if (!btn) return;
    var calcId = btn.getAttribute('data-calc-id');
    var calcName = btn.getAttribute('data-calc-name');
    var calcUrl = window.location.pathname;

    updateHeartIcon(calcId);

    btn.addEventListener('click', function() {
      toggleFavorite(calcId, calcName, calcUrl);
    });
  }

  // Initialize on homepage
  function initHomepage() {
    renderFavoritesSection();
  }

  // Run on page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    initCalculatorPage();
    initHomepage();

    // Update fav icons on cards if present
    document.querySelectorAll('.fav-btn-inline').forEach(function(btn) {
      var id = btn.getAttribute('data-calc-id');
      if (isFavorite(id)) btn.classList.add('is-favorite');
    });
  }

  // Expose for external use
  window.CalcToWorkFavorites = {
    get: getFavorites,
    is: isFavorite,
    add: addFavorite,
    remove: removeFavorite,
    toggle: toggleFavorite
  };
})();
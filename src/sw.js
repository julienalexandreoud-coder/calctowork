/* CalcToWork Service Worker – shell cache for offline/fast repeat visits */
var CACHE = 'ctw-v2';
var SHELL = [
  '/css/styles.css',
  '/js/calculator.js',
  '/js/favorites.js',
  '/js/history.js',
  '/js/dark-mode.js',
  '/favicon.svg'
];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE).then(function (c) { return c.addAll(SHELL); })
  );
  self.skipWaiting();
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  var url = e.request.url;
  // Cache-first for static assets, network-first for HTML pages
  if (/\.(css|js|svg|png|ico|woff2?)(\?|$)/.test(url)) {
    e.respondWith(
      caches.match(e.request).then(function (cached) {
        return cached || fetch(e.request).then(function (res) {
          if (res && res.status === 200) {
            var clone = res.clone();
            caches.open(CACHE).then(function (c) { c.put(e.request, clone); });
          }
          return res;
        });
      })
    );
  }
});

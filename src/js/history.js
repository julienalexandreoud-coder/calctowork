/* CalcToWork – Recently Visited History */
(function () {
  'use strict';
  var KEY = 'ctw_history';
  var MAX = 8;

  function get() {
    try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; }
  }
  function save(items) {
    try { localStorage.setItem(KEY, JSON.stringify(items)); } catch (e) {}
  }
  function record(id, name, url) {
    var items = get().filter(function (i) { return i.id !== id; });
    items.unshift({ id: id, name: name, url: url, ts: Date.now() });
    if (items.length > MAX) items = items.slice(0, MAX);
    save(items);
  }
  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function render() {
    var container = document.getElementById('recent-list');
    if (!container) return;
    var section = container.closest('.recent-section');
    if (!section) return;
    var items = get();
    if (!items.length) { section.style.display = 'none'; return; }
    section.style.display = '';
    var html = '';
    items.forEach(function (f) {
      html += '<a href="' + f.url + '" class="fav-item"><span class="fav-name">' + esc(f.name) + '</span></a>';
    });
    container.innerHTML = html;
  }

  // Record visit on calculator pages
  var favBtn = document.getElementById('fav-btn');
  if (favBtn) {
    var id = favBtn.getAttribute('data-calc-id');
    var name = favBtn.getAttribute('data-calc-name') || document.title;
    if (id) record(id, name, window.location.pathname);
  }

  // Render on homepage
  render();

  window.CalcToWorkHistory = { record: record, render: render };
}());

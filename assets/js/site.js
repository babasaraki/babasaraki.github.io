/* Site behaviour: theme toggle, mobile nav, publication filtering, email
   assembly. No dependencies, no build step. */
(function () {
  'use strict';

  /* ---------------------------------------------------------------- theme */
  var root = document.documentElement;
  function paintThemeIcons() {
    var t = root.getAttribute('data-theme');
    document.querySelectorAll('[data-theme-icon]').forEach(function (el) {
      el.hidden = el.getAttribute('data-theme-icon') !== t;
    });
  }
  paintThemeIcons();

  var themeBtn = document.getElementById('themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
      paintThemeIcons();
    });
  }

  /* ------------------------------------------------------------------ nav */
  var navBtn = document.getElementById('navToggle');
  var nav = document.getElementById('siteNav');
  if (navBtn && nav) {
    navBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      navBtn.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('open');
        navBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---------------------------------------------------------------- email */
  document.querySelectorAll('.js-email').forEach(function (a) {
    var addr = a.dataset.user + '@' + a.dataset.domain;
    a.textContent = addr;
    a.href = 'mailto:' + addr;
  });

  /* --------------------------------------------------------- publications */
  var list = document.getElementById('pubList');
  if (!list) return;

  var items = Array.prototype.slice.call(list.querySelectorAll('.pub'));
  var search = document.getElementById('pubSearch');
  var countEl = document.getElementById('pubCount');
  var emptyEl = document.getElementById('pubEmpty');
  var state = { text: '', type: '', quartile: '' };

  function apply() {
    var shown = 0;
    items.forEach(function (li) {
      var okType = !state.type || li.dataset.type === state.type;
      var okQ = !state.quartile ||
                state.quartile.split(',').indexOf(li.dataset.quartile) !== -1;
      var okText = !state.text || li.dataset.text.indexOf(state.text) !== -1;
      var show = okType && okQ && okText;
      li.hidden = !show;
      if (show) shown++;
    });
    if (countEl) {
      countEl.textContent = shown === items.length
        ? 'Showing all ' + items.length + ' outputs.'
        : 'Showing ' + shown + ' of ' + items.length + ' outputs.';
    }
    if (emptyEl) emptyEl.hidden = shown !== 0;
  }

  if (search) {
    var timer;
    search.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () {
        state.text = search.value.trim().toLowerCase();
        apply();
      }, 120);
    });
  }

  document.querySelectorAll('.filter').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var group = btn.dataset.filter;
      document.querySelectorAll('.filter[data-filter="' + group + '"]').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b === btn));
      });
      state[group] = btn.dataset.value;
      apply();
    });
  });

  apply();
})();

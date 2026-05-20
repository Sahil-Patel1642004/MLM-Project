// Minimal UI helpers (no API wiring yet)
(function () {
  function setActiveNav() {
    const links = document.querySelectorAll('.nav__link[data-nav]');
    const path = (location.pathname || '').toLowerCase();

    let activeKey = null;
    for (const a of links) {
      const key = a.getAttribute('data-nav');
      if (!key) continue;
      const href = (a.getAttribute('href') || '').toLowerCase();
      if (href && path.includes(href)) {
        activeKey = key;
        break;
      }
      if (location.pathname && location.pathname.toLowerCase().endsWith(href)) {
        activeKey = key;
        break;
      }
    }

    if (!activeKey) {
      const last = (location.href || '').toLowerCase();
      for (const a of links) {
        const href = (a.getAttribute('href') || '').toLowerCase();
        if (last.includes(href)) {
          activeKey = a.getAttribute('data-nav');
          break;
        }
      }
    }

    for (const a of links) {
      const key = a.getAttribute('data-nav');
      if (!key) continue;
      a.classList.toggle('nav__link--active', key === activeKey);
    }
  }

  function setBreadcrumb() {
    const crumb = document.getElementById('pageBreadcrumb');
    if (!crumb) return;
    if (crumb.textContent && crumb.textContent.trim()) return;
    crumb.textContent = document.title || 'Page';
  }

  window.addEventListener('DOMContentLoaded', () => {
    setBreadcrumb();
    setActiveNav();
  });
})();


const CACHE_NAME = 'ncm-site-v2';
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/about.html',
  '/contact.html',
  '/portfolio.html',
  '/process.html',
  '/projects.html',
  '/services.html',
  '/tech.html',
  '/testimonials.html',
  '/thanks.html',
  '/404.html',
  '/styles.min.css',
  '/script.min.js',
  '/site.webmanifest',
  '/assets/favicon.ico',
  '/assets/favicon.svg',
  '/assets/icons/safari-pinned-tab.svg',
  '/assets/icons/app-icon.svg',
  '/assets/logo.svg',
  '/assets/og-image.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE_URLS))
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;

  if (req.mode === 'navigate') {
    // Network-first for HTML navigations
    event.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(req, copy));
          return res;
        })
        .catch(() => caches.match(req).then((r) => r || caches.match('/404.html')))
    );
    return;
  }

  // Cache-first for static assets
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(req, copy));
        return res;
      });
    })
  );
});

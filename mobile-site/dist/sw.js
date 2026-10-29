const CACHE = "ict-mobile-93c937ca240d";
const ASSETS = ["./index.html", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png"];
self.addEventListener("install", event => event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting())));
self.addEventListener("activate", event => event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith("ict-mobile-") && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener("fetch", event => {
  const url = new URL(event.request.url);
  if (event.request.method !== "GET" || url.origin !== self.location.origin) return;
  if (event.request.mode === "navigate") {
    event.respondWith(fetch(event.request).then(response => {
      if (response.ok && response.headers.get("content-type")?.includes("text/html")) {
        const copy = response.clone(); event.waitUntil(caches.open(CACHE).then(cache => cache.put("./index.html", copy)));
      }
      return response;
    }).catch(() => caches.match("./index.html")));
  } else event.respondWith(caches.match(event.request).then(response => response || fetch(event.request)));
});

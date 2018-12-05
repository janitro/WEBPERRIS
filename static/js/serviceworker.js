importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.2.0/workbox-sw.js');

if (workbox) {
  console.log(`Service Worker Cargado`);
} else {
  console.log(`No carga lloro`);
}

workbox.setConfig({
  debug: false
});

// workbox.core.setLogLevel(workbox.core.LOG_LEVELS.debug);


workbox.routing.registerRoute(
  /\.(?:js|css)$/,
  workbox.strategies.staleWhileRevalidate({
    cacheName: 'static-resources',
  }),
);

workbox.routing.registerRoute(
  /\.(?:png|gif|jpg|jpeg|svg)$/,
  workbox.strategies.cacheFirst({
    cacheName: 'images' , 
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 60,
        maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Dias
      }),
    ],
  }),
);

workbox.routing.registerRoute(
  new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
  workbox.strategies.cacheFirst({
    cacheName: 'googleapis',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 30,
      }),
    ],
  }),
);

workbox.precaching.precacheAndRoute(
  [
    '/',
    '/login',
    '/ListarPerros',
    '/Mascota',
    '/signup',
    '/logout'
    
  ],
  {
    directoryIndex: null,
  }
);

workbox.routing.registerRoute(
 
      new RegExp('/'), 
      workbox.strategies.networkFirst({
        cacheName: 'html-resources',
      })
    );

// fallback a offline page en caso de no encontrar nada en cache
var networkFirstHandler = workbox.strategies.networkFirst({
  cacheName: 'default',
  plugins: [
    new workbox.expiration.Plugin({
      maxEntries: 10
    }),
    new workbox.cacheableResponse.Plugin({
      statuses: [200]
    })
  ]
});

const matcher = ({event}) => event.request.mode === 'navigate';
const handler = (args) => networkFirstHandler.handle(args).then((response) => (!response) ? caches.match('/offline') : response);

workbox.routing.registerRoute(matcher, handler);
// fin fallback offline
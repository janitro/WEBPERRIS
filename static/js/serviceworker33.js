var CACHE_NAME = "misitio";
var CACHED_URLS = [
  
  
  "/static/images/misperris.png",
  "/templates/home.html"

 
]

self.addEventListener("install", function(event){
  event.waitUntil(// dont' let install event finish until this succeeds
    caches.open(CACHE_NAME)// open new or existing cache, returns a promise
      .then(function(cache){// if cache-opening promise resolves
        return cache.addAll(CACHED_URLS)// add CACHED_URLS
    })
  );
});

self.addEventListener("activate", function(event){
  event.waitUntil( // don't finish activation until this succeeds
    caches.keys() // a promise containing an array of all cache names
      .then(function(cacheNames){
        return Promise.all( // return a promise that only succeeds if all of the promises in the array succeed
          cacheNames.map(function(cacheName){ // to create an array of promises, map the array of cachenames
            // for each of them:
            if (CACHE_NAME !== cacheName ){ // if name is not the same as current caches name
              return caches.delete(cacheName); // delete it and succeeds after that
            };
          })
        );
      })
  );
});

self.addEventListener("fetch", function(event){
  var requestURL = new URL(event.request.url);
  // request for a html file
  if (event.request.headers.get("accept").includes("text/html")){
    event.respondWith( // answer the request with ...
      caches.open(CACHE_NAME).then(function(cache){ //open cache
        return fetch(event.request) // try to fetch from server
          .then(function(networkResponse){ //if suceeds
            if (networkResponse.ok){ //if it is not some errorpage
              //put a copy of the response in the cache
              cache.put(event.request, networkResponse.clone());
            };
            return networkResponse; // and return the response
          }).catch(function(){ // if fetching from server fails
            // return copy from cache or offline page from cache
            return cache.match(event.request).then(function(response){
              return response || cache.match("/templates/home.html");
            });
          });
      })
    );
  //request is one of the resources cached during registration
  } else if(
    CACHED_URLS.includes(requestURL.href) ||
    CACHED_URLS.includes(requestURL.pathname)
  ){
    event.respondWith( // answer the request with ...
      caches.open(CACHE_NAME).then(function(cache){ // open cache
        return cache.match(event.request).then(function(response){
          // return matched result from cache or try to fetch from network
          return response || fetch(event.request);
        });
      })
    );
  };
});

self.addEventListener("message", function(event){
  if (event.data === "offline?"){ // check the message data
    fetch("/templates/").catch(function(response){ // fetch from the network and if it fails
      self.clients.get(event.source.id).then(function(client){ // get the client that sent this message
        client.postMessage("offline"); // and send a confirmation message
      });
    });
  };
});
$(document).ready(function () {
    /** Initiates google maps API */
    function initMap() {
      const Nybrogatan23 = {
        lat: 59.335502546345275,
        lng: 18.07753893553396
      };
      const map = new google.maps.Map(document.getElementById("google-map"), {
        zoom: 14,
        mapId: 'c3bf27aa22c010f7',
        center: Nybrogatan23,
      });
      const marker = new google.maps.Marker({
        position: Nybrogatan23,
        map: map,
      });
    }
  
    window.initMap = initMap;
    initMap();
  });
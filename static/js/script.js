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


  /** Sets the slide change interval for the carousels */
  $('#carouselExampleIndicators').carousel({
    interval: 8000
  })
  $('#nybro23-image-gallery').carousel({
    interval: 4000
  })

  /** Unpauses zoom animation then navigates to the Nybrogatan23 page after short delay. */
  function timeOut(initialDelay) {
    if (initialDelay === true) {
      setTimeout(function () {
        $('#nybrogatan-image').css("animation-play-state", "running");
      }, 500);
      setTimeout(function () {
        let path = window.location.href.slice(0, -2).concat("/nybrogatan23")
        window.open(path, "_self")
      }, 750);
    } else {
      $('#nybrogatan-image').css("animation-play-state", "running");
      setTimeout(function () {
        let path = window.location.href.slice(0, -2).concat("/nybrogatan23")
        window.open(path, "_self")
      }, 500);
    }
  }


  /** Changes the carousel slide to corresponding navlink when clicked. */
  for (let i = 0; i < $('.carousel-inner').children().length; i++) {
    $('#slide-' + i).click(function () {
      $('.carousel').carousel(i);
    })
  }


  /** Removes active class from current navlink then add it to the corresponding slide. */
  $('#carouselExampleIndicators').on('slide.bs.carousel', function () {
    for (let i = 0; i < $('.carousel-inner').children().length; i++) {
      $('#slide-' + i).parent().removeClass('active');
    }
    if ($('.carousel-indicators').children().hasClass('active')) {
      let slideNum = ($('.active').attr('data-slide-to'));
      $('#slide-' + slideNum).parent().addClass('active');
    }
  })


  /** Collapses the navbar on click anywhere on the page. */
  $('body').click(function () {
    $('#navbarSupportedContent').collapse('hide');
  })


  $('#slide-2').click(function () {
    timeOut(true);
  })


  $('#nybrogatan-image').click(function () {
    timeOut(false);
  })
});
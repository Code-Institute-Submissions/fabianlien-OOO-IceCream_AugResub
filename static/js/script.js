$(document).ready(function() { 
    $('.carousel').carousel({
      interval: 8000
    })


    /** Changes the carousel slide to corresponding navlink when clicked */
    for (let i = 0; i < $('.carousel-inner').children().length; i++) {
      $('#slide-' + i).click(function() {
          $('.carousel').carousel(i);
      })
    }


    /** Removes active class from current navlink then add it to the corresponding slide */
    $('#carouselExampleIndicators').on('slide.bs.carousel', function () {
      for (let i = 0; i < $('.carousel-inner').children().length; i++) {
          $('#slide-' + i).parent().removeClass('active')
      }
      if ($('.carousel-indicators').children().hasClass('active')) {
          let slideNum = ($('.active').attr('data-slide-to'))
          console.log($('#slide-' + slideNum))
          $('#slide-' + slideNum).parent().addClass('active')
      }
    })
});

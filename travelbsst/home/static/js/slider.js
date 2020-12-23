$(window).on('load', function () {
var owl = $('.owl-carousel');
owl.trigger('play.owl.autoplay',[6000]);

owl.owlCarousel({
    autoplayHoverPause:false
});
})
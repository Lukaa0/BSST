(function ($) {
	jQuery('.owl-carousel').owlCarousel({
        loop:false,
        nav:true,
        margin:10,
        mouseDrag:true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:3
            }
        }
    });


})(jQuery);
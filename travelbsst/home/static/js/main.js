(function ($) {

  "use strict";

  

  // Preloader

  $(window).on('load', function () {
	// Page is loaded
    $(function() {

        $('.lazy').Lazy({
			effect: "fadeIn",
          effectTime: 2000,
          threshold: 0,
        });
	});
	
    if ($('#preloader').length) {

      $('#preloader').delay(100).fadeOut('slow', function () {

        $(this).remove();

      });


// Favorite Button - Heart
$('.favme').click(function() {
	$(this).toggleClass('active');
});

/* when a user clicks, toggle the 'is-animating' class */
$(".favme").on('click touchstart', function(){
  $(this).toggleClass('is_animating');
});

/*when the animation is over, remove the class*/
$(".favme").on('animationend', function(){
  $(this).toggleClass('is_animating');
});

    }

	});

	



  // Back to top button

  $(window).scroll(function() {

    if ($(this).scrollTop() > 100) {

	  $('.back-to-top').fadeIn('slow');
	  $('.play-btn').fadeIn('slow');

    } else {

	  $('.back-to-top').fadeOut('slow');
	  $('.play-btn').fadeOut('slow');


    }

  });

  $('.back-to-top').click(function(){

    $('html, body').animate({scrollTop : 0},1500, 'easeInOutExpo');

    return false;

  });
  
  $('.owl-carousel').owlCarousel({
    loop:false,
	nav:true,
	margin:0,
    mouseDrag:false,
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

  function adjustSize(id,more,dots,readmore,readless){
	var element = id
	var width=element.width();
	var height = element.height();
	element.css("background-size",width+ "px "+height+"px");
	
	$(more).slideToggle("slow");
			$(dots).hide();
			$(readmore).hide();
			$(readmore).innerHTML = "Read less"; 
			$(readless).show();
};

	

$(".rm").click(function(){
	
	var parent = $(this).parents("section");
	var readMore = parent.find('div[id*=readMore]');
	var more = parent.find('p[id*=more]');

	var dots = parent.find('span[id*=dots]');

	var read_more = parent.find('button[id*=read-more]');

	var read_less = parent.find('button[id*=read-less]');
	adjustSize(readMore,more,dots,read_more,read_less);

});
$(".rl").click(function(){
	var parent = $(this).parents("section");
	var readMore = parent.find('div[id*=readMore]');
	var more = parent.find('p[id*=more]');

	var dots = parent.find('span[id*=dots]');

	var read_more = parent.find('button[id*=read-more]');

	var read_less = parent.find('button[id*=read-less]');
	initiateReadLess(dots,read_less,read_more,more,readMore);
});

	function initiateReadLess(dots,read_less,read_more,more,readMore){

			$(dots).slideToggle("fast");
			$(read_less).innerHTML = "Read more"; 
			$(read_less).slideToggle("slow");
			$(read_more).slideToggle("slow");
			$(more).slideToggle("slow",function(){
				readMore.css("background-size","cover");

			});
		
		};
	var nav = $('nav');

	var navHeight = nav.outerHeight();



	/*--/ ScrollReveal /Easy scroll animations for web and mobile browsers /--*/

	window.sr = ScrollReveal();

	sr.reveal('.foo', { duration: 1000, delay: 15 });



	/*--/ Carousel owl /--*/

	$('#carousel').owlCarousel({

		loop: true,

		margin: -1,

		items: 1,

		nav: true,

		navText: ['<i class="ion-ios-arrow-back" aria-hidden="true"></i>', '<i class="ion-ios-arrow-forward" aria-hidden="true"></i>'],

		autoplay: true,

		autoplayTimeout: 3000,

		autoplayHoverPause: true

	});



	/*--/ Animate Carousel /--*/

	$('.intro-carousel').on('translate.owl.carousel', function () {

		$('.intro-content .intro-title').removeClass('zoomIn animated').hide();

		$('.intro-content .intro-price').removeClass('fadeInUp animated').hide();

		$('.intro-content .intro-title-top, .intro-content .spacial').removeClass('fadeIn animated').hide();

	});



	$('.intro-carousel').on('translated.owl.carousel', function () {

		$('.intro-content .intro-title').addClass('zoomIn animated').show();

		$('.intro-content .intro-price').addClass('fadeInUp animated').show();

		$('.intro-content .intro-title-top, .intro-content .spacial').addClass('fadeIn animated').show();

	});



	/*--/ Navbar Collapse /--*/

	$('.navbar-toggle-box-collapse').on('click', function () {

		$('body').removeClass('box-collapse-closed').addClass('box-collapse-open');

	});

	$('.close-box-collapse, .click-closed').on('click', function () {

		$('body').removeClass('box-collapse-open').addClass('box-collapse-closed');

		$('.menu-list ul').slideUp(700);

	});



	/*--/ Navbar Menu Reduce /--*/

	$(window).trigger('scroll');

	$(window).bind('scroll', function () {

		var pixels = 50;

		var top = 1200;

		if ($(window).scrollTop() > pixels) {

			$('.navbar-default').addClass('navbar-reduce');

			$('.navbar-default').removeClass('navbar-trans');

		} else {

			$('.navbar-default').addClass('navbar-trans');

			$('.navbar-default').removeClass('navbar-reduce');

		}

		if ($(window).scrollTop() > top) {

			$('.scrolltop-mf').fadeIn(1000, "easeInOutExpo");

		} else {

			$('.scrolltop-mf').fadeOut(1000, "easeInOutExpo");

		}

	});



	/*--/ Property owl /--*/

	$('#property-carousel').owlCarousel({

		loop: true,

		margin: 30,

		responsive: {

			0: {

				items: 1,

			},

			769: {

				items: 2,

			},
			
			992: {
				
				items: 3,

			}

		}

	});



	/*--/ Property owl owl /--*/

	$('#property-single-carousel').owlCarousel({

		loop: true,

		margin: 0,  

		nav: true,

		navText: ['<i class="ion-ios-arrow-back" aria-hidden="true"></i>', '<i class="ion-ios-arrow-forward" aria-hidden="true"></i>'],

		responsive: {

			0: {

				items: 1,

			}

		}

	});



	/*--/ News owl /--*/

	$('#new-carousel').owlCarousel({

		loop: true,

		margin: 30,

		responsive: {

			0: {  

				items: 1,

			},

			769: {

				items: 2,

			},

			992: {

				items: 3,

			}

		}

	});



	/*--/ Testimonials owl /--*/

	$('#testimonial-carousel').owlCarousel({

		margin: 0,

		autoplay: true,

		nav: true,

		animateOut: 'fadeOut',

		animateIn: 'fadeInUp',

		navText: ['<i class="ion-ios-arrow-back" aria-hidden="true"></i>', '<i class="ion-ios-arrow-forward" aria-hidden="true"></i>'],

		autoplayTimeout: 4000,

		autoplayHoverPause: true,

		responsive: {

			0: {

				items: 1,

			}

		}

	});

	
// Accomodation sticky-form js

    function checkOffset() {
    if($('#modal_content_desktop ').offset().top + $('#modal_content_desktop ').height()
                                           >= $('#footer').offset().top - 10)
        $('#modal_content_desktop ').css('position', 'absolute');
    if($(document).scrollTop() + window.innerHeight < $('#footer').offset().top)
        $('#modal_content_desktop ').css('position', 'fixed'); // restore when you scroll up
    $('#modal_content_desktop ').text($(document).scrollTop() + window.innerHeight);
    if(screen.width<575){

    }
}

$(document).scroll(function() {
    checkOffset();
});

	



})(jQuery);


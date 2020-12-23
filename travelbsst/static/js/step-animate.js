$(window).on('scroll', function (e) {
    var top = $(window).scrollTop() + $(window).height(),
        isVisible1 = top >= $('#step1').offset().top;
        isVisible2 = top >= $('#step2').offset().top;
        isVisible3 = top >= $('#step3').offset().top;
        noneVisible1 = top >= $('#no-step1').offset().top;
        noneVisible2 = top >=$('#no-step2').offset().top;


if(isVisible1){

    if($('#step1-circle').hasClass('circle-animate')==false){
    $('#step1-circle').toggleClass('circle-animate');
    $('.step-text-one').toggleClass('step-text-animate');
    $('.step-text-two').removeClass('step-text-animate');
    $('.step-text-three').removeClass('step-text-animate');

    $('#step2-circle').removeClass('circle-animate');
    
    $('#step3-circle').removeClass('circle-animate');
    }
}

 if(isVisible2){
    if($('#step2-circle').hasClass('circle-animate')==false){
        $('.step-text-two').toggleClass('step-text-animate');
        $('.step-text-one').removeClass('step-text-animate');
        $('.step-text-three').removeClass('step-text-animate');
    
    $('#step2-circle').toggleClass('circle-animate');
    $('#step1-circle').removeClass('circle-animate');
    $('#step3-circle').removeClass('circle-animate');
    }
}

 if(isVisible3){
    if($('#step3-circle').hasClass('circle-animate')==false){
        $('.step-text-three').toggleClass('step-text-animate');
        $('.step-text-two').removeClass('step-text-animate');
        $('.step-text-one').removeClass('step-text-animate');
    
    $('#step3-circle').toggleClass('circle-animate');
    $('#step1-circle').removeClass('circle-animate');
    $('#step2-circle').removeClass('circle-animate');
    }
}


 });
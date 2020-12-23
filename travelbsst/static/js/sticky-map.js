
var $parent_margin =0;
function sticky_relocate() {
    var window_top = $(window).scrollTop();
    var footer_top = $("#map-stop").offset().top;
    var navbar_height=125;
    var div_top = $('#sticky-anchor').offset().top - navbar_height;
    var div_height = $("#sticky").height();
    var padding = 20; 
    if (window_top + div_height > footer_top - padding){
        $('#sticky').css({top: ((window_top + div_height - footer_top + padding) * -1)})
    }
    else if (window_top > div_top) {
        $('#sticky').addClass('stick');
        $('#sticky').css({top: navbar_height})
        var $width = $('#sticky').parent().width();
        $('#sticky').css({width: $width})
        

    } else {
        $('#sticky').removeClass('stick');
    }
}

$(function () {
 $parent_margin =0-($("#sticky").offset().left);
        // $("#sticky").css('margin-left',$parent_margin +'px');
        // var $width = $('#sticky').parent().width();
        // $('#sticky').css({width: $width-$parent_margin})

    $(window).scroll(sticky_relocate);
    sticky_relocate();
});

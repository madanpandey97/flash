( function( window, $ ){
    "use strict";

    // Mobile Menu
    $('.exc-menu-btn').on('click', function(){
        var $this = $(this),
        isOpened = $this.hasClass('exc-menu-close');

        $('.main-navigation').animate({
            right: isOpened ? "-220px" : "0px"
        }, 500);

        $('body').animate({
            right: isOpened ? "0px" : "220px"
        }, 500);

        $(this).toggleClass('exc-menu-close');
    });

    // Dropdown
    $('li.dropdown.dropdown-custom > a').on('click', function(e) {
        e.preventDefault();

        var self = $( this ),
            li = self.parent();

        $('li.dropdown.dropdown-custom').not( li ).removeClass('open');

        if ( li.hasClass('open') )
        {
            li.removeClass("open");
        } else
        {
            li.addClass("open");
        }
    });

    $('.dropdown-menu li a').on('click', function(){
        console.log("I am here");
    });
    // Camera Slider
    $('#camera_wrap').camera({
        height: '37.5%',
        playPause: false,
        loader: false,
        pagination: false,
        opacityOnGrid: true
    });

    $(".close-collapse").click(function(){
        $(this).parent().removeClass('in');
    });

    // perfectScrollbar
    $('.scroll-block').perfectScrollbar();

     // selectpicker
    $('.selectpicker').selectpicker();

s



})( window, jQuery );
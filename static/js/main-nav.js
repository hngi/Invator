// Nav 
$(function() {
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 10) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });
});

// Collapse the navbar link is clicked 

$('.navbar-nav>li>a').on('click', function() {
    $('.navbar-collapse').collapse('hide');
});



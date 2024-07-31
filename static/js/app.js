"use strict";

// Spinner
setTimeout(function() {
    if ($('#spinner').length > 0) {
        $('#spinner').removeClass('show');
    }
}, 1);

// Sticky Navbar
$(window).scroll(function() {
    try {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    } catch (error) {
        console.error("Error in sticky navbar:", error);
    }
});



// Testimonial carousel
try {
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        dots: true,
        loop: true,
        margin: 25,
        nav: true,
        navText: [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 2
            },
            1200: {
                items: 3
            }
        }
    });
} catch (error) {
    console.error("Error in testimonial carousel:", error);
}

// Back to top button
$(window).scroll(function() {
    try {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    } catch (error) {
        console.error("Error in back to top button:", error);
    }
});

$('.back-to-top').click(function() {
    try {
        $('html, body').animate({
            scrollTop: 0
        }, 1500, 'easeInOutExpo');
        return false;
    } catch (error) {
        console.error("Error in back to top button click:", error);
    }
});

// Carousel control
try {
    $("#carouselId").carousel({ interval: 5000 }); // Set the interval for auto sliding to 5 seconds (5000 milliseconds)

    $(".carousel-control-prev").click(function() {
        $("#carouselId").carousel("prev");
    });

    $(".carousel-control-next").click(function() {
        $("#carouselId").carousel("next");
    });
} catch (error) {
    console.error("Error in carousel initialization:", error);
}


// Initialize Owl Carousel
$('.owl-banner').owlCarousel({
    center: true,
    items: 1,
    loop: true,
    nav: true,
    navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
    margin: 30,
    responsive: {
        992: {
            items: 1
        },
        1200: {
            items: 1
        }
    }
});

// Calendly linking
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('scheduleMeetingButton').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default link behavior
        Calendly.initPopupWidget({
            url: 'https://calendly.com/estheradanma010/prouesse-fashion-meeting',
            color: '#0069ff',
            textColor: '#ffffff',
            branding: false
        });
    });
});
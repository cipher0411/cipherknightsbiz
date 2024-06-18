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



//Testimonial carousel

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


// testimonial
$(document).ready(function() {
    $(".testimonial-carousel").owlCarousel({
        items: 3, // Display three testimonials at a time
        loop: true,
        autoplay: true,
        autoplayTimeout: 5000,
        dots: true,
        nav: true,
        navText: [
            '<i class="fas fa-chevron-left"></i>',
            '<i class="fas fa-chevron-right"></i>'
        ],
    });
});




// Owl Carousel initialization for home video
function playVideo(videoId) {
    var video = document.getElementById(videoId);
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
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

// // Calendly linking
// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById('scheduleMeetingButton').addEventListener('click', function(event) {
//         event.preventDefault(); // Prevent the default link behavior
//         Calendly.initPopupWidget({
//             url: 'https://calendly.com/cipherknights-support/meeting-with-cipherknights',
//             color: '#0069ff',
//             textColor: '#ffffff',
//             branding: false
//         });
//     });
// });



document.addEventListener('DOMContentLoaded', function() {
    var videos = document.querySelectorAll('video');
    videos.forEach(function(video) {
        video.addEventListener('click', function() {
            if (video.paused) {
                video.play();
            } else {
                video.pause();
            }
        });
    });
});
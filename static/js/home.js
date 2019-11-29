

$(document).ready(function () {

    /// wrap inner content of each anchor with first layer and append background layer
    $("#menu1 li a").wrapInner('<span class="out"></span>').append('<span class="bg"></span>');

    // loop each anchor and add copy of text content
    $("#menu1 li a").each(function () {
        $('<span class="over">' + $(this).text() + '</span>').appendTo(this);
    });

    $("#menu1 li a").hover(function () {
        // this function is fired when the mouse is moved over
        $(".out", this).stop().animate({'top': '40px'}, 250); // move down - hide
        $(".over", this).stop().animate({'top': '0px'}, 250); // move down - show
        $(".bg", this).stop().animate({'top': '0px'}, 120); // move down - show

    }, function () {
        // this function is fired when the mouse is moved off
        $(".out", this).stop().animate({'top': '0px'}, 250); // move up - show
        $(".over", this).stop().animate({'top': '-40px'}, 250); // move up - hide
        $(".bg", this).stop().animate({'top': '-40px'}, 120); // move up - hide
    });


    /*	2nd example	*/

    $("#menu2 li a").wrapInner('<span class="out"></span>');

    $("#menu2 li a").each(function () {
        $('<span class="over">' + $(this).text() + '</span>').appendTo(this);
    });

    $("#menu2 li a").hover(function () {
        $(".out", this).stop().animate({'top': '40px'}, 300); // move down - hide
        $(".over", this).stop().animate({'top': '0px'}, 300); // move down - show

    }, function () {
        $(".out", this).stop().animate({'top': '0px'}, 300); // move up - show
        $(".over", this).stop().animate({'top': '-40px'}, 300); // move up - hide
    });

});


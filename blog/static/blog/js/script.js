function toggleScreen(){
    $(".toggle-wrap").click(function(){
        var content_main = $("#content-main");
        if(content_main.hasClass("col-md-9"))
        {
            content_main.removeClass("col-md-9");
            content_main.addClass("col-md-12");
            $("#content-aside").hide();
            $(".toggle-text").text("Half Screen")
        }
        else
        {
            content_main.removeClass("col-md-12");
            content_main.addClass("col-md-9");
            $("#content-aside").show();
            $(".toggle-text").text("Full Screen")
        }
    });
}

function setReadmoreAnimation(){
    $(".more-link span").hide();

    var more_link = $(".more-link");

    more_link.mouseenter(function(){
        $(this).children("span").stop().fadeIn(250);
    });

    more_link.mouseleave(function(){
        $(this).children("span").stop().fadeOut(250);
    });
}

$(document).ready(function(){
    toggleScreen();
    setReadmoreAnimation();
})
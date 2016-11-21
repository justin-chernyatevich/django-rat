$(document).ready(function(){

    var doExpand = function () {
        $(".post-text").toggle();
        $(".expand").children("span").toggleClass("glyphicon-menu-down");
    };

    doExpand();  // Runs when page loaded

    $(".expand").click(function(){  // Runs when user clicked on elem .expand
        doExpand();
    });


});
$(function(){
    $('#good-button').click(function() {
        var numElement = $("#good-num");
        if(!numElement.hasClass("done")){
            var num = numElement.text();
            num = Number(num) + 1;
            numElement.addClass("done");
            var num = numElement.text(num);
        }
    })
})
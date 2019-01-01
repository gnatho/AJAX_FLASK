$(document).ready(function(){

    var currentPage = 1;

    $( "#pageHolder" ).dblclick(function() {
        var audioElement = document.createElement('audio');
        audioElement.setAttribute('src', '/static/54/audio/'+currentPage+'.mp3');
        audioElement.play();


    });

    $("#pageHolder").swipe({
    swipe:function(event, direction, distance, duration, fingerCount) {



        if (direction == "left") {
        currentPage ++;
        $('#testImg').remove();
        $('#pageHolder').append('<img src="/static/54/img/'+currentPage+'.jpg" class="story-img" id="testImg">');

    }


        }
    });
});
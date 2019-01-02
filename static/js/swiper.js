$(document).ready(function(){



    var currentPage = 1;

    $( "#pageHolder" ).dblclick(function() {
        var audioElement = document.createElement('audio');
        audioElement.setAttribute('src', '/static/content/'+id+'/audio/'+currentPage+'.mp3');
        audioElement.play();


    });

    $("#pageHolder").swipe({
    swipe:function(event, direction, distance, duration, fingerCount) {



        if (direction == "left") {
            currentPage ++;
            $('#testImg').remove();
            $('#pageHolder').append('<img src="/static/content/'+id+'/img/'+currentPage+'.jpg" class="story-img" id="testImg">');

        } else if (direction == "right") {

            if (currentPage > 1) {

            currentPage --;
            $('#testImg').remove();
            $('#pageHolder').append('<img src="/static/content/'+id+'/img/'+currentPage+'.jpg" class="story-img" id="testImg">');

            }


        }


        }
    });
});
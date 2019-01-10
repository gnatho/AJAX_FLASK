$(function() {


    $('a#calculate').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });

    $('a#pokaz').bind('click', function() {
        $.getJSON($SCRIPT_ROOT + '/_get_data', function(data, status) {
        $("#wynik").append('<p>'+data.result+'</p>');
      });
      return false;
    });

    $('a#new_page_button').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_balony', {
        city: $('input[name="city"]').val(),
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });

//    $("#testImg").swipe({
//    swipe:function(event, direction, distance, duration, fingerCount) {
//
//    if (direction == "left") {
//        alert(typeof(direction));
//        $('#testImg').remove();
//
//    }







  }
});


});

 $(document).ready(function () {


 $("span").click(function(event) {
    var sracz = '#a'+event.target.id;

    $('#'+event.target.id).css('color', 'blue');
    $(sracz)[0].play();
		$(sracz)[0].onended = function() {
			$('#'+event.target.id).css('color', 'black');
		}

});
});

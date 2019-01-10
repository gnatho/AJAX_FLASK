 $(document).ready(function () {


 $("span").click(function(event) {

    var sracz = '#a'+event.target.id;

    $('#'+event.target.id).css('color', 'blue');
    $(sracz)[0].play();
		$(sracz)[0].onended = function() {
			$('#'+event.target.id).css('color', 'black');
		}

});

$("#audiotester").click(function(event) {

    var _snd = new Audio();
    var source = document.createElement('source');
    source.type = "audio/mpeg";
    source.src = "https://content.raz-kids.com/audio/2581/raz_aesopsfables_lp37_p15_text.mp3";

    _snd.appendChild(source);
    _snd.load(); // Needed on safari / idevice
    _snd.play();

});



});

 $(document).ready(function () {


 $("span").click(function(event) {
    var sracz = '#a'+event.target.id;
    $(sracz)[0].play();


});
});

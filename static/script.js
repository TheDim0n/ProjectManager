$(document).ready(function() {
    var a = window.location.href 
    $('.navbar-nav .nav-link').removeClass('active');
    var b = (a).split("/")[3];
    if(b == "users") b = (a).split("/")[4];
    console.log(b);
    if(b) $("." + b).addClass('active');
    $('.zero-card').hover(
        function(){
          $(this).find(".icons").removeClass("invisible");
        },
        function(){
            $(this).find(".icons").addClass("invisible");
        });

    $('.markdown').keyup(function() {
      var content = $(this).find(".no-markdown").val();
      var markedContent = marked(content);
      $(this).find(".preview-markdown").html(markedContent);
    });
});

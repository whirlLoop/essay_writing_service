$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown(
        {
          'closeOnClick': false
        }
      );
    $('#close').on('click', function () {
      $('.sidenav').sidenav('close');
      $('.hidden').addClass('hidden');
     });
  });

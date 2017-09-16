$(document).ready(function() {
  $('label').click(function() {
    $('label').removeClass('active');
    $(this).addClass('active');
  });
});

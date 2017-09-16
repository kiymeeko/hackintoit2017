jQuery(document).ready(function($){
  $('#goal').on('click', other_function());
  console.log($('#goal').id)
  function other_function() {
    console.log("yes")
  }
  function some_function() {
    $('#Mountain View').style.visibility = "hidden";
  }
});

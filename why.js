function modalCode() {
  //noinspection JSAnnotator
  return  `
  <div class="why_popup_open" style="display: none"></div>
  <div class="why_popup_close" style="display: none"></div>
  <div id="why_popup" class="modal">

<div class="container">
  <form id="whyform">

    <label for="response" id="whyquestion">Why do you want this?</label>
    <textarea name="response" placeholder="I want to purchase these items because..." required></textarea>

    <button class="proceed proceedButton">Proceed To Purchase</button>
  </form>
  <div id="shouldnot" style="display: none">
    <p>According to your past purchases, you may not value this decision in the future.</p>
    <button class="proceedAnyway proceedButton" style="background-color: #af3630;">Proceed To Purchase Anyway</button>
  </div>
  <div id="loader"></div>


</div>

  </div>
`;
}

function modalCss() {
  //noinspection JSAnnotator
  return `input[type=text], select, textarea {
    width: 100%; /* Full width */
    padding: 12px; /* Some padding */
    border: 1px solid #ccc; /* Gray border */
    border-radius: 4px; /* Rounded borders */
    box-sizing: border-box; /* Make sure that padding and width stays in place */
    margin-top: 6px; /* Add a top margin */
    margin-bottom: 16px; /* Bottom margin */
    resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}
#loader {
    border: 16px solid #f3f3f3; /* Light grey */
    border-top: 16px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
/* Style the submit button with a specific background color etc */
.proceedButton {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

#whyquestion {
    font-size: 3em;
    padding: 0 3em 1em 3em;
    margin: auto;

}

/* When moving the mouse over the submit button, add a darker green color */
input[type=submit]:hover {
    background-color: #45a049;
}

/* Add a background color and some padding around the form */
.container {
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
}
`;
}


$('body').append(modalCode());
$('head').append("<style>" + modalCss() + "</style>");

var shouldAllowCheckout = false;
function clickToCheckout() {
  shouldAllowCheckout = true;
  $('.why_popup_close').trigger('click');
  setTimeout(function() {
    $('input[name=proceedToCheckout]').click();
  }, 300);
}

$('#whyform').submit(function () {
  console.log('submitting form');

  let formdata = $(this).serialize();

  $('#whyform').hide();
  $('#loader').show();
  $('#shouldnot').hide();

  chrome.runtime.sendMessage({
    method: 'POST',
    action: 'xhttp',
    url: 'http://localhost:8000/why.php',
    data: formdata
  }, function(responseText) {
    if (responseText == 0) {
      // success!
      clickToCheckout();
    } else {
      $('#whyform').hide();
      $('#loader').hide();
      $('#shouldnot').show();
    }
  });

    return false;
});


$('#why_popup').popup();

$('.proceedAnyway').click(clickToCheckout);

var checkoutButton = 0;


const elementsToRunPopupOn = [
    '.sc-proceed-to-checkout',
    '.ewc-button'
];

const wrapClassName = 'asdfghjklqwertyuiop';


function onCheckout(event) {
    if (shouldAllowCheckout) {
      return;
    }
    event.preventDefault();
  $('#whyform').show();
  $('#shouldnot').hide();
  $('#loader').hide();
    $('.why_popup_open').click();
    checkoutButton = this;
    console.log('running');
}

window.onload = function() {
    for (var i = 0; i < elementsToRunPopupOn.length; i++) {
        $(elementsToRunPopupOn[i]).wrap("<div class='" + wrapClassName + "'></div>");
    }
    $('.' + wrapClassName).click(onCheckout);
};

function fade() {
  document.getElementById("div1").visibility = "hidden";
}

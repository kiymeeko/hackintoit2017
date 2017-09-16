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
    <p>According to your past purchases, this reason is likely to lead to a not-worth purchase.</p>
    <button class="proceedAnyway proceedButton" style="background-color: #af3630;">Proceed To Purchase Anyway</button>
  </div>
  
  
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

function clickToCheckout() {
  $('.why_popup_close').trigger('click');
  setTimeout(function() {
    $('input[name=proceedToCheckout]').click();
  }, 300);
}

$('#whyform').submit(function () {
  console.log('submitting form');

  let formdata = $(this).serialize();

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
      $('#shouldnot').show();
    }
    /*Callback function to deal with the response*/
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
    event.preventDefault();
    $('.why_popup_open').click();
    checkoutButton = this;
    console.log('running');
}

window.onload = function() {
    for (var i = 0; i < elementsToRunPopupOn.length; i++) {
        $(elementsToRunPopupOn[i]).wrap("<div class='" + wrapClassName + "'></div>");
    }
    $('.' + wrapClassName).one('click', onCheckout);
};


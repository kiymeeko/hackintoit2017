function modalCode() {
  return  `
  <div id="my_popup">
    <p>Content!</p>
  </div>
`;
}

$('body').append(modalCode());



const elementsToRunPopupOn = [
    '.sc-proceed-to-checkout'
];

const wrapClassName = 'asdfghjklqwertyuiop';

function onCheckout(event) {
    event.preventDefault();
    $('#my_popup').popup();
    console.log('running');
}

window.onload = function() {
    for (var i = 0; i < elementsToRunPopupOn.length; i++) {
        $(elementsToRunPopupOn[i]).wrap("<div class='" + wrapClassName + " my_popup_open'></div>");
    }
    $('.' + wrapClassName).one('click', onCheckout);
};


const elementsToRunPopupOn = [
    '.sc-proceed-to-checkout'
];

const wrapClassName = 'asdfghjklqwertyuiop';

function onCheckout(event) {
    event.preventDefault();

    console.log('running');
}

window.onload = function() {
    for (var i = 0; i < elementsToRunPopupOn.length; i++) {
        $(elementsToRunPopupOn[i]).wrap("<div class='" + wrapClassName + "'></div>");
    }
    $('.' + wrapClassName).one('click', onCheckout);
};


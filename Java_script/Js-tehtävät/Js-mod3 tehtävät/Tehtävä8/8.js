const button = document.querySelector('#start');
const result = document.querySelector('#result');

button.addEventListener('click', function() {
    const num1 = parseInt(document.querySelector('#num1').value);
    const num2 = parseInt(document.querySelector('#num2').value);
    const operation = document.querySelector('#operation').value;

    let answer;

    switch (operation) {
        case 'add':
            answer = num1 + num2;
            break;
        case 'sub':
            answer = num1 - num2;
            break;
        case 'multi':
            answer = num1 * num2;
            break;
        case 'div':
            answer = num1 / num2;
            break;
    }

    result.innerHTML = answer;
});
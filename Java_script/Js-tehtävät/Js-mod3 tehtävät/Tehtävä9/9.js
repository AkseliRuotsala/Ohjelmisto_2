const button = document.querySelector('#start');
const result = document.querySelector('#result');

button.addEventListener('click', function() {
    const input = document.querySelector('#calculation').value;
    let answer;

    if (input.includes('+')) {
        const numbers = input.split('+');
        answer = parseInt(numbers[0]) + parseInt(numbers[1]);
    } else if (input.includes('-')) {
        const numbers = input.split('-');
        answer = parseInt(numbers[0]) - parseInt(numbers[1]);
    } else if (input.includes('*')) {
        const numbers = input.split('*');
        answer = parseInt(numbers[0]) * parseInt(numbers[1]);
    } else if (input.includes('/')) {
        const numbers = input.split('/');
        answer = parseInt(numbers[0]) / parseInt(numbers[1]);
    }

    result.innerHTML = answer;
});
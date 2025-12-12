

const target = document.querySelector('#target');
const names = ['John', 'Paul', 'Jones'];

let listContent = '';

for (let name of names) {
    listContent += `<li>${name}</li>`;
}

target.innerHTML = listContent;
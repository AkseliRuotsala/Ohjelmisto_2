const target = document.querySelector('#target');

const item1 = document.createElement('li');
item1.textContent = 'First item';
target.appendChild(item1);

const item2 = document.createElement('li');
item2.textContent = 'Second item';
item2.classList.add('my-item');
target.appendChild(item2);

const item3 = document.createElement('li');
item3.textContent = 'Third item';
target.appendChild(item3);
'use strict';

// hae viittaus kaikkiin output class elementteihin taulukkona
const outupElement =
    document.getElementsByClassName('output');

console.log(outupElement);

//viittaus yhteen elementtiin id:n perusteella
const outputElement2 =
    document.getElementById('output');

console.log(outputElement2);

//viittaus kaikkiin p-elementteihin tagin perusteella
const outputElement3 = document.querySelectorAll('p');

console.log(outputElement3);

// viittaus koko body-elementtiin
const body = document.querySelector('body');
body.querySelector ('#output');

//listan (ul) käsittely
const ulElement= document.querySelector('ul');
const newLi = document.createElement('li');
ulElement.appendChild(newLi);
newLi.textContent= 'uusi itemi';


//innerHTML-esimerkkejä
//ulElement.innerHTML = '<li> uusi itemi</li>

//haetaan viittaus kaikkiin li-elementteihin listan sisällä

const liElems = ulElement.querySelectorAll('li');

for (let i= 0; i<liElems.length; i++) {
    liElems[i].textContent=`${i+1}.itemi `;
}
// luodaan html-lista, jossa js-taulukko
const inventory= ['kynä', 'kumi', 'läppäri', 'reppu'];
const inventory0Elem = document.createElement('al');
for (const item of inventory) {
    //luodaan html li-elemntit ja sijoitetaan al-elementti lapseksi
    const liElem = document.createElement('li');
    liElem.textContent=item;
    inventory0Elem.appendChild(liElem);
}
const inventoryHeader=document.createElement('h2');
inventoryHeader.textContent='Inventaario';
body.appendChild(inventoryHeader);
body.appendChild(inventory0Elem);
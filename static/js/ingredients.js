

console.log('Hola mundo');

var i = 0;

function update_ingredients(){
    let ingredient = document.getElementById('ingredient-input');
    i+=1;
    if(!ingredient.value.includes('gr')){
        console.log('invalido');
        ingredient.classList.add('is_invalid');
        return;
    }

    ingredient.classList.remove('is_invalid');

    document.getElementById('ingredients').innerHTML += `
        <li>
            ${ingredient.value}
        </li>
        <input type="hidden" name="ingredient-${i}" value="${ingredient.value}">
    `
    ingredient.value='';
    ingredient.setAttribute('autofocus','true');
};
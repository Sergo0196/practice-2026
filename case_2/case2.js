document.addEventListener('DOMContentLoaded', () => {

const getButtonPlus = document.getElementById('plus');
const getButtonMinus = document.getElementById('minus')
const getSpan = document.getElementById('result');
const attantionId = document.getElementById('attantion');


let count = 0;

function updateCount() {
    getSpan.textContent = count;
    if (count > 0) {
        getSpan.style.background = '#ffff00';
    } else if (count < 0) {
        getSpan.style.background = '#008000'
    } else {
        getSpan.style.background = '#ff0000'
    }
    };

function blocedButton() {
    if(count >= 10) {
        getButtonPlus.disabled = true;
    } else {
        getButtonPlus.disabled = false;
    }  


    if (count <= -10) {
        getButtonMinus.disabled = true;
    }else{
        getButtonMinus.disabled = false;
    }
}

function attantionMessage(){
    if (count >= 10 || count <= -10) {
        attantionId.textContent = 'вы достигли экстремального значения'
    }else{attantionId.textContent = ''}
}

getButtonPlus.addEventListener('click', () => {
    count++;
    updateCount();
    blocedButton();
    attantionMessage()
});

getButtonMinus.addEventListener('click', () => {
    count--;
    updateCount();
    blocedButton();
    attantionMessage()
});

updateCount();
blocedButton();
attantionMessage();

});
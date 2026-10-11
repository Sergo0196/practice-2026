let val1Id = document.getElementById('val1');
let val2Id = document.getElementById('val2');
let plusId = document.getElementById('plus');
let minusId = document.getElementById('minus');
let multId = document.getElementById('mult');
let divisionId = document.getElementById('division');
let resultId = document.getElementById('result');


plusId.addEventListener('click', function() {

    const num1 = parseFloat(val1Id.value);
    const num2 = parseFloat(val2Id.value);

    if (isNaN(num1) || isNaN(num2)) {
        resultId.textContent = "Пожалуйста введите числа";
    } else {
        resultId.textContent = num1 + num2;
    }  
});

minusId.addEventListener('click', function() {

    const num1 = parseFloat(val1Id.value);
    const num2 = parseFloat(val2Id.value);

    if (isNaN(num1) || isNaN(num2)) {
        resultId.textContent = "Пожалуйста введите числа";
    } else {
        resultId.textContent = num1 - num2
    }
});

multId.addEventListener('click', function() {

    const num1 = parseFloat(val1Id.value);
    const num2 = parseFloat(val2Id.value);

    if (isNaN(num1) || isNaN(num2)) {
        resultId.textContent = "Пожалуйста введите числа";
    } else {
        resultId.textContent = num1 * num2
    }
});

divisionId.addEventListener('click', function() {

    const num1 = parseFloat(val1Id.value);
    const num2 = parseFloat(val2Id.value);

    if (isNaN(num1) || isNaN(num2)) {
        resultId.textContent = "Пожалуйста введите числа";
    }
    else if (num2 === 0) {
        resultId.textContent = "На 0 делить нельзя!!!!";
    }else {
        resultId.textContent = num1 / num2
    }
});


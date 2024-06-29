function realizarOperacao(tipoOperacao) {
    const spanResultado = document.querySelector("#resultado");
    const inputNumero1 = document.querySelector("#numero1");
    const inputNumero2 = document.querySelector("#numero2");
    const numero1 = inputNumero1.value;
    const numero2 = inputNumero2.value;
    let resultado = 0;
    if (tipoOperacao == "+") {
        resultado = soma(numero1, numero2);
    }
    else if (tipoOperacao == "-") {
        resultado = subtracao(numero1, numero2);
    }
    else if (tipoOperacao == "*") {
        resultado = multiplicacao(numero1, numero2);
    }
    else if (tipoOperacao == "/") {
        resultado = divisao(numero1, numero2);
    }
    spanResultado.innerHTML = resultado;
}
function soma(numero1, numero2) {
    return parseFloat(numero1) + parseFloat(numero2);
}

function subtracao(numero1, numero2) {
    return numero1 - numero2;
}

function multiplicacao(numero1, numero2) {
    return numero1 * numero2;
}

function divisao(numero1, numero2) {
    if (numero2 == 0) {
        return numero1;
    }
    return numero1 / numero2;
}

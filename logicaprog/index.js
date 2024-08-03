/*
1 - criar uma função para numeros pares printa true e para numeros impares printa false
2 - faça uma função para numeros divisiveis por 2 printa fizz e para numeros divisiveis por 5 printa buzz
 e para numeros que sao divisieveis por 2 e 5 printa fizzbuzz 
*/


function parImpar(n) {
    const resto = n % 2;
    if (resto == 0) {
        console.log("true")
    }
    else {
        console.log("false")
    }


}
 parImpar(10)
 parImpar(11)






function divisao(n) {

     if (n % 2 === 0 && n % 5 === 0) {
        console.log("fizzbuzz");

    }

    else if (n % 2 === 0) {
        
        console.log("fizz");
    }

    else if (n % 5 === 0) {
        console.log("buzz");
    }
}
divisao(4)
divisao(15)
divisao(10)
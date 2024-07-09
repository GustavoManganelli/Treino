const button = document.querySelector('.btn')
const input = document.querySelector('.input')

let minhaLista = []



function addTarefa() {
    minhaLista.push(input.value)
    console.log(minhaLista)
}

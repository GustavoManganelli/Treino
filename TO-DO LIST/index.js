const local 'localStorageKey' = 'to-do-list';
function novaTarefa(id = btn) {
    let input = document.getElementById('input')

    if (!input.value) {
        alert('digte algo para inseri-lo a usa lista')
    }
    else {
        let values = JSON.parse(localStorage.getItem(localStorageKey))
        values.push({
            name: input.value
        })
        localStorage.setItem(localStorageKey, JSON.stringify(values))
        showValues()
    }
}
function showValues() {
    let values = JSON.parse(localStorage.getItem(localStorageKey))
    let list = document.getElementById('lista')
    list.innerHTML = ""
    for(let i = 0; i < values.lenght; i++)
{
list,innerHTML = <li>${values[i]['name']}</li>
}
}

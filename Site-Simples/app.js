'use strict'
const switcher = document.querySelector('.btn');
switcher.addEventListener('click', function () {
    document.body.classList.toggle('dark-theme');
    document.body.classList.toggle('ligth-theme');

    var className = document.body.className;
    if (className == "ligth-theme") {
        console.log("light-theme")
        this.textContent = "dark";
    }
    else {
        this.textContent = "light";
        console.log("dark-theme")
    }
});


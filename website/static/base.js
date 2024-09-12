let menu = document.querySelector(".nav-hamburguer")
console.log(menu)

let menuOpen = document.querySelector(".nav-hamburguer-open")
console.log(menuOpen)

menu.addEventListener("click", function(){ 
    console.log("hamburguer ativo")
    menuOpen.classList.toggle("active")
    menu.classList.toggle("active")
})

let closeMessageButton = document.querySelector(".close")
console.log(closeMessageButton)

let flashMessageDiv = document.querySelector(".flash")
console.log(flashMessageDiv)

closeMessageButton.addEventListener("click", function(){
    console.log("closemessagebutton ativado")
    flashMessageDiv.classList.toggle("active")
})
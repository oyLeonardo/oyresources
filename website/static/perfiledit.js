
let buttonCancelar = document.querySelector(".button-cancelar")
console.log("button-cancelar")
let perfilInfo = document.querySelector(".perfil-info")
console.log(perfilInfo)
let perfilEditButton = document.getElementById("perfil-edit-button")
console.log(perfilEditButton)

perfilEditButton.addEventListener("click", function(){
    console.log("botao editar perfil ativo")
    perfilInfo.classList.toggle("active")
})

buttonCancelar.addEventListener("click", function(){ 
    console.log("cancelar ativo")
    perfilInfo.classList.toggle("active")
})


function deletarUser(userId) {
    fetch("/deleteuser",{
        method: "POST",
        body: JSON.stringify({userId:userId})
    }).then((_res) => {
        window.location.href = "/db";
    });
}                    

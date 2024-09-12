let buttonDelete = document.querySelectorAll(".popup-button-delete")

console.log(buttonDelete,"delete")

let confirmButtonsDiv = document.querySelectorAll(".action-container-confirmbuttons")

let buttonCancel = document.querySelectorAll(".popup-button-cancel")
console.log(buttonCancel,"cancel")

let buttonConfirm = document.querySelectorAll(".popup-button-confirm")

let buttonEdit = document.querySelectorAll(".popup-button-edit")

for (let i=0; i<buttonDelete.length ; i++){
    buttonDelete[i].addEventListener("click", function(){
        console.log(confirmButtonsDiv,"confirmaction")
        confirmButtonsDiv[i].classList.toggle("active")  
        buttonDelete[i].classList.toggle("active")
        buttonConfirm[i].classList.toggle("active")
        buttonEdit[i].classList.toggle("active")
    })
    buttonCancel[i].addEventListener("click", function() {
        console.log(buttonCancel, "cancel");
        confirmButtonsDiv[i].classList.toggle("active");
        buttonDelete[i].classList.toggle("active");
        buttonConfirm[i].classList.toggle("active")
        buttonEdit[i].classList.toggle("active")
    });
}
function deletarUser(userId) {
    fetch("/deleteuser",{
        method: "POST",
        body: JSON.stringify({userId:userId})
    }).then((_res) => {
        window.location.href = "/db";
    });
}

function deletarPost(postId) {
    fetch("/deletepost", {
        method: "POST",
        body: JSON.stringify({postId:postId})
        
    }).then((_res) => {
        window.location.href = "/db"
    });
}


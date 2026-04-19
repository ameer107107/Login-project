const container = document.querySelector(".container")
    PwShowHide = document.querySelectorAll(".ShowHidePw")
    PwFields =document.querySelectorAll(".password")

    PwShowHide.forEach(eyeIcon => {
        eyeIcon.addEventListener("click",()=>{
            PwFields.forEach(PwFields => {
                if (PwFields.type === "password" ){
                    PwFields.type = "text";
                    PwShowHide.forEach(icon => {
                        icon.classList.replace("uil-eye-slash","uil-eye")
                    })

                }else{
                    PwFields.type = "password"
                     PwShowHide.forEach(icon => {
                        icon.classList.replace("uil-eye","uil-eye-slash")
                    })
                }
            })
        })
    });
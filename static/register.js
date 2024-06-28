const form = document.querySelector("form")
const error1 = document.querySelector(".error1")
const error4 = document.querySelector(".error4")
const error5 = document.querySelector(".error5")
const username = document.querySelector(".username")
const password = document.querySelector(".password")
const repeat = document.querySelector(".repeat")

const usernamePattern = /^[a-zA-Z]$/
const passwordPattern = /^(?=.*[0-9])(?=.*[a-zA-Z]).{8,20}$/



form.addEventListener('submit', async (e) => {
    try{
        e.preventDefault()
        
        const passwordPattern = /^[a-zA-Z0-9!@#$%^&*]{6,}$/;
        const usernamePattern = /^[a-zA-Z]+$/;

        error1.textContent = "";
        error4.textContent = "";
        error5.textContent = "";


        if (username.value.trim() === "") {
            error1.textContent = "Type Username";
        } else if (!usernamePattern.test(username.value)) {
            error1.textContent = "Username is invalid";
        } else if (username.value.length > 30) {
            error1.textContent = "Too long";
        } else if (username.value.length < 3) {
            error1.textContent = "Too Short";
        }

        if (password.value.trim() === "") {
            error4.textContent = "Type password";
        } else if (!passwordPattern.test(password.value)) {
            error4.textContent = "Password is invalid";
        } else if (password.value.length > 20) {
            error4.textContent = "Too long";
        } else if (password.value.length < 6) {
            error4.textContent = "Too Short";
        }

        if (repeat.value.trim() === "") {
            error5.textContent = "Type password";
        } else if (repeat.value !== password.value) {
            error5.textContent = "Password does not match";
        }

        function setma(){
            setTimeout(() => {
                error5.textContent = ""
                error4.textContent = ""
                error1.textContent = ""
            }, 2000)
        }

        setma()




    }catch(err){
        console.log(err)
    }
})
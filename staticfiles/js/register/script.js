let usernameMessage = document.querySelector('.username-validation')
let nameMessage = document.querySelector('.name-validation')
let passwordMessage = document.querySelector('.password-validation')

let usernameInput = document.querySelector('.username')
let nameInput = document.querySelector('.name')
let passwordInput = document.querySelector('.password')

function nameValidation () {
    // alert('name')
    if (nameInput.value.length < 10) {
        nameMessage.style.color = 'red'
        nameMessage.innerHTML = 'Must Contain 10 Character (Min)'
        nameMessage.style.display = 'block'
    } else {
        nameMessage.style.color = 'green'
        nameMessage.innerHTML = 'Correct name Value'
    }
}

function usernameValidation () {
    // alert('username')
    if (usernameInput.value.length < 12) {
        usernameMessage.style.color = 'red'
        usernameMessage.innerHTML = 'Must Contain 12 Character (Min)'
        usernameMessage.style.display = 'block'
    } else {
        usernameMessage.style.color = 'green'
        usernameMessage.innerHTML = 'Correct Username Value'
    }
}

function passwordValidation () {
    // alert('Password')
    if (passwordInput.value.length < 8) {
        passwordMessage.style.color = 'red'
        passwordMessage.innerHTML = 'Must Contain 8 Character (Min)'
        passwordMessage.style.display = 'block'
    } else {
        passwordMessage.style.color = 'green'
        passwordMessage.innerHTML = 'Correct Password Value'
    }
    
}
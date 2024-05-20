function validateForm() {
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');
    
    if (username.value === '') {
        usernameError.classList.remove('hidden');
    } else {
        usernameError.classList.add('hidden');
    }

    if (password.value === '') {
        passwordError.classList.remove('hidden');
    } else {
        passwordError.classList.add('hidden');
    }
}

console.log("Forms with Validation Example Loaded");
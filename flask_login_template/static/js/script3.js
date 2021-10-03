const regButton = document.getElementById('reg');
const signIn = document.getElementById('signin');
const signUp = document.getElementById('signup');

regButton.addEventListener('click', () => {
    signIn.style.display = "none";
    signUp.style.display = "flex";
    
});
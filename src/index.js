const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', ()=> {
	wrapper.classList.add('active');
});

let fullscreen;
let fsEnter = document.getElementById('fullscr');
fsEnter.addEventListener('click', function (e) {
    e.preventDefault();
    if (!fullscreen) {
        fullscreen = true;
        document.documentElement.requestFullscreen();
        fsEnter.innerHTML = "Exit Fullscreen";
    }
    else {
        fullscreen = false;
        document.exitFullscreen();
        fsEnter.innerHTML = "Go Fullscreen";
    }
});

loginLink.addEventListener('click', ()=> {
	wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
	wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=> {
	wrapper.classList.remove('active-popup');
});

const loginForm = document.querySelector('#login-form');
loginForm.addEventListener('submit', function(event) {
  event.preventDefault(); // prevent the form from submitting

  // Get the email and password values from the form inputs
  const emailInput = loginForm.querySelector('#email-input');
  const passwordInput = loginForm.querySelector('#password-input');
  const email = emailInput.value;
  const password = passwordInput.value;

  // Check if the email and password are correct
  if (email === 'Admin@gmail.com' && password === 'Admin@123') {
    // Redirect to the main.html page
    window.location.href = 'Loader.html';
  } else {
    // Display an error message
    alert('Invalid email or password. Please try again.');
  }
});



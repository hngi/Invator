const email = document.getElementById('email');
const password = document.getElementById('password');
const navBtn = document.getElementById('nav-btn');
const navBar = document.querySelector('.nav');


const darkMode = () => {
  document.body.classList.toggle('dark');
  navBar.classList.toggle('dark');
 
  navBtn.classList.toggle('dark')
  
};

navBtn.addEventListener('click', darkMode);
const formSubmit = (e) => {
  e.preventDefault();
  if (email.value == '') {
    email.style.borderColor = 'red';
    email.style.backgroundColor = 'transparent';
  } else {
    email.style.borderColor = 'green';
  }
  if (password.value == '') {
    password.style.borderColor = 'red';
    password.style.backgroundColor = 'transparent';
  } else {
    password.style.borderColor = 'green';
  }
};

// form.addEventListener('submit', formSubmit);

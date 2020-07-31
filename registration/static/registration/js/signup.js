const email = document.getElementById('email');
const name = document.getElementById('name');
const userName = document.getElementById('username');
const passwordOne = document.getElementById('password1');
const passwordTwo = document.getElementById('password2');
const job = document.getElementById('job');
const navBtn = document.getElementById('nav-btn');
const navBar = document.querySelector('.nav');


const darkMode = () => {
  document.body.classList.toggle('dark');
  navBar.classList.toggle('dark');
   
};


const formSubmit = (e) => {
  e.preventDefault();
  
  if (userName.value == ''){
    userName.style.borderColor = 'red';
    userName.style.backgroundColor = 'transparent';
  }
  else {
    userName.style.borderColor = 'green';
    
  }

  if (email.value == ''){
    email.style.borderColor = 'red';
    email.style.backgroundColor = 'transparent';
  }
  else {
    email.style.borderColor = 'green';
    
  }
  
  if (passwordOne.value == ''){
    passwordOne.style.borderColor = 'red';
    passwordOne.style.backgroundColor = 'transparent';
  }
  
  else {
    passwordOne.style.borderColor = 'green';
    
  }
  
  if (passwordTwo.value == ''){
    passwordTwo.style.borderColor = 'red';
    passwordTwo.style.backgroundColor = 'transparent';
  }
  else {
    passwordTwo.style.borderColor = 'green';
   
  }
  
  if (name.value == ''){
    name.style.borderColor = 'red';
    name.style.backgroundColor = 'transparent';
  }

  else {
    name.style.borderColor = 'green';
    
  }
  
  if (job.value == ''){
    job.style.borderColor = 'red';
    job.style.backgroundColor = 'transparent';
  }
  else {
    job.style.borderColor = 'green';
    
  }
};

navBtn.addEventListener('click', darkMode);
// form.addEventListener('submit', formSubmit);





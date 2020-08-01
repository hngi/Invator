/* const options = {
    bottom: '32px', // default: '32px'
    right: '32px', // default: '32px'
    left: 'unset', // default: 'unset'
    time: '0.3s', // default: '0.3s'
    mixColor: '#fff', // default: '#fff'
    backgroundColor: '#fff',  // default: '#fff'
    buttonColorDark: '#100f2c',  // default: '#100f2c'
    buttonColorLight: '#fff', // default: '#fff'
    saveInCookies: false, // default: true,
    label: '🌓', // default: ''
    autoMatchOsTheme: true, // default: true
}

const darkmode = new Darkmode(options);

darkmode.showWidget();
 */

/*  const checkbox = document.querySelector('input[name=theme]');

 checkbox.addEventListener('change', function() {
     if(this.checked) {
        trans()
        document.documentElement.setAttribute('data-theme', 'dark')
     } else {
         trans()
         document.documentElement.setAttribute('data-theme', 'light')
     }
 })
 const trans = () => {
     document.documentElement.classList.add('transition');
     window.setTimeout(() {
         document.documentElement.classList.remove('transition');
     }, 1000)
 } */

 $(document).ready(function(){
    $('.color-changer').on('click', function(){
        $('body').toggleClass("switch")
    })
})
$(document).ready(function(){
    $('.color-changer').on('click', function(){
        $('nav ul li a').toggleClass("switch")
    })
})
$(document).ready(function(){
    $('.color-changer').on('click', function(){
        $('.color-changer').toggleClass("switch")
    })
})
$(document).ready(function(){
    $('.color-changer').on('click', function(){
        $('.card-body').toggleClass("switch")
    })
})
$(document).ready(function(){
    $('.color-changer').on('click', function(){
        $('.burger span').toggleClass("switch")
    })
})

let changeColor =  document.querySelector('.color-changer')
let body =  document.querySelector('body')

changeColor.addEventListener('click',() => {
    if(body.className == ""){
        changeColor.innerHTML = "Light"
    }
    else{
        changeColor.innerHTML = "Dark"
    }
})
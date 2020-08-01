const navToggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.links');
const linksContainer = document.querySelector('.links-container')

const date = document.querySelector(".date");
date.innerHTML = new Date().getFullYear();

navToggle.addEventListener('click', function(){
    linksContainer.classList.toggle('show-links');
    navToggle.classList.toggle('show-icon')
})

// boostrap modal
$('#myModal').on('shown.bs.modal', function () {
	$('#myInput').trigger('focus')
  })
// toggling the invoice
  $("#toggleButton").click(function(){
    $("#invoice").toggle();
  });


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
        $('.nav-toggle span').toggleClass("switch")
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



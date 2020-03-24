$(document).ready(function(){

$('#button').on('click', function(){
	alert('Hello, it is jQuery');
});

$('.header__burger').click(function(event){
	$('.header__burger,.header__menu').toggleClass('active');
	$('body').toggleClass('lock');
});

});

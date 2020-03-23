// Reading
		var modal = document.getElementById("MyModel_Reading");
		var btn = document.getElementById("myBtn_Reading"); 
		var span = document.getElementsByClassName("close")[0];

		btn.onclick = function () {
			modal.style.display = "block";		
		}	
		span.onclick = function () {
			modal.style.display = "none";
		}
		window.onckick = function (event) {
			if (event.target == modal) {
				modal.style.display = "none";
			}
		}



// SWEET ALERT



// var = atert_sweet_1 = document.getElementById("atert_sweet_1");

// atert_sweet_1.addEventListener('click', function() {
// 	swal("Here's the title!", "...and here's the text!");	
// });


















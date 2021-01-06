/*
===================
INDEX FUNCTIONS
templates/index.html
===================
*/


/*
Sends subject matter to server as POST request using ajax
*/
function sendSubjectMatter(){
	var subject_matter = '';
	var chosenSM = document.getElementById("first_select").value;
	subject_matter = chosenSM.substring(3, chosenSM.length);
	$.ajax({
		type: "POST",
		contentType: "application/json",
		url: "../",
		traditional: "true",
		data: JSON.stringify(subject_matter),
		dataType: "json"
	});
}


/*
Sends confirmation value to server as POST request using ajax to run py file (splitting video to frames)
*/
function sendV2FConfirmation(){
	var submit = document.getElementById("vidFile").value;
	var confirmation = 0;
	if(submit != ""){
		confirmation = 1;
	}

	$.ajax({
		type: "POST",
		contentType: "application/json",
		url: "../",
		traditional: "true",
		data: JSON.stringify(confirmation),
		dataType: "json"
	});

}
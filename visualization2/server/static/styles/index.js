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
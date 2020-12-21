
/*
INDEX FUNCTIONS
*/

function changeSelection(){
	var value = document.getElementById("first_select").value;
	return value;
}

function updatesVidToFrame(){

	var selection = changeSelection();
	var option = Number(document.getElementById(selection).innerHTML);

	option+=1;

	document.getElementById(selection).innerHTML = option;
}
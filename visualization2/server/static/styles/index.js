/*
INDEX FUNCTIONS
*/

 function changeSelection(){
 	var value = document.getElementById("first_select").value;
 	return value;
 }

 function updatesVidToFrame(){


/*
	var correctNumDog = data["Step_1"]["numDog"];
	var correctNumCar = data["Step_1"]["numCar"];
	var correctNumPlane = data["Step_1"]["numPlane"];


	document.getElementById("numDog").innerHTML = correctNumDog;
	document.getElementById("numCar").innerHTML = correctNumCar;
	document.getElementById("numPlane").innerHTML = correctNumPlane;
*/
	
	var selection = changeSelection();
	var option = Number(document.getElementById(selection).innerHTML);

	option+=1;

	document.getElementById(selection).innerHTML = option;
}
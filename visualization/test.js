const fs = require("fs");


function updatesVidToFrame(){
	let rawdata = fs.readFileSync('./json/data.json');
	let data = JSON.parse(rawdata);
	//console.log(data);

	var correctNumDog = data["Step_1"]["numDog"];
	var correctNumCar = data["Step_1"]["numCar"];
	var correctNumPlane = data["Step_1"]["numPlane"];

	console.log(correctNumDog, correctNumCar, correctNumPlane);
}

updatesVidToFrame();
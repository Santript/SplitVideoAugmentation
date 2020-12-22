var fs = require("fs");
/*
INDEX FUNCTIONS
*/

function changeSelection(){
	var value = document.getElementById("first_select").value;
	return value;
}

function updatesVidToFrame(){

	fs.readFile("/json/data.json", function(err, content) {
		if(err){
			return;
		}
		var json_data = JSON.parse(content);
		console.log(json_data);
	});

	/*
	var selection = changeSelection();
	var option = Number(document.getElementById(selection).innerHTML);

	option+=1;

	document.getElementById(selection).innerHTML = option;
	*/
}
/*
INDEX FUNCTIONS
*/

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

function loadJSON(callback){
	var xobj = new XMLHttpRequest();
	        xobj.overrideMimeType("application/json");
	xobj.open('GET', '../json/data.json', true);
	xobj.onreadystatechange = function () {
	          if (xobj.readyState == 4 && xobj.status == "200") {
	            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
	            callback(xobj.responseText);
	          }
	    };
	xobj.send(null);
}

function changeSelection(){
 	loadJSON(function(response){ 
 		var data = JSON.parse(response);
	})
	console.log(data);
}

changeSelection();

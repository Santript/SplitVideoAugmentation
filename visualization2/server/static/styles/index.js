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

function checkAugmentation(){

	var grayScaleChecked = document.getElementById("makeGrayScale").checked;
	var embossChecked = document.getElementById("addEmboss").checked;
	var edgeEnhanceChecked = document.getElementById("addEdgeEnhance").checked;
	var extraEdgeEnhanceChecked = document.getElementById("addExtraEdgeEnhance").checked;
	var rgbToHSVChecked = document.getElementById("convertRGBToHSV").checked;
	var flipImgChecked = document.getElementById("flipImg").checked;
	var mirrorImgChecked = document.getElementById("mirrorImg").checked;
	var xShearImgChecked = document.getElementById("xShearImg").checked;
	var yShearImgChecked = document.getElementById("yShearImg").checked;

	console.log(JSON.stringify(augmentationMap));

	$.ajax({
		type: "POST",
		url: "../",
		traditional: "true",
		contentType: "application/json",
		data: {
			"makeGrayScale": grayScaleChecked,
			"addEmboss": embossChecked,
			"addEdgeEnhance": edgeEnhanceChecked,
			"addExtraEdgeEnhance": extraEdgeEnhanceChecked,
			"convertRGBToHSV" : rgbToHSVChecked,
			"flipImg": flipImgChecked,
			"mirrorImg": mirrorImgChecked,
			"xShearImg": xShearImgChecked,
			"yShearImg": yShearImgChecked
		},
		dataType: "json"
	});
}

function showAugmentationMethods(){
	var grayScaleChecked = document.getElementById("makeGrayScale").checked;
	var embossChecked = document.getElementById("addEmboss").checked;
	var edgeEnhanceChecked = document.getElementById("addEdgeEnhance").checked;
	var extraEdgeEnhanceChecked = document.getElementById("addExtraEdgeEnhance").checked;
	var rgbToHSVChecked = document.getElementById("convertRGBToHSV").checked;
	var flipImgChecked = document.getElementById("flipImg").checked;
	var mirrorImgChecked = document.getElementById("mirrorImg").checked;
	var xShearImgChecked = document.getElementById("xShearImg").checked;
	var yShearImgChecked = document.getElementById("yShearImg").checked;

	if(grayScaleChecked === true){
		document.getElementById("showGrayScale").innerHTML = "Make Gray Scale";
	}
	if(embossChecked === true){
		document.getElementById("showEmboss").innerHTML = "Emboss Data";
	}
	if(edgeEnhanceChecked === true){
		document.getElementById("showEdgeEnhance").innerHTML = "Add Edge Enhancement";
	}
	if(extraEdgeEnhanceChecked === true){
		document.getElementById("showExtraEdgeEnhance").innerHTML = "Add Extra Edge Enhancement";
	}
	if(rgbToHSVChecked === true){
		document.getElementById("showRGBToHSV").innerHTML = "Convert to HSV";
	}
	if(flipImgChecked === true){
		document.getElementById("showFlipImg").innerHTML = "Flip Image";
	}
	if(mirrorImgChecked === true){
		document.getElementById("showMirrorImg").innerHTML = "Mirror Image";
	}
	if(xShearImgChecked === true){
		document.getElementById("showXShear").innerHTML = "Apply X-Axis Shear";
	}
	if(yShearImgChecked === true){
		document.getElementById("showYShear").innerHTML = "Apply Y-Axis Shear";
	}
}

function showAugmentation(){
	var augmentationDiv = document.getElementById("postAugmentation");
	augmentationDiv.style.display = "block";
}
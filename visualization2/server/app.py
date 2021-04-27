from flask import *
from preprocessing import removeSomeFrames
from augmentation import fullAugmentationProcess

import os
import json
import log
import downloadZip
import pathlib
import zipfile

app = Flask(__name__)
application = app


#opening json file and reading content
with open("static/json/step_1.json", "r") as read_file:
	crucialData = json.load(read_file)
	subject_matter = crucialData["step_1"]["subject_matter"]
	numDog = crucialData["step_1"]["numDog"]
	numCar = crucialData["step_1"]["numCar"]
	numPlane = crucialData["step_1"]["numPlane"]

	read_file.close()


#directory where all videos will be uploaded into
app.config["VIDEO_UPLOADS"] = "uploads/"

#setting methods for post or get requests and setting route
@app.route("/videotoframes", methods=["GET", "POST"])


#Calls all other side functions to complete all the processes (video splitting, augmentation, etc.)
#@return html page and necessary variables to complete the page

def allProcesses():
	
	#calling other necessary functions
	updateSubjectMatter()
	uploadVideoFileAndRun()
	updateSubjectMatterJson()
	removeCloseFrames()

	#writing to json file
	#with open("static/json/data.json", "w") as read_file:
	#	json.dump(crucialData, read_file)
	#	read_file.close()

	temp_data = {
		'numberDog': numDog,
		'numberCar': numCar,
		'numberPlane': numPlane
	}

	#allowing html page to render from app		
	return render_template("videoToFrames.html", **temp_data)



#Receives post request from client side to update subject_matter variable in json file and updates json

def updateSubjectMatter():

	#checking if POST request was received
	if request.method == 'POST':
		#getting the json object from client-side
		sm = request.get_json()

		#checking if object is of none_type
		#If it is, then the json file won't be updated
		if sm != None and isinstance(sm, str) == True and len(sm.split()) == 1:
			crucialData["step_1"]["subject_matter"] = sm

	with open("static/json/step_1.json", "w") as write_file:
		json.dump(crucialData, write_file)
		write_file.close()
	#else:
		#print("err updating subject matter")



#Saves the uploaded video file into uploads directory and changes the json variable called "vid_file"

def uploadVideoFileAndRun():

	#checking if POST request was received
	if request.method == 'POST':
		if request.files:
			#print(request.files["vidFile"])
			video = request.files["vidFile"]
			#changing json object variable
			crucialData["step_1"]["vid_file"] = video.filename
			#saving video in directory
			if video.filename != "":
				video.save(os.path.join(app.config["VIDEO_UPLOADS"], video.filename))
				with open("static/json/step_1.json", "w") as read_file:
					json.dump(crucialData, read_file)
					read_file.close()

				#opening videoToFrames.py and reading it
				v2fFile = open(r'videoToFrames.py', 'r').read()
				#executing py script
				log.LOG_INFO("Splitting video into frames-----------------------------------------")
				return exec(v2fFile)

		else:
			log.LOG_INFO("unable to save video and execute py script")

		#checking if POST request was received
		


#reads json file that videoToFrames.py file writes to and changes the value in the main json file

def updateSubjectMatterJson():

	#opening the secondary json file and reading it
	with open("static/json/video2Frames.json", "r") as read_file:
		vid2FramesData = json.load(read_file)
		read_file.close()

	#setting main json file variables equal to the same variable in the secondary json file
	crucialData["step_1"]["numDog"] = vid2FramesData["numDog"]
	crucialData["step_1"]["numCar"] = vid2FramesData["numCar"]
	crucialData["step_1"]["numPlane"] = vid2FramesData["numPlane"]

	with open("static/json/step_1.json", "w") as write_file:
		json.dump(crucialData, write_file)
		write_file.close()


def removeCloseFrames():
	if request.method == "POST":
		removeFramesConfirmation = request.get_json()

		if removeFramesConfirmation == "Remove Frames":
			log.LOG_INFO("removing frames------------------------------------------------------")
			removeSomeFrames.removeFrames()


#receives confirmation POST request from js file and then runs videoToFrames.py, which generates all the frames and places them in dataset directory


with open("static/json/step_2.json", "r") as read_file:
	augmentationData = json.load(read_file)
	read_file.close()

#changes url root to /augmentation, which is the second step of the process
@app.route("/augmentation", methods=["GET", "POST"])
	

#main method of the augmentation phase

def index():
	temp_data = {
		'numberDog': numDog,
		'numberCar': numCar,
		'numberPlane': numPlane
	}

	changeAugmentationMethods()

	if request.method == "POST":
		return redirect(url_for('allProcesses'))

	return render_template("augmentation.html", **temp_data)


#gets the post request from user regarding augmentation methods they selected and this is updated in the json file

def changeAugmentationMethods():

	if request.method == "POST":
		augmentationMethods = request.get_json()
		
		augmentationData["step_2"]["makeGrayScale"] = augmentationMethods["makeGrayScale"]
		augmentationData["step_2"]["addEmboss"] = augmentationMethods["addEmboss"]
		augmentationData["step_2"]["addEdgeEnhance"] = augmentationMethods["addEdgeEnhance"]
		augmentationData["step_2"]["addExtraEdgeEnhance"] = augmentationMethods["addExtraEdgeEnhance"]
		augmentationData["step_2"]["convertRGBToHSV"] = augmentationMethods["convertRGBToHSV"]
		augmentationData["step_2"]["flipImg"] = augmentationMethods["flipImg"]
		augmentationData["step_2"]["mirrorImg"] = augmentationMethods["mirrorImg"]
		augmentationData["step_2"]["xShearImg"] = augmentationMethods["xShearImg"]
		augmentationData["step_2"]["yShearImg"] = augmentationMethods["yShearImg"]

		with open("static/json/step_2.json", "w") as write_file:
			json.dump(augmentationData, write_file)
			write_file.close()
		with open("static/json/step_2.json", "r") as read_file:
			data = json.load(read_file)
			read_file.close()

		fullAugmentationProcess.runAugmentationMethods(data)


@app.route("/preprocess", methods=["GET", "POST"])

def allPreprocess():
	createZip()

	temp_data = {
		'numberDog': numDog,
		'numberCar': numCar,
		'numberPlane': numPlane
	}

	#if request.method == "POST":
	#	return redirect(url_for('index'))

	return render_template("preprocess.html", **temp_data)

#creates the zipfile from the augmentedDataset directory
def createZip():
	zipFile = pathlib.Path("test.zip")
	if zipFile.exists():
		log.LOG_INFO("Zipfile Exists")
	else:
		if request.method == "POST":
			zipFileConf = request.get_json()
			if zipFileConf == "Create Zipfile":
				log.LOG_INFO("Zipping Dataset")
				downloadZip.zipDirectory('augmentedDataset/')
				log.LOG_INFO("zipfile generated successfully")

				#return send_file('dataset.zip', mimetype='application/zip', as_attachment=True, attachment_filename='dataset.zip')

@app.route("/downloadZip/")

#Sending zipfile of dataset to user
def download_file():
	filename = 'dataset.zip'
	log.LOG_INFO("Sending zip file")
	return send_file(filename, as_attachment=True)

#Running flask app on localhost 5000

if __name__ == '__main__':
	app.run(debug=True, threaded=True)

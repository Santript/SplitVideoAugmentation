from flask import *
import os
import json

app = Flask(__name__)
application = app


#opening json file and reading content
with open("static/json/data.json", "r") as read_file:
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
	#print(crucialData)

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
		if sm != None and isinstance(sm, str) == True:
			crucialData["step_1"]["subject_matter"] = sm
		#print(sm)
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
			video.save(os.path.join(app.config["VIDEO_UPLOADS"], video.filename))
			with open("static/json/data.json", "w") as read_file:
				json.dump(crucialData, read_file)
				read_file.close()

			#opening videoToFrames.py and reading it
			v2fFile = open(r'videoToFrames.py', 'r').read()
			#executing py script
			return exec(v2fFile)

		else:
			print("unable to save video and execute py script")

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


#receives confirmation POST request from js file and then runs videoToFrames.py, which generates all the frames and places them in dataset directory


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
		
		crucialData["step_2"]["makeGrayScale"] = augmentationMethods["makeGrayScale"]
		crucialData["step_2"]["addEmboss"] = augmentationMethods["addEmboss"]
		crucialData["step_2"]["addEdgeEnhance"] = augmentationMethods["addEdgeEnhance"]
		crucialData["step_2"]["addExtraEdgeEnhance"] = augmentationMethods["addExtraEdgeEnhance"]
		crucialData["step_2"]["convertRGBToHSV"] = augmentationMethods["convertRGBToHSV"]
		crucialData["step_2"]["flipImg"] = augmentationMethods["flipImg"]
		crucialData["step_2"]["mirrorImg"] = augmentationMethods["mirrorImg"]
		crucialData["step_2"]["xShearImg"] = augmentationMethods["xShearImg"]
		crucialData["step_2"]["yShearImg"] = augmentationMethods["yShearImg"]

		with open("static/json/data.json", "w") as write_file:
			json.dump(crucialData, write_file)
			write_file.close()


#Running flask app on localhost 5000

if __name__ == '__main__':
	app.run(debug=True, threaded=True)

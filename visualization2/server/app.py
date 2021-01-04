from flask import *
import os
import json

app = Flask(__name__)


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
@app.route("/", methods=["GET", "POST"])



#Calls all other side functions to complete all the processes (video splitting, augentation, etc.)
#@return html page and necessary variables to complete the page

def allProcesses():
	#calling other necessary functions
	updateSubjectMatter()
	uploadVideoFile()
	#print(crucialData)

	#writing to json file
	with open("static/json/data.json", "w") as read_file:
		json.dump(crucialData, read_file)
		read_file.close()

	#allowing html page to render from app		
	return render_template("index.html", numberDog=numDog, numberCar=numCar, numberPlane=numPlane)



#Receives post request from client side to update subject_matter variable in json file and updates json

def updateSubjectMatter():
	if request.method == 'POST':
		#getting the json object from client-side
		sm = request.get_json()

		#checking if object is of none_type
		#If it is, then the json file won't be updated
		if sm != None:
			crucialData["step_1"]["subject_matter"] = sm
		#print(sm)
	else:
		print("err updating subject matter")



#Saves the uploaded video file into uploads directory and changes the json variable called "vid_file"

def uploadVideoFile():
	if request.method == 'POST':
		if request.files:
			#print(request.files["vidFile"])
			video = request.files["vidFile"]
			#changing json object variable
			crucialData["step_1"]["vid_file"] = video.filename
			#saving video in directory
			video.save(os.path.join(app.config["VIDEO_UPLOADS"], video.filename))
		else:
			print("unable to save video")



#Running flask app on localhost 5000

if __name__ == '__main__':
	app.run(debug=True)
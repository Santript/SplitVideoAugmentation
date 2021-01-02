from flask import *
import os
import json

app = Flask(__name__)


#opening json file and reading content
with open("json/data.json", "r") as read_file:
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


def allProcesses():

	#requesting video file that is uploaded and saving it to uploads directory (using POST request for security)
	if request.method == "POST":
		if request.files:
			video = request.files["vidFile"]
			#changing json object variable
			crucialData["step_1"]["vid_file"] = video.filename
			print(numPlane)
			#saving video in directory
			#video.save(os.path.join(app.config["VIDEO_UPLOADS"], video.filename))

			#writing new json data to the same json file
			with open("json/data.json", "w") as read_file:
				json.dump(crucialData, read_file)
				read_file.close()
		else:
			print("nope")
	#allowing html page to render from app		
	return render_template("index.html", subj_matter=subject_matter, numberDog=numDog, numberCar=numCar, numberPlane=numPlane)


if __name__ == '__main__':
	app.run(debug=True)
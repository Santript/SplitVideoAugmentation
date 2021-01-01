from flask import *
import os
import json

app = Flask(__name__)


#first step to create json object dictionary
data = {
	"step_1": {
		"vid_file": "",
		"subject_matter": "",
		"numDog": 0,
		"numCar": 0,
		"numPlane": 0
	}
}

#taking above dictionary and converting it to string datatype
jsondata = json.dumps(data)
#converting to json dictionary
crucialData = json.loads(jsondata)


#directory where all videos will be uploaded into
app.config["VIDEO_UPLOADS"] = "uploads/"

@app.route("/", methods=["GET", "POST"])


def allProcesses():

	#requesting video file that is uploaded and saving it to uploads directory (using POST request for security)
	if request.method == "POST":
		if request.files:
			video = request.files["vidFile"]
			#changing json object variable
			crucialData["step_1"]["vid_file"] = video.filename
			#saving video in directory
			#video.save(os.path.join(app.config["VIDEO_UPLOADS"], video.filename))
			print("video saved")
		else:
			print("nope")
	#allowing html page to render from app		
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
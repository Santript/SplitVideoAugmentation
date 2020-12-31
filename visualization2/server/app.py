from flask import *
import os

app = Flask(__name__)

app.config["VIDEO_UPLOADS"] = "/home/santript/ImportantProjects/SplitVideoAugmentation/visualization2/server/uploads/"

@app.route("/", methods=["GET", "POST"])


#def home():
#	return render_template("index.html")



#@app.route("/upload", methods=["GET", "POST"])


def getVideo():
	if request.method == "POST":
		if request.files:
			video = request.files["vidFile"]
			video.save(os.path.join(app.config["VIDEO_UPLOADS"], video.filename))
			print("video saved")
		else:
			print("nope")
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
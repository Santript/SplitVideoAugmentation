import json

with open("static/json/step_1.json", "r") as read_file:
	allData = json.load(read_file)
	read_file.close()

if allData["step_1"]["subject_matter"] == "Remove Frames":
	print("It is working")
else:
	print("not working")
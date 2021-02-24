import json

with open("../static/json/data.json", "r") as main_read_file:
	all_data = json.load(main_read_file)
	vidFile = all_data["step_1"]["vid_file"]
	main_read_file.close()

print(vidFile)
all_data["step_1"]["vid_file"] = ""

with open("../static/json/data.json", "w") as main_read_file:
	json.dump(all_data, main_read_file)
	main_read_file.close()

print(all_data["step_1"]["vid_file"])
#import statements
import cv2
import os
import time
import json


#accessing data from json file
with open("static/json/data.json", "r") as main_read_file:
	all_data = json.load(main_read_file)
	step1data = all_data["step_1"]
	vid_filename = step1data["vid_file"]
	object_type = step1data["subject_matter"]
	main_read_file.close()

with open("static/json/video2Frames.json", "r") as python_read_file:
	v2FData = json.load(python_read_file)
	python_read_file.close() 


#creates VideoCapture object to view the video
vidcap = cv2.VideoCapture(os.path.join("uploads/", vid_filename))
interval = 0

#splits video into frames and checks if it's successful or not
starttime = time.time()
while(vidcap.isOpened()):
	determine, frame = vidcap.read()
	if(determine == False):
		break
	#saves all frames in the "frames" directory in the "outputs" directory
	cv2.imwrite('dataset/'+str(object_type)+os.path.splitext(vid_filename)[0]+str(interval)+'.jpg', frame)
	interval+=1
#ends VideoCapture and displays time taken
vidcap.release()
cv2.destroyAllWindows()
endtime = time.time()
print(interval,"images created (",round(endtime-starttime, 2),"sec )")

#changing the json value for the number of images

"""
for item in v2FData:
	v2FData[item] = 0
"""

json_img_type = "num"+str(object_type)
v2FData[json_img_type] = interval


#changing the json file using "dump()" function part of json
with open("static/json/video2Frames.json", "w") as python_read_file:
	json.dump(v2FData, python_read_file)
	python_read_file.close()

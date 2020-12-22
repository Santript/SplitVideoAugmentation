#import statements
import cv2
import os
import time
import json


#accessing data from json file
with open("../visualization/json/data.json", "r") as read_file:
	all_data = json.load(read_file)
	step1data = all_data["Step_1"]
	vid_filename = step1data["vid_file"]
	object_type = step1data["subject_matter"]
	read_file.close()


#creates VideoCapture object to view the video
vidcap = cv2.VideoCapture(vid_filename)
interval = 0

#splits video into frames and checks if it's successful or not
starttime = time.time()
while(vidcap.isOpened()):
	determine, frame = vidcap.read()
	if(determine == False):
		break
	#saves all frames in the "frames" directory in the "outputs" directory
	cv2.imwrite(os.path.abspath(os.path.join(os.getcwd(), '..'))+'/outputs/frames/'+object_type+str(interval)+'.jpg', frame)
	interval+=1
#ends VideoCapture and displays time taken
vidcap.release()
cv2.destroyAllWindows()
endtime = time.time()
print(interval,"images created (",round(endtime-starttime, 2),"sec )")

#changing the json value for the number of images
json_img_type = "num"+object_type
step1data[json_img_type] = interval

#changing the json file using "dump()" function part of json
with open("../visualization/json/data.json", "w") as read_file:
	json.dump(all_data, read_file)
	read_file.close()
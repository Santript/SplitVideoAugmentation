#import statements
import cv2
import os
import time

vid_filename = "../assets/dog_1.mp4"
object_type = "dog"

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
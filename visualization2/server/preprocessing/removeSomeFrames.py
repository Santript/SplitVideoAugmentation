from PIL import Image

import imagehash
import os
import time
import json


"""
Compares two frames and checks whether they are similar
Removes the second frame if it is too similar to first frame
@params frame1, frame2 : filepaths to frames
"""

def removeFrames():

	with open("static/json/video2Frames.json") as read_file:
		allData = json.load(read_file)
		read_file.close()

	#starting time
	#collects all frames from dataset directory and stores it into a list
	starttime = time.time()
	allFrames = os.listdir('dataset/')
	removeFrames = []
	numDogRemovedFrames = 0
	numCarRemovedFrames = 0
	numPlaneRemovedFrames = 0
	frameSubjectMatter = ""

	#opening images, finds average hash value and decides whether to place into removed category or keep category
	for index in range(len(allFrames)-1):
		file1 = os.path.join('dataset/', allFrames[index])
		file2 = os.path.join('dataset/', allFrames[index+1])

		#opening images
		pic1 = Image.open(file1)
		pic2 = Image.open(file2)

		#finding the average hash value of each frame for comparison
		hash1 = imagehash.average_hash(pic1)
		hash2 = imagehash.average_hash(pic2)
		#cut off value to determine how similar or different the frames should be
		cutoff = 0.5

		#checks if difference between average hash values are less than the cutoff value
		if hash1-hash2 < cutoff:
			removeFrames.append(file2)

	#remove frames with hash value less than cutoff
	for frame in removeFrames:
		if "Car" in frame:
			numCarRemovedFrames+=1
		if "Dog" in frame:
			numDogRemovedFrames+=1
		if "Plane" in frame:
			numPlaneRemovedFrames+=1

		os.remove(frame)

	#finding end time
	#outputting number of frames removed and time taken for whole process
	endtime = time.time()
	print("Number of frames removed: ", len(removeFrames))
	print("Time taken: ", round(endtime-starttime, 2), "sec")

	#changing json file based on how many images were removed (based on subject matter)
	allData["numDog"] = allData["numDog"] - numDogRemovedFrames
	allData["numCar"] = allData["numCar"] - numCarRemovedFrames
	allData["numPlane"] = allData["numPlane"] - numPlaneRemovedFrames

	#writing to json file
	with open("static/json/video2Frames.json", "w") as write_file:
		json.dump(allData, write_file)
		write_file.close()
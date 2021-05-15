from PIL import Image

import imagehash
import os
import time
import json
import log


def sortList(list):
	newList = []

	for index in range(len(list)):
		for name in list:
			if int(name.split('_')[2].split('.')[0]) == index:
				newList.append(name)

	return newList


"""
Compares two frames and checks whether they are similar
Removes the second frame if it is too similar to first frame
@params frame1, frame2 : filepaths to frames
"""

def removeFrames(smList):

	with open("static/json/step_1.json", "r") as read_file:
		allData = json.load(read_file)
		read_file.close()

	with open("static/json/video2Frames.json", "r") as read_file:
		v2F_data = json.load(read_file)
		read_file.close()

	#starting time
	#collects all frames from dataset directory and stores it into a list
	starttime = time.time()
	numDogRemovedFrames, numCarRemovedFrames, numPlaneRemovedFrames, total_removed = 0, 0, 0, 0
	allRemoved = []

	for sm in smList:

		orig_allFrames = os.listdir(os.path.join('dataset/', sm))
		allFrames = sortList(orig_allFrames)
		moveFirstImage = False

		#opening images, finds average hash value and decides whether to place into removed category or keep category
		file1 = os.path.join(os.path.join('dataset/', sm), allFrames[0])
		for index in range(1, len(allFrames)-1):

			if moveFirstImage:
				file1 = os.path.join(os.path.join('dataset/', sm), allFrames[index-1])
				file2 = os.path.join(os.path.join('dataset/', sm), allFrames[index])
			else:
				file2 = os.path.join(os.path.join('dataset/', sm), allFrames[index])

			#opening images
			pic1 = Image.open(file1)
			pic2 = Image.open(file2)

			#finding the average hash value of each frame for comparison
			hash1 = imagehash.average_hash(pic1)
			hash2 = imagehash.average_hash(pic2)
			#cut off value to determine how similar or different the frames should be
			cutoff = 8.5

			#checks if difference between average hash values are less than the cutoff value
			if abs(hash1-hash2) < cutoff:
				#remove frames with hash value less than cutoff
				#os.remove(file2)
				#allRemoved.append(file2)
				os.remove(file2)
				total_removed += 1
				moveFirstImage = False
			else:
				moveFirstImage = True
			

		if sm == 'Dog':
			numDogRemovedFrames += total_removed
		elif sm == 'Car':
			numCarRemovedFrames += total_removed
		else:
			numPlaneRemovedFrames += total_removed

		total_removed = 0

	print(allRemoved)
	for remove in allRemoved:
		os.remove(remove)

	#finding end time
	#outputting number of frames removed and time taken for whole process
	endtime = time.time()

	if 'Dog' in smList:
		log.LOG_INFO("Number of dog frames removed: ", numDogRemovedFrames)
	if 'Car' in smList:
		log.LOG_INFO("Number of car frames removed: ", numCarRemovedFrames)
	if 'Plane' in smList:
		log.LOG_INFO("Number of plane frames removed: ", numPlaneRemovedFrames)

	log.LOG_INFO("Time taken: ", round(endtime-starttime, 2), "sec")

	#changing json file based on how many images were removed (based on subject matter)
	allData["step_1"]["numDog"] = allData["step_1"]["numDog"] - numDogRemovedFrames
	allData["step_1"]["numCar"] = allData["step_1"]["numCar"] - numCarRemovedFrames
	allData["step_1"]["numPlane"] = allData["step_1"]["numPlane"] - numPlaneRemovedFrames

	v2F_data["numDog"] = v2F_data["numDog"] - numDogRemovedFrames
	v2F_data["numCar"] = v2F_data["numCar"] - numCarRemovedFrames
	v2F_data["numPlane"] = v2F_data["numPlane"] - numPlaneRemovedFrames

	#writing to json file
	with open("static/json/step_1.json", "w") as write_file:
		json.dump(allData, write_file, indent=2)
		write_file.close()

	with open("static/json/video2Frames.json", "w") as write_file:
		json.dump(v2F_data, write_file, indent=2)
		write_file.close()
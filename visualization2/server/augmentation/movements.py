from PIL import Image, ImageOps

import os
import json


class MovementsAugmentationMethods:

	degrees = 0

	def __init__(self, dirPath, smList):
		self.dirPath = dirPath
		self.smList = smList

		self.addedDogFrames = 0
		self.addedCarFrames = 0
		self.addedPlaneFrames = 0


	"""
	Returns the directory path containing all frames

	"""
	def getDirPath(self, cls):
		return self.dirPath


	"""
	Flips the image 180 degrees

	"""
	def flip(self, allFiles):
		for sm in self.smList:
			allFrames = allFiles[sm]

			for frame in allFrames:
				img = Image.open(os.path.join(os.path.join(self.dirPath, sm), frame))
				imgFlip = ImageOps.flip(img)

				newImgName = os.path.join(os.path.join(self.dirPath, sm), os.path.splitext(frame)[0] + "_flipped.jpg")
				imgFlip.save(newImgName, quality=95)

				if sm == "Car":
					self.addedCarFrames+=1
				elif sm == "Dog":
					self.addedDogFrames+=1
				else:
					self.addedPlaneFrames+=1


	"""
	Mirrors the original image

	"""
	def mirror(self, allFiles):
		for sm in self.smList:
			#allFrames = os.listdir(os.path.join(self.dirPath, sm))
			allFrames = allFiles[sm]

			for frame in allFrames:
				img = Image.open(os.path.join(os.path.join(self.dirPath, sm), frame))
				imgMirror = ImageOps.mirror(img)

				newImgName = os.path.join(os.path.join(self.dirPath, sm), os.path.splitext(frame)[0] + "_mirrored.jpg")
				imgMirror.save(newImgName, quality=95)

				if sm == "Car":
					self.addedCarFrames+=1
				elif sm == "Dog":
					self.addedDogFrames+=1
				else:
					self.addedPlaneFrames+=1


	"""
	Rotates image a specified number of degrees
	"""
	def rotate(self, degrees):
		for sm in self.smList:
			allFrames = os.listdir(os.path.join(self.dirPath, sm))

			for frame in allFrames:
				img = Image.open(os.path.join(os.path.join(self.dirPath, sm), frame))
				imgRotate = img.rotate(degrees)

				newImgName = os.path.join(os.path.join(self.dirPath, sm), os.path.splitext(frame)[0] + "_rotated.jpg")
				imgRotate.save(newImgName, quality=95)

				if sm == "Car":
					self.addedCarFrames+=1
				elif sm == "Dog":
					self.addedDogFrames+=1
				else:
					self.addedPlaneFrames+=1


	def updateJson(self):
		with open("static/json/video2Frames.json", "r") as read_file:
			allData = json.load(read_file)
			read_file.close()

		allData["numDog"] += self.addedDogFrames
		allData["numCar"] += self.addedCarFrames
		allData["numPlane"] += self.addedPlaneFrames

		with open("static/json/video2Frames.json", "w") as write_file:
			json.dump(allData, write_file, indent=2)
			write_file.close()

		self.addedDogFrames = 0
		self.addedCarFrames = 0
		self.addedPlaneFrames = 0
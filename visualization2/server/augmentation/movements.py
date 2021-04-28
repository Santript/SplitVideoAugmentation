from PIL import Image, ImageOps

import os
import json


class MovementsAugmentationMethods:

	degrees = 0

	def __init__(self, dirPath):
		self.dirPath = dirPath

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
	def flip(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))
			imgFlip = ImageOps.flip(img)

			newImgName = os.path.join("dataset/", os.path.splitext(frame)[0] + "_flipped.jpg")
			imgFlip.save(newImgName, quality=95)

			if "Car" in frame:
				self.addedCarFrames+=1
			if "Dog" in frame:
				self.addedDogFrames+=1
			if "Plane" in frame:
				self.addedPlaneFrames+=1


	"""
	Mirrors the original image

	"""
	def mirror(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))
			imgMirror = ImageOps.mirror(img)

			newImgName = os.path.join("dataset/", os.path.splitext(frame)[0] + "_mirrored.jpg")
			imgMirror.save(newImgName, quality=95)

			if "Car" in frame:
				self.addedCarFrames+=1
			if "Dog" in frame:
				self.addedDogFrames+=1
			if "Plane" in frame:
				self.addedPlaneFrames+=1


	"""
	Rotates image a specified number of degrees
	"""
	def rotate(self, degrees):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))
			imgRotate = img.rotate(degrees)

			newImgName = os.path.join("dataset/", os.path.splitext(frame)[0] + "_rotated.jpg")
			imgRotate.save(newImgName, quality=95)

			if "Car" in frame:
				self.addedCarFrames+=1
			if "Dog" in frame:
				self.addedDogFrames+=1
			if "Plane" in frame:
				self.addedPlaneFrames+=1
				

	def updateAddedVariables(self):
		if "Car" in frame:
			self.addedCarFrames+=1
		if "Dog" in frame:
			self.addedDogFrames+=1
		if "Plane" in frame:
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
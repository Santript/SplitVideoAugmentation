from PIL import Image, ImageOps

import os


class MovementsAugmentationMethods:

	degrees = 0

	def __init__(self, dirPath):
		self.dirPath = dirPath


	"""
	Returns the directory path containing all frames

	"""
	def getDirPath(self):
		return self.dirPath


	"""
	Flips the image 180 degrees

	"""
	def flip(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))
			imgFlip = ImageOps.flip(img)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_flipped.jpg")
			imgFlip.save(newImgName, quality=95)


	"""
	Mirrors the original image

	"""
	def mirror(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))
			imgMirror = ImageOps.mirror(img)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_mirrored.jpg")
			imgMirror.save(newImgName, quality=95)


	"""
	Rotates image a specified number of degrees
	"""
	def rotate(self, degrees):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))
			imgRotate = img.rotate(degrees)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_rotated.jpg")
			imgRotate.save(newImgName, quality=95)
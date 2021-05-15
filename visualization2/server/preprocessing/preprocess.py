from PIL import Image

import cv2
import numpy as np
import os


class Preprocess(object):

	def __init__(self, dirPath, smList):
		self.dirPath = dirPath
		self.smList = smList

	"""
	Resizes an image with a base width of 200 and a certain height that maintains aspect ratio of the inputted image
	"""

	def resizeAspectRatio(self, baseWidth):

		for sm in self.smList:
			allFrames = os.listdir(os.path.join(self.dirPath, sm))

			for frame in allFrames:
				img = Image.open(os.path.join(os.path.join(self.dirPath, sm), frame))

				#printing the original size of the inputted image
				owidth, oheight = img.size

				print("Size of original image:", owidth, "x", oheight)

				#calculating height to maintain aspect ratio based on the base width
				wpercent = (baseWidth/float(img.size[0]))
				hsize = int((float(img.size[1])*float(wpercent)))

				#resizing image
				imgResized = img.resize((baseWidth, hsize), Image.ANTIALIAS)

				#printing new size of image
				nwidth, nheight = imgResized.size

				print("Size of new image:", nwidth, "x", nheight)

				#saving image in a certain directory
				newImgName = os.path.join(os.path.join(self.dirPath, sm), frame)
				imgResized.save(newImgName, quality=95)

	"""
	Resizing image without maintaining aspect ratio (x,x)
	"""
	def resize(self, size, allFiles):
		for sm in self.smList:
			allFrames = allFiles[sm]
			for frame in allFrames:
				image = Image.open(os.path.join(os.path.join(self.dirPath, sm), frame))
				image = image.resize((size, size))

				newImgName = os.path.join(os.path.join(self.dirPath, sm), frame)
				image.save(newImgName)

	"""
	normalizing each image
	"""
	def normalize(self, allFiles):
		for sm in self.smList:
			allFrames = allFiles[sm]
			for frame in allFrames:
				#reading image
				img = cv2.imread(os.path.join(os.path.join(self.dirPath, sm), frame))
				final_img = cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
				newImgName = os.path.join(os.path.join(self.dirPath, sm), frame)
				cv2.imwrite(newImgName, final_img)

	def deNoise(self):
		for sm in self.smList:
			allFrames = os.listdir(os.path.join(self.dirPath, sm))
			for frame in allFrames:
				image = cv2.imread(os.path.join(os.path.join(self.dirPath, sm), frame))
				blur = cv2.GaussianBlur(image, (5, 5), 0)
				
				newImgName = os.path.join(os.path.join(self.dirPath, sm), frame)
				cv2.imwrite(newImgName, blur)

	"""
	Converting image color tensors to RGB
	"""
	def convert_rgb(self, allFiles):
		for sm in self.smList:
			allFrames = allFiles[sm]
			for frame in allFrames:
				image = cv2.imread(os.path.join(os.path.join(self.dirPath, sm), frame))
				image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

				newImgName = os.path.join(os.path.join(self.dirPath, sm), frame)
				cv2.imwrite(newImgName, image)

	"""
	Converting image color tensors to BGR
	"""
	def convert_bgr(self, allFiles):
			for sm in self.smList:
				allFrames = allFiles[sm]
				for frame in allFrames:
					image = cv2.imread(os.path.join(os.path.join(self.dirPath, sm), frame))
					image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

					newImgName = os.path.join(os.path.join(self.dirPath, sm), frame)
					cv2.imwrite(newImgName, image)
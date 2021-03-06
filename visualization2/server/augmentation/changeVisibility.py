from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from skimage.util import random_noise

import cv2
import numpy as np
import os
import time
import tensorflow as tf



class VisibilityAugmentationMethods:

	#class variables
	contrastControl = 0
	brightnessControl = 0
	blur_x = 5
	blur_y = 5
	spAmount = 0

	#for VisibilityAugmentationMethods object
	def __init__(self, dirPath):
		self.dirPath = dirPath


	def getDirPath(self):
		return self.dirPath


	"""
	converting rgb image to grayscale
	@params filename: path of file

	"""
	def makeGrayScale(self):
		allFrames = os.listdir(self.dirPath)
		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath,frame))
			imgGray = ImageOps.grayscale(img)
			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_gray.jpg")
			imgGray.save(newImgName)


	"""
	Changing both the contrast and the brightness of an image
	@params filename: path of file, contrastControl: changes contrast of image(value between 1.0 and 3.0), 
	brightnessControl: changes brightness of image(value between 1 and 100)

	"""
	def changeContrastBrightness(self, contrastControl, brightnessControl):

		allFrames = os.listdir(self.dirPath)
		start_time = time.time()

		for frame in allFrames:
			#reading image
			img = cv2.imread(os.path.join(self.dirPath, frame))

			#copying inputted image shape
			imgDiffBrightness = np.zeros(img.shape, img.dtype)

			#changing the brightness and contrast
			for y in range(img.shape[0]):
				for x in range(img.shape[1]):
					for c in range(img.shape[2]):
						imgDiffBrightness[y,x,c] = np.clip(contrastControl*img[y,x,c] + brightnessControl, 0, 255)

			#saving image to certain directory
			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_diffbright.jpg")
			cv2.imwrite(newImgName, imgDiffBrightness)
		end_time = time.time()
		time_taken = end_time - start_time
		print("Time taken: ", round(time_taken, 2), "sec")



	"""
	Adding blur to image
	@params filename: path of file, blur_x & blur_y: needed for cv2.GaussianBlur() to add blur to image

	"""
	def addBlur(self, blur_x, blur_y):

		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			#reading image
			img = cv2.imread(os.path.join(self.dirPath, frame))
			#creating new image with slight blur
			imgDiffResolution = cv2.GaussianBlur(img, (blur_x,blur_y), 0)
			#saving new image to certain directory
			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_diffresolution.jpg")
			cv2.imwrite(newImgName, imgDiffResolution)


	"""
	Adding salt and pepper effect on each frame
	@params amount: amount of salt and pepper to add, self.dirPath: directory path that contains all the frames

	"""
	def addSaltAndPepper(self, amount):

		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			#reading image
			img = cv2.imread(os.path.join(self.dirPath, frame))

			#adding random noise and salt & pepper to image with specified amount
			noise_img = random_noise(img, mode='s&p',amount=amount)
			#changed it to 'uint8' and from [0,255]
			noise_img = np.array(255*noise_img, dtype = 'uint8')

			#saving image
			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_saltpepper.jpg")
			cv2.imwrite(newImgName, noise_img)
		


	"""
	Adding shear to image along the x-axis
	@params filename: path of file

	"""
	def xAxisShear(self):

		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			#reading image
			img = cv2.imread(os.path.join(self.dirPath, frame))
			rows, cols, dim = img.shape

			#transformation matrix for x-axis shearing
			M = np.float32([[1, 0.5, 0],
		             	    [0, 1  , 0],
		            	    [0, 0 , 1]])

			#applying perspective transformation to image
			x_axis_shearedImg = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))

			#saving sheared image
			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_xshear.jpg")
			cv2.imwrite(newImgName, x_axis_shearedImg)



	"""
	Adding shear to image along the y-axis
	@params filename: path of file

	"""
	def yAxisShear(self):

		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			#reading image
			img = cv2.imread(os.path.join(self.dirPath, frame))
			rows, cols, dim = img.shape

			#transformation matrix for y-axis shearing
			M = np.float32([[1,   0, 0],
		             	    [0.5, 1, 0],
		             	    [0,   0, 1]])

			#applying perspective transformation to image
			y_axis_shearedImg = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))

			#saving sheared image
			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_yshear.jpg")
			cv2.imwrite(newImgName, y_axis_shearedImg)



	"""
	Embossing image (looks like engraving)
	@params filename: path of file

	"""
	def emboss(self):

		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))

			#embossing inputted image
			imgEmboss = img.filter(ImageFilter.EMBOSS)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_emboss.jpg")
			imgEmboss.save(newImgName)



	"""
	Smoothening image
	@params filename: path of file

	"""
	def smooth(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))

			#adding smoothening filter from ImageFilter library
			imgSmooth = img.filter(ImageFilter.SMOOTH)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_smooth.jpg")
			imgSmooth.save(newImgName)



	"""
	Smoothening image even more
	@params filename: path of file

	"""
	def extraSmooth(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))

			#adding extra smoothening filter from ImageFilter library
			imgSmooth = img.filter(ImageFilter.SMOOTH_MORE)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_smoothmore.jpg")
			imgSmooth.save(newImgName)



	"""
	Adding edge enhancement filter
	@params filename: path of file

	"""
	def edgeEnhance(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))

			#adding extra smoothening filter from ImageFilter library
			imgSmooth = img.filter(ImageFilter.EDGE_ENHANCE)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_edgeenhance.jpg")
			imgSmooth.save(newImgName)



	"""
	Adding extra edge enhancement filter
	@params filename: path of file

	"""
	def extraEdgeEnhance(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = Image.open(os.path.join(self.dirPath, frame))

			#adding extra smoothening filter from ImageFilter library
			imgSmooth = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_edgeenhancemore.jpg")
			imgSmooth.save(newImgName)



	"""
	Converting rgb image to hsv
	@params filename: path of file

	"""
	def rgbToHSV(self):
		allFrames = os.listdir(self.dirPath)

		for frame in allFrames:
			img = cv2.imread(os.path.join(self.dirPath,frame))

			#converting RGB image to HSV
			imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

			newImgName = os.path.join("augmentedDataset/", os.path.splitext(frame)[0] + "_HSV.jpg")
			cv2.imwrite(newImgName, imgHSV)
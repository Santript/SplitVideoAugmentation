from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from skimage.util import random_noise

import cv2
import numpy as np
import os
import time
import tensorflow as tf


file = "../testPics/htmlcar.jpg"


"""
converting rgb image to grayscale
@params filename: path of file

"""
def makeGrayScale(filename):
	img = Image.open(filename)
	imgGrey = ImageOps.grayscale(img)
	imgGrey.save("../testPics/car_gray.jpg")


"""
Changing both the contrast and the brightness of an image
@params filename: path of file, contrastControl: changes contrast of image(value between 1.0 and 3.0), 
brightnessControl: changes brightness of image(value between 1 and 100)

"""
def changeContrastBrightness(filename, contrastControl, brightnessControl):

	#reading image
	img = cv2.imread(filename)
	start_time = time.time()

	#copying inputted image shape
	imgDiffBrightness = np.zeros(img.shape, img.dtype)

	#changing the brightness and contrast
	for y in range(img.shape[0]):
		for x in range(img.shape[1]):
			for c in range(img.shape[2]):
				imgDiffBrightness[y,x,c] = np.clip(contrastControl*img[y,x,c] + brightnessControl, 0, 255)

	#saving image to certain directory
	cv2.imwrite("../testPics/car_diffbright.jpg", imgDiffBrightness)
	end_time = time.time()
	time_taken = end_time - start_time
	print("Time taken: ", round(time_taken, 2), "sec")



"""
Adding blur to image
@params filename: path of file, blur_x & blur_y: needed for cv2.GaussianBlur() to add blur to image

"""
def addBlur(filename, blur_x=5, blur_y=5):

	#reading image
	img = cv2.imread(filename)
	#creating new image with slight blur
	imgDiffResolution = cv2.GaussianBlur(img, (blur_x,blur_y), 0)
	#saving new image to certain directory
	cv2.imwrite("../testPics/car_diffresolution.jpg", imgDiffResolution)


def addSaltAndPepper(filename, amount):

	#reading image
	img = cv2.imread(filename)

	#adding random noise and salt & pepper to image with specified amount
	noise_img = random_noise(img, mode='s&p',amount=amount)
	#changed it to 'uint8' and from [0,255]
	noise_img = np.array(255*noise_img, dtype = 'uint8')

	#saving image
	cv2.imwrite("../testPics/car_saltpepper.jpg", noise_img)
	

"""
Adding shear to image along the x-axis
@params filename: path of file

"""
def xAxisShear(filename):

	#reading image
	img = cv2.imread(filename)
	rows, cols, dim = img.shape

	#transformation matrix for x-axis shearing
	M = np.float32([[1, 0.5, 0],
             	    [0, 1  , 0],
            	    [0, 0 , 1]])

	#applying perspective transformation to image
	x_axis_shearedImg = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))

	#saving sheared image
	cv2.imwrite("../testPics/car_xshear.jpg", x_axis_shearedImg)



"""
Adding shear to image along the y-axis
@params filename: path of file

"""
def yAxisShear(filename):

	#reading image
	img = cv2.imread(filename)
	rows, cols, dim = img.shape

	#transformation matrix for y-axis shearing
	M = np.float32([[1,   0, 0],
             	    [0.5, 1, 0],
             	    [0,   0, 1]])

	#applying perspective transformation to image
	y_axis_shearedImg = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))

	#saving sheared image
	cv2.imwrite("../testPics/car_yshear.jpg", y_axis_shearedImg)


"""
Embossing image (looks like engraving)
@params filename: path of file

"""
def emboss(filename):
	img = Image.open(filename)

	#embossing inputted image
	imgEmboss = img.filter(ImageFilter.EMBOSS)
	imgEmboss.save("../testPics/car2_emboss.jpg")



"""
Smoothening image
@params filename: path of file

"""
def smooth(filename):
	img = Image.open(filename)

	#adding smoothening filter from ImageFilter library
	imgSmooth = img.filter(ImageFilter.SMOOTH)
	imgSmooth.save("../testPics/car2_smooth.jpg")



"""
Smoothening image even more
@params filename: path of file

"""
def extraSmooth(filename):
	img = Image.open(filename)

	#adding extra smoothening filter from ImageFilter library
	imgSmooth = img.filter(ImageFilter.SMOOTH_MORE)
	imgSmooth.save("../testPics/car2_smoothmore.jpg")



"""
Adding edge enhancement filter
@params filename: path of file

"""
def edgeEnhance(filename):
	img = Image.open(filename)

	#adding extra smoothening filter from ImageFilter library
	imgSmooth = img.filter(ImageFilter.EDGE_ENHANCE)
	imgSmooth.save("../testPics/car2_edgeenhance.jpg")



"""
Adding extra edge enhancement filter
@params filename: path of file

"""
def extraEdgeEnhance(filename):
	img = Image.open(filename)

	#adding extra smoothening filter from ImageFilter library
	imgSmooth = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
	imgSmooth.save("../testPics/car2_edgeenhancemore.jpg")



"""
Converting rgb image to hsv
@params filename: path of file

"""
def rgbToHSV(filename):
	img = cv2.imread(filename)

	#converting RGB image to HSV
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	cv2.imwrite("../testPics/car2_HSV.jpg", imgHSV)

#makeGrayScale(file)
#emboss(file)
#edgeEnhance(file)
#extraEdgeEnhance(file)
#rgbToHSV(file)
#xAxisShear(file)
#yAxisShear(file)
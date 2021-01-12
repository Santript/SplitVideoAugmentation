from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from skimage.util import random_noise

import cv2
import numpy as np
import os
import time
import tensorflow as tf


file = "../testPics/car.jpeg"


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
from PIL import Image

import cv2
import numpy as np


#test file
file = "../testPics/car.jpeg"


"""
Resizes an image with a base width of 200 and a certain height that maintains aspect ratio of the inputted image

"""
def resize(filename, baseWidth=200):
	img = Image.open(filename)

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
	imgResized.save('../testPics/car_resized.jpg', quality=95)

def normalize(filename):
	#reading image
	img = cv2.imread(filename)
	normalized_img = np.zeros((800,800))
	final_img = cv2.normalize(img, normalized_img, 0, 255, cv2.NORM_MINMAX)
	cv2.imwrite("../testPics/car_normalized.jpg", final_img)

#resize(file)
#normalize(file)
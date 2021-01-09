from PIL import Image


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

resize(file)
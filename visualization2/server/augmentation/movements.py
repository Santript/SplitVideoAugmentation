from PIL import Image, ImageOps

#test file
file = "../testPics/htmlcar.jpg"


"""
Flips the image 180 degrees

"""
def flip(filename):
	img = Image.open(filename)
	imgFlip = ImageOps.flip(img)

	imgFlip.save('../testPics/car_flipped.jpg', quality=95)


"""
Mirrors the original image

"""
def mirror(filename):
	img = Image.open(filename)
	imgMirror = ImageOps.mirror(img)

	imgMirror.save('../testPics/car_mirrored.jpg', quality=95)


"""
Rotates image a specified number of degrees
"""
def rotate(filename, degrees):
	img = Image.open(filename)
	imgRotate = img.rotate(degrees)

	imgRotate.save('../testPics/car_rotated.jpg', quality=95)

#flip(file)
#mirror(file)
from PIL import Image, ImageOps

file = "../testPics/car.jpeg"

def flip(filename):
	img = Image.open(filename)
	imgFlip = ImageOps.flip(img)

	imgFlip.save('../testPics/car_flipped.jpg', quality=95)

def mirror(filename):
	img = Image.open(filename)
	imgMirror = ImageOps.mirror(img)

	imgMirror.save('../testPics/car_mirrored.jpg', quality=95)

def rotate(filename, degrees):
	img = Image.open(filename)
	imgRotate = img.rotate(degrees)

	imgRotate.save('../testPics/car_rotated.jpg', quality=95)
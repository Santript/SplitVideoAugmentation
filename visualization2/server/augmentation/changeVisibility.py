from PIL import Image, ImageOps


file = "../testPics/car.jpeg"


"""
converting rgb image to grayscale

"""
def makeGrayScale(filename):
	img = Image.open(filename)
	imgGrey = ImageOps.grayscale(img)
	imgGrey.save("../testPics/car_gray.jpg")

#def changeColoration(filename):

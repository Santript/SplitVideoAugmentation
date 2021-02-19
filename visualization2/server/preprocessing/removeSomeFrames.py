from PIL import Image
import imagehash

#file paths
image1 = "../testPics/car.jpeg"
image2 = "../testPics/car2.jpg"


"""
Compares two frames and checks whether they are similar
Removes the second frame if it is too similar to first frame
@params frame1, frame2 : filepaths to frames
"""
def compareFrames(frame1, frame2):

	#opening both frames
	pic1 = Image.open(frame1)
	pic2 = Image.open(frame2)

	#finding the average hash value of each frame for comparison
	hash1 = imagehash.average_hash(pic1)
	hash2 = imagehash.average_hash(pic2)
	#cut off value to determine how similar or different the frames should be
	cutoff = 5

	print("This is hash1-hash2:", hash1-hash2)

	#checks if difference between average hash values are less than the cutoff value
	if hash1-hash2 < cutoff:
		print("Second is too similar to first frame...remove it")
	else:
		print("Both are fine")
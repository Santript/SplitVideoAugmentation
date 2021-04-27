import zipfile
import os

def getFileNames(directoryPath):
	filePaths = []

	for root, directories, files in os.walk(directoryPath):
	    for filename in files:
	        # Create the full filepath by using os module.
	        filePath = os.path.join(root, filename)
	        filePaths.append(filePath)
	         
	  # return all paths
	return filePaths

def zipDirectory(directoryPath):
	filePaths = getFileNames(directoryPath)

	zip_file = zipfile.ZipFile('dataset.zip', 'w')
	with zip_file:
		for file in filePaths:
			zip_file.write(file)
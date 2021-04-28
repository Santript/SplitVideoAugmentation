from augmentation.changeVisibility import VisibilityAugmentationMethods
from augmentation.movements import MovementsAugmentationMethods

import json
import os
import time
import shutil
import log


def runAugmentationMethods(augmentationJson):
	step2Data = augmentationJson["step_2"]
	dirPath = "dataset/"

	grayScale = step2Data["makeGrayScale"]
	emboss = step2Data["addEmboss"]
	edgeEnhance = step2Data["addEdgeEnhance"]
	extraEdgeEnhance = step2Data["addExtraEdgeEnhance"]
	rgbToHSV = step2Data["convertRGBToHSV"]
	flipImg = step2Data["flipImg"]
	mirrorImg = step2Data["mirrorImg"]
	xShearImg = step2Data["xShearImg"]
	yShearImg = step2Data["yShearImg"]

	log.LOG_INFO("Beginning Augmentation")

	start_time = time.time()
	if grayScale:
		grayScaleAugment = VisibilityAugmentationMethods(dirPath)
		grayScaleAugment.makeGrayScale()
		grayScaleAugment.updateJson()
		log.LOG_INFO("Images converted to gray scale")
	if emboss:
		embossAugment = VisibilityAugmentationMethods(dirPath)
		embossAugment.emboss()
		embossAugment.updateJson()
		log.LOG_INFO("Images embossed")
	if edgeEnhance:
		edgeEnhanceAugment = VisibilityAugmentationMethods(dirPath)
		edgeEnhanceAugment.edgeEnhance()
		edgeEnhanceAugment.updateJson()
		log.LOG_INFO("Images edges enhanced")
	if extraEdgeEnhance:
		extraEdgeEnhanceAugment = VisibilityAugmentationMethods(dirPath)
		extraEdgeEnhanceAugment.extraEdgeEnhance()
		extraEdgeEnhanceAugment.updateJson()
		log.LOG_INFO("Images edges enhanced: EXTRA!")
	if rgbToHSV:
		rgbToHSVAugment = VisibilityAugmentationMethods(dirPath)
		rgbToHSVAugment.rgbToHSV()
		rgbToHSVAugment.updateJson()
		log.LOG_INFO("Images converted from RGB to HSV")
	if flipImg:
		flipImgAugment = MovementsAugmentationMethods(dirPath)
		flipImgAugment.flip()
		flipImgAugment.updateJson()
		log.LOG_INFO("Images flipped")
	if mirrorImg:
		mirrorImgAugment = MovementsAugmentationMethods(dirPath)
		mirrorImgAugment.mirror()
		mirrorImgAugment.updateJson()
		log.LOG_INFO("Images mirrored")
	if xShearImg:
		xShearImgAugment = VisibilityAugmentationMethods(dirPath)
		xShearImgAugment.xAxisShear()
		xShearImgAugment.updateJson()
		log.LOG_INFO("Images sheared on the x-axis")
	if yShearImg:
		yShearImgAugment = VisibilityAugmentationMethods(dirPath)
		yShearImgAugment.yAxisShear()
		yShearImgAugment.updateJson()
		log.LOG_INFO("Images sheared on the y-axis")

	log.LOG_INFO("Moving Original Images")
	moveOriginalImages('dataset/', 'augmentedDataset/')


	end_time = time.time()
	time_taken = end_time - start_time
	log.LOG_INFO("Augmentation Time Taken: ", round(time_taken, 2), "sec")


def moveOriginalImages(originalDirPath, finalDirPath):
	subjectMatters = ["Dog", "Car", "Plane"]
	makeDog, makeCar, makePlane = False, False, False

	fileNames = os.listdir(originalDirPath)

	for fileName in fileNames:
		if fileName.split("_")[0] == "Dog":
			makeDog = True
		elif fileName.split("_")[0] == "Car":
			makeCar = True
		else:
			makePlane = True

		if makeDog == True and makeCar == True and makePlane == True:
			break

	if makeDog:
		os.mkdir("augmentedDataset/Dog/")
	if makeCar:
		os.mkdir("augmentedDataset/Car/")
	if makePlane:
		os.mkdir("augmentedDataset/Plane/")

	specific_path = ""
	for fileName in fileNames:
		if fileName.split('_')[0] == "Dog":
			specific_path = os.path.join(os.path.join(finalDirPath, 'Dog/'), fileName)
		elif fileName.split('_')[0] == "Car":
			specific_path = os.path.join(os.path.join(finalDirPath, 'Car/'), fileName)
		else:
			specific_path = os.path.join(os.path.join(finalDirPath, 'Plane/'), fileName)

		#print(specific_path)
		shutil.move(os.path.join(originalDirPath, fileName), specific_path)
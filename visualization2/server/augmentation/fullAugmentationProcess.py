from augmentation.changeVisibility import VisibilityAugmentationMethods
from augmentation.movements import MovementsAugmentationMethods

import json
import os
import time
import shutil


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

	start_time = time.time()

	if grayScale:
		grayScaleAugment = VisibilityAugmentationMethods(dirPath)
		grayScaleAugment.makeGrayScale()
		grayScaleAugment.updateJson()
		print("Images converted to gray scale")
	if emboss:
		embossAugment = VisibilityAugmentationMethods(dirPath)
		embossAugment.emboss()
		embossAugment.updateJson()
		print("Images embossed")
	if edgeEnhance:
		edgeEnhanceAugment = VisibilityAugmentationMethods(dirPath)
		edgeEnhanceAugment.edgeEnhance()
		edgeEnhanceAugment.updateJson()
		print("Images edges enhanced")
	if extraEdgeEnhance:
		extraEdgeEnhanceAugment = VisibilityAugmentationMethods(dirPath)
		extraEdgeEnhanceAugment.extraEdgeEnhance()
		extraEdgeEnhanceAugment.updateJson()
		print("Images edges enhanced: EXTRA!")
	if rgbToHSV:
		rgbToHSVAugment = VisibilityAugmentationMethods(dirPath)
		rgbToHSVAugment.rgbToHSV()
		rgbToHSVAugment.updateJson()
		print("Images converted from RGB to HSV")
	if flipImg:
		flipImgAugment = MovementsAugmentationMethods(dirPath)
		flipImgAugment.flip()
		flipImgAugment.updateJson()
		print("Images flipped")
	if mirrorImg:
		mirrorImgAugment = MovementsAugmentationMethods(dirPath)
		mirrorImgAugment.mirror()
		mirrorImgAugment.updateJson()
		print("Images mirrored")
	if xShearImg:
		xShearImgAugment = VisibilityAugmentationMethods(dirPath)
		xShearImgAugment.xAxisShear()
		xShearImgAugment.updateJson()
		print("Images sheared on the x-axis")
	if yShearImg:
		yShearImgAugment = VisibilityAugmentationMethods(dirPath)
		yShearImgAugment.yAxisShear()
		yShearImgAugment.updateJson()
		print("Images sheared on the y-axis")

	print("Moving Original Images")
	moveOriginalImages('dataset/', 'augmentedDataset/')


	end_time = time.time()
	time_taken = end_time - start_time
	print("Augmentation Time Taken: ", round(time_taken, 2), "sec")


def moveOriginalImages(originalDirPath, finalDirPath):
	fileNames = os.listdir(originalDirPath)

	for fileName in fileNames:
		shutil.move(os.path.join(originalDirPath, fileName), finalDirPath)
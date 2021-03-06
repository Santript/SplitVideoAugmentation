from augmentation.changeVisibility import VisibilityAugmentationMethods
from augmentation.movements import MovementsAugmentationMethods

import json
import os
import time


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
		print("Images converted to gray scale")
	if emboss:
		embossAugment = VisibilityAugmentationMethods(dirPath)
		embossAugment.emboss()
		print("Images embossed")
	if edgeEnhance:
		edgeEnhanceAugment = VisibilityAugmentationMethods(dirPath)
		edgeEnhanceAugment.edgeEnhance()
		print("Images edges enhanced")
	if extraEdgeEnhance:
		extraEdgeEnhanceAugment = VisibilityAugmentationMethods(dirPath)
		extraEdgeEnhanceAugment.extraEdgeEnhance()
		print("Images edges enhanced: EXTRA!")
	if rgbToHSV:
		rgbToHSVAugment = VisibilityAugmentationMethods(dirPath)
		rgbToHSVAugment.rgbToHSV()
		print("Images converted from RGB to HSV")
	if flipImg:
		flipImgAugment = MovementsAugmentationMethods(dirPath)
		flipImgAugment.flip()
		print("Images flipped")
	if mirrorImg:
		mirrorImgAugment = MovementsAugmentationMethods(dirPath)
		mirrorImgAugment.mirror()
		print("Images mirrored")
	if xShearImg:
		xShearImgAugment = VisibilityAugmentationMethods(dirPath)
		xShearImgAugment.xAxisShear()
		print("Images sheared on the x-axis")
	if yShearImg:
		yShearImgAugment = VisibilityAugmentationMethods(dirPath)
		yShearImgAugment.yAxisShear()
		print("Images sheared on the y-axis")

	end_time = time.time()
	time_taken = end_time - start_time
	print("Augmentation Time Taken: ", round(time_taken, 2), "sec")

"""
with open("../static/json/step_2.json", "r") as read_file:
	data = json.load(read_file)
	read_file.close()

runAugmentationMethods(data)
"""
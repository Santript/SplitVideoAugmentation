from augmentation.changeVisibility import VisibilityAugmentationMethods
from augmentation.movements import MovementsAugmentationMethods

import time
import log

def runAugmentationMethods(augmentationJson, sm, allFiles):
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
	visibility_augmentationObj = VisibilityAugmentationMethods(dirPath, sm)
	movements_augmentationObj = MovementsAugmentationMethods(dirPath, sm)

	start_time = time.time()
	if grayScale:
		visibility_augmentationObj.makeGrayScale(allFiles)
		visibility_augmentationObj.updateJson()
		log.LOG_INFO("Images converted to gray scale")
	if emboss:
		visibility_augmentationObj.emboss(allFiles)
		visibility_augmentationObj.updateJson()
		log.LOG_INFO("Images embossed")
	if edgeEnhance:
		visibility_augmentationObj.edgeEnhance(allFiles)
		visibility_augmentationObj.updateJson()
		log.LOG_INFO("Images edges enhanced")
	if extraEdgeEnhance:
		visibility_augmentationObj.extraEdgeEnhance(allFiles)
		visibility_augmentationObj.updateJson()
		log.LOG_INFO("Images edges enhanced: EXTRA!")
	if rgbToHSV:
		visibility_augmentationObj.rgbToHSV(allFiles)
		visibility_augmentationObj.updateJson()
		log.LOG_INFO("Images converted from RGB to HSV")
	if flipImg:
		movements_augmentationObj.flip(allFiles)
		movements_augmentationObj.updateJson()
		log.LOG_INFO("Images flipped")
	if mirrorImg:
		movements_augmentationObj.mirror(allFiles)
		movements_augmentationObj.updateJson()
		log.LOG_INFO("Images mirrored")
	if xShearImg:
		visibility_augmentationObj.xAxisShear(allFiles)
		visibility_augmentationObj.updateJson()
		log.LOG_INFO("Images sheared on the x-axis")
	if yShearImg:
		visibility_augmentationObj.yAxisShear(allFiles)
		visibility_augmentationObj.updateJson()
		log.LOG_INFO("Images sheared on the y-axis")

	end_time = time.time()
	time_taken = end_time - start_time
	log.LOG_INFO("Augmentation Time Taken: ", round(time_taken, 2), "sec")
from augmentation.changeVisibility import VisibilityAugmentationMethods
from augmentation.movements import MovementsAugmentationMethods

import time
import log

def runAugmentationMethods(augmentationJson, sm):
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
		grayScaleAugment = VisibilityAugmentationMethods(dirPath, sm)
		grayScaleAugment.makeGrayScale()
		grayScaleAugment.updateJson()
		log.LOG_INFO("Images converted to gray scale")
	if emboss:
		embossAugment = VisibilityAugmentationMethods(dirPath, sm)
		embossAugment.emboss()
		embossAugment.updateJson()
		log.LOG_INFO("Images embossed")
	if edgeEnhance:
		edgeEnhanceAugment = VisibilityAugmentationMethods(dirPath, sm)
		edgeEnhanceAugment.edgeEnhance()
		edgeEnhanceAugment.updateJson()
		log.LOG_INFO("Images edges enhanced")
	if extraEdgeEnhance:
		extraEdgeEnhanceAugment = VisibilityAugmentationMethods(dirPath, sm)
		extraEdgeEnhanceAugment.extraEdgeEnhance()
		extraEdgeEnhanceAugment.updateJson()
		log.LOG_INFO("Images edges enhanced: EXTRA!")
	if rgbToHSV:
		rgbToHSVAugment = VisibilityAugmentationMethods(dirPath, sm)
		rgbToHSVAugment.rgbToHSV()
		rgbToHSVAugment.updateJson()
		log.LOG_INFO("Images converted from RGB to HSV")
	if flipImg:
		flipImgAugment = MovementsAugmentationMethods(dirPath, sm)
		flipImgAugment.flip()
		flipImgAugment.updateJson()
		log.LOG_INFO("Images flipped")
	if mirrorImg:
		mirrorImgAugment = MovementsAugmentationMethods(dirPath, sm)
		mirrorImgAugment.mirror()
		mirrorImgAugment.updateJson()
		log.LOG_INFO("Images mirrored")
	if xShearImg:
		xShearImgAugment = VisibilityAugmentationMethods(dirPath, sm)
		xShearImgAugment.xAxisShear()
		xShearImgAugment.updateJson()
		log.LOG_INFO("Images sheared on the x-axis")
	if yShearImg:
		yShearImgAugment = VisibilityAugmentationMethods(dirPath, sm)
		yShearImgAugment.yAxisShear()
		yShearImgAugment.updateJson()
		log.LOG_INFO("Images sheared on the y-axis")

	end_time = time.time()
	time_taken = end_time - start_time
	log.LOG_INFO("Augmentation Time Taken: ", round(time_taken, 2), "sec")
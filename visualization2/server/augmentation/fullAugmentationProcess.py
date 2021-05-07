from augmentation.changeVisibility import VisibilityAugmentationMethods
from augmentation.movements import MovementsAugmentationMethods

import json
import os
import time
import shutil
import log
import random

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

	log.LOG_INFO("Moving Images")

	moveDataset(sm, 0.8)


	end_time = time.time()
	time_taken = end_time - start_time
	log.LOG_INFO("Augmentation Time Taken: ", round(time_taken, 2), "sec")

def moveDataset(subjectMatter, trainPercentage):
	hasDog, hasCar, hasPlane = False, False, False

	if 'Dog' in subjectMatter:
		dogDirectory = os.listdir('dataset/Dog')
		totalDog = len(dogDirectory)
		hasDog = True
	if 'Car' in subjectMatter:
		carDirectory = os.listdir('dataset/Car')
		totalCar = len(carDirectory)
		hasCar = True
	if 'Plane' in subjectMatter:
		planeDirectory = os.listdir('dataset/Plane')
		totalPlane = len(planeDirectory)
		hasPlane = True

	if hasDog:
		dog_train_index = int(trainPercentage * len(dogDirectory))
		random.shuffle(dogDirectory)
		index = 0

		while index < dog_train_index:
			shutil.move(os.path.join('dataset/Dog', dogDirectory[index]), os.path.join('augmentedDataset/train/Dog/', dogDirectory[index]))
			index +=1

		while index < len(dogDirectory):
			shutil.move(os.path.join('dataset/Dog', dogDirectory[index]), os.path.join('augmentedDataset/validation/Dog/', dogDirectory[index]))
			index += 1

	if hasCar:
		car_train_index = int(trainPercentage * len(carDirectory))
		random.shuffle(carDirectory)
		index = 0

		while index < car_train_index:
			shutil.move(os.path.join('dataset/Car', carDirectory[index]), os.path.join('augmentedDataset/train/Car/', carDirectory[index]))
			index +=1

		while index < len(carDirectory):
			shutil.move(os.path.join('dataset/Car', carDirectory[index]), os.path.join('augmentedDataset/validation/Car/', carDirectory[index]))
			index += 1


	if hasPlane:
		plane_train_index = int(trainPercentage * len(planeDirectory))
		random.shuffle(planeDirectory)
		index = 0

		while index < plane_train_index:
			shutil.move(os.path.join('dataset/Plane', planeDirectory[index]), os.path.join('augmentedDataset/train/Plane/', planeDirectory[index]))
			index +=1

		while index < len(planeDirectory):
			shutil.move(os.path.join('dataset/Plane', planeDirectory[index]), os.path.join('augmentedDataset/validation/Plane/', planeDirectory[index]))
			index += 1
import time
import log
import os
import random
import shutil

from preprocessing.preprocess import Preprocess

def full_preprocess(preprocessing_data, sm):
	normalize = preprocessing_data["normalize"]
	rgb = preprocessing_data["rgb"]
	bgr = preprocessing_data["bgr"]
	resize = preprocessing_data["resize"]

	directory = 'dataset/'
	preprocessObj = Preprocess(directory, sm)
	start_time = time.time()

	if normalize:
		preprocessObj.normalize()

	if rgb and bgr:
		log.LOG_ERR("Can not convert images to both RGB and BGR")
	elif rgb:
		preprocessObj.convert_rgb()
	elif bgr:
		preprocessObj.convert_bgr()

	if resize.isnumeric():
		preprocessObj.resize(int(resize))

	log.LOG_INFO("Moving Images")

	moveDataset(sm, 0.8)

	end_time = time.time()
	time_taken = end_time - start_time
	log.LOG_INFO("Preprocess Time Taken: ", round(time_taken, 2), "sec")


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
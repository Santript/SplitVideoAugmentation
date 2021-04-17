from tensorflow.keras import layers
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import RMSprop

import tensorflow as tf
import numpy as np
import log
import zipfile
import os

"""
Extracts zipfile into /tmp directory
"""
def extractDataset(zipFile, endDirectory='/tmp'):
	unzip = zipfile.ZipFile(zipFile, "r")
	unzip.extractall(endDirectory)
	unzip.close()

#PREPROCESSING STEP SKIPPED SINCE IT'S ALREADY DONE!

def alignTrainTest():
	#trainDog = 
	#testDog = 
	#trainCar = 
	#testCar = 
	#trainPlane = 
	#testPlane = 

	#return all of them

def defineModel():
	log.LOG_INFO("Defining Model")

	input = layers.Input(shape=(48,48,3))

	layer = layers.Conv2D(16, 3, activation='relu')(input)
	layer = layers.MaxPooling2D(2)(layer)

	layer = layers.Conv2D(32, 3, activation='relu')(layer)
	layer = layers.MaxPooling2D(2)(layer)

	layer = layers.Conv2D(64, 3, activation='relu')(layer)
	layer = layers.MaxPooling2D(2)(layer)

	layer = layers.Flatten()(layer)
	layer = layers.Dense(512, activation='relu')(layer)

	output = layers.Dense(1, activation='sigmoid')(layer)

	model = Model(input, output)
	log.LOG_INFO("Done")
	log.LOG_INFO(model.summary())
	print()
	log.LOG_INFO("Compiling Model")

	model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.001), metrics=['accuracy'])

	return model

def train(model):
	model_name = 'DogCarPlane.h5'

	checkpointer = ModelCheckpoint(model_name, monitor='val_loss',verbose=1,save_best_only=True,save_weights_only=False, mode='auto',save_freq='epoch')
	early_stop=tf.keras.callbacks.EarlyStopping(patience=10, monitor='val_loss',restore_best_weights=True)

	callback_list=[checkpointer, early_stop]

	history = model.fit({trainingData}, validation_data={validationData}, batch_size=64, epochs=20, callbacks=[callback_list], verbose=2)

	return history

def visualizePrediction(history):

def samplePrediction(model, images):

def main():
	zipFileName = ""
	extractDataset(zipFileName)

	model = defineModel()
	history = train(model)
	visualizePrediction(history)
	samplePrediction(model, ["something"])
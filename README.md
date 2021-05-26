# SplitVideoAugmentation


This is an application that aims to ease the process of creating an image dataset with the use of image augmentation.\
This application was developed and tested on Python 3.6.9 and uses the Flask framework.


## What Can Be Done?
*   User can select classes to be added for an image dataset (ie. dog, cats, trees, etc.)
*   Multiple videos can be uploaded, which will be split into frames --> Live count provided
*   Simultaneously, unecessary images are removed automatically
*   User can then select 10-15 different augmentation methods to be performed on each frame (grayscale, mirror, etc.)
*   **Preprocessing can also be done through this application (normalization, RGB/BGR conversion, resizing, etc.)**
*   Images are then moved to a proper image dataset format, shown below
*   Dataset zipped and sent to the user for their use!

## Dependencies
1. OpenCV:\
 `pip install opencv-python`
2. Flask:\
 `pip install Flask`
3. ImageHash:\
 `pip install ImageHash`
4. Shutil:\
 `pip install pytest-shutil`
5. Python PIL:\
 `pip install Pillow`

## Quick Start

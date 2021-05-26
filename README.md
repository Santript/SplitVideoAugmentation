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

![properdatasetformat](https://user-images.githubusercontent.com/63558643/119702393-44e8f400-be0a-11eb-8947-43d7b7d9845f.png)


*   Dataset zipped and sent to the user for their use!

## Dependencies (plus version # tested on)
1. OpenCV 4.5.2.52:\
 `pip install opencv-python`
2. Flask 2.0.1:\
 `pip install Flask`
3. ImageHash 4.2.0:\
 `pip install ImageHash`
4. Shutil 1.7.0:\
 `pip install pytest-shutil`
5. Python Pillow 8.2.0:\
 `pip install Pillow`
6. scikit-image 0.17.2:\
 `pip install scikit-image`

or

```
cd SplitVideoAugmentation
vi requirements.txt
```

## Quick Start

```
#navigate to server directory
cd VideoSplitAugmentation/visualization2/server

#run the application and start server
sudo flask run

#navigate to http://127.0.0.1:5000/videotoframes
```

## Sample Dataset (Dog vs Car cs Plane) - 96% acc

Download here: [dataset.zip](https://github.com/Santript/SplitVideoAugmentation/files/6549346/dataset.zip)


## Demos


https://user-images.githubusercontent.com/63558643/119703239-3222ef00-be0b-11eb-90dc-5f4437d3873f.mp4

https://user-images.githubusercontent.com/63558643/119703443-65657e00-be0b-11eb-8f37-aa9d60f04cd3.mp4

https://user-images.githubusercontent.com/63558643/119703477-6d252280-be0b-11eb-9c5b-9b0ba12f9ff9.mp4


## Table of Content
* [General info](#general-info)
* [Dependencies](#dependencies)
* [Prerequisites](#prerequisites)
* [Execution](#execution)

## General info
In this project, pixel-wise comparison between two input images is performed and differences are displayed as numerical parameters. This project is basically divided into two parts (these process happen in the backend using ```image_processing.py``` file):
1. Pre-processing - In which steps like greyscale conversion, maintaining uniform dimensions, removal of noise are perfomed.
2. Compare function - Here the actual comparison between two images takes place which uses skimage's Structual Similarity Index, Mean square Error and Histogramical difference.

## Dependencies
Project is created with the help of:
* Numpy
* Scikit Image
* OpenCV

## Prerequisites
To use it, you require the following:
```
1. Python3
2. Pip
```

## Installation and Setup
Once you got the requisites on your machine, for a UNIX based system executing the following command to install the required libraries:
```
make init
source .venv/bin/activate
```

OR executing the following command will install all the required libraries for you:
```
$ pip install -r requirements.txt
```
	
## Execution
To run the project, you can directly run the ```compare_img.py``` file and provide the directory path for both the images.

```$ python3 compare_img.py DIR_PATH_IMG1 DIR_PATH_IMG2```

Example: ```$ python3 compare_img.py ./images/img1.jpg ./images/img1.jpg ```

Note that image path can be a git blob url as well.
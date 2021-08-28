
## Table of contents
* [General info](#general-info)
* [Prerequisites](#prerequisites)
* [Dependencies](#dependencies)
* [How to use](#how-to-use)

## General info
In this project, pixel-wise comparison on two input images is performed and differences are displayed as quantised parameters. This project is basically divided into two parts (these process happen in the backend using ```image_processing.py``` file):
1. Pre-processing - In which steps like greyscale conversion, maintaining uniform diemensions, removal of noise are perfomed.
2. Compare function - Here the actual comparison between two images takes place, skimage's Structual Similarity Index, Mean square Error and Histogramical difference is computed.

## Dependencies
Project is created with:
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
Once you got the requisites on your machine, for a UNIX based system please execute the following command to install the required dependencies.
```
make init
source .venv/bin/activate
```

OR execute the following command:
```
$ pip install -r requirements.txt
```
This will install all the required libraries for you.
	
## How to use
To run the project, you can directly run the ```compare_img.py``` file and provide the directory path for both the images.

```$ python3 compare_img.py DIR_PATH_IMG1 DIR_PATH_IMG2```

Example: ```$ python3 compare_img.py ./images/img1.jpg ./images/img1.jpg ```

Note that image path can be a git blob url as well.
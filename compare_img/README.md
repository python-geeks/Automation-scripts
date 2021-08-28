
## Table of Content
* [About](#about)
* [Prerequisites](#prerequisites)
* [Installation and Setup](#installation-and-setup)
* [Execution](#execution)
* [Results](#results)

## About
In this project, pixel-wise comparison between two input images is performed and differences are displayed as numerical parameters. This project is basically divided into two parts:
1. Pre-processing - In which steps like greyscale conversion, maintaining uniform dimensions are perfomed.
2. Compare function - Here the actual comparison between two images takes place which uses skimage's Structual Similarity Index, Mean square Error and Histogramical difference.

This project is created with the help of:
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

Example: 

```$ python3 compare_img.py ./images/img1.jpg ./images/img2.jpg ```

Note: The image path can be a raw url as well. 

Example: 
```
$ python3 compare_img.py https://raw.githubusercontent.com/SiddhanthNB/Automation-scripts/main/compare_img/images/img1.jpg https://raw.githubusercontent.com/SiddhanthNB/Automation-scripts/main/compare_img/images/img2.jpg 
```

## Results
After running the script, you will find the output as
```
SSI value is (some value)
MSE value is (some value)
Histogram difference is (some value)
```

* Here SSI value ranges from ```-1``` to ```1```, where ```1``` implies both images being completely same(which happens when same image is loaded twice). 
* MSE value is the mean square difference between each pixel loaction in both the both the images, typically for same image loaded twice the value should be ```0```.
* Histogram difference shows the intensity-level difference between the two images, which tends be very small, nevertheless shows the difference. 

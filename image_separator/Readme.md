
## Table of contents
* [General info](#general-info)
* [Prerequisites](#prerequisites)
* [Dependencies](#dependencies)
* [Setup](#setup)

## General info
In this project, we have developed the project to separate the images based on the feature vectors. We have used a pre-trained vgg16 model to extract features from images and separate them using kmeans clustering.


## Prerequisites
To use it, you require the following:

```
1. Python3
2. Pip
```

## Installing
Once you got the requisites on your machine, execute the following command:

```
$ pip install -r requirements.txt
```
This will install all the required libraries for you.
	
## Dependencies
Project is created with:
* Keras: ```pip3 install keras```
* Numpy: ```pip3 install numpy```
* Scikit Learn: ```pip install sklearn```
* OpenCV: ```pip install opencv-python```
* Tensorflow: ```pip install tensorflow```

	
## Setup
To run the project, you can directly run the ```main.py``` file and provide the image directory path and number of cluster you want and also give the output directory(optional).

```$ python3 main.py -p DIR_PATH -c NUM_CLUSTER -o OUTPUT_DIRECTORY[optional]```

To test the scrript, open a new terminal and execute the following:

```$ python3 main.py -p ./sample_images -c 2```
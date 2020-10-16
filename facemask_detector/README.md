# Face Mask Detection in PyTorch

Author - [abhinand5](https://github.com/abhinand5)

The scripts in this project contains all the necessary code to predict if a person is wearing face mask. Actually it can predict 3 things, 

1. Wearing Mask - green box
2. Incorrectly wearing Mask - orange box
3. No mask - red box

**Note: Since the saved model ckpt file and the data are too big, I have uploaded the saved model in google drive and linked the data source and drive link below.**

[Data Source](https://www.kaggle.com/andrewmvd/face-mask-detection/)

[Link to Saved Model](https://drive.google.com/file/d/1wPjFnbMY0zahUTXY6qpFY-VFTrnW0bfl/view?usp=sharing)

## Installing requirements
You can run the following command to install the requirements,

`$ pip install -r requirements.txt` 

## Usage
To detect face masks from your custom images...you can execute this following command
It takes two arguments, first one is the path to the image you want to use to predict and secondly the file name to save the results in.

`$ python detect_face_mask.py [PATH TO YOUR IMAGE] [FILE NAME FOR RESULT]`

Example: 

`$ python detect_face_mask.py ./my_image.png my_result`

There are a few results already saved in the results folder. 

You can play with the code to do any sort of retraining of the model.
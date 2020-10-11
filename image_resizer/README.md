# Image Resizer

Resize the .jpeg or .png image to preferred ratio aspect.

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

### Pre-requisites
Setup virtual environment from previous step or install requirements manually:
```
$ pip install opencv-python
```

### How to Use
```
$ python image_resizer.py
```

***follow the step-by-step console guide as below:***

1. Enter the image path
    - Enter an image path. ex. /home/user/img.jpeg
    - If the path is invalid, you will be asked to enter again.
    - After entering the valid image path, the image ratio aspect will be shown as std out on console.
2. Enter the new width
    - Enter an image width to which you want to resize it.
    - input format need to be integer. You will be asked to enter again if the input data is not an integer.
3. Enter the new height
    - Enter an image height to which you want to resize it.
    - input format need to be integer. You will be asked to enter again if the input data is not an integer.
4. Enter new file name
    - Enter the new file name for the resized image.




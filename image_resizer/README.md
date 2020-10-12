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
$ python image_resizer.py [-h] [-f F] [-rw RW] [-rh RH] [-n N]
```

If not adding any argument, the script will resize demo.jpeg and generate "demo_640x480.jpeg" as default

```
optional arguments:
  -h, --help  show this help message and exit
  -f F        The file path of target image. ex. /home/user/example.jpeg.
              Default value is "demo.jpeg"
  -rw RW      The new width to be resize. Default value is "640"
  -rh RH      The new height to be resize. Default value is "480"
  -n N        The file name. Default value is current {current file
              name}_{rw}x{rh}.jpeg
```






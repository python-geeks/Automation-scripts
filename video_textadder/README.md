# Video Textadder

Add a watermark on top-center of the video.

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

### Pre-requisites
Setup virtual environment from previous step or install requirements manually:

* ImageMagick installation
```
$ sudo apt install imagemagick
```

* moviepy installation
```
$ pip install moviepy
```

### How to Use
```
$ python video-textadder.py [-h] [-f F] [-t T] [-s S] [-n N]
```

If not adding any argument, the script will add the default watermark text on the top center of demo.mp4 and generate "demo_title.mp4" as default

```
optional arguments:
  -h, --help  show this help message and exit
  -f F        The file path of target video. ex. /home/user/example.mp4.
              Default value is "demo.mp4"
  -t T        The text you want to add to video top. ex. "Hellow Video"
  -s S        The font size of video watermark. ex. 30
  -n N        The new file name. Default value is {current file
              name}_title.mp4
```






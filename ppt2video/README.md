# PPT TO VIDEO CONVERTOR
This automated script can be used on Windows to convert Power Point
Presentation slides into mp4 video format using win32com.client.
A user can add custom text slides before each presentation slide to be included in the video.
For other systems it would require to use Python2.7 version to be able to install pypiwin32/pywin32 cause of the syntax incompatibility with Python3.

## Virtual environment

You can create <a href="https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/">virtual environment</a> to install the dependencies in a separate environment not to interfere with other packages on your machine.

## To install dependencies
```
pip install -r requirements.txt
```

## To run the script
Fill in:<br>
**file_name <br>
video_name<br>
UseTimingsAndNarrations<br>
DefaultSlideDuration<br>
VertResolution<br>
FramesPerSecond<br>
Quality variables<br>
input_dict**

with desired values in convertor.py, more instructions are in the script, and run it:
```
python3 convertor.py
```

## Adding slides
A user can add text slides before the desired slides by adding the slide number and the text as
keys and values to the input dictionary or leave it blank.

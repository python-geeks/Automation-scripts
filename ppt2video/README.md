# PPT TO VIDEO CONVERTOR
This automated script can be used on Windows to convert Power Point
Presentation slides into mp4 video format using win32com.client.
For other systems it would require to use Python2.7 version to be able to install pypiwin32/pywin32 cause of the syntax incompatibility with Python3.

## Virtual environment

You can create <a href="https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/">virtual environment</a> to install the dependencies in a separate environment not to interfere with other packages on your machine.

### If you are using Python2.7 version
You can install the package with:
```
python -m pip install pywin32
# or
pip install -U pypiwin32
```
To develop this application I am using Python 3.10.2 through bash console.

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
Quality variables**

with desired values and run the script:
```
python3 convertor.py
```

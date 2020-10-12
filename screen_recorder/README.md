# Screen Recorder

Record your screen and save it as a 1080p 60fps .avi file.

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

### Pre-requisites
Setup virtual environment from previous step or install requirements manually:
```
$ pip install numpy
$ pip install opencv-python
$ pip install pyautogui
```

### How to Use
```
$ python screen_recorder.py
```
- Press `s` : Start the screen recording
- Press `w` : Pause/Resume the screen recording
- Press `q` : End the screen recording

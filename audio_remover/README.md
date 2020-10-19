# Audio Remover

Remove the audio from video file

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

### Pre-requisites
Setup virtual environment from previous step or install requirements manually:
```
$ pip install moviepy
```

### How to Use
```
$ python audio-remover.py [-h] [-f F] [-n N]
```

If not adding any argument, the script will remove the audio from demo.mp4 and generate "demo_noAudio.mp4" as default

```
optional arguments:
  -h, --help  show this help message and exit
  -f F        The file path of target video. ex. /home/user/example.mp4.
              Default value is "demo.mp4"
  -n N        The new file name. Default value is {current file
              name}_noAudio.mp4
```






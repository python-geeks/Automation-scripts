
# Non blocking Audio Recorder for Raspberry PI
----
## Features

- Record audio using a push button

## Dependencies 

Follow following steps to install dependencies (Linux)

```bash
python3 -m pip install -r requirements.txt  #To install all dependencies stated in requirements.txt file
```

## Usage

This directory contains a python program to record audio clips in wav format using a push button. Opertion is as follows :

1. Button Pressed   --> Start Recording
1. Button Hold      --> Record
1. Button Depressed --> Stop Recording and save audio file (Locally)


## Schematic

![Schematic Diagram](schematic.png?raw=true "Schematic Diagram")


##### You can run the script by typing :

```bash
python3 non_blocking_audio_recorder.py 
```


##### Sample Output

###### Here, I am using Raspberry PI 3B+ and a simple Push Button connected to GPIO 17 and a GROUND of PI as shown in Schematic above

```
Audio Directory is Unavailable, so that's why creating one
Button is pressed
Starting Recording
print("In recordTag")
Saving with timestamp audio recording to loaction : /home/atom/Documents/projects/Automation-scripts/non_blocking_audio_recorder_raspberrypi/Audio/1603126373.wav
Recording Started
Button is depressed,Turning off recording
Recording Finished
^C Keyboard Interrupt caught -> Exiting
```
from recorder import Recorder  # custom recorder script
from gpiozero import Button  # for button interface
from datetime import datetime
import signal    # Using this library to catch keyboard interrupts
import os
import sys

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..'))


def signal_handler(signal, frame):
    print(" Keyboard Interrupt caught -> Exiting")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


class ButtonRecorder():
    def __init__(self):
        """
        Initialize button and recorder
        * Connect a push button to GPIO 17 and GROUND
        * OPeration ->
          Button Pressed -> Start Recording
          Button Hold    -> Record
          Button Depressed -> Stop Recording and save the file with wave format
        """
        self.button = Button(17, pull_up=True)

        # For  mono channels = 1, for stereo channels = 2
        # Optional arguments rate=16000 (Bit Rate), frames_per_buffer=1024*4 (Buffer Size)
        self.recorderHandler = Recorder(channels=1)
        self.recfile = None

        # path where audio files will be saved
        if os.path.isdir(ROOT_PATH + "/Audio"):
            print("Audio Directory is Available")
        else:
            print("Audio Directory is Unavailable, so that's why creating one")
            os.makedirs(ROOT_PATH + "/Audio")

        self.path = ROOT_PATH + "/Audio/"
        self.button.when_pressed = self.pressed

    def timeStamp(self):
        """
        Generate time stamp
        """
        now = datetime.now()
        timestamp1 = int(datetime.timestamp(now))
        return str(timestamp1)

    def pressed(self):
        print("Button is pressed")
        recordingFileName = self.timeStamp()
        recordingFileNameWithLocation = self.path + recordingFileName + ".wav"
        print("Starting Recording")
        self.startRecording(recordingFileNameWithLocation)

    def startRecording(self, name):
        """
        Summary: records audio clip and saves it to appropiate location

        Parameters
        ----------
        tag : recordingFileName

        TYPE: str
        Description :
        """
        print("In recordTag")
        self.button.when_released = self.released
        print("Saving with timestamp audio recording to loaction : {}".format(name))
        self.recfile = self.recorderHandler.open(name, 'wb')
        self.recfile.start_recording()
        print("Recording Started")

    def released(self):
        """
        Summary: On button released save recorded Clip
        """
        print("Button is depressed,Turning off recording")
        self.recfile.stop_recording()
        self.recfile.close()
        print("Recording Finished")
        self.button.when_released = None  # Make button release to none

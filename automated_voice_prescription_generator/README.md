# Automated Voice based Prescription Generator

## Use Case:
Generates Prescriptions in the form of PDF Files by recognizing the voice from doctors. This process will remove a lot of manual works and human errors as well as useful for the cases where doctor can't prescribe medicines physically.

## Features:
* Input information through voice.
* Control instructions through voice inputs.
* Generates simply formatted PDF as Output.
* Auto Noice Adjustment.
* Exceptions Handling.

## Technologies used:
* Python
* Speech Recognition
* Text to PDF Convertion

## Steps to run locally:
<br>

1.      clone the repository
2.      cd automated_voice_prescription_generator
3.      pip install -r requirements.txt
4.      python main.py
5.      Terminate the code anytime by saying 'exit'
## Errors:
* Incase you face issues related to **PyAudio**, run the below commands:

        pip install pipwin
        pipwin install pyaudio

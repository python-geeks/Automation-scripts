# Voice to text
Transcribes speech from inputted audio file using PocketSphinx. 
## Prerequisites
- Python 3.x
- SpeechRecognition package
# Usage Examples
- Output to terminal
```
$ python voice_to_text.py -p whatstheweatherlike.wav
```
- Output to file
```
$ python voice_to_text.py -p whatstheweatherlike.wav -o text.txt
```
- You can also use this script without the "python" for the sake of comfort on UNIX systems.
```
$ chmod +x voice_to_text.py
$ ./voice_to_text.py -p whatstheweatherlike.wav
```

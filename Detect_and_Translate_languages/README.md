# Detect and Translate languages with the help of speech recognition

This python script first records the user's voice and then convert it to text. After that it detects the language of the text and then translates the language to the user's desired language, which is asked to the user. After converting the language to the desired language, the translated text would be displayed and the system would read the text for the user.

## Prerequisite

- Any system with microphone and speaker.
- System with python installed in it. (or any IDE like Spyder, Jupyter, VScode etc)

## Dependencies

Install the following dependencies using pip

```
$ pip install speech_recognition
```

```
$ pip install langdetect
```

```
$ pip install pyttsx3
```

```
$ pip install google_trans_new
```

#### Running the script

Simply run the script using python in any IDE

```
$ python ./detect_translate.py
```

Note: google_trans_new may cause some error like "JSONDecodeError: Extra data", to fix it go to the location where all the python packages are installed and change line 151 in google_trans_new/google_trans_new.py which is: "response = (decoded_line + ']')" to "response = decoded_line"

You can also refer the git issue for more reference on this topic: https://github.com/lushan88a/google_trans_new/issues/36

Author: Tejaswi Kumar

LinkedIn: https://www.linkedin.com/in/tejaswi24/

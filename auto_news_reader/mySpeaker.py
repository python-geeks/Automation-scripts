# Import the platform module to identify your OS
import platform
# If you are using Windows, use pyttsx3 for text to speech
if platform.system() == "Windows":
    import pyttsx3
    try:
        engine = pyttsx3.init()
    except ImportError:
        pass
    except RuntimeError:
        pass
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.2)

    def print_say(txt):
        print(txt)
        engine.say(txt)
        engine.runAndWait()
# If you are using Mac or Linux, use gtts for text to speech
if platform.system() == "Darwin" or platform.system() == "Linux":
    import os

    def print_say(texts):
        print(texts)
        texts = texts.replace('"','')
        texts = texts.replace("'","")
        os.system(f'gtts-cli --nocheck "{texts}" | mpg123 -q -')
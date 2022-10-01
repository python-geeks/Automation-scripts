from win32com.client import Dispatch
import speech_recognition as sr
import os
import time


def speak(audio):
    speak = Dispatch(("sapi.spvoice"))
    speak.speak(audio)


speak("Hello, I am your personal assistant")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            Query = r.recognize_google(audio, language='en-in')

        except Exception:
            speak("Say that again please")
            return "None"
    return Query


while (True):
    if __name__ == '__main__':
        Query = TakeCommand().lower()

    if "shut down" or "shutdown" in Query:
        speak("Do you want to shutdown your pc ")
        Query2 = TakeCommand().lower()

        if "yes" in Query2:
            speak("ok shutdowning...")
            time.sleep(3)
            os.system("shutdown /s /t 0")
        elif "no" in Query2:
            speak("Ok")

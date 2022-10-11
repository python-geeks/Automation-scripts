# -*- coding: utf-8 -*-
"""
@author: Tejaswi

"""

# Python program to detect and translate with the help of speech recognition

import speech_recognition as sr
from langdetect import detect
from google_trans_new import google_translator
import pyttsx3

'''
Supported Languages:
{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic',
'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian',
'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan',
'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)',
'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish',
'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian',
'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi',
'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo',
'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese',
'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer',
'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao',
'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish',
'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam',
'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian',
'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto',
'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi',
'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic',
'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi',
'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',
'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish',
'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish',
'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese',
'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba',
'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}

'''

r = sr.Recognizer()
translator = google_translator()


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def trans(x, d):
    s = detect(x)
    result = translator.translate(x, lang_src=s, lang_tgt=d)
    return result


print("Start speaking.....(To terminate the program say 'Stop!')")
while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText.lower()
            if MyText == 'stop':
                break
            print("Did you say "+MyText)
            d = input(
                'Enter the language you need the text to be translated into:')
            translated = trans(MyText, d)
            print(translated)
            SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")

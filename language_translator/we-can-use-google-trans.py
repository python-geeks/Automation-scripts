import googletrans
from googletrans import Translator

# Get the list of languages from the google translate API
langList = googletrans.LANGUAGES
# Get the input from the user
inputSentence = input("Please enter a sentence to translate :\n")
translator = Translator()
# Detect the Language
sourceLang = translator.detect(inputSentence).lang
sourceLang = langList[sourceLang]
# Get the translation
translateString = translator.translate(inputSentence).text

print("The language detected was: " + sourceLang + "\n" + "The translation is: " + translateString)

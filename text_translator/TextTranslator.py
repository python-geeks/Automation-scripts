from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

# translate text in any language to english text (by default)
translation = translator.translate(input("Enter text to translate into English"))
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

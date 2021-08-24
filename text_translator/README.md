# Using TextTranslator script
## Steps to translate : 
1. Run the script `TextTranslator.py` using python.

2. After execution of the script you will be prompted to enter the Text you want to translate.

3. You will get the correct translation of the given text in English.

## NOTE : The input text could be in any language, it will be automatically detected and translated into English.
##         If you want to change the output Language, you may add a dest field to translation in `TextTranslator.py` and provide the language code for the required language  :
```
translation = translator.translate("INPUT_TEXT", dest="LANGUAGE_CODE")
```

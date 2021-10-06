#importing libraries
import pytesseract as pyt
from PIL import Image
from gtts import gTTS

#Loading the image file using PIL
image_file = Image.open("./PictureName.jpg")

#converting the text in image to string
text = pyt.image_to_string(image_file)

#replacing newline with space
text=text.replace("\n"," ")
print(text)

#converting the text to audio file with language "en" (English)
sound=gTTS(text, lang="en")
sound.save("sound.mp3")

print("Text in the image has been converted to audio file and saved")
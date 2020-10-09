from gtts import gTTS
from playsound import playsound
t1 = gtts.gTTS("Welcome to India")
t1.save("welcome.mp3")
playsound("welcome.mp3")

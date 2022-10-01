from gtts import gTTS
from playsound import playsound
text_val = 'All the best for your exam.'
language = 'en'
obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("exam.mp3")
playsound("exam.mp3")

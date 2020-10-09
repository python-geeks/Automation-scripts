from gtts import gTTS
from playsound import playsound
text_val = 'All the best for your exam.'  

language = 'en'
# Passing the text and language to the engine,
# here we have assign slow=False. Which denotes  
# the module that the transformed audio should
# have a high speed
obj = gTTS(text=text_val, lang=language, slow=False)  
#Here we are saving the transformed audio in a mp3 file named
# exam.mp3
obj.save("exam.mp3")  
# Play the exam.mp3 file
playsound("exam.mp3")

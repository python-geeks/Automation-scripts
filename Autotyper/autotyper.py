import pyautogui
import time
time.sleep(5)
#paste code in the text file-CV
for line in open("text.txt", "r",encoding="utf-8"):
    pyautogui.typewrite(line)
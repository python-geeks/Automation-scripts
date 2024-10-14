import pyautogui
import time

# Wait for 5 seconds before starting
time.sleep(5)

# Paste code from the text file - CV
with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        pyautogui.typewrite(line)

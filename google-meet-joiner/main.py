import time
import webbrowser
import schedule
import pyautogui

url1 = "https://meet.google.com/"
url2 = "https://www.google.com/"

def class1():
	webbrowser.open(url1)
	time.sleep(3)
	print("Joining Class")
	time.sleep(2)
	pyautogui.hotkey('command', 'd')
	print("turned off camera")
	time.sleep(2)
	pyautogui.hotkey('command', 'e')
	print("turned off mic")
	time.sleep(3)

	for i in range(4):
		pyautogui.press('tab')

	time.sleep(3)
	pyautogui.press('enter')

def class2():
	webbrowser.open(url2)
	time.sleep(3)
	print("Joining Class")
	time.sleep(2)
	pyautogui.hotkey('command', 'd')
	print("turned off camera")
	time.sleep(2)
	pyautogui.hotkey('command', 'e')
	print("turned off mic")
	time.sleep(3)

	for i in range(4):
		pyautogui.press('tab')

	time.sleep(3)
	pyautogui.press('enter')


if __name__ == "__main__":
    schedule.every().day.at("16:37").do(class1)
    schedule.every().day.at("14:00").do(class2)

    while True:
        schedule.run_pending()  # check if we need to run anything
        time.sleep(10)  # wait 10 seconds before checking each time again

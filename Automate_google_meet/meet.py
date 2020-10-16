import pyautogui, sys
import time
import webbrowser

def trackMouse():
	print('Press Ctrl-C to quit.')
	try:
	    while True:
	        x, y = pyautogui.position()
	        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
	        print(positionStr, end='')
	        print('\b' * len(positionStr), end='', flush=True)
	except KeyboardInterrupt:
	    print('\n')

def doMeet():
	webbrowser.open('https://your-class-url.com', new=2)
	time.sleep(5)
	pyautogui.moveTo(100, 200)
	pyautogui.click()
	time.sleep(2)
	pyautogui.moveTo(300, 400)
	pyautogui.click()


doMeet()

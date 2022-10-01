import time
import webbrowser
import schedule
import pyautogui
import pyperclip


url1 = "PASTE gmeet link/zoom link/zoom meeting id"
url2 = "PASTE gmeet link/zoom link/zoom meeting id"


def gMeet(url):
    webbrowser.open(url)
    time.sleep(3)
    print("Joining Class")
    time.sleep(2)
    pyautogui.hotkey('command', 'd')
    print("Turned off camera")
    pyautogui.hotkey('command', 'e')
    print("Turned off mic")
    time.sleep(3)

    for i in range(4):
        pyautogui.press('tab')

    time.sleep(3)
    pyautogui.press('enter')


def zMeet(url):
    # copy link
    pyperclip.copy(url)

    time.sleep(0.2)

    pyautogui.press('esc', interval=0.1)

    time.sleep(0.3)

    # open shart
    pyautogui.press('win', interval=0.5)
    # type zoom
    pyautogui.write('zoom')
    time.sleep(2)
    # press enter
    pyautogui.press('enter', interval=0.5)

    time.sleep(8)

    # Click zoom button
    x, y = pyautogui.locateCenterOnScreen('zoom_btn.png')
    pyautogui.click(x, y)

    pyautogui.press('enter', interval=0.5)

    # paste link
    pyautogui.hotkey('ctrl', 'v')

    # use tabs to move to next section
    pyautogui.press('tab', interval=0.5)
    pyautogui.press('tab', interval=0.5)
    pyautogui.press('tab', interval=0.5)
    pyautogui.press('enter', interval=0.5)  # mute mic

    pyautogui.press('tab', interval=0.5)
    pyautogui.press('enter', interval=0.5)  # turn off  camera

    pyautogui.press('tab', interval=0.5)
    pyautogui.press('enter', interval=3)  # join zoom link


if __name__ == "__main__":
    schedule.every().day.at("16:00").do(gMeet(url1) if (
        url1.startswith("https://meet")) else zMeet(url1))
    schedule.every().day.at("06:00").do(gMeet(url2) if (
        url2.startswith("https://meet")) else zMeet(url2))

    while True:
        schedule.run_pending()  # check if we need to run anything
        time.sleep(10)  # wait 10 second before checking again'''

import time
import webbrowser
import schedule
import pyautogui


url1 = "https://meet.google.com"
url2 = "https://www.google.com"


def attend_class(url):
    webbrowser.open(url1)
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


if __name__ == "__main__":
    schedule.every().day.at("16:00").do(attend_class(url1))
    schedule.every().day.at("06:00").do(attend_class(url2))

    while True:
        schedule.run_pending()  # check if we need to run anything
        time.sleep(10)  # wait 10 second before checking again

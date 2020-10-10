from PIL import ImageGrab
import pytesseract
import threading
import pynput.mouse as ms
import pynput.keyboard as kb
from pynput.keyboard import Key, Controller
from selenium import webdriver

keyboard = Controller()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Autosearch(threading.Thread):

    def __init__(self, pImage, defined, pCords, clickCount, chromepath):
        super(Autosearch, self).__init__()

        self.pImage = pImage
        self.defined = defined
        self.pCords = pCords
        self.clickCount = clickCount
        self.chromepath = chromepath

    def area_select(self):

        def on_click(x, y, button, pressed):

            if pressed:

                if self.clickCount == 0:
                    self.pCords[0], self.pCords[1] = x, y

                elif self.clickCount == 1:
                    self.pCords[2], self.pCords[3] = x, y

                    self.defined = True
                    self.clickCount = 0
                    return False
                self.clickCount += 1

        with ms.Listener(on_click=on_click) as listener:
            listener.join()

    def keyPress(self):

        def on_press(key):
            i = 10
            print(i)

        def on_release(key):
            if key == Key.f2:
                Autosearch.area_select(self)
                Autosearch.capture(self)
                return False

        with kb.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    def capture(self):

        if self.defined:
            self.pImage = ImageGrab.grab(bbox=(self.pCords[0], self.pCords[1], self.pCords[2], self.pCords[3]))
            parastring = pytesseract.image_to_string(self.pImage)

            parastring.replace('/n', '+')
            parastring.replace(' ', '+')

            Autosearch.searches(self, parastring)

        else:
            print('error')

    def searches(self, parastring):

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        browser = webdriver.Chrome(executable_path=self.chromepath, options=options)
        url = browser.get("https://www.google.com/search?q=" + parastring + "&start=" + '0')

        browser.get(url)


if __name__ == '__main__':

    r = Autosearch(None, False, [0, 0, 0, 0], 0, "/Users/HP/Desktop/chromedriver")
    r.keyPress()

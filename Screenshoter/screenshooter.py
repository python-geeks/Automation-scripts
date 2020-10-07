import cv2
import numpy as np
import pynput.mouse as ms
import pynput.keyboard as kb
from pynput.keyboard import Key, Controller
import pyautogui

keyboard = Controller()


class TwoClicksScreenShot:
    clickCount = 0
    pCords = [0, 0, 0, 0]
    defined = False
    screenShot = None
    filename = "screenshot"

    @staticmethod
    def area_select():

        print('Click twice to define Screenshot area')

        def on_click(x, y, button, pressed):

            if pressed:

                if TwoClicksScreenShot.clickCount == 0:
                    print('First point ({0}, {1})'.format(x, y))
                    TwoClicksScreenShot.pCords[0] = x
                    TwoClicksScreenShot.pCords[1] = y
                elif TwoClicksScreenShot.clickCount == 1:
                    print('Second point ({0}, {1})'.format(x, y))
                    TwoClicksScreenShot.pCords[2] = x - TwoClicksScreenShot.pCords[0]
                    TwoClicksScreenShot.pCords[3] = y - TwoClicksScreenShot.pCords[1]
                    TwoClicksScreenShot.defined = True
                    print('')
                    TwoClicksScreenShot.clickCount = 0
                    return False
                TwoClicksScreenShot.clickCount += 1

        with ms.Listener(on_click=on_click) as listener:
            listener.join()

    @staticmethod
    def keypress():

        print('Press UP key to define Screenshot Area')

        def on_release(key):
            if key == Key.up:
                print('Pressed\n')
                TwoClicksScreenShot.area_select()
                if TwoClicksScreenShot.capture():
                    return False
                else:
                    print('Define points properly!! Press UP again to define')
                    return True

        with kb.Listener(on_release=on_release) as listener:
            listener.join()

    @staticmethod
    def start_typing():

        print('Press DOWN key to capture')

        def on_release(key):
            if key == Key.down:
                print('Pressed\n')
                TwoClicksScreenShot.output()
                return False

        with kb.Listener(on_release=on_release) as listener:
            listener.join()

    @staticmethod
    def capture():
        if TwoClicksScreenShot.pCords[2] <= 0 or TwoClicksScreenShot.pCords[3] <= 0:
            return False

        if TwoClicksScreenShot.defined:
            TwoClicksScreenShot.screenShot = pyautogui.screenshot(region=(TwoClicksScreenShot.pCords[0],
                                                                          TwoClicksScreenShot.pCords[1],
                                                                          TwoClicksScreenShot.pCords[2],
                                                                          TwoClicksScreenShot.pCords[3]))
            TwoClicksScreenShot.screenShot = cv2.cvtColor(np.array(TwoClicksScreenShot.screenShot), cv2.COLOR_BGR2RGB)
            return True

    @staticmethod
    def output():
        cv2.imwrite(TwoClicksScreenShot.filename + ".png", TwoClicksScreenShot.screenShot)
        print("Screenshot saved as " + TwoClicksScreenShot.filename + ".png")


def start():
    TwoClicksScreenShot.keypress()
    TwoClicksScreenShot.start_typing()


if __name__ == '__main__':
    start()

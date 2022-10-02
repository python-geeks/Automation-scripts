import getpass
import os_test
import readline


class MyCompleter:

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options
                                if s and s.startswith(text)]
            else:
                self.matches = self.options[:]

        try:
            return self.matches[state]
        except IndexError:
            return None


completer = MyCompleter([file for file in os_test.listdir(f'/home/{getpass.getuser()}') if not file.startswith('.')])
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

input("Input: ")

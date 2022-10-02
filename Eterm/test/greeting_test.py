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


subject_completer = MyCompleter(
    [greeting.strip() for greeting in open('Autocompletions/greeting.txt', 'r').readlines()])
readline.set_completer(subject_completer.complete)
readline.parse_and_bind('tab: complete')
input('>')

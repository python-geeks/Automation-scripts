class MyCompleter:

    def __init__(self, options):
        self.options = sorted(options)
        self.matches = None

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options
                                if text in s]
            else:
                self.matches = self.options[:]

        try:
            return self.matches[state]
        except IndexError:
            return None

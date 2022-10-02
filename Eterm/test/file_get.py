import argparse


class Test:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--file', '-f', type=str, nargs='+', help="Add Files to your emails , Enter the ")
        self.args = self.parser.parse_args(['-f', 'autocomplete.py', 'k.py'])

    def test(self):
        print(self.args.file)

Test().test()

from utils import printCalendar
import argparse

parser = argparse.ArgumentParser(
    description='Get a list of all competitive programming contests happening on various sites.'
)

parser.add_argument(
    '--today',
    action='store_true',
    help='Print only today\'s contests'
)

args = vars(parser.parse_args())
today = args["today"]

printCalendar(today)

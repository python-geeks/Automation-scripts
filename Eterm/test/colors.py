from colorama import Fore
from colorama import init as colorama_init

colorama_init(autoreset=True)

colors = dict(Fore.__dict__.items())

for color in colors.keys():
    print(colors[color] + f"{color}")
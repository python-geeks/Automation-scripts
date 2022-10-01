import requests
import argparse

parser = argparse.ArgumentParser(description='Fetch information about Github user.')
parser.add_argument('user', type=str, nargs=1, help='User that you want to look up into.')
parser.add_argument('--json', action='store_true', help='Output data in json format')

args = vars(parser.parse_args())
user = args["user"][0]
is_json = args["json"]

API_URL = "https://api.github.com"

req = requests.get(f'{API_URL}/users/{user}')
data = req.json()

if is_json:
    print(data)
else:
    for key, value in data.items():
        print(f'{key}: {value}')

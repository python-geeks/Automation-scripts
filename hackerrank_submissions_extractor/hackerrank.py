import requests
import json
from time import sleep
from os import path

BASE = <WHERE TO SAVE THE FILES>
EXTENTION = {
    "python": "py",
    "python3": "py",
    "java8": "java",
    "java": "java",
    "bash": "sh",
    "c": "c",
    "go": "go",
    "cpp": "cpp",
    "cpp14": "cpp",
    "haskell": "hs",
    "text": "txt"
}

headers = {}
headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
headers["Cookie"] = <PLACE YOUR COOKIE HERE>
headers["User-Agent"] = "curl/7.64.1"

url = "https://www.hackerrank.com/rest/contests/master/submissions/?offset=0&limit=1000"
resp = requests.get(url, headers=headers)
accepted_submissions = []
for submission in resp.json()['models']:
    print(submission['challenge']['name'], submission['status'])
    if "Accepted" in submission['status']:
        accepted_submissions.append(
            {
                "slug": submission['challenge']['slug'],
                "name": submission['challenge']['name'],
                "id": submission['id'],
                "language": submission['language'],
                "code": ""
            }
        )
print(len(accepted_submissions))
i = 0
for submission in accepted_submissions:
    print(i)
    i += 1
    file_path = f"{BASE}/{submission['slug']}_{submission['language']}_{submission['id']}.{EXTENTION[submission['language']]}"
    if path.exists(file_path):
        continue
    url = f"https://www.hackerrank.com/rest/contests/master/challenges/{submission['slug']}/submissions/{submission['id']}"
    resp = requests.get(url, headers=headers)
    try:
        submission['code'] = resp.json()['model']['code']
        with open(file_path, "w") as f:
            f.write(submission['code'])
    except:
        print(f'Failed getting code for {submission}')
    sleep(5)
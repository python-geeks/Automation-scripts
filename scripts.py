# imports
import sys
import json
from github import Github
import os

if(len(sys.argv) > 1):
    # access token
    token = sys.argv[1]
    repo_name = 'python-geeks/Automation-scripts'
    files_to_be_excluded = sys.argv[2:]
    repo_contents = {}

    try:
        gitHub = Github(token)
        repo = gitHub.get_repo(repo_name)

        contents = repo.get_contents("")
        for content in contents:
            script = content
            if((script.type == "dir") and (script.name not in files_to_be_excluded)):
                repo_contents[script.name] = script.html_url

        with open('SCRIPTS.json', 'w') as jsonfile:
            json.dump(repo_contents, jsonfile, indent=4)

    except:
        print('Either wrong token entered or poor internet connection..!')


else:
    print('Please pass the token (and the files to be excluded if any).')

os.system('python json_to_md/script.py -i SCRIPTS.json')
os.remove("SCRIPTS.json")
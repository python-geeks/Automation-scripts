import subprocess
import sys
from github import Github


def fork():

    print("To quit at any point click ctrl-c")
    accOrOrg = input(
        "Fork to your profile or an organization"
        "(type org for organization, acc for profile): ")
    while (accOrOrg != "acc" and accOrOrg != "org"):
        accOrOrg = input("invalid answer: acc or org: ")
    username = input("Your github username: ")
    password = input("Your github password: ")
    try:
        g = Github(username, password)
        user = g.get_user()
        repo = input(
            "Name of repo you want to fork (in the form owner/repo): ")
        if (accOrOrg == "acc"):
            user.create_fork(g.get_repo(repo))
        else:
            org = input("name of your organization: ")
            org = g.get_organization(org)
            org.create_fork(g.get_repo(repo))
        clone(username, repo)
    except Exception as e:
        print("ERROR: " + str(e))
        print("You can try again or click ctrl-c and exit")
        fork()


def clone(repo):

    location = input(
        "Path for cloning repo into"
        "(default is current directory): ")
    try:
        if len(location.strip()) != 0:
            arr = repo.split("/")
            subprocess.run(
                "git clone https://github.com/" + repo + ".git " + location
                + "\\" + arr[0] + "\\" + arr[1], shell=True, check=True)
        else:
            subprocess.run(
                "git clone https://github.com/" + repo + ".git",
                shell=True, check=True)

    except Exception as e:
        print("ERROR: " + str(e))
        fnc = input(
            "To start from the forking type fork, to start from"
            "cloning type clone, to exit press ctrl-c: ").lower()
        if fnc == "fork":
            fork()
        elif fnc == "clone":
            clone(repo)
        else:
            print("Invalid Input: Exiting Now")
            sys.exit()


if __name__ == "__main__":
    fork()

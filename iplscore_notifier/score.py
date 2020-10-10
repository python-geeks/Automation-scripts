from pycricbuzz import Cricbuzz
from win10toast import ToastNotifier

c = Cricbuzz()
n = ToastNotifier()
matches = c.matches()

srs_to_watch = "Indian Premier League 2020"
match_id = []


def match_info(mid):
    c = Cricbuzz()
    minfo = c.matchinfo(mid)

    print('------------------------------------------')
    print(" Match No  : " + minfo["mnum"])
    print(" Match Between : " + minfo["team1"]["name"] + " v/s " + minfo["team2"]["name"])

    if(minfo["toss"] == ""):
        print(" Toss is yet to happen")
    else:
        print(" Toss : " + minfo["toss"])

    print(" Match Location : " + minfo["venue_name"] + " located at " + minfo["venue_location"])
    print(" Match Status : " + minfo["status"])


def live_score(mid):

    c = Cricbuzz()
    lscore = c.livescore(mid)

    if lscore == {}:
        pass
    else:
        print("-------------------------------------------")
        print("Innings No : " + lscore["batting"]["score"][0]["inning_num"])
        print(lscore["batting"]["team"] + " : " + lscore["batting"]["score"][0]["runs"] + "/"
              + lscore["batting"]["score"][0]["wickets"] + " in " + lscore["batting"]["score"][0]["overs"] + " overs")

        message = (lscore["batting"]["team"] + " : " + lscore["batting"]["score"][0]["runs"] + "/"
                   + lscore["batting"]["score"][0]["wickets"] + " in " + lscore["batting"]["score"][0]["overs"]
                   + " overs")

        n.show_toast("LIVE MATCH SCORE", message, duration=10)


for i in matches:
    if(i["srs"] == srs_to_watch):
        match_id.append(i["id"])

print("Match Details Available : ")
for id in match_id:
    match_info(id)

while True:

    print("Live Score of the ongoing/over match is as follows : ")
    for id in match_id:
        live_score(id)

    message = input("Do you want to refresh the score ? [Y/N]")

    if message == "Y":
        print('------------------------------------------')
    elif message == "N":
        break
    else:
        print('Please enter "Y" or "N" only.')
        continue

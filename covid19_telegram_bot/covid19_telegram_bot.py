"""
Author: Shanmukha Vishnu
Github: @iam-shanmukha
"""
import requests
from covid import Covid

previous_data = []
# #######################Telegram###########################


def send_msg(text):
    token = "YOUR-TOKEN-HERE"
    chat_id = "GROUP-CHAT-ID-HERE"
    url_req = (
        'https://api.telegram.org/'
        'bot' + token + '/sendMessage' + '?chat_id'
        '=' + chat_id + "&text=" + text)
    results = requests.get(url_req)
    print(results.json())


# ##---One Time Run---###
covid = Covid(source="worldometers")
India_cases = covid.get_status_by_country_name("india")
stat = (
    "\n".join(
        "{} : \t{}".format(k, v)
        for k, v in India_cases.items()
        if not k.startswith(("population", "total"))
    )
    + "\n#IndiaFightsCorona"
)

previous_data.append(stat)
while 1:
    covid = Covid(source="worldometers")
    India_cases = covid.get_status_by_country_name("india")
    stat = (
        "\n".join(
            "{} : \t{}".format(k, v)
            for k, v in India_cases.items()
            if not k.startswith(("population", "total"))
        )
        + "\n#IndiaFightsCorona"
    )
    if stat in previous_data:
        print("Duplicate")
    else:
        print("msg _posted")
        previous_data = []
        previous_data.append(stat)
        send_msg(stat)

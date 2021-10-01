import os
import sys
import json
import time
import requests
from pprint import pprint
import winrt.windows.data.xml.dom as dom
import winrt.windows.ui.notifications as notifications


def check_availability():
    # check if the running device is windows
    if os.name == 'nt':
        pass
    else:
        print('This script only runs on windows.')
        sys.exit(0)


def get_quote():
    # access api to get a quote
    url = 'https://zenquotes.io/api/random'
    req = requests.request('GET', url)

    if req.status_code != 200:
        print('Connot reach api.')
        sys.exit(0)
    else:
        pass

    data = json.loads(req.content)
    # pprint(data)
    return data


def create_notifier(data):
    quote = data[0]['q']
    author = data[0]['a']
    app = '''
    {1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\WindowsPowerShell\\v1.0\\powershell.exe
    '''

    nManager = notifications.ToastNotificationManager
    notifier = nManager.create_toast_notifier(app)
    tString = f"""
      <toast>
        <visual>
          <binding template='ToastGeneric'>
            <text>Motivational Quote</text>
            <text>By {author},</text>
            <text>{quote}</text>
          </binding>
        </visual>
        <actions>
          <action
            content="Delete"
            arguments="action=delete"/>
          <action
            content="Dismiss"
            arguments="action=dismiss"/>
        </actions>
      </toast>
    """

    xDoc = dom.XmlDocument()
    xDoc.load_xml(tString)

    notifier.show(notifications.ToastNotification(xDoc))


def main_app():
    while True:
        check_availability()
        data = get_quote()
        create_notifier(data)
        print('Sent notification.')
        time.sleep(repeat_time * 3600)


if __name__ == '__main__':
    main_app()

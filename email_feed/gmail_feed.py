import xmltodict
import requests
import datetime
from datetime import datetime, timedelta

username="xxx"
password="xxx"

URL = 'https://%s:%s@mail.google.com/mail/u/0/feed/atom/all' % (username, password)
r = requests.get(URL)

if r.status_code == 401:
    print("login [%s] or password [%s] is incorrect\n%s" % (username, password,
                                                            'Also try enable "Allow less secure apps" on https://myaccount.google.com/lesssecureapps and |Gmail Settings -> Forwarding and POP / IMAP -> IMAP Acess to Enable IMAP| '))
    # https://stackoverflow.com/questions/33119667/reading-gmail-is-failing-with-imap/59922147#59922147
elif r.status_code != 200:
    print("Requests error [%s] - %s" % (r.status_code, URL))
elif r.status_code == 200:
    contents = r.text
    a = xmltodict.parse(contents)
    now_date=datetime.now()
    for k in range(len(a['feed']['entry'])):
        issued_date = (datetime.strptime(a['feed']['entry'][k]['issued'], '%Y-%m-%dT%H:%M:%SZ') - timedelta(hours=-2, minutes=0))
        timer = issued_date.strftime('%Y-%m-%d %H:%M:%S')
        #print((now_date - issued_date) / timedelta(minutes=1))
        if str(a['feed']['entry'][k]['author']['email']) == str(username) and ((now_date - issued_date) / timedelta(minutes=1))<15:
            print(a['feed']['entry'][k]['title'])
            print(a['feed']['entry'][k]['summary'][0:50])
            print(timer)
            print(a['feed']['entry'][k]['author']['email'])
            print('----------')

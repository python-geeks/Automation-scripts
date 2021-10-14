import xmltodict
import re
import requests

username = "xxx"
password = "xxx"

URL = 'https://%s:%s@mail.google.com/mail/u/0/feed/atom/all' % (username, password)
r = requests.get(URL)

if r.status_code == 401:
    print("login [%s] or password [%s] is incorrect\n%s" % (username, password, 'Error'))
elif r.status_code != 200:
    print("Requests error [%s] - %s" % (r.status_code, URL))
elif r.status_code == 200:
    contents = r.text
    a = xmltodict.parse(contents)
    for k in range(len(a['feed']['entry'])):
        text = a['feed']['entry'][k]['summary']
        key_words1 = re.findall('unsusbscribe', text)
        key_words2 = re.findall('Stop these mails', text)
        keys = key_words1 + key_words2
        urls = re.findall(r'''(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+''', text)
        if len(keys) > 0 and len(urls) > 0:
            print(a['feed']['entry'][k]['title'])
            print(a['feed']['entry'][k]['summary'][0:50])
            print(a['feed']['entry'][k]['author']['email'])
            print(urls)
            print('----------')

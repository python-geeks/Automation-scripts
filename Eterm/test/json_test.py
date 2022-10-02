import json

gmail = input('gmail:')
password = input('pass:')
x = {'gmail': gmail,
     'password': password}

with open('test.json', 'w') as f:
    json.dump(x, f)

with open('test.json', 'r') as n:
    x = json.load(n)
    print(x['gmail'])
    if x['gmail'] == "ello":
        print('k')
    else:
        print('not k')

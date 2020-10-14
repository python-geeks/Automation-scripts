import requests
no = input("enter your no")
r = requests.get('https://get.geojs.io/')
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipadd = ip_request.json()['ip']
url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
geo_request = requests.get(url)
geo_data = geo_request.json()
msg = f"latitude: {geo_data['latitude']} longitude : {geo_data['longitude']} city : {geo_data['city']}"
url1 = "https://www.fast2sms.com/dev/bulk"
query = {"authorization" : "your api key ",
         "sender_id" : "FSTSMS",
         "message" : msg,
         "language" : "english",
         "route" : "p",
         "numbers" : no
         }

headers = {
    'cache-control' : "no-cache"
}
response = requests.request("GET", url1, headers=headers, params=query)
print(response.text)

import http.client
import json
import sys


def main():
    url = "ip-api.com"
    address = ""
    if len(sys.argv) > 1:
        # getting address from command line.
        address = ''.join(sys.argv[1:])
    
    conn = http.client.HTTPConnection(url)
    conn.request("GET", f"/json/{address}")
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    # final response in JSON format
    response = json.loads(data)

    if response['status'] == 'fail':
        sys.exit(f'''
status  :   {response['status']}
message :   {response['message']}
        ''')

    print(f'''
Country         : {response['country']}
Country Code    : {response['countryCode']}
Region          : {response['region']}
Region Name     : {response['regionName']}
City            : {response['city']}
Zip             : {response['zip']}
Latitude        : {response['lat']}
Longitude       : {response['lon']}
Timezone        : {response['timezone']}
ISP             : {response['isp']}
Organization    : {response['org']}
    ''')


if __name__ == "__main__":
    main()

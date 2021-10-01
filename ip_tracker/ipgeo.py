import requests
import sys


def main():
    url = "http://ip-api.com/json/"
    if len(sys.argv) > 1:
        # getting address from command line.
        address = ''.join(sys.argv[1:])
        url += address

    response = requests.request("GET", url)
    response = response.json()

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

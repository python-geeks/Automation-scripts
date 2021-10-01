import requests
import sys
import getopt


def main(argv):

    def usage():
        print('usage: %s [-c city] [-a accesstoken] [-h help] ...') \
            % argv[0]
        return 100

    try:
        (opts, args) = getopt.getopt(argv[1:], 'c:a:h')
    except getopt.GetoptError:
        return usage()

    def help():
        print("AQI Tracker -"
              "\tLets the user know the real-time air quality values"
              "\t\t(usage: %s [-c city] [-a accesstoken] [-h help])"
              "\ncity:\t\tname of the cit"
              "\naccesstoken:\tYou need to get access token by "
              "registering on http://aqicn.org/data-platform/register/"
              "\n\t\t*if no accesstoken provided then demo accesstoken will"
              " be used \n\t\tand with demo access token only Shanghai's"
              " air quality values can be retrieved.")

    city = 'shanghai'
    accesstoken = 'demo'

    for (k, v) in opts:
        if k == '-c':
            city = v
        elif k == '-a':

            accesstoken = v
        elif k == '-h':

            return help()

    url = 'http://api.waqi.info/feed/' + city + '/?token=' + accesstoken
    print('URL: ', url)

    r = requests.get(url, auth=('user', 'pass'))

    if r.status_code == 200:
        data = r.json()
        value = data['data']['iaqi']['pm25']['v']
        toDisplay = str(value)

        if value > 0 and value < 50:
            print('Air Quality Alert ->')
            print('Current Value: Healthy - ' + toDisplay)
        elif value > 50 and value < 100:
            print('Air Quality Alert ->')
            print('Current Value: Moderate - ' + toDisplay)
        elif value > 100 and value < 150:
            print('Air Quality Alert ->')
            print('Current Value: Sensitive - ' + toDisplay)
        elif value > 150 and value < 200:
            print('Air Quality Alert ->')
            print('Current Value: UnHealhty - ' + toDisplay)
        elif value > 200 and value < 250:
            print('Air Quality Alert ->')
            print('Current Value: UnHealthy - ' + toDisplay)
        elif value > 250 and value > 300:
            print('Air Quality Alert ->')
            print('Current Value: Hazardous - ' + toDisplay)
    else:

        print('Error: Unable to connect to server')


if __name__ == '__main__':
    sys.exit(main(sys.argv))

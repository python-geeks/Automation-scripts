from bs4 import BeautifulSoup
import requests
import time
from win10toast import ToastNotifier

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    current_time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    information = f"{location} \n {current_time} \n {info} \n {weather} °C "

    toaster = ToastNotifier()
    toaster.show_toast("Weather Information",
                       f"{information}",
                       duration=10,
                       threaded=True)
    while toaster.notification_active():
        time.sleep(0.005)


# print("enter the city name")
# city=input()
city = "London"
city = city+" weather"
weather(city)

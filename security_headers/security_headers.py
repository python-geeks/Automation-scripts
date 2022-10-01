from datetime import datetime
import requests
from bs4 import BeautifulSoup

# website = input("enter the t website you want to test")
website_url = [
    "https:/google.com",
    "https://facebook.com",
    "https://instagram.com",
    "https://github.com",
    "https://youtube.com",
]

getdate = datetime.now().strftime("%d-%m-%y")


# Making a GET request
def find_headers():
    for url in website_url:
        r = requests.get(f'https://securityheaders.com/?q='
                         f'{url}&followRedirects=on')

        Strict_Transport_Security_status = False
        X_Content_Type_Options_status = False
        X_Frame_Options_status = False
        Content_Security_Policy_status = False
        Referrer_Policy_status = False
        Permissions_Policy_status = False

        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')
        print(soup)

        score = soup.find("div", {"class": "score"})
        # print(score)

        text = soup.findAll("li", {'class': "headerItem pill pill-green"})
        # print("headers present")
        for i in text:
            if i.text == "Strict-Transport-Security":
                Strict_Transport_Security_status = True
            elif i.text == "X-Content-Type-Options":
                X_Content_Type_Options_status = True
            elif i.text == "X-Frame-Options":
                X_Frame_Options_status = True
            elif i.text == "Content-Security-Policy":
                Content_Security_Policy_status = True
            elif i.text == "Referrer-Policy":
                Referrer_Policy_status = True
            elif i.text == "Permissions-Policy":
                Permissions_Policy_status = True

        data = [url, getdate, score, Strict_Transport_Security_status,
                X_Content_Type_Options_status,
                X_Frame_Options_status,
                Content_Security_Policy_status,
                Referrer_Policy_status, Permissions_Policy_status]

        print(data)


find_headers()

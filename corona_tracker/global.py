#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:46:47 2020

@author: edoardottt
"""

import requests
import time
from bs4 import BeautifulSoup

url = "https://worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_="maincounter-number")

for x in range(0, 5):
    b = "Fetching data" + "." * x
    print(b, end="\r")
    time.sleep(0.5)

print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())

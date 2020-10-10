#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:27:37 2020

@author: edoardottt
https://edoardoottavianelli.it
"""
import csv
import requests
import socket
import getopt
import sys

CSV_URL = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/\
dpc-covid19-ita-andamento-nazionale.csv"
data = []
mood = ""


# check internet connection status
def check_connection(host="8.8.8.8", port=53):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        print("[ERROR] Ensure you are connected to Internet.")
        return False


# data <-- Obtaining data from CSV
def retrieve_data(CSV_URL):
    print("Obtaining data...")
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode("utf-8")
        cr = csv.reader(decoded_content.splitlines(), delimiter=",")
        my_list = list(cr)
        for row in my_list:
            if len(row) > 0:
                data.append(row)
    return data


options, remainder = getopt.getopt(
    sys.argv[1:], "h", ["help"]
)  # all the options allowed
for opt, arg in options:
    if opt in ("-h", "--help"):
        mood = "h"


def print_help():
    print("USAGE: python covid-19.py [-h]")
    print("")
    print("       It shows the data on the command line.")
    print("")
    print("-h or --help:")
    print("")
    print("        Help doc")
    print("")
    print("Use python3 if you are on Linux.")
    print("")
    sys.exit()


def increase(new_d, old_d):
    diff = int(new_d) - int(old_d)
    diff2 = diff / int(old_d) * 100
    if diff2 > 0:
        return "+" + str(round(diff2)) + "%"
    return str(round(diff2)) + "%"


def print_diff(title, i):
    print(
        " - "
        + title
        + ": "
        + data[len(data) - 1][i]
        + " ("
        + increase(data[len(data) - 1][i], data[len(data) - 2][i])
        + ")"
    )


# PRINTING DATA ON COMMAND LINE
def print_cmd(data):
    lens = []
    for i in range(len(data[2])):
        temp = [data[j][i] for j in range(len(data)) if j != 0]
        maxx = 0
        for elem in temp:
            if len(elem) > maxx:
                maxx = len(elem)
        lens.append(maxx)
    for i in range(len(data)):
        s = "| "
        for j in range(len(data[0])):
            elem = data[i][j]
            if j > 1:
                s += elem + " " * (lens[j] - len(elem)) + " | "
            else:
                s += elem + " | "
        print(s)
    # HERE THE INCREASE FROM YESTERDAY
    titles = [
        "hospitalized with symptoms",
        "intensive therapy",
        "total hospitalized",
        "home isolation",
        "total currently positives",
        "total positives variation",
        "new currently positives",
        "discharged healed",
        "deceased",
        "total cases",
        "swabs",
    ]
    print("")
    print(" ### (Compared to Yesterday): ###")
    for i, title in enumerate(titles):
        print_diff(title, i + 2)


if check_connection():
    if mood == "h":
        print_help()
    else:
        data = retrieve_data(CSV_URL)
        print_cmd(data)

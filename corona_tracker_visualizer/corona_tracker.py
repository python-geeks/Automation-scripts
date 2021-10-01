import json
import requests
from pandas import DataFrame
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import messagebox
import numpy as np
from bs4 import BeautifulSoup
import textwrap as tw
from selenium import webdriver


frame_stat = None
frame_data = None
button_show = None
canvas1 = None
frame1 = None
root = None
info = None


def call_browser(arg):
    """opening pages on browser using selenium"""

    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    if arg == '1':
        browser.get("https://www.who.int/")

    if arg == '2':
        browser.get("https://sandipandas898.wixsite.com/sandipandas")


def get_data(url):
    response = requests.get(url)
    data = json.loads(response.content)
    return data


def save_data(content, extension):
    with open("corona_timeseries." + extension, "w") as f:
        f.write(str(content))
        f.close()


def get_chart(country):
    """To plot the growth graph based on the country"""

    """To get current data"""
    info = get_data("https://pomber.github.io/covid19/timeseries.json")
    save_data(info, "txt")
    save_data(info, "csv")

    # Uncomment the below three lines of code if API endpoint is
    # not working, or you are working offline, or you don't want
    # to fetch new information for any reason
    # with open("corona_timeseries.txt", "r") as f:
    #     info = eval(f.read())
    #         f.close()

    print("Reading done")

    try:
        if country == '':
            return

        df = DataFrame(info[country])
        df.to_csv('corona_timeseries.csv')
        plt.rcParams.update({'font.size': 8})
        figure = Figure(figsize=(5, 5), dpi=90)
        subplot = figure.add_subplot(111)

        subplot.plot(
            df['date'], df['confirmed'],
            label='confirmed', color='blue'
        )
        subplot.plot(
            df['date'], df['deaths'],
            label='deaths', color='red'
        )
        subplot.plot(
            df['date'], df['recovered'],
            label='recovered', color='green'
        )
        subplot.legend(loc='upper left')

        start, end = subplot.get_xlim()
        subplot.xaxis.set_ticks(np.arange(start, end, 45))

        for tick in subplot.get_xticklabels():
            tick.set_rotation(60)

        canvas = FigureCanvasTkAgg(figure, master=frame_stat)

        canvas.get_tk_widget().grid(
            row=4, column=0, columnspan=3,
            sticky="wen", padx=20, pady=5
        )
        plt.show()

    except Exception as e:
        print("Error", e)
        messagebox.showerror("Name Error", "Enter the correct country name")


def scrape_data():
    """
    Scrape data from 'https://www.worldometers.info/coronavirus/'
    official website
    """

    response = requests.get("https://www.worldometers.info/coronavirus/")
    data = BeautifulSoup(response.content, "html.parser")
    data_table = data.find('table', id="main_table_countries_today")

    # data_title = data_table.find('thead').text
    data_info = data_table.find('tbody').find_all('tr')

    country = []
    total_cases = []
    new_cases = []
    total_deaths = []
    new_deaths = []
    total_recovered = []
    active_cases = []
    continent = []

    for i in range(len(data_info)):
        country_data = data_info[i].find_all('td')
        country.append(country_data[1].text)
        total_cases.append(country_data[2].text)
        new_cases.append(country_data[3].text)
        total_deaths.append(country_data[4].text)
        new_deaths.append(country_data[5].text)
        total_recovered.append(country_data[6].text)
        active_cases.append(country_data[7].text)
        continent.append(country_data[14].text)

    totals = [total_cases[7], total_recovered[7], total_deaths[7]]
    country = country[8:]
    total_cases = total_cases[8:]
    new_cases = new_cases[8:]
    total_deaths = total_deaths[8:]
    new_deaths = new_deaths[8:]
    total_recovered = total_recovered[8:]
    active_cases = active_cases[8:]
    continent = continent[8:]

    return (
        totals, country,
        total_cases, new_cases,
        total_deaths, new_deaths,
        total_recovered, active_cases,
        continent
    )


def put_data_to_ui():
    """put data on the interface to show"""

    (totals, country, total_cases, new_cases, total_deaths,
        new_deaths, total_recovered, active_cases,
        continent) = scrape_data()

    frame_total = tk.Frame(frame_data, bg="#6197ed")
    frame_total.grid(row=0, column=0, sticky="we", padx=3)

    main_title1 = tk.Label(
        frame_total, font=(
            "Times New Roman", 18, "bold"
        ), bg="#6197ed", fg="#000000",
        text="World Corona Dashboard"
    )
    main_title1.grid(row=0, column=1, sticky="we", pady=10)
    main_title2 = tk.Label(
        frame_total, font=(
            "Times New Roman", 12, "italic"
        ), bg="#6197ed", fg="#000000",
        text="get real time update of COVID-19 cases"
    )
    main_title2.grid(row=1, column=1, sticky="we")

    confirmed_label = tk.Label(
        frame_total, font=(
            "Times New Roman", 12, "bold"
        ), bg="#5a54f7", fg="#000000",
        text="Total Confirmed\n" + str(totals[0])
    )
    confirmed_label.grid(
        row=2, column=0, sticky="we", ipadx=65, ipady=5, pady=12
    )
    recovered_label = tk.Label(
        frame_total, font=(
            "Times New Roman", 12, "bold"
        ),
        bg="#73fa8e", fg="#000000",
        text="Recovered\n" + str(totals[1])
    )
    recovered_label.grid(row=2, column=1, sticky="we", ipadx=21, ipady=5)
    death_label = tk.Label(
        frame_total, font=(
            "Times New Roman", 12, "bold"
        ), bg="#f25a49", fg="#000000",
        text="Death\n" + str(totals[2])
    )
    death_label.grid(row=2, column=2, sticky="we", ipadx=100, ipady=5)

    frame_title = tk.Frame(frame_data, bg="#ff8317")
    frame_title.grid(row=1, column=0, sticky="n", pady=3)

    title_label_c = tk.Label(
        frame_title, borderwidth=2, relief="solid", bg="#ff8317",
        fg="#000000",
        font=("Times New Roman", 12, "bold"), text="Counry"
    )
    title_label_tc = tk.Label(
        frame_title, borderwidth=2, relief="solid", bg="#ff8317",
        fg="#000000",
        font=("Times New Roman", 12, "bold"), text="Total \nCases"
    )
    title_label_nc = tk.Label(
        frame_title, borderwidth=2, relief="solid", bg="#ff8317",
        fg="#000000",
        font=("Times New Roman", 12, "bold"), text="New \nCases"
    )
    title_label_td = tk.Label(
        frame_title, borderwidth=2, relief="solid", bg="#ff8317",
        fg="#000000",
        font=("Times New Roman", 12, "bold"), text="Total \nDeaths"
    )
    title_label_nd = tk.Label(
        frame_title, borderwidth=2, relief="solid", bg="#ff8317",
        fg="#000000",
        font=("Times New Roman", 12, "bold"), text="New \nDeaths"
    )
    title_label_tr = tk.Label(
        frame_title, borderwidth=2, relief="solid", bg="#ff8317",
        fg="#000000",
        font=("Times New Roman", 12, "bold"), text="Total \nRecovered"
    )
    title_label_ac = tk.Label(
        frame_title, borderwidth=2, relief="solid", bg="#ff8317",
        fg="#000000",
        font=("Times New Roman", 12, "bold"), text="Active \nCases"
    )
    title_label_con = tk.Label(
        frame_title, borderwidth=2, relief="solid",
        bg="#ff8317", fg="#000000",
        font=("Times New Roman", 12, "bold"),
        text="Continent"
    )

    title_label_c.grid(row=0, column=0, padx=1, pady=1, ipadx=24, ipady=10)
    title_label_tc.grid(row=0, column=1, padx=1, pady=1, ipadx=24)
    title_label_nc.grid(row=0, column=2, padx=1, pady=1, ipadx=20)
    title_label_td.grid(row=0, column=3, padx=1, pady=1, ipadx=18)
    title_label_nd.grid(row=0, column=4, padx=1, pady=1, ipadx=14)
    title_label_tr.grid(row=0, column=5, padx=1, pady=1, ipadx=11)
    title_label_ac.grid(row=0, column=6, padx=1, pady=1, ipadx=21)
    # title_label_s.grid(row=0, column=7, padx=1, pady=1, ipadx=14, ipady=10)
    title_label_con.grid(row=0, column=7, padx=1, pady=1, ipadx=15, ipady=10)

    canvas = tk.Canvas(frame_data, bg="#f5c167")
    canvas.grid(row=2, column=0, sticky="ewn", ipady=85, padx=6, pady=3)

    scrollable_frame = tk.Frame(canvas, bg="#f5c167")

    scrollbar = tk.Scrollbar(
        frame_data, orient="vertical", command=canvas.yview
    )
    scrollbar.grid(row=2, column=1, sticky="e", ipady=200, ipadx=3)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=scrollable_frame)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    for i in range(len(country)):
        data_label1 = tk.Label(
            scrollable_frame, fg="#000000",
            bg="#f5c167", text=tw.fill(country[i], width=12)
        )
        data_label1.grid(row=i, column=0, sticky="ew", padx=(5, 0))
        data_label2 = tk.Label(
            scrollable_frame, fg="#000000",
            bg="#f5c167", text=total_cases[i]
        )
        data_label2.grid(row=i, column=1, sticky="ew", padx=(17, 18))
        data_label3 = tk.Label(
            scrollable_frame, fg="#000000",
            bg="#f5c167", text=new_cases[i]
        )
        data_label3.grid(row=i, column=2, sticky="ew", padx=(15, 15))
        data_label4 = tk.Label(
            scrollable_frame, fg="#000000",
            bg="#f5c167", text=total_deaths[i]
        )
        data_label4.grid(row=i, column=3, sticky="ew", padx=(24, 20))
        data_label5 = tk.Label(
            scrollable_frame, fg="#000000",
            bg="#f5c167", text=new_deaths[i]
        )
        data_label5.grid(row=i, column=4, sticky="ew", padx=(18, 25))
        data_label6 = tk.Label(
            scrollable_frame, fg="#000000",
            bg="#f5c167", text=total_recovered[i]
        )
        data_label6.grid(row=i, column=5, sticky="ew", padx=(20, 30))
        data_label7 = tk.Label(
            scrollable_frame, fg="#000000",
            bg="#f5c167", text=active_cases[i]
        )
        data_label7.grid(row=i, column=6, sticky="ew", padx=(10, 13))
        data_label8 = tk.Label(
            scrollable_frame, fg="#000000",
            bg="#f5c167", font=("Helvetica", 9, "italic"), text=continent[i]
        )
        data_label8.grid(row=i, column=7, sticky="ew", padx=(0, 0))

    refresh_btn = tk.Button(
        frame_data, text="Update Data",
        font=(
            "Helvetica", 12, "bold"
        ), fg="#000000", command=refresh
    )
    refresh_btn.grid(row=3, column=0, sticky="ew", padx=250)


def refresh():
    put_data_to_ui()


def main_ui():
    """Main user interface"""

    global root
    global frame_stat
    global frame_data

    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("{}x{}".format(screen_width, screen_height))
    root.title("Real time COVID-19 information tracker")
    # root.attributes('-fullscreen', True)
    # root.state('withdrawn')
    # root.wm_state('normal')

    frame_data = tk.Frame(root, bg="#6197ed")
    frame_data.grid(row=0, column=0, sticky="wns", ipady=screen_height)

    frame_stat = tk.Frame(root, bg="#e3c1f7")
    frame_stat.grid(
        row=0, column=1, sticky="ens",
        ipady=screen_height, ipadx=screen_width
    )

    visit_btn1 = tk.Button(
        frame_stat, text="Visit developer's site", bg="#fcaccd",
        font=("Helvetica", 11, "bold"), relief="flat",
        fg="#000000", command=lambda: call_browser(2)
    )
    visit_btn1.grid(
        row=0, column=0, ipady=3, ipadx=5, pady=(60, 5),
        padx=(20, 5), sticky="w"
    )

    visit_btn2 = tk.Button(
        frame_stat, text="Visit WHO's official site", bg="#fcaccd",
        font=("Helvetica", 11, "bold"), fg="#000000",
        relief="flat", command=lambda: call_browser(1)
    )
    visit_btn2.grid(
        row=0, column=1, ipady=3, ipadx=5,
        pady=(60, 5), padx=5, sticky="w"
    )

    show_label = tk.Label(
        frame_stat, text="Enter Country name to show the growth Trend",
        font=("Helvetica", 11, "italic"), bg="#e3c1f7", fg="#000000"
    )
    show_label.grid(
        row=2, column=0, padx=20, pady=(18, 5),
        columnspan=5, sticky="w"
    )

    name = tk.StringVar()
    entry = tk.Entry(
        frame_stat, width=15, textvariable=name,
        font=("Helvetica", 12, "bold")
    )
    entry.grid(
        column=0, row=3, padx=(20, 5),
        pady=5, ipady=5, sticky="w"
    )

    button = tk.Button(
        frame_stat, text="Show Trend",
        font=("Helvetica", 11, "bold"), fg="#000000",
        command=lambda: get_chart(name.get())
    )
    button.grid(
        column=1, row=3, pady=5, ipadx=3,
        ipady=2, sticky="w"
    )

    put_data_to_ui()

    root.mainloop()


if __name__ == "__main__":
    main_ui()

from tkinter import *
from  tkinter import ttk
import requests

# Free Open Weather API (https://rapidapi.com/community/api/open-weather-map/)
url = "https://community-open-weather-map.p.rapidapi.com/forecast"

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "8e9e50a21bmshda23fe83770e19ep14a949jsn482dfa5dc300"
    }

# initialize tkinter GUI
root = Tk()

weather_frame = Frame(root)
weather_frame.grid(columnspan=3, row=3)
weather_view = ttk.Treeview(weather_frame)

# Initialize table for US city weather information
def createTable(data, city):
    weather_view['columns'] = ('city', 'temperature', 'minTemp', 'maxTemp', 'condition', 'description')
    weather_view.column("#0", width=0,  stretch=NO)
    weather_view.column("city",anchor=CENTER, width=85)
    weather_view.column("temperature",anchor=CENTER,width=95)
    weather_view.column("minTemp",anchor=CENTER,width=75)
    weather_view.column("maxTemp",anchor=CENTER,width=75)
    weather_view.column("condition",anchor=CENTER,width=75)
    weather_view.column("description",anchor=CENTER,width=95)

    weather_view.heading("#0",text="",anchor=CENTER)
    weather_view.heading("city",text="City Name",anchor=CENTER)
    weather_view.heading("temperature",text="Temperature (F)",anchor=CENTER)
    weather_view.heading("minTemp",text="Min Temp",anchor=CENTER)
    weather_view.heading("maxTemp",text="Max Temp",anchor=CENTER)
    weather_view.heading("condition",text="Condition",anchor=CENTER)
    weather_view.heading("description",text="Description",anchor=CENTER)
    NewEntry(data, city)

# Populate table with weather information for each new US city
def NewEntry(data, city):
    try:
        temp = str(round((((int(data['list'][1]['main']['temp']) - 273.15) * 1.8) + 32), 2))
        temp_min = str(round((((int(data['list'][1]['main']['temp_min']) - 273.15) * 1.8) + 32), 2))
        temp_max = str(round((((int(data['list'][1]['main']['temp_max']) - 273.15) * 1.8) + 32), 2))
        weather = data['list'][2]['weather'][0]['main']
        weather_desc = data['list'][2]['weather'][0]['description']

        weather_view.insert(parent='',index='end',iid=None,text='',
        values=(city, temp, temp_min, temp_max, weather, weather_desc))
        weather_view.grid(columnspan=3, row=3)

    except:
        weather_view.insert(parent='',index='end',iid=None,text='',
        values=(city, None, None, None, None, None))
        weather_view.grid(columnspan=3, row=3)


root.title("US Weather Tracker")

canvas = Canvas(root, width=600, height=120)
canvas.grid(columnspan=3, rowspan=5)

# Weather Tracker application - title
label = Label(root, text="US Weather Tracker")
label.grid(columnspan=3, row=0, pady=30)
label.configure(font=("Courier", 25, "bold"), fg='#092653')

# Weather Tracker application - title
desc = Label(root, text="Provide a US city name below...")
desc.grid(columnspan=3, row=1, pady=10)
desc.configure(font=("Courier", 10))

# Prompts the user to enter a city
cityLabel = Label(text="City Name:")
cityLabel.grid(column=0, row=2, pady=20)
cityLabel.configure(font=("Courier", 16))

cityEntry = Entry(root, width=50, borderwidth = 2)
cityEntry.grid(column=1, row=2, pady=20)

# Global variables to update button text and check if table exists
newTable = True
button_text = StringVar()
button_text.set("Get Weather");

# Function to add a new city to the list of weather forecasts
def addWeather():
    global newTable
    if newTable == True:
        city = cityEntry.get()
        location = city + ",us"
        querystring = {"q":location}
        response = requests.request("GET", url, headers=headers, params=querystring)
        createTable(response.json(), city)
        button_text.set("Add New City");
        newTable = False
    elif newTable == False:
        city = cityEntry.get()
        location = city + ",us"
        querystring = {"q":location}
        response = requests.request("GET", url, headers=headers, params=querystring)
        NewEntry(response.json(), city)

# Button to add cities to weather forecast table
getCityWeather = Button(root, textvariable=button_text, command=addWeather, width = 30,
font=("Courier", 15), bg='#092653', fg="white").grid(columnspan=3, row=4, pady=10)


root.mainloop()

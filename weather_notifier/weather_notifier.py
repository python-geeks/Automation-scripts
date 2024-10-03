import tkinter as tk
from tkinter import messagebox
import requests
import time
import threading
import os

# Global variable to control the notifier state
notifier_running = False

# Function to get weather data
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    return response.json()

# Function to display weather
def display_weather():
    city = city_entry.get()
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")  # Get API key from environment variable
    if not api_key:
        messagebox.showerror("Error", "API key not found in environment variables")
        return
    
    weather_data = get_weather(api_key, city)
    
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temp_celsius = main["temp"] - 273.15  # Convert from Kelvin to Celsius
        temp_fahrenheit = (temp_celsius * 9/5) + 32  # Convert from Celsius to Fahrenheit
        messagebox.showinfo("Weather Info", f"City: {city}\nTemperature: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F\nDescription: {weather_desc}")
    else:
        messagebox.showerror("Error", "City Not Found")

# Function to run the notifier at fixed intervals
def run_notifier(interval):
    global notifier_running
    while notifier_running:
        display_weather()
        time.sleep(interval)

# Function to start the notifier in a separate thread
def start_notifier():
    global notifier_running
    notifier_running = True
    interval = int(interval_entry.get())
    time_unit = time_unit_var.get()
    
    if time_unit == "Minute(s)":
        interval *= 60
    elif time_unit == "Hour(s)":
        interval *= 3600
    elif time_unit == "Day(s)":
        interval *= 86400
    
    threading.Thread(target=run_notifier, args=(interval,)).start()

# Function to stop the notifier
def stop_notifier():
    global notifier_running
    notifier_running = False

# GUI setup
root = tk.Tk()
root.title("Weather Notifier")

tk.Label(root, text="City:").grid(row=0, column=0)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1)

tk.Label(root, text="Interval:").grid(row=1, column=0)
interval_entry = tk.Entry(root)
interval_entry.grid(row=1, column=1)

time_unit_var = tk.StringVar(value="Second(s)")
time_unit_menu = tk.OptionMenu(root, time_unit_var, "Second(s)", "Minute(s)", "Hour(s)", "Day(s)")
time_unit_menu.grid(row=1, column=2)

tk.Button(root, text="Get Weather", command=display_weather).grid(row=2, column=0)
tk.Button(root, text="Start Notifier", command=start_notifier).grid(row=2, column=1)
tk.Button(root, text="Stop Notifier", command=stop_notifier).grid(row=2, column=2)

root.mainloop()
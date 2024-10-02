import os
from geopy.geocoders import Nominatim
import tkinter as tk
from tkinter import messagebox
import requests
import threading
import time
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
if API_KEY is None:
    raise ValueError(
        "API key not found.  Set the OPENWEATHER_API_KEY in the .env file.")


def calculate_lat_long(city):
    geolocator = Nominatim(user_agent="weather_notifier")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None, None


def get_weather(lat, long):
    try:
        print(lat, long)
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}"
            f"&lon={long}&units=metric&appid={API_KEY}"
        )
        res = requests.get(url)
        data = res.json()
        if data['cod'] != 404:
            weather_info = {
                "City": data.get(
                    "name",
                    "N/A"),
                "Latitude": data['coord']['lat'],
                "Longitude": data['coord']['lon'],
                "Temperature": data['main']['temp'],
                "Feels Like": data['main']['feels_like'],
                "Min Temp": data['main']['temp_min'],
                "Max Temp": data['main']['temp_max'],
                "Pressure": data['main']['pressure'],
                "Humidity": data['main']['humidity'],
                "Wind Speed": data['wind']['speed'],
                "Wind Degree": data['wind']['deg'],
                "Weather": data['weather'][0]['description'].capitalize(),
                "Clouds": f"{data['clouds']['all']}%",
                "Visibility": data.get(
                    'visibility',
                    "N/A"),
                "Sunrise": time.strftime(
                    '%Y-%m-%d %H:%M:%S',
                    time.gmtime(
                        data['sys']['sunrise'] + data['timezone'])),
                "Sunset": time.strftime(
                    '%Y-%m-%d %H:%M:%S',
                    time.gmtime(
                        data['sys']['sunset'] + data['timezone'])),
            }
            return weather_info
        else:
            return None

    except Exception as e:
        messagebox.showerror("Error", f"Error fetching weather data: {str(e)}")
        return None

# updating the weather


def update_weather():
    city = city_entry.get()
    if city:
        lat, lon = calculate_lat_long(city)
        if lat and lon:
            weather_info = get_weather(lat, lon)
            if weather_info:
                weather_info_in_str_to_display = covert_the_info_to_display(
                    weather_info)
                weather_label.config(text=weather_info_in_str_to_display)
                stop_button.pack(pady=5)
                city_label.pack_forget()
                city_entry.pack_forget()
                manual_radio.pack_forget()
                auto_radio.pack_forget()
                start_button.pack_forget()
                interval_label.pack_forget()
                interval_entry.pack_forget()
            else:
                weather_label.config(text="Unable to find coordinates!")
                stop_button.pack_forget()
        else:
            weather_label.config(text="Unable to find coordinates!")
            stop_button.pack_forget()
    else:
        messagebox.showerror("Error", "Please enter a valid city name.")
        stop_button.pack_forget()
#  displaying the info in the tkinter created box


def covert_the_info_to_display(weather_info):
    # Clear the previous text
    weather_info_in_str_to_display = (
        f"City: {weather_info['City']}\n\n"
        f"Coordinates: ({weather_info['Latitude']}, "
        f"{weather_info['Longitude']})\n\n"
        f"Temperature: {weather_info['Temperature']}°C "
        f"(Feels like {weather_info['Feels Like']}°C)\n\n"
        f"Min Temp: {weather_info['Min Temp']}°C, "
        f"Max Temp: {weather_info['Max Temp']}°C\n\n"
        f"Pressure: {weather_info['Pressure']} hPa\n\n"
        f"Humidity: {weather_info['Humidity']}%\n\n"
        f"Wind: {weather_info['Wind Speed']} m/s, "
        f"{weather_info['Wind Degree']}°\n\n"
        f"Clouds: {weather_info['Clouds']}\n\n"
        f"Visibility: {weather_info['Visibility']} meters\n\n"
        f"Weather: {weather_info['Weather']}\n\n"
        f"Sunrise: {weather_info['Sunrise']}\n\n"
        f"Sunset: {weather_info['Sunset']}\n\n"
    )

    return weather_info_in_str_to_display

# run_in_background logic


def run_in_background(interval):
    while auto_mode.get():
        update_weather()
        time.sleep(interval)

#  Function to handle click


def start_notifier():
    if auto_mode.get():
        interval_str = interval_entry.get().strip()
        if not interval_str:
            messagebox.showerror(
                "Error", "Please enter a valid interval (in seconds).")
            return
        try:
            interval = int(interval_str)
            if interval <= 0:
                messagebox.showerror(
                    "Error", "Please enter a valid interval (in seconds).")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return
        start_button.config(state=tk.DISABLED)

        threading.Thread(
            target=run_in_background, args=(
                interval,), daemon=True).start()
    else:
        update_weather()

# Function to stop auto-updating


def stop_notifier():
    auto_mode.set(False)
    start_button.config(state=tk.NORMAL)
    stop_button.pack_forget()
    go_back()


def go_back():
    weather_label.config(text="")
    city_label.pack(pady=10)
    city_entry.pack(pady=5)
    manual_radio.pack(anchor=tk.W, padx=20)
    auto_radio.pack(anchor=tk.W, padx=20)
    start_button.pack(pady=10)
    interval_label.pack_forget()
    interval_entry.pack_forget()
    stop_button.pack_forget()

# gui setup


def show_interval_entry():
    if auto_mode.get():
        interval_label.pack(pady=5)
        interval_entry.pack(pady=5)
    else:
        interval_label.pack_forget()
        interval_entry.pack_forget()


def toggle_stop_button():
    if auto_mode.get():
        stop_button.pack(pady=5)
    else:
        stop_button.pack_forget()


if __name__ == '__main__':
    city = "Surat"
    lat, long = calculate_lat_long(city)
    if lat is None or long is None:
        print('No city found')
        exit(0)

    root = tk.Tk()
    root.title("Weather Notifier")
    root.geometry("550x500")
    root.resizable(False, False)

    # City Label and Entry
    city_label = tk.Label(root, text="Enter your city:")
    city_label.pack(pady=10)
    city_entry = tk.Entry(root, width=30)  # Define city_entry here
    city_entry.pack(pady=5)

    # Weather Info Label
    weather_label = tk.Label(
        root, text="", font=(
            "Helvetica", 10), justify="left")
    weather_label.pack(pady=20)

    # Mode Selection: Manual or Automatic
    auto_mode = tk.BooleanVar()

    manual_radio = tk.Radiobutton(
        root,
        text="On-click only",
        variable=auto_mode,
        value=False)
    manual_radio.pack(anchor=tk.W, padx=20)

    auto_radio = tk.Radiobutton(
        root,
        text="Run after a fixed interval",
        variable=auto_mode,
        value=True)
    auto_radio.pack(anchor=tk.W, padx=20)

    # Interval Entry (only visible when interval mode is selected)
    interval_label = tk.Label(root, text="Enter interval (seconds):")
    interval_entry = tk.Entry(root, width=10)

    auto_mode.trace_add("write", lambda *args: show_interval_entry())

    # Start Button
    start_button = tk.Button(
        root,
        text="Start Notifier",
        command=start_notifier)
    start_button.pack(pady=10)

    # Stop Button (visible only when auto mode is active)
    stop_button = tk.Button(root, text="Stop Notifier", command=stop_notifier)
    stop_button.pack_forget()

    auto_mode.trace_add("write", lambda *args: toggle_stop_button())

    # Run the GUI loop
    root.mainloop()

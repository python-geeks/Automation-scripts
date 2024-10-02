# Weather Notifier - README

# Overview
The ** Weather Notifier ** is a Python - based GUI application built with `Tkinter`, which allows users to retrieve weather information for any city using the OpenWeatherMap API. It provides two modes of operation:
- **Manual Mode**: Fetch the weather on - demand with a single click.
- **Auto Mode**: Fetch the weather at regular intervals and can also run in the background.

The app displays current weather details such as temperature, humidity, wind speed, and more in a user - friendly interface.

# Features
- Fetch current weather for any city globally.
- Switch between manual and automatic weather updates.
- Display detailed weather information, including temperature, humidity, wind, and more.
- Option to stop the automatic weather updates and return to the main city selection screen.

# Prerequisites
1. Python 3.x
2. The following Python libraries:
    - `Tkinter`
    - `requests`
    - `threading`
    - `geopy`
    - `dotenv`

To install the required libraries, use the following command:
```bash
pip install - r requirements.txt
```

# Screenshots
![Main Screen](. / images / box.jpg)
![Error](. / images / error_box.jpg)
![Error](. / images / automated_gui.jpg)
![Error](. / images / data_automated.jpg)

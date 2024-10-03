# Weather Notifier

This script provides a simple GUI application to display weather information for a specified city and can notify the user at regular intervals.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:
    ```sh
    pip install requests
    ```

## Setup

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Set the API key as an environment variable:
    - On Windows:
        ```sh
        setx OPENWEATHERMAP_API_KEY "your_api_key_here"
        ```
    - On macOS/Linux:
        ```sh
        export OPENWEATHERMAP_API_KEY="your_api_key_here"
        ```

## Usage

1. Navigate to the directory containing the script.
2. Run the script:
    ```sh
    python weather_notifier.py
    ```
3. Enter the city name and the interval for notifications.
4. Click "Get Weather" to display the current weather.
5. Click "Start Notifier" to start receiving weather notifications at the specified interval.
6. Click "Stop Notifier" to stop the notifications.

## Features

- Display current weather information for a specified city.
- Notify the user at regular intervals with updated weather information.
- Supports intervals in seconds, minutes, hours, and days.

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API.

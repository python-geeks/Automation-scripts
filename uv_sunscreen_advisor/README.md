# UV Index and Sunscreen Advisor

This Python script fetches the current UV index for a given location and provides personalized sunscreen advice based on the UV index and whether the user is indoors or outdoors.

## Features

- Fetches real-time UV index data based on user-provided latitude and longitude.
- Provides personalized sunscreen advice based on UV exposure:
  - Low UV index: minimal protection recommended.
  - Moderate to extreme UV index: higher SPF and protective measures are suggested.
- Differentiates advice for indoor and outdoor scenarios.

## Requirements

- Python 3.x
- `requests` library for making HTTP API requests.

## Setup

### Install the required libraries:

```bash
pip install requests

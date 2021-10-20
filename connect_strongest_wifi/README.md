# Connect to the Strongest Wi-Fi

## About

The Script can be used to find 3 strongest Wi-Fi's available based on signal strength in Windows OS.

User can then choose one of the networks from the list of 3 Wi-Fi detected and give the password for the same. Once password is provided, the script connects to the Wi-Fi specified.

- Language: Python 3
- Package used: pywifi
- OS: Windows

## Pre-requisites

To execute the script, the following are required:

1. Python 3
2. pip

## Setup instructions

1. Navigate to the directory:

```
cd connect_strongest_wifi
```

2. Install the requirements:

```
pip install -r requirements.txt
```

## Detailed Explanation of Script

When the script is executed, the main function is being invoked which in turns invoke the get_available_wifi(). This function scan through the available Wi-Fi and returns the entire list of it with SSID and their respective signal, in Windows.

In main, slicing till top 3 SSIDs have been done to take the 3 strongest Wi-Fi signals available. Then, the options are displayed for the User to choose from one of them. Once the User chooses a connection, input for password is prompted.

Next, the chosen SSID and the provided password is passed to the connect_wifi() and connection is established with the Wi-Fi.

Note: If the script fails to connect with Wi-Fi even with correct password, try increasing the Sleep time in connect_wifi().

## Execution

Run the script directly with :

```
python connect_strongest_wifi.py
```

When prompted for which Wi-Fi to choose, enter the Option Number with respect to the Wi-Fi name. Enter the password for the same to get connected.

# SCAN PORTS
This Port Scanner will work for both the Web Applications as well as remote Host. This tool has been created to provide the basic functionality of a Port Scanner. The general concept of Sockets had been used to provide the functionality. Port Scanner is built on Python 3 and uses some extra libraries such as socket and pyfigle

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

**Prerequisite**
- python3

**Modules used**
- sys
- socket
- datetime
- pyfiglet

## How to use

> python3 scan_port.py *localhost*
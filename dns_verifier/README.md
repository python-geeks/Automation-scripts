## DNSLU - DNS LOOK UP

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

Domain availability checker (DNS lookup) #138

Usage: 

    python dnslu.py --dns <DNS>


output:

    python dnslu.py --dns google.com
    {
        "DNS": "google.com",
        "IP": [
            "172.217.172.78"
        ],
        "AVAIL": false
    }
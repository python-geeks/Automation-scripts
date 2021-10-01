# Wake on discount 

## Setup and activate virtual environment:
For Unix based systems please execute the following command to create venv and install requirements.
```
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

### Objectives
- [x]  Amazon: almost Finished.
        
        - [x] Twillio: sends sms when the priced equals or less than desired price

- [ ] Flipkart: Need time to invest.

- [ ] Any Smiliar: Please [open an issue](https://github.com/python-geeks/Automation-scripts/issues/new/choose) if you want to extend the idea!


### Requirements
- Twilio account and API Access
- Python
- Docker :+1:

#### USAGE:
##### Using Local/Remote machine:
This compatible with Linux and OSx
```
$export ACCOUNT_SID="bzPFSbOiL0t3ZQ10LO1NwHHy7tAZUxZ2IuHwSYej"
$export AUTH_TOKEN="fWXgfraSQ0iOQCwkRErVa9PLb7QcjOxCRYFeCHAcX8DwjeHOG0"
$export URL="https://www.amazon.de/Web-Scraping-Python-Collecting-Modern/dp/1491985577/"
```

##### Using Docker-Container
Build the Docker Image
```
docker build -t wake-on-discount .
```

Run the Docker Image
```
docker run -it -e CONSUMER_KEY="<Cosumer Key>" \
 -e ACCOUNT_SID="<Account SID>" \
 -e AUTH_TOKEN="<Authentication Token>" \
 -e URL="amazon_url" \
 wake-on-discount
```

suggestions: Please open an issue and tag me @ashkankamyab


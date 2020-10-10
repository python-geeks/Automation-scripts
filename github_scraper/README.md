# Github users scrapper

```bash
usage: scrapper.py [-h] [--json] user

Fetch information about Github user.

positional arguments:
  user        User that you want to look up into.

optional arguments:
  -h, --help  show this help message and exit
  --json      Output data in json format
```

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## Example usage
```bash
$ python3 scrapper.py python-geeks
```
# Broken Link Finder

Script helps to identify each hyperlink in a website if it leads somewhere or is broken i.e. ends up at "ERROR 404: Page not found" page </br>
The website which needs to be searched for a broken link is provided as an argument to the script while running.

## Setup and activate virtual environment

For Unix based systems please execute the following command to create venv and install requirements.

```
make init
source .venv/bin/activate
```

## Usage

```
python broken_linkfinder.py [url]
```

## Example

![Capture.png](Capture.png)

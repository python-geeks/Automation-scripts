# YouTube Thumbnail Grabber

Get the thumbnail from a YouTube video

## Setup and activate virtual environment:
For Unix based systems, execute the following commands to create a virtual environment and install requirements

```
make init
source .venv/bin/activate
```

## How to use
```
$ python ytthumbnail.py [-h] [URL] [-n]
```

If no URL is selected, no new file will be created.

```
Arguments:
    -h      Show help message and exit
    URL     URL of video to grab thumbnail of
    -n      The desired filename of the resulting thumbnail
```

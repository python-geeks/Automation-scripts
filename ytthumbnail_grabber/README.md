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
$ python ytthumbnail_grabber.py [-h] [-n NAME] URL
```

```
Postional Arguments:
    URL     URL of video to grab thumbnail of
```

```
Optional Arguments:
    -h, --help      Show help message and exit
    -n NAME, --name NAME      The desired filename of the resulting thumbnail (default = 'thumbnail.jpg')
```

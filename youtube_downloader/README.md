# YouTube Downloader

Basic automation script for download youtube hosted videos.

## Setup

For Unix based systems please execute the following command to create venv and install requirements :

```bash
make init
source .venv/bin/activate
```

## Usage

This script can download YouTube videos in different resolutions, with captions (if available).

```bash
python ytdownloader.py <YOUTUBE_VIDEO_URL> [OPTIONS]
```

```bash
positional arguments:
  URL                   Youtube video URL

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Destination file path
  -c CAPTIONS, --captions CAPTIONS
                        Captions lang to download (if exists)
  -r RES, --res RES     Resolution to download (if exists)
  -v VERBOSE, --verbose VERBOSE
                        Show information about script processing
```

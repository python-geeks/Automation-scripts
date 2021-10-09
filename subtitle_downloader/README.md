# Subtitle Downloader
```
This folder contains a python3 script to download subtitles from youtube videos, provided that they have subtitles.
```

# Requirements
1. youtube_transcript_api
        
```
pip install youtube_transcript_api
```
<p align='center'>or</p>

```
pip install -r requirements.txt
```

# How this script works
* Just execute the subtitle_downloader.py file with the youtube video link as a command line argument 
    
```
python subtitle_downloader.py <video link>
```

* A new file named subtitle.txt is created in the same directory.

* This file contains the subtitles of the video given as argument along with timestamps.
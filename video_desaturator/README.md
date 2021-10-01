# video_desaturator
Simple command line utility to alter the saturation level of videos
## Installing the Dependencies
This program requires `ffmpeg` to run.  
It also requires that `ffmpeg` be added to your PATH

You can usually download it on any Linux distro through your package manager.
On Windows you can download builds from [the FFMPEG official downloads page](https://ffmpeg.org/download.html) and then add `ffmpeg` to your PATH.
[This tutorial](https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10) tells you how.

## Usage
```
$ python video_desaturator.py --help
usage: video_desaturator.py [-h] [-l LEVEL] [-y] in_file out_file

positional arguments:
  in_file               the file to desaturate
  out_file              the file to output to

optional arguments:
  -h, --help            show this help message and exit
  -l LEVEL, --level LEVEL
                        the saturation percentage to use (default: 0, max: 300)
  -y, --yes             skip the prompt to overwrite the file
```

Set a video's saturation level to 0% (black and white)
```
python video_desaturator.py example.mp4 example-out.mp4
```
Set a video's saturation level to 50%
```
python video_desaturator.py example.mp4 -l 50 example-out.mp4
```
Set a video's saturation level to 100% (no change)
```
python video_desaturator.py example.mp4 -l 100 example-out.mp4
```
Set a video's saturation level to 300%
```
python video_desaturator.py example.mp4 -l 300 example-out.mp4
```
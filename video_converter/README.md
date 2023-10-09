# video_converter

Simple command line utility to convert any format videos to .mp4

## Installing the Dependencies

This program requires `ffmpeg` and `ffmpeg-python` to run.  
It also requires that `ffmpeg` be added to your PATH

For `ffmpeg-python` run:

```
pip3 install ffmpeg-python
```

For `ffmpeg` you can usually download it on any Linux distro through your package manager.
On Windows you can download builds from [the FFMPEG official downloads page](https://ffmpeg.org/download.html) and then add `ffmpeg` to your PATH.
[This tutorial](https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10) tells you how.

## Usage

```
$ python video_converter.py --help
usage: video_converter.py [-h] [-i INPUT] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        the file to convert
  -o OUTPUT, --output OUTPUT
                        the file to output to (cannot be the same as input file)
```

Convert a .avi video to .mp4

```
python video_converter.py -i video.avi
```

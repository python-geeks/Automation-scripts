# video_cropper
Simple command line utility to crop videos
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
$ python video_cropper.py --help
usage: video_cropper.py [-h] [-i INPUT] [-c CROP] [-t TOP] [-b BOTTOM] [-l LEFT] [-r RIGHT] [-o OUTPUT] [-y]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        the file to crop
  -c CROP, --crop CROP  the amount to crop (pixels or percent) in the format "TOP,BOTTOM,LEFT,RIGHT"
  -t TOP, --top TOP     the amount to crop (pixels or percent) off the top of the video
  -b BOTTOM, --bottom BOTTOM
                        the amount to crop (pixels or percent) off the bottom of the video
  -l LEFT, --left LEFT  the amount to crop (pixels or percent) off the left of the video
  -r RIGHT, --right RIGHT
                        the amount to crop (pixels or percent) off the right of the video
  -o OUTPUT, --output OUTPUT
                        the file to output to (cannot be the same as input file)
  -y, --yes             skip the prompt to confirm overwriting a file
```

Crop 50 pixels off of each side of the video
```
python video_cropper.py -i example.mp4 -c 50,50,50,50 -o example_cropped.mp4
```
Crop 10% off of each side of the video
```
python video_cropper.py -i example.mp4 -c 10%,10%,10%,10% -o example_cropped.mp4
```
Crop 10 pixels off of the top and bottom
```
python video_cropper.py -i example.mp4 -t 10 -b 10 -o example_cropped.mp4
```
Crop 15 pixels off of the left and right
```
python video_cropper.py -i example.mp4 -l 15 -r 15 -o example_cropped.mp4
```
Crop 30 pixels off the top and 12 pixels off the right
```
python video_cropper.py -i example.mp4 -t 30 -r 12 -o example_cropped.mp4
```
Crop 10% off the top
```
python video_cropper.py -i example.mp4 -t 10% -o example_cropped.mp4
```
Crop 10% off the left and 20 pixels off the right
```
python video_cropper.py -i example.mp4 -l 10% -r 20 -o example_cropped.mp4
```
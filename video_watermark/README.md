# Automating watermarking video
This is a pretty short python script which is used to easily watermark video.
In order to use it please check out [usage](#usage)

## Usage
First, Install the required dependencies:
```sh
python -m pip install moviepy
```

Secondly, make sure you've installed ImageMagick and ffmpeg (If you have any troubles, Please check [Troubleshooting](#Troubleshooting))

Thirdly, run the following command in terminal:
```sh
python main.py -p <path to file> -t <watermark text> -f <watermark text font> -c <text color> -s <fontsize>
```
** Don't forget to change the variables according to your requirements.

## Troubleshooting
Here I wrote a few problems that I stalked with at the moment of building this program, and how to fix it.
Firstly, if you get such error:
```sh
OSError: MoviePy Error: creation of None failed because of the following error:

[WinError 2] The system cannot find the file specified.

.This error can be due to the fact that ImageMagick is not installed on your computer, or (for Windows users) that you didn't specify the path to the ImageMagick binary in file conf.py, or that the path you specified is incorrect
```
Then, make sure you downloaded ImageMagick, and ffmpeg using the following command for linux:
```sh
sudo apt-get install ffmpeg imagemagick
```
Or download the files from the following websites (Sometimes, Downloading ImageMagick will also recommend you downloading ffmpeg, so you can download only ImageMagick or both of them and uncheck the ffmpeg in the ImageMagick installation dialog):
* [ffmpeg](https://ffmpeg.org/download.html#build-windows) - Make sure you download the Binary and NOT the source code.
* [ImageMagick](https://imagemagick.org/script/download.php#windows) - Make sure you download the Windows Version.

For windows users only:
Go to your Python installation folder, from there go to "Lib", from there go to "site-packages" and from there search for "moviepy" once there, open the "config-defaults.py" file using an IDE / Notepad, and make sure to change the "auto-detect" in `IMAGEMAGICK_BINARY` to the path to ImageMagick binary.

## Issues
If you still have issues even after following the troubleshooting steps, please open an issue / contact me [GitHub - maxily1](https://github.com/maxily1)
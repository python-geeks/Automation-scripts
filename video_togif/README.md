# Video to GIF converter

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

Utility to convert video files to animated GIFs. Supports many video formats and the conversion quality is configurable.

Requires MoviePy, which should work in Python 2.7+ and 3. During installation, imageio and FFMPEG should be automatically
configured. These two modules are required for the conversion. Moreover, for video scaling, at least one of Scipy,
PIL, Pillow or OpenCV are needed.

Can be used as a script (`python video2gif.py`) or imported into other projects by using the `convert2gif()` function. It
requires a filename for the original video, and optionally a conversion quality and resulting filename (must end with .gif).

Conversion quality can be one of the built-in options or can be manually configured. The default is `MediumQuality()`.

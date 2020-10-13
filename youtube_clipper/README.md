# Youtube Clipper
Youtube Clipper downloads a video clip from youtube from starting time to ending time told by the user without downloading the whole video.
## Installing the Dependencies:
Install these two packages: ffmpeg and youtube_dl

For youtube_dl type the following command in terminal:
```cmd
pip install youtube_dl
```
For ffmpeg install it according to your OS

After installing them check whether both of them have been installed correctly by just typing 'ffmpeg' and 'youtube_dl' on terminal

## Steps to download the video
Run the script ```youtube_clip.py``` on terminal
```
python youtube_clip.py
```
After executing the script you will be asked for the link of the video, start time of the clip, end time of the clip and name of the output video

First you will be asked about the link of the youtube video you want to download as shown below:
```
Enter the Youtube video link:
```
Sample Input:
```
Enter the Youtube video link: https://www.youtube.com/watch?v=hlWiI4xVXKY&ab_channel=SoothingRelaxation
```
Now you will be asked to enter the start time of your video clip as shown below:
```
Enter start time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format:
```
Sample Input:
```
Enter start time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format: 1:23
```
Now you will be asked to enter the end time of your video clip as shown below:
```
Enter end time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format:
```
Sample Input:
```
Enter end time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format: 1:23:45
```
Then you will be asked to name your output video file as shown below:
```
Enter your output video name:
```
Sample Input:
```
Enter your output video name: Relaxing_Video
```
Now your youtube video will be downloaded from start time to end time with the name of output file name you gave.

## Note: This script works only for videos with mp4 format as most of the youtube videos have that link

# importing the packages
import subprocess


# function that returns time in seconds
def time_manipulation(time):
    if len(time) == 1:
        time = "00:00:0" + time
    if len(time) == 2:
        time = "00:00:" + time
    if len(time) == 4:
        time = "00:0" + time
    if len(time) == 5:
        time = "00:" + time
    if len(time) == 7:
        time = "0" + time
    h, m, s = time.split(':')
    time = int(h) * 3600 + int(m) * 60 + int(s)
    return time


youtube_link = input("Enter the Youtube video link: ")
start_time = input("Enter start time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format: ")
start_time = time_manipulation(start_time)  # start time in seconds
end_time = input("Enter end time of the video clip in HH:MM:SS|H:MM:SS|MM:SS|M:SS|SS|S format: ")
end_time = time_manipulation(end_time)  # end time in seconds
duration = end_time - start_time
Output_file_name = input("Enter your output video name: ")
Output_file_name = Output_file_name + '.mp4'

# Error-1
if duration <= 0:
    print("ERROR: Start time should be less than End time")
    quit()

# calculating the length of youtube video in seconds
duration_of_video = subprocess.run(["youtube-dl", "--no-check-certificate", "--get-duration", youtube_link],
                                   stdout=subprocess.PIPE, text=True)
video_length = duration_of_video.stdout
video_length = video_length[:-1]
video_length = time_manipulation(video_length)  # video length in seconds

# Error-2
if end_time > video_length:
    print("ERROR: End time should be less than the Length of video")
    quit()

# removing the channel name from link if it is present
for ch in youtube_link:
    if ch == '&':
        youtube_link = youtube_link[:youtube_link.index(ch)]

# getting the download link of the youtube video
download_link = subprocess.run(["youtube-dl", "--no-check-certificate", "-f", "22", "--get-url", youtube_link],
                               stdout=subprocess.PIPE, text=True)
link = download_link.stdout

# downloading the video from start_time to end_time
subprocess.run(["ffmpeg", "-ss", str(start_time), "-i", link, "-t", str(duration), "-c:v", "copy", "-c:a",
                "copy", Output_file_name])

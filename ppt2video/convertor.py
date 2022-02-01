import win32com.client
import os
import sys

# PpSaveAsFileType enumeration (PowerPoint)
ppSaveAsMP4	 = 39

def ppt2video(pptx, video, timing, duration, resolution, frames, quality):

    # Check if system requirements are met.
    if sys.platform == "win32":
        pass
    else:
        print("Sorry, this script can be run only on Windows.")

    # Create fill pathes for the ppt and video files.
    ppt_path = os.path.abspath(pptx)
    video_path = os.path.abspath(video)

    # Presentation object
    # https://docs.microsoft.com/en-us/office/vba/api/powerpoint.presentation
    ppt = win32com.client.Dispatch("PowerPoint.Application")

    # Open presentation
    presentation = ppt.Presentations.Open(ppt_path, WithWindow=False)

    # Presentation.CreateVideo method (PowerPoint)
    # https://docs.microsoft.com/en-us/office/vba/api/powerpoint.presentation.createvideo
    presentation.CreateVideo(video_path, timing, duration, resolution, frames, quality)
    while True:
        try:
            # Update the video file, if already exists.
            os.rename(video_path, video_path)
            print(f'The video from PowerPoint Presentation {pptx} has been created.')
            break
        except Exception:
            pass
    presentation.Close()
    ppt.Quit()
    pass

if __name__ == '__main__':
    file_name = "test.pptx" # PPT file expected to be in the root folder
    video_name = "test_video" # Video will be created in the root folder
    UseTimingsAndNarrations =  False # Boolean value
    DefaultSlideDuration = 2  # Int
    VertResolution =  480 # Int
    FramesPerSecond =  24 # Int
    Quality = 60

    ppt2video(f"./{file_name}", f"./{video_name}.mp4",
              UseTimingsAndNarrations, DefaultSlideDuration, VertResolution, FramesPerSecond, Quality)
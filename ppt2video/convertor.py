import win32com.client
import os
import sys

# PpSaveAsFileType enumeration (PowerPoint)
ppSaveAsMP4 = 39
# PpSlideLayout enumeration (PowerPoint)
ppLayoutText = 6
# msoShapeRectangle
msoShapeRectangle = 1


def ppt2video(pptx, video, timing, duration,
              resolution, frames, quality, dict):

    # Check if system requirements are met.
    if sys.platform == "win32":
        pass
    else:
        print("Sorry, this script can be run only on Windows.")

    # Create files pathes for the ppt and video files.
    ppt_path = os.path.abspath(pptx)
    video_path = os.path.abspath(video)

    # Presentation object
    # https://docs.microsoft.com/en-us/office/vba/api/powerpoint.presentation
    ppt = win32com.client.Dispatch("PowerPoint.Application")

    # Open presentation
    presentation = ppt.Presentations.Open(ppt_path, WithWindow=False)

    new_presentation = ppt.Presentations.Add(WithWindow=False)

    # Compare input and slides by indexes, creating lists and comparing them
    keys = [int(key) for key, value in dict.items()]
    slides = [slide.SlideIndex for slide in presentation.Slides]
    # List of indexes with user input texts.
    list = [key for key in keys if key in slides]

    # Slides indexes start with 1
    for slide in presentation.Slides:
        # Checking if user provided input
        if slide.SlideIndex in list:
            # Create new slide with new text
            len_new_ppt = len(new_presentation.Slides)
            new_slide = new_presentation.Slides.Add(len_new_ppt + 1,
                                                    ppLayoutText)
            new_slide.Shapes.addShape(
                msoShapeRectangle, 150, 150, 250, 250). \
                TextFrame.TextRange.Text = dict.get(str(slide.SlideIndex))
            # Copying slide from original presentation and adding it new one.
            slide.Copy()
            len_new_ppt = len(new_presentation.Slides)
            new_presentation.Slides.Paste(len_new_ppt + 1)
        else:
            # Adding slide to new presentation without user provided text
            slide.Copy()
            len_new_ppt = len(new_presentation.Slides)
            new_presentation.Slides.Paste(len_new_ppt + 1)

    # Presentation.CreateVideo method (PowerPoint)
    # https://docs.microsoft.com/en-us/office/vba/api/powerpoint.presentation.createvideo
    new_presentation.CreateVideo(video_path, timing, duration,
                                 resolution, frames, quality)
    while True:
        try:
            # Update the video file, if already exists.
            os.rename(video_path, video_path)
            print(f'The video from {pptx} has been created.')
            break
        except Exception:
            pass
    new_presentation.Close()
    presentation.Close()
    ppt.Quit()
    pass


if __name__ == '__main__':
    # e.g.:test.pptx, file expected to be in the root folder
    file_name = ""
    # e.g.: test_video, will be created in the root folder
    video_name = ""
    UseTimingsAndNarrations = False  # Boolean value
    DefaultSlideDuration = 2  # Int
    VertResolution = 720  # Int
    FramesPerSecond = 24  # Int
    Quality = 60  # Int

    # User Input is in dictionary format. The keys in the dict represent the
    # number of the slides in the presentation.
    # Slides indexes, and input_dict as well, start with 1, "first slide", e.g.
    # {"1":"input before slide number 1, the first slide",
    #  "2":"input before slide number 2, the second slide",
    #  "4":"input before slide number 4, the forth slide"}
    # You can choose to what slides to add precending text and what slides
    # to leave without additional input.
    input_dict = {}

    ppt2video(f"./{file_name}", f"./{video_name}.mp4",
              UseTimingsAndNarrations,
              DefaultSlideDuration, VertResolution,
              FramesPerSecond, Quality, input_dict)

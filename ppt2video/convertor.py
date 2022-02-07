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
              resolution, frames, quality, input_list, dict):

    # Check if system requirements are met.
    if sys.platform == "win32":
        pass
    else:
        print ("Sorry, this script can be run only on Windows.")

    # Create files pathes for the ppt and video files.
    ppt_path = os.path.abspath(pptx)
    video_path = os.path.abspath(video)

    # Presentation object
    # https://docs.microsoft.com/en-us/office/vba/api/powerpoint.presentation
    ppt = win32com.client.Dispatch("PowerPoint.Application")

    # Open presentation
    presentation = ppt.Presentations.Open(ppt_path, WithWindow=False)

    # slides_len = len(presentation.Slides)

    # powerpoint = win32com.client.Dispatch('PowerPoint.Application')
    new_presentation = ppt.Presentations.Add(WithWindow=False)
    # slides = new_presentation.Slides
    # presentation.Slides[1].Copy()
    # new_presentation.Slides.Paste(1)
    # graphSlideID = gslides.Add(2, ppLayoutChart).SlideID
    # slides.FindBySlideID(graphSlideID)

    # Slides indexes start with 1
    for slide in presentation.Slides:
        for key, value in dict.items():
            if slide.SlideIndex == int(key) and value != "":
                len_new_ppt = len(new_presentation.Slides)

                # print(" slide.SlideIndex == key", slide.SlideIndex)

                new_slide = new_presentation.Slides.Add(
                            len_new_ppt+1, ppLayoutText)
                new_slide.Shapes.addShape(
                    msoShapeRectangle, 150, 150, 250, 250). \
                    TextFrame.TextRange.Text = value
                # print("added new slide at position", len_new_ppt+1)
                slide.Copy()
                new_presentation.Slides.Paste(len_new_ppt+1)
                # print("copied old slide, at position", slide.SlideIndex,
                #     len_new_ppt+2)
            # else:
            #     slide.Copy()
            #     new_presentation.Slides.Paste(len_new_ppt+1)
            #     print("copied old slide, at position", slide.SlideIndex,
            #         len_new_ppt+2)

    print("new presentation", len(new_presentation.Slides))

    # while input_list:
    #     if len(input_list) == slides_len:
    #         n = 1  # To track the slide number to be created
    #         x = 0  # Index in the user input list
    #         while x < slides_len:
    #             # Create slide and insert it at n position with
    #             # input_list[x] text
    #             slide = presentation.Slides.Add(n, ppLayoutText)
    #             slide.Shapes.addShape(
    #                 msoShapeRectangle, 150, 150, 250, 250). \
    #                 TextFrame.TextRange.Text = input_list[x]
    #             n += 2
    #             x += 1
    #         break
    #     else:
    #         print("The length of input data should be equal to the \
    #             slides count")
    #         break

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
    file_name = "presentation.pptx"  # e.g.:test.pptx, file expected to be in the root folder
    video_name = "presentation_video"  # e.g.: test_video, will be created in the root folder
    UseTimingsAndNarrations = False  # Boolean value
    DefaultSlideDuration = 2  # Int
    VertResolution = 720  # Int
    FramesPerSecond = 24  # Int
    Quality = 60  # Int
    # A list of user input text to insert before slides, starts with
    # the first slide. You can leave it blank and no additional
    # slides will be inserted in the video.
    user_input_list = []
    # key in the dict represents the index of the slides in the presentation
    # to be converted into video. Slides indexes start with 1, "first slide".
    input_dict = { "1":"input index 1",
                  "2":"input index 2", "4":"input index 4", "5":"input index 5",
                  "10":"input index 10",}

    ppt2video(f"./{file_name}", f"./{video_name}.mp4",
              UseTimingsAndNarrations,
              DefaultSlideDuration, VertResolution,
              FramesPerSecond, Quality, user_input_list, input_dict)

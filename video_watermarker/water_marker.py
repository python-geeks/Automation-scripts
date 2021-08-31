# Made by MiTo0o (https://github.com/MiTo0o/)

# Import moviepy
import moviepy.editor as mp

# Creating a VideoFileClip object using the input video
video = mp.VideoFileClip("input.mp4")

# Declaring a couple different constraints for the watermarker
mark = (mp.ImageClip("mark.png")
          .set_duration(video.duration)
          .resize(height=100)
          .margin(right=8, top=8, opacity=0)
          .set_pos(("right", "bottom")))

# Combining the watermark with the video
final = mp.CompositeVideoClip([video, mark])

# Writes the edited video to a file
final.write_videofile("output.mp4", audio_codec='aac')

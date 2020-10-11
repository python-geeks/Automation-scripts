# Made by Maxim Iliouchenko (https://github.com/maxily1)

# Importing Libraries
from moviepy.editor import *
import argparse

# Creating an argument parser
parser = argparse.ArgumentParser(description='Process video path and data')

# Adding arguments
parser.add_argument('-p', type=str, required=True, help="File Name")
parser.add_argument('-t', type=str, required=True, help="Watermark Text")
parser.add_argument('-f', type=str, required=True, help="Watermark Text Font")
parser.add_argument('-c', type=str, required=True, help="Watermark Text Color")
parser.add_argument('-s', type=int, required=True, help="Font size")

# Parsing Args
args = parser.parse_args()

# Defining the args into variables
file_name = args.p
watermark_text = args.t
font_choice = args.f
color_choice = args.c
font_size = args.s

# Start of code
clip = VideoFileClip(file_name, audio=True)
w, h = clip.size

# A clip with a text, and semi-opaque bg
text = TextClip(
    watermark_text, font=font_choice,
    color=color_choice, fontsize=font_size
    )
text_col = text.on_color(
    size=(clip.w+text.w, text.h-10),
    color=(0, 0, 0), pos=(6, 'center'), col_opacity=0.6
    )



# Save the file
final_clip = CompositeVideoClip([clip, text_col])
final_clip.duration = clip.duration
final_clip.write_videofile("Output.mp4", fps=24, codec='libx264')

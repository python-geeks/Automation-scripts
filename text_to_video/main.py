import os
import textwrap

import cv2
from PIL import Image, ImageDraw, ImageFont


def create_image(text, font, index=0, image_size=(1920, 1080),
                 bg_color=(255, 255, 255), font_color=(0, 0, 0),
                 save_location="./resource/tmp"):
    font_size = font.size
    # text treatment
    text = textwrap.wrap(text, width=font_size)
    # drawing text on image
    MAX_W, MAX_H = image_size
    img = Image.new('RGB', image_size, bg_color)
    draw = ImageDraw.Draw(img)
    # drawing lines in text with padding
    current_h, pad = MAX_H / 2 - ((len(text) * font_size / 2)), 10
    for line in text:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h),
                  line, font=font, fill=font_color)
        current_h += h + pad
    # saving image
    path = f"{save_location}/{index}.png"
    img.save(path)
    return path


def get_file_content(file_name):
    try:
        file = open(file_name, 'r')
        lines = file.read().split('\n')
        return lines
    except Exception as e:
        print(e)


def create_frames(images, fps=10, duration_per_frame=3):
    img_array = []
    for filename in images:
        img = cv2.imread(filename)
        for i in range(fps * duration_per_frame):
            img_array.append(img)
    return img_array


def create_video_from_frames(frames, dimensions, output_file, fps=10):
    try:
        video = cv2.VideoWriter(
            output_file, cv2.VideoWriter_fourcc(*'DIVX'), fps, dimensions)
        for frame in frames:
            video.write(frame)
        video.release()

    except Exception as e:
        print(e)


def remove_temp_files(files):
    for file in files:
        os.unlink(file)


if __name__ == "__main__":
    # create images from text
    dimensions = (1920, 1080)
    fps = 1
    font_size = 50
    font = ImageFont.truetype('./resource/Urbanist.ttf', font_size)
    sentences = get_file_content("input.txt")
    images = []
    for idx, sentence in enumerate(sentences):
        imagePath = create_image(
            sentence, font, idx + 1, image_size=dimensions)
        images.append(imagePath)
    # read all images
    frames = create_frames(images, fps=fps, duration_per_frame=1)
    create_video_from_frames(frames, dimensions, "output.mp4", fps=fps)
    remove_temp_files(images)

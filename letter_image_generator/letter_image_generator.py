from PIL import Image, ImageDraw, ImageFont
from typing import Tuple
import os
import random


def letter_image_generator(letter: str, width: int = 480,
                           height: int = 480) -> Image:
    def random_color_generator() -> Tuple:
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255), )

    img = Image.new(mode="RGB", size=(width, height),
                    color=random_color_generator())
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.join("fonts", "OpenSans-Bold.ttf"),
                              size=height // 2)
    w, h = draw.textsize(letter, font=font)
    draw.text(((width - w) / 2, (height - h) / 4), letter,
              (255, 255, 255,), font=font)
    return img


if __name__ == "__main__":
    try:
        os.mkdir("images")
    except FileExistsError:
        pass

    for _ in range(65, 91):
        letter = chr(_)
        img = letter_image_generator(letter)
        img.save(os.path.join("images", f"{letter}.png"), format="png")

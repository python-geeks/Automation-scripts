import os

from moviepy.editor import VideoFileClip


class ConversionQuality:
    def __init__(self, scale, fps, program):
        self.scale = scale
        self.fps = fps
        self.program = program


class HighestQuality(ConversionQuality):
    """
    Requires imageio module
    """
    def __init__(self):
        ConversionQuality.__init__(self, 1.0, 12, "imageio")


class MediumQuality(ConversionQuality):
    def __init__(self):
        ConversionQuality.__init__(self, 0.6, 12, "ffmpeg")


class LowQuality(ConversionQuality):
    def __init__(self):
        ConversionQuality.__init__(self, 0.2, 8, "ffmpeg")


def convert2gif(path, quality=MediumQuality(), out_filename=None):
    filename, _ = os.path.splitext(path)
    with (VideoFileClip(path).resize(quality.scale)) as clip:
        if not out_filename:
            out_filename = filename + ".gif"
        clip.write_gif(out_filename, fps=quality.fps, program=quality.program)
        return out_filename


if __name__ == '__main__':
    file = input("Write the file name: ")
    result = convert2gif(file)
    print("Generated GIF at " + result)

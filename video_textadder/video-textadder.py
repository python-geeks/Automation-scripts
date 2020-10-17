from moviepy.editor import CompositeVideoClip, VideoFileClip
from moviepy.video.VideoClip import TextClip
import os
import argparse

# Define the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '-f',
    type=str,
    help='The file path of target video. '
    + 'ex. /home/user/example.mp4.\nDefault value is "demo.mp4"',
    default=base_dir + '/demo.mp4'
)
parser.add_argument(
    '-t',
    type=str,
    help='The text you want to add to video top. '
    + 'ex. "Hellow Video"',
    default='This is demo example'
)
parser.add_argument(
    '-s',
    type=int,
    help='The font size of video watermark. '
    + 'ex. 30',
    default='30'
)
parser.add_argument(
    '-n',
    type=str,
    help='The new file name.\n'
    + 'Default value is {current file name}_title.mp4',
)

# Define Variable
args = parser.parse_args()
video_path = args.f
video_watermark = args.t
font_size = args.s

# Check whether or not the input video path is valid. If not, ask user to input again.
while True:
    try:
        video = VideoFileClip(video_path)
        print('video resultion: ', video.size)
        break
    except Exception:
        print(
            'Directory or file is not valid,'
            + ' please enter a valid file directory ...')
        video_path = str(input('Enter the video path again (absolute path without space): '))

origin_file = (lambda x: x.split('/')[-1])(video_path)

if args.n:
    new_file = args.n
else:
    new_file = f'{origin_file.split(".")[0]}_title.{origin_file.split(".")[1]}'


def add_text(content, font_size):
    '''
    add text on the top of video stream
    '''
    txt_clip = (TextClip(content, fontsize=font_size, color='white')
                .set_position('top')
                .set_duration(video.duration))
    result = CompositeVideoClip([video, txt_clip])
    result.write_videofile(new_file)


def main():
    add_text(video_watermark, font_size)


if __name__ == '__main__':
    main()

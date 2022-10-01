from moviepy.editor import VideoFileClip
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
    '-n',
    type=str,
    help='The new file name.\n'
    + 'Default value is {current file name}_noAudio.mp4',
)

args = parser.parse_args()
audio_path = args.f

# Check whether or not the input video path is valid. If not, ask user to input again.
while True:
    try:
        VideoFileClip(audio_path)
        break
    except Exception:
        print(
            'Directory or file is not valid,'
            + ' please enter a valid file directory ...')
        audio_path = str(input('Enter the video path again (absolute path without space): '))

origin_file = (lambda x: x.split('/')[-1])(audio_path)

if args.n:
    new_file = args.n
else:
    new_file = f'{origin_file.split(".")[0]}_noAudio.{origin_file.split(".")[1]}'


def remove_audio(audio):
    '''
    main function to remove audio from input video
    '''
    video = VideoFileClip(audio)
    video = video.without_audio()
    video.write_videofile(os.path.join(base_dir, new_file))


def main():
    remove_audio(audio_path)


if __name__ == '__main__':
    main()

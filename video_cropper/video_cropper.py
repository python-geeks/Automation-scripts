import ffmpeg
import argparse
import sys
import os


def to_int(a, rel_to):
    '''
    Converts string to integer.

    If string contains "%" it converts it to a float and multiplies by rel_to
    EG: 50% -> 0.5*rel_to
    '''
    if isinstance(a, int):
        return a
    else:
        if '%' in a:
            return int((int(a.replace('%', '')) / 100) * rel_to)
        else:
            return int(a)


if __name__ == '__main__':
    # set up the arguments to be parsed
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', type=str, help='the file to crop')
    parser.add_argument(
        '-c',
        '--crop',
        type=str,
        help='the amount to crop in the format "TOP,BOTTOM,LEFT,RIGHT"')
    parser.add_argument(
        '-t',
        '--top',
        type=str,
        help='the amount to crop off the top of the video')
    parser.add_argument(
        '-b',
        '--bottom',
        type=str,
        help='the amount to crop off the bottom of the video')
    parser.add_argument(
        '-l',
        '--left',
        type=str,
        help='the amount to crop off the left of the video')
    parser.add_argument(
        '-r',
        '--right',
        type=str,
        help='the amount to crop off the right of the video')
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='the file to output to (cannot be the same as input file)')
    parser.add_argument(
        '-y',
        '--yes',
        action='store_true',
        help='skip the prompt to confirm overwriting a file')

    args = parser.parse_args()

    # check whether the user is using the --crop arg
    # or a combination of the --left, --right, --top, --bottom args
    if args.crop is not None:
        args.crop = args.crop.split(',')
        if len(args.crop) == 4:
            # check it is the right length
            crop = {
                'top': args.crop[0],
                'bottom': args.crop[1],
                'left': args.crop[2],
                'right': args.crop[3]
            }
        else:
            # if the length is not 4 then the format is not supported
            sys.stderr.write(
                'ERROR: crop arg must be in the format "TOP,BOTTOM,LEFT,RIGHT"'
            )
            sys.exit(1)
    else:
        # parse all of the other possible crop kwargs
        crop = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        if args.top:
            crop['top'] = args.top
        if args.bottom:
            crop['bottom'] = args.bottom
        if args.left:
            crop['left'] = args.left
        if args.right:
            crop['right'] = args.right
        # if no values were supplied all crops will equal 0
        if all(i == 0 for i in crop.values()):
            sys.stderr.write('ERROR: no crop applied. All crops equal to 0')
            sys.exit(1)

    # validate that args.input is a file
    if args.input is None or not os.path.isfile(args.input):
        sys.stderr.write('ERROR: input file does not exist')
        sys.exit(1)

    # find the video data for the input file
    # and find it's default video stream (the first one)
    metadata = ffmpeg.probe(args.input)
    vid_stream = None
    for stream in metadata['streams']:
        if stream['codec_type'] == 'video':
            vid_stream = stream
            break

    # if no video stream has been found we cannot crop it
    if vid_stream is None:
        sys.stderr.write('ERROR: could not find valid video stream in file')
        sys.exit(1)

    # convert all crop values to an integer
    crop['top'] = to_int(crop['top'], vid_stream['height'])
    crop['bottom'] = to_int(crop['bottom'], vid_stream['height'])
    crop['left'] = to_int(crop['left'], vid_stream['width'])
    crop['right'] = to_int(crop['right'], vid_stream['width'])

    # calculate the new width and height of the video
    width = vid_stream['width'] - (crop['left'] + crop['right'])
    height = vid_stream['height'] - (crop['top'] + crop['bottom'])
    if width <= 0:
        # the new width cannot be less than or equal to 0
        sys.stderr.write('ERROR: resulting width must be greater than 0')
        sys.exit(1)
    if height <= 0:
        # the new height cannot be less than or equal to 0
        sys.stderr.write('ERROR: resulting height must be greater than 0')
        sys.exit(1)

    # call ffmpeg with the required args
    cmd = (
        'ffmpeg -hide_banner -loglevel error -i "{}" -c:a copy '
        '-filter:v "crop={}:{}:{}:{}" {}{}'
    )

    cmd = cmd.format(
        args.input,
        width,
        height,
        crop['left'],
        crop['top'],
        "-y " if args.yes else "",
        args.output
    )
    os.system(cmd)

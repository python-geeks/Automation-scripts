import argparse
import sys
import os


if __name__ == '__main__':
    # set up the arguments to be parsed
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--level', type=int, help='the saturation percentage to use (default: 0, max: 300)')
    parser.add_argument('-y', '--yes', action='store_true', help='skip the prompt to overwrite the file')
    parser.add_argument('in_file', type=str, help='the file to desaturate')
    parser.add_argument('out_file', type=str, help='the file to output to')

    args = parser.parse_args()

    # check if the supplied file exists
    if not os.path.isfile(args.in_file):
        sys.stderr.write('ERROR: input file does not exist')
        sys.exit(1)

    # check that the level given is within range
    level = 0
    if args.level is not None:
        if args.level < 0 or args.level > 300:
            sys.stderr.write('ERROR: saturation level must be between 0 and 300')
            sys.exit(1)
        level = args.level

    # ffmpeg allows saturation values between 0.0 and 3.0
    # so we convert the percentage value here
    level = level / 100

    # create the ffmpeg command and run it
    cmd = 'ffmpeg -hide_banner -loglevel error -i "{}" -c:a copy -vf "eq=saturation={}" {}{}'
    cmd = cmd.format(
        args.in_file,
        level,
        "-y " if args.yes else "",
        args.out_file
    )
    os.system(cmd)

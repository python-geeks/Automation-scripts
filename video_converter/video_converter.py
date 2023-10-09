import ffmpeg
import argparse
import sys
import os

if __name__ == '__main__':
    # set up the arguments to be parsed
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', type=str, help='the file to crop')

    args = parser.parse_args()

    # validate that args.input is a file
    if args.input is None or not os.path.isfile(args.input):
        sys.stderr.write('ERROR: input file does not exist')
        sys.exit(1)

    try:
        base_name = os.path.splitext(os.path.basename(args.input))[0]
        output_file = f"{base_name}.mp4"

        input_stream = ffmpeg.input(args.input)

        output_file = f"{base_name}.mp4"
        output_stream = ffmpeg.output(input_stream, output_file)
        ffmpeg.run(output_stream)

        print(f"Conversion successful! Output saved as {output_file}")
    except ffmpeg.Error as e:
        print(f"Error: {e.stderr.decode('utf-8')}")

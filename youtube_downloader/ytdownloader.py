import argparse
from pytube import YouTube


def cli_parse():
    cli = argparse.ArgumentParser(prog='ytdownloader',
                                  description='Basic automation script for downloading YouTube hosted videos')
    cli.add_argument("url", metavar='URL', type=str, help="Youtube video URL")
    cli.add_argument("-p", "--path", type=str, help="Destination file path")
    cli.add_argument("-c", "--captions", type=str,
                     help="Captions lang to download")
    cli.add_argument("-r", "--res", type=str, help="Resolution to download")
    cli.add_argument("-v", "--verbose", type=bool, default=False,
                     help="Show information about script processing")
    return cli.parse_args()


args = cli_parse()
video = YouTube(args.url)
if not args.res:
    stream = video.streams.get_highest_resolution()
else:
    stream = video.streams.get_by_resolution(args.res)
    if not stream:
        stream = video.streams.get_highest_resolution()
        print(
            f"Sorry, '{args.res}' resolution is not available for this video.\nDownloading highest resolution...")


if not args.path:
    dest = stream.download()
else:
    dest = stream.download(args.path)

if args.captions:
    try:
        caps = video.captions[args.captions].generate_srt_captions()
        filename = f"{dest.split('.', 1)[0]}.srt"
        file = open(filename, "w")
        file.write(caps)
        file.close()
    except KeyError:
        print(
            f"Sorry, '{args.captions}' captions are not available for this video.")

if args.verbose:
    print(f"Successfully downloaded video: {dest}")

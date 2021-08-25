import argparse
import urllib.request

from pytube import YouTube


def parser():
    parse = argparse.ArgumentParser(
        prog='ytthumbnail',
        description="Script for grabbing thumbnail from Youtube video"
    )
    parse.add_argument(
        "url", metavar='URL', type=str, help="Youtube video URL"
        )
    parse.add_argument("-n", "--name", type=str, help="Select filename.")
    return parse.parse_args()


if __name__ == '__main__':
    name = "thumbnail.jpg"
    args = parser()
    if args.name:
        name = args.name
    if args.url:
        thumbnail = YouTube(args.url).thumbnail_url
        urllib.request.urlretrieve(thumbnail, name)
    else:
        print("No URL selected.")

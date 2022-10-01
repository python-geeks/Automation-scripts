import os
import imdb
import argparse
from termcolor import colored

arg_parser = argparse.ArgumentParser(
    usage='python rename.py [-h] [options]')

arg_parser.add_argument(
    '-c',
    '--code',
    type=str,
    help='IMDb CODE for the Series',
    required=False,
    metavar='')

arg_parser.add_argument(
    '-e',
    '--episode',
    type=str,
    help='Rename EPISODES of the series in the specified Directory',
    default=False,
    metavar='')

arg_parser.add_argument('-s', '--subtitle', type=str,
                        help='Rename SUBTITLES of the Series in the Directory',
                        default=False, metavar='')

arg_parser.add_argument(
    '-t',
    '--tag',
    type=str,
    help='Rename VIDEO TAGS for MKV Videos',
    required=False,
    metavar='')

args = arg_parser.parse_args()

not_allowed = r":\*<>\|"


def get_episodes(imdb_code):
    ia = imdb.IMDb()
    if "tt" in imdb_code:
        imdb_code = imdb_code[2:]

    series = ia.get_movie(imdb_code)
    print("SERIES: {}".format(colored(series, "magenta")))

    ia.update(series, "episodes")
    episodes = series.data['episodes']

    episode_list = []

    for season in episodes.keys():
        for episode in episodes[season]:
            title = episodes[season][episode]['title']

            if season < 10:
                if episode < 10:
                    ep_name = "{} S0{}E0{} - {}".format(series,
                                                        season, episode, title)
                else:
                    ep_name = "{} S0{}E{} - {}".format(series,
                                                       season, episode, title)
            else:
                if episode < 10:
                    ep_name = "{} S{}E0{} - {}".format(series,
                                                       season, episode, title)
                else:
                    ep_name = "{} S{}E{} - {}".format(series,
                                                      season, episode, title)

            for i in ep_name:
                if i in not_allowed:
                    ep_name = ep_name.replace(i, " -")
                if i in "\\/":
                    ep_name = ep_name.replace(i, "-")
                if i in "?":
                    ep_name = ep_name.replace(i, "")
            episode_list.append(ep_name)
    return episode_list


def rename_episode(directory, episode_list):
    files = os.listdir(directory)

    print("Renaming episodes...")

    for i in range(len(files)):
        ep_name = episode_list[i]
        og_name = files[i]
        ext = og_name[-4:]
        if ext != ".srt":
            ep_name += ext
            filename = os.path.join(directory, og_name)
            newfilename = os.path.join(directory, ep_name)
            print("Renaming {} to {}".format(
                colored(filename, 'yellow'),
                colored(newfilename, 'green')))
            os.rename(filename, newfilename)
    print(
        colored(
            "RENAMING", "red"), colored(
            "EPISODES", "cyan"), colored(
                "FINISHED!\n", "red"))


def rename_subtitle(directory, episode_list):
    files = os.listdir(directory)
    print("Renaming subtitles...")

    for i in range(len(files)):
        ep_name = episode_list[i]
        og_name = files[i]
        ext = og_name[-4:]
        if ext == ".srt":
            ep_name += ext
            filename = os.path.join(directory, og_name)
            newfilename = os.path.join(directory, ep_name)
            print(
                "Renaming {} to {}".format(
                    colored(
                        filename, 'yellow'), colored(
                        newfilename, 'green')))
            os.rename(filename, newfilename)
    print(
        colored(
            "RENAMING", "red"), colored(
            "SUBTITLES", "cyan"), colored(
                "FINISHED!\n", "red"))


def edit_tag(directory):
    for file in os.listdir(directory):
        if ".mkv" in file:
            title = file.replace(".mkv", "")
            command = r'mkvpropedit "{}\{}" --set "title={}"'.format(
                directory, file, title)
            os.system(command)

        if ".mp4" in file:
            title = file.replace(".mp4", "")
            command = r'mkvpropedit "{}\{}" --set "title={}"'.format(
                directory, file, title)
            os.system(command)

    print(
        colored(
            "RENAMING", "red"), colored(
            "VIDEO TAGS", "cyan"), colored(
                "FINISHED!\n", "red"))


if __name__ == "__main__":

    if args.code:
        episodes = get_episodes(args.code)

    if args.episode:
        args.episode = r'{}'.format(args.episode)
        rename_episode(args.episode, episodes)

    if args.subtitle:
        args.subtitle = r'{}'.format(args.subtitle)
        rename_subtitle(args.subtitle, episodes)

    if args.tag:
        args.tag = r'{}'.format(args.tag)
        edit_tag(args.tag)

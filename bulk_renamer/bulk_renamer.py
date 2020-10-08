import os
import sys


def add_end_slash(path):
    if path[-1] != "\\" or path[-1] != "/":
        return path + "\\"


def handle_ext(filename):
    if (len(filename.split(".")) > 1):
        return filename.split(".")[-1]
    else:
        return ""


def main(path, new_name):
    path = add_end_slash(path)

    for count, filename in enumerate(os.listdir(path)):

        src = path + filename
        ext = handle_ext(filename)
        dst = f"{path}{new_name} - ({str(count)}).{ext}"

        os.rename(src, dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

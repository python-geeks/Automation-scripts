import re
import sys


def get_urls(file_path):
    """[start method to fire extracting urls process]

    Arguments:
        file_path {[str]} -- [target text file path]
    """
    text = read_text_file(file_path)
    urls = extract_urls(text)
    export_urls(urls, file_path)


def read_text_file(file_path):
    """[summary]

    Arguments:
        file_path {[str]} -- [target text file path]

    Returns:
        [str] -- [file content to works on]
    """
    with open(file_path) as f:
        text = f.read()
    return text


def extract_urls(text):
    """[summary]

    Arguments:
        text {[str]} -- [file content to works on]

    Returns:
        [list] -- [extracted urls]
    """
    url_regex_pattern = r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+"
    urls = re.findall(url_regex_pattern, text)
    return urls


def export_urls(urls, file_path):
    """[summary]

    Arguments:
        urls {[list]} -- [extracted urls]
        file_path {[str]} -- [result text file path]
    """
    with open(file_path.replace(".txt", "_links.txt"), "w") as f:
        f.write("\n".join(urls))


if __name__ == "__main__":
    file_path = sys.argv[1]
    get_urls(file_path)

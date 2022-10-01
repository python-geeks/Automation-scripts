import os
from pathlib import Path


def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue

        file_path = Path(entry)
        file_format = file_path.suffix.lower()

        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

        else:
            directory_path = Path('Others')
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except Exception:
                pass


DIRECTORIES = {

    "Webpages": [".html5", ".html", ".htm", ".xhtml", ".aspx", ".php"],

    "Images": [".jpg", ".jpeg", ".png", ".tiff", ".gif", ".bmp", ".bpg", ".svg",
               ".heif", ".psd"],

    "Videos": [".avi", ".mp4", ".flv", ".mkv", ".wmv", ".mov", ".webm", ".vob",
               ".3gp", ".mpeg", ".mpg", ".qt"],

    "Docs": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".epub",
             ".opus", ".txt", ".in", ".out", ".xml"],

    "Archive": [".rar", ".zip", ".7z"],

    "Audio": [".mp3", ".aac", ".ogg", ".m4a", ".wav", ".aa", ".dvf", ".m4b",
              ".m4p", ".msv", ".oga", ".raw", ".vox"]

}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


if __name__ == "__main__":
    organize_junk()

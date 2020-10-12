# Empty folder cleaner

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

Basic script that recursively removes empty folders and subdirectories. Given a path, the script walks the directory
tree and removes folders with no files. Folders with empty subdirectories are also removed. Intuitively, folders that occupy
no size in memory are removed.

Doesn't require any module. Should work on Python 2 and 3.

Can be used as a script (`python EmptyFolderCleaner.py`) or imported into other projects by using the
`clean_empty_folders()` function. It requires a path, and more options are available.

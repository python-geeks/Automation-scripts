# Near Duplicate Files Remover
A script that searches for duplicate files and delete them to save up storage.



## Setup instructions
```
python pip install -r requirements.txt
python main.py
```

## Detailed explanation of script, if needed
After running the script, it crawls a given directory returning all the files in the directory, after that it generates a hash for every file
and save them in a pandas dataframe hashtable. Then, The script looks for similar hashes in the hashtable and deletes all the files with the
similar hashtable only keeping the original one.

## Author(s)

Rami Janini

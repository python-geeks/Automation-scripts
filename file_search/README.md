# File Search

Automation script to search any file/folder inside any directory within your computer

Just run the following command to search
```
python filesearch.py "search_term" "path/to/folder"
```

To go through all the available options, type
```
python filesearch.py -h
```

You will get options like this:
```
usage: filesearch.py [-h] [-dc] [-f] [-nb] term dir      

Search files within your computer

positional arguments:
  term                 Filename/Word to search for       
  dir                  Directory where you want to search

options:
  -h, --help           show this help message and exit   
  -dc, --disable-case  Perform case insensitive search   
  -f, --folder         Search only folders (default: searches files)
  -nb, --no-bar        Not show progress bar
```

##### Contributed By: [visheshdvivedi](https://github.com/visheshdvivedi)

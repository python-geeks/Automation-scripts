# IMDB Episode Rename
Python script to rename episodes and subtitles and video tags.
The episode names are taken from IMDb using the IMDBPy package.
Video Tags are renamed using MKVToolNix's CLI.

## Setup
- Use the included ```requirements.txt``` to install all dependencies using pip. Run ```pip install -r requirements.txt```.
- To use the tag rename feature, make sure to install MKVToolNix from [here](https://mkvtoolnix.download/) and add the installation directory to your System PATH.

## Usage

```
usage: python rename.py [-h] [options]

optional arguments:
  -h, --help        show this help message and exit
  -c , --code       IMDb CODE for the Series
  -e , --episode    Rename EPISODES of the series in the specified Directory
  -s , --subtitle   Rename SUBTITLES of the Series in the Directory
  -t , --tag        Rename VIDEO TAGS for MKV Videos
```

### Example
- For *It's Always Sunny in Philadelphia*, the IMDb Code is ```tt000472954```. You can use ```000472954``` as well.
- The Folder Structure is as given below:
```
. Windows D: Drive
├── Episode Directory       # Directory containing the episodes
└── Subtitle Directory      # Directory containing the subtitles
```

- Run the script using this convention:
```
python rename.py -c tt000472954 -e "D:\Episode Directory" -s "D:\Subtitle Directory" -t "D:\Episode Directory"

python rename.py --code tt000472954 --episode "D:\Episode Directory" --subtitle "D:\Subtitle Directory" --tag "D:\Episode Directory"
```

- The IMDb Code is compulsory. ```-e```, ```-s```, ```-t``` tags aren't.

## NOTES
- Make sure that **ALL** episodes/subtitles are available in the one folder, not nested folders!
- Due to certain limitations not yet handled, ensure that the **Episodes and Subtitles are in separate folders**!

## Authors
[IAmOZRules](https://github.com/IAmOZRules/)
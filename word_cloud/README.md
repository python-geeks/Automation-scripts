# Script to create wordcloud for a text file

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## How to use:
1. Make the directory structure as shown below:
<br>.
<br>├── word_cloud.py
<br>└── text_file.txt

2. Call the function giving two arguments, the path to the text file and the title of the plot (which is optional)
<br> example :-
<br>```wordcloud("./text_file.txt, title = "xyz")```


# Script to create wordcloud for a text file

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## How to use:
1. Call the function giving two arguments, the path to the doc file and the output path. (Include the file name that you want in the output path as well)
<br> example :-
<br>```input_file = "C:/User/Desktop/xyz.docx"```
<br>```output_file = "C:/User/Desktop/xyz.pdf"```
<br>```doc_to_pdf(input_file, output_file)```


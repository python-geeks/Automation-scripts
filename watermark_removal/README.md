# Script to remove watermark from images and pdfs

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## How to use:
1. Call the function giving two arguments, the path to the images whose watermark is to be removed and the output path (where you want to store the cleaned images). (This script will remove the watermarks from all jpg images in the folder and store them into another folder "Cleaned")
<br> example :-
<br>```input_folder = "C:/User/Desktop"```
<br>```output_folder = "C:/User/Desktop"```
<br>```watermark_removal(input_file)```

2. If you have a pdf with watermarks to be removed, you need to call the pdf_to_jpg function. This takes two arguments the input folder (where your pdf exists) and the output folder(where the images of each page will be stored).
<br> example :-
<br>```input_folder = "C:/User/Desktop"```
<br>```output_folder = "C:/User/Desktop"```
<br>```pdf_to_jpg(input_folder, output_folder)```

3. After calling the pdf function you can call the watermark_removal function to remove the watermarks from the pdf.

# pdf_editor

## What it does

Replaces text in PDF with another word.
Sequence:
Convert PDF to docx format
Search and replace word in file
Convert edited docx back to PDF

Suitable for simple styled PDFs only. Style of edited PDF may vary from original depending on the original PDF template structure.

## How to use

### Setup modules

Python and the following modules must be installed on the computer running this script.
Install the required modules by running this command in the directory of the requirements.txt file:
```
pip install -r requirements.txt
```

##install libreoffice
```
sudo add-apt-repository ppa:libreoffice/ppa
sudo apt-get update
sudo apt-get install libreoffice
```

### Run program

Run using:
```
python pdf_editor.py
```

You will be prompted for your settings. Example:
```
Your settings (format: file_name.pdf text_to_replace replacement_text): file.pdf HelloWorld HelloUniverse
```

The exported file "converted.pdf" is your edited pdf.
# Script to extract text from image

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```
## Libraries used :
opencv-python <br />
pytesseract <br />

## How to use :
```
pip install opencv-python
pip install tesseract
```
Just modify the path of files inside the code according to your setup and you're good to go.

## Possible error :

raise TesseractNotFoundError() <br />
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your path

If you get this error, please refer to: https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderror

# Captcha Solver
A simple python script for solving simple captchas

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## Modules Used

- pytesseract
- sys
- os
- PIL

## Requirements

- tesseract
`You can download tesseract from https://tesseract-ocr.github.io/tessdoc/Home.html`
- pytesseract

- After you install tesseract replace with your tesseract location in csolver.py

## How to use
`python csolver.py captcha_image`


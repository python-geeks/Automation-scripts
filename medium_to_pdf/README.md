# Medium Article PDF Downloader.

## Module Used.
- pdfkit

## How to use.
- Download the folder `medium-to-pdf`.
- Create virtual enviroment.
  - `virtualenv env`
- Activate It.
  - `. ./env/bin/activate`
- Install `wkhtmltopdf`.
  - In Ubuntu/Debian:
    - `apt-get install wkhtmltopdf`
  - For installation on other platforms.
    - https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
- Install python dependencies.
  - `pip install -r ./requirements.txt`
- Finally Use the file `main.py`.
  - `python ./main.py --url <medium-article-link> --output <name-of-output-file>`


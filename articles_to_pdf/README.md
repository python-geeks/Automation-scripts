# articles_to_pdf

Convert online articles to PDF.

## What it does

There are 2 ways to use this script:

- Option 1: Perform a search on Medium and export 1 to 10 articles from the search results as pdf
- Option 2: Export a single online article by pasting a direct URL to the article

## How to use

### Download browser and driver (Needed if using option 1)
You need to have either Firefox or Chrome installed. You also need the corresponding driver for the browser.

For Firefox download geckodriver:
https://github.com/mozilla/geckodriver/releases

For Chrome download chromedriver:
https://chromedriver.chromium.org/downloads

Place the driver in the same directory as the script.

### Setup modules

Python and the following modules must be installed on the computer running this script.
Install the required modules by running this command in the directory of the requirements.txt file:
```
pip install -r requirements.txt
```

### Install wkhtmltopdf
```
sudo apt-get install wkhtmltopdf
```

### Run program

Run using:
```
python articles_to_pdf.py
```

You will be prompted for your settings.
```
Enter '1' to search medium or '2' to export a single medium article: 
```

**For Option 1.** You should type in the search you want to perfom on Medium and the number of articles you want exported to PDF. The number of articles should be between 1 and 10. Example:
```
Enter search term followed by number of articles between 1 and 10 (e.g "learn python 5"): learn python 5
```
In this case "learn python" will be searched on Medium and 5 articles will be exported as PDF. The file name will contain the article titles.

**For Option 2.** Paste the URL for the article to convert to pdf. Example:
```
Paste URL to convert to PDF (must begin with 'https://'): https://medium.com/fintechexplained/everything-about-python-from-beginner-to-advance-level-227d52ef32d2
```
The article will be exported as PDF in a file called "converted.pdf"

### Tips for developers

Using Option 1 runs the browser in headless mode which means the browser GUI is not opened while running the program.
If you want the GUI to open while the script is running do the following:
- If using geckodriver change `firefox_options.headless = True` to `firefox_options.headless = False`
- If using chromedriver change `chrome_options.add_argument('--headless')` to `chrome_options.add_argument('--None')`
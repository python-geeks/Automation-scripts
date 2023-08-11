# Instagram Scraper with Scrapfly Integration

This project demonstrates how to ethically scrape and download images and videos from an Instagram profile using Selenium and the Scrapfly library. The scraping process is optimized using headless Chrome and Scrapfly's API for ethical and efficient data extraction.

## Getting Started

1. Clone the repository to your local machine:

    git clone https://github.com/your-username/instagram-scraper.git
    cd instagram-scraper

2. Install the required dependencies:
    pip install -r requirements.txt

## Set up Scrapfly API Key

Before running the scripts, set your Scrapfly API key as an environment variable. You can obtain your API key by signing up at Scrapfly.

    export SCRAPFLY_KEY="your_api_key_here"

## Usage

### 'scrapscrape.py'

This script uses Selenium and Scrapfly to scrape an Instagram profile for images and videos and saves them to the 'downloads' folder.

    python scrapescrape.py

### 'igscraper.py'

This script uses Selenium to scrape an Instagram profile for image and video links.

    python igscraper.py

### 'iglist.py'

This script uses Selenium to generate and display a list of download URLs for images and videos from an Instagram profile.

    python iglist.py

## Running Tests

### 'list_tests.py'

This script contains a test that generates and displays a list of download URLs for images and videos.

    pytest list_tests.py

### 'tests.py'

This script contains a test that scrapes and downloads limited posts from an Instagram profile.

    pytest tests.py

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or create a pull request.

## License

This project is licensed under the MIT License

I didn't invent any of this.  Use it at your own risk.  Logan Reese is the homie on keys.
# Zomato Dine-in Resaturant Scraper 

This python script scrapes the Name, Cuisine, Area, and Rate for Two details of Dine-in Reaturants from Zomato.
This script cotnains a user defined function which scrapes the restaurant details from certain city and return a DataFrame of the fetched details.

## Setup instructions

Steps to run the script:
1. Clone this repository
2. Download the [Chrome Webdriver](https://chromedriver.chromium.org/downloads) for your current Google Chrome version. Save the downloaded file to the cloned `zomato_dinein_restaurant_scraper` folder.
3. Install the required dependencies by running the command `pip install -r requirements.txt`
4. Run the `zomato_scraper.py` file.

## Addtional Information of script

In the Python script, we have scraped the restaurants for `Indore`. One can scrape resaturants of other citties by changing the `url` variable.
For example, if you want to scrape the Resaturants for `Mumbai`, change the url to `https://www.zomato.com/mumbai/dine-out`.
With time, number resaturants may increase, thus try increasing the number of iterations in the `for loop` if you think all the resaturants are not fetched.


## Output

![Sample](https://user-images.githubusercontent.com/43356237/137814799-c9180b73-0163-4f93-a230-b7fdb0a2b00a.png)

## Author(s)

Rahul Shah

## Disclaimers, if any

Author shall not be responsible for any malpractice done because of this script.

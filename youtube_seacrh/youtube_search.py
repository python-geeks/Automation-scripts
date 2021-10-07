from selenium import webdriver
import argparse
links = []
path_to_gekoDriver = ""  # enter the path here

# taking input from command line
parser = argparse.ArgumentParser()

# adding arguments
parser.add_argument('query', help='Enter the query to search video on youtube')
parser.add_argument(
    '-n', '--number', help='Video number which is to be opened',
    type=int, default=1)
args = parser.parse_args()


query = args.query
number = args.number

# opens firefox
driver = webdriver.Firefox(executable_path=path_to_gekoDriver)
url = f"https://www.youtube.com/results?search_query={query}"
driver.get(url)

try:
    # opens the nth video requested by the user
    xxpath = (driver.find_elements_by_xpath('//*[@id="video-title"]'))
    xxpath[number - 1].click()

except Exception as e:
    print("error : ")
    print(e)

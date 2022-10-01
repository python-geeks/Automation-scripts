from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Options_firefox
from selenium.webdriver.chrome.options import Options as Options_chrome

from pathlib import Path
import pdfkit


def setup_driver():

    # use the driver that exists in working directory - chromedriver and geckodriver supported

    find_geckodriver = Path("geckodriver")
    find_chromedriver = Path("chromedriver")

    if find_geckodriver.exists():
        driver = 'geckodriver'
        print('Using %s' % driver)
        PATH_TO_DRIVER = './%s' % driver

        firefox_options = Options_firefox()

        # run in headless mode
        firefox_options.headless = True

        # disable cookies to prevent popups
        opt = webdriver.FirefoxProfile()
        opt.set_preference("network.cookie.cookieBehavior", 2)

        browser = webdriver.Firefox(executable_path=PATH_TO_DRIVER, options=firefox_options, firefox_profile=opt)

    elif find_chromedriver.exists():
        driver = 'chromedriver'
        print('Using %s' % driver)
        PATH_TO_DRIVER = './%s' % driver

        chrome_options = Options_chrome()

        # run in headless mode
        chrome_options.add_argument('--headless')

        # disable cookies to prevent popups
        chrome_options.add_experimental_option('prefs', {'profile.default_content_setting_values.cookies': 2})

        browser = webdriver.Chrome(executable_path=PATH_TO_DRIVER, options=chrome_options)

    else:
        print('ERROR: No valid driver found. Only geckodriver or chromedriver is supported!')
        exit()

    return browser


def scrape_medium(browser, search_term, search_count):

    # perform search of keyword in medium

    browser.get('https://medium.com/search?q=%s' % search_term)
    browser.implicitly_wait(10)

    results = browser.find_elements_by_xpath('//a[contains(text(), "Read more")]')

    all_articles = []
    # get the links for all articles and store in list
    for each_article in results:
        all_articles.append(each_article.get_attribute('href'))

    # go to link of each article and export as PDF
    for counter, url in enumerate(all_articles, 1):
        print('Exporting article %s/%s: %s' % ((counter), search_count, url))

        browser.get(url)
        browser.implicitly_wait(10)

        # get title
        article_title = browser.title

        # get url of page to export
        url_to_export = browser.current_url

        # pdf name will contain article title
        pdf = 'Medium-%s.pdf' % article_title
        pdf = pdf.replace(' ', '-')

        # export pdf
        quiet_mode = {'quiet': ''}
        pdfkit.from_url(url_to_export, pdf, options=quiet_mode)

        # stop when we reach specified search count
        if (counter == int(search_count)):
            print('Complete. %s medium articles exported to PDF.' % search_count)
            browser.close()
            return


def process_option_1():

    # get user settings
    user_input = input('Enter search term followed by number of articles between 1 and 10 (e.g "learn python 5"): ')
    user_input = user_input.split(' ')

    # last entry should be a number
    try:
        search_count = int(user_input[-1])
    except ValueError:
        print('ERROR: Invalid input. The last entry must end with a number!')
        return

    # remove number from list
    user_input.pop()

    # join strings to load the phrase to search
    search_term = ' '
    for each_word in user_input:
        search_term = search_term + each_word + ' '

    browser = setup_driver()
    scrape_medium(browser, search_term, search_count)
    exit()


def process_option_2():

    # export a single article from the URL
    url = input("Paste URL to convert to PDF (must begin with 'https://'): ")

    print('Converting to PDF...')
    quiet_mode = {'quiet': ''}
    pdfkit.from_url(url, 'converted.pdf', options=quiet_mode)
    print('Complete. See "converted.pdf"')
    exit()


def program_run():

    while True:
        # get user option
        option = input("Enter '1' to search medium or '2' to export a single medium article: ")

        if option == '1':
            process_option_1()

        elif option == '2':
            process_option_2()

        elif option == 'x':
            exit()

        else:
            print("Invalid option. Try again! Or enter x to exit")
            continue
    pass


if __name__ == "__main__":
    program_run()
    pass

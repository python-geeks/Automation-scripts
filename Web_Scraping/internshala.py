import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


filename = "WorkfromHomeIntern.csv"
f = open(filename, "w")
headers = "Company, Internship, Location, Duration, StartDate, Stipend, PostedOn, ApplyBy, Link"
f.write(headers)


page_number = 1
while(page_number < 140):

    next_page = 'https://internshala.com/internships/work-from-home-jobs/page-' + \
        str(page_number)
    uClient = uReq(next_page)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "lxml")
    page_number = page_number+1

    for i in range(25):
        company = page_soup.findAll("div", {"class": "individual_internship_header"})[i].text.strip().split("\n")[3]
        internshipname = page_soup.findAll("div", {"class": "individual_internship_header"})[i].text.strip().split("\n")[0]
        startDate = page_soup.findAll("div", {"class": "individual_internship_details individual_internship_internship"})[i].text.strip().split("\n")[18]
        location = page_soup.findAll("div", {"class": "individual_internship_details individual_internship_internship"})[i].text.strip().split("\n")[2]
        duration = page_soup.findAll("div", {"class": "individual_internship_details individual_internship_internship"})[i].text.strip().split("\n")[21]
        stipend = page_soup.findAll("div", {"class": "individual_internship_details individual_internship_internship"})[i].text.strip().split("\n")[23]
        postedOn = page_soup.findAll("div", {"class": "individual_internship_details individual_internship_internship"})[i].text.strip().split("\n")[25]
        applyby = page_soup.findAll("div", {"class": "individual_internship_details individual_internship_internship"})[i].text.strip().split("\n")[26]
        ApplyNow = page_soup.findAll("div", {"class": "individual_internship_header"})[i].a["href"]
        f.write("\n" + company + "|" + internshipname + " | " + location + " | " + duration + " | " +
                startDate + " | " + stipend + " | " + postedOn + " | " + applyby + " | " + ApplyNow + "\n")

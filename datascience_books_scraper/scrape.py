import requests
from bs4 import BeautifulSoup
import csv
Book_name = []
Year = []
Publisher = []
Author = []

for j in range(1, 11):
    source = requests.get(
        f'https://1lib.in/s/data%20science?page={j}').text
    soup = BeautifulSoup(source, 'lxml')
    books = soup.find_all('table', attrs={'style': 'width:100%;height:100%;'})
    for i in books:
        # book name
        try:
            Book_name.append(i.find('h3').text.strip())
        except Exception:
            Book_name.append('nan')
        # year
        try:
            Year.append(
                i.find('div', class_='property_year').text.strip()[6:10])
        except Exception:
            Year.append('nan')
        # publisher
        try:
            Publisher.append(
                i.find('div', attrs={'title': 'Publisher'}).text.strip())
        except Exception:
            Publisher.append('nan')
        # Author
        try:
            Author.append(i.find('div', class_='authors').text.strip())
        except Exception:
            Author.append('nan')

file_name = '500Datasciencebooks.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'Book name', 'Publisher', 'Author', 'Year'])

    for i in range(1, len(Book_name)):
        writer.writerow([i, Book_name[i], Publisher[i], Author[i], Year[i]])

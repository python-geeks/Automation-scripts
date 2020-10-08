#Install python3
#Install pip
#Install pdfkit --> pip install pdfkit
#Install wkhtmltopdf ---> https://wkhtmltopdf.org/downloads.html depedning on your operating system.

import pdfkit
import os

fr_url = input('Enter the url the html of which will be converted to pdf : ')
to_pdf = input('Enter the output of the file without pdf extension :')

try:
	pdfkit.from_url(fr_url, to_pdf + '.pdf')
except:
	print("Some error occured while converting to pdf. Please check entered url and output file format")
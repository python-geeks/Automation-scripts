import pdfkit

fr_url = input('Enter the url the html of which will be converted to pdf : ')
to_pdf = input('Enter the output of the file without pdf extension :')
pdfkit.from_url(fr_url, to_pdf + '.pdf')

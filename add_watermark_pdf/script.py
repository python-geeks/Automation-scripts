"""
@hardik
@2020
@add_watermark to pdf
@py code
"""
import PyPDF2

inputFile = open('Demo.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(inputFile)
inputFirstPage = pdfReader.getPage(0)

pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
inputFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(inputFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
outputFile = open('output.pdf', 'wb')
pdfWriter.write(outputFile)
inputFile.close()
outputFile.close()

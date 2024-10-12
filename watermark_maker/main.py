from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfFileReader, PdfFileWriter

print("Enter file names with its extenstion!")


def makeWatermark():
    text = input("Enter the watermark text here:")
    pdf6 = canvas.Canvas("watermark.pdf", pagesize=A4)
    pdf6.translate(inch, inch)
    pdf6.setFillColor(colors.grey, alpha=0.6)
    pdf6.setFont("Helvetica", 50)
    pdf6.rotate(45)
    pdf6.drawCentredString(400, 100, text)
    pdf6.save()


def makepdf():
    pdf_file = input("PDF file: ")
    watermark = 'watermark.pdf'
    merged = "finalDraft.pdf"
    with open(pdf_file, "rb") as input_file, \
            open(watermark, "rb") as watermark_file:
        input_pdf = PdfFileReader(input_file)
        watermark_pdf = PdfFileReader(watermark_file)
        watermark_page = watermark_pdf.getPage(0)

        output = PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            pdf_page = input_pdf.getPage(i)
            pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)


makeWatermark()
makepdf()

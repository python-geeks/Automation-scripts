import markdown
import pdfkit
import sys

args = sys.argv[1:]  # get command line *args
assert args, "No file/dir was provided"  # raise error is no arg is passed

print(args)

html_texts = []
for arg in args:
    with open(arg, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html_texts.append(markdown.markdown(text))

# configuring pdfkit to point to our installation of wkhtmltopdf
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

for html_text in enumerate(html_texts):
    print(html_text[0])
    filename = args[html_text[0]].split('.')[0]
    pdfkit.from_string(html_text[1], f'{filename}.pdf', configuration=config)

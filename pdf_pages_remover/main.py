from PyPDF2 import PdfFileWriter, PdfFileReader

print("What is the file that you would like to modify?\n[Provide file address]")
file = str(input())
inputFile = PdfFileReader(file)

pagesToDelete = []
print("How many pages do you need to delete?")
n = int(input())

print("Enter the page numbers of the files you want to delete:\n[Enter page numbers followed by pressing 'Enter']")
for i in range(0, n):
    givenPage = int(input()) - 1
    pagesToDelete.append(givenPage)


output = PdfFileWriter()

for i in range(inputFile.getNumPages()):
    if i not in pagesToDelete:
        p = inputFile.getPage(i)
        output.addPage(p)

with open('output.pdf', 'wb') as f:
    output.write(f)

print("Done!")

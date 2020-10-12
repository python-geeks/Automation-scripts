import os
from PyPDF2 import PdfFileMerger

print("""
__________________  ___  ___
| ___ \\  _  \\  ___| |  \\/  |
| |_/ / | | | |_    | .  . | ___ _ __ __ _  ___ _ __
|  __/| | | |  _|   | |\\/| |/ _ \\ '__/ _` |/ _ \\ '__|
| |   | |/ /| |     | |  | |  __/ | | (_| |  __/ |
\\_|   |___/ \\_|     \\_|  |_/\\___|_|  \\__, |\\___|_|
                                      __/ |
                                     |___/           """)
print("📚  Step 1: put the PDFs you want to merge in a folder!")
print("✏️  Step 2: name your files in the order you want to merge!\
 (like 'file1.pdf', 'file2.pdf'...)")

path = os.path.abspath(input("📬 Step 3: Type the path of the folder\
 containing the PDFs you want to merge (relative path): "))
os.chdir(path)

output_file = input("💌 Step 4 (required): Name your output file: ") + ".pdf"

pdfs_list = [file for file in os.listdir() if file.endswith(".pdf")]
pdfs_list = sorted(pdfs_list, key=lambda file: os.path.splitext(file)[0])

merger = PdfFileMerger()
for pdf in pdfs_list:
    merger.append(pdf)

merger.write(output_file)
merger.close()
print("✨  Done! Your PDFs has been merged!  ✨")

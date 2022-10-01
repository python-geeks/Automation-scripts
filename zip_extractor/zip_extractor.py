from zipfile import ZipFile
import easygui
import time
# import the required libraries
print("Select the path of zip file...")
# a function in easygui that opens
# a window for selecrting the zip file
path = easygui.fileopenbox()
# for better presentation
# i added a break
time.sleep(2)

# opening the zip file selected
# in read mode
with ZipFile(path, 'r') as zip:
    # prints the contents in the zip folder
    zip.printdir()
    print("Select the destination directory to extract!!")
    # prompts the user to select the destination
    # folder where zip will be extracted
    path1 = easygui.diropenbox()
    print("Extracting files to the selected directory...")
    time.sleep(3)
    # extracts all the contents in the selected path
    zip.extractall(path1)
    time.sleep(2)
    # prints a message after extracting
    print("Done!")

Steps to build the QR Code Generator in Python
To build the QR code generator project using Python we need to follow the below steps:
1. Importing the modules
2. Creating the main window
3. Taking the input of the text/URL, location to store the QR code, name of the QR code and the size of the QR code
4. Writing the function to generate and save the QR Code
TUTORIAL
# Barcode-generator
Desktop app to generate EAN-13, EAN-8 and EAN-5 barcodes (other types are coming soon) 
automatically and save them as PDF or PNG, JPEG GIF image files with several sizes. 
As a database it uses native python csv module and saves as csv file.
(Using PyUPC-EAN module)

*Requirements*
- Standart python3 modules
- [Pillow](https://pypi.python.org/pypi/Pillow/4.3.0)
- [PyUPC-EAN](https://pypi.python.org/pypi/PyUPC-EAN/)

Usage
-----

Run script and set default values on Settings window. 
Then just click  `Generate` button: if barcode value is empty, 
then app generates barcode automatically according to initial value of barcode, 
else it generates by input value.

To save barcode value and its comment, click `Save`. 
This saves barcode as a file according to default filetype and filepath.

To change barcode comment, just double click on barcode row in table below, 
then make changes and click `Save` button. That it!

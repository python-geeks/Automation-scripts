# Email Slicer

Asks for user input in the form of an email address and separates the username from the domain.

## Setup instructions

0. Ensure you have python installed from python.org.
1. Open the folder containing this file.
2. Right click the empty area and select 'Open with Terminal' or similar.
3. Execute the script with `python3 email_slicer.py` (Linux, MacOS) or `python email_slicer.py` (Windows).


## Detailed explanation of script

- Utilises the `split` method to generate a list of strings separated by the @ symbol.
- The first element of the list is the username and the second is the domain.
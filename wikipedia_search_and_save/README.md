# Wikipedia Search & Save as PDF
A python script that allows the user to search for articles in Wikipedia and saves the summary of the article as a PDF file.

## Modules Used

- argparse
- wikipedia
- fpdf

## Requirements
We need to install the wikipedia and fpdf module. To install the modules type the following into the terminal:
```bash
pip install wikipedia
pip install fpdf
```

Recommended: Install the module after creating a virtual environment.

## Execution
- To run the program, type the following command into your terminal 

```bash
python wikipedia_search_and_save.py -s [Your search query]
```
Example
```bash
python wikipedia_search_and_save.py -s "Computers"
```
- Alternatively, type the following command into your terminal 

```bash
python wikipedia_search_and_save.py --search [Your search query]
```
Example
```bash
python wikipedia_search_and_save.py --search "Mobile Phones"
```

As an example, we have searched for "Computers" or "Mobile Phones".
After the search is completed successfully, the article is saved as "Computers.pdf" or "Mobile Phones.pdf" (based on which topic you have searched for) and the program gives the following output on the terminal.
```bash
[+] Your file was successfully saved.
```
- For help, type the following command into your terminal 

```bash
python wikipedia_search_and_save.py --help
```
Or
```bash
python wikipedia_search_and_save.py -h
```
Note: The file temp.txt saves the content of the search result temporarily. The file is emptied after the content is saved as PDF file.
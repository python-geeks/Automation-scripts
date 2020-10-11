# Wikipedia Search & Save as PDF
A python script that allows the user to search for articles in Wikipedia and saves the summary of the article as a PDF file.

## Modules Used

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
python wikipedia_search_and_save.py
```
The program will run and ask you to enter the search keywords.
```bash
Input here to search: Python Language
```
As an example, we have searched for "Python Language".
After the search is completed successfully, the article is saved as "Python Language.pdf" and the program gives the following output.
```bash
Successfully saved!
```
Note: The file temp.txt saves the content of the search result temporarily. The file is emptied after the content is saved as PDF file.
# Simple Plagiarism Checker

This is the simplest way to calculate similarity between two texts. Using cosine similarity between them. So, it is rather a similarity measure between two texts. Which in this case might be useful when comparing two texts for similarity/plagiarism. 

## Requirements 
Only uses in-built Python packages.

## Usage 

Specify the text files you want to compare while running the script as arguments.

`$ python simple-plagiarism-detector.py file1.txt file2.txt`

**Sample Output:**

`file1.txt` contents
> This is an example sentence

`file2.txt` contents
> This sentence is similar to an example sentence


`$ python simple-plagiarism-detector.py file1.txt file2.txt`

Similarity Score: 0.8485281374238569

**Contributor:** [abhinand5](https://github.com/abhinand5)
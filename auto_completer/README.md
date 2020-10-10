# Auto Complete / Language Modelling with N-Grams

There are two main components here, 
1. The Notebook
2. The Script

It is recommended to go through the notebook to understand the basics of ngram model and how to implement it in PyTorch. 

Next we will use the trained model from the notebook to auto complete words of your own. (although it might not be perfect)

> It is important to consider this just as a starting point. 

I will list out a few things you definitely need to make it run locally,

1. Python 3.7 or later
2. PyTorch 1.6 or later
3. Numpy and Matplotlib
4. pkbar - keras style progress bar 

These are the major requirements. If you wish you can install my entire setup using this command

`$ make install`

> **Note: We will be using Charles Dickens' great novel "A Tale of two cities" to train our model.**

You can download the novel using the code in cell 3 of the notebook, or from [this link](https://www.gutenberg.org/files/98/98-0.txt)

If you decide to download from the website, make sure to remove unwanted text from gutenberg at the start and end of the txt file. However I have included the text file with all the changes in this repo.

> **Author: [abhinand5](https://github.com/abhinand5)** 

Running the `auto-complete.py` script is very simple... just execute it and follow the prompts. 
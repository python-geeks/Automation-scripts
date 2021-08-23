# social_media_scraper_and_analyzer

# ONE


Fake or inaccurate news spread through social media in the country has become a serious problem, with the potential of it resulting in mob lynching, cyber-bullying, child abuse, child pornography, drug peddling, etc. Fake news can cause an unwanted political riot to a case of murder.
Social media is a platform of discussing memories and connecting with people has also become a place of murder or terrorism or cyber bullying or drug peddling using coded languages and unauthorised profiles. 
Being a large network it’s difficult to monitor such kind of medium manually (by humans) completely and provide precautions. 
Hereby, the prototype will help in controlling the trend of fake news by analysing the posts and declaring as proper or improper. Also our system is been design in a way that it reads data (text or image) and scans it whether it has any abusive or sexual content which might affect the society.   
Getting Started
These instructions will get you a copy of the prototype up and running on your local machine for development and testing purposes. 

In order to run the programs on Jupyter Notebook/Visual studio code , the following libraries need to be installed.
Please go through the "requirement.txt" file

# Stage of the project
This is a proof of concept stage and will eventually be maintained by rectifying and adding new features, in such a way that it becomes a strong stand alone system.   

# This folder contains:

# 1. Datasets
jigsaw-toxic-comment-train.csv – This csv file provided by kaggle(google) contains comments used for toxic comment classification. 

# 2. Jupyter Notebooks
It has 3 files, so that its easy for some one to change and modify who uses Jupyter Notebook as a primary IDE
1. analyzer-notebook --> has the Ml solution of naive bayes
2. Integrated --> has the combied file
3. WA_scrapper --> has the WhatsApp text scraper and message sending bot initialization

# 3. Other dependencies 
1. It has a chrome driver as an .exe file 

# 4. Testing
Once you have cloned the code simply run the "app.py" and scroll down to search for "try!" in demo section.
Pre-requisites 
1. Create  a group called "Bot" in your whatsapp account.
2. Then Scan the QR to log into WhatsApp to let the bot retrive the last message.
3. If the messag eis toxic the bot will again run, and likewise you need to log in scanning the QR code, so that the bot sends the messages.
4. One needs to scan the QR code within the span of 20 secs as I have mentioned in the code (you can also change it :) ).

# Technology used
1. Selenuim
2. Scikit Learn
3. Python (as a main language)
4. Flask
5. Html/css


Happy to connect and share.
:)

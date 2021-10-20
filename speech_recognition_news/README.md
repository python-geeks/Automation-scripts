# Speech News

## Execution

To execute the script, the dotenv and newspaper3 package will need to be downloaded. Documentation can be found below.
- newspaper3: https://newspaper.readthedocs.io/en/latest/
- dotenv: https://pypi.org/project/python-dotenv/

From there, you will need to go to https://newsapi.org/ and create an account and get the api key". 

Documentation for this can be found per below.
- Getting Started: https://newsapi.org/docs/get-started#search
- Python: https://newsapi.org/docs/client-libraries/python

Once you have the required packages, execute the scipt and it should pull the latest news articles, summarize them and put it into a json format under the folder "news_summary".

# Resume Details Extractor

Parse a Resume to get its details.

## Installation


# Features

- Extract name
- Extract email
- Extract mobile numbers
- Extract skills
- Extract total experience
- Extract college name
- Extract degree
- Extract designation
- Extract company names

# Installation

- You can install this package using

```bash
pip install resume-parser
```

- Dependency of spacy

```bash
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
pip install importlib-metadata==3.2.0
```

- For NLP operations we use spacy and nltk. Install them using below commands:

```bash
# spaCy
python -m spacy download en_core_web_sm

# nltk
python -m nltk.downloader stopwords
python -m nltk.downloader punkt
python -m nltk.downloader averaged_perceptron_tagger
python -m nltk.downloader universal_tagset
python -m nltk.downloader wordnet
python -m nltk.downloader brown
python -m nltk.downloader maxent_ne_chunker
```


# Supported File Formats

- PDF and DOCx and TXT files are supported on all Operating Systems


# Result

The module would return a dictionary with result as follows:

```
{'degree': ['BSc','MSc'],
     'designition': [
         'content writer',
         'data scientist',
         'systems administrator',
     ],
     'email': 'maunarokguy@gmail.com',
     'name': 'Brian Njoroge',
     'phone': '+918511593595',
     'skills': [
         'Python',
         ' C++',
         'Power BI',
         'Tensorflow',
         'Keras',
         'Pytorch',
         'Scikit-Learn',
         'Pandas',
         'NLTK',
         'OpenCv',
         'Numpy',
         'Matplotlib',
         'Seaborn',
         'Django',
         'Linux',
         'Docker'],
     'total_exp': 3,
     'university': ['gujarat university', 'wuhan university', 'egerton university']}
```
Check out the [Full Respository](https://github.com/kbrajwani/resume_parser)
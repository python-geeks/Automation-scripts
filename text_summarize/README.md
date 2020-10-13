# Text summarizer

Summarize the given text

# Requirements:
pytorch and bert-extractive-summarizer is required as well as all packages required by it. 


# Usage 
text_summarize.py [-h] [-t TEXT] [-f FILE] [-r RATIO] [-o OUTPUT]

Summarize the given text

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Text to summarize
  -f FILE, --file FILE  Filename to read text from
  -r RATIO, --ratio RATIO
                        Given the ratio of the summarized text (default: 0.2)
  -o OUTPUT, --output OUTPUT
                        Given the path to an output file. Otherwise stdout
                        will be used

# GPU vs CPU
CUDA is used if a gpu is available. To run it on CPU only, use following

CUDA_VISIBLE_DEVICES='' python3 text_summarize.py [-h] [-t TEXT] [-f FILE] [-r RATIO] [-o OUTPUT]

With CUDA_VISIBLE_DEVICES='', the GPUs are not visible to python and therefore the CPU is used. 

# Languages
Currently, only english is supported.  
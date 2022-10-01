import pandas as pd
import sys
import os

args = sys.argv[1:]  # get command line *args
assert args, "No file was provided; Provide a CSV filename"


isdir = os.path.isdir(args[-1])
# If input is CSV file
if not isdir:
    assert args[-1].endswith(".csv"), "Input file is not CSV"
    data = pd.read_csv(args[-1])  # load CSV data as Pd object
    data.to_json(args[-1][:-4] + ".json", orient='records')
    del data

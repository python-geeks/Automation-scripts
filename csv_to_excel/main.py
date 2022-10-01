import pandas as pd
import sys
import os

args = sys.argv[1:]  # get command line *args
assert args, "No file/dir was provided"  # raise error is no arg is passed

isdir = os.path.isdir(args[-1])

# If input is CSV file
if not isdir:
    assert args[-1].endswith(".csv"), "Input file is not CSV; Provide CSV file"
    data = pd.read_csv(args[-1])  # load CSV data as Pd object
    data.to_excel(args[-1][:-4] + ".xlsx", index=None, header=True)
    del data

# If input is Directory containing multiple csv
else:
    try:
        # remove "/" from end of directory is passed
        if args[-1][-1] == "/":
            args[-1] = args[-1][:-1]
        # create a dir to save the excel datasheet
        os.mkdir(args[-1] + "_excel")
    except Exception:
        pass
    for filename in os.listdir(args[-1]):
        if filename.endswith(".csv"):
            data = pd.read_csv(filename)
            data.to_excel(
                args[-1] + "_excel/" + filename[:-4] + ".xlsx"
            )  # write as excel
            del data  # delete the pandas DataFrame object

exit(0)

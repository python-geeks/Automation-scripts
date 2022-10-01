# import libraries
import glob
import tqdm
import os

PATH = "INPUT FOLDER"
# extension
et = "pptx"  # or ppt
files = [f for f in glob.glob(PATH + "/**/*.{}".format(et), recursive=True)]
for f in tqdm.tqdm(files):
    command = "unoconv -f pdf \"{}\"".format(f)
    os.system(command)

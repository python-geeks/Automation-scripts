# import libraries
import os
import glob
import tqdm

PATH="INPUT FOLDER"
extension="pptx" # or ppt
files = [f for f in glob.glob(PATH+ "/**/*.{}".format(extension), recursive=True)]
for f in tqdm.tqdm(files):
    command = "unoconv -f pdf \"{}\"".format(f)
    os.system(command)

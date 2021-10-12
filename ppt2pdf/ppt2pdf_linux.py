import glob
import tqdm
import os 

PATH = "<INPUT FOLDER>"
extension = "pptx"
files = [f for f in glob.glob(PATH + "/**/*.{}".format(extension), recursive=True)]
for f in tqdm.tqdm(files):
    command = "unoconv -f pdf \"{}\"".format(f)
    os.system(command)

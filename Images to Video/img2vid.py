import cv2

from imutils import paths
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path to input directory")
ap.add_argument("-o", "--output_video", type=str, required=True, help="output video name")
args = vars(ap.parse_args())

out = None
(w, h) = (None, None)
img_array = []

imagePaths = list(paths.list_images(args["path"]))

for filename in imagePaths:
    img = cv2.imread(filename)
    img = cv2.resize(img, (1400, 800))
    height, width, layers = img.shape
    if w is None or h is None:
        (w, h) = (width, height)
    img_array.append(img)

if out is None:
    out = cv2.VideoWriter(args["output_video"], cv2.VideoWriter_fourcc(*'DIVX'), 1, (w, h), True)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()

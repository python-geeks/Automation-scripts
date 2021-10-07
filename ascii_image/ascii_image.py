from PIL import Image
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('inputImage', help='Enter the path to image')
parser.add_argument('outputFile', help='Enter the path to output File')
parser.add_argument(
    '-w', '--width', help='Enter width of output image', type=int, default=75)
parser.add_argument('-c', '--colorInvert',
                    help='Enter to invert color of image', action='store_true')
args = parser.parse_args()


inputImagePath = args.inputImage
outputPath = args.outputFile
widd = args.width

asci = r"@%#*+=-:. "[::1]

if args.colorInvert:
    asci = r"@%#*+=-:. "[:: - 1]

# input image
img = Image.open(inputImagePath)

wid, height = img.size
img = img.resize((widd, int(widd * ((height * 9) / (wid * 20)))))
wid, height = img.size

img = img.convert("L")


def avg(imggg):
    return (np.average(np.array(imggg)))


# opening file
f = open(outputPath, "w")

for j in range(height):
    for i in range(wid):
        img1 = img.crop((i, int(j), i + 1, int((j + 1))))
        f.write(asci[int((avg(img1) * 9) / 255)])
        print(asci[int((avg(img1) * 9) / 255)], end="")
    print("\n", end="")
    f.write("\n")


f.close()

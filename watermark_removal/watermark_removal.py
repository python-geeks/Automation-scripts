import numpy as np
import glob
import cv2
from pdf2image import convert_from_path


def pdf_to_jpg(path_to_folder, output_path):

    for pdf in glob.glob(path_to_folder + "/*.pdf"):
        pages = convert_from_path(pdf, 500)
        i = 0

        for page in pages:
            page.save(output_path + "/image%04i.jpg" % i, 'JPEG')
            i += 1


def watermark_removal(path_to_folder, output_path):
    i = 0
    alpha = 2.0
    beta = -160

    for img1 in glob.glob(path_to_folder + "/*.jpg"):
        originalimage = cv2.imread(img1)
        imgGrayscale = cv2.cvtColor(originalimage, cv2.COLOR_BGR2GRAY)
        imgcleaned = alpha * imgGrayscale + beta
        imgcleaned = np.clip(imgcleaned, 0, 255).astype(np.uint8)
        cv2.imwrite("Cleaned/image%03i.jpg" % i, imgcleaned)
        i += 1

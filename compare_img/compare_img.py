import sys
import cv2
import numpy as np
from skimage import io
from skimage.metrics import structural_similarity as ssim


def compare(imageA, imageB):
    # Structural Similarity Index from skimage
    s = ssim(imageA, imageB, multichannel=True)

    # Mean Sqaure Error
    m = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    m /= float(imageA.shape[0] * imageA.shape[1])

    # Histogram Difference using numpy.histogram
    diff = 0.0
    h1, b1 = np.histogram(imageA)
    h2, b2 = np.histogram(imageB)
    for i in range(len(h1)):
        diff += abs(h1[i] - h2[i])
    maxSum = max(h1.sum(), h2.sum())
    return (s, m, diff / (2 * maxSum))


def pre_processing(imageA, imageB):
    def uniform_dim(imageA, imageB):
        h1, w1 = imageA.shape
        h2, w2 = imageB.shape
        if (h1 != h2) or (w1 != w2):
            imageA = cv2.resize(imageA, (min(w1, w2), min(h1, h2)))
            imageB = cv2.resize(imageB, (min(w1, w2), min(h1, h2)))
        return imageA, imageB

    # clr to grey
    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # uniform dimensions
    imageA, imageB = uniform_dim(imageA, imageB)

    return (imageA, imageB)


before = io.imread(sys.argv[1])
after = io.imread(sys.argv[2])

before, after = pre_processing(before, after)
ssi, mse, hist_diff = compare(before, after)

print(f"SSI value is {ssi}")
print(f"MSE value is {mse}")
print(f"Histogram difference is {hist_diff}")

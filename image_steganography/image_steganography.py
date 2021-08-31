import cv2
import numpy as np
from Crypto.Cipher import AES
import math

image = cv2.imread('file location')


def encrypt(mess, key):
    """Encrypt the plain text using AES encrypt"""
    if len(key) % 16 != 0:
        a = 16 - len(key) % 16
        key = key.ljust(len(key) + a)
    if len(mess) % 16 != 0:
        a = 16 - len(mess) % 16
        mess = mess.ljust(len(mess) + a)
    cipher = AES.new(key)
    encrypted_data = cipher.encrypt(mess)
    return encrypted_data


def correlation(M1, M2):
    """Correlation of two matrices"""
    li, wi = M1.shape
    ls, ws = M2.shape
    lo = li + ls - 1
    wo = wi + ws - 1
    g = np.zeros([li + ls * 2 - 2, wi + ws * 2 - 2])
    g[ls - 1:li + ls - 1, ws - 1:wi + ws - 1] = M1
    out = np.zeros([lo, wo])
    for x in range(lo):
        for y in range(wo):
            C = np.multiply(g[x:x + ls, y:y + ws], M2)
            out[x, y] = np.sum(C)
    return out


def gaussian_filter(dim):
    """Produce a filter to smoothen the image"""
    sigma = math.sqrt(dim)
    fil = np.zeros((dim, dim))
    k = dim
    m = int((dim / 2) + 1)
    for i in range(int((dim / 2) + 1)):
        for j in range(int((dim / 2) + 1)):
            fil[i, j] = np.exp(-((((m - i - 1)**2) + ((m - j - 1)**2)) / (2 * sigma**2)))
            fil[i, j] = fil[i, j] / (2 * np.pi * sigma**2)
            fil[i, k - j - 1] = fil[k - i - 1, j] = fil[k - i - 1, k - j - 1] = fil[i, j]
    s = np.sum(fil)
    fil = fil / s
    return fil


def sobelfilter(s):
    """Function to detect the edges of an image"""
    filter1 = gaussian_filter(3)
    s = correlation(s, filter1)
    sobelxy = cv2.Sobel(src=s, ddepth=cv2.CV_8U, dx=1, dy=1, ksize=3)
    return sobelxy


def image_steg(img, mess, key):
    """Main Function"""
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edge_img = sobelfilter(img_gray)
    indices = np.where(edge_img != 0)
    f_points = np.column_stack((indices[0], indices[1]))
    no_edge, r = f_points.shape
    en_mess = str(encrypt(mess, key))
    f = np.array([])
    le = np.array([])
    n = 0
    for i in en_mess:
        arr = " ".join(f"{ord(x):08b}" for x in i)
        for j in arr:
            f = np.append(f, int(j))
    l1 = str(len(en_mess) * 8)
    l1 = l1 + "/"
    arr = " ".join(f"{ord(x):08b}" for x in l1)
    for j in arr:
        if j != ' ':
            le = np.append(le, int(j))
    for i in le:
        x, y = f_points[n]
        pix_val = img_gray[x, y]
        if (pix_val % 2 == i):
            img_gray[x, y] = img_gray[x, y]
        else:
            img_gray[x, y] = img_gray[x, y] - 1
        n = n + 1
    n = 82
    for i in f:
        x, y = f_points[n]
        pix_val = img_gray[x, y]
        if (pix_val % 2 == i):
            img_gray[x, y] = img_gray[x, y]
        else:
            img_gray[x, y] = img_gray[x, y] - 1
        n = n + 1
    print(n)
    return img_gray


message = "Message to encrypt"
key = "key to encrypt the message"

test_image = image_steg(image, message, key)

import cv2
import numpy as np
from Crypto.Cipher import AES
import math
import codecs


def decrypt(mess, key):
    """Decrypt the cypher text using AES decrypt"""
    if len(key) % 16 != 0:
        a = 16 - len(key) % 16
        key = key.ljust(len(key) + a)
    cipher = AES.new(key)
    plain_txt = cipher.decrypt(mess)
    return plain_txt


def correlation(M1, M2):
    """correlation of two matrices"""
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
    """Producing filter to smoothen the image"""
    sigma = math.sqrt(dim)
    fil = np.zeros((dim, dim))
    k = dim
    m = int((dim / 2) + 1)
    for i in range(int((dim / 2) + 1)):
        for j in range(int((dim / 2) + 1)):
            fil[i, j] = np.exp(- ((((m - i - 1)**2) + ((m - j - 1)**2)) / (2 * sigma ** 2)))
            fil[i, j] = fil[i, j] / (2 * np.pi * sigma**2)
            fil[i, k - j - 1] = fil[k - i - 1, j] = fil[k - i - 1, k - j - 1] = fil[i, j]
    s = np.sum(fil)
    fil = fil / s
    return fil


def sobelfilter(s):
    """To detect the edges of the image"""
    filter1 = gaussian_filter(3)
    s = correlation(s, filter1)
    sobelxy = cv2.Sobel(src=s, ddepth=cv2.CV_8U, dx=1, dy=1, ksize=3)
    return sobelxy


def pix_decode(pos, img):
    """idenitify the binary code from the edge pixel"""
    x = pos[0]
    y = pos[1]
    pix_val = img[x, y]
    if pix_val % 2 == 1:
        c = 1
    else:
        c = 0
    return c


def image_steg_decode(orimg, gr, key):
    """Main function"""
    img_gray = cv2.cvtColor(orimg, cv2.COLOR_BGR2GRAY)
    edge_img = sobelfilter(img_gray)
    indices = np.where(edge_img != 0)
    f_points = np.column_stack((indices[0], indices[1]))
    no_edge, r = f_points.shape
    f = np.array([])
    n = 80
    for i in range(n):
        num = pix_decode(f_points[i], gr)
        f = np.append(f, num)
    ascii_string = ""
    for i in range(int(n / 8)):
        b = ' '.join(str(int(e)) for e in f[i * 8:(i * 8) + 8])
        b = b.replace(" ", "")
        an_integer = int(b, 2)
        ascii_character = chr(an_integer)
        if ascii_character == "/":
            break
        ascii_string += ascii_character
    le = int(ascii_string)
    n = 82
    for i in range(le + 80):
        num = pix_decode(f_points[n], gr)
        f = np.append(f, num)
        n = n + 1
    ascii_string = ""
    for i in range(int((le + 80) / 8)):
        b = ' '.join(str(int(e)) for e in f[i * 8:(i * 8) + 8])
        b = b.replace(" ", "")
        an_integer = int(b, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    ascii_string = ascii_string[12:-1]
    ascii_string = bytes(ascii_string, 'utf-8')
    ed, _ = codecs.escape_decode(ascii_string, 'hex')
    print(ed)
    ans = decrypt(ed, key)
    return (ans)


image = cv2.imread("original image")
test_image = cv2.imread("Output image from the encode function")
key = "key from previous funtion"
decoded_message = image_steg_decode(image, test_image, key)

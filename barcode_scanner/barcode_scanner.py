from pyzbar.pyzbar import decode
from glob import glob
import cv2

def barcode(decoded, image):
    imge = cv2.rectangle(image, (decoded.rect.left,
           decoded.rect.top), (decoded.rect.left + decoded.rect.width,
           decoded.rect.top + decoded.rect.height),
           color=(0, 255, 0), thickness=5)
    return imge

def scan(image):
    dcode = decode(image)
    for obj in dcode:
        print("Given barcode:", obj)
        image = barcode(obj, image)
        print("Barcode Type:", obj.type)
        print("Scanned Data:", obj.data)
        print()
    return image


data = input("Enter the path of the barcode")
dat = glob(data)
for code in dat:
    img = cv2.imread(code)
    img = scan(img)
    cv2.imshow("img", img)
    cv2.waitKey(0)

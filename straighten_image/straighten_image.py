import cv2
import math
import numpy as np
from scipy import ndimage


path = "test.jpg"
image = cv2.imread(path)
image_edges = cv2.Canny(image, 100, 100, apertureSize=3)
lines = cv2.HoughLinesP(
    image_edges,
    rho=1,
    theta=np.pi / 180.0,
    threshold=160,
    minLineLength=100,
    maxLineGap=10,
)

# calculate all the angles
angles = []
for [[x1, y1, x2, y2]] in lines:
    # drawing Hough lines
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)

# median of angles
median_angle = np.median(angles)
# rotate
image = ndimage.rotate(image, median_angle)

cv2.imwrite("rotated.png", image)

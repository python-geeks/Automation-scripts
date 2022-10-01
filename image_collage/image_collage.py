import requests
from PIL import Image
from io import BytesIO
import numpy as np

lst = []
for i in range(0, 4):
    url = input("Enter your image URL:")
    try:
        res = requests.get(url)
    except Exception:
        print("Can't access the URL")
        continue
    img = Image.open(BytesIO(res.content))
    new_image = img.resize((200, 200))
    lst.append(new_image)
image1 = np.array(lst[0])
image2 = np.array(lst[1])
image3 = np.array(lst[2])
image4 = np.array(lst[3])
final = np.vstack([np.hstack([image1, image2]), np.hstack([image3, image4])])
collageimage = Image.fromarray(final)
collageimage.save("D:/Imagecollage.jpg")
print("Image saved in the given path")

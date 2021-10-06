import requests
from PIL import Image
from io import BytesIO
import os

download_path = os.path.dirname(os.path.abspath(__file__))
count = 1
while True:
    url = input("Enter Image URL: ")
    try:
        res = requests.get(url)
    except Exception:
        print("Invalid URL / Can't Access The URL")
        continue

    img = Image.open(BytesIO(res.content))
    format = img.format
    imgLoc = os.path.join(download_path, f"{count}.{format.lower()}")
    img = img.save(imgLoc, format=format.upper())
    print(f"Image Downloaded: {imgLoc}")
    count += 1

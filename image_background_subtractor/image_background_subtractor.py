import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

IMAGE_FILES = ['location_to_image/image.jpg']  # You can use multiple Images for removal at a go by just specifying the name of the images in the list.
BG_COLOR = (255, 255, 255)  # White Background
with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
    for idx, file in enumerate(IMAGE_FILES):
        image = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        image_height, image_width, _ = image.shape
        results = selfie_segmentation.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        bg_image = np.zeros(image.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        output_image = np.where(condition, image, bg_image)
        cv2.imwrite('./white_bg' + str(idx) + '.png', output_image)
        #  Converting the White Background to Transparent Background.
        img = Image.open("./white_bg"+str(idx)+".png")
        img = img.convert("RGBA")
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save("location_to_store_result/Result" + str(idx) + ".png", "PNG")

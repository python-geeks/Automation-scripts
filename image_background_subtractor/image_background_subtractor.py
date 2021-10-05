import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
# You can use multiple Images for removal at a go by just specifying the name of the images in the list.
IMAGE_FILES = ['location_to_image/image.jpg']
BG_COLOR = (192, 192, 192)  # gray, you can set to any
with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
    for idx, file in enumerate(IMAGE_FILES):
        image = cv2.imread(file)
        image_height, image_width, _ = image.shape
        results = selfie_segmentation.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        bg_image = np.zeros(image.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        output_image = np.where(condition, image, bg_image)
        cv2.imwrite('location_to_store_result/result' + str(idx) + '.png', output_image)

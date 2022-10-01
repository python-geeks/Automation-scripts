# Author - Abhinand --> https://github.com/abhinand5
# =====================================================================
# IMPORTS
# ======================================================================

import torch
from torchvision import transforms

import os
import sys
from PIL import Image

from model import FaceMaskDetector
from train import plot_result

# =====================================================================
# HELPER FUNCTION TO PREDICT CUSTOM IMAGES AND SAVE IN RESULTS DIR
# ======================================================================


def predict(img_path, model):
    if os.path.splitext(img_path)[-1] not in [".jpg", ".png", ".jpeg"]:
        raise Exception(
            f"Image format ->{os.path.splitext(img_path)[-1]}<- not supported"
        )

    image = Image.open(img_path).convert("RGB")
    to_tensor = transforms.ToTensor()
    image_t = to_tensor(image)

    pred = model.predict(image_t.unsqueeze(0))

    return image_t, pred


if __name__ == "__main__":

    device = torch.device("cpu")
    print("Device set to: ", device)

    model = FaceMaskDetector(data_loader=None, device=device, pretrained=True)

    model.build_model(n_classes=3)

    LOAD_CKPT = "./faster-rcnn_s2.ckpt"
    model.load_model(LOAD_CKPT)

    img_path = sys.argv[1]
    save_name = sys.argv[2]

    print("Running image through the model...")

    image_t, pred = predict(img_path, model)
    plot_result(image_t, pred[0], save_name)

    print(f"Successfully saved result image at ./results/{save_name}")

# Author - Abhinand --> https://github.com/abhinand5
# =====================================================================
# IMPORTS
# ======================================================================

import torch

import os
from PIL import Image
from bs4 import BeautifulSoup

######################################################################
# Data source - https://www.kaggle.com/andrewmvd/face-mask-detection
# =====================================================================
# Writing the Dataset class for PyTorch
# ======================================================================


class FaceMaskDataset(object):
    def __init__(self, transforms):
        self.images = list(sorted(os.listdir("./data/images")))
        self.annotations = list(sorted(os.listdir("./data/annotations")))
        self.transforms = transforms

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img = "maksssksksss" + str(idx) + ".png"
        label = "maksssksksss" + str(idx) + ".xml"

        img_path = os.path.join("./data/images/", img)
        label_path = os.path.join("./data/annotations/", label)

        img = Image.open(img_path).convert("RGB")
        label = self.generate_label(idx, label_path)

        if self.transforms is not None:
            img = self.transforms(img)

        return img, label

    def generate_label(self, image_idx, label_file):
        with open(label_file) as f:
            data = f.read()
            soup = BeautifulSoup(data, "xml")
            objects = soup.find_all("object")

            boxes = []
            labels = []

            for ob in objects:
                boxes.append(self.get_box(ob))
                labels.append(self.get_label(ob))

            boxes = torch.as_tensor(boxes, dtype=torch.float32)
            labels = torch.as_tensor(labels, dtype=torch.int64)

            img_idx = torch.tensor([image_idx])

            target = {}
            target["boxes"] = boxes
            target["labels"] = labels
            target["image_id"] = img_idx

            return target

    def get_label(self, obj):
        if obj.find("name").text == "with_mask":
            return 1
        elif obj.find("name").text == "mask_weared_incorrect":
            return 2
        return 3

    def get_box(self, obj):
        x0 = int(obj.find("xmin").text)
        x1 = int(obj.find("xmax").text)
        y0 = int(obj.find("ymin").text)
        y1 = int(obj.find("ymax").text)

        return [x0, y0, x1, y1]

# Author - Abhinand --> https://github.com/abhinand5
# =====================================================================
# IMPORTS
# ======================================================================

import torch
from torchvision import transforms

import os

from dataset import FaceMaskDataset
from model import FaceMaskDetector

import matplotlib.pyplot as plt
import matplotlib.patches as patches

import warnings

warnings.filterwarnings("ignore")


def plot_result(image_tensor, annotations, savename, ucb=0.9):
    """Helper function to plot and save the results"""
    fig, ax = plt.subplots(1)
    image = image_tensor.cpu().data

    ax.imshow(image.permute(1, 2, 0))

    color_map = {1: "green", 2: "orange", 3: "red"}

    for i, box in enumerate(annotations["boxes"]):
        if float(annotations["scores"][i]) > ucb:
            x0, y0, x1, y1 = box

            color = color_map[int(annotations["labels"][i])]
            rect = patches.Rectangle(
                (x0, y0),
                (x1 - x0),
                (y1 - y0),
                linewidth=1,
                edgecolor=color,
                facecolor="none",
            )

            ax.add_patch(rect)
        else:
            pass

    plt.axis("off")
    plt.savefig(f"./results/{savename}.png")


# ======================================================================
# Setting up Device and Data
# ======================================================================
if __name__ == "__main__":

    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print("Device set to: ", device)

    # Get images and annotations
    images = list(sorted(os.listdir("./data/images")))
    annotations = list(sorted(os.listdir("./data/annotations")))

    # Set up data for training
    BATCH_SIZE = 4

    data_transform = transforms.Compose(
        [
            transforms.ToTensor(),
        ]
    )

    def collate_fn(batch):
        return tuple(zip(*batch))

    # Create the torch dataset
    dataset = FaceMaskDataset(transforms=data_transform)
    data_loader = torch.utils.data.DataLoader(
        dataset, batch_size=BATCH_SIZE, collate_fn=collate_fn
    )

    # ======================================================================
    # Training the Faster-RCNN model
    # ======================================================================
    model = FaceMaskDetector(
        data_loader=data_loader,
        device=device,
        pretrained=True
    )

    model.build_model(n_classes=3)

    LOAD = True
    LOAD_CKPT = "./faster-rcnn_s2.ckpt"
    SAVE_CKPT = "./faster-rcnn_s2.ckpt"

    N_EPOCHS = 10
    LEARNING_RATE = 0.005

    if LOAD:
        model.load_model(LOAD_CKPT)

    losses = model.train(n_epochs=N_EPOCHS, learning_rate=LEARNING_RATE)
    model.save_model(SAVE_CKPT)

    # ======================================================================
    # Making inference using the trained model
    # ======================================================================
    iters = 1
    ctr = 0

    for i, (imgs, annotations) in enumerate(data_loader):
        if i > iters - 1:
            break
        imgs = list(img.to(device) for img in imgs)
        annotations = [
            {k: v.to(device) for k, v in t.items()}
            for t in annotations
        ]

        pred = model.predict(imgs)

        for j in range(len(pred)):
            plot_result(imgs[j], pred[j], ucb=0.8, savename=ctr)
            ctr += 1

    print("Resultant images saved at './results/' folder")

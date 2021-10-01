# Author - Abhinand --> https://github.com/abhinand5
# =====================================================================
# IMPORTS
# ======================================================================

import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

import pkbar

# =====================================================================
# PyTorch class for the model
# ======================================================================


class FaceMaskDetector(object):
    def __init__(self, data_loader, device, pretrained=True):
        self.pretrained = pretrained
        self.data_loader = data_loader
        self.device = device

    def build_model(self, n_classes):
        model = torchvision.models.detection.fasterrcnn_resnet50_fpn(
            pretrained=self.pretrained
        )
        in_features = model.roi_heads.box_predictor.cls_score.in_features
        model.roi_heads.box_predictor = FastRCNNPredictor(
            in_features,
            n_classes + 1
        )

        self.model = model

    def train(self, n_epochs, learning_rate):
        dl_len = len(self.data_loader)

        self.model.to(self.device)
        params = [p for p in self.model.parameters() if p.requires_grad]
        optimizer = torch.optim.SGD(
            params, lr=learning_rate, momentum=0.9, weight_decay=0.0005
        )

        losses_per_ep = []

        for epoch in range(n_epochs):
            self.model.train()

            ep_loss = 0
            kbar = pkbar.Kbar(
                target=dl_len,
                epoch=epoch,
                num_epochs=n_epochs,
                width=20,
                always_stateful=True,
            )

            for i, (images, annotations) in enumerate(self.data_loader):
                images = list(image.to(self.device) for image in images)
                annotations = [
                    {
                        k: v.to(self.device)
                        for k, v in t.items()
                    } for t in annotations
                ]

                losses = self.model([images[0]], [annotations[0]])
                loss = sum(loss for loss in losses.values())

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                ep_loss += loss.item()

                kbar.update(i, values=[("loss", ep_loss)])

            losses_per_ep.append(ep_loss)
            kbar.add(1)

        return losses_per_ep

    def predict(self, images):
        self.model.to(self.device)
        self.model.eval()
        preds = self.model(images)

        return preds

    def save_model(self, path):
        torch.save(self.model.state_dict(), path)

    def load_model(self, path):
        self.model.load_state_dict(torch.load(path))

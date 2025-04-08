from fastapi import FastAPI, Request
from pydantic import BaseModel
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO
import os, time

app = FastAPI()
trained_model_path = r"./model/best.pt"
output_image_path = r"./app/test_data/output/"

@app.post("/detect/")
async def detect_image(input_image_path):
    output_path = predict_cell_seg(input_image_path)
    return {"output_image_path": output_path}

@app.get("/test/")
async def detect_image():
    return {"Output": "Hello World"}


def overlay_masks(image, masks, alpha=0.5, colors=None):
    overlay = image.copy()
    if colors is None:
        colors = [np.random.randint(0, 255, (3,), dtype=np.uint8) for _ in masks]
    for mask, color in zip(masks, colors):
        colored_mask = np.zeros_like(image, dtype=np.uint8)
        for c in range(3):
            colored_mask[:, :, c] = mask * color[c]
        overlay = cv2.addWeighted(overlay, 1, colored_mask, alpha, 0)
    return overlay

def predict_cell_seg(image_path, model_path = trained_model_path):
    model = YOLO(model_path)
    image = cv2.imread(image_path)
    results = model(image_path)[0] 
    masks = results.masks.data.cpu().numpy()
    masks = (masks > 0.5).astype(np.uint8)
    mask_list = [mask for mask in masks]
    result_image = overlay_masks(image, mask_list)
    timestr = time.strftime("%Y%m%d%H%M%S")
    output_path = output_image_path + "output_{}.jpg".format(timestr)
    print(output_path)
    if not cv2.imwrite(output_path, result_image):
        raise Exception("Could not write image")
    return output_path
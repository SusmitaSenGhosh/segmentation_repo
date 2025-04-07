import os
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Pretrained model

def process_image(img_path):
    if not os.path.exists(img_path):
        return "Image not found"

    results = model(img_path)
    output_img_path = img_path.replace(".jpg", "_output.jpg")
    results[0].save(filename=output_img_path)
    return output_img_path

## YOLO-based Cell Segmentation on LiveCell Dataset

This repository implements a YOLO-based cell segmentation model to identify and segment cells in images from the LiveCell dataset. The project utilizes YOLO (You Only Look Once) to classify and segment cell instances from microscopy images.

# Dataset
This project uses the LiveCell dataset. You can download the dataset from here (https://github.com/sartorius-research/LIVECell). The dataset consists of microscopy images containing cell structures and is designed for cell segmentation tasks.


The dataset contains 5239 total images divided into training, validation and testing purpose. Along with this corresponding .json files are also provided for the annotations in COCO object detection format. To get the seprate annotations for each images in YOLO format, use coco_to_yolo.py. The 

# Train
For training, use train.py which uses yolov8n-seg model pretrained with COCO dataset.

# Test
For testing, we can use the API http://localhost:8000/detect ( as configured for now ) to send an input image location and receive the output image location with segmentation mask as a resposne.

#Here is a sample code to do the same

import requests
url = "http://localhost:8000/test"
data = {"input" : "./app/test_data/input1.tif"}
response = requests.post(url, json=data)
if response.status_code == 200:
    print("Success:", response.json())  # If the API responds with JSON data
else:
    print("Error:", response.status_code)

# segmentation_repo
#docker run -v D:/work/git_forest/segmentation_repo/app/test_data/output:/app/test_data/output -p 8000:8000 segment-app1
#./app/test_data/input1.tif



## YOLO-based Cell Segmentation on LiveCell Dataset

This repository implements a YOLO-based cell segmentation model to identify and segment cells in images from the LiveCell dataset. The project utilizes YOLO (You Only Look Once) to classify and segment cell instances from microscopy images.

# Dataset
This project uses the LiveCell dataset. You can download the dataset from here (https://github.com/sartorius-research/LIVECell). The dataset consists of microscopy images containing cell structures and is designed for cell segmentation tasks.


The dataset contains total images divided into training, validation and testing purpose. Along with this corresponding .json files are also provided for the annotations in COCO object detection format. To get the seprate annotations for each images in YOLO format, use coco_to_yolo.py. The 

# Train
For training, use train.py which uses yolov8n-seg model pretrained with COCO dataset.

#

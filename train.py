
from ultralytics import YOLO
from matplotlib import pyplot as plt
from PIL import Image

if __name__ ==  '__main__':

    # model = YOLO('yolov8n-seg.pt')  # Transfer the weights from a pretrained model (recommended for training)
    model = YOLO("C:\\Users\\susmi\\ThreeV_cell_seg_SusmitaGhosh\\try_v2\\runs\\segment\\train3\\weights\\last.pt")  # Transfer the weights from a pretrained model (recommended for training)

    results = model.train(data="C:\\Users\\susmi\\ThreeV_cell_seg_SusmitaGhosh\\try_v2\\livecell\\output\\data.yaml",
                        #   project=project,
                        #   name=name,
                        epochs=200,
                        patience=0, #I am setting patience=0 to disable early stopping.
                        batch=4,
                        imgsz=520,
                        resume = True)
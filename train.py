# YOLO train

from ultralytics import YOLO

# Load a model
if __name__ ==  '__main__':
    model = YOLO("yolo11n-seg.pt")  # load a pretrained model (recommended for training)
    # Train the model
    results = model.train(data="F:\\ThreeV_cell_seg_SusmitaGhosh\\data.yaml", epochs=100, cache = "disk", imgsz=256,batch = 16, device=0, save_dir = "F:\\ThreeV_cell_seg_SusmitaGhosh\\model",workers = 6)
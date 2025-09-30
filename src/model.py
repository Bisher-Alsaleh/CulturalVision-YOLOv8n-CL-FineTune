from ultralytics import YOLO

def load_model(weights="yolov8n-cls.pt"):
    return YOLO(weights)
